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
  - **`character.md` *(Tùy chọn)*:** Mô tả trực tiếp nhân vật mới ngay tại từng cảnh độc lập trong `storyboard.md` và `image.txt` để mỗi bức ảnh là một lát cắt độc bản; chỉ dùng `character.md` khi cần lưu hồ sơ tham khảo riêng.
  - **`storyboard.md`:** Mở đầu bằng **1 dòng khóa `Địa điểm, Quy luật & Kiến trúc kỳ lạ của thị trấn`**, sau đó triển khai theo **Quy trình 2 Tầng (`Quy hoạch Đại Cảnh` $\to$ `Triển khai Tiểu Cảnh độc lập`)** khớp 1:1 số dòng và mốc giờ với `timestamps.txt` (duyệt xong dịch 1:1 sang `image.txt` theo [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md)):
    1. **Phần 1 — Quy hoạch Đại Cảnh theo Phân đoạn nhạc (`Macro-Sequence Blueprint`):** Xác lập mục tiêu cảm xúc, cơ chế tạo Điểm sai siêu thực, công trình kiến trúc điểm nhấn, nhân vật mới và điểm `Hook / Mini-Hook` cho từng phân đoạn (`Intro`, `Verse`, `Pre-Chorus`, `Chorus`, `Vocalise / Interlude`, `Bridge`, `Outro`).
    2. **Phần 2 — Bảng Tiểu Cảnh (`Micro-Scenes`):**

| Cảnh & Giờ | Đoạn nhạc & Lời hát | Vai trò Giữ chân, Lý do nối cảnh & Thông số (Cỡ, Góc, Bối cảnh, Chuyển động) | Nhân vật, Khoảnh khắc hành động & Ánh sáng |
| :--- | :--- | :--- | :--- |
| 01 (00:00-00:04) | [Lời hát / Nhạc] | Vai trò & Nối cảnh: [Hook / Mini-Hook / Bồi tiếp Cảnh trước như thế nào & Tại sao]<br>Cỡ: [...] \| Góc: [...]<br>Bối cảnh: [...]<br>Chuyển động: [Hướng máy + Diễn biến hành động + Cảm xúc cảnh] | [Mô tả nhân vật + Biểu cảm, dáng điệu & khoảnh khắc hành động đang diễn ra + Ánh sáng] |

---

## 2. Quy Trình Thực Chiến 2 Tầng & Kỹ Thuật Giữ Chân (`storyboard.md`)

- **1. Tầng 1 — Chia Đại Cảnh theo Phân đoạn Nhạc (`Macro-Blocks`):**
  - Mỗi phân đoạn bài hát là một Đại Cảnh mang một nhiệm vụ giải quyết vấn đề giữ chân rõ ràng:
    - **`Intro` (Hook tổng lực):** Gây ấn tượng thị giác mạnh mẽ và đánh thức trí tò mò ngay giây đầu tiên để giữ người nghe và người xem ở lại.
    - **`Verse 1` (Khởi phát câu chuyện):** Mở lời bằng hình ảnh trả lời sự tò mò của `Intro` và dẫn dắt người xem vào tâm tình chủ đạo.
    - **`Pre-Chorus` (Đà nâng năng lượng):** Chuyển dịch không gian và nhịp điệu để tích lũy sự háo hức trước điểm bùng nổ.
    - **`Chorus` (Bung mở thế giới & Thông điệp):** Mở rộng biên độ thị giác của thị trấn siêu thực, lan tỏa cảm xúc của câu `Hook` qua nhiều góc nhìn và con người.
    - **`Verse 2` (Đổi mới không gian & Giữ nhịp giữa bài):** Mở ra bối cảnh mới và hoạt động tương tác mới để làm tươi mới trải nghiệm thị giác.
    - **`Vocalise / Interlude` (Đỉnh cao chất thơ thị giác):** Dành những khung hình siêu thực kỳ diệu và giàu cảm xúc nhất cho đoạn nhạc ngân giai điệu.
    - **`Bridge` & `Final Chorus` (Điểm lắng nội tâm $\to$ Cao trào trọn vẹn):** Thu cận vào chiều sâu gắn kết giữa người với người ở `Bridge` rồi bung ra đại cảnh ấm áp nhất ở `Final Chorus`.
    - **`Outro` (Gặt lại chi tiết & Dư âm):** Khép vòng câu chuyện bằng hình ảnh đọng lại sự bình yên sâu lắng.
  - **Sự linh hoạt của Đại Cảnh:** Một Đại Cảnh là một khối chủ đề và cảm xúc thống nhất, bên trong gồm các Tiểu Cảnh là những lát cắt độc lập qua những con người, ngôi nhà, khu vườn và công trình khác nhau cùng cộng hưởng chung một nhịp sống của thị trấn.
