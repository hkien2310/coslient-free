# 🌿 COSLIENT FREE (V2 — KỶ NGUYÊN SỐNG ĐỘNG)

> 🔒 **PHÂN KỲ KHO DỮ LIỆU:**
> - **Coslient Video:** ĐÃ KHÓA (Season trước / Legacy archive).
> - **Coslient Free V1 (Projects 001–017):** ĐÃ KHÓA (giai đoạn cũ).
> - **Coslient Free V2 (Active):** Khởi động từ **Project 018** trở đi. Định hướng: Thế giới sống động, nhân vật sinh hoạt tự nhiên, chuyển động sinh học mượt mà (không stopmotion con rối).

## 1. ĐỊNH VỊ KÊNH
* **Khán giả mục tiêu:** Người nghe 45–85+ (Trung niên & Cao tuổi, người tìm kiếm sự an ủi, hồi ức và chốn nương náu tâm hồn).
* **Hai tuyến nội dung chính:**
  1. *Soul Sanctuary (Chốn nương náu / Ru ngủ / An trú):* Phi kịch tính, xoa dịu nỗi đau, gợi ký ức đẹp, nhịp êm đềm.
  2. *Lived-in Character Story (Chuyện đời sống động):* Vết xước đời thường, chiêm nghiệm tuổi trung niên.
* **Thể loại âm nhạc:** Folk là bắt buộc (Folk thuần mộc/acoustic, hoặc kết hợp linh hoạt 1 thể loại lai như Americana, Country-Folk, Chamber... tùy ý tưởng từng bài).
* **Tinh thần:** Những câu chuyện và không gian nhỏ bé — ấm áp, tĩnh lặng, đôi khi ngọt đắng. Không giảng đạo, không drama gượng ép.

---

## 2. WORKFLOW LÀM VIỆC (3 BƯỚC)
Mỗi project = 1 video hoàn chỉnh:

1. **Idea (`1-idea.md`):** Chọn tuyến (Soul Sanctuary hoặc Character Story), xác định cảm xúc cốt lõi, Send Test và móc neo giác quan (tuân thủ [`craft/idea_craft.md`](./craft/idea_craft.md)). Tuyệt đối không áp đặt đạo cụ gò bó hay vẽ trước storyboard.
2. **Music (`2-music.md` & `3-lyrics.txt`):** Sáng tác bài hát & xuất lời sạch DistroKid.
   * *Bộ lọc Anti-Slop tinh gọn:* Diệt triệt để từ ngữ đao to búa lớn vô hồn (`whispers, tapestry, celestial...`), nhưng **tôn trọng cổ mẫu (archetypes) và móc neo giác quan đời thực (sensory anchors)**. Không đem tiêu chuẩn văn học lý tính đi phán xét ca từ vỗ về cảm xúc.
   * *Trích xuất mốc thời gian:* Sau khi có file audio `.wav` và `3-lyrics.txt`, chạy:
     `uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio.wav>`
     để sinh bộ file `timestamps.json`, `timestamps.txt`, `lyrics.srt` (chuẩn Zero-Gap, tự động gộp theo từng câu trong `3-lyrics.txt`).
3. **Visual:**
   * Chọn phong cách thị giác trong `style/` và Chế độ thị giác trong [`craft/storyboard_craft.md`](./craft/storyboard_craft.md):
     - **Chế độ A — World Vignettes (Thế giới lát cắt):** Hoàn toàn KHÔNG cần tạo `character.txt`, nối cảnh bằng ánh sáng & không khí. Mặc định cho Soul Sanctuary / Nhạc an trú.
     - **Chế độ B — Single/Companion Journey:** Chuyện kể một người hoặc người và thú cưng. Khóa bằng mỏ neo trang phục mộc (áo len, góc sau lưng, đôi bàn tay), tạo `character.txt` nếu cần.
   * `storyboard.md`: Bảng phân cảnh tinh gọn theo [`craft/storyboard_craft.md`](./craft/storyboard_craft.md) (Cảnh này là gì, rộng/hẹp, tại sao, tác dụng gì, liên kết cảnh trước) chia theo nhịp retention ~5s.
   * `image.txt`: Viết prompts ảnh theo đúng quy chuẩn và cú pháp của style đã chọn.
   * `animation.txt`: Từ ảnh thực tế đã tạo, viết prompt chuyển động (tuân thủ [`craft/animation_craft.md`](./craft/animation_craft.md)).

