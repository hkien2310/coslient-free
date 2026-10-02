# 🎬 ANIMATION CRAFT — QUY CHUẨN CHUYỂN ĐỘNG VIDEO AI
v4.0 — Precision Production Edition (Kling / Runway / Veo3 / Luma / Seedance)

> **Mục tiêu:** Chuyển hóa các ảnh keyframe đã được lựa chọn trên bàn dựng (Timeline Montage) thành các prompt chuyển động (Animation Prompts) bằng tiếng Anh chuẩn xác trong file `prompt-animate.txt` cho tool video AI.
>
> 🔒 **Kiến trúc phân tầng:**
> - `animation_craft.md` độc lập với mọi Style hình ảnh. Dù ảnh đầu vào là đất sét sa bàn, vẽ tay, hay 35mm, prompt diễn hoạt đều tuân thủ ngữ pháp vật lý và quy chuẩn camera dưới đây để triệt tiêu 100% lỗi biến dạng (morphing).
> - **Tham chiếu chuyên sâu:** Sử dụng từ điển chuyển động máy và bài học thực chiến tại [`.agents/skills/cinematic-video-prompt/`](../.agents/skills/cinematic-video-prompt/).

---

## 1. NGUYÊN TẮC VÀNG CHỐNG DỊ TẬT & BIẾN DẠNG (ANTI-MORPHING)
Các mô hình AI Video nhận đầu vào là ảnh tĩnh (Keyframe) và nội suy ra chuyển động trong 5–8 giây. Nếu prompt đòi hỏi hành động quá lớn, AI sẽ làm vỡ nát khung hình, biến dạng bàn tay, méo mặt hoặc mọc thừa chi.

### 🚫 Điều Cấm Kỵ Tuyệt Đối (Failure Triggers):
1. **Cấm đổi tư thế cơ thể:** Đang ngồi đứng phắt dậy, đang quay lưng ngoảnh mặt lại 180°, đang đi dừng lại đột ngột.
2. **Cấm chuỗi hành động liên hoàn:** *"Vừa đi vừa lấy chìa khóa vừa mở cửa"* $\rightarrow$ AI sẽ làm biến dạng chìa khóa và tay dính vào cửa.
3. **Cấm biểu cảm kịch tính quá đà:** *"Bật khóc nức nở", "cười há hốc miệng"* $\rightarrow$ Khuôn mặt sẽ bị méo mó kỳ dị. Phải kìm hãm biểu cảm bằng các câu lệnh giới hạn.
4. **Cấm dùng từ máy quay mơ hồ:** Tránh dùng `zoom in / push in` (dễ bị AI crop số làm vỡ hạt); bắt buộc dùng `dolly in` (máy trượt trên ray).

### ✅ Chuyển Động Sinh Học Vừa Tầm (Micro-Movements):
1. **Cử chỉ vi mô:** Khóe môi mỉm cười nhẹ từ tốn, hàng mi chớp khẽ, ánh mắt hướng sang một bên, lồng ngực phập phồng nhịp thở êm ái, ngón tay khẽ vuốt ve bề mặt gỗ mòn hoặc chạm nhẹ bàn tay người đối diện.
2. **Vật lý môi trường (Environmental Physics):** Vạt áo lanh lay nhẹ theo gió, vài sợi tóc bay lất phất, khói bếp lững lờ bốc lên, hơi nước nghi ngút từ chén trà nóng, ngọn đèn dầu bập bùng nhẹ, lá cây rơi êm.
3. **Chuyển động máy quay mượt mà (Smooth Camera Moves):** Ưu tiên máy chuyển động để tạo cảm giác sống động, nhân vật chỉ cần cử động vi mô.

---

## 2. CÔNG THỨC PROMPT ANIMATION 4 THÀNH PHẦN

Mỗi prompt animation bắt buộc được cấu trúc theo 4 khối rõ ràng:

```text
[1. Cú máy Camera điện ảnh] + [2. Vi cử động nhân vật (Micro-actions)] + [3. Vật lý môi trường & Nguồn sáng] + [4. Câu lệnh an toàn & Hạn chế dị tật]
```

### Các Khối Cú Máy Chuẩn Đã Kiểm Chứng (AI Video Tested):
* **Tiến chậm:** `Slow smooth cinematic dolly-in shot toward the [subject]...`
* **Lùi xa buông lắng:** `Slow continuous dolly-out shot from the [subject], gradually expanding the surrounding environment...`
* **Trượt thị sai (Vũ khí tạo chiều sâu 3D):** `Subtle horizontal parallax camera slider moving behind the foreground [tree branch/porch railing], revealing the [subject] in the midground...`
* **Nâng hạ trục máy:** `Slow pedestal up / pedestal down shot, maintaining smooth level perspective...`
* **Lượn vòng cung:** `Slow orbital arc shot (30 degrees) rotating gently around the [subject]...`
* **Máy tĩnh tuyệt đối:** `Static locked-off camera with shallow depth of field, zero camera movement...`

