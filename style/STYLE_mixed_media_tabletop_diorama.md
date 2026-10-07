# STYLE: Mixed-Media Tabletop Diorama
*Coslient Free · Plugin chất liệu thế giới búp bê nghệ thuật dân gian thu nhỏ trên sa bàn giữa thiên nhiên thật.*

Nhân vật thủ công đa chất liệu đặt giữa thiên nhiên thật thu nhỏ, chụp macro tilt-shift. Duyên dáng, mộc mạc ấm áp, dáng người cao ráo thanh thoát, đầu gỗ tròn nhẵn, gương mặt tối giản ngây ngô vẽ cọ phẳng. Kẻ thù duy nhất: da thịt người thật, giải phẫu gân guốc, số tuổi cụ thể, chắp vá rách rưới, hoặc đầu trồi lên từ mặt đất.

---

## 1. Style Anchor & Thứ Tự Thông Tin (Nguyên Tắc Trọng Số Giảm Dần)

Trong prompt diffusion, **thứ tự từ trái sang phải quyết định attention weight: cái gì quan trọng hơn bắt buộc phải ở phía trước, cái gì ít quan trọng hơn ở phía sau.**

### Bảng Phân Tầng Thứ Tự Ưu Tiên

| Thứ tự | Thành phần | Mức độ quan trọng | Vai trò kỹ thuật & Cơ chế | Cú pháp quy chuẩn |
|:---:|---|:---:|---|---|
| **1 (Vị trí 0)** | **Style Anchor (Prefix)** | **TỐI THƯỢNG** | Khóa không gian sa bàn ngay lập tức; chặn đứng thiên kiến sinh người thật / ảnh chụp thật. | `Handcrafted mixed-media tabletop diorama, macro tilt-shift, ` |
| **2** | **Cỡ cảnh & Tiêu điểm máy quay** | **CỰC CAO** | Định hình phối cảnh, trường nhìn và vật thể trọng tâm máy quay ngắm vào. | `[Cỡ cảnh + Góc máy] [focusing on / framing tiêu điểm], ` |
| **3** | **Chủ thể chính (Neo tức thì)** | **CỰC CAO** | Khóa vật liệu búp bê gỗ ngay lập tức sau tên nhân vật; cấm neo trễ `both as` ở cuối. | `[nhân vật] as a stylized folk art miniature figure with a smooth round wooden head...` |
| **4** | **Hành vi dở dang & Điểm neo vật lý** | **CAO** | Tạo sinh khí chuyển động; đảm bảo tay/chân và đồ treo có điểm tựa vững chắc. | `[tay chân từ áo] [đang làm dở] [trên vật có điểm neo/điểm tựa], ` |
| **5** | **Hậu cảnh & Phối cảnh xa** | **TRUNG BÌNH** | Tạo chiều sâu không gian, khóa nhân vật phụ ở xa thành tí hon (tránh tranh chấp tiền cảnh). | `in the far distant background, tiny miniature figures...` |
| **6** | **Động học, Màu nhấn & Ánh sáng** | **BỔ TRỢ** | Thêm sinh khí môi trường (lá bay, hơi nước) và nguồn sáng cụ thể (không u tối). | `swirling golden leaves, warm low golden-hour backlight` |
| **7 (Cuối cùng)** | **Tham số kỹ thuật** | **THAM SỐ** | Tham số render dòng lệnh, luôn đặt ở đuôi. | ` --ar 16:9` |

### Công thức chuẩn ráp theo đúng thứ tự ưu tiên:
```text
Handcrafted mixed-media tabletop diorama, macro tilt-shift, [1. Cỡ cảnh & Tiêu điểm], [2. Nhân vật 1 bọc ngay búp bê gỗ], [3. Nhân vật 2 bọc ngay búp bê gỗ], [4. Hành động dở dang & Điểm neo vật lý], [5. Hậu cảnh xa & Động học], [6. Màu nhấn & Ánh sáng] --ar 16:9
```

