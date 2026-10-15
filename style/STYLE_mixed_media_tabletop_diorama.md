# European Arthouse Stop-Motion World Style

## Mục lục nhanh

- **PHẦN I — DÀNH CHO AI VẬN HÀNH (PRODUCTION)**
  - [1. Bản chất thế giới, chất liệu và Điểm nhấn Siêu thực](#1-bản-chất-thế-giới-chất-liệu-và-điểm-nhấn-siêu-thực)
  - [2. Hệ thống cỡ cảnh, góc máy và điều tiết mật độ chi tiết](#2-hệ-thống-cỡ-cảnh-góc-máy-và-điều-tiết-mật-độ-chi-tiết)
  - [3. Tạo hình nhân vật, Điểm nhấn Trang phục/Tóc/Phụ kiện và Hành động Đời thường](#3-tạo-hình-nhân-vật-điểm-nhấn-trang-phụctócphụ-kiện-và-hành-động-đời-thường)
  - [4. Ánh sáng một nguồn thuận tự nhiên và bảng màu](#4-ánh-sáng-một-nguồn-thuận-tự-nhiên-và-bảng-màu)
  - [5. Cấu trúc Output Text Thuần (Mặc định cho AI Vận Hành)](#5-cấu-trúc-output-text-thuần-mặc-định-cho-ai-vận-hành)
  - [6. Quy trình tự kiểm tra trước khi xuất Prompt](#6-quy-trình-tự-kiểm-tra-trước-khi-xuất-prompt)
- **PHẦN II — DÀNH RIÊNG CHO NHÀ PHÁT TRIỂN (DEVELOPER R&D — AI VẬN HÀNH BỎ QUA)**
  - [7. Khung cấu trúc JSON nghiên cứu](#7-khung-cấu-trúc-json-nghiên-cứu)
  - [8. Giải thích nhiệm vụ từng trường JSON](#8-giải-thích-nhiệm-vụ-từng-trường-json)
  - [9. Quy tắc bảo trì tài liệu gốc](#9-quy-tắc-bảo-trì-tài-liệu-gốc)

---

# PHẦN I — DÀNH CHO AI VẬN HÀNH (PRODUCTION)

## 1. Bản chất thế giới, chất liệu và Điểm nhấn Siêu thực

Phong cách này dựng lại khung hình phim hoạt hình stop-motion nghệ thuật châu Âu (`Cinematic European arthouse stop-motion animation film still`) trên nền màu phim nhựa 35mm Kodak (`rich saturated Kodak analog 35mm film color grading with deep chromatic density`). Bối cảnh là thế giới sống rộng mở tràn qua bốn cạnh khung hình.

- **Điểm nhấn Môi trường Siêu thực & Tâm thái Thản nhiên (`Unbothered Surrealism`):** Mỗi bức ảnh tích hợp cơ chế siêu thực theo [`craft/plugins/plugin_surreal_whimsy.md`](../craft/plugins/plugin_surreal_whimsy.md) (Đảo lộn bối cảnh, Hoán đổi tỷ lệ vĩ mô, Thản nhiên giữa phi lý, Phương tiện hoài niệm, hoặc Vật chất hóa điều kỳ ảo). Điểm cốt lõi xuyên suốt gần như mọi bức ảnh là **sự thản nhiên trước điều phi lý**: khung cảnh mang yếu tố siêu thực kỳ lạ, nhưng nhân vật bên trong luôn thực hiện những cử chỉ, công việc sinh hoạt đời thường một cách bình thản như chuyện hiển nhiên hàng ngày.
- **Độ mềm bề mặt và độ trong không khí:** Toàn bộ bề mặt mang độ mịn mờ như nhung (`velvety matte surfaces with sfumato soft edges`), khóa `crystal-clear air` (hoặc `zero milky haze`) để giữ ống kính trong vắt và bảo toàn độ đậm màu.

## 2. Hệ thống cỡ cảnh, góc máy và điều tiết mật độ chi tiết

Hệ thống máy quay mở toàn bộ biên độ góc nhìn điện ảnh để phục vụ đúng ý đồ từng cảnh:
- **Đa dạng cỡ cảnh và góc máy:**
  - **Đại cảnh & Toàn cảnh rộng (`Extreme wide shot`, `Wide landscape / architectural shot`):** Mở rộng không gian nhiều lớp chiều sâu (tiền cảnh - trung cảnh - hậu cảnh), tôn vinh sự hùng vĩ của thiên nhiên, phố xá, công trình cùng hiện tượng siêu thực quy mô lớn.
  - **Cảnh toàn thân & Cảnh trung (`Full-body shot`, `Medium shot`, `Stage-planar shot`, `Orthographic front-on cross-section`):** Phù hợp cho tương tác nhân vật hoặc góc cắt ngang trực diện nhìn xuyên vào cấu trúc bên trong căn phòng, ngôi nhà, toa tàu.
  - **Cận cảnh & Đặc tả chi tiết (`Close-up`, `Extreme close-up / Macro detail shot`):** Tập trung vào biểu cảm gương mặt, đôi bàn tay đang thao tác, hoặc kết cấu vi mô của vật thể thủ công.
  - **Góc máy linh hoạt (`Eye-level`, `High-angle looking down`, `Low-angle looking up`, `Over-the-shoulder`, `Deep perspective`):** Tự do chọn góc đặt máy theo cảm xúc và bố cục không gian của từng cảnh.
- **Điều tiết mật độ chi tiết & Tách lớp chủ thể (`Optical Depth Separation`):**
  - Cho phép dựng cả những **không gian tối giản nhiều khoảng thở** lẫn những **không gian giàu chi tiết** (xưởng chế tác, thư viện ngập sách, khu vườn rậm rạp, góc bếp ấm cúng).
  - Luôn dùng tiêu cự quang học (`natural optical depth of field`, `creamy lens bokeh`) kết hợp độ tương phản sáng - tối để tách bật chủ thể chính và điểm nhấn siêu thực khỏi lớp nền phía sau.

## 3. Tạo hình nhân vật, Điểm nhấn Trang phục/Tóc/Phụ kiện và Hành động Đời thường

- **Linh hoạt số lượng chủ thể (Từ 0 đến nhiều nhân vật):** Khung hình có thể là cảnh tĩnh vật/kiến trúc/phong cảnh (không có người), cảnh 1 nhân vật, hoặc cảnh nhiều nhân vật tương tác.
- **Khung DNA chất liệu chung (Khi cảnh có người):** Nhân vật mang tỷ lệ cơ thể thanh mảnh kéo dài (`1:7.5 stylized arthouse proportions, never doll-like`), làn da bột giấy đúc mịn mờ mang sắc da ấm tự nhiên (`natural warm velvety matte molded paper-pulp skin with zero wrinkles`), mái tóc dày bồng bềnh nhiều sợi (`voluminous soft fibrous hair`), dáng điệu tự nhiên và chất vải mờ không đan len thô (`smooth matte clothing with zero chunky knitwear`). Định danh nhân vật bằng hình dáng và độ tuổi ước lượng bằng chữ (`slender young woman`, `compact-shouldered older man`, `taller softly rounded older woman`).
- **Hành động đời thường bình thản giữa khung cảnh phi lý (`Mundane Action in Surreal Setting`):** Nhân vật luôn thực hiện các hành động sinh hoạt đời thường, quen thuộc và điềm nhiên (`calm, unbothered everyday actions` như uống trà, đọc sách, cắt tóc, may vá, ôm nhau, ghi chép, phơi đồ, trò chuyện nhẹ nhàng), hoàn toàn coi hiện tượng siêu thực xung quanh là điều bình thường của cuộc sống.
- **Điểm nhấn Thị giác trên Nhân vật (`Character Visual Hook` — Linh hoạt giữa Trang phục, Tóc hoặc Phụ kiện):**
  - Mỗi nhân vật cần có ít nhất 1 điểm nhấn tạo hình thu hút ánh nhìn, chọn linh hoạt từ một hoặc kết hợp các yếu tố sau tùy theo ngữ cảnh:
    - **Điểm nhấn trên Trang phục (`Statement Garment`):** Phom dáng trang phục bay bổng (như tà váy dài vải lanh bung rộng trong gió, áo măng-tô dáng dài, tạp dề thợ thủ công, quần yếm vải thô) hoặc mảng màu trang phục tương phản nổi bật trên nền bối cảnh.
    - **Điểm nhấn ở Mái tóc & Mũ/Kính (`Hair & Headwear`):** Mái tóc sợi dày tạo khối ấn tượng (tóc xoăn xù lớn, tóc bạc pha đen gợn sóng, tóc tết bím dài) đi cùng mũ cói, mũ nồi dạ, khăn trùm đầu hoặc kính gọng mảnh.
    - **Điểm nhấn Phụ kiện gắn kết (`Storytelling Accessory`):** Phụ kiện mang tính kể chuyện hoặc kết nối tương tác tự nhiên theo đúng tình huống cảnh (dây tai nghe nghe chung, khăn choàng dài, máy ảnh cổ, túi đeo, nhạc cụ, giỏ mây...).
- **Tả chi tiết nhân vật thích ứng theo Cỡ cảnh (`Scale-Adaptive Character Detail`):**
  - **Ở cảnh Cận & Cảnh Trung (`Close-up` / `Medium shot`):** Tả rõ đường nét gương mặt cùng điểm nhấn trang phục/tóc/phụ kiện. Khi có từ 2 nhân vật trở lên, thiết kế mỗi người một cấu trúc xương mặt, dáng mũi, cằm và khung vai đối lập rõ rệt.
  - **Ở Toàn cảnh & Đại cảnh (`Wide` / `Extreme wide shot`):** Tập trung mô tả **phom dáng tổng thể (`silhouette`), chênh lệch chiều cao, mảng màu/chuyển động của trang phục, kiểu tóc/mũ lớn** để máy quay giữ đúng góc rộng, đồng thời giữ lộ rõ trọn vẹn đôi chân dài tỷ lệ `1:7.5` và bàn chân chạm mặt sàn (`with full legs and shoes clearly visible`).

## 4. Ánh sáng một nguồn thuận tự nhiên và bảng màu

- **Một nguồn sáng vật lý duy nhất (`Single Directional Key Light`):**
  - Toàn bộ khung hình chỉ dùng **duy nhất 1 nguồn sáng chính chiếu từ 1 hướng cố định**, tạo 1 hướng bóng đổ đồng nhất: phần hướng về nguồn sáng đón sáng trực tiếp, phần khuất sáng chuyển êm vào vùng bóng râm tự nhiên (`casting a single coherent natural shadow toward the unlit side`).
  - Cảnh ban ngày dùng hoàn toàn ánh nắng mặt trời hoặc ánh sáng trời tự nhiên (kèm khóa `with zero artificial lamps`). Cảnh ban đêm hoặc phòng kín dùng 1 nguồn đèn thực tế chính chiếu từ một hướng cố định.
- **Màu ánh sáng thuận theo nguồn sáng thực tế:**
  - Sắc độ vùng sáng (`highlights`) trên da nhân vật, trang phục và bối cảnh đi theo đúng bản chất vật lý của nguồn sáng trong cảnh: nắng ban ngày trong trẻo mang sắc trắng kem ấm (`crisp warm-ivory daylight`); ánh sáng cửa sổ ngày/mùa đông mang sắc trắng dịu tự nhiên (`soft natural window daylight`); hoàng hôn/bình minh mang sắc cam đào/hổ phách; đèn đêm mang sắc vàng ấm; ánh trăng mang sắc bạc xanh dịu.
  - Bảng màu phân bổ theo tỷ lệ 70-20-10 với độ đậm sắc độ cao (`deep chromatic density`): 70% màu khí quyển và bối cảnh chủ đạo; 20% màu bổ trợ của kiến trúc, đồ vật và trang phục; 10% điểm nhấn màu tương phản và viền sáng tại tâm điểm.

## 5. Cấu trúc Output Text Thuần (Mặc định cho AI Vận Hành)

Khi vận hành thực tế để sinh ảnh, AI xuất trực tiếp **1 đoạn văn tiếng Anh liền mạch (khoảng 110–140 từ)** ghép từ **5 khối câu theo đúng thứ tự cố định** dưới đây:

### 5.1. Khung mẫu Output Text Thuần
```text
Cinematic European arthouse stop-motion animation film still, rich saturated Kodak analog 35mm film color grading with deep chromatic density, vintage lens with natural optical depth of field and crystal-clear air. [Khối 2: Cỡ cảnh & Góc máy + Bối cảnh không gian + Điểm nhấn Môi trường / Siêu thực (theo plugin_surreal_whimsy.md)]. [Khối 3: Chủ thể trung tâm + Phân hóa ngoại hình theo cỡ cảnh + Điểm nhấn Nhân vật (Trang phục / Tóc / Phụ kiện) + Hành động đời thường thản nhiên giữa cảnh phi lý]. [Khối 4: Khóa DNA chất liệu nhân vật và bề mặt thủ công]. [Khối 5: 1 Nguồn sáng duy nhất + Sắc độ thuận nguồn sáng + Hướng bóng đổ đồng nhất]. No text.
```

### 5.2. Giải thích nhiệm vụ từng khối cho AI Vận Hành
1. **Khối 1 – Mỏ neo Chất phim & Ống kính (Câu 1 cố định):**
   - Luôn mở đầu nguyên văn: `Cinematic European arthouse stop-motion animation film still, rich saturated Kodak analog 35mm film color grading with deep chromatic density, vintage lens with natural optical depth of field and crystal-clear air.`
   - Nhiệm vụ: Khóa chất liệu hoạt hình stop-motion nghệ thuật châu Âu, độ đậm màu phim nhựa Kodak 35mm và độ trong của ống kính ngay từ đầu đoạn.
2. **Khối 2 – Cỡ cảnh, Góc máy, Bối cảnh & Điểm nhấn Siêu thực (Câu 2):**
   - Mở đầu bằng cỡ cảnh và góc máy chính xác (`Extreme wide landscape shot`, `Wide full-body shot`, `Wide high-angle shot`, `Low-angle wide shot`, `Wide orthographic front-on cross-section`, `Medium-full shot`, `Medium waist-up shot`, `Close-up portrait`, hoặc `Macro extreme close-up shot`).
   - Mô tả không gian bối cảnh gắn liền với điểm nhấn thị giác / cơ chế siêu thực tham chiếu từ [`craft/plugins/plugin_surreal_whimsy.md`](../craft/plugins/plugin_surreal_whimsy.md).
3. **Khối 3 – Chủ thể trung tâm, Điểm nhấn Nhân vật & Hành động Đời thường Thản nhiên (Câu 3):**
   - **Nếu cảnh có nhân vật:** Tả vị trí, ngoại hình thích ứng theo cỡ cảnh (Cận/Trung tả rõ cấu trúc mặt đối lập; Toàn/Rộng tả phom dáng `silhouette` và lộ rõ đôi chân `with full legs and shoes clearly visible`), kết hợp **Điểm nhấn Nhân vật linh hoạt trên Trang phục, Mái tóc hoặc Phụ kiện**, và luôn đặt nhân vật vào **một hành động sinh hoạt đời thường, bình thản (`calm, unbothered everyday action`)** giữa khung cảnh phi lý.
   - **Nếu cảnh tĩnh vật / phong cảnh không có người:** Mô tả chi tiết kết cấu chất liệu thủ công và chuyển động tương tác giữa sinh vật/đồ vật tại tâm điểm.
4. **Khối 4 – Khóa DNA chất liệu (Câu 4):**
   - **Khi cảnh có nhân vật:** `All figures have 1:7.5 stylized proportions (never doll-like), natural warm velvety matte molded paper-pulp skin with zero wrinkles, voluminous soft fibrous hair, and smooth matte clothing with zero chunky knitwear.`
   - **Khi cảnh không có người:** `All crafted elements feature tactile velvety matte surfaces, finely sculpted miniature textures, and sfumato soft edges with zero plastic sheen.`
5. **Khối 5 – Nguồn sáng duy nhất, Sắc độ thuận nguồn sáng & Kết câu (Câu 5 + `No text.`):**
   - Chỉ định **duy nhất 1 nguồn sáng chính chiếu từ 1 hướng cố định** với sắc độ thuận theo đúng thời gian/không gian của cảnh (kèm `with zero artificial lamps` cho cảnh ban ngày).
   - Nêu rõ phía đón sáng trên chủ thể, trang phục/phụ kiện và tâm điểm môi trường, khóa 1 hướng bóng đổ tự nhiên về phía khuất sáng (`illuminating the [lit side] of [subjects and focal element] while casting a single coherent natural shadow toward the [unlit side] against [background].`). Kết thúc bằng `No text.`

## 6. Quy trình tự kiểm tra trước khi xuất Prompt

Trước khi trả kết quả cho người dùng, AI vận hành tự đối chiếu 6 điểm sau:
1. **Định dạng đầu ra:** Xuất đúng **Output Text Thuần 5 khối (Mục 5)** theo mặc định; chỉ xuất JSON (Mục 7) khi người dùng yêu cầu đích danh định dạng JSON.
2. **Bối cảnh Siêu thực & Hành động Đời thường Thản nhiên:**
   - *Môi trường (Khối 2):* Ứng dụng linh hoạt các cơ chế chất thơ siêu thực từ [`craft/plugins/plugin_surreal_whimsy.md`](../craft/plugins/plugin_surreal_whimsy.md).
   - *Nhân vật (Khối 3):* Có điểm nhấn tạo hình tự nhiên nằm ở **Trang phục, Mái tóc hoặc Phụ kiện**, và luôn thực hiện **hành động đời thường với tâm thái thản nhiên, bình yên** giữa khung cảnh phi lý.
3. **Đúng cỡ cảnh và độ chi tiết thích ứng:** Chọn đúng cỡ cảnh/góc máy. Cảnh rộng tả phom dáng (`silhouette`), mảng màu trang phục và lộ rõ đôi chân; cảnh gần tả cấu trúc mặt đối lập và chi tiết chất liệu.
4. **Một nguồn sáng và đúng sắc độ:** Toàn cảnh có duy nhất 1 nguồn sáng chiếu từ 1 hướng cố định, màu ánh sáng thuận theo nguồn sáng thực tế của cảnh và tạo 1 hướng bóng đổ đồng nhất.
5. **Tính toàn vẹn tạo hình:** Định danh tuổi bằng chữ, giữ màu da tự nhiên `natural warm velvety matte molded paper-pulp skin`, và lộ trọn đôi chân tỷ lệ `1:7.5` ở các cảnh toàn thân.
6. **Đủ các cụm khóa kỹ thuật:** Giữ đủ `crystal-clear air` / `zero milky haze`, `with zero artificial lamps` (cho cảnh ban ngày), và `never doll-like`, `zero wrinkles`, `zero chunky knitwear` (khi cảnh có người).

---

# PHẦN II — DÀNH RIÊNG CHO NHÀ PHÁT TRIỂN (DEVELOPER R&D)

> **Lưu ý:** Toàn bộ Phần II (Mục 7, 8, 9) chỉ phục vụ Nhà phát triển nghiên cứu bóc tách tham số và bảo trì file tài liệu gốc. **AI vận hành bỏ qua phần này.**

## 7. Khung cấu trúc JSON nghiên cứu

```json
{
  "id": "prompt_001",
  "type": "generate image",
  "text": "NO TEXT",
  "STYLE": {
    "world": "Cinematic European arthouse stop-motion animation film still, rich saturated Kodak analog 35mm film color grading with deep chromatic density, crystal-clear air with zero milky haze, velvety matte surfaces with sfumato soft edges, [cỡ cảnh và kiểu bố cục không gian của cảnh], [tông sáng chính thuận theo nguồn sáng thực tế] highlights against [tông màu trung gian chủ đạo đậm sâu] midtones.",
    "palette": "70 percent [màu khí quyển và bối cảnh chủ đạo đậm sâu gắn kèm trạng thái ánh sáng của cảnh] with 20 percent [màu bổ trợ kiến trúc, đồ vật và trang phục] and 10 percent [điểm nhấn màu tương phản tại khối siêu thực và ánh sáng viền theo nguồn sáng chính]",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Stylized elongated slender human figures (1:7.5 arthouse proportions, never doll-like), natural warm velvety matte molded paper-pulp skin with sfumato soft blended edges, and zero wrinkles or creases, abundant voluminous soft fibrous hair, natural relaxed posture, and simplified smooth matte clothing with zero chunky knitwear.",
    "interaction": "[tên_tương_tác_giữa_nhân_vật_với_khối_kỳ_lạ_siêu_thực]",
    "figures": [
      {
        "id": "figure_1",
        "role": "[cụm định danh tạo hình bằng chữ, vóc dáng và vị trí trong không gian]",
        "look": "[mô tả thích ứng theo cỡ cảnh + Điểm nhấn Nhân vật linh hoạt trên Trang phục / Mái tóc / Phụ kiện + da natural warm matte paper-pulp đón sáng theo hướng nguồn sáng chính]",
        "action": "[hành động tương tác trực tiếp với tâm điểm; cảnh toàn thân lộ rõ đôi chân và giày trên mặt đất]"
      }
    ]
  },
  "CREATURES": [
    {
      "id": "creature_1",
      "name": "[số lượng, loài sinh vật và vị trí]",
      "details": "[màu sắc, chất liệu thủ công/tự nhiên và hành động tương tác với nhân vật hoặc tâm điểm]"
    }
  ],
  "ENVIRONMENT": {
    "camera": "[Tiêu cự ống kính phù hợp cỡ cảnh: Vintage 35mm/50mm/85mm macro lens], [cỡ cảnh và góc máy], natural optical depth of field with [chi tiết sắc nét tại tâm điểm] and soft bokeh on [chi tiết tiền cảnh/hậu cảnh], keeping the air crystal-clear with zero milky fog so colors remain deep and vibrant.",
    "setting": "[bối cảnh không gian mở, kiến trúc, thiên nhiên và hệ thống đạo cụ chi tiết; nếu ban ngày khóa thêm: with zero lamps, zero bulbs, and zero artificial light fixtures]",
    "focal_elements": [
      {
        "id": "element_1",
        "name": "[Điểm nhấn Môi trường / Siêu thực theo plugin_surreal_whimsy.md hoặc Phụ kiện kết nối trung tâm]",
        "material_and_texture": "[mô tả giàu tính thị giác về kết cấu chất liệu thủ công hữu hình và sự kết nối với nhân vật/không gian]",
        "details": "[cách nguồn sáng chính duy nhất chiếu sáng mặt đón nắng và tạo viền sáng đúng sắc độ nguồn sáng lên tâm điểm và chủ thể]"
      }
    ],
    "staging": "[Bố cục sắp đặt các lớp không gian tiền cảnh - trung cảnh - hậu cảnh hoặc trái - giữa - phải, làm nổi bật tâm điểm]",
    "real_nature": "[các sợi tóc, hoa cỏ, lông vũ, thớ gỗ, hạt bụi nắng hoặc chất liệu tự nhiên bắt sáng trong cảnh]",
    "backdrop": "Richly saturated [mô tả hậu cảnh phía xa đồng nhất hướng sáng và sắc độ với nguồn sáng chính].",
    "lighting": "[mô tả DUY NHẤT 1 nguồn sáng chính theo đúng thời gian/không gian thực tế từ 1 hướng cố định (nếu ban ngày thêm with zero artificial lamps), casting a single coherent shadow direction with natural shade on the unlit side]",
    "motion": "[chuyển động tinh tế của tà váy, hoa cỏ, gió, ánh sáng hoặc nhân vật]"
  }
}
```

## 8. Giải thích nhiệm vụ từng trường JSON

- **`id` / `type` / `text`:** Định danh prompt, lệnh tạo ảnh và khóa `"NO TEXT"` để giữ khung hình sạch chữ.
- **`STYLE.world`:** Chuỗi khóa phong cách stop-motion châu Âu, màu phim Kodak 35mm đậm sắc độ, không khí trong trẻo `zero milky haze`, bề mặt mịn mờ `sfumato`, kiểu bố cục không gian linh hoạt theo cảnh, và tương phản giữa vùng sáng (thuận theo nguồn sáng thực tế) với tông màu trung gian chủ đạo.
- **`STYLE.palette`:** Phân bổ tỷ lệ màu 70-20-10 gắn liền với trạng thái chiếu sáng tự nhiên của cảnh (70% màu khí quyển và bối cảnh lớn; 20% màu kiến trúc, đồ vật và quần áo; 10% điểm nhấn màu tương phản trên phụ kiện/tâm điểm và viền sáng thuận theo nguồn sáng chính).
- **`CHARACTERS.dna`:** Chuỗi khóa tỷ lệ cơ thể `1:7.5 (never doll-like)`, làn da bột giấy màu da tự nhiên `natural warm velvety matte molded paper-pulp skin` (`zero wrinkles or creases`), mái tóc dày bồng bềnh `abundant voluminous soft fibrous hair`, tư thế tự nhiên và quần áo vải mờ (`zero chunky knitwear`). Nếu cảnh không có người, để trống chuỗi này.
- **`CHARACTERS.interaction`:** Cụm từ ngắn tóm tắt hành động kết nối trực tiếp giữa các nhân vật hoặc với tâm điểm (hoặc `"NONE"` nếu cảnh không có người).
- **`CHARACTERS.figures[]`:** Mảng liệt kê các nhân vật trong cảnh (để mảng rỗng `[]` nếu cảnh không người):
  - `role`: Dùng cụm định danh tạo hình bằng chữ và phân hóa vóc dáng (`tall slender build` đối lập với `compact-shouldered` hoặc `softly rounded build with full 1:7.5 leg length`).
  - `look`: Thích ứng theo cỡ cảnh (Cận/Trung tả rõ cấu trúc mặt đối lập; Toàn/Rộng tả phom dáng `silhouette`), kèm **Điểm nhấn Nhân vật linh hoạt trên Trang phục, Mái tóc hoặc Phụ kiện**; dùng màu da tự nhiên `natural warm matte paper-pulp skin` đón sáng theo hướng nguồn sáng chính.
  - `action`: Tả tư thế tay chân tự nhiên tương tác với tâm điểm; cảnh toàn thân giữ lộ rõ đôi chân và bàn chân chạm sàn.
- **`CREATURES[]`:** Mảng mô tả động vật tự nhiên hoặc sinh vật bằng chất liệu thủ công. Nếu cảnh không có sinh vật thì để mảng rỗng `[]`.
- **`ENVIRONMENT.camera`:** Chọn tiêu cự (`35mm` cho đại cảnh rộng, `50mm` cho cảnh trung/toàn thân, `85mm macro` cho cận cảnh đặc tả) và góc máy linh hoạt (`eye-level`, `high-angle`, `low-angle`, `orthographic cross-section`), kết hợp độ sâu trường ảnh tự nhiên và khóa `keeping the air crystal-clear with zero milky fog`.
- **`ENVIRONMENT.setting`:** Tả không gian mở tràn 4 cạnh khung hình cùng hệ thống kiến trúc, thiên nhiên và đạo cụ theo đúng mật độ chi tiết của cảnh. Cảnh ban ngày thêm cụm `with zero lamps, zero bulbs, and zero artificial light fixtures` ở cuối câu.
- **`ENVIRONMENT.focal_elements[]`:** Điểm nhấn Thị giác / Siêu thực Trung tâm (tham chiếu từ [`craft/plugins/plugin_surreal_whimsy.md`](../craft/plugins/plugin_surreal_whimsy.md)); `material_and_texture` tả kết cấu chất liệu thủ công hữu hình; `details` tả cách nguồn sáng chính chiếu sáng mặt đón nắng và tạo viền sáng đúng sắc độ.
- **`ENVIRONMENT.staging`:** Sắp xếp vị trí các lớp không gian (tiền cảnh - trung cảnh - hậu cảnh; trái - giữa - phải) sao cho chủ thể chính và tâm điểm tách lớp rõ ràng khỏi nền.
- **`ENVIRONMENT.real_nature`:** Liệt kê các chất liệu sợi tự nhiên, hoa cỏ, lông vũ, hạt bụi hoặc thớ gỗ bắt sáng trong cảnh.
- **`ENVIRONMENT.backdrop`:** Mô tả lớp nền xa phía sau giữ nguyên độ đậm màu, đồng nhất cả hướng chiếu lẫn sắc độ với nguồn sáng chính.
- **`ENVIRONMENT.lighting`:** Xác định duy nhất 1 nguồn sáng chính từ 1 hướng cố định với sắc độ trung thực theo bối cảnh, kèm khóa `casting a single coherent shadow direction with natural shade on the unlit side`.
- **`ENVIRONMENT.motion`:** Một chuyển động vật lý đang diễn ra giữa chừng của khối siêu thực, gió, ánh sáng hoặc nhân vật.

## 9. Quy tắc bảo trì tài liệu gốc

1. **Sửa đúng chỗ (`/ponytail`):** Chỉ sửa đúng dòng cần thay đổi bằng công cụ chỉnh sửa cục bộ, ưu tiên cắt gọn.
2. **Chỉ viết quy luật (`No Use Cases`):** Rút ra quy tắc chung, giữ tài liệu độc lập với kịch bản hay bài nhạc cụ thể.
3. **Chỉ đưa vào các từ khóa cốt lõi:** Chỉ ghi những thuộc tính mang tính quy luật cho toàn bộ style.
4. **Viết khẳng định, ngắn gọn, tự nhiên (`/humanizer` & `stop-slop`):** Hướng dẫn trực tiếp những gì cần viết thay vì liệt kê danh sách từ cấm; đi thẳng vào kỹ thuật.
5. **Giữ 5 chốt chặn kỹ thuật cố định & Khối Siêu Thực bắt buộc:** Mọi bức ảnh bắt buộc có ít nhất 1 Khối Kỳ Lạ / Siêu Thực (`Poetic Surreal Hook`); chỉ dùng 5 cụm khóa kỹ thuật đã kiểm chứng (`never doll-like`, `zero milky haze`, `zero wrinkles or creases`, `zero chunky knitwear`, và `zero artificial lamps` cho cảnh ban ngày) cùng cụm da tự nhiên `natural warm velvety matte molded paper-pulp skin`.
6. **Bảo toàn Khung JSON (Mục 7) và Giải thích trường JSON (Mục 8):** Giữ nguyên hai mục riêng biệt ở cuối file cho mục đích R&D của Nhà phát triển.
