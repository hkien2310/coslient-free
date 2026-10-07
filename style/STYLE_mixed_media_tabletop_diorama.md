# STYLE: Mixed-Media Tabletop Diorama
*Coslient Free · Plugin chất liệu thế giới búp bê nghệ thuật dân gian thu nhỏ trên sa bàn giữa thiên nhiên thật.*

Phong cách mô phỏng một sa bàn nghệ thuật thu nhỏ kết hợp giữa đồ chế tác thủ công mộc và thiên nhiên thật, ghi lại bằng ống kính macro tilt-shift. Toát lên vẻ mộc mạc, ấm áp và giàu cảm xúc xúc giác.

---

## 1. Thế Giới Hai Lớp (Two-Layer Materiality)
* **Lớp tạo tác (Chế tác thủ công):** Mọi thực thể nhân tạo (nhân vật, kiến trúc, vật dụng) bắt buộc chế tác từ vật liệu mộc thủ công. Cấm vật liệu công nghiệp, nhựa bóng hoặc kim loại sáng bóng hiện đại.
* **Lớp môi trường (Thiên nhiên thật thu nhỏ):** Toàn bộ không gian cảnh quan sử dụng chất liệu thiên nhiên thật ở tỷ lệ thu nhỏ và ánh sáng tự nhiên thật. Tuyệt đối không dùng phông nền nhân tạo, cỏ giả hay hoa nhựa.

---

## 2. Tạo Hình Nhân Vật (Character Craftsmanship)
* **Hình thể toàn vẹn & Điểm tựa vật lý:** Búp bê gỗ luôn là thực thể hoàn chỉnh toàn thân (full-body), có tư thế tiếp xúc vật lý vững vàng với mặt sàn hoặc bề mặt đồ vật. Tuyệt đối không tả bán thân (waist-up) nhằm tránh lỗi cắt cụt thân. Tự do tỷ lệ và tạng người theo từng nhân vật.
* **Trang phục che kín da thịt:** Nhân vật luôn mặc trang phục vải may thủ công và mang giày/ủng tiếp xúc bề mặt. Không để lộ các phần cơ thể trần trụi nhằm tránh lỗi AI vẽ chi tiết da thịt người thật.
* **Ngũ quan phẳng 2D tối giản:** Nét mặt là nét vẽ cọ 2D phẳng mộc mạc trên khối gỗ tiện nhẵn. Mắt có tròng và đồng tử phân định rõ (chống mắt nút gấu bông); miệng là một nét cọ mảnh hoặc rãnh khắc khép kín (chống mất miệng). Mặt mộc tự nhiên, cấm vẽ má hồng phấn son.
* **Triệt tiêu lão hóa sinh học:** Khối đầu gỗ luôn giữ bề mặt nhẵn bóng. Tuyệt đối không vẽ nếp nhăn da thịt, bọng mắt, rãnh cơ mặt hay nhe răng. Tuổi tác và đặc trưng nhân vật được định danh qua chất liệu tóc, trang phục, phụ kiện và dáng dấp.
* **Bàn tay thao tác:** Bàn tay gỗ khắc ngón có khớp, ưu tiên gắn liền với hành động thao tác vật lý cụ thể.

---

## 3. Biểu Cảm & Dáng Điệu (Expressions & Postures)
* **Biểu cảm qua tư thế & Dáng dấp (Pose over Face):** Trạng thái cảm xúc toát lên từ ngôn ngữ cơ thể, độ nghiêng của đầu và hành động dở dang; không dựa vào cử động cơ mặt sinh học.
* **Quy tắc hướng nhìn chủ đích (Intentional Gaze):** Hướng nhìn luôn có điểm tựa thị giác rõ ràng vào nhân vật đồng hành, đồ vật trên tay hoặc cảnh quan không gian; không hướng ánh nhìn vô hồn vào ống kính máy quay.

---

## 4. Không Gian & Điện Ảnh (Cinematography & Space)
* **Nguyên lý đường cong hữu cơ (Organic Curves):** Không gian, kiến trúc và đồ vật ưu tiên đường nét uốn lượn mềm mại, bất đối xứng tự nhiên. Hạn chế đường thẳng tắp và góc hộp vuông vức cơ khí.
* **Quang học sa bàn (Macro Tilt-Shift):** Sử dụng ống kính macro tilt-shift với độ sâu trường ảnh mỏng để tôn vinh tỷ lệ thế giới thu nhỏ và chất cảm bề mặt vật liệu.
* **Ánh sáng tự nhiên định hướng:** Nguồn sáng phải có phương hướng và góc rọi rõ rệt, tạo bóng đổ mềm mại nhằm khắc họa khối tích và xúc cảm không gian.

