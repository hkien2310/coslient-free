---
name: palmier-music-video
description: >-
  Edit music videos in Palmier Pro via MCP. Downbeat-locked pacing [3.0s-6.0s],
  phrase-boundary cuts, 5-bucket asset triage, ammo banking, 4D contrast,
  zero duplicates. Trigger: "edit video X", "dựng video X", "music video".
---

# Palmier Music Video Editor

## Tools

| Tool | When |
|---|---|
| `get_timeline` | Read timeline state (fps, tracks, clips, gaps) |
| `get_media` | List all source assets (video clips, audio tracks) |
| `search_media` | Find clips by visual description (`scope: "visual"`) |
| `inspect_media` | View clip contact sheet, get word timestamps |
| `inspect_timeline` | Visual QA — see rendered frames on timeline |
| `detect_beats` | Get BPM, beats[], downbeats[] from music |
| `get_transcript` | Get word-level timestamps from vocal track |
| `add_clips` | Place clips on timeline (use `endFrame`, not `source`) |
| `set_clip_properties` | Volume, fade, trim, speed |
| `swap_clip_media` | Replace a placed clip with a different source |
| `manage_tracks` | Rename, reorder, remove tracks |
| `manage_markers` | Create section markers on timeline |
| `split_clips` | Split a clip at a frame |
| `move_clips` | Shift clips on timeline |
| `set_keyframes` | Animate blur, scale, position |
| `add_texts` | Title cards, stencil mattes |
| `inspect_color` | Scopes, exposure, vectorscope |
| `apply_color` | Fix exposure/white balance |
| `capture_frame` | Screenshot a timeline frame |

---

## Hard Rules

1. **Duration:** Every shot in [3.0s, 6.0s]. Sweet spot: 3.8s-5.0s. No exceptions except Outro up to 6.5s.
2. **Cuts on phrase boundaries:** Use `get_transcript`/`inspect_media({ wordTimestamps: true })` to find silence gaps >= 0.3s between phrases. Cut there, snapped to nearest downbeat.
3. **No mid-phrase cuts.** If a downbeat falls mid-word, skip to the next downbeat after the phrase ends.
4. **4D contrast at every cut:** Scale(t) != Scale(t-1), Angle(t) != Angle(t-1), alternate motion vectors, alternate warm/cool lighting.
5. **Zero duplicates.** Track `used_set` globally. Each `mediaRef` appears exactly once.
6. **No sequential placement.** Never dump STT_001->002->003. Use `search_media` with cinematic queries for every clip.
7. **Search query format:** `[narrative subtext] + [camera scale/lens] + [physical action] + [lighting/atmosphere]`. Never bare keywords.
8. **Ammo banking:** Chorus 1 gets max 2-3 Tier S clips. Bridge = silence (Atmo only). Final Climax = 8-10 Tier S, fast cuts 3.0-3.5s.
9. **Intro Foley:** Keep clip 1 audio at 0dB with fadeOut 60f. Mute all clips from Verse 1 onward at -60dB.
10. **Outro:** Last shot >= 4.5s. Music fadeOut 3s, raise ambient audio, L-cut bleed 1.5-2.0s into black.
11. **Use `endFrame` not `source`** in `add_clips` to prevent 1-frame black gaps. Clip i endFrame = Clip i+1 startFrame.
12. **All timing from tools.** `detect_beats`, `get_transcript`, `inspect_media` are the timing sources. Lyrics/music docs = narrative reference only.
13. **No scripts.** No Python, Node, Bash. Every action = MCP tool call.
14. **Batch limit:** Max 20 entries per `add_clips` call.
15. **First 30s = hero shots only.** Clips in frames 0–900 must be Tier S or exceptional Tier A. Valid hook types: (a) macro mystery — extreme close detail withholding context, (b) surreal wide — vast impossible landscape, (c) kinetic shock — explosive action mid-motion, (d) expressive eyeline — face with charged emotion. Generic, calm, or flat shots are banned from the first 30s.
16. **Trim 1s from source edges.** Never use source second 0 or the final source second. All clips: startSeconds >= 1.0, endSeconds <= (sourceDuration - 1.0). For 8s clips: usable window = 1.0s→7.0s = 6.0s max, compatible with [3.0s, 6.0s] rule.

---

## Asset Triage

Before placing any clip, classify all sources into 5 buckets and 3 tiers:

| Bucket | % of pool | What |
|---|---|---|
| `01_WIDE` | 15-20% | Establishing shots, landscapes, world-building |
| `02_EMOTION` | 25-30% | Close-ups, eyes, facial expressions |
| `03_TACTILE` | 15-20% | Object details, textures, hands, props |
| `04_KINETIC` | 20-25% | Running, throwing, explosions, high-energy |
| `05_ATMO` | 10-15% | Clouds, mist, breathing room, stillness |

