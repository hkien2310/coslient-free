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
  - **`3-lyrics.txt`:** Lời sạch chuẩn DistroKid (chỉ giữ thuần lời hát, viết hoa đầu dòng, mỗi dòng 1 câu đơn, để trống dấu câu cuối dòng, ghi đủ các khổ lặp lại, cách khổ 1 dòng trống).
  - **`ref/lyrics-index.md`:** Cập nhật bài hát mới.

---

## 2. Luật Bài Nhạc (`Universal Song Rules`)

### 2.1. Phần Lời & Ca Khúc
- **Ngôi kể & Tâm tình (`I – You` Storytelling):** Hát từ góc nhìn ngôi thứ nhất thủ thỉ trực tiếp với ngôi thứ hai (`I – You` / `We`) như lời tâm sự của một người tri kỷ; mỗi khổ điểm xuyết 1–2 tín hiệu giác quan quen thuộc từ `1-idea.md` làm điểm tựa rồi mở rộng sang chiêm nghiệm, ký ức và lòng biết ơn êm đềm (nhường phần triển khai hoạt cảnh đa nhân vật cho `storyboard.md`).
- **Tên bài & Câu Hook:** Đặt tên bài và câu `Hook` ngắn gọn bằng từ ngữ đời thường giàu sức gợi, đặt tại điểm nhấn mở hoặc khép của điệp khúc để neo vào trí nhớ người nghe và đồng bộ 1:1 trên mọi file.
- **Cấu trúc bài hát:** Sắp xếp linh hoạt các phân đoạn (`Intro`, `Verse`, `Pre-Chorus`, `Chorus`, `Interlude / Instrumental Solo`, `Bridge`, `Outro`) khớp với mạch cảm xúc câu chuyện, cân đối hài hòa giữa phần lời hát và khoảng thở nhạc dạo.
- **Dùng từ & Độ mở liên tưởng:** Dùng từ vựng tiếng Anh đời thường giản dị như lời trò chuyện thật, giữ độ mở cao để người nghe dễ đồng cảm và đạo diễn hình ảnh dễ lồng ghép nhiều lát cắt cuộc sống (tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) và [`humanizer`](../.agents/skills/humanizer/SKILL.md)).
- **Nhịp câu văn nói (`Conversational Phrasing`) & Gieo vần:** Viết câu hát theo nhịp lời nói tự nhiên với độ dài dòng co giãn linh hoạt theo hơi thở, kết hợp khẩu ngữ, vần chính, vần bán âm và những câu chốt ngắn đứng độc lập để ca sĩ nhả chữ lơi nhịp, truyền cảm.

### 2.2. Phần Âm Nhạc & Bản Phối
- **Thể loại & Nhịp đàn tự nhiên:** Lấy `Warm Cinematic / Acoustic Folk` kết hợp hơi thở đồng quê ấm áp (`Americana / pastoral countryside atmosphere`) ở tốc độ thư thả (`74–82 BPM`), dẫn dắt bởi đàn guitar gảy có độ co giãn nhịp tự nhiên của người thật (`fingerpicked acoustic guitar with natural timing variations`) cùng lớp quạt nhẹ tạo đà tiến êm (`soft strummed layers creating a gentle forward motion`).
- **Nhịp nền, Hòa âm tiết chế & `Signature Sound`:** Giữ nhịp nền trầm ổn bằng bass gỗ ấm đi hơi trễ sau phách (`upright bass sitting slightly behind the beat`) cùng trống kick mềm và chổi quét giữ dòng chảy (`light kick and brushed snare maintaining a steady grounded flow`); điểm xuyết thật thưa thoáng (`sparse / used sparingly`) các nhạc cụ mộc gợi không gian hoài niệm cùng 1 câu ngân hoặc âm sắc định danh (`Signature Motif`) nhẹ nhàng xuyên suốt bài.
- **Giọng hát & Giai điệu dễ nhớ:** Ưu tiên 1 giọng hát đơn ca từng trải, ấm áp, điềm tĩnh xuyên suốt bài (`mature, warm, slightly weathered vocal, calm and content, expressive phrasing`), kết hợp giai điệu giản dị dễ ngân nga (`simple, hummable, soothing melody`).
- **Độ mở tiết chế (`Restrained Dynamics`):** Xây dựng bản phối dày dần một cách tinh tế với điệp khúc sáng rõ hơn để tạo độ nhớ trong khi tổng thể luôn giữ sự chừng mực, êm dịu (`arrangement builds gradually with slightly stronger choruses for memorability while remaining restrained`).

---

## 3. Kỹ Thuật Suno (`Suno Technique`)

### 3.1. `Style prompt` & `Exclude`
- **Mô hình `Style prompt` văn xuôi tự nhiên:** Viết thành đoạn văn tiếng Anh liền mạch mô tả cảm giác âm nhạc và sự tiết chế của người chơi đàn theo trình tự: `[Thể loại Warm Cinematic/Acoustic Folk + Không khí đồng quê + 74–82 BPM]` $\to$ `[Đàn guitar gảy có độ lơi nhịp tự nhiên (fingerpicked acoustic guitar with natural timing variations) + Lớp quạt nhẹ tạo đà tiến]` $\to$ `[Nhịp bass gỗ trễ sau phách + Kick mềm & brushed snare giữ dòng chảy êm + Nhạc cụ điểm xuyết thưa thoáng (sparse/used sparingly) + Signature Motif]` $\to$ `[Độ mở điệp khúc tiết chế (builds gradually while remaining restrained) + 1 giọng hát từng trải ấm áp + Giai điệu giản dị dễ ngân nga (simple, hummable, soothing melody)]`.
- **`Exclude`:** Tách riêng các yếu tố điện tử, trống mạnh, kỹ xảo giọng hát và âm tần chói gắt vào trường `Exclude`, cách nhau bằng dấu phẩy.

### 3.2. Thẻ Điều Phối & `Lyrics`
- **Thẻ phân đoạn tối giản:** Giữ các thẻ phân đoạn chính gọn sạch (`[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`) để duy trì dòng chảy giọng hát liền mạch từ đầu đến cuối; chỉ ghi chú chỉ dẫn nhạc cụ và sắc thái ngắn gọn bằng tiếng Anh tại các điểm chuyển lớn (`[Intro: ...]`, `[Interlude: ...]`, `[Final Chorus: ...]`, `[Outro: ..., gentle fade out]`).
- **Lời bè / Tiếng ngân `(...)`:** Dành riêng ngoặc đơn `(...)` cho những âm ngân hoặc câu hát bè thực sự phát ra tiếng của ca sĩ.
