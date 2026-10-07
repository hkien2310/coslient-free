# IMAGE AVOID — Luật viết prompt
*Coslient Free · Đọc trước khi viết bất kỳ prompt nào. Thế giới hình ảnh: file `STYLE_*.md` đang dùng.*

Model ảnh đọc prompt theo nghĩa đen, gắn tính từ vào danh từ gần nhất và kéo theo thiên kiến dữ liệu huấn luyện. 6 rule dưới đây chặn các lỗi phát sinh từ cơ chế đó.

---

## Rule 1. Thực thể Chủ quyền bất biến (Host Entity Invariance — "Luôn tả người")
Không bao giờ để bộ phận cơ thể (tay, chân, mắt), trang phục (giày, váy, áo), hoặc hành động vi mô đứng đơn độc làm chủ ngữ của prompt.
- Bất kỳ cận cảnh nào (tay bóc hạt dẻ, chân đung đưa, tay gõ búa, tà áo bay) **bắt buộc phải khai báo nhân vật búp bê chủ quyền** ngay trong câu: `an elderly woman as a stylized storybook miniature figure, her simple rounded wooden hands emerging from wool sleeves to...`.
- *Hệ quả cơ chế:* Nếu bỏ qua người mà tả bộ phận rời rạc (`two wooden hands cracking a bag`), AI sẽ vẽ bàn tay ma-nơ-canh bị cưa cụt rời rạc đặt trên bàn. Nếu chỉ tả `boots kicking in the air`, AI sẽ vẽ đôi ủng tàng hình bay lơ lửng không người.

## Rule 2. Ống kính & Điểm neo vật lý (Camera Target & Structural Anchor — "Tả máy quay chụp cái gì")
- Câu mở đầu phải định hình góc máy và **tiêu điểm cụ thể mà máy quay đang bắt trọn** (`[Cỡ cảnh + Góc máy] focusing on / capturing [vật thể/hành vi tiêu điểm]`).
- Mọi vật thể treo, đung đưa, lơ lửng hoặc chịu lực (dây xích đu, lồng đèn, dây phơi, khinh khí cầu) **phải có điểm neo vật lý liên kết trong tầm nhìn của máy quay** (ví dụ: `suspended by brass chains from the thick lower branch of an ancient oak tree`).
- *Hệ quả cơ chế:* Nếu viết `a swing with brass chains` mà không tả điểm treo, dây xích sẽ bị đứt đoạn lơ lửng giữa trời xanh.

## Rule 3. Đóng băng phong cách mọi nhân vật trong khung (Universal Character Bracketing)
Mọi danh từ chỉ người xuất hiện trong prompt (`man`, `woman`, `child`, `companion`, `craftsman`) dù ở tiền cảnh, trung cảnh hay mờ ở hậu cảnh (`background`) **bắt buộc phải được bọc nhãn phong cách búp bê ngay lập tức**:
- Dùng: `[nhân vật] as a stylized storybook miniature figure with a painted wooden face`.
- Cảnh có người hậu cảnh: `in the soft-focus background a companion miniature elderly figure watching with a gentle painted smile`.
- *Hệ quả cơ chế:* Diffusion models có thiên kiến mặc định biến các danh từ người thông thường (`elderly man watching`) thành NGƯỜI THẬT ĐỜI THƯỜNG. Không bao giờ thả lỏng một danh từ người đứng trơ trọi.

## Rule 4. Chỉ tả cái ống kính thấy & Không mâu thuẫn tín hiệu
Mọi thứ được viết ra sẽ bị ép vẽ ra.
- Nhìn xuống đất/bàn: không tả trời.
- Ngước nhìn lên: không tả chi tiết dưới mặt đất.
- Cận cảnh nửa người: không tả quần, giày hay mặt đường.
- Một bề mặt chỉ có một tính chất (mịn phẳng hoặc sần sùi, không cả hai).

## Rule 5. Vị trí token & Tính từ tỷ lệ là cục bộ
- Tính từ chất liệu (`needle-felted`, `linen`, `timber`) chỉ đứng sát danh từ nó thuộc về.
- Các từ `miniature`, `tiny`, `small` co danh từ ngay sau nó lại, không co cả thế giới. Không gắn tính từ tỷ lệ cho thứ nhân vật đứng lên, ngồi vào hay dùng bằng cả người (cầu, thuyền, bàn, nhà, ban công). Tả theo công năng: `in natural proportion`.
- Suffix áp lên mọi pixel: chỉ chứa thuộc tính toàn cảnh (phong cách, ống kính, tỉ lệ khung). Không nhét chất liệu hay giờ trong ngày vào suffix.

## Rule 6. Tả trạng thái mong muốn, không gọi tên khuyết tật
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
