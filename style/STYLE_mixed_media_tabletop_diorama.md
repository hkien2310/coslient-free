# European Arthouse Stop-Motion World Style

> **GHI CHÚ CỐ ĐỊNH (CẤM XÓA KHI CHỈNH SỬA FILE):**
> 1. **Sửa đúng chỗ (`/ponytail`):** Chỉ sửa đúng dòng cần thay đổi bằng công cụ chỉnh sửa cục bộ, ưu tiên cắt gọn, không ghi đè toàn bộ file.
> 2. **Chỉ viết quy luật, không đưa ví dụ (`No Use Cases`):** Rút ra quy tắc chung, không lấy bối cảnh hay tình huống của một bài nhạc cụ thể đưa vào tài liệu gốc.
> 3. **Không liệt kê từ khóa riêng lẻ:** Không liệt kê sự vật, hiện tượng, màu sắc hay chất liệu cụ thể nếu nó không bắt buộc có mặt trong mọi bức ảnh của style.
> 4. **Viết ngắn gọn, tự nhiên (`/humanizer` & `stop-slop`):** Dùng từ ngữ bình thường, đi thẳng vào kỹ thuật; bỏ văn phong đao to búa lớn, trạng từ cực đoan và cấu trúc câu rập khuôn của AI.
> 5. **Chỉ giữ 5 chốt chặn kỹ thuật ngắn gọn & để mở cảm xúc gương mặt:** Không liệt kê danh sách từ cấm dài dòng; chỉ dùng đúng 5 cụm chặn kỹ thuật đã kiểm chứng (`never doll-like`, `zero milky haze`, `zero wrinkles or creases`, `zero chunky knitwear`, và `zero artificial lamps` cho cảnh ban ngày). Giữ `CHARACTERS.dna` gọn nhẹ để đường nét khuôn mặt và sắc ửng hồng trên má biến thiên linh hoạt theo độ tuổi và cảm xúc của từng bức ảnh.

## 1. Bản chất thế giới và bề mặt chất liệu

Phong cách này dựng lại khung hình phim hoạt hình stop-motion nghệ thuật châu Âu (`Cinematic European arthouse stop-motion animation film still`) trên nền màu phim nhựa 35mm Kodak (`rich saturated Kodak analog 35mm film color grading with deep chromatic density`). Bối cảnh là thế giới sống rộng mở tràn qua bốn cạnh khung hình của nhân vật. Khi cần thể hiện không gian bên trong, dùng góc máy mặt cắt ngang trực diện (`orthographic front-on cross-section`). Các hiện tượng tự nhiên hoặc cảm xúc vô hình trong cảnh được thể hiện bằng chất liệu thủ công hữu hình mang tỷ lệ thực của thế giới đó.

**Độ mềm bề mặt và chiều sâu quang học:**
- Toàn bộ bề mặt nhân vật và chất liệu mang độ mịn mờ như nhung với đường viền chuyển êm (`velvety matte surfaces with sfumato soft edges on characters`).
- Giữ bầu không khí trong trẻo không sương đục (`crystal-clear air with zero milky haze`) và tách lớp không gian bằng tiêu cự ống kính cổ điển 50mm xóa phông mịn (`Vintage 50mm lens, shallow optical depth of field with creamy lens bokeh`), giúp màu nền luôn sâu và tươi rõ.

## 2. Bố cục dải trung cảnh phẳng (Stage-Planar Midground Staging)

Toàn bộ nhân vật, đạo cụ kể chuyện và hành động chính đặt gọn trên một dải trung cảnh ngang (`stage-planar midground composition`). Tiền cảnh và hậu cảnh đóng vai trò khung bao tách lớp bằng tiêu cự xóa phông, giữ nguyên độ sâu sắc độ.

## 3. Tạo hình nhân vật và sự đa dạng theo cảm xúc cảnh

- **Khung DNA chung (`CHARACTERS.dna`):** Nhân vật mang tỷ lệ cơ thể thanh mảnh kéo dài (`Stylized elongated slender human figures (1:7.5 arthouse proportions, never doll-like)`), làn da bột giấy đúc mịn mờ tông hồng đào ấm không nếp nhăn (`warm rosy-apricot velvety matte molded paper-pulp skin with sfumato soft blended edges, and zero wrinkles or creases`), mái tóc dày nhiều sợi bông (`abundant voluminous soft fibrous hair`), dáng đứng ngồi tự nhiên (`natural relaxed posture`) và trang phục vải mờ giản lược (`simplified smooth matte clothing with zero chunky knitwear`).
- **Đa dạng hóa gương mặt và sắc má theo cảm xúc từng ảnh (`figures[].look`):**
  - Không khóa cứng một kiểu khung xương mặt duy nhất trong `dna`. Tùy theo cảm giác mong muốn của bức ảnh (thanh lịch, trầm tư, ấm áp, hiền hậu hay e ấp) mà mô tả đường nét gương mặt và biểu cảm phù hợp ở `look`. Gọi đúng độ tuổi ở `role` và `look` (`slender young woman`, `tall slender man`, `slender older man` — tránh gọi người lớn là `boy` hay `small girl`).
  - **Kiểm soát má hồng (`blush`):** Mặc định không để `blush` trong `dna` và `palette`. Chỉ thêm `soft terracotta-rose blush on cheeks` vào `look` khi nhân vật trong cảnh có cảm xúc ngại ngùng, e ấp, xúc động hoặc ửng hồng dưới nắng lạnh; các cảnh sinh hoạt bình thường giữ nguyên làn da `warm rosy-apricot` đều màu.
