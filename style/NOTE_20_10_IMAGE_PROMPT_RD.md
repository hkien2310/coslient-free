# NOTE 20/10: Đúc Kết R&D Cải Tiến Cấu Trúc Prompt Ảnh Stop-Motion (`Ponytail` 4-Block Formula)

> **Ngày ghi nhận & cập nhật:** 20/10/2026 (Bản nâng cấp chuẩn hóa Tách biệt Chất liệu & Đa dạng Nhân vật)
> **Mục đích:** Lưu trữ toàn bộ kết quả thử nghiệm thực tế qua 7 vòng R&D, nguyên nhân gốc rễ của từng lỗi và công thức **Prompt 4 Khối Tách Bạch Chất Liệu** đã test thành công để không mất dữ liệu khi compact context.

---

## 1. Giải Phẫu Lịch Sử 7 Vòng Test & Nguyên Nhân Gốc Rễ Của Từng Lỗi

1. **Vòng 1 — Prompt cũ 220 từ (`STYLE_mixed_media_tabletop_diorama.md` cũ + Use Case tạo dáng):**
   - *Lỗi:* Nhân vật trông như người thật (`1:7.5 human proportions`), đứng tạo dáng vô nghĩa (*vẩy khăn ra không trung, đứng ở cửa sổ trơ trọi rót nước, dắt xe đạp leo bậc đá*).
   - *Nguyên nhân:* 120 từ tả giải phẫu mặt mũi nuốt chửng 15 từ tả hành động; tỷ lệ `1:7.5` là tỷ lệ người thật; danh sách Use Case tạo dáng trong `visual_craft.md` biến nhân vật thành người mẫu chụp ảnh.
2. **Vòng 2 — Cắt ngắn ngoại hình nhưng gộp danh từ số nhiều (`two tall 1:7.5 men with oval faces and white hair`):**
   - *Lỗi:* **Hội chứng Sinh Đôi (`Twin Cloning`)** — 2 nhân vật giống hệt nhau như đúc.
   - *Nguyên nhân:* Dùng chung một cụm tính từ ngoại hình cho số nhiều khiến AI nhân bản cùng 1 khuôn mặt.
3. **Vòng 3 — Bỏ chất liệu stop-motion, chỉ dùng danh từ nghề nghiệp (`schoolteacher`, `captain`):**
   - *Lỗi:* Khác mặt nhưng **sa hẳn vào người thật**, mất chất cách điệu như đối thủ.
4. **Vòng 4 — Dùng từ `puppet` + `spindly-limbed` + `clay-and-felt skin` + đối cực gắt (`tall lanky` vs `short stout plump`):**
   - *Lỗi:* Lộ khớp cầu xương que củi và vết chỉ khâu kinh dị kiểu *Tim Burton*, da xám xi măng, lệch kích thước thành "Người khổng lồ & Chú lùn".
5. **Vòng 5 — Rút gọn 4 khối nhưng để `felt-and-clay` ở đầu câu + viết `old man` + `shorter stout / plump`:**
   - *Lỗi:*
     1. Chữ `felt` ở đầu câu + `cardigan/sweater/beanie` làm nhân vật mặc **đồ len sợi to (`chunky knitwear`)**.
     2. Chữ `old man` không khóa tóc làm nhân vật bị **hói đỉnh đầu (`balding dome`)**.
     3. Chữ `shorter stout / plump / petite` khi đặt cạnh `tall` làm nhân vật thứ 2 bị thu nhỏ thành **chú lùn hoặc em bé mập**.
     4. Điểm sáng: Nhân vật `tall curly-haired cafe host in a linen apron` đạt **10/10** (mặt đất sét cách điệu có hồn, tóc xoăn dày không hói, áo vải lanh không đồ len).
6. **Vòng 6 — Đổi đầu câu thành `Handcrafted sculpted-clay stop-motion`:**
   - *Lỗi:* Chữ `sculpted-clay` đặt ở Khối 1 (đầu câu) khiến **đất sét bị lem vào cả tóc (tóc vón cục đất sét) và môi trường**.
7. **Vòng 7 (BẢN THÀNH CÔNG) — Tách bạch chất liệu từng phần (Môi trường thật – Da đất sét – Tóc sợi – Áo vải thật):**
   - *Kết quả:* Môi trường, cây cỏ, mặt nước, bàn ghế gỗ, ấm chén giữ nguyên độ chân thực tự nhiên; chỉ có làn da nhân vật mang chất đất sét mờ cách điệu (`matte sculpted clay skin`), tóc và râu lên dạng sợi mảnh rõ đẹp (`thick full fine strand hair`), quần áo là vải dệt thật (`real woven fabric clothing`).

---

