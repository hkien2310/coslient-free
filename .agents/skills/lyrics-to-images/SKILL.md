---
name: lyrics-to-images
description: >
  Bước 5 workflow Coslient. Đọc 4-visual.md + 2-music.md + style file + DIVERSITY_ENGINE.md,
  chia lyrics thành scenes, tạo 5–10 prompt ảnh mỗi scene, đảm bảo đa dạng 11 chiều.
  Trigger: "tạo ảnh cho lyrics", "làm ảnh video", "bước 5", "batch images", "làm ảnh project".
---

# SKILL: Lyrics → Image Batch (Bước 5)

## BƯỚC 0 — ĐỌC TRƯỚC KHI LÀM GÌ

Đọc đủ 3 file, theo thứ tự này:

1. **`4-visual.md`** của project → visual story đã chốt, style được chọn, ghi chú từ test
2. **Style file được chỉ định trong `4-visual.md`** → BASE DNA, NEGATIVE, quy tắc vật liệu
3. **`style/DIVERSITY_ENGINE.md`** → 11 chiều đa dạng, cách không lặp combo

Chưa đọc đủ 3 → không viết prompt.

## BƯỚC 1 — CHIA SCENES

Đọc `2-music.md` → chia lyrics thành scenes theo cảm xúc:

- 1–2 dòng lyrics có cảm xúc thuần nhất = 1 scene
- Đoạn không lời = 1 scene cảnh (tập trung môi trường, ít/không nhân vật)
- Điệp khúc lặp: nếu cảm xúc giống nhau → gộp, nếu cường độ tăng → tách

Với mỗi scene ghi rõ: câu hát / cảm xúc cốt lõi / số ảnh (5 / 7 / 10).

## BƯỚC 2 — TẠO PROMPT

Với mỗi ảnh trong scene:
- Lấy visual story từ `4-visual.md` làm nền
- Chọn combo 11 chiều theo DIVERSITY_ENGINE (không lặp combo trong cùng batch)
- Dịch combo sang ngôn ngữ của style file (dùng từ vựng/vật liệu đặc trưng của style)
- Giữ nguyên BASE DNA và NEGATIVE của style — không cắt bớt

**Cấu trúc mỗi prompt:**
```
[BASE DNA của style],
[nhân vật / trang phục / đạo cụ],
[hành động / biểu cảm],
[môi trường / kiến trúc],
[thời gian / thời tiết],
[ánh sáng],
[góc máy / cỡ cảnh],
[bố cục / atmosphere],
[NEGATIVE của style]
```

## BƯỚC 3 — XUẤT OUTPUT vào `5-image.txt`

```
# IMAGE BATCH — [TÊN PROJECT]
Style: [tên style file]
Tổng: __ scenes | __ ảnh

---

## SCENE 1: [Câu hát]
Cảm xúc: [__] | Số ảnh: [__]

### IMG 1.1
[full prompt]

### IMG 1.2
[full prompt]

---

## SCENE 2: ...
```

## QUY TẮC CỨNG

**Shot mix bắt buộc mỗi batch scene (5 ảnh tối thiểu):**

| Loại | Bắt buộc | Mô tả |
|---|---|---|
| Cảnh rộng / thiết lập | ≥ 1 | Wide/extreme wide — thấy toàn bộ thế giới, không gian |
| Cảnh trung có nhân vật | ≥ 1 | Medium shot — thấy người + môi trường xung quanh |
| Cảnh cận nhân vật | ≥ 1 | Close-up — mặt / tay / chi tiết cảm xúc |
| Cảnh không có nhân vật | ≥ 1 | Chỉ môi trường / kiến trúc / đồ vật |
| Góc bất thường | ≥ 1 | Góc thấp / góc cao / overhead / POV |

Batch 7 ảnh: mỗi loại ≥ 1, phân bổ tự do phần còn lại.
Batch 10 ảnh: mỗi loại ≥ 2.
Không 2 ảnh liên tiếp cùng loại shot.

**Constants từ `4-visual.md` — bắt buộc nhất quán:**
- Visual anchor object phải xuất hiện trong ≥ 30% số ảnh của batch
- Color signature phải nhất quán trong toàn bộ batch (không có ảnh nào lạc palette)
- Atmosphere phải nhất quán — dù cảnh ở đâu, cảm giác thế giới phải cùng 1 loại

**Nhân vật — được phép thay đổi tự do:**
- Mỗi ảnh có thể là người/nhân vật khác nhau
- Không cần cùng 1 nhân vật xuyên suốt

---

## ⛔ QUY TẮC CHỐNG ANCHOR BIAS — BẮT BUỘC

