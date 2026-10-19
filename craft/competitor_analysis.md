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
- Người dùng cung cấp **1 hoặc nhiều Link YouTube** (dán trực tiếp vào chat hoặc lưu trong file `.md`/`.txt`) hoặc bỏ các file nhạc/video viral (`.mp3`, `.wav`, `.m4a`, `.mp4`) vào `projects/XXX/doi-thu/`.
- Hỗ trợ 2 chế độ: **Chế độ Chỉ Phân tích Nhạc Hàng loạt (Multi-Link Audio Batch — mặc định khi ném nhiều link nhạc)** và **Chế độ Giải phẫu Toàn diện cả Nhạc & MV**.

### 1.2. Các bước AI tự động thực thi
1. **Lưu dữ liệu đầu vào:** Tạo thư mục `projects/XXX/doi-thu/` và lưu danh sách link (kèm thông tin SEO/Comments nếu có) vào `projects/XXX/doi-thu/links.txt` (hoặc `seo.md`).
2. **Tự động tải Audio & Đo thông số kỹ thuật DSP hàng loạt (Bắt buộc cho mọi link/file nhạc):**
   ```bash
   python3 tools/analyze_audio.py projects/XXX/doi-thu
   ```
   - Script tự động quét toàn bộ link YouTube trong thư mục (hoặc nhận danh sách link truyền thẳng qua CLI `python3 tools/analyze_audio.py <url1> <url2> --out-dir projects/XXX/doi-thu`), tải luồng audio nhẹ kèm metadata (`title`, `channel`, `view_count`, `like_count`) và xuất báo cáo JSON tổng hợp cho tất cả các bài: `Duration`, `BPM` (`Half-time BPM`, `Beat Stability`), `Key & Scale`, `Crest Factor (Dynamic Range)`, `Tỷ lệ năng lượng 6 dải tần số`, `Energy Sections` và file `*_listen.mp3`.
3. **Tách cảnh & Cắt lưới hình ảnh 4K (Chỉ chạy khi người dùng yêu cầu phân tích cả hình ảnh/chuyển động MV):**
   ```bash
   python3 tools/analyze_motion.py projects/XXX/doi-thu
   ```
   - Xuất bộ **4K Shot Sheets** (`projects/XXX/doi-thu/shot_sheets/shots_*.jpg` — lưới `3x3 @ 1280x720`) và **4K Motion Grids** (`projects/XXX/doi-thu/grids/grid_*.jpg` — lưới `6x10 @ 4 FPS`) cùng `motion_metadata.json`.
4. **Nghe trực tiếp & So sánh mẫu số chung (Khi phân tích nhiều bài nhạc):**
   - Dùng công cụ đọc file mở trực tiếp các file `*_listen.mp3` để nghe màu giọng, cách nhả chữ, nhạc cụ dẫn dắt, vòng hòa thanh, cấu trúc câu Hook và khoảng thở solo; lập bảng so sánh ngang giữa các bài để tìm **Mẫu số chung ăn đề xuất (Viral Audio Denominator)**.
5. **Xuất Báo cáo Giải phẫu (`projects/XXX/doi-thu/phan-tich.md` hoặc `projects/XXX/phan-tich.md`):**
   - Tổng hợp kết quả (bỏ qua Tầng 3 nếu chỉ phân tích nhạc) và rút ra phương án chuyển hóa sang bản sắc Folk của kênh.

---

## 2. Cấu Trúc Báo Cáo Giải Phẫu (`projects/XXX/phan-tich.md`)

### Tầng 1: Âm Thanh & Kỹ Thuật DSP (Sound & DSP)
- **Bảng thông số kỹ thuật chuẩn:** Trình bày bảng gồm `Thời lượng`, `Tempo (BPM & Half-time)`, `Beat Stability`, `Key & Scale`, `Dynamic Range (Crest Factor)` và `Phân bổ năng lượng 6 dải tần`, kèm giải mã tác động thính giác đối với tệp người nghe 45–85+.
- **Giải phẫu Âm sắc, Nhạc cụ & Giọng hát:** Xác định thể loại chính, nhánh phụ, thập niên tham chiếu, bầu không khí cảm xúc, vai trò của từng lớp nhạc cụ (nhạc cụ dẫn dắt ở Intro/Solo, nhạc cụ giữ nhịp nền, lớp đệm chiều sâu) và màu giọng hát (vị trí thu mic, độ khàn/ấm, cách xử lý bè ở Chorus).
- **Cấu trúc bài hát & Đường cong Năng lượng (Energy Arc):** Lập bảng mốc thời gian từng phân đoạn (`Intro`, `Verse`, `Pre-Chorus`, `Chorus`, `Solo / Break`, `Bridge`, `Outro`) đối chiếu với `energy_score` và sự thay đổi phối khí (đặc biệt là các điểm rút nhạc cụ tạo khoảng thở).

### Tầng 2: Nội Dung Ca Từ & Công Thức Hook (Lyrical Formula)
- **Lời bài hát đầy đủ theo phân đoạn:** Chép lại lời bài hát kèm nhãn thời gian và chỉ dẫn nhạc cụ.
- **Giải mã công thức ca từ:** Xác định thông điệp cốt lõi, cấp độ từ vựng, cấu trúc câu Hook điệp khúc, mật độ âm tiết và cách bài mẫu giữ mạch cảm xúc thống nhất từ đầu đến cuối.

### Tầng 3: Hình Ảnh, Chuyển Động & Nhịp Dựng (Khi phân tích MV)
- **Phong cách mỹ thuật & Bảng màu:** Tạo hình nhân vật, chất liệu bề mặt và bảng màu chủ đạo.
- **Cấu trúc cảnh cắt & Nhóm bố cục lặp lại:** Tổng số cảnh (`shots`), độ dài trung bình mỗi cảnh và các nhóm cảnh chủ đạo (`Shot Archetypes`) được đan xen theo cấu trúc nhạc.

### Tầng 4: Tác Động Khán Giả, SEO & Phương Án Chuyển Hóa Sang Coslient Free
- **Bằng chứng khán giả & Công thức SEO:** Phân tích ngôn ngữ, trạng thái cảm xúc trong Top Comments và cấu trúc Title/Hashtags giúp video ăn đề xuất.
- **Bản đồ Chuyển hóa sang Coslient Free (`Adversarial Adaptation`):**
  1. **Giữ nguyên đòn bẩy cấu trúc:** Kế thừa chính xác `BPM`, `Đường cong năng lượng (Energy Arc)`, `Tỷ lệ dải tần ấm (Bass + Low-mid)`, `Khoảng thở Solo/Bridge` và `Độ thuần khiết của mạch lời` từ bài mẫu.
  2. **Chuyển hóa hệ nhạc cụ về chuẩn Folk của kênh:** Khi bài mẫu thuộc dòng nhạc ngoài Folk (như Electric Blues, Pop Ballad, Soft Rock, Jazz Soul), ánh xạ từng nhạc cụ dẫn dắt của bài mẫu sang nhạc cụ mộc tương đương trong hệ sinh thái Acoustic Folk / Americana của kênh (ví dụ: Guitar điện / Saxophone $\rightarrow$ Fingerpicked Acoustic Guitar, Slide Acoustic, Harmonica, Singing Fiddle, Cello, Mandolin, Upright Bass, Brushed Snare) và giữ quy tắc mở đầu ấm áp (`Warm Start`).
