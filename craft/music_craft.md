# Music craft

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` để thiết kế âm nhạc (`Style prompt`), sáng tác lời bài hát theo đúng Chế độ Kể chuyện đã chọn và xuất ra `2-music.md`, `3-lyrics.txt` cùng cập nhật `ref/lyrics-index.md`. Không chứa quy tắc tạo hình nhân vật (`character.md`), chia cảnh (`storyboard.md`) hay câu lệnh sinh ảnh (`image.txt`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## Nguyên tắc cốt lõi

- **Kể chuyện đời thường gần gũi, đọng chất thơ ở câu chốt:** Phần lớn lời hát kể lại những hành động, đồ vật và cuộc trò chuyện quen thuộc hàng ngày bằng ngôn ngữ tự nhiên như lời nói thật; chất thơ chỉ điểm nhẹ ở câu kết khổ hoặc điệp khúc bằng từ ngữ giản dị (1 đến 2 âm tiết) đúc rút tình người từ chính chi tiết vừa kể.
- **Nhịp câu song hành mượt mà và vần tự nhiên:** Giữ dòng hát gọn vừa một hơi thở tự nhiên (`6 đến 10 âm tiết` trọn vẹn một ý nghĩa hoặc chia hai vế cân xứng qua dấu phẩy), tạo đà lướt bằng cấu trúc câu song hành và tự do chọn sơ đồ vần hợp mạch cảm xúc (`AABB`, `ABCB` thả tự do dòng lẻ, `ABAB`, vần bán âm hoặc điệp cấu trúc).
- **Phối giọng linh hoạt và điểm lắng cuối bài:** Điều phối màu giọng đơn ca hoặc song ca Nam trầm và Nữ trong trẻo đối đáp theo mạch truyện, phát triển cảm xúc điệp khúc qua các chặng của bài và tạo khoảng lắng rút nhạc cụ về mộc ở cuối bài để giọng hát thủ thỉ sát mic hoặc ngân vang dư âm.
- **Đồng bộ Hình và Âm độc bản:** Chuyển hóa nhịp chuyển động và âm thanh đặc trưng của bối cảnh trung tâm thành âm sắc nhạc cụ định danh trong bản phối kèm câu ngân giai điệu dễ nhớ, ăn khớp trực tiếp với các từ gợi âm thanh trong lời hát.

## 1. Cấu trúc Input & Output

- **Input:** `1-idea.md`, `ref/lyrics-index.md`, `ref/banned_lyrics_motifs.md`.
- **Output:**
  - `projects/XXX/2-music.md`: Gồm tên bài, `Style prompt`, `Exclude` và `Lyrics` kèm thẻ điều phối (mặc định 1 bài đơn, hoặc 2 bài liên kết khi làm dự án đa bài).
  - `3-lyrics.txt` (hoặc `track-N-<track-title-slug>/3-lyrics.txt` với dự án đa bài): Bản lời sạch chuẩn DistroKid.
  - `ref/lyrics-index.md`: Cập nhật bài hát mới, giữ câu `Hook` và hình ảnh trung tâm độc bản trong kho nhạc.

## 2. Luật của Nhạc

### 2.1. Luật của tên bài nhạc (`Track Title`)
- Đặt tên tiếng Anh ngắn gọn (3 đến 6 từ) bằng từ vựng đời thường giản dị, giàu chất Folk và gợi ngay bối cảnh hoặc tâm tình của `1-idea.md`.
- Đồng bộ 1:1 tên bài giữa `1-idea.md`, tiêu đề `## Track N: [Track Title]` trong `2-music.md`, tên thư mục `track-N-<track-title-slug>/` và bảng `ref/lyrics-index.md`.

### 2.2. Luật của Style nhạc (`Style prompt` & `Exclude`)
- Lấy `Acoustic Folk` mộc mạc làm gốc (thuần mộc hoặc kết hợp nhánh âm nhạc thính phòng hợp bối cảnh `1-idea.md`), thiết kế nhịp 2 tốc độ (`112-124 BPM with a half-time vocal feel` khi cần nhịp nền linh hoạt nâng đỡ giọng hát ngân chậm ở mức `~56-62 BPM`, hoặc `58-76 BPM` cho bản ballad tĩnh lặng).
- Phối nhạc 2 tầng tách bạch tốc độ và độ ngân (`Two-Speed Layering`):
  - Tầng nền giữ nhịp linh hoạt ở dưới: Đàn guitar tỉa dây liên tục (`continuous nimble fingerpicked guitar`), bass gỗ bước đều và bộ gõ chổi quét kết hợp shaker giữ nhịp chảy tự nhiên xuyên suốt bên dưới.
  - Tầng giai điệu và giọng hát ngân chậm ở trên: Đàn dây kéo vĩ liền hơi (`sustained legato cello, lyrical fiddle`), nhạc cụ định danh bối cảnh và giọng hát trôi chậm rãi theo nhịp half-time mềm mại phía trên tầng nền, đối đáp với câu hát và dẫn dắt đoạn nhạc dạo (`Instrumental Solo / Interlude`).
