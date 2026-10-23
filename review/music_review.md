# Music & Lyrics Review Gate (Cổng kiểm toán Bài hát Chiến thắng — `2-music.md` & `3-lyrics.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `2-music.md` và `3-lyrics.txt` (trước khi tạo file âm thanh và chuyển sang Bước 3 `character.md` / `storyboard.md`), dùng để thẩm định khách quan các tiêu chuẩn thực chứng `[FATAL]` và `[HIGH RISK]` giúp biến bản thảo nhạc thành **Bài hát WIN** (nằm trọn trong vùng ngọt âm học của khán giả 45–85+, có vũ đạo giọng hát đối thoại, nhịp thở ca từ thư thả, câu Hook dễ thuộc và cú nâng cấp cảm xúc ở cuối bài).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Cấu trúc Kiểm toán Bài hát WIN (`[FATAL]` & `[HIGH RISK]` - Đúc kết từ [`ref/doi-thu/RANKING.md`](../ref/doi-thu/RANKING.md) & [`ref-real-music/index.md`](../ref-real-music/index.md))

### 1.1. Kiểm toán theo 3 khối Luật của Nhạc (`[FATAL]` - Đạt 100% trước khi tạo nhạc)

- **Kiểm toán Tên bài nhạc (`Track Title` - Mục 2.1):**
  - Đặt tên tiếng Anh ngắn gọn (3 đến 6 từ) bằng từ vựng đời thường giản dị, giàu chất Folk và gợi ngay bối cảnh hoặc tâm tình của `1-idea.md`.
  - Đồng bộ 1:1 tên bài giữa `1-idea.md`, tiêu đề trong `2-music.md`, tên thư mục dự án và bảng [`ref/lyrics-index.md`](../ref/lyrics-index.md).
- **Kiểm toán Style nhạc (`Style prompt` & `Exclude` - Mục 2.2):**
  - **Thể loại & Nhịp độ:** Lấy `Acoustic Folk` làm gốc (thuần mộc hoặc kết hợp nhánh âm nhạc hợp bối cảnh `1-idea.md`), tempo thư thả quanh `58-86 BPM`.
  - **Cấu trúc nhạc 2 tầng:** Có tầng nền giữ nhịp trôi đều đặn (guitar tỉa/quạt nhẹ, upright bass, bộ gõ mềm) và tầng giai điệu/nhạc cụ mộc kể chuyện hợp bối cảnh `1-idea.md`.
  - **Giọng hát & Không gian bản thu:** Giọng hát ấm thu gần mic, phối giọng hợp câu chuyện kết hợp tiếng ngân (`humming / whistling`); âm sắc gỗ ấm, dịu mượt dải tần cao.
  - **Cấu trúc `Style prompt` (khoảng 55 đến 85 từ) & `Exclude` (4 đến 6 thành phần):** Ghép cụm danh từ âm thanh trực quan đủ 4 ý (thể loại/tông/BPM, nhạc cụ tầng nền, nhạc cụ tầng giai điệu, màu giọng/bản thu ấm); khi loại bỏ một nhạc cụ ở `Exclude`, đã ghi rõ nhạc cụ mộc dẫn dắt trong `Style prompt`.
- **Kiểm toán Lyrics (`2-music.md` & `3-lyrics.txt` - Mục 2.3):**
  - **Cách dùng thẻ điều phối:** Có đủ các đoạn (bao gồm `[Instrumental Solo / Interlude]` và đoạn lắng nhạc cụ); đầu mỗi đoạn có thẻ `[...]` gọn (3 đến 10 từ) ghi rõ tên đoạn, nhạc cụ dẫn dắt, người hát (`Male vocal / Female vocal / Duet`) và độ mạnh nhẹ; dấu ngoặc đơn `(...)` chỉ chứa tiếng ngân hoặc lời bè hát thành tiếng.
  - **Cách dùng từ:** Từ vựng tiếng Anh đời thường mộc mạc; mọi con số viết bằng chữ tiếng Anh; tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md), [`humanizer`](../.agents/skills/humanizer/SKILL.md) và [`stop-slop`](../.agents/skills/stop-slop/SKILL.md).
  - **Cách gieo vần & nhịp câu:** Mỗi dòng vừa gọn một hơi thở hát (khoảng 3 đến 4 nhịp nhấn), đan xen câu dài và câu ngắn; gieo vần thuận theo nghĩa và đổi mới cặp vần so với các bài liền kề.
  - **Cách kể chuyện (`Verse` & `Chorus`):** Giữ đúng ngôi kể đã chọn ở `1-idea.md`; câu đầu `Verse 1` vào thẳng hành động, lời nói thân tình hoặc khung cảnh cụ thể; đan cài đủ 2 đến 3 móc neo giác quan từ `1-idea.md`; `Chorus` gom cảm xúc chính tự nhiên và đặt câu `Hook` ngắn gọn vừa một hơi thở ở vị trí đinh (độc bản trong [`ref/lyrics-index.md`](../ref/lyrics-index.md)); giữ mạch thời gian và cảm xúc liền lạc đến cuối bài.
  - **Định dạng file lời:** `3-lyrics.txt` khớp 1:1 từng dòng lời có chữ với `2-music.md`, viết hoa chữ cái đầu dòng, để trống dấu câu cuối dòng và cách các khổ đúng 1 dòng trống.

### 1.2. Ba đòn bẩy thực chứng `[HIGH RISK]` (Chọn đòn bẩy phù hợp với từng bài từ [`ref/doi-thu/RANKING.md`](../ref/doi-thu/RANKING.md))

- **Phối giọng đối đáp hoặc giọng thứ hai bước vào sau:** Nam trầm ấm và nữ trong trẻo hát đối đáp theo khổ hoặc cặp câu, hoặc một giọng hát nửa đầu rồi giọng thứ hai bước vào ở nửa sau bài.
- **Tiếng ngân con người và nhạc cụ gợi bối cảnh:** Điểm tiếng ngân (`"Mmm...", "Ooh..."`, `whistling`) cùng nhạc cụ mộc gợi không gian văn hóa của bài ở `Intro`, đoạn nối và `Outro`.
- **Câu hát đinh giàu sức gợi và nâng cấp điệp khúc cuối:** Có cặp câu hát đinh giàu sức gợi từ chi tiết đời thường, kết hợp nâng nhẹ màu âm hoặc cách nhả chữ ở `[Final Chorus]`.

---

## 2. Quy trình 3 bước kiểm toán trên `2-music.md` và `3-lyrics.txt`

- **Bước 1 (Đối chiếu Input/Output):** Đọc `1-idea.md`, `2-music.md`, `3-lyrics.txt`, [`ref/lyrics-index.md`](../ref/lyrics-index.md) và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) để kiểm tra đồng bộ tên bài, chế độ kể chuyện, 2 đến 3 móc neo giác quan và tính độc bản của câu `Hook`.
- **Bước 2 (Thẩm định theo 3 khối Luật của Nhạc & Đòn bẩy WIN):** Kiểm tra lần lượt Tên bài nhạc (Mục 2.1), Style nhạc (Mục 2.2), Lyrics (Mục 2.3) và các đòn bẩy `[HIGH RISK]` phù hợp với bài.
- **Bước 3 (Phán quyết `Pre-Audio Music Sign-Off`):** Chỉ cấp `PASS` và cập nhật [`ref/lyrics-index.md`](../ref/lyrics-index.md) khi cả 3 khối Luật của Nhạc (`2.1 Tên bài`, `2.2 Style nhạc`, `2.3 Lyrics`) đạt `100%`.
