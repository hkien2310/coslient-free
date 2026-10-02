# Style Feedback Guide — Quy trình Chẩn đoán & Sửa lỗi Hình ảnh

Tài liệu hướng dẫn xử lý khi ảnh render ra bị lỗi. Nguyên tắc cốt lõi: **sửa câu dương (positive prompt), không thêm từ cấm**.

---

## 1. Quy trình Chẩn đoán (3 bước)

### Bước 1: Xác định triệu chứng
Mô tả ngắn gọn cái gì sai trong ảnh (da nứt, đầu to, tóc rối, chất liệu lạ...).

### Bước 2: Truy tìm từ khóa gốc
Đọc prompt đã dùng và **Suffix** trong file style tương ứng (ví dụ: `STYLE_handcrafted_tactile_diorama.md`). Hỏi: *"Từ khóa nào trong câu dương đang **ra lệnh** cho AI tạo ra hiện tượng này?"*

Cách tìm:
- **Tách từng cụm trong suffix** ra riêng, đánh giá cụm nào có khả năng gây ra triệu chứng.
- **Kiểm tra xung đột:** Có 2 cụm nào đang mâu thuẫn nhau không? (AI nhận 2 lệnh trái ngược → kết quả bất ổn).
- **Kiểm tra đẩy quá đà:** Cụm nào đang bị AI hiểu theo nghĩa đen quá mạnh ở cỡ cảnh này?

### Bước 3: Sửa logic câu dương
- **Thay thế** cụm gây lỗi bằng cụm mô tả chính xác hơn ý định thực sự.
- **Loại bỏ** cụm band-aid (băng bó) nếu gốc đã sửa.
- **KHÔNG** thêm từ cấm vào Negative Prompt hay Luật cấm — nếu câu dương đúng, AI không có lý do tạo ra lỗi đó.

---

## 2. Bảng Bẫy Từ khóa đã gặp (Keyword Trap Log)

Mỗi lần phát hiện và sửa lỗi, ghi lại vào bảng này để tránh tái phạm:

| Triệu chứng | Từ khóa gốc gây lỗi | Tại sao | Đã sửa thành |
|---|---|---|---|
| Da tay nứt nẻ như đất khô, lỗ rỗ xác ướp | `sculpted matte polymer clay` (mô tả nguyên liệu thô) | AI hiểu "đất sét chưa hoàn thiện" → render vân đất, nứt nẻ, dấu dao. Ở cảnh cận, hiệu ứng bị phóng đại | `smooth painted stop-motion puppet` (mô tả thành phẩm) |
| Da tay vừa nứt vừa mịn, kết quả bất ổn | `sculpted matte polymer clay` + `velvety smooth finish` (2 lệnh đấm nhau) | AI nhận 2 tín hiệu trái ngược, chọn ngẫu nhiên mỗi lần | Bỏ cả 2, thay bằng 1 cụm nhất quán |
| Da lộ vết đục khoét, rãnh dao khắc | `subtle hand-tooled details` trong suffix | `hand-tooled` = dấu dụng cụ đục. Ở cảnh rộng: chất gỗ đẹp. Ở cảnh cận da: dao đục lên da | `finely crafted miniature details` |
| Đầu to quá khổ, thân lùn | `caricature` trong suffix (đã sửa trước đó) | `caricature` kích hoạt trọng số bobblehead trong training data | Bỏ hẳn, dùng `charmingly quirky yet endearing` |
| Nhân vật biến thành thú bông len | `chunky knit sweater` trong prompt body | AI lan truyền chất liệu len sang da, tóc, cả sa bàn | Dùng `cotton flannel`, `tweed`, `canvas` thay thế |
| Tóc râu bết dính như sợi mì đất sét | `sculpted clay hair` trong prompt | AI nặn tóc thành từng dải đất sét dính cục | Thay bằng `natural fiber hair with fine separated strands` |
| Lộ rãnh khớp cổ tay, khuỷu tay | Dùng từ `puppet` quá nhiều + bẫy từ `no joints / unjointed` | AI bắt sóng từ `joints` và vẽ ngấn khớp búp bê | Đổi Suffix sang `stop-motion figures`, tả `continuous organic arms, seamless smooth skin` |
| Trang phục thành áo thụng tu sĩ / bao tải | Dùng từ `smock` hoặc `linen dress` chung chung | `smock` là áo thụng nông dân trung cổ, váy không phom thành bao tải | Dùng trang phục thường ngày có cấu trúc (`button-down shirt`, `chinos`, `sundress with fitted waist`) |

---

## 3. Nguyên tắc khi viết/sửa từ khóa

### A. Mô tả thành phẩm, không mô tả nguyên liệu thô
- ❌ `sculpted matte polymer clay` (nguyên liệu đang nặn)
- ✅ `smooth painted stop-motion puppet` (búp bê đã sơn xong)

### B. Một ý = một cụm. Không dùng 2 cụm đấm nhau
- ❌ `polymer clay` + `velvety smooth finish` (thô + mịn)
- ✅ `smooth painted` (một tín hiệu rõ ràng)

### C. Kiểm tra từ khóa theo cỡ cảnh
Cùng một cụm từ có thể an toàn ở cảnh rộng nhưng nguy hiểm ở cảnh cận:
- `finely crafted miniature details` → cảnh rộng: chi tiết sa bàn ✅ / cảnh cận da: vẫn ổn vì "miniature" hướng AI về đồ vật ✅
- `hand-tooled details` → cảnh rộng: vân gỗ đẹp ✅ / cảnh cận da: vết đục ❌

### D. Tránh gắn từ chất liệu thô vào bộ phận cơ thể
- ❌ `clay hand`, `weathered clay`, `sculpted clay fingers`
- ✅ `puppet hands with smooth painted finish`

### E. Khi sửa xong gốc → dọn dẹp band-aid
Nếu câu dương đã sửa đúng, quay lại xóa:
- Từ cấm trong Negative Prompt mà chỉ tồn tại để chống triệu chứng cũ.
- Luật cấm trong mục "Luật cấm" mà chỉ mô tả triệu chứng chứ không phải nguyên tắc thiết kế.
