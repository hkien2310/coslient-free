# Lyric Craft — Kỹ Thuật Viết Lyrics
> v3.0 — Dual-Layer Semantics + Scene Transplant + Reverse Restraint Full Spectrum | 2026-08-20

---

## MỤC LỤC

- [0 — QUY ĐỊNH CẤU TRÚC FILE (MUSIC.MD & LYRICS.MD)](#0--quy-định-cấu-trúc-file-musicmd--lyricsmd)
- [1 — ĐẶT TÊN BÀI](#1--đặt-tên-bài)
- [2 — SHOW DON'T TELL](#2--show-dont-tell)
- [3 — OBJECT LEITMOTIF](#3--object-leitmotif)
- [4 — KỸ THUẬT NÂNG CAO](#4--kỹ-thuật-nâng-cao)
- [5 — FAILURE PATTERNS](#5--failure-patterns)
- [6 — PATTERNS LIBRARY](#6--patterns-library-file-riêng) *(file riêng: `lyric_patterns_library.md`)*
- [7 — CHECKLIST FINALIZE](#7--checklist-finalize)

---

# 0 — QUY ĐỊNH CẤU TRÚC FILE (MUSIC.MD & LYRICS.MD)

> **NGUYÊN TẮC CỐT LÕI:**
> 1. **Gộp toàn bộ Lyrics có Tag cấu trúc Suno vào `music.md` (hoặc `music_trackX.md`).**
> 2. **File `lyrics.md` (hoặc `lyrics_trackX.md`) CHỈ CHỨA LỜI NGUYÊN BẢN (Plain Lyrics) để upload lên DistroKid.**

### Quy Chuẩn 10 Điểm Bắt Buộc Cho File `lyrics.md` (DistroKid Plain Lyrics):

1. **Chỉ chứa lời bài hát thuần túy (Just add lyrics. No other information).**
2. **Không ghi tên ca sĩ/vocalist (Do not include the vocalist's name).**
3. **Không chứa bất kỳ text thừa hoặc tag đoạn nào (Do not include extra text: CẤM ghi "Intro", "Verse", "Chorus", "Bridge", "Outro", credit, link social...).**
4. **Các câu/đoạn lặp lại phải được viết đầy đủ từng dòng (Repeated lines must be written out. Don't write "Chorus 2x", "Repeat 3x").**
5. **Mỗi dòng bắt buộc bắt đầu bằng một chữ viết hoa (Begin each line with a capital letter).**
6. **CẤM TUYỆT ĐỐI dấu câu ở cuối mỗi dòng (Do not use punctuation at the end of a line — không chấm `.`, không phẩy `,`, không chấm than `!`, không chấm hỏi `?` ở cuối dòng).**
7. **Chỉ dùng đúng 1 dòng trống cách giữa các khổ (Do not include blank lines except between verses or chorus).**
8. **Mỗi dòng là một câu trọn vẹn, không quá dài (One sentence per line. Avoid excessively long lines).**
9. **Không tự ý che giấu từ ngữ nhạy cảm trừ khi bài hát thực tế bị bleep/mute âm thanh (Don't censor explicit words unless dropped/bleeped).**
10. **Không format markdown phức tạp, không code block trong file này.**

---

# 1 — ĐẶT TÊN BÀI

> Tiêu đề là điểm chạm đầu tiên. Phải như một tác phẩm nghệ thuật — không phải tóm tắt nội dung.

## Quy Tắc Cứng

- **Tối đa 3 từ** — không được dài hơn
- Gợi hồn bài mà người chưa nghe cũng cảm nhận được
- Hoặc kỳ lạ — gây tò mò, buộc người ta bấm nghe
- Luôn đưa **3–5 phương án** kèm phân tích ngắn

## Bộ Lọc Chống Cheesy

- ❌ Cấm từ cường điệu: *Agony, Shattered, Bleeding Heart, Tears, Sorrow, Weeping*
- ❌ Cấm công thức "Of The": *Echoes of the Heart · Symphony of the Soul*
- ❌ Cấm câu hỏi tu từ sến: *Why Did You Leave? · Where Did Our Love Go?*

## 5 Trụ Cột Đặt Tên Sang

**Trụ cột 1 — Trừu Tượng Hóa, Hiện Tượng Học & Semantic Hijacking (Cướp Nghĩa Thuật Ngữ)**
Mượn thuật ngữ vật lý/khoa học/kỹ thuật/địa lý để tạo ẩn dụ 2 tầng nghĩa (nghĩa đen là khoa học, nghĩa bóng là cảm xúc nhân sinh).
- ✅ *Blood Bank · Chinese Satellite · Event Horizon · Cold Start · Half-Life · Escape Velocity · Holocene*

**Trụ cột 2 — Vật Thể Hóa & Không Gian Cụ Thể**
Vật thể đời thường đại diện toàn bộ câu chuyện.
- ✅ *Casimir Pulaski Day · Stoned at the Nail Salon · Fake Plastic Trees*

**Trụ cột 3 — Phá Vỡ Ngữ Pháp & Xung Đột Hình Ảnh**
Kết hợp từ đối lập kịch liệt → siêu thực.
- ✅ *Bullet With Butterfly Wings · Crying Lightning · Flightless Bird, American Mouth*

**Trụ cột 4 — Chữ Thường & Lời Nói Đời Thường**
Lowercase → riêng tư, thì thầm.
- ✅ *when the party's over · hope is a dangerous thing · Why'd You Only Call Me When You're High?*

**Trụ cột 5 — Câu Hỏi Bỏ Ngỏ & Nghịch Lý**
Mâu thuẫn buộc người nghe bấm vào để hiểu.
- ✅ *The System Only Dreams in Total Darkness · How to Disappear Completely*

## Bài Kiểm Tra Tiêu Đề (4 Điểm)

1. **Kiểm tra sến:** Có từ nào giống AI tạo ra không? (*Echoes, Whispers, Forever*) → Đổi.
2. **Kiểm tra hình ảnh:** Tiêu đề gợi bức tranh cụ thể hay chỉ khái niệm?
3. **Kiểm tra tò mò:** Đọc lên có kỳ quặc, muốn bấm nghe không?
4. **Kiểm tra định dạng:** Cân nhắc *toàn bộ chữ thường* để tăng tính indie/tự sự.

---

# 2 — SHOW DON'T TELL

> Cảm xúc gắn vào **vật thể, địa điểm, hành động, chi tiết giác quan** — không bao giờ kể tên trực tiếp.

| ❌ Yếu (Trừu tượng) | ✅ Mạnh (Giác quan) |
| :--- | :--- |
| *I was sad. I miss the past.* | *Your coat still hangs behind the kitchen door.* |
| *Love is in my heart.* | *The blue cup caught the morning on my windowsill.* |
| *Memories shine forever.* | *The chair by the window still knows your shape.* |

**Thủ pháp Siêu thực:**
- **Xung đột Thời gian:** *The clock on the wall ticks backwards, bringing 1982 to the kitchen door.*
- **Biến đổi Vật chất:** *I planted tea leaves in your cup, and a tiny forest grew from the porcelain rim.*
- **Kiến trúc Sống:** *The floorboards hum the song you used to play.*

---

# 3 — OBJECT LEITMOTIF

> Chọn 1 vật thể bình thường TRƯỚC KHI viết → lên kế hoạch xuất hiện nhiều lần → lần cuối phải gây chấn động.

**Bước 1 — Chọn Vật thể.** Phải:
- Cực kỳ bình thường (không phải "trái tim", "bầu trời", "ngọn gió")
- Gắn với nhân vật cụ thể
- Có thể nhìn/chạm/ngửi/nghe — không phải khái niệm

**Bước 2 — Lên kế hoạch Xuất hiện (tối thiểu 3 lần):**

| Lần | Ngữ cảnh | Mức độ cảm xúc |
| :--- | :--- | :--- |
| **1** (V1/V2) | Giới thiệu — bình thường, trung tính | 0% — chỉ là vật |
| **2** (Chorus/V3) | Gắn với hành động/kỷ niệm | 40% — bắt đầu mang ý nghĩa |
| **3** (Bridge/V4) | Thể hiện sự thay đổi | 70% — người nghe bắt đầu lo |
| **4** (Outro/Final) | Ngữ cảnh đã hoàn toàn thay đổi | 100% — sự đền đáp |

**Bước 3 — Quy tắc Đền đáp.** Lần cuối phải có ít nhất 1 trong:
- Ngữ cảnh đã đảo ngược hoàn toàn
- Hành động đi kèm đã thay đổi
- Cùng từ nhưng nghĩa đã khác hoàn toàn

**Bước 4 — Scene Transplant: Cho Vật Thể Lên Tiếng (Biến Thể Cao Trào)**

Tại lần xuất hiện thứ 3 hoặc 4 (cao trào), cho vật thể **nói bằng ngôi thứ nhất**. Vật thể kể điều nó chứng kiến mà không bao giờ nêu tên nhân vật chính. Người nghe tự điền.

```
PROGRESSION MẪU — Chiếc cốc xanh:

Lần 1 (V1): "The blue cup sat on the windowsill."
             [Giới thiệu. Chỉ là vật. 0% cảm xúc.]

Lần 2 (V2): "The blue cup caught the morning light while she hummed."
             [Gắn với hành động. Bắt đầu mang ý nghĩa. 40%.]

Lần 3 (Bridge — LÊN TIẾNG):
             "The blue cup said: I've been full of nothing since Tuesday."
             [Vật thể nói. Nén cả sự vắng mặt vào 1 câu phàn nàn. 80%.]

Lần 4 (Outro): "The blue cup is gone."
             [Đền đáp. Ngay cả vật chứng cũng biến mất. 100%.]
```

**3 kiểu cho vật thể lên tiếng:**

| Kiểu | Vật thể nói gì | Ví dụ |
| :--- | :--- | :--- |
| **Phàn nàn** | Kêu ca về việc bị bỏ rơi / quá tải / vô dụng | *"The alarm clock: I've been screaming at nobody for eleven days."* |
| **Nhân chứng** | Kể lại điều nó nhìn thấy mà không phán xét | *"The hallway light: She packed quiet. Shoes first, then the pictures."* |
| **Tự hào lặng lẽ** | Khoe nhỏ về vai trò mà không ai biết | *"The doorknob: I'm the last thing she touches before the world starts."* |

**Quy tắc cứng cho Scene Transplant:**
- Vật thể chỉ được nói **đúng 1 lần** trong bài — dùng nhiều hơn thì thành phim hoạt hình, mất trọng lượng
- Vật thể nói bằng **vocabulary của chính nó** — cốc nói về rỗng/đầy, đồng hồ nói về tiếng kêu, đèn nói về sáng/tối
- Không bao giờ nêu tên nhân vật chính trong lời vật thể nói — "she" hoặc "someone" hoặc "nobody", không bao giờ dùng tên riêng

---

# 4 — KỸ THUẬT NÂNG CAO

## Nhóm A — Thời Gian & Ký Ức

**A1. Ngày Vô Danh Làm Vũ Khí Cảm Xúc**
Đặt khoảnh khắc trọng đại vào ngày bình thường nhất (Thứ Ba, Thứ Tư).
```
✅ "That the last time looked exactly like a Tuesday"
✅ "He called his daughter on a Wednesday — just to say the yard was looking fine"
```
**Công thức:** `[Khoảnh khắc quan trọng] + [ngày/thời điểm vô danh nhất]`

**A2. Habit Language — Nén Cả Đời Vào Một Hành Động**
```
✅ "She measured out the flour like she always had"
✅ "One hand along the fence the way a man does when a thing has been familiar"
```
**Công thức:** `[Hành động] + "like she/he always had"` hoặc `"the way [a/the] [noun] does"`

**A3. Ký Ức Cơ Thể Trước Ký Ức Trí Tuệ**
Ưu tiên giác quan thấp (tay, chân, trọng lượng, nhiệt độ) trước giác quan cao.
```
✅ "My fingers remember the weight of the key"
✅ "The door knob still catches halfway through the turn"
```

**A4. Lão Hóa Song Song**
Đặt sự lão hóa của con người cạnh sự lão hóa của thực thể tự nhiên.
```
✅ "The oak tree is older. And I am old, too."
```

## Nhóm B — Hình Ảnh & Metaphor

**B1. Numbered Specificity — Độ Cụ Thể Theo Số**
```
✅ "The third wooden step has the very same sound."
   → Người nghe biết: người này đã leo cầu thang này hàng nghìn lần.
```

**B2. Compressed Metaphor — Ẩn Dụ Nén**
`[Vật thể] like [khái niệm]` — càng ít từ, người nghe điền nhiều bằng ký ức cá nhân.
```
✅ "Hands like stories"         → 3 từ chứa toàn bộ biography người già
✅ "Like loose change pressed against her chest"
```

**B3. Universal Specific — Chi Tiết Phổ Quát**
Chi tiết đủ cụ thể để hình dung rõ, nhưng đủ phổ quát để người nghe thay bằng ký ức của mình.
```
✅ "The pencil lines carved on the edge of the door."
```

**B4. Animating the Inanimate — Hoạt Hóa Vật Vô Sinh**
```
✅ "I go where the honey learns to breathe."
```

**B5. Reframing Decay as Completion — Đảo Nghĩa Lão Hóa**
```
❌ "The iron is rusted and broken"
✅ "The iron is rusted but perfectly healed"
```

**B6. Productive Ambiguity — Mơ Hồ Có Chủ Đích**
Một từ mang hai nghĩa đều đúng → chiều sâu mà không cần giải thích.
```
✅ "Now I'm still, and I'm not ashamed."
   Still (1): vẫn còn đây / Still (2): bất động, không còn chạy trốn
```

**B7. Safe Surrealism — Siêu Thực An Toàn**
```
✅ "A giant wing moves through the sky,
    Doesn't scare me, doesn't fly.
    It just watches like it knows my name."
```
**Công thức:** `[Hình ảnh kỳ dị] + [câu trấn an ngay sau]`

**B8. Semantic Hijacking & Double-Layered Punchlines (Ẩn Dụ 2 Tầng Nghĩa Từ Thuật Ngữ)**
Lấy thuật ngữ kỹ thuật, thiên văn, vật lý hay hệ thống áp dụng hoàn toàn theo nghĩa đen vào mối quan hệ người-với-người hoặc thân phận con người. Tầng mặt là khoa học/vật lý, tầng ngầm là cảm xúc.
```
✅ "Event Horizon: The point where even light gives up turning back."
✅ "Cold Start: We built the whole fire by hand before the spark caught on."
✅ "Background Noise: You were screaming, but the galaxy was just tuning its guitar."
```
**Công thức:** `[Thuật ngữ chuyên ngành] + [hành động thể hiện nghĩa đen của nó trong đời sống]`

**5 Vùng Thuật Ngữ Khai Thác:**

| Vùng | Ví dụ thuật ngữ | Cảm xúc ngầm |
| :--- | :--- | :--- |
| Vật lý / Thiên văn | Event Horizon, Half-Life, Escape Velocity, Redshift | Mất mát, xa dần, điểm không quay lại |
| Công nghệ / Hệ thống | Cold Start, Background Noise, Deadlock, Fallback | Cô đơn, bế tắc, phương án B |
| Sinh học / Y khoa | Phantom Limb, Dormant, Scar Tissue, Antibody | Vắng mặt mà vẫn đau, tự vệ, hồi phục |
| Địa lý / Khí tượng | Fault Line, Undertow, Windshear, Permafrost | Rạn nứt ngầm, sức kéo vô hình, đóng băng |
| Kiến trúc / Vật liệu | Load-Bearing Wall, Foundation Crack, Scaffolding | Cái giữ mọi thứ đứng, đổ vỡ cấu trúc |

**⚠️ LUẬT MỘT NHẢY (One-Jump Rule) — LUẬT CỨNG BẮT BUỘC:**

Từ tầng mặt (nghĩa đen) đến tầng ngầm (cảm xúc), người nghe chỉ được nhảy **đúng 1 lần**. Vẽ chuỗi liên tưởng ra — nếu có hơn 1 mũi tên → viết lại.

```
✅ 1 NHẢY (pass):
   "Event Horizon" → điểm mà ánh sáng không quay lại = điểm mà tình yêu không quay lại
   "Phantom Limb" → cảm giác đau ở chân đã mất = cảm giác nhớ người đã đi
   "Load-Bearing Wall" → bức tường giữ cả nhà đứng = người giữ cả gia đình đứng

❌ 2+ NHẢY (fail — viết lại):
   "Quantum Entanglement" → hạt lượng tử → liên kết bí ẩn → duyên phận (2 nhảy)
   "Heisenberg Uncertainty" → đo vị trí thì mất vận tốc → biết rõ thì mất tự do (2 nhảy)
   "Entropy" → nhiệt động lực → hỗn loạn tăng → tình yêu phai (2 nhảy, quá trừu tượng)
```

**Tự kiểm tra:** Nói thuật ngữ cho 1 người bạn bình thường. Nếu họ cần giải thích nghĩa gốc trước khi hiểu nghĩa bóng → fail. Nếu nghe xong là "à, tao hiểu" → pass.

**⚠️ LUẬT ĐIỂM PHÁ THÌ CHẾT (Explain-It-And-It-Dies) — LUẬT CỨNG BẮT BUỘC:**

Chỉ viết tầng mặt. **KHÔNG BAO GIỜ** giải thích tầng ngầm trong chính lyrics. Người nghe tự nhảy sang — khoảnh khắc "à tao hiểu rồi" tạo ra khoái cảm. Giải thích = giết khoái cảm đó.

```
❌ CHẾT (giải thích ngay sau ẩn dụ):
   "Event Horizon — that's what love is, the point of no return"
   "Escape Velocity — just like how we need to break free from pain"
   "Phantom Limb — I still feel you even though you're gone"

✅ SỐNG (chỉ tầng mặt, người nghe tự nhảy):
   "Event Horizon — even light gave up turning back"
   "Escape Velocity — we burned everything just to leave the ground"
   "Phantom Limb — the bed still dips on your side at three a.m."
```

**Quét lỗi:** Dòng tiếp theo sau ẩn dụ có chứa "like", "meaning", "that's what", "it means", "just like", "in other words", "the way that" không? → Xóa dòng đó. Ẩn dụ phải tự đứng.

## Nhóm C — Cấu Trúc & Arc

**C1. POV Arc — Hành Trình Điểm Nhìn**
```
Verse 1  → "An old man... She..."          [HỌ — quan sát]
Chorus   → "We keep living..."             [CHÚNG TA — kéo vào]
Bridge   → "You thought... You thought..." [BẠN — chỉ thẳng]
Outro    → "So sit a little longer..."    [BẠN — hành động]
```
**Công thức:** `They (observe) → We (include) → You (implicate) → [action]`

**C2. Anaphora + Cú Cắt**
```
✅ "You thought there would be another    [lặp 1]
    You thought that it could wait        [lặp 2]
    You thought you'd have the words      [lặp 3]
    But words don't always wait."         [CÚ CẮT]
```

**C3. Negative Definition — Định Nghĩa Bằng Phủ Định**
```
✅ "The house doesn't ask where we travel so far.
    It doesn't keep track of the miles or the scars.
    It only remembers the shape of our hands."
```

**C4. Verbal Callback — Gọi Lại Âm Thanh**
```
Verse 2: "The bus still rolls, it hums instead."   [hum = già nua]
Outro:   "This unusual town will hum you home."    [hum = lời ru, nhà]
```

**C5. Inversion of Agency — Đảo Chiều Chủ Thể**
```
❌ "I finally accepted the world"
✅ "Like the world is letting me in"
```

**C6. Ritual Object as Threshold — Vật Thể Nghi Lễ**
Mở bài bằng hành động nghi lễ nhỏ có sẵn ý nghĩa văn hóa.
```
✅ "I leave my shoes outside the door."
```

**C7. Absence as Presence — Vắng Mặt Như Hiện Diện**
```
✅ "There's no rush on the corner now,
    No young shoes chasing time."
```
**Công thức:** `"No [vật thể động] [verb]-ing [điều trừu tượng]"`

**C8. Elder Dialogue — Hỏi Người Già**
```
✅ I asked a man with silver hair,
   "Don't you miss the faster years?"
   He smiled like he'd already been there,
   Said, "Speed's not what keeps us here."
```

## Nhóm D — Outro & Kết Thúc

**D1. Elegy → Instruction**
Bài về mất mát không kết thúc bằng grief — chuyển hóa thành hành động ngay hôm nay.
```
✅ "So sit a little longer at the table
    Let the phone call run a little long"
```

**D2. Tactile Time — Thời Gian Xúc Giác**
```
✅ "A woman counts the afternoon,
    Like loose change pressed against her chest."
```

**D3. The Shrinking Mirror — Gương Chiếu Hậu**
```
✅ "The mirror is shrinking." [nhà thu nhỏ trong gương]
   "The home out of you."    [nhà rút ra khỏi tâm hồn]
```

**D4. Dấu "..." và Kết Thúc Hiện Tại**
```
✅ "That the last time could be today..."
   → "..." = không đóng lại / "could be today" = hiện tại, không phải quá khứ
```

**D5. Reverse Restraint — Full Spectrum (Nghịch Đảo Tối Giản Toàn Diện)**

Hai chiều tương phản cùng lúc — cả **âm nhạc** lẫn **ngôn ngữ** đều cắt về tối thiểu tại khoảnh khắc cao trào cuối cùng.

**Chiều 1 — Drop Silence (Âm nhạc):**
Khi cả bài đang dồn dập nhiều lớp nhạc cụ (Synth, Drum, Bass) → **cắt cụt toàn bộ nhạc cụ về khoảng lặng** → chỉ còn tiếng thở / giọng mộc.

**Chiều 2 — Strip Rhetoric (Ngôn ngữ):**
Khi cả bài đang dày đặc ẩn dụ, siêu thực, semantic hijacking, nhiều layer → **câu cuối cùng PHẢI là tiếng người bình thường nói**. Không metaphor. Không simile. Không surrealism. Không thuật ngữ.

```
✅ TOÀN DIỆN (cả 2 chiều):
   3 verse đầy thiên văn + surrealism + dàn nhạc dày
   → Beat tắt. Giọng mộc:
   "Go home early tonight."

✅ CHỈ CHIỀU NGÔN NGỮ (beat vẫn nhẹ nhàng):
   Chuỗi hình ảnh siêu thực dày → câu cuối tối giản:
   "The rain still falls when you forget your coat."
   "She left the light on. That's all."

❌ FAIL — Câu cuối vẫn đang chơi thủ pháp:
   "The cosmos exhaled its final constellation" ← vẫn đang metaphor
   "We are the stardust returning to silence" ← vẫn đang poetic
```

**Nguyên tắc:** Ai đã dùng 20 thủ pháp mà kết bằng 1 câu trần trụi → người nghe nhớ câu đó, quên hết thủ pháp. Đó là mục tiêu.

**Tự kiểm tra:** Lấy câu cuối bài ra, đọc cho đứa trẻ 10 tuổi. Nó hiểu ngay không cần giải thích → pass. Nó nhíu mày → vẫn đang tu từ → viết lại.

---

# 5 — FAILURE PATTERNS

**Failure 1 — Aesthetic Break Giữa Verse và Chorus**
```
❌ Verse: "The doctor orders your tattoo"    [quirky, specific]
   Chorus: "You can be happy where you are" [greeting card]
```

**Failure 2 — Broken Promise**
```
❌ Setup:   "But don't be fooled, there's trouble too"
   Deliver: [Không xuất hiện lại]
```

**Failure 3 — "Boom Kaboom" Moment**
Một dòng chất lượng thấp đột ngột giữa bài tinh tế. Kiểm tra: đặt dòng đó cạnh dòng hay nhất bài — nó có xứng đáng không?

**Failure 4 — Gap Lớn Giữa Prompt và Lyrics**
```
❌ Prompt: "Tim Burton, dark-pop cabaret"
   Lyrics: "I got to have faith" / "These are the best days of my life"
```
Kiểm tra 4/5: lấy 5 từ khóa từ prompt → tìm echo trong lyrics.

**Failure 5 — Không Có Editorial Pass Cuối**
```
❌ "You're homey" / "Where you're" / "when you die, the people that you love" [câu không hoàn chỉnh]
```

**Failure 6 — Bẫy Lời Đóng Hẹp & Thuyết Minh Sa Bàn (Diorama Narration Trap) — [TỬ HUYỆT BẮT BUỘC TRÁNH]**
```
❌ Biểu hiện: Lời bài hát bị biến thành bản thuyết minh đồ vật/sa bàn (điểm danh từng chiếc đinh ốc, con hạc giấy, mũ xô, khay gốm, ca kíp công nhân). Lặp đi lặp lại 1 đồ vật khiến bài hát bị giam hãm trong 1 căn phòng hẹp, thiếu tầm vóc.
✅ CHÌA KHÓA BẮT BUỘC: TÍNH MỞ RỘNG TOÀNG KHÔNG GIAN (EXPANSIVE SONGWRITING). Lời bài hát BẮT BUỘC phải mở toang ra vũ trụ, bầu trời, thiên nhiên bao la, mặt trời, sự thức tỉnh, tính vô thường và cảm xúc nhân sinh phổ quát (học Pink Floyd, Frank Ocean, Daft Punk).
```

**Failure 7 — Bẫy Văn Phong AI Sáo Rỗng (AI Slop Diction Trap)**
```
❌ Biểu hiện: Lời bài hát chứa các từ vựng "muôn thuở" của AI, chung chung, sến sẩm, thiếu độ bám giác quan.
   CÁC TỪ CẤM KỴ: Echoes, whispers, shadows, endless, dancing in the light, symphony of soul, tapestry, unravel, ignite the flame, forevermore.
✅ CÁCH KHẮC PHỤC: Thay thế bằng ĐỘNG TỪ mạnh và VẬT THỂ cụ thể.
   - Thay "Echoes of your voice in the dark" → "Your voicemail still sits at twenty-four seconds."
   - Thay "Our endless love will shine" → "The tea went cold while we stopped keeping score."
```

**Failure 8 — Mổ Xẻ Ẩn Dụ Ngay Trong Bài (Autopsy Annotation) — [TỬ HUYỆT BẮT BUỘC TRÁNH]**
Viết ẩn dụ hay xong rồi GIẢI THÍCH nó ngay dòng tiếp theo = giết khoái cảm "à tao hiểu rồi".
**QUÉT LỖI:** Dòng sau ẩn dụ chứa "like", "meaning", "that's what", "it means", "just like", "in other words"? → Xóa dòng đó. Ví dụ pass/fail chi tiết: xem B8 — Luật Điểm Phá Thì Chết.

**Failure 9 — Ẩn Dụ Hai Nhảy (Two-Jump Metaphor)**
Thuật ngữ / ẩn dụ quá xa — người nghe phải suy luận 2+ bước mới tới cảm xúc → họ bỏ qua.
**KIỂM TRA:** Vẽ chuỗi liên tưởng bằng mũi tên. 1 mũi tên → pass. 2+ → đổi thuật ngữ. Ví dụ pass/fail chi tiết: xem B8 — Luật Một Nhảy.

---

# 6 — PATTERNS LIBRARY (FILE RIÊNG)

> **80+ patterns từ 936 hit thế giới → xem `style_music/lyric_patterns_library.md`**
> Chỉ tra cứu khi cần cảm hứng hoặc ví dụ cụ thể. Không cần đọc mỗi lần viết bài.

| Nhóm | Nội dung | Pattern đáng nhớ nhất |
| :--- | :--- | :--- |
| 1. Mở bài | Question-as-Entry, Time Anchor, Situation-Drop, Confession, Imperative, Chorus-First | *"Is this the real life?"* |
| 2. Hook & Chorus | Compressed Paradox, Anti-Chorus, Parallel List, 3-Word Punch, Title Placement | *"I can't feel my face... But I love it"* |
| 3. Word Choice | Body-Part Proxy, Mundane Object, Counter-Intuitive Verb, Negation, Proper Noun | *"Guilty feet have got no rhythm"* |
| 4. Verse Story | Verse-Specific/Chorus-Universal, Time-Jump, List-Story, Confession→Complicity | *"Fifteen years old smoking hand-rolled..."* |
| 5. Bridge & Outro | Future Scenario, Minimalist Collapse, Power Flip, Circular Return, Rhetorical Inversion | *"War, children" → "Love, sister"* |
| 6. POV & Dialogue | 1st→2nd Pivot, Rules List, Future Dialogue, 9 Question Types | *"One: Don't pick up the phone"* |
| 7. Hình ảnh & Thời gian | Weather=Emotion, Metaphor Escalation, Tense Split, Clock Time, Olfactory Anchor | *"Heat waves been fakin' me out"* |
| 8. Cấu trúc & Rhythm | "But" Pivot, Density Contrast, Anaphora, Call-and-Echo | *"...for a thousand MORE"* |

---

# 7 — CHECKLIST FINALIZE

```
NAMING:
[ ] Tối đa 3 từ?
[ ] Không có từ cheesy (Echoes, Whispers, Tears)?
[ ] Gợi hình ảnh cụ thể, không chỉ khái niệm?
[ ] Đã có 3–5 phương án với phân tích?

OPENING:
[ ] Có câu hỏi, time anchor, situation-drop, hoặc confession?
[ ] Không mở bằng abstract statement?

VERSE:
[ ] Có ít nhất 1 proper noun (tên, brand, địa danh)?
[ ] Có body-part-as-emotion hoặc mundane-object-as-symbol?
[ ] Ít nhất 1 sensory detail không phải visual (mùi, nhiệt độ, trọng lượng)?
[ ] Verb có gây bất ngờ (counter-intuitive)?

CHORUS:
[ ] Đủ generic để triệu người hát theo?
[ ] Không có chi tiết chỉ đúng với 1 người?
[ ] Có paradox, question, hoặc defeat-as-power?
[ ] Syllable density thấp hơn verse?
[ ] Có "but" / "yet" / "still" hoặc pivot word?

BRIDGE:
[ ] Ở thì/không gian khác với verse?
[ ] Flip POV hoặc power dynamic?
[ ] Không chỉ là chorus lặp lại?

OUTRO:
[ ] Ngắn hơn chorus?
[ ] Chọn 1 trong: circular return / declaration strip / unresolved state / rhetorical inversion / reverse restraint?
[ ] Reverse Restraint Full Spectrum: câu cuối là tiếng người bình thường nói? (đứa trẻ 10 tuổi hiểu ngay?)
[ ] Nếu Drop Silence: beat thực sự tắt tại câu cuối?

OBJECT LEITMOTIF:
[ ] Vật thể xuất hiện ít nhất 3 lần?
[ ] Lần cuối đảo ngữ cảnh hoàn toàn?
[ ] Đã cân nhắc Scene Transplant (cho vật thể lên tiếng tại lần 3/4)?
[ ] Nếu dùng Scene Transplant: vật thể chỉ nói đúng 1 lần? Dùng vocabulary của chính nó? Không nêu tên nhân vật?

SEMANTIC HIJACKING (DUAL-LAYER):
[ ] Có áp dụng Semantic Hijacking (ẩn dụ 2 tầng nghĩa từ thuật ngữ)?
[ ] LUẬT MỘT NHẢY: Vẽ chuỗi liên tưởng — chỉ có 1 mũi tên? (2+ → viết lại)
[ ] LUẬT ĐIỂM PHÁ THÌ CHẾT: Dòng sau ẩn dụ có giải thích nghĩa bóng không? (có → xóa dòng đó)
[ ] Thuật ngữ chọn có quen thuộc với người nghe bình thường không? (nói cho bạn bè, họ "à hiểu rồi" ngay?)

TOÀN BÀI:
[ ] Đã quét sạch AI Slop Diction (không có: echoes, whispers, shadows, endless, dancing in the light, symphony of soul)?
[ ] Đã quét Autopsy Annotation (không có dòng giải thích ẩn dụ chứa "like/meaning/that's what/it means/just like")?
[ ] Đã quét Two-Jump Metaphor (không có ẩn dụ cần 2+ bước suy luận)?
[ ] Abstract statement nào cũng có ≥ 2 concrete images trước đó?
[ ] Metaphor leo thang từ thấp → cao?
[ ] Chorus không có proper noun?
[ ] Có ít nhất 1 POV shift có chủ đích?
[ ] Alignment lyrics ↔ style prompt: ≥ 4/5 từ khóa có echo?
[ ] Mọi tension/setup đều có resolution hoặc bỏ ngỏ có chủ đích?
[ ] Không có lỗi ngữ pháp, câu bỏ lửng không có chủ đích?
```

---

*v3.0 — Tích hợp Dual-Layer Semantics (One-Jump Rule, Explain-It-And-It-Dies, Scene Transplant, Reverse Restraint Full Spectrum) từ phương pháp luận 杜蕾斯 2011-2017 | 2026-08-20*
*v2.0 — Merge từ coslient_lyrics.md + lyric_craft_world.md | 2026-08-06*
