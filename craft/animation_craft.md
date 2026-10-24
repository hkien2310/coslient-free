# ANIMATION CRAFT — KỸ THUẬT CHUYỂN ĐỘNG VIDEO (I2V)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào trực tiếp từ `image.txt` để xuất file `prompt-animate.txt`, điều khiển **chuyển động của ống kính một trục và hành động tiếp diễn của chủ thể trong 5 giây tiếp theo**. File `image.txt` đã khóa trọn vẹn tạo hình, tư thế gốc, vật dụng, màu sắc, chất liệu và bối cảnh ở giây 0.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Quy chuẩn file `prompt-animate.txt` và Cấu trúc 3 phần tối giản

- **Định dạng xuất bản:** Mỗi câu lệnh nằm trọn vẹn trên **1 dòng duy nhất** trong `prompt-animate.txt`, xếp khớp đúng thứ tự từng bức ảnh tương ứng trong `image.txt`.
- **Ba thành phần cốt lõi của một dòng lệnh chuyển động (diễn đạt linh hoạt, tự nhiên):**

1. **Phần 1 — Chuyển động ống kính một trục có hướng rõ ràng (`Clear 1-Axis Camera Motion`):**
   - Nêu ngắn gọn trạng thái hoặc hướng di chuyển một trục của máy quay phù hợp với bố cục không gian trong ảnh gốc, luân chuyển đa dạng giữa các cảnh liền kề ($N \to N+1$):
     1. **Giữ khung tĩnh ổn định (`Static / Hold / Linger`):** Máy giữ yên vị trí để tập trung vào hành động chính trong khung hình.
     2. **Lia ngang theo hướng rõ ràng (`Slow pan left / right`):** Thân máy xoay ngang mượt mà theo hướng di chuyển của phương tiện, ánh nhìn hoặc đường dẫn không gian.
     3. **Ngẩng hoặc hạ dọc (`Gentle tilt up / down`):** Thân máy xoay dọc êm ái theo chiều cao của hành động hoặc kiến trúc.
     4. **Tiến lại gần (`Slow push-in / move closer`):** Thân máy tiến nhẹ vào chủ thể hoặc cử chỉ tương tác trung tâm.
     5. **Lùi ra xa mở không gian (`Slow pull-back`):** Thân máy lùi nhẹ để mở rộng toàn cảnh bao quanh chủ thể.
     6. **Trượt ngang hoặc đi song song (`Smooth lateral glide / follow alongside`):** Thân máy trượt ngang tạo chiều sâu thị sai hoặc đi song song cùng tốc độ và cùng hướng với chủ thể đang di chuyển.
     7. **Nâng dọc mở tầm nhìn (`Gentle crane / rise up`):** Thân máy nâng lên êm ái mở rộng tầm mắt ra cảnh quan phía xa.

2. **Phần 2 — Một chuyển động lớn duy nhất theo một hướng (`Single Unidirectional Macro Action`):**
   - **Với cảnh có người:** Gọi chủ thể ngắn gọn khớp với `image.txt` và chỉ mô tả **một hành động lớn duy nhất tiếp diễn theo một hướng rõ ràng** từ tư thế khởi đầu ở giây `0s` (như bước đều về phía trước dọc con đường, trao túi bánh qua cửa sổ, đặt chiếc giỏ lên giá, hoặc ngồi đung đưa nhẹ trên ghế). Giữ nguyên một vector chuyển động xuyên suốt 5 giây để cơ thể nhân vật vận động liền mạch và mượt mà.
   - **Với cảnh tĩnh vật hoặc phong cảnh (`B-roll`):** Lấy vật thể trung tâm hoặc yếu tố thiên nhiên trong ảnh làm chủ thể và mô tả một chuyển động vật lý tự nhiên, êm ái theo không gian sẵn có.

3. **Phần 3 — Sắc thái cảm xúc cảnh và dòng chảy tự nhiên (`Scene Mood & Natural Flow`):**
   - Kết hợp gợi mở ngắn gọn bầu không khí cảm xúc của cảnh (như bình yên, ấm áp, hoài niệm, dịu dàng, tĩnh lặng, tươi vui...) và giao phần biểu cảm gương mặt cùng môi trường xung quanh tự vận động hài hòa theo bức ảnh gốc bằng ngôn ngữ tự nhiên, linh hoạt theo từng cảnh.

---

## 2. Nguyên lý bảo toàn độ mượt và tính một chiều trong 5 giây

1. **Nguyên tắc một hướng duy nhất (`Unidirectional Momentum`):** Mỗi chủ thể trong cảnh chỉ thực hiện một hành động chính đi theo một hướng nhất quán từ đầu đến cuối cảnh, giúp hình thể và bước chân giữ được quán tính tự nhiên.
2. **Tối giản câu chữ để tập trung vào động học:** Viết câu lệnh ngắn gọn, súc tích, chỉ nêu hướng máy quay, hành động lớn và cảm xúc chung của cảnh; để bức ảnh gốc trong `image.txt` tự đảm nhận toàn bộ thông tin về trang phục, màu sắc, chất liệu và chi tiết tĩnh.
3. **Để AI tự suy diễn vi chuyển động qua cảm xúc (`Mood-Driven Micro-Motion`):** Thay vì liệt kê chi tiết từng cử động nhỏ của nét mặt, cái gật đầu hay ngọn cỏ, sử dụng sắc thái cảm xúc của cảnh kết hợp với mệnh đề chuyển động tự nhiên ở cuối câu để mô hình tự sinh nhịp thở, ánh mắt và làn gió mềm mại.

---

## 3. Gợi ý khung câu lệnh linh hoạt cho `prompt-animate.txt`

Mỗi dòng trong `prompt-animate.txt` viết ngắn gọn, linh hoạt theo ngữ cảnh từng bức ảnh:

```text
# Với cảnh có người (diễn đạt tự nhiên, linh hoạt từ ngữ theo từng cảnh):
[Chuyển động máy quay 1 trục + hướng rõ ràng]. [Chủ thể thực hiện 1 hành động lớn duy nhất theo 1 hướng], while facial expressions and everything around move naturally in a [sắc thái cảm xúc phù hợp với cảnh] mood/atmosphere.

# Với cảnh tĩnh vật / phong cảnh B-roll:
[Chuyển động máy quay 1 trục + hướng rõ ràng]. [Vật thể / yếu tố thiên nhiên chuyển động êm ái theo 1 nhịp tự nhiên], while everything around moves naturally in a [sắc thái cảm xúc phù hợp với cảnh] mood/atmosphere.
```
