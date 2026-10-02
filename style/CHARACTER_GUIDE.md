# Character Creation Guide

> 💡 **PHẠM VI ÁP DỤNG:**
> Hướng dẫn này **CHỈ ÁP DỤNG khi dự án chọn style [`style/IMAGE_STYLE.md`](./IMAGE_STYLE.md)**.
> Tuyệt đối **KHÔNG ÁP DỤNG** khi dự án chọn [`style/STYLE_handcrafted_tactile_diorama.md`](./STYLE_handcrafted_tactile_diorama.md) (vì style thủ công mô tả trực tiếp, không dùng bảng nhân vật).

Tài liệu quy chuẩn cấu trúc, định dạng (format) và **nguyên tắc đa dạng hóa nhân vật** cho AI thực thi.

---

## 1. Triết lý Thiết kế: Kì quặc nhẹ (Quirky) + Thiện cảm & Đẹp (Wholesome & Aesthetic)

Nhân vật búp bê stop-motion cần có cá tính hóm hỉnh độc đáo nhưng luôn giữ được mỹ cảm và thiện cảm:
- **Cá tính độc đáo (Charmingly Quirky):** Mỗi nhân vật sở hữu một dấu ấn nhận diện giải phẫu riêng biệt, không trùng lặp.
- **Thần thái thiện cảm (Wholesome & Expressive):** Gương mặt toát lên nét nhân văn, ấm áp, tạo cảm giác tin cậy và yêu mến; cảm xúc biến chuyển linh hoạt theo cốt truyện (từ hiền từ, sâu lắng, hóm hỉnh đến trầm ngâm, xúc động).
- **Mỹ cảm điêu khắc (Aesthetically Pleasing):** Đường nét điêu khắc hài hòa, da đất sét polymer mịn màng với độ tán xạ ánh sáng ấm (`warm soft subsurface scattering`).
- **Ranh giới cấm:** Tuyệt đối cấm tạo hình dị hợm, quái đản, biến dạng ghê rợn hay nét mặt độc ác (cấm `ugly, grotesque, creepy, deformed, angry`).

---

## 2. Quy chuẩn Đa dạng hóa Nhân vật (Diversity Standards)

Để tránh tình trạng các nhân vật bị "nhân bản" giống nhau, AI thực thi bắt buộc áp dụng 4 nguyên tắc đa dạng hóa sau:

### A. Nguyên tắc Tương phản Đa nhân vật (Multi-Character Contrast Rule)
* Khi có từ 2 nhân vật trở lên trong một dự án, **bắt buộc phải có sự phân hóa rõ rệt** về:
  1. Chiều cao số học chênh lệch thực tế.
  2. Phom dáng hình thể (ví dụ: người cao gầy đứng cạnh người đậm đà, người thanh thoát đứng cạnh người chắc nịch).
  3. Hình khối khuôn mặt đối lập.
  4. Vị trí đặt nét độc đáo (người nhấn ở mũi, người nhấn ở tóc, người nhấn ở gò má/mắt, người nhấn ở phụ kiện).

### B. Phổ Đa dạng Hình thể (Body Morphology Spectrum)
* AI thực thi tự do phát triển bất kỳ phom người nào phù hợp với xuất thân, lứa tuổi và tính cách nhân vật (gầy guộc, cao kều, vạm vỡ, đậm đà, chắc nịch đến tròn trịa phúc hậu).
* **Rào chắn kỹ thuật bắt buộc (để khóa tỷ lệ, chống lùn/chibi):**
  * Chiều cao cụ thể bằng số: `[X]cm tall`.
  * Tỉ lệ đầu/thân người lớn: Khóa trong dải `6.8` đến `7.5-heads-tall` (trẻ em: `5.5-heads-tall`). CẤM tỉ lệ dưới 5.5 đầu.
  * Luôn có cổ rõ ràng: `defined visible neck` (hoặc `defined slender neck`, tránh dán đầu sát ngực).

