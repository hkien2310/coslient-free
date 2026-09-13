---
name: visual-story
description: >
  Bước 4 workflow Coslient. Trao đổi với user để xác định visual story (style + câu chuyện),
  tạo test prompts, iterate đến khi user duyệt, tổng hợp thành 4-visual.md.
  Trigger: "làm visual", "bước 4", "visual story", "chọn style", "tạo ảnh cho bài".
---

# SKILL: Visual Story Builder (Bước 4)

## BƯỚC 0 — ĐỌC CONTEXT TRƯỚC
Đọc `2-music.md` của project → hiểu bài hát, cảm xúc, leitmotif trước khi nói chuyện với user.

## BƯỚC 1 — CHỌN STYLE
Đọc thư mục `style/` → list tất cả file `STYLE_*.md` đang có để user chọn.
Không hard-code tên file — list động từ thư mục mỗi lần chạy.

User chọn style nào thì đọc file đó → nắm BASE DNA, NEGATIVE, quy tắc vật liệu.

## BƯỚC 2 — KHÁM PHÁ VISUAL STORY (CONVERSATIONAL)

**Nguyên tắc quan trọng nhất:**
User sẽ không có đầy đủ thông tin. Họ sẽ nói những thứ rất vắn tắt như "thế giới loài vật fantasy", "nhà bay", "những mảnh rời rạc". Đó là đủ để bắt đầu.

**Cách agent làm:**
- Lấy bất cứ thứ gì user nói làm điểm xuất phát
- Agent tự suy ra những gì còn thiếu dựa trên bài hát + style đã chọn
- Chỉ hỏi thêm khi thực sự cần — và hỏi tự nhiên, không phải điền form
- Nếu user nói "không biết" → agent tự đề xuất 2-3 hướng để user chọn hoặc bác

**Những thông tin agent cần tổng hợp được (không nhất thiết hỏi hết):**
- Visual world: thế giới này trông như thế nào?
- Nhân vật (nếu có)
- Mood / cảm xúc chủ đạo
- 1-2 hình ảnh / vật thể đặc trưng xuyên suốt (visual anchor)

Agent tự điền những gì không hỏi được dựa trên context từ `2-music.md` và style file.

## BƯỚC 3 — TẠO TEST PROMPTS
Khi đã có đủ hình dung (dù chưa hoàn hảo) → tạo 3-5 test prompt.
- Đa dạng góc máy, cảnh vật, nhân vật
- Tuân thủ BASE DNA + NEGATIVE của style file đã chọn
- Format copy-paste được ngay vào tool tạo ảnh

Xuất rõ: `PROMPT 1: ...` / `PROMPT 2: ...` ...

## BƯỚC 4 — ITERATE
- User test → feedback tự do (không cần format — ưng/không ưng/sửa cái này/kiểu khác...)
- Agent đọc feedback → xác định vấn đề cụ thể → sửa đúng chỗ đó
- Tạo batch mới
- Lặp đến khi user nói xong / ưng / ok

## BƯỚC 5 — GHI 4-visual.md
Khi user ưng, tổng hợp tất cả thành `4-visual.md` trong project folder:

```
# 4-VISUAL — [TÊN PROJECT]

## STYLE
File: [tên style file]
Điều chỉnh: [nếu có]

## VISUAL STORY
[Mô tả tự do — thế giới này là gì, cảm xúc chủ đạo, câu chuyện kể về điều gì]

## CONSTANTS — Không thay đổi dù cảnh ở đâu, shot nào
Visual anchor: [1-2 vật / biểu tượng lặp lại — phải có trong ≥ 30% số ảnh]
Color signature: [1-2 màu chủ đạo xuyên suốt]
Atmosphere: [cảm giác thế giới này — dù cảnh thay đổi, atmosphere phải nhất quán]

## VARIABLES — Được phép thay đổi tự do
Nhân vật: nhiều người khác nhau, không cố định
Địa điểm, shot type, góc máy, thời gian, hành động — tất cả

## GHI CHÚ
[điều chỉnh phát hiện khi test — để agent bước 5 không lặp lỗi]
```

## QUY TẮC CỨNG
- KHÔNG hỏi user theo form cứng nhắc — trao đổi tự nhiên
- KHÔNG chờ đủ thông tin mới tạo prompt — có ý tưởng sơ bộ là đủ để test
- KHÔNG bỏ qua bước test — dù visual story có rõ đến đâu
- 1 agent chỉ làm bước 4 — tạo ảnh hàng loạt (bước 5) là agent khác đảm nhiệm

## ⛔ QUY TẮC THÉP — TEST PROMPTS KHÔNG ĐƯỢC GHI VÀO 4-visual.md
Test prompts chỉ xuất ra chat để user test và feedback.
**TUYỆT ĐỐI KHÔNG** copy prompt vào file `4-visual.md`.

Lý do: agent đọc `4-visual.md` ở bước 5 sẽ bị anchor bias — dùng prompt mẫu như khuôn, dẫn đến toàn bộ batch chỉ là biến thể của 1-2 cảnh test thay vì xây dựng thế giới đa dạng thực sự.

File `4-visual.md` chỉ chứa: STYLE + VISUAL STORY + CONSTANTS + VARIABLES + GHI CHÚ.
Prompts test thuộc về chat history — không thuộc về design doc.
