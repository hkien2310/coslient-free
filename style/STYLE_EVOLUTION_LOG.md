# Nhật Ký Tiến Hóa Phong Cách & Lịch Sử Tri Thức (Style Evolution Log)

Tài liệu ghi lại toàn bộ quá trình thử nghiệm thực tế (A/B testing), bài học thành công, nguyên nhân thất bại và các nguyên tắc đúc kết cho phong cách **Mixed-Media Tabletop Diorama**.

---

## [2026-10-13] — Cuộc Đại Nâng Cấp V2: Giải Phóng Ánh Sáng & Bẻ Gãy Khớp Bi

### 1. Bối cảnh & Điểm nghẽn ở Bản V1 (The Problem)
* **Triệu chứng:** Ảnh render từ bản V1 thường bị xám xịt, phẳng lì, thiếu chất thơ điện ảnh và nhân vật hay bị biến thành búp bê gỗ vô hồn với khớp nối ma-nơ-canh hoặc cọc gỗ ở chân.
* **Nguyên nhân gốc rễ đã mổ xẻ:**
  1. *Khóa cứng màu sắc:* Ép toàn dự án vào một dải màu `Charcoal and slate with saffron-mustard` làm mất đi tính biến thiên bối cảnh (thiếu hẳn chất Wes Anderson hay Vermeer).
  2. *Nỗi sợ CGI cực đoan:* Cấm tiệt các từ `glowing`, `luminous`, khiến AI không thể tạo ra nguồn sáng thực tế giấu trong mô hình (Practical Lights).
  3. *Từ khóa gây bẫy:* Cụm từ `carved wooden figurine` kết hợp việc để lộ cẳng tay/cổ tay kích hoạt bias của AI về búp bê rối gỗ (puppet/mannequin), khiến nó tự đục khớp bi tròn vào tay chân.

---

### 2. Thất bại đã kiểm chứng (Failures & Pitfalls)

| Hiện tượng lỗi | Nguyên nhân kỹ thuật | Hậu quả thị giác | Bài học / Cách khắc phục |
| :--- | :--- | :--- | :--- |
| **Khớp bi ở cổ tay & cùi chỏ** (Ảnh thợ đồng hồ hải đăng) | Dùng từ `carved wooden figurine` và mô tả xắn tay áo (`sleeves cuffed to wrists`). | Cổ tay bị đục một viên bi tròn như ma-nơ-canh vẽ tranh, làm mất cảm xúc nhân vật. | Tuyệt đối không cho xắn tay áo. Dùng tay áo dài vải thô trùm kín đến khớp cổ tay (`sleeves covering wrists`), dùng `smooth matte sculpted skin (seamless limbs)`. |
| **Cọc gỗ cắm vào giày** (Ảnh cô bé nghe đĩa than) | Quần áo ngắn để hở một khoảng mắt cá chân. | AI tiện một cọc gỗ tròn nối giữa chân và giày. | Quần hoặc váy vải may đo phải buông rủ dài phủ kín mu bàn chân (`trouser cuffs resting directly over shoes`). |
| **Mặt khô khốc như gỗ lũa** | Tả chi tiết nếp nhăn chạm khắc gỗ quá gắt (`carved wrinkles`, `knife-carved`, `faceted planar`). | Mặt nhân vật trông già nua, bị đẽo vát cạnh như tượng gỗ đục dở. | Chuyển sang tả bề mặt đất sét mờ mịn chuẩn studio (`smooth matte bisque-clay skin`), tuyệt đối không đánh má hồng (`rosy blush`). |
| **Hậu cảnh bị xóa phông mờ tịt** | Lạm dụng cụm từ `shallow depth of field` không kiểm soát. | Mất sạch chi tiết sa bàn ở phía sau, trông giống ảnh chân dung xóa phông rẻ tiền. | Dùng `deep miniature staging, readable layered background` hoặc bokeh có kiểm soát để giữ chiều sâu lớp lang diorama. |

---

### 3. Thành công đột phá (Breakthroughs & Wins)