- Giọng hát ấm thu gần mic với lối nhả chữ liền hơi chậm rãi (`soft half-time legato flow`), chọn cách phối hợp với câu chuyện (hát đơn có bè hòa âm ở điệp khúc, song ca Nam và Nữ đối đáp, hoặc giọng thứ hai bước vào ở nửa sau bài) kèm tiếng ngân giai điệu; âm sắc gỗ ấm, dịu dải tần cao.
- `Style prompt` (55 đến 85 từ tiếng Anh): Ghép cụm danh từ âm thanh trực quan theo 4 ý: (1) Thể loại, điệu thức, BPM và nhịp cuốn; (2) Nhạc cụ tầng nền giữ nhịp; (3) Nhạc cụ tầng giai điệu và độ mở ở điệp khúc; (4) Màu giọng, cách phối bè và chất âm bản thu ấm. Dự án 2 bài giữ chung chất nhạc mộc và đổi nhẹ BPM hoặc màu giọng giữa hai bài.
- `Exclude` (4 đến 6 thành phần): Ghi các yếu tố điện tử, trống mạnh, kỹ xảo giọng hát hoặc âm tần chói cần loại bỏ, cách nhau bằng dấu phẩy; khi loại bỏ một nhạc cụ ở `Exclude`, ghi rõ nhạc cụ mộc dẫn dắt trong `Style prompt`.

### 2.3. Luật của Lyrics (`2-music.md` & `3-lyrics.txt`)
- **Thẻ điều phối:**
  - Chia cấu trúc bài cân đối theo mạch chuyện (`Intro`, `Verse`, `Chorus`, `Instrumental Solo / Interlude`, `Bridge`, `Outro`) cùng một đoạn lắng nhạc cụ tự nhiên, vừa vặn trong một lần sinh nhạc trọn vẹn của Suno.
  - Đầu mỗi đoạn đặt một thẻ `[...]` tiếng Anh ngắn gọn (3 đến 10 từ) ghi rõ tên đoạn, nhạc cụ dẫn dắt, người hát (`Male vocal / Female vocal / Duet`) và độ mạnh nhẹ; đặt tín hiệu kết êm ái ở thẻ cuối bài (`[Outro: ..., gentle fade out]`).
  - Dấu ngoặc đơn `(...)` chỉ dùng cho tiếng ngân không lời hoặc lời hát bè thực sự phát ra tiếng.
- **Cách dùng từ:**
  - Dùng chủ đạo từ vựng tiếng Anh đời thường 1 đến 2 âm tiết, kết hợp rút gọn khẩu ngữ và từ nối câu tự nhiên để ca sĩ hát tròn vành, mềm mại như đang trò chuyện.
  - Luôn neo các từ cảm xúc và thời gian quen thuộc vào đồ vật, bộ phận cơ thể hoặc góc không gian cụ thể kèm giới từ định vị để câu hát vừa chạm cảm xúc vừa giàu hình ảnh thực.
  - Mỗi danh từ ưu tiên đi kèm một tính từ đơn giản (hoặc cặp tính từ chỉ dấu vết thời gian và màu sắc, chất liệu) để câu chữ gọn, thoáng.
  - Tạo chất thơ tự nhiên ở các điểm lắng bằng động từ chuyển động khoan thai hoặc phép nhân hóa giản dị gắn với cảnh vật, đồ vật xung quanh.
  - Diễn đạt thời gian và sự vật bằng hình ảnh cùng lượng từ tự nhiên, nhường phần mô tả dây chuyền thao tác tay chân cho `storyboard.md`, và tuân thủ [`ref/banned_lyrics_motifs.md`](file:///Users/hoangkien/Youtube/coslient-free/ref/banned_lyrics_motifs.md), [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md).
- **Nhịp câu & gieo vần:**
  - Giữ dòng hát vừa một hơi thở tự nhiên (`6 đến 10 âm tiết/dòng`, tương ứng `3 đến 4 nhịp nhấn`), mỗi dòng khép trọn một cụm mệnh đề hoặc chia hai vế cân xứng qua dấu phẩy để ca sĩ nhả chữ trôi chảy, mượt mà ở cả đoạn chậm lẫn điệp khúc.
  - Kết nối các từ bằng nguyên âm mở cùng phụ âm vang mềm, sử dụng phép lặp từ đầu câu hoặc cấu trúc ngữ pháp song hành giữa các cặp câu để giai điệu tự bắt nhịp cuốn hút.
  - Linh hoạt chọn sơ đồ vần hợp mạch tự sự (`AABB` liền kề, `ABCB` thả tự do dòng lẻ, `ABAB`, vần bán âm hoặc điệp cấu trúc): Ưu tiên từ kết câu có âm mở hoặc âm vang êm tai và chủ động đổi mới cặp từ gieo vần qua từng bài.
- **Cách kể chuyện (`Verse` & `Chorus`):**
  - Giữ đúng ngôi kể đã chọn ở `1-idea.md` (**Chế độ 1**: theo tuyến nhân vật xuyên suốt; **Chế độ 2**: các lát cắt đời sống độc lập cùng chụm về điệp khúc).
  - `Verse`: Câu đầu tiên vào thẳng một hành động, lời nói thân tình hoặc khung cảnh cụ thể; phát triển câu chuyện bằng chi tiết sinh hoạt đời thường gần gũi và đan cài 2 đến 3 móc neo giác quan từ `1-idea.md`.
  - `Chorus` & `Hook`: Gom cảm xúc chính của `1-idea.md` một cách tự nhiên; đặt câu `Hook` gắn với tên bài, ngắn gọn, bắt tai và vừa một hơi thở ở vị trí đinh của điệp khúc; giữ mạch thời gian và cảm xúc liền lạc đến cuối bài.
- **Định dạng file lời:**
  - `2-music.md`: Giữ đầy đủ thẻ `[...]`, lời bè `(...)` và dấu câu tự nhiên.
  - `3-lyrics.txt`: Chỉ giữ lời hát thành tiếng, ghi đầy đủ toàn văn các điệp khúc lặp lại, viết hoa chữ cái đầu dòng, để trống dấu câu cuối dòng và cách các khổ đúng 1 dòng trống.
