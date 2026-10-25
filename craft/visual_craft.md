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
  - **`storyboard.md`:** Triển khai theo **Quy trình 2 Tầng (`Quy hoạch Đại Cảnh` $\to$ `Triển khai Tiểu Cảnh`)** khớp 1:1 số dòng và mốc giờ với `timestamps.txt` (duyệt xong dịch 1:1 sang `image.txt` theo [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md)):
    1. **Phần 1 — Quy hoạch Đại Cảnh theo Phân đoạn nhạc (`Macro-Sequence Blueprint`):** Xác lập mục tiêu cảm xúc, cách tổ chức không gian/nhân vật và điểm `Hook / Mini-Hook` cho từng phân đoạn (`Intro`, `Verse`, `Pre-Chorus`, `Chorus`, `Vocalise / Interlude`, `Bridge`, `Outro`).
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
  - **Sự linh hoạt của Đại Cảnh:** Một Đại Cảnh là một khối chủ đề thống nhất, bên trong được tự do triển khai thành: *(a) Toàn cảnh thị trấn cắt vào những con người khác nhau*, *(b) Nhiều góc không gian cùng chủ đề qua các ngôi nhà/khu vườn khác nhau*, hoặc *(c) Chuỗi hành động nối tiếp nhau của nhân vật*.
- **2. Tầng 2 — Triển khai Tiểu Cảnh theo Nhịp sóng `Hook -> Bồi tiếp Nhân-Quả -> Mini-Hook` (`Micro-Scenes`):**
  - **Mở đầu mỗi Đại Cảnh bằng `Hook` hoặc `Mini-Hook`:** Cảnh đầu tiên của mỗi phân đoạn luôn tung ra một khung hình đẹp mắt choáng ngợp hoặc một tình huống gây hiếu kỳ để neo chặt ánh nhìn.
  - **Các Tiểu Cảnh tiếp theo nối mạch Nhân – Quả (`Cảnh N -> Cảnh N+1`):** Mỗi cảnh kế tiếp phải xác định rõ lý do xuất hiện và cách nó bồi tiếp, giải thích hoặc mở rộng cảm xúc từ cảnh ngay trước đó để duy trì sự cuốn hút liên tục cho tới `Mini-Hook` tiếp theo.
- **3. Bước nhảy Không gian & Đảo nhịp Góc máy ($N \to N+1$):**
  - Khi chuyển từ Cảnh $N$ sang Cảnh $N+1$, chủ động chuyển đổi vị trí không gian/điểm nhìn, đổi cỡ cảnh (Toàn $\leftrightarrow$ Trung/Cận) và luân phiên đổi độ cao góc máy (Góc ngang tầm mắt `Eye-level` $\leftrightarrow$ Góc thấp hất lên `Low-angle` $\leftrightarrow$ Góc cao nhìn xuống `High-angle` $\leftrightarrow$ Góc qua vai `Over-the-shoulder POV` $\leftrightarrow$ Góc xuyên khung tiền cảnh `Framed-through`) sau khi đã khóa chắc lý do nối cảnh.

---

## 3. Luật Hình Ảnh & Thế Giới

- **Luật Siêu thực:** Thị trấn kỳ lạ phải gọi tên rõ một đặc điểm định danh xuyên suốt mọc ra từ câu chuyện bài hát, nơi nhân vật sống và sinh hoạt tự nhiên cùng đặc điểm đó.
- **Luật Tối giản:** Mỗi cảnh tập trung vào 1 ý tưởng hình ảnh rõ ràng trong không gian thoáng rộng, có thể xóa phông hậu cảnh khi cần làm nổi bật chủ thể.
- **Luật Đa dạng & Chiều sâu Điện ảnh:** Luân phiên đa dạng góc độ cao-thấp của máy quay (góc ngang tầm mắt kết nối cảm xúc, góc thấp hất lên, góc cao nhìn xuống, góc nhìn qua vai, góc nhìn xuyên qua tiền cảnh) cùng bố cục nhiều lớp tiền-trung-hậu cảnh và cỡ cảnh; mỗi nhân vật có ngoại hình và màu trang phục riêng.
- **Luật Cảm xúc & Ý nghĩa:** Mỗi khung hình đặt trạng thái nội tâm, ánh mắt, nụ cười và ý nghĩa của sự gắn kết giữa người với người làm trung tâm, nơi hành động là sự bộc lộ cảm xúc tự nhiên giữa đời sống.
- **Luật Cỡ cảnh & Tỷ lệ vật lý:**
  - Dùng cỡ bán thân hoặc trung cận khi nhân vật ở trong không gian có vách che phần dưới hoặc khi lấy cận biểu cảm.
  - Dùng cỡ toàn thân thấy đủ trang phục đến giày chạm sàn/đất khi nhân vật ở không gian mở hoặc phòng rộng.
  - Nhà cửa và phương tiện có kích thước thật cao lớn hơn đầu người.
- **Luật Ánh sáng:** Mỗi cảnh có 1 nguồn sáng chính chiếu theo 1 hướng; ánh sáng chuyển dịch mượt theo thời gian câu chuyện.