### 5 Quy Tắc Thép Chặn Đứng Biến Dạng Thực Tế:
1. **Khóa cứng Đầu gỗ & Mặt vẽ phẳng là bất khả phân:** Từ `miniature figure` đứng một mình sẽ sinh ra tượng sáp tả thực hoặc đầu người thật ghép tay gỗ. Mọi nhân vật bắt buộc phải chứa cụm nguyên tử dính liền: `smooth round light-toned wooden head crowned with [flax/mohair] hair under [cap/beret], sweet minimalist face with delicate brush-painted dark eyes, completely flat painted facial features`.
2. **Cấm tuyệt đối số tuổi (`Zero Age Number Rule`):** Cấm `30-year-old`, `28-year-old`, `68-year-old`. Số tuổi kích hoạt dữ liệu ảnh chân dung người thật có râu ria, nếp nhăn. Chỉ dùng danh từ phân loại: `a young man`, `a young woman`, `an elderly couple`, `a young child`.
3. **Cấm Close-up vào đầu/mặt trên sa bàn (Diorama Close-up Head Trap):** Máy quay macro zoom vào mặt/trán sẽ cắt phăng thân thể và cắm cái đầu búp bê trơ trọi xuống đất rêu. Mọi tương tác thân mật (vuốt tóc, nhìn nhau, bóc hạt dẻ) bắt buộc dùng **trung cảnh (`eye-level medium shot`)** hoặc **toàn cảnh (`full-body shot`)** nơi nhân vật ngồi trên ghế dài hoặc đứng trên mặt đất. `Close-up` CHỈ DÀNH RIÊNG CHO ĐỒ VẬT VÔ TRI.
4. **Quy tắc Một Tiêu Điểm Duy Nhất (Single Focus Law):** Cấm tả 4 người (2 cặp) cùng đu 2 xích đu hoặc làm hành động song song trong 1 frame gây vỡ tải token. Mỗi frame chỉ tập trung vào MỘT cặp nhân vật hoặc MỘT nhân vật chính làm tiêu điểm.
5. **Chống chắp vá trang phục (Anti-Patchwork):** Để từ `mixed-media` không biến áo quần thành giấy rách, bìa các-tông lởm chởm, trang phục luôn dùng: `single-piece pressed felt coat/dress hanging in soft clean folds`.

---

## 2. Hai lớp thế giới
- **Làm tay:** người, thú, nhà, xe, đồ vật. Xoay vòng gỗ sáng màu, giấy bồi, vải lanh, dạ, da mềm, dây đay, thiếc gỉ, đồng thau. Len chỉ dùng điểm xuyết một bộ phận (không phủ cả người); hai nhân vật cạnh nhau không dùng cùng bộ chất liệu.
- **Thật:** rêu, sỏi, cỏ khô, hoa dại, nước, trời, khói, núi xa. Hoàn toàn là tự nhiên thật thu nhỏ, không làm bằng len nỉ.

---

## 3. Khối nhân vật chuẩn (Cao ráo - Đầu gỗ nhẵn - Mặt vẽ phẳng)
Mỗi lỗi hay gặp có đúng một cụm neo. Ngoài cụm neo, không mô tả giải phẫu cơ thể. Tuyệt đối không đưa số tuổi vào.

```text
a [young/elderly] [man/woman/craftsman] as a stylized whimsical folk art miniature figure, tall slender silhouette, smooth [round/oval] light-toned wooden head crowned with a full thick head of [màu] [chất liệu] hair under a [mũ/nón/beret], sweet minimalist face with delicate brush-painted dark eyes and a faint subtle smile line, smooth featureless cheeks, completely flat painted facial features with zero wrinkles, loose-fitting single-piece [màu] pressed felt [món áo] hanging in soft clean folds, visible long slim legs in trousers and small boots
```

- **Tôn dáng cao (Khử lùn chibi):** Luôn dùng `tall slender silhouette, visible long slim legs` và áo nỉ dài ngang đùi (`mid-thigh`), kết hợp quần suông buông dài phủ ủng da (`trousers and small boots`) để lộ đôi chân dài thanh thoát.
- **Đầu & Chống trọc lốc:** Dùng `smooth [round/oval/softly rectangular] light-toned wooden head` gắn liền với `crowned with a full thick head of [màu] [sợi mộc] hair under a [mũ/nón/beret]`. **Luôn luôn khóa chặt tóc hoặc nón che kín đỉnh đầu**, không để đầu gỗ trơ trọi. Tuyệt đối **không dùng `carved`** (tránh bị đục vát mặt gồ ghề).
- **Mắt & Ngũ quan:** Luôn dùng `delicate brush-painted dark eyes and a faint subtle smile line, smooth featureless cheeks, completely flat painted facial features`. Tuyệt đối **không dùng `dot eyes`, `bead`, `button`** để tránh AI đính hạt cườm nhựa hay cúc áo lồi.
- **Người già:** Tuổi tác thể hiện qua **mái tóc/râu bạc** (`fluffy grey-white flax hair`, `curly white mohair beard`), kính mắt hoặc dáng đứng, **tuyệt đối không đục nếp nhăn vào mặt**. Cả người già lẫn trẻ nhỏ đều chung nguyên lý mặt tròn nhẵn + mắt cọ vẽ phẳng.
- **Đa dạng tạng người & biểu cảm (Ponytail):**
  - *Thợ thủ công:* `tall sturdy build, broad solid shoulders, smooth softly rectangular wooden head`.
  - *Cụ già uyên bác:* `tall lean elderly frame, smooth oval wooden head, tiny circular brass spectacles`.
  - *Thiếu nữ thanh mảnh:* `tall statuesque silhouette, smooth oval wooden head, painted crescent smiling eyes`.
  - *Trẻ nhỏ:* `tall nimble youthful build, smooth round wooden head, curious painted dark eyes`.
