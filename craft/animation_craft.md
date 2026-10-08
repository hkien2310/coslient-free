# 🎬 ANIMATION CRAFT — QUY CHUẨN KỸ THUẬT CHUYỂN ĐỘNG VIDEO AI
v5.0 — Technical Motion Spec (Kling / Runway / Hailuo / Wan 2.1 / Luma)

> **Mục tiêu:** Quy định chuẩn kỹ thuật để chuyển hóa ảnh tĩnh (Keyframe Image) thành prompt diễn hoạt (Animation Prompt) ngắn gọn, chính xác, **chuyển động mượt mà, êm ái, không giật cục**, và triệt tiêu 100% hiện tượng biến dạng (morphing).

---

## 1. NGUYÊN TẮC BẮT BUỘC: CHỈ ĐẠO VECTOR CHUYỂN ĐỘNG (KHÔNG TẢ LẠI ẢNH)

1. **Ảnh (Keyframe) đã quyết định 100% phần nhìn:**
   - Model AI Video (I2V) đã nhìn thấy toàn bộ nhân vật, trang phục, gương mặt, màu sắc, ánh sáng và bối cảnh.
   - **Tuyệt đối cấm tả lại bối cảnh hay quần áo:** Không viết những câu thừa thãi như *"The grandfather in worn tweed coat on the wooden porch"*. Việc nhồi lại từ ngữ miêu tả tĩnh sẽ làm AI bị xung đột ngữ nghĩa, dẫn đến lỗi biến dạng (morphing) hoặc đè nát chất liệu của ảnh gốc.
2. **Nhiệm vụ duy nhất của Prompt Animation:**
   - Chỉ đạo **hướng chuyển động (motion vectors)** và **tốc độ thay đổi** trong 5–8 giây.
   - Tập trung vào **động từ hành động** và **cú máy điện ảnh**.

---

## 2. TIÊU CHUẨN MƯỢT MÀ, KHÔNG GIẬT CỤC (SMOOTH & FLUID DYNAMICS)

- **Chuyển động mượt mà (Fluid & Continuous):** Dù bối cảnh là thế giới sa bàn thủ công, tả thực hay hoạt họa, chuyển động trong video phải giữ được độ mượt mà điện ảnh, không giật khựng (no stutter, no jitter, no frame drops).
- **Vận tốc êm ái (Ease-in / Ease-out):** Mọi chuyển động của máy quay hay nhân vật đều có gia tốc tự nhiên, chuyển động từ tốn, không đổi hướng đột ngột.
- **Biên độ vi mô (Micro-amplitude):** Biên độ chuyển động nhỏ và tinh tế luôn mang lại chất lượng render video cao nhất.

---

## 3. CÔNG THỨC CHUYỂN ĐỘNG 3+1 (THE 3+1 MOTION FORMULA)

Mỗi prompt animation bắt buộc được cấu trúc tinh gọn theo đúng 4 thành phần kỹ thuật:

```text
[1. Cú máy Camera mượt] + [2. Hành động Chủ thể] + [3. Vật lý Môi trường] + [4. Khóa kỹ thuật an toàn]
```

### Chi tiết 4 thành phần:

| Thành phần | Ý nghĩa kỹ thuật | Ví dụ thực tế |
|---|---|---|
| **1. Camera Motion** | Hướng di chuyển và tiêu cự của máy quay (luôn êm ái, có ray trượt). | `Slow smooth cinematic slider drift...`, `gentle continuous dolly-in...`, `static locked-off camera...` |
| **2. Subject Motion** | Hành động vi mô duy nhất của nhân vật hoặc vật thể chính. | `The swing arcs smoothly forward and back; small boots kick gently upward.` / `The artisan smoothly rotates the carved wooden bowl with steady hands.` |
| **3. Environmental Physics** | Chuyển động của các hạt vật lý trong môi trường (gió, lá, nước, khói, lửa). | `Autumn leaves drift gently across the foreground; water ripples softly in the current.` / `Sparks spray smoothly from the glowing anvil.` |
| **4. Technical Guardrails** | Khóa an toàn chặn AI tự ý cắt cảnh, giật lag, sinh chữ hoặc biến dạng. | `Single continuous shot, smooth fluid motion, no cuts, no stutter, no morphing, no text, no watermark.` |

---

## 4. TỪ ĐIỂN CÚ MÁY VÀ ĐỘNG TỪ CHUẨN HÓA

### A. Bộ cú máy Camera mượt mà (Camera Moves):
- **Trượt ngang êm ái (Slider/Dolly):** `Slow smooth horizontal camera drift past foreground [element], maintaining steady focus on [subject]...`
- **Tiến chậm mượt mà (Dolly-in):** `Slow continuous cinematic dolly-in shot toward [subject], smooth fluid motion...`
- **Góc ngước lướt nhẹ (Low-angle tracking):** `Low-angle smooth tracking shot moving gently alongside [subject]...`
- **Góc cao bao quát (High-angle drift):** `High-angle slow sweeping drift looking down across [setting]...`
- **Máy tĩnh lấy nét sâu (Static Macro):** `Static locked-off macro camera with shallow depth of field, steady focus...`

