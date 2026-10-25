# SEO & Packaging Review Gate (Cổng kiểm toán Đóng gói & CTR — `6-seo.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `6-seo.md` (trước khi tạo ảnh Thumbnail và xuất bản lên YouTube / DistroKid), dùng để thẩm định khách quan các tiêu chuẩn thực chứng `[FATAL]` và `[HIGH RISK]` giúp tối ưu tỷ lệ nhấp (`CTR`), khả năng ăn đề xuất tự nhiên (`Viral Ratio`) và tỷ lệ tương tác (`Like/View & Comments`) cho khán giả 45–85+.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Phân cấp tiêu chuẩn kiểm toán Đóng gói & SEO WIN (`[FATAL]` & `[HIGH RISK]`)

### 1.1. Năm tiêu chuẩn nền tảng `[FATAL]` (Đạt 100% trước khi tạo Thumbnail và đăng tải)

1. **Kiến trúc Tiêu đề dưới 70 ký tự, Câu chuyện Đứng đầu và Trung thực Nội dung (`Story-First <70-Char Title & Content Integrity`):**
   - Tiêu đề chính và 2 tiêu đề dự phòng nằm gọn trong giới hạn **dưới 70 ký tự**, đặt trọn vẹn mệnh đề cảm xúc câu chuyện hoặc tên bài hát ở phần đầu trước dấu phân cách hậu tố (`| A Dream Town (4K)` hoặc `| Short Folk Film (4K)`), giúp hiển thị trọn vẹn trên cả màn hình TV và thiết bị di động.
   - Mệnh đề tiêu đề vận dụng linh hoạt các khuôn mẫu kích hoạt đồng cảm ở khán giả 45-85+ (`Mệnh đề Chốn về & Cộng đồng An nhiên`, `Mệnh đề Chứng nhân Bền bỉ theo Năm tháng`, `Mệnh đề Thủ thỉ Mở Đa tầng nghĩa`, hoặc `Mệnh đề Đối xứng Chăm sóc và Gắn bó`) và phản ánh trung thực bối cảnh, thời điểm/mùa cùng câu chuyện thực tế trong lời hát và hình ảnh.
   - Định danh file gốc (`[story-clause-slug].mp4` và `[story-clause-slug]-thumbnail.jpg`) đồng bộ trực tiếp với mệnh đề tiêu đề chính.

2. **Bộ 3 Prompt Poster Thumbnail đối lập quy mô và chuẩn Khung 4 khối Stop-Motion (`Three-Angle Iconic Poster Prompts & Stylized Mold Integrity`):**
   - Xuất đầy đủ **3 câu lệnh tiếng Anh 4 khối trực quan hoàn chỉnh** (`--ar 16:9`) đại diện cho 3 góc tiếp cận Poster điện ảnh rõ nét mọc ra từ câu chuyện bài hát:
     1. **Prompt 1 (`Poster Không Gian Thơ Mộng & Câu Chuyện`):** Khung hình rộng hoặc trung-rộng đặt các nhân vật sống và tương tác tự nhiên bên trong không gian đặc trưng nhất của bài hát với khoảng thở thoáng rộng (`expansive scenic focus with generous open negative space`).
     2. **Prompt 2 (`Poster Ánh Sáng & Hành Trình Đồng Hành`):** Khung hình toàn cảnh hoặc rộng khai thác khoảnh khắc đồng hành, làm việc hoặc sẻ chia dưới ánh sáng vàng ấm hoặc chạng vạng giữa không gian mô hình.
     3. **Prompt 3 (`Poster Khoảnh Khắc Gắn Kết Đắt Giá`):** Khung hình bán thân hoặc trung-rộng đặt trước hậu cảnh mờ dịu (`softly blurred warm background`), bắt trọn cử chỉ trao-nhận tình cảm sâu sắc nhất giữa các nhân vật.
   - Cả 3 câu lệnh Thumbnail đều tuân thủ trọn vẹn chuẩn thế giới Stop-Motion tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md) và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5): mở đầu bằng `Handcrafted stop-motion animation film still set in a warm poetic surreal town... harmonious character-to-object scale`, khóa phôi tạo hình thanh mảnh liền khối (`matte paper-pulp skin, soft rounded noses, slender elongated proportions`), tóc sợi bông phủ kín đỉnh đầu, mô tả nhân vật 4 trục tinh gọn phù hợp cỡ cảnh và khóa cuối bằng một nguồn sáng duy nhất.

