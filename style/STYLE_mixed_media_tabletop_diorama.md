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

### 10 Quy Tắc Thép Chặn Đứng Biến Dạng Sa Bàn:
1. **Luật Búp Bê Nguyên Khối — CẤM TUYỆT ĐỐI BÁN THÂN (Whole-Figurine Law):** CẤM 100% các từ `waist-up`, `visible upper body`, `upper torso`, `half-body`. Trên sa bàn đồ chơi, búp bê là vật thể 3D nguyên khối. Dùng các từ bán thân khiến AI đúc ra tượng cụt cắm xuống đất cỏ như củ khoai mọc mầm (Xem Case Image 3). Mọi cảnh có người BẮT BUỘC là `full-body shot` hoặc `framing the complete full-body miniature figures [standing / seated] with visible legs in tailored trousers and small boots`.
2. **Luật Mặc Quần Đầy Đủ — Chống "Ở Chuồng" (The Mandatory Trousers Law):** CẤM TUYỆT ĐỐI cụm `visible legs in boots` đơn độc (thiếu quần khiến AI vẽ chân gỗ mộc trần truồng không mặc quần, Xem Case Image 1). Bắt buộc: `visible long legs in [charcoal/brown/navy/olive] tailored wool trousers and small leather boots` (nam) hoặc `loose pressed felt dress falling to small leather boots` (nữ).
3. **Luật Che Khuất Không Gian — Chống "Cơ Thể Đứt Đoạn" (Spatial Occlusion Law):** Cấm đặt bệ đá dày, lan can kín chắn ngang hông nhân vật mà lại đòi vẽ chân khiến model vẽ chân lòi ra dưới đáy sàn lơ lửng (Xem Case Image 2). Khi ở trên cao (tháp, ban công, cầu đá), nhân vật phải đứng trên **sàn phẳng thoáng (open stone terrace / open wooden deck)** lùi máy quay ra để thấy trọn vẹn toàn thân từ đầu đến ủng đặt trên nền sàn.
4. **Khóa cứng Đầu gỗ, Tóc & Mũ là bất khả phân (Chống Đầu Trọc Lốc):** Khi prompt chỉ ghi `smooth oval wooden head` mà quên tả tóc/mũ, AI sẽ vẽ một quả cầu gỗ tiện nhẵn trọc lốc như bóng đèn bowling (Xem Case Image 2, 3, 4, 5). Mọi nhân vật bắt buộc phải chứa cụm dính liền: `smooth round light-toned wooden head crowned with styled [auburn / chestnut / flax / gray] needle-felted wool hair under a tailored [flat cap / beret / hood], charming hand-painted storybook face with soft warm dark eyes, delicate blushed cheeks`.
5. **Cấm Bàn Tay Cục Doraemon (Articulated Fingers vs Spherical Stubs):** Cụm `smooth rounded wooden hands` khiến model vẽ quả cầu tròn xoe không ngón như tay Doraemon (Xem Case Image 1, 3). Bắt buộc dùng: `delicate carved wooden hands with articulated slender fingers holding [vật]` hoặc `expressive miniature wooden hands with visible delicate fingers`.
6. **Mặt Truyện Tranh Có Hồn vs Mặt Alien Dị Hợm (Charming Storybook Face):** Cấm để cụm `completely flat painted facial features, crescent eyes` đứng đơn độc trên đầu gỗ vì dễ kích hoạt các nét mực đen rạch ngang quái đản như hình nộm voodoo. Luôn dùng: `charming hand-painted storybook face with soft warm dark painted eyes, delicate blushed rosy cheeks, and a subtle gentle smile`.
7. **Cấm tuyệt đối số tuổi (`Zero Age Number Rule`):** Cấm `30-year-old`, `28-year-old`, `68-year-old`. Số tuổi kích hoạt dữ liệu ảnh chân dung người thật có râu ria, nếp nhăn. Chỉ dùng danh từ phân loại: `a young man`, `a young woman`, `an elderly couple`, `a young child`.
8. **Cấm Close-up vào đầu/mặt trên sa bàn (Diorama Close-up Head Trap):** Máy quay macro zoom vào mặt/trán sẽ cắt phăng thân thể và cắm cái đầu búp bê trơ trọi xuống đất rêu. Mọi tương tác thân mật bắt buộc dùng **toàn cảnh (`full-body shot`)** nơi nhân vật ngồi trên ghế dài hoặc đứng trên mặt đất. `Close-up` CHỈ DÀNH RIÊNG CHO ĐỒ VẬT VÔ TRI.
9. **Quy tắc Một Tiêu Điểm Duy Nhất (Single Focus Law):** Cấm tả 4 người (2 cặp) cùng đu 2 xích đu hoặc làm hành động song song trong 1 frame gây vỡ tải token. Mỗi frame chỉ tập trung vào MỘT cặp nhân vật hoặc MỘT nhân vật chính làm tiêu điểm.
10. **Chống chắp vá trang phục (Anti-Patchwork):** Để từ `mixed-media` không biến áo quần thành giấy rách, bìa các-tông lởm chởm, trang phục luôn dùng: `single-piece pressed felt coat/dress hanging in soft clean folds`.

