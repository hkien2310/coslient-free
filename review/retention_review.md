# Retention Review Gate (Bộ lọc kiểm toán giữ chân khán giả)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán độc lập chạy ngay sau khi dựng xong `character.md` và `storyboard.md` (trước khi xuất `image.txt`), dùng để đánh giá tiêu chuẩn `[FATAL]` / `[HIGH RISK]` về ý nghĩa hoạt động thực tế, tính đồng nhất của thế giới sa bàn thủ công trực quan, sự đối lập hình khối nhân vật 4 trục, nhịp điệu thị giác và tính nhất quán với Chế độ Kể chuyện đã chọn.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Góc Nhìn Khán Giả 45–85+ Xem Lần Lượt Từng Cảnh + Câu Hát (`audience-reviewer`)

- **Bạn đang đóng vai ai:** Một khán giả 45–85+ đang cầm điều khiển TV hoặc iPad xem và nghe MV từ giây `0:00` đến hết bài.
- **Cách duyệt bắt buộc — Đi lần lượt từng cặp `[Cảnh N + Câu hát/Nhạc N] -> [Cảnh N+1 + Câu hát/Nhạc N+1]` từ đầu đến cuối:**
  - Với mỗi bước chuyển cảnh nối tiếp nhau, đặt mình vào đúng trạng thái mắt đang nhìn hình ảnh đó và tai đang nghe câu hát đó để trả lời trực diện: **Liệu tôi còn ở lại xem tiếp sang cảnh sau không, hay bấm thoát? Và vì sao?**
  - **1. Tại Cảnh 1 $\to$ Cảnh 2 $\to$ Cảnh 3 (15 giây mở đầu):**
    - *Đang nhìn Cảnh 1 (kèm nhạc dạo/câu mở đầu) $\to$ sang Cảnh 2 $\to$ sang Cảnh 3:* Cảnh 1 có bắt mắt hoặc gây tò mò/khó hiểu (*"Ủa chuyện gì đang xảy ra thế?"*) không? Sang Cảnh 2 và 3, hình ảnh và âm nhạc có dẫn tôi đi sâu vào giải đáp sự tò mò đó không, hay đứng yên một chỗ làm tôi bấm thoát ngay?
  - **2. Tại từng chuỗi chuyển tiếp `[Cảnh N + Câu hát N] -> [Cảnh N+1 + Câu hát N+1]` xuyên suốt bài:**
    - Hình ảnh ở Cảnh $N$ có ăn khớp với cảm xúc/ý nghĩa của Câu hát $N$ đang vang lên không?
    - Khi cắt sang Cảnh $N+1$ và nghe Câu hát $N+1$, câu chuyện/hành động có tiến thêm một bước mới (Khởi phát $\to$ Tương tác $\to$ Kết quả) hoặc mở ra góc nhìn mới làm tôi muốn xem tiếp không?
    - **Chỉ đích danh mọi điểm gãy (`Drop-off`):** Bất kỳ đoạn nào mà từ Cảnh $N$ sang Cảnh $N+1, N+2$ lặp lại cùng một tư thế/hành động, hoặc hình ảnh trật nhịp với câu hát đang vang lên khiến người xem tụt cảm xúc và muốn bấm thoát.
  - **3. Tại đoạn chuyển sang Cao trào & Kết thúc (`Bridge -> Chorus cuối -> Outro`):**
    - Khi câu hát và âm nhạc đẩy lên đỉnh cảm xúc ở nửa cuối bài, hình ảnh chuyển sang cảnh đó có thực sự đắt giá, giải đáp trọn vẹn hành trình từ đầu bài và làm tôi xúc động muốn bấm Like trước khi lắng lại ở `Outro` không?

---

## 2. Nhập Vai Đạo Diễn Hình Ảnh, Dựng Phim & Kỹ Sư Prompt (`adversarial-reviewer`)

- **Bạn đang đóng vai ai:** Một Đạo diễn hình ảnh, Dựng phim kiêm Kỹ sư Prompt Stop-Motion. Bạn soi kịch bản và câu lệnh bằng con mắt nghề để bắt mọi lỗi trùng góc máy, đứt mạch dựng hoặc câu mô tả làm AI vẽ sai giải phẫu/tỷ lệ.
- **Câu hỏi phản biện chuyên môn & Kiểm tra đầu ra (`[FATAL]`):**
  - **Kỹ thuật đạo diễn & Nhịp dựng ($N \to N+1$):** *"Hai cảnh cắt nối sát nhau ($N \to N+1$) có tạo được độ tương phản rõ về cỡ cảnh, góc máy và bối cảnh không? Kịch bản đã chuyển hóa ý nghĩa câu hát thành tình huống có diễn biến thay vì minh họa chữ nghĩa máy móc chưa?"*
  - **Chặn bẫy lỗi AI (Giải phẫu, Tỷ lệ & Cấu trúc):** *"Cỡ cảnh đã khớp với không gian chưa (bán thân/trung cận khi có vách che phần dưới; toàn thân thấy đủ đến giày chạm sàn khi ở không gian mở)? Có câu mô tả nào dễ làm AI vẽ cụt chân, cắt xẻ xe cộ/nhà cửa hoặc làm phương tiện/nhà cửa bé như đồ chơi không?"*
  - **Kiểm tra chuẩn đầu ra:** `storyboard.md` và `image.txt` khớp 1:1 số dòng và mốc giờ với `timestamps.txt`; nhân vật trong `character.md` đồng nhất ngoại hình xuyên suốt; `image.txt` đúng chuẩn 4 khối tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md), sạch từ cấm tại [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5) và khóa cuối dòng bằng 1 nguồn sáng duy nhất (`--ar 16:9`).
