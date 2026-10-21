# 🌿 COSLIENT FREE (V2 — KỶ NGUYÊN SỐNG ĐỘNG)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & PHÂN KỲ KHO DỮ LIỆU (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của `CLAUDE.md`:** Là bản đồ điều phối trung tâm của dự án, quy định định vị kênh, trình tự các bước sản xuất, danh mục file chuẩn trong thư mục dự án và các nguyên tắc vận hành cốt lõi (`/ponytail`, `/humanizer`, `adversarial-verifier`, Git branch). Mọi quy tắc chuyên sâu của từng khâu đều nằm độc lập trong thư mục `craft/` và `style/`; file này chỉ điều hướng, không sao chép lặp lại quy tắc chi tiết của các file con.
> - **Phân kỳ kho dữ liệu:**
>   - **Coslient Video:** ĐÃ KHÓA (Season trước / Legacy archive).
>   - **Coslient Free V1 (Projects 001–017):** ĐÃ KHÓA (giai đoạn cũ).
>   - **Coslient Free V2 (Active):** Khởi động từ **Project 018** trở đi. Định hướng: Thế giới giàu chất thơ đời thường, nhân vật có hồn, bố cục điện ảnh thoáng rộng và chuyển động I2V tự nhiên mượt mà.

## 1. ĐỊNH VỊ KÊNH
* **Khán giả mục tiêu:** Người nghe 45–85+ (Trung niên & Cao tuổi, người tìm kiếm sự an ủi, hồi ức và chốn nương náu tâm hồn).
* **Hai tuyến nội dung chính:**
  1. *Soul Sanctuary (Chốn nương náu / Ru ngủ / An trú):* Phi kịch tính, xoa dịu nỗi đau, gợi ký ức đẹp, nhịp êm đềm.
  2. *Lived-in Character Story (Chuyện đời sống động):* Vết xước đời thường, chiêm nghiệm tuổi trung niên.
* **Thể loại âm nhạc:** Folk là bắt buộc (Folk thuần mộc/acoustic, hoặc kết hợp linh hoạt 1 thể loại lai như Americana, Country-Folk, Chamber... tùy ý tưởng từng bài).
* **Tinh thần:** Những khoảnh khắc nhỏ bé — ấm áp, tĩnh lặng, đôi khi ngọt đắng. Không giảng đạo, không drama gượng ép. *"Nhỏ" là cử chỉ/lát cắt, KHÔNG phải bối cảnh: không gian được phép rộng, ngoài trời, có gió, có đám đông (đồi, bến tàu, hội chợ, cánh đồng, sân ga...).*
* **Khởi động ấm áp (Warm Start Only — Bảo vệ Retention):** Tuyệt đối không mở đầu idea hay bài hát bằng bi kịch, than thở, chia ly, cãi vã hay không khí nặng nề để "cố tạo tương phản". 30 giây đầu tiên luôn đón người nghe bằng sự ấm áp, cảm giác an toàn hoặc một nụ cười/tò mò tích cực. Chiêm nghiệm sâu sắc hay vết xước cuộc đời chỉ được mở ra sau khi người nghe đã an lòng.

---

## 2. WORKFLOW LÀM VIỆC (QUY TRÌNH 6 BƯỚC — PONYTAIL)
Mỗi project = 1 hoặc 2 video hoàn chỉnh:

1. **Idea (`1-idea.md`):** **BẮT BUỘC ĐỌC TRƯỚC** [`craft/idea_craft.md`](./craft/idea_craft.md) và `1-idea.md` của 3 dự án liền kề. Viết đúng 4 gạch đầu dòng: Cảm xúc cốt lõi + Trục câu chuyện & Lát cắt (chốt rõ **Chế độ 1 — Kể chuyện Cá nhân** hoặc **Chế độ 2 — Ý niệm / Đa diện 100% Lát cắt**) + 2–3 Móc neo giác quan đời thực + Câu chốt (1 câu tiếng Việt gói trọn idea, kim chỉ nam cho mọi bước sau).
   * *Nghiên cứu ký ức thực tế (Tùy chọn `last30days`):* Khi làm chủ đề theo mùa/dịp lễ hoặc cần chất liệu mới, dùng `last30days` quét các cộng đồng người lớn tuổi để lấy kỷ niệm và chi tiết xúc giác đời thực.
   * *Giải phẫu Nhạc & Video Đối thủ (Tùy chọn `ref/doi-thu/`):* Khi cần phân tích bài hát hoặc MV viral của đối thủ trước khi lên Idea/Nhạc, chạy `tools/analyze_audio.py` và `tools/analyze_motion.py` để bóc tách 4 tầng dữ liệu vào `ref/doi-thu/<ten-kenh>/<ten-video>/phan-tich.md` theo quy chuẩn tại [`craft/competitor_analysis.md`](./craft/competitor_analysis.md).
