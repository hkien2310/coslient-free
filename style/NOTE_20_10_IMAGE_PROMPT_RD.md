# NOTE 20/10: Đúc Kết R&D Cải Tiến Cấu Trúc Prompt Ảnh Stop-Motion (`Ponytail` 4-Block & 7-Axis Formula)

> **Ngày ghi nhận & chốt chuẩn:** 20/10/2026 (Bản hoàn thiện sau 8 vòng R&D thực nghiệm)
> **Mục đích:** Lưu trữ toàn bộ lịch sử thử nghiệm 8 vòng, nguyên nhân gốc rễ của từng lỗi và công thức **Prompt 4 Khối + Nén 7 Trục Đa Dạng Nhân Vật** đã chốt để đồng bộ vào hệ thống tài liệu (`STYLE`, `visual_craft`, `retention_review`).

---

## 1. Tóm Tắt 8 Vòng R&D Thực Nghiệm & Nguyên Nhân Kỹ Thuật

1. **Vòng 1 — Prompt cũ 220 từ (`1:7.5` + 120 từ giải phẫu + `70%-20%-10%` + Use Case tạo dáng):**
   - *Lỗi:* Nhân vật giống người thật (`1:7.5`), đứng tạo dáng vô nghĩa (*vẩy khăn ra không trung, đứng ở cửa sổ trơ trọi rót nước, dắt xe đạp leo bậc đá*).
   - *Nguyên nhân:* 120 từ tả mặt mũi nuốt chửng 15 từ tả hành động; tỷ lệ `1:7.5` là giải phẫu người thật; Use Case tạo dáng trong `visual_craft.md` biến nhân vật thành người mẫu đứng diễn.
2. **Vòng 2 — Rút gọn ngoại hình nhưng dùng danh từ số nhiều chung (`two tall 1:7.5 men with oval faces and white hair`):**
   - *Lỗi:* **Hội chứng Sinh Đôi (`Twin Cloning`)** — 2 nhân vật giống hệt nhau.
3. **Vòng 3 — Bỏ chất liệu rối, dùng danh từ nghề nghiệp (`schoolteacher`, `captain`):**
   - *Lỗi:* Khác mặt nhưng **sa hẳn vào người thật**, mất chất cách điệu.
4. **Vòng 4 — Dùng `puppet` + `spindly-limbed` + `clay-and-felt skin` + đối cực gắt (`tall lanky` vs `short stout plump`):**
   - *Lỗi:* Lộ khớp cầu xương que củi và vết chỉ khâu kinh dị kiểu *Tim Burton*, da xám xi măng, lệch kích thước thành "Người khổng lồ & Chú lùn".
5. **Vòng 5 — Rút gọn 4 khối nhưng để `felt-and-clay` ở đầu câu + viết `old man` + `shorter stout / plump`:**
   - *Lỗi:* Chữ `felt` + `cardigan/sweater/beanie` làm nhân vật mặc **đồ len sợi to**; chữ `old man` không khóa tóc làm **hói đỉnh đầu**; chữ `shorter stout / plump` làm nhân vật thứ 2 biến thành **chú lùn / em bé mập**.
6. **Vòng 6 & 7 — Dùng chữ `clay` (`sculpted-clay` hoặc `matte sculpted clay skin`):**
   - *Lỗi:* Hễ có chữ **`clay`** đi cùng `stop-motion`, AI kích hoạt chế độ *Claymation* khiến **đất sét lem lên cả tóc và râu (tóc vón cục đất sét)**.
7. **Vòng 7B — Xóa `clay` nhưng lại viết chữ `realistic` 2 lần (`realistic natural landscape` + `realistic fine wispy hair`) và bỏ tỷ lệ đầu cách điệu:**
   - *Lỗi:* Chữ **`realistic`** kích hoạt bộ lọc *Photorealism*, kéo nhân vật trở lại gần với **người thật**.
