# STYLE: Mixed-Media Tabletop Diorama

Sa bàn thu nhỏ kết hợp đồ thủ công và thiên nhiên thật, chụp cận cảnh bằng ống kính macro tilt-shift.

---

## 1. Hai Lớp Chất Liệu

* **Đồ thủ công:** Nhân vật, kiến trúc và đồ đạc làm từ gỗ mộc, vải dệt, nỉ ép, đất nung. Bề mặt nhám mờ, lộ rõ vân gỗ, vết đẽo gọt và thớ vải.
* **Thiên nhiên thật:** Rêu tươi, cành cây khô, sỏi cuội, đất cát, quả dại thu nhỏ. Ánh sáng tự nhiên có hướng rọi rõ, bóng đổ êm.

---

## 2. Tạo Hình Nhân Vật (Handcrafted Carved Wooden Figurine)

* **Tượng điêu khắc thủ công (Figurine - Tuyệt đối không dùng doll/puppet):** Định danh nhân vật luôn là `carved wooden figurine` (tượng gỗ tạc thủ công liền khối). Tuyệt đối không dùng chữ `doll`, `puppet`, hay `mannequin` vì AI sẽ vẽ khớp bi (ball-and-socket joints) như tượng ma-nơ-canh vẽ tranh.
* **Vải mềm gánh độ mềm (Chống lộ khớp):** Trang phục vải dệt thủ công thật (lanh, len) luôn có tay áo dài che kín toàn bộ cánh tay tới tận cổ tay (`long fabric sleeves covering arms to wrists`). Chỉ để lộ bàn tay gỗ tạc mềm mại. Vải mềm rủ tự nhiên vừa tạo độ sống động, vừa che hoàn toàn thân gỗ để AI không có chỗ vẽ khớp.
* **Tóc & Râu buông rủ tự nhiên (Chống hói & chống xù):** Luôn có cụm `full head of hair covering the scalp` để chống khuôn mẫu hói đầu ở người già. Tóc và râu làm từ sợi chỉ lanh mềm buông rủ tự nhiên theo trọng lực (`soft natural thread hair draping naturally`), ôm nhẹ đầu và cằm, không ép thẳng đơ và không xù bông gòn.
* **Biểu cảm ấm áp, có thần (Chống mặt đơ ma-nơ-canh):** Mặt gỗ gọt nhẵn mịn mờ lì, toát lên nét hiền từ, tươi vui, mắt mở to tròn hiền hòa có nét cười (`warm friendly carved face with gentle smiling eyes`). Tránh mổ xẻ vụn vặt từng chi tiết mắt mũi miệng như thông số kỹ thuật.
* **Dáng người có trọng lực (Chống đơ cọc gỗ):** Tỉ lệ dong dỏng cao ráo, nhưng tư thế luôn có độ chùng tự nhiên của đời thực: vai thả lỏng, đầu hơi nghiêng, tỳ tay lên bàn, tựa lưng hoặc dồn trọng tâm (`relaxed posture, resting forearms on table, slight natural tilt`).
* **Không nhồi nhét từ khóa (Tả thoáng để AI sáng tạo):** Mô tả nhân vật bằng văn miêu tả tự nhiên, gợi mở thần thái và không gian thay vì nhồi một chuỗi từ khóa rời rạc. Càng ép tiểu tiết vụn vặt, AI càng nghẽn token và khóa chết sự sống động của nhân vật.

---

## 3. Không Gian & Màu Sắc

