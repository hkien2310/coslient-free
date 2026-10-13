# STYLE: Mixed-Media Tabletop Diorama

Sa bàn thu nhỏ kết hợp đồ thủ công và thiên nhiên thật, chụp cận cảnh bằng ống kính macro tilt-shift.

---

## 1. Hai Lớp Chất Liệu

* **Đồ thủ công:** Nhân vật, kiến trúc và đồ đạc làm từ gỗ mộc, vải lanh may đo, đất nung, gốm mờ. Bề mặt nhám mờ, lộ rõ vân gỗ, vết đẽo gọt và thớ vải dệt. TUYỆT ĐỐI KHÔNG DÙNG ĐỒ LEN (no wool, no yarn, no knitting, no felted wool).
* **Thiên nhiên thật:** Rêu tươi, cành cây khô, sỏi cuội, đất cát, quả dại thu nhỏ. Ánh sáng tự nhiên có hướng rọi rõ, bóng đổ êm.

---

## 2. Tạo Hình Nhân Vật (Handcrafted Carved Wooden Figurine)

* **Tượng điêu khắc thủ công (Figurine - Tuyệt đối không dùng doll/puppet):** Định danh nhân vật luôn là `carved wooden figurine` (tượng gỗ tạc thủ công liền khối). Tuyệt đối không dùng chữ `doll`, `puppet`, hay `mannequin` vì AI sẽ vẽ khớp bi (ball-and-socket joints) như tượng ma-nơ-canh vẽ tranh.
* **Nguyên tắc "Gỗ chỉ là da thịt, trang phục là trang phục rời":** Gỗ CHỈ ĐẠI DIỆN CHO DA THỊT (chỉ để lộ đầu, mặt, cổ và đôi bàn tay gỗ gọt mịn). Toàn bộ trang phục và giày dép là phụ kiện may đo riêng bằng chất liệu thủ công thật, TUYỆT ĐỐI KHÔNG đẽo tiện từ gỗ (no carved wooden clothes, no carved wooden shoes/clogs).
* **Trang phục vải may đo toàn thân từ cổ tới chân (Chống lộ khớp & chống đẽo quần áo gỗ):** Thân tượng luôn được mặc kín bằng vải lanh hoặc vải cotton dệt thủ công may đo thật từ cổ xuống tận mắt cá chân (`dressed fully in tailored linen cloth from neck to ankles`). Luôn gồm cả áo dài tay che kín cổ tay (`long fabric sleeves covering arms to wrists`) VÀ váy/quần vải mềm rủ phủ kín chân (`flowing fabric skirt or trousers covering legs`). Tuyệt đối không dùng đồ len hay áo len đan.
* **Giày dép thủ công rời (Tuyệt đối không dùng giày gỗ):** Dưới chân luôn mang ủng da mềm tí hon hoặc giày vải khâu tay đặt vững trên mặt đất (`small stitched leather boots or soft cloth shoes planted firmly on the ground`). Cấm tuyệt đối giày gỗ, guốc mộc, hay cọc gỗ cụt tiện dính vào chân (no wooden shoes, no wooden clogs, no carved wooden stumps).
* **Tóc & Râu buông rủ tự nhiên (Chống hói & chống xù):** Luôn có cụm `full head of hair covering the scalp` để chống khuôn mẫu hói đầu ở người già. Tóc và râu làm từ sợi chỉ lanh mềm buông rủ tự nhiên theo trọng lực (`soft natural linen thread hair draping naturally`), ôm nhẹ đầu và cằm, không ép thẳng đơ và không xù bông gòn. Tuyệt đối không dùng sợi len (no wool/yarn).
* **Thả rông biểu cảm theo cảnh (Chống mặt đơ ma-nơ-canh):** Mặt gỗ gọt nhẵn mịn mờ lì, đôi mắt mở sáng linh hoạt (`expressive carved wooden face with open eyes reflecting the mood`). Không đóng đinh một biểu cảm cười hiền từ cho mọi hoàn cảnh; người viết được tự do thả rông biểu cảm tùy theo tình huống từng cảnh (tò mò, tập trung cao độ, ngạc nhiên, suy tư, thư thái, mơ màng, mỉm cười...).
* **Dáng người có trọng lực (Chống đơ cọc gỗ):** Tỉ lệ dong dỏng cao ráo, nhưng tư thế luôn có độ chùng tự nhiên của đời thực: vai thả lỏng, đầu hơi nghiêng, tỳ tay lên bàn, tựa lưng hoặc dồn trọng tâm (`relaxed posture, resting forearms on table, slight natural tilt`).
* **Khóa số lượng nhân vật đơn (Chống đẻ thêm người lạ):** Khung hình 16:9 rất rộng, khi cảnh chỉ có 1 người già thì AI thường tự vẽ thêm một đứa bé đứng cạnh để lấp khoảng trống. Khi cảnh chỉ có 1 người, bắt buộc mở đầu `figures.look` bằng: `"A single solitary figurine, the sole human character in the scene..."` và lấp khoảng trống đối trọng bằng đạo cụ sa bàn (`props`) hoặc thiên nhiên thật, tuyệt đối không để trống nửa khung hình.
* **Không nhồi nhét từ khóa (Tả thoáng để AI sáng tạo):** Mô tả nhân vật bằng văn miêu tả tự nhiên, gợi mở thần thái và không gian thay vì nhồi một chuỗi từ khóa rời rạc. Càng ép tiểu tiết vụn vặt, AI càng nghẽn token và khóa chết sự sống động của nhân vật.

