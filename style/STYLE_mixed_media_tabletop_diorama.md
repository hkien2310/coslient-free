# STYLE: Mixed-Media Tabletop Diorama
*Quy chuẩn tượng gỗ thu nhỏ điêu khắc mộc trên sa bàn giữa thiên nhiên.*

Phong cách sa bàn thu nhỏ kết hợp đồ thủ công và thiên nhiên thật, ghi hình bằng ống kính macro tilt-shift.

---

## 1. Thế Giới Hai Lớp (Two-Layer Materiality)
* **Lớp tạo tác:** Nhân vật, kiến trúc và đồ vật chế tác từ vật liệu thủ công. Bề mặt nhám mờ (matte), có vết đẽo gọt, vân gỗ và xơ vải thô. Không dùng hiệu ứng 3D CGI, nhựa bóng hoặc kim loại đúc công nghiệp.
* **Lớp môi trường:** Cảnh quan dùng chất liệu thiên nhiên thu nhỏ và ánh sáng tự nhiên. Không dùng phông nền nhân tạo, cỏ giả hay hoa nhựa.

---

## 2. Tạo Hình Nhân Vật (Character Craftsmanship)
* **Hình thể liền khối:** Nhân vật là tượng gỗ thu nhỏ điêu khắc nguyên khối toàn thân (full-body), thân tượng liền mạch không có khớp nối cơ khí hay khớp bi (`no mechanical joints, no ball-joints, no visible seams`). Chân chạm sàn hoặc ngồi vững trên bề mặt. Không tả bán thân (waist-up) để tránh lỗi cụt người. Tỷ lệ và vóc dáng tùy theo nhân vật.
* **Trang phục:** Mặc đồ vải thủ công phủ kín da thịt, đi giày hoặc ủng. Không để lộ cơ thể để tránh AI vẽ chi tiết da thịt người thật.
* **Ngũ quan phẳng 2D:** Nét mặt vẽ cọ 2D phẳng trên khối gỗ tiện nhẵn. Mắt vẽ có đồng tử (tránh mắt nút đen như gấu bông). Miệng là một nét kẻ mảnh hoặc rãnh khắc khép kín (tránh mất miệng hoặc há răng). Mặt mộc, không vẽ má hồng.
* **Bề mặt đầu gỗ:** Đầu tượng luôn là gỗ nhẵn bóng. Không vẽ nếp nhăn da thịt, bọng mắt, rãnh cơ hay răng. Tuổi tác thể hiện qua màu tóc len, mũ nón, phụ kiện và dáng người.
* **Bàn tay:** Bàn tay gỗ điêu khắc liền khối thon thả với các ngón tay, thò ra từ cổ tay áo (`sculpted wooden hands carved with delicate fingers, emerging seamlessly from sleeves`), không có chốt khớp cơ khí.

---

## 3. Biểu Cảm & Dáng Điệu (Expressions & Postures)
* **Biểu cảm qua dáng dấp (Pose over Face):** Cảm xúc thể hiện qua tư thế, độ nghiêng đầu và hành động; không dựa vào cử động cơ mặt.
* **Hướng nhìn (Intentional Gaze):** Mắt nhìn vào bạn đồng hành, đồ vật trên tay hoặc cảnh quan; không nhìn thẳng vào máy quay.

---

## 4. Không Gian & Bảng Màu (Cinematography & Space)
* **Đường nét & Góc bo (Organic Curves):** Ưu tiên đường cong tự nhiên và góc bo tròn, vát mép mịn (`smoothly rounded, chamfered edges`). Cấm góc nhọn sắc, gai nhọn (`no sharp jagged angles, no pointy spikes`), hạn chế góc hộp vuông cơ khí.
* **Bố cục (Framing & Negative Space):** Bố cục cân bằng, có khoảng trống theo hướng nhìn nhân vật. Dùng bố cục chính giữa hoặc một phần ba, không nhồi nhét chi tiết.
* **Quang học (Macro Tilt-Shift):** Dùng ống kính macro tilt-shift với độ sâu trường ảnh mỏng để làm nổi bật tỷ lệ thu nhỏ và chất liệu bề mặt.
* **Ánh sáng:** Nguồn sáng tự nhiên có hướng rọi rõ, tạo bóng đổ mềm.
* **Bảng màu nhận diện (Signature Palette):** Khung hình sáng rõ, không bết đen hay ám đục. Bảng màu gồm Xám than/Xám đá (`Charcoal / Slate`) làm nền trầm và Vàng mù tạt/Hổ phách (`Saffron-Mustard / Warm Amber`) làm điểm nhấn, phối cùng màu trắng ngà yến mạch (`oatmeal`), gỗ sáng (`blond wood`) và xanh rêu (`deep moss green`).

