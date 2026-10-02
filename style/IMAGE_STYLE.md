# Image Style Reference

> 💡 **QUY TẮC NHÂN VẬT:**
> * Khi dự án chọn style này, **BẮT BUỘC tạo file `character.txt`** theo hướng dẫn tại [`style/CHARACTER_GUIDE.md`](./CHARACTER_GUIDE.md) với hệ thống `@tag`, cấu trúc FIXED + DEFAULT OUTFIT.
> * Các prompt trong `image.txt` sử dụng `@tag` nhân vật inline và ghép **Style Suffix A** (cảnh có người) hoặc **Style Suffix B** (cảnh không người) bên dưới.

## Style Suffix (bắt buộc — ghép cuối mọi prompt)

### A. Dành cho cảnh CÓ nhân vật:
```
whimsical handcrafted miniature diorama, smooth painted stop-motion figures, proportional head-to-body anatomy, defined neck, charmingly quirky yet endearing character design, aesthetically pleasing stylized features, finely crafted miniature details, warm soft subsurface scattering, non-photorealistic, shallow depth of field, 16:9
```

### B. Dành cho cảnh KHÔNG CÓ nhân vật (Phong cảnh sa bàn / Tĩnh vật):
*(Tự động lược bỏ các từ khóa giải phẫu người để tránh AI tự ý vẽ thêm đầu/người vào cảnh)*
```
whimsical handcrafted miniature diorama, sculpted matte polymer clay, finely crafted miniature details, warm soft subsurface scattering, non-photorealistic, shallow depth of field, 16:9
```

---

## Luật cấm

- **KHÔNG** trẻ em dưới 5 tuổi (không toddler, không baby, không infant)
- **KHÔNG** đầu to / nhân vật lùn / bobblehead / caricature / chibi / mất cổ / quái đản ghê rợn (không bobblehead, oversized head, big head, caricature, dwarf, gnome, chibi, squat body, 4-heads-tall, no neck, ugly, grotesque, creepy) — giữ khung xương cân đối theo tỷ lệ giải phẫu (proportional head-to-body anatomy), diện mạo thiện cảm và ưa nhìn (endearing, aesthetically pleasing)
- **KHÔNG** đồ đan móc len sợi to / búp bê len móc (không chunky knit, crochet, amigurumi, bulky knitted sweaters) — trang phục mùa đông ưu tiên nỉ dạ, vải tweed mộc, cotton flannel, canvas trần bông, denim dày; tránh các thớ len đan nổi cục khiến AI biến búp bê đất sét thành thú bông móc sợi
- **KHÔNG** tóc bết đất sét hoặc tự ý hói đầu (không dùng `clay hair`) — dùng sợi tơ tách lớp tự nhiên (`natural fiber hair with fine separated strands`); với nhân vật lớn tuổi bắt buộc khóa độ phủ tóc 100% (`full thick head of fiber hair with zero baldness`) hoặc đội mũ mộc (flat cap/beret)
- **KHÔNG** áo thụng trung cổ, áo bao tải vô phom (không dùng `smock`, không tả `linen dress` chung chung không phom) — trang phục đời thường phải có cấu trúc may đo rõ ràng: sơ mi cài cúc, áo polo, quần kaki/chinos có thắt lưng, váy chiết eo nhẹ, măng-sét cài khuy che cổ tay
- **KHÔNG** rãnh khớp búp bê / ngấn khớp cổ tay khuỷu tay — TUYỆT ĐỐI KHÔNG dùng các từ `joint`, `socket`, `unjointed`, `ball joint` (tránh bẫy từ khiến AI vẽ khớp). Luôn dùng câu khẳng định tự nhiên: `continuous organic arms, seamless smooth skin`
- **KHÔNG** chữ, nhãn, số, watermark trong ảnh (không text, labels, writing, letters, watermark trên background, chai lọ, kệ gỗ, thùng hàng)
- **KHÔNG** vật sắc nhọn (không dao, kéo, kim, đục, cưa, đinh, lưỡi dao, mũi khoan, dùi)
- **KHÔNG** đèn porch / porch light / lantern treo hiên (thay bằng đèn dây festoon, ánh sáng ấm từ khung cửa sổ)
- **KHÔNG** copper / kettle / ấm nước / bánh răng / gears / cogs
- **KHÔNG** người thật / photorealistic / hyperrealistic / 3D CGI render bóng bẩy (mọi nhân vật và bối cảnh phải rõ ràng là búp bê sa bàn đất sét thủ công)
- **KHI 2+ NHÂN VẬT TƯƠNG TÁC** (nắm tay, ôm, chạm) — tả rõ cả hai bên cùng kích cỡ/tuổi, không dùng "holding fingers" hay cách tả khiến một bên bị nhỏ thành trẻ con
- **MỖI PROMPT = 1 DÒNG DUY NHẤT** (không xuống dòng, không ngắt dòng)

