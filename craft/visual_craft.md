# Visual Craft: Đạo diễn Storyboard & Chuỗi khung hình (`character.md` & `storyboard.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` và `timestamps.txt` để thiết lập hồ sơ nhân vật `character.md` và đạo diễn bảng phân cảnh `storyboard.md` (hoạt động sống có mục đích thực tế, tương tác nhân-quả trong khung hình, đường cong năng lượng theo cấu trúc nhạc, tỷ lệ 70/30 cùng 4 động cơ chất ngông, bố cục không gian, ma trận góc máy và luật đảo nhịp $N \to N+1$). Toàn bộ nguyên lý chất liệu sa bàn stop-motion trực quan, công thức nén nhận diện 4 trục và khung câu lệnh 4 khối tiếng Anh cho `character.md` / `image.txt` nằm độc lập tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra

- **Đầu vào:** `1-idea.md`, `3-lyrics.txt` và `timestamps.txt`.
- **Đầu ra:**
  - **`character.md`:** Danh sách nhân vật cố định viết bằng `@Tên` kèm mô tả ngoại hình (nếu có). Nhân vật xuất hiện lẻ ở cảnh nào thì tả trực tiếp ở cảnh đó.
  - **`storyboard.md`:** Bảng mạch chuyện bằng chữ khớp 1:1 số dòng và mốc giờ với `timestamps.txt` theo 4 cột (duyệt xong dịch 1:1 sang `image.txt` theo [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md)):

| Cảnh & Giờ | Đoạn nhạc & Lời hát | Thông số đạo diễn (Cỡ, Góc, Bối cảnh, Chuyển động) | Nhân vật, Hành động ở giây 0 & Ánh sáng |
| :--- | :--- | :--- | :--- |
| 01 (00:00-00:04) | [Lời hát / Nhạc] | Cỡ: [...]<br>Góc: [...]<br>Bối cảnh: [...]<br>Chuyển động: [Hướng máy + Hành động lớn 1 chiều + Cảm xúc cảnh] | [Mô tả nhân vật + Biểu cảm, dáng điệu & 1 hành động ở giây 0 + Ánh sáng] |

---

## 2. Luật Kịch Bản & Kỹ Thuật Giữ Chân Người Xem (`storyboard.md`)

- **1. Hook 15 giây đầu (`0:00–0:15` / Cảnh 1–3) — Chọn 1 trong 2 cách (hoặc kết hợp):**
  - **Cách 1 — Bắt mắt / Choáng ngợp:** Mở ngay bằng khung cảnh thị trấn siêu thực kỳ lạ, ấn tượng nhất (khớp lời hứa ở Tiêu đề/Thumbnail).
  - **Cách 2 — Gây tò mò / Khó hiểu:** Mở ngay bằng một hành động hoặc tình huống kỳ lạ đang diễn ra lưng chừng khiến người xem phải tự hỏi *"Ủa họ đang làm cái gì thế? Chuyện gì đang xảy ra ở đây?"*.
  - Cảnh 2–3 đổi ngay cỡ cảnh và góc nhìn để đi sâu vào hành động đó, giữ người xem ở lại tìm câu trả lời.
- **2. Chuỗi tình huống Nhân-Quả 2–3 cảnh (`Micro-Arcs`):** Gom các cảnh liên tiếp thành từng cụm tình huống nhỏ có diễn biến: **Khởi phát hành động $\to$ Gặp gỡ / Tương tác $\to$ Phản ứng cảm xúc / Kết quả** để người xem luôn muốn xem cảnh tiếp theo.
- **3. Làm mới thị giác mỗi khi chuyển đoạn nhạc (`Pattern Interrupt` mỗi 20–30 giây):** Mỗi khi sang đoạn nhạc mới (`Intro`, `Verse`, `Chorus`, `Solo`, `Bridge`), mở khóa một góc không gian/nét kỳ diệu mới của thị trấn hoặc đổi quy mô khung hình (từ góc hẹp ấm cúng mở bừng ra đại cảnh thoáng rộng, hoặc ngược lại) để giữ sự chú ý giữa bài.
- **4. Đảo nhịp liên cảnh ($N \to N+1$):** Hai cảnh sát nhau khác nhau rõ rệt về bối cảnh, cỡ cảnh (Toàn $\leftrightarrow$ Trung/Cận), góc máy và hành động; đan xen hợp lý giữa cảnh có người tương tác và cảnh tĩnh vật/không gian (`B-roll`) theo nhịp nhạc.
- **5. Gieo và Gặt chi tiết (`Setup & Payoff`):** Cài một chi tiết, đồ vật hoặc nhân vật ở đầu/giữa bài để gặp lại hoặc hoàn thành ý nghĩa ở cuối bài; đồng thời chuyển ý nghĩa câu hát thành tình huống cụ thể và đặt đúng các chi tiết đắt giá của `1-idea.md` vào mốc giờ tương ứng.
- **6. Đỉnh cảm xúc & Dư âm kết bài (`Peak-End Rule`):** Đặt khung hình siêu thực đẹp nhất và cử chỉ tình người xúc động nhất ở cao trào cuối bài (`Bridge / Chorus cuối`), sau đó hạ nhịp êm ái ở `Outro` để khép lại trọn vẹn hành trình từ Cảnh 1.

---

## 3. Luật Hình Ảnh & Thế Giới

- **Luật Siêu thực:** Nét kỳ lạ, siêu thực của thị trấn mọc ra từ câu chuyện của bài hát; nhân vật sống và sinh hoạt bên trong không gian đó.
- **Luật Tối giản:** Mỗi cảnh tập trung vào 1 ý tưởng hình ảnh rõ ràng trong không gian thoáng rộng, có thể xóa phông hậu cảnh khi cần làm nổi bật chủ thể.
- **Luật Đa dạng:** Đa dạng góc máy, bố cục, bối cảnh và cỡ cảnh (từ cận cảnh đến siêu rộng — mang tính tham khảo, tự do sáng tạo hoặc thay đổi thêm theo cảnh); mỗi nhân vật có ngoại hình và màu trang phục riêng.
- **Luật Tự nhiên:** Biểu cảm, dáng điệu, hành động và sự tương tác tâm tình giữa các nhân vật tự nhiên, đa dạng như đời sống hằng ngày; ở giây 0 mỗi nhân vật thực hiện 1 hành động rõ ràng làm đà cho chuyển động một chiều.
- **Luật Cỡ cảnh & Tỷ lệ vật lý:**
  - Dùng cỡ bán thân hoặc trung cận khi nhân vật ở trong không gian có vách che phần dưới hoặc khi lấy cận biểu cảm.
  - Dùng cỡ toàn thân thấy đủ trang phục đến giày chạm sàn/đất khi nhân vật ở không gian mở hoặc phòng rộng.
  - Nhà cửa và phương tiện có kích thước thật cao lớn hơn đầu người.
- **Luật Ánh sáng:** Mỗi cảnh có 1 nguồn sáng chính chiếu theo 1 hướng; ánh sáng chuyển dịch mượt theo thời gian câu chuyện.
