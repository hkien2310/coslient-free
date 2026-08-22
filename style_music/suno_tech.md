# Coslient — Suno Tech

> **Vai trò file này:** Mọi thứ đặc thù cho Suno AI — cách viết prompt, tag syntax, viết hoa/thường, performance cues.
> Đây là kỹ thuật của **công cụ**, không phải kỹ thuật âm nhạc hay lyric craft.
>
> **Quy định file đầu ra trong project:**
> - File `music.md` (hoặc `music_trackX.md`) **bắt buộc tuân thủ đúng thứ tự 4 phần:**
>   1. `## 🔍 1. PHÂN TÍCH (ANALYSIS & PHILOSOPHY)` (Tứ thơ, cốt truyện, leitmotif, kỹ thuật)
>   2. `## 🏷️ 2. TÊN BÀI HÁT (SONG TITLE)` (Tên bài tối đa 3 từ)
>   3. `## 🎛️ 3. SUNO STYLE PROMPT` (Style prompt 8 thành phần chuẩn)
>   4. `## 📜 4. SUNO PERFORMANCE LYRICS` (Lời bài hát đầy đủ tag Suno để copy-paste)
> - File `lyrics.md` (hoặc `lyrics_trackX.md`) **chỉ chứa lời nguyên bản (Plain Lyrics)** theo đúng chuẩn đăng DistroKid (xem chi tiết tại `lyric_craft.md` §0).
>
> **Đọc kèm:**
> - [`lyric_craft.md`](lyric_craft.md) — Kỹ thuật viết lời & Show Don't Tell

---

## MỤC LỤC

