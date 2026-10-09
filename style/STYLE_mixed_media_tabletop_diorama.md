# STYLE: Mixed-Media Tabletop Diorama

Sa bàn thu nhỏ kết hợp đồ thủ công và thiên nhiên thật, chụp cận cảnh bằng ống kính macro tilt-shift.

---

## 1. Hai Lớp Chất Liệu

* **Đồ thủ công:** Nhân vật, nhà cửa, đồ đạc làm từ gỗ mộc, vải dệt, nỉ ép, đất nung. Bề mặt nhám mờ, lộ rõ vân gỗ, vết đẽo gọt và thớ vải.
* **Thiên nhiên thật:** Rêu tươi, cành cây khô, sỏi cuội, đất cát, quả dại thu nhỏ. Ánh sáng tự nhiên có hướng rọi rõ, bóng đổ êm.

---

## 2. Tạo Hình Nhân Vật

* **Chất liệu:** Tượng búp bê gỗ chạm tay. Đầu, cổ và bàn tay là gỗ mộc để mờ lì.
* **Tỉ lệ & Dáng vẻ:** Tỉ lệ người trưởng thành cao ráo, cân đối. Tư thế đứng hoặc ngồi tự nhiên theo việc đang làm, đầu hơi nghiêng nhẹ.
* **Trang phục:** Vải dệt thật (lanh thô, len, nỉ ép) may đo bọc ngoài thân tượng, viền chỉ thêu to bản. Tay áo dài che kín cổ tay, vạt áo phủ dài tới ủng.
* **Khuôn mặt:** Đầu gỗ đẽo tròn mịn màng. Sống mũi nhỏ tạc chìm êm ái trên mặt gỗ. Tóc len sợi dày dặn phủ kín đầu.
* **Đôi mắt:** Mắt khắc rãnh nông hình hạnh nhân, bên trong vẽ tròng mắt màu than mở to hiền lành, nhìn rõ việc đang làm.
* **Nếp nhăn:** Người trẻ mặt nhẵn mộc mạc. Người già có vài rãnh khắc cười nông ở khóe mắt, toát lên vẻ phúc hậu.
* **Bàn tay:** Bàn tay gỗ chạm khắc rõ từng ngón cong tự nhiên theo động tác cầm nắm.

---

## 3. Không Gian & Màu Sắc

* **Đường nét:** Mọi góc bàn ghế, đồ đạc đều bo tròn mép mộc mạc, tránh các góc nhọn sắc.
* **Bảng màu chủ đạo:** Nền trầm màu xám than / đá phiến (`charcoal / slate`), điểm xuyết sắc vàng mù tạt / hổ phách (`saffron-mustard / warm amber`), phối cùng màu gỗ sáng và xanh rêu.
* **Góc máy:** Chụp ngang tầm mắt nhân vật, độ sâu trường ảnh mỏng (tilt-shift) làm mờ nhẹ hậu cảnh để nổi bật chi tiết sa bàn.

---

## 4. Cấu Trúc Prompt JSON

Mỗi prompt là một JSON Object độc lập. Toàn bộ giá trị mô tả bằng tiếng Anh tự nhiên.

```json
{
  "id": "<id_prompt>",
  "STYLE": {
    "world": "Handcrafted mixed-media diorama, raw carved wood and genuine tailored linen fabric",
    "palette": "Charcoal and slate with glowing saffron-mustard and warm amber accents, blond wood",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Hand-carved wooden folk doll in miniature tailored linen clothing. Smooth carved wooden head, small natural nose, warm open eyes carved and painted with dark pupils, thick yarn hair. Carved wooden hands with distinct curved fingers.",
    "figures": [
      {
        "id": "figure_1",
        "role": "<Vai trò và độ tuổi>",
        "build": "<Dáng người cao ráo, tư thế tự nhiên hơi nghiêng nhẹ>",
        "head": "<Đầu gỗ đẽo tròn, tóc len dày phủ kín đầu, mũi nhỏ tạc êm, mắt mở hiền lành>",
        "attire": "<Trang phục vải lanh/dạ viền chỉ thêu, tay áo dài che kín cổ tay>",
        "action": "<Hành động cụ thể, bàn tay ngón cong cầm nắm tự nhiên>",
        "gaze": "<Mắt mở nhìn chăm chú vào đồ vật hoặc người đối diện>"
      }
    ]
  },
  "ENVIRONMENT": {
    "camera": "Eye-level macro tilt-shift lens with soft shallow depth of field",
    "setting": "<Không gian bàn gỗ hoặc góc thiên nhiên thu nhỏ>",
    "focal_elements": [
      {
        "id": "prop_1",
        "item": "<Đồ vật chính>",
        "material": "<Chất liệu thủ công: gỗ, gốm mờ, đồng cũ>",
        "details": "<Mép bo tròn, bề mặt nhám mộc>"
      }
    ],
    "staging": "<Sắp xếp vị trí nhân vật và đồ vật trên mặt bàn>",
    "real_nature": "<Vật liệu tự nhiên thật ở cạnh nhân vật: rêu tươi, mẩu gỗ, viên sỏi>",
    "backdrop": "<Hậu cảnh xa làm mờ nhẹ>",
    "lighting": "Natural directional window light creating soft warm shadows"
  },
  "SURREAL": {
    "type": "<absurd_setting | displacement | macro_interaction>",
    "description": "<Tùy chọn: Tình huống phi lý mộc mạc như đọc sách dưới tai nấm, chèo thuyền vỏ hạt dẻ>"
  }
}
```
