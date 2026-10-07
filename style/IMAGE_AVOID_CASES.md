# IMAGE AVOID — Luật viết prompt
*Coslient Free · Đọc trước khi viết bất kỳ prompt nào. Thế giới hình ảnh: file `STYLE_*.md` đang dùng.*

Model ảnh đọc prompt theo nghĩa đen, gắn tính từ vào danh từ gần nhất và kéo theo thiên kiến dữ liệu huấn luyện. 6 rule dưới đây chặn các lỗi phát sinh từ cơ chế đó.

---

## Rule 1. Thực thể Chủ quyền & Khớp Cỡ cảnh Thân thể (Host Entity & Torso Boundary)
- Không bao giờ để bộ phận cơ thể (tay, chân, mắt), trang phục (giày, váy, áo), hoặc hành động vi mô đứng đơn độc làm chủ ngữ của prompt. Bất kỳ cận cảnh nào cũng phải gắn chặt với một nhân vật búp bê chủ quyền đầy đủ (`an elderly woman as a stylized storybook miniature figure, her hands emerging from wool cuffs...`).
- **Khử lỗi mất thân:** Cận cảnh trung (`Medium close-up`) chỉ lấy từ thắt lưng trở lên. Bắt buộc phải khai báo tư thế phần thân trên (`waist-up view... with visible upper torsos in tailored wool coats standing chest-to-chest`). **Tuyệt đối cấm dùng từ `tall` đơn độc trong cận cảnh khi không có chân**, vì AI sẽ bị xung đột giữa chiều cao và góc cận, dẫn đến việc vùi dập thân thể dưới đất và chỉ vẽ đầu mọc lên từ thảm lá.

## Rule 2. Neo Tức Thì Từng Cá Thể — Cấm Neo Trễ (Immediate Individual Bracketing)
Diffusion models xử lý văn bản tuần tự từ trái sang phải. Bất kỳ danh từ người nào (`young man`, `wife`, `elderly woman`, `craftsman`) xuất hiện lần đầu tiên mà không có nhãn phong cách đi kèm NGAY LẬP TỨC sẽ bị model khởi tạo thành **NGƯỜI THẬT ĐỜI THƯỜNG**.
- **Cấm neo trễ:** Tuyệt đối không viết một loạt nhân vật rồi mới chốt `both as tall storybook miniature figures` ở cuối câu. Cụm ở cuối không thể ghi đè nhân vật đã bị biến thành người thật ở đầu câu.
- **Quy tắc:** Mỗi nhân vật khi được gọi tên phải được bọc ngay lập tức: `a young man as a stylized whimsical storybook miniature figure... pulling his wife, also a miniature figure in a felt dress...`.
- Cấm bỏ quên nhãn ở nhân vật chính trong cận cảnh (`focusing on the swinging motion of an elderly woman...` $\rightarrow$ biến bà cụ thành người thật ngay lập tức).

## Rule 3. Phân Bậc Phối Cảnh Chiều Sâu (Depth Gradient & Scale Anchoring)
Khung hình `--ar 16:9` rất rộng theo chiều ngang. Nếu đưa 2 nhóm nhân vật vào cùng một shot toàn cảnh mà không khóa khoảng cách hình học, AI sẽ dàn đều bố cục và vẽ nhóm hậu cảnh to ngang ngửa hoặc to hơn nhóm tiền cảnh.
- Nhân vật hậu cảnh **bắt buộc phải có từ khóa khoảng cách và tỷ lệ rõ ràng**: `in the far distant background, a tiny miniature elderly couple seated on a faraway bench with painted wooden faces`.
- Tiền cảnh là trọng tâm (`in the foreground`), hậu cảnh phải là "tiny / far-off".

## Rule 4. Toàn Vẹn Tư Thế Nhân Vật Hậu Cảnh (Explicit Stance Anchor)
Khi nhân vật hậu cảnh chỉ được mô tả hành động trừu tượng như `watching with a smile` mà không có tư thế chân/chỗ đứng, AI sẽ chỉ vẽ phần đầu hoặc nửa thân trên lấp ló, cắm luôn nhân vật xuống đất dẫn đến mất chân.
- **Quy tắc:** Mọi nhân vật hậu cảnh muốn thấy rõ dáng người phải có tư thế cơ thể hoàn chỉnh gắn với một điểm tựa cụ thể: `standing upright beside the great oak trunk with visible legs in boots` hoặc `seated securely upon a distant timber bench`.

