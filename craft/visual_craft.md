# 🎨 VISUAL CRAFT — BỘ SINH KHO NGUYÊN LIỆU THỊ GIÁC (VISUAL POOL GENERATOR)
v9.0 — Ponytail Montage Edition

> **Bản chất của file này:**
> `visual_craft.md` là cẩm nang tạo ra **kho ảnh nguyên liệu đa dạng (~30–40 prompts)** trong file `image.txt` để tool (`dola-auto-download`) tải về, phục vụ việc dựng phim tự do (Montage) trên timeline.
>
> 🔒 **Không còn phụ thuộc vào bảng Storyboard:**
> - Nhận trực tiếp cảm hứng từ **Không gian & Móc neo** ở `1-idea.md`.
> - Kết hợp với **Chất liệu mỹ thuật & Style Suffix** từ file phong cách được chọn trong `style/`.
> - Bắn phá trực tiếp ra danh sách prompt sạch trong `image.txt`.

---

## 1. CÔNG THỨC ĐA DẠNG HÓA KHO ẢNH (BẬC THANG CỠ CẢNH)

Để phòng dựng (Edit) có đủ nguyên liệu phong phú và tránh cảnh nào cũng giống cảnh nào, danh sách 30–40 prompts trong `image.txt` bắt buộc phải trải đều qua **4 nhóm lát cắt**:

1. **Toàn cảnh không gian (Wide / Establishing — ~25% số ảnh):**
   * Thiết lập thế giới bao la: Toàn cảnh thị trấn mờ sương, bến thuyền lúc hoàng hôn, ngọn đồi dốc đá, con đường làng quanh co.
2. **Trung cảnh sinh hoạt đời thường (Medium / Human slices — ~35% số ảnh):**
   * Sinh khí cuộc sống bình dị: Bóng lưng người quét lá, tiệm bánh sáng đèn than củi, người ngồi đọc sách bên hiên, ai đó dắt xe đạp qua cầu đá. Không soi cận mặt, giữ người như một phần hòa vào cảnh vật.
3. **Cận cảnh xúc giác & tĩnh vật (Close-up / Sensory Anchors — ~25% số ảnh):**
   * Đánh thức giác quan: Tách trà gốm bốc khói trên bậu cửa sổ gỗ, chuông gió lay nhẹ, đôi bàn tay già nua gọt táo, vệt nắng rọi trên cuốn sách cũ, mèo cuộn tròn sưởi nắng.
4. **Lát cắt thơ mộng / Siêu thực nhẹ nhàng (Poetic Whimsy slices — ~15% số ảnh):**
   * Điểm xuyết chất thơ kỳ lạ (tham chiếu [`craft/plugins/plugin_surreal_whimsy.md`](./plugins/plugin_surreal_whimsy.md)): Chiếc ghế gỗ đặt trên mỏm đá ngắm sóng, giường treo nhẹ dưới tán cây đại thụ, thuyền gỗ nhỏ nằm giữa đồng hoa cúc vàng.

---

## 2. CÔNG THỨC GHÉP NỐI PROMPT (ASSEMBLY RULES)

Mỗi prompt trong `image.txt` được cấu thành từ 4 mảnh ghép:

```text
[Cỡ cảnh & Góc máy] + [Chủ thể / Lát cắt hành động / Bối cảnh] + [Ánh sáng & Không khí] + [Style Suffix bắt buộc từ style/*.md] + [--ar 16:9]
```

### Ví dụ minh họa:
* **Toàn cảnh:**
  `An extreme wide shot, eye-level view of a peaceful coastal village at dusk, cobblestone slope leading to the sea, soft warm incandescent lights from old wooden cottages, distant lighthouse beam in the mist. Handcrafted tactile diorama style, miniature felt and carved wood texture, soft warm ambient lighting, volumetric fog, stop-motion animation aesthetic, 8k resolution. --ar 16:9`
* **Cận cảnh:**
  `A cozy close-up shot, 45-degree angle of a rustic ceramic mug steaming on an aged wooden windowsill, soft autumn morning light filtering through linen curtains, wild chamomile flowers in a glass jar. Handcrafted tactile diorama style, tangible woolen and clay textures, shallow depth of field, warm cozy atmosphere. --ar 16:9`

---

## 3. BỘ KIỂM TRA LỖI KỸ THUẬT (TOOL VALIDATION GATE)

Trước khi đưa `image.txt` vào tool tự động tải ảnh (`dola-auto-download`), bắt buộc kiểm tra 5 tiêu chí:

- [ ] **Định dạng 1 dòng:** Mỗi prompt nằm trọn vẹn trên **1 dòng duy nhất** (không bấm xuống dòng `\n` bên trong prompt).
- [ ] **Khoảng cách dòng:** Giữa 2 prompt liên tiếp cách nhau đúng **1 dòng trống** (chuẩn tool download).
- [ ] **Số lượng đủ giàu:** Tối thiểu 30–40 prompts để phòng dựng có đủ sự lựa chọn ngẫu hứng.
- [ ] **Sạch cú pháp:** Không có 2 dấu phẩy cạnh nhau (`, ,`), không thừa dấu phẩy ở cuối câu, không dùng cờ `--no` thừa thãi.
- [ ] **Cờ tỷ lệ chuẩn:** 100% prompt đều có cờ tỷ lệ video ở cuối cùng: `--ar 16:9`.