---

## 3. Không Gian & Màu Sắc

* **Tràn viền tuyệt đối (Full-bleed / Edge-to-Edge - Chống lộ viền sa bàn):** Máy quay macro đặt chìm hẳn vào bên trong bối cảnh sa bàn (`camera immersed within the miniature scene`). Bề mặt mặt đất, sàn nhà, vách đá, cây cối trải dài vô tận ra ngoài cả 4 cạnh của khung hình 16:9 (`seamless miniature environment extending beyond all edges of the frame`). Tuyệt đối cấm để lộ mép bàn, gờ khay sa bàn, bệ đỡ, hoặc căn phòng studio bên ngoài (`no visible tabletop edges, no diorama borders, trays, pedestals, or studio background`).
* **Đường nét:** Mọi vật thể trong sa bàn (nhân vật, kiến trúc, bàn ghế, đạo cụ, dụng cụ, địa hình) đều bo tròn mép mộc mạc, tránh các góc nhọn sắc hay mũi nhọn chông gai.
* **Bảng màu chủ đạo:** Nền trầm màu xám than / đá phiến (`charcoal / slate`), điểm xuyết sắc vàng mù tạt / hổ phách (`saffron-mustard / warm amber`), phối cùng màu gỗ sáng và xanh rêu.
* **Góc máy:** Đa dạng góc máy (ngang tầm mắt, cận cảnh macro, góc thấp nhìn lên, góc cao nhìn xuống bao quát sa bàn), luôn dùng ống kính macro tilt-shift với độ sâu trường ảnh mỏng để tôn lên chi tiết chế tác và tỷ lệ thu nhỏ. Cảnh luôn kín tràn viền.

---

## 4. Cấu Trúc Prompt JSON

Mỗi prompt là một JSON Object độc lập. Toàn bộ giá trị mô tả bằng tiếng Anh tự nhiên.

### Quy Tắc Điều Kiện Khối
* **Bắt buộc (100% mọi prompt):** `STYLE`, `ENVIRONMENT`, và `SURREAL`. Mọi cảnh trong dự án bắt buộc phải có yếu tố phi lý mộc mạc (Surreal diorama).
* **Có điều kiện:**
  * **`CHARACTERS`**: Chỉ xuất hiện khi cảnh có con người. Đã có người thì mô tả đầy đủ (`dna`, `figures` hoặc `background_figures`). Cảnh không có người thì bỏ khối này.
  * **`CREATURES`**: Chỉ xuất hiện khi cảnh có động vật (`role`, `build`, `material`, `action`, `gaze`). Cảnh không có động vật thì bỏ khối này.
  * **`motion`**: Chỉ xuất hiện khi có chuyển động môi trường (lá bay, khói bốc, gió lay...).