2. **Music (`2-music.md` & `3-lyrics.txt`):** **BẮT BUỘC ĐỌC TRƯỚC** [`craft/music_craft.md`](./craft/music_craft.md), [`ref/lyrics-index.md`](./ref/lyrics-index.md) và [`ref/banned_lyrics_motifs.md`](./ref/banned_lyrics_motifs.md). Sáng tác bài hát Folk theo đúng Chế độ Kể chuyện đã chọn ở `1-idea.md` & xuất lời sạch DistroKid.
   * *Nguyên tắc Phân vai Nhạc & Hình:* Đặt tâm tình, tín hiệu gợi mở (Subtle Cues) và chiêm nghiệm có độ mở cao vào lời bài hát theo quy định của Chế độ 1 hoặc Chế độ 2 tại [`craft/music_craft.md`](./craft/music_craft.md); giao phần diễn giải trực diện hoạt cảnh và thao tác cụ thể cho bảng phân cảnh hình ảnh (`storyboard.md`).
   * *Trích xuất mốc thời gian & Nhịp Beat (Hybrid Vocal + Palmier Beat-Snap):* Sau khi có file audio `.wav` và `3-lyrics.txt`, gọi `import_media` + `detect_beats` qua MCP của **Palmier Pro** để lấy mảng `beats`/`downbeats`, sau đó chạy:
     `uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio.wav> --beats <beats.json>`
     để sinh bộ 3 file chuẩn Zero-Gap: `timestamps.json` và `timestamps.txt` (tự động chia các đoạn nhạc dạo dài thành các cảnh ~5s rơi đúng `downbeats` Beat 1 và hút nhẹ các điểm cắt cảnh có lời vào phách nhạc trong ngưỡng `±0.25s`) cùng `lyrics.srt` (giữ nguyên 100% mốc giọng hát gốc cho phụ đề).
3. **Characters & Storyboard (`character.md` & `storyboard.md`):** **BẮT BUỘC ĐỌC TRƯỚC** [`craft/visual_craft.md`](./craft/visual_craft.md), [`style/STYLE_mixed_media_tabletop_diorama.md`](./style/STYLE_mixed_media_tabletop_diorama.md), [`ref/banned_lyrics_motifs.md`](./ref/banned_lyrics_motifs.md) (Mục 5 — Cấm Đồ đồng, Đồ len, Đèn bão, Bánh răng) và kiểm toán đầu ra bằng [`craft/retention_review.md`](./craft/retention_review.md).
   * Lập file `character.md` theo đúng chế độ của bài hát (Chế độ 1: định nghĩa cụm nhận diện 4 trục vật lý cố định cho từng `@Tên_nhân_vật` kèm Prompt tạo hình gốc chuẩn Stop-Motion; Chế độ 2: ghi chú 100% lát cắt độc lập ở từng cảnh).
   * Dựa trên `1-idea.md`, `character.md` và `timestamps.txt`, lập bảng đạo diễn 4 cột bằng tiếng Việt trong `storyboard.md` (~5s/cảnh, khớp 1:1 với các dòng cảnh trong `timestamps.txt`). Áp dụng tỷ lệ **70% đời thường tối giản : 30% điểm nhấn dịch chuyển siêu thực đơn biến tại bối cảnh (4 chiều dịch chuyển không gian)**, tư thế phóng khoáng tự nhiên ở giây 0 (`t = 0s`), 1 nguồn sáng duy nhất, mái tóc dày kín đỉnh đầu và trán thấp, ma trận góc máy và quỹ đạo I2V trước khi xuất prompt tiếng Anh.
