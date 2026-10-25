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
- **Đầu ra (`storyboard.md`):** Mở đầu bằng **1 dòng khóa `Địa điểm & Kiến trúc kỳ lạ của thị trấn`**, sau đó triển khai theo **Quy trình 2 Tầng (`Quy hoạch Đại Cảnh` $\to$ `Triển khai Tiểu Cảnh`)** khớp 1:1 số dòng và mốc giờ với `timestamps.txt` (duyệt xong dịch 1:1 sang `image.txt` theo [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md)):
  1. **Phần 1 — Quy hoạch Đại Cảnh theo Phân đoạn nhạc (`Macro-Sequence Blueprint`):** Xác lập mục tiêu cảm xúc, **điểm nhấn công trình/địa hình siêu thực riêng của đoạn đó**, nhóm nhân vật mới và điểm `Hook / Mini-Hook` cho từng phân đoạn (`Intro`, `Verse`, `Pre-Chorus`, `Chorus`, `Vocalise / Interlude`, `Bridge`, `Outro`).
  2. **Phần 2 — Bảng Tiểu Cảnh (`Micro-Scenes`):**

| Cảnh & Giờ | Đoạn nhạc & Lời hát | Vai trò Giữ chân, Lý do nối cảnh & Thông số (Cỡ, Góc, Công trình/Bối cảnh siêu thực, Chuyển động) | Nhân vật, Khoảnh khắc hành động & Ánh sáng |
| :--- | :--- | :--- | :--- |
| 01 (00:00-00:04) | [Lời hát / Nhạc] | Vai trò & Nối cảnh: [Hook / Mini-Hook / Bồi tiếp Cảnh trước như thế nào & Tại sao]<br>Cỡ: [...] \| Góc: [...]<br>Bối cảnh siêu thực: [...]<br>Chuyển động: [Hướng máy + Diễn biến hành động + Cảm xúc cảnh] | [Mô tả nhân vật theo cỡ cảnh + Biểu cảm, dáng điệu & khoảnh khắc hành động đang diễn ra + Ánh sáng] |

---

## 2. Quy Trình Thực Chiến 2 Tầng & Kỹ Thuật Giữ Chân (`storyboard.md`)

- **1. Tầng 1 — Chia Đại Cảnh theo Phân đoạn Nhạc & Đổi mới Công trình/Nhân vật (`Macro-Blocks`):**
  - Mỗi phân đoạn bài hát là một Đại Cảnh mang một nhiệm vụ giữ chân rõ ràng, gắn với **những con người mới và điểm nhấn công trình/địa hình siêu thực mới**:
    - **`Intro` (Hook tổng lực):** Gây ấn tượng thị giác mạnh mẽ và đánh thức trí tò mò ngay giây đầu tiên bằng đại cảnh địa hình và kiến trúc siêu thực kỳ vĩ nhất của thị trấn.
    - **`Verse 1` (Khởi phát câu chuyện):** Mở lời bằng hình ảnh trả lời sự tò mò của `Intro` và dẫn dắt người xem vào tâm tình chủ đạo qua cụm nhân vật đầu tiên.
    - **`Pre-Chorus` (Đà nâng năng lượng):** Chuyển dịch sang các góc không gian và cư dân khác nhau để tích lũy sự háo hức trước điểm bùng nổ.
    - **`Chorus` (Bung mở thế giới & Thông điệp):** Mở rộng biên độ thị giác của các công trình siêu thực trong thị trấn, lan tỏa cảm xúc của câu `Hook` qua nhiều góc nhìn và con người.
    - **`Verse 2` (Đổi mới không gian & Giữ nhịp giữa bài):** Đổi sang công trình/phương tiện siêu thực mới và cặp/nhóm nhân vật mới để làm tươi mới hoàn toàn trải nghiệm thị giác.
    - **`Vocalise / Interlude` (Đỉnh cao chất thơ thị giác):** Dành những khung hình kiến trúc và thiên nhiên siêu thực kỳ diệu, thoáng rộng nhất cho đoạn nhạc ngân giai điệu.
    - **`Bridge` & `Final Chorus` (Điểm lắng nội tâm $\to$ Cao trào trọn vẹn):** Thu cận vào chiều sâu gắn kết giữa người với người ở `Bridge` rồi bung ra đại cảnh lễ hội/cộng đồng kỳ vĩ ở `Final Chorus`.
    - **`Outro` (Gặt lại chi tiết & Dư âm):** Khép vòng câu chuyện bằng hình ảnh gặt lại chi tiết mỏ neo đầu bài và đọng lại sự bình yên sâu lắng.
  - **Luân chuyển nhân vật tự do theo Đại Cảnh / Cụm hành động:** Nhân vật chỉ giữ đồng nhất trong phạm vi 1 cụm ngắn (2–3 tiểu cảnh liền kề khi cần hoàn tất một chuỗi hành động nhân-quả), sau đó chuyển hẳn sang những cư dân khác với trang phục và hoạt động mới ở các cụm và Đại Cảnh tiếp theo.
