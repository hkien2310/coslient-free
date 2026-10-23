# Music craft

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` để thiết kế âm nhạc (`Style prompt`), sáng tác lời bài hát theo đúng Chế độ Kể chuyện đã chọn và xuất ra `2-music.md`, `3-lyrics.txt` cùng cập nhật `ref/lyrics-index.md`. Không chứa quy tắc tạo hình nhân vật (`character.md`), chia cảnh (`storyboard.md`) hay câu lệnh sinh ảnh (`image.txt`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## 1. Đầu vào, Đầu ra & Định danh

- **Input:** `1-idea.md`, `ref/lyrics-index.md`, `ref/banned_lyrics_motifs.md`, `ref/doi-thu/RANKING.md`, `ref-real-music/index.md` (tùy chọn).
- **Output:**
  1. `projects/XXX/2-music.md`: Gồm tên bài, `Style prompt`, `Exclude` và `Lyrics` kèm thẻ điều phối (mặc định 1 bài độc lập, hoặc 2 bài liên kết khi làm dự án đa bài).
  2. `3-lyrics.txt` (hoặc `track-N-<track-title-slug>/3-lyrics.txt` với dự án đa bài): Bản lời sạch chuẩn DistroKid, chỉ giữ lời hát thành tiếng, viết hoa chữ cái đầu dòng, để trống dấu câu cuối dòng và cách các khổ đúng 1 dòng trống.
  3. `ref/lyrics-index.md`: Cập nhật bài hát mới, giữ câu chủ đề (`Hook`) và hình ảnh trung tâm độc bản trong kho nhạc.
- **Tên bài hát (`Track Title`):** Đặt tên tiếng Anh ngắn gọn (3 đến 6 từ) bằng từ vựng đời sống giản dị, giàu chất Folk và gợi ra bối cảnh hoặc lời tâm tình của `1-idea.md`. Đồng bộ 1:1 tên bài giữa `1-idea.md`, tiêu đề `## Track N: [Track Title]` trong `2-music.md`, thư mục `track-N-<track-title-slug>/` và bảng `ref/lyrics-index.md`.

## 2. Thiết kế Âm nhạc cho Suno (`Style prompt` & `Exclude`)

- **Nền nhạc mộc & Nhịp hai tầng:** Lấy Acoustic Folk mộc mạc (thuần mộc hoặc pha trộn tự nhiên với nhánh âm nhạc hợp bối cảnh `1-idea.md`) làm gốc, tempo thư thả quanh `58-86 BPM`. Phối theo cấu trúc nhịp hai tầng: lớp đệm dưới giữ nhịp chuyển động đều đặn giúp khung hình có sức sống, lớp giai điệu và giọng hát phía trên ngân thong thả, nhiều khoảng nghỉ. Bản thu ưu tiên chất gỗ ấm, giọng hát thu gần mic đặt ở giữa như hát trong phòng nhỏ, bộ gõ nhẹ và dải tần cao dịu mượt để nghe lâu vẫn êm tai.
- **Biến đổi màu âm qua các đoạn:**
  - Chọn cách phối giọng hợp nhất với câu chuyện ở `1-idea.md`, có thể là nam trầm ấm và nữ trong trẻo hát đối đáp, giọng thứ hai bước vào ở nửa sau bài, hoặc một giọng kể chuyện đi cùng bè hòa âm và tiếng ngân (`humming / whistling`).
  - Chọn nhạc cụ mộc gắn với không gian văn hóa của `1-idea.md` để vừa đệm, vừa đối đáp với giọng hát và dẫn dắt đoạn nghỉ khí nhạc (`Instrumental Solo / Interlude`). Các đoạn trong bài có độ mở năng lượng khác nhau và có một đoạn lắng mộc mạc để tôn lời hát.