---

## 3. QUY CHUẨN THƯ MỤC (`projects/XXX/` hoặc `projects-<tên>/XXX/`)
Chỉ chứa các file chuẩn trên + file `.wav` + thư mục `image/`. Tuyệt đối không lưu file rác/file nháp trung gian.

### 3.1 Quy chuẩn Dự án Đa bài (Multi-Track Projects):
Khi một Project phát triển từ **2 bài hát trở lên** (hai câu chuyện, hai tuyến nhân vật hoặc hai bản phối khác nhau):
* **Bắt buộc chia hẳn thành các thư mục con riêng biệt** theo định dạng:
  ```text
  projects/XXX/
  ├── 1-idea.md
  ├── 2-music.md
  ├── track-1-<tên_slug>/
  │   ├── <audio>.wav
  │   ├── timestamps.json, timestamps.txt, lyrics.srt
  │   ├── 3-lyrics.txt
  │   ├── storyboard.md  (khóa nhịp riêng 3–6s/shot, điểm ngọt 5s)
  │   ├── character.txt  (nếu style được chọn yêu cầu tạo nhân vật)
  │   ├── image.txt      (prompts Midjourney riêng theo style)
  │   └── animation.txt  (prompts chuyển động riêng)
  └── track-2-<tên_slug>/
      └── (đầy đủ bộ file chuẩn như trên)
  ```
* **Thư mục gốc `projects/XXX/`** chỉ lưu 2 file ý tưởng & âm nhạc chung: `1-idea.md` và `2-music.md`.
* **Mỗi track là một workspace độc lập**: Tên file bên trong giữ nguyên chuẩn (`storyboard.md`, `character.txt`, `image.txt`, `animation.txt`, `3-lyrics.txt`) để tương thích 100% với các tool tự động tải ảnh (`dola-auto-download`) và script render.

---

## 4. NGUYÊN TẮC PONYTAIL (BẮT BUỘC)
Bắt buộc áp dụng tư duy [ponytail](file:///Users/hoangkien/.gemini/config/skills/ponytail/SKILL.md) xuyên suốt toàn bộ dự án:
* **YAGNI & Tối giản:** Không sinh thêm file, abstraction hay prompt thừa thãi. Giải pháp ít bước nhất, ngắn nhất là giải pháp thắng.
* **Dọn dẹp định kỳ:** Sử dụng `/ponytail-audit` và `/ponytail-review` để rà soát và triệt tiêu phình to dự án.

---

## 5. NGUYÊN TẮC TỰ PHẢN BIỆN & CHỐNG NỊNH BỢ (ADVERSARIAL VERIFIER - BẮT BUỘC)
Bắt buộc kích hoạt tư duy [`adversarial-verifier`](./.agents/skills/adversarial-verifier/SKILL.md) trên toàn bộ ý tưởng, lời nhạc, storyboard và kế hoạch:
* **Tuyệt đối không nịnh bợ:** Không khen xã giao ("Tuyệt vời", "Ý tưởng hay"). Coi mọi đề xuất như một giả thuyết cần chứng minh độc lập.
* **Bóc trần tử huyệt:** Phân cấp rõ rủi ro (`[FATAL]` vs `[HIGH RISK]`), không giấu lỗi, không giới hạn số lượng lỗi nếu thực sự chí mạng.
* **Phân biệt Lỗi Kỹ Thuật (Bug) vs Đặc trưng Thể loại (Feature):** `[FATAL]` CHỈ dành cho lỗi gãy vỡ dữ liệu/logic (lệch timeline, hở gap, sai character bible, trùng catalog). Tuyệt đối KHÔNG gán `[FATAL]` cho sự lặp lại êm ái, nhịp chậm, hay chuỗi lát cắt đời sống (vignettes) vốn là đặc trưng của dòng nhạc/video an trú (Soul Sanctuary).
* **Chỉ đổi ý khi có dữ liệu mới:** Không nhượng bộ chỉ vì người dùng lặp lại ý kiến. Cửa thoát duy nhất: khi người dùng ra lệnh *"chỉ làm thôi"* / *"just execute"*.

---

## 6. QUY TẮC ĐA THÀNH VIÊN & NHÁNH GIT (BẮT ĐẦU PHIÊN)
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
