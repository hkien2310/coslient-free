# STYLE: Mixed-Media Tabletop Diorama

Sa bàn thu nhỏ kết hợp đồ thủ công và thiên nhiên thật, chụp cận cảnh bằng ống kính macro tilt-shift.

---

## 1. Hai Lớp Chất Liệu

* **Đồ thủ công:** Nhân vật, kiến trúc và đồ đạc làm từ gỗ mộc, vải dệt, nỉ ép, đất nung. Bề mặt nhám mờ, lộ rõ vân gỗ, vết đẽo gọt và thớ vải.
* **Thiên nhiên thật:** Rêu tươi, cành cây khô, sỏi cuội, đất cát, quả dại thu nhỏ. Ánh sáng tự nhiên có hướng rọi rõ, bóng đổ êm.

---

## 2. Tạo Hình Nhân Vật (Folk Art Wooden Doll)

* **Tỉ lệ người lớn dong dỏng cao (Chống Chibi):** Tỉ lệ cơ thể người trưởng thành cao ráo (`tall slender adult human proportions`), đầu nhỏ cân đối đúng tỉ lệ với thân người, chân tay dài (`small proportionate head, long slender limbs`). Thân tượng đẽo liền khối không khớp nối, tay áo dài che kín cổ tay.
* **Tóc & Râu dạng sợi thẳng suôn mượt (Chống xù bông):** Tóc và râu làm từ các sợi chỉ lanh hoặc chỉ thêu chải thẳng buông suôn (`straight combed linen thread strands falling flat and neat`), ôm sát đầu và cằm tự nhiên. Phủ kín toàn bộ đầu (không hói), không dùng sợi bông xù phồng như cục bông gòn.
* **Khuôn mặt trau chuốt:** Đầu gỗ đẽo gọt sạch sẽ, bề mặt nhẵn mịn mờ lì (`clean, smoothly finished matte wooden face`), không vết dao băm vằm trên mặt. Mũi nhỏ nhắn xinh xắn tạc êm ái trên mặt gỗ.
* **Đôi mắt có hồn:** Mắt to tròn mở sáng, vẽ cọ tỉ mỉ bên trong rãnh khắc nông, toát lên vẻ ngây thơ, hiền hòa, ấm áp kiểu hoạt hình cổ điển.
* **Bàn tay:** Bàn tay gỗ chạm khắc thanh thoát, các ngón tay cong nhẹ nhàng, tự nhiên cầm nắm đồ vật.
* **Trang phục:** Vải dệt thủ công thật (lanh, len dạ) may đo vừa vặn bọc ngoài thân tượng, viền chỉ thêu to bản mộc mạc. Tay áo dài che kín cổ tay, vạt áo phủ dài tới ủng.
* **Độ tuổi:** Người trẻ mặt nhẵn mịn, tươi tắn. Người già có vài nét cười nhẹ ở khóe mắt, toát lên vẻ phúc hậu hiền từ.

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
    "dna": "Tall slender wooden folk doll with small proportionate head and long limbs in tailored cloth clothing. Solid seamless wood body with long sleeves covering wrists. Clean smoothly carved wooden head, gentle open eyes, small petite nose, straight combed thread hair and beard falling flat and neat. Carved wooden hands with distinct curved fingers.",
    "figures": [
      {
        "id": "figure_1",
        "role": "<role_and_age>",
        "build": "<posture_and_build>",
        "head": "<head_hair_eyes_expression>",
        "attire": "<clothing_and_fabrics>",
        "action": "<hands_and_activity>",
        "gaze": "<look_direction>"
      },
      {
        "id": "figure_2",
        "role": "<optional_second_figure_role>",
        "build": "<posture_and_build>",
        "head": "<head_hair_eyes_expression>",
        "attire": "<clothing_and_fabrics>",
        "action": "<hands_and_activity>",
        "gaze": "<look_direction>"
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
* **`dna`**: Câu định nghĩa gốc cho nhân vật: tượng búp bê gỗ dáng cao ráo thanh mảnh, đầu nhỏ đúng tỉ lệ, chân tay dài, mặc đồ vải may đo; thân gỗ liền khối không khớp nối, ống tay dài che kín cổ tay; đầu gỗ đẽo gọt sạch sẽ nhẵn mịn mờ lì, nét mặt mộc mạc biểu cảm duyên dáng, mũi nhỏ xinh, mắt mở to tròn hiền hòa, mái tóc và râu bằng sợi chỉ thẳng buông suôn ôm sát đầu và cằm (chải mượt, không xù bông), bàn tay gỗ chạm ngón cong tự nhiên.
* **`figures`**: Danh sách nhân vật trong cảnh:
  - *`id`*: Mã định danh (`figure_1`, `figure_2`...) để `staging` gọi tên.
  - *`role`*: Vai trò và lứa tuổi cụ thể của nhân vật.
  - *`build`*: Dáng người dong dỏng cao ráo, đầu nhỏ cân đối, tư thế tự nhiên (đầu hơi nghiêng, vai thả lỏng, người hơi chùng nhẹ theo hành động).
  - *`head`*: Đầu gỗ nhẵn mịn trau chuốt, nét mặt cách điệu hiền từ, tóc và râu sợi chỉ chải thẳng buông suôn phủ kín đầu (không hói, không xù bông), mũi nhỏ xinh, mắt mở to tròn hiền từ (người già thêm vài nét cười nhẹ ở khóe mắt).
  - *`attire`*: Trang phục vải dệt thật có viền thêu, ống tay dài che kín cổ tay, vạt áo phủ dài tới ủng.
  - *`action`*: Hành động cụ thể, miêu tả bàn tay gỗ chạm rõ ngón đang uốn cong cầm nắm đồ vật.
  - *`gaze`*: Hướng nhìn có chủ đích của đôi mắt mở, nhìn vào việc đang làm hoặc bạn đồng hành, không nhìn vào ống kính máy quay.
* **Quy tắc trọn vẹn hình thể:** Dù máy quay cận cảnh thao tác tay, vẫn mô tả đầy đủ từ đầu, tóc, áo quần đến dáng điệu để AI giữ giải phẫu thống nhất, tránh lỗi bàn tay trôi nổi một mình.
* **Tham chiếu thực thể:** Mọi đối tượng tương tác trong `action`, `gaze`, `staging` phải có ID rõ ràng (`figure_*`, `creature_*`, `prop_*`).
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