### Vấn đề
Agent thường đọc lyrics buồn / đơn độc → tự suy ra "nên chỉ dùng 1 nhân vật cô đơn". Đây là lỗi suy luận.

### Nguyên tắc cốt lõi
> **Cảm xúc bài hát chỉ ảnh hưởng đến ATMOSPHERE — KHÔNG phải số lượng nhân vật hay sự sống trong frame.**

Một thế giới **bình yên, chậm rãi** vẫn có: chợ buổi sáng, bà cụ và đàn vịt, khói bếp từ mỗi nhà, trẻ em vẫy tay ở xa — những thứ này KHÔNG phá vỡ cảm xúc, chúng LÀM cho thế giới trở nên thật.

### W-code bắt buộc mỗi batch 5 ảnh

| W-code | Mô tả | Số lần |
|--------|-------|--------|
| W-SOLO | 1 nhân vật, không sinh vật | ≤ 2/5 ảnh |
| W-PET | Nhân vật + sinh vật (chó/mèo/chim/bò...) | Khuyến khích |
| W-CROWD | 5+ người, dù xa (chợ / làng / lễ hội) | Bắt buộc ≥1/5 hoặc |
| W-LIFE | Dấu hiệu người sống (khói bếp, quần phơi...) | ≥1/5 ảnh |
| W-ANIMAL | Sinh vật tự nhiên, không có người | Khuyến khích |

**Rule tối thiểu:** Mỗi batch 5 ảnh → **ít nhất 1 ảnh** phải là `W-CROWD`, `W-PET`, hoặc `W-ANIMAL`.

### Ví dụ đúng — Scene "bình yên, đơn độc"
```
IMG1: W-CROWD  → Cảnh làng sáng sớm, vài người ra chợ từ xa (SZ-EW)
IMG2: W-SOLO   → Ông lão ngồi uống trà một mình trên hiên (SZ-M)
IMG3: W-PET    → Bà cụ cho gà ăn, con chó nằm bên cạnh (SZ-W)
IMG4: W-LIFE   → Khói bếp từ ống khói, quần áo phơi trên dây, không thấy người (SZ-EW)
IMG5: W-SOLO   → Cận tay ông lão đặt tách trà xuống bàn gỗ (SZ-XCU)
```

### Ví dụ SAI — Anchor bias từ lyrics buồn
```
IMG1: W-SOLO   → Ông lão ngồi một mình
IMG2: W-SOLO   → Ông lão nhìn ra cửa sổ
IMG3: W-SOLO   → Ông lão đứng ở đồng
IMG4: W-LIFE   → Tách trà nguội trên bàn
IMG5: W-SOLO   → Ông lão đi bộ một mình  ← 4/5 W-SOLO = FAIL
```

---

## 🛡️ BỘ LỌC AN TOÀN TỪ VỰNG (CONTENT MODERATION SAFE-LIST) — BẮT BUỘC

Mọi prompt trước khi ghi vào file output PHẢI được rà soát khử 100% các từ nhạy cảm có thể kích hoạt Safety Filter (Google Imagen, Gemini, DALL-E) dẫn đến lỗi *"I can't generate the requested content"*:

- **Chất cấm / Cần sa:**
  - ❌ CẤM `maple` / `maple leaf` $\rightarrow$ ✅ Thay bằng `oak leaf`, `willow leaf`, `birch leaf`.
  - ❌ CẤM `flowerpot` / `pot` $\rightarrow$ ✅ Thay bằng `ceramic planter`, `terracotta planter`, `ceramic vase`.
  - ❌ CẤM `crystalline` / `crystals` $\rightarrow$ ✅ Thay bằng `glistening`, `sparkling`, `clear`, `pristine`.
  - ❌ CẤM `twig` $\rightarrow$ ✅ Thay bằng `small branch`, `wooden sprig`.
- **Chất kích thích / Thuốc lá:**
  - ❌ CẤM `tobacco` / `cigar` / `pipe` $\rightarrow$ ✅ Thay bằng `tin tea caddy`, `wooden spice box`, `pocket watch`.
- **Vũ khí / Bạo lực:**
  - ❌ CẤM `knife` / `blade` / `cut` $\rightarrow$ ✅ Thay bằng `carved`, `sculpted`, `artisan chisel`.
  - ❌ CẤM `shoot` / `shot` (chụp/bắn) $\rightarrow$ ✅ Thay bằng `view`, `perspective`, `framing`, `camera angle`.
- **Quy tắc cộng dồn rủi ro:** Tuyệt đối không gom các từ nhạy cảm nhẹ vào cùng 1 câu. Luôn kiểm tra prompt sạch trước khi xuất.