### 4.1. Khung Cấu Trúc Prompt

```json
{
  "id": "<id_prompt>",
  "type": "generate image",
  "STYLE": {
    "world": "Handcrafted mixed-media diorama world, seamless edge-to-edge miniature environment, raw carved wood and genuine tailored linen fabric",
    "palette": "Charcoal and slate with glowing saffron-mustard and warm amber accents, blond wood",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Slender handcrafted carved wooden figurine where wood strictly represents skin and flesh (head, face, and hands only), dressed fully in separately tailored fabric garments from neck to ankles with long sleeves covering arms to wrists and trousers or skirt covering legs, wearing miniature stitched leather boots or cloth shoes (no wooden shoes, no wooden clogs, no carved wooden clothing), expressive carved face with open eyes reflecting the scene's mood, and a full head of soft natural thread hair covering the scalp. Zero exposed mechanical joints, no ball-and-socket joints, no mannequin parts.",
    "figures": [
      {
        "id": "figure_1",
        "role": "<role_and_age>",
        "look": "<appearance_attire_hair_and_expression_in_natural_prose>",
        "action": "<natural_posture_and_activity_with_relaxed_gravity>"
      },
      {
        "id": "figure_2",
        "role": "<optional_second_figure_role>",
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
      "material": "<craft_material: matte clay | terracotta | carved wood>",
      "action": "<specific_activity>",
      "gaze": "<look_direction>"
    }
  ],
  "ENVIRONMENT": {
    "camera": "<macro_tilt_shift_camera_angle_with_seamless_edge_to_edge_framing>",
    "setting": "<miniature_location_or_surface_extending_beyond_frame>",
    "focal_elements": [
      {
        "id": "prop_1",
        "item": "<main_prop_name>",
        "material": "<craft_material>",
        "details": "<surface_details_and_wear>"
      },
      {
        "id": "prop_2",
        "item": "<secondary_prop_name>",
        "material": "<craft_material>",
        "details": "<surface_details>"
      }
    ],
    "staging": "<placement_of_figures_creatures_props_in_frame>",
    "real_nature": "<real_miniature_natural_elements: moss | pebbles | twigs | dried leaves>",
    "backdrop": "<softly_blurred_background>",
    "lighting": "<directional_natural_light_and_shadows>",
    "motion": "<optional_environmental_motion>"
  },
  "SURREAL": {
    "type": "<displacement | macro_interaction | absurd_setting | scale_contrast>",
    "description": "<craft_based_surreal_situation_with_unbothered_character>"
  }
}
```

---

### 4.2. Quy Tắc Từng Trường

* **`id`**: Định danh của prompt.
* **`type`**: Field cứng cố định luôn là `"generate image"` để phân loại tác vụ render ảnh.

#### Khối 1: `STYLE` (Bắt buộc)
* **`world`**: Khóa thể loại sa bàn thu nhỏ thủ công tràn viền (`Handcrafted mixed-media diorama world, edge-to-edge miniature environment, raw carved wood and genuine tailored linen fabric`). Giữ nguyên ở mọi prompt để tránh ảnh chụp người thật, tránh 3D CGI và tránh lộ mép bàn/studio.
* **`palette`**: Khóa bảng màu nhận diện (`Charcoal and slate with glowing saffron-mustard and warm amber accents, blond wood`). Giữ đồng nhất toàn dự án.
* **`aspect_ratio`**: Tỷ lệ khung hình (luôn là `"16:9"`).

