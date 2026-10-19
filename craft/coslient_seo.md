# COSLIENT SEO — QUY CHUẨN SIÊU DỮ LIỆU & THUMBNAIL YOUTUBE (`6-seo.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Đóng gói siêu dữ liệu phát hành YouTube và DistroKid (`6-seo.md`), bao gồm Title, bộ 3 Prompt Thumbnail chuyên biệt tối ưu CTR, Description, Tags, Pinned Comment, Shorts và phân phối Playlist. Toàn bộ thông số chất liệu tạo hình Stop-Motion tham chiếu từ [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. **Ưu tiên dùng khẳng định hơn phủ định:** Hướng dẫn trực tiếp cấu trúc tiêu đề, bố cục khung hình Thumbnail và thông số cần đạt bằng câu khẳng định rõ ràng.
>   2. **Luôn Rule hóa thông tin (`Rule-First`) & Hạn chế tối đa thiên kiến liệt kê:** Khái quát hóa mọi nguyên lý thành quy tắc chung hoạt động cho mọi bài hát và mọi bối cảnh toàn kênh; tránh liệt kê danh sách đạo cụ hay tình huống cụ thể gây thiên kiến lặp lại cho AI.
>   3. **Ưu tiên thêm mới và làm giàu quy tắc, bảo toàn dữ liệu:** Chỉnh sửa cục bộ đúng chỗ cần thiết (`/ponytail`, `/humanizer`), giữ nguyên mọi trường nhập YouTube Studio trong ô code block (` ```text `) để copy 1-click.

---

## 1. CÔNG THỨC TITLE & FILE NAME

### File Name (Trước khi upload):
- Video: `[story-hook-slug].mp4` (ví dụ: `he-kept-a-chair-waiting.mp4`)
- Thumbnail: `[story-hook-slug]-thumbnail.jpg`

### Title (Dưới 70 ký tự):
- **Cấu trúc linh hoạt (2 lựa chọn):**
  * **Kiểu A — Tên bài thơ mộng + Nhãn định dạng (Khuyên dùng cho Soul Sanctuary):**  
    `[Song Title] | A Dream Town (4K)` hoặc `[Song Title]… | Surreal AI Film (4K)`  
    *(Ví dụ thực tế kiểm chứng: "The House That Waited at the End of the Road | Three-Quarter Town", "Still Walking Beside You… | Surreal AI Film (4K)")*
  * **Kiểu B — Story Hook gợi tò mò:**  
    `[1 câu chuyện gợi tò mò — ai, làm gì, thiếu mảnh gì] | A Dream Town`  
    *(Ví dụ: "He kept a chair waiting for an old friend | A Dream Town")*
- **Lưu ý:** Cho phép gắn nhãn giá trị cao `(4K)` hoặc `Surreal AI Film` để kích hoạt đề xuất hiển thị trên màn hình lớn. Không nhồi nhét tên kênh "Coslient" hay nhãn thể loại thừa vào title.

---

## 2. QUY CHUẨN DESCRIPTION & TAGS

### Description (3 dòng đầu là Story Hook):
- 2–3 câu kể chuyện tự nhiên như đang nói với bạn bè, không viết văn mẫu quảng cáo.
- Đính kèm link Spotify, Apple Music, toàn bộ Lyrics và Hashtags.

### Tags Mặc Định (Cố định kênh):
```text
coslient, a dream town, original music, stop motion, handcrafted animation, miniature world, indie folk, acoustic, healing music, nostalgic song, a very old town, three quarter town
```
- Khi upload: Thêm 5–7 tag riêng theo nội dung bài vào ô nhập.

### Hashtags (Cuối Description):
```text
#adreamtown #coslient #stopmotion + [3 hashtag theo bài]
```

---

## 3. QUY CHUẨN THUMBNAIL (3 PROMPTS POSTER TUYỂN CHỌN 1) & SHORTS

### 3.1. Bốn nguyên tắc thiết kế Thumbnail chuẩn Poster Phim Điện Ảnh (Đẹp hơn cảnh thường & Tối ưu CTR)
1. **Giữ nguyên 100% cú pháp nghệ thuật của `image.txt` (Không chèn từ khóa bố cục kỹ thuật máy móc):** Câu lệnh Thumbnail dùng chính xác 100% khung câu lệnh chuẩn của [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md) để giữ trọn vẻ đẹp điêu khắc, ánh sáng phim nhựa Kodak 35mm và chiều sâu không gian của thế giới Stop-Motion (không chèn các cụm từ kỹ thuật khô cứng như `% diện tích khung hình`, `góc dưới bên phải` hay `vị trí 1/3` vào câu lệnh tiếng Anh vì sẽ làm AI vẽ phẳng và mất chất điện ảnh).
2. **Nâng cấp ý tưởng lên tầm "Poster Phim Độc Bản" (Hội tụ đỉnh cao chất thơ của cả video):** Thay vì chỉ minh họa một câu hát chuyển tiếp như cảnh thường, mỗi Thumbnail là một bức Poster độc lập gói trọn linh hồn của cả video: kết hợp trực tiếp **Nhân vật chính + Đạo cụ biểu tượng đắt giá nhất + Bối cảnh kiến trúc/thiên nhiên choáng ngợp** để người xem vừa bị hút mắt bởi vẻ đẹp hội họa vừa tự hỏi *"Câu chuyện phía sau khung hình này là gì?"*.
3. **Đẩy kịch trần độ tương phản màu khoáng chất và ánh sáng (`70% - 20% - 10%`):** Chọn thời khắc ánh sáng đẹp và kịch tính nhất (hoàng hôn đỏ cam rực rỡ trên nền biển xanh sapphire thẫm, nắng chiều vàng hổ phách xiên qua vách đá biển coban, hoặc ánh đèn lồng/ánh nến vàng ấm giữa đêm xanh chàm) để chủ thể và đạo cụ tự động bật sáng rực rỡ trên giao diện YouTube.
4. **Quy trình xuất 3 Prompt Poster cho mỗi Video YouTube để tạo và chọn 1 tấm xuất sắc nhất:** Dù dự án có 1 hay 2 bài hát gộp chung thành 1 video, mỗi video chỉ dùng **1 bộ SEO thống nhất** trong `6-seo.md` và xuất **3 câu lệnh tiếng Anh hoàn chỉnh** (`no text --ar 16:9`) đại diện cho 3 ý tưởng Poster đắt giá nhất:
   - **Prompt 1 — Poster Chất Ngông Chân Trời (`35mm` Iconic Poetic Horizon):** Khung hình trung-rộng toàn thân (`Spacious full-body wide shot`) đặt nhân vật và đạo cụ biểu tượng trên một điểm tựa kiến trúc hoặc địa hình cao khoáng đạt trước biển/trời bao la (Động cơ 1 & 2), tạo sự đối sánh tỷ lệ đầy chất thơ như một poster phim hoạt hình nghệ thuật.
   - **Prompt 2 — Poster Phép Màu Ánh Sáng & Ẩn Dụ (`35mm` Dramatic Light & Metaphor):** Khung hình trung cảnh hoặc trung-rộng khai thác phép màu thị giác mạnh nhất của video: bóng đổ khổng lồ in lên tường đá dưới nắng xiên thấp, phương tiện cổ điển lướt gió, hoặc nguồn sáng đèn lồng/ánh nến ấm rực thắp lên giữa không gian chạng vạng xanh coban sâu thẫm (Động cơ 3 & 4).
   - **Prompt 3 — Poster Khoảnh Khắc Gắn Kết Đắt Giá (`50mm` Soulful Storyteller Mid-Shot):** Khung hình trung cảnh cắt ngang thắt lưng (`Intimate medium waist-up shot`) đặt trong không gian kiến trúc mở nhìn ra cảnh sắc thiên nhiên có chiều sâu bokeh dịu, bắt trọn biểu cảm lắng đọng và cử chỉ gắn kết tình cảm sâu sắc nhất giữa các nhân vật cùng đạo cụ trung tâm.

### 3.2. Shorts
- **Shorts:** Dưới 30 giây, trích đoạn hook âm nhạc mạnh nhất, đăng trước video full 1–2 ngày.

---

## 4. PHÂN PHỔI PLAYLIST & DISTROKID
- **YouTube Playlists (Quy tắc 3 chạm):** Tra cứu chọn đúng 1 Mood Playlist, 1 Album Playlist và 1 Master Playlist tại [`../ref/youtube_playlists.md`](../ref/youtube_playlists.md).
- **DistroKid Album:** Tra cứu chọn đúng Album/EP tại [`distrokid.md`](../ref/distrokid.md).

---

## 5. SEO FILE TEMPLATE (1-CLICK COPY READY — 1 BỘ SEO THỐNG NHẤT CHO 1 VIDEO)

File `6-seo.md` chuẩn cho mỗi project (khi project gồm 2 bài hát ghép thành 1 video YouTube, gộp chung trong 1 bộ SEO duy nhất kèm `⏱ CHAPTERS` trong Description và tách 2 bài ở mục DistroKid cuối file):

````markdown
# SEO: [TÊN VIDEO / DỰ ÁN]

## 1. FILE NAME (TRƯỚC KHI UPLOAD)

### Video File:
```text
[story-hook-slug].mp4
```

### Thumbnail File:
```text
[story-hook-slug]-thumbnail.jpg
```

## 2. TITLE (DƯỚI 70 KÝ TỰ)
```text
[1 câu chuyện hoặc tên bài thơ mộng] | Surreal AI Folk Film (4K)
```

*(Dự phòng 1: `[Story Hook dự phòng 1] | A Dream Town (4K)`)*  
*(Dự phòng 2: `[Story Hook dự phòng 2] | Surreal Folk Film (4K)`)*

## 3. THUMBNAIL (3 PROMPTS POSTER TUYỂN CHỌN 1)
- **Ý tưởng Poster & Tương phản chủ đạo:** [Tóm tắt 3 ý tưởng Poster hội tụ linh hồn của video và cặp tương phản ánh sáng – màu sắc]
- **Text gợi ý (nếu chèn ngoài, 2-3 từ):** `[2-3 TỪ LỚN GỌN GÀNG]` *(hoặc để trống như Poster phim)*

### Prompt 1 — Poster Chất Ngông Chân Trời (`35mm` Iconic Poetic Horizon):
```text
Cinematic European arthouse stop-motion animation film still, rich Kodak 35mm analog film color grading, crystal-clear air, tactile handcrafted surfaces with lived-in timeless patina and sfumato soft edges. Spacious full-body wide shot from a [low-angle upward / 45-degree high-angle] three-quarter view with generous open scenic space on an expansive open-air [điểm tựa kiến trúc/vách đá/bến cảng ấn tượng nhất nhìn ra thiên nhiên bao la] of stylized 1:7.5 figure(s) with warm natural hand-molded matte paper-pulp skin: [Chế độ 1 gọi @Tên_nhân_vật | Chế độ 2 tả trực tiếp nhân vật], with a subtle charcoal-black and saffron-yellow accent on [chi tiết nhỏ], in a carefree unbuttoned bohemian posture [hành động chất ngông thơ mộng và tương tác đạo cụ biểu tượng đắt giá nhất của video]. Single directional [nguồn sáng ấm rực rỡ: warm amber-gold afternoon sunlight / blazing orange-gold sunset light] casting a single coherent shadow direction across a mineral palette of 70% [màu biển/trời xanh sâu thẫm: deep cobalt / deep sapphire], 20% [màu kiến trúc/địa hình và trang phục], and 10% [màu điểm nhấn đạo cụ rực rỡ + charcoal-black and saffron-yellow accents] with 35mm crisp deep environmental focus and clear horizon, no text --ar 16:9
```

### Prompt 2 — Poster Phép Màu Ánh Sáng & Ẩn Dụ (`35mm` Dramatic Light & Metaphor):
```text
Cinematic European arthouse stop-motion animation film still, rich Kodak 35mm analog film color grading, crystal-clear air, tactile handcrafted surfaces with lived-in timeless patina and sfumato soft edges. Spacious [full-body wide / medium] shot from a [low-angle upward / eye-level] three-quarter view with generous open scenic space on an expansive open-air [bối cảnh mang phép màu ánh sáng/bóng đổ hoặc chạng vạng phố biển] of stylized 1:7.5 figure(s) with warm natural hand-molded matte paper-pulp skin: [Chế độ 1 gọi @Tên_nhân_vật | Chế độ 2 tả trực tiếp nhân vật], with a subtle charcoal-black and saffron-yellow accent on [chi tiết nhỏ], in a carefree unbuttoned bohemian posture [khoảnh khắc thắp sáng đèn lồng/ánh nến hoặc phóng đại bóng đổ ẩn dụ trên bề mặt đá cổ]. Single directional [warm candle and brass lantern glow against cool twilight / low golden sunset light casting giant metaphorical shadows] casting a single coherent shadow direction across a mineral palette of 70% [deep twilight-indigo sky and cobalt sea / warm sunlit stone wall and cerulean sky], 20% [màu kiến trúc và trang phục], and 10% [glowing amber light / crimson accent + charcoal-black and saffron-yellow accents] with 35mm crisp deep environmental focus and clear horizon, no text --ar 16:9
```

### Prompt 3 — Poster Khoảnh Khắc Gắn Kết Đắt Giá (`50mm` Soulful Storyteller Mid-Shot):
```text
Cinematic European arthouse stop-motion animation film still, rich Kodak 35mm analog film color grading, crystal-clear air, tactile handcrafted surfaces with lived-in timeless patina and sfumato soft edges. Intimate medium waist-up shot from an eye-level three-quarter view with an airy uncluttered softly defocused scenic background on an expansive open-air [hiên gỗ/bậc thềm đá cổ nhìn ra vịnh biển hoặc đồi thông] of stylized 1:7.5 figure(s) with warm natural hand-molded matte paper-pulp skin: [Chế độ 1 gọi @Tên_nhân_vật | Chế độ 2 tả trực tiếp nhân vật], with a subtle charcoal-black and saffron-yellow accent on [chi tiết nhỏ], in a relaxed natural asymmetrical posture [cử chỉ gắn kết tình cảm ấm áp nhất cùng đạo cụ trung tâm của câu chuyện]. Single directional [warm amber-gold sunlight / warm brass porch lantern light] casting a single coherent shadow direction across a mineral palette of 70% [deep sapphire ocean / twilight cobalt bay in the background], 20% [weathered timber/stone and woven linen clothing], and 10% [hero prop color + charcoal-black and saffron-yellow accents] with 50mm natural optical depth of field and soft background bokeh, no text --ar 16:9
```

## 4. DESCRIPTION
```text
[2-3 câu kể chuyện]

🎧 Spotify: https://open.spotify.com/artist/4FVU7hNPy3mc5HAm68iSB9
🍎 Apple Music: https://music.apple.com/us/artist/coslient/1895068939

---
LYRICS:
[paste full]
---

Original Music & Visuals by Coslient

#adreamtown #coslient #stopmotion #[bài] #[bài] #[bài]
```

## 5. TAGS (THÊM NGOÀI DEFAULT)
```text
[5-7 cụm theo nội dung bài, cách nhau bằng dấu phẩy]
```

## 6. PINNED COMMENT
```text
[1 câu hỏi gợi ký ức]
```

## 7. SHORTS (DƯỚI 30 GIÂY)
- **Đoạn:** [timestamp]
- **Title Shorts:**
```text
[hook ngắn] #shorts #adreamtown
```

## 8. PLAYLISTS & DISTROKID (TRA CỨU & TICK CHỌN)
> 🔗 **Hướng dẫn logic:**  
> - YouTube Playlists: Xem logic phân bổ tại đầu file [`youtube_playlists.md`](../ref/youtube_playlists.md)  
> - DistroKid Album/EP: Xem logic phân bổ tại đầu file [`distrokid.md`](../ref/distrokid.md)

### YouTube Playlists (Tick chọn khi upload):
```text
[Tên Playlist Mood — tra từ đầu file youtube_playlists.md]
[Tên Playlist Album/EP — khớp DistroKid]
The Universe Hidden Inside the Mind | All Videos
```

### DistroKid Release:
```text
Track Title: [Tên bài]
Artist: Coslient
Album / EP: [Tên Album/EP — tra từ đầu file distrokid.md]
Genre: Singer-Songwriter / Folk
```
````

---

*Một câu chuyện hay trong title đáng giá hơn mọi tag, label, và keyword cộng lại.*