---

## 2. Hai lớp thế giới
- **Làm tay:** người, thú, nhà, xe, đồ vật. Xoay vòng gỗ sáng màu, giấy bồi, vải lanh, dạ, da mềm, dây đay, thiếc gỉ, đồng thau. Len chỉ dùng điểm xuyết một bộ phận (không phủ cả người); hai nhân vật cạnh nhau không dùng cùng bộ chất liệu.
- **Thật:** rêu, sỏi, cỏ khô, hoa dại, nước, trời, khói, núi xa. Hoàn toàn là tự nhiên thật thu nhỏ, không làm bằng len nỉ.

---

## 3. Khối nhân vật chuẩn (Cao ráo - Đầu gỗ nhẵn - Mặt vẽ phẳng)
Mỗi lỗi hay gặp có đúng một cụm neo. Ngoài cụm neo, không mô tả giải phẫu cơ thể. Tuyệt đối không đưa số tuổi vào.

```text
a [young/elderly] [man/woman/craftsman] as a stylized whimsical folk art miniature figure, tall slender silhouette, smooth [round/oval] light-toned wooden head crowned with styled [auburn/chestnut/gray/flaxen] needle-felted wool hair under a tailored [flat cap/beret/bonnet], charming hand-painted storybook face with soft warm dark painted eyes, delicate blushed rosy cheeks, and a subtle gentle smile, loose-fitting single-piece [màu] pressed felt [món áo] hanging in soft clean folds, delicate carved wooden hands with articulated slender fingers holding [vật], visible long slim legs in trousers and small leather boots
```

- **Tôn dáng cao & Chân tiếp đất (Grounded Whole Figurine):** Luôn dùng `tall slender silhouette, visible long slim legs` và áo nỉ dài ngang đùi (`mid-thigh`), kết hợp quần suông buông dài phủ ủng da (`trousers and small boots`) để lộ đôi chân dài thanh thoát, cắm rễ vững chắc trên mặt đất. Khi ngồi ghế, bắt buộc thấy chân chạm đất (`seated with visible legs in trousers and small boots resting on the ground`), cấm dùng `waist-up view`.
- **Đầu & Chống trọc lốc (BẮT BUỘC TÓC/MŨ):** Dùng `smooth [round/oval/softly rectangular] light-toned wooden head` BẮT BUỘC gắn liền với `crowned with styled [màu] needle-felted wool hair under a tailored [flat cap/beret/bonnet]`. **Luôn luôn khóa chặt tóc hoặc nón che kín đỉnh đầu**, tuyệt đối không để đầu gỗ trơ trọi. Tuyệt đối **không dùng `carved` cho mặt** (tránh bị đục vát mặt gồ ghề).
- **Mắt & Ngũ quan (Charming Storybook Face):** Luôn dùng `charming hand-painted storybook face with soft warm dark painted eyes, delicate blushed rosy cheeks, and a subtle gentle smile`. Cấm `dot eyes`, `bead`, `button`. Cấm để cụm `completely flat painted facial features, crescent eyes` đứng trơ trọi không có gò má ửng hồng / nụ cười ấm.
- **Bàn tay (CẤM TAY CỤC DORAEMON):** Bàn tay luôn là `delicate carved wooden hands with articulated slender fingers` thò ra từ tay áo dài (`hands emerging from tailored wool sleeves`). CẤM TUYỆT ĐỐI `smooth rounded wooden hands` hoặc `rounded mitten-shaped hands` (gây lỗi thành khối cầu tròn vo Doraemon).
- **Người già:** Tuổi tác thể hiện qua **mái tóc/râu bạc** (`styled fluffy gray needle-felted wool hair`, `soft white mohair beard`), kính mắt hoặc dáng đứng, **tuyệt đối không đục nếp nhăn vào mặt**. Cả người già lẫn trẻ nhỏ đều chung nguyên lý mặt tròn nhẵn + mắt cọ vẽ phẳng.
- **Đa dạng tạng người & biểu cảm (Ponytail):**
  - *Thợ thủ công:* `tall sturdy build, broad solid shoulders, smooth softly rectangular wooden head crowned with chestnut hair under a flat cap`.
  - *Cụ già uyên bác:* `tall lean elderly frame, smooth oval wooden head crowned with gray flax hair, tiny circular brass spectacles`.
  - *Thiếu nữ thanh mảnh:* `tall statuesque silhouette, smooth oval wooden head crowned with auburn wool yarn hair under a knit beret`.
  - *Trẻ nhỏ:* `tall nimble youthful build, smooth round wooden head crowned with flaxen hair under a bonnet, curious dark eyes`.
