# 🎨 VISUAL CRAFT — BỘ SINH KHO NGUYÊN LIỆU THỊ GIÁC (VISUAL POOL)
v10.0 — Ponytail Edition

> **Mục tiêu:** Sinh trực tiếp danh sách prompt vào `image.txt` để tool (`dola-auto-download`) tải ảnh về phục vụ dựng phim tự do (Montage). Số lượng prompt hoàn toàn tự do theo độ dài bài hát và nhu cầu dựng.

---

## 1. NGUYÊN TẮC TỰ DO ĐA DẠNG HÓA & RULE THOÁNG
Khi viết prompt, AI tự do biến hóa tổ hợp đa dạng theo các trục cốt lõi:
* **Rule Thoáng & Không gian mở (BẮT BUỘC):** Đa số là cảnh ngoài trời lộng gió hoặc không gian mở. Nếu ở trong nhà: bắt buộc mở toang cửa sổ vòm lớn (panoramic window) hoặc hiên nhà nhìn ra thiên nhiên bao la ngập nắng. Tối thiểu 40% diện tích là khoảng nghỉ thị giác (`generous negative space`), cấm nhồi nhét đồ đạc (`anti-clutter`).
* **Điểm neo vàng nhỏ tinh tế:** Mọi khung hình luôn có một chi tiết nhỏ mang sắc vàng ấm (`antique mustard / buttercup yellow / amber brass`, chiếm ~2-5% khung hình, kín đáo: cúc áo, ruy băng nhỏ, hoa dại, dây đồng hồ quả quýt).
* **Cỡ cảnh:** Trải từ siêu rộng (`extreme wide shot`), rộng (`wide shot`), trung cảnh sinh hoạt (`medium shot`), đến cận cảnh tĩnh vật (`close-up shot` — *dùng chắt chiu*).  
  🚫 **Khóa cứng:** Tuyệt đối cấm `macro` và cấm `extreme close-up`.
* **Góc nhìn & Chủ thể:** Tự do luân chuyển tự nhiên giữa thiên nhiên thật, kiến trúc mộc, con người và sinh vật sống động (len nỉ).

---

## 2. CÔNG THỨC 7 KHỐI CHUẨN HÓA

Mọi prompt trong `image.txt` tuân thủ nghiêm ngặt 7 khối trên 1 dòng:
```text
[1. Cỡ cảnh & Mở rộng] + [2. Danh tính (Token Inversion)] + [3. Khóa neo đất sét (#2)] + [4. Tóc & Trang phục dệt + Điểm neo vàng nhỏ] + [5. Hành động tối giản & Tầm nhìn ngoài trời] + [6. Rule thoáng & Nắng tươi sáng] + [7. Suffix chuẩn --ar 16:9]
```

### 5 Điều kiện kỹ thuật cho Tool:
- [ ] **Rà soát bẫy từ khóa:** Bắt buộc tuân thủ 100% các từ cấm và từ thay thế tại [`style/IMAGE_AVOID_CASES.md`](../style/IMAGE_AVOID_CASES.md) (chống lùn/tròn, cấm quần áo đất sét, áp dụng Token Inversion chống trùng lặp nhân vật trên Meta AI).
- [ ] **1 dòng duy nhất:** Mỗi prompt nằm trọn vẹn trên 1 dòng.
- [ ] **Cách dòng:** Giữa 2 prompt liên tiếp cách nhau đúng 1 dòng trống.
- [ ] **Sạch cú pháp:** Không thừa dấu phẩy, không 2 dấu phẩy cạnh nhau, không dùng cờ `--no`.
- [ ] **Tỷ lệ video:** Kết thúc bằng `--ar 16:9`.
