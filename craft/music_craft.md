# Music craft

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` để thiết kế âm nhạc (`Style prompt`), sáng tác lời bài hát theo đúng Chế độ Kể chuyện đã chọn và xuất ra `2-music.md`, `3-lyrics.txt` cùng cập nhật `ref/lyrics-index.md`. Không chứa quy tắc tạo hình nhân vật (`character.md`), chia cảnh (`storyboard.md`) hay câu lệnh sinh ảnh (`image.txt`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## Nguyên tắc cốt lõi

- **Câu thơ nghiệm sinh 1–2 âm tiết chạm tuổi già (`Poetic Payoff Line`):** Mỗi khổ hát (`Verse`, `Chorus`, `Bridge`) kết tinh ít nhất 1 câu thơ giản dị bằng từ vựng 1 đến 2 âm tiết theo một trong hai cơ chế: nhân hóa để năm tháng, ký ức và tuổi già được dịu dàng nghỉ ngơi, hoặc đảo chiều một cử chỉ nhỏ của con người thành việc mở lối cho thiên nhiên và ánh sáng ùa vào chở che.
- **Nhịp sóng mượt mà ở đoạn chậm (`Wave Cadence 7–8 / 6`):** Đan xen dòng mở ý (`7 đến 8 âm tiết`) với dòng hạ vần (`6 âm tiết`) có khoảng ngân cuối câu và gieo vần toàn phần sát nhau, giúp giọng hát lướt mềm, bắt vần nhanh và giữ nhịp cuốn hút.
- **Vũ đạo đổi giọng & Biến thiên điệp khúc (`Vocal Hand-off & Progressive Chorus`):** Luân phiên màu giọng Nam trầm và Nữ trong trẻo ngay giữa các nửa khổ hát hoặc qua cầu nối `[Pre-Chorus]`, phát triển lời `Chorus` theo dòng chảy thời gian và giao câu kết cuối bài cho giọng trầm lắng đọng sát mic.

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
- Lấy `Acoustic Folk` mộc mạc làm gốc (thuần mộc hoặc kết hợp nhánh âm nhạc hợp bối cảnh `1-idea.md`), tempo `58-86 BPM` có độ nhún và nhịp lôi cuốn dễ phiêu theo (`walking pulse / gentle sway / lilting waltz`).
- Phối nhạc 2 tầng:
  - Tầng nền giữ nhịp: Nhạc cụ dây tỉa/quạt nhẹ, bass mộc ấm và bộ gõ mềm tạo độ trôi cuốn hút giúp hình ảnh chuyển động tự nhiên.
  - Tầng giai điệu: Nhạc cụ mộc hợp bối cảnh `1-idea.md` ngân giai điệu, đối đáp với câu hát và dẫn dắt đoạn nhạc dạo (`Instrumental Solo / Interlude`).
- Giọng hát ấm thu gần mic (`warm close-mic vocal`), chọn cách phối hợp với câu chuyện (hát đơn có bè hòa âm ở điệp khúc, song ca Nam - Nữ đối đáp, hoặc giọng thứ hai bước vào ở nửa sau bài) kèm tiếng ngân (`humming / whistling`); âm sắc gỗ ấm, dịu dải tần cao.
- `Style prompt` (55 đến 85 từ tiếng Anh): Ghép cụm danh từ âm thanh trực quan theo 4 ý: (1) Thể loại, điệu thức, BPM và nhịp cuốn; (2) Nhạc cụ tầng nền giữ nhịp; (3) Nhạc cụ tầng giai điệu và độ mở ở điệp khúc; (4) Màu giọng, cách phối bè và chất âm bản thu ấm. Dự án 2 bài giữ chung chất nhạc mộc và đổi nhẹ BPM hoặc màu giọng giữa hai bài.
- `Exclude` (4 đến 6 thành phần): Ghi các yếu tố điện tử, trống mạnh, kỹ xảo giọng hát hoặc âm tần chói cần loại bỏ, cách nhau bằng dấu phẩy; khi loại bỏ một nhạc cụ ở `Exclude`, ghi rõ nhạc cụ mộc dẫn dắt trong `Style prompt`.

### 2.3. Luật của Lyrics (`2-music.md` & `3-lyrics.txt`)
- **Thẻ điều phối:**
  - Chia cấu trúc bài (`Intro`, `Verse`, `Chorus`, `Interlude / Instrumental Solo`, `Bridge`, `Outro`) và một đoạn lắng nhạc cụ linh hoạt theo câu chuyện, vừa vặn trong một lần sinh nhạc trọn vẹn của Suno.
  - Đầu mỗi đoạn đặt một thẻ `[...]` tiếng Anh ngắn gọn (3 đến 10 từ) ghi rõ tên đoạn, nhạc cụ dẫn dắt, người hát (`Male vocal / Female vocal / Duet`) và độ mạnh nhẹ; đặt tín hiệu kết êm ái ở thẻ cuối bài (`[Outro: ..., gentle fade out]`).
  - Dấu ngoặc đơn `(...)` chỉ dùng cho tiếng ngân (`"Mmm...", "Ooh..."`) hoặc lời hát bè thực sự phát ra tiếng.
- **Cách dùng từ:**
  - Dùng chủ đạo từ vựng tiếng Anh đời thường 1 đến 2 âm tiết, kết hợp rút gọn khẩu ngữ và từ nối câu tự nhiên để ca sĩ hát tròn vành, mềm mại như đang trò chuyện.
  - Luôn neo các từ cảm xúc và thời gian quen thuộc vào đồ vật, bộ phận cơ thể hoặc góc không gian cụ thể kèm giới từ định vị để câu hát vừa chạm cảm xúc vừa giàu hình ảnh thực.
  - Mỗi danh từ ưu tiên đi kèm một tính từ đơn giản (hoặc cặp tính từ chỉ dấu vết thời gian và màu sắc, chất liệu) để câu chữ gọn, thoáng.
  - Tạo chất thơ tự nhiên bằng các động từ chuyển động khoan thai và phép nhân hóa gắn động từ hơi thở, tri giác của con người cho cảnh vật, đồ vật xung quanh.
  - Diễn đạt thời gian và sự vật bằng hình ảnh cùng lượng từ tự nhiên, nhường phần mô tả dây chuyền thao tác tay chân cho `storyboard.md`, và tuân thủ [`ref/banned_lyrics_motifs.md`](file:///Users/hoangkien/Youtube/coslient-free/ref/banned_lyrics_motifs.md), [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md).
- **Nhịp câu & gieo vần:**
  - Giữ độ dài dòng hát gọn đều (`6 đến 8 âm tiết/dòng`, tương ứng `3 nhịp nhấn`) trên toàn bộ các đoạn chậm (`Verse`, `Bridge`) lẫn điệp khúc (`Chorus`), giúp ca sĩ nhả chữ gọn nảy, giữ tốc độ câu hát mượt mà và dễ hát theo ở tempo Folk thư thả.
  - Phối âm liền hơi (`Legato Singability`): Kết nối các từ bằng nguyên âm mở và phụ âm vang mềm (`l, r, m, n, w`), luân phiên nhịp nhấn và nhịp lướt đều đặn giữa các từ để giọng hát trôi mượt qua từng phách nhạc.
  - Gieo vần dày và sát ở mọi khổ hát (`AABB`, `ABAB` hoặc chuỗi vần đan cài toàn phần nơi 100% các dòng trong khổ đều có vần ăn khớp): Đặt các từ vần cách nhau ngắn để tai người nghe bắt được vần liên tục; ưu tiên từ kết câu có âm mở hoặc âm vang êm tai và chủ động đổi mới cặp từ gieo vần qua từng bài.
- **Cách kể chuyện (`Verse` & `Chorus`):**
  - Giữ đúng ngôi kể đã chọn ở `1-idea.md` (**Chế độ 1**: theo tuyến nhân vật xuyên suốt; **Chế độ 2**: các lát cắt đời sống độc lập cùng chụm về điệp khúc).
  - `Verse`: Câu đầu tiên vào thẳng một hành động, lời nói thân tình hoặc khung cảnh cụ thể; phát triển câu chuyện bằng chi tiết đời thực và đan cài 2 đến 3 móc neo giác quan từ `1-idea.md`.
  - `Chorus` & `Hook`: Gom cảm xúc chính của `1-idea.md` theo đúng chất bài hát (lời hẹn ước, nhịp bước chân giữa cảnh vật, cảm giác bình yên nơi thuộc về, hoặc suy ngẫm nhẹ nhõm); đặt câu `Hook` gắn với tên bài, ngắn gọn, bắt tai và vừa một hơi thở ở vị trí đinh của điệp khúc; giữ mạch thời gian và cảm xúc liền lạc đến cuối bài.
- **Định dạng file lời:**
  - `2-music.md`: Giữ đầy đủ thẻ `[...]`, lời bè `(...)` và dấu câu tự nhiên.
  - `3-lyrics.txt`: Chỉ giữ lời hát thành tiếng, ghi đầy đủ toàn văn các điệp khúc lặp lại, viết hoa chữ cái đầu dòng, để trống dấu câu cuối dòng và cách các khổ đúng 1 dòng trống.
