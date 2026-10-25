# Visual Craft: Đạo diễn Storyboard & Chuỗi khung hình (`character.md` & `storyboard.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` và `timestamps.txt` để thiết lập hồ sơ nhân vật `character.md` và đạo diễn bảng phân cảnh `storyboard.md` (hoạt động sống có mục đích thực tế, tương tác nhân-quả trong khung hình, đường cong năng lượng theo cấu trúc nhạc, tỷ lệ 70/30 cùng 4 động cơ chất ngông, bố cục không gian, ma trận góc máy và luật đảo nhịp $N \to N+1$). Toàn bộ nguyên lý chất liệu sa bàn stop-motion trực quan, công thức nén nhận diện 4 trục và khung câu lệnh 4 khối tiếng Anh cho `character.md` / `image.txt` nằm độc lập tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra

- **Đầu vào:** `1-idea.md`, `3-lyrics.txt` và `timestamps.txt`.
- **Đầu ra:**
  - **`character.md`:** Danh sách nhân vật cố định viết bằng `@Tên` kèm mô tả ngoại hình (nếu có). Nhân vật xuất hiện lẻ ở cảnh nào thì tả trực tiếp ở cảnh đó.
  - **`storyboard.md`:** Bảng mạch chuyện bằng chữ khớp 1:1 số dòng và mốc giờ với `timestamps.txt` theo 4 cột (duyệt xong dịch 1:1 sang `image.txt` theo [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md)):

| Cảnh & Giờ | Đoạn nhạc & Lời hát | Thông số đạo diễn (Cỡ, Góc, Bối cảnh, Chuyển động) | Nhân vật, Khoảnh khắc hành động & Ánh sáng |
| :--- | :--- | :--- | :--- |
| 01 (00:00-00:04) | [Lời hát / Nhạc] | Cỡ: [...]<br>Góc: [...]<br>Bối cảnh: [...]<br>Chuyển động: [Hướng máy + Diễn biến hành động + Cảm xúc cảnh] | [Mô tả nhân vật + Biểu cảm, dáng điệu & khoảnh khắc hành động đang diễn ra + Ánh sáng] |

---

## 2. Luật Kịch Bản & Kỹ Thuật Giữ Chân (`storyboard.md`)

- **1. Hook mở màn (Cảnh 1–3) — Chọn 1 trong 2 cách (hoặc kết hợp):**
  - **Cách 1 — Bắt mắt / Choáng ngợp:** Mở ngay bằng khung cảnh thị trấn siêu thực kỳ lạ, ấn tượng nhất (khớp lời hứa ở Tiêu đề/Thumbnail).
  - **Cách 2 — Gây tò mò / Khó hiểu:** Mở ngay bằng một hành động hoặc tình huống kỳ lạ đang diễn ra lưng chừng khiến người xem tự hỏi *"Ủa họ đang làm cái gì thế? Chuyện gì đang xảy ra ở đây?"*.
- **2. Trọng tâm Cảm xúc & Ý nghĩa trong từng Khung hình (`[Cảnh N + Câu hát N]`):**
  - Mỗi bức ảnh phải tự nói lên được **trạng thái cảm xúc và ý nghĩa câu chuyện** của nhân vật ở khoảnh khắc đó (niềm vui háo hức khi mang quà đi sẻ chia, sự nhẹ nhõm biết ơn khi được kiên nhẫn đợi chờ, sự ấm áp khi tâm tình cùng bạn già, vẻ tĩnh tại khi ngắm nhìn thiên nhiên), truyền tải trực tiếp cái hồn của câu hát đang vang lên.
- **3. Bước nhảy Không gian & Đảo nhịp Góc máy ($N \to N+1$):**
  - Mỗi cảnh là một lát cắt cảm xúc trọn vẹn; khi chuyển từ Cảnh $N$ sang Cảnh $N+1$ phải chuyển sang vị trí không gian/điểm nhìn mới, đổi cỡ cảnh (Toàn $\leftrightarrow$ Trung/Cận) và đổi độ cao góc máy (Góc thấp hất lên $\leftrightarrow$ Góc cao nhìn xuống $\leftrightarrow$ Góc qua vai POV $\leftrightarrow$ Góc xuyên khung tiền cảnh), liên tục mở ra các khung cảnh kỳ diệu mới của thị trấn.
- **4. Gieo – Gặt chi tiết & Điểm nổ cảm xúc cuối bài:** Chi tiết/nhân vật gieo ở đầu bài được gặt lại ấm áp ở cuối bài; dành khung hình siêu thực đẹp nhất và cử chỉ tình người xúc động nhất cho cao trào cuối bài trước khi khép lại êm đềm.

---

## 3. Luật Hình Ảnh & Thế Giới

- **Luật Siêu thực:** Nét kỳ lạ, siêu thực của thị trấn mọc ra từ câu chuyện của bài hát; nhân vật sống và sinh hoạt bên trong không gian đó.
- **Luật Tối giản:** Mỗi cảnh tập trung vào 1 ý tưởng hình ảnh rõ ràng trong không gian thoáng rộng, có thể xóa phông hậu cảnh khi cần làm nổi bật chủ thể.
- **Luật Đa dạng & Chiều sâu Điện ảnh:** Luân phiên đa dạng góc độ cao-thấp của máy quay (góc thấp hất lên, góc cao nhìn xuống, góc nhìn qua vai, góc chéo dọc chiều sâu, góc nhìn xuyên qua tiền cảnh) cùng bố cục nhiều lớp tiền-trung-hậu cảnh và cỡ cảnh; mỗi nhân vật có ngoại hình và màu trang phục riêng.
- **Luật Cảm xúc & Ý nghĩa:** Mỗi khung hình đặt trạng thái nội tâm, ánh mắt, nụ cười và ý nghĩa của sự gắn kết giữa người với người làm trung tâm, nơi hành động là sự bộc lộ cảm xúc tự nhiên giữa đời sống.
- **Luật Cỡ cảnh & Tỷ lệ vật lý:**
  - Dùng cỡ bán thân hoặc trung cận khi nhân vật ở trong không gian có vách che phần dưới hoặc khi lấy cận biểu cảm.
  - Dùng cỡ toàn thân thấy đủ trang phục đến giày chạm sàn/đất khi nhân vật ở không gian mở hoặc phòng rộng.
  - Nhà cửa và phương tiện có kích thước thật cao lớn hơn đầu người.
- **Luật Ánh sáng:** Mỗi cảnh có 1 nguồn sáng chính chiếu theo 1 hướng; ánh sáng chuyển dịch mượt theo thời gian câu chuyện.
