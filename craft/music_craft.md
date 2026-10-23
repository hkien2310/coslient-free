# Music craft

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` để thiết kế âm nhạc (`Style prompt`), sáng tác lời bài hát theo đúng Chế độ Kể chuyện đã chọn và xuất ra `2-music.md`, `3-lyrics.txt` cùng cập nhật `ref/lyrics-index.md`. Không chứa quy tắc tạo hình nhân vật (`character.md`), chia cảnh (`storyboard.md`) hay câu lệnh sinh ảnh (`image.txt`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## 1. Cấu trúc Input & Output

- **Input:** `1-idea.md`, `ref/lyrics-index.md`, `ref/banned_lyrics_motifs.md`, `ref/doi-thu/RANKING.md`, `ref-real-music/index.md` (tùy chọn).
- **Output:**
  - `projects/XXX/2-music.md`: Gồm tên bài, `Style prompt`, `Exclude` và `Lyrics` kèm thẻ điều phối (mặc định 1 bài đơn, hoặc 2 bài liên kết khi làm dự án đa bài).
  - `3-lyrics.txt` (hoặc `track-N-<track-title-slug>/3-lyrics.txt` với dự án đa bài): Bản lời sạch chuẩn DistroKid.
  - `ref/lyrics-index.md`: Cập nhật bài hát mới, giữ câu `Hook` và hình ảnh trung tâm độc bản trong kho nhạc.

## 2. Luật của Nhạc

### 2.1. Luật của tên bài nhạc (`Track Title`)
- Đặt tên tiếng Anh ngắn gọn (3 đến 6 từ) bằng từ vựng đời thường giản dị, giàu chất Folk và gợi ngay bối cảnh hoặc tâm tình của `1-idea.md`.
- Đồng bộ 1:1 tên bài giữa `1-idea.md`, tiêu đề `## Track N: [Track Title]` trong `2-music.md`, tên thư mục `track-N-<track-title-slug>/` và bảng `ref/lyrics-index.md`.

### 2.2. Luật của Style nhạc (`Style prompt` & `Exclude`)
- **Thể loại & Nhịp độ:** Lấy `Acoustic Folk` mộc mạc làm gốc (thuần mộc hoặc kết hợp một nhánh âm nhạc hợp với bối cảnh và văn hóa của `1-idea.md`), tempo thư thả quanh `58-86 BPM`.
- **Cấu trúc nhạc 2 tầng:**
  - **Tầng nền giữ nhịp:** Dùng nhạc cụ dây tỉa/quạt nhẹ, tiếng bass mộc trầm ấm và bộ gõ mềm giữ nhịp trôi đều đặn giúp hình ảnh chuyển động tự nhiên.
  - **Tầng giai điệu & nhạc cụ kể chuyện:** Chọn nhạc cụ mộc đặc trưng của bối cảnh `1-idea.md` để ngân giai điệu, đối đáp với câu hát và dẫn dắt đoạn nhạc dạo (`Instrumental Solo / Interlude`).
- **Giọng hát & Không gian bản thu:** Giọng hát ấm thu gần mic (`warm close-mic vocal`), chọn cách phối hợp với câu chuyện (hát đơn có bè hòa âm ở điệp khúc, song ca Nam - Nữ đối đáp, hoặc giọng thứ hai bước vào ở nửa sau bài) kết hợp tiếng ngân (`humming / whistling`); âm sắc gỗ ấm, dịu mượt dải tần cao.
- **Cấu trúc viết `Style prompt` (khoảng 55 đến 85 từ tiếng Anh):** Ghép các cụm danh từ âm thanh trực quan theo 4 ý: (1) Thể loại, điệu thức, BPM và nhịp cảm nhận; (2) Nhạc cụ tầng nền giữ nhịp; (3) Nhạc cụ tầng giai điệu và cách mở năng lượng ở điệp khúc; (4) Màu giọng, cách phối bè và chất âm bản thu ấm. Dự án 2 bài giữ chung không gian nhạc mộc và đổi nhẹ BPM hoặc màu giọng giữa hai bài.
- **Cấu trúc viết `Exclude` (4 đến 6 thành phần):** Ghi các yếu tố điện tử, trống mạnh, kỹ xảo giọng hát hoặc âm tần chói cần loại bỏ, cách nhau bằng dấu phẩy; khi loại bỏ một nhạc cụ ở `Exclude`, ghi rõ nhạc cụ mộc dẫn dắt trong `Style prompt`.