4. **Visual Prompts (`image.txt`):** **BẮT BUỘC ĐỌC TRƯỚC** file phong cách tương ứng trong `style/` (ví dụ [`style/STYLE_mixed_media_tabletop_diorama.md`](./style/STYLE_mixed_media_tabletop_diorama.md)), [`craft/visual_craft.md`](./craft/visual_craft.md) và [`ref/banned_lyrics_motifs.md`](./ref/banned_lyrics_motifs.md) (Mục 5).
   * Dịch 1:1 từng dòng đã duyệt trong `storyboard.md` sang câu lệnh tiếng Anh 4 khối trực quan (`65–85 từ/câu`, mở đầu bằng `Handcrafted stop-motion miniature diorama, clean natural [time-of-day] light, shallow depth of field.`) vào `image.txt` (Chế độ 1 điền cụm 4 trục vật lý cố định của `@Tên_nhân_vật` từ `character.md` kèm tư thế phóng khoáng tự nhiên ở từng cảnh; Chế độ 2 mô tả riêng từng nhân vật 4 trục trên nền phôi rối chung ở từng dòng).
   * Chạy tool tự động tải ảnh (`dola-auto-download`) về thư mục ảnh.
5. **Animation Prompts (`prompt-animate.txt`):** **BẮT BUỘC ĐỌC TRƯỚC** [`craft/animation_craft.md`](./craft/animation_craft.md).
   * Đọc trực tiếp câu prompt gốc của từng cảnh trong `image.txt` để xác định đúng chủ thể, tư thế đang diễn ra và đạo cụ/phương tiện đang trực tiếp thao tác, sau đó viết prompt chuyển động khớp 1:1 vào `prompt-animate.txt`.
6. **Palmier Pro Assembly & SEO Packaging (`6-seo.md`):** **BẮT BUỘC ĐỌC TRƯỚC** [`craft/coslient_seo.md`](./craft/coslient_seo.md).
   * *Dựng Timeline tự động qua Palmier Pro MCP:* Dùng bộ công cụ MCP (`import_media`, `add_clips`, `add_captions`, `manage_markers`, `manage_tracks`, `inspect_timeline`) để xếp nối tiếp toàn bộ video clips theo đúng khung frame của `timestamps.json` trên track `Main` (`includeAudio: false`), đồng bộ phụ đề từ `lyrics.srt` trên track `Captions` nằm trên cùng (`index: 0`), đặt nhạc nền gốc trên track `Music` và gắn Range Markers phân đoạn theo chương nhạc.
   * *Đóng gói siêu dữ liệu & 3 Prompt Thumbnail (`6-seo.md`):* Xuất đầy đủ tiêu đề, bộ 3 Prompt Thumbnail tiếng Anh chuyên biệt tối ưu CTR (để tạo ảnh và chọn lấy 1 tấm tốt nhất), mô tả, từ khóa, Shorts và phân phối Playlist/DistroKid theo mẫu tại [`craft/coslient_seo.md`](./craft/coslient_seo.md). Tùy chọn dùng `last30days` để tham khảo cấu trúc tiêu đề và từ khóa đang thu hút tương tác cao trong 30 ngày qua trên các kênh nhạc cùng ngách.

---

## 3. QUY CHUẨN THƯ MỤC (`projects/XXX/` hoặc `projects-<tên>/XXX/`)
Chỉ chứa các file thực tế được tool và phòng dựng sử dụng:

