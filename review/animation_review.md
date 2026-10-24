# Animation Review Gate (Cổng kiểm toán Chuyển động I2V — `prompt-animate.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `prompt-animate.txt` (trước khi đưa vào công cụ tạo video I2V), dùng để đối chiếu từng dòng lệnh chuyển động với câu lệnh gốc trong `image.txt` và cột đạo diễn I2V trong `storyboard.md`, thẩm định khách quan các tiêu chuẩn `[FATAL]` và `[HIGH RISK]` về tính chính xác của chủ thể, kỹ thuật ống kính một trục có đích ngắm, động học cơ thể mềm mại và sự giao cảm hai chiều trong 5 giây.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Phân cấp tiêu chuẩn kiểm toán Chuyển động I2V (`[FATAL]` & `[HIGH RISK]`)

### 1.1. Năm tiêu chuẩn nền tảng `[FATAL]` (Đạt 100% trước khi kết xuất video I2V)

1. **Đồng bộ 1:1 số dòng, chủ thể, tư thế gốc và đạo cụ với `image.txt` (`1:1 Subject, Posture & Prop Fidelity`):**
   - Tổng số dòng lệnh trong `prompt-animate.txt` khớp chính xác 1:1 với tổng số dòng trong `image.txt`, mỗi câu lệnh nằm trọn vẹn trên một dòng duy nhất.
   - Danh từ chỉ người (số lượng nhân vật, độ tuổi, giới tính), tư thế cơ thể ở giây 0 (`t = 0s`) và vật thể/phương tiện trong câu lệnh chuyển động khớp hoàn toàn với những gì đã được thiết lập tại dòng tương ứng của `image.txt`.

2. **Chuyển động máy quay một trục rõ hướng và mượt mà (`Clear 1-Axis Camera Motion`):**
   - Nêu rõ ràng, ngắn gọn trạng thái hoặc hướng di chuyển một trục của máy quay (giữ tĩnh, lia ngang trái/phải, ngẩng/hạ dọc, tiến nhẹ, lùi mở cảnh, trượt ngang, nâng cao hoặc đi theo cùng hướng với chủ thể), đảm bảo quỹ đạo máy quay thuận chiều và đồng nhất với hướng vận động của cảnh.

3. **Một chuyển động lớn duy nhất theo một hướng và Dòng chảy tự nhiên (`Single Unidirectional Macro Action & Natural Flow`):**
   - **Với cảnh có người:** Chỉ mô tả **một hành động lớn duy nhất tiếp diễn theo một hướng nhất quán** phát triển trực tiếp từ tư thế giây `0s` (như đi thẳng dọc con đường về phía đích, trao vật dụng qua cửa, đặt đồ lên kệ), giữ vững quán tính một chiều xuyên suốt 5 giây và để biểu cảm gương mặt cùng môi trường xung quanh vận động tự nhiên.
   - **Với cảnh tĩnh vật (`B-roll`) hoặc cảnh sắc thiên nhiên thuần túy (`completely without people`):** Lấy vật thể trung tâm hoặc yếu tố thiên nhiên trong ảnh làm chủ ngữ và mô tả một chuyển động vật lý êm ái, tự nhiên của không gian.

4. **Luân chuyển kỹ thuật máy quay giữa hai cảnh liền kề ($N \to N+1$ `Consecutive Camera Motion Rotation`):**
   - Hai dòng lệnh sát nhau ($N \to N+1$) sử dụng các kỹ thuật chuyển động ống kính khác nhau, khớp với thiết kế quỹ đạo máy tại cột đạo diễn I2V của `storyboard.md`.

5. **Tối giản câu chữ và Gợi mở cảm xúc cảnh (`Concise Kinematic Focus & Scene Mood`):**
   - Mỗi câu lệnh viết ngắn gọn, súc tích, chỉ tập trung vào chuyển động máy quay, một chuyển động lớn của chủ thể và sắc thái cảm xúc/bầu không khí của cảnh (diễn đạt linh hoạt, tự nhiên theo từng cảnh để mô hình tự suy diễn biểu cảm và vi chuyển động môi trường).

### 1.2. Hai đòn bẩy thực chứng `[HIGH RISK]` (Tối ưu cảm xúc điện ảnh và độ mượt liên cảnh)

