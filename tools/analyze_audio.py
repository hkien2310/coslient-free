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


def detect_key(y: np.ndarray, sr: int) -> dict:
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


def analyze_file(target: Path) -> dict:
    listen_mp3 = ensure_listen_mp3(target)
    y, sr = librosa.load(str(listen_mp3), sr=22050, mono=True)
    duration = float(librosa.get_duration(y=y, sr=sr))

    # 1. Tempo & Beats
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    bpm = float(np.ndim(tempo) and tempo[0] or tempo)
    beat_times = librosa.frames_to_time(beats, sr=sr)
    ibi = np.diff(beat_times)
    beat_stability = float(1.0 - min(1.0, np.std(ibi) / (np.mean(ibi) + 1e-6))) if len(ibi) > 2 else 0.0

    # 2. Key & Harmony
    key_info = detect_key(y, sr)

    # 3. Loudness & Dynamic Range
    rms = librosa.feature.rms(y=y)[0]
    rms_db = librosa.amplitude_to_db(rms, ref=1.0)
    mean_rms_db = float(np.mean(rms_db))
    peak_db = float(librosa.amplitude_to_db(np.array([np.max(np.abs(y))]), ref=1.0)[0])
    crest_factor_db = round(peak_db - mean_rms_db, 1)

    # 4. Frequency Balance (Spectral Energy Distribution)
    S = np.abs(librosa.stft(y)) ** 2
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

    # 5. Structural Segmentation & Energy Arc
    n_segments = max(4, min(10, int(round(duration / 25))))
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    raw_frames = librosa.segment.agglomerative(mfcc, k=n_segments)
    raw_times = list(librosa.frames_to_time(raw_frames, sr=sr))
    bound_times = [0.0]
    for t in raw_times:
        if t - bound_times[-1] >= 4.0 and duration - t >= 4.0:
            bound_times.append(float(t))
    bound_times.append(duration)
    rms_times = librosa.frames_to_time(np.arange(len(rms)), sr=sr)

    max_rms = float(np.percentile(rms, 95)) + 1e-8
    min_rms = float(np.percentile(rms, 10))
    sections = []
    for i in range(len(bound_times) - 1):
        t0, t1 = bound_times[i], bound_times[i + 1]
        mask = (rms_times >= t0) & (rms_times < t1)
        sec_rms = float(np.mean(rms[mask])) if np.any(mask) else 0.0
        norm_e = max(0.0, min(1.0, (sec_rms - min_rms) / (max_rms - min_rms + 1e-8)))
        if norm_e >= 0.75:
            level = "High / Peak"
        elif norm_e >= 0.45:
            level = "Medium / Groove"
        else:
            level = "Low / Atmospheric"
        sections.append({
            "time_range": f"{fmt_time(t0)} - {fmt_time(t1)}",
            "duration_sec": round(t1 - t0, 1),
            "energy_score": round(norm_e, 2),
            "energy_level": level,
        })

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
        "dynamics_and_mix": {
            "mean_rms_db": round(mean_rms_db, 1),
            "peak_db": round(peak_db, 1),
            "crest_factor_db": crest_factor_db,
            "compression_character": (
                "Dense / Heavily Compressed (Club/Modern Pop)" if crest_factor_db < 11.0
                else "Balanced / Punchy Dynamic" if crest_factor_db < 15.0
                else "Wide Dynamic / Breathing & Cinematic"
            ),
            "frequency_energy_pct": freq_profile,
        },
        "energy_sections": sections,
    }


def download_yt_audio(yt_url: str, vid_id: str, out_dir: Path) -> tuple[Path, dict]:
    out_dir.mkdir(parents=True, exist_ok=True)
    meta_path = out_dir / f"{vid_id}_meta.json"
    existing = [f for f in out_dir.glob(f"{vid_id}*") if f.suffix.lower() in AUDIO_EXTS and not f.stem.endswith("_listen")]
    ytdlp_cmd = ["yt-dlp"] if shutil.which("yt-dlp") else ["uvx", "yt-dlp"]

    meta = {}
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    if not existing or not meta:
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
                "title": raw.get("title", ""),
                "channel": raw.get("uploader") or raw.get("channel", ""),
                "channel_follower_count": raw.get("channel_follower_count"),
                "view_count": raw.get("view_count"),
                "like_count": raw.get("like_count"),
                "comment_count": raw.get("comment_count"),
                "upload_date": raw.get("upload_date"),
                "description": (raw.get("description") or "")[:1500],
                "tags": (raw.get("tags") or [])[:25],
                "top_comments": top_comments,
            }
            meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    if existing:
        return existing[0], meta

    out_tmpl = str(out_dir / f"{vid_id}.%(ext)s")
    subprocess.run(
        ytdlp_cmd + ["--no-playlist", "-f", "bestaudio[ext=m4a]/bestaudio", "-o", out_tmpl, yt_url],
        stdout=subprocess.DEVNULL, check=True
    )
    downloaded = [f for f in out_dir.glob(f"{vid_id}.*") if f.suffix.lower() in (AUDIO_EXTS | VIDEO_EXTS)]
    if not downloaded:
        raise FileNotFoundError(f"Không tải được audio cho {yt_url}")
    return downloaded[0], meta


YT_REGEX = re.compile(r"https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([A-Za-z0-9_-]{11})")


def resolve_inputs(args: list[str]) -> list[tuple[Path, dict]]:
    out_dir = Path("projects/025/doi-thu")
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
                    results.append(download_yt_audio(m.group(0), vid_id, out_dir))
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
                        results.append(download_yt_audio(m.group(0), vid_id, out_dir))
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
                            results.append(download_yt_audio(m.group(0), vid_id, out_dir))
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
        print("Usage: python3 tools/analyze_audio.py <url1> [url2 ...] [--out-dir <folder>]", file=sys.stderr)
        sys.exit(1)
    targets = resolve_inputs(sys.argv[1:])
    all_reports = []
    for target_file, yt_meta in targets:
        rep = analyze_file(target_file)
        if yt_meta:
            rep["youtube_meta"] = yt_meta
        all_reports.append(rep)
    output = all_reports[0] if len(all_reports) == 1 else {"count": len(all_reports), "tracks": all_reports}
    print(json.dumps(output, indent=2, ensure_ascii=False))
