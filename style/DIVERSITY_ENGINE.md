# 🎲 DIVERSITY ENGINE v1.0
**Coslient Free · Bộ Máy Đa Dạng Hoá Ảnh AI**

File này được agent tạo ảnh đọc **song song** với file STYLE được chọn.  
Mục đích: **đảm bảo mỗi batch ảnh (5–10 ảnh/cảnh) không lặp combo** trên 11 chiều đa dạng hoá.

---

## ⚠️ QUY TẮC NỀN TẢNG

**QUY TẮC 1 — KHÔNG LẶP COMBO:**  
Trong 1 batch (cùng câu hát / cùng cảnh), mỗi ảnh phải khác ít nhất **3 chiều** so với ảnh trước.  
Dùng bảng TRACKING SHEET ở cuối file để kiểm tra trước khi xuất prompt.

**QUY TẮC 2 — STYLE FILE LUÔN THẮNG:**  
Mọi lựa chọn từ các chiều dưới đây đều phải nằm trong vùng được phép của STYLE file đang dùng.  
Nếu xung đột → bỏ lựa chọn đó, chọn option kế tiếp. KHÔNG phá vỡ ngôn ngữ vật liệu của style.

**QUY TẮC 3 — SỐ ẢNH MỖI CẢNH:**  
- Cảnh đơn giản (1 cảm xúc, ít biến số) → 5 ảnh  
- Cảnh phức tạp (cảm xúc layered, nhiều nhân vật, địa điểm đặc biệt) → 7–10 ảnh  
- Đừng tạo nhiều hơn cần thiết. Chất lượng > số lượng.

---

## CHIỀU 1 — NHÂN VẬT (Character Identity)

Số lượng và tính chất nhân vật trong frame.

| Code | Mô tả |
|------|-------|
| C-A | Nhân vật đơn độc — toàn thân |
| C-B | Nhân vật đơn độc — nhìn từ sau lưng |
| C-C | Đôi (couple / bạn bè / thầy-trò) |
| C-D | Nhóm 3 người trở lên |
| C-E | Nhân vật ẩn — chỉ thấy bóng / dấu vết / vật để lại |
| C-F | Nhân vật xa xôi — điểm nhỏ giữa khung cảnh bao la |

**Quy tắc:** Trong 6 ảnh đầu của batch, dùng ít nhất 4 code khác nhau.

---

## CHIỀU 1.5 — SỰ SỐNG & ĐÔNG ĐÚC (World Liveliness) ⭐ MỚI

> [!IMPORTANT]
> **Đây là chiều bổ sung bắt buộc.** Cảm xúc bài hát (đơn độc, tĩnh lặng) chỉ ảnh hưởng đến ATMOSPHERE — KHÔNG được dùng để biện minh cho việc giảm W-diversity. Thế giới sống động CÓ THỂ chứa cô đơn nhưng không phải TẤT CẢ đều cô đơn.

| Code | Mô tả | Ví dụ cụ thể |
|------|-------|-------------|
| W-SOLO | 1 nhân vật, không sinh vật, không đám đông | Ông lão ngồi một mình trên đồi |
| W-PET | Nhân vật + ≥1 sinh vật gần (chó, mèo, chim, bò, ngựa, vịt...) | Bà cụ cho gà ăn trước cửa nhà |
| W-CROWD | Cảnh đông người — chợ / lễ hội / xóm làng / quảng trường (5+ người, dù xa) | Buổi sáng làng cối xay gió nhộn nhịp, người qua lại trên đường |
| W-LIFE | Cảnh vật vô sinh nhưng có dấu hiệu người sống (không cần thấy người) | Khói bếp buổi sáng, quần áo phơi trên dây, đèn cửa sổ le lói đêm |
| W-ANIMAL | Thiên nhiên có sinh vật nhưng KHÔNG có người | Đàn chim đậu trên cánh cối xay gió, con bướm trên bông hoa cúc |

**Quy tắc bắt buộc cho batch 5 ảnh:**
- `W-SOLO` không quá **2/5 ảnh**
- Ít nhất **1 ảnh** phải là `W-CROWD` hoặc `W-PET` hoặc `W-ANIMAL`
- Không 2 ảnh liên tiếp cùng W-code

**Ví dụ phân bổ chuẩn batch 5:**
```
IMG1: W-CROWD  → Cảnh làng sáng sớm, người ra chợ
IMG2: W-SOLO   → Ông lão ngồi uống trà một mình
IMG3: W-PET    → Bà cụ và con mèo ngủ trên hiên
IMG4: W-LIFE   → Khói bếp bay từ ống khói, không thấy người
IMG5: W-ANIMAL → Đàn bồ câu trên cánh quạt cối xay gió
```