---

## 5. Quy Chuẩn Prompt Định Dạng JSON (Object-in-Object)
Mỗi prompt là một **JSON Object độc lập, tự thân hoàn chỉnh (Standalone Self-Contained)**. Gồm 4 khối chức năng:

### 5.1. Khung Cấu Trúc Cho Một Prompt Độc Lập

```json
{
  "id": "<Số thứ tự prompt>",
  "STYLE": {
    "world": "Handcrafted mixed-media tabletop diorama of a whimsical folk art miniature world",
    "handcrafted": "<Định danh chất liệu thủ công cụ thể của cảnh>",
    "real_nature": "<Định danh chất liệu thiên nhiên thật cụ thể của cảnh>",
    "aspect_ratio": "16:9"
  },
  "CHARACTERS": {
    "dna": "Stylized wooden folk art figurine, smooth turned wooden head, flat minimalist painted face with soft pupils and fine single-line mouth, zero skin wrinkles, no teeth, no blushed cheeks, articulated hands",
    "figure_1": {
      "role": "<Vai trò & lứa tuổi ước lệ của nhân vật>",
      "head": "<Hình khối đầu + chất liệu tóc + phụ kiện đầu nếu có + mặt phẳng 2D không nếp nhăn, không răng>",
      "attire": "<Trang phục vải thủ công phủ kín chân tới giày/ủng>",
      "action": "<Hành động dở dang cụ thể>",
      "gaze": "<Hướng nhìn chủ đích vào đối tượng cụ thể>"
    },
    "figure_2": {
      "role": "<Nhân vật thứ hai nếu có trong cảnh>",
      "head": "<Hình khối đầu + tóc + phụ kiện + mặt phẳng 2D>",
      "attire": "<Trang phục vải thủ công che kín da thịt>",
      "action": "<Hành động tương tác>",
      "gaze": "<Hướng nhìn đối ứng>"
    },
    "background_figures": "<Tùy chọn: Chấm bóng người tí hon ở hậu cảnh xa đo tỷ lệ không gian>"
  },
  "ENVIRONMENT": {
    "camera": "<Góc máy & Cỡ cảnh quang học macro>",
    "setting": "<Không gian kiến trúc hoặc địa điểm thu nhỏ>",
    "focal_elements": {
      "prop_1": {
        "item": "<Tên & loại vật thể chính>",
        "material": "<Chất liệu thủ công chế tác>",
        "details": "<Chi tiết tạo tác & bề mặt>"
      },
      "prop_2": {
        "item": "<Tùy chọn: Vật thể tương tác thứ hai>",
        "material": "<Chất liệu chế tác>",
        "details": "<Chi tiết tạo tác & bề mặt>"
      }
    },
    "staging": "<Dàn cảnh vị trí & quan hệ không gian: figure_1, figure_2 ở đâu so với prop_1, prop_2, tương quan với nhau và tiếp xúc bề mặt ra sao>",
    "backdrop": "<Không gian hậu cảnh xa tạo độ sâu trường ảnh>",
    "real_nature": "<Chất liệu tự nhiên thật thu nhỏ cụ thể của cảnh>",
    "lighting": "<Nguồn sáng tự nhiên có hướng rọi cụ thể>",
    "motion": "<Tùy chọn: Yếu tố động lực học môi trường>"
  },
  "SURREAL": {
    "quirk": "<Chi tiết kỳ ảo mộc mạc hoặc chơi đùa tỷ lệ>"
  }
}
```

---

### 5.2. Quy Tắc Chi Tiết Từng Trường (Field Rules)

#### Khối 1: `STYLE` (Định Hình Thế Giới & Tham Số)
* **`world`**: Khóa thể loại sa bàn thu nhỏ thủ công (`Handcrafted mixed-media tabletop diorama...`). Cố định ở mọi prompt để chặn ảnh chụp người thật đời thường.
* **`handcrafted`**: Tự do định danh các chất liệu làm tay cụ thể của cảnh (vải dệt, gỗ gọt, kim loại mờ...). Cấm nhựa bóng, kim loại công nghiệp.
* **`real_nature`**: Tự do định danh các chất liệu thiên nhiên thật cụ thể theo bối cảnh (rêu, đất, đá, nước, tuyết, cát, lá, ánh nắng...).
* **`aspect_ratio`**: Tỷ lệ khung hình kỹ thuật (luôn là `"16:9"`).

