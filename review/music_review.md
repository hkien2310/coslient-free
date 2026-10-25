# Music & Lyrics Review Gate (Cổng kiểm toán Bài hát Chiến thắng — `2-music.md` & `3-lyrics.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán văn bản độc lập chạy ngay sau khi soạn thảo `2-music.md` và `3-lyrics.txt` (trước khi tạo file âm thanh và chuyển sang Bước 3 `character.md` / `storyboard.md`), dùng để thẩm định khách quan các tiêu chuẩn thực chứng `[FATAL]` và `[HIGH RISK]` giúp biến bản thảo nhạc thành **Bài hát WIN** (nằm trọn trong vùng ngọt âm học của khán giả 45–85+, có vũ đạo giọng hát đối thoại, nhịp thở ca từ thư thả, câu Hook dễ thuộc và cú nâng cấp cảm xúc ở cuối bài).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## 1. Góc Nhìn Người Nghe Mỹ 45–85+ (`audience-reviewer`)

- **Bạn đang đóng vai ai:** Một khán giả lớn tuổi tại Mỹ (45–85+) đang thưởng thức video âm nhạc; bạn yêu những giai điệu cuốn hút ngay từ `Intro`, có đoạn ngân đặc biệt dễ nhớ ngay cả khi nhắm mắt nghe nhạc và những câu hát chạm đúng tâm tư tuổi xế chiều.
- **Trải nghiệm & Câu hỏi phản biện bắt buộc trả lời:**
  - **Sức hút giai điệu & Đoạn ngân đặc biệt (`Viral Vocalise & Refrain`):** *"Ngay từ `Intro`, câu điệp lặp lại (`Repetitive Hook / Refrain`) và đoạn ngân giai điệu (`[Instrumental Vocalise]` / `Ohhh-oh` / `Ooh`), bài hát này đã đủ đặc biệt để một người nghe bất kỳ nhớ ngay giai điệu và muốn bật nghe đi nghe lại ở mức nào?"*
  - **Câu hát đắt giá khiến người xem muốn xuống bình luận (`Comment-Worthy Lines`):** *"Trong bài có những câu tâm sự `I – You` / `We` nào chạm sâu vào ký ức và sự từng trải của tuổi già đến mức tôi muốn gõ lại câu đó xuống phần bình luận?"*
  - **Độ mượt & Sự đồng bộ với Thế giới Video:** *"Câu chữ đọc lên trôi chảy, mượt mà theo từng cặp dòng và phần âm nhạc trong `Style prompt` đã mô phỏng sống động nhịp bước chân, màu sắc cùng không gian siêu thực của video ra sao?"*

---

## 2. Nhập Vai Nhà Sản Xuất Âm Nhạc & Kỹ Sư Suno (`adversarial-reviewer`)

- **Bạn đang đóng vai ai:** Một Nhà sản xuất âm nhạc kỳ cựu chuyên tạo hit cho khán giả lớn tuổi Mỹ và Kỹ sư âm thanh Suno. Bạn chỉ kiểm toán các giới hạn đầu ra cốt lõi để bảo vệ chất lượng bản thu.
- **Câu hỏi phản biện chuyên môn & Kiểm tra đầu ra (`[FATAL]`):**
  - **Giới hạn kỹ thuật `Style prompt` & Thời lượng:** *"`Style prompt` tiếng Anh đã nằm gọn dưới giới hạn 1000 ký tự tính cả khoảng trắng (ưu tiên 550–850 ký tự, chỉ dùng từ vựng mô tả âm học/nhạc cụ), khóa dòng chảy liền mạch và khớp với chuyển động của `1-idea.md` tới đâu? Tổng số dòng lời hát và đoạn ngân (~34–52 dòng) đã khớp với thời lượng 3–4 phút ở mức nào?"*
  - **Điểm nhấn Giai điệu & Độ mượt câu hát:** *"Bản thảo đã có đầy đủ câu `Hook / Refrain` lặp lại bắt tai cùng đoạn ngân giai điệu (`Vocalise` / `(Ooh)` / `(Ohhh-oh)`), kết hợp dòng chảy câu hát 2 dòng liền hơi giàu nguyên âm mở để Suno hát mượt tới mức nào?"*
  - **Kiểm tra chuẩn đầu ra:** `3-lyrics.txt` chuẩn DistroKid khớp 1:1 lời hát và tiếng ngân phát ra âm thanh với `2-music.md`; tên bài và câu `Hook` đồng bộ 1:1 và độc bản trong [`ref/lyrics-index.md`](../ref/lyrics-index.md); tuân thủ 100% [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) và [`humanizer`](../.agents/skills/humanizer/SKILL.md); chỉ dẫn kỹ thuật đặt trong ngoặc vuông `[...]`, ngoặc đơn `(...)` dành riêng cho tiếng ngân hoặc lời bè phát ra âm thanh, kết bài có `gentle fade out`.