3. **Mô tả 4 Trụ cột chuẩn Văn phong Con người và Khớp 1:1 Lời bài hát (`Four-Pillar Humanized Description & Verified Lyrics`):**
   - Phần `DESCRIPTION` hội tụ đủ 4 trụ cột theo đúng trật tự:
     1. **Lời mở đầu tâm tình như thư tay (2 đến 3 dòng đầu):** Thủ thỉ chân thành, ấm áp bằng giọng văn tự nhiên của con người (tuân thủ [`humanizer`](../.agents/skills/humanizer/SKILL.md) và [`stop-slop`](../.agents/skills/stop-slop/SKILL.md)), đi thẳng vào cảm xúc đời sống của bài hát.
     2. **Mốc thời gian chính xác (`⏱ CHAPTERS`):** Khớp từng giây với điểm bắt đầu thực tế của từng bản nhạc trong file âm thanh xuất bản, đi kèm đầy đủ liên kết Spotify, Apple Music và Bandcamp của kênh.
     3. **Toàn văn lời bài hát chuẩn xác (`LYRICS`):** Khớp 100% từng từ và từng khổ với bản thu thực tế và `3-lyrics.txt`.
     4. **Tuyên ngôn Nghệ thuật Con người & Bộ 6 Hashtags:** Khẳng định tác phẩm bắt nguồn từ cảm xúc con người và những câu chuyện đời thực của cộng đồng người nghe, khép lại bằng 3 hashtags cố định (`#adreamtown #coslient #stopmotion`) cùng 3 hashtags riêng theo tâm lý, nhạc Folk và không gian bài hát.

4. **Ma trận Từ khóa 3 Tầng Ngữ nghĩa chạm đúng Tệp 55–85+ (`Three-Layer Senior Semantic Tags`):**
   - Ngoài bộ Tags cố định của kênh, mục `TAGS` bổ sung đầy đủ **6 đến 9 cụm từ khóa riêng** phủ kín cả 3 tầng ngữ nghĩa:
     1. **Tầng Tâm lý & Giai đoạn cuộc đời (3 cụm):** Từ khóa đánh trực diện vào tâm thế sống chậm, tình nghĩa vợ chồng lâu năm, tình bạn tri kỷ, sự tưởng niệm/biết ơn và niềm vui tuổi xế chiều của khán giả 55–85+.
     2. **Tầng Thể loại & Nhạc cụ Mộc (2 đến 3 cụm):** Từ khóa gọi đúng nhánh nhạc Folk và các nhạc cụ mộc chủ đạo thực tế vang lên trong bản thu.
     3. **Tầng Mỹ học Thị giác & Không gian (2 đến 3 cụm):** Từ khóa mô tả thế giới hoạt hình thủ công và bối cảnh địa lý trung tâm của câu chuyện.

5. **Đồng bộ Bình luận Ghim mở ký ức, Shorts và Phân phối Playlist / DistroKid / Bandcamp (`Pinned Comment, Shorts & Distribution Sync`):**
   - **Mục `PINNED COMMENT`:** Đặt 1 câu hỏi ấm áp, gần gũi gắn trực tiếp với hạt nhân bài hát để khơi gợi khán giả lớn tuổi kể lại kỷ niệm đời thực của chính họ.
   - **Mục `SHORTS`:** Chọn đúng mốc thời gian `15–30 giây` đắt giá nhất (điệp khúc hoặc điểm chuyển nhạc cụ/khung hình) kèm tiêu đề ngắn gọn.
   - **Mục `PLAYLISTS, DISTROKID & BANDCAMP`:** Tra cứu, cập nhật bài hát mới và điền chính xác 3 Playlists YouTube từ [`ref/youtube_playlists.md`](../ref/youtube_playlists.md), thông tin Album/EP tương ứng trong [`ref/distrokid.md`](../ref/distrokid.md) và thông tin Album kèm `About this track` trong [`ref/bandcamp.md`](../ref/bandcamp.md) (đồng bộ 1:1 `Track Title` với `1-idea.md` và `2-music.md`).

### 1.2. Hai đòn bẩy thực chứng `[HIGH RISK]` (Tối ưu đột phá đề xuất Browse Features và tỷ lệ Bình luận)

1. **Đòn bẩy Móc neo Địa lý & Khoảng trống Tò mò trong Tiêu đề (`Geographic Belonging & Curiosity Gap`):**
   - Kết hợp khéo léo một danh từ chỉ không gian/địa hình gợi ước mơ nghỉ hưu bình yên với một mệnh đề tâm tình bỏ lửng hoặc hành động giàu sức gợi để kích thích đồng thời cả sự đồng cảm nhân khẩu học lẫn trí tò mò thị giác trên trang chủ YouTube.
