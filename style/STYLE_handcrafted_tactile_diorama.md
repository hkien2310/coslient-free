# 🎨 QUY CHUẨN THỊ GIÁC — TACTILE STOP-MOTION DIORAMA
v28.0 — Chỉ Dẫn Tinh Gọn, Tự Do Sáng Tạo & Đa Dạng Tiêu Cự

---

## 1. THẾ GIỚI QUAN (DIORAMA IN REAL NATURE)
* **Vật thể nhân tạo (Con rối, Nhà cửa, Đồ đạc):** Chế tác thủ công tí hon từ len nỉ ghim kim, gỗ mộc gọt đẽo, gốm men rạn, tường vôi đá mộc (`needle-felted puppet, handcrafted miniature stonework, carved timber`).
* **Môi trường tự nhiên:** Thiên nhiên điện ảnh thực tế 100% (sóng nước thật, mây trời thật, rặng núi, đồi cỏ bạt ngàn). Tuyệt đối không làm cảnh nền giả lập bằng len thô.

---

## 2. HỆ THỐNG CỠ CẢNH

| Cỡ cảnh | Ghi chú |
| :--- | :--- |
| **Siêu rộng** | Bao quát toàn cảnh không gian lớn |
| **Toàn cảnh** | Nhân vật + môi trường xung quanh |
| **Trung cảnh** | Nhân vật từ thắt lưng trở lên hoặc toàn thân |
| **Cận cảnh** | Bàn tay, đồ vật, hoặc biểu cảm khuôn mặt |
| **Siêu cận** | Chi tiết nhỏ — cẩn thận tránh lộ xơ len |

---

## 3. GÓC MÁY

1. Từ trên cao nhìn xuống
2. Toàn cảnh chân trời / mép không gian
3. Ngang tầm mắt
4. Từ mặt đất nhìn lên
5. Chính diện
6. 3/4 trước
7. Nghiêng cạnh (profile)
8. 3/4 sau / sau lưng
9. Nghiêng điện ảnh (Dutch angle)


## 4. TẠO HÌNH NHÂN VẬT

* **Tỷ lệ cơ thể:** Dáng người cao gầy, thanh mảnh, tứ chi thon dài. Tránh dáng mập tròn kiểu búp bê.
* **Khuôn mặt:** Sống mũi và vành tai hơi to hơn một chút, nét mặt đôn hậu, da len nỉ mịn.
* **Mái tóc:** Tóc dày phủ kín chân tóc. Hạn chế mũ phẳng che đầu.
* **Trang phục:** Vải mộc tự nhiên, cổ điển. Tránh lạm dụng áo len dệt kim dày cộp và đồ hiện đại.

---

## 5. HÀNH ĐỘNG TRONG PROMPT

* Ưu tiên nhân vật đang **làm gì đó** thay vì đứng/ngồi nhìn thụ động.

---

## 6. AN TOÀN TỪ KHÓA (SAFETY FILTER)
* **Chống mắt hạt cườm vô hồn:** CẤM `bead eyes, button eyes, glass beads`. Bắt buộc dùng `expressive sculpted stop-motion eyes with detailed pupils`.
* **Chống búp bê hóa đồ vật & thú bông:** CẤM gán chữ `needle-felted` vào đồ vật và con vật (`needle-felted cup, needle-felted bird`...). Cốc chén, bàn ghế, chim muông phải dùng chất liệu mộc tự nhiên (`ceramic, timber, real birds`). Chỉ dùng `handcrafted needle-felted stop-motion diorama style` ở cuối prompt làm phong cách nền.
* **Chống bẫy AI hiểu nghĩa đen:** CẤM dùng từ thức ăn hay đồ vật khi tả mặt (`potato, pear, button, beak`...). Chỉ dùng thuật ngữ hình khối điêu khắc thuần túy (`slightly oversized sculpted nose`, `slightly larger sculpted ears`, `plump cheeks`).
* **Chống chặn lệnh an toàn (Safety Filter):** CẤM `knife, blade` khi tả thao tác gọt đẽo ➔ Thay bằng `sculpting tool, carving gouge`.
* **Chống Steampunk & Kim loại bóng:** CẤM `brass, copper, bronze, gears, clockwork`. Dùng vật liệu mộc hữu cơ: `carved timber, terracotta, wrought iron, ceramic`.

---

## 7. QUY TẮC KỸ THUẬT BẮT BUỘC (PROMPT GUARDRAILS)
1. **Cảnh nào tả cái nấy (Chống nhồi nhét):**
   * *Cảnh phong cảnh / siêu rộng:* Chỉ tả kiến trúc, phố xá và thiên nhiên. Tuyệt đối không nhồi mặt người hay mắt.
   * *Cảnh tĩnh vật / thao tác tay / cận cảnh:* Chỉ tả đôi tay và đồ vật. Không tả mặt hay tóc.
   * *Cảnh bóng lưng / góc nghiêng:* Tả dáng dấp và hành động, không cần tả mắt.
   * *Cảnh trung / cận nhân vật:* Lúc này mới tả nét mặt và ánh mắt.
2. **100% câu khẳng định:** Tuyệt đối không dùng từ phủ định (`no...`, `not...`) trong prompt dương bản.
3. **Chống sinh đôi (Đa nhân vật):** Khi có 2+ nhân vật cùng giới/tuổi trong khung hình, tạo ít nhất 3 cặp tương phản bất đối xứng (tóc, chiều cao, trang phục hoặc cử chỉ).
4. **Chống lặp từ:** Không dùng lại cùng một cụm từ mô tả qua các prompt liên tiếp.
5. **Ưu tiên cô đọng:** Viết súc tích đủ ý (300 – 450 ký tự). Tránh từ thừa lặp lại làm loãng trọng số AI.

---

## 8. CÔNG THỨC PROMPT CHUẨN (IMAGE GENERATION)
```text
[Góc máy chuẩn & Cỡ cảnh] of [Chủ thể cách điệu nhẹ: mũi/tai hơi to hơn một chút, tóc dày, áo sơ mi lanh/tạp dề/gile, vi hành động], handcrafted needle-felted stop-motion diorama style, set against [Bối cảnh nội/ngoại cảnh cụ thể], [Ánh sáng tự nhiên], rich tactile craft textures --ar 16:9
```
