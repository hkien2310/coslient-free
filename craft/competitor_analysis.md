# COMPETITOR ANALYSIS: GIẢI PHẪU NHẠC & HÌNH ẢNH VIRAL (`doi-thu/` & `phan-tich.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Quy định quy trình tự động chạy script kỹ thuật (`tools/analyze_audio.py`, `tools/analyze_motion.py`), nghe và giải phẫu các bài hát hoặc video viral của đối thủ để xuất báo cáo `projects/XXX/phan-tich.md`, làm đầu vào thực chứng cho Bước 1 (`1-idea.md`) và Bước 2 (`2-music.md`). Không sao chép lặp lại quy tắc viết lời của [`craft/music_craft.md`](./music_craft.md) hay quy tắc tạo hình của [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. **Ưu tiên dùng khẳng định hơn phủ định:** Hướng dẫn trực tiếp quy trình đo đạc, tiêu chí bóc tách và cách chuyển hóa sang định vị kênh bằng câu khẳng định rõ ràng.
>   2. **Luôn Rule hóa thông tin (`Rule-First`) & Hạn chế tối đa thiên kiến liệt kê:** Khái quát hóa thành quy tắc giải phẫu áp dụng cho mọi bài hát và video mẫu.
>   3. **Ưu tiên thêm mới và làm giàu quy tắc, bảo toàn dữ liệu:** Chỉnh sửa cục bộ đúng chỗ cần thiết (`/ponytail`, `/humanizer`).

---

## 1. Đầu Vào & Quy Trình Thực Thi Tự Động 100%

### 1.1. Đầu vào từ Người dùng
- Người dùng cung cấp **1 hoặc nhiều Link YouTube** (dán trực tiếp vào chat hoặc lưu trong file `.md`/`.txt`) hoặc bỏ các file nhạc/video viral (`.mp3`, `.wav`, `.m4a`, `.mp4`) vào `ref/doi-thu/`.
- Hỗ trợ 2 chế độ: **Chế độ Chỉ Phân tích Nhạc Hàng loạt (Multi-Link Audio Batch — mặc định khi ném nhiều link nhạc)** và **Chế độ Giải phẫu Toàn diện cả Nhạc & MV**.

### 1.2. Các bước AI tự động thực thi
1. **Tự động tải Audio, SEO & Phân chia Thư mục theo Kênh / Video (`analyze_audio.py`):**
   ```bash
   python3 tools/analyze_audio.py <url1> <url2> ... --out-dir ref/doi-thu
   ```
   - Script tự động lấy metadata từ YouTube và tạo cấu trúc thư mục chuẩn theo **Kênh $\rightarrow$ Tên Video $\rightarrow$ `raw/`**:
     ```text
     ref/doi-thu/
     └── <ten-kenh-slug>/
         └── <ten-video-slug>/
             ├── phan-tich.md               (Bản phân tích tổng hợp bằng AI dựa trên bộ dữ liệu raw)
             └── raw/
                 ├── seo.md & seo_meta.json (1. Thông tin SEO, sub, views, likes, tags, mô tả & top comments)
                 ├── audio.m4a              (2. File nhạc gốc tải về & audio_listen.mp3 để AI nghe)
                 └── audio_technical.md     (3. Thông số phân tích nhạc thuần kỹ thuật bằng code + .json)
     ```
2. **Tách cảnh & Cắt lưới hình ảnh 4K (Chỉ chạy khi người dùng yêu cầu phân tích cả hình ảnh/chuyển động MV):**
   ```bash
   python3 tools/analyze_motion.py ref/doi-thu/<ten-kenh-slug>/<ten-video-slug>
   ```
3. **Đọc chéo Cả 3 Nguồn Input & Xuất Báo cáo Giải phẫu Phản biện (`phan-tich.md`):**
   - Bắt buộc dùng công cụ `read_file` đọc đồng thời **cả 3 nguồn trong `raw/`**: (1) `raw/seo.md`, (2) `raw/audio_technical.md`, và (3) **nghe trực tiếp `raw/audio_listen.mp3`**.
   - Tổng hợp chéo dữ liệu kỹ thuật với âm thanh nghe thực tế và tâm lý khán giả trong bình luận; tuyệt đối không chỉ tóm tắt lại file raw mà phải phân tích nhân quả, chỉ ra cả điểm mạnh lẫn hạt sạn/lỗi của đối thủ (`Adversarial Critique`) vào `phan-tich.md` (và lập bảng xếp hạng `RANKING.md` khi phân tích hàng loạt).

---

## 2. Cấu Trúc Báo Cáo Giải Phẫu Chuyên Sâu (`phan-tich.md`)