---

## 5. Cấu Trúc Prompt JSON

Mỗi prompt là một JSON Object độc lập. Toàn bộ giá trị (values) viết bằng tiếng Anh.

### Quy Tắc Điều Kiện Khối
* **Bắt buộc:** `STYLE` và `ENVIRONMENT` luôn có ở mọi prompt.
* **Có điều kiện:**
  * **`CHARACTERS`**: Chỉ xuất hiện khi cảnh có con người. Đã có người thì mô tả đầy đủ theo schema (`dna`, `figures` hoặc `background_figures`). Cảnh không có người thì lược bỏ khối này.
  * **`CREATURES`**: Chỉ xuất hiện khi cảnh có động vật. Đã có thì mô tả đầy đủ (`role`, `build`, `material`, `action`, `gaze`). Cảnh không có động vật thì lược bỏ.
  * **`motion`**: Chỉ xuất hiện khi có chuyển động môi trường (lá bay, khói bốc, gió lay...).
  * **`SURREAL`**: Chỉ xuất hiện ở cảnh phi lý (~20%–30% tổng số cảnh). Định nghĩa: biến một thứ bình thường thành bất thường bằng vật liệu sa bàn thủ công. Gồm `type` (1 trong 4 dạng) và `description`.

### 5.1. Khung Cấu Trúc Prompt

```json
{
  "id": "<id_prompt>",
  "STYLE": {
    "world": "Handcrafted mixed-media tabletop diorama of a whimsical folk art miniature world",
    "palette": "Luminous and clear, charcoal and dark slate with glowing saffron-mustard and warm amber accents, natural blond wood",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Hand-carved stylized wooden figurine, seamless sculpted body without mechanical joints or visible seams, smooth turned wooden head, flat minimalist painted face with soft pupils and fine single-line mouth, zero skin wrinkles, no teeth, no blushed cheeks, sculpted wooden hands carved with delicate fingers emerging seamlessly from sleeve cuffs",
    "figures": [
      {
        "id": "figure_1",
        "role": "<Vai trò & lứa tuổi của nhân vật>",
        "build": "<Vóc dáng & tỷ lệ hình thể tương quan>",
        "head": "<Hình khối đầu + chất liệu tóc + phụ kiện đầu nếu có + mặt phẳng 2D không nếp nhăn, không răng>",
        "attire": "<Trang phục vải thủ công phủ kín chân tới giày/ủng>",
        "action": "<Hành động cụ thể>",
        "gaze": "<Hướng nhìn có chủ đích>"
      },
      {
        "id": "figure_2",
        "role": "<Tùy chọn: Vai trò nhân vật thứ hai>",
        "build": "<Vóc dáng & tỷ lệ hình thể tương quan>",
        "head": "<Hình khối đầu + tóc + phụ kiện + mặt phẳng 2D>",
        "attire": "<Trang phục vải thủ công che kín da thịt>",
        "action": "<Hành động tương tác>",
        "gaze": "<Hướng nhìn đối ứng>"
      }
    ],
    "background_figures": "<Tùy chọn: Chấm bóng người hoặc đàn thú tí hon ở hậu cảnh xa đo tỷ lệ>"
  },
  "CREATURES": [
    {
      "id": "creature_1",
      "role": "<Tùy chọn: Loài thú & vai trò>",
      "build": "<Tỷ lệ hình thể tương quan>",
      "material": "<Chất liệu thủ công chế tác riêng>",
      "action": "<Hành động cụ thể>",
      "gaze": "<Hướng nhìn có chủ đích>"
    }
  ],
  "ENVIRONMENT": {
    "camera": "<Góc máy & cỡ cảnh quang học macro>",
    "setting": "<Không gian kiến trúc hoặc địa điểm thu nhỏ>",
    "focal_elements": [
      {
        "id": "prop_1",
        "item": "<Tên & loại vật thể chính>",
        "material": "<Chất liệu chế tác>",
        "details": "<Chi tiết bề mặt và độ mòn>"
      },
      {
        "id": "prop_2",
        "item": "<Tùy chọn: Vật thể thứ hai>",
        "material": "<Chất liệu chế tác>",
        "details": "<Chi tiết bề mặt>"
      }
    ],
    "staging": "<Dàn cảnh: vị trí figure_*, creature_*, prop_* trong khung hình và khoảng trống thị giác tiếp xúc bề mặt>",
    "real_nature": "<Chất liệu tự nhiên thật thu nhỏ ở cự ly tiếp xúc>",
    "backdrop": "<Cảnh quan xa ngoài vùng lấy nét>",
    "lighting": "<Nguồn sáng tự nhiên có hướng rọi cụ thể>",
    "motion": "<Tùy chọn: Chuyển động môi trường>"
  },
  "SURREAL": {
    "type": "<1 trong 4 dạng: displacement | macro_interaction | absurd_setting | scale_contrast>",
    "description": "<Mô tả chi tiết tình huống phi lý bằng vật liệu sa bàn thủ công, nhân vật an nhiên>"
  }
}
```