## Rule 5. Ống kính & Điểm neo vật lý (Camera Target & Structural Anchor)
- Câu mở đầu phải định hình góc máy và **tiêu điểm cụ thể mà máy quay đang bắt trọn** (`[Cỡ cảnh + Góc máy] focusing on / framing [vật thể/hành vi tiêu điểm]`).
- Mọi vật thể treo, đung đưa, lơ lửng hoặc chịu lực (dây xích đu, lồng đèn, dây phơi, khinh khí cầu) **phải có điểm neo vật lý liên kết trong tầm nhìn của máy quay** (ví dụ: `suspended by brass chains from the thick lower branch of an ancient oak tree`). Nếu không tả cành cây, dây xích sẽ bị đứt đoạn lơ lửng giữa trời.

## Rule 6. Vị trí token & Tính từ tỷ lệ là cục bộ
- Tính từ chất liệu (`needle-felted`, `linen`, `timber`) chỉ đứng sát danh từ nó thuộc về.
- Các từ `miniature`, `tiny`, `small` co danh từ ngay sau nó lại, không co cả thế giới. Không gắn tính từ tỷ lệ cho thứ nhân vật đứng lên, ngồi vào hay dùng bằng cả người (cầu, thuyền, bàn, nhà, ban công). Tả theo công năng: `in natural proportion`.
- Suffix áp lên mọi pixel: chỉ chứa thuộc tính toàn cảnh (phong cách, ống kính, tỉ lệ khung). Không nhét chất liệu hay giờ trong ngày vào suffix.

## Rule 7. Tả trạng thái mong muốn, không gọi tên khuyết tật
Gọi tên khuyết tật là gọi nó ra. Từ ngữ mô tả quá trình hay vật liệu thô kéo theo dấu vết thô.
- Tả thành phẩm (`smooth light-toned wooden head`), không tả công cụ cắt gọt nguyên liệu (`carved`, `chiseled`).
- Sửa câu khẳng định tích cực. Không dùng `--no` (bộ lọc phủ định không hiệu quả trên diffusion models).
## Rule 8. Khóa Cứng Tóc & Mũ — Chống Đầu Trọc Lốc (The Mandatory Hair & Headwear Anchor)
Khi prompt chỉ ghi `smooth oval wooden head` mà quên tả tóc hoặc mũ, diffusion model sẽ hiểu theo nghĩa đen là quả cầu gỗ tiện trần trụi, trọc lốc như quả trứng hoặc bóng đèn bowling (Xem Case Image 2, 3, 4, 5).
- **Quy tắc:** Bất kỳ nhân vật nào (nam, nữ, già, trẻ, nghệ nhân) BẮT BUỘC phải có tóc và/hoặc mũ nón đi liền ngay sau đầu gỗ:
  `smooth light-toned wooden head crowned with styled [auburn / chestnut / gray / flaxen] needle-felted wool hair under a tailored [flat cap / beret / bonnet / hood]`.
- **Tuyệt đối cấm:** Để cụm `smooth [round/oval] wooden head` đứng trơ trọi mà không có tóc hay mũ che phủ.

## Rule 9. Chống Bàn Tay Cục Doraemon (Articulated Fingers vs Spherical Stubs)
Cụm từ `smooth rounded wooden hands` hoặc `wooden hands` đứng đơn độc khiến AI vẽ một khối cầu tròn vo bằng gỗ không ngón, y hệt bàn tay Doraemon hoặc núm cửa tròn (Xem Case Image 1, 3).
- **Quy tắc:** Cấm tuyệt đối `rounded wooden hands`.
- **Cú pháp chuẩn:** `delicate carved wooden hands with articulated slender fingers holding [vật]` hoặc `expressive miniature wooden hands with visible delicate fingers`.

## Rule 10. Chống Cụt Thân / Mất Người Khi Ngồi Ghế (Grounded Figurine Stance)
Cụm từ `waist-up view sitting on a bench` khiến model cắt ngang cơ thể tại thắt lưng, biến nhân vật thành khúc gỗ cụt bị cắm xuống mặt ghế hoặc vùi trong rêu đá mà không có chân (Xem Case Image 1, 3, 5).
- **Quy tắc:** Cấm dùng `waist-up view` khi nhân vật ngồi trên ghế park bench, thềm đá hay bãi cỏ. Búp bê sa bàn bắt buộc phải thấy trọn vẹn tư thế ngồi tiếp đất:
  `eye-level medium shot, framing the figures seated side by side on a curved timber bench with visible legs in tailored trousers and small leather boots resting firmly on the mossy flagstones`.

