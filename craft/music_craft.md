# Music craft

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` để thiết kế âm nhạc (`Style prompt`), sáng tác lời bài hát theo đúng Chế độ Kể chuyện đã chọn và xuất ra `2-music.md`, `3-lyrics.txt` cùng cập nhật `ref/lyrics-index.md`. Không chứa quy tắc tạo hình nhân vật (`character.md`), chia cảnh (`storyboard.md`) hay câu lệnh sinh ảnh (`image.txt`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra

- **Đầu vào:** `1-idea.md`, `ref/lyrics-index.md`, `ref/banned_lyrics_motifs.md`.
- **Đầu ra:**
  - **`2-music.md`:** Tên bài, `Style prompt`, `Exclude` và `Lyrics` kèm thẻ `[...]`.
  - **`3-lyrics.txt`:** Lời sạch chuẩn DistroKid (chỉ giữ lời hát, viết hoa đầu dòng, mỗi dòng 1 câu đơn, bỏ thẻ `[...]`, bỏ dấu câu cuối dòng, ghi đủ các khổ lặp lại, cách khổ 1 dòng trống).
  - **`ref/lyrics-index.md`:** Cập nhật bài hát mới.

---

## 2. Luật Bài Nhạc (`Universal Song Rules`)

### 2.1. Phần Lời & Ca Khúc
- **Ý niệm & Kể chuyện:** Kể chuyện tự nhiên qua những chi tiết và khoảnh khắc đời sống từ `1-idea.md`, để cảm xúc tự thấm qua mạch truyện.
- **Tên bài & Câu Hook:** Đặt tên bài và câu `Hook` ngắn gọn bằng từ ngữ đời thường giàu sức gợi, đặt tại điểm nhấn của điệp khúc để neo vào trí nhớ người nghe và đồng bộ 1:1 trên mọi file.
- **Cấu trúc bài hát:** Sắp xếp linh hoạt các phân đoạn (`Intro`, `Verse`, `Pre-Chorus`, `Chorus`, `Refrain / Post-Chorus`, `Interlude / Instrumental Solo`, `Bridge`, `Outro` — tùy chọn theo từng bài) khớp với mạch cảm xúc câu chuyện, cân đối hài hòa giữa phần lời hát và khoảng thở nhạc dạo.
- **Dùng từ & Hình ảnh:** Dùng từ vựng tiếng Anh đời thường giản dị như lời trò chuyện thật, gắn cảm xúc với sự vật và không gian cụ thể (tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) và [`humanizer`](../.agents/skills/humanizer/SKILL.md)).
- **Nhịp câu & Độ dễ hát:** Giữ mỗi dòng hát gọn vừa một hơi thở tự nhiên, ngắt nhịp rõ ràng, kết hợp khẩu ngữ và âm mở/âm vang mềm để ca sĩ nhả chữ mượt mà, liền hơi.
- **Gieo vần:** Linh hoạt chọn kiểu vần (vần cách, vần cặp, vần bán âm) hợp với mạch tự sự, ưu tiên sự tự nhiên của câu chữ và làm mới cặp từ vần qua từng bài.

### 2.2. Phần Âm Nhạc & Bản Phối
- **Thể loại & Không khí:** Lấy `Acoustic Folk` mộc mạc làm gốc, linh hoạt pha trộn màu sắc âm nhạc (thính phòng, đồng quê, ballad...) trong không gian âm thanh ấm cúng hợp với câu chuyện.
- **Tốc độ, Nhịp phách & Điệu thức:** Chọn tốc độ (`BPM`), nhịp phách (`4/4`, `3/4`, `6/8`...) và điệu thức (`Major / Minor`) khớp với nhịp thở và sắc thái cảm xúc riêng của bài hát.
- **Nhạc cụ & Âm thanh định danh (`Signature Sound`):** Phối hợp lớp nhạc cụ mộc giữ nhịp nền với lớp nhạc cụ giai điệu ngân dài; chọn 1 âm sắc nhạc cụ hoặc câu ngân giai điệu độc bản chuyển hóa trực tiếp từ âm thanh/nhịp điệu đặc trưng của bối cảnh trong `1-idea.md` làm dấu ấn riêng xuyên suốt bài hát.
- **Giọng hát:** Chọn giọng Nam, Nữ hoặc Song ca ấm áp, thu gần mic giàu hơi thở và nhả chữ thong thả như đang tâm sự.
- **Cao trào & Độ lắng:** Điều phối độ dày mỏng của nhạc cụ lên xuống tự nhiên theo mạch bài: mở đầu mộc mạc, mở rộng hòa âm ở cao trào và rút gọn nhạc cụ ở các điểm lắng hoặc đoạn kết để tôn giọng hát.

---

## 3. Kỹ Thuật Suno (`Suno Technique`)

### 3.1. `Style prompt` & `Exclude`
- **Mô hình cấu trúc 4 khối ngăn cách bằng dấu chấm phẩy `;`:**
  `[Cảm xúc + Thể loại Folk + Nhịp đàn chính, BPM & Điệu thức] ; [Lớp nhạc cụ nền & Tốc độ lớp nền + Nhạc cụ giai điệu ngân dài + Nhạc cụ định danh Signature Sound] ; [Không gian thu mộc + Điểm nhấn đoạn dạo/cao trào] ; [Màu giọng + Tốc độ/Lối nhả chữ liền hơi]`
- **`Exclude`:** Ghi các yếu tố điện tử, trống mạnh, kỹ xảo giọng hát và âm tần chói cần lọc bỏ, cách nhau bằng dấu phẩy.

### 3.2. Thẻ Điều Phối & `Lyrics`
- **Các thẻ cấu trúc (tùy chọn linh hoạt theo bài):** `[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Refrain]` / `[Post-Chorus]`, `[Interlude]` / `[Instrumental Solo]`, `[Bridge]`, `[Outro]`.
- **Cách viết thẻ `[...]` đầu mỗi đoạn:** Ghi ngắn gọn bằng tiếng Anh theo mẫu `[Tên đoạn: Nhạc cụ dẫn dắt / Signature Sound, Giọng hát, Sắc thái]`.
- **Thẻ kết bài:** Dùng `[Outro: ..., gentle fade out]` để nhạc hạ dần êm ái.
- **Lời bè / Tiếng ngân `(...)`:** Chỉ đặt trong ngoặc đơn `(...)` những âm ngân hoặc câu hát bè thực sự phát ra tiếng.