---

### 5.2. Quy Tắc Từng Trường

#### Khối 1: `STYLE` (Bắt buộc)
* **`world`**: Khóa thể loại sa bàn thu nhỏ thủ công (`Handcrafted mixed-media tabletop diorama of a whimsical folk art miniature world`). Giữ nguyên ở mọi prompt để tránh ảnh chụp người thật hoặc 3D.
* **`palette`**: Khóa bảng màu nhận diện (`Luminous and clear, charcoal and dark slate with glowing saffron-mustard and warm amber accents, natural blond wood`). Giữ đồng nhất toàn dự án.
* **`aspect_ratio`**: Tỷ lệ khung hình (luôn là `"16:9"`).

#### Khối 2: `CHARACTERS` (Có khi có người)
* **`dna`**: Định nghĩa gốc cho nhân vật: tượng gỗ điêu khắc mộc thu nhỏ, thân tượng liền khối không khớp nối cơ khí (`no mechanical joints, no ball-joints, no visible seams`), mặt vẽ cọ phẳng 2D trên gỗ tiện nhẵn, mắt có đồng tử, miệng đường kẻ mảnh, nhẵn thín không nếp nhăn, không răng, không má hồng, bàn tay gỗ điêu khắc liền khối thon ngón thò ra từ cổ tay áo.
* **`figures`**: Danh sách nhân vật trong cảnh:
  - *`id`*: Mã định danh (`figure_1`, `figure_2`...) để `staging` gọi tên.
  - *`role`*: Vai trò và lứa tuổi của nhân vật.
  - *`build`*: Vóc dáng và tỷ lệ tương quan giữa các nhân vật (giúp AI phân biệt chiều cao và thể trạng).
  - *`head`*: Hình khối đầu gỗ gọt nhẵn + chất liệu tóc len/sợi + phụ kiện + mặt vẽ 2D phẳng không nếp nhăn, không răng.
  - *`attire`*: Trang phục vải thủ công phủ kín chân tới giày/ủng.
  - *`action`*: Hành động của nhân vật (đặc tả thao tác tay nếu là cảnh cận).
  - *`gaze`*: Hướng nhìn có chủ đích, không nhìn vào máy quay.