#### Khối 2: `CHARACTERS` (Có khi có người)
* **`dna`**: Câu định nghĩa gốc chuẩn hóa cho tượng gỗ tạc thủ công (`carved wooden figurine`), quy định rõ gỗ CHỈ LÀ DA THỊT (chỉ đầu, mặt và bàn tay để lộ), mặc kín trang phục vải lanh may đo rời từ cổ xuống chân (`dressed fully in tailored linen cloth from neck to ankles`), tay áo dài che kín cổ tay, quần/váy vải che chân, mang ủng da mềm hoặc giày vải dệt khâu tay (TUYỆT ĐỐI KHÔNG làm giày dép hay quần áo bằng gỗ). Mặt gỗ chạm khắc giàu biểu cảm với đôi mắt mở sáng linh hoạt phản chiếu tâm trạng cảnh, tóc sợi chỉ lanh buông rủ tự nhiên phủ kín da đầu. Cấm triệt để khớp bi ma-nơ-canh và đồ len (no wool/yarn, no ball-and-socket joints).
* **`figures`**: Danh sách nhân vật trong cảnh (tối giản còn 2 trường mô tả tự nhiên để AI sáng tạo dáng, không mổ xẻ vụn vặt):
  - *`id`*: Mã định danh (`figure_1`, `figure_2`...) để `staging` gọi tên.
  - *`role`*: Vai trò và lứa tuổi cụ thể của nhân vật.
  - *`look`*: Diện mạo, thần thái, trang phục và râu tóc viết thành 1 câu văn xuôi gợi cảm tự nhiên. Bắt buộc có:
    - Khi chỉ có 1 nhân vật: Bắt buộc mở đầu bằng `A single solitary figurine, the sole human character in the scene...` (chống AI tự vẽ thêm đứa trẻ lấp chỗ trống).
    - `full head of hair covering scalp` (chống hói).
    - `dressed fully in tailored linen cloth with long sleeves and flowing skirt/trousers covering down to ankles, wearing miniature stitched leather boots or soft cloth shoes` (trang phục vải lanh may đo rời và giày da/vải khâu tay; tuyệt đối không đẽo khắc quần áo hay giày bằng gỗ; không len; không lộ khớp bi).
    - Biểu cảm thả rông tự do theo tâm trạng cảnh nhưng phải có chi tiết cơ mặt sống động (`expressive, soulful face with raised warm brows, subtle mouth curvature, open lively eyes reflecting mood...`). Tuyệt đối không nhồi nhét chuỗi từ khóa kỹ thuật rời rạc.
  - *`action`*: Tư thế toàn thân tự nhiên có trọng lực đời thực (vai thả lỏng, tỳ cùi chỏ lên bàn, đầu hơi nghiêng, chùng lưng tự nhiên) kèm theo việc đang làm.
* **Quy tắc trọn vẹn hình thể:** Dù máy quay cận cảnh thao tác tay, vẫn giữ đủ `look` và `action` để AI giữ giải phẫu thống nhất, tránh lỗi bàn tay trôi nổi một mình.
* **Tham chiếu thực thể:** Mọi đối tượng tương tác trong `action`, `staging` phải có ID rõ ràng (`figure_*`, `creature_*`, `prop_*`).
* **`background_figures` (Tùy chọn):** Chấm bóng người tí hon mờ ở hậu cảnh xa để đo tỷ lệ không gian, không tả chi tiết.

#### Khối 3: `CREATURES` (Có khi có động vật)
* **Chất liệu riêng:** Động vật làm từ đất nung (`terracotta`), đất sét nung mờ (`matte clay`) hoặc gỗ mộc đẽo gọt (`carved wood`), tách biệt với chất gỗ của người để AI không ghép nhầm chi tiết. TUYỆT ĐỐI KHÔNG DÙNG NỈ ÉP HAY LEN (no felted wool, no wool, no yarn).
* **Cảnh ngụ ngôn:** Khi cảnh chỉ có muông thú sinh hoạt, dùng khối `CREATURES` và bỏ khối `CHARACTERS`.
* Các trường gồm: *`id`*, *`role`* (loài vật và vai trò), *`build`* (tỷ lệ kích thước), *`material`* (chất liệu chế tác: clay, terracotta, carved wood), *`action`* (hành động cụ thể), *`gaze`* (hướng nhìn).

