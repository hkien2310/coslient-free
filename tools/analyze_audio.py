#!/usr/bin/env python3
"""
Local Audio Technical Analyzer for Coslient Free Workflow.
Usage:
    python3 tools/analyze_audio.py <path_to_audio_or_video_or_dir>
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
import librosa
import numpy as np

AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".flac", ".ogg", ".aac"}
VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm"}

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Krumhansl-Schmuckler key profiles
MAJOR_PROFILE = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MINOR_PROFILE = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])


def fmt_time(sec: float) -> str:
    m, s = divmod(int(round(sec)), 60)
    return f"{m}:{s:02d}"


def ensure_listen_mp3(input_path: Path) -> Path:
    """If input is video or oversized audio (>25MB), create a lightweight 128k mp3 for AI listening."""
    if input_path.suffix.lower() == ".mp3" and input_path.stat().st_size <= 25 * 1024 * 1024:
        return input_path
    out_mp3 = input_path.with_name(f"{input_path.stem}_listen.mp3")
    if not out_mp3.exists():
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(input_path), "-vn", "-ac", "2", "-ar", "44100", "-b:a", "128k", str(out_mp3)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
    return out_mp3


def detect_key(y: np.ndarray, sr: int, y_harm: np.ndarray | None = None) -> dict:
    if y_harm is None:
        y_harm = librosa.effects.harmonic(y)
    chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=librosa.note_to_hz("C2"))
    chroma_vals = np.mean(chroma, axis=1)

    maj_norm = (MAJOR_PROFILE - MAJOR_PROFILE.mean()) / MAJOR_PROFILE.std()
    min_norm = (MINOR_PROFILE - MINOR_PROFILE.mean()) / MINOR_PROFILE.std()
    c_norm = (chroma_vals - chroma_vals.mean()) / (chroma_vals.std() + 1e-8)

    candidates = []
    for i in range(12):
        maj_corr = float(np.dot(c_norm, np.roll(maj_norm, i)) / 12)
        min_corr = float(np.dot(c_norm, np.roll(min_norm, i)) / 12)
        maj_3_7 = chroma_vals[(i + 4) % 12] + 0.5 * chroma_vals[(i + 11) % 12]
        min_3_7 = chroma_vals[(i + 3) % 12] + 0.5 * chroma_vals[(i + 10) % 12]
        if min_3_7 > maj_3_7 * 1.1:
            min_corr += 0.08
        candidates.append((f"{NOTE_NAMES[i]} Major", maj_corr))
        candidates.append((f"{NOTE_NAMES[i]} Minor", min_corr))

    candidates.sort(key=lambda x: x[1], reverse=True)
    top_notes = [NOTE_NAMES[idx] for idx in np.argsort(chroma_vals)[::-1][:5]]
    return {
        "primary_key": candidates[0][0],
        "confidence": round(candidates[0][1], 3),
        "secondary_key": candidates[1][0],
        "secondary_confidence": round(candidates[1][1], 3),
        "dominant_notes": top_notes,
    }


def measure_ebur128(audio_path: Path) -> dict:
    """Measure Integrated LUFS, Loudness Range (LRA), and True Peak (dBTP) via ffmpeg ebur128."""
    proc = subprocess.run(
        ["ffmpeg", "-nostats", "-i", str(audio_path), "-filter_complex", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True, text=True, check=False
    )
    text = proc.stderr or ""
    i_lufs = re.findall(r"I:\s*(-?\d+(?:\.\d+)?)\s*LUFS", text)
    lra = re.findall(r"LRA:\s*(\d+(?:\.\d+)?)\s*LU", text)
    tp = re.findall(r"Peak:\s*(-?\d+(?:\.\d+)?)\s*dBFS", text)
    return {
        "integrated_lufs": float(i_lufs[-1]) if i_lufs else None,
        "loudness_range_lu": float(lra[-1]) if lra else None,
        "true_peak_dbtp": float(tp[-1]) if tp else None,
    }


def detect_sub_tracks(y: np.ndarray, sr: int, y_harm: np.ndarray, duration: float) -> list[dict]:
    """Detect if a long audio file contains multiple distinct songs separated by silence gaps (>= 1.5s)."""
    intervals = librosa.effects.split(y, top_db=38, frame_length=4096, hop_length=1024)
    if len(intervals) <= 1:
        return []
    merged = [[float(intervals[0][0]) / sr, float(intervals[0][1]) / sr]]
    for start_f, end_f in intervals[1:]:
        t0, t1 = float(start_f) / sr, float(end_f) / sr
        if t0 - merged[-1][1] < 1.5:
            merged[-1][1] = t1
        else:
            merged.append([t0, t1])

    # Keep only substantive tracks (>= 45s) or merge tiny intro/outro tails into neighbors
    tracks = []
    for t0, t1 in merged:
        if tracks and (t1 - t0 < 45.0 or t0 < 45.0):
            tracks[-1][1] = t1
        else:
            tracks.append([t0, t1])

    if len(tracks) <= 1:
        return []

    sub_reports = []
    for idx, (t0, t1) in enumerate(tracks, 1):
        s0, s1 = int(t0 * sr), int(t1 * sr)
        y_sub = y[s0:s1]
        yh_sub = y_harm[s0:s1]
        tempo, _ = librosa.beat.beat_track(y=y_sub, sr=sr)
        bpm = float(np.ndim(tempo) and tempo[0] or tempo)
        key_sub = detect_key(y_sub, sr, y_harm=yh_sub)
        sub_reports.append({
            "track_index": idx,
            "time_range": f"{fmt_time(t0)} - {fmt_time(t1)}",
            "start_sec": round(t0, 1),
            "end_sec": round(t1, 1),
            "duration_formatted": fmt_time(t1 - t0),
            "duration_sec": round(t1 - t0, 1),
            "bpm": round(bpm, 1),
            "half_time_bpm": round(bpm / 2, 1),
            "primary_key": key_sub["primary_key"],
            "secondary_key": key_sub["secondary_key"],
        })
    return sub_reports


def analyze_file(target: Path) -> dict:
    listen_mp3 = ensure_listen_mp3(target)
    y_stereo, sr = librosa.load(str(listen_mp3), sr=22050, mono=False)
    if y_stereo.ndim == 2 and y_stereo.shape[0] >= 2:
        left, right = y_stereo[0], y_stereo[1]
        mid_sig = 0.5 * (left + right)
        side_sig = 0.5 * (left - right)
        mid_rms = float(np.sqrt(np.mean(mid_sig ** 2))) + 1e-12
        side_rms = float(np.sqrt(np.mean(side_sig ** 2)))
        stereo_width_pct = round((side_rms / (mid_rms + side_rms)) * 100.0, 1)
        stereo_corr = round(float(np.corrcoef(left, right)[0, 1]), 3)
        y = mid_sig
    else:
        y = y_stereo if y_stereo.ndim == 1 else y_stereo[0]
        stereo_width_pct = 0.0
        stereo_corr = 1.0

    duration = float(librosa.get_duration(y=y, sr=sr))

    # 1. Tempo, Beats & Harmonic/Percussive Separation
    y_harm, y_perc = librosa.effects.hpss(y)
    harm_e = float(np.sum(y_harm ** 2))
    perc_e = float(np.sum(y_perc ** 2)) + 1e-12
    harm_pct = round((harm_e / (harm_e + perc_e)) * 100.0, 1)
    perc_pct = round(100.0 - harm_pct, 1)
    hpr_ratio = round(harm_e / perc_e, 2)

    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    bpm = float(np.ndim(tempo) and tempo[0] or tempo)
    beat_times = librosa.frames_to_time(beats, sr=sr)
    ibi = np.diff(beat_times)
    beat_stability = float(1.0 - min(1.0, np.std(ibi) / (np.mean(ibi) + 1e-6))) if len(ibi) > 2 else 0.0

    # 2. Key & Harmony (Overall + Sub-tracks if multi-song video)
    key_info = detect_key(y, sr, y_harm=y_harm)
    sub_tracks = detect_sub_tracks(y, sr, y_harm, duration)

    # 3. Loudness, EBU R128 LUFS, Stereo & Dynamic Range
    rms = librosa.feature.rms(y=y)[0]
    rms_db = librosa.amplitude_to_db(rms, ref=1.0)
    mean_rms_db = float(np.mean(rms_db))
    peak_db = float(librosa.amplitude_to_db(np.array([np.max(np.abs(y))]), ref=1.0)[0])
    crest_factor_db = round(peak_db - mean_rms_db, 1)
    ebur128 = measure_ebur128(target)

    # 4. Frequency Balance & Spectral Timbre (Centroid & Rolloff)
    S_mag = np.abs(librosa.stft(y))
    S = S_mag ** 2
    freqs = librosa.fft_frequencies(sr=sr)
    total_energy = np.sum(S) + 1e-12
    bands = {
        "sub_bass_20_60Hz_pct": (20, 60),
        "bass_60_250Hz_pct": (60, 250),
        "low_mid_250_500Hz_pct": (250, 500),
        "mid_500_2000Hz_pct": (500, 2000),
        "high_mid_2k_6kHz_pct": (2000, 6000),
        "high_6k_plus_pct": (6000, sr // 2),
    }
    freq_profile = {
        name: round(float(np.sum(S[(freqs >= lo) & (freqs < hi), :]) / total_energy * 100), 1)
        for name, (lo, hi) in bands.items()
    }
    centroid_hz = int(round(float(np.mean(librosa.feature.spectral_centroid(S=S_mag, sr=sr)))))
    rolloff_85_hz = int(round(float(np.mean(librosa.feature.spectral_rolloff(S=S_mag, sr=sr, roll_percent=0.85)))))

    return {
        "source_file": str(target),
        "listen_file": str(listen_mp3),
        "duration_sec": round(duration, 1),
        "duration_formatted": fmt_time(duration),
        "tempo": {
            "bpm": round(bpm, 1),
            "bpm_rounded": int(round(bpm)),
            "half_time_bpm": round(bpm / 2, 1),
            "double_time_bpm": round(bpm * 2, 1),
            "beat_stability": round(beat_stability, 2),
        },
        "harmony": key_info,
        "sub_tracks": sub_tracks,
        "timbre_and_texture": {
            "harmonic_energy_pct": harm_pct,
            "percussive_energy_pct": perc_pct,
            "harmonic_to_percussive_ratio": hpr_ratio,
            "spectral_centroid_mean_hz": centroid_hz,
            "spectral_rolloff_85_hz": rolloff_85_hz,
        },
        "dynamics_and_mix": {
            "integrated_lufs": ebur128["integrated_lufs"],
            "loudness_range_lu": ebur128["loudness_range_lu"],
            "true_peak_dbtp": ebur128["true_peak_dbtp"],
            "mean_rms_db": round(mean_rms_db, 1),
            "peak_db": round(peak_db, 1),
            "crest_factor_db": crest_factor_db,
            "stereo_width_pct": stereo_width_pct,
            "stereo_correlation": stereo_corr,
            "compression_character": (
                "Dense / Heavily Compressed (Club/Modern Pop)" if crest_factor_db < 11.0
                else "Balanced / Punchy Dynamic" if crest_factor_db < 15.0
                else "Wide Dynamic / Breathing & Cinematic"
            ),
            "frequency_energy_pct": freq_profile,
        },
    }


def slugify(text: str, max_len: int = 60) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE)
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    return s[:max_len].strip("-") or "untitled"


def write_seo_md(folder: Path, meta: dict) -> Path:
    seo_path = folder / "seo.md"
    lines = [
        f"# {meta.get('title', 'Untitled')}",
        "",
        f"- **URL:** {meta.get('url', '')}",
        f"- **Video ID:** `{meta.get('video_id', '')}`",
        f"- **Kênh:** {meta.get('channel', '')} ({meta.get('channel_follower_count') or 'N/A'} subscribers)",
        f"- **Views:** {meta.get('view_count') or 0:,}",
        f"- **Likes:** {meta.get('like_count') or 0:,}",
        f"- **Comments:** {meta.get('comment_count') or 0:,}",
        f"- **Ngày đăng:** {meta.get('upload_date', '')}",
        f"- **Tags:** {', '.join(meta.get('tags') or [])}",
        "",
        "## Mô tả (Description)",
        "```text",
        (meta.get("description") or "").strip(),
        "```",
        "",
        "## Top Comments",
    ]
    for c in meta.get("top_comments") or []:
        lines.append(f"- **{c.get('author', '')}** ({c.get('likes', 0)} likes): {c.get('text', '')}")
    seo_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return seo_path


def write_technical_md(raw_dir: Path, rep: dict) -> Path:
    tech_md = raw_dir / "audio_technical.md"
    t = rep.get("tempo", {})
    h = rep.get("harmony", {})
    tb = rep.get("timbre_and_texture", {})
    d = rep.get("dynamics_and_mix", {})
    f = d.get("frequency_energy_pct", {})
    sub_tracks = rep.get("sub_tracks") or []

    lines = [
        "# Phân Tích Kỹ Thuật Âm Thanh Bằng Code (DSP Raw Data)",
        "",
        "## 1. Tổng Quan Nhịp Độ, Hòa Âm & Âm Sắc",
        f"- **Thời lượng:** `{rep.get('duration_formatted')}` (`{rep.get('duration_sec')}s`)",
        f"- **Tempo (BPM):** `{t.get('bpm')} BPM` (Half-time: `{t.get('half_time_bpm')} BPM`, Double-time: `{t.get('double_time_bpm')} BPM`)",
        f"- **Beat Stability:** `{t.get('beat_stability')}`",
        f"- **Tone chính (Primary Key):** `{h.get('primary_key')}` (Confidence: `{h.get('confidence')}`)",
        f"- **Tone phụ (Secondary Key):** `{h.get('secondary_key')}` (Confidence: `{h.get('secondary_confidence')}`)",
        f"- **Các nốt chủ đạo (Dominant Notes):** `{', '.join(h.get('dominant_notes') or [])}`",
        f"- **Tỷ lệ Giai điệu / Nhịp gõ (Harmonic / Percussive):** `{tb.get('harmonic_energy_pct')}%` Harmonic vs `{tb.get('percussive_energy_pct')}%` Percussive (HPR: `{tb.get('harmonic_to_percussive_ratio')}`)",
        f"- **Trọng tâm tần số (Spectral Centroid):** `{tb.get('spectral_centroid_mean_hz')} Hz` | **Rolloff 85%:** `{tb.get('spectral_rolloff_85_hz')} Hz`",
        "",
        "## 2. Âm Lượng Mastering (EBU R128), Dải Động & Stereo",
        f"- **Chuẩn phát sóng (EBU R128):** Integrated `{d.get('integrated_lufs')} LUFS` | Loudness Range (LRA): `{d.get('loudness_range_lu')} LU` | True Peak: `{d.get('true_peak_dbtp')} dBTP`",
        f"- **Dynamics (RMS/Peak):** Mean RMS `{d.get('mean_rms_db')} dB` | Peak `{d.get('peak_db')} dB` | Crest Factor `{d.get('crest_factor_db')} dB` ({d.get('compression_character')})",
        f"- **Không gian Stereo:** Độ rộng Stereo `{d.get('stereo_width_pct')}%` | Tương quan 2 kênh (Correlation): `{d.get('stereo_correlation')}`",
        "",
        "## 3. Phân Bổ Năng Lượng 6 Dải Tần (Spectral Energy)",
        f"- **Sub-bass (20–60Hz):** `{f.get('sub_bass_20_60Hz_pct')}%`",
        f"- **Bass (60–250Hz):** `{f.get('bass_60_250Hz_pct')}%`",
        f"- **Low-mid (250–500Hz):** `{f.get('low_mid_250_500Hz_pct')}%`",
        f"- **Mid (500–2000Hz):** `{f.get('mid_500_2000Hz_pct')}%`",
        f"- **High-mid (2k–6kHz):** `{f.get('high_mid_2k_6kHz_pct')}%`",
        f"- **High (>6kHz):** `{f.get('high_6k_plus_pct')}%`",
    ]

    if sub_tracks:
        lines.extend([
            "",
            f"## 4. Phát Hiện Video Ghép Nhiều Bài ({len(sub_tracks)} Sub-Tracks tách qua khoảng lặng)",
            "| Track | Khoảng thời gian | Thời lượng | BPM (Half-time) | Tone chính | Tone phụ |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |",
        ])
        for st in sub_tracks:
            lines.append(
                f"| Track {st['track_index']} | `{st['time_range']}` | `{st['duration_formatted']}` | `{st['bpm']} ({st['half_time_bpm']})` | `{st['primary_key']}` | `{st['secondary_key']}` |"
            )

    tech_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return tech_md


def download_yt_audio(yt_url: str, vid_id: str, base_out_dir: Path) -> tuple[Path, dict]:
    base_out_dir.mkdir(parents=True, exist_ok=True)
    ytdlp_cmd = ["yt-dlp"] if shutil.which("yt-dlp") else ["uvx", "yt-dlp"]

    # Check if already downloaded in any channel/video/raw subfolder
    for existing_meta in base_out_dir.rglob("raw/seo_meta.json"):
        try:
            m = json.loads(existing_meta.read_text(encoding="utf-8"))
            if m.get("video_id") == vid_id:
                raw_dir = existing_meta.parent
                aud = [f for f in raw_dir.glob("audio.*") if f.suffix.lower() in AUDIO_EXTS and not f.stem.endswith("_listen")]
                if aud:
                    return aud[0], m
        except Exception:
            pass

    proc = subprocess.run(
        ytdlp_cmd + [
            "--dump-single-json",
            "--no-playlist",
            "--write-comments",
            "--extractor-args", "youtube:max_comments=15,15,0,0;comment_sort=top",
            yt_url,
        ],
        capture_output=True, text=True, check=False
    )
    meta = {"video_id": vid_id, "url": f"https://www.youtube.com/watch?v={vid_id}"}
    if proc.returncode == 0 and proc.stdout.strip():
        raw = json.loads(proc.stdout.splitlines()[-1])
        raw_comments = raw.get("comments") or []
        top_comments = [
            {
                "author": c.get("author", ""),
                "likes": c.get("like_count", 0),
                "text": (c.get("text") or "").strip(),
            }
            for c in sorted(raw_comments, key=lambda x: x.get("like_count") or 0, reverse=True)[:12]
            if (c.get("text") or "").strip()
        ]
        meta = {
            "video_id": vid_id,
            "url": f"https://www.youtube.com/watch?v={vid_id}",
            "title": raw.get("title", vid_id),
            "channel": raw.get("uploader") or raw.get("channel") or "unknown-channel",
            "channel_follower_count": raw.get("channel_follower_count"),
            "view_count": raw.get("view_count"),
            "like_count": raw.get("like_count"),
            "comment_count": raw.get("comment_count"),
            "upload_date": raw.get("upload_date"),
            "description": (raw.get("description") or "")[:1500],
            "tags": (raw.get("tags") or [])[:25],
            "top_comments": top_comments,
        }

    channel_slug = slugify(meta.get("channel") or "unknown-channel", max_len=40)
    video_slug = slugify(meta.get("title") or vid_id, max_len=65)
    raw_dir = base_out_dir / channel_slug / video_slug / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    (raw_dir / "seo_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    write_seo_md(raw_dir, meta)

    existing = [f for f in raw_dir.glob("audio.*") if f.suffix.lower() in AUDIO_EXTS and not f.stem.endswith("_listen")]
    if existing:
        return existing[0], meta

    out_tmpl = str(raw_dir / "audio.%(ext)s")
    subprocess.run(
        ytdlp_cmd + ["--no-playlist", "-f", "bestaudio[ext=m4a]/bestaudio", "-o", out_tmpl, yt_url],
        stdout=subprocess.DEVNULL, check=True
    )
    downloaded = [f for f in raw_dir.glob("audio.*") if f.suffix.lower() in (AUDIO_EXTS | VIDEO_EXTS)]
    if not downloaded:
        raise FileNotFoundError(f"Không tải được audio cho {yt_url}")
    return downloaded[0], meta


YT_REGEX = re.compile(r"https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([A-Za-z0-9_-]{11})")


def resolve_inputs(args: list[str]) -> list[tuple[Path, dict]]:
    out_dir = Path("ref/doi-thu")
    raw_items = []
    i = 0
    while i < len(args):
        if args[i] in ("-o", "--out-dir") and i + 1 < len(args):
            out_dir = Path(args[i + 1])
            i += 2
        else:
            raw_items.append(args[i])
            i += 1

    results: list[tuple[Path, dict]] = []
    seen_ids = set()

    for item in raw_items:
        # 1. Direct YouTube URL(s) in argument string
        matches = list(YT_REGEX.finditer(item))
        if matches:
            for m in matches:
                vid_id = m.group(1)
                if vid_id not in seen_ids:
                    seen_ids.add(vid_id)
                    try:
                        results.append(download_yt_audio(m.group(0), vid_id, out_dir))
                    except Exception as e:
                        print(f"[WARN] Lỗi tải {m.group(0)}: {e}", file=sys.stderr)
            continue

        p = Path(item)
        if p.is_file():
            if p.suffix.lower() in (".md", ".txt"):
                out_dir = p.parent
                text = p.read_text(encoding="utf-8", errors="ignore")
                for m in YT_REGEX.finditer(text):
                    vid_id = m.group(1)
                    if vid_id not in seen_ids:
                        seen_ids.add(vid_id)
                        try:
                            results.append(download_yt_audio(m.group(0), vid_id, out_dir))
                        except Exception as e:
                            print(f"[WARN] Lỗi tải {m.group(0)}: {e}", file=sys.stderr)
            elif p.suffix.lower() in (AUDIO_EXTS | VIDEO_EXTS):
                results.append((p, {}))
        elif p.is_dir():
            out_dir = p
            # Check text files for YouTube URLs first
            for f in sorted(p.iterdir()):
                if f.is_file() and f.suffix.lower() in (".md", ".txt") and f.name != "phan-tich.md":
                    text = f.read_text(encoding="utf-8", errors="ignore")
                    for m in YT_REGEX.finditer(text):
                        vid_id = m.group(1)
                        if vid_id not in seen_ids:
                            seen_ids.add(vid_id)
                            try:
                                results.append(download_yt_audio(m.group(0), vid_id, out_dir))
                            except Exception as e:
                                print(f"[WARN] Lỗi tải {m.group(0)}: {e}", file=sys.stderr)
            # Also include any standalone local audio/video files not already added
            added_paths = {r[0].resolve() for r in results}
            for f in sorted(p.iterdir()):
                if (
                    f.is_file()
                    and f.suffix.lower() in (AUDIO_EXTS | VIDEO_EXTS)
                    and not f.stem.endswith("_listen")
                    and f.resolve() not in added_paths
                ):
                    meta_f = p / f"{f.stem}_meta.json"
                    meta = json.loads(meta_f.read_text(encoding="utf-8")) if meta_f.exists() else {}
                    results.append((f, meta))

    if not results:
        raise FileNotFoundError("Không tìm thấy link YouTube hoặc file audio hợp lệ.")
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/analyze_audio.py <url1> [url2 ...] [--out-dir <folder>] [--force]", file=sys.stderr)
        sys.exit(1)
    force = "--force" in sys.argv
    clean_args = [a for a in sys.argv[1:] if a != "--force"]
    targets = resolve_inputs(clean_args)
    all_reports = []
    for target_file, yt_meta in targets:
        try:
            raw_dir = target_file.parent if target_file.parent.name == "raw" else target_file.parent / "raw"
            raw_dir.mkdir(parents=True, exist_ok=True)
            cached_tech = raw_dir / "audio_technical.json"
            if cached_tech.exists() and not force:
                rep = json.loads(cached_tech.read_text(encoding="utf-8"))
                if not (raw_dir / "audio_technical.md").exists():
                    write_technical_md(raw_dir, rep)
                all_reports.append(rep)
                continue
            rep = analyze_file(target_file)
            rep["video_folder"] = str(raw_dir.parent)
            rep["raw_folder"] = str(raw_dir)
            write_technical_md(raw_dir, rep)
            if yt_meta:
                rep["youtube_meta"] = yt_meta
            cached_tech.write_text(
                json.dumps(rep, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            all_reports.append(rep)
        except Exception as e:
            print(f"[WARN] Lỗi phân tích {target_file}: {e}", file=sys.stderr)
    output = all_reports[0] if len(all_reports) == 1 else {"count": len(all_reports), "tracks": all_reports}
    print(json.dumps(output, indent=2, ensure_ascii=False))
