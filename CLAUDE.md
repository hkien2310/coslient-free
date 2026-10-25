# 🌿 COSLIENT FREE (V2 — KỶ NGUYÊN SỐNG ĐỘNG)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & PHÂN KỲ KHO DỮ LIỆU (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của `CLAUDE.md`:** Là bản đồ điều phối trung tâm của dự án, quy định định vị kênh, trình tự các bước sản xuất, danh mục file chuẩn trong thư mục dự án và các nguyên tắc vận hành cốt lõi (`/ponytail`, `/humanizer`, `adversarial-verifier`, Git branch). Mọi quy tắc chuyên sâu của từng khâu đều nằm độc lập trong thư mục `craft/` và `style/`; file này chỉ điều hướng, không sao chép lặp lại quy tắc chi tiết của các file con.
> - **Phân kỳ kho dữ liệu:**
>   - **Coslient Video:** ĐÃ KHÓA (Season trước / Legacy archive).
>   - **Coslient Free V1 (Projects 001–017):** ĐÃ KHÓA (giai đoạn cũ).
>   - **Coslient Free V2 (Active):** Khởi động từ **Project 018** trở đi. Định hướng: Thế giới giàu chất thơ đời thường, nhân vật có hồn, bố cục điện ảnh thoáng rộng và chuyển động I2V tự nhiên mượt mà.

## 1. QUY TRÌNH 6 BƯỚC (CHỈ ĐIỀU HƯỚNG FILE)

> **Nguyên tắc một chiều bất biến:** Mỗi bước chỉ đọc đầu ra đã duyệt của các bước trước làm dữ liệu đầu vào cố định và chỉ tạo/cập nhật các file thuộc phạm vi của bước hiện tại.

1. **Bước 1 — Idea (`1-idea.md`):** Đọc [`craft/idea_craft.md`](./craft/idea_craft.md) $\to$ Xuất `1-idea.md` $\to$ Kiểm toán qua [`review/idea_review.md`](./review/idea_review.md) $\to$ Cập nhật [`ref/idea-index.md`](./ref/idea-index.md). *(Tùy chọn chạy `tools/analyze_audio.py` & `tools/analyze_motion.py` theo [`craft/competitor_analysis.md`](./craft/competitor_analysis.md)).*
2. **Bước 2 — Music (`2-music.md` & `3-lyrics.txt`):** Đọc [`craft/music_craft.md`](./craft/music_craft.md), [`ref/lyrics-index.md`](./ref/lyrics-index.md), [`ref/banned_lyrics_motifs.md`](./ref/banned_lyrics_motifs.md) $\to$ Xuất `2-music.md` & `3-lyrics.txt` $\to$ Kiểm toán qua [`review/music_review.md`](./review/music_review.md) $\to$ Cập nhật [`ref/lyrics-index.md`](./ref/lyrics-index.md).
   - **Tách mốc thời gian (khi có `.wav`):** Gọi `import_media` + `detect_beats` (Palmier Pro MCP), sau đó chạy `uv run --with "faster-whisper" --with "av<14" python3 tools/extract_timestamps.py <audio.wav> --beats <beats.json>` để sinh `timestamps.json`, `timestamps.txt`, `lyrics.srt`.
3. **Bước 3 — Storyboard (`storyboard.md`):** Đọc [`craft/visual_craft.md`](./craft/visual_craft.md), [`style/STYLE_mixed_media_tabletop_diorama.md`](./style/STYLE_mixed_media_tabletop_diorama.md), [`ref/banned_lyrics_motifs.md`](./ref/banned_lyrics_motifs.md) $\to$ Xuất `storyboard.md` $\to$ Kiểm toán qua [`review/retention_review.md`](./review/retention_review.md).
4. **Bước 4 — Image Prompts (`image.txt`):** Đọc [`style/STYLE_mixed_media_tabletop_diorama.md`](./style/STYLE_mixed_media_tabletop_diorama.md) $\to$ Dịch 1:1 từ `storyboard.md` sang `image.txt` $\to$ Kiểm toán qua [`review/retention_review.md`](./review/retention_review.md) $\to$ Tải ảnh về `dola-auto-download/` hoặc `images/`.
5. **Bước 5 — Animation Prompts (`prompt-animate.txt`):** Đọc [`craft/animation_craft.md`](./craft/animation_craft.md) $\to$ Xuất `prompt-animate.txt` khớp 1:1 với `image.txt` $\to$ Kiểm toán qua [`review/animation_review.md`](./review/animation_review.md).
6. **Bước 6 — Dựng Video & SEO (`6-seo.md`):** Đọc [`craft/editing_craft.md`](./craft/editing_craft.md) và [`craft/coslient_seo.md`](./craft/coslient_seo.md) $\to$ Dựng timeline qua Palmier Pro MCP & xuất `6-seo.md` $\to$ Kiểm toán qua [`review/seo_review.md`](./review/seo_review.md) $\to$ Cập nhật [`ref/distrokid.md`](./ref/distrokid.md) và [`ref/bandcamp.md`](./ref/bandcamp.md).

