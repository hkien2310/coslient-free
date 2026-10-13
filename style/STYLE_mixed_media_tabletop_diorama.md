# STYLE: Mixed-Media Tabletop Diorama

Sa bàn thu nhỏ kết hợp đồ thủ công và thiên nhiên thật, chụp cận cảnh bằng ống kính macro tilt-shift theo ngôn ngữ điện ảnh stop-motion.

---

## 1. Nguyên Lý Thế Giới Sa Bàn & Chất Cảm Vật Liệu (Tactile Craft World)

Mọi cảnh vật trong thế giới này đều là mô hình thu nhỏ được chế tác thủ công bằng tay. Không phân loại vật liệu thành danh mục khô cứng; thay vào đó, bất kỳ chất liệu nào có xúc giác thực tế ở tỷ lệ tí hon đều được tự do sử dụng.

### Nguyên tắc mô tả chất liệu gắn liền với ánh sáng:
Mô tả vật thể đi liền với bề mặt vật lý và cách nó phản ứng với ánh sáng (phản chiếu, xuyên qua, hoặc hấp thụ):
* **Gỗ và bề mặt nhám:** Gỗ sồi, gỗ balsa, ván ghép mộc mạc nhẵn lì hoặc phong hóa, hấp thụ ánh sáng êm, không bóng loáng.
* **Vải dệt may đo:** Vải lanh dệt thô, vải xô, bao tải đay sợi lớn, chỉ khâu mềm buông rủ theo trọng lực. TUYỆT ĐỐI KHÔNG DÙNG ĐỒ LEN ĐAN (no knitted wool, no yarn, no crochet) trên người nhân vật để tránh AI vẽ thành búp bê len nghiệp dư.
* **Kim loại thủ công:** Đồng thau xỉn màu, sắt gỉ nhẹ, thiếc uốn tạo vệt phản quang kim loại mờ đục.
* **Gốm, khoáng chất & vữa:** Đất nung đỏ, gốm men rạn mờ, đá cuội nhẵn, tường vữa tróc vôi lộ lớp gạch bên dưới.
* **Vật liệu xuyên sáng (Translucent Materials):** Giấy da mỏng, giấy bồi, vải voan mỏng cho phép ánh sáng đèn bên trong xuyên qua tạo vầng sáng ấm mềm mại (subsurface glow).
* **Mặt phẳng phản quang & Môi trường lỏng:** Nhựa đúc resin trong vắt, nước gel bóng nhẹ tạo mặt hồ hoặc vũng nước mưa phản chiếu ánh đèn đường.
* **Vật liệu tự nhiên thu nhỏ:** Bông gòn sợi thô làm mây, rêu khô, cành cây khô, sỏi cát thật.

---

## 2. Tạo Hình Nhân Vật (Handcrafted Carved Wooden Figurine)

Nhân vật là tượng gỗ tạc thủ công liền khối, giữ vững cấu trúc giải phẫu chuẩn xác, không dùng khớp nối ma-nơ-canh:

* **Định danh nhân vật:** Luôn dùng `carved wooden figurine` (tượng gỗ tạc thủ công). Tuyệt đối cấm dùng `doll`, `puppet`, hay `mannequin` vì AI sẽ vẽ khớp bi xoay tròn (ball-and-socket joints).
* **Gỗ chỉ là da thịt:** Gỗ chỉ lộ ra ở đầu, mặt, cổ và đôi bàn tay gọt mịn màng (`smooth sanded carved wood`). Toàn bộ trang phục và giày dép may đo riêng bằng vải thật, tuyệt đối không đẽo quần áo hay giày dép dính liền từ gỗ.
* **Trang phục may đo kín thân:** Luôn mặc vải lanh hoặc cotton may đo từ cổ xuống mắt cá chân (`dressed fully in tailored cloth from neck to ankles`). Áo dài tay che kín cổ tay (`long sleeves covering wrists`) và quần/váy phủ kín chân.
* **Giày dép rời:** Mang ủng da mềm tí hon hoặc giày vải dệt khâu tay đặt vững trên mặt đất (`small stitched leather boots or soft cloth shoes`). Cấm giày gỗ, cọc gỗ cụt tiện dính vào chân.
* **Tóc & Râu tự nhiên:** Tóc và râu làm từ sợi chỉ lanh buông rủ tự nhiên (`soft natural thread hair draping naturally`), ôm nhẹ đầu và cằm. Luôn có cụm `full head of hair covering the scalp` để tránh khuôn mẫu hói đầu ở người già.
* **Thần thái và biểu cảm sống động:** Mặt gỗ gọt mịn mờ lì, đôi mắt mở sáng linh hoạt phản chiếu cảm xúc từng cảnh (tập trung, trầm ngâm, mơ màng, an nhiên, kinh ngạc...). Không dùng biểu cảm cười công nghiệp.
* **Dáng người có trọng lực đời thực:** Dáng người dong dỏng, tư thế có độ chùng tự nhiên: vai thả lỏng, tỳ cùi chỏ lên bàn, tựa lưng hoặc dồn trọng tâm.
* **Khóa số lượng nhân vật đơn:** Khi cảnh chỉ có 1 người già, bắt buộc mở đầu `figures.look` bằng: `"A single solitary figurine, the sole human character in the scene..."` và lấp khoảng trống đối trọng bằng đạo cụ sa bàn, tránh việc AI tự vẽ thêm trẻ em.

