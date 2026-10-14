# European Arthouse Stop-Motion World Style

> **GHI CHÚ CỐ ĐỊNH (CẤM XÓA KHI CHỈNH SỬA FILE):**
> 1. **Sửa đúng chỗ (`/ponytail`):** Chỉ sửa đúng dòng cần thay đổi bằng công cụ chỉnh sửa cục bộ, ưu tiên cắt gọn, không ghi đè toàn bộ file.
> 2. **Chỉ viết quy luật, không đưa ví dụ (`No Use Cases`):** Rút ra quy tắc chung, không lấy bối cảnh hay tình huống của một bài nhạc cụ thể đưa vào tài liệu gốc.
> 3. **Không liệt kê từ khóa riêng lẻ:** Không liệt kê sự vật, hiện tượng, màu sắc hay chất liệu cụ thể nếu nó không bắt buộc có mặt trong mọi bức ảnh của style.
> 4. **Viết ngắn gọn, tự nhiên (`/humanizer` & `stop-slop`):** Dùng từ ngữ bình thường, đi thẳng vào kỹ thuật; bỏ văn phong đao to búa lớn, trạng từ cực đoan và cấu trúc câu rập khuôn của AI.
> 5. **Chỉ giữ 5 chốt chặn kỹ thuật ngắn gọn & để mở cảm xúc gương mặt:** Không liệt kê danh sách từ cấm dài dòng; chỉ dùng đúng 5 cụm chặn kỹ thuật đã kiểm chứng (`never doll-like`, `zero milky haze`, `zero wrinkles or creases`, `zero chunky knitwear`, và `zero artificial lamps` cho cảnh ban ngày). Giữ `CHARACTERS.dna` gọn nhẹ để đường nét khuôn mặt và sắc ửng hồng trên má biến thiên linh hoạt theo độ tuổi và cảm xúc của từng bức ảnh.
> 6. **Tách biệt Khung JSON (Mục 5) và Giải thích trường JSON (Mục 6) – Cấm xóa:** Mục 5 chỉ chứa khung cấu trúc JSON sạch và chuỗi từ khóa cố định; Mục 6 giải thích nhiệm vụ và quy tắc điền từng trường. Hai mục này làm hai nhiệm vụ riêng biệt, cấm gộp chung và cấm xóa trong mọi trường hợp.

## 1. Bản chất thế giới và bề mặt chất liệu

Phong cách này dựng lại khung hình phim hoạt hình stop-motion nghệ thuật châu Âu (`Cinematic European arthouse stop-motion animation film still`) trên nền màu phim nhựa 35mm Kodak (`rich saturated Kodak analog 35mm film color grading with deep chromatic density`). Bối cảnh là thế giới sống rộng mở tràn qua bốn cạnh khung hình của nhân vật. Khi cần thể hiện không gian bên trong, dùng góc máy mặt cắt ngang trực diện (`orthographic front-on cross-section`). Các hiện tượng tự nhiên hoặc cảm xúc vô hình trong cảnh được thể hiện bằng chất liệu thủ công hữu hình mang tỷ lệ thực của thế giới đó.

**Đường cong thủ công, độ mềm bề mặt và cách xử lý sương mù:**
- **Ưu tiên đường cong tự nhiên và dáng liêu xiêu thủ công:** Toàn bộ kiến trúc, đồ vật, phương tiện và đạo cụ đều mang đường lượn cong mềm, hơi phồng hoặc nghiêng liêu xiêu bất đối xứng của đồ nặn gọt bằng tay (`soft organic hand-carved curves with gently wonky asymmetrical contours and zero rigid ruler-straight lines`). Tránh các khối hộp thẳng tắp như vẽ kỹ thuật công nghiệp.
- Toàn bộ bề mặt nhân vật và chất liệu mang độ mịn mờ như nhung với đường viền chuyển êm (`velvety matte surfaces with sfumato soft edges on characters`).
- **Phân biệt Độ trong ống kính và Thời tiết sương mù:** Ở `STYLE.world` và `ENVIRONMENT.camera`, luôn khóa `crystal-clear air with zero milky haze` để giữ ống kính trong vắt, ngăn AI phủ lớp màng trắng đục làm bạc màu toàn khung hình. Khi bối cảnh thực sự có sương sớm, mây mù hoặc khói, không đặt ở `camera` mà mô tả tại `focal_elements` hoặc `setting` thành **những dải sương/bông hữu hình trôi tách lớp giữa không gian**, giữ nguyên độ đậm màu của nhân vật và cảnh vật.