| Tier | % of pool | Usage |
|---|---|---|
| **S (Hero)** | 10-15% | Lock for Final Climax. Max 2-3 at Chorus 1. |
| **A (Anchor)** | 50-60% | Verses, Pre-Chorus — narrative backbone. |
| **B (Buffer)** | 25-30% | Cooldown between intense shots. Bridges, transitions. |

**Trim rules** (never use raw 8s source):
- Emotion clips: trim 1.5s->5.5s (Apex Cut — peak expression)
- Kinetic clips: trim 0.8s->4.8s (Front-Momentum — peak force)
- Static/Wide clips: trim 3.0s->7.5s (Resolve Cut — settling motion)

---

## Workflow

### Phase 1: Pre-flight

```
get_timeline()  -> store fps, width, height, tracks, totalFrames
get_media()     -> separate video clips vs audio tracks
                -> classify clips into 5 buckets + 3 tiers
                -> lock Tier S clips (do not use until Climax)
```

Read project docs (`music.md`, `lyrics.md`) for **narrative context only** — not for timing.

### Phase 2: Beat detection + Vocal transcript

```
detect_beats({ mediaRef: "<music_id>" })
  -> store BPM, beats[], downbeats[]
  -> dedupe: if two downbeats < (60/BPM * 0.4)s apart, keep first
  -> bar_duration = (60/BPM) * 4

get_transcript({ granularity: "words" })        <- preferred after music placed
  OR inspect_media({ mediaRef: "<music_id>", wordTimestamps: true })
  -> store word_timeline: [{text, start, end}, ...]
```

**Build phrase_boundaries** from word_timeline:
- Silence gap >= 0.3s between words -> phrase boundary
- Punctuation (. ! ? ,) at word end -> phrase boundary
- No words for > 2.0s (instrumental) -> boundary at both edges

### Phase 3: Cut point selection

**Algorithm: phrase-first, beat-validated.**

```
For each phrase_boundary:
  snap to nearest downbeat within tolerance = (60/BPM) * 0.5
  if no downbeat within tolerance -> use first downbeat AFTER boundary

Enforce duration bounds:
  interval < 3.0s -> merge (remove cut point, extend shot)
  interval > 6.0s -> split at midpoint downbeat (prefer sub-phrase pause >= 0.15s)

Final check: every cut point must be a real downbeat AND between phrases.
```

**Section pacing** (from docs or energy-based fallback):

| Section | Target duration | Tier allocation |
|---|---|---|
| Intro | 4.0s-5.5s | B + Atmo, Foley active |
| Verse | 3.8s-4.5s | A + B |
| Pre-Chorus | 3.5s-4.2s | A, build tension |
| Chorus | 3.8s-4.5s | Max 2-3 S + A |
| Bridge | 4.0s-5.5s | Atmo + B only (starve visuals) |
| Solo | 4.0s-5.5s | A, beauty shots |
| Final Chorus | 3.0s-3.5s | **8-10 S**, max energy |
| Outro | 4.5s-6.0s | B + Atmo, ambient bleed |

If no vocals (instrumental only), divide by duration: 0-12% opening, 12-35% intimate, 35-65% explosive, 65-82% reflective, 82-100% closure.

### Phase 4: Curate + Place

For each cut point:

```
1. search_media({ query: "<cinematic query>", scope: "visual", limit: 5 })
2. Pick best unused clip (not in used_set, different scale from previous)
3. inspect_media({ mediaRef: "<pick>", overview: true })
   -> find trim window (Apex/Front-Momentum/Resolve cut)
4. Add to used_set
```

Batch place with `add_clips`:
```
add_clips({ entries: [
  { mediaRef: "AAA", startFrame: 1804, endFrame: 1919 },
  { mediaRef: "BBB", startFrame: 1919, endFrame: 2033 },
  ...
]})
```

Safety: `endFrame - startFrame` must not exceed `source_duration * fps`.

### Phase 5: Audio

```
1. Place music:     add_clips({ entries: [{ mediaRef: "<music>", startFrame: 0 }] })
2. Music fades:     set_clip_properties({ clipIds: ["<music_clip>"], fadeInFrames: 30, fadeOutFrames: 90 })
3. Intro Foley:     set_clip_properties({ clipIds: ["<clip1_audio>"], volumeDb: 0, fadeOutFrames: 60, fadeOutInterpolation: "smooth" })
4. Mute scratch:    set_clip_properties({ clipIds: ["<all_other_audio>"], volumeDb: -60 })
5. Outro ambient:   set_clip_properties({ clipIds: ["<last_audio>"], volumeDb: -4, fadeInFrames: 30 })
```

