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

| Cảnh & Giờ | Đoạn nhạc & Lời hát | Thông số đạo diễn (Cỡ, Góc, Bối cảnh, Chuyển động) | Nhân vật, Hành động ở giây 0 & Ánh sáng |
| :--- | :--- | :--- | :--- |
| 01 (00:00-00:04) | [Lời hát / Nhạc] | Cỡ: [...]<br>Góc: [...]<br>Bối cảnh: [...]<br>Chuyển động: [Hướng máy + Hành động lớn 1 chiều + Cảm xúc cảnh] | [Mô tả nhân vật + Biểu cảm, dáng điệu & 1 hành động ở giây 0 + Ánh sáng] |

---

## 2. Luật Kịch Bản & Giữ Chân (`storyboard.md`)

- **Hook mở đầu (15 giây đầu / Cảnh 1–3):** Mở ngay bằng hình ảnh thị trấn kỳ lạ bắt mắt nhất kèm một hành động đang khởi phát có mục đích để tạo câu hỏi tò mò giữ chân người xem.
- **Giữ chân giữa bài (Mở khóa không gian & Tình huống nhân-quả):** Mỗi đoạn nhạc mới dẫn sang một góc không gian/nét kỳ diệu mới của thị trấn và triển khai các cụm tình huống có diễn biến (bắt đầu $\to$ tương tác $\to$ kết quả).
- **Đỉnh cảm xúc & Kết bài (`Payoff`):** Đặt khoảnh khắc thị giác và tình người đắt giá nhất ở nửa cuối bài (`Bridge / Chorus cuối`) để giải đáp hành trình từ đầu bài, rồi khép lại trọn vẹn ở `Outro`.
- **Diễn dịch câu hát thành tình huống:** Chuyển ý nghĩa và cảm xúc của câu hát thành tình huống, hành động cụ thể để kể tiếp câu chuyện theo `1-idea.md`, đặt đúng các chi tiết đắt giá vào mốc giờ tương ứng.
- **Biến thiên liên cảnh ($N \to N+1$):** Cảnh sau là một lát cắt hoặc bước tiến mới, khác cảnh trước về bối cảnh, cỡ cảnh, góc máy và hành động; chọn cảnh động hay tĩnh khớp nhịp nhạc.

---

## 3. Luật Hình Ảnh & Thế Giới

- **Luật Siêu thực:** Nét kỳ lạ, siêu thực của thị trấn mọc ra từ câu chuyện của bài hát; nhân vật sống và sinh hoạt bên trong không gian đó.
- **Luật Tối giản:** Mỗi cảnh tập trung vào 1 ý tưởng hình ảnh rõ ràng trong không gian thoáng rộng, có thể xóa phông hậu cảnh khi cần làm nổi bật chủ thể.
- **Luật Đa dạng:** Đa dạng góc máy, bố cục, bối cảnh và cỡ cảnh (từ cận cảnh đến siêu rộng — mang tính tham khảo, tự do sáng tạo hoặc thay đổi thêm theo cảnh); mỗi nhân vật có ngoại hình và màu trang phục riêng.
- **Luật Tự nhiên:** Biểu cảm, dáng điệu, hành động và sự tương tác tâm tình giữa các nhân vật tự nhiên, đa dạng như đời sống hằng ngày; ở giây 0 mỗi nhân vật thực hiện 1 hành động rõ ràng làm đà cho chuyển động một chiều.
- **Luật Cỡ cảnh & Tỷ lệ vật lý:**
  - Dùng cỡ bán thân hoặc trung cận khi nhân vật ở trong không gian có vách che phần dưới hoặc khi lấy cận biểu cảm.
  - Dùng cỡ toàn thân thấy đủ trang phục đến giày chạm sàn/đất khi nhân vật ở không gian mở hoặc phòng rộng.
  - Nhà cửa và phương tiện có kích thước thật cao lớn hơn đầu người.
- **Luật Ánh sáng:** Mỗi cảnh có 1 nguồn sáng chính chiếu theo 1 hướng; ánh sáng chuyển dịch mượt theo thời gian câu chuyện.