- **Áo & Tay:** Vải dạ nỉ ép trơn nguyên khối (`pressed felt`, `woven linen`, `soft leather`).
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
| `smooth rounded wooden hands`, `wooden hands` | Cục tròn xoe Doraemon, núm bóng gỗ cụt | `delicate carved wooden hands with articulated slender fingers holding...` |
| `smooth oval wooden head` (quên tả tóc/mũ) | Đầu trọc lốc như bóng đèn bowling, quả trứng | `smooth light-toned wooden head crowned with styled [màu] wool hair under a [mũ/cap/beret]` |
| `waist-up`, `visible upper body`, `upper torso` | Tượng bán thân cụt cắm xuống đất như củ khoai | `eye-level full-body shot` (búp bê nguyên khối đứng/ngồi chạm đất) |
| `visible legs in boots` (không quần) | "Ở chuồng", chân gỗ trần truồng | `visible long legs in [charcoal/brown] tailored wool trousers and small leather boots` |
| `behind railing with visible legs` | Cưa đôi người, chân lơ lửng dưới đáy sàn | Đứng trên sàn mở (`open timber deck / terrace`), lùi toàn cảnh thấy từ đầu đến chân |
| `completely flat painted facial features, crescent eyes` (đơn độc) | Nét mực đen rạch ngang dị hợm, bowling pin vô hồn | `charming hand-painted storybook face with soft warm dark painted eyes, delicate blushed rosy cheeks, subtle gentle smile` |
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
| `jointed`, `carved wooden hands`, `stiff`, `rounded mitten hands` | Tay hình nộm cứng đơ hoặc cục tròn | `delicate carved wooden hands with articulated slender fingers`, `holding gently` |
| `two wooden hands`, `hands` đứng một mình | Bàn tay cụt/rời rạc đặt trên bàn | Gắn vào ống tay áo/nhân vật: `[nhân vật] in [áo] with sleeves, hands holding...` |
| `boots and dress hem swinging` (không người) | Quần áo tàng hình bay lơ lửng | Luôn có nhân vật ngồi/mặc: `an elderly woman seated, kicking boots...` |
| Nhân vật hậu cảnh thiếu neo (`elderly man watching`) | Trượt thành NGƯỜI THẬT hoặc mất chân | Luôn gắn neo: `a companion miniature figure standing upright beside... with visible legs` |
| `swing with chains` không tả điểm treo | Dây xích đứt đoạn lơ lửng giữa trời | Luôn gắn điểm treo: `suspended by brass chains from the curving branch of an ancient oak tree` |
| `dark wood face`, `burnt wood`, `dark clay` | Mặt gỗ mục đen cháy | `smooth round light-toned wooden head` |
| `cinematic lighting`, `dark shadows`, `noir` | Tương phản gắt, u tối | Chọn một nguồn sáng cụ thể ở Mục 5 |
| `maple leaves`, `pipe`, `knife` | Kích hoạt bộ lọc kiểm duyệt giả | `golden oak leaves`, `wooden flute`, `artisan chisel` |
