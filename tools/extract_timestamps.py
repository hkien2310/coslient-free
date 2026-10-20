#!/usr/bin/env python3
"""
General Audio Timestamp Extractor for Song Lyrics & Music Structure.
Works for ANY project, ANY language, ANY audio file (.wav, .mp3, .m4a, .flac).

Uses Faster-Whisper with Word-level Timestamps + Lyrics Alignment:
- Gộp từ chuẩn xác theo từng câu hát trong 3-lyrics.txt (không bị chém vụn chữ).
- Tự động tách câu dài (>6.5s) tại đúng nhịp ngắt tự nhiên.
- Liền mạch 100% (Zero-Gap): các khoảng nghỉ/solo được điền [INSTRUMENTAL],
  không làm rơi rụng bất kỳ giây nào của bài hát.
- Xuất 3 file chuẩn:
  1. timestamps.json  (Machine-readable cho AI agents / Palmier Pro MCP automation)
  2. timestamps.txt   (Human-readable phân bổ bài hát, đã chia sẵn cảnh nhạc dạo & snap beat)
  3. lyrics.srt       (Phụ đề chuẩn Palmier Pro / Premiere / CapCut - giữ 100% mốc giọng hát gốc)

Usage:
    uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio_path>
    uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio_path> --beats beats.json
    uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio_path> --lyrics 3-lyrics.txt
    uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio_path> --lang vi --gap 2.0
"""

import sys
import re
import json
import difflib
import argparse
from pathlib import Path