---

## CHIỀU 2 — NGOẠI HÌNH & ĐẶC ĐIỂM NHÂN VẬT (Appearance)

Biến số tuỳ style — agent ưu tiên lấy từ SLOT A của style file hiện tại.  
Nếu style không có slot, chọn từ pool sau:

| Code | Mô tả |
|------|-------|
| AP-1 | Trẻ / thanh thiếu niên |
| AP-2 | Trung niên |
| AP-3 | Người cao tuổi |
| AP-4 | Trẻ em (6–12 tuổi) |
| AP-5 | Nhân vật phi giới tính / trung tính |

**Quy tắc:** Không dùng cùng một age range quá 2 lần trong 1 batch 5 ảnh.

---

## CHIỀU 3 — TRANG PHỤC & PHỤ KIỆN (Costume & Accessories)

Trang phục ưu tiên lấy từ SLOT B của style file (nếu có).  
Nếu không — đa dạng theo nhóm sau:

| Code | Nhóm | Gợi ý |
|------|------|-------|
| CO-1 | Nhẹ nhàng / thường ngày | áo đơn, váy đơn giản |
| CO-2 | Nghi lễ / trang trọng | áo choàng, trang phục đặc biệt |
| CO-3 | Dày dặn / nhiều lớp | áo khoác dài + khăn + mũ |
| CO-4 | Cởi bỏ bớt lớp / tự nhiên | áo ngắn, tay trần |
| CO-5 | Phụ kiện là điểm nhấn chính | nón lớn, balo, dù, đèn lồng |

**Đạo cụ xoay vòng (mỗi ảnh 1 đạo cụ khác nhau):**  
Batch 5: sách · giỏ · đèn lồng · nhạc cụ · hoa  
Batch 10: + gương · bản đồ · chìa khoá · vật kỷ niệm · con vật nhỏ đi kèm

---

## CHIỀU 4 — CẢNH VẬT & MÔI TRƯỜNG (Environment)

| Code | Loại | Mô tả |
|------|------|-------|
| ENV-1 | Nội thất ấm áp | trong nhà, ánh đèn, không gian nhỏ |
| ENV-2 | Ngoại thất tự nhiên — mở | đồng nội, biển, núi, bầu trời rộng |
| ENV-3 | Ngoại thất tự nhiên — hẹp | hẻm núi, rừng rậm, hang động, lạch nước |
| ENV-4 | Không gian nhân tạo đời thường | phố, chợ, bến cảng, đường làng |
| ENV-5 | Không gian chuyển tiếp | cầu, cổng, cửa, ngưỡng cửa, bến đò |
| ENV-6 | Không gian trên cao | mái nhà, vách núi, tháp, ngọn đồi |
| ENV-7 | Không gian dưới thấp | lòng giếng, tầng hầm, dưới tán cây khổng lồ |

**Quy tắc:** Trong 1 batch 7 ảnh → không dùng ENV code nào quá 2 lần.

---

## CHIỀU 5 — KIẾN TRÚC (Architecture Density)

Lượng kiến trúc xuất hiện trong frame — độc lập với ENV.

| Code | Mô tả |
|------|-------|
| AR-0 | Không kiến trúc — thiên nhiên thuần tuý |
| AR-1 | Kiến trúc nhỏ — 1 yếu tố (cánh cửa, cột đèn, giếng) |
| AR-2 | Kiến trúc vừa — 1 công trình (nhà, cầu, tháp) |
| AR-3 | Kiến trúc dày — cả khu (làng, phố, quảng trường) |
| AR-4 | Kiến trúc bị thiên nhiên nuốt chửng / hoang phế |

---

## CHIỀU 6 — THỜI GIAN & THỜI TIẾT (Time & Weather)

| Code | Mô tả | Tông màu bầu trời |
|------|-------|------------------|
| TW-1 | Bình minh / sương sớm | hồng tím, cam nhạt |
| TW-2 | Ban ngày trong xanh | xanh da trời, trắng mây |
| TW-3 | Ban ngày흐리 / mây phủ | xám bạc, khuếch tán |
| TW-4 | Hoàng hôn | cam đỏ, vàng cháy |
| TW-5 | Chạng vạng / blue hour | xanh navy sâu |
| TW-6 | Đêm — ánh sao / trăng | xanh đen, bạc |
| TW-7 | Đêm — ánh đèn nhân tạo | vàng ấm, lung linh |
| TW-8 | Mưa / sau mưa | phản chiếu, ẩm ướt |
| TW-9 | Tuyết / sương giá | trắng tinh, tĩnh lặng |
| TW-10 | Gió mạnh | tóc bay, vạt áo phấp phới |

