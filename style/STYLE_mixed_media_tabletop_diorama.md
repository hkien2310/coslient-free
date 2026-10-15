# European Arthouse Stop-Motion World Style

## Mục lục nhanh

- **PHẦN I: DÀNH CHO AI VẬN HÀNH (PRODUCTION)**
  - [1. Chất liệu thế giới và yếu tố siêu thực](#1-chất-liệu-thế-giới-và-yếu-tố-siêu-thực)
  - [2. Cỡ cảnh, góc máy và mật độ chi tiết](#2-cỡ-cảnh-góc-máy-và-mật-độ-chi-tiết)
  - [3. Tạo hình nhân vật, điểm nhấn và hành động đời thường](#3-tạo-hình-nhân-vật-điểm-nhấn-và-hành-động-đời-thường)
  - [4. Ánh sáng một nguồn và màu sắc](#4-ánh-sáng-một-nguồn-và-màu-sắc)
  - [5. Cấu trúc Output Text Thuần (Mặc định cho AI Vận Hành)](#5-cấu-trúc-output-text-thuần-mặc-định-cho-ai-vận-hành)
  - [6. Bảng kiểm trước khi xuất Prompt](#6-bảng-kiểm-trước-khi-xuất-prompt)
- **PHẦN II: DÀNH RIÊNG CHO NHÀ PHÁT TRIỂN (DEVELOPER R&D)**
  - [7. Khung cấu trúc JSON nghiên cứu](#7-khung-cấu-trúc-json-nghiên-cứu)
  - [8. Giải thích nhiệm vụ từng trường JSON](#8-giải-thích-nhiệm-vụ-từng-trường-json)
  - [9. Quy tắc bảo trì tài liệu gốc](#9-quy-tắc-bảo-trì-tài-liệu-gốc)

---

# PHẦN I: DÀNH CHO AI VẬN HÀNH (PRODUCTION)

## 1. Chất liệu thế giới và yếu tố siêu thực

Phong cách này dựng lại khung hình phim hoạt hình stop-motion nghệ thuật châu Âu (`Cinematic European arthouse stop-motion animation film still`) trên nền màu phim nhựa 35mm Kodak (`rich saturated Kodak analog 35mm film color grading with deep chromatic density`). Bối cảnh là không gian mở tràn qua bốn cạnh khung hình.

- **Yếu tố siêu thực và thái độ bình thản:** Mỗi bức ảnh tích hợp một cơ chế siêu thực theo [`craft/plugins/plugin_surreal_whimsy.md`](../craft/plugins/plugin_surreal_whimsy.md). Bối cảnh mang yếu tố siêu thực kỳ lạ, nhưng con người bên trong luôn làm những công việc sinh hoạt đời thường với vẻ bình thản tự nhiên.
- **Bề mặt và không khí:** Toàn bộ bề mặt mang độ mịn mờ như nhung với đường viền chuyển êm (`velvety matte surfaces with sfumato soft edges`), giữ không khí trong vắt (`crystal-clear air` hoặc `zero milky haze`) để bảo toàn độ đậm màu.

## 2. Cỡ cảnh, góc máy và mật độ chi tiết

Sử dụng linh hoạt mọi cỡ cảnh và góc máy điện ảnh theo đúng ý đồ của từng cảnh:
- **Đại cảnh và toàn cảnh rộng (`Extreme wide shot`, `Wide landscape / architectural shot`):** Mở rộng không gian nhiều lớp chiều sâu (tiền cảnh, trung cảnh, hậu cảnh), lấy trọn thiên nhiên, kiến trúc và hiện tượng siêu thực lớn.
- **Cảnh toàn thân, cảnh trung và mặt cắt ngang (`Full-body shot`, `Medium shot`, `Orthographic front-on cross-section`):** Phù hợp cho tương tác nhân vật hoặc góc cắt ngang nhìn thẳng vào cấu trúc bên trong không gian nội thất.
- **Cận cảnh và đặc tả (`Close-up`, `Macro extreme close-up`) cùng góc máy đa chiều (`Eye-level`, `High-angle`, `Low-angle`, `Over-the-shoulder`, `Deep perspective`):** Tập trung vào biểu cảm gương mặt, đôi bàn tay hoặc chi tiết bề mặt đồ vật.
- **Mật độ chi tiết và tách lớp chủ thể:** Cho phép dựng cả không gian thoáng tối giản lẫn không gian giàu chi tiết. Dùng độ sâu trường ảnh quang học (`natural optical depth of field`, `creamy lens bokeh`) kết hợp tương phản sáng tối để tách chủ thể chính và điểm nhấn siêu thực khỏi nền.

## 3. Tạo hình nhân vật, điểm nhấn và hành động đời thường

- **Số lượng chủ thể linh hoạt:** Cảnh có thể không có người (tĩnh vật, phong cảnh, kiến trúc, sinh vật), có 1 người, hoặc nhiều người tương tác.
- **Khung DNA chất liệu (Khi cảnh có người):** Tỷ lệ cơ thể thanh mảnh kéo dài (`1:7.5 stylized proportions, never doll-like`), da bột giấy đúc mịn mờ màu tự nhiên (`natural warm velvety matte molded paper-pulp skin with zero wrinkles`), tóc dày nhiều sợi (`voluminous soft fibrous hair`), chất vải mờ không đan len thô (`smooth matte clothing with zero chunky knitwear`). Gọi nhân vật bằng hình dáng và độ tuổi ước lượng bằng chữ.
- **Hành động đời thường bình thản:** Nhân vật thực hiện các cử chỉ, công việc quen thuộc hàng ngày (`calm, unbothered everyday actions`), đón nhận hiện tượng siêu thực xung quanh như điều hiển nhiên.
- **Điểm nhấn tạo hình trên nhân vật:** Mỗi nhân vật có ít nhất một điểm nhấn thị giác tự nhiên gắn với ngữ cảnh cảnh quay, nằm ở **Trang phục** (phom dáng bay bổng, kiểu đồ đặc trưng hoặc màu sắc tương phản nổi bật trên nền cảnh), **Mái tóc / Mũ / Kính**, hoặc **Phụ kiện kể chuyện**.
- **Chi tiết nhân vật thích ứng theo cỡ cảnh:**
  - **Cảnh Cận và Trung (`Close-up` / `Medium`):** Tả rõ đường nét gương mặt cùng điểm nhấn trang phục, tóc hoặc phụ kiện. Khi có từ 2 người trở lên, mỗi người có cấu trúc xương mặt, dáng mũi, cằm và khung vai đối lập nhau.
  - **Toàn cảnh và Đại cảnh (`Wide` / `Extreme wide`):** Tả phom dáng tổng thể (`silhouette`), chênh lệch chiều cao, mảng màu và chuyển động của trang phục, kiểu tóc để máy quay giữ đúng góc rộng; cảnh toàn thân lộ rõ đôi chân dài tỷ lệ `1:7.5` và bàn chân chạm sàn (`with full legs and shoes clearly visible`).

## 4. Ánh sáng một nguồn và màu sắc

- **Một nguồn sáng chính duy nhất:** Toàn bộ khung hình chỉ dùng **1 nguồn sáng chính chiếu từ 1 hướng cố định**, tạo 1 hướng bóng đổ đồng nhất: phần đón sáng rõ nét, phần khuất sáng chuyển êm vào vùng bóng râm tự nhiên. Cảnh ban ngày dùng ánh sáng tự nhiên kèm khóa `with zero artificial lamps`; cảnh đêm hoặc phòng kín dùng 1 nguồn đèn chính từ 1 hướng cố định.
- **Màu ánh sáng đúng với nguồn sáng thực:** Sắc độ vùng sáng (`highlights`) đi theo đúng nguồn sáng trong cảnh (nắng ngày trắng kem ấm, cửa sổ ngày trắng dịu, hoàng hôn cam đào/hổ phách, đèn đêm vàng ấm, ánh trăng bạc xanh) trên nền màu đậm sắc độ (`deep chromatic density`).

## 5. Cấu trúc Output Text Thuần (Mặc định cho AI Vận Hành)

Khi vận hành thực tế để sinh ảnh, AI xuất trực tiếp **1 đoạn văn tiếng Anh liền mạch (khoảng 100–135 từ)** ghép từ **5 khối câu theo thứ tự cố định**:

### 5.1. Khung mẫu Output Text Thuần
```text
Cinematic European arthouse stop-motion animation film still, rich saturated Kodak analog 35mm film color grading with deep chromatic density, velvety matte surfaces with sfumato soft edges, vintage lens with natural optical depth of field and crystal-clear air. [Khối 2: Cỡ cảnh & Góc máy + Bối cảnh + Yếu tố siêu thực (theo plugin_surreal_whimsy.md)]. [Khối 3: Chủ thể trung tâm + Ngoại hình theo cỡ cảnh + Điểm nhấn (Trang phục / Tóc / Phụ kiện) + Hành động đời thường bình thản]. [Khối 4: Khóa DNA nhân vật (bỏ qua nếu cảnh không có người)]. [Khối 5: 1 Nguồn sáng duy nhất + Màu ánh sáng thuận nguồn sáng + 1 hướng bóng đổ đồng nhất]. No text.
```

### 5.2. Nhiệm vụ từng khối
1. **Khối 1 (Câu 1 cố định):** Sao chép nguyên văn câu mở đầu ở khung mẫu 5.1 để khóa chất phim stop-motion châu Âu, màu Kodak 35mm, bề mặt mịn mờ `sfumato` và độ trong của ống kính ngay từ đầu đoạn.
2. **Khối 2 (Câu 2):** Mở đầu bằng cỡ cảnh và góc máy chính xác, tiếp nối bằng bối cảnh không gian và yếu tố siêu thực tham chiếu từ [`craft/plugins/plugin_surreal_whimsy.md`](../craft/plugins/plugin_surreal_whimsy.md).
3. **Khối 3 (Câu 3):** Nếu cảnh có người, tả ngoại hình thích ứng theo cỡ cảnh (cảnh gần tả cấu trúc mặt đối lập; cảnh rộng tả phom dáng `silhouette` và lộ rõ đôi chân), kèm điểm nhấn tự nhiên ở trang phục, tóc hoặc phụ kiện và hành động đời thường bình thản. Nếu cảnh không có người, tả chi tiết hình khối và chuyển động của đồ vật hoặc sinh vật tại tâm điểm.
4. **Khối 4 (Câu 4 cố định khi có người):** Điền nguyên văn: `All figures have 1:7.5 stylized proportions (never doll-like), natural warm velvety matte molded paper-pulp skin with zero wrinkles, voluminous soft fibrous hair, and smooth matte clothing with zero chunky knitwear.` (Nếu cảnh không có người thì bỏ qua câu này).
5. **Khối 5 (Câu cuối + `No text.`):** Chỉ định 1 nguồn sáng chính từ 1 hướng cố định với màu sắc đúng nguồn sáng thực tế (thêm `with zero artificial lamps` nếu là ban ngày), nêu rõ phía đón sáng và 1 hướng bóng đổ tự nhiên về phía khuất sáng. Kết thúc bằng `No text.`

## 6. Bảng kiểm trước khi xuất Prompt

1. **Định dạng:** Xuất **Output Text Thuần (Mục 5)** theo mặc định; chỉ xuất JSON (Mục 7) khi người dùng yêu cầu rõ định dạng JSON.
2. **Siêu thực & Đời thường:** Bối cảnh có yếu tố siêu thực theo [`plugin_surreal_whimsy.md`](../craft/plugins/plugin_surreal_whimsy.md); nhân vật có điểm nhấn ở trang phục/tóc/phụ kiện và thực hiện hành động đời thường bình thản.
3. **Cỡ cảnh & Tạo hình:** Cảnh rộng tả phom dáng (`silhouette`) và lộ rõ đôi chân tỷ lệ `1:7.5`; cảnh gần tả cấu trúc mặt đối lập; định danh tuổi bằng chữ và dùng màu da tự nhiên `natural warm velvety matte molded paper-pulp skin`.
4. **Ánh sáng:** Duy nhất 1 nguồn sáng từ 1 hướng cố định, màu ánh sáng thuận theo nguồn sáng thực tế và tạo 1 hướng bóng đổ đồng nhất.
5. **Chốt khóa kỹ thuật:** Đủ `crystal-clear air` / `zero milky haze`, `with zero artificial lamps` (ban ngày), và `never doll-like`, `zero wrinkles`, `zero chunky knitwear` (khi có người).

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
