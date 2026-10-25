# Music & Lyrics Review Gate (Cổng kiểm toán Bài hát Chiến thắng — `2-music.md` & `3-lyrics.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `2-music.md` và `3-lyrics.txt` (trước khi tạo file âm thanh và chuyển sang Bước 3 `character.md` / `storyboard.md`), dùng để thẩm định khách quan các tiêu chuẩn thực chứng `[FATAL]` và `[HIGH RISK]` giúp biến bản thảo nhạc thành **Bài hát WIN** (nằm trọn trong vùng ngọt âm học của khán giả 45–85+, có vũ đạo giọng hát đối thoại, nhịp thở ca từ thư thả, câu Hook dễ thuộc và cú nâng cấp cảm xúc ở cuối bài).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## 1. Góc Nhìn Người Nghe 45–85+ (`audience-reviewer`)

- **Bạn đang đóng vai ai:** Một người nghe nhạc 45–85+ đang bật loa TV/iPad tìm kiếm sự đồng cảm và thư giãn; tai nhạy cảm với âm thanh chói gắt/ồn ào, yêu chất nhạc Folk mộc mạc và lời ca giản dị, chân thật.
- **Trải nghiệm & Câu hỏi phản biện bắt buộc trả lời:**
  - **Cảm giác khi nghe lời hát:** *"Lời bài hát này nghe có tự nhiên như một người bạn già đang thủ thỉ kể chuyện đời thường không, hay nghe sượng trân, hoa mỹ sáo rỗng kiểu văn mẫu AI?"*
  - **Độ bắt tai của Tên bài & Câu Hook:** *"Nghe xong 1 lần, tôi có thuộc và nhẩm lại được câu đinh (`Hook`) ở điệp khúc không?"*
  - **Độ dễ hát & Nhịp thở:** *"Đọc to từng dòng lời lên, câu chữ có ngắn gọn, êm tai và vừa một hơi thở tự nhiên không, hay bị dài dòng làm ca sĩ hát líu lưỡi?"*
  - **Trải nghiệm thính giác & `Signature Sound`:** *"Bản phối thiết kế trong `Style prompt` và các thẻ `[...]` có tạo ra không gian mộc mạc ấm áp, có khoảng nghỉ nhạc dạo để thở và có 1 âm thanh đặc trưng (`Signature Sound`) của thị trấn làm tôi nhớ mãi không?"*

---

## 2. Góc Nhìn Chuyên Gia Nhạc Sĩ & Chuẩn Đầu Ra (`adversarial-reviewer` — `[FATAL]`)

- **Đúng định dạng & Đồng bộ 1:1:**
  - `2-music.md` có đủ Tên bài, `Style prompt` (4 khối ngăn cách bằng `;`), `Exclude` và `Lyrics` kèm thẻ `[...]`.
  - `3-lyrics.txt` chuẩn DistroKid khớp 1:1 lời hát với `2-music.md` (chỉ giữ lời hát, viết hoa đầu dòng, mỗi dòng 1 câu đơn, bỏ thẻ `[...]`, bỏ dấu câu cuối dòng, ghi đủ các khổ lặp lại, cách khổ 1 dòng trống).
  - Tên bài và câu `Hook` đồng bộ 1:1 và độc bản trong [`ref/lyrics-index.md`](../ref/lyrics-index.md).
- **Sạch từ cấm & Văn phong AI:** Tuân thủ tuyệt đối [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md), [`humanizer`](../.agents/skills/humanizer/SKILL.md), [`stop-slop`](../.agents/skills/stop-slop/SKILL.md) và [`avoid-ai-writing`](../.agents/skills/avoid-ai-writing/SKILL.md); làm mới cặp từ vần so với các bài gần nhất.
- **Chuẩn Kỹ thuật Suno:** Đầu mỗi đoạn có thẻ `[Tên đoạn: Nhạc cụ / Signature Sound, Giọng hát, Sắc thái]`, kết bài bằng `[Outro: ..., gentle fade out]`, ngoặc đơn `(...)` chỉ chứa tiếng ngân/bè phát ra tiếng.
