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
- **2. Mạch nối tiếp mượt mà từng cảnh (`[Cảnh N + Câu hát N] -> [Cảnh N+1 + Câu hát N+1]`):**
  - Người xem chỉ trải nghiệm cảnh hiện tại nối với cảnh ngay trước đó: từ Cảnh $N$ sang Cảnh $N+1$ phải nối tiếp mượt mà về mặt không gian, cảm xúc câu hát và tiến triển hành động (**Khởi phát $\to$ Tương tác $\to$ Kết quả**) để giữ người xem ở lại xem cảnh kế tiếp.
  - Chuyển ý nghĩa và cảm xúc của câu hát đang vang lên thành tình huống cụ thể (đặt đúng các chi tiết đắt giá của `1-idea.md` vào mốc giờ tương ứng).
- **3. Đảo nhịp liên cảnh ($N \to N+1$) & Mở khóa không gian:** Cảnh $N+1$ phải khác Cảnh $N$ về cỡ cảnh (Toàn $\leftrightarrow$ Trung/Cận), góc máy và hành động; liên tục mở ra các góc nhìn/nét kỳ diệu mới của thị trấn, kết hợp hài hòa giữa các cảnh động giàu tương tác sống động với những cảnh lắng đọng có bố cục tuyệt đẹp nơi nhân vật thực hiện hành động mang chiều sâu nội tâm và chiêm nghiệm không gian.
- **4. Gieo – Gặt chi tiết & Điểm nổ cảm xúc cuối bài:** Chi tiết/nhân vật gieo ở đầu bài được gặt lại ấm áp ở cuối bài; dành khung hình siêu thực đẹp nhất và cử chỉ tình người xúc động nhất cho cao trào cuối bài trước khi khép lại êm đềm.

---

## 3. Luật Hình Ảnh & Thế Giới

- **Luật Siêu thực:** Nét kỳ lạ, siêu thực của thị trấn mọc ra từ câu chuyện của bài hát; nhân vật sống và sinh hoạt bên trong không gian đó.
- **Luật Tối giản:** Mỗi cảnh tập trung vào 1 ý tưởng hình ảnh rõ ràng trong không gian thoáng rộng, có thể xóa phông hậu cảnh khi cần làm nổi bật chủ thể.
- **Luật Đa dạng & Chiều sâu Điện ảnh:** Luân phiên đa dạng góc độ cao-thấp của máy quay (góc thấp hất lên, góc cao nhìn xuống, góc nhìn qua vai, góc chéo dọc chiều sâu, góc nhìn xuyên qua tiền cảnh) cùng bố cục nhiều lớp tiền-trung-hậu cảnh và cỡ cảnh; mỗi nhân vật có ngoại hình và màu trang phục riêng.
- **Luật Lát cắt Sống động:** Mỗi khung hình là một lát cắt cuộc sống tự nhiên bắt trọn khoảnh khắc con người và phương tiện đang vận động hoặc tương tác tâm tình giữa dòng chảy đời thường.
- **Luật Cỡ cảnh & Tỷ lệ vật lý:**
  - Dùng cỡ bán thân hoặc trung cận khi nhân vật ở trong không gian có vách che phần dưới hoặc khi lấy cận biểu cảm.
  - Dùng cỡ toàn thân thấy đủ trang phục đến giày chạm sàn/đất khi nhân vật ở không gian mở hoặc phòng rộng.
  - Nhà cửa và phương tiện có kích thước thật cao lớn hơn đầu người.
- **Luật Ánh sáng:** Mỗi cảnh có 1 nguồn sáng chính chiếu theo 1 hướng; ánh sáng chuyển dịch mượt theo thời gian câu chuyện.