- **2. Tầng 2 — Triển khai Tiểu Cảnh Độc lập theo Nhịp sóng `Hook -> Bồi tiếp Cảm xúc -> Mini-Hook` (`Micro-Scenes`):**
  - **Mở đầu mỗi Đại Cảnh bằng `Hook` hoặc `Mini-Hook`:** Cảnh đầu tiên của mỗi phân đoạn luôn tung ra một khung hình đẹp mắt choáng ngợp hoặc một tình huống gây hiếu kỳ để neo chặt ánh nhìn.
  - **Mỗi Tiểu Cảnh tiếp theo là 1 Lát cắt Độc lập nối mạch Cảm xúc (`Cảnh N -> Cảnh N+1`):** Mỗi cảnh kế tiếp mở ra một góc không gian mới và nhân vật mới độc lập, đồng thời xác định rõ lý do xuất hiện và cách nó bồi tiếp, giải thích hoặc mở rộng cảm xúc từ cảnh ngay trước đó trong cùng một thế giới lớn.
- **3. Bước nhảy Không gian & Đảo nhịp Góc máy ($N \to N+1$):**
  - Khi chuyển từ Cảnh $N$ sang Cảnh $N+1$, chủ động chuyển đổi vị trí không gian/điểm nhìn, đổi cỡ cảnh (Toàn $\leftrightarrow$ Trung/Cận) và luân phiên đổi độ cao góc máy (Góc ngang tầm mắt `Eye-level` $\leftrightarrow$ Góc thấp hất lên `Low-angle` $\leftrightarrow$ Góc cao nhìn xuống `High-angle` $\leftrightarrow$ Góc qua vai `Over-the-shoulder POV` $\leftrightarrow$ Góc xuyên khung tiền cảnh `Framed-through`) sau khi đã khóa chắc lý do nối cảnh.

---

## 3. Luật Hình Ảnh & Thế Giới