## 2. Quy Chuẩn Vàng Về Tách Bạch Chất Liệu & Tạo Hình Nhân Vật (Đúc Kết Từ Vòng 7)

### 2.1. Phân tách 4 lớp chất liệu độc lập (Chống lem đất sét & Chống đồ len)
1. **Môi trường, Cây cỏ & Đồ dùng = Như thật (`Realistic Natural Materials`):**
   - Khối 1 mở đầu bằng: `Cinematic stop-motion film still, warm Kodak 35mm color grading, realistic natural [landscape/environment], real wood, stone, and foliage textures.`
   - **Tuyệt đối không đặt chữ `clay` hay `felt` ở Khối 1** để bảo vệ cây cỏ, mặt nước, đồ dùng và mái tóc khỏi bị hóa đất sét hoặc hóa nỉ len.
2. **Da mặt & Tay nhân vật = Đất sét mờ cách điệu (`matte sculpted clay skin`):**
   - Chỉ gắn chữ `matte sculpted clay` trực tiếp vào danh từ `skin` của nhân vật (`Stylized stop-motion characters with matte sculpted clay skin`).
3. **Mái tóc & Râu = Dạng sợi mảnh, dày kín đầu, đa dạng kiểu (`thick full fine strand hair` — Không hói, Không vón đất sét):**
   - Luôn khóa cụm `thick full fine strand hair` (và `soft-strand beard/mustache`) để từng sợi tóc tách biệt, bồng bềnh tự nhiên và phủ kín đầu (không bao giờ viết `old man` trơ trọi gây hói đỉnh đầu).
4. **Trang phục = Vải dệt thật (`real woven fabric clothing` — 0% Đồ len):**
   - Chỉ dùng các chất liệu vải dệt phẳng và đứng phom: `woven linen`, `cotton`, `corduroy`, `canvas`, `chambray` (kết hợp mũ vải `cotton flat cap`, `canvas cap`, `corduroy cap`). Loại bỏ hoàn toàn `felt`, `wool`, `knitted`, `sweater`, `cardigan`, `beanie`.

### 2.2. Đa dạng Dáng người & Khuôn mặt ở Cùng Tỷ Lệ Người Lớn (`Adult Diversity without Dwarf/Child Distortion`)
- Giữ các nhân vật người lớn ở **cùng hệ chiều cao trưởng thành cân đối** (`matching adult height` / `balanced adult height`), tuyệt đối không dùng `shorter stout`, `plump`, `petite` cạnh người cao.
- Xoay vòng **Khung xương người lớn + Khối mặt điêu khắc + Kiểu tóc sợi** để mỗi nhân vật có diện mạo độc bản:
  - **Khung người (`Body Frame`):** `slender lean-framed` (thanh mảnh) $\leftrightarrow$ `broad-shouldered sturdy` (vai rộng vững chãi) $\leftrightarrow$ `graceful / tall poised` (đằm thắm cân đối).
  - **Khối mặt (`Face Shape`):** `long sculpted face` (mặt thon dài) $\leftrightarrow$ `broad square-jawed face` (mặt chữ điền) $\leftrightarrow$ `warm round face` (mặt tròn phúc hậu) $\leftrightarrow$ `soft oval face` (mặt trái xoan).
  - **Kiểu tóc sợi dày (`Hair Style`):** `wavy silver strand hair swept back` (lượn sóng vuốt ngược) $\leftrightarrow$ `curly chestnut/white hair strands` (xoăn bồng bềnh) $\leftrightarrow$ `tousled white hair strands` (bồng tự nhiên) $\leftrightarrow$ `braided hair strands` (tết bím) $\leftrightarrow$ `thick full bun of hair strands` (búi cao dày).

---

## 3. Khung Cấu Trúc Prompt 4 Khối Chuẩn Hóa (`~65–75 từ/câu`)

```text
[KHỐI 1: Môi trường & Đồ vật Thật + Màu phim Kodak 35mm]
Cinematic stop-motion film still, warm Kodak 35mm color grading, realistic natural [coastal landscape / stone architecture / meadow], real [wood, stone, ceramic, water, and foliage] textures.

[KHỐI 2: Cỡ cảnh + Góc máy + Bối cảnh thực tế]
[Wide low-angle shot / Medium waist-up shot / Extreme wide high-angle panoramic shot / Medium-wide side-profile shot / Close-up shot] on a [địa điểm cụ thể đúng công năng].

[KHỐI 3: Nhân vật (Da đất sét + Tóc sợi mảnh dày + Áo vải thật) & Hoạt động Tương tác Nhân – Quả]
Stylized stop-motion characters with matte sculpted clay skin, thick full fine strand hair, and real woven fabric clothing: [Nhân vật A: khung người lớn + khối mặt + kiểu tóc sợi dày + trang phục vải linen/cotton/corduroy/canvas + hành động thực tế có mục đích] with/to [Nhân vật B cùng tỷ lệ người lớn: khung người đối lập + khối mặt khác + kiểu tóc sợi/râu/kính/mũ vải + hành động tương tác đáp lại].

[KHỐI 4: Ánh sáng & Tiêu cự khóa đuôi]
[Soft morning / Warm afternoon / Golden sunset / Twilight] sunlight, [crisp 35mm focus | shallow 50mm bokeh], no text --ar 16:9
```