8. **Vòng 8 & 9 (BẢN CHỐT THÀNH CÔNG) — Điểm ngọt Cách điệu Stop-Motion + Tóc sợi tơ + Môi trường tự nhiên + Trang phục vải dệt đời thường dài tay:**
   - **Bỏ hoàn toàn cả 3 cụm từ gây nhiễu:** Không dùng `Kodak 35mm color grading` (tránh ám vàng thừa), không dùng chữ `clay` (tránh vón đất sét lên tóc), không dùng chữ `realistic` (tránh kéo nhân vật về người thật).
   - **Bài học trang phục Vòng 9:** Không ép nhân vật mặc vest lịch thiệp cứng nhắc (`blazer, double-breasted coat, bow tie, cravat`) vì làm mất chất tự nhiên đời thường; ngược lại không dùng áo xắn tay (`rolled-sleeve`) vì làm lộ khớp khuỷu tay rối gỗ. Giải pháp tối ưu là **trang phục vải dệt đời thường dài tay hoặc phối nhẹ 2 lớp đời thường** (`long-sleeved linen shirt-jacket`, `canvas coat over a cotton shirt`, `long-sleeved cotton shirt and corduroy vest`, `long-sleeved chambray shirt and canvas apron`).
   - **Khóa công thức Điểm Ngọt:**
     - **Khối 1 & 2 (Môi trường & Đồ dùng tự nhiên):** `Cinematic handcrafted stop-motion animation still on a natural [bối cảnh] with real [wood, stone, ceramic, water, and plants]...`
     - **Khối 3A (Chất liệu & Tỷ lệ Cách điệu chung):** `Whimsical stylized stop-motion characters of matching/balanced adult height with slightly oversized expressive heads, smooth warm hand-molded matte paper-pulp skin, thick full soft fibrous hair strands, and long-sleeved woven fabric clothing:`
     - **Khối 3B (Nén 7 Trục Đa dạng Nhân vật bằng từ ghép 1–2 từ + Hoạt động tương tác thực tế).**
     - **Khối 4 (Ánh sáng tự nhiên & Khóa đuôi):** `[Soft morning / Warm afternoon / Golden sunset] sunlight, no text --ar 16:9`

---

## 2. Ma Trận Nén 7 Trục Đa Dạng Nhân Vật (`15–18 từ/nhân vật`)

```text
a [1. Dáng (1-2 từ)], [2. Khối mặt (1-2 từ)], [3. Nét đặc trưng (1-2 từ)] [man/woman] with [4. Thần thái mắt/mày (2 từ)], [5. Râu/Kính/Mũ (2-4 từ)], and [6. Tóc sợi dày theo tuổi (4-5 từ)] in a [7. Trang phục vải dệt đời thường dài tay (4-6 từ)]
```

| Trục (1–2 từ/trục) | Kho từ khóa xoay vòng (Tạo hàng nghìn tổ hợp độc bản, không bao giờ sinh đôi) |
| :--- | :--- |
| **1. Khung người lớn (`Frame`)** | `lean-framed` · `broad-shouldered` · `sturdy` · `tall poised` · `graceful` *(luôn giữ `matching / balanced adult height` giữa các người lớn; trẻ em dùng `waist-high child reaching the adult's waist`)* |
| **2. Khối mặt (`Face Shape`)** | `long-faced` · `square-jawed` · `round-cheeked` · `oval-faced` · `high-cheekboned` |
| **3. Ngũ quan (`Feature`)** | `prominent-nosed` · `button-nosed` · `bushy-browed` · `dimpled` · `freckled` |
| **4. Ánh mắt (`Gaze`)** | `kind-eyed` · `twinkling-eyed` · `calm-eyed` · `bright-eyed` · `warm-eyed` |
| **5. Râu / Kính / Mũ (`Detail`)** | `clean-shaven` · `soft white mustache` · `neat trimmed beard` · `full soft beard` · `round wire spectacles` · `tortoiseshell glasses` · `cotton flat cap` · `canvas cap` · `corduroy cap` · `cotton sunhat` |
| **6. Tóc sợi dày (`Fibrous Hair`)** | `full head of swept-back silver hair strands` · `thick curly chestnut hair strands` · `thick braided dark-brown hair strands` · `thick tousled salt-and-pepper hair strands` · `thick high bun of silver-streaked auburn hair strands` · `thick flowing wavy white hair strands` |
| **7. Áo vải dệt đời thường dài tay (`Casual Long-Sleeved Woven Attire`)** | `long-sleeved blue linen shirt-jacket and suspenders` · `ochre canvas coat over a cotton shirt` · `sage-green linen shirt-jacket and cotton neck scarf` · `long-sleeved cream cotton shirt and brown corduroy vest` · `long-sleeved chambray shirt and canvas apron` · `long-sleeved terracotta cotton dress and linen vest` |

---

## 3. Lưu Trữ 5 Prompt Chuẩn Hóa (`Shots 01–05` — Bản Chốt Đời Thường Dài Tay)

