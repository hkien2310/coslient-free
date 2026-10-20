# NOTE 20/10: Đúc Kết R&D Cải Tiến Cấu Trúc Prompt Ảnh Stop-Motion (`Ponytail` 4-Block Formula)

> **Ngày ghi nhận:** 20/10/2026
> **Mục đích:** Lưu trữ toàn bộ kết quả thử nghiệm thực tế, nguyên nhân lỗi của cấu trúc prompt cũ (210–250 từ) và cấu trúc **Prompt 4 Khối Tối Giản (~50–60 từ)** đang phát triển để không bao giờ mất dữ liệu khi compact context.

---

## 1. Giải Phẫu Lịch Sử 5 Lần Test & Nguyên Nhân Gốc Rễ Của Từng Lỗi

### Lần Test 1 — Prompt cũ 220 từ (`STYLE_mixed_media_tabletop_diorama.md` hiện hành + Use Case tạo dáng)
- **Hiện tượng lỗi:**
  1. Nhân vật trông giống **người thật / tượng sáp người mẫu (`1:7.5 human proportions`)**, thiếu nét cách điệu duyên dáng của các kênh đối thủ (*Walter AI Art*, *Walter's Puppet Box*, *Three-Quarter Town*, *Oltsev Art*).
  2. Hành động trong ảnh **vô nghĩa và phi thực tế**: ông cụ ngồi một mình vẩy khăn ướt ra không trung, bà cụ đứng ở khung cửa sổ mọc trơ trọi trên vách đá rót nước sôi, hai ông bà dắt xe đạp leo bậc đá gập ghềnh, ông thợ bánh cúi cầm cái ghế lùn tịt trước bao bột mì ngoài sân, đôi giày bỏ lại sát mép nước.
- **Nguyên nhân gốc rễ:**
  1. **Quá tải kiểm soát giải phẫu (110–120 từ tả người / 15 từ tả hành động):** Khi 85% câu prompt là giải phẫu mặt mũi, mí mắt, chân tóc và thông số màu `70%-20%-10%`, AI hiểu đây là lệnh chụp chân dung người mẫu (`Portrait`) nên kéo nhân vật đứng đơ tạo dáng và làm hỏng logic vật lý của hành động.
  2. **Tỷ lệ `1:7.5` là tỷ lệ giải phẫu người thật:** Càng khóa `1:7.5 human proportions` + `smooth nose, smaller eyes, even skin tone`, nhân vật càng trượt về người thật.
  3. **Danh sách Use Case tạo dáng trong `visual_craft.md`:** Các cụm *ngả lưng, co một chân, tháo giày, mở cúc áo, vung khăn* biến nhân vật thành người mẫu đứng diễn (`posing`) thay vì làm việc thực tế.

### Lần Test 2 — Cắt ngắn phần tả người nhưng gộp chung danh từ số nhiều (`two tall 1:7.5 men with softly rounded mature faces and snow-white hair`)
- **Hiện tượng lỗi:** Hành động đã có ý nghĩa thực tế, nhưng 2 nhân vật trong cùng bức ảnh bị **Hội chứng Sinh Đôi (`Twin Cloning`)** — mặt mũi và dáng người giống hệt nhau như hai giọt nước.
- **Nguyên nhân gốc rễ:** Dùng chung một cụm mô tả ngoại hình (`oval face + snow-white hair + tall slender`) cho nhiều nhân vật khiến AI lấy đúng 1 khuôn mẫu nhân bản ra làm hai.

### Lần Test 3 — Bỏ hết chất liệu rối, chỉ dùng danh từ nghề nghiệp đời thực (`retired schoolteacher`, `harbor captain`)
- **Hiện tượng lỗi:** Nhân vật khác mặt nhau hoàn toàn, nhưng **sa hẳn vào người thật**, mất chất hoạt hình Stop-Motion cách điệu của đối thủ.
- **Nguyên nhân gốc rễ:** Các danh từ nghề nghiệp đời thực khi không đi kèm chất liệu `felt-and-clay stop-motion` sẽ kéo AI về kho dữ liệu ảnh chụp người thật.

### Lần Test 4 — Ép từ khóa `puppet` + `spindly-limbed` + `clay-and-felt skin` + đối cực gắt (`tall lanky` vs `short stout plump`)
- **Hiện tượng lỗi:** Ra chất cách điệu nhưng bị **dị dạng / kinh dị**:
  1. Lộ khớp cầu gỗ, tay chân que củi như bộ xương khô (*Tim Burton / Corpse Bride*) và lộ vết chỉ khâu rách trên má.
  2. Màu da xám ngoét như đất sét xi măng chết chóc (`clay-and-felt skin` thiếu khóa màu ấm).
  3. Lệch kích thước thành **"Người khổng lồ 2m & Chú lùn 60cm"** do ép đối cực hình thể quá đà trong một câu prompt dài.

### Lần Test 5 — Cởi trói khỏi bệnh "Nghiện Kiểm Soát" (`Over-controlling`): Cấu trúc 4 Khối Tối Giản (~55 từ)
- **Triết lý cốt lõi:** Ngừng kiểm soát tiểu tiết ở mọi khối. Để cụm đầu câu (`Handcrafted felt-and-clay stop-motion animation film still, warm Kodak 35mm color grading`) tự động xử lý độ cách điệu thủ công của thế giới và nhân vật; dành 50% dung lượng câu prompt cho **Tương tác Nhân – Quả thực tế giữa các nhân vật**.

---

## 2. Cấu Trúc Prompt 4 Khối Tối Giản (`~50–60 từ/câu`)

```text
[KHỐI 1: Chất liệu Thế giới & Màu phim (9 từ)]
Handcrafted felt-and-clay stop-motion animation film still, warm Kodak 35mm color grading.

[KHỐI 2: Cỡ cảnh + Góc máy + Bối cảnh (10–14 từ)]
[Wide low-angle shot / Medium waist-up shot / Extreme wide high-angle panoramic shot / Close-up shot] on a [địa điểm cụ thể khớp với công năng hoạt động + hậu cảnh].

[KHỐI 3: Chủ thể (Dáng + 1 nét nhận diện đối lập) & Hoạt động Tương tác Thực (25–30 từ)]
A [vóc dáng + độ tuổi + 1 đặc điểm râu/tóc/kính + áo] [hành động thực tế có mục đích] with/to [nhân vật thứ 2 có vóc dáng & phụ kiện khác biệt + hành động phản hồi].

[KHỐI 4: Ánh sáng & Tiêu cự khóa đuôi (8–10 từ)]
[Soft morning / Warm afternoon / Golden sunset / Twilight] light, [crisp 35mm focus | shallow 50mm bokeh], no text --ar 16:9
```

---

## 3. Bảng Phân Định: Những Gì Kiểm Soát vs Những Gì Bỏ Kiểm Soát

| Khối | GIỮ KIỂM SOÁT (Đòn bẩy cốt lõi) | BỎ KIỂM SOÁT (Tránh làm AI ngộp token & cứng đơ) |
| :--- | :--- | :--- |
| **Khối 1: Chất liệu & Màu phim** | - `Handcrafted felt-and-clay stop-motion animation film still`<br>- `warm Kodak 35mm color grading` | - Bỏ các từ lý thuyết thừa: `European arthouse`, `crystal-clear air`, `lived-in timeless patina`, `sfumato soft edges`. |
| **Khối 2: Máy quay & Bối cảnh** | - **Cỡ cảnh & Góc máy** (`Wide low-angle`, `Medium waist-up`, `Extreme wide high-angle`, `Close-up`) để giữ nhịp dựng phim.<br>- **Bối cảnh đời thực đúng công năng**. | - Bỏ văn mẫu rườm rà: `Spacious ... with generous open scenic space on an expansive open-air weathered...` |
| **Khối 3: Nhân vật & Hành động** | - **1 tính từ vóc dáng + 1 phụ kiện/râu tóc khác nhau** cho mỗi nhân vật để chống sinh đôi.<br>- **Hoạt động & Tương tác Nhân – Quả thực tế** (Ai đang làm việc gì, trao/nhận/giao tiếp như thế nào với ai). | - Bỏ đo đạc giải phẫu chi tiết (`1:7.5`, `oval face`, `curved jawline`, `nose bridge`, `upper eyelids`, `natural hairline`, `paper-pulp skin`).<br>- Bỏ từ `puppet` + `spindly-limbed` (tránh lộ khớp xương que củi).<br>- Bỏ bắt buộc gắn `charcoal-black and saffron-yellow accent` ở mọi câu. |
| **Khối 4: Ánh sáng & Tiêu cự** | - **Thời điểm ánh sáng** (`Soft morning sunlight`, `Golden sunset`, `Warm twilight`).<br>- **Tiêu cự theo cỡ cảnh:** `crisp 35mm focus` (cảnh rộng) vs `shallow 50mm bokeh` (cảnh trung/cận). | - Bỏ công thức chia phần trăm màu cứng nhắc `casting a single coherent shadow direction across a mineral palette of 70%..., 20%..., and 10%...`. |

---

## 4. Lưu Trữ 5 Prompt Mẫu (`Shots 01–05` — Bản 4 Khối ~55 từ)

```text
Handcrafted felt-and-clay stop-motion animation film still, warm Kodak 35mm color grading. Wide low-angle shot on a coastal cliff path overlooking the deep blue sea. A tall slender old man in a blue linen jacket wipes morning dew off a wooden bench with a cloth and waves to his friend, a shorter stout old man with a white beard, flat cap, and walking stick walking up the path toward the seat. Soft morning sunlight, crisp 35mm focus, no text --ar 16:9

Handcrafted felt-and-clay stop-motion animation film still, warm Kodak 35mm color grading. Medium waist-up shot on a stone cottage porch overlooking a softly blurred blue bay. A petite older woman in round glasses and a sage-green knitted cardigan pours steaming coffee from a blue kettle into a ceramic mug held out by a tall older man with a white mustache sitting on the porch bench. Warm morning sunlight, shallow 50mm bokeh, no text --ar 16:9

Handcrafted felt-and-clay stop-motion animation film still, warm Kodak 35mm color grading. Extreme wide high-angle panoramic shot on a green coastal hilltop with a dirt lane and a lone pine tree overlooking a wide bay. A bearded old fisherman in a yellow coat and navy beanie parks his vintage bicycle and holds the hand of his petite wife in a blue scarf, leading her across the grass toward a wooden bench under the pine tree. Warm morning sunlight, crisp 35mm focus, no text --ar 16:9

Handcrafted felt-and-clay stop-motion animation film still, warm Kodak 35mm color grading. Medium-wide side-profile shot on a stone harbor cafe terrace overlooking the sparkling sea. A tall curly-haired cafe host in a linen apron arranges two wooden chairs at a round table while a plump cheerful woman with braided brown hair sets a steaming terracotta teapot and cups on the tabletop. Soft morning sunlight, crisp 35mm focus, no text --ar 16:9

Handcrafted felt-and-clay stop-motion animation film still, warm Kodak 35mm color grading. Medium waist-up shot on a stone lookout terrace with white sailboats on the softly blurred blue bay behind them. Two contrasting old friends sit side by side on a wooden bench: a lanky man in a navy beanie and ochre sweater points toward a passing sailboat while his round-cheeked friend in glasses and a blue cardigan looks through binoculars. Soft morning sunlight, shallow 50mm bokeh, no text --ar 16:9
```