- [1 — STYLE PROMPT ENGINEERING](#1--style-prompt-engineering)
- [2 — KEYWORD BANKS](#2--keyword-banks)
- [3 — ALIGNMENT TEST (4/5)](#3--alignment-test-45)
- [4 — TAG SYNTAX](#4--tag-syntax)
- [5 — PERFORMANCE CUES](#5--performance-cues)
- [6 — STRESS CAPITALIZATION](#6--stress-capitalization)
- [7 — NHỮNG TỪ TRÁNH TRONG PROMPT](#7--những-từ-tránh-trong-prompt)
- [8 — CHECKLIST TRƯỚC KHI GENERATE](#8--checklist-trước-khi-generate)

---

## 1 — STYLE PROMPT ENGINEERING

### 8-Component Structure

Một style prompt tốt phải có đủ 8 thành phần sau theo đúng thứ tự:

```
[1] Genre core        — 1–2 genre chính, không mâu thuẫn nhau
[2] Instrumentation   — tên nhạc cụ thực, không mô tả chung
[3] Vocal direction   — giới tính, tông, kỹ thuật delivery
[4] Cultural anchor   — nếu có aesthetic đặc thù vùng/thời đại
[5] Mood/atmosphere   — 2–3 từ, không chồng chéo nhau
[6] BPM + time sig    — tempo cụ thể hoặc dải BPM
[7] Production quality — melody/mix keywords
[8] Special Instrument — instrument chỉ xuất hiện tại 1 điểm (nếu có)
```

> [!WARNING]
> **Genre Lock Trap — [1] là thành phần nguy hiểm nhất.**
> Các label overloaded như `pop`, `folk`, `indie` bị Suno map thẳng vào training bucket và
> **override** mọi thứ viết ở [2]–[8]. Khi thấy "folk" nó lock vào sparse/acoustic/slow;
> khi thấy "pop" nó lock vào upbeat/synthetic/commercial. Hai từ không thể coexist.
>
> **Quy tắc:** Nếu bài là blend của 2 genre, ưu tiên ghi nhạc cụ cụ thể ở [2] thay vì ghi label ở [1].
> Dùng Cultural Anchor [4] để định hình feel thay vì genre name.

**Ví dụ hoàn chỉnh:**
```
[1] singer-songwriter ballad, chamber arrangement          ← label trung tính, không lock
[2] fingerpicked acoustic guitar, upright bass, piano, light brushed drums
[3] warm mature female alto, intimate close-mic delivery, no vibrato excess
[4] 1970s Laurel Canyon feel — James Taylor-esque fingerpicking, Carol King piano warmth
[5] melancholic, tender, introspective
[6] 72 BPM, 4/4
[7] organic cinematic production, wide stereo soundscape, haunting unforgettable melody
[8] A solo cello enters only at the final chorus, providing deep melodic counterpoint.
```

**Kỹ thuật thoát Genre Lock:**

| Vấn đề | Cách fix |
| :--- | :--- |
| `folk` lock sparse/acoustic quá mức | Xóa "folk", viết nhạc cụ trực tiếp: `fingerpicked nylon guitar, upright bass, no electronic elements` |
| `pop` lock synthetic/commercial | Xóa "pop", anchor vào era: `1970s Laurel Canyon singer-songwriter` |
| `folk + pop` conflict — AI chọn 1 trong 2 | Tách thành phần: `acoustic folk foundation [guitar, upright bass] with pop chorus arrangement [string pads, close harmonies]` |
| Genre không xác định | Anchor bằng reference thật: `in the style of Sufjan Stevens' Illinois-era production` |

**Cách viết Special Instrument vào prompt:**
```
A [cello/piano/glockenspiel] enters only at [section], providing [emotional description].
Ví dụ: "A solo cello enters only at the chorus, providing deep melodic counterpoint."
```

---

## 2 — KEYWORD BANKS

### Giai Điệu

```
soaring memorable melody
catchy singalong chorus
earworm hook
anthemic melody
haunting unforgettable melody
hummable tune
sweeping melodic lines
lyrical flowing melody
```

### Hòa Âm

```
rich emotional chord changes
unexpected harmonic shifts
bittersweet major-minor transitions
lush jazz-influenced harmonies
dramatic chord progression
emotionally complex chords
suspended chords resolving
```

### Nhịp Điệu / Groove

```
infectious groove
driving rhythmic pulse
syncopated rhythm
head-nodding beat
foot-tapping groove
rolling rhythmic momentum
hypnotic pulse
body-moving rhythm
```

### Sản Xuất

```
lush layered production
wide stereo soundscape
punchy compressed drums
warm analog tape saturation
crystal clear high fidelity
rich textured arrangement
cinematic wide-screen production
intimate studio quality
organic cinematic production
```

### Vocal

```
warm mature female alto
deep resonant male baritone
close intimate mic placement
raw emotional delivery
no excessive vibrato
Southern drawl with traditional harmonies
mature non-shrieky tone
high-lonesome harmony (3rd/5th intervals)
gang vocals in climax
stadium choir backing
```

---

## 3 — ALIGNMENT TEST (4/5)

Trước khi finalize, lấy 5 từ khóa từ prompt → tìm echo trong lyrics. Cần đạt **4/5**:

```
Ví dụ:
Prompt keywords: "Moroccan desert · midnight spice market · sultry · pheromone · burning"

Lyrics check:
✅ "desert fire"               ← Moroccan desert
✅ "market of the midnight mind" ← midnight spice market
✅ "it's a pheromone"          ← pheromone
✅ "salt upon the skin"        ← sultry
✅ "burning through the night" ← burning
→ 5/5 — alignment hoàn hảo ✅
```

Nếu < 4/5: hoặc revise lyrics, hoặc revise prompt, hoặc cả hai.

---

## 4 — TAG SYNTAX

Tags điều khiển cấu trúc bài. Suno đọc và thực thi chúng.

### Section Tags (bắt buộc)

```
[Intro]
[Verse]
[Verse 1]
[Verse 2]
[Pre-Chorus]
[Chorus]
[Bridge]
[Final Chorus]
[Outro]
[Short Intro]     ← 4–8 giây, dùng cho bài 2 phút
[Instrumental]
[Interlude]
```

### Section Tags (nâng cao)

```
[Build]
[Drop]
[Beat Breakdown]
[Solo]
[Guitar Solo]
[Piano Solo]
[Cello Solo]
[Vamp]
[Coda]
[Fade Out]
```

### Instrument Cue Tags

```
[cello enters]
[piano enters]
[strings swell]
[drums drop]
[bass drops]
[drums drop out]
[acoustic guitar only]
[full band]
[stripped back]
[solo voice]
```

### Silence/Texture Tags

```
[Pause]
[Silence]
[Music abruptly stops]
[Beat drops]
[Soft piano transition]
```

---

## 5 — PERFORMANCE CUES

Performance cues làm AI "con người" hơn. Đặt trong ngoặc vuông ngay trước hoặc sau dòng lyrics.

### Vocal Delivery

```
[whispered]
[spoken]
[half-spoken]
[breathless]
[hushed]
[tender]
[raw]
[passionate]
[anguished]
[restrained]
```

### Physical Cues

```
[Sigh]
[voice crack]
[catch in throat]
[trailing off]
[fading to silence]
```

### Harmony Cues

```
[harmonies enter]
[backing vocals]
[unison]
[close harmonies]
[3-part harmony]
[choir swells]
```

### Ví dụ sử dụng trong lyrics

```
[Outro]
[acoustic guitar fades]
[whispered]
This is home

[Bridge]
[strings swell]
[anguished]
I thought I'd have the words by then...
[voice crack]
But words don't always wait
```

---

## 6 — STRESS CAPITALIZATION

Kỹ thuật viết hoa phần âm tiết được nhấn, viết thường phần không nhấn. Suno v4+ đọc pattern này để xác định **trọng tâm nhịp và diction**.

> [!IMPORTANT]
> Kỹ thuật này **không thay thế** stress pattern thông thường — nó truyền tải stress pattern đó **trực tiếp** cho Suno thay vì để Suno tự đoán.

### Cú pháp cơ bản

```
someWHERE dayDREAMS    → "some" nhẹ, "WHERE" nặng; "day" nhẹ, "DREAMS" nặng
midNIGHT reCALLS       → nhịp waltz/compound tự nhiên
```

### 3 cách dùng

| Cách | Ví dụ | Khi nào |
| :--- | :--- | :--- |
| **Nhấn âm tiết cuối** | `softLY SLEEPS` / `gently CALLS` | Waltz 3/4, nhịp nhẹ nhàng |
| **Nhấn giữa từ ghép** | `underWORLD` / `sweetHEART` | Từ compound, cần split rõ |
| **Nhấn âm tiết đầu** | `DREAMing softly` | Verse downbeat, nhịp mạnh |

### Quy tắc cứng

- Nhất quán trong suốt một section (verse/chorus cùng pattern)
- Không mix ngẫu nhiên — nếu dùng, dùng có chủ đích toàn bài
- **Tối đa 1–2 từ được nhấn mỗi dòng** — nhấn quá nhiều = không nhấn gì cả
- Chorus nên có stress pattern khác verse (nhấn mạnh hơn, rõ hơn)

### Ví dụ áp dụng

```
❌ Không dùng kỹ thuật:
Somewhere daydreams become untrue
Meanwhile midnight withholds value

✅ Dùng stress capitalization:
SomeWHERE dayDREAMS beCOME unTRUE
MeanWHILE midNIGHT withHOLDS valUE
```

### Khai báo bắt buộc trong Style Prompt

> [!IMPORTANT]
> **Không khai báo = Suno bỏ qua capitalization.** Phải có dòng này thì kỹ thuật mới có tác dụng.

```
# Nhịp waltz / compound — nhấn âm tiết cuối:
"Very clear diction with emphasis on each stressed syllable as written in the lyrics."

# Nhịp 4/4 thông thường — nhấn âm tiết đã viết hoa:
"Sing each capitalized syllable with clear emphasis; unstressed syllables light and flowing."

# Khi muốn diction ảnh hưởng melody rõ:
"Honor the stress pattern in the lyrics exactly — capitalized syllables carry the melodic accent."
```

---

## 7 — NHỮNG TỪ TRÁNH TRONG PROMPT

```
❌ "High quality production"   — mọi người đều muốn, không có thông tin
❌ "4k production quality"     — thuật ngữ video, vô nghĩa với âm thanh
❌ "Emotional depth"           — không thể hướng dẫn AI bằng cách mô tả kết quả
❌ "Sophisticated energy"      — quá generic
❌ "Weirdcore/fantasy aesthetic" — subculture internet, AI không hiểu chính xác
❌ "Amazing vocals"            — không có thông tin cụ thể nào
❌ "Professional mix"          — tương tự "high quality"
❌ "Epic"                      — quá generic, AI hiểu theo nghĩa random
```

### ⛔ QUY TẮC CỨNG — TUYỆT ĐỐI CẤM NHẮC TÊN NGHỆ SĨ & TÁC PHẨM

> [!CAUTION]
> **CẤM TUYỆT ĐỐI** nhắc tên nghệ sĩ, ban nhạc, hoặc tên tác phẩm cụ thể trong bất kỳ Suno Style Prompt nào.
> Ví dụ: `Sade`, `Enya`, `Pink Floyd`, `Neil Young`, `Norah Jones`, `"Sailing"`, `"Harvest Moon"` — **tất cả đều bị cấm**.

**Lý do:**
1. **Gây hiệu ứng ngược (Semantic Bleed):** Suno sẽ cố clone phong cách cụ thể đó thay vì tạo ra âm nhạc thuần chất theo chỉ định nhạc cụ và cảm xúc.
2. **Rủi ro bản quyền:** Nhắc tên nghệ sĩ nổi tiếng trong prompt tạo ra nội dung có thể vi phạm copyright và gây vấn đề khi phân phối.
3. **Làm loãng thông tin:** Tên nghệ sĩ là "anchor mờ" — mỗi người nghe có định nghĩa khác nhau về "nghe như Sade". Mô tả nhạc cụ và texture mới là thông tin thực sự.

**Thay thế đúng chuẩn — Dùng mô tả âm thanh thay vì tên:**

| ❌ Cấm dùng | ✅ Thay bằng mô tả âm thanh |
| :--- | :--- |
| `in the style of Sade` | `smooth syncopated electric bassline, clean electric guitar with tape delay, intimate alto vocal with breathy delivery` |
| `like Enya` | `layered multi-tracked female choir harmonies, oceanic synth pads, lush cathedral spatial reverb, celtic harp arpeggios` |
| `Pink Floyd "Breathe" feel` | `shimmering 12-string acoustic guitar with analog tape delay, warm hammond organ pad, wide panoramic stereo, brushed drum groove` |
| `Norah Jones warmth` | `warm felt acoustic piano, soft nylon-string guitar, upright bass, hushed close-mic alto vocal, half-spoken delivery` |
| `like Neil Young "Harvest Moon"` | `vintage acoustic guitar with natural room reverb, warm brushed snare, steel guitar shimmer, laid-back nostalgic groove` |
| `Christopher Cross "Sailing"` | `coastal groove, syncopated warm electric bass, clean chorus guitar, mellow Rhodes piano, breezy lightweight production` |

### Genre Lock Labels — Nguy Hiểm Đặc Biệt

Các từ dưới đây là **overloaded** trong Suno training data. Khi xuất hiện ở vị trí [1] Genre Core,
chúng override toàn bộ các thành phần khác và lock bài vào 1 bucket duy nhất:

```
⚠️  "folk"    — lock: sparse, acoustic, fingerpicked, slow. Xóa → dùng nhạc cụ trực tiếp.
⚠️  "pop"     — lock: upbeat, synthetic, commercial hook. Xóa → dùng cultural anchor.
⚠️  "indie"   — quá rộng, AI hiểu rất nhiều thứ khác nhau → không có thông tin hữu ích.
⚠️  "country" — lock: twang, pedal steel heavy. Chỉ dùng khi muốn rõ ràng là Americana.
⚠️  "rock"    — lock: distorted guitar, loud drums ngay từ đầu. Dùng "blues rock 12/8" thay.
```

**Thay thế an toàn:**

| Thay vì | Dùng |
| :--- | :--- |
| `folk` | `fingerpicked acoustic guitar, upright bass, no electronic elements` |
| `pop` | `1970s Laurel Canyon singer-songwriter` hoặc `chamber pop arrangement` |
| `folk pop` | `acoustic folk foundation with pop chorus sensibility [string pads at chorus]` |
| `indie` | Tên era/region cụ thể: `early 2000s Pacific Northwest indie` |

---

## 8 — CHECKLIST TRƯỚC KHI GENERATE

```
STYLE PROMPT:
[ ] Đủ 8 components (genre, instruments, vocal, anchor, mood, BPM, production, special instrument)?
[ ] Không có từ trong danh sách "từ cần tránh"?
[ ] ⛔ KHÔNG có tên nghệ sĩ, ban nhạc, hoặc tên tác phẩm nổi tiếng nào (Xem §7)?
[ ] Special instrument được ghi rõ section và mô tả cảm xúc?
[ ] Stress capitalization được khai báo nếu dùng?

LYRICS:
[ ] Tất cả section tags đúng cú pháp [Chorus], [Bridge], v.v.?
[ ] Performance cues đặt đúng chỗ?
[ ] Stress capitalization nhất quán trong từng section?
[ ] Không mix kiểu nhấn ngẫu nhiên?

ALIGNMENT:
[ ] Đã chạy alignment test 4/5 giữa prompt keywords và lyrics?
[ ] Style prompt và lyrics cùng một vision không?

SPECIAL INSTRUMENT:
[ ] Ghi trong prompt?
[ ] Ghi tag [instrument enters] trong lyrics đúng section?
[ ] KHÔNG xuất hiện trước Chorus hoặc Bridge?
```

---

*v1.0 — Tách từ `suno_style_coslient_base.md` v8.2 | 2026-07-27*
