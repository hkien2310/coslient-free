# COMPETITOR ANALYSIS: GIẢI PHẪU NHẠC & HÌNH ẢNH VIRAL (`doi-thu/` & `phan-tich.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Quy định quy trình tự động chạy script kỹ thuật (`tools/analyze_audio.py`, `tools/analyze_motion.py`), nghe và giải phẫu các bài hát hoặc video viral của đối thủ để xuất báo cáo `projects/XXX/phan-tich.md`, làm đầu vào thực chứng cho Bước 1 (`1-idea.md`) và Bước 2 (`2-music.md`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu vào và quy trình thực thi tự động

### 1.1. Đầu vào từ người dùng
- Người dùng cung cấp đường dẫn YouTube hoặc đặt các file âm thanh/video vào thư mục đối thủ của dự án.
- Hỗ trợ 2 chế độ vận hành: **Chế độ phân tích âm thanh hàng loạt (`Multi-Link Audio Batch`)** và **Chế độ giải phẫu toàn diện cả âm thanh và hình ảnh MV**.

### 1.2. Các bước thực thi tự động
1. **Tải âm thanh, siêu dữ liệu SEO và phân chia thư mục theo kênh (`analyze_audio.py`):**
   ```bash
   python3 tools/analyze_audio.py <url1> <url2> ... --out-dir ref/doi-thu
   ```
   - Script tự động trích xuất siêu dữ liệu từ YouTube và khởi tạo cấu trúc thư mục chuẩn theo **Kênh $\rightarrow$ Tên Video $\rightarrow$ `raw/`**:
     ```text
     ref/doi-thu/
     └── <ten-kenh-slug>/
         └── <ten-video-slug>/
             ├── phan-tich.md               (Báo cáo giải phẫu chuyên sâu tổng hợp từ 3 nguồn raw)
             └── raw/
                 ├── seo.md & seo_meta.json (Siêu dữ liệu SEO, sub, views, likes, tags, mô tả & top comments)
                 ├── audio.m4a              (File nhạc gốc & audio_listen.mp3 để nghe trực tiếp)
                 └── audio_technical.md     (Thông số kỹ thuật âm thanh đo bằng code + .json)
     ```
2. **Tách cảnh và cắt lưới hình ảnh 4K (Khi phân tích hình ảnh và chuyển động MV):**
   ```bash
   python3 tools/analyze_motion.py ref/doi-thu/<ten-kenh-slug>/<ten-video-slug>
   ```
3. **Đọc chéo cả 3 nguồn dữ liệu và xuất báo cáo giải phẫu phản biện (`phan-tich.md`):**
   - Dùng công cụ `read_file` đọc đồng thời **cả 3 nguồn trong `raw/`**: (1) `raw/seo.md`, (2) `raw/audio_technical.md`, và (3) **nghe trực tiếp `raw/audio_listen.mp3`**.
   - Tổng hợp chéo dữ liệu kỹ thuật với âm thanh thực tế và tâm lý khán giả trong bình luận, phân tích rõ nguyên lý nhân-quả giúp tác phẩm thành công cùng các điểm giới hạn cần nâng cấp vào `phan-tich.md` (kèm bảng tổng hợp `RANKING.md` khi phân tích hàng loạt).

---

## 2. Cấu trúc báo cáo giải phẫu chuyên sâu (`phan-tich.md`)

### Tầng 1: Giải phẫu âm thanh, phối khí và kỹ thuật DSP
- **Bảng thông số kỹ thuật và giải mã thính giác thực tế:** Đối chiếu các đại lượng vật lý đo bằng code (`Thời lượng & Sub-tracks`, `BPM & Half-time`, `Beat Stability`, `Key & Dominant Notes`, `HPR Harmonic/Percussive %`, `Spectral Centroid & Rolloff`, `EBU R128 LUFS / LRA / True Peak`, `Crest Factor`, `Stereo Width & Correlation`, `Phân bổ 6 dải tần`) với **hệ nhạc cụ và âm sắc thực tế nghe được trong `audio_listen.mp3`**.
- **Giải phẫu âm sắc, hệ nhạc cụ và biên đạo giọng hát:** Xác định thể loại chính, nhánh phụ, thời kỳ tham chiếu; bóc tách từng lớp nhạc cụ xuất hiện theo mốc thời gian; giải phẫu màu giọng, kỹ thuật ngân giai điệu và cách hòa âm bè ở điệp khúc.
- **Bảng cấu trúc bài hát và đường cong năng lượng (`Song Structure & Energy Arc`):** Lập bảng chi tiết từng phân đoạn thực tế theo mốc thời gian, ghi rõ sự biến thiên lớp nhạc cụ và cơ chế giữ chân người nghe tại mỗi mốc.

### Tầng 2: Giải phẫu ca từ, cấu trúc lời và kịch bản tự sự
- **Lời bài hát đầy đủ theo phân đoạn (`Full Lyrics`):** Nghe trực tiếp `audio_listen.mp3` để hiệu đính chính xác toàn văn lời bài hát theo từng phân đoạn cấu trúc và phân vai giọng hát.
- **Giải mã công thức ca từ và kịch bản:** Phân tích diễn tiến tự sự qua từng khổ, hệ thống móc neo giác quan, sơ đồ vần, mật độ âm tiết, tốc độ nhả chữ (`WPM`), cấu trúc lặp của câu `Hook` điệp khúc và các câu hát trọng tâm.

### Tầng 3: Giải phẫu SEO, tâm lý học khán giả và phản biện đối chứng
- **Chiến thuật đóng gói SEO và hiệu suất lan tỏa:** Phân tích cấu trúc Title, Description, Tags và giải thích nguyên nhân đạt tỷ lệ `Views/Subs` cùng `Like/View %` trong tương quan với các video cùng kênh.
- **Tâm lý học khán giả qua bình luận thực tế (`Voice of Customer`):** Bóc tách ký ức cá nhân, độ tuổi và chi tiết âm nhạc hoặc hình ảnh mà khán giả nhắc tới trực tiếp trong bình luận.
- **Phản biện đối chứng (`Adversarial Critique`):** Đánh giá khách quan cả điểm mạnh cốt lõi lẫn những giới hạn về cấu trúc nhạc, lời hát, phối khí hoặc đóng gói SEO của đối thủ để xác lập phương án nâng cấp.

### Tầng 4: Bản đồ chuyển hóa và công thức nâng cấp sang Coslient Free
- **Bảng ánh xạ chuyển hóa (`Đối thủ -> Bản nâng cấp của Coslient Free`):** Kế thừa đòn bẩy cấu trúc (`BPM`, `Energy Arc`, `Phổ tần ấm`, `Khoảng thở khí nhạc`, `Móc neo giác quan`) và chuyển hóa về chuẩn âm nhạc Acoustic Folk cùng mỹ học hoạt hình Stop-Motion của kênh.
- **Đúc kết nguyên lý phối khí, cấu trúc lời và nhịp điệu đạo diễn rút ra từ bài mẫu.**
