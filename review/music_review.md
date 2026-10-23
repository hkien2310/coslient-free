# Music & Lyrics Review Gate (Cổng kiểm toán Bài hát Chiến thắng — `2-music.md` & `3-lyrics.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `2-music.md` và `3-lyrics.txt` (trước khi tạo file âm thanh và chuyển sang Bước 3 `character.md` / `storyboard.md`), dùng để thẩm định khách quan các tiêu chuẩn thực chứng `[FATAL]` và `[HIGH RISK]` giúp biến bản thảo nhạc thành **Bài hát WIN** (nằm trọn trong vùng ngọt âm học của khán giả 45–85+, có vũ đạo giọng hát đối thoại, nhịp thở ca từ thư thả, câu Hook dễ thuộc và cú nâng cấp cảm xúc ở cuối bài).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Phân cấp tiêu chuẩn kiểm toán Bài hát WIN (`[FATAL]` & `[HIGH RISK]` - Đúc kết từ [`ref/doi-thu/RANKING.md`](../ref/doi-thu/RANKING.md) & [`ref-real-music/index.md`](../ref-real-music/index.md))

### 1.1. Năm tiêu chuẩn nền tảng `[FATAL]` (Đạt 100% trước khi tạo nhạc và mở khóa Bước 3)

1. **Tên bài hát (`Track Title`) giàu chất Folk và câu `Hook` ngắn bắt tai:**
   - **Tên bài hát (`Track Title`, 3 đến 6 từ tiếng Anh):** Dùng từ vựng đời sống giản dị, giàu chất Folk và gợi ra bối cảnh hoặc lời tâm tình của `1-idea.md`.
   - **Câu `Hook` ở điệp khúc:** Đặt câu `Hook` ngắn gọn, dễ hát và vừa một hơi thở ở vị trí đinh của `[Chorus]` để khán giả 45-85+ dễ nhẩm thuộc ngay lần đầu.

2. **Nhịp thở dễ hát, mở đầu trực diện và vần tự nhiên:**
   - **Nhịp thở câu hát:** Mỗi dòng vừa một hơi thở hát (khoảng 3 đến 4 nhịp nhấn), đan xen tự nhiên giữa câu dài kể chuyện và câu ngắn nghỉ hơi.
   - **Vần tự nhiên & tươi mới:** Gieo vần thuận theo nghĩa câu chữ và chủ động đổi cặp từ gieo vần so với các bài liền kề.
   - **Điểm mở trực diện & ngôi kể nhất quán:** Câu đầu tiên của `Verse 1` vào thẳng một hành động, lời nói thân tình hoặc khung cảnh cụ thể; giữ đúng ngôi kể đã chọn xuyên suốt bài.

3. **Chuẩn `Style prompt` cho Suno, nhịp hai tầng và thẻ `[...]` gọn:**
   - **`Style prompt` (khoảng 55 đến 85 từ tiếng Anh) & `Exclude` (4 đến 6 thành phần):** Dùng các cụm danh từ mô tả âm thanh trực quan. Câu đầu nêu rõ nhánh Folk, điệu thức ấm, tempo thư thả quanh `58-86 BPM` với cấu trúc nhịp hai tầng (lớp đệm dưới giữ nhịp chuyển động đều đặn, lớp giai điệu và giọng hát phía trên ngân thong thả), màu giọng/cách phối giọng và nhạc cụ mộc hợp bối cảnh `1-idea.md`; bản thu ấm gần mic, bộ gõ nhẹ và dải tần cao dịu mượt.
   - **Biến đổi màu âm & đoạn nghỉ khí nhạc:** Thẻ `[...]` tiếng Anh ngắn gọn (3 đến 10 từ) ở đầu mỗi đoạn ghi rõ tên đoạn, nhạc cụ dẫn dắt, người hát (`Male vocal / Female vocal / Duet`) và độ mạnh nhẹ; có đoạn nghỉ khí nhạc (`[Instrumental Solo / Interlude]`); dấu ngoặc đơn `(...)` chỉ chứa tiếng ngân hoặc lời bè hát thành tiếng.

4. **Mạch kể chuyện linh hoạt, điểm rơi điệp khúc và móc neo giác quan:**
   - **Kể chuyện ở `Verse` & gom cảm xúc ở `Chorus`:** Mạch lời ở `Verse` phát triển tự nhiên qua các khổ và đan cài 2 đến 3 móc neo giác quan của `1-idea.md`; `Chorus` gom cảm xúc chính của bài hát lại một cách tự nhiên (lời hẹn ước, nhịp bước chân giữa cảnh vật, cảm giác bình yên hoặc suy ngẫm nhẹ nhõm).
   - **Độ mở năng lượng & sự liền lạc:** Các đoạn có độ mở năng lượng khác nhau và có một đoạn lắng mộc mạc để tôn lời hát, giữ mạch thời gian và cảm xúc liền lạc đến hết bài.

5. **Văn phong đời thực và chuẩn định dạng DistroKid:**
   - Ca từ dùng từ vựng và chi tiết đời thực tự nhiên, tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md), [`humanizer`](../.agents/skills/humanizer/SKILL.md) và [`stop-slop`](../.agents/skills/stop-slop/SKILL.md).
   - Tên bài hát đồng bộ 1:1 giữa `1-idea.md`, `2-music.md`, thư mục dự án và [`ref/lyrics-index.md`](../ref/lyrics-index.md); mọi con số viết thành chữ tiếng Anh; file `3-lyrics.txt` khớp 1:1 từng dòng lời có chữ với `2-music.md`, viết hoa chữ cái đầu dòng, để trống dấu câu cuối dòng và cách các khổ đúng 1 dòng trống.

