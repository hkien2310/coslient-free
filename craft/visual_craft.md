# 🎨 VISUAL CRAFT — BỘ SINH KHO NGUYÊN LIỆU THỊ GIÁC (VISUAL POOL)
v10.0 — Ponytail Edition

> **Mục tiêu:** Sinh trực tiếp danh sách prompt vào `image.txt` để tool (`dola-auto-download`) tải ảnh về phục vụ dựng phim tự do (Montage). Số lượng prompt hoàn toàn tự do theo độ dài bài hát và nhu cầu dựng.

---

## 1. NGUYÊN TẮC TỰ DO ĐA DẠNG HÓA (AI TỰ FILL)
Khi viết prompt, AI tự do biến hóa tổ hợp đa dạng theo 3 trục:
* **Cỡ cảnh:** Trải từ siêu rộng (`extreme wide shot`), rộng (`wide shot`), trung cảnh sinh hoạt (`medium shot`), đến cận cảnh tĩnh vật (`close-up shot` — *dùng chắt chiu*).  
  🚫 **Khóa cứng:** Tuyệt đối cấm `macro` và cấm `extreme close-up`.
* **Góc nhìn:** Tự do biến chuyển (ngang mắt, nhìn chếch từ trên cao sa bàn, hoặc bóng lưng nhìn ra xa).
* **Chủ thể:** Luân chuyển tự nhiên giữa cảnh quan thiên nhiên, kiến trúc phố xá, con người sinh hoạt đời thường, vật nuôi và đồ vật xúc giác.

---

## 2. CÔNG THỨC & RÀO CHẮN KỸ THUẬT

Mọi prompt trong `image.txt` tuân thủ:
```text
[Cỡ cảnh & Góc máy], [Lát cắt chủ thể/bối cảnh trên sân khấu 1-idea.md], [Ánh sáng], [Style Suffix từ style/*.md] --ar 16:9
```

### 4 Điều kiện kỹ thuật cho Tool:
- [ ] **1 dòng duy nhất:** Mỗi prompt nằm trọn vẹn trên 1 dòng.
- [ ] **Cách dòng:** Giữa 2 prompt liên tiếp cách nhau đúng 1 dòng trống.
- [ ] **Sạch cú pháp:** Không thừa dấu phẩy, không 2 dấu phẩy cạnh nhau, không dùng cờ `--no`.
- [ ] **Tỷ lệ video:** Kết thúc bằng `--ar 16:9`.