- **Áo & Tay:** Vải dạ nỉ ép trơn nguyên khối (`pressed felt`, `woven linen`, `soft leather`). Cảnh trung cảnh dùng `simple rounded mitten-shaped wooden hands` đang cầm/thao tác đồ vật.
- **Thú:** `a [chất] [loài]` (`twine-wrapped`, `felted wool`, `shaggy mohair`), đổi chất liệu giữa các con thú.

---

## 4. Ba nguyên tắc tạo hình cốt lõi
1. **Đường cong hữu cơ (Curved & Organic):** Không dùng đường thẳng hay góc hộp vuông khô cứng. Tường cong, mái võng, cầu đá uốn lượn, lan can uốn khúc (`curved timber`, `sweeping organic path`, `curvilinear facades`).
2. **Bất đối xứng (Asymmetry):** Tránh trang phục đối xứng cứng nhắc. Vạt đắp chéo, khăn vắt lệch một bên vai, hàng cúc lệch ngực, túi lệch một bên hông (`asymmetrical cut`, `off-center closure`, `draped over one shoulder`).
3. **Sai lệch thị giác (Whimsical Quirk):** Mỗi khung cảnh lồng 1 chi tiết kỳ ảo mộc mạc hoặc chơi đùa tỷ lệ duyên dáng: lò nướng dáng ấm trà khổng lồ, tháp đá cong lưỡi liềm, cụm mây bông nhỏ xíu là là mặt cỏ, guồng nước thìa đồng (`whimsical environmental quirk`).

---

## 5. Khung hình & Quy định cỡ cảnh (Kinetic & Framing)
- **Cấm Close-up vào đầu/mặt:** Cận cảnh (`close-up shot`) chỉ dành cho đồ vật vô tri hoặc động vật nhỏ (túi hạt dẻ bốc khói, xích đu, tách trà, con ốc sên).
- **Nhân vật luôn từ Trung cảnh tới Toàn cảnh:** Mọi tương tác nhân vật phải xuất phát từ `medium eye-level shot` (thấy rõ cả người ngồi trên ghế dài/đứng cạnh bàn) tới `full-body shot` và `wide shot`.
- **Hành động dở dang (Mid-action):** Luôn dùng động từ đang diễn ra nửa chừng (`kicking boots into the air`, `leaning forward to blow steam`, `mid-stride tossing an acorn`) thay vì đứng/ngồi tạo dáng tĩnh (`standing/sitting still`).
- **Yếu tố động học:** Mỗi khung hình ưu tiên có 1 chi tiết chuyển động nhẹ: hơi nước bốc lên (`wisps of steam`), gió lay tà áo (`breeze fluttering coat hem`), lá vàng chao lượn (`swirling autumn leaves`), sóng nước lăn tăn.
- Nền mờ hẳn khi nhấn nhân vật: `very shallow depth of field, soft bokeh`. Nền đọc được khi kể bối cảnh: `moderate depth of field`.
- Khi quay cảnh rộng không người: hạ máy sát đất (`ground-level`), luôn có một chi tiết hoặc nhân vật nhỏ làm thước tỷ lệ. Không dùng `high-angle` đơn độc cho cảnh toàn không người.

---

## 6. Màu sắc & Ánh sáng
- **Tâm điểm màu ấm:** Một mảng màu nhấn rực rỡ (vàng mù tạt `saffron mustard`, đất nung `terracotta`, đỏ gỉ, hổ phách ấm) nổi bật trên nền tông đất mộc.
- **Ánh sáng luân chuyển linh hoạt:** Không lạm dụng mãi một ánh hoàng hôn. Xoay vòng giữa `soft misty dawn light` · `clear airy daylight` · `warm low golden-hour backlight` · `blue dusk with warm glowing amber lamps`.

---