**Quy tắc:** Batch 5 ảnh → ít nhất 3 code TW khác nhau. Batch 10 → ít nhất 5 code TW.

---

## CHIỀU 7 — ÁNH SÁNG & PALETTE MÀU (Lighting & Color)

**Nguồn sáng:**
| Code | Mô tả | Kelvin |
|------|-------|--------|
| L-1 | Khuếch tán mềm — overcast | 5500–6500K |
| L-2 | Nắng vàng xiên — golden hour | 3200–4000K |
| L-3 | Đèn dầu / dây tóc — indoor glow | 2200–2400K |
| L-4 | Rim light / backlit — ngược sáng | tuỳ background |
| L-5 | Ánh sáng từ dưới lên — campfire | 2000–2800K |
| L-6 | Ánh trăng / sao lạnh | 5000–8000K |
| L-7 | Ánh sáng lọc qua tán cây — dappled | 4000–5000K |
| L-8 | Ánh nước phản chiếu | lạnh + lung linh |

**Palette chủ đạo:**
| Code | Palette | Cảm xúc |
|------|---------|---------| 
| P-warm | Amber, ochre, rust, cream | Ấm áp, hoài niệm |
| P-cool | Navy, slate, mist, silver | Tĩnh lặng, xa xôi |
| P-earth | Brown, moss, clay, sand | Gần gũi, chân thực |
| P-vivid | Crimson, cobalt, gold | Kịch tính, mạnh mẽ |
| P-muted | Dusty rose, sage, ivory | Nhẹ nhàng, thơ mộng |

**Quy tắc:** Không dùng cùng L-code quá 2 lần / batch. Không dùng cùng P-code quá 2 lần / batch.

---

## CHIỀU 8 — HÀNH ĐỘNG & BIỂU CẢM (Action & Expression)

**Hành động — 4 nhóm:**
| Nhóm | Code | Mô tả |
|------|------|-------|
| Tĩnh | ACT-S1 | Đứng ngắm / quan sát |
| | ACT-S2 | Ngồi nghỉ / đọc / uống trà |
| | ACT-S3 | Nằm / dựa / thả lơi |
| Chuyển động chậm | ACT-M1 | Đi bộ / dạo bước |
| | ACT-M2 | Với tay / chạm nhẹ vào thứ gì đó |
| | ACT-M3 | Nhìn về phía sau / quay đầu |
| Chuyển động mạnh | ACT-D1 | Chạy / nhảy / nhảy múa |
| | ACT-D2 | Làm việc tay chân / gánh / kéo |
| | ACT-D3 | Tung hứng / biểu diễn |
| Tương tác | ACT-I1 | Tương tác với vật thể (cầm, đặt, mở) |
| | ACT-I2 | Tương tác với sinh vật / con vật |
| | ACT-I3 | Tương tác với người khác (đưa tay, ôm, nhìn nhau) |
| | ACT-I4 | Tương tác với thiên nhiên (nước, gió, lá) |

**Biểu cảm — xoay vòng 7 trạng thái:**  
bình yên → suy tư → vui tươi → ngạc nhiên → nhớ thương → tập trung → mơ màng

**Quy tắc:** Trong 5 ảnh → ít nhất 2 nhóm ACT khác nhau. Không dùng cùng biểu cảm quá 2 lần.

---

## CHIỀU 9 — GÓC MÁY & CỠ CẢNH (Camera Angle & Shot Size)

**ĐÂY LÀ CHIỀU QUAN TRỌNG NHẤT.** Nhiều batch thất bại vì toàn dùng medium-shot thẳng góc.

### Cỡ cảnh:
| Code | Tên | Mô tả |
|------|-----|-------|
| SZ-EW | Extreme Wide | Nhân vật rất nhỏ, cảnh chiếm 80%+ frame |
| SZ-W | Wide | Thấy toàn thân nhân vật rõ |
| SZ-M | Medium | Ngang thắt lưng trở lên |
| SZ-CU | Close-Up | Mặt + vai hoặc chi tiết cụ thể |
| SZ-XCU | Extreme Close-Up | 1 chi tiết duy nhất (đôi tay, đôi mắt) |
| SZ-OTS | Over-the-Shoulder | Nhìn qua vai vào cảnh trước mặt |

### Góc máy:
| Code | Mô tả |
|------|-------|
| CA-EYE | Ngang tầm mắt — trung tính |
| CA-LOW | Góc thấp / worm's eye — nhìn lên |
| CA-HIGH | Góc cao / bird's eye — nhìn xuống |
| CA-DUTCH | Nghiêng frame — dynamic / dramatic |
| CA-BEHIND | Nhìn từ sau lưng nhân vật |
| CA-AERIAL | Toàn cảnh từ trên không |

