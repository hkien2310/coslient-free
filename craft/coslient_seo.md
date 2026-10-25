# COSLIENT SEO — QUY CHUẨN SIÊU DỮ LIỆU & THUMBNAIL YOUTUBE (`6-seo.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Đóng gói siêu dữ liệu phát hành YouTube và DistroKid (`6-seo.md`), bao gồm Title, bộ 3 Prompt Thumbnail chuyên biệt tối ưu CTR, Description, Tags, Pinned Comment, Shorts và phân phối Playlist. Toàn bộ thông số chất liệu tạo hình Stop-Motion và khung câu lệnh 4 khối tham chiếu từ [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra (`6-seo.md`)

- **Đầu vào:** `1-idea.md`, `2-music.md`, `3-lyrics.txt`, [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md), [`ref/youtube_playlists.md`](../ref/youtube_playlists.md), [`ref/distrokid.md`](../ref/distrokid.md) và [`ref/bandcamp.md`](../ref/bandcamp.md).
- **Đầu ra:** File `6-seo.md` theo đúng khung mẫu dưới đây, đồng thời cập nhật bài hát mới vào [`ref/distrokid.md`](../ref/distrokid.md) và [`ref/bandcamp.md`](../ref/bandcamp.md):

````markdown
# SEO: [TÊN VIDEO / DỰ ÁN]

## 1. FILE NAME (TRƯỚC KHI UPLOAD)
- **Video File:** `[story-clause-slug].mp4`
- **Thumbnail File:** `[story-clause-slug]-thumbnail.jpg`

## 2. TITLE (DƯỚI 70 KÝ TỰ)
```text
[Mệnh đề câu chuyện hoặc tên bài thơ mộng] | A Dream Town (4K)
```
*(Dự phòng 1: `[Mệnh đề câu chuyện dự phòng 1] | Short Folk Film (4K)`)*  
*(Dự phòng 2: `[Mệnh đề câu chuyện dự phòng 2] | A Dream Town (4K)`)*

## 3. THUMBNAIL (3 PROMPTS POSTER TUYỂN CHỌN 1)
- **Ý tưởng Poster & Tương phản chủ đạo:** [Tóm tắt 3 ý tưởng Poster và cặp tương phản ánh sáng – màu sắc]
- **Text gợi ý (2-3 từ cô đọng khi cần thiết kế ngoài):** `[2-3 TỪ LỚN GỌN GÀNG]`

### Prompt 1 - Poster Không Gian Thơ Mộng & Câu Chuyện (`Wide Poetic World & Story`):
```text
Handcrafted stop-motion animation film still set in a warm poetic surreal town, golden morning light, harmonious character-to-object scale, expansive scenic focus with generous open negative space and gentle atmospheric depth. [Wide / Medium-wide] eye-level [three-quarter / side-profile] shot in [không gian sống, con đường hoặc bối cảnh thơ mộng đặc trưng nhất mọc ra từ câu chuyện bài hát] with stylized stop-motion figures with matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [Nhân vật A mô tả 4 trục tinh gọn + tư thế tự nhiên có hồn] close beside [Nhân vật B mô tả 4 trục tinh gọn ở cự ly gần gũi ấm áp + cử chỉ tương tác tự nhiên]. Single directional morning sunlight casting a single coherent shadow direction --ar 16:9
```

### Prompt 2 - Poster Ánh Sáng & Hành Trình Đồng Hành (`Wide Light & Journey`):
```text
Handcrafted stop-motion animation film still set in a warm poetic surreal town, warm golden afternoon light, harmonious character-to-object scale, expansive scenic focus with generous open negative space and gentle atmospheric depth. Wide eye-level [three-quarter / side-profile] shot along [cung đường, hiên nhà, khu vườn hoặc phương tiện đồng hành đặc trưng của bài hát] with stylized stop-motion figures with matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [Nhân vật A mô tả 4 trục tinh gọn + tư thế hành trình hoặc sẻ chia tự nhiên] alongside [Nhân vật B mô tả 4 trục tinh gọn ở cự ly gần gũi + tư thế đồng hành]. Single directional golden afternoon sunlight casting a single coherent shadow direction --ar 16:9
```

### Prompt 3 - Poster Khoảnh Khắc Gắn Kết Đắt Giá (`Medium Close-Up / Medium-Wide Soulful Connection`):
```text
Handcrafted stop-motion animation film still set in a warm poetic surreal town, warm sunset light, harmonious character-to-object scale, shallow depth of field with a softly blurred warm background. [Medium close-up waist-up / Medium-wide] eye-level three-quarter shot beside [kiến trúc hoặc vật dụng đời thường bo tròn sơn mờ ấm áp] with stylized stop-motion figures with matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [Nhân vật A mô tả 4 trục tinh gọn + tư thế thư thái gắn kết] close opposite [Nhân vật B mô tả 4 trục tinh gọn ở cự ly gần gũi + tư thế đón nhận]. Single directional warm sunset light casting a single coherent shadow direction --ar 16:9
```