- **Phân cấp chi tiết theo số lượng người:**
  - **Cảnh 1–2 người:** Mô tả rõ thần thái, biểu cảm và đường nét khuôn mặt phủ mịn `sfumato` theo đúng cảm xúc của cảnh.
  - **Cảnh đông người (từ 3 người trở lên):** Giản lược nét mặt thành mảng khối ẩn dịu (`impressionistic understated faces`), tập trung vào dáng người thanh mảnh, mái tóc nhiều sợi, màu sắc trang phục và cử chỉ.

## 4. Ánh sáng và Màu sắc

- **Quy tắc nguồn sáng ngày và đêm:**
  - Cảnh ban ngày dùng 100% ánh nắng mặt trời tự nhiên và bầu trời, khóa cụm `with zero artificial lamps` trong `setting` và `lighting` để chặn AI tự vẽ đèn bật sáng ban ngày.
  - Cảnh ban đêm hoặc phòng kín dùng ánh đèn ấm thực tế tương phản với nền tối sâu.
- **Tương phản Nắng Ấm và Nền Đậm Sâu (70-20-10):**
  - Cuối `STYLE.world` luôn xác định rõ tương phản giữa vùng sáng ấm và tông màu trung gian đậm sâu của cảnh (ví dụ: `warm golden-honey highlights against rich cool [blue / lavender-violet / slate-teal] midtones`).
  - Bảng màu giữ độ đậm sắc độ (`deep chromatic density`): 70% màu khí quyển và bối cảnh chủ đạo đậm sâu; 20% màu bổ trợ của kiến trúc, gỗ và trang phục; 10% điểm nhấn màu nổi bật trên đạo cụ, hoa cỏ hoặc phụ kiện.

## 5. Cấu trúc JSON Prompt

```json
{
  "id": "prompt_001",
  "type": "generate image",
  "text": "NO TEXT",
  "STYLE": {
    "world": "Cinematic European arthouse stop-motion animation film still, rich saturated Kodak analog 35mm film color grading with deep chromatic density, crystal-clear air with zero milky haze, velvety matte surfaces with sfumato soft edges on characters, stage-planar midground composition, warm golden-honey highlights against rich cool [tông màu nền chủ đạo của cảnh] midtones.",
    "palette": "70 percent [màu khí quyển và bối cảnh chủ đạo đậm sâu] with 20 percent [màu bổ trợ kiến trúc, gỗ và trang phục] and 10 percent [điểm nhấn màu tương phản trên phụ kiện, hoa cỏ hoặc ánh nắng viền]",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Stylized elongated slender human figures (1:7.5 arthouse proportions, never doll-like), warm rosy-apricot velvety matte molded paper-pulp skin with sfumato soft blended edges, and zero wrinkles or creases, abundant voluminous soft fibrous hair, natural relaxed posture, and simplified smooth matte clothing with zero chunky knitwear.",
    "interaction": "[tương tác chính]",
    "figures": [
      {
        "id": "figure_1",
        "role": "[vai trò và độ tuổi đúng thực tế - ví dụ: slender young woman / tall slender man]",
        "look": "[Cảnh 1-2 người: tả nét mặt và biểu cảm linh hoạt theo cảm giác của ảnh, da warm rosy-apricot matte paper-pulp (chỉ thêm soft blush khi nhân vật ngại ngùng/xúc động), tóc nhiều sợi bồng bềnh, trang phục vải mờ. Cảnh đông người: tả dáng thanh mảnh, tóc nhiều sợi, màu áo cơ bản, mặt ẩn dịu impressionistic understated faces]",
        "action": "[Hành động và dáng điệu tự nhiên trên dải trung cảnh]"
      }
    ]
  },
  "CREATURES": [],
  "ENVIRONMENT": {
    "camera": "Vintage 50mm lens, shallow optical depth of field with creamy lens bokeh on [hậu cảnh/tiền cảnh], keeping the air crystal-clear with zero milky fog so background colors remain deep and vibrant.",
    "setting": "[Mô tả bối cảnh rộng mở tràn khung hình với màu sắc đậm sâu; nếu là ban ngày thêm: with zero lamps, zero bulbs, and zero artificial light fixtures]",
    "focal_elements": [
      {
        "id": "element_1",
        "name": "[Chi tiết ẩn dụ chất liệu trung tâm]",
        "material_and_texture": "[Mô tả chất liệu thủ công hữu hình với đường nét mềm mại và sắc độ tươi rõ]",
        "details": "[Chi tiết tương tác với ánh sáng]"
      }
    ],
    "staging": "[Stage-planar midground layout: mô tả vị trí các cụm chính trên dải trung cảnh ngang, tiền cảnh và hậu cảnh tách lớp xóa phông]",
    "real_nature": "[Các chất liệu sợi bông, mây, hoa lá, gỗ đá tự nhiên trong cảnh]",
    "backdrop": "[Softly out-of-focus yet richly saturated...: mô tả hậu cảnh xóa phông bokeh mịn nhưng giữ nguyên độ đậm đà của màu sắc]",
    "lighting": "[Ban ngày: 100 percent natural direct ... sunlight with zero artificial lamps, casting warm golden highlights across the rosy-apricot paper-pulp skin... Ban đêm/phòng kín: ánh đèn ấm tương phản với bóng tối sâu]",
    "motion": "[Chuyển động tinh tế của gió, ánh sáng hoặc chất liệu]"
  }
}
```