---

## 3. Không Gian, Bố Cục & Ánh Sáng Điện Ảnh

### Bố cục sân khấu thu nhỏ (Proscenium & Diorama Framing)
* **Tràn viền tuyệt đối (Full-bleed):** Ống kính macro đặt chìm hẳn vào bên trong bối cảnh sa bàn (`camera immersed within the miniature scene`). Địa hình, sàn nhà, vách đá tràn ra ngoài cả 4 cạnh khung hình 16:9 (`seamless edge-to-edge frame`). Tuyệt đối không để lộ mép bàn, gờ khay, bệ đỡ hay căn phòng studio bên ngoài.
* **Mặt cắt sân khấu (Frontal Cutaway):** Góc máy ngang tầm mắt nhìn thẳng vào mặt cắt không gian như một ngôi nhà búp bê hoặc lát cắt viện bảo tàng.
* **Tỷ lệ & Nhịp điệu đồ họa:** Bố cục cân bằng, sắp xếp nhân vật và đạo cụ theo hàng ngang ngay ngắn, mang hơi thở trật tự và tĩnh tại đặc trưng của Wes Anderson và Laika Studios.
* **Ống kính Macro Tilt-shift:** Độ sâu trường ảnh nông làm mờ dịu tiền cảnh và hậu cảnh xa, dồn toàn bộ sự sắc nét vào chi tiết chế tác của chủ thể trung tâm.

### Ánh sáng hai vùng nhiệt độ (Dual-Temperature Lighting)
* **Tương phản ấm - lạnh:** Mọi khung hình đều có sự va đập giữa ánh sáng môi trường mát dịu (`cool ambient light: blue hour, soft overcast, coastal daylight, misty dawn`) và nguồn sáng điểm ấm áp (`warm key / practical light: golden sunlight, amber glow`).
* **Đèn thực tế giấu trong mô hình (Embedded Practical Lights):** Khuyến khích các nguồn sáng vật lý hữu hình đặt ngay trong set quay:
  * Lồng đèn hộp giấy mỏng phát sáng ấm từ bên trong (`glowing translucent paper lanterns`).
  * Bóng đèn dây tóc Edison tí hon tỏa ánh sáng vàng ngà (`warm miniature filament bulbs`).
  * Đèn bão, đèn dầu hắt vệt sáng loang trên mặt nước hoặc bàn gỗ (`oil lantern casting warm localized light`).
  * Chuỗi đèn hạt li ti giấu trong đạo cụ (`embedded warm fairy lights`).
* **Độ tắt sáng vật lý (Inverse-Square Falloff):** Ánh sáng sáng nhất tại nguồn phát và giảm nhanh êm ái ra xung quanh, tạo chiều sâu thị giác. Không có chùm tia laser, không có hào quang thần tiên lơ lửng vô căn cứ.
* **Bụi hạt không khí (Atmospheric Dust Motes):** Cho phép các vệt nắng xiên nhẹ làm nổi rõ những hạt bụi thủ công li ti lơ lửng trong không khí.

