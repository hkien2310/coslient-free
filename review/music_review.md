# Music & Lyrics Review Gate (Cổng kiểm toán Bài hát Chiến thắng — `2-music.md` & `3-lyrics.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `2-music.md` và `3-lyrics.txt` (trước khi tạo file âm thanh và chuyển sang Bước 3 `character.md` / `storyboard.md`), dùng để thẩm định khách quan các tiêu chuẩn thực chứng `[FATAL]` và `[HIGH RISK]` giúp biến bản thảo nhạc thành **Bài hát WIN** (nằm trọn trong vùng ngọt âm học của khán giả 45–85+, có vũ đạo giọng hát đối thoại, nhịp thở ca từ thư thả, câu Hook dễ thuộc và cú nâng cấp cảm xúc ở cuối bài).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## 1. Góc Nhìn Người Nghe 45–85+ (`audience-reviewer`)

- **Bạn đang đóng vai ai:** Một người nghe nhạc 45–85+ đang bật loa TV/iPad tìm kiếm sự đồng cảm và thư giãn; tai yêu thích chất nhạc Folk mộc mạc, giai điệu giản dị dễ ngân nga và lời tâm sự chân thật giữa người với người.
- **Trải nghiệm & Câu hỏi phản biện bắt buộc trả lời:**
  - **Cảm giác khi nghe lời tâm sự (`I – You`):** *"Lời bài hát này nghe tự nhiên như một người bạn già đang thủ thỉ tâm sự trực tiếp với tôi (`I – You`) ở mức nào? Các tín hiệu giác quan đã điểm xuyết vừa đủ để gợi ký ức và nhường chỗ cho cảm xúc lắng đọng ra sao?"*
  - **Độ bắt tai của Tên bài & Câu Hook:** *"Nghe xong 1 lần, tôi thuộc và nhẩm lại ngay được câu đinh (`Hook`) ở điệp khúc dễ dàng tới đâu?"*
  - **Độ mượt của dòng chảy câu hát (`Flowing Phrasing`):** *"Đọc to từng cặp 2 dòng lời lên, câu chữ có nối liền nhau thành một hơi thở mềm mại với nguyên âm mở êm tai và vần liền kề tự nhiên ở mức nào?"*
  - **Trải nghiệm thính giác & Lớp đệm mượt:** *"Bản phối trong `Style prompt` và các thẻ `[...]` đã tạo ra không gian mộc mạc trong trẻo, có lớp đệm êm (`light piano, gentle bowed bass or very soft cello used sparingly, airy strings`) nâng đỡ tiếng guitar gảy và giọng hát dịu dàng giàu cảm xúc (`tenderness, gratitude, calm emotional clarity`) cùng 1 `Signature Motif` đáng nhớ ra sao?"*

---

## 2. Nhập Vai Nhạc Sĩ / Nhà Sản Xuất Folk & Kỹ Sư Suno (`adversarial-reviewer`)

- **Bạn đang đóng vai ai:** Một Nhạc sĩ kiêm Nhà sản xuất nhạc Acoustic Folk và Kỹ sư âm thanh Suno. Bạn thẩm định bản nhạc bằng con mắt chuyên môn về nhạc lý, độ mượt của dòng chảy thanh nhạc (`Smooth Melodic Flow`) và độ liền mạch trên Suno.
- **Câu hỏi phản biện chuyên môn & Kiểm tra đầu ra (`[FATAL]`):**
  - **Kỹ thuật viết lời & Độ mượt thanh nhạc:** *"Lời hát đã giữ vững ngôi tâm sự `I – You`, kết nối từng cặp 2 dòng thành một mạch câu liền hơi tự nhiên (`enjambment / flowing couplets`), dùng từ ngữ giàu nguyên âm mở và phụ âm mềm để ca sĩ ngân mượt và lướt chữ êm ái ở mức nào?"*
  - **Kỹ thuật phối khí & Suno Prompt:** *"Đoạn văn `Style prompt` đã khóa rõ tiếng guitar gảy trong trẻo (`clean, open tone`), lớp đệm dây/piano êm ái tiết chế (`gentle bowed bass or very soft cello used sparingly, airy strings`), 1 giọng hát từng trải giàu sự dịu dàng (`singing with tenderness, gratitude, calm emotional clarity, expressive phrasing`) và giai điệu dễ ngân nga (`simple, hummable, soothing melody`) tới đâu? Các thẻ `[...]` đã đủ tối giản để giữ mạch nhạc liền lạc xuyên suốt bài tới mức nào?"*
  - **Kiểm tra chuẩn đầu ra:** `3-lyrics.txt` chuẩn DistroKid khớp 1:1 lời hát với `2-music.md`; tên bài và câu `Hook` đồng bộ 1:1 và độc bản trong [`ref/lyrics-index.md`](../ref/lyrics-index.md); tuân thủ 100% [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) và [`humanizer`](../.agents/skills/humanizer/SKILL.md); kết bài bằng `[Outro: ..., gentle fade out]`, ngoặc đơn `(...)` chỉ chứa tiếng ngân hoặc lời bè phát ra tiếng.
