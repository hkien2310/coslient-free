# IMAGE AVOID — Luật viết prompt
*Coslient Free · Đọc trước khi viết bất kỳ prompt nào. Thế giới hình ảnh: file `STYLE_*.md` đang dùng.*

Model ảnh đọc prompt theo nghĩa đen, gắn tính từ vào danh từ gần nhất và ưu tiên trọng số chú ý (attention weight) cho các token đầu dòng. **Nguyên lý cốt lõi: Thứ tự thông tin trong prompt quyết định tất cả — cái gì quan trọng hơn bắt buộc phải ở phía trước, cái gì ít quan trọng hơn ở phía sau.** 7 rule dưới đây là luật cơ chế chặn đứng mọi lỗi biến dạng.

---

## Rule 1. Thứ Tự Thông Tin: Nguyên Tắc Trọng Số Giảm Dần & Style Anchor Vị Trí 0
Diffusion models đọc prompt tuần tự từ trái sang phải, các token ở đầu nhận attention weight cao nhất. **Thứ tự thông tin quyết định toàn bộ chất lượng ảnh: cái gì quan trọng hơn bắt buộc phải ở phía trước, cái gì ít quan trọng hơn ở phía sau.**
- **Vị trí 0 (Đầu prompt):** Luôn là Style Anchor (`Handcrafted mixed-media tabletop diorama, macro tilt-shift, `) để khóa thế giới sa bàn thủ công, dập tắt thiên kiến ảnh chụp thật ngay từ pixel đầu tiên.
- **Tiếp theo:** Cỡ cảnh & Tiêu điểm máy quay (`[Shot type] focusing on / framing [focal target]`).
- **Tiếp theo:** Nhân vật chính kèm ngay nhãn chất liệu búp bê gỗ (Neo tức thì).
- **Tiếp theo:** Hành động dở dang & Điểm neo vật lý (vật tựa, chỗ ngồi).
- **Hậu cảnh xa:** Nhân vật phụ hoặc cảnh vật ở khoảng cách xa để tạo chiều sâu.
- **Cuối cùng:** Động học môi trường, ánh sáng và tham số kỹ thuật (` --ar 16:9`).

## Rule 2. Khóa Cứng Đầu Gỗ & Mặt Vẽ Phẳng Là Cặp Đôi Bất Khả Phân (Inseparable Head-Face Lock)
Diffusion models có thiên kiến cực lớn về khuôn mặt người thật. Từ `miniature figure` hay `wooden hands` đứng một mình là KHÔNG ĐỦ — model sẽ hiểu là tượng sáp tả thực thu nhỏ và ghép một cái **ĐẦU NGƯỜI THẬT 100%** (có nếp nhăn, da thịt, râu ria sinh học) lên thân hình búp bê tay gỗ!
- **Quy tắc:** Bất kỳ nhân vật nào được nhắc tới bắt buộc phải kèm cụm khóa nguyên tử bất khả phân:
  `smooth round light-toned wooden head crowned with [flax/mohair] hair under [beret/cap], sweet minimalist face with delicate brush-painted dark eyes, completely flat painted facial features`.

## Rule 3. Cấm Tuyệt Đối Số Tuổi (Zero Age Number Rule)
Tuyệt đối không đưa số tuổi cụ thể vào prompt (`30-year-old`, `28-year-old`, `68-year-old`).
- **Cơ chế lỗi:** Các con số tuổi gắn với `year-old` kích hoạt trực tiếp các tập dữ liệu ảnh chân dung người thật đời thường (stock photo, portrait photography), lập tức vô hiệu hóa phong cách búp bê gỗ và sinh ra người thật.
- **Thay thế:** Chỉ dùng danh xưng nhân vật định tính: `a young man`, `a young woman`, `an elderly man`, `an elderly woman`, `a young child`.

## Rule 4. Cấm Close-up Vào Đầu/Mặt Trên Sa Bàn (Diorama Close-up Head Trap)
Khác với phim người thật, sa bàn tabletop diorama có tỷ lệ vi mô. Ống kính macro tilt-shift khi zoom cận cảnh vào `face`, `forehead`, `head` sẽ phóng đại phần đầu và **cắt đứt hoàn toàn thân thể**, khiến nhân vật trông như cái đầu tượng bị chặt cắm trơ trọi xuống đất rêu hoặc lấp ló mất thân sau hàng rào.
- **Quy tắc:** Cấm hoàn toàn `close-up shot` vào đầu/mặt/trán của nhân vật.
- `Close-up` CHỈ DÀNH CHO ĐỒ VẬT VÔ TRI HOẶC ĐỘNG VẬT NHỎ (túi hạt dẻ bốc khói, xích đu sồi, tách trà, con ốc sên).
- Mọi tương tác thân mật giữa các nhân vật bắt buộc phải lùi ống kính về **Trung cảnh (`medium eye-level shot`)** hoặc **Toàn cảnh (`full-body shot`)**, nơi nhân vật ngồi vững trên ghế dài hoặc đứng trên mặt đất rêu.

