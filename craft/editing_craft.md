# Editing Craft: Kỹ thuật Dựng Timeline, Đồng bộ Nhịp Beat và Hòa âm Môi trường (Palmier Pro)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ bộ mốc thời gian (`timestamps.json`, `lyrics.srt`), file nhạc gốc (`.wav`) và thư mục video đã kết xuất để lắp ráp timeline hoàn chỉnh trên **Palmier Pro** thông qua MCP. File này quy định cấu trúc phân lớp track, quy trình khóa điểm cắt theo phách nhạc (`Beat-Synced Cutting`), quy trình kiểm duyệt và pha trộn âm thanh môi trường gốc từ video (`Source Ambient Audio Mixing`), cùng hệ thống đánh dấu phân đoạn (`Timeline Markers`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Kiến trúc Phân lớp 4 Track trên Palmier Pro (`Four-Track Hierarchy`)

Mọi timeline dự án trên Palmier Pro được thiết lập ở tốc độ khung hình cố định (`30fps`) và sắp xếp theo trật tự 4 lớp từ trên xuống dưới:

1. **Track `V2` (`index: 0` — `Captions`):** Nằm ở tầng trên cùng, chứa toàn bộ chuỗi phụ đề từ `lyrics.srt` đồng bộ chính xác với thời điểm cất giọng hát. Thiết lập phông chữ rõ nét, cỡ chữ vừa vặn ở cạnh dưới khung hình để khán giả lớn tuổi dễ đọc và thưởng thức trọn vẹn bối cảnh.
2. **Track `V1` (`index: 1` — `Main`):** Chứa chuỗi các video clip (`STT_001` đến `STT_N`) xếp nối tiếp liên tục (`Zero-Gap`) từ khung hình `0` đến khung hình kết thúc của bản nhạc.
3. **Track `A1` (`index: 2` — `Ambience`):** Chứa các clip âm thanh gốc đi kèm (`linked audio`) của những video clip trên track `Main` đã vượt qua bước kiểm duyệt âm thanh môi trường, giúp bổ sung hơi thở không gian tự nhiên vào bản dựng.
4. **Track `A2` (`index: 3` — `Music`):** Chứa file âm thanh master (`.wav`) giữ nguyên mức âm lượng chuẩn (`0dB`), đóng vai trò trục xương sống dẫn dắt toàn bộ nhịp điệu và cảm xúc của tác phẩm.

---

## 2. Đồng bộ Điểm cắt vào Phách nhạc và Đánh dấu Cấu trúc (`Beat-Synced Cutting & Structural Markers`)

1. **Trích xuất lưới nhịp phách (`On-Device Beat Detection`):**
   - Ngay khi đưa file nhạc master vào dự án, chạy công cụ `detect_beats` của Palmier Pro trên file nhạc gốc để trích xuất toàn bộ danh sách phách mạnh đầu ô nhịp (`downbeats` — Beat 1), phách thường (`beats`) và chỉ số nhịp độ (`BPM`).
2. **Khóa điểm chuyển cảnh vào phách nhạc (`Beat-Snapped Cut Alignment`):**
   - Các đoạn nhạc dạo (`Intro`, `Interlude / Solo`, `Outro`) được chia thành các cảnh đều đặn rơi chính xác vào phách mạnh đầu ô nhịp (`downbeats`).
   - Điểm chuyển cảnh giữa các câu hát được hút về phách mạnh (`downbeat`) hoặc phách chuẩn (`beat`) gần nhất trong ngưỡng dung sai `±0.25 giây` (thông qua `tools/extract_timestamps.py --beats`) để mỗi cú chuyển hình đều khớp nhịp trống và nhịp gảy đàn mà vẫn giữ nguyên vẹn câu chữ phụ đề trên track `Captions`.
3. **Hệ thống Điểm đánh dấu phân đoạn và nhịp chủ đạo (`Section & Downbeat Markers`):**
   - Sử dụng `manage_markers` để gắn các điểm đánh dấu vùng (`Range Markers`) phân định rõ từng chương nhạc (`Intro`, `Verse`, `Chorus`, `Solo`, `Bridge`, `Outro`) cùng các điểm nhấn phách mạnh quan trọng trên trục thời gian, giúp kiểm soát trực quan nhịp thở và cấu trúc cao trào của toàn bộ bản dựng.

---

## 3. Kiểm duyệt và Pha trộn Âm thanh Môi trường Gốc (`Source Ambient Audio Auditing & Mixing`)

Từng video clip đưa lên timeline đều đi qua quy trình lọc và cân chỉnh âm lượng 3 bước để giữ lại tiếng động thiên nhiên chân thực trong khi bảo vệ trọn vẹn khoảng thở của bản nhạc:

1. **Bước 1 — Đặt toàn bộ clip kèm âm thanh lên Timeline và Quét lời thoại (`Batch Placement & Transcript Scan`):**
   - Đặt các video clip lên track `V1` với `includeAudio: true` để các kênh âm thanh gốc nằm trên track `A1` (`Ambience`).
   - Chạy công cụ `get_transcript` của Palmier Pro riêng trên track `A1` (`trackIndex` của track `Ambience`) để phát hiện toàn bộ các clip có chứa giọng nói, tiếng hát nhại hoặc âm절 lạ do mô hình tạo video tự sinh ra.
2. **Bước 2 — Phân loại, Lọc sạch và Cân chỉnh Âm lượng Nền (`Selective Muting & Subtle Ambient Bed`):**
   - **Với các clip chỉ chứa âm thanh môi trường tự nhiên của cảnh vật:** Giữ lại kênh âm thanh trên track `Ambience` và dùng `set_clip_properties` hạ âm lượng (`volumeDb`) xuống mức nền thật khẽ từ **`-24dB` đến `-28dB`**, đồng thời đặt độ mượt chuyển âm ở hai đầu clip (`fadeInFrames: 5`, `fadeOutFrames: 5`, `fadeInInterpolation: "smooth"`, `fadeOutInterpolation: "smooth"`). Mức âm lượng này tạo lớp không gian sống động phảng phất phía sau và dành trọn khoảng thở trong trẻo cho giọng hát cùng nhạc cụ mộc ở track `Music` (`0dB`).
   - **Với các clip xuất hiện từ ngữ/giọng nói trong kết quả `get_transcript` hoặc âm thanh cơ học:** Dùng `set_clip_properties` đưa âm lượng của clip âm thanh tương ứng về mức tĩnh lặng hoàn toàn (`volumeDb: -60`).
3. **Bước 3 — Ghi Nhật ký Kiểm duyệt Âm thanh (`Ambient Audio Audit Log`):**
   - Sau khi hoàn tất pha trộn trên timeline, lưu lại danh sách đối soát ngắn gọn trong báo cáo dựng phim: ghi rõ những cảnh nào giữ âm thanh môi trường (kèm mức `dB`) và những cảnh nào đưa về mức tĩnh lặng (`-60dB` kèm lý do phát hiện giọng nói) để dễ dàng kiểm tra khi xem duyệt.
