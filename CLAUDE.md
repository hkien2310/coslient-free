# 🌿 COSLIENT FREE (V2 — KỶ NGUYÊN SỐNG ĐỘNG)

> 🔒 **PHÂN KỲ KHO DỮ LIỆU:**
> - **Coslient Video:** ĐÃ KHÓA (Season trước / Legacy archive).
> - **Coslient Free V1 (Projects 001–017):** ĐÃ KHÓA (giai đoạn cũ).
> - **Coslient Free V2 (Active):** Khởi động từ **Project 018** trở đi. Định hướng: Thế giới sống động, nhân vật sinh hoạt tự nhiên, chuyển động sinh học mượt mà (không stopmotion con rối).

## 1. ĐỊNH VỊ KÊNH
* **Khán giả mục tiêu:** Người nghe 45+, tìm kiếm sự bình yên trong tâm hồn.
* **Thể loại âm nhạc:** Folk là bắt buộc (Folk thuần mộc/acoustic, hoặc kết hợp linh hoạt 1 thể loại lai như Americana, Pop, Indie, Chamber... tùy ý tưởng từng bài, không bắt buộc phải lai).
* **Tinh thần:** Những câu chuyện nhỏ bé về con người và nơi chốn — ấm áp, tĩnh lặng, đôi khi ngọt đắng. Không giảng đạo, không drama.

---

## 2. WORKFLOW LÀM VIỆC (3 BƯỚC)
Mỗi project = 1 video hoàn chỉnh:

1. **Idea (`1-idea.md`):** Chủ đề cảm xúc cốt lõi, Send Test và hình ảnh gợi cảm xúc (tuân thủ [`craft/idea_craft.md`](./craft/idea_craft.md)). Tuyệt đối không vẽ trước kịch bản hay áp đặt đạo cụ gò bó.
2. **Music (`2-music.md` & `3-lyrics.txt`):** Sáng tác bài hát & xuất lời sạch DistroKid. Bắt buộc kích hoạt tư duy chống AI slop (`stop-slop`, `humanizer`, `avoid-ai-writing`), tuyệt đối không dùng sáo ngữ đao to búa lớn hay văn mẫu trị liệu tâm lý.
3. **Visual:**
   * `storyboard.md`: Chia bài hát thành shots 4–6s, mô tả cảnh gì tại mỗi thời điểm (tuân thủ [`craft/visual_craft.md`](./craft/visual_craft.md)).
   * `image.txt`: Từ storyboard, viết prompts ảnh cho từng shot (tuân thủ [`style/STYLE_handcrafted_tactile_diorama.md`](./style/STYLE_handcrafted_tactile_diorama.md)).
   * `animation.txt`: Từ ảnh thực tế đã tạo, viết prompt chuyển động riêng từng shot (tuân thủ [`craft/animation_craft.md`](./craft/animation_craft.md)).

---

## 3. QUY CHUẨN THƯ MỤC (`projects/XXX/` hoặc `projects-<tên>/XXX/`)
Chỉ chứa các file chuẩn trên + file `.wav` + thư mục `image/`. Tuyệt đối không lưu file rác/file nháp trung gian.

---

## 4. NGUYÊN TẮC PONYTAIL (BẮT BUỘC)
Bắt buộc áp dụng tư duy [ponytail](file:///Users/hoangkien/.gemini/config/skills/ponytail/SKILL.md) xuyên suốt toàn bộ dự án:
* **YAGNI & Tối giản:** Không sinh thêm file, abstraction hay prompt thừa thãi. Giải pháp ít bước nhất, ngắn nhất là giải pháp thắng.
* **Dọn dẹp định kỳ:** Sử dụng `/ponytail-audit` và `/ponytail-review` để rà soát và triệt tiêu phình to dự án.

---

## 5. QUY TẮC ĐA THÀNH VIÊN & NHÁNH GIT (BẮT ĐẦU PHIÊN)
Áp dụng ngay khi bắt đầu phiên làm việc:
1. **Kiểm tra file cấu hình local (`.current_member`):**
   - Đọc file `.current_member` ở thư mục gốc để lấy tên định danh.
   - Nếu file **chưa tồn tại** hoặc **rỗng**: AI mới hỏi *"Ai là người đang làm phiên này?"*, sau đó lưu tên vào `.current_member` (đã gitignore) để ghi nhớ cho các phiên sau.
2. **Tự động xử lý Git branch:**
   - Nếu là `master` hoặc `main`: Giữ nguyên nhánh chính.
   - Nếu là thành viên (vd: `khanh`): Nhánh quy chuẩn là `member-<tên>` (vd: `member-khanh`). Tự kiểm tra và checkout sang (hoặc tạo mới từ nhánh chính nếu chưa có). Thành viên không cần gõ lệnh Git.
3. **Cô lập thư mục dự án:**
   - Nhánh chính (`master`/`main`): Làm việc trong thư mục `projects/` gốc.
   - Thành viên (`member-<tên>`): Chỉ làm việc trong thư mục riêng `projects-<tên>/` (vd: `projects-khanh/001/`). Tuyệt đối không can thiệp hay sửa đổi trong `projects/` gốc hoặc thư mục của member khác.
