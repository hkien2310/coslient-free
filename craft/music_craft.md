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
  - **`2-music.md`:** Tên bài, `Style prompt`, `Exclude` và `Lyrics` kèm thẻ điều phối.
  - **`3-lyrics.txt`:** Lời sạch chuẩn DistroKid (chỉ giữ thuần lời hát và tiếng ngân phát ra âm thanh, viết hoa đầu dòng, mỗi dòng 1 câu đơn, để trống dấu câu cuối dòng, ghi đủ các khổ lặp lại, cách khổ 1 dòng trống).
  - **`ref/lyrics-index.md`:** Cập nhật bài hát mới.

---

## 2. Luật Đầu Ra & Cảm Xúc (`Output & Audience Rules`)

- **1. Khán giả mục tiêu (Người lớn tuổi Mỹ 45–85+) & Thời lượng (~3–4 phút):**
  - Sáng tác bài hát dài khoảng 3–4 phút (~34–52 dòng lời hát và tiếng ngân) theo đúng gu thưởng thức của khán giả lớn tuổi tại Mỹ: giai điệu cuốn hút ngay từ `Intro`, ấm áp, dễ nghe, dễ hát nhẩm theo, mang thông điệp tích cực và khiến người nghe muốn bật nghe lại nhiều lần.
- **2. Điểm nhấn Giai điệu Đặc biệt (`Viral Melodic Hook & Vocalise`):**
  - Thiết kế phần giai điệu đủ đặc biệt để chinh phục người nghe vượt qua mọi rào cản ngôn ngữ bằng 2 điểm nhấn:
    - **Câu điệp lặp lại gây nghiện (`Repetitive Hook / Refrain`):** Lặp lại 2 lần liên tiếp câu `Hook` ngắn gọn, giàu nhịp điệu tại điệp khúc hoặc cuối khổ hát để người nghe thuộc ngay từ lần đầu.
    - **Đoạn ngân giai điệu (`[Instrumental Vocalise]` & Tiếng ngân `(Ooh)` / `(Ohhh-oh)`):** Đưa vào bài hát một phân đoạn ngân giai điệu giàu cảm xúc hoặc đan xen các tiếng ngân `(Ooh)`, `(Ohhh-oh)`, `(Mmm-hmm)` trong điệp khúc để Suno bung ra nét giai điệu bắt tai nhất.
- **3. Lời tâm sự (`I – You` / `We`) & Những câu hát đắt giá (`Comment-Worthy Lines`):**
  - Kể chuyện tự nhiên, mượt mà từ góc nhìn `I – You` / `We` (nối từng cặp 2 dòng liền hơi bằng từ ngữ đời thường giản dị, giàu nguyên âm mở); điểm xuyết tín hiệu giác quan từ `1-idea.md` và cài cắm những câu hát đắt giá chạm sâu vào ký ức, sự từng trải của tuổi già khiến khán giả muốn trích dẫn lại dưới phần bình luận (tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) và [`humanizer`](../.agents/skills/humanizer/SKILL.md)).
- **4. Tự do sáng tạo `Style prompt` khớp Chuyển động & Không gian Video (Tối đa 1000 ký tự):**
  - Viết `Style prompt` hoàn toàn bằng tiếng Anh với độ dài tối đa 1000 ký tự tính cả khoảng trắng (ưu tiên khoảng 550–850 ký tự, chỉ dùng thuần túy từ ngữ mô tả âm học, nhạc cụ và cảm xúc).
  - Tự do lựa chọn thể loại, nhạc cụ, nhịp độ (`BPM`) và điệu thức đặc sắc nhất để **mô phỏng trực tiếp nhịp chuyển động vật lý, màu sắc và bầu không khí siêu thực của video (`1-idea.md`)**; khóa rõ tính chất giai điệu dễ nhớ (`simple, hummable, soothing melody`) và dòng chảy âm nhạc liền mạch mượt mà xuyên suốt bài.
  - Tách riêng các yếu tố điện tử lạc tông, trống ồn ào và âm tần chói gắt vào trường `Exclude`.
- **5. Thẻ điều phối trong `Lyrics`:**
  - Tự do đặt nhãn phân đoạn và mô tả thêm giai điệu, nhạc cụ, sắc thái bằng tiếng Anh trong ngoặc vuông `[...]` từ `[Intro: ...]` đến `[Outro: ..., gentle fade out]` để dẫn dắt Suno đạt hiệu quả cảm xúc cao nhất; dành riêng ngoặc đơn `(...)` cho tiếng ngân và lời hát bè thực sự phát ra âm thanh.