### Bảng màu điện ảnh linh hoạt (Dynamic Cinematic Palette)
Không khóa chết một tông màu cho mọi cảnh. Bảng màu tuân theo tỷ lệ:
* **60% Nền trầm / mát dịu (Muted Cool / Neutral Base):** Tường vôi xám ngà, tuyết xanh đá phiến, biển xanh trầm, gạch men rêu phong... làm dịu mắt người xem.
* **30% Tông màu tự nhiên:** Màu gỗ sồi mộc, đất nung đỏ gạch, kim loại xỉn, vải thô.
* **10% Điểm nhấn rực rỡ có chủ đích (Warm Focal Accents):** Một chiếc áo khoác cam đất, chiếc ghế bành nhung đỏ gụ, hay ánh vàng hổ phách của lồng đèn làm bừng sáng khung hình.
* **Highlight kem & Shadow nhung:** Vùng sáng nhất đạt đỉnh ở màu ngà/kem (`creamy highlights`), không bao giờ cháy trắng mất chi tiết (`no clipped white`). Vùng tối được nâng nhẹ (`lifted velvety shadows`), nhuộm chút sắc xanh trầm hoặc nâu ấm, không đen kịt.

---

## 4. Cấu Trúc Prompt JSON

Mỗi prompt là một JSON Object độc lập, toàn bộ mô tả bằng tiếng Anh tự nhiên.

### Khung Cấu Trúc

```json
{
  "id": "<id_prompt>",
  "type": "generate image",
  "STYLE": {
    "world": "Handcrafted stop-motion diorama world, rich tactile miniature craft materials, seamless edge-to-edge environment, raw carved wood and tailored woven fabric",
    "palette": "<cinematic_palette: cool_ambient_base_contrasted_with_warm_accents_and_earth_materials>",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Slender handcrafted carved wooden figurine where smooth sanded wood strictly represents skin and flesh (head, face, and hands only), dressed fully in separately tailored fabric garments from neck to ankles with long sleeves covering arms to wrists and trousers or skirt covering legs, wearing miniature stitched leather boots or cloth shoes (no wooden shoes, no wooden clogs, no carved wooden clothing), expressive carved face with open eyes reflecting the scene's mood, and a full head of soft natural thread hair covering the scalp. Zero exposed mechanical joints, no ball-and-socket joints, no mannequin parts.",
    "figures": [
      {
        "id": "figure_1",
        "role": "<role_and_age>",
        "look": "<appearance_attire_hair_and_expression_in_natural_prose>",
        "action": "<natural_posture_and_activity_with_relaxed_gravity>"
      }
    ],
    "background_figures": "<optional_tiny_distant_silhouettes_for_scale>"
  },
  "CREATURES": [
    {
      "id": "creature_1",
      "role": "<animal_type_and_role>",
      "build": "<relative_size>",
      "material": "<craft_material: clay | terracotta | carved wood | papier-mache>",
      "action": "<specific_activity>",
      "gaze": "<look_direction>"
    }
  ],
  "ENVIRONMENT": {
    "camera": "<macro_tilt_shift_camera_with_frontal_cutaway_or_eye_level_seamless_framing>",
    "setting": "<miniature_location_or_surface_extending_beyond_frame>",
    "focal_elements": [
      {
        "id": "prop_1",
        "item": "<main_prop_name>",
        "material_and_texture": "<tactile_surface_description_and_light_interaction>",
        "details": "<craft_wear_and_finish>"
      }
    ],
    "staging": "<placement_of_figures_creatures_props_with_graphic_balance>",
    "real_nature": "<real_miniature_elements: moss | pebbles | twigs | dried leaves | cotton>",
    "backdrop": "<softly_blurred_background_retaining_depth>",
    "lighting": "<dual_temperature_lighting: cool_ambient_paired_with_warm_practical_lights_and_organic_falloff>",
    "motion": "<optional_environmental_motion: drifting_dust_motes | paper_drifting | gentle_breeze>"
  },
  "SURREAL": {
    "type": "<displacement | macro_interaction | absurd_setting | scale_contrast>",
    "description": "<poetic_craft_based_surreal_situation_with_tangible_materials_and_natural_physics>"
  }
}
```

---

## 5. Quy Tắc Từng Trường

* **`id`**: Định danh của prompt (ví dụ: `prompt_001`).
* **`type`**: Giá trị cố định luôn là `"generate image"` để phân loại tác vụ sinh ảnh.