## 2. Bố cục dải trung cảnh phẳng (Stage-Planar Midground Staging)

Toàn bộ nhân vật, đạo cụ kể chuyện và hành động chính đặt gọn trên một dải trung cảnh ngang (`stage-planar midground composition`). Tiền cảnh và hậu cảnh đóng vai trò khung bao tách lớp bằng tiêu cự xóa phông, giữ nguyên độ sâu sắc độ. Vùng nền nằm ngay sau lưng tâm điểm phải giữ thoáng, đồng nhất hoặc tách biệt rõ về độ sáng và màu sắc để không làm chìm đường viền nhân vật.

## 3. Tạo hình nhân vật và sự đa dạng trong cùng khung hình

- **Khung DNA chung (`CHARACTERS.dna`):** Nhân vật mang tỷ lệ cơ thể thanh mảnh kéo dài (`Stylized elongated slender human figures (1:7.5 arthouse proportions, never doll-like)`), làn da bột giấy đúc mịn mờ tông hồng đào ấm không nếp nhăn (`warm rosy-apricot velvety matte molded paper-pulp skin with sfumato soft blended edges, and zero wrinkles or creases`), thần thái hiền từ ấm áp không u buồn hay hốc hác (`warm benevolent expression, never sad, gloomy, or gaunt`), mái tóc dày nhiều sợi bông không bị hói (`abundant full thick soft fibrous hair, never bald`), dáng đứng ngồi tự nhiên (`natural relaxed posture`) và trang phục vải mờ giản lược (`simplified smooth matte clothing with zero chunky knitwear`).
- **Đa dạng hóa biểu cảm tích cực và kiểm soát má hồng (`figures[].look`):**
  - Biểu cảm biến thiên linh hoạt nhưng luôn giữ sắc thái tích cực, hiền từ, bình yên hoặc vui vẻ nhẹ nhàng (`gentle contented smile`, `warm benevolent gaze`, `serene joyful wonder`). Cấm các tính từ gây mặt buồn, hốc hác, khắc khổ hoặc hói đầu (`sad`, `melancholic`, `gloomy`, `gaunt`, `hollow-cheeked`, `bald`). Gọi đúng độ tuổi ở `role` và `look`, tránh dùng từ chỉ trẻ em (`boy`, `small girl`) cho nhân vật trưởng thành.
  - **Kiểm soát má hồng (`blush`):** Mặc định không để `blush` trong `dna` và `palette`. Chỉ thêm `soft terracotta-rose blush on cheeks` vào `look` khi nhân vật trong cảnh có cảm xúc ngại ngùng, e ấp, xúc động hoặc đứng dưới nắng lạnh; các cảnh bình thường giữ nguyên làn da `warm rosy-apricot` đều màu.
- **Chống trùng lặp ngoại hình và phân cấp theo số lượng người:**
  - Khi trong ảnh có từ 2 người trở lên, phân hóa hình khối bằng sự đối lập giữa dáng cao thanh mảnh (`tall slender`) và dáng thấp tròn trịa, bầu bĩnh (`short plump`, `round-cheeked`, `petite`), kết hợp khác biệt kiểu tóc dày, râu bông, mũ, kính và màu trang phục.
  - **Cảnh có nhân vật chính (từ 1 đến 4 người trung tâm):** Tách riêng từng nhân vật chính trong `figures[]`, mô tả rõ thần thái hiền hòa, góc mặt và đường nét phủ mịn `sfumato`. Nếu có người phụ xung quanh, gom vào một phần tử và đẩy ra lớp tiền cảnh hoặc hậu cảnh xóa phông.
  - **Cảnh đại cảnh nhóm (không có nhân vật chính đơn lẻ):** Nhân vật phải đứng hoặc ngồi trọn vẹn trên mặt phẳng sàn (không cắt cụt nửa người trong hộp kín), chia thành các cụm bất đối xứng tương tác tự nhiên thả lỏng với nhau (trò chuyện mỉm cười, nhắm mắt nghe nhạc, nghiêng đầu thư thái) thay vì đứng đơ nhìn cứng nhắc về một phía.

