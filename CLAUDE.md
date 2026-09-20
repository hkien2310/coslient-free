# 🌿 COSLIENT FREE

## 1. ĐỊNH VỊ KÊNH
* **Khán giả mục tiêu:** Người nghe 45+, tìm kiếm sự bình yên trong tâm hồn.
* **Thể loại âm nhạc:** Folk là bắt buộc (Folk thuần mộc/acoustic, hoặc kết hợp linh hoạt 1 thể loại lai như Americana, Pop, Indie, Chamber... tùy ý tưởng từng bài, không bắt buộc phải lai).
* **Tinh thần:** Nếp sống bình dị, gắn kết lâu bền giữa con người và nơi chốn. Không drama, không trốn chạy.

---

## 2. WORKFLOW LÀM VIỆC (3 BƯỚC)
Mỗi project = 1 video hoàn chỉnh:

1. **Idea (`1-idea.md`):** Ý tưởng bối cảnh, nếp sống thường nhật và mỏ neo xúc giác.
2. **Music (`2-music.md` & `3-lyrics.txt`):** Sáng tác bài hát & xuất lời sạch DistroKid.
3. **Visual:**
   * `image.txt`: Prompts ảnh chia theo các đoạn nhạc (Intro, Verse, Chorus...).
   * `animation.txt` *(Optional)*: Prompt diễn hoạt video (ưu tiên dùng 1 universal prompt vi chuyển động cho toàn bộ clips).

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