#### Khối 4: `ENVIRONMENT` (Bắt buộc)
* **`camera`**: Góc máy linh hoạt (ngang tầm mắt, góc thấp, góc cao, cận cảnh macro tilt-shift). Bắt buộc quy định khung hình tràn viền (`seamless edge-to-edge frame, no visible tabletop edge, no tray or diorama borders, environment extends beyond all edges`).
* **`setting`**: Không gian thu nhỏ với bề mặt đất, đá, rêu hoặc sàn gỗ tràn ra ngoài mép khung hình.
* **`focal_elements`**: Danh sách đồ vật chính (`prop_1`, `prop_2`...): gồm *`id`*, *`item`* (tên vật thể), *`material`* (gỗ, gốm, kim loại mờ, đá, vải lanh... TUYỆT ĐỐI KHÔNG LEN/YARN), *`details`* (chi tiết gia công, mép bo tròn mộc mạc).
* **`staging`**: Vị trí sắp đặt các `figure_*`, `creature_*`, `prop_*` trong khung hình và khoảng trống trên mặt nền.
* **`real_nature`**: Vật liệu tự nhiên thật ở cự ly tiếp xúc (rêu tươi, viên sỏi, cành cây khô, vỏ hạt, quả dại).
* **`backdrop`**: Hậu cảnh xa làm mờ nhẹ để tạo độ sâu trường ảnh tilt-shift, luôn kín khung hình không để lộ phòng ngoài.
* **`lighting`**: Hướng rọi sáng tự nhiên (ánh nắng cửa sổ, ánh lửa ấm), tạo bóng đổ mềm êm.
* **`motion` (Tùy chọn):** Chuyển động môi trường (vệt khói bốc, lá khô bay, gió lay nhẹ).

#### Khối 5: `SURREAL` (Bắt buộc 100% mọi prompt)
* **Bản chất:** Mọi cảnh bắt buộc phải có một chi tiết phi lý mộc mạc — đưa đồ vật hoặc hành động bình thường vào hoàn cảnh bất thường bằng vật liệu sa bàn thủ công. Nhân vật luôn giữ thái độ an nhiên, bình thản làm việc.
* **`type`**: 1 trong 4 dạng phi lý:
  - `displacement`: Thay thế bộ phận đồ vật bằng vật thể tự nhiên (bánh răng bằng quả thông/hạt dẻ, giọt nước bằng hạt cườm, mái chèo bằng cành cây).
  - `macro_interaction`: Tương tác với vật thể tự nhiên phóng đại hoặc siêu nhỏ (lá làm đèn bàn/thuyền bơi, vỏ hạt dẻ làm ghế, vỏ trứng làm bồn cây).
  - `absurd_setting`: Đặt sinh hoạt đời thường vào vị trí bất thường (tiệm bánh trong hốc rễ cây, đọc sách trên nhánh nấm, câu cá trong tách trà).
  - `scale_contrast`: Tương phản tỷ lệ giữa các đồ vật mộc mạc.
* **`description`**: Mô tả chi tiết tình huống phi lý bằng vật liệu thủ công (gỗ, vải lanh, đất nung, gốm mờ, hổ phách, đá). CẤM TUYỆT ĐỐI dùng len (no wool/yarn) và CẤM TUYỆT ĐỐI dùng ánh sáng (phát sáng, đốm sáng bay lơ lửng, tia sáng ma thuật, vệt sáng, glowing, luminous, sparkles) để tạo chi tiết siêu thực vì sẽ gây hiệu ứng CGI rẻ tiền ("phèn chúa"). Ánh sáng trong cảnh chỉ tồn tại như nguồn sáng tự nhiên của môi trường (nắng, lửa, trăng). Siêu thực bắt buộc phải đến từ chất liệu, chạm khắc, tỷ lệ hoặc công năng vật lý hữu hình.