## Rule 5. Khử Ép Khớp Búp Bê & Chống Chắp Vá Trang Phục (Anti-Patchwork & Solid Felt)
- **Khử ép khớp (No unnatural doll strain):** Búp bê gỗ thủ công không có khớp cổ uốn lượn để "chạm trán" (`resting foreheads together`) như người thật. Tương tác thân mật phải mang tính tự nhiên của búp bê: đứng kề vai (`standing shoulder-to-shoulder`), tựa đầu lên vai nhau khi ngồi ghế dài (`resting head gently on shoulder while seated on a bench`).
- **Chống chắp vá (Anti-patchwork):** Cụm từ `mixed-media` rất dễ kích hoạt thiên kiến nghệ thuật cắt dán giấy vụn, bìa các-tông hoặc vải rách chắp vá (`patchwork quilt`). Trang phục bắt buộc phải khóa bằng: `loose single-piece pressed felt coat/dress hanging in soft clean folds`.

## Rule 6. Quy Tắc Một Tiêu Điểm Duy Nhất (Single Focus Law)
Không bao giờ nhồi nhét quá nhiều nhân vật hành động phức tạp trong cùng một khung hình (ví dụ: 4 người / 2 cặp vợ chồng cùng đu 2 xích đu song song).
- **Cơ chế lỗi:** Khi prompt chứa quá nhiều chủ thể người và động từ tương tác phức tạp, mô hình khuếch tán bị quá tải token (token overload), bỏ qua phong cách diorama ở đầu dòng và trượt về vẽ người thật ngoài công viên.
- **Quy tắc:** Mỗi khung hình chỉ tập trung vào **MỘT cặp nhân vật** hoặc **MỘT nhân vật chính** làm tiêu điểm. Nếu có người khác, họ phải ở hậu cảnh rất xa (`in the far distant background, tiny miniature figures...`).

## Rule 7. Neo Tức Thì Từng Cá Thể — Cấm Neo Trễ (Immediate Individual Bracketing)
Diffusion models xử lý văn bản tuần tự từ trái sang phải. Bất kỳ danh từ người nào (`young man`, `wife`, `elderly woman`, `craftsman`) xuất hiện lần đầu tiên mà không có nhãn phong cách đi kèm NGAY LẬP TỨC sẽ bị model khởi tạo thành **NGƯỜI THẬT ĐỜI THƯỜNG**.
- **Cấm neo trễ:** Tuyệt đối không viết một loạt nhân vật rồi mới chốt `both as tall storybook miniature figures` ở cuối câu. Cụm ở cuối không thể ghi đè nhân vật đã bị biến thành người thật ở đầu câu.
- **Quy tắc:** Mỗi nhân vật khi được gọi tên phải được bọc ngay lập tức: `a young man as a stylized whimsical folk art miniature figure with a smooth round wooden head... pulling his wife, also a miniature figure in a felt dress with a painted face...`.

## Rule 8. Toàn Vẹn Tư Thế & Phân Bậc Phối Cảnh Chiều Sâu (Scale & Stance Anchoring)
- **Tránh người sau to hơn người trước:** Trong khung hình 16:9, nhân vật hậu cảnh bắt buộc phải có từ khóa tỷ lệ và cự ly xa rõ ràng: `in the far distant background, tiny miniature figures...`.
- **Tránh mất chân người sau:** Mọi nhân vật phụ ở hậu cảnh muốn nhìn thấy rõ phải có tư thế cơ thể và điểm tựa hoàn chỉnh: `standing upright beside the oak trunk with visible legs in small boots` hoặc `seated securely upon a distant timber bench`. Không tả lơ lửng `watching with a smile`.

## Rule 9. Điểm Neo Vật Lý & Trọng Lực (Structural Anchors)
Mọi vật thể treo, đung đưa, lơ lửng hoặc chịu lực (dây xích đu, lồng đèn, dây phơi, khinh khí cầu) **phải có điểm neo vật lý liên kết trong tầm nhìn của máy quay** (ví dụ: `suspended by brass chains from the low thick branch of an ancient oak tree`). Nếu không tả cành cây, dây xích sẽ bị đứt đoạn lơ lửng giữa trời.

---

## Từ điển token kích hoạt
Các từ dưới đây kéo theo thiên kiến dữ liệu, không suy ra được từ nghĩa thông thường.

| Token | Model hiểu thành | Dùng thay |
|---|---|---|
| `30-year-old`, `28-year-old`, `68-year-old` (số tuổi) | Người thật đời thường, nếp nhăn, râu ria sinh học | `a young man`, `a young woman`, `an elderly couple`, `a child` |
| `close-up on face/forehead/head` | Cắt đứt thân thể, đầu tượng cắm xuống đất rêu | Chuyển thành `medium eye-level shot` ngồi trên ghế hoặc đứng |
| `miniature figure` đứng một mình không tả đầu | Tượng sáp tả thực, đầu người thật ghép tay gỗ | `folk art miniature figure with a smooth round wooden head and painted face` |
| `resting foreheads together` (chạm trán) | Ép khớp cổ dị dạng, mất thân búp bê | `standing shoulder-to-shoulder` hoặc `resting head on shoulder while seated` |
| `two swings with 4 people` (nhồi nhét) | Quá tải token, trượt thành người thật | Tách thành 1 cặp nhân vật duy nhất làm tiêu điểm |
| `patchwork`, `patched`, `rags`, `mixed-media` tự do | Cắt dán giấy vụn, bìa các-tông chắp vá rách rưới | `loose single-piece pressed felt coat/dress in soft clean folds` |
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
