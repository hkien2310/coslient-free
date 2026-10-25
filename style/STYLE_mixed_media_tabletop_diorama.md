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
- **Đầu ra 1 — Cấu trúc file `character.md`:**
  - Nhân vật xuất hiện xuyên suốt nhiều cảnh: định nghĩa mã `@Tên_nhân_vật` kèm cụm nhận diện 4 trục (`4-Axis & Accent Phrase`) và `Character Prompt` (điều chỉnh linh hoạt phần thân dưới khi cảnh lấy cỡ bán thân `Waist-up / Medium close-up`).
  - Nhân vật xuất hiện lẻ ở từng cảnh: mô tả trực tiếp bằng công thức 4 trục tại cảnh đó trong `storyboard.md` và `image.txt`.

```markdown
# CHARACTERS: [TÊN TRACK]

1. **@[Tên_1]** ([Vai trò & độ tuổi bằng tiếng Việt]):
   - **4-Axis & Accent Phrase (Dùng trong `image.txt`):** `a [tall slender / medium-height slender] [character role/age] with [Trục 2: Eyewear / Facial Hair / Headwear] and [style + color] cotton-fiber hair in [Trục 4: Trang phục vải dệt + điểm nhấn màu sắc, kèm quần dài/váy dài và giày khi lấy cảnh toàn thân]`
   - **Character Prompt:** `2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town, clean natural daylight, harmonious character-to-object scale, shallow depth of field with a softly blurred warm studio backdrop. Wide full-body character reference portrait of a stylized stop-motion figure with matte paper-pulp skin, a soft rounded nose, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [4-Axis & Accent Phrase with footwear resting on a wooden base], standing in a relaxed natural posture with calm gentle warmth. Single directional warm afternoon light casting a single coherent shadow direction --ar 16:9`

2. **@[Tên_Trẻ_Nhỏ]** *(khi câu chuyện có nhân vật trẻ nhỏ)*:
   - **4-Axis & Accent Phrase (Dùng trong `image.txt`):** `a waist-high little [child role] with [style + color] cotton-fiber hair and [phụ kiện nhỏ] in [Trục 4: Trang phục vải dệt + điểm nhấn màu sắc]`
   - **Character Prompt:** `2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town, clean natural daylight, harmonious character-to-object scale, shallow depth of field with a softly blurred warm studio backdrop. Wide full-body character reference portrait of a waist-high stylized stop-motion child with matte paper-pulp skin, a soft rounded nose, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [4-Axis & Accent Phrase with footwear resting on a wooden base], standing in a relaxed natural posture with a gentle warm expression. Single directional warm afternoon light casting a single coherent shadow direction --ar 16:9`
```

- **Đầu ra 2 — Khung câu lệnh 4 khối tiếng Anh cho `image.txt` (1 dòng/cảnh khớp 1:1 với `storyboard.md`):**

```text
# 1. Cảnh có Nhân vật:
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town, [time-of-day] light, harmonious character-to-object scale, [shallow depth of field with a softly blurred warm background | expansive scenic focus with generous open negative space and gentle atmospheric depth]. [Cỡ cảnh tương thích không gian + Góc máy điện ảnh giàu chiều sâu (low-angle / high-angle / over-the-shoulder / diagonal perspective / framing through foreground)] shot [bối cảnh không gian sống, con đường, phương tiện hoặc cảnh quan thơ mộng nguyên vẹn mọc ra từ câu chuyện bài hát] with stylized stop-motion figure(s) with matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [Mô tả nhân vật 4 trục tinh gọn phù hợp cỡ cảnh + trạng thái cảm xúc sâu sắc trên gương mặt, ánh mắt, dáng điệu + hành động mang ý nghĩa sẻ chia, gắn kết hoặc chiêm nghiệm]. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9

# 2. Cảnh Tĩnh vật B-Roll hoặc Cảnh Sắc Không Gian (Vắng bóng người):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town, [time-of-day] light, [shallow depth of field with a softly blurred warm background | expansive scenic focus with generous open negative space]. [Close-up / Wide + Góc máy] shot of [1 chi tiết vật dụng đời thường bo tròn sơn mờ giàu sức gợi hoặc một khung cảnh thiên nhiên/kiến trúc thơ mộng thoáng rộng], completely without people. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9
```

---

## 2. Luật Đầu Ra (`character.md` & `image.txt`)

- **Thế giới, Khoảng thở & Độ sâu trường ảnh (`Khối 1`):**
  - Mở đầu bằng `2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town, [time-of-day] light, harmonious character-to-object scale`.
  - Chọn `shallow depth of field with a softly blurred warm background` khi tập trung vào cảm xúc con người, tương tác gần hoặc tĩnh vật chi tiết (`Close-up / Medium close-up / Waist-up / Medium-wide`).
  - Chọn `expansive scenic focus with generous open negative space and gentle atmospheric depth` khi mở rộng không gian sinh hoạt hoặc đại cảnh hành trình (`Wide / Extreme wide panoramic`).
  - Các công trình kiến trúc siêu thực, phương tiện và vật dụng đời thường được bo tròn sơn mờ thủ công (`softly rounded matte-painted tactile everyday objects and vehicles`), tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
- **Phôi rối cách điệu liền khối (`Khối 2`):** Mọi nhân vật có chung làn da giấy bồi mờ (`matte paper-pulp skin`), mũi tròn mềm (`soft rounded noses`), tỷ lệ hình thể thanh mảnh kéo dài (`slender elongated proportions`) và mái tóc/râu sợi bông xù dày phủ kín đỉnh đầu (`thick full fluffy cotton-fiber hair covering the crown`).
- **Công thức nén nhận diện 4 trục & Tương phản nhóm (`Khối 3`):**
  - **Trục 1 — Dáng vóc:** Phân biệt rõ người lớn cao mảnh (`tall slender`), người lớn tầm vóc cân đối (`medium-height slender`) và trẻ nhỏ cao ngang thắt lưng người lớn (`waist-high child`).
  - **Trục 2 — Phụ kiện vùng đầu:** Đa dạng hóa râu, kính mắt và mũ đội đầu.
  - **Trục 3 — Tóc sợi bông:** Đa dạng màu sắc và kiểu tạo hình tóc sợi bông phủ kín đỉnh đầu.
  - **Trục 4 — Trang phục vải dệt & Điểm nhấn:** Trang phục vải dệt phẳng tự nhiên kèm điểm nhấn sắc độ riêng; mô tả đủ bộ từ áo, quần dài/váy dài đến giày chạm mặt phẳng khi lấy cảnh toàn thân (`Wide / Medium-wide full-body`), hoặc tập trung vào phần thân trên và cử chỉ đôi tay khi lấy cảnh bán thân có vách che (`Medium close-up / Waist-up`). Khi cảnh có nhóm người, phối hợp đa dạng cả 4 trục để mỗi nhân vật tách biệt rõ.
- **Cự ly ấm áp, Trạng thái cảm xúc & Ý nghĩa khoảnh khắc:** Đặt nhân vật ở cự ly gần gũi tự nhiên (`warm conversational proximity with clean silhouette clarity`), làm nổi bật trạng thái cảm xúc chân thật (niềm vui sẻ chia, sự biết ơn, nỗi bâng khuâng, sự bình yên tĩnh tại) qua ánh mắt, nét mặt và ngôn ngữ cơ thể có hồn trong từng khung hình.
- **Một nguồn sáng chính duy nhất (`Khối 4`):** Khóa ở cuối mỗi câu lệnh một nguồn sáng tự nhiên duy nhất chiếu theo một hướng bóng đổ thống nhất (`Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9`).