### B. Động từ diễn hoạt mượt (Smooth Action Verbs):
- **Cơ thể & Búp bê:** `smoothly sways`, `gently turns head`, `steadily guides hands`, `softly leans forward`, `fluidly pedals`.
- **Muông thú sa bàn:** `smoothly cocks head with curious curiosity`, `gently twitches tail`, `smoothly glides through calm water`.
- **Môi trường & Đạo cụ:** `drift lazily`, `ripple smoothly`, `flutter softly in the breeze`, `steam rises steadily`, `sparks spray fluidly`.

---

## 5. BẢNG TRA CỨU CÁC LỖI GÂY NÁT VIDEO (FAILURE MODES)

| ❌ Lỗi Cấm Kỵ (Failure Trigger) | Hậu Quả Kỹ Thuật |  Giải Pháp Kỹ Thuật Thay Thế |
|---|---|---|
| **Tả lại quần áo/mặt mũi** (*"An old man in wool tweed..."*) | AI vẽ lại chi tiết $\rightarrow$ nát hình, lệch ảnh gốc | **Bỏ hoàn toàn tả hình thức.** Chỉ gọi tên: `The man...`, `The artisan...`, `The sparrow...` |
| **Hành động chuỗi liên hoàn** (*"Đứng lên, bước ra cửa, mở cửa"*) | Đứt gãy khung hình, tay chân dính vào cửa | **Chỉ 1 hành động liên tục duy nhất** trong suốt 5 giây. |
| **Đổi tư thế cơ thể đột ngột** (*Đang ngồi đứng phắt dậy*) | Biến dạng cơ thể, mọc thừa chi, méo cột sống | Giữ nguyên tư thế gốc: `maintains seated posture throughout the shot`. |
| **Dùng từ mơ hồ** (*"zoom in", "speed up"*) | Crop số vỡ hạt pixel, giật khung hình | Dùng: `slow smooth continuous dolly-in`, `steady fluid tracking`. |
| **Thiếu câu lệnh kỹ thuật** | AI tự nhảy cảnh, chèn chữ nhảm, méo mặt | Luôn kết thúc bằng: `Single continuous shot, smooth fluid motion, no cuts, no stutter, no morphing, no text, no watermark.` |

---

## 6. KHUNG MẪU THỰC CHIẾN (PRODUCTION PROMPT TEMPLATES)

### Mẫu 1: Cảnh Xích đu / Hành động bay bổng (Swing / Dynamic Action)
```text
Slow smooth low-angle camera drift. The wooden swing arcs fluidly forward and back in a graceful pendulum motion, leather boots kicking gently upward toward the golden tree canopy. Autumn leaves swirl smoothly in the trailing air. Single continuous shot, smooth fluid motion, no cuts, no stutter, no morphing, no text, no watermark.
```

### Mẫu 2: Cảnh Nghệ nhân thao tác / Đời sống (Artisan / Craft Action)
```text
Slow smooth macro slider shot. The blacksmith steadily brings the hammer down onto the glowing anvil with rhythmic precision, bright orange sparks spraying fluidly outward. Thin curls of forge smoke drift steadily upward into the rafters. Single continuous shot, smooth fluid motion, no cuts, no stutter, no morphing, no text, no watermark.
```

### Mẫu 3: Cảnh Muông thú sa bàn (Wildlife / Nature Action)
```text
Smooth static macro shot with shallow depth of field. The whittled cedar sparrow smoothly tilts its head with alert, curious micro-movements on the weathered fence post. Autumn breeze softly ripples through the dry grass below. Single continuous shot, smooth fluid motion, no cuts, no stutter, no morphing, no text, no watermark.
```

### Mẫu 4: Cảnh Tĩnh vật / Cảm xúc buông lắng (Contemplative / Still-life)
```text
Slow gentle camera drift across the scene. The empty wooden swing sways very slowly in the faint autumn breeze. Warm lantern light flickers softly against the ancient oak bark as distant twilight mist rolls lazily across the lawn. Single continuous shot, smooth fluid motion, no cuts, no stutter, no morphing, no text, no watermark.
```

---

## 7. QUY CHUẨN LƯU TRỮ VÀ TÍCH HỢP PIPELINE

1. **Ưu tiên tích hợp trực tiếp vào JSON:**
   Mỗi prompt trong `projects/<id>/<track>/image.json` sẽ chứa trực tiếp trường `"ANIMATION"`:
   ```json
   {
     "id": 4,
     "STYLE": { ... },
     "ENVIRONMENT": { ... },
     "ANIMATION": {
       "prompt": "Slow smooth low-angle camera drift. The wooden swing arcs fluidly forward and back in a graceful pendulum motion, leather boots kicking gently upward toward the golden tree canopy. Autumn leaves swirl smoothly in the trailing air. Single continuous shot, smooth fluid motion, no cuts, no stutter, no morphing, no text, no watermark."
     }
   }
   ```
2. **Khả năng trích xuất linh hoạt (CLI Ready):**
   Khi cần nạp vào tool render hàng loạt (như Kling API, ComfyUI, Runway batch), chỉ cần dùng 1 lệnh `jq` để xuất ra danh sách:
   ```bash
   jq -r '.[] | "\(.id). \(.ANIMATION.prompt)"' image.json > prompt-animate.txt
   ```