## Rule 11. Mặt Truyện Tranh Ấm Áp vs Mặt Dị Hợm / Bowling Pin (Warm Storybook Face Anchor)
Cụm từ `completely flat painted facial features, minimalist painted crescent eyes` khi đi cùng đầu gỗ trọc sẽ kích hoạt các nét mực đen rạch ngang ma quái, vô hồn như hình nộm voodoo hoặc tượng bowling pin (Xem Case Image 2, 4).
- **Quy tắc:** Khuôn mặt búp bê dân gian phải được neo bằng tính từ truyện tranh ấm áp, giàu sinh khí:
  `charming hand-painted storybook face with soft warm dark painted eyes, delicate blushed rosy cheeks, and a subtle gentle smile`.

---

## Từ điển token kích hoạt
Các từ dưới đây kéo theo thiên kiến dữ liệu, không suy ra được từ nghĩa thông thường.

| Token | Model hiểu thành | Dùng thay |
|---|---|---|
| `smooth rounded wooden hands`, `wooden hands` | Cục tròn xoe Doraemon, bóng gỗ cụt không ngón | `delicate carved wooden hands with articulated slender fingers holding...` |
| `smooth oval wooden head` (không tóc/mũ) | Đầu trọc lốc như bóng đèn, quả trứng gỗ | `smooth light-toned wooden head crowned with styled [màu] wool hair under a [mũ/cap/beret]` |
| `waist-up view sitting on a bench` | Cụt nửa người, khúc gỗ cắm xuống ghế | `medium shot framing the figures seated with visible legs in trousers and small boots resting on the ground` |
| `completely flat painted facial features, crescent eyes` (đơn độc) | Mắt rạch vệt đen dị hợm, bowling pin vô hồn | `charming hand-painted storybook face, soft warm dark painted eyes, delicate blushed rosy cheeks, subtle gentle smile` |
| `puppet`, `doll`, `joints`, `seams`, `stitched` | Khớp cơ khí, đường khâu | `claymation figure`, `continuous organic arms` |
| `photorealistic`, `photo`, `skin texture`, `pores`, `veins`, `detailed skin` | Da người thật | `smooth satin-matte painted clay` |
| `wrinkles`, `crevices`, `aged skin` | Mặt nứt kiểu xác ướp | `soft sculptural planes, kind smile` |
| `clay skin` đứng một mình | Đất sét xám | `painted clay face in warm [tông da]` |
| `wispy hair`, `thin hair` (người già) | Hói | `softly styled brushed mohair hair in gentle natural locks` hoặc mũ vải |
| `wig`, `doll hair`, `plastic hair`, `flyaway`, `loose strands` | Tóc giả dán keo hoặc sợi cước/mạng nhện lơ lửng | `softly styled brushed mohair hair in gentle natural locks` |
| `elongated neck`, `long neck` | Cổ dị dạng | `natural balanced proportions` |
| `chubby`, `plump`, `round face`, `stout`, `short` (tả dáng người) | Thần lùn | `natural balanced proportions, slender or medium build` |
| `sharp`, `pointed`, `caricature` | Mặt yêu tinh | `soft rounded contours` |
| `weathered`, `aged`, `rustic` (mặt hoặc gỗ) | Mặt nứt, gỗ mục | Mặt: `smooth sculptural planes`. Gỗ: `hand-planed solid timber with visible grain` |
| `chunky knit`, `cable sweater`, `crochet`, `yarn loops` | Áo len khổng lồ nuốt dáng | `woven linen`, `tailored wool-blend` |
| `heavy wool coat`, `duster coat` | Phom cứng phồng | Mùa lạnh: `tailored woven wool coat with soft drape` |
| `solitary`, `alone`, `lonely`, `isolated` | U sầu, cô độc, thị trấn ma | Thêm `softly blurred in the background, distant townsfolk` |
| `small houses`, `tiny cottages`, `miniature roofs` | Nhà búp bê tí hon, hiệu ứng Gulliver | `grand towering multi-story townhouses in majestic natural scale` |
| `crooked cabin`, `shack`, `hovel`, `lean-to` | Túp lều rách nát, ổ chuột chắp vá | `curved bulbous timber dwelling`, `fairytale townhouse` |
| `laundry on rope/line` cạnh nhà | Quần áo rách phơi bừa bãi, nghèo túng | Chậu hoa ban công, giỏ quả tươi (`blooming planter, fruit basket`) |
| `pulling`, `straining`, `heaving` | Còng lưng gồng mình, mưu sinh lam lũ | `resting leisurely`, `holding gently`, `strolling` |
| `straight walls`, `rigid geometry` | Hộp bê tông hiện đại, khô cứng | `organic curvilinear architecture with no straight lines` |
| `dark wood face`, `raw unpainted wood face` | Mặt đen xì, vân gỗ khô thô ráp | `smooth carved light-toned wooden head with a warm fair complexion` |
| `fantasy costume`, `elaborate embroidery`, `costume props` | Diêm dúa, cosplay phù thủy lố lăng | `tasteful, beautifully designed thick timeless clothing with clean graceful silhouette` |
| `cinematic`, `moody`, `dark shadows` | Tương phản đen, noir | `soft diffused light` |
| `lens flare`, `glare`, `god rays`, `sunbeams`, `chiaroscuro` | Lóe sáng, tia gắt | `gentle ambient glow` |
| `drone shot`, `aerial photography`, `satellite view` | Ảnh flycam thật | `high-angle bird's-eye diorama view` |
| `macro`, `extreme close-up` | Ảnh sản phẩm, lộ chất liệu thô | Tối đa `close-up` |
| `crowded`, `cluttered`, `packed shelves` | Nhồi đồ | `generous negative space` |
| `daylight` trong suffix | Khóa cứng ban ngày | Đặt giờ trong khối ánh sáng |
| `gloomy`, `overcast`, `thick cold fog` | Trời xám xịt, lạnh lẽo, cạn năng lượng | `clear warm natural daylight`, `warm low golden-hour backlight` |
| `standing still`, `blank stare`, `stiff pose` | Tượng ma-nơ-canh chết | Tư thế cử động cụ thể (`strolling briskly`, `leaning gently`, `smiling warmly`) |
| `deserted street`, `empty alley` | Thị trấn ma hoang vắng | `softly blurred in the background, distant townsfolk...` |
| `two wooden hands`, `hands` đứng một mình | Bàn tay cụt/rời rạc đặt trên bàn | Gắn vào ống tay áo/nhân vật: `[nhân vật] in [áo] with sleeves, hands holding...` |
| `boots and dress hem swinging` (không người) | Quần áo tàng hình bay lơ lửng | Luôn có nhân vật ngồi/mặc: `an elderly woman seated, kicking boots...` |
| Nhân vật hậu cảnh thiếu neo chất liệu (`elderly man watching`) | Trượt thành NGƯỜI THẬT | Luôn gắn neo: `a softly blurred elderly man as a storybook miniature figure with a painted wooden face watching` |
| `swing with chains` không tả điểm treo | Dây xích đứt đoạn lơ lửng giữa trời | Luôn gắn điểm treo: `suspended by brass chains from the curving branch of an ancient oak tree` |

### Bộ lọc kiểm duyệt (báo động giả)
| Token | Dùng thay |
|---|---|
| `maple leaves` | `oak / willow / birch leaves` |
| `pot`, `flowerpot` | `ceramic planter`, `ceramic vase` |
| `crystal`, `crystalline` | `glistening`, `sparkling`, `clear` |
| `pipe`, `tobacco` | `pocket watch`, `wooden flute` |
| `knife`, `blade` | `artisan chisel`, `carved` |

---

## Khi ảnh render ra lỗi
1. Gọi đúng triệu chứng trong ảnh.
2. Tìm rule bị vi phạm: thứ ngoài tầm nhìn (R1), cụm mâu thuẫn (R2), token sai vị trí (R3), tính từ tỷ lệ (R4), gọi tên khuyết tật (R5), từ cảm xúc (R6), hay một token trong từ điển.
3. Sửa câu dương theo rule đó. Nếu lỗi do một token mới chưa có trong từ điển, thêm một dòng vào bảng. Không thêm mô tả tình huống.