def format_time_mmss(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"


def format_time_srt(seconds: float) -> str:
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"


def normalize(text: str) -> str:
    """Normalize text for phonetic/fuzzy comparison."""
    return re.sub(r'[^a-zA-Z0-9\u00C0-\u1EF9]', '', text.lower())


def pick_model_name(model: str, lang: str) -> str:
    """Pick the right model variant. English-only models (.en) are faster
    and more accurate for English. Multilingual models handle everything else."""
    if "." in model:
        return model
    if lang == "en":
        return f"{model}.en"
    return model


def find_lyrics_file(audio_path: Path, output_dir: Path = None, explicit_lyrics: str = None) -> Path:
    """Auto-detect lyrics file if not explicitly provided."""
    if explicit_lyrics:
        p = Path(explicit_lyrics).resolve()
        if p.exists():
            return p

    candidates = [
        audio_path.parent / "3-lyrics.txt",
        audio_path.parent / "lyrics.txt",
        audio_path.parent / "clean_lyrics.txt",
    ]
    if output_dir:
        candidates.extend([
            output_dir / "3-lyrics.txt",
            output_dir / "lyrics.txt",
        ])

    for c in candidates:
        if c.exists():
            return c
    return None


def split_instrumental_shots(
    section: str,
    text: str,
    start: float,
    end: float,
    downbeats: list[float],
    beats: list[float],
    max_shot_duration: float = 6.5,
) -> list[dict]:
    """Split long instrumental sections into ~5s shots aligned to Palmier downbeats (Beat 1)."""
    dur = end - start
    if dur <= max_shot_duration:
        return [{
            "type": "INSTRUMENTAL",
            "section": section,
            "start": round(start, 2),
            "end": round(end, 2),
            "duration": round(dur, 2),
            "time_range": f"{format_time_mmss(start)} - {format_time_mmss(end)}",
            "text": text,
        }]

    n_shots = max(2, round(dur / 5.2))
    cuts = [start]
    for k in range(1, n_shots):
        ideal_t = start + k * (dur / n_shots)
        prev_cut = cuts[-1]
        # Prefer Palmier downbeats (Beat 1) within ±1.8s that keep shot >= 2.8s
        candidates = [db for db in downbeats if prev_cut + 2.8 <= db <= end - 2.8 and abs(db - ideal_t) <= 1.8]
        if not candidates:
            candidates = [b for b in beats if prev_cut + 2.8 <= b <= end - 2.8 and abs(b - ideal_t) <= 1.2]
        cut_t = min(candidates, key=lambda x: abs(x - ideal_t)) if candidates else ideal_t
        cuts.append(round(cut_t, 2))
    cuts.append(round(end, 2))

    shots = []
    for idx in range(len(cuts) - 1):
        s, e = cuts[idx], cuts[idx + 1]
        shots.append({
            "type": "INSTRUMENTAL",
            "section": section,
            "start": round(s, 2),
            "end": round(e, 2),
            "duration": round(e - s, 2),
            "time_range": f"{format_time_mmss(s)} - {format_time_mmss(e)}",
            "text": f"{text} (Part {idx + 1}/{len(cuts) - 1})" if len(cuts) > 2 else text,
        })
    return shots


def apply_hybrid_beat_snap(
    sequence: list[dict],
    downbeats: list[float],
    beats: list[float],
    snap_tolerance: float = 0.25,
) -> int:
    """Snap shot cut boundaries to nearest Palmier downbeat/beat within snap_tolerance (Zero-Gap)."""
    if not downbeats and not beats:
        return 0
    snapped_count = 0
    for i in range(1, len(sequence)):
        prev_item = sequence[i - 1]
        curr_item = sequence[i]
        t = curr_item["start"]
        # Check downbeats first (Beat 1), then regular beats
        db_hits = [db for db in downbeats if abs(db - t) <= snap_tolerance]
        b_hits = [b for b in beats if abs(b - t) <= snap_tolerance]
        target = (
            min(db_hits, key=lambda x: abs(x - t))
            if db_hits
            else (min(b_hits, key=lambda x: abs(x - t)) if b_hits else None)
        )
        if target is not None:
            new_t = round(target, 2)
            if new_t - prev_item["start"] >= 2.0 and curr_item["end"] - new_t >= 2.0:
                if new_t != curr_item["start"]:
                    snapped_count += 1
                prev_item["end"] = new_t
                prev_item["duration"] = round(prev_item["end"] - prev_item["start"], 2)
                prev_item["time_range"] = f"{format_time_mmss(prev_item['start'])} - {format_time_mmss(prev_item['end'])}"
                curr_item["start"] = new_t
                curr_item["duration"] = round(curr_item["end"] - curr_item["start"], 2)
                curr_item["time_range"] = f"{format_time_mmss(curr_item['start'])} - {format_time_mmss(curr_item['end'])}"
                curr_item["beat_snapped"] = True
    return snapped_count


def extract_audio_timestamps(
    audio_path: str,
    output_dir: str = None,
    lyrics_path: str = None,
    model_size: str = "base",
    lang: str = "en",
    gap_threshold: float = 2.0,
    max_shot_duration: float = 6.5,
    beats_path: str = None,
    snap_tolerance: float = 0.25,
):
    from faster_whisper import WhisperModel

    audio_file = Path(audio_path).resolve()
    if not audio_file.exists():
        print(f"❌ Error: File not found: {audio_file}")
        sys.exit(1)

    target_dir = Path(output_dir).resolve() if output_dir else audio_file.parent
    target_dir.mkdir(parents=True, exist_ok=True)

    detected_lyrics = find_lyrics_file(audio_file, target_dir, lyrics_path)
    model_name = pick_model_name(model_size, lang)

    downbeats, beats, bpm = [], [], None
    if beats_path and Path(beats_path).exists():
        with open(beats_path, "r", encoding="utf-8") as bf:
            bdata = json.load(bf)
            downbeats = bdata.get("downbeats", [])
            beats = bdata.get("beats", [])
            bpm = bdata.get("bpm")

    print(f"🎵 Audio: {audio_file.name}")
    print(f"📂 Output: {target_dir}")
    print(f"📜 Lyrics: {detected_lyrics.name if detected_lyrics else 'Not provided (transcribe only)'}")
    print(f"🧠 Model: {model_name} | Language: {lang} | Gap threshold: {gap_threshold}s | Max shot: {max_shot_duration}s")
    if downbeats or beats:
        print(f"🥁 Palmier Beats loaded: BPM={bpm} | Downbeats={len(downbeats)} | Beats={len(beats)} | Snap={snap_tolerance}s")

    model = WhisperModel(model_name, device="cpu", compute_type="int8")

    print(f"🎙️ Transcribing with word-level timestamps...")
    transcribe_opts = dict(
        beam_size=5,
        word_timestamps=True,
    )
    if lang != "en":
        transcribe_opts["language"] = lang

    segments_raw, info = model.transcribe(str(audio_file), **transcribe_opts)
    segments = list(segments_raw)
    duration = info.duration

    print(f"⏱️ Duration: {format_time_mmss(duration)} ({duration:.2f}s)")
    print(f"📝 Raw vocal segments: {len(segments)}")

    matched_lines = []

    # --- Mode 1: Align with lyrics file (Ground Truth) ---
    if detected_lyrics:
        with open(detected_lyrics, "r", encoding="utf-8") as f:
            lyrics_lines = [line.strip() for line in f if line.strip()]

        print(f"🔗 Aligning {len(lyrics_lines)} lyrics lines with audio...")
        words = [w for s in segments for w in (s.words or []) if normalize(w.word)]
        l_chars, l_map = [], []
        for idx, line in enumerate(lyrics_lines):
            c = normalize(line)
            l_chars.append(c)
            l_map.extend([idx] * len(c))
        w_chars, w_map = [], []
        for idx, w in enumerate(words):
            c = normalize(w.word)
            w_chars.append(c)
            w_map.extend([idx] * len(c))

        matcher = difflib.SequenceMatcher(None, "".join(l_chars), "".join(w_chars), autojunk=False)
        word_votes = {}
        for i, j, n in matcher.get_matching_blocks():
            if n < 2:
                continue
            for k in range(n):
                li, wi = l_map[i + k], w_map[j + k]
                word_votes.setdefault(wi, {})[li] = word_votes.get(wi, {}).get(li, 0) + 1

        line_words = {i: [] for i in range(len(lyrics_lines))}
        last_li = 0
        for wi in sorted(word_votes):
            li = max(word_votes[wi], key=word_votes[wi].get)
            if li >= last_li:
                line_words[li].append(wi)
                last_li = li

        # Fill any internal unmatched lines using words between neighboring matched lines
        for idx in range(len(lyrics_lines)):
            if not line_words[idx]:
                prev_w = max((max(line_words[p]) for p in range(idx - 1, -1, -1) if line_words[p]), default=-1)
                next_w = min((min(line_words[n]) for n in range(idx + 1, len(lyrics_lines)) if line_words[n]), default=-1)
                if prev_w != -1 and next_w != -1 and next_w > prev_w + 1:
                    line_words[idx] = list(range(prev_w + 1, next_w))

        for l_idx, line in enumerate(lyrics_lines):
            ws = sorted(set(line_words[l_idx]))
            if not ws:
                matched_lines.append({"text": line, "start": None, "end": None, "duration": 0.0, "is_split": False})
                continue
            # Keep only the main contiguous word cluster (prevent spanning across >2.5s instrumental solos/echoes)
            clusters = [[ws[0]]]
            for w_i in ws[1:]:
                if words[w_i].start - words[clusters[-1][-1]].end > 2.5:
                    clusters.append([w_i])
                else:
                    clusters[-1].append(w_i)
            ws = max(clusters, key=len)
            start_t = words[ws[0]].start
            end_t = min(words[ws[-1]].end, words[ws[-1]].start + 1.5)
            matched_lines.append({
                "text": line,
                "start": round(start_t, 2),
                "end": round(end_t, 2),
                "duration": round(end_t - start_t, 2),
                "is_split": False,
            })

        # Interpolate any internal unmatched lines into the time window between matched neighbors
        i = 0
        while i < len(matched_lines):
            if matched_lines[i]["start"] is None:
                j = i
                while j < len(matched_lines) and matched_lines[j]["start"] is None:
                    j += 1
                if i > 0 and j < len(matched_lines) and matched_lines[i - 1]["end"] is not None:
                    t1 = matched_lines[j]["start"]
                    start_idx = i - 1 if (t1 - matched_lines[i - 1]["end"]) < 2.0 * (j - i) else i
                    t0 = matched_lines[start_idx]["start"] if start_idx == i - 1 else matched_lines[i - 1]["end"]
                    step = max(0.5, (t1 - t0) / (j - start_idx))
                    for k in range(start_idx, j):
                        st = round(t0 + (k - start_idx) * step, 2)
                        et = round(t0 + (k - start_idx + 1) * step, 2)
                        matched_lines[k].update(start=st, end=et, duration=round(et - st, 2))
                i = j
            else:
                i += 1
        matched_lines = [m for m in matched_lines if m["start"] is not None]
    else:
        # --- Mode 2: Pure Whisper Segments ---
        for s in segments:
            text = s.text.strip()
            if not text:
                continue
            start_t = s.words[0].start if s.words else s.start
            end_t = s.words[-1].end if s.words else s.end
            matched_lines.append({
                "text": text,
                "start": round(start_t, 2),
                "end": round(end_t, 2),
                "duration": round(end_t - start_t, 2),
                "is_split": False,
            })

    # --- Build Zero-Gap Continuous Timeline ---
    full_sequence = []
    current_time = 0.0

    # Intro (Instrumental)
    if matched_lines and matched_lines[0]["start"] > 1.5:
        intro_end = matched_lines[0]["start"]
        full_sequence.extend(
            split_instrumental_shots("Intro", "[Intro / Instrumental Opening]", 0.0, intro_end, downbeats, beats, max_shot_duration)
        )
        current_time = intro_end

    for line in matched_lines:
        gap = line["start"] - current_time

        # Real instrumental gap
        if gap >= gap_threshold:
            full_sequence.extend(
                split_instrumental_shots(
                    "Solo / Interlude",
                    "[Instrumental Solo / Musical Break]",
                    round(current_time, 2),
                    line["start"],
                    downbeats,
                    beats,
                    max_shot_duration,
                )
            )
            current_time = line["start"]
        elif gap > 0:
            # Micro breath gap (< threshold): smoothly absorb into previous section to maintain 100% zero-gap
            if full_sequence:
                full_sequence[-1]["end"] = line["start"]
                full_sequence[-1]["duration"] = round(full_sequence[-1]["end"] - full_sequence[-1]["start"], 2)
                full_sequence[-1]["time_range"] = (
                    f"{format_time_mmss(full_sequence[-1]['start'])} - {format_time_mmss(full_sequence[-1]['end'])}"
                )
            current_time = line["start"]

        full_sequence.append({
            "type": "VOCAL",
            "section": "Lyrics",
            "start": line["start"],
            "end": line["end"],
            "vocal_start": line["start"],
            "vocal_end": line["end"],
            "duration": line["duration"],
            "time_range": f"{format_time_mmss(line['start'])} - {format_time_mmss(line['end'])}",
            "text": line["text"],
        })
        current_time = line["end"]

    # Outro (Instrumental)
    if current_time < duration - 1.0:
        full_sequence.extend(
            split_instrumental_shots(
                "Outro",
                "[Outro / Instrumental Ending]",
                round(current_time, 2),
                round(duration, 2),
                downbeats,
                beats,
                max_shot_duration,
            )
        )

    # Preserve contiguous vocal SRT windows BEFORE beat-snapping video cuts
    for item in full_sequence:
        if item["type"] == "VOCAL":
            item["srt_start"] = item["start"]
            item["srt_end"] = item["end"]

    # Apply Hybrid Vocal + Palmier Beat-Snap to video cut boundaries
    snapped_cuts = apply_hybrid_beat_snap(full_sequence, downbeats, beats, snap_tolerance)
    for idx, item in enumerate(full_sequence, 1):
        item["index"] = idx

    # --- Write Outputs ---
    json_path = target_dir / "timestamps.json"
    json_data = {
        "audio_file": audio_file.name,
        "language": lang,
        "model": model_name,
        "lyrics_file": detected_lyrics.name if detected_lyrics else None,
        "duration_seconds": round(duration, 2),
        "duration_formatted": format_time_mmss(duration),
        "bpm": bpm,
        "beat_snapped_cuts": snapped_cuts,
        "gap_threshold": gap_threshold,
        "max_shot_duration": max_shot_duration,
        "total_sections": len(full_sequence),
        "vocal_lines_count": len([s for s in full_sequence if s["type"] == "VOCAL"]),
        "sequence": full_sequence,
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    txt_path = target_dir / "timestamps.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"# TIMESTAMPS: {audio_file.name}\n")
        f.write(f"# Duration: {format_time_mmss(duration)} ({duration:.2f}s) | Shots: {len(full_sequence)} | Vocal lines: {json_data['vocal_lines_count']} | BPM: {bpm or 'N/A'}\n")
        f.write(f"# Model: {model_name} | Language: {lang} | Lyrics: {detected_lyrics.name if detected_lyrics else 'None'} | Zero-Gap Hybrid Beat-Snap: ON\n\n")
        for item in full_sequence:
            tag = f"[{item['type']}]".ljust(15)
            f.write(f"{item['time_range']}  ({item['duration']:5.2f}s)  {tag}  {item['text']}\n")

    srt_path = target_dir / "lyrics.srt"
    vocal_items = [s for s in full_sequence if s["type"] == "VOCAL"]
    with open(srt_path, "w", encoding="utf-8") as f:
        for idx, item in enumerate(vocal_items, 1):
            f.write(f"{idx}\n")
            f.write(f"{format_time_srt(item['srt_start'])} --> {format_time_srt(item['srt_end'])}\n")
            f.write(f"{item['text']}\n\n")

    print(f"\n✅ Done! 3 files generated at {target_dir} (Shots: {len(full_sequence)}, Beat-snapped cuts: {snapped_cuts}):")
    print(f"   timestamps.json  (Agent / Palmier Pro MCP automation)")
    print(f"   timestamps.txt   (Human review - Zero Gap & Downbeat Split)")
    print(f"   lyrics.srt       (Subtitle editor - Exact Vocal Timing)")

    return json_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract vocal & instrumental timestamps aligned with song lyrics + Palmier Pro Beats (Zero-Gap)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  # Auto-detects 3-lyrics.txt in same folder:
  uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py song.wav

  # Hybrid Vocal + Palmier Pro Beat-Snap:
  uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py song.wav --beats beats.json
""",
    )
    parser.add_argument("audio", help="Audio file path (.wav, .mp3, .m4a, .flac)")
    parser.add_argument("--lyrics", help="Path to lyrics text file (default: auto-detect 3-lyrics.txt)", default=None)
    parser.add_argument("--output-dir", help="Output directory (default: same as audio file)", default=None)
    parser.add_argument("--model", help="Whisper model size: tiny, base, small, medium (default: base)", default="base")
    parser.add_argument("--lang", help="Language code: en, vi, fr, ja... (default: en)", default="en")
    parser.add_argument("--gap", help="Min silence (seconds) to mark as instrumental solo (default: 2.0)", type=float, default=2.0)
    parser.add_argument("--max-shot", help="Max duration (seconds) before splitting long line (default: 6.5)", type=float, default=6.5)
    parser.add_argument("--beats", help="Path to JSON file containing Palmier Pro detect_beats output (beats & downbeats)", default=None)
    parser.add_argument("--snap-tolerance", help="Max seconds to snap vocal cut to nearest beat (default: 0.25)", type=float, default=0.25)

    args = parser.parse_args()
    extract_audio_timestamps(
        audio_path=args.audio,
        output_dir=args.output_dir,
        lyrics_path=args.lyrics,
        model_size=args.model,
        lang=args.lang,
        gap_threshold=args.gap,
        max_shot_duration=args.max_shot,
        beats_path=args.beats,
        snap_tolerance=args.snap_tolerance,
    )