### Góc nhìn:
| Code | Mô tả |
|------|-------|
| PV-FRONT | Nhân vật nhìn thẳng vào camera |
| PV-PROFILE | Nhân vật nhìn nghiêng 90 độ |
| PV-3QTR | Quarter turn — ba phần tư |
| PV-AWAY | Nhân vật quay lưng / nhìn đi chỗ khác |

**Mỗi ảnh trong batch = combo [SZ + CA + PV] chưa dùng trong batch đó.**

**Phân bổ chuẩn — batch 5 ảnh:**
```
Ảnh 1: SZ-EW  + CA-HIGH   + PV-AWAY    → mở cảnh hoành tráng
Ảnh 2: SZ-W   + CA-EYE    + PV-PROFILE → giới thiệu nhân vật
Ảnh 3: SZ-M   + CA-LOW    + PV-3QTR    → cảm xúc đẩy lên
Ảnh 4: SZ-CU  + CA-EYE    + PV-FRONT   → cận mặt / đỉnh điểm
Ảnh 5: SZ-W   + CA-BEHIND + PV-AWAY    → đóng cảnh / ra đi
```

**Mở rộng — batch 10 ảnh:**
```
Ảnh 6:  SZ-OTS + CA-EYE    + PV-FRONT   → POV nhân vật phụ
Ảnh 7:  SZ-EW  + CA-AERIAL + PV-AWAY    → toàn cảnh từ trên không
Ảnh 8:  SZ-M   + CA-DUTCH  + PV-3QTR    → góc dramatic
Ảnh 9:  SZ-XCU + CA-EYE    + PV-FRONT   → chi tiết cực cận
Ảnh 10: SZ-W   + CA-LOW    + PV-PROFILE → khép lại hùng tráng
```

---

## CHIỀU 10 — BỐ CỤC & TỶ LỆ KHÔNG GIAN (Composition & Scale)

**Bố cục:**
| Code | Mô tả |
|------|-------|
| COMP-R3 | Rule of thirds — nhân vật lệch sang 1/3 frame |
| COMP-C | Centered / symmetry — đối xứng trung tâm |
| COMP-F | Framed — nhân vật được khung bởi yếu tố cảnh (cửa, cây, hang) |
| COMP-L | Leading lines — đường dẫn từ rìa frame vào nhân vật |
| COMP-NEG | Negative space lớn — nhân vật nhỏ, nhiều khoảng trống |
| COMP-LAYER | Layered depth — tiền / trung / hậu cảnh rõ 3 lớp |

**Tỷ lệ / Scale:**
| Code | Mô tả |
|------|-------|
| SC-NORMAL | Nhân vật tỷ lệ tự nhiên với môi trường |
| SC-SMALL | Nhân vật nhỏ bé trong thế giới to lớn |
| SC-GIANT | Vật thể / sinh vật khổng lồ bên cạnh nhân vật bình thường |
| SC-INVERT | Đảo ngược scale — vật nhỏ hoá thành khổng lồ |

---

## CHIỀU 11 — MẬT ĐỘ CHI TIẾT & TRẠNG THÁI MÔI TRƯỜNG (Density & Atmosphere)

**Mật độ chi tiết trong frame:**
| Code | Mô tả |
|------|-------|
| DD-SPARSE | Tối giản — ít vật thể, nhiều khoảng trống |
| DD-MEDIUM | Cân bằng — đủ chi tiết không rối mắt |
| DD-RICH | Dày đặc — mọi góc đều có thứ để nhìn |

**Trạng thái môi trường (phối hợp với CHIỀU 6):**
| Code | Mô tả |
|------|-------|
| ATM-STILL | Tĩnh lặng — không khí đứng, nước phẳng |
| ATM-BREEZE | Gió nhẹ — lá bay, váy phấp phới |
| ATM-MIST | Sương mù / mây khói phủ |
| ATM-WET | Mưa / ẩm — bề mặt phản chiếu, nước đọng |
| ATM-DRY | Khô hanh — bụi bay, ánh sáng sắc nét |
| ATM-SNOW | Tuyết rơi / đóng băng |

---

## TRACKING SHEET — Dán vào khi bắt đầu mỗi batch

