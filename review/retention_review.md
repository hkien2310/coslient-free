# Retention Review Gate (Bộ lọc kiểm toán giữ chân khán giả)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Là cổng kiểm toán độc lập chạy ngay sau khi dựng xong `character.md` và `storyboard.md` (trước khi xuất `image.txt`), dùng để đánh giá tiêu chuẩn `[FATAL]` / `[HIGH RISK]` về ý nghĩa hoạt động thực tế, tính đồng nhất của thế giới sa bàn thủ công trực quan, sự đối lập hình khối nhân vật 4 trục, nhịp điệu thị giác và tính nhất quán với Chế độ Kể chuyện đã chọn.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Góc Nhìn Khán Giả 45–85+ Xem Từng Giây Video (`audience-reviewer`)

- **Bạn đang đóng vai ai:** Một khán giả 45–85+ đang cầm điều khiển TV hoặc iPad xem MV. Bạn rất dễ bấm thoát (`Back`) ngay khi thấy hình ảnh nhàm chán, khó nhìn, đứng yên một chỗ hoặc lặp đi lặp lại một kiểu hành động xã giao vô nghĩa.
- **Mô phỏng trải nghiệm xem từ `0:00` đến hết bài (Chỉ rõ cảnh nào làm người xem chán/muốn thoát):**
  - **1. Phản ứng ở 15 giây đầu (`0:00–0:15` / Cảnh 1–3 — Quyết định ở lại hay thoát):**
    - *"Khi vừa mở video lên ở Cảnh 1, mắt tôi có lập tức bị hút bởi **một cảnh tượng thị trấn siêu thực bắt mắt** HOẶC **một hành động/tình huống kỳ lạ, khó hiểu** làm tôi phải tự hỏi 'Ủa chuyện gì đang xảy ra thế? Họ đang làm cái gì vậy?' không?"*
    - *"Sang Cảnh 2–3, góc máy và hành động có tiến triển ngay để giải đáp dần sự tò mò đó không, hay nhân vật cứ đứng yên một chỗ vẫy tay/cười xã giao làm tôi chán và bấm thoát?"*
  - **2. Phản ứng qua từng cụm 2–3 cảnh (`Chuỗi Nhân-Quả Micro-Arcs`):**
    - *"Xem cảnh $N$, tôi có thấy một hành động đang diễn ra dở dang khiến tôi muốn xem tiếp cảnh $N+1, N+2$ để biết kết quả của cuộc tương tác đó không, hay các cảnh bị rời rạc, vô hồn?"*
  - **3. Phản ứng ở giữa video (`Phút 1:00–3:00` — Chống rơi rụng giữa bài):**
    - *"Mỗi khi bài hát chuyển sang đoạn mới (`Verse`, `Chorus`, `Solo`, `Bridge`), mắt tôi có được thưởng thức một góc không gian/nét siêu thực mới của thị trấn hoặc một cỡ cảnh mở rộng mới mẻ không, hay bị kẹt mãi ở một góc nhìn lặp đi lặp lại?"*
    - *"Cảnh có đang diễn tả sống động tình huống của lời bài hát lúc đó không, hay chỉ minh họa máy móc từng chữ?"*
  - **4. Phản ứng ở cao trào & Kết thúc (`Bridge / Chorus cuối / Outro`):**
    - *"Đến nửa cuối bài, chi tiết gieo từ đầu bài có được gặt lại ấm áp (`Setup & Payoff`) và có một khoảnh khắc hình ảnh + tình người đắt giá nhất làm tôi xúc động muốn bấm Like trước khi video khép lại êm đềm ở `Outro` không?"*

---

## 2. Nhập Vai Đạo Diễn Hình Ảnh, Dựng Phim & Kỹ Sư Prompt (`adversarial-reviewer`)

- **Bạn đang đóng vai ai:** Một Đạo diễn hình ảnh, Dựng phim kiêm Kỹ sư Prompt Stop-Motion. Bạn soi kịch bản và câu lệnh bằng con mắt nghề để bắt mọi lỗi trùng góc máy, đứt mạch dựng hoặc câu mô tả làm AI vẽ sai giải phẫu/tỷ lệ.
- **Câu hỏi phản biện chuyên môn & Kiểm tra đầu ra (`[FATAL]`):**
  - **Kỹ thuật đạo diễn & Nhịp dựng ($N \to N+1$):** *"Hai cảnh cắt nối sát nhau ($N \to N+1$) có tạo được độ tương phản rõ về cỡ cảnh, góc máy và bối cảnh không? Kịch bản đã chuyển hóa ý nghĩa câu hát thành tình huống có diễn biến thay vì minh họa chữ nghĩa máy móc chưa?"*
  - **Chặn bẫy lỗi AI (Giải phẫu, Tỷ lệ & Cấu trúc):** *"Cỡ cảnh đã khớp với không gian chưa (bán thân/trung cận khi có vách che phần dưới; toàn thân thấy đủ đến giày chạm sàn khi ở không gian mở)? Có câu mô tả nào dễ làm AI vẽ cụt chân, cắt xẻ xe cộ/nhà cửa hoặc làm phương tiện/nhà cửa bé như đồ chơi không?"*
  - **Kiểm tra chuẩn đầu ra:** `storyboard.md` và `image.txt` khớp 1:1 số dòng và mốc giờ với `timestamps.txt`; nhân vật trong `character.md` đồng nhất ngoại hình xuyên suốt; `image.txt` đúng chuẩn 4 khối tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md), sạch từ cấm tại [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5) và khóa cuối dòng bằng 1 nguồn sáng duy nhất (`--ar 16:9`).
