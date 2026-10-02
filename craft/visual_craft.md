# 🔌 VISUAL CRAFT — BO MẠCH GHÉP NỐI PROMPT ẢNH (PROMPT COMPILER)
v8.0 — System Adapter Edition

> **Bản chất của file này:**
> `visual_craft.md` là **BO MẠCH CHỦ (Motherboard / Pipeline Adapter)** trong hệ thống sản xuất. Nó **KHÔNG quyết định nội dung câu chuyện** và **KHÔNG quyết định chất liệu mỹ thuật**.
>
> 🔒 **Phân định rạch ròi 3 tầng kiến trúc:**
> 1. [`storyboard_craft.md`](./storyboard_craft.md) = **ĐẠO DIỄN & BIÊN KỊCH:** Quyết định chuyện gì xảy ra, bối cảnh, cỡ cảnh (Toàn/Trung/Cận), cú máy và nhịp cắt.
> 2. `style/*.md` = **PHÒNG MỸ THUẬT (Art Department):** Quyết định chất liệu (len nỉ, đất sét, màu nước, 3D), giải phẫu nhân vật, luật cấm riêng và Master Prompt Template kèm Style Suffix.
> 3. `visual_craft.md` (file này) = **BỘ BIÊN DỊCH (Compiler):** Nhận dữ liệu từ Storyboard và Style, ghép nối chính xác thành file `image.txt` chuẩn cho Midjourney / AI Image Generator.

---

## ⚙️ 1. QUY TRÌNH VẬN HÀNH (COMPILATION PIPELINE)

Để tạo ra file `image.txt`, bo mạch thực hiện ghép nối 3 nguồn dữ liệu:

```text
[DỮ LIỆU TỪ STORYBOARD]          [DỮ LIỆU TỪ STYLE ĐƯỢC CHỌN]
Cột 4: Cỡ cảnh (Shot Scale)       Khuôn mẫu Master Prompt (Mẫu A hoặc B)
          +                                    +
Cột 5: Mô tả hành động/bối cảnh   Quy chuẩn nhân vật & Style Suffix
              │                                │
              └───────────────┬────────────────┘
                              ▼
                 [FILE ĐẦU RA: image.txt]
```

---

## 📋 2. CÔNG THỨC GHÉP NỐI (PROMPT ASSEMBLY RULES)

Với từng shot trong `storyboard.md`, bo mạch đọc Cột 4 và Cột 5 rồi nạp vào khuôn mẫu của file Style được chọn trong thư mục `style/`:

1. **Trường hợp cảnh CÓ nhân vật:**
   - Lấy Cỡ cảnh từ Cột 4 (ví dụ: `A close-up shot, eye-level angle`).
   - Lấy Chủ thể & Hành vi từ Cột 5.
   - Ghép theo **Mẫu A** của Style file (bổ sung giải phẫu/trang phục đặc thù của style đó).
   - Ghép **Style Suffix** bắt buộc ở cuối prompt.

2. **Trường hợp cảnh KHÔNG CÓ nhân vật (Phong cảnh / Tĩnh vật):**
   - Lấy Cỡ cảnh từ Cột 4 (ví dụ: `An extreme wide shot, high-angle view`).
   - Lấy Bối cảnh / Đồ vật từ Cột 5.
   - Ghép theo **Mẫu B** của Style file (tự động loại trừ các từ khóa giải phẫu người).
   - Ghép **Style Suffix** bắt buộc ở cuối prompt.

---

## 🛡️ 3. BỘ KIỂM TRA LỖI CÚ PHÁP (SYNTAX VALIDATION GATE)

Trước khi xuất file `image.txt`, bo mạch bắt buộc quét qua 5 điều kiện kỹ thuật:

- [ ] **Khóa số lượng dòng:** Số lượng prompt trong `image.txt` khớp chính xác 100% với số shot trong `storyboard.md` (ví dụ: 40 shot = đúng 40 prompt).
- [ ] **Định dạng 1 dòng:** Mỗi prompt nằm trên **1 dòng duy nhất** (không có ký tự xuống dòng `\n` bên trong một prompt).
- [ ] **Khoảng cách dòng:** Giữa 2 prompt liên tiếp cách nhau đúng **1 dòng trống**.
- [ ] **Sạch cú pháp:** Không có 2 dấu phẩy cạnh nhau (`, ,`), không thừa dấu phẩy ở cuối câu, không dùng câu lệnh negative (`--no`).
- [ ] **Cờ tỷ lệ khung hình:** 100% prompt đều có cờ tỷ lệ ở cuối cùng: `--ar 16:9`.