2. **Đòn bẩy Tâm sự Hậu trường Thủ công trong Mở đầu Description (`Human-Crafted Epistolary Framing`):**
   - Lồng nhẹ vào 2 đến 3 câu mở đầu Description một nét chia sẻ chân thành về quá trình chăm chút giai điệu, nhịp thở và từng khung hình thủ công để tạo thiện cảm sâu sắc và xóa nhòa khoảng cách công nghệ với khán giả lớn tuổi.

---

## 2. Quy trình 3 bước kiểm toán độc lập trên `6-seo.md`

Trước khi tạo ảnh Thumbnail và xuất bản dự án, thực hiện kiểm toán độc lập theo 3 bước:

### Bước 1: Đối chiếu chéo `1-idea.md`, `2-music.md`, `3-lyrics.txt`, `ref/youtube_playlists.md`, `ref/distrokid.md` và `ref/bandcamp.md`
- Đọc đồng thời `6-seo.md` cùng các file gốc của dự án và 3 file danh mục phân phối.
- Xác nhận sự đồng bộ 1:1 của `Track Title`, thời lượng `CHAPTERS`, toàn văn `LYRICS` và việc cập nhật đầy đủ vào tên Playlist / Album DistroKid / Album Bandcamp.

### Bước 2: Thẩm định từng phần theo 5 Cổng `[FATAL]` (`Empirical SEO Stress Test`)
- **Cổng 1 (`FILE NAME` & `TITLE`):** Đếm số ký tự Title (`<70 ký tự`), kiểm tra mệnh đề câu chuyện nằm ở phần đầu tiêu đề, vận dụng khuôn mẫu đồng cảm và khớp trung thực với nội dung bài hát.
- **Cổng 2 (`3 PROMPTS THUMBNAIL`):** Kiểm tra đủ 3 góc độ Poster (`Poetic World & Story`, `Journey`, `Soulful Connection`), đúng cú pháp 4 khối Stop-Motion, phôi tạo hình liền khối thanh mảnh, khoảng thở không gian thoáng rộng và tuân thủ danh mục vật liệu tại [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
- **Cổng 3 (`DESCRIPTION`):** Kiểm tra đủ 4 trụ cột, giọng văn thư tay tự nhiên chuẩn [`humanizer`](../.agents/skills/humanizer/SKILL.md), đủ 3 liên kết nền tảng (`Spotify`, `Apple Music`, `Bandcamp`), lời bài hát khớp 100% và đủ 6 hashtags.
- **Cổng 4 (`TAGS`):** Kiểm tra các cụm từ khóa riêng chia đều vào 3 tầng (Tâm lý 55-85+, Nhạc cụ Folk thực tế, Không gian/Mỹ học).
- **Cổng 5 (`PINNED COMMENT`, `SHORTS` & `PLAYLISTS/DISTROKID/BANDCAMP`):** Kiểm tra câu hỏi mở ký ức, mốc thời gian Shorts (<30s) và việc đồng bộ thông tin phân phối chính xác vào cả `ref/distrokid.md` lẫn `ref/bandcamp.md`.

### Bước 3: Bảng đối soát 5 tiêu chuẩn và Phán quyết (`Pre-Publish SEO Sign-Off`)
Xác nhận `6-seo.md` đạt trọn vẹn 5 tiêu chuẩn trước khi xuất bản:
- **Chỉ số 1 (Chuẩn `Title <70 ký tự` đặt câu chuyện lên đầu & File Name đồng bộ):** Ngắn gọn, hiển thị trọn vẹn, trung thực nội dung và đúng khuôn mẫu tâm lý 45-85+.
- **Chỉ số 2 (Bộ 3 Prompt Poster Thumbnail đối lập quy mô & Chuẩn 4 khối Stop-Motion):** Đủ 3 góc Poster điện ảnh mọc ra từ câu chuyện, phôi tạo hình liền khối tương thích cỡ cảnh và 1 nguồn sáng duy nhất.
- **Chỉ số 3 (Description đủ 4 trụ cột, văn phong thư tay con người & Lyrics khớp 1:1):** Tự nhiên, ấm áp, đúng mốc thời gian, đủ link 3 nền tảng và chuẩn văn phong con người.
- **Chỉ số 4 (Ma trận Tags phủ đủ 3 tầng ngữ nghĩa):** Đủ cả từ khóa tâm lý tuổi già, nhạc cụ mộc và không gian bài hát.
- **Chỉ số 5 (Hoàn chỉnh Pinned Comment, Shorts & Phân phối Playlist/DistroKid/Bandcamp):** Khớp 1:1 và đã cập nhật vào danh mục hệ thống.