---

## 2. CẤU TRÚC THƯ MỤC DỰ ÁN (`projects/XXX/`)

```text
projects/XXX/
├── 1-idea.md
├── 2-music.md
├── 3-lyrics.txt
├── <audio>.wav
├── timestamps.json, timestamps.txt, lyrics.srt
├── storyboard.md
├── image.txt
├── prompt-animate.txt
├── 6-seo.md
└── dola-auto-download/ (hoặc images/)
```
- **Dự án đa bài (`Multi-Track`):** Thư mục gốc `projects/XXX/` chỉ lưu `1-idea.md` và `2-music.md`; mỗi bài hát nằm trong thư mục con riêng `track-1-<slug>/`, `track-2-<slug>/` chứa đủ các file còn lại.

---

## 3. QUY TẮC VẬN HÀNH BẮT BUỘC

- **Ponytail ([`ponytail`](file:///Users/hoangkien/.gemini/config/skills/ponytail/SKILL.md)):** Tối giản tuyệt đối (YAGNI), ít file nhất, ngắn gọn nhất, xóa bỏ thay vì thêm mới, ưu tiên đưa thẳng cấu trúc và luật của Đầu ra lên đầu.
- **Humanizer ([`humanizer`](./.agents/skills/humanizer/SKILL.md), [`stop-slop`](./.agents/skills/stop-slop/SKILL.md), [`avoid-ai-writing`](./.agents/skills/avoid-ai-writing/SKILL.md)):** Viết tự nhiên như người thật, câu chữ ngắn gọn, trực diện, giàu chi tiết cụ thể; loại bỏ hoàn toàn văn phong sáo rỗng của AI.
- **5 Quy tắc chỉnh sửa tài liệu gốc (`CLAUDE.md`, `AGENTS.md`, `craft/*.md`, `review/*.md`, `style/*.md`):**
  1. Bảo toàn nguyên vẹn khối `🔒 GHI CHÚ CỐ ĐỊNH` ở đầu mỗi file và giữ đúng ranh giới chức năng từng file.
  2. Chỉnh sửa cục bộ đúng chỗ (`edit_file`), bảo toàn quy tắc kỹ thuật cốt lõi.
  3. Ưu tiên câu khẳng định trực tiếp hơn câu phủ định.
  4. Luôn đúc kết thành quy tắc chung (`Rule-First`), tránh liệt kê `Use Case` gây thiên kiến lặp lại.
  5. **Review-Before-Commit:** Kiểm tra `git diff` theo 4 quy tắc trên, sau đó tự động `git commit` ngay theo mẫu `docs(<phạm-vi>): [YYYY-MM-DD HH:MM] <Tóm tắt>`.
- **Cơ chế Kiểm toán Kép 2 Subagent Song Song (`Creator` vs [`audience-reviewer`](./.agents/agents/audience-reviewer.md) + [`adversarial-reviewer`](./.agents/agents/adversarial-reviewer.md)):**
  - Sau mỗi bước (`1-idea.md`, `2-music.md & 3-lyrics.txt`, `character.md/storyboard.md/image.txt`, `prompt-animate.txt`, `6-seo.md`), Agent chính bắt buộc gọi **song song 2 Subagent** (giữ nguyên cặp `conversationId` qua `send_message` xuyên suốt dự án):
    1. **[`audience-reviewer`](./.agents/agents/audience-reviewer.md) (Khán giả 45–85+ khó tính):** Đọc Mục 1 của file `review/*.md` để đánh giá độ chạm cảm xúc, sự tò mò 15s đầu, điểm chán giữa bài và quyết định Click/Like.
    2. **[`adversarial-reviewer`](./.agents/agents/adversarial-reviewer.md) (Chuyên gia & Kỹ thuật):** Đọc Mục 2 của file `review/*.md` và chạy lệnh đếm định lượng để kiểm tra cấu trúc đầu ra, nhịp/vần, góc máy, tỷ lệ vật lý và từ cấm.
  - Bản nháp chỉ qua cổng khi **cả 2 Subagent cùng `PASS`**; sửa triệt để lỗi trên file trước khi trình kết quả cho User. (Cửa thoát: khi User ra lệnh *"chỉ làm thôi"* / *"just execute"*).
- **Quy tắc Đa thành viên & Git Branch (`.current_member`):**
  - Đọc `.current_member` ở đầu phiên (nếu chưa có thì hỏi tên và lưu lại).
  - Nếu là `master`/`main`: Làm việc trên nhánh chính và thư mục `projects/`.
  - Nếu là thành viên (`<tên>`): Tự động checkout nhánh `member-<tên>` và chỉ làm việc trong thư mục `projects-<tên>/`.