## 4. DESCRIPTION
```text
[2-3 câu tâm tình như thư tay chia sẻ cảm hứng đời sống và sự đồng cảm với người nghe]

⏱ CHAPTERS:
00:00 [Tên Bài 1 / Chương 1]
[MM:SS] [Tên Bài 2 / Chương 2 — khớp từng giây với file âm thanh thực tế]

🎧 Spotify: https://open.spotify.com/artist/4FVU7hNPy3mc5HAm68iSB9
🍎 Apple Music: https://music.apple.com/us/artist/coslient/1895068939
🎹 Bandcamp: https://coslient.bandcamp.com

---
LYRICS:
[Dán đầy đủ lời bài hát đã hiệu đính khớp 100% với bản thu và 3-lyrics.txt]
---

Every song and miniature world on this channel begins with human feeling and the real life stories you share with us in the comments.
Original Music & Visuals by Coslient

#adreamtown #coslient #stopmotion #[hashtag_tâm_lý] #[hashtag_nhạc_folk] #[hashtag_không_gian]
```

## 5. TAGS (THÊM NGOÀI DEFAULT THEO 3 TẦNG NGỮ NGHĨA)
```text
[3 cụm tâm lý/độ tuổi 55-85+], [2-3 cụm thể loại/nhạc cụ folk mộc], [2-3 cụm mỹ học stop-motion/không gian bài hát]
```

## 6. PINNED COMMENT (MỞ SỔ LƯU NIỆM KÝ ỨC)
```text
[1 câu hỏi ấm áp đánh thức kỷ niệm cá nhân gắn với bài hát + 1 câu nhắn trân trọng mời khán giả chia sẻ câu chuyện đời thực]
```

## 7. SHORTS (15–30 GIÂY)
- **Đoạn:** `[MM:SS - MM:SS]`
- **Title Shorts:** `[Mệnh đề cảm xúc ngắn gọn] #shorts #adreamtown`

## 8. PLAYLISTS, DISTROKID & BANDCAMP
### YouTube Playlists:
```text
[Tên Playlist Mood — tra từ youtube_playlists.md]
[Tên Playlist Album/EP — khớp DistroKid]
The Universe Hidden Inside the Mind | All Videos
```
### DistroKid Release:
```text
Track Title: [Tên bài] | Artist: Coslient | Album / EP: [Tên Album/EP trong distrokid.md] | Genre: Singer-Songwriter / Folk
```
### Bandcamp Release:
```text
Track Title: [Tên bài] | Album: [Tên Album trên Bandcamp] | URL: [URL Album] | Price: $1.50
About this track: [1-2 câu tiếng Anh tóm tắt câu chuyện bài hát]
```
````

---

## 2. Luật Đầu Ra (`6-seo.md`)

- **Luật Title & File Name (`<70 ký tự`):**
  - Đặt mệnh đề cảm xúc câu chuyện hoặc tên bài hát lên đầu tiêu đề trước hậu tố (`| A Dream Town (4K)` hoặc `| Short Folk Film (4K)`), tổng độ dài dưới 70 ký tự và đồng bộ với tên file `.mp4` / `-thumbnail.jpg`.
  - Mệnh đề tiêu đề phản ánh trung thực nội dung bài và khơi gợi sự đồng cảm/tò mò ở khán giả 45–85+ (gợi chốn về bình yên, người/vật chứng nhân qua năm tháng, lời thủ thỉ đa tầng nghĩa hoặc sự gắn bó ấm áp).
- **Luật 3 Prompt Poster Thumbnail (`--ar 16:9`):**
  - Tuân thủ 100% khung câu lệnh 4 khối trực quan, công thức nhân vật 4 trục của [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md) và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
  - Thiết kế như 3 Poster phim độc bản có độ tương phản ánh sáng – màu sắc nổi bật ở kích thước thu nhỏ, khác nhau rõ về quy mô: (1) *Không gian thơ mộng & Câu chuyện (`Wide / Medium-wide`)*, (2) *Ánh sáng & Hành trình đồng hành (`Wide`)*, (3) *Khoảnh khắc gắn kết đắt giá (`Medium close-up / Medium-wide` xóa phông mờ dịu)*.
- **Luật Description 4 trụ cột & Hashtags:**
  - Hội tụ đủ: (1) 2–3 câu mở đầu tâm tình như thư tay chuẩn [`humanizer`](../.agents/skills/humanizer/SKILL.md); (2) `⏱ CHAPTERS` khớp từng giây với file âm thanh kèm đủ link Spotify, Apple Music, Bandcamp; (3) `LYRICS` khớp 100% với `3-lyrics.txt`; (4) Tuyên ngôn nghệ thuật con người và 6 hashtags (`#adreamtown #coslient #stopmotion` + 3 hashtags theo tâm lý, nhạc Folk, không gian).
- **Luật Tags 3 tầng ngữ nghĩa:**
  - Ngoài bộ Tags cố định của kênh (`coslient, a dream town, original music, stop motion, handcrafted animation, miniature world, indie folk, acoustic, healing music, nostalgic song, a very old town, three quarter town`), bổ sung 6–9 cụm từ khóa riêng phủ đủ 3 tầng: (1) *Tâm lý & Giai đoạn cuộc đời 55–85+ (3 cụm)*, (2) *Thể loại & Nhạc cụ Folk mộc thực tế trong bài (2–3 cụm)*, (3) *Mỹ học Stop-Motion & Không gian bài hát (2–3 cụm)*.
- **Luật Pinned Comment, Shorts & Phân phối:**
  - Ghim 1 câu hỏi ấm áp đánh thức hồi ức cá nhân của người xem (làm chất liệu hạt giống cho các dự án sau); trích xuất đoạn Shorts `15–30s` đắt giá nhất; tra cứu và cập nhật đồng bộ bài hát mới vào cả [`ref/youtube_playlists.md`](../ref/youtube_playlists.md), [`ref/distrokid.md`](../ref/distrokid.md) và [`ref/bandcamp.md`](../ref/bandcamp.md).