## 4. Ánh sáng và Màu sắc

- **Quy tắc nguồn sáng ngày và đêm:**
  - Cảnh ban ngày dùng 100% ánh nắng mặt trời tự nhiên và bầu trời, khóa cụm `with zero artificial lamps` trong `setting` và `lighting` để chặn AI tự vẽ đèn bật sáng ban ngày.
  - Cảnh ban đêm hoặc phòng kín dùng ánh đèn ấm thực tế tương phản với nền tối sâu.
- **Tương phản Nắng Ấm và Nền Đậm Sâu (70-20-10):**
  - Cuối `STYLE.world` luôn xác định rõ tương phản giữa vùng sáng ấm và tông màu trung gian đậm sâu của cảnh (`warm [tông sáng chính] highlights against rich cool [tông màu nền chủ đạo] midtones`).
  - Bảng màu giữ độ đậm sắc độ (`deep chromatic density`): 70% màu khí quyển và bối cảnh chủ đạo đậm sâu; 20% màu bổ trợ của kiến trúc, gỗ và trang phục; 10% điểm nhấn màu nổi bật trên đạo cụ, hoa cỏ hoặc phụ kiện.

## 5. Cấu trúc JSON Prompt (Khung chuẩn cố định, cấm xóa)

> **Lưu ý cố định:** Mục 5 (Khung JSON) và Mục 6 (Giải thích trường JSON) có nhiệm vụ riêng biệt và bắt buộc giữ nguyên cả hai. Mục 5 chỉ giữ bộ khung JSON sạch và các chuỗi khóa style cố định để sao chép trực tiếp khi tạo prompt.

