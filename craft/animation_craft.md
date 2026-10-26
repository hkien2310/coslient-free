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
- **Chủ thể Neo trụ Hành động 1 Chiều & Môi trường Mang Chuyển động Chính (`Anchored Subject & Environmental Motion`):**
  - Giữ nhân vật hoặc phương tiện ở vị trí neo trụ ổn định trong không gian và chỉ thực hiện 1 cử chỉ tay/chân/đầu tiếp diễn theo 1 hướng duy nhất từ tư thế gốc trong ảnh, đồng thời trao biên độ chuyển động liên tục cho các yếu tố môi trường xung quanh (làn gió lay động mái tóc bông và tà trang phục, mặt nước gợn sóng, làn hơi ấm bay lên, ánh sáng và tán cây đung đưa) để khung hình sống động và mượt mà về mặt vật lý.
- **Biểu cảm chuyển biến 2 nhịp (`Trạng thái A -> then -> Trạng thái B`):**
  - Luôn mô tả **sự thay đổi nét mặt và ánh mắt qua 2 nhịp nối tiếp tự nhiên** gắn liền với cử chỉ cơ thể của nhân vật suốt thời lượng cảnh.
