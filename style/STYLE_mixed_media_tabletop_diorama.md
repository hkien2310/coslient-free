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
  - Mô tả trực tiếp nhân vật đa dạng theo từng cảnh hoặc cụm 2–3 cảnh trong `storyboard.md` và `image.txt` bằng công thức 4 trục; chỉ tạo `character.md` khi cần lưu mẫu tham chiếu riêng.

```markdown
# CHARACTERS: [TÊN TRACK]

1. **@[Tên_1]** ([Vai trò & độ tuổi bằng tiếng Việt]):
   - **4-Axis & Accent Phrase (Dùng trong `image.txt`):** `a [tall slender / medium-height slender] [character role/age] with [Trục 2: Eyewear / Facial Hair / Headwear] and [style + color] cotton-fiber hair in [Trục 4: Trang phục vải dệt + điểm nhấn màu sắc, kèm quần dài/váy dài và giày khi lấy cảnh toàn thân]`
   - **Character Prompt:** `2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], clean natural daylight, harmonious character-to-object scale, shallow depth of field with a softly blurred warm studio backdrop. Wide full-body character reference portrait of a stylized stop-motion figure with matte paper-pulp skin, a soft rounded nose, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [4-Axis & Accent Phrase with footwear resting on a wooden base], standing in a relaxed natural posture with calm gentle warmth. Single directional warm afternoon light casting a single coherent shadow direction --ar 16:9`
```

- **Đầu ra 2 — Khung câu lệnh 4 khối tiếng Anh cho `image.txt` (1 dòng/cảnh khớp 1:1 với `storyboard.md`):**

```text
# 1. Cảnh Trung & Cận có Nhân vật (Medium-wide / Waist-up / Medium close-up):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], [time-of-day] light, harmonious character-to-object scale, shallow depth of field with a softly blurred warm background. [Medium-wide full-body / Medium close-up waist-up + Góc máy điện ảnh luân phiên] shot [công trình kiến trúc siêu thực hoặc không gian sống thơ mộng cao lớn vượt trội] with stylized stop-motion figure(s) with matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [Mô tả 1-2 nhân vật theo 4 trục phù hợp cỡ cảnh + trạng thái cảm xúc sâu sắc trên gương mặt, ánh mắt, dáng điệu + hành động tương tác có ý nghĩa]. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9

# 2. Đại cảnh Kiến trúc Siêu thực & Không gian Rộng (Extreme wide / Wide panoramic):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], [time-of-day] light, monumental architectural scale, expansive scenic focus with generous open negative space and gentle atmospheric depth. [Extreme wide panoramic / Wide + Góc máy] shot of [công trình kiến trúc siêu thực khổng lồ và cảnh quan thiên nhiên kỳ vĩ], [completely without people | with tiny distant figures in simple warm attire strolling far below the towering structures]. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9

# 3. Cảnh Tĩnh vật B-Roll (Close-up):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], [time-of-day] light, shallow depth of field with a softly blurred warm background. [Close-up + Góc máy] shot of [1 chi tiết vật dụng hoặc yếu tố siêu thực bo tròn sơn mờ giàu sức gợi], completely without people. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9
```

---

## 2. Luật Đầu Ra (`character.md` & `image.txt`)

- **Thế giới, Khoảng thở & Độ sâu trường ảnh (`Khối 1`):**
  - Mở đầu bằng `2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], [time-of-day] light, harmonious character-to-object scale` (gọi tên rõ đặc điểm kỳ lạ xuyên suốt của thị trấn đó).
  - Chọn `shallow depth of field with a softly blurred warm background` khi tập trung vào cảm xúc con người, tương tác gần hoặc tĩnh vật chi tiết (`Close-up / Medium close-up / Waist-up / Medium-wide`).
  - Chọn `expansive scenic focus with generous open negative space and gentle atmospheric depth` khi mở rộng không gian sinh hoạt hoặc đại cảnh hành trình (`Wide / Extreme wide panoramic`).
  - Các công trình kiến trúc siêu thực, phương tiện và vật dụng đời thường được bo tròn sơn mờ thủ công (`softly rounded matte-painted tactile everyday objects and vehicles`), tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
- **Phôi rối cách điệu & Công thức 4 trục cho Cảnh Trung / Cận (`Khối 2 & 3`):**
  - Chỉ áp dụng cụm phôi rối (`matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown`) và công thức nhận diện 4 trục cho **1–2 nhân vật ở cảnh Trung và Cận (`Medium-wide / Waist-up / Medium close-up`)**.
  - Ở **Đại cảnh (`Extreme wide / Wide panoramic`)**, chỉ mô tả kiến trúc siêu thực đồ sộ (`monumental architectural scale`) kèm `completely without people` hoặc `with tiny distant figures in simple warm attire strolling far below` để bảo toàn tỷ lệ công trình cao lớn gấp nhiều lần con người.
  - **4 trục nhận diện ở cảnh Trung & Cận:** (1) Dáng vóc (`tall slender`, `medium-height slender`, `waist-high child`), (2) Phụ kiện vùng đầu, (3) Tóc sợi bông, (4) Trang phục vải dệt phẳng tự nhiên kèm điểm nhấn sắc độ riêng (đủ bộ đến giày chạm mặt phẳng khi lấy `Medium-wide full-body`, hoặc chỉ thân trên và đôi tay khi lấy `Medium close-up / Waist-up`). Đổi mới trang phục và nhân vật qua từng Đại Cảnh để tạo sự đa dạng phong phú.
- **Cự ly ấm áp, Trạng thái cảm xúc & Ý nghĩa khoảnh khắc:** Đặt nhân vật ở cự ly gần gũi tự nhiên (`warm conversational proximity with clean silhouette clarity`), làm nổi bật trạng thái cảm xúc chân thật (niềm vui sẻ chia, sự biết ơn, nỗi bâng khuâng, sự bình yên tĩnh tại) qua ánh mắt, nét mặt và ngôn ngữ cơ thể có hồn trong từng khung hình.
- **Một nguồn sáng chính duy nhất (`Khối 4`):** Khóa ở cuối mỗi câu lệnh một nguồn sáng tự nhiên duy nhất chiếu theo một hướng bóng đổ thống nhất (`Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9`).
