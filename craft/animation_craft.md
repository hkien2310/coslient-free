# ANIMATION CRAFT — KỸ THUẬT CHUYỂN ĐỘNG VIDEO (I2V)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào trực tiếp từ `image.txt` để xuất file `prompt-animate.txt`, điều khiển **chuyển động của ống kính một trục và hành động tiếp diễn của chủ thể trong 5 giây tiếp theo**. File `image.txt` đã khóa trọn vẹn tạo hình, tư thế gốc, vật dụng, màu sắc, chất liệu và bối cảnh ở giây 0.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra (`prompt-animate.txt`)

- **Đầu vào:** `image.txt` và `storyboard.md`.
- **Đầu ra (`prompt-animate.txt`):** Mỗi cảnh 1 dòng tiếng Anh khớp 1:1 thứ tự dòng với `image.txt`:

```text
# Với cảnh có người:
[Chuyển động máy quay 1 trục + hướng rõ ràng]. [Chủ thể thực hiện 1 hành động tay/chân 1 chiều] and [1 động từ biểu cảm gương mặt / ánh mắt / cử động đầu cụ thể: smiles warmly / nods gently / glances fondly / blinks softly...], while [chuyển động nhẹ của gió/ánh sáng/vạt áo] in a [sắc thái cảm xúc cảnh] mood.

# Với cảnh tĩnh vật / không gian (completely without people):
[Chuyển động máy quay 1 trục + hướng rõ ràng]. [Vật thể / yếu tố thiên nhiên chuyển động êm ái theo 1 nhịp tự nhiên] in a [sắc thái cảm xúc cảnh] mood.
```

---

## 2. Luật Đầu Ra (`prompt-animate.txt`)

- **Đồng bộ 1:1 với `image.txt`:** Khớp chính xác số lượng người, danh từ chủ thể, tư thế ở giây 0 (`t = 0s`) và đạo cụ/phương tiện của từng dòng trong `image.txt`.
- **Chuyển động máy quay 1 trục & Đảo nhịp ($N \to N+1$):** Mở đầu bằng hướng di chuyển 1 trục rõ ràng của máy quay (`holds steady`, `pans slowly left/right`, `tilts gently up/down`, `moves slowly closer`, `pulls slowly back`, `glides laterally`, `rises gently`, `follows alongside`); hai cảnh sát nhau ($N \to N+1$) dùng chuyển động máy khác nhau theo `storyboard.md`.
- **Một hành động lớn 1 chiều:** Mỗi nhân vật hoặc phương tiện chỉ thực hiện 1 hành động chính tiếp diễn theo 1 hướng duy nhất từ tư thế giây 0 để cơ thể không bị biến dạng.
- **Động từ biểu cảm gương mặt & Ánh mắt trực tiếp (Chống đơ mặt nhân vật Stop-Motion):**
  - Vì nhân vật trong ảnh là rối Stop-Motion (`paper-pulp skin`), mô hình AI sẽ giữ cứng đơ mặt nhân vật nếu chỉ viết câu chung chung kiểu *"facial expressions move naturally"*.
  - Bắt buộc dùng **động từ biểu cảm, ánh mắt và cử động đầu cụ thể** ngay trong câu hành động của nhân vật (như `smiles warmly`, `nods gently`, `turns head and looks fondly at...`, `blinks softly with a tender smile`, `laughs softly`) để kích hoạt cơ mặt và ánh mắt sống động trong 5 giây.