#### Khối 2: `CHARACTERS` (Quản Lý Nhân Diện Thực Thể)
* **`dna` (Bảo vệ giải phẫu chung):** Dòng định nghĩa bất biến khóa cứng búp bê gỗ toàn thân, mặt vẽ cọ phẳng 2D, mắt có đồng tử mềm (chặn bear eyes), miệng đường mảnh (chặn mất miệng), nhẵn thín không nếp nhăn da thịt, không răng, không má hồng, tay có ngón.
* **Quy tắc giải phẫu bắt buộc (Không bao giờ bỏ sót người):** Khi có người xuất hiện, **dù máy quay chụp cận cảnh (macro close-up) chỉ lấy thao tác đôi bàn tay, BẮT BUỘC phải miêu tả trọn vẹn toàn bộ nhân vật (`figure_1`) từ đầu, tóc, trang phục, đến hướng nhìn**. Việc này giúp AI neo giữ giải phẫu búp bê gỗ nguyên khối thống nhất, triệt tiêu hoàn toàn lỗi tạo ra các bàn tay người thật trôi nổi ma quái (disembodied hands).
* **`figure_1`, `figure_2` (Thuộc tính tự thân của nhân vật):**
  - *`role`*: Vai trò & lứa tuổi ước lệ của nhân vật.
  - *`head`*: Hình khối đầu gỗ gọt nhẵn + chất liệu tóc len/sợi dệt + phụ kiện đầu nếu có + nét mặt phẳng 2D tối giản (mắt có đồng tử mềm, nét miệng một đường mảnh duy nhất, zero nếp nhăn da, không răng).
  - *`attire`*: Trang phục vải thủ công phủ kín chân tới giày/ủng tiếp xúc bề mặt.
  - *`action`*: Hành động dở dang của nhân vật (đặc tả thao tác tay nếu là cảnh cận).
  - *`gaze`*: Hướng nhìn chủ đích vào đối tượng cụ thể trong bối cảnh, không nhìn chằm chằm vào máy quay.
* **`background_figures` (Tùy chọn):** Chấm bóng người tí hon ở hậu cảnh xa để đo tỷ lệ, không tả mặt mũi hay quần áo chi tiết.
* *Biến thể sinh vật / thú cưng:* Chỉ khi cảnh hoàn toàn không có người, mới thay thế `figure_*` bằng `creature: { "type": "<loài thú làm tay>", "posture": "<tư thế ngủ/đứng>" }`.

#### Khối 3: `ENVIRONMENT` (Sân Khấu, Dàn Cảnh & Bối Cảnh)
* **`camera`**: Định vị góc quay và cỡ cảnh quang học macro (`macro close-up shot` / `eye-level full-body shot` / `medium shot from behind` / `panoramic wide shot`).
* **`setting`**: Không gian kiến trúc hoặc địa điểm thu nhỏ.
* **`focal_elements` (Vật thể tiền cảnh tương tác chi tiết - tương tự figure_1, 2):** Được định danh và mô tả chi tiết từng vật thể (`prop_1`, `prop_2` nếu có) để AI đắp đủ texture và chất cảm thủ công:
  - *`item`*: Tên và định danh vật thể.
  - *`material`*: Chất liệu chế tác thủ công cụ thể.
  - *`details`*: Chi tiết gia công, thớ vân, độ mòn thời gian, bu-lông đinh tán, độ bóng mờ.
* **`staging` (Dàn cảnh không gian & Quan hệ vị trí):** Nơi điều phối mối quan hệ không gian chính xác giữa `figure_1`, `figure_2` với `prop_1`, `prop_2` và mặt đất/bề mặt:
  - Ai đứng/ngồi ở đâu trên hoặc cạnh `prop_1`?
  - Ai đang cầm/thao tác trên `prop_2`?
  - Tư thế bàn chân tiếp xúc bề mặt ra sao?
* **`backdrop` (Hậu cảnh xa):** Không gian nền phía sau tạo chiều sâu trường ảnh.
* **`real_nature`**: Chất liệu tự nhiên thật thu nhỏ cụ thể của cảnh này.
* **`lighting`**: Nguồn sáng tự nhiên có hướng rọi cụ thể.
* **`motion` (Tùy chọn):** Yếu tố động lực học môi trường.

#### Khối 4: `SURREAL` (Sai Lệch Thị Giác & Yếu Tố Kỳ Ảo Mộc Mạc)
* **`quirk`**: Một chi tiết kỳ ảo mộc mạc hoặc chơi đùa tỷ lệ duyên dáng.
