# Music craft

> 🔒 **QUY TẮC CHỈNH SỬA TÀI LIỆU NÀY:**
> 1. Không liệt kê lẻ tẻ sự vật sự kiện.
> 2. Không dùng phủ định.
> 3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## Nguyên tắc ngôn ngữ đời thường (Everyday Spoken Language)

1. **Khẩu ngữ sinh hoạt thực tế:** Ca từ phản ánh giọng điệu trò chuyện trực tiếp giữa những người thân thuộc trong cuộc sống hàng ngày. Lời hát mang tính chất tâm tình, mộc mạc và chân phương.
2. **Trường từ vựng vật chất cụ thể:** Lựa chọn danh từ định danh đồ vật thực tế và động từ hành động trực diện. Ưu tiên các từ đơn âm tiết hoặc hai âm tiết có tần suất xuất hiện cao trong giao tiếp đại chúng.
3. **Cấu trúc ngữ pháp thuận:** Giữ trật tự câu theo thói quen nói tự nhiên, rõ ràng, rành mạch. Mỗi dòng gói trọn một cụm ngữ pháp hoàn chỉnh và tương ứng với một nhịp thở tự nhiên.
4. **Mỏ neo cảm xúc và thời gian qua vật lý:** Thể hiện tình cảm và dòng chảy thời gian thông qua hành vi thực tế, cử chỉ đời thường và dấu vết biến chuyển trên các vật thể xung quanh.
5. **Bộ chuẩn hóa văn phong:** Áp dụng bắt buộc các nguyên lý từ [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md) và [`ref/banned_lyrics_motifs.md`](file:///Users/hoangkien/Youtube/coslient-free/ref/banned_lyrics_motifs.md) nhằm giữ trọn thanh âm mộc mạc và nhịp điệu chân thực của con người.

## Input / Output

- **Input:** `1-idea.md`, `ref/lyrics-index.md`, `ref/banned_lyrics_motifs.md`.
- **Output:**
  - `projects/XXX/2-music.md`: 2 track, mỗi track gồm tên bài, style prompt, exclude, lyrics có thẻ.
  - `track-N-<slug>/3-lyrics.txt`: lời sạch cho DistroKid.
  - Cập nhật `ref/lyrics-index.md`.

## Dự án & Kiến trúc thời lượng

- **Quy mô:** 2 bài / project, chung chủ đề và chung nền tảng âm nhạc.
- **Thời lượng mục tiêu:** Mỗi bài đạt từ 4 phút trở lên thông qua kiến trúc âm nhạc và các khoảng thở khí nhạc.
- **Khung cấu trúc chuẩn 4 phút+:** `Intro (nhạc dạo dài) -> Verse 1 -> Pre-Chorus -> Chorus -> Interlude -> Verse 2 -> Pre-Chorus -> Chorus -> Instrumental Solo -> Bridge (rút gọn nhạc cụ) -> Chorus -> Final Chorus -> Outro (kết gọn)`.

## Thể loại và giọng

- **Thể loại:** Nền Folk chủ đạo, kết hợp tối đa 1 nhánh phụ (Americana, country folk, chamber folk, Celtic, acoustic folk blues).
- **Nhánh Acoustic Blues:** Sử dụng kỹ thuật mộc (`acoustic`, Piedmont fingerpicking, slide, harmonica) ở giọng trưởng (major key) với nhịp điệu thong thả để bảo toàn cảm giác ấm áp ngay từ đầu bài.
- **Tempo:** 60 đến 95 BPM.
- **Giọng hát:** Nam trầm từng trải (`male baritone`), nữ mộc (`female alto`), hoặc song ca (`male and female duet`). Giọng hát giữ vị trí trung tâm, dàn nhạc cụ mộc đệm mở không gian cho lời.

## Style prompt

- **Độ dài và trọng tâm:** Viết thành đoạn văn mô tả bản thu tự nhiên dưới 100 từ. Đặt các thông tin định hình cốt lõi trong 20 từ đầu tiên.
- **Công thức thứ tự:**

```text
{Thể loại + nhánh lai}{, thập niên/vùng}. {Groove}, {BPM} BPM, {major/minor key}. {Nhạc cụ chính}, {nhạc cụ phụ}. {Chất giọng}, {cách hát}, clear diction. {Đường cảm xúc}. {Không gian thu âm}.
```

- **Tham số thành phần:**
  - Groove: Ghi rõ nhịp điệu và số chỉ nhịp nếu dùng nhịp 3/4 (`gentle 3/4 waltz`, `unhurried walking pocket`).
  - Đường cảm xúc: `Gentle verses swelling into a warm chorus` / `Hushed and soothing throughout` / `Stripped-back reflective storytelling, tender lifts`.
  - Không gian thu âm: Luân chuyển linh hoạt giữa các không gian mộc theo bối cảnh bài (`Warm analog tape room, dry acoustic space` / `Intimate living-room ribbon mic recording` / `Close-mic wood cabin acoustics, natural wooden room warmth`) để đa dạng hóa hạt giống giọng hát giữa các dự án.
- **Tính thống nhất trong project:** Hai bài trong cùng project dùng chung nền style prompt, chỉ điều chỉnh 1 đến 2 thông số (BPM, groove, đường cảm xúc) theo thời điểm câu chuyện.
- **Exclude:** Liệt kê 3 đến 5 thành phần âm thanh điện tử hoặc kỹ xảo cần loại trừ, ngăn cách bằng dấu phẩy. Khi loại trừ một nhạc cụ, nêu rõ nhạc cụ mộc đóng vai trò dẫn dắt trong style prompt.

```text
autotune, synths, electronic drums, vocal ad-libs, oohs
```

## Lời và Thẻ điều phối (Metatags)

- **Thẻ cấu trúc `[...]`:** Dùng cho chỉ dẫn sản xuất (`[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Interlude]`, `[Solo]`, `[Bridge]`, `[Final Chorus]`, `[Outro]`, `[Spoken]`, `[Whispered]`).
- **Cú pháp điều phối `[Section | chỉ dẫn]`:** Phần chỉ dẫn sau dấu `|` giới hạn tối đa 6 từ, chỉ nêu tên nhạc cụ và trạng thái âm lượng hoặc nhịp điệu.
- **Hát bè `(...)`:** Đặt phần lời hát phụ hoặc tiếng ngân bè trong ngoặc đơn.
- **Tương phản nhịp điệu (Prosodic Contrast):**
  - **Verse:** Giữ mật độ 6 đến 9 âm tiết mỗi dòng (độ lệch giữa các dòng trong cùng khổ tối đa 2 âm tiết) để tạo nhịp kể chuyện ổn định.
  - **Chorus & Hook:** Tạo độ bật giai điệu bằng cách co gọn dòng hook cuối (4 đến 6 âm tiết) hoặc mở rộng biên độ ngân. Ưu tiên kết thúc dòng hook bằng nguyên âm mở hoặc phụ âm vang (`-m, -n, -l, -r`).
- **Điểm mở và điểm kết:**
  - Câu đầu tiên của Verse 1 mở trực tiếp vào một câu thoại đời thường hoặc một hành động vật lý đang diễn ra.
  - Dòng cuối của Chorus chứa câu Hook chính ngắn gọn, cô đọng trọn ý.
  - Đoạn Outro thu gọn trong 1 đến 2 dòng lời thực tế để giữ nhịp nhạc ổn định đến giây cuối cùng.
- **Dấu câu:** Giữ dấu câu tự nhiên trong `2-music.md`. Viết toàn bộ con số thành chữ tiếng Anh chuẩn.

## 3-lyrics.txt (DistroKid)

- Chỉ giữ lại phần lời được hát thành tiếng.
- Viết hoa chữ cái đầu mỗi dòng.
- Để trống ký tự dấu câu ở cuối dòng.
- Ngăn cách giữa các khổ bằng đúng 1 dòng trống.

## Quản lý Catalog

- Đối chiếu `ref/lyrics-index.md` trước khi sáng tác để đảm bảo tính độc bản của câu Hook và đạo cụ trung tâm. Cập nhật đầy đủ cả 2 bài vào bảng index sau khi hoàn thành.