1. **Sự đồng điệu giữa Quỹ đạo ống kính, Cảm xúc cảnh và Đường cong âm nhạc (`Musical-Mood-Kinematic Alignment`):**
   - Điều tiết tốc độ ống kính và sắc thái cảm xúc của cảnh ăn khớp với từng chương nhạc: ưu tiên các cú máy giữ khung ấm cúng hoặc tiến nhẹ mang cảm xúc lắng đọng ở các khổ hát tự sự (`Verse`, `Bridge`), và mở rộng bằng các cú máy lùi mở cảnh quan, nâng dọc, lia ngang hoặc đi theo hành trình mang cảm xúc khoáng đạt tại chuỗi mở màn, Điệp khúc (`Chorus`) và Nhạc dạo (`Solo`).
2. **Tính một chiều của hướng di chuyển (`Unidirectional Continuity`):**
   - Ở các cảnh nhân vật hoặc phương tiện đang di chuyển trên đường, giữ trọn vẹn một hướng tiến về phía trước rõ ràng từ đầu đến cuối cảnh để tạo dòng chảy thị giác mượt mà.

---

## 2. Quy trình 3 bước kiểm toán độc lập trên `prompt-animate.txt`

Trước khi đưa vào kết xuất video I2V, thực hiện kiểm toán độc lập theo 3 bước:

### Bước 1: Đối chiếu chéo 1:1 giữa `storyboard.md`, `image.txt` và `prompt-animate.txt`
- Đọc đồng thời `storyboard.md`, `image.txt` và `prompt-animate.txt`.
- Xác nhận tổng số dòng bằng nhau tuyệt đối và từng dòng `N` trong `prompt-animate.txt` gọi đúng số lượng người, đúng nhân vật và đúng đạo cụ/bối cảnh của dòng `N` trong `image.txt`.

### Bước 2: Thẩm định từng dòng theo 5 Cổng `[FATAL]` (`Line-by-Line I2V Stress Test`)
- **Cổng 1 (`Chuyển động máy quay`):** Kiểm tra hướng máy quay một trục rõ ràng, mượt mà và thuận chiều với bố cục ảnh gốc.
- **Cổng 2 (`Luân chuyển liên cảnh`):** Kiểm tra cặp dòng liền kề ($N \to N+1$) thay đổi động tác máy và khớp với cột I2V của `storyboard.md`.
- **Cổng 3 (`Một chuyển động lớn một chiều`):** Kiểm tra mỗi cảnh chỉ tập trung vào 1 hành động chính theo 1 hướng duy nhất từ tư thế giây `0s`, giữ đà chuyển động mượt mà xuyên suốt 5 giây.
- **Cổng 4 (`Biểu cảm & Môi trường tự nhiên`):** Kiểm tra mệnh đề để biểu cảm gương mặt (với cảnh có người) và vạn vật xung quanh tự vận động tự nhiên.
- **Cổng 5 (`Ngắn gọn & Có cảm xúc cảnh`):** Kiểm tra câu lệnh súc tích và có gợi mở sắc thái cảm xúc/bầu không khí phù hợp với cảnh.

### Bước 3: Bảng đối soát 5 tiêu chuẩn và Phán quyết (`Pre-I2V Animation Sign-Off`)
Xác nhận `prompt-animate.txt` đạt trọn vẹn 5 tiêu chuẩn trước khi chạy công cụ tạo video:
- **Chỉ số 1 (Đồng bộ 1:1 số dòng, chủ thể và đạo cụ với `image.txt`):** Khớp chính xác số lượng dòng và danh từ chủ thể/vật thể ở từng cảnh.
- **Chỉ số 2 (Chuyển động máy quay 1 trục rõ hướng & mượt mà):** Quỹ đạo ống kính rõ ràng, tự nhiên ở mọi dòng.
- **Chỉ số 3 (Luân chuyển động tác máy liền kề $N \to N+1$):** Các cảnh sát nhau thay đổi kỹ thuật máy quay mượt mà theo `storyboard.md`.
- **Chỉ số 4 (Đúng 1 chuyển động lớn một chiều & dòng chảy tự nhiên):** Chỉ 1 hành động chính nhất quán, để biểu cảm và môi trường tự vận động mượt mà.
- **Chỉ số 5 (Tối giản câu chữ & giàu cảm xúc cảnh):** Ngắn gọn, có sắc thái cảm xúc để AI tự suy diễn nhịp điệu tự nhiên.