```
BATCH TRACKER ─ [TÊN CẢNH / CÂU HÁT: _____________________]
Style file: _______________  |  Số ảnh target: ___
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      C    W      AP  CO  ENV AR  TW   L   ACT  SZ+CA+PV       COMP       ATM
IMG1: _    _____  _   _   _   _   __   __  ___  ___+___+___    ______     ______
IMG2: _    _____  _   _   _   _   __   __  ___  ___+___+___    ______     ______
IMG3: _    _____  _   _   _   _   __   __  ___  ___+___+___    ______     ______
IMG4: _    _____  _   _   _   _   __   __  ___  ___+___+___    ______     ______
IMG5: _    _____  _   _   _   _   __   __  ___  ___+___+___    ______     ______
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECK W-code:  W-SOLO ≤ 2 lần? [ ]   Có ≥1 W-CROWD/W-PET/W-ANIMAL? [ ]
CHECK C-code:  Dùng ≥ 3 code khác nhau? [ ]
CHECK TW-code: Dùng ≥ 3 code khác nhau? [ ]
CHECK combo SZ+CA: Không 2 ảnh giống nhau? [ ]
```

---

## QUY TRÌNH AGENT (Quick Reference)

```
BƯỚC 1  Đọc STYLE file được chỉ định → nắm ngôn ngữ vật liệu bất biến
BƯỚC 2  Đọc lyrics / music file → chia câu hát thành SCENES (mỗi scene = 1 cảm xúc cốt lõi)
BƯỚC 3  Với mỗi scene → lập TRACKING SHEET trước khi viết prompt
BƯỚC 4  Gán combo 11+1 chiều (thêm W-code) cho từng ảnh — mỗi ảnh khác ≥ 3 chiều so với ảnh trước
BƯỚC 5  Dịch combo → prompt text theo template của style file (giữ nguyên BASE DNA + SUFFIX)
BƯỚC 6  Kiểm tra: W-SOLO ≤ 2/5, có ≥1 W-CROWD/W-PET/W-ANIMAL, không vi phạm blacklist
BƯỚC 7  Xuất prompt list
```

---

## 7 LỖI PHỔ BIẾN NHẤT

| Lỗi | Hậu quả | Fix |
|-----|---------|-----|
| Toàn batch dùng CA-EYE + SZ-M | Mọi ảnh trông giống nhau | Xoay vòng ít nhất 4 combo góc khác |
| Toàn batch ánh sáng L-1 overcast | Batch buồn tẻ, không năng lượng | Xen kẽ golden hour + ánh đèn ấm |
| Không thay đổi biểu cảm | Nhân vật như robot | Lên lịch biểu cảm trước khi viết prompt |
| ENV code giống nhau cả batch | Nhân vật như không di chuyển | Thay ENV ít nhất 3 lần / 5 ảnh |
| Quên màu đặc trưng style | Mất nhận dạng thương hiệu | Luôn giữ 1 màu neo của style |
| **Toàn batch W-SOLO** | **Thế giới trông như sa mạc không người** | **Bắt buộc ≥1 W-CROWD/W-PET/W-ANIMAL mỗi batch** |
| **Anchor bias từ lyrics buồn → chỉ 1 nhân vật** | **215 ảnh na ná nhau, thiếu sức sống** | **Cảm xúc đơn độc → atmosphere, không phải W-code** |

Biến số tuỳ style — agent ưu tiên lấy từ SLOT A của style file hiện tại.  
Nếu style không có slot, chọn từ pool sau:

| Code | Mô tả |
|------|-------|
| AP-1 | Trẻ / thanh thiếu niên |
| AP-2 | Trung niên |
| AP-3 | Người cao tuổi |
| AP-4 | Trẻ em (6–12 tuổi) |
| AP-5 | Nhân vật phi giới tính / trung tính |

**Quy tắc:** Không dùng cùng một age range quá 2 lần trong 1 batch 5 ảnh.

---

## CHIỀU 3 — TRANG PHỤC & PHỤ KIỆN (Costume & Accessories)

Trang phục ưu tiên lấy từ SLOT B của style file (nếu có).  
Nếu không — đa dạng theo nhóm sau:

| Code | Nhóm | Gợi ý |
|------|------|-------|
| CO-1 | Nhẹ nhàng / thường ngày | áo đơn, váy đơn giản |
| CO-2 | Nghi lễ / trang trọng | áo choàng, trang phục đặc biệt |
| CO-3 | Dày dặn / nhiều lớp | áo khoác dài + khăn + mũ |
| CO-4 | Cởi bỏ bớt lớp / tự nhiên | áo ngắn, tay trần |
| CO-5 | Phụ kiện là điểm nhấn chính | nón lớn, balo, dù, đèn lồng |

**Đạo cụ xoay vòng (mỗi ảnh 1 đạo cụ khác nhau):**  
Batch 5: sách · giỏ · đèn lồng · nhạc cụ · hoa  
Batch 10: + gương · bản đồ · chìa khoá · vật kỷ niệm · con vật nhỏ đi kèm

---

## CHIỀU 4 — CẢNH VẬT & MÔI TRƯỜNG (Environment)

