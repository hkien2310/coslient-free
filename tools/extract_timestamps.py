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
  1. timestamps.json  (Machine-readable cho AI agents / automation)
  2. timestamps.txt   (Human-readable phân bổ bài hát)
  3. lyrics.srt       (Phụ đề chuẩn Premiere / CapCut / DaVinci)

Usage:
    uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio_path>
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


def extract_audio_timestamps(
    audio_path: str,
    output_dir: str = None,
    lyrics_path: str = None,
    model_size: str = "base",
    lang: str = "en",
    gap_threshold: float = 2.0,
    max_shot_duration: float = 6.5,
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

    print(f"🎵 Audio: {audio_file.name}")
    print(f"📂 Output: {target_dir}")
    print(f"📜 Lyrics: {detected_lyrics.name if detected_lyrics else 'Not provided (transcribe only)'}")
    print(f"🧠 Model: {model_name} | Language: {lang} | Gap threshold: {gap_threshold}s | Max shot: {max_shot_duration}s")

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
        seg_idx = 0
        for l_idx, line in enumerate(lyrics_lines):
            line_norm = normalize(line)
            best_seg_count = 1
            best_match_ratio = 0.0

            # Scan ahead 1 to 3 segments to group sub-phrases
            for count in [1, 2, 3]:
                if seg_idx + count > len(segments):
                    continue
                cand_text = normalize(" ".join(s.text for s in segments[seg_idx : seg_idx + count]))
                ratio = difflib.SequenceMatcher(None, line_norm, cand_text).ratio()
                if ratio > best_match_ratio:
                    best_match_ratio = ratio
                    best_seg_count = count

            matched_segs = segments[seg_idx : seg_idx + best_seg_count]
            if not matched_segs:
                continue

            start_t = matched_segs[0].words[0].start if matched_segs[0].words else matched_segs[0].start
            end_t = matched_segs[-1].words[-1].end if matched_segs[-1].words else matched_segs[-1].end
            dur = end_t - start_t

            # Smart Intra-line Split: If longer than max_shot_duration and has multiple sub-segments
            if dur > max_shot_duration and len(matched_segs) > 1:
                for sub_s in matched_segs:
                    sub_st = sub_s.words[0].start if sub_s.words else sub_s.start
                    sub_et = sub_s.words[-1].end if sub_s.words else sub_s.end
                    matched_lines.append({
                        "text": sub_s.text.strip(),
                        "start": round(sub_st, 2),
                        "end": round(sub_et, 2),
                        "duration": round(sub_et - sub_st, 2),
                        "is_split": True,
                    })
            else:
                matched_lines.append({
                    "text": line,
                    "start": round(start_t, 2),
                    "end": round(end_t, 2),
                    "duration": round(dur, 2),
                    "is_split": False,
                })

            seg_idx += best_seg_count
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
    seq_index = 1
    current_time = 0.0

    # Intro (Instrumental)
    if matched_lines and matched_lines[0]["start"] > 1.5:
        intro_end = matched_lines[0]["start"]
        full_sequence.append({
            "index": seq_index,
            "type": "INSTRUMENTAL",
            "section": "Intro",
            "start": 0.0,
            "end": intro_end,
            "duration": round(intro_end, 2),
            "time_range": f"00:00 - {format_time_mmss(intro_end)}",
            "text": "[Intro / Instrumental Opening]",
        })
        seq_index += 1
        current_time = intro_end

    for line in matched_lines:
        gap = line["start"] - current_time

        # Real instrumental gap
        if gap >= gap_threshold:
            full_sequence.append({
                "index": seq_index,
                "type": "INSTRUMENTAL",
                "section": "Solo / Interlude",
                "start": round(current_time, 2),
                "end": line["start"],
                "duration": round(gap, 2),
                "time_range": f"{format_time_mmss(current_time)} - {format_time_mmss(line['start'])}",
                "text": "[Instrumental Solo / Musical Break]",
            })
            seq_index += 1
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
            "index": seq_index,
            "type": "VOCAL",
            "section": "Lyrics",
            "start": line["start"],
            "end": line["end"],
            "duration": line["duration"],
            "time_range": f"{format_time_mmss(line['start'])} - {format_time_mmss(line['end'])}",
            "text": line["text"],
        })
        seq_index += 1
        current_time = line["end"]

    # Outro (Instrumental)
    if current_time < duration - 1.0:
        outro_dur = duration - current_time
        full_sequence.append({
            "index": seq_index,
            "type": "INSTRUMENTAL",
            "section": "Outro",
            "start": round(current_time, 2),
            "end": round(duration, 2),
            "duration": round(outro_dur, 2),
            "time_range": f"{format_time_mmss(current_time)} - {format_time_mmss(duration)}",
            "text": "[Outro / Instrumental Ending]",
        })

    # --- Write Outputs ---
    json_path = target_dir / "timestamps.json"
    json_data = {
        "audio_file": audio_file.name,
        "language": lang,
        "model": model_name,
        "lyrics_file": detected_lyrics.name if detected_lyrics else None,
        "duration_seconds": round(duration, 2),
        "duration_formatted": format_time_mmss(duration),
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
        f.write(f"# Duration: {format_time_mmss(duration)} ({duration:.2f}s) | Sections: {len(full_sequence)} | Vocal lines: {json_data['vocal_lines_count']}\n")
        f.write(f"# Model: {model_name} | Language: {lang} | Lyrics: {detected_lyrics.name if detected_lyrics else 'None'} | Zero-Gap Mode: ON\n\n")
        for item in full_sequence:
            tag = f"[{item['type']}]".ljust(15)
            f.write(f"{item['time_range']}  ({item['duration']:5.2f}s)  {tag}  {item['text']}\n")

    srt_path = target_dir / "lyrics.srt"
    vocal_items = [s for s in full_sequence if s["type"] == "VOCAL"]
    with open(srt_path, "w", encoding="utf-8") as f:
        for idx, item in enumerate(vocal_items, 1):
            f.write(f"{idx}\n")
            f.write(f"{format_time_srt(item['start'])} --> {format_time_srt(item['end'])}\n")
            f.write(f"{item['text']}\n\n")

    print(f"\n✅ Done! 3 files generated at {target_dir}:")
    print(f"   timestamps.json  (Agent / Code automation)")
    print(f"   timestamps.txt   (Human review - Zero Gap)")
    print(f"   lyrics.srt       (Subtitle editor)")

    return json_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract vocal & instrumental timestamps aligned with song lyrics (Zero-Gap Whisper)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  # Auto-detects 3-lyrics.txt in same folder:
  uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py song.wav

  # Specify lyrics explicitly:
  uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py song.wav --lyrics 3-lyrics.txt

  # Vietnamese song with custom max shot duration:
  uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py song.wav --lang vi --max-shot 6.0
""",
    )
    parser.add_argument("audio", help="Audio file path (.wav, .mp3, .m4a, .flac)")
    parser.add_argument("--lyrics", help="Path to lyrics text file (default: auto-detect 3-lyrics.txt)", default=None)
    parser.add_argument("--output-dir", help="Output directory (default: same as audio file)", default=None)
    parser.add_argument("--model", help="Whisper model size: tiny, base, small, medium (default: base)", default="base")
    parser.add_argument("--lang", help="Language code: en, vi, fr, ja... (default: en)", default="en")
    parser.add_argument("--gap", help="Min silence (seconds) to mark as instrumental solo (default: 2.0)", type=float, default=2.0)
    parser.add_argument("--max-shot", help="Max duration (seconds) before splitting long line (default: 6.5)", type=float, default=6.5)

    args = parser.parse_args()
    extract_audio_timestamps(
        audio_path=args.audio,
        output_dir=args.output_dir,
        lyrics_path=args.lyrics,
        model_size=args.model,
        lang=args.lang,
        gap_threshold=args.gap,
        max_shot_duration=args.max_shot,
    )