* **Đường nét:** Mọi vật thể trong sa bàn (nhân vật, kiến trúc, bàn ghế, đạo cụ, dụng cụ, địa hình) đều bo tròn mép mộc mạc, tránh các góc nhọn sắc hay mũi nhọn chông gai.
* **Bảng màu chủ đạo:** Nền trầm màu xám than / đá phiến (`charcoal / slate`), điểm xuyết sắc vàng mù tạt / hổ phách (`saffron-mustard / warm amber`), phối cùng màu gỗ sáng và xanh rêu.
* **Góc máy:** Đa dạng góc máy (ngang tầm mắt, cận cảnh macro, góc thấp nhìn lên, góc cao nhìn xuống bao quát sa bàn), luôn dùng ống kính macro tilt-shift với độ sâu trường ảnh mỏng để tôn lên chi tiết chế tác và tỷ lệ thu nhỏ.

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
  "STYLE": {
    "world": "Handcrafted mixed-media diorama, raw carved wood and genuine tailored linen fabric",
    "palette": "Charcoal and slate with glowing saffron-mustard and warm amber accents, blond wood",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Slender handcrafted carved wooden figurine in soft tailored linen clothes, solid seamless wood body under long fabric sleeves, warm friendly carved face with gentle smiling eyes, and a full head of soft natural thread hair covering the scalp.",
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
      "material": "<craft_material: felted wool | clay | wood>",
      "action": "<specific_activity>",
      "gaze": "<look_direction>"
    }
  ],
  "ENVIRONMENT": {
    "camera": "<macro_tilt_shift_camera_angle>",
    "setting": "<miniature_location_or_surface>",
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

#### Khối 1: `STYLE` (Bắt buộc)
* **`world`**: Khóa thể loại sa bàn thu nhỏ thủ công (`Handcrafted mixed-media diorama, raw carved wood and genuine tailored linen fabric`). Giữ nguyên ở mọi prompt để tránh ảnh chụp người thật hoặc 3D CGI.
* **`palette`**: Khóa bảng màu nhận diện (`Charcoal and slate with glowing saffron-mustard and warm amber accents, blond wood`). Giữ đồng nhất toàn dự án.
* **`aspect_ratio`**: Tỷ lệ khung hình (luôn là `"16:9"`).

#### Khối 2: `CHARACTERS` (Có khi có người)
* **`dna`**: Câu định nghĩa gốc chuẩn hóa cho tượng gỗ tạc thủ công (`carved wooden figurine`), thân liền khối giấu kín dưới tay áo vải dài, mặt ấm áp có nét cười hiền dịu, tóc sợi chỉ buông rủ tự nhiên phủ kín da đầu.
* **`figures`**: Danh sách nhân vật trong cảnh (tối giản còn 2 trường mô tả tự nhiên để AI sáng tạo dáng, không mổ xẻ vụn vặt):
  - *`id`*: Mã định danh (`figure_1`, `figure_2`...) để `staging` gọi tên.
  - *`role`*: Vai trò và lứa tuổi cụ thể của nhân vật.
  - *`look`*: Diện mạo, thần thái, trang phục và râu tóc viết thành 1 câu văn xuôi gợi cảm tự nhiên. Bắt buộc có: `full head of hair covering scalp` (chống hói), `long fabric sleeves covering arms to wrists` (áo dài tay che kín tay chống lộ khớp bi), và biểu cảm ấm áp có nét cười (`warm friendly face with gentle smiling eyes`). Tuyệt đối không nhồi nhét chuỗi từ khóa kỹ thuật rời rạc.
  - *`action`*: Tư thế toàn thân tự nhiên có trọng lực đời thực (vai thả lỏng, tỳ cùi chỏ lên bàn, đầu hơi nghiêng, chùng lưng tự nhiên) kèm theo việc đang làm.
* **Quy tắc trọn vẹn hình thể:** Dù máy quay cận cảnh thao tác tay, vẫn giữ đủ `look` và `action` để AI giữ giải phẫu thống nhất, tránh lỗi bàn tay trôi nổi một mình.
* **Tham chiếu thực thể:** Mọi đối tượng tương tác trong `action`, `staging` phải có ID rõ ràng (`figure_*`, `creature_*`, `prop_*`).
* **`background_figures` (Tùy chọn):** Chấm bóng người tí hon mờ ở hậu cảnh xa để đo tỷ lệ không gian, không tả chi tiết.

#### Khối 3: `CREATURES` (Có khi có động vật)
* **Chất liệu riêng:** Động vật làm từ nỉ ép, len thô hoặc đất nung, tách biệt với chất gỗ của người để AI không ghép nhầm chi tiết.
* **Cảnh ngụ ngôn:** Khi cảnh chỉ có muông thú sinh hoạt, dùng khối `CREATURES` và bỏ khối `CHARACTERS`.
* Các trường gồm: *`id`*, *`role`* (loài vật và vai trò), *`build`* (tỷ lệ kích thước), *`material`* (chất liệu chế tác), *`action`* (hành động cụ thể), *`gaze`* (hướng nhìn).

#### Khối 4: `ENVIRONMENT` (Bắt buộc)
* **`camera`**: Góc máy linh hoạt (ngang tầm mắt, góc thấp, góc cao, cận cảnh macro tilt-shift).
* **`setting`**: Không gian sa bàn hoặc mặt gỗ đặt bối cảnh.
* **`focal_elements`**: Danh sách đồ vật chính (`prop_1`, `prop_2`...): gồm *`id`*, *`item`* (tên vật thể), *`material`* (gỗ, gốm, kim loại mờ, đá...), *`details`* (chi tiết gia công, mép bo tròn mộc mạc).
* **`staging`**: Vị trí sắp đặt các `figure_*`, `creature_*`, `prop_*` trong khung hình và khoảng trống trên mặt bàn.
* **`real_nature`**: Vật liệu tự nhiên thật ở cự ly tiếp xúc (rêu tươi, viên sỏi, cành cây khô, vỏ hạt, quả dại).
* **`backdrop`**: Hậu cảnh xa làm mờ nhẹ để tạo độ sâu trường ảnh tilt-shift.
* **`lighting`**: Hướng rọi sáng tự nhiên (ánh nắng cửa sổ, ánh lửa ấm), tạo bóng đổ mềm êm.
* **`motion` (Tùy chọn):** Chuyển động môi trường (vệt khói bốc, lá khô bay, gió lay nhẹ).

#### Khối 5: `SURREAL` (Bắt buộc 100% mọi prompt)
* **Bản chất:** Mọi cảnh bắt buộc phải có một chi tiết phi lý mộc mạc — đưa đồ vật hoặc hành động bình thường vào hoàn cảnh bất thường bằng vật liệu sa bàn thủ công. Nhân vật luôn giữ thái độ an nhiên, bình thản làm việc.
* **`type`**: 1 trong 4 dạng phi lý:
  - `displacement`: Thay thế bộ phận đồ vật bằng vật thể tự nhiên (bánh răng bằng quả thông/hạt dẻ, giọt nước bằng hạt cườm, mái chèo bằng cành cây).
  - `macro_interaction`: Tương tác với vật thể tự nhiên phóng đại hoặc siêu nhỏ (lá làm đèn bàn/thuyền bơi, vỏ hạt dẻ làm ghế, vỏ trứng làm bồn cây).
  - `absurd_setting`: Đặt sinh hoạt đời thường vào vị trí bất thường (tiệm bánh trong hốc rễ cây, đọc sách trên nhánh nấm, câu cá trong tách trà).
  - `scale_contrast`: Tương phản tỷ lệ giữa các đồ vật mộc mạc.
* **`description`**: Mô tả chi tiết tình huống phi lý bằng vật liệu thủ công (gỗ, nỉ, đất nung, gốm). Cấm hiệu ứng phát sáng neon hay CGI ma quái.