### C. Phổ Đa dạng Nét độc đáo (Quirk Spectrum)
* Nét nhận diện độc đáo phân bổ tự do, không đóng khung vào một bộ phận cố định:
  * *Tỷ lệ diện mạo:* Bất kỳ hình khối mặt nào hài hòa với tính cách.
  * *Ngũ quan:* Đa dạng cấu trúc sống mũi, dáng vành tai, đường cung chân mày, hình dáng khóe mắt, khuôn miệng.
  * *Đặc điểm bề mặt:* Vết tàn nhang nhẹ, nếp nhăn cười sâu, lúm đồng tiền, râu tóc tơ đất sét đặc trưng.
  * *Dấu ấn nghề nghiệp & lối sống:* Kính mắt mộc mạc, phụ kiện tóc thủ công, dấu ấn lao động trên bàn tay.

### D. Phổ Thần thái & Cảm xúc (Aura & Expression Spectrum)
* Cảm xúc biến chuyển linh hoạt theo vai trò và hoàn cảnh từng cảnh:
  * Từ đôn hậu hiền từ, trầm tĩnh sâu lắng, hóm hỉnh tếu táo, dịu dàng e ấp đến năng động hoạt bát hay ngây thơ thuần khiết.

---

## 3. Cấu trúc chuẩn của `character.txt`

Mỗi nhân vật được định nghĩa bằng đúng 4 dòng theo cú pháp chuẩn sau:

```text
@<tag_nhân_vật>
FIXED: <định_dạng_nhân_dạng_và_khung_xương_bất_biến>
DEFAULT HAIR: <định_dạng_kiểu_tóc_mặc_định>
DEFAULT OUTFIT: <định_dạng_trang_phục_mặc_định>
```

---

## 4. Quy chuẩn Format tinh gọn từng dòng

### A. Dòng `FIXED` (Gồm 3 khối thông tin cốt lõi — súc tích, chống loãng token)

```text
FIXED: [Khối 1: Nhân dạng & Khung xương số học], [Khối 2: Diện mạo, Nét riêng & Thần thái], [Khối 3: Tông da, Tóc & Bàn tay điêu khắc]
```

* **Khối 1 (Nhân dạng & Khung xương):**
  `a [Tuổi]-year-old [Sắc tộc] [Giới tính], [X]cm tall, [X]-heads-tall body proportion, defined visible neck, [phom dáng hình thể tự do: gầy/đậm/tròn/thanh mảnh/thể thao] with [proportional / slightly elongated limbs], [tư thế tự nhiên]`
* **Khối 2 (Diện mạo, Nét riêng & Thần thái):**
  `[hình khối mặt] with [1-2 nét quirky độc đáo riêng], [đặc điểm mắt & thần thái/cảm xúc chủ đạo], [khóe môi & nét cười thiện cảm]`
* **Khối 3 (Tông da, Tóc & Bàn tay điêu khắc):**
  `smooth painted skin with soft warm undertones, continuous organic arms with natural seamless wrists, [màu & kết cấu tóc sợi tơ tự nhiên tách lớp (natural fiber hair with fine separated strands; người già bắt buộc zero baldness hoặc đội mũ mộc)], expressive hands with smooth painted finish, [phụ kiện cố định nếu có]`

---

### B. Dòng `DEFAULT HAIR`
* Cú pháp: `[Độ dài] [Kiểu dáng tạo hình sợi tóc tự nhiên tách lớp (natural fiber hair with fine separated strands); người lớn tuổi thêm zero baldness]`

---

### C. Dòng `DEFAULT OUTFIT`
* Cú pháp: `[Chất liệu vải mộc] [Màu sắc] [Kiểu dáng trang phục thường ngày có cấu trúc may đo] [Fit], [Kiểu quần/váy có cúc/thắt lưng/chiết eo], [Giày dép mộc], [Phụ kiện đi kèm]`
* **Chất liệu cho phép:** Vải dệt tự nhiên (cotton, linen, denim, canvas, chambray, cotton flannel, twill, nỉ dạ tweed).
* **LUẬT CẤM:**
  - CẤM đồ len móc sợi to, đồ đan nổi cục (chunky knit, crochet, amigurumi) gây biến dạng thành búp bê len.
  - CẤM áo thụng trung cổ (smock) và váy bao tải suông đuỗn. Trang phục phải là đồ thường ngày có phom dáng rõ ràng: sơ mi cài cúc, áo polo, quần chinos/jeans, váy chiết eo.