| Code | Loại | Mô tả |
|------|------|-------|
| ENV-1 | Nội thất ấm áp | trong nhà, ánh đèn, không gian nhỏ |
| ENV-2 | Ngoại thất tự nhiên — mở | đồng nội, biển, núi, bầu trời rộng |
| ENV-3 | Ngoại thất tự nhiên — hẹp | hẻm núi, rừng rậm, hang động, lạch nước |
| ENV-4 | Không gian nhân tạo đời thường | phố, chợ, bến cảng, đường làng |
| ENV-5 | Không gian chuyển tiếp | cầu, cổng, cửa, ngưỡng cửa, bến đò |
| ENV-6 | Không gian trên cao | mái nhà, vách núi, tháp, ngọn đồi |
| ENV-7 | Không gian dưới thấp | lòng giếng, tầng hầm, dưới tán cây khổng lồ |

**Quy tắc:** Trong 1 batch 7 ảnh → không dùng ENV code nào quá 2 lần.

---

## CHIỀU 5 — KIẾN TRÚC (Architecture Density)

Lượng kiến trúc xuất hiện trong frame — độc lập với ENV.

| Code | Mô tả |
|------|-------|
| AR-0 | Không kiến trúc — thiên nhiên thuần tuý |
| AR-1 | Kiến trúc nhỏ — 1 yếu tố (cánh cửa, cột đèn, giếng) |
| AR-2 | Kiến trúc vừa — 1 công trình (nhà, cầu, tháp) |
| AR-3 | Kiến trúc dày — cả khu (làng, phố, quảng trường) |
| AR-4 | Kiến trúc bị thiên nhiên nuốt chửng / hoang phế |

---

## CHIỀU 6 — THỜI GIAN & THỜI TIẾT (Time & Weather)

| Code | Mô tả | Tông màu bầu trời |
|------|-------|------------------|
| TW-1 | Bình minh / sương sớm | hồng tím, cam nhạt |
| TW-2 | Ban ngày trong xanh | xanh da trời, trắng mây |
| TW-3 | Ban ngày흐리 / mây phủ | xám bạc, khuếch tán |
| TW-4 | Hoàng hôn | cam đỏ, vàng cháy |
| TW-5 | Chạng vạng / blue hour | xanh navy sâu |
| TW-6 | Đêm — ánh sao / trăng | xanh đen, bạc |
| TW-7 | Đêm — ánh đèn nhân tạo | vàng ấm, lung linh |
| TW-8 | Mưa / sau mưa | phản chiếu, ẩm ướt |
| TW-9 | Tuyết / sương giá | trắng tinh, tĩnh lặng |
| TW-10 | Gió mạnh | tóc bay, vạt áo phấp phới |

**Quy tắc:** Batch 5 ảnh → ít nhất 3 code TW khác nhau. Batch 10 → ít nhất 5 code TW.

---

## CHIỀU 7 — ÁNH SÁNG & PALETTE MÀU (Lighting & Color)

**Nguồn sáng:**
| Code | Mô tả | Kelvin |
|------|-------|--------|
| L-1 | Khuếch tán mềm — overcast | 5500–6500K |
| L-2 | Nắng vàng xiên — golden hour | 3200–4000K |
| L-3 | Đèn dầu / dây tóc — indoor glow | 2200–2400K |
| L-4 | Rim light / backlit — ngược sáng | tuỳ background |
| L-5 | Ánh sáng từ dưới lên — campfire | 2000–2800K |
| L-6 | Ánh trăng / sao lạnh | 5000–8000K |
| L-7 | Ánh sáng lọc qua tán cây — dappled | 4000–5000K |
| L-8 | Ánh nước phản chiếu | lạnh + lung linh |

**Palette chủ đạo:**
| Code | Palette | Cảm xúc |
|------|---------|---------|
| P-warm | Amber, ochre, rust, cream | Ấm áp, hoài niệm |
| P-cool | Navy, slate, mist, silver | Tĩnh lặng, xa xôi |
| P-earth | Brown, moss, clay, sand | Gần gũi, chân thực |
| P-vivid | Crimson, cobalt, gold | Kịch tính, mạnh mẽ |
| P-muted | Dusty rose, sage, ivory | Nhẹ nhàng, thơ mộng |

**Quy tắc:** Không dùng cùng L-code quá 2 lần / batch. Không dùng cùng P-code quá 2 lần / batch.

---

## CHIỀU 8 — HÀNH ĐỘNG & BIỂU CẢM (Action & Expression)