### Khối 1: `STYLE` (Bắt buộc)
* **`world`**: Chuỗi chuẩn hóa định vị thế giới: `Handcrafted stop-motion diorama world, rich tactile miniature craft materials, seamless edge-to-edge environment, raw carved wood and tailored woven fabric`. Khóa chặt phong cách sa bàn thủ công, ngăn chặn hoàn toàn ảnh chụp người thật và 3D CGI nhựa bóng.
* **`palette`**: Mô tả bảng màu cụ thể của cảnh theo công thức điện ảnh: 60% Nền mát dịu/trung tính + 30% Tông đất tự nhiên + 10% Điểm nhấn ấm áp rực rỡ (Ví dụ: `Dusty slate blue and weathered off-white base with natural blond wood and glowing amber accents`).
* **`aspect_ratio`**: Luôn là `"16:9"`.

### Khối 2: `CHARACTERS` (Có khi có người)
* **`dna`**: Câu định nghĩa chuẩn hóa bắt buộc cho tượng gỗ tạc thủ công:
  `Slender handcrafted carved wooden figurine where smooth sanded wood strictly represents skin and flesh (head, face, and hands only), dressed fully in separately tailored fabric garments from neck to ankles with long sleeves covering arms to wrists and trousers or skirt covering legs, wearing miniature stitched leather boots or cloth shoes (no wooden shoes, no wooden clogs, no carved wooden clothing), expressive carved face with open eyes reflecting the scene's mood, and a full head of soft natural thread hair covering the scalp. Zero exposed mechanical joints, no ball-and-socket joints, no mannequin parts.`
* **`figures`**: Danh sách nhân vật trong cảnh:
  * *`id`*: Mã định danh (`figure_1`, `figure_2`...) để khối `staging` gọi tên vị trí.
  * *`role`*: Vai trò và lứa tuổi cụ thể của nhân vật.
  * *`look`*: Diện mạo, thần thái, trang phục và râu tóc viết thành văn xuôi tự nhiên. Bắt buộc tuân thủ:
    - Khi cảnh chỉ có 1 nhân vật: Bắt buộc mở đầu bằng `A single solitary figurine, the sole human character in the scene...` để ngăn AI tự vẽ thêm trẻ em lấp chỗ trống.
    - Luôn có `full head of hair covering the scalp` để chống khuôn mẫu hói đầu ở người già.
    - Luôn có `dressed fully in tailored cloth with long sleeves and flowing skirt/trousers covering down to ankles, wearing miniature stitched leather boots or soft cloth shoes` (trang phục vải may đo kín thân, giày dép rời; cấm quần áo/giày tiện từ gỗ; cấm đồ len đan).
    - Biểu cảm cơ mặt sống động, mắt mở linh hoạt theo tâm trạng cảnh (`expressive, soulful face with open lively eyes reflecting mood...`).
  * *`action`*: Tư thế toàn thân tự nhiên có trọng lực đời thực (vai thả lỏng, tỳ cùi chỏ lên bàn, đầu hơi nghiêng, chùng lưng tự nhiên) kèm theo hành động đang làm.
* **Quy tắc trọn vẹn hình thể:** Dù máy quay cận cảnh thao tác tay, vẫn giữ đủ `look` và `action` để AI giữ giải phẫu thống nhất, tránh lỗi bàn tay trôi nổi một mình.
* **`background_figures` (Tùy chọn):** Chấm bóng người tí hon mờ ở hậu cảnh xa để đo tỷ lệ không gian, không tả chi tiết.

### Khối 3: `CREATURES` (Có khi có động vật)
* Động vật làm từ đất nung (`terracotta`), đất sét nung mờ (`matte clay`), gỗ gọt (`carved wood`) hoặc giấy bồi (`papier-mâché`), tách biệt với chất gỗ của người để AI không ghép nhầm chi tiết. TUYỆT ĐỐI KHÔNG DÙNG NỈ ÉP HAY LEN (no felted wool, no wool, no yarn).
* Cảnh ngụ ngôn: Khi cảnh chỉ có muông thú sinh hoạt, dùng khối `CREATURES` và bỏ khối `CHARACTERS`.
* Các trường gồm: *`id`*, *`role`* (loài vật và vai trò), *`build`* (tỷ lệ kích thước), *`material`* (chất liệu chế tác: clay, terracotta, carved wood, papier-mache), *`action`* (hành động cụ thể), *`gaze`* (hướng nhìn).