## 7. Từ điển Token chuyển dịch
| Token gây lỗi | Model hiểu thành | Thay bằng cụm chuẩn |
|---|---|---|
| `30-year-old`, `28-year-old`, `68-year-old` (số tuổi) | Người thật đời thường, nếp nhăn, râu ria sinh học | `a young man`, `a young woman`, `an elderly couple`, `a child` |
| `close-up on face/forehead/head` | Đầu tượng bị chặt cắm xuống đất, mất thân | Chuyển thành `medium eye-level shot` ngồi trên ghế dài hoặc đứng |
| `miniature figure` đứng một mình không tả đầu | Tượng sáp tả thực thu nhỏ, đầu người thật ghép tay gỗ | `folk art miniature figure with a smooth round wooden head and painted face` |
| `two swings side by side with 4 people` (nhồi nhét) | Vỡ tải token, trượt thành 4 người thật | Tách thành 1 cặp nhân vật duy nhất làm tiêu điểm |
| `bald`, quên tả tóc đỉnh đầu | Đầu trọc lốc như bóng đèn | `crowned with a full thick head of [chất] hair under a [mũ]` |
| `carved wooden head`, `chiseled`, `wood grain face` | Mặt đục đẽo gồ ghề, rãnh vát dao nhăn nheo | `smooth [round/oval] light-toned wooden head, smooth featureless cheeks` |
| `dot eyes`, `bead eyes`, `button eyes`, `plastic eyes` | Mắt hạt cườm nhựa lồi, cúc áo bóng loáng | `delicate brush-painted dark eyes, completely flat painted facial features` |
| `puppet`, `doll`, `joints`, `articulated` | Búp bê khớp cơ khí, con rối dây giật | `storybook miniature figure` hoặc `folk art figurine` |
| Tả chi tiết sống mũi, mí mắt, rãnh cười, nếp nhăn | Mặt người lớn giải phẫu tả thực, mặt già nua | `sweet minimalist face with delicate brush-painted dark eyes and a faint subtle smile line` |
| `wrinkles`, `aged skin`, `weathered face` | Mặt nứt nẻ xác ướp, rãnh sâu | Tả tuổi qua tóc bạc (`fluffy white mohair hair`) và dáng đi |
| `chubby`, `round`, `plump`, `short`, `stout`, `cute`, `chibi` | Người lùn một mẩu, chibi biến dạng | `tall slender silhouette, visible long slim legs` |
| `standing still`, `sitting still`, `posing` | Tượng ma-nơ-canh chết đơ | Đổi thành động từ dở dang (`kicking boots`, `leaning`, `mid-stride`) |
| `knit`, `wool`, `crochet` cho cả người | Cả người biến thành cục len | `pressed felt`, `woven linen`, len chỉ dùng 1 chi tiết nhỏ |
| `clean`, `seamless`, `polished`, `plastic`, `resin`, `glossy` | Đồ công nghiệp, đồ nhựa bóng | Tên chất liệu thủ công thật (`solid timber`, `felt`, `brass`) |
| `patchwork`, `patched`, `rags`, `mixed-media` tự do | Tranh cắt dán giấy vụn, bìa các-tông chắp vá rách rưới | `loose single-piece pressed felt coat/dress in soft clean folds` |
| `jointed`, `carved wooden hands`, `stiff` | Tay hình nộm cứng đơ | `simple rounded mitten-shaped hands`, `holding gently` |
| `two wooden hands`, `hands` đứng một mình | Bàn tay cụt/rời rạc đặt trên bàn | Gắn vào ống tay áo/nhân vật: `[nhân vật] in [áo] with sleeves, hands holding...` |
| `boots and dress hem swinging` (không người) | Quần áo tàng hình bay lơ lửng | Luôn có nhân vật ngồi/mặc: `an elderly woman seated, kicking boots...` |
| Nhân vật hậu cảnh thiếu neo (`elderly man watching`) | Trượt thành NGƯỜI THẬT hoặc mất chân | Luôn gắn neo: `a companion miniature figure standing upright beside... with visible legs` |
| `swing with chains` không tả điểm treo | Dây xích đứt đoạn lơ lửng giữa trời | Luôn gắn điểm treo: `suspended by brass chains from the curving branch of an ancient oak tree` |
| `dark wood face`, `burnt wood`, `dark clay` | Mặt gỗ mục đen cháy | `smooth round light-toned wooden head` |
| `cinematic lighting`, `dark shadows`, `noir` | Tương phản gắt, u tối | Chọn một nguồn sáng cụ thể ở Mục 5 |
| `maple leaves`, `pipe`, `knife` | Kích hoạt bộ lọc kiểm duyệt giả | `golden oak leaves`, `wooden flute`, `artisan chisel` |
