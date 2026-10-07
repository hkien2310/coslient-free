# IMAGE AVOID — Luật viết prompt
*Coslient Free · Đọc trước khi viết bất kỳ prompt nào. Thế giới hình ảnh: file `STYLE_*.md` đang dùng.*

Model ảnh đọc prompt theo nghĩa đen, gắn tính từ vào danh từ gần nhất và ưu tiên trọng số chú ý (attention weight) cho các token đầu dòng. **Nguyên lý cốt lõi: Thứ tự thông tin trong prompt quyết định tất cả — cái gì quan trọng hơn bắt buộc phải ở phía trước, cái gì ít quan trọng hơn ở phía sau.** 7 rule dưới đây là luật cơ chế chặn đứng mọi lỗi biến dạng.

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
- Không dùng từ ngữ cảm xúc nặng nề kéo theo tông màu đen tối (`dark`, `gloomy`, `lonely`).

---

## Từ điển token kích hoạt
Các từ dưới đây kéo theo thiên kiến dữ liệu, không suy ra được từ nghĩa thông thường.

| Token | Model hiểu thành | Dùng thay |
|---|---|---|
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
