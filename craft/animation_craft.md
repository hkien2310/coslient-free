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
[Chuyển động máy quay 1 trục + hướng rõ ràng]. [Chủ thể thực hiện 1 hành động tay/chân 1 chiều], [Biểu cảm/Ánh mắt nhịp 1] then [Biểu cảm/Ánh mắt nhịp 2 chuyển biến tự nhiên], while [chuyển động nhẹ của gió/ánh sáng/môi trường] in a [sắc thái cảm xúc cảnh] mood.

# Với cảnh tĩnh vật / không gian (completely without people):
[Chuyển động máy quay 1 trục + hướng rõ ràng]. [Vật thể / yếu tố thiên nhiên chuyển động êm ái theo 1 nhịp tự nhiên] in a [sắc thái cảm xúc cảnh] mood.
```

---

## 2. Luật Đầu Ra (`prompt-animate.txt`)

- **Đồng bộ 1:1 với `image.txt`:** Khớp chính xác số lượng người, danh từ chủ thể, khoảnh khắc tư thế trong `image.txt` và đạo cụ/phương tiện của từng dòng.
- **Chuyển động máy quay 1 trục & Đảo nhịp ($N \to N+1$):** Mở đầu bằng hướng di chuyển 1 trục rõ ràng của máy quay (`holds steady`, `pans slowly left/right`, `tilts gently up/down`, `moves slowly closer`, `pulls slowly back`, `glides laterally`, `rises gently`, `follows alongside`); hai cảnh sát nhau ($N \to N+1$) dùng chuyển động máy khác nhau theo `storyboard.md`.
- **Một hành động cơ thể 1 chiều:** Mỗi nhân vật hoặc phương tiện chỉ thực hiện 1 hành động tay/chân chính tiếp diễn theo 1 hướng duy nhất từ khoảnh khắc trong ảnh để cơ thể vận động mượt mà.
- **Biểu cảm chuyển biến 2 nhịp (`Trạng thái A -> then -> Trạng thái B`):**
  - Để gương mặt nhân vật sống động suốt 5–7 giây (không bị đơ cứng và cũng không giữ lì một nụ cười giả tạo từ đầu đến cuối), luôn mô tả **sự thay đổi nét mặt và ánh mắt qua 2 nhịp nối tiếp** gắn với hành động (ví dụ: *đang chăm chú nhìn xuống tay làm $\to$ ngước lên và nét mặt giãn ra ấm áp*; *đang lắng nghe trầm ngâm $\to$ khẽ chớp mắt và gật đầu thấu hiểu*; *đang nhìn xa xăm $\to$ thở nhẹ một hơi bình yên*).