**Hành động — 4 nhóm:**
| Nhóm | Code | Mô tả |
|------|------|-------|
| Tĩnh | ACT-S1 | Đứng ngắm / quan sát |
| | ACT-S2 | Ngồi nghỉ / đọc / uống trà |
| | ACT-S3 | Nằm / dựa / thả lơi |
| Chuyển động chậm | ACT-M1 | Đi bộ / dạo bước |
| | ACT-M2 | Với tay / chạm nhẹ vào thứ gì đó |
| | ACT-M3 | Nhìn về phía sau / quay đầu |
| Chuyển động mạnh | ACT-D1 | Chạy / nhảy / nhảy múa |
| | ACT-D2 | Làm việc tay chân / gánh / kéo |
| | ACT-D3 | Tung hứng / biểu diễn |
| Tương tác | ACT-I1 | Tương tác với vật thể (cầm, đặt, mở) |
| | ACT-I2 | Tương tác với sinh vật / con vật |
| | ACT-I3 | Tương tác với người khác (đưa tay, ôm, nhìn nhau) |
| | ACT-I4 | Tương tác với thiên nhiên (nước, gió, lá) |

**Biểu cảm — xoay vòng 7 trạng thái:**  
bình yên → suy tư → vui tươi → ngạc nhiên → nhớ thương → tập trung → mơ màng

**Quy tắc:** Trong 5 ảnh → ít nhất 2 nhóm ACT khác nhau. Không dùng cùng biểu cảm quá 2 lần.

---

## CHIỀU 9 — GÓC MÁY & CỠ CẢNH (Camera Angle & Shot Size)

**ĐÂY LÀ CHIỀU QUAN TRỌNG NHẤT.** Nhiều batch thất bại vì toàn dùng medium-shot thẳng góc.

### Cỡ cảnh:
| Code | Tên | Mô tả |
|------|-----|-------|
| SZ-EW | Extreme Wide | Nhân vật rất nhỏ, cảnh chiếm 80%+ frame |
| SZ-W | Wide | Thấy toàn thân nhân vật rõ |
| SZ-M | Medium | Ngang thắt lưng trở lên |
| SZ-CU | Close-Up | Mặt + vai hoặc chi tiết cụ thể |
| SZ-XCU | Extreme Close-Up | 1 chi tiết duy nhất (đôi tay, đôi mắt) |
| SZ-OTS | Over-the-Shoulder | Nhìn qua vai vào cảnh trước mặt |

### Góc máy:
| Code | Mô tả |
|------|-------|
| CA-EYE | Ngang tầm mắt — trung tính |
| CA-LOW | Góc thấp / worm's eye — nhìn lên |
| CA-HIGH | Góc cao / bird's eye — nhìn xuống |
| CA-DUTCH | Nghiêng frame — dynamic / dramatic |
| CA-BEHIND | Nhìn từ sau lưng nhân vật |
| CA-AERIAL | Toàn cảnh từ trên không |

### Góc nhìn:
| Code | Mô tả |
|------|-------|
| PV-FRONT | Nhân vật nhìn thẳng vào camera |
| PV-PROFILE | Nhân vật nhìn nghiêng 90 độ |
| PV-3QTR | Quarter turn — ba phần tư |
| PV-AWAY | Nhân vật quay lưng / nhìn đi chỗ khác |

**Mỗi ảnh trong batch = combo [SZ + CA + PV] chưa dùng trong batch đó.**

**Phân bổ chuẩn — batch 5 ảnh:**
```
Ảnh 1: SZ-EW  + CA-HIGH   + PV-AWAY    → mở cảnh hoành tráng
Ảnh 2: SZ-W   + CA-EYE    + PV-PROFILE → giới thiệu nhân vật
Ảnh 3: SZ-M   + CA-LOW    + PV-3QTR    → cảm xúc đẩy lên
Ảnh 4: SZ-CU  + CA-EYE    + PV-FRONT   → cận mặt / đỉnh điểm
Ảnh 5: SZ-W   + CA-BEHIND + PV-AWAY    → đóng cảnh / ra đi
```

**Mở rộng — batch 10 ảnh:**
```
Ảnh 6:  SZ-OTS + CA-EYE    + PV-FRONT   → POV nhân vật phụ
Ảnh 7:  SZ-EW  + CA-AERIAL + PV-AWAY    → toàn cảnh từ trên không
Ảnh 8:  SZ-M   + CA-DUTCH  + PV-3QTR    → góc dramatic
Ảnh 9:  SZ-XCU + CA-EYE    + PV-FRONT   → chi tiết cực cận
Ảnh 10: SZ-W   + CA-LOW    + PV-PROFILE → khép lại hùng tráng
```

---

## CHIỀU 10 — BỐ CỤC & TỶ LỆ KHÔNG GIAN (Composition & Scale)