### Phase 6: Track cleanup

```
get_timeline()
manage_tracks({ set: [
  { trackId: "<V1>", name: "Main" },
  { trackId: "<A1>", name: "Music" },
  { trackId: "<A2>", name: "Foley" }
]})
```

### Phase 7: QA (11-point audit)

| # | Check | Tool | Pass |
|---|---|---|---|
| 1 | No gaps | `get_timeline` | `gaps == []` |
| 2 | No duplicates | `get_timeline` | unique mediaRef == total clips |
| 3 | Duration bounds | `get_timeline` | all shots in [3.0s, 6.0s] |
| 4 | Phrase alignment | `get_transcript` + `detect_beats` | no word straddling cut points |
| 5 | Intro Foley | `get_timeline` | clip 1 audio >= -6dB |
| 6 | No dead frames | `inspect_timeline` | all frames render content |
| 7 | 4D contrast | `inspect_timeline` | Scale(t) != Scale(t-1) |
| 8 | Exposure | `inspect_color` | shadow/highlight clip < 5%, lum 15-85% |
| 9 | Color balance | `inspect_color` | no jarring casts |
| 10 | Source integrity | `inspect_media` | no corrupted files |
| 11 | Climax escalation | `inspect_timeline` | Tier S concentrated at Final Chorus |

**Fail -> fix -> re-check.** QA agents are read-only; edit agents fix via `swap_clip_media`/`set_clip_properties`.

### Phase 8: Delivery

```
Music Video assembled (Director Cut)
  Song: [name] ([duration]) | BPM: [bpm]
  Clips placed: [N] (0% duplicate)
  Pacing: [3.0s-6.0s] enforced
  Phrase-boundary cuts: verified
  Press Space in Palmier to preview.
```

---

## Multi-song

When multiple songs on one timeline:
- Strict source pool partitioning (zero cross-contamination)
- Independent `detect_beats` per song
- Global `used_set` across all songs
- Song 2 starts at Song 1's last frame

---

## Cut on Action

```
Clip A: cut at F_Apex (peak of motion — arm at highest, foot leaving ground)
Clip B: start at F_Impact (landing — blade hits, foot lands)
Downbeat falls between F_Apex and F_Impact.
```

Use `inspect_media({ overview: true })` to find these frames.

**3 match cut types:**
- **Occlusion:** A turns away (screen darkens) -> B reveals new scene from darkness
- **Directional whip:** A sweeps L->R with blur -> B continues L->R motion
- **Graphic/eyeline:** A ends with round object at center -> B starts with different round object at center

---

## Footage Recycling (when short on clips)

| Technique | How |
|---|---|
| Punch-in 250% | Crop into eyes/hands from a wide used earlier |
| Speed ramp | 400% -> 25% slow-mo on kick -> 300% out |
| Horizontal flip | Mirror to reverse screen direction |
| Reverse | Play backwards (sit down -> stand up) |
| Flash cut | 3-5 frame subliminal insert between hard cuts |

---

## Markers

| Color | Section |
|---|---|
| `#FF6D00` Orange | Hook / Intro |
| `#2979FF` Blue | Verse |
| `#AA00FF` Purple | Chorus |
| `#00C853` Green | Bridge / Solo |
| `#FF1744` Red | Final Climax |
| `#78909C` Grey | Outro |

---

## Common Failures

| Problem | Cause | Fix |
|---|---|---|
| Silent intro | Muted all scratch audio | Keep clip 1 at 0dB, fadeOut 60f |
| Weak climax | Used Tier S too early | Lock S clips; max 2-3 at Chorus 1 |
| Scale stutter | Two same-scale shots adjacent | Enforce Scale(t) != Scale(t-1) |
| Mid-phrase cut | Bar-math without transcript | Use `get_transcript`, cut at phrase gaps |
| 1-frame black gap | Used `source` instead of `endFrame` | Always use `endFrame` in `add_clips` |
| Sequential clips | STT_001->002->003 | Use `search_media` for every clip |
| Shot < 3.0s | 1-2 bars at high BPM | Merge to 3-4 bars |
| Shot > 6.0s | Missing intermediate cut | Split at midpoint downbeat |

---

## Guardrails

- Never modify or delete source media files.
- Never export without explicit user request.
- All frame math uses `fps` from `get_timeline`.
- Prefer visual variety over literal keyword accuracy.
- Trust `search_media` results over `image.txt` descriptions.