#### Đột phá 1: Bông gòn thô đánh bại hoàn toàn 3D CGI (Case study: Xe buýt sa mạc muối)
* **Prompt:** `a dense fluffy cumulus cloud made of raw fibrous cotton, bound with knotted coarse hemp twine`.
* **Kết quả:** Đám mây hiện lên chân thực đến từng sợi tơ bông xù xì bắt nắng, được neo bằng dây thừng thô có sức nặng vật lý thực thụ, xóa sạch hoàn toàn cảm giác kỹ xảo hoạt hình giả tạo.

#### Đột phá 2: Ánh sáng 2 vùng nhiệt độ & Đèn thực tế giấu trong mô hình (Practical Lights)
* **Kết quả:** 
  * Cửa sổ vòm ánh sáng biển đêm xanh lạnh đối chọi với đèn bàn vàng rực.
  * Đèn lồng trăng giấy bồi (`papier-mâché moon`) phát sáng xuyên chất liệu giấy ấm áp trên nền trời đêm xanh navy.
  * Đèn dây tóc treo phản chiếu vệt sáng lung linh trên mặt nước kênh bằng nhựa resin.

---

## [2026-10-14] — Bước Nhảy V3: Chuẩn Cinematic Stop-Motion Studio & Phá Vỡ Kho Dữ Liệu Hẹp Của Meta AI

Qua đối chiếu thực nghiệm trên Meta AI và phân tích sâu bộ ảnh chuẩn từ **Dream Canteen Studio** (Video 1 & Video 2) cùng **Walter's Puppet Box**, chúng ta phát hiện và xử lý triệt để 4 căn bệnh lớn:

| Hiện tượng lỗi trên Meta AI | Nguyên nhân gốc rễ (Root Cause) | Giải pháp chuẩn hóa (V3 Fix) |
| :--- | :--- | :--- |
| **Mặt và tay bị đẽo vát cạnh gỗ kỳ dị** | Dùng từ khóa `faceted planar sculpted face`, `knife-carved`, `linden-wood`, `spatula marks` cho da người. | Xóa sạch từ khóa gọt đẽo gỗ khỏi nhân vật. Chuyển sang **`smooth matte bisque-clay skin`** (da đất sét/nhựa mờ mịn màng như phim của Laika và Dream Canteen Studio). |
| **Nhân vật bị lùn 1:3.5 như chú lùn sân vườn** | Bắt buộc mô tả trọn vẹn từ đầu tới đôi giày da (`full-body grounded shoes`) ngay cả trong góc máy cận và trung (`Close-Up / Medium`). | **Quy tắc Khung hình (Framing Rule):** Cảnh cận/trung dùng `Waist-up shot` hoặc `Thigh-up shot` (không nhắc tới giày để AI không ép lùn người). Chỉ dùng `Full-body shot` kèm giày ở cảnh toàn (`Wide`). |
| **Chót mũi và gò má đỏ choét như đánh phấn tuồng** | Đưa cụm `warm rosy blush on cheeks and nose tip` vào `CHARACTERS.dna`. | Xóa bỏ hoàn toàn `rosy blush`. Giữ sắc độ đất sét tự nhiên (`ivory-clay`, `warm cream`, `warm ochre-tan`). |
| **Hội chứng nhân bản (Toàn ông bà già mũi khoằm, tóc len trắng, đeo kính tròn)** | Dùng từ khóa DIY (`handcrafted puppet`, `craft materials`, `hand-molded`, `yarn hair`) làm Meta AI rơi vào kho dữ liệu búp bê dân gian tự làm trên Etsy. | 1. Đổi sang hệ từ khóa điện ảnh: **`Cinematic European stop-motion animation film still`** + **`Refined stop-motion animation figure`**. <br>2. Áp dụng **Ma trận 5 Kiểu Hình Khối Mặt & Mũi** + phân bổ đều 4 nhóm tuổi + giới hạn kính mắt và khăn len ở mức tối đa 15–20%. |

