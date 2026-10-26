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
2.5D handcrafted stop-motion animation film still, matte-painted tactile world, slender figures with matte paper-pulp skin, soft rounded noses, and thick full cotton-fiber hair. [Full-body medium-wide | Waist-up medium close-up + Góc máy + Không gian có chiều sâu, Bảng màu & Tương phản ánh sáng], where [Nhân vật đa dạng vóc dáng/vai trò với kiểu tóc dày biến hóa theo cảnh (full head of [kiểu dáng + màu sắc] hair), trang phục khớp cỡ cảnh (đủ áo-quần/váy chạm sàn ở cảnh toàn thân hoặc đặt sau mặt phẳng tiền cảnh ở cảnh bán thân) + Khoảnh khắc hành động & cảm xúc tự nhiên + Điểm xuyết chất thơ siêu thực tinh tế nếu ở cảnh Hook], no text --ar 16:9

# 2. Cảnh Đặc tả Chi tiết / Tĩnh vật / Đại cảnh Vắng người (Close-up / Detail / Wide):
2.5D handcrafted stop-motion animation film still, matte-painted tactile wood, stone, and paper-pulp world. [Cỡ cảnh + Góc máy + Không gian/Chi tiết giàu sức gợi, Bảng màu & Ánh sáng], where [Diễn biến tinh tế của chi tiết/tự nhiên hoặc bóng người nhỏ bé ở xa đối với Đại cảnh], no text --ar 16:9
```

---

## 2. Luật Đầu Ra (`character.md` & `image.txt`)

- **Khóa Chất liệu Cố định ở Đầu Câu (`Material Prefix Lock`) & Hậu tố cuối câu (`Suffix Lock`):**
  - Đặt toàn bộ cụm khóa chất liệu thế giới và chất liệu phôi rối nhân vật có mật độ tóc bông dày (`2.5D handcrafted stop-motion animation film still, matte-painted tactile world, slender figures with matte paper-pulp skin, soft rounded noses, and thick full cotton-fiber hair.`) ngay câu đầu tiên để giữ đồng nhất chất liệu, bảo toàn tỷ lệ 1:1 hài hòa giữa người với kiến trúc và dành trọn phần thân câu cho mô tả nghệ thuật.
  - Với cảnh tĩnh vật hoặc đặc tả chi tiết, mở đầu bằng cụm khóa chất liệu thế giới (`2.5D handcrafted stop-motion animation film still, matte-painted tactile wood, stone, and paper-pulp world.`).
  - Khóa hậu tố `, no text --ar 16:9` ở cuối mỗi dòng câu lệnh trong `image.txt`.
- **Đa dạng Nhân vật, Mái tóc Dày Đổi kiểu & Đồng bộ Tỷ lệ Cơ thể theo Cỡ cảnh:**
  - Mỗi cảnh có người đều định danh nhân vật bằng vóc dáng, vai trò sinh hoạt mới và **một kiểu tóc dày phủ kín đầu được biến hóa đa dạng về phom dáng và sắc độ** (`a full head of [kiểu dáng + màu sắc] hair` hoặc kiểu tóc tết/búi dày kết hợp phụ kiện đầu/râu/kính khác biệt) để mỗi khung hình mang diện mạo độc bản.
  - **Đồng bộ cỡ cảnh, giải phẫu cục bộ và điểm tựa cơ thể:** Ở cảnh trung-rộng thấy mặt sàn hoặc mặt đất (`Full-body medium-wide shot`), mô tả trang phục tinh gọn đủ cả phần thân trên và thân dưới tiếp xúc trực tiếp với mặt phẳng đứng; ở cảnh trung cận lấy nửa người (`Waist-up medium close-up`), đóng khung từ thắt lưng trở lên gắn với mặt phẳng nội thất hoặc kiến trúc tiền cảnh hợp lý; ở cảnh đặc tả cục bộ bàn tay hoặc bàn chân/giày dép (`Close-up / Ground-level detail shot`), khóa rõ số lượng chi tiết giải phẫu đầy đủ, phần cổ tay hoặc ống chân/gấu trang phục nối liền vào bàn tay/đôi giày và sự tiếp xúc vật lý vững chắc trên mặt phẳng tựa (`firmly grounded flat on surface`, `showing full legs and feet inside shoes`); ở cảnh cận gương mặt (`Portrait close-up`), khóa rõ đường nét gương mặt tròn trịa phúc hậu cùng chiếc mũi tròn nhỏ nhắn mềm mại (`gentle kind round face, small cute rounded nose`) và ưu tiên trạng thái đôi mắt khép nhẹ tận hưởng khoảnh khắc.
  - Đa dạng hóa cách xuất hiện của con người qua các cảnh: trực diện ấm áp, bóng lưng lặng yên, bóng in qua lớp vật liệu xuyên sáng, nhìn qua khung tiền cảnh, đặc tả cử chỉ cục bộ, hoặc bóng người nhỏ bé giữa thiên nhiên rộng lớn (`70% open negative space`).
- **Đa dạng Không gian, Bảng màu Ấm Chủ Đạo & Ánh sáng Tự nhiên Thuần khiết:**
  - Mỗi cảnh mở ra một không gian nội-ngoại cảnh với bảng màu ấm áp chủ đạo (`warm earthy-beige and amber palette` kết hợp điểm nhấn màu tương phản), ưu tiên nguồn sáng ngược chiều giờ vàng (`warm golden-hour rim light`) tôn đường viền mái tóc bông dày và dành ánh sáng đèn ấm áp lúc chạng vạng cho phân đoạn kết (`Outro`), giữ toàn bộ sự vật và chất thơ siêu thực ở trạng thái bề mặt sơn mờ thủ công (`matte-painted tactile surface`), tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
