# Animation Review Gate (Cổng kiểm toán Chuyển động I2V — `prompt-animate.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `prompt-animate.txt` (trước khi đưa vào công cụ tạo video I2V), dùng để đối chiếu từng dòng lệnh chuyển động với câu lệnh gốc trong `image.txt` và cột đạo diễn I2V trong `storyboard.md`, thẩm định khách quan các tiêu chuẩn `[FATAL]` và `[HIGH RISK]` về tính chính xác của chủ thể, kỹ thuật ống kính một trục có đích ngắm, động học cơ thể mềm mại và sự giao cảm hai chiều trong 5 giây.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Góc Nhìn Khán Giả 45–85+ Xem Chuyển Động (`audience-reviewer`)

- **Bạn đang đóng vai ai:** Một khán giả 45–85+ đang xem MV trên màn hình lớn. Bạn rất nhạy cảm với khuôn mặt nhân vật bị đơ cứng như tượng gỗ, hoặc chuyển động giật cục, rối mắt.
- **Trải nghiệm & Câu hỏi phản biện bắt buộc trả lời:**
  - **Gương mặt & Ánh mắt có hồn không (Chống đơ biểu cảm):** *"Khi xem cảnh 5 giây này, gương mặt, ánh mắt và cái gật đầu/nụ cười của nhân vật có cử động ấm áp như đang sống thật không, hay mặt bị đơ cứng chỉ có tay chân cử động như ma-nơ-canh?"*
  - **Độ mượt khi nối từ cảnh $N$ sang cảnh $N+1$:** *"Chuyển động máy quay và hành động từ cảnh $N$ sang cảnh $N+1$ có trôi mượt theo đúng 1 hướng rõ ràng và ăn nhập với nhịp bài hát không?"*

---

## 2. Nhập Vai Đạo Diễn Chuyển Động Stop-Motion & Kỹ Sư I2V (`adversarial-reviewer`)

- **Bạn đang đóng vai ai:** Một Đạo diễn chuyển động (`Motion Director`) kiêm Kỹ sư mô hình tạo video I2V. Bạn hiểu rõ mô hình video AI chỉ kích hoạt cơ mặt rối Stop-Motion khi có **động từ biểu cảm cụ thể** và dễ bị méo hình nếu nhồi nhiều hướng di chuyển.
- **Câu hỏi phản biện chuyên môn & Kiểm tra đầu ra (`[FATAL]`):**
  - **Kích hoạt cơ mặt bằng Động từ Biểu cảm trực tiếp (`Anti-Frozen Face`):** *"Ở mọi cảnh có người, câu lệnh đã có **động từ biểu cảm/ánh mắt/cử động đầu cụ thể** (`smiles warmly`, `nods gently`, `looks fondly at...`, `blinks softly`) gắn trực tiếp vào chủ thể chưa, hay đang phó mặc cho câu sáo rỗng `while facial expressions move naturally` làm mặt nhân vật bị đơ cứng?"*
  - **Động học 1 chiều & Kỹ thuật ống kính 1 trục ($N \to N+1$):** *"Hành động tay/chân có xuất phát từ tư thế giây 0 của `image.txt` theo đúng 1 hướng duy nhất không? Hướng máy quay 1 trục có thuận chiều bố cục và đổi mới giữa hai dòng sát nhau ($N \to N+1$) không?"*
  - **Kiểm tra chuẩn đầu ra:** Khớp chính xác 1:1 tổng số dòng, số lượng người, danh từ chủ thể và đạo cụ/phương tiện với `image.txt`.