```text
projects/XXX/
├── 1-idea.md              (4 dòng: cảm xúc, trục câu chuyện/lát cắt [Chế độ 1 hoặc 2], móc neo & câu chốt)
├── 2-music.md             (Ý tưởng phối âm & Suno prompt)
├── 3-lyrics.txt           (Lời sạch DistroKid)
├── <audio>.wav            (File âm thanh master)
├── timestamps.json, timestamps.txt, lyrics.srt (Bộ mốc thời gian)
├── character.md           (Hồ sơ @Tên_nhân_vật cố định [Chế độ 1] hoặc Ghi chú 100% lát cắt độc lập [Chế độ 2])
├── storyboard.md          (Bảng phân cảnh tối giản 1 dòng/shot ~5s để duyệt trước)
├── image.txt              (Kho prompts ảnh phẳng khớp 1:1 với storyboard.md)
├── prompt-animate.txt     (Kho prompts chuyển động khớp 1:1 với image.txt)
├── 6-seo.md               (Tiêu đề, 3 prompts Thumbnail, mô tả & từ khóa YouTube)
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
  │   ├── character.md       (Hồ sơ nhân vật riêng của track theo Chế độ 1 hoặc Chế độ 2)
  │   ├── storyboard.md      (bảng phân cảnh tối giản riêng của track)
  │   ├── image.txt          (prompts ảnh phẳng riêng theo storyboard.md)
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

### 4.3. Quy tắc Chỉnh sửa Tài liệu Quy chuẩn Toàn Dự án (`Universal File Editing Rules`):
Mọi thao tác chỉnh sửa các file tài liệu trong `craft/`, `style/`, `CLAUDE.md` và `projects/` bắt buộc tuân thủ 5 nguyên tắc bất biến:
1. **Bảo toàn tuyệt đối mục `🔒 GHI CHÚ CỐ ĐỊNH` và ranh giới chức năng file:** Tuyệt đối không chỉnh sửa hoặc xóa khối `🔒 GHI CHÚ CỐ ĐỊNH` ở đầu mỗi file; giữ đúng chức năng độc lập của từng file, không sao chép chồng chéo quy tắc giữa các khâu.
2. **Chỉnh sửa cục bộ đúng chỗ (`Surgical Edit`), bảo toàn dữ liệu:** Luôn dùng công cụ chỉnh sửa cục bộ (`replace_file_content`) tại đúng dòng cần cập nhật; ưu tiên làm giàu và tinh chỉnh quy tắc, tuyệt đối không ghi đè toàn bộ file gây mất mát các quy tắc kỹ thuật, chất liệu và từ vựng cấu trúc đã đúc kết.
3. **Ưu tiên dùng câu khẳng định hơn câu phủ định (`Affirmative over Negative`):** Hướng dẫn trực tiếp những gì cần thiết kế, cần vẽ và cần đạt được bằng câu khẳng định rõ ràng. Chỉ liệt kê từ khóa cấm (`Hard Bans`) đối với các lỗi kỹ thuật đặc thù của AI không thể xử lý bằng cách khác.
4. **Luôn Rule hóa thông tin (`Rule-First`) & Hạn chế tối đa thiên kiến liệt kê:** Khái quát hóa mọi ý tưởng thành quy tắc chung hoạt động cho mọi video và mọi bối cảnh. Tránh liệt kê danh sách sự vật, đạo cụ, chủ đề hay sự kiện cụ thể trong tài liệu quy tắc để không tạo mồi nhử (`Use Case bias`) khiến AI lặp lại máy móc.
5. **Chạy Review Rule trước khi Commit & Tự động Commit ngay khi sửa Docs gốc (`Review-Before-Commit`):** Mỗi khi chỉnh sửa bất kỳ file tài liệu gốc nào của dự án (`CLAUDE.md`, `AGENTS.md`, `craft/*.md`, `style/*.md`), bắt buộc thực hiện ngay quy trình 2 bước:
   - **Bước 1 (Review Rule):** Kiểm tra lại toàn bộ `git diff` đối chiếu với 4 nguyên tắc trên và khối `🔒 GHI CHÚ CỐ ĐỊNH` của chính file đó (đảm bảo đã rút thành quy tắc chung `Rule-First`, không liệt kê `Use Case` gây thiên kiến, câu khẳng định ngắn gọn chuẩn `/ponytail` và `/humanizer`, không làm mất dữ liệu cũ). Nếu vi phạm phải sửa lại ngay.
   - **Bước 2 (Commit ngay kèm Ngày, Giờ và Nội dung chỉnh sửa):** Ngay sau khi vượt qua bước Review Rule, tự động thực thi `git commit` cho các file tài liệu gốc vừa sửa với commit message ghi rõ ngày, giờ và nội dung chỉnh sửa theo định dạng: `docs(<phạm-vi>): [YYYY-MM-DD HH:MM] <Tóm tắt nội dung chỉnh sửa>`.

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