* **Quy tắc giải phẫu:** Khi có người xuất hiện, dù máy quay cận cảnh thao tác tay, vẫn phải mô tả trọn vẹn nhân vật từ đầu, tóc, trang phục đến hướng nhìn để tránh lỗi bàn tay trôi nổi (disembodied hands).
* **Tham chiếu thực thể:** Mọi đối tượng tương tác trong `action`, `gaze`, `staging` phải có ID (`figure_*`, `creature_*`, `prop_*`), không dùng danh từ chung không rõ nguồn gốc.
* **`background_figures` (Tùy chọn):** Chấm bóng người tí hon ở hậu cảnh xa để đo tỷ lệ, không tả chi tiết mặt hay trang phục.

#### Khối 3: `CREATURES` (Có khi có động vật)
* **Chất liệu:** Động vật có chất liệu chế tác thủ công riêng (nỉ ép, len thô, đất nung), tách bạch với `CHARACTERS.dna` để tránh AI ghép chi tiết người vào con vật.
* **Cảnh ngụ ngôn:** Khi cảnh chỉ có động vật sinh hoạt, dùng khối `CREATURES` và bỏ khối `CHARACTERS`.
* Các trường:
  - *`id`*: Mã định danh (`creature_1`, `creature_2`...) để `staging` gọi tên.
  - *`role`*: Loài vật và vai trò trong cảnh.
  - *`build`*: Vóc dáng và tỷ lệ tương quan.
  - *`material`*: Chất liệu chế tác cụ thể.
  - *`action`*: Hành động cụ thể.
  - *`gaze`*: Hướng nhìn có chủ đích.

#### Khối 4: `ENVIRONMENT` (Bắt buộc)
* **`camera`**: Góc máy và cỡ cảnh macro phù hợp với bối cảnh.
* **`setting`**: Địa điểm hoặc không gian kiến trúc thu nhỏ.
* **`focal_elements`**: Danh sách đạo cụ chính (`prop_1`, `prop_2`...):
  - *`id`*: Mã định danh để `staging` gọi tên.
  - *`item`*: Tên và định danh vật thể.
  - *`material`*: Chất liệu chế tác cụ thể.
  - *`details`*: Chi tiết gia công, vân bề mặt, độ mòn.
* **`staging`**: Vị trí của `figure_*`, `creature_*`, `prop_*` trong khung hình và khoảng trống tiếp xúc bề mặt.
* **`real_nature`**: Chất liệu tự nhiên thu nhỏ ở cự ly tiếp xúc (rêu, đá, gỗ, đất).
* **`backdrop`**: Cảnh quan xa ngoài vùng lấy nét tạo độ sâu trường ảnh tilt-shift.
* **`lighting`**: Nguồn sáng tự nhiên có hướng rọi cụ thể, tạo bóng đổ mềm.
* **`motion` (Tùy chọn):** Chuyển động môi trường (lá bay, khói bốc, gió lay...).

#### Khối 5: `SURREAL` (Có ở cảnh phi lý — Chiếm ~20%–30% tổng số cảnh)
* **Bản chất:** Đưa một vật thể hoặc hành động bình thường vào hoàn cảnh bất thường bằng vật liệu sa bàn thủ công.
* **`type`**: 1 trong 4 dạng phi lý:
  - `displacement`: Thay thế bộ phận đồ vật bằng vật thể tự nhiên (bánh răng bằng hạt bồ công anh, giọt nước bằng hạt cườm).
  - `macro_interaction`: Tương tác với vật thể tự nhiên phóng đại hoặc siêu nhỏ (lá làm đèn bàn, vỏ hạt dẻ làm ghế).
  - `absurd_setting`: Đặt sinh hoạt đời thường vào vị trí bất thường (xưởng mộc trong hốc rễ cây, đọc sách trên nhánh nấm).
  - `scale_contrast`: Tương phản tỷ lệ giữa các vật thể mộc mạc.
* **`description`**: Tình huống phi lý bằng vật liệu thủ công (gỗ, nỉ, dây cước, đất nung, gốm, kim loại mờ); nhân vật giữ tâm thế an nhiên (`calm, unbothered acceptance`). Cấm hiệu ứng phát sáng neon hay CGI ma quái.
