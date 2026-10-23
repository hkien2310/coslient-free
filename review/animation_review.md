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
   - Danh từ chỉ người (số lượng nhân vật, độ tuổi, giới tính), tư thế cơ thể ở giây 0 (`t = 0s`) và vật thể/phương tiện đang thao tác trong câu lệnh chuyển động khớp hoàn toàn với những gì đã được thiết lập tại dòng tương ứng của `image.txt`.

2. **Chủ ngữ máy quay tường minh, Kỹ thuật ống kính một trục có đích ngắm và Nhịp thở khung hình (`Explicit Camera Subject, Motivated 1-Axis Motion & Frame Breathing`):**
   - Mở đầu mọi câu lệnh bằng chủ ngữ tường minh `The camera` hoặc `Unstabilized camera` kết hợp động từ di chuyển một trục rõ ràng và đích mở khung hình cụ thể (`from [X] to [Y]`, `keeping [X] centered`, `at the same pace`, `until [Y] comes into view`, `to reveal [Y]`).
   - Sử dụng đúng cụm nhịp thở khung hình tương ứng với trạng thái máy:
     - **Khi giữ khung hoặc xoay trục tại chỗ (`holds steady / lingers / pans / tilts`):** Đi kèm cụm `, the frame breathing with natural motion.`
     - **Khi tịnh tiến thân máy một trục (`moves slowly closer / pulls slowly back / glides laterally / rises gently / circles gently`):** Đi kèm cụm `, the frame swaying with natural motion.`
     - **Khi bám song song cùng nhịp di chuyển của chủ thể (`Unstabilized camera moves alongside [X] at the same pace`):** Đi kèm cụm `, the frame visibly bobbing and swaying.`

3. **Động học cơ thể mềm mại, Tương tác giao cảm hai chiều và Đuôi khóa chuẩn xác (`Fluid Human Kinematics, Reciprocal Affection & Exact Closing Tail`):**
   - **Với cảnh có người:** Mô tả một chuyển động tiếp diễn liền mạch trong 5 giây phát triển trực tiếp từ tư thế giây 0 bằng các động từ ở thì hiện tại đơn kèm trạng từ chỉ sự khoan thai, uyển chuyển (`with fluid, unhurried motion`, `gently shifting weight`, `smoothly`); khi cảnh có từ hai nhân vật trở lên, thể hiện rõ sự hưởng ứng và giao cảm qua lại giữa các chủ thể (ánh mắt nhìn nhau ấm áp, nghiêng đầu lắng nghe rồi mỉm cười gật đầu, cử chỉ chăm sóc tiếp diễn êm ái), và kết thúc bằng đúng cụm đuôi cố định: **`, while facial expressions and everything around move naturally.`**
   - **Với cảnh tĩnh vật (`B-roll`) hoặc cảnh sắc thiên nhiên thuần túy (`completely without people`):** Lấy vật thể trung tâm hoặc yếu tố thiên nhiên trong ảnh làm chủ ngữ, mô tả chuyển động vật lý tự nhiên êm ái trong 5 giây và kết thúc bằng đúng cụm đuôi cố định: **`, while everything around moves naturally.`**

4. **Luân chuyển kỹ thuật máy quay giữa hai cảnh liền kề ($N \to N+1$ `Consecutive Camera Motion Rotation`):**
   - Hai dòng lệnh sát nhau ($N \to N+1$) sử dụng các kỹ thuật chuyển động ống kính khác nhau, khớp với thiết kế quỹ đạo máy đã duyệt tại cột đạo diễn I2V của `storyboard.md`.

5. **Tập trung thuần túy vào động học trong khoảng `25–38 từ/dòng` (`Pure Kinematic Focus & Word-Count Discipline`):**
   - Mỗi câu lệnh gói gọn trong khoảng `25–38 từ`, dành trọn 100% dung lượng cho chuyển động của ống kính và cử chỉ tiếp diễn mềm mại của chủ thể trong vùng không gian hiện hữu của bức ảnh gốc (để phần thông tin về chất liệu, màu sắc trang phục và nguồn sáng cho `image.txt` đảm nhận).

### 1.2. Hai đòn bẩy thực chứng `[HIGH RISK]` (Tối ưu cảm xúc điện ảnh và độ mượt liên cảnh)

