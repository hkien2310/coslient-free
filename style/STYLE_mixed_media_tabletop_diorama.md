# Handcrafted Stop-Motion Style (`character.md` & `image.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Định nghĩa nguyên lý thế giới sa bàn thủ công stop-motion trực quan (`Handcrafted stop-motion miniature diorama`), tạo hình nhân vật cách điệu (da giấy bồi mờ, mũi tròn cách điệu, tỷ lệ thanh mảnh kéo dài, tóc và râu sợi bông xù, trang phục vải dệt đủ bộ áo-quần dài-giày kèm điểm nhấn nhận diện độc bản), công thức nén nhận diện trực quan, tư thế khởi đầu hành động ở giây 0 và **khung câu lệnh 4 khối tiếng Anh trực quan** để viết `character.md` cũng như biên dịch `storyboard.md` sang `image.txt`. Nghệ thuật đạo diễn kịch bản `storyboard.md`, tỷ lệ 70/30, bố cục không gian và ma trận góc máy nằm độc lập tại [`craft/visual_craft.md`](../craft/visual_craft.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra (`image.txt`)

- **Đầu vào:** `1-idea.md`, `storyboard.md` và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
- **Đầu ra — Khung câu lệnh tiếng Anh cho `image.txt` theo 3 mẫu cỡ cảnh (1 dòng/cảnh khớp 1:1 với `storyboard.md`):**

```text
# Mẫu 1 — Cảnh Trung & Cận tập trung vào Nhân vật (Medium-wide / Medium / Medium close-up / Waist-up — 1 đến 2 người):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town with realistic natural water, clouds, trees, and stone, [time-of-day] light, asymmetric organic composition, shallow depth of field with a softly blurred warm background. [Medium-wide / Medium close-up waist-up + Góc máy điện ảnh luân phiên] shot at/inside [1 bối cảnh kiến trúc hoặc kết cấu bám đất có "điểm sai" siêu thực về hình khối uốn cong đa chiều, tỷ lệ hoặc vị trí xây dựng phi chuẩn mực] with stylized stop-motion figure(s) with matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [Mô tả nhân vật 4 trục tinh gọn phù hợp cỡ cảnh + biểu cảm ánh mắt, nụ cười + hành động gắn kết/chiêm nghiệm]. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9

# Mẫu 2 — Đại cảnh & Toàn cảnh Kiến trúc/Địa hình Siêu thực có Người ở xa hoặc Đông người (Extreme wide / Wide):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town with realistic natural water, clouds, trees, and stone, [time-of-day] light, asymmetric unplanned organic layout, monumental surreal scale, expansive scenic focus with generous open negative space on one side and gentle atmospheric depth. [Extreme wide panoramic / Wide + Góc máy] shot showcasing [1 kỳ quan kiến trúc hoặc kết cấu bám đất mang "điểm sai" siêu thực về hình khối uốn cong ngang-đứng, tỷ lệ hoặc vị trí địa hình kỳ vĩ], where tiny distant miniature townspeople in varied warm clothing [hoạt động sinh hoạt hoặc lễ hội nhìn từ xa hòa vào không gian]. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9

# Mẫu 3 — Cảnh Tĩnh vật B-Roll hoặc Cảnh Sắc Không Gian Siêu Thực (Vắng bóng người):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town with realistic natural water, clouds, trees, and stone, [time-of-day] light, asymmetric organic composition, [shallow depth of field with a softly blurred warm background | expansive scenic focus with generous open negative space]. [Close-up / Extreme wide + Góc máy] shot of [1 chi tiết vật dụng hoặc công trình bám đất mang "điểm sai" siêu thực về hình khối, tỷ lệ hoặc kết cấu giữa thiên nhiên chân thực], completely without people. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9
```

---

## 2. Luật Đầu Ra (`image.txt`)

- **Thiên nhiên Chân thực, Bám đất & "Điểm Sai Kiến trúc Siêu thực" (`Khối 1`):**
  - Mở đầu bằng `2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town with realistic natural water, clouds, trees, and stone, [time-of-day] light, asymmetric [organic composition | unplanned organic layout]`.
  - Giữ nguyên bản chất tự nhiên chân thực của nước, mây, bầu trời, cây cối và đất đá; mọi công trình và vật thể đều bám vững trên mặt đất, vách đá hoặc mặt nước.
  - **Mỗi câu lệnh bắt buộc phải chứa ít nhất 1 "Điểm Sai Siêu Thực" (`Surreal Architectural / Structural Paradox`)**: tự do bẻ cong hình khối kiến trúc theo cả chiều ngang lẫn chiều thẳng đứng, phá vỡ quy chuẩn tỷ lệ hoặc vị trí xây dựng thông thường để tạo sự kỳ diệu độc bản cho từng cảnh, tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
  - Chọn `shallow depth of field with a softly blurred warm background` cho Cảnh Trung/Cận (`Mẫu 1` & `Mẫu 3 Close-up`); chọn `expansive scenic focus with generous open negative space on one side and gentle atmospheric depth` cho Đại cảnh/Toàn cảnh (`Mẫu 2` & `Mẫu 3 Wide`).
- **Phân cấp mô tả Con người theo Cỡ cảnh (`Mẫu 1` vs `Mẫu 2`):**
  - **Ở Đại cảnh & Toàn cảnh (`Extreme wide / Wide` — `Mẫu 2`):** Dành trọn trọng tâm mô tả cho kỳ quan kiến trúc siêu thực và thiên nhiên chân thực; chỉ gọi tên con người bằng cụm từ quy mô nhỏ ở xa (`tiny distant miniature townspeople in varied warm clothing`).
  - **Ở Cảnh Trung & Cận (`Medium-wide / Medium close-up` — `Mẫu 1`):** Dùng phôi rối cách điệu (`matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown`) kết hợp mô tả 4 trục cho 1–2 nhân vật đang sinh hoạt tự nhiên trong bối cảnh đó.
- **Một nguồn sáng chính duy nhất (`Khối cuối`):** Khóa ở cuối mỗi câu lệnh một nguồn sáng tự nhiên duy nhất chiếu theo một hướng bóng đổ thống nhất (`Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9`).
