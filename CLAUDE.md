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

## 2. WORKFLOW LÀM VIỆC (QUY TRÌNH MONTAGE 4 BƯỚC — PONYTAIL)
Mỗi project = 1 video hoàn chỉnh:

1. **Idea (`1-idea.md`):** Đúng 3 gạch đầu dòng: Không gian + Cảm xúc cốt lõi + 2–3 Móc neo giác quan đời thực (tuân thủ [`craft/idea_craft.md`](./craft/idea_craft.md)). Tuyệt đối không ép nhân vật cố định, không tạo gia phả hay kịch bản biến cố.
2. **Music (`2-music.md` & `3-lyrics.txt`):** Sáng tác bài hát Folk & xuất lời sạch DistroKid (tuân thủ [`craft/music_craft.md`](./craft/music_craft.md)).
   * *Bộ lọc Anti-Slop:* Diệt triệt để từ ngữ trừu tượng vô hồn, nhưng **tôn trọng cổ mẫu và móc neo giác quan đời thực**.
   * *Trích xuất mốc thời gian:* Sau khi có file audio `.wav` và `3-lyrics.txt`, chạy:
     `uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio.wav>`
     để sinh bộ file `timestamps.json`, `timestamps.txt`, `lyrics.srt` (chuẩn Zero-Gap, khớp từng câu hát).
3. **Visual Pool (`image.txt`):** 
   * **BẮT BUỘC ĐỌC TRƯỚC:** Rà soát ngay sổ tay bẫy từ khóa [`style/IMAGE_AVOID_CASES.md`](./style/IMAGE_AVOID_CASES.md) để tự động né 100% các từ cấm (búp bê khâu vá, người thật, len nỉ bao phủ, gỗ mục nát).
   * Dựa trên không gian ở `1-idea.md` và phong cách trong `style/`, viết trực tiếp danh sách prompt ảnh đa dạng (số lượng tự do theo bài hát) vào `image.txt` (tuân thủ [`craft/visual_craft.md`](./craft/visual_craft.md)).
   * Chạy tool tự động tải ảnh (`dola-auto-download`) về thư mục ảnh. Hoàn toàn không qua bảng storyboard trung gian.
4. **Montage & Animation (`prompt-animate.txt`):**
   * *Phòng dựng tự do (Montage):* Thả nhạc và kho ảnh vào timeline (Premiere/CapCut/DaVinci), ghép ảnh theo nhịp nhạc (`timestamps.txt`) bằng rung cảm trực tiếp. Tự do quyết định nhịp cắt và sự va chạm hình ảnh (juxtaposition).
   * *Chuyển động video:* Với các ảnh đã được chọn trên timeline, viết prompt chuyển động vào `prompt-animate.txt` (tuân thủ [`craft/animation_craft.md`](./craft/animation_craft.md)) để đưa vào tool render video.

---

## 3. QUY CHUẨN THƯ MỤC (`projects/XXX/` hoặc `projects-<tên>/XXX/`)
Chỉ chứa các file thực tế được tool và phòng dựng sử dụng. Tuyệt đối không tạo file trung gian thừa (`storyboard.md`, `character.txt`):

```text
projects/XXX/
├── 1-idea.md              (3 dòng không gian & cảm xúc)
├── 2-music.md             (Ý tưởng phối âm & Suno prompt)
├── 3-lyrics.txt           (Lời sạch DistroKid)
├── <audio>.wav            (File âm thanh master)
├── timestamps.json, timestamps.txt, lyrics.srt (Bộ mốc thời gian)
├── image.txt              (Kho prompts ảnh cho tool tải ảnh)
├── prompt-animate.txt     (Kho prompts chuyển động cho tool video)
├── 6-seo.md               (Tiêu đề, mô tả YouTube)
└── dola-auto-download/    (Thư mục ảnh tải về)
```

### 3.1 Quy chuẩn Dự án Đa bài (Multi-Track Projects):
Khi một Project phát triển từ **2 bài hát trở lên**:
* **Thư mục gốc `projects/XXX/`** chỉ lưu 2 file ý tưởng & âm nhạc chung: `1-idea.md` và `2-music.md`.
* **Mỗi track là một workspace con độc lập**:
  ```text
  projects/XXX/
  ├── 1-idea.md
  ├── 2-music.md
  ├── track-1-<tên_slug>/
  │   ├── <audio>.wav
  │   ├── timestamps.json, timestamps.txt, lyrics.srt
  │   ├── 3-lyrics.txt
  │   ├── image.txt          (prompts Midjourney riêng theo style)
  │   ├── prompt-animate.txt (prompts chuyển động riêng)
  │   └── 6-seo.md
  └── track-2-<tên_slug>/
      └── (đầy đủ bộ file chuẩn như trên)
  ```

---

## 4. NGUYÊN TẮC PONYTAIL (BẮT BUỘC)
Bắt buộc áp dụng tư duy [ponytail](file:///Users/hoangkien/.gemini/config/skills/ponytail/SKILL.md) xuyên suốt toàn bộ dự án:
* **YAGNI & Tối giản:** Không sinh thêm file, abstraction hay prompt thừa thãi. Giải pháp ít bước nhất, ngắn nhất là giải pháp thắng.
* **Dọn dẹp định kỳ:** Sử dụng `/ponytail-audit` và `/ponytail-review` để rà soát và triệt tiêu phình to dự án.

---

## 5. NGUYÊN TẮC TỰ PHẢN BIỆN & CHỐNG NỊNH BỢ (ADVERSARIAL VERIFIER - BẮT BUỘC)
Bắt buộc kích hoạt tư duy [`adversarial-verifier`](./.agents/skills/adversarial-verifier/SKILL.md) trên toàn bộ ý tưởng, lời nhạc, kho ảnh và kế hoạch:
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