1. **Sự đồng điệu giữa Quỹ đạo ống kính và Đường cong năng lượng âm nhạc (`Musical-Kinematic Alignment`):**
   - Điều tiết tốc độ và biên độ mở của ống kính ăn khớp với từng chương nhạc: ưu tiên các cú máy giữ khung ấm cúng (`holds steady`, `lingers`) hoặc tiến nhẹ (`moves slowly closer`) ở các khổ hát tự sự (`Verse`, `Bridge`), và mở rộng bằng các cú máy lùi mở cảnh quan (`pulls slowly back to reveal`), nâng dọc (`rises gently`), trượt ngang (`glides laterally`) hoặc bám hành trình (`Unstabilized camera moves alongside`) tại chuỗi mở màn, Điệp khúc (`Chorus`) và Nhạc dạo (`Solo`).
2. **Phản ứng vật lý tinh tế của Môi trường xung quanh (`Subtle Environmental Micro-Motion`):**
   - Kết hợp hài hòa chuyển động của chủ thể với một nhịp chuyển động tự nhiên rất khẽ của môi trường sẵn có trong ảnh gốc để toàn bộ khung hình thở cùng một nhịp sống động.

---

## 2. Quy trình 3 bước kiểm toán độc lập trên `prompt-animate.txt`

Trước khi đưa vào kết xuất video I2V, thực hiện kiểm toán độc lập theo 3 bước:

### Bước 1: Đối chiếu chéo 1:1 giữa `storyboard.md`, `image.txt` và `prompt-animate.txt`
- Đọc đồng thời `storyboard.md`, `image.txt` và `prompt-animate.txt`.
- Xác nhận tổng số dòng bằng nhau tuyệt đối và từng dòng `N` trong `prompt-animate.txt` gọi đúng số lượng người, đúng nhân vật và đúng đạo cụ/bối cảnh của dòng `N` trong `image.txt`.

### Bước 2: Thẩm định từng dòng theo 5 Cổng `[FATAL]` (`Line-by-Line I2V Stress Test`)
- **Cổng 1 (`Chủ ngữ & Kỹ thuật máy`):** Kiểm tra mở đầu bằng `The camera` / `Unstabilized camera`, có đích ngắm rõ ràng và đúng cụm nhịp thở (`breathing` / `swaying` / `bobbing and swaying`).
- **Cổng 2 (`Luân chuyển liên cảnh`):** Kiểm tra cặp dòng liền kề ($N \to N+1$) thay đổi động tác máy và khớp với cột I2V của `storyboard.md`.
- **Cổng 3 (`Động học & Giao cảm 2 chiều`):** Kiểm tra động từ hiện tại đơn kèm trạng từ mềm mại và sự tương tác hai chiều giữa các nhân vật trong cảnh.
- **Cổng 4 (`Câu đuôi cố định`):** Kiểm tra 100% cảnh có người kết thúc bằng `, while facial expressions and everything around move naturally.` và 100% cảnh tĩnh vật/cảnh sắc thuần túy kết thúc bằng `, while everything around moves naturally.`
- **Cổng 5 (`Độ dài & Thuần động học`):** Kiểm tra độ dài `25–38 từ/dòng` và sự tập trung thuần túy vào chuyển động.

### Bước 3: Bảng đối soát 5 chỉ số định lượng và Phán quyết (`Pre-I2V Animation Sign-Off`)
Thống kê và xác nhận `prompt-animate.txt` đạt trọn vẹn 5 chỉ số trước khi chạy công cụ tạo video:
- **Chỉ số 1 — Đồng bộ 1:1 số dòng, chủ thể và đạo cụ với `image.txt` (`100%`):** Khớp chính xác số lượng dòng và danh từ chủ thể/vật thể ở từng cảnh.
- **Chỉ số 2 — Chuẩn chủ ngữ `The camera`, đích khung hình & nhịp thở ống kính (`100%`):** Đúng cấu trúc mở đầu và trạng thái nhịp thở khung hình ở mọi dòng.
- **Chỉ số 3 — Luân chuyển động tác máy liền kề $N \to N+1$ (`100%`):** Các cảnh sát nhau thay đổi kỹ thuật máy quay mượt mà theo `storyboard.md`.
- **Chỉ số 4 — Động học mềm mại, tương tác hai chiều & đúng câu đuôi cố định (`100%`):** Cử chỉ khoan thai, có giao cảm qua lại và khớp từng chữ câu đuôi khóa.
- **Chỉ số 5 — Thuần túy động học trong khung `25–38 từ/dòng` (`100%`):** Ngắn gọn, súc tích, tập trung hoàn toàn vào chuyển động 5 giây.
