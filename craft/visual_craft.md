# Visual Craft: Đạo diễn Storyboard & Chuỗi khung hình (`character.md` & `storyboard.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` và `timestamps.txt` để thiết lập hồ sơ nhân vật `character.md` và đạo diễn bảng phân cảnh `storyboard.md` (hoạt động sống có mục đích thực tế, tương tác nhân-quả trong khung hình, đường cong năng lượng theo cấu trúc nhạc, tỷ lệ 70/30 cùng 4 động cơ chất ngông, bố cục không gian, ma trận góc máy và luật đảo nhịp $N \to N+1$). Toàn bộ nguyên lý chất liệu sa bàn stop-motion trực quan, công thức nén nhận diện 4 trục và khung câu lệnh 4 khối tiếng Anh cho `character.md` / `image.txt` nằm độc lập tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra

- **Đầu vào (Chỉ đọc — giữ nguyên vẹn các file của bước trước):** `1-idea.md`, `3-lyrics.txt` và `timestamps.txt`.
- **Đầu ra:**
  - **`storyboard.md`:** Mở đầu bằng **1 mục khóa `Thế giới Hoài cổ Vượt thời gian & Quy luật Siêu thực`** (chủ động kiến tạo không gian mở mang phong vị cơ khí – thủ công vượt thời gian và hệ quy luật siêu thực của dự án ngay tại đầu file `storyboard.md`), sau đó triển khai theo **Quy trình 2 Tầng (`Quy hoạch Đại Cảnh` $\to$ `Triển khai Tiểu Cảnh độc lập`)** khớp 1:1 số dòng và mốc giờ với `timestamps.txt` (duyệt xong dịch 1:1 sang `image.txt` theo [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md)):
    1. **Phần 1 — Quy hoạch Đại Cảnh theo Phân đoạn nhạc (`Macro-Sequence Blueprint`):** Xác lập mục tiêu cảm xúc, cơ chế tạo Điểm sai siêu thực, không gian điểm nhấn, nhân vật mới và điểm `Hook / Mini-Hook` cho từng phân đoạn (`Intro`, `Verse`, `Pre-Chorus`, `Chorus`, `Vocalise / Interlude`, `Bridge`, `Outro`).
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
    - **`Chorus` (Bung mở thế giới & Thông điệp):** Mở rộng biên độ thị giác của thế giới siêu thực, lan tỏa cảm xúc của câu `Hook` qua nhiều góc nhìn và con người.
    - **`Verse 2` (Đổi mới không gian & Giữ nhịp giữa bài):** Mở ra bối cảnh mới và hoạt động tương tác mới để làm tươi mới trải nghiệm thị giác.
    - **`Vocalise / Interlude` (Đỉnh cao chất thơ thị giác):** Dành những khung hình siêu thực kỳ diệu và giàu cảm xúc nhất cho đoạn nhạc ngân giai điệu.
    - **`Bridge` & `Final Chorus` (Điểm lắng nội tâm $\to$ Cao trào trọn vẹn):** Thu cận vào chiều sâu gắn kết giữa người với người ở `Bridge` rồi bung ra đại cảnh ấm áp nhất ở `Final Chorus`.
    - **`Outro` (Gặt lại chi tiết & Dư âm):** Khép vòng câu chuyện bằng hình ảnh đọng lại sự bình yên sâu lắng.
  - **Sự linh hoạt của Đại Cảnh:** Một Đại Cảnh là một khối chủ đề và cảm xúc thống nhất, bên trong gồm các Tiểu Cảnh là những lát cắt độc lập qua những con người và không gian đa dạng cùng cộng hưởng chung một nhịp cảm xúc.
- **2. Tầng 2 — Triển khai Tiểu Cảnh Độc lập theo Nhịp sóng `Hook -> Bồi tiếp Cảm xúc -> Mini-Hook` (`Micro-Scenes`):**
  - **Mở đầu mỗi Đại Cảnh bằng Điểm xuyết Siêu thực (`Hook / Mini-Hook`):** Cảnh mở đầu của mỗi phân đoạn điểm xuyết một hình ảnh siêu thực giàu chất thơ gắn với bản chất kỳ diệu của thế giới và câu hát chủ đạo để nâng tầm cảm xúc và kích hoạt sự hiếu kỳ.
  - **Các Tiểu Cảnh tiếp theo (`Bồi tiếp`) mang Độ Lệch Pha Thơ Mộng & Hành Động Phóng Khoáng (`Cảnh N -> Cảnh N+1`):** Các cảnh đi sau trong Đại Cảnh bồi đắp chiều sâu tình cảm con người qua những không gian mới và nhân vật mới độc lập, luôn duy trì sự cuốn hút thị giác thông qua các hành động ngẫu hứng bất quy tắc, sự dịch chuyển vị trí đầy chất thơ hoặc cử chỉ thân mật khác thường.
- **3. Bước nhảy Không gian & Đảo nhịp Góc máy ($N \to N+1$):**
  - Khi chuyển từ Cảnh $N$ sang Cảnh $N+1$, chủ động chuyển đổi vị trí không gian/điểm nhìn, đổi cỡ cảnh (Toàn $\leftrightarrow$ Trung/Cận) và luân phiên đổi độ cao góc máy (Góc ngang tầm mắt `Eye-level` $\leftrightarrow$ Góc thấp hất lên `Low-angle` $\leftrightarrow$ Góc cao nhìn xuống `High-angle` $\leftrightarrow$ Góc qua vai `Over-the-shoulder POV` $\leftrightarrow$ Góc xuyên khung tiền cảnh `Framed-through`) sau khi đã khóa chắc lý do nối cảnh.

---

