# Animation Review Gate (Cổng kiểm toán Chuyển động I2V — `prompt-animate.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `prompt-animate.txt` (trước khi đưa vào công cụ tạo video I2V), dùng để đối chiếu từng dòng lệnh chuyển động với câu lệnh gốc trong `image.txt` và cột đạo diễn I2V trong `storyboard.md`, thẩm định khách quan các tiêu chuẩn `[FATAL]` và `[HIGH RISK]` về tính chính xác của chủ thể, kỹ thuật ống kính một trục có đích ngắm, động học cơ thể mềm mại và sự giao cảm hai chiều trong 5 giây.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Nhập Vai Khán Giả 45–85+ Xem Chuyển Động Video (`Viewer Motion Roleplay`)

- **Bạn đang đóng vai ai:** Một khán giả 45–85+ đang xem MV trên màn hình lớn. Mắt người lớn tuổi rất nhạy với chuyển động giật cục, rối mắt, máy quay lắc lư vô hướng hoặc nhân vật làm nhiều động tác phức tạp gây biến dạng hình ảnh.
- **Trải nghiệm & Câu hỏi phản biện bắt buộc trả lời:**
  - **Độ êm mắt & Chiều hướng rõ ràng:** *"Khi xem cảnh 5 giây này chuyển động, mắt tôi có thấy máy quay và nhân vật trôi mượt theo đúng 1 hướng rõ ràng không, hay bị nhồi nhét nhiều hành động làm hình ảnh méo mó?"*
  - **Nhịp thở khi nối từ cảnh $N$ sang cảnh $N+1$:** *"Khi cắt từ cảnh $N$ sang cảnh $N+1$, chuyển động máy quay có được đổi mới mượt mà và khớp với cảm xúc ấm áp/khoáng đạt của đoạn nhạc lúc đó không?"*

---

## 2. Kiểm Toán Chuẩn Đầu Ra (`prompt-animate.txt` — `[FATAL]`)

- **Đồng bộ 1:1 với `image.txt` và `storyboard.md`:** Khớp chính xác tổng số dòng (mỗi câu lệnh 1 dòng); danh từ chỉ người, số lượng nhân vật, tư thế giây 0 (`t = 0s`) và đạo cụ/phương tiện khớp 100% với dòng tương ứng trong `image.txt`.
- **Chuyển động máy quay 1 trục & Đảo nhịp ($N \to N+1$):** Nêu rõ hướng di chuyển 1 trục của máy quay thuận chiều với bố cục ảnh; hai dòng sát nhau ($N \to N+1$) dùng kỹ thuật chuyển động ống kính khác nhau theo cột đạo diễn của `storyboard.md`.
- **Một chuyển động lớn 1 chiều & Cảm xúc cảnh:**
  - **Cảnh có người:** Chỉ mô tả 1 hành động lớn tiếp diễn theo 1 hướng nhất quán từ tư thế giây 0, để biểu cảm gương mặt và môi trường xung quanh tự vận động tự nhiên.
  - **Cảnh tĩnh vật / Không gian (`completely without people`):** Lấy vật thể hoặc yếu tố thiên nhiên làm chủ ngữ với 1 chuyển động vật lý êm ái; gợi mở ngắn gọn sắc thái cảm xúc/bầu không khí của cảnh.