- **Luật Công thức Siêu thực (`1 Điểm sai + 1 Hành động thản nhiên = Siêu thực`):**
  - **Nguyên lý cốt lõi:** Đặt trên nền kiến trúc đời thực cổ điển trầm ấm và chất liệu ký ức của người trưởng thành, mỗi khung hình kết hợp **1 Điểm sai duy nhất** với **1 việc làm đời thường ở nhịp độ chậm**, nơi nhân vật đón nhận điều kỳ lạ bằng thái độ thản nhiên, thân thuộc và ấm áp như nhịp sống tự nhiên hàng ngày.
  - **5 Cơ chế tạo Điểm sai (Luân phiên qua các Đại Cảnh để tạo `Hook / Mini-Hook` và kiến trúc thị trấn):**
    1. **Lai ghép (`Ngoại hình bên Nhỏ/Mềm + Tính chất bên Lớn/Vững`):** Ghép hai thực thể bằng cách lấy ngoại hình của thực thể nhỏ hoặc mềm đắp vào thực thể lớn hoặc vững chãi, đồng thời giữ nguyên tính chất vật lý của bên lớn hơn (giữ tính tĩnh tại để ở của công trình kiến trúc hoặc tính gợn sóng bồng bềnh của mặt biển/cảnh quan).
    2. **Phóng đại (`Phóng to vượt bậc 1 thực thể duy nhất theo 2 nhánh`):**
       - *Nhánh Đồ vật quen thuộc:* Phóng đại kích thước và đổi công năng thành công trình kiến trúc, nơi trú ẩn hoặc phương tiện.
       - *Nhánh Sinh vật nhỏ bé hiền lành:* Phóng đại kích thước với đường nét thủ công bo tròn mềm mại và giữ nguyên tính chất là người bạn sinh vật hiền hòa để con người tựa vào hoặc bầu bạn.
    3. **Vật thể hóa tự nhiên (`1 hiện tượng tự nhiên + đối xử như vật cầm nắm được`):** Chuyển hóa hiện tượng tự nhiên nhẹ nhàng thành chất liệu thủ công hữu hình để nhân vật nâng niu và bầu bạn.
    4. **Lạc quẻ không gian (`1 vật dụng riêng tư + đặt giữa thiên nhiên bao la`):** Đặt một góc nội thất đơn lẻ, tối giản và mang tính an ủi giữa cảnh quan thiên nhiên rộng lớn.
    5. **Tọa độ siêu thực (`Tự nhiên nguyên bản + đặt ở tọa độ đặc biệt`):** Đặt cấu trúc tự nhiên hoặc công trình giữ nguyên tính chất vật lý ở cao độ lơ lửng với trọng lực tĩnh lặng.
- **Luật Lát cắt Độc lập trong Cùng một Thế giới Lớn:** Mỗi bức ảnh (mỗi Tiểu Cảnh) là một lát cắt độc lập với nhân vật, trang phục, công trình và góc không gian riêng biệt để tối đa hóa sự đa dạng thị giác; đồng thời tất cả các lát cắt đều gắn kết chặt chẽ trong cùng một thế giới thị trấn thống nhất qua quy luật siêu thực định danh, tiến trình ánh sáng và mạch cảm xúc của bài hát.
- **Luật Tối giản:** Mỗi cảnh tập trung vào 1 ý tưởng hình ảnh rõ ràng trong không gian thoáng rộng, có thể xóa phông hậu cảnh khi cần làm nổi bật chủ thể.
- **Luật Đa dạng & Chiều sâu Điện ảnh:** Luân phiên đa dạng góc độ cao-thấp của máy quay (góc ngang tầm mắt kết nối cảm xúc, góc thấp hất lên, góc cao nhìn xuống, góc nhìn qua vai, góc nhìn xuyên qua tiền cảnh) cùng bố cục nhiều lớp tiền-trung-hậu cảnh và cỡ cảnh.
- **Luật Cảm xúc & Ý nghĩa:** Mỗi khung hình đặt trạng thái nội tâm, ánh mắt, nụ cười và ý nghĩa của sự gắn kết giữa người với người làm trung tâm, nơi hành động là sự bộc lộ cảm xúc tự nhiên giữa đời sống.
- **Luật Cỡ cảnh & Tỷ lệ vật lý:**
  - **Ở Đại cảnh / Toàn cảnh rộng (`Extreme wide / Wide panoramic`):** Đặt trọng tâm vào quy mô đồ sộ của công trình kiến trúc siêu thực và thiên nhiên; giữ vắng người hoặc chỉ điểm xuyết bóng người nhỏ bé ở xa (`tiny distant silhouette`) để bảo toàn tỷ lệ kiến trúc khổng lồ.
  - **Ở Trung cảnh (`Medium-wide full-body`):** Đặt 1–2 nhân vật ở cự ly vừa phải thấy đủ trang phục đến giày chạm mặt phẳng trong không gian mở.
  - **Ở Trung cận / Bán thân (`Medium close-up / Waist-up`):** Dùng khi nhân vật đứng sau vách che phần dưới hoặc khi tập trung vào biểu cảm gương mặt và đôi tay.
- **Luật Ánh sáng:** Mỗi cảnh có 1 nguồn sáng chính chiếu theo 1 hướng; ánh sáng chuyển dịch mượt theo thời gian câu chuyện.