### 2.3. Luật của Lyrics (`2-music.md` & `3-lyrics.txt`)
- **Cách dùng thẻ điều phối:**
  - Chia cấu trúc bài (`Intro`, `Verse`, `Chorus`, `Interlude / Instrumental Solo`, `Bridge`, `Outro`) và một đoạn lắng nhạc cụ linh hoạt theo câu chuyện.
  - Đầu mỗi đoạn đặt một thẻ ngoặc vuông `[...]` tiếng Anh ngắn gọn (3 đến 10 từ) ghi rõ tên đoạn, nhạc cụ dẫn dắt, người hát (`Male vocal / Female vocal / Duet`) và độ mạnh nhẹ.
  - Dấu ngoặc đơn `(...)` chỉ dùng cho tiếng ngân (`"Mmm...", "Ooh..."`) hoặc lời hát bè thực sự phát ra tiếng.
- **Cách dùng từ:**
  - Dùng từ vựng tiếng Anh đời thường, mộc mạc như lời trò chuyện trực tiếp.
  - Mọi con số viết bằng chữ tiếng Anh chuẩn.
  - Lời bài hát giữ phần tâm tình và cảm xúc; phần mô tả hoạt cảnh và thao tác vật lý cụ thể để dành cho `storyboard.md`.
  - Tuân thủ [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md) và [`ref/banned_lyrics_motifs.md`](file:///Users/hoangkien/Youtube/coslient-free/ref/banned_lyrics_motifs.md).
- **Cách gieo vần & nhịp câu:**
  - Mỗi dòng vừa gọn một hơi thở hát (khoảng 3 đến 4 nhịp nhấn tự nhiên), đan xen câu dài kể chuyện và câu ngắn nghỉ hơi.
  - Gieo vần tự nhiên thuận theo nghĩa câu chữ và chủ động đổi mới cặp từ gieo vần qua từng bài.
- **Cách kể chuyện (`Verse` & `Chorus`):**
  - Giữ đúng ngôi kể đã chọn ở `1-idea.md` (**Chế độ 1**: theo tuyến nhân vật xuyên suốt; **Chế độ 2**: các lát cắt đời sống độc lập cùng chụm về điệp khúc).
  - **Khổ hát (`Verse`):** Câu đầu tiên vào thẳng một hành động, lời nói thân tình hoặc khung cảnh cụ thể; phát triển câu chuyện bằng chi tiết đời thực và đan cài 2 đến 3 móc neo giác quan từ `1-idea.md`.
  - **Điệp khúc (`Chorus`) & Câu `Hook`:** Gom cảm xúc chính của `1-idea.md` theo đúng chất của bài hát (lời hẹn ước bình dị, nhịp bước chân giữa cảnh vật, cảm giác bình yên nơi thuộc về, hoặc suy ngẫm nhẹ nhõm); đặt câu `Hook` ngắn gọn, dễ hát và vừa một hơi thở ở vị trí đinh của điệp khúc; giữ mạch thời gian và cảm xúc liền lạc đến cuối bài.
- **Định dạng file lời:**
  - Trong `2-music.md`: Giữ đầy đủ thẻ `[...]`, lời bè `(...)` và dấu câu tự nhiên.
  - Trong `3-lyrics.txt`: Chỉ giữ lời hát thành tiếng, viết hoa chữ cái đầu dòng, để trống dấu câu cuối dòng và cách các khổ đúng 1 dòng trống.
