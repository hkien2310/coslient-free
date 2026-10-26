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
# 1. Cảnh Có Nhân vật (Trung cảnh, Trung cận, Bóng lưng, Nhìn xuyên khung):
2.5D handcrafted stop-motion miniature film still, matte-painted tactile world, slender figures with matte paper-pulp skin, soft rounded noses, and fluffy cotton-fiber hair. [Cỡ cảnh + Góc máy + Không gian có chiều sâu, Bảng màu & Tương phản ánh sáng], where [Khoảnh khắc hành động & cảm xúc tự nhiên của nhân vật với trang phục tối giản + Điểm xuyết chất thơ siêu thực tinh tế nếu ở cảnh Hook] --ar 16:9

# 2. Cảnh Đặc tả Chi tiết / Tĩnh vật / Đại cảnh Vắng người (Close-up / Detail / Wide):
2.5D handcrafted stop-motion miniature film still, matte-painted tactile wood, stone, and paper-pulp world. [Cỡ cảnh + Góc máy + Không gian/Chi tiết giàu sức gợi, Bảng màu & Ánh sáng], where [Diễn biến tinh tế của chi tiết/tự nhiên hoặc bóng người nhỏ bé ở xa đối với Đại cảnh] --ar 16:9
```

---

## 2. Luật Đầu Ra (`character.md` & `image.txt`)

- **Khóa Chất liệu Cố định ở Đầu Câu (`Material Prefix Lock`):**
  - Đặt toàn bộ cụm khóa chất liệu thế giới và chất liệu phôi rối nhân vật (`2.5D handcrafted stop-motion miniature film still, matte-painted tactile world, slender figures with matte paper-pulp skin, soft rounded noses, and fluffy cotton-fiber hair.`) ngay câu đầu tiên để giữ đồng nhất chất liệu tuyệt đối và dành trọn phần thân câu cho mô tả nghệ thuật.
  - Với cảnh tĩnh vật hoặc đặc tả chi tiết, mở đầu bằng cụm khóa chất liệu thế giới (`2.5D handcrafted stop-motion miniature film still, matte-painted tactile wood, stone, and paper-pulp world.`).
- **Tối giản Nhân vật & Giải phóng Điểm nhìn Điện ảnh:**
  - Mô tả nhân vật và trang phục ngắn gọn trong vài từ gợi chất liệu tự nhiên để ưu tiên dung lượng câu lệnh cho **bố cục, tương phản ánh sáng và khoảnh khắc cảm xúc**.
  - Đa dạng hóa cách xuất hiện của con người qua các cảnh: trực diện ấm áp, bóng lưng lặng yên, bóng in qua lớp vật liệu xuyên sáng, nhìn qua khung tiền cảnh, đặc tả cử chỉ cục bộ, hoặc bóng người nhỏ bé giữa thiên nhiên rộng lớn (`70% open negative space`).
- **Đa dạng Không gian, Bảng màu & Ánh sáng Cảm xúc:**
  - Mỗi cảnh mở ra một không gian nội-ngoại cảnh, bảng màu thời gian/thời tiết và độ tương phản sáng-tối riêng biệt gắn chặt với cảm xúc của câu hát tại thời điểm đó, tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