### Tầng 1: Giải Phẫu Âm Thanh, Phối Khí & Kỹ Thuật DSP (Đối Chiếu `audio_technical.md` + Nghe Thực Tế `audio_listen.mp3`)
- **Bảng thông số kỹ thuật & Mastering (Đo bằng code) kèm giải mã thính giác thực tế:** Code (`ffmpeg ebur128` + `librosa`) chỉ đo các đại lượng vật lý cứng mà tai không tự định lượng được (`Thời lượng & Sub-tracks`, `BPM & Half-time`, `Beat Stability`, `Key chính/phụ & Dominant Notes`, `HPR Harmonic/Percussive %`, `Spectral Centroid & Rolloff`, `EBU R128 LUFS / LRA / True Peak`, `Crest Factor`, `Stereo Width & Correlation`, `Phân bổ 6 dải tần`). AI đối chiếu trực tiếp các con số này với **nhạc cụ và âm thanh thực tế nghe được trong `audio_listen.mp3`** (ví dụ: nhạc cụ nào tạo nên độ dày `Low-mid`, nhạc cụ nào được pan sang 2 kênh Stereo).
- **Giải phẫu Âm sắc, Hệ Nhạc cụ & Vũ đạo Giọng hát (AI nghe trực tiếp `audio_listen.mp3`):** Xác định thể loại chính, nhánh phụ, nghệ sĩ/thập niên tham chiếu; bóc tách từng lớp nhạc cụ xuất hiện theo mốc giây và các tiếng động hiện trường (`Diegetic Foley`); giải phẫu vũ đạo giọng hát (Nam/Nữ/Song ca đối đáp, màu giọng, kỹ thuật ngân `Humming` / huýt sáo / kể chuyện thì thầm, cách phối bè quãng 3/quãng 6 ở Chorus & Bridge).
- **Bảng Cấu trúc bài hát & Đường cong Năng lượng (`Song Structure & Energy Arc` — AI bấm giờ trực tiếp từ `audio_listen.mp3`):** Lập bảng chi tiết từng phân đoạn thực tế (`Intro -> Verse -> Pre-Chorus -> Chorus -> Instrumental Solo -> Bridge -> Outro`), ghi rõ sự thêm/bớt nhạc cụ và cơ chế giữ chân người nghe (`Retention Hook`) tại mỗi mốc.

### Tầng 2: Giải Phẫu Ca Từ, Cấu Trúc Lời & Kịch Bản Tự Sự (AI Nghe & Bóc Tách Trực Tiếp Từ `audio_listen.mp3`)
- **Lời bài hát đầy đủ theo phân đoạn (`Full Lyrics`):** Nghe trực tiếp `audio_listen.mp3` để chép chính xác 100% lời bài hát, chia rõ nhãn `[Intro]`, `[Verse]`, `[Chorus]`, `[Instrumental Solo]`, `[Bridge]`, `[Outro]` và nhãn giọng `[Male]` / `[Female]` / `[Duet]` kèm mô tả nhạc cụ trong ngoặc đơn.
- **Giải mã công thức ca từ & kịch bản:** Phân tích diễn tiến tự sự/lát cắt qua từng đoạn, hệ thống móc neo 5 giác quan (`Sensory Anchors`), sơ đồ vần, mật độ âm tiết, tốc độ nhả chữ (`WPM`), cấu trúc lặp của câu Hook điệp khúc và mổ xẻ 3 câu hát đắt giá nhất bài.

### Tầng 3: Giải Phẫu SEO, Tâm Lý Học Khán Giả & Phản Biện Đối Chứng (`seo.md` + `Adversarial Critique`)
- **Chiến thuật đóng gói SEO & Hiệu suất Viral:** Phân tích cấu trúc Title, Description, Tags và giải thích nguyên nhân đạt mức `Views/Subs` cùng `Like/View %` (so sánh chéo với các bài khác trong cùng kênh).
- **Tâm lý học khán giả qua Top Comments (`Voice of Customer`):** Bóc tách ký ức cá nhân, độ tuổi và chi tiết âm nhạc/ca từ mà khán giả nhắc tới trực tiếp trong bình luận.
- **Phản biện đối chứng (`Adversarial Critique — Điểm Mạnh vs Điểm Yếu / Hạt Sạn Của Đối Thủ`):** Chỉ ra thẳng những điểm yếu, hạt sạn trong bản thu/lời hát/SEO của đối thủ (câu chữ lặp AI, chuyển đoạn gãy, dải tần đục/gắt, kịch bản kéo dài gây loãng) để tránh lặp lại sai lầm của họ.

### Tầng 4: Bản Đồ Chuyển Hóa & Công Thức Nâng Cấp Sang Coslient Free
- **Bảng ánh xạ chuyển hóa (`Đối thủ -> Bản nâng cấp của Coslient Free`):** Kế thừa đòn bẩy cấu trúc (`BPM`, `Energy Arc`, `Phổ ấm <500Hz`, `Khoảng thở Solo`, `Móc neo giác quan`) và chuyển hóa hệ nhạc cụ về chuẩn Acoustic Folk / Americana cùng quy tắc mở đầu ấm áp (`Warm Start`).
- **Mẫu Suno Prompt & Khuôn mẫu Lời/Storyboard thực chiến rút ra từ bài mẫu.**
