# Retention Review Gate (Bộ lọc kiểm toán giữ chân khán giả)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán độc lập chạy ngay sau khi dựng xong `character.md` và `storyboard.md` (trước khi xuất `image.txt`), dùng để đánh giá tiêu chuẩn `[FATAL]` / `[HIGH RISK]` về ý nghĩa hoạt động thực tế, tính đồng nhất của thế giới sa bàn thủ công trực quan, sự đối lập hình khối nhân vật 4 trục, nhịp điệu thị giác và tính nhất quán với Chế độ Kể chuyện đã chọn.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Luật Kiểm Toán Đầu Ra `character.md`, `storyboard.md` & `image.txt`

### 1.1. Tiêu chuẩn bắt buộc (`[FATAL]`)
- **Đồng bộ dòng & mốc giờ:** `storyboard.md` và `image.txt` khớp 1:1 số dòng, mốc giờ và nội dung cảnh với `timestamps.txt`; nhân vật cố định trong `character.md` đồng nhất ngoại hình xuyên suốt các cảnh.
- **Hook mở đầu (15 giây đầu / Cảnh 1–3):** Mở ngay bằng hình ảnh thị trấn kỳ lạ bắt mắt nhất kèm một hành động đang khởi phát có mục đích để tạo câu hỏi tò mò giữ chân người xem.
- **Diễn dịch câu hát & Biến thiên liên cảnh ($N \to N+1$):** Chuyển ý nghĩa câu hát thành tình huống và hành động cụ thể theo `1-idea.md` (đặt đúng các chi tiết đắt giá vào mốc giờ tương ứng); cảnh sau khác cảnh trước về bối cảnh, cỡ cảnh, góc máy và hành động.
- **Luật Hình ảnh, Tỷ lệ vật lý & Khung câu lệnh 4 khối (`image.txt`):**
  - Mỗi cảnh tập trung vào 1 ý tưởng hình ảnh rõ ràng trong không gian thị trấn siêu thực thoáng rộng; mỗi nhân vật thực hiện 1 hành động rõ ràng ở giây 0 (`t = 0s`).
  - Chọn cỡ bán thân/trung cận khi có vách che phần dưới hoặc lấy cận biểu cảm; chọn cỡ toàn thân thấy đủ trang phục đến giày chạm sàn/đất khi ở không gian mở hoặc phòng rộng; nhà cửa và phương tiện cao lớn hơn đầu người.
  - Khớp chuẩn 4 khối tiếng Anh tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md), tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5) và khóa cuối dòng bằng 1 nguồn sáng duy nhất chiếu 1 hướng bóng đổ (`--ar 16:9`).

### 1.2. Đòn bẩy giữ chân & Cảm xúc (`[HIGH RISK]`)
- **Giữ chân giữa bài (Mở khóa không gian & Tình huống nhân-quả):** Mỗi đoạn nhạc mới dẫn sang một góc không gian/nét kỳ diệu mới của thị trấn và triển khai các cụm tình huống có diễn biến (bắt đầu $\to$ tương tác $\to$ kết quả).
- **Đỉnh cảm xúc & Kết bài (`Payoff`):** Đặt khoảnh khắc thị giác và tình người đắt giá nhất ở nửa cuối bài (`Bridge / Chorus cuối`) để giải đáp hành trình từ đầu bài, rồi khép lại trọn vẹn ở `Outro`.
- **Đa dạng ngoại hình & Bảng màu:** Mỗi nhân vật có ngoại hình và màu sắc trang phục riêng biệt, hài hòa với ánh sáng chuyển dịch theo thời gian câu chuyện.
