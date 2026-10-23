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

1. **Kiểm toán Tên bài nhạc (`Track Title` - Mục 2.1):**
   - Đặt tên tiếng Anh ngắn gọn (3 đến 6 từ) bằng từ vựng đời sống giản dị, giàu chất Folk và gợi ra bối cảnh hoặc lời tâm tình của `1-idea.md`.
   - Đồng bộ 1:1 tên bài giữa `1-idea.md`, tiêu đề trong `2-music.md`, thư mục dự án và bảng [`ref/lyrics-index.md`](../ref/lyrics-index.md).

2. **Kiểm toán Style nhạc (`Style prompt` & `Exclude` - Mục 2.2):**
   - **Nền nhạc, Nhịp hai tầng & Màu âm:** Dùng cụm danh từ mô tả âm thanh trực quan (khoảng 55 đến 85 từ tiếng Anh). Câu đầu nêu rõ nhánh Folk, điệu thức ấm, tempo quanh `58-86 BPM` với nhịp hai tầng (lớp đệm dưới giữ nhịp chuyển động đều đặn, lớp giai điệu và giọng hát phía trên ngân thong thả), màu giọng/cách phối giọng và nhạc cụ mộc hợp bối cảnh `1-idea.md`; bản thu chất gỗ ấm gần mic, bộ gõ nhẹ và dải tần cao dịu mượt.
   - **`Exclude` (4 đến 6 thành phần):** Ghi các yếu tố điện tử, trống mạnh, kỹ xảo giọng hát hoặc âm tần chói cần loại bỏ; khi loại bỏ một nhạc cụ ở `Exclude`, đã ghi rõ nhạc cụ mộc dẫn dắt trong `Style prompt`.

3. **Kiểm toán Lyrics (`2-music.md` & `3-lyrics.txt` - Mục 2.3):**
   - **Cấu trúc & Thẻ điều phối `[...]`:** Cấu trúc bài, độ dài các khổ, các đoạn nhạc dạo (`[Instrumental Solo / Interlude]`) và đoạn lắng mộc mạc đi theo câu chuyện. Đầu mỗi đoạn có thẻ `[...]` gọn (3 đến 10 từ) ghi rõ tên đoạn, nhạc cụ dẫn dắt, người hát (`Male vocal / Female vocal / Duet`) và độ mạnh nhẹ; dấu ngoặc đơn `(...)` chỉ chứa tiếng ngân hoặc lời bè hát thành tiếng.
   - **Mạch kể chuyện (`Verse` & `Chorus`):** Giữ đúng ngôi kể đã chọn ở `1-idea.md`. Câu đầu `Verse 1` vào thẳng một hành động, lời nói thân tình hoặc khung cảnh cụ thể; `Verse` đan cài đủ 2 đến 3 móc neo giác quan từ `1-idea.md`. `Chorus` gom cảm xúc chính của bài hát lại tự nhiên, có câu `Hook` ngắn gọn vừa một hơi thở ở vị trí đinh (độc bản trong [`ref/lyrics-index.md`](../ref/lyrics-index.md)), giữ mạch thời gian và cảm xúc liền lạc đến cuối bài.
   - **Nhịp thở câu hát, Vần & Định dạng sạch:** Dòng hát vừa một hơi thở (khoảng 3 đến 4 nhịp nhấn), đan xen câu dài kể chuyện và câu ngắn nghỉ hơi; cặp vần thuận theo nghĩa và đổi mới so với các bài liền kề. Tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md), [`humanizer`](../.agents/skills/humanizer/SKILL.md) và [`stop-slop`](../.agents/skills/stop-slop/SKILL.md); mọi con số viết thành chữ tiếng Anh; `3-lyrics.txt` khớp 1:1 từng dòng lời có chữ với `2-music.md`, viết hoa chữ cái đầu dòng, để trống dấu câu cuối dòng và cách các khổ đúng 1 dòng trống.

### 1.2. Ba đòn bẩy thực chứng `[HIGH RISK]` (Chọn đòn bẩy phù hợp với từng bài từ [`ref/doi-thu/RANKING.md`](../ref/doi-thu/RANKING.md))

1. **Phối giọng đối đáp hoặc giọng thứ hai bước vào sau:** Nam trầm ấm và nữ trong trẻo hát đối đáp theo khổ hoặc cặp câu, hoặc một giọng hát nửa đầu rồi giọng thứ hai bước vào ở nửa sau bài tạo cảm giác bầu bạn.
2. **Tiếng ngân con người và nhạc cụ gợi bối cảnh:** Điểm tiếng ngân (`"Mmm...", "Ooh..."`, `whistling`) cùng nhạc cụ mộc gợi không gian văn hóa của bài ở `Intro`, đoạn nối và `Outro`.
3. **Câu hát đinh giàu sức gợi và nâng cấp điệp khúc cuối:** Có cặp câu hát đinh giàu sức gợi từ chi tiết đời thường, kết hợp nâng nhẹ màu âm hoặc cách nhả chữ ở `[Final Chorus]`.

---

## 2. Quy trình 3 bước kiểm toán trên `2-music.md` và `3-lyrics.txt`

1. **Bước 1 (Đối chiếu Input/Output):** Đọc `1-idea.md`, `2-music.md`, `3-lyrics.txt`, [`ref/lyrics-index.md`](../ref/lyrics-index.md) và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) để kiểm tra đồng bộ tên bài, chế độ kể chuyện, 2 đến 3 móc neo giác quan và tính độc bản của câu `Hook`.
2. **Bước 2 (Thẩm định theo 3 khối Luật của Nhạc & Đòn bẩy WIN):** Kiểm tra lần lượt Tên bài nhạc (Mục 2.1), Style nhạc (Mục 2.2), Lyrics (Mục 2.3) và các đòn bẩy `[HIGH RISK]` phù hợp với bài.
3. **Bước 3 (Phán quyết `Pre-Audio Music Sign-Off`):** Chỉ cấp `PASS` và cập nhật [`ref/lyrics-index.md`](../ref/lyrics-index.md) khi cả 3 khối Luật của Nhạc (`2.1 Tên bài`, `2.2 Style nhạc`, `2.3 Lyrics`) đạt `100%`.