- **Quy cách `Style prompt` & `Exclude`:**
  - `Style prompt` (khoảng 55 đến 85 từ tiếng Anh): Dùng các cụm danh từ mô tả âm thanh trực quan mà Suno bắt tốt nhất. Câu đầu tiên nêu rõ nhánh Folk, điệu thức, BPM, màu giọng/cách phối giọng và nhạc cụ chính. Dự án có 2 bài thì giữ chung chất âm mộc và đổi nhẹ nhịp độ hoặc màu giọng giữa hai bài.
  - `Exclude` (4 đến 6 thành phần): Ghi các yếu tố điện tử, trống mạnh, kỹ xảo giọng hát hoặc âm tần chói cần loại bỏ, cách nhau bằng dấu phẩy. Khi loại bỏ một nhạc cụ ở `Exclude`, hãy ghi rõ nhạc cụ mộc dẫn dắt trong `Style prompt`.

## 3. Sáng tác Ca từ & Thẻ điều phối (`Lyrics`)

- **Cấu trúc mở & Thẻ `[...]` cho Suno:**
  - Chia cấu trúc bài hát, độ dài các khổ (`Verse`) và các đoạn nhạc dạo (`Intro`, `Interlude`, `Instrumental Solo`, `Outro`) linh hoạt theo độ dài câu chuyện và hơi thở tự nhiên của bản nhạc.
  - Đầu mỗi phân đoạn đặt một thẻ ngoặc vuông `[...]` tiếng Anh ngắn gọn (3 đến 10 từ) ghi rõ tên đoạn, nhạc cụ dẫn dắt, người hát (`Male vocal / Female vocal / Duet`) và độ mạnh nhẹ để Suno đổi màu âm.
  - Dấu ngoặc đơn `(...)` chỉ dùng cho tiếng ngân (`"Mmm...", "Ooh..."`) hoặc lời hát bè thực sự phát ra tiếng.
- **Mạch kể chuyện ở `Verse` & Điểm rơi cảm xúc ở `Chorus`:**
  - Giữ đúng ngôi kể đã chọn ở `1-idea.md` (**Chế độ 1**: tự sự hoặc đối thoại theo tuyến nhân vật xuyên suốt; **Chế độ 2**: các lát cắt đời sống độc lập cùng chụm về ý niệm trung tâm ở điệp khúc).
  - **Khổ hát (`Verse`):** Câu đầu tiên vào thẳng một hành động, lời nói thân tình hoặc khung cảnh cụ thể. Kể chuyện bằng chi tiết đời thực và đan cài tự nhiên 2 đến 3 móc neo giác quan từ `1-idea.md`.
  - **Điệp khúc (`Chorus`) & Câu `Hook`:** Gom cảm xúc chính của `1-idea.md` lại theo đúng chất của bài hát (một lời hẹn ước bình dị, một nhịp bước chân giữa cảnh vật, cảm giác bình yên nơi thuộc về, hoặc một suy ngẫm nhẹ nhõm). Đặt câu `Hook` ngắn gọn, dễ hát và vừa một hơi thở ở vị trí đinh của điệp khúc để người nghe dễ thuộc ngay lần đầu; giữ mạch thời gian và cảm xúc liền lạc đến cuối bài.
- **Nhịp thở câu hát, Vần & Văn phong:**
  - Viết câu chữ giản dị như lời nói chuyện ngoài đời, vừa một hơi thở hát (khoảng 3 đến 4 nhịp nhấn mỗi dòng), đan xen tự nhiên giữa câu dài kể chuyện và câu ngắn nghỉ hơi. Gieo vần thuận theo nghĩa câu chữ và chủ động đổi cặp từ gieo vần qua từng bài.
  - Lời bài hát giữ phần tâm tình và cảm xúc; phần mô tả hoạt cảnh và động tác cụ thể để dành cho `storyboard.md`.
  - Tuân thủ [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md) và [`ref/banned_lyrics_motifs.md`](file:///Users/hoangkien/Youtube/coslient-free/ref/banned_lyrics_motifs.md). Giữ dấu câu tự nhiên trong `2-music.md` và viết mọi con số thành chữ tiếng Anh.