**Bố cục:**
| Code | Mô tả |
|------|-------|
| COMP-R3 | Rule of thirds — nhân vật lệch sang 1/3 frame |
| COMP-C | Centered / symmetry — đối xứng trung tâm |
| COMP-F | Framed — nhân vật được khung bởi yếu tố cảnh (cửa, cây, hang) |
| COMP-L | Leading lines — đường dẫn từ rìa frame vào nhân vật |
| COMP-NEG | Negative space lớn — nhân vật nhỏ, nhiều khoảng trống |
| COMP-LAYER | Layered depth — tiền / trung / hậu cảnh rõ 3 lớp |

**Tỷ lệ / Scale:**
| Code | Mô tả |
|------|-------|
| SC-NORMAL | Nhân vật tỷ lệ tự nhiên với môi trường |
| SC-SMALL | Nhân vật nhỏ bé trong thế giới to lớn |
| SC-GIANT | Vật thể / sinh vật khổng lồ bên cạnh nhân vật bình thường |
| SC-INVERT | Đảo ngược scale — vật nhỏ hoá thành khổng lồ |

---

## CHIỀU 11 — MẬT ĐỘ CHI TIẾT & TRẠNG THÁI MÔI TRƯỜNG (Density & Atmosphere)

**Mật độ chi tiết trong frame:**
| Code | Mô tả |
|------|-------|
| DD-SPARSE | Tối giản — ít vật thể, nhiều khoảng trống |
| DD-MEDIUM | Cân bằng — đủ chi tiết không rối mắt |
| DD-RICH | Dày đặc — mọi góc đều có thứ để nhìn |

**Trạng thái môi trường (phối hợp với CHIỀU 6):**
| Code | Mô tả |
|------|-------|
| ATM-STILL | Tĩnh lặng — không khí đứng, nước phẳng |
| ATM-BREEZE | Gió nhẹ — lá bay, váy phấp phới |
| ATM-MIST | Sương mù / mây khói phủ |
| ATM-WET | Mưa / ẩm — bề mặt phản chiếu, nước đọng |
| ATM-DRY | Khô hanh — bụi bay, ánh sáng sắc nét |
| ATM-SNOW | Tuyết rơi / đóng băng |

---

## TRACKING SHEET — Dán vào khi bắt đầu mỗi batch

```
BATCH TRACKER ─ [TÊN CẢNH / CÂU HÁT: _____________________]
Style file: _______________  |  Số ảnh target: ___
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      C   AP  CO  ENV AR  TW   L   ACT  SZ+CA+PV            COMP       ATM
IMG1: _   _   _   _   _   __   __  ___  ___+______+___       ______     ______
IMG2: _   _   _   _   _   __   __  ___  ___+______+___       ______     ______
IMG3: _   _   _   _   _   __   __  ___  ___+______+___       ______     ______
IMG4: _   _   _   _   _   __   __  ___  ___+______+___       ______     ______
IMG5: _   _   _   _   _   __   __  ___  ___+______+___       ______     ______
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECK: Mỗi cột ≥ 3 giá trị khác nhau? [ ] Có   [ ] Chưa — cần điều chỉnh
```

---

## QUY TRÌNH AGENT (Quick Reference)

```
BƯỚC 1  Đọc STYLE file được chỉ định → nắm ngôn ngữ vật liệu bất biến
BƯỚC 2  Đọc lyrics / music file → chia câu hát thành SCENES (mỗi scene = 1 cảm xúc cốt lõi)
BƯỚC 3  Với mỗi scene → lập TRACKING SHEET trước khi viết prompt
BƯỚC 4  Gán combo 11 chiều cho từng ảnh — mỗi ảnh khác ≥ 3 chiều so với ảnh trước
BƯỚC 5  Dịch combo → prompt text theo template của style file (giữ nguyên BASE DNA + SUFFIX)
BƯỚC 6  Kiểm tra: không combo nào trùng, không vi phạm blacklist / negative của style
BƯỚC 7  Xuất prompt list
```

---

## 5 LỖI PHỔ BIẾN NHẤT

| Lỗi | Hậu quả | Fix |
|-----|---------|-----|
| Toàn batch dùng CA-EYE + SZ-M | Mọi ảnh trông giống nhau | Xoay vòng ít nhất 4 combo góc khác |
| Toàn batch ánh sáng L-1 overcast | Batch buồn tẻ, không năng lượng | Xen kẽ golden hour + ánh đèn ấm |
| Không thay đổi biểu cảm | Nhân vật như robot | Lên lịch biểu cảm trước khi viết prompt |
| ENV code giống nhau cả batch | Nhân vật như không di chuyển | Thay ENV ít nhất 3 lần / 5 ảnh |
| Quên màu đặc trưng style | Mất nhận dạng thương hiệu | Luôn giữ 1 màu neo của style (ví dụ: butter-yellow Coslient) |
