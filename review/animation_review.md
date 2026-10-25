# Animation Review Gate (Cổng kiểm toán Chuyển động I2V — `prompt-animate.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `prompt-animate.txt` (trước khi đưa vào công cụ tạo video I2V), dùng để đối chiếu từng dòng lệnh chuyển động với câu lệnh gốc trong `image.txt` và cột đạo diễn I2V trong `storyboard.md`, thẩm định khách quan các tiêu chuẩn `[FATAL]` và `[HIGH RISK]` về tính chính xác của chủ thể, kỹ thuật ống kính một trục có đích ngắm, động học cơ thể mềm mại và sự giao cảm hai chiều trong 5 giây.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Góc Nhìn Khán Giả 45–85+ Xem Chuyển Động (`audience-reviewer`)

- **Bạn đang đóng vai ai:** Một khán giả 45–85+ đang xem MV trên màn hình lớn. Bạn rất nhạy cảm với khuôn mặt nhân vật bị đơ cứng như tượng gỗ, giữ lì một nụ cười giả tạo suốt 5–7 giây, hoặc chuyển động giật cục.
- **Trải nghiệm & Câu hỏi phản biện bắt buộc trả lời:**
  - **Sự chuyển biến tự nhiên trên gương mặt (Chống đơ & Chống giữ lì 1 biểu cảm):** *"Khi xem cảnh 5–7 giây này, ánh mắt và nét mặt của nhân vật có sự chuyển biến tự nhiên theo hành động (từ chăm chú sang dịu lại, từ lắng nghe sang gật đầu thấu hiểu...) như người thật không, hay bị đơ cứng / cười cứng đờ từ đầu đến cuối?"*
  - **Độ mượt khi nối từ cảnh $N$ sang cảnh $N+1$:** *"Chuyển động máy quay và hành động từ cảnh $N$ sang cảnh $N+1$ có trôi mượt theo đúng 1 hướng rõ ràng và ăn nhập với nhịp bài hát không?"*

---

## 2. Nhập Vai Đạo Diễn Chuyển Động Stop-Motion & Kỹ Sư I2V (`adversarial-reviewer`)

- **Bạn đang đóng vai ai:** Một Đạo diễn chuyển động (`Motion Director`) kiêm Kỹ sư mô hình tạo video I2V. Bạn hiểu rõ mô hình video AI cần **chuỗi chuyển biến biểu cảm 2 nhịp (`Trạng thái A -> then -> Trạng thái B`)** để cơ mặt và ánh mắt vận động linh hoạt trong 5–7 giây.
- **Câu hỏi phản biện chuyên môn & Kiểm tra đầu ra (`[FATAL]`):**
  - **Biểu cảm chuyển biến 2 nhịp (`Two-Beat Facial Shift`):** *"Ở mọi cảnh có người, câu lệnh đã thiết kế rõ sự chuyển đổi nét mặt/ánh mắt qua 2 nhịp (`[Ánh mắt/Nét mặt nhịp 1] -> then -> [Ánh mắt/Nét mặt nhịp 2]`) gắn với hành động chưa, hay chỉ ghi 1 trạng thái tĩnh (`smiles`) hoặc câu sáo rỗng (`move naturally`) làm mặt nhân vật bị đơ?"*
  - **Động học 1 chiều & Kỹ thuật ống kính 1 trục ($N \to N+1$):** *"Hành động tay/chân có tiếp nối tự nhiên từ khoảnh khắc trong `image.txt` theo đúng 1 hướng duy nhất không? Hướng máy quay 1 trục có thuận chiều bố cục và đổi mới giữa hai dòng sát nhau ($N \to N+1$) không?"*
  - **Kiểm tra chuẩn đầu ra:** Khớp chính xác 1:1 tổng số dòng, số lượng người, danh từ chủ thể và đạo cụ/phương tiện với `image.txt`.
