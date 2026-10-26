# Handcrafted Stop-Motion Style (`character.md` & `image.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Định nghĩa nguyên lý thế giới sa bàn thủ công stop-motion trực quan (`Handcrafted stop-motion miniature diorama`), tạo hình nhân vật cách điệu (da giấy bồi mờ, mũi tròn cách điệu, tỷ lệ thanh mảnh kéo dài, tóc và râu sợi bông xù, trang phục vải dệt đủ bộ áo-quần dài-giày kèm điểm nhấn nhận diện độc bản), công thức nén nhận diện trực quan, tư thế khởi đầu hành động ở giây 0 và **khung câu lệnh 4 khối tiếng Anh trực quan** để viết `character.md` cũng như biên dịch `storyboard.md` sang `image.txt`. Nghệ thuật đạo diễn kịch bản `storyboard.md`, tỷ lệ 70/30, bố cục không gian và ma trận góc máy nằm độc lập tại [`craft/visual_craft.md`](../craft/visual_craft.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra (`character.md` & `image.txt`)

- **Đầu vào:** `1-idea.md`, `storyboard.md` và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
- **Đầu ra 1 — Cấu trúc file `character.md` *(Tùy chọn)*:**
  - Khóa trực tiếp chất liệu thế giới và chất liệu nhân vật ngay ở cụm mở đầu của từng dòng trong `image.txt` kèm mô tả trang phục tinh gọn để mỗi ảnh là một lát cắt độc lập thoáng đãng; chỉ tạo `character.md` khi cần lưu mẫu tham chiếu riêng.

- **Đầu ra 2 — Khung câu lệnh tiếng Anh tinh gọn cho `image.txt` (1 dòng/cảnh khớp 1:1 với `storyboard.md`):**

```text
# 1. Cảnh Có Nhân vật (Trung-rộng toàn thân, Trung cận bán thân, Bóng lưng, Nhìn xuyên khung):
2.5D handcrafted stop-motion animation film still, photorealistic miniature diorama, stylized figures with matte paper-pulp skin and abundant full-volume hair with clearly defined individual strands. [Full-body medium-wide | Waist-up medium close-up + Góc máy + Không gian sa bàn giàu kết cấu vật lý, Bảng màu & Tương phản ánh sáng], where [Nhân vật tự do biến hóa vóc dáng/đường nét với mái tóc dày rõ từng sợi đổi kiểu linh hoạt + trang phục vải dệt khớp cỡ cảnh (đủ áo-quần/váy chạm sàn ở cảnh toàn thân hoặc đặt sau mặt phẳng tiền cảnh ở cảnh bán thân) + Khoảnh khắc hành động đời thường tự nhiên (sinh hoạt bình thường, ngắm cảnh, chăm sóc tình thân, phiêu lưu, vui chơi sống lại thời trẻ) kết hợp điểm xuyết tư thế ngẫu hứng phóng khoáng hoặc chất thơ siêu thực ở cảnh Hook]. Macro 85mm, shallow depth of field, no text --ar 16:9

# 2. Cảnh Đặc tả Chi tiết / Tĩnh vật / Đại cảnh Thoáng rộng (Close-up / Detail / Wide):
2.5D handcrafted stop-motion animation film still, photorealistic miniature diorama. [Cỡ cảnh + Góc máy + Không gian/Chi tiết giàu kết cấu vật lý, Bảng màu & Ánh sáng], where [Diễn biến tinh tế của chi tiết/tự nhiên hoặc bóng người nhỏ bé ở xa đối với Đại cảnh]. Macro 85mm, shallow depth of field, no text --ar 16:9
```

---

## 2. Luật Đầu Ra (`character.md` & `image.txt`)

- **Khóa Chất liệu Sa bàn Tả thực & Mái tóc Dày Rõ Từng Sợi ở Đầu Câu (`Material & Stranded Hair Prefix Lock`):**
  - Khóa chất liệu thế giới sa bàn thu nhỏ tả thực, chất liệu da bột giấy mờ và đặc tính mái tóc dày phồng tách rõ từng sợi ngay ở câu đầu tiên (`2.5D handcrafted stop-motion animation film still, photorealistic miniature diorama, stylized figures with matte paper-pulp skin and abundant full-volume hair with clearly defined individual strands.`), dành toàn bộ kiểu tóc, đường nét gương mặt, tỷ lệ hình thể, thời đại bối cảnh và thần thái cho mô hình tự do biến hóa đa dạng theo ngữ cảnh từng câu chuyện.
  - Với cảnh tĩnh vật hoặc đại cảnh thiên nhiên, mở đầu bằng cụm khóa chất liệu thế giới (`2.5D handcrafted stop-motion animation film still, photorealistic miniature diorama.`).
  - Khóa hậu tố ống kính `. Macro 85mm, shallow depth of field, no text --ar 16:9` ở cuối mỗi dòng câu lệnh trong `image.txt`.
- **Mở tự do Kiểu tóc trên Nền Tóc Dày Rõ Sợi & Đồng bộ Tỷ lệ Cơ thể theo Cỡ cảnh:**
  - Mỗi cảnh có người đều định danh nhân vật bằng vóc dáng, vai trò sinh hoạt mới và **tự do thay đổi kiểu tóc theo từng nhân vật trên nền tảng mái tóc dày tách rõ từng sợi** (`abundant full-volume [kiểu dáng + màu sắc] hair with distinct strands`) cùng trang phục vải dệt tự nhiên để mỗi khung hình mang diện mạo sống động.
  - **Đồng bộ cỡ cảnh, liên kết giải phẫu và điểm tựa vật lý:** Ở cảnh trung-rộng thấy mặt sàn hoặc mặt đất (`Full-body medium-wide shot`), mô tả trang phục tinh gọn đủ cả phần thân trên và thân dưới tiếp xúc trực tiếp với mặt phẳng đứng; ở cảnh trung cận lấy nửa người (`Waist-up medium close-up`), đóng khung từ thắt lưng trở lên gắn với mặt phẳng nội thất hoặc kiến trúc tiền cảnh hợp lý; ở cảnh đặc tả cục bộ hoặc cận cảnh (`Close-up / Detail shot`), mô tả rõ sự tiếp nối giải phẫu với phần cơ thể liền kề, đường nét gương mặt hài hòa mềm mại và điểm tiếp xúc vật lý vững chắc của sự vật trên mặt phẳng tựa để ưu tiên dung lượng câu lệnh cho **bố cục, tương phản ánh sáng và khoảnh khắc cảm xúc**.
  - Đa dạng hóa cách xuất hiện của con người qua các cảnh: trực diện ấm áp, bóng lưng lặng yên, bóng in qua lớp vật liệu xuyên sáng, nhìn qua khung tiền cảnh, đặc tả cử chỉ cục bộ, hoặc bóng người nhỏ bé giữa thiên nhiên rộng lớn (`70% open negative space`).
- **Tôn Trọng Yếu Tố Môi Trường Chân Thực & Ánh Sáng Tự Nhiên Thuần Khiết (`Authentic Environment & Natural Lighting`):**
  - Giữ nguyên bản chất tự nhiên chân thực của toàn bộ môi trường (mây trời, sóng nước, cây cối, hoa lá, chim muông, thú vật) và chỉ sử dụng nguồn sáng môi trường tự nhiên theo thời gian thực (bình minh, nắng sớm, chiều vàng, hoàng hôn, ánh đèn ấm từ cửa sổ nhà) có chiều sâu tách khối, tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