---

## 4. Lưu Trữ 5 Prompt Chuẩn Hóa (`Shots 01–05` — Bản Vòng 7 Đã Duyệt)

```text
Cinematic stop-motion film still, warm Kodak 35mm color grading, realistic natural coastal landscape, real wood, stone, and plant textures. Wide low-angle shot on a coastal cliff path overlooking the deep blue sea. Stylized stop-motion characters with matte sculpted clay skin, thick full fine strand hair, and real woven fabric clothing: a slender lean-framed man with a long sculpted face and thick full wavy silver strand hair swept back, wearing a slate-blue woven linen jacket and cotton trousers, wipes morning dew off a real weathered wooden bench with a cloth and waves to his friend of matching adult height, a broad-shouldered sturdy man with a square face, thick full white strand hair, a full soft-strand beard, and a cotton flat cap in an ochre canvas coat walking up the stone path with a wooden stick. Soft morning sunlight, crisp 35mm focus, no text --ar 16:9

Cinematic stop-motion film still, warm Kodak 35mm color grading, realistic natural stone architecture, real ceramic and foliage textures. Medium waist-up shot on a stone cottage porch overlooking a softly blurred blue bay. Stylized stop-motion characters with matte sculpted clay skin, thick full fine strand hair, and real woven fabric clothing: a graceful woman with a soft oval face, round wire glasses, and a thick full bun of fine silver-streaked auburn hair strands, wearing a sage-green woven linen shirt-jacket, pours steaming coffee from a blue enameled kettle into a real ceramic mug held out by a broad-shouldered man with a warm round face, thick full silver strand hair, and a soft white mustache in a cream cotton shirt and brown corduroy vest sitting on the wooden porch bench. Warm morning sunlight, shallow 50mm bokeh, no text --ar 16:9

Cinematic stop-motion film still, warm Kodak 35mm color grading, realistic natural coastal meadow, real grass, pine needles, and water textures. Extreme wide high-angle panoramic shot on a green coastal hilltop with a dirt lane and a lone pine tree overlooking a wide bay. Stylized stop-motion characters with matte sculpted clay skin, thick full fine strand hair, and real woven fabric clothing: a sturdy broad-shouldered fisherman with a full soft-strand white beard, thick silver strand hair under a canvas cap, and a yellow cotton jacket parks his vintage metal bicycle and holds the hand of his graceful wife of balanced adult height with thick flowing wavy white hair strands and a blue linen coat with a cotton scarf, leading her across the real grass toward a wooden bench under the pine tree. Warm morning sunlight, crisp 35mm focus, no text --ar 16:9

Cinematic stop-motion film still, warm Kodak 35mm color grading, realistic natural stone terrace, real wood furniture, ceramic, and sparkling sea water. Medium-wide side-profile shot on a stone harbor cafe terrace overlooking the sparkling sea. Stylized stop-motion characters with matte sculpted clay skin, thick full fine strand hair, and real woven fabric clothing: a slender lean-framed cafe host with a long sculpted face, a neat beard, and thick full curly chestnut hair strands in a rolled-sleeve blue linen shirt and canvas apron arranges two real wooden chairs at a round table, while a tall poised woman with a soft oval face and thick full braided dark-brown hair strands in a terracotta cotton dress sets a steaming ceramic teapot and cups on the wooden tabletop. Soft morning sunlight, crisp 35mm focus, no text --ar 16:9

Cinematic stop-motion film still, warm Kodak 35mm color grading, realistic natural coastal stone terrace and real ocean water. Medium waist-up shot on a stone lookout terrace with white sailboats on the softly blurred blue bay behind them. Two contrasting stylized stop-motion friends with matte sculpted clay skin, thick full fine strand hair, and real woven fabric clothing sit side by side on a real weathered wooden bench: on the left, a lean-framed man with a long sculpted face, a soft white mustache, and thick full wavy silver hair strands under a navy corduroy cap in an ochre linen overshirt points toward a passing sailboat, while beside him a broad-shouldered man with a round face, tortoiseshell glasses, and a thick full head of tousled white hair strands in a slate-blue cotton jacket looks through matte-black binoculars. Soft morning sunlight, shallow 50mm bokeh, no text --ar 16:9
```
