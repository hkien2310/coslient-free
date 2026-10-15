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
* **Tinh thần:** Những khoảnh khắc nhỏ bé — ấm áp, tĩnh lặng, đôi khi ngọt đắng. Không giảng đạo, không drama gượng ép. *"Nhỏ" là cử chỉ/lát cắt, KHÔNG phải bối cảnh: không gian được phép rộng, ngoài trời, có gió, có đám đông (đồi, bến tàu, hội chợ, cánh đồng, sân ga...).*
* **Khởi động ấm áp (Warm Start Only — Bảo vệ Retention):** Tuyệt đối không mở đầu idea hay bài hát bằng bi kịch, than thở, chia ly, cãi vã hay không khí nặng nề để "cố tạo tương phản". 30 giây đầu tiên luôn đón người nghe bằng sự ấm áp, cảm giác an toàn hoặc một nụ cười/tò mò tích cực. Chiêm nghiệm sâu sắc hay vết xước cuộc đời chỉ được mở ra sau khi người nghe đã an lòng.

---

## 2. WORKFLOW LÀM VIỆC (QUY TRÌNH MONTAGE 4 BƯỚC — PONYTAIL)
Mỗi project = 1 video hoàn chỉnh:

1. **Idea (`1-idea.md`):** Đúng 4 gạch đầu dòng: Cảm xúc cốt lõi + Câu chuyện & Lát cắt + 2–3 Móc neo giác quan đời thực + Câu chốt (1 câu tiếng Việt gói trọn idea, kim chỉ nam cho mọi bước sau) (tuân thủ [`craft/idea_craft.md`](./craft/idea_craft.md)).
2. **Music (`2-music.md` & `3-lyrics.txt`):** Sáng tác bài hát Folk & xuất lời sạch DistroKid (tuân thủ [`craft/music_craft.md`](./craft/music_craft.md)).
   * *Bộ lọc Anti-Slop:* Diệt triệt để từ ngữ trừu tượng vô hồn, nhưng **tôn trọng cổ mẫu và móc neo giác quan đời thực**.
   * *Trích xuất mốc thời gian:* Sau khi có file audio `.wav` và `3-lyrics.txt`, chạy:
     `uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio.wav>`
     để sinh bộ file `timestamps.json`, `timestamps.txt`, `lyrics.srt` (chuẩn Zero-Gap, khớp từng câu hát).
3. **Visual Pool (`image-index.md` & `image.json`):** 
   * **BẮT BUỘC ĐỌC TRƯỚC:** Rà soát [`ref/image-index.md`](./ref/image-index.md), file `image-index.md` của track hiện tại (nếu đang viết tiếp batch) và file phong cách tương ứng trong `style/` (ví dụ [`style/STYLE_mixed_media_tabletop_diorama.md`](./style/STYLE_mixed_media_tabletop_diorama.md)).
   * Dựa trên mạch cảm xúc ở `1-idea.md` cùng phong cách trong `style/`, viết danh sách prompt ảnh độc lập vào `image.json` (tuân thủ [`craft/visual_craft.md`](./craft/visual_craft.md)), đồng thời **cập nhật song song vào `image-index.md` (1 dòng tóm tắt / 1 cảnh: `ID | Cỡ cảnh & Không gian/Thời gian | Bảng màu (70% Nền - 10% Điểm nổ) | Nhân vật & Tương phản hình khối | Ý niệm Thơ ca (Focal Twist) & Chuyển động bắt dính`)** để kiểm soát độ đẹp và sự đa dạng liên tục mà không cần đọc lại hàng nghìn dòng JSON.
   * Chạy tool tự động tải ảnh (`dola-auto-download`) về thư mục ảnh.
4. **Montage & Animation (`prompt-animate.txt`):**
   * *Phòng dựng tự do (Montage):* Thả nhạc và kho ảnh vào timeline (Premiere/CapCut/DaVinci), ghép ảnh theo nhịp nhạc (`timestamps.txt`) bằng rung cảm trực tiếp. Tự do quyết định nhịp cắt và sự va chạm hình ảnh (juxtaposition).
   * *Chuyển động video:* Với các ảnh đã được chọn trên timeline, tra cứu `image-index.md` và viết prompt chuyển động vào `prompt-animate.txt` (tuân thủ [`craft/animation_craft.md`](./craft/animation_craft.md)) để đưa vào tool render video.

---

## 3. QUY CHUẨN THƯ MỤC (`projects/XXX/` hoặc `projects-<tên>/XXX/`)
Chỉ chứa các file thực tế được tool và phòng dựng sử dụng:

```text
projects/XXX/
├── 1-idea.md              (4 dòng cảm xúc, câu chuyện lát cắt, móc neo & câu chốt)
├── 2-music.md             (Ý tưởng phối âm & Suno prompt)
├── 3-lyrics.txt           (Lời sạch DistroKid)
├── <audio>.wav            (File âm thanh master)
├── timestamps.json, timestamps.txt, lyrics.srt (Bộ mốc thời gian)
├── image-index.md         (Bản đồ tóm tắt 1 dòng/cảnh để kiểm soát đa dạng & tra cứu nhanh)
├── image.json             (Kho prompts ảnh JSON độc lập)
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
  │   ├── image-index.md     (bản đồ tóm tắt 1 dòng/cảnh của track)
  │   ├── image.json         (prompts ảnh JSON riêng theo style)
  │   ├── prompt-animate.txt (prompts chuyển động riêng)
  │   └── 6-seo.md
  └── track-2-<tên_slug>/
      └── (đầy đủ bộ file chuẩn như trên)
  ```

---

## 4. NGUYÊN TẮC PONYTAIL & HUMANIZER (BẮT BUỘC TOÀN DỰ ÁN)
Bắt buộc kích hoạt và tuân thủ 2 kỹ năng cốt lõi trên mọi tác vụ:

### 4.1. Ponytail (`/ponytail` — Lazy Senior Dev Mode):
Áp dụng tư duy [ponytail](file:///Users/hoangkien/.gemini/config/skills/ponytail/SKILL.md) trên toàn bộ code, script, cấu trúc thư mục, quy trình và prompt:
* **YAGNI & Tối giản tuyệt đối:** Không sinh thêm file, abstraction hay prompt thừa thãi. Giải pháp ít bước nhất, ít file nhất, diff ngắn nhất là giải pháp thắng.
* **Xóa bỏ thay vì thêm mới:** Boring over clever, deletion over addition.
* **Dọn dẹp định kỳ:** Sử dụng `/ponytail-audit` và `/ponytail-review` để rà soát và triệt tiêu phình to dự án.

### 4.2. Humanizer (`/humanizer` — Diệt Triệt Để Văn Phong AI):
Áp dụng tư duy [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md) trên toàn bộ văn bản (ý tưởng, tài liệu, kịch bản, lời bài hát, mô tả SEO, câu trả lời):
* **Xóa bỏ 25 dấu hiệu AI (AI tells):** Không dùng cấu trúc tương phản sáo rỗng (*not X but Y*), không dùng câu chốt đao to búa lớn một dòng, không dùng bộ 3 ép buộc (*forced triads*), không lạm dụng dấu gạch ngang (—), không dùng văn phong bán hàng/quảng cáo.
* **Diệt danh sách từ AI slop:** Cấm tuyệt đối các từ trừu tượng vô hồn (`tapestry`, `whispers`, `testament`, `vibrant`, `beacon`, `interplay`, `delve`, `landscape`...).
* **Giọng văn con người:** Luôn neo vào giác quan vật lý có thật, câu từ tự nhiên, có nhịp thở, độ dài câu luân chuyển tự nhiên như người thật trò chuyện.

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
