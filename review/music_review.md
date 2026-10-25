# Music & Lyrics Review Gate (Cổng kiểm toán Bài hát Chiến thắng — `2-music.md` & `3-lyrics.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `2-music.md` và `3-lyrics.txt` (trước khi tạo file âm thanh và chuyển sang Bước 3 `character.md` / `storyboard.md`), dùng để thẩm định khách quan các tiêu chuẩn thực chứng `[FATAL]` và `[HIGH RISK]` giúp biến bản thảo nhạc thành **Bài hát WIN** (nằm trọn trong vùng ngọt âm học của khán giả 45–85+, có vũ đạo giọng hát đối thoại, nhịp thở ca từ thư thả, câu Hook dễ thuộc và cú nâng cấp cảm xúc ở cuối bài).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## 1. Luật Kiểm Toán Đầu Ra `2-music.md` & `3-lyrics.txt`

### 1.1. Tiêu chuẩn bắt buộc (`[FATAL]`)
- **Định dạng đầu ra:**
  - **`2-music.md`:** Có đủ Tên bài, `Style prompt` (4 khối ngăn cách bằng `;`), `Exclude` và `Lyrics` kèm thẻ điều phối `[...]`.
  - **`3-lyrics.txt` (Chuẩn DistroKid):** Khớp 1:1 lời hát thực tế với `2-music.md`; chỉ giữ lời hát, viết hoa đầu dòng, mỗi dòng 1 câu đơn, bỏ thẻ `[...]`, bỏ dấu câu cuối dòng, ghi đủ các khổ lặp lại, cách khổ 1 dòng trống.
  - **Đồng bộ tên bài & Câu Hook:** Tên bài và câu `Hook` đồng bộ 1:1 giữa `1-idea.md`, `2-music.md`, `3-lyrics.txt` và độc bản trong [`ref/lyrics-index.md`](../ref/lyrics-index.md).
- **Kiểm toán Phần Lời (`Lyrics`):**
  - **Ý niệm & Kể chuyện:** Kể chuyện tự nhiên qua các chi tiết đời sống từ `1-idea.md`, để cảm xúc tự thấm qua mạch truyện.
  - **Dùng từ & Hình ảnh:** Dùng từ vựng tiếng Anh đời thường giản dị, gắn cảm xúc với sự vật cụ thể; tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md), [`humanizer`](../.agents/skills/humanizer/SKILL.md), [`stop-slop`](../.agents/skills/stop-slop/SKILL.md) và [`avoid-ai-writing`](../.agents/skills/avoid-ai-writing/SKILL.md).
  - **Nhịp câu & Gieo vần:** Mỗi dòng hát gọn vừa một hơi thở tự nhiên, dễ hát liền hơi; gieo vần tự nhiên hợp mạch tự sự và làm mới cặp từ vần so với các bài gần nhất.
- **Kiểm toán Phần Nhạc & Kỹ thuật Suno (`Style prompt` & Thẻ `[...]`):**
  - **`Style prompt` 4 khối `;`:** Khớp cảm xúc với `1-idea.md`, lấy `Acoustic Folk` làm gốc, ghi rõ BPM/nhịp/điệu thức, lớp nhạc cụ nền + giai điệu ngân dài + nhạc cụ định danh (`Signature Sound` gắn với bối cảnh `1-idea.md`), không gian thu mộc và màu giọng thu gần mic.
  - **Thẻ điều phối `[...]`:** Sắp xếp linh hoạt các phân đoạn hợp mạch bài (cân đối giữa lời hát và nhạc dạo), đầu mỗi đoạn có thẻ `[Tên đoạn: Nhạc cụ / Signature Sound, Giọng hát, Sắc thái]`, kết bài bằng `[Outro: ..., gentle fade out]`, ngoặc đơn `(...)` chỉ dùng cho tiếng ngân/bè phát ra tiếng.

### 1.2. Đòn bẩy nâng cấp (`[HIGH RISK]` — Chọn lọc theo bài)
- **Phối giọng linh hoạt:** Đối đáp Nam – Nữ hoặc giọng thứ hai bước vào ở nửa sau bài hợp với câu chuyện.
- **Điểm nhấn `Signature Sound` & Cao trào:** Nhạc cụ định danh hoặc tiếng ngân con người xuất hiện đúng điểm nhấn ở `Intro`, đoạn dạo và `Outro`; nâng cảm xúc ở điệp khúc cuối rồi lắng mộc ở câu kết.
