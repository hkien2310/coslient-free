# IMAGE AVOID — Luật viết prompt
*Coslient Free · Đọc trước khi viết bất kỳ prompt nào. Thế giới hình ảnh: [`STYLE_handcrafted_tactile_diorama.md`](./STYLE_handcrafted_tactile_diorama.md).*

Model ảnh đọc prompt theo nghĩa đen, gắn tính từ vào danh từ gần nhất và kéo theo thiên kiến dữ liệu huấn luyện. 6 rule dưới đây chặn các lỗi phát sinh từ cơ chế đó.

---

## Rule 1. Chỉ tả cái ống kính thấy
Mọi thứ được viết ra sẽ bị vẽ ra. Thứ nằm ngoài tầm nhìn mà vẫn được viết thì model sẽ ép nó vào khung (cắt đôi khung, dán phông giả, sinh bộ phận rời).
- Nhìn xuống: chỉ có mặt đất, mặt bàn, đỉnh đầu, vai. Không trời.
- Ngước lên: tiền cảnh, thân người, tán cây, trời. Không chi tiết dưới chân.
- Nửa người: mặt, thân trên, tay. Không quần, giày, nền đang đứng.
- Bộ phận cơ thể chỉ xuất hiện khi gắn với một cơ thể hoặc ống tay áo trong khung.

## Rule 2. Một ý, một tín hiệu
Hai cụm mâu thuẫn trong cùng prompt cho ra kết quả nửa vời hoặc biến dạng.
- Cỡ cảnh, góc máy, tư thế, bối cảnh phải cùng chỉ về một hình ảnh.
- Mỗi bề mặt một tính chất (thô hoặc mịn, không cả hai).

## Rule 3. Vị trí token quyết định chất liệu
- Danh tính là chủ thể đầu tiên, neo chất liệu của style đứng ngay sau. Neo đặt muộn sẽ bị hút sang đồ vật gần đó, nhân vật trượt thành người thật. Nhiều người thì neo chung đứng sau tất cả danh tính.
- Nhiều nhân vật chính thì mỗi người phải khác rõ ở tuổi, giới hoặc màu tóc, và mỗi người ít chi tiết hơn: mô tả càng dày, model càng gán nhầm tóc, áo giữa các người.
- Tính từ chất liệu (`needle-felted`, `clay`) chỉ đứng sát danh từ nó thuộc về.
- Suffix áp lên mọi pixel: chỉ chứa thuộc tính toàn cảnh (phong cách, ống kính, tỉ lệ khung). Không chất liệu, không giờ trong ngày.

## Rule 4. Tính từ tỷ lệ là cục bộ
`miniature`, `tiny`, `small` co danh từ đứng sau nó lại, không co cả thế giới. Kết quả: người to đứng trên công trình tí hon.
- Không gắn tính từ tỷ lệ cho thứ nhân vật đứng lên, ngồi vào hay dùng bằng cả người (cầu, thuyền, bàn, nhà, ban công). Tả theo công năng, `in natural proportion`.
- Đồ đeo, đồ cầm tay thì được (`small ribbon`).

## Rule 5. Tả trạng thái mong muốn, không gọi tên khuyết tật
Gọi tên khuyết tật là gọi nó ra. Từ ngữ mô tả quá trình hay vật liệu thô kéo theo dấu vết thô.
- Tả thành phẩm (`smooth painted figure`), không tả nguyên liệu đang làm (`sculpted polymer clay`).
- Sửa câu dương. Không dùng `--no`. Token trong từ điển bị cấm kể cả khi đi kèm `zero` hoặc `no`.

## Rule 6. Từ mang cảm xúc kéo theo cả bối cảnh
Một tính từ cảm xúc hay thể loại kéo theo ánh sáng, màu và bố cục của thể loại đó. Phép thử: *từ này thuộc thể loại phim nào?* Thể loại tối, buồn, hành động thì bỏ.

---

## Từ điển token kích hoạt
Các từ dưới đây kéo theo thiên kiến dữ liệu, không suy ra được từ nghĩa thông thường.

| Token | Model hiểu thành | Dùng thay |
|---|---|---|
| `puppet`, `doll`, `joints`, `seams`, `stitched` | Khớp cơ khí, đường khâu | `claymation figure`, `continuous organic arms` |
| `photorealistic`, `photo`, `skin texture`, `pores`, `veins`, `detailed skin` | Da người thật | `smooth satin-matte painted clay` |
| `wrinkles`, `crevices`, `aged skin` | Mặt nứt kiểu xác ướp | `soft sculptural planes, kind smile` |
| `clay skin` đứng một mình | Đất sét xám | `painted clay face in warm [tông da]` |
| `wispy hair`, `thin hair` (người già) | Hói | `full thick head of hair` hoặc mũ vải |
| `elongated neck`, `long neck` | Cổ dị dạng | `natural balanced proportions` |
| `chubby`, `plump`, `round face`, `stout`, `short` (tả dáng người) | Thần lùn | `natural balanced proportions, slender or medium build` |
| `sharp`, `pointed`, `caricature` | Mặt yêu tinh | `soft rounded contours` |
| `weathered`, `aged`, `rustic` (mặt hoặc gỗ) | Mặt nứt, gỗ mục | Mặt: `smooth sculptural planes`. Gỗ: `hand-planed solid timber with visible grain` |
| `chunky knit`, `cable sweater`, `crochet`, `yarn loops` | Áo len khổng lồ nuốt dáng | `woven linen`, `tailored wool-blend` |
| `heavy wool coat`, `duster coat` | Phom cứng phồng | Mùa lạnh: `tailored woven wool coat with soft drape` |
| `solitary`, `alone`, `lonely`, `isolated` | U sầu, cô độc | Thêm bạn đồng hành |
| `cinematic`, `moody`, `dark shadows` | Tương phản đen, noir | `soft diffused light` |
| `lens flare`, `glare`, `god rays`, `sunbeams`, `chiaroscuro` | Lóe sáng, tia gắt | `gentle ambient glow` |
| `drone shot`, `aerial photography`, `satellite view` | Ảnh flycam thật | `high-angle bird's-eye diorama view` |
| `macro`, `extreme close-up` | Ảnh sản phẩm, lộ chất liệu thô | Tối đa `close-up` |
| `crowded`, `cluttered`, `packed shelves` | Nhồi đồ | `generous negative space` |
| `daylight` trong suffix | Khóa cứng ban ngày | Đặt giờ trong khối ánh sáng |

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
