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
| **Mặt khô khốc như gỗ lũa** | Tả chi tiết nếp nhăn chạm khắc gỗ quá gắt (`carved wrinkles`). | Mặt nhân vật trông già nua, khô khan, thiếu sức sống. | Chuyển sang tả bề mặt gốm sơn mờ (`porcelain-matte`) hoặc da nặn mịn lì có vệt má hồng nhẹ (`subtle warm blush`). |
| **Hậu cảnh bị xóa phông mờ tịt** | Lạm dụng cụm từ `shallow depth of field` không kiểm soát. | Mất sạch chi tiết sa bàn ở phía sau, trông giống ảnh chân dung xóa phông rẻ tiền. | Dùng `deep miniature staging, readable layered background` để giữ chiều sâu lớp lang diorama. |

---

### 3. Thành công đột phá (Breakthroughs & Wins)

#### Đột phá 1: Bông gòn thô đánh bại hoàn toàn 3D CGI (Case study: Xe buýt sa mạc muối)
* **Prompt:** `a dense fluffy cumulus cloud made of raw fibrous cotton, bound with knotted coarse hemp twine`.
* **Kết quả:** Đám mây hiện lên chân thực đến từng sợi tơ bông xù xì bắt nắng, được neo bằng dây thừng thô có sức nặng vật lý thực thụ, xóa sạch hoàn toàn cảm giác kỹ xảo hoạt hình giả tạo.

#### Đột phá 2: Công thức "Áo phủ kín + Kính râm đen" (The Black-Anchor Armor)
* **Kết quả:** Khi nhân vật mặc âu phục vải thô dài tay che kín cổ tay, quần dài trùm mắt cá chân, và đeo cặp kính tròn to bản màu đen:
  * Khớp bi và cọc gỗ biến mất 100%.
  * Cặp kính đen đóng vai trò mỏ neo tương phản (Black Anchor), ghim trọn điểm nhìn, mang lại nét mặt an nhiên, đáng yêu và đầy tính nhân văn (soulful caricature).

#### Đột phá 3: Ánh sáng 2 vùng nhiệt độ & Đèn thực tế giấu trong mô hình (Practical Lights)
* **Kết quả:** 
  * Cửa sổ vòm ánh sáng biển đêm xanh lạnh đối chọi với đèn bàn vàng rực.
  * Đèn lồng trăng giấy bồi (`papier-mâché moon`) phát sáng xuyên chất liệu giấy ấm áp trên nền trời đêm xanh navy.
  * Đèn dây tóc treo phản chiếu vệt sáng lung linh trên mặt nước kênh bằng nhựa resin.

---

### 4. Quy tắc vàng đúc kết (Standard Operating Procedures)

1. **Nguyên tắc "Mỏ neo tương phản" (Visual Anchors):** Mọi khung hình nên có ít nhất một chi tiết đen tuyền (kính râm, đĩa than vinyl, vali da, lốp cao su, khung sắt đen) kết hợp ánh sáng vàng ngà/đồng thau để ghim độ tương phản, chống bạc màu.
2. **Nguyên tắc "Hành vi quang học của chất liệu":** Không gắn nhãn danh mục khô cứng. Luôn mô tả cách vật liệu tương tác với ánh sáng (đồng xỉn phản quang mờ, giấy da xuyên sáng, nhựa resin trong vắt).
3. **Nguyên tắc "Che phủ giải phẫu":** Muốn nhân vật stop-motion không bị lỗi dị tật cơ học, luôn cho mặc trang phục may đo rời che kín cổ tay và cổ chân.