---

## 3. BÀI HỌC THỰC CHIẾN TỪ CÁC MODEL AI VIDEO MỚI (VEO3 / KLING / RUNWAY)

1. **Khóa liên tục, không cắt cảnh:** Luôn bổ sung câu `single continuous shot, no cuts, no transitions` để ngăn AI tự ý cắt ghép thành 2 cảnh trong 1 clip 5s.
2. **Chặn sinh chữ bừa bãi:** Model video rất hay tự vẽ chữ giả, phụ đề hoặc logo nhảm nhí lên màn hình. Luôn chốt đuôi bằng: `no subtitles, no captions, no on-screen text, no watermark`.
3. **Kìm hãm cảm xúc bằng câu cấm cụ thể:** Khi muốn nhân vật rưng rưng xúc động, ghi rõ: `gentle emotional eyes, tears stay in eyes and never fall, no crying, no dramatic facial distortion, soft peaceful expression`.
4. **Giữ nguyên trạng thái nhân vật:** Luôn ghi rõ tư thế ban đầu của ảnh tĩnh: `the character maintains their seated posture throughout the entire shot`.

---

## 4. BỘ MẪU PROMPT THỰC CHIẾN

### 🌟 Mẫu 1: Toàn cảnh / Trung cảnh sinh hoạt (Wide / Medium Shot)
> **Ví dụ Shot 02:**
> ```text
> Slow smooth cinematic dolly-in shot toward the warm wooden porch. The elderly grandfather gently tilts the vintage watering can, sending a soft sparkling stream of water onto the blooming flowerbed, his worn flannel shirt hem softly rustling in the evening breeze. He pauses and lifts his head with a warm, gentle smile. Strings of warm incandescent bulbs glow softly above as delicate evening mist drifts across the yard. Single continuous shot, no cuts, natural organic movement, no subtitles, no text, no watermark.
> ```

### 🌟 Mẫu 2: Cận cảnh Xúc giác / Cảm xúc (Close-Up / Macro)
> **Ví dụ Shot 15:**
> ```text
> Static locked-off camera with shallow depth of field. The weathered, calloused hand of the grandfather tenderly clasps the grandmother's slender fingers resting on the polished timber railing, with a gentle natural thumb stroke and subtle finger twitch. Soft rim lighting outlines their hands against the warm dusk ambient. Gentle natural breathing movement, rich tactile texture, single continuous shot, no cuts, no morphing, no subtitles, no watermark.
> ```

### 🌟 Mẫu 3: Cảnh trượt thị sai chiều sâu (Parallax Slider)
> **Ví dụ Shot 22:**
> ```text
> Subtle horizontal parallax slider slowly drifting past an out-of-focus oak branch in the foreground, smoothly revealing the elderly couple drinking tea at the weathered patio table in the midground. Gentle steam rises continuously from the ceramic tea cups into the cool evening air. The grandmother takes a tiny slow sip while looking out thoughtfully. Smooth cinematic motion, no abrupt movement, no cuts, no subtitles, no on-screen text.
> ```

---

## 5. CHECKLIST TIỀN BAY (PRE-FLIGHT VERIFICATION)

Trước khi xuất file `animation.txt`, AI/Editor bắt buộc phải rà soát qua 7 câu hỏi sống còn:

- [ ] **1. Quy tắc 1-1:** Mỗi shot chỉ có duy nhất **1 lệnh camera** và **1 hành động chính**?
- [ ] **2. Khóa tư thế:** Nhân vật có giữ nguyên tư thế của ảnh gốc không (không đứng dậy, không quay ngoắt)?
- [ ] **3. Vi cử động:** Động tác nhân vật có ở mức vi mô (thở, cười mỉm, chớp mắt, chạm nhẹ tay)?
- [ ] **4. Vật lý môi trường:** Đã mô tả khói/sương/gió/hơi nước/ánh đèn để cảnh sống động tự nhiên chưa?
- [ ] **5. Khóa cú máy:** Đã có câu lệnh `single continuous shot, no cuts` chưa?
- [ ] **6. Chặn chữ & logo:** Đã có câu lệnh `no subtitles, no on-screen text, no watermark` chưa?
- [ ] **7. Khớp số lượng:** Số lượng prompt trong file có khớp chính xác 100% với số lượng ảnh đã tạo không?

---

## 6. ĐẦU RA CHUẨN: `animation.txt` (HOẶC `prompt-animate.txt`)

* File lưu tại thư mục project: `projects/<id>/animation.txt`.
* Mỗi prompt là một đoạn văn tiếng Anh hoàn chỉnh, cách nhau bằng 1 dòng trống.
* Đánh số thứ tự khớp chính xác với Shot:
  ```text
  # SHOT 01 (00:00 - 00:11)
  Slow smooth cinematic dolly-in shot toward...

  # SHOT 02 (00:11 - 00:15)
  Subtle horizontal parallax camera slider moving...
  ```
