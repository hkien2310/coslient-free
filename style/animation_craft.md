# 🎬 ANIMATION CRAFT — QUY CHUẨN CHUYỂN ĐỘNG VIDEO

> **Mục tiêu:** Viết prompt chuyển động riêng cho từng ảnh đã tạo thành công, để render clip 8s qua Veo3/Kling.

---

## 1. ĐẦU VÀO

* Dựa trên image.txt hoặc ảnh thực tế (có STT).
* **Viết prompt animation cho tất cả** — kể cả ảnh thiếu (vì đã có prompt ảnh).
* **Kiểm tra mismatch:** So khớp list ảnh thực tế với image.txt. Ảnh nào thiếu → báo user tự tạo lại. Nếu prompt ảnh gốc có vấn đề → viết lại prompt ảnh thay thế.

---

## 2. CÔNG THỨC PROMPT CHUYỂN ĐỘNG

```
[Camera — kiểu di chuyển, tốc độ, điểm bắt đầu → điểm kết thúc] +
[Nhân vật — hành động, cử chỉ, biểu cảm] +
[Môi trường — gió, ánh sáng, khói, lá, nước...] +
[Kỹ thuật — fps, motion style]
```

---

## 3. NGUYÊN TẮC

* **One-take:** Mỗi prompt là 1 cú máy liền mạch. Không chia mốc giây (0-3s, 3-6s...).
* **Đa dạng camera:** Không lặp cùng kiểu chuyển động máy giữa các shot liên tiếp.
* **Tốc độ theo cảnh:** Camera chậm nhẹ cho cảnh tĩnh lặng, nhanh hơn cho cảnh sôi động.
* **Chuyển động nhân vật (QUAN TRỌNG NHẤT):** Mô tả cực kỳ chi tiết — từng cử chỉ, hướng quay đầu, tay đang làm gì, trọng tâm cơ thể dịch chuyển ra sao. Không viết chung chung "gentle movement" hay "subtle motion".
* **Môi trường sống:** Gió, khói bếp, lá rụng, sóng nước, bụi vàng... — tùy cảnh.

---

## 4. ĐẦU RA: `animation.txt`

File chỉ chứa prompt tiếng Anh theo thứ tự, mỗi prompt tương ứng 1 ảnh đã đánh STT:

```
[Prompt chuyển động shot 1]

[Prompt chuyển động shot 2]

[Prompt chuyển động shot 3]

...
```