### 1.2. Ba đòn bẩy thực chứng `[HIGH RISK]` (Chọn đòn bẩy phù hợp với từng bài từ [`ref/doi-thu/RANKING.md`](../ref/doi-thu/RANKING.md))

1. **Phối giọng đối đáp hoặc giọng thứ hai bước vào sau:**
   - Nam trầm ấm và nữ trong trẻo hát đối đáp theo khổ hoặc cặp câu, hoặc một giọng hát nửa đầu rồi giọng thứ hai bước vào ở nửa sau bài tạo cảm giác bầu bạn.
2. **Tiếng ngân con người và nhạc cụ gợi bối cảnh:**
   - Điểm tiếng ngân (`"Mmm...", "Ooh..."`, `whistling`) cùng nhạc cụ mộc gợi không gian văn hóa của bài ở `Intro`, đoạn nối và `Outro`.
3. **Câu hát đinh giàu sức gợi và nâng cấp điệp khúc cuối:**
   - Có cặp câu hát đinh giàu sức gợi từ chi tiết đời thường, kết hợp nâng nhẹ màu âm hoặc cách nhả chữ ở `[Final Chorus]`.

---

## 2. Quy trình 3 bước kiểm toán độc lập trên `2-music.md` và `3-lyrics.txt`

### Bước 1: Đối chiếu chéo `1-idea.md`, `ref/lyrics-index.md` và `ref/banned_lyrics_motifs.md`
- Đọc `projects/XXX/1-idea.md`, `projects/XXX/2-music.md`, `3-lyrics.txt`, [`ref/lyrics-index.md`](../ref/lyrics-index.md) và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md).
- Kiểm tra đồng bộ 1:1 của `Track Title`, Chế độ kể chuyện, 2 đến 3 móc neo giác quan từ `1-idea.md` và tính độc bản của câu `Hook` trong kho nhạc.

### Bước 2: Thẩm định theo 5 Cổng `[FATAL]` và 3 Đòn bẩy `[HIGH RISK]`
- **Cổng 1 (`Track Title` & `Hook`):** Kiểm tra `Track Title` (3 đến 6 từ) và câu `Hook` ngắn gọn vừa một hơi thở ở `Chorus`.
- **Cổng 2 (`Nhịp thở câu hát`, `Mở bài trực diện` & `Vần`):** Kiểm tra câu đầu `Verse 1` vào thẳng hành động/lời nói cụ thể, dòng hát co giãn dài ngắn tự nhiên (khoảng 3 đến 4 nhịp nhấn) và cặp vần tươi mới.
- **Cổng 3 (`Style prompt`, `Nhịp hai tầng` & `Thẻ [...] gọn 3-10 từ`):** Đếm từ `Style prompt` (khoảng 55 đến 85 từ), kiểm tra mô tả trực quan cho Suno (nhánh Folk, nhịp hai tầng quanh `58-86 BPM`, màu giọng, nhạc cụ mộc hợp bối cảnh, thu âm ấm dịu tần số cao), thẻ `[...]` gọn rõ vai và có `[Instrumental Solo / Interlude]`.
- **Cổng 4 (`Mạch kể chuyện`, `Độ mở năng lượng` & `Móc neo`):** Kiểm tra mạch chuyện phát triển tự nhiên, đủ 2 đến 3 móc neo từ `1-idea.md`, điểm rơi cảm xúc ở `Chorus` và đoạn lắng mộc mạc tôn lời hát.
- **Cổng 5 (`Văn phong`, `3-lyrics.txt` & `Đòn bẩy WIN`):** Quét [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md), kiểm tra [`humanizer`](../.agents/skills/humanizer/SKILL.md), số viết bằng chữ tiếng Anh, khớp 1:1 với `3-lyrics.txt` và các đòn bẩy `[HIGH RISK]` phù hợp với bài.

### Bước 3: Bảng đối soát định lượng và Phán quyết (`Pre-Audio Music Sign-Off`)
Xác nhận `2-music.md` và `3-lyrics.txt` đạt đủ 5 chỉ số `[FATAL]` cùng các đòn bẩy `[HIGH RISK]` phù hợp trước khi cập nhật [`ref/lyrics-index.md`](../ref/lyrics-index.md):
- **Chỉ số 1 (`Track Title` 3-6 từ & Câu `Hook` ngắn dễ thuộc - `100%`):** Tên bài gợi hình/tâm tình và câu Hook vừa một hơi thở.
- **Chỉ số 2 (Mở đầu trực diện Câu 1, Nhịp thở câu dài ngắn tự nhiên & Vần tươi mới - `100%`):** Dòng hát vừa hơi thở trò chuyện, vần tự nhiên và giữ đúng ngôi kể xuyên suốt.
- **Chỉ số 3 (Chuẩn `Style prompt` Suno 55-85 từ, Nhịp hai tầng & Thẻ `[...]` gọn 3-10 từ - `100%`):** Mô tả âm thanh trực quan quanh `58-86 BPM` có nhịp hai tầng, phân vai giọng hát/nhạc cụ rõ và có `[Instrumental Solo / Interlude]`.
- **Chỉ số 4 (Đủ 2-3 Móc neo từ `1-idea.md`, Mạch kể linh hoạt & Độ mở năng lượng - `100%`):** Khớp móc neo giác quan, điệp khúc gom đúng cảm xúc chính và có đoạn lắng mộc mạc.
- **Chỉ số 5 (Từ vựng đời thực, Đồng bộ 1:1 `3-lyrics.txt` & Đòn bẩy WIN - `100%`):** Đạt chuẩn văn phong con người và định dạng phát hành.