```json
{
  "id": "prompt_001",
  "type": "generate image",
  "text": "NO TEXT",
  "STYLE": {
    "world": "Cinematic European arthouse stop-motion animation film still, rich saturated Kodak analog 35mm film color grading with deep chromatic density, crystal-clear air with zero milky haze, velvety matte surfaces with sfumato soft edges on characters, soft organic hand-carved curves with gently wonky asymmetrical contours and zero rigid ruler-straight lines, stage-planar midground composition, warm [tông sáng chính] highlights against rich cool [tông màu nền chủ đạo] midtones.",
    "palette": "70 percent [màu khí quyển và bối cảnh chủ đạo đậm sâu] with 20 percent [màu bổ trợ kiến trúc, gỗ và trang phục] and 10 percent [điểm nhấn màu tương phản trên phụ kiện, hoa cỏ hoặc ánh sáng viền]",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Stylized elongated slender human figures (1:7.5 arthouse proportions, never doll-like), warm rosy-apricot velvety matte molded paper-pulp skin with sfumato soft blended edges, and zero wrinkles or creases, warm benevolent expression (never sad, gloomy, or gaunt), abundant full thick soft fibrous hair (never bald), natural relaxed posture, and simplified smooth matte clothing with zero chunky knitwear.",
    "interaction": "[tên_tương_tác_ngắn_gọn]",
    "figures": [
      {
        "id": "figure_1",
        "role": "[vai trò, độ tuổi và vị trí trên dải trung cảnh]",
        "look": "[cỡ cảnh, hướng nhìn, nét mặt và biểu cảm theo cảm xúc ảnh, da warm rosy-apricot matte paper-pulp, kiểu tóc sợi và trang phục vải mờ]",
        "action": "[hành động và dáng điệu cụ thể đang thực hiện]"
      }
    ]
  },
  "CREATURES": [
    {
      "id": "creature_1",
      "name": "[số lượng, loài sinh vật và vị trí]",
      "details": "[màu sắc, chất liệu thủ công/tự nhiên và hành động tương tác với nhân vật hoặc bối cảnh]"
    }
  ],
  "ENVIRONMENT": {
    "camera": "Vintage 50mm lens, shallow optical depth of field with [chi tiết tiền cảnh/trung cảnh] and creamy lens bokeh on [chi tiết hậu cảnh], keeping the air crystal-clear with zero milky fog so background colors remain deep and vibrant.",
    "setting": "[bối cảnh mở tràn khung hình, kiến trúc và đồ vật xung quanh; nếu ban ngày khóa thêm: with zero lamps, zero bulbs, and zero artificial light fixtures]",
    "focal_elements": [
      {
        "id": "element_1",
        "name": "[vật thể trung tâm hoặc chi tiết ẩn dụ chất liệu của cảnh]",
        "material_and_texture": "[chất liệu thủ công hữu hình, bề mặt mờ và cách kết cấu vật thể]",
        "details": "[chi tiết tương tác với ánh sáng, màu sắc hoặc nhân vật]"
      }
    ],
    "staging": "Stage-planar midground layout: [vị trí sắp đặt trái - giữa - phải trên dải trung cảnh ngang, tiền cảnh và hậu cảnh]",
    "real_nature": "[các chất liệu tự nhiên và thủ công có mặt trong cảnh]",
    "backdrop": "Softly out-of-focus yet richly saturated [mô tả hậu cảnh xóa phông bokeh mịn nhưng giữ nguyên độ đậm màu].",
    "lighting": "[mô tả nguồn sáng theo thời gian, hướng chiếu và màu sắc ánh sáng phản xạ lên da nhân vật và cảnh vật]",
    "motion": "[chuyển động tinh tế của gió, ánh sáng, nhân vật hoặc chất liệu]"
  }
}
```

## 6. Giải thích nhiệm vụ từng trường JSON (Cấm xóa)

- **`id` / `type` / `text`:** Định danh prompt, lệnh tạo ảnh và khóa `"NO TEXT"` để chặn chữ viết vô nghĩa xuất hiện trong khung hình.
- **`STYLE.world`:** Giữ nguyên chuỗi khóa phong cách stop-motion châu Âu, màu phim Kodak 35mm đậm sắc độ, không khí trong trẻo `zero milky haze`, bề mặt mịn mờ `sfumato`, đường cong thủ công liêu xiêu `soft organic hand-carved curves with gently wonky asymmetrical contours and zero rigid ruler-straight lines` và bố cục trung cảnh phẳng; chỉ điền cặp tương phản ánh sáng ấm và màu nền lạnh ở cụm cuối câu cho khớp với từng cảnh.
- **`STYLE.palette`:** Phân bổ tỷ lệ màu 70-20-10 của bức ảnh (70% màu khí quyển và bối cảnh lớn; 20% màu kiến trúc, nội thất và quần áo; 10% điểm nhấn màu rực trên phụ kiện, hoa cỏ hoặc nguồn sáng).
- **`CHARACTERS.dna`:** Giữ nguyên chuỗi khóa tỷ lệ cơ thể `1:7.5`, chất liệu da bột giấy hồng đào ấm `warm rosy-apricot` không nếp nhăn, thần thái hiền từ ấm áp `warm benevolent expression (never sad, gloomy, or gaunt)`, mái tóc dày bồng bềnh `abundant full thick soft fibrous hair (never bald)` và quần áo vải mờ không len sợi to.
- **`CHARACTERS.interaction`:** Cụm từ ngắn (dạng `snake_case` hoặc câu ngắn) tóm tắt hành động kết nối giữa các nhân vật hoặc giữa nhân vật với bối cảnh.
- **`CHARACTERS.figures[]`:** Mảng liệt kê các nhân vật hoặc cụm người trong cảnh:
  - `role`: Chỉ rõ độ tuổi thực tế, vóc dáng (`tall slender` đối lập với `short plump`, `round-cheeked` hoặc `petite`), vai trò và vị trí đứng/ngồi trọn vẹn trên mặt phẳng sàn.
  - `look`:
    - *Cảnh có nhân vật chính (từ 1 đến 4 người trung tâm):* Tách riêng từng nhân vật chính, tả rõ cỡ cảnh, góc mặt, chiều cao, độ tròn đầy của má, đường nét hiền từ vui vẻ nhẹ nhàng (`gentle contented smile`, `warm benevolent gaze`, tuyệt đối không dùng `gaunt`, `sad`, `bald`), làn da `warm rosy-apricot matte paper-pulp` (chỉ thêm `soft terracotta-rose blush on cheeks` khi nhân vật ngại ngùng, xúc động hoặc đứng dưới nắng lạnh), mái tóc dày sợi và trang phục tương phản với nhân vật đứng cạnh.
    - *Cảnh đại cảnh nhóm hoặc nhóm người phụ:* Chia thành các cụm bất đối xứng ở độ cao và góc xoay người khác nhau, dùng `impressionistic understated faces with warm gentle demeanor`, phân biệt rõ vóc dáng, kiểu tóc sợi dày và màu áo giữa các cụm.
  - `action`: Tả tư thế tay chân tự nhiên, tương tác đời thường thả lỏng (trò chuyện mỉm cười, nhắm mắt lắng nghe, thao tác nhẹ nhàng) và hướng nhìn dẫn về tâm điểm.