---

## Shot Scale Guide

Cảnh càng gần → càng tả chi tiết bề mặt. Cảnh càng xa → tả không gian, bỏ chi tiết nhỏ.

| Shot | Tả gì | KHÔNG tả |
|------|-------|----------|
| **Wide / Establishing** | silhouette, tư thế, bối cảnh, thời tiết, ánh sáng tổng | da, texture vải, nếp nhăn tay |
| **Medium-wide** | hành động, trang phục tổng thể, biểu cảm lớn | nếp nhăn nhỏ, sợi tóc riêng lẻ |
| **Medium close-up** | biểu cảm rõ, chất liệu vải, kiểu tóc | vân tay, chi tiết da cực nhỏ |
| **Close-up** | nếp nhăn da, từng sợi tóc, texture vải dệt, vân gỗ | toàn cảnh phòng, bầu trời |
| **Extreme close-up macro** | nếp nhăn cực nhỏ, vân ngón tay, sợi chỉ, hạt bụi, subsurface glow | nhân vật toàn thân, bối cảnh rộng |

---

## Composition Formula

```text
[Shot], [Angle], [@tag_nhân_vật / Chủ thể] [ACTION / TƯ THẾ] in the mid-ground, [Background] beyond, [STYLE SUFFIX PHÙ HỢP]
```

* **Dùng @tag inline:** Đặt trực tiếp tại vị trí nhân vật hành động (ví dụ: `@walter smiling as he hands a ripe apple to @margaret`).
* **Cảnh cận (mặt/tay):** Tự động lược bỏ mô tả chân/giày để tránh giằng xé cỡ cảnh.
* **Cảnh không có người:** Dùng Style Suffix B (dành cho tĩnh vật/phong cảnh).

---

## Quy chuẩn Đa dạng hóa Bối cảnh, Ánh sáng & Bầu không khí

### 1. Đa dạng hóa Bối cảnh (Settings & Environments)
- **Tự do sáng tạo 100% theo cốt truyện:** Bối cảnh nội và ngoại cảnh hoàn toàn linh hoạt theo chủ đề bài hát và storyboard (nhà bếp cổ điển, phòng khách, xưởng chế tác, tiệm bánh, bến tàu làng chài, tiệm sách cũ, ngọn hải đăng, con đường làng, đồi hoa dại, thung lũng tuyết, hiên nhà mùa thu...).
- **Tính đồng nhất sa bàn (Diorama Consistency):** Mọi công trình, địa hình, cây cối và đạo cụ đều được thể hiện dưới dạng mô hình sa bàn tí hon chế tác thủ công tinh xảo từ đất sét polymer mờ, gỗ mộc, đá cuội, rêu khô, nước nhựa resin.

### 2. Đa dạng hóa Ánh sáng & Bầu không khí (Lighting & Atmosphere)
- Ánh sáng biến chuyển đa dạng theo nhịp cảm xúc:
  - *Bình minh:* ánh sáng tinh khôi, làn sương mỏng lãng đãng trôi.
  - *Ban ngày:* nắng ấm, vệt nắng xuyên qua tán cây, bóng đổ dịu nhẹ.
  - *Hoàng hôn:* ánh sáng vàng cam hổ phách rực rỡ, bóng ngả dài trên cỏ sa bàn.
  - *Đêm khuya:* ánh trăng bạc huyền ảo, dải đèn dây festoon vàng ấm, đốm lửa củi bập bùng, đom đóm lập lòe.
  - *Thời tiết:* mưa rào gõ nhẹ mặt kính, tuyết trắng phủ cành cây, gió mùa thu lay động lá vàng.
- **Ranh giới bất biến:** Tuyệt đối cấm đèn porch light / lantern treo hiên. Cấm mọi chi tiết kim loại bóng loáng hiện đại.