```text
Cinematic handcrafted stop-motion animation still on a natural coastal cliff path with real weathered wood, stone, and plants overlooking the deep blue sea. Wide low-angle shot. Whimsical stylized stop-motion characters of matching adult height with slightly oversized expressive heads, smooth warm hand-molded matte paper-pulp skin, thick full soft fibrous hair strands, and long-sleeved woven fabric clothing: a lean-framed, long-faced, prominent-nosed man with kind eyes, clean-shaven cheeks, and a full head of swept-back silver hair strands in a long-sleeved blue linen shirt-jacket and suspenders wipes morning dew off a wooden bench with a cloth and waves to his friend, a broad-shouldered, square-jawed, bushy-browed man with twinkling eyes, a full soft white beard, and a cotton flat cap in an ochre canvas coat over a cotton shirt walking up the stone path with a wooden stick. Soft morning sunlight, no text --ar 16:9

Cinematic handcrafted stop-motion animation still on a natural stone cottage porch with real stone, ceramic, and foliage overlooking a softly blurred blue bay. Medium waist-up shot. Whimsical stylized stop-motion characters with slightly oversized expressive heads, smooth warm hand-molded matte paper-pulp skin, thick full soft fibrous hair strands, and long-sleeved woven fabric clothing: a graceful, oval-faced, dimpled woman with warm eyes, round wire spectacles, and a thick high bun of silver-streaked auburn hair strands in a sage-green linen shirt-jacket and cotton neck scarf pours steaming coffee from a blue enameled kettle into a ceramic mug held out by a sturdy, round-cheeked, button-nosed man with calm eyes, a soft white mustache, and a full head of side-parted silver hair strands in a long-sleeved cream cotton shirt and brown corduroy vest sitting on the wooden porch bench. Warm morning sunlight, no text --ar 16:9

Cinematic handcrafted stop-motion animation still on a natural green coastal hilltop with real grass, a dirt lane, and a lone pine tree overlooking a wide bay. Extreme wide high-angle panoramic shot. Whimsical stylized stop-motion characters of balanced adult height with slightly oversized expressive heads, smooth warm hand-molded matte paper-pulp skin, thick full soft fibrous hair strands, and long-sleeved woven fabric clothing: a broad-shouldered, square-jawed, full-bearded fisherman with thick tousled salt-and-pepper hair strands under a canvas cap and a yellow cotton jacket parks his vintage metal bicycle and holds the hand of his tall poised, high-cheekboned wife with bright eyes and thick flowing wavy white hair strands in a long-sleeved slate-blue linen coat and cotton sunhat, leading her across the grass toward a wooden bench under the pine tree. Warm morning sunlight, no text --ar 16:9

Cinematic handcrafted stop-motion animation still on a natural stone harbor cafe terrace with real wooden furniture, ceramic, and sparkling sea water. Medium-wide side-profile shot. Whimsical stylized stop-motion characters of matching adult height with slightly oversized expressive heads, smooth warm hand-molded matte paper-pulp skin, thick full soft fibrous hair strands, and long-sleeved woven fabric clothing: a lean-framed, long-faced, prominent-nosed cafe host with bright eyes, a neat trimmed beard, and a full head of curly chestnut hair strands in a long-sleeved chambray shirt and canvas apron arranges two wooden chairs at a round table, while a graceful, oval-faced, button-nosed woman with kind eyes and thick braided dark-brown hair strands in a long-sleeved terracotta cotton dress and linen vest sets a steaming ceramic teapot and cups on the wooden tabletop. Soft morning sunlight, no text --ar 16:9

Cinematic handcrafted stop-motion animation still on a natural coastal stone lookout terrace with white sailboats on the softly blurred blue bay behind them. Medium waist-up shot. Two contrasting whimsical stylized stop-motion friends with slightly oversized expressive heads, smooth warm hand-molded matte paper-pulp skin, thick full soft fibrous hair strands, and long-sleeved woven fabric clothing sit side by side on a weathered wooden bench: on the left, a lean-framed, long-faced, prominent-nosed man with bushy brows, a drooping white mustache, and thick wavy silver hair strands under a navy corduroy cap in a long-sleeved ochre linen overshirt points toward a passing sailboat, while beside him a broad-shouldered, round-cheeked, button-nosed man with twinkling eyes, tortoiseshell glasses, and a full head of tousled white hair strands in a long-sleeved slate-blue cotton jacket looks through matte-black binoculars. Soft morning sunlight, no text --ar 16:9
```