- **`CREATURES[]`:** Mảng mô tả động vật tự nhiên hoặc sinh vật bằng chất liệu thủ công. Nếu cảnh có sinh vật thì điền đối tượng gồm `id`, `name` (số lượng, tên loài và vị trí) và `details` (màu sắc, chất liệu bề mặt và hành động hướng ánh nhìn về tâm điểm); nếu cảnh không có sinh vật thì để mảng rỗng `[]`.
- **`ENVIRONMENT.camera`:** Giữ ống kính `Vintage 50mm lens` với độ sâu trường ảnh mỏng (`shallow optical depth of field`), chỉ rõ chi tiết nào mờ ở tiền cảnh/hậu cảnh (`creamy lens bokeh`), chi tiết nào nét ở trung cảnh và giữ cụm `keeping the air crystal-clear with zero milky fog` để bảo vệ độ trong của ống kính (không thêm `tilt-shift` hay khẩu độ `f/4.0`).
- **`ENVIRONMENT.setting`:** Tả không gian kiến trúc hoặc thiên nhiên mở tràn 4 cạnh khung hình (`orthographic front-on cross-section` nếu là cảnh cắt ngang trong nhà) với đường nét uốn cong thủ công hơi liêu xiêu bất đối xứng (`gently wonky hand-shaped curves`) và bề mặt chất liệu mịn mờ (tránh các tính từ kích nét HDR như `weathered`, `patinated`, `distressed`). Nếu là cảnh ban ngày, khóa cụm `with zero lamps, zero bulbs, and zero artificial light fixtures` ở cuối câu.
- **`ENVIRONMENT.focal_elements[]`:** Điểm nhấn thị giác hoặc chi tiết siêu thực của bức ảnh (kể cả những dải sương mù hoặc khói hữu hình trôi tách lớp nếu là cảnh có sương), tách rõ `name` (tên gọi), `material_and_texture` (chất liệu thủ công hữu hình có đường cong mềm mại) và `details` (cách bắt sáng và tương tác với nhân vật).
- **`ENVIRONMENT.staging`:** Sắp xếp vị trí các khối chính (trái, giữa, phải) dọc theo dải trung cảnh ngang (`Stage-planar midground layout`) và cách khóa tâm điểm (đặt trên bệ đỡ giữa khoảng trống âm, đặt tại ranh giới nền, đóng khung qua cửa kiến trúc, hoặc gom dưới chóp sáng).
- **`ENVIRONMENT.real_nature`:** Liệt kê ngắn gọn 3 đến 4 chất liệu vật lý và thủ công chủ đạo tạo nên cảm giác xúc giác của bức ảnh.
- **`ENVIRONMENT.backdrop`:** Mô tả lớp nền xa phía sau được xóa phông bokeh mịn nhưng vẫn giữ độ đậm đà của màu sắc (`Softly out-of-focus yet richly saturated...`), đảm bảo vùng nền ngay sau lưng tâm điểm thoáng và tách khối rõ ràng.
- **`ENVIRONMENT.lighting`:** Xác định nguồn sáng chính theo thời gian thực tế:
  - *Ban ngày:* Mở đầu bằng `100 percent natural direct ... sunlight with zero artificial lamps`, tả hướng nắng chiếu tạo viền vàng ấm (`golden-honey / amber rim light`) trên da và tóc.
  - *Ban đêm hoặc phòng kín:* Tả nguồn sáng ấm thực tế hoặc chóp sáng chiếu trực tiếp vào tâm điểm, tương phản với vùng bóng tối sâu có màu của môi trường xung quanh.