## 3. Luật Hình Ảnh & Thế Giới

- **Luật Thế Giới Hoài Cổ Vượt Thời Gian & Dải Lệch Pha Tự Nhiên (`Timeless Analog World & Poetic Displacement`):**
  - **Không gian Mở Hoài cổ Cơ khí (`Timeless Analog World`):** Kiến tạo thế giới mở kết hợp tự do giữa thiên nhiên khoáng đạt và đời sống phố thị mang phong vị cơ khí – thủ công cổ điển vượt thời gian, nơi con người tương tác trực tiếp với nhau thông qua các phương tiện, nhạc cụ và vật dụng cơ học hữu hình.
  - **Dải Lệch pha Tự nhiên xuyên suốt (`Poetic Displacement Continuum`):** Đặt một quy luật kỳ diệu cốt lõi về mặt bản chất câu chuyện để điểm xuyết yếu tố siêu thực tại điểm `Hook / Mini-Hook` của mỗi Đại Cảnh làm ẩn dụ thị giác trực tiếp nâng tầm lời bài hát; đồng thời ở các Tiểu Cảnh bồi tiếp, luôn đặt hoạt động đời thường vào một vị trí, phương tiện hoặc vai trò bất ngờ nhưng được nhân vật thực hiện với thái độ hoàn toàn thản nhiên, tự tại.
  - **4 Cơ chế tạo Điểm sai bám quy luật vật lý (Chọn lọc cho `Hook / Mini-Hook` và giao thoa sang cảnh Bồi tiếp):**
    1. **Lai ghép (`Ngoại hình bên Nhỏ/Mềm + Tính chất bên Lớn/Vững`):** Ghép hai thực thể bằng cách lấy ngoại hình của thực thể nhỏ hoặc mềm đắp vào thực thể lớn hoặc vững chãi, đồng thời giữ nguyên tính chất vật lý của bên lớn hơn (giữ tính tĩnh tại để ở của công trình kiến trúc hoặc tính gợn sóng bồng bềnh của mặt biển/cảnh quan).
    2. **Phóng đại (`Phóng to vượt bậc 1 thực thể duy nhất theo 2 nhánh`):**
       - *Nhánh Đồ vật quen thuộc:* Phóng đại kích thước và đổi công năng thành công trình kiến trúc, nơi trú ẩn hoặc phương tiện.
       - *Nhánh Sinh vật nhỏ bé hiền lành:* Phóng đại kích thước với đường nét thủ công bo tròn mềm mại và giữ nguyên tính chất là người bạn sinh vật hiền hòa để con người tựa vào hoặc bầu bạn.
    3. **Vật thể hóa tự nhiên (`1 hiện tượng tự nhiên + đối xử như vật cầm nắm được`):** Chuyển hóa hiện tượng tự nhiên nhẹ nhàng thành chất liệu thủ công hữu hình để nhân vật nâng niu và bầu bạn.
    4. **Lạc quẻ không gian (`1 vật dụng/hoạt động riêng tư + đặt giữa thiên nhiên bao la`):** Đặt một vật dụng nội thất, nhạc cụ hoặc sinh hoạt riêng tư ra giữa cảnh quan thiên nhiên rộng lớn.
- **Luật Lát cắt Độc lập & Đa dạng Không gian, Bảng màu:** Mỗi Tiểu Cảnh mở ra một không gian nội-ngoại cảnh mới cùng bảng màu và độ tương phản sáng-tối riêng biệt, đồng thời kết nối hài hòa trong cùng một thế giới hoài cổ vượt thời gian.
- **Luật Tối giản & Khoảng thở (`Negative Space`):** Mỗi cảnh tập trung vào 1 khoảnh khắc cảm xúc và 1 ý tưởng thị giác duy nhất với mô tả trang phục tinh gọn, dành tối đa khoảng thở cho ánh sáng và không khí điện ảnh.
- **Luật Giải phóng Điểm nhìn & Cỡ cảnh Điện ảnh ($N \to N+1$):**
  - Luân phiên đa dạng cách đặt máy và sự hiện diện của con người giữa các cảnh kế tiếp: góc nhìn xuyên qua lớp vật liệu hoặc khung tiền cảnh (`framed-through / silhouette`), góc nhìn từ phía sau bóng lưng, góc nhìn thẳng từ đỉnh đầu xuống (`top-down`), cảnh đặc tả cử chỉ cục bộ, trung cảnh sinh hoạt ấm cúng và đại cảnh thiên nhiên thoáng rộng (`70% open sky/landscape`).
- **Luật Cảm xúc, Chất Ngông Tự Tại & Chất thơ Vi mô (`Unapologetic Freedom, Candid Posture & Micro-Poetry`):**
  - Giải phóng nhân vật trưởng thành khỏi những cử chỉ khuôn phép rập khuôn: kết hợp các cử chỉ thân mật sâu lắng với những hành động tận hưởng cuộc sống đầy phóng khoáng, ngẫu hứng và phá vỡ giới hạn tuổi tác cùng một thần thái hoàn toàn thản nhiên, tự tại như thể thế giới thuộc về riêng họ.
  - Tạo độ lệch nghệ thuật giữa không gian, phục trang và ngôn ngữ cơ thể: ưu tiên các tư thế có trọng tâm thả lỏng bất đối xứng (ngồi bệt, tựa nghiêng, gác chân ngẫu hứng), hướng sự chú ý vào bạn đồng hành hoặc hoạt động trong cảnh, gắn kết đôi tay với vật dụng hữu hình kèm điểm nhấn phụ kiện cá tính; khi điểm xuyết yếu tố siêu thực, ưu tiên những nét chấm phá tinh tế hòa quyện tự nhiên vào khung cảnh.