- **2. Tầng 2 — Triển khai Tiểu Cảnh theo Nhịp sóng `Hook -> Bồi tiếp Nhân-Quả -> Mini-Hook` (`Micro-Scenes`):**
  - **Mở đầu mỗi Đại Cảnh bằng `Hook` hoặc `Mini-Hook`:** Cảnh đầu tiên của mỗi phân đoạn luôn tung ra một công trình/khung cảnh siêu thực đẹp mắt choáng ngợp hoặc một tình huống gây hiếu kỳ để neo chặt ánh nhìn.
  - **Các Tiểu Cảnh tiếp theo nối mạch Nhân – Quả (`Cảnh N -> Cảnh N+1`):** Mỗi cảnh kế tiếp phải xác định rõ lý do xuất hiện và cách nó bồi tiếp, giải thích hoặc mở rộng cảm xúc từ cảnh ngay trước đó để duy trì sự cuốn hút liên tục cho tới `Mini-Hook` tiếp theo.
- **3. Bước nhảy Không gian & Đảo nhịp Góc máy ($N \to N+1$):**
  - Khi chuyển từ Cảnh $N$ sang Cảnh $N+1$, chủ động chuyển đổi vị trí không gian/điểm nhìn, đổi cỡ cảnh (Đại cảnh/Toàn cảnh $\leftrightarrow$ Trung/Cận) và luân phiên đổi độ cao góc máy (Góc ngang tầm mắt `Eye-level` $\leftrightarrow$ Góc thấp hất lên `Low-angle` $\leftrightarrow$ Góc cao nhìn xuống `High-angle` $\leftrightarrow$ Góc qua vai `Over-the-shoulder POV` $\leftrightarrow$ Góc xuyên khung tiền cảnh `Framed-through`) sau khi đã khóa chắc lý do nối cảnh.

---

## 3. Luật Hình Ảnh, Kiến Trúc Siêu Thực & Tỷ Lệ Con Người Theo Cỡ Cảnh

- **Luật Kiến trúc & Địa hình Siêu thực:** Bên cạnh motif chủ đạo của thị trấn, mỗi Đại Cảnh phải có điểm nhấn kiến trúc, công trình hoặc địa hình mang cấu trúc siêu thực kỳ vĩ mọc ra từ câu chuyện bài hát, nơi con người sinh hoạt tự nhiên bên trong đó.
- **Luật Bố cục Bất đối xứng & Tối giản:** Mọi khung hình đặt theo bố cục lệch tâm phần ba (`asymmetric rule-of-thirds composition`) cùng đường dẫn chéo hoặc uốn lượn tự nhiên (`winding diagonal or S-curve layout`), tập trung vào 1 ý tưởng hình ảnh và 1 điểm nhấn siêu thực rõ ràng trong không gian thoáng rộng lệch một bên.
- **Luật Mô tả Con người theo Cỡ cảnh (Bảo toàn Tỷ lệ & Sự đa dạng đám đông):**
  - **Ở Đại cảnh, Toàn cảnh rộng hoặc Cảnh đông người (`Extreme wide` / `Wide`):** Tập trung mô tả sự kỳ vĩ của công trình siêu thực và cảnh quan; con người chỉ gọi bằng cụm từ quy mô nhỏ (`tiny distant figures` / `small miniature townspeople in varied warm attire`), giúp giữ chuẩn tỷ lệ con người nhỏ bé trước kiến trúc đồ sộ và tạo sự đa dạng tự nhiên cho đám đông.
  - **Ở Cảnh Trung và Cận (`Medium` / `Medium close-up` / `Close-up` — 1 đến 2 người):** Mô tả rõ gương mặt, biểu cảm ánh mắt và trang phục của 1–2 nhân vật trung tâm; dùng cỡ bán thân khi có vách che phần dưới hoặc lấy cận biểu cảm, và dùng cỡ toàn thân thấy đủ đến giày chạm sàn khi ở không gian mở cự ly gần.
- **Luật Ánh sáng:** Mỗi cảnh có 1 nguồn sáng chính chiếu theo 1 hướng; ánh sáng chuyển dịch mượt theo thời gian câu chuyện.