- **`ENVIRONMENT.motion`:** Một chuyển động vật lý đang diễn ra giữa chừng giúp khung hình tĩnh có sức sống như một cảnh phim đang chạy.

## 7. Chỉ thị tự kiểm duyệt dành cho AI (Khi upload file lên Meta AI / Chat AI)

Khi người dùng tải file này lên cuộc trò chuyện và gửi yêu cầu tạo ảnh hoặc gửi JSON prompt, AI bắt buộc thực hiện quy trình tự kiểm duyệt (Self-Verify) gồm 6 điểm sau trước khi sinh ảnh hoặc xuất kết quả:
1. **Kiểm tra đường cong thủ công:** Mọi kiến trúc, đồ vật, tàu thuyền, bàn ghế, nhạc cụ phải có đường cong hữu cơ mềm mại, hơi phồng hoặc liêu xiêu bất đối xứng (`soft organic hand-carved curves, gently wonky asymmetrical contours, zero rigid ruler-straight lines`). Nếu prompt có vật thể hình hộp thẳng cứng, tự động điều chỉnh sang dáng uốn cong thủ công.
2. **Kiểm tra thần thái hiền từ và mái tóc dày:** Mọi nhân vật (đặc biệt là người già) phải có gương mặt ấm áp, hiền từ, bình yên hoặc mỉm cười nhẹ (`warm benevolent expression, gentle smile`), má đầy đặn và mái tóc dày nhiều sợi (`abundant full thick hair`). Tự động xóa bỏ và thay thế ngay nếu thấy các từ gây mặt buồn, hốc hác, khắc khổ hoặc hói đầu (`gaunt`, `hollow`, `haggard`, `sad`, `gloomy`, `melancholic`, `bald`).
3. **Kiểm tra tư thế tự nhiên và sự đa dạng nhân vật:** Các nhân vật đứng cạnh nhau phải lệch nhau về chiều cao và độ tròn đầy (`tall slender` đối lập với `short plump / round-cheeked / petite`), đứng hoặc ngồi trọn vẹn tự nhiên trên sàn (không bị cắt cụt nửa người trong hộp), tương tác thả lỏng tự nhiên thay vì đứng đơ nhìn cứng nhắc.
4. **Kiểm tra khóa tâm điểm:** Vùng hậu cảnh ngay sau lưng nhân vật chính phải thoáng, đồng nhất hoặc tách biệt rõ về ánh sáng và màu sắc để nổi bật đường viền nhân vật.
5. **Kiểm tra ánh sáng và độ trong ống kính:** Giữ nguyên `crystal-clear air with zero milky haze` để màu phim Kodak 35mm luôn đậm sâu; nếu là cảnh ban ngày, giữ chặt `with zero artificial lamps`.
6. **Kiểm tra bảo toàn cấu trúc JSON:** Giữ đủ toàn bộ các trường của Mục 5 khi truyền lệnh vẽ ảnh.