### Khối 4: `ENVIRONMENT` (Bắt buộc)
* **`camera`**: Ống kính macro tilt-shift, góc ngang tầm mắt hoặc mặt cắt sân khấu (frontal cutaway). Bắt buộc quy định khung hình tràn viền (`seamless edge-to-edge frame, no visible tabletop edge, no tray or diorama borders, environment extends beyond all edges`).
* **`setting`**: Không gian thu nhỏ với bề mặt đất, đá, rêu hoặc sàn gỗ tràn ra ngoài mép khung hình.
* **`focal_elements`**: Danh sách đồ vật chính (`prop_1`, `prop_2`...): gồm *`id`*, *`item`* (tên vật thể), *`material_and_texture`* (mô tả bề mặt xúc giác và cách phản ứng ánh sáng: đồng xỉn phản quang mờ, gỗ sồi nhám lì, giấy da mỏng xuyên sáng, vũng nhựa resin trong suốt), *`details`* (chi tiết gia công, vết mòn thời gian).
* **`staging`**: Vị trí sắp đặt các `figure_*`, `creature_*`, `prop_*` trong khung hình theo nhịp điệu đồ họa cân bằng.
* **`real_nature`**: Vật liệu tự nhiên thật ở cự ly tiếp xúc (rêu khô, viên sỏi, cành cây khô, bụi bông gòn thô làm mây).
* **`backdrop`**: Hậu cảnh xa làm mờ nhẹ để tạo độ sâu trường ảnh tilt-shift, luôn kín khung hình không để lộ studio bên ngoài.
* **`lighting`**: Luôn quy định ánh sáng hai vùng nhiệt độ: ánh sáng môi trường mát dịu (`cool ambient light: blue hour, overcast, coastal daylight`) kết hợp với nguồn sáng điểm ấm áp từ đèn thực tế giấu trong mô hình (`embedded practical lights: glowing paper lanterns, miniature warm filament bulbs, oil lanterns`) tỏa sáng với độ suy giảm tự nhiên (`organic soft falloff`), có thể kèm bụi hạt không khí (`subtle floating dust motes`).
* **`motion` (Tùy chọn):** Chuyển động môi trường (vệt khói bốc, mảnh giấy bay lơ lửng, gió lay nhẹ).

### Khối 5: `SURREAL` (Bắt buộc 100% mọi prompt)
* **Bản chất:** Mọi cảnh bắt buộc phải có một chi tiết phi lý mộc mạc mang tính thơ, bắt nguồn từ vật liệu thủ công hữu hình. Nhân vật luôn giữ thái độ an nhiên, tập trung vào công việc.
* **`type`**: 1 trong 4 dạng phi lý:
  - `displacement`: Thay thế bộ phận đồ vật bằng vật thể tự nhiên (bánh răng bằng quả thông/hạt dẻ, giọt nước bằng hạt cườm, mái chèo bằng cành cây).
  - `macro_interaction`: Tương tác với vật thể tự nhiên phóng đại hoặc siêu nhỏ (lá làm dù che/thuyền bơi, vỏ hạt dẻ làm ghế, vỏ trứng làm bồn cây).
  - `absurd_setting`: Đặt sinh hoạt đời thường vào vị trí bất thường (tiệm bánh trong hốc rễ cây, đọc sách trên nhánh nấm, câu cá trong tách trà).
  - `scale_contrast`: Tương phản tỷ lệ giữa các đồ vật mộc mạc.
* **`description`**: Mô tả chi tiết tình huống phi lý bằng vật liệu thủ công (mây bằng bông gòn neo dây thừng, tóc rụng hóa chim bồ câu giấy, lồng đèn hộp giấy thả trên nền tuyết lạnh). Cho phép và khuyến khích các vật thể thủ công phát sáng có nguồn phát vật lý (đèn lồng giấy, bóng đèn dây tóc nhỏ giấu bên trong, vệt phản chiếu mặt nước). Tuyệt đối cấm hiệu ứng kỹ xảo CGI ma quái (tia laser, hạt bụi phát sáng lơ lửng kiểu tiên nữ, hào quang ma thuật neon).
