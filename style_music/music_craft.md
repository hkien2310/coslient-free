# 🎵 CẨM NANG SÁNG TÁC ÂM NHẠC — COSLIENT FREE
v10.0 — Tự Do Sáng Tạo, Giản Dị & Chân Thực

---

## ⚡ KIM CHỈ NAM SÁNG TÁC

1. **Folk là gốc (Acoustic Roots):**
   * Tuân thủ [Định vị kênh trong CLAUDE.md](file:///Users/hoangkien/Youtube/coslient-free/CLAUDE.md): Thể loại Folk thuần mộc hoặc kết hợp linh hoạt nhánh lai.
   * Nhạc cụ mộc tự nhiên, ấm áp (không dùng synth điện tử). Tự do chọn nhạc cụ và nhịp điệu phù hợp với cảm xúc bài hát, không đóng đinh khuôn mẫu.
2. **Giọng và hình thức:**
   * AI tự chọn chất giọng và số lượng người hát phù hợp với câu chuyện để đưa vào prompt Suno.
3. **Thời lượng bài hát:**
   * Độ dài vừa vặn (~3 phút): đủ trọn vẹn câu chuyện và có khoảng lặng lắng đọng.
4. **Kỷ luật chống AI Slop (Bắt buộc):**
   * Áp dụng triệt để nguyên tắc từ các skill tại `.agents/skills/` ([stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md)).
   * Cấm tiệt sáo ngữ đao to búa lớn và văn mẫu trị liệu tâm lý (tuân thủ [banned_lyrics_motifs.md](./banned_lyrics_motifs.md)). Ca từ phải chân thực, không giả tạo.

---

## PHẦN 1 — TÊN BÀI HÁT (SONG TITLE)

- **2–4 từ tiếng Anh**, cô đọng, dễ nhớ trên các nền tảng streaming.
- Mượn thuật ngữ đời thường tạo chiều sâu tự nhiên. Tránh sáo ngữ, ủy mị.

---

## PHẦN 2 — SUNO STYLE PROMPT

**Công thức chuẩn 30–40 từ (0% Placebo):**

```text
[1] Genre & Subgenre   — Thể loại folk cụ thể (Folk thuần mộc hoặc nhánh lai).
[2] Instrumentation    — Nhạc cụ acoustic chính dẫn dắt.
[3] Vocal              — Giọng và hình thức thể hiện.
[4] Production & Space — Không gian mộc tự nhiên (warm room / porch acoustic) + Nhịp điệu/BPM.
```

*(Tuyệt đối không nhét Hz, dB, Anti-Drop hay thuật ngữ DSP giả lập vào prompt).*

---

## PHẦN 3 — LYRICS & KỂ CHUYỆN

1. **Giọng kể gần gũi:** Tự do chọn ngôi kể và mức độ tả cảnh. Giữ giọng kể khiêm nhường, bình dị. Không lên lớp giảng đạo. Tả cảnh được — miễn cảnh phục vụ cảm xúc, không tả cho đủ chữ.
2. **Mỏ neo đời thường:** Chi tiết vật lý phải gần gũi, thân thuộc, ai cũng từng thấy. Không giới hạn số lượng — dùng bao nhiêu tùy câu chuyện cần.
3. **Mộc mạc & Dễ hát (Singability):** Từ ngữ đời thường, câu chữ gãy gọn, ngắt dòng theo hơi thở tự nhiên của giai điệu, hát êm và không líu lưỡi.

---

## PHẦN 4 — CƠ CHẾ CHỐNG TRÙNG LẶP (ANTI-COLLISION)

Trước khi viết, đối chiếu [idea-index.md](file:///Users/hoangkien/Youtube/coslient-free/idea-index.md) và [lyrics-index.md](file:///Users/hoangkien/Youtube/coslient-free/lyrics-index.md):
- Không lặp lại đạo cụ mỏ neo đặc trưng đã chiếm ở các bài trước.
- Sở hữu câu hook và màu sắc giai điệu độc lập.

---

## PHẦN 5 — QUY CHUẨN FILE & XUẤT BẢN

* **`2-music.md`** — File làm việc:
  1. `## 🔍 1. PHÂN TÍCH` — Tứ thơ, cảm xúc, không gian.
  2. `## 🏷️ 2. TÊN BÀI HÁT`
  3. `## 🎛️ 3. SUNO STYLE PROMPT`
  4. `## 📜 4. SUNO PERFORMANCE LYRICS` — Ca từ dùng thẻ cấu trúc inline chuẩn Suno: `[tag | mô tả ngắn gọn về nhạc cụ, giọng hát hoặc năng lượng]`.

* **`3-lyrics.txt`** — Lời sạch chuẩn DistroKid:
  - Chỉ lời thuần túy, không thẻ cấu trúc, không credit.
  - Các đoạn lặp viết đầy đủ từng dòng.
  - Mỗi dòng viết hoa chữ đầu, **0% dấu câu ở cuối bất kỳ dòng nào**.
  - Cách đúng 1 dòng trống giữa các khổ.
