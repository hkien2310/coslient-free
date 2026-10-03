# 🛡️ IMAGE AVOID CASES & STYLE FEEDBACK GUIDE
*Sổ tay Chẩn đoán Lỗi, Bẫy Từ khóa & Quy chuẩn Hình ảnh Đồng bộ · Coslient Free*

> 🤖 **CHỈ THỊ CHO AI (BẮT BUỘC ĐỌC TRƯỚC KHI TẠO PROMPT):**
> - Trước khi viết bất kỳ prompt nào vào `image.txt` hoặc tạo prompt test, AI **bắt buộc phải đọc file này**.
> - Tuyệt đối không dùng các từ khóa trong cột **TỪ KHÓA CẤM**.
> - Luôn thay thế bằng cụm từ tương ứng trong cột **TỪ KHÓA THAY THẾ BẮT BUỘC**.
> - Khi phát hiện lỗi mới từ ảnh render, tuân thủ đúng quy trình chẩn đoán 3 bước và cập nhật case mới vào tài liệu duy nhất này.

---

## 🔍 1. QUY TRÌNH CHẨN ĐOÁN & SỬA LỖI (3 BƯỚC)

*Nguyên tắc cốt lõi: **Sửa câu dương (Positive Prompt), không thêm từ cấm vào Negative Prompt**.*

### Bước 1: Xác định triệu chứng
Mô tả chính xác cái gì sai trong ảnh (da người thật, tay khổng lồ, mất chân, búp bê nứt nẻ, len nỉ xâm chiếm...).

### Bước 2: Truy tìm từ khóa gốc
Đọc prompt đã dùng và hỏi: *"Từ khóa/cụm từ nào trong câu dương đang **ra lệnh hoặc vô tình kích hoạt** AI tạo ra hiện tượng này?"*
- **Kiểm tra xung đột:** Có 2 cụm nào đang mâu thuẫn nhau không? (Ví dụ: `Medium shot` đấm nhau với `standing on a miniature balcony`).
- **Kiểm tra thiên kiến training data:** Cụm từ có vô tình kích hoạt kho ảnh chụp người thật/ảnh sản phẩm Etsy không? (Ví dụ: `hands of a gardener` + `needle-felted bird` = ảnh người thật cầm đồ chơi len).
- **Kiểm tra đánh tráo Token:** Token chất liệu có bị hút sang đồ vật thay vì nhân vật không? (Ví dụ: nặn đất sét $\rightarrow$ cái bình thành đất sét, người thành người thật).

### Bước 3: Sửa logic câu dương & 5 nguyên tắc bất biến
1. **Mô tả thành phẩm, không mô tả nguyên liệu thô:**
   - ❌ `sculpted matte polymer clay` (nguyên liệu đang nặn $\rightarrow$ dễ sinh vân nứt).
   - ✅ `smooth painted claymation figure` (búp bê đã hoàn thiện).
2. **Một ý = một cụm nhất quán, không dùng 2 cụm đấm nhau:**
   - ❌ `polymer clay` + `velvety smooth finish` (thô + mịn $\rightarrow$ kết quả bất ổn).
   - ✅ `smooth painted finish` (một tín hiệu rõ ràng).
3. **Kiểm tra từ khóa theo cỡ cảnh:**
   - `finely crafted miniature details` $\rightarrow$ cảnh rộng: đẹp; cảnh siêu cận da: có thể sinh vết đục nếu thiếu định tính mịn.
4. **Tránh mô tả bộ phận cơ thể trơ trọi mà thiếu định danh con rối:**
   - ❌ `the hands of an old gardener` $\rightarrow$ AI lôi ngay tay người thật vào vẽ.
   - ✅ `the miniature clay hands of a handcrafted claymation gardener character`.
5. **Dọn dẹp triệt để:** Khi sửa đúng câu dương gốc, không cần nhồi nhét các từ cấm vô nghĩa.

---

## 📌 2. BẢNG TRA CỨU BẪY TỪ KHÓA (KEYWORD TRAP CHEAT SHEET)

| STT | Hiện tượng lỗi (Triệu chứng) | Từ khóa cấm / Gây lỗi | Tại sao gây lỗi | Từ khóa thay thế bắt buộc |
|:---:|---|---|---|---|
| **1** | **Búp bê khâu vá Frankenstein, lộ ngấn khớp cổ tay/gáy** | `puppet`, `puppets`, `seamless`, `stitched`, `doll`, `joints`, `no joints` | AI bắt dính gốc từ `seam` và `joint` rồi vẽ chỉ khâu chằng chịt, vẽ khớp nối cơ học | Gọi thẳng: `character figure`, `craftsman`, `grandfather`. Dùng: `continuous organic arms and hands with smooth finish` |
| **2** | **Trượt sang người thật 100%, diễn viên hóa trang** | `photorealistic`, `photo`, `skin texture`, tả giải phẫu người thiếu chất liệu điêu khắc | Kích hoạt máy ảnh chụp người thật, mất chất hoạt hình thủ công | Bắt buộc có: `stylized character design`, `crafted as a tactile handcrafted claymation figure`, `smooth matte finish` |
| **3** | **Len nỉ xâm chiếm toàn cảnh, đồi cỏ/khói hóa len** | `needle-felted` hoặc `craft textures` nằm trong Suffix dùng chung | Suffix toàn cục ép 100% pixel (kể cả cỏ, mây, suối, khói) thành thảm len nỉ | Bỏ khỏi suffix chung. `needle-felted` **CHỈ** gắn vào sinh vật/động vật sống |
| **4** | **Cốc/đồ vật bị chắp vá vải nỉ, khâu chỉ méo mó** | `ceramic mug` đi kèm `needle-felted / craft textures` trong prompt | AI hiểu nhầm thành đồ thủ công nỉ chắp vá | `smooth glazed terracotta ceramic mug with glossy kiln finish` |
| **5** | **Khói lò sưởi / hơi nước biến thành 2 dải len xoắn** | Thiếu định danh môi trường thật trong cảnh stop-motion | AI dùng sợi len/bông gòn làm khói giả kiểu stop-motion cổ điển | Khẳng định môi trường thật: `real wisps of steam`, `natural smoke rising smoothly`, `atmospheric natural vapor` |
| **6** | **Gỗ bị mục rỗng, mủn nát, nứt toác, bám rêu nấm** | `weathered timber`, `weathered wood`, `aged oak`, `rustic` | Kích hoạt dữ liệu gỗ ẩm mốc mục nát ngoài bãi rác | `hand-planed solid timber with visible grain`, `sturdy carved oak with subtle surface scratches and artisan tool marks`, `smooth waxed pine` |
| **7** | **Mặt nhọn góc cạnh, gân guốc (Ác hiểm, yêu tinh)** | `sharp`, `pointed`, `planar facial features`, `caricature` | Góc nhọn sinh cảm giác hiểm độc, yêu tinh, phù thủy | `zero sharp angles, exclusively soft bulbous rounded contours, charming exaggerated features` |
| **8** | **Cụ già bị hói đầu mảng lớn, tóc lơ thơ** | `wispy hair`, `thin hair`, quên khóa tóc cho người già | AI mặc định gán người già với chứng rụng tóc hói đầu | Khóa 100%: `a full thick head of wavy silver wool hair` hoặc đội `vintage wool tweed flat cap` |
| **9** | **Quần áo đất sét cứng đờ HOẶC phồng to thành cục len đan (Chunky Knit / Crochet)** | `sculpted clothing`, `clay clothes`, `chunky hand-knitted cable sweater`, `yarn loops`, `knit cardigan`, `crochet` | Đất sét làm cứng đờ; len đan to sợi khiến AI đan sợi len khổng lồ bao trùm cả người, nuốt mất phom | Bắt buộc dùng vải dệt may đo: `tailored woven linen shirt`, `tailored tweed vest / waistcoat`, `tailored corduroy jacket`, `tailored wool-blend overcoat` (Zero chunky knitwear, zero clay clothing) |
| **10** | **Kích hoạt bộ lọc kiểm duyệt an toàn (False Positives)** | `maple leaves` (cần sa), `pot / flowerpot` (chất cấm), `pipe / tobacco`, `knife / blade`, `crystals` | Trùng từ khóa nhạy cảm trong hệ thống an toàn của Midjourney / DALL-E | Đổi thành: `oak leaves`, `ceramic planter`, `pocket watch`, `carving gouge / artisan chisel`, `glistening / sparkling` |
| **11** | **Thần lùn Gnome / Củ khoai tây tròn lùn tịt** | `chubby`, `plump`, `round face`, `short`, `stout`, `double chin` | Kích hoạt dữ liệu thần lùn, thú bông béo tròn mất vẻ thanh lịch | Khóa trục thanh mảnh: `tall slender frame, graceful upright posture, narrow/oval face, natural balanced proportions` |
| **12** | **Meta AI bị kẹt vào 1 nhân vật duy nhất (Trùng lặp 100%)** | Đặt `puppet` hoặc `stop-motion` lên đầu câu lệnh | Kích hoạt ngăn tủ dữ liệu 3D con rối nghèo nàn duy nhất của Meta AI | Bắt buộc dùng Token Inversion: Đưa `[Tuổi]-year-old [Quốc tịch] [Nghề nghiệp] with [Mặt hẹp]` lên đầu câu |
| **13** | **Cụ già mặt như xác ướp mốc thếch, nứt nẻ, gân cổ gà tây** | `weathered`, `crinkled`, `wrinkles`, `crevices`, `deep lines`, `aged skin`, `aged jaw` | AI khuếch đại nếp nhăn thành rãnh nứt toác, biến đất sét thành xác ướp | Khóa mặt mịn: `smooth matte clay face with clean sculptural planes, kind warm smile, wire-rimmed spectacles, zero craggy wrinkles` |
| **14** | **Da mặt/tay xám ngoét, trắng bệch như thạch cao** | `clay skin`, `matte clay` trơ trọi đi cùng bối cảnh màu than xám | AI hiểu nhầm thành đất sét xám công nghiệp hoặc bị lan màu xám | Bắt buộc khóa sắc tố da đào ấm: `warm peach-toned matte clay skin with healthy subtle blush`, `warm ivory-peach skin tone` |
| **15** | **Cổ dài ngoằng lêu nghêu, dị dạng như hươu cao cổ** | `elongated neck`, `long neck` | AI hiểu nghĩa đen là kéo dài dị thường, biến cổ thành ống nước | Bỏ hẳn `elongated neck`. Khóa: `natural balanced neck and body proportions, graceful upright posture` |
| **16** | **Mất chân, nhân vật bị "chôn" nửa người trong bệ đá/giếng đá tròn** | `standing on a miniature [balcony/bridge/platform]` đi cùng `Medium shot` mà thiếu mô tả quần/giày | `Medium shot` cắt ngang eo đấm nhau với lệnh `standing on`; từ `miniature` ép ban công co lại thành chậu tròn quanh eo | Nếu muốn thấy chân: Dùng `Full-body shot / Cowboy shot` + `tailored wool trousers, leather boots`. Nếu Medium shot: Dùng `standing behind an open waist-high stone railing` |
| **17** | **Trượt sang người thật 100% ở nhân vật nữ trẻ / thợ thủ công** | Thiếu `crafted as a tactile handcrafted claymation figure`, tả kiểu tóc người thật (`neat low bun`), tả nặn đồ đất sét | AI có thiên kiến "gái trẻ đẹp" tự động vẽ người thật; từ `clay` bị hút hết vào món đồ gốm đang nặn thay vì gán cho nhân vật | Bắt buộc đưa `crafted as a tactile handcrafted claymation figure, stylized character design` lên đầu câu; dùng `stylized hair sculpted from unspun wool roving`; khóa da: `painted clay finish, zero photorealistic skin texture` |
| **18** | **Bàn tay người thật khổng lồ cầm con chim/đồ chơi len tí hon (Bẫy ảnh Etsy/Pinterest)** | Tả cận cảnh bàn tay trơ trọi: `Close-up, the hands of a 65-year-old [person]` đi cùng `needle-felted animal` | AI kéo dữ liệu ảnh thợ thủ công người thật chụp macro sản phẩm len tí hon trên tay; tự động thêm tay áo len đan (`chunky knit sleeve`) | Tránh cận cảnh bàn tay trơ trọi; dùng góc `Over-the-shoulder medium-close shot of a stylized claymation character...`. Nếu bắt buộc chụp cận tay: phải định danh `the miniature clay hands of a handcrafted claymation figure, zero human skin pores, wearing tailored tweed coat sleeve` |
| **19** | **Hội chứng Gulliver / Người khổng lồ bước lên đồ chơi (Người to, cầu/thuyền/nhà tí hon)** | Gắn chữ `miniature` trực tiếp vào công trình/vật thể tương tác: `miniature stone bridge`, `miniature boat`, `miniature balcony` | AI hiểu `miniature` là tính từ cục bộ của vật thể (biến cầu/thuyền thành đồ chơi mini), trong khi nhân vật được tả to lớn. Kết quả: người khổng lồ dẫm lên đồ chơi | Bỏ hẳn chữ `miniature` trước cầu, thuyền, nhà, ban công. Chữ `miniature` CHỈ nằm ở Suffix toàn cục. Tả công năng thực tế: `an arched stone footbridge in natural proportion spanning across the river` |
| **20** | **Khung hình ngột ngạt nhồi nhét (Horror Vacui) HOẶC u ám kiểu noir** | `cinematic`, `dark shadows`, `moody`, `crowded`, `cluttered`, `packed shelves`, quên điểm neo vàng nhỏ | AI sợ khoảng trống nên nhồi đầy đồ đạc li ti; từ `cinematic` kích hoạt bóng đổ đen kịt và sương mù u ám | Bắt buộc dùng Rule Thoáng: `generous negative space, airy breathable composition, bright natural morning sunlight, fresh cheerful color palette`. Luôn kèm một điểm neo vàng nhỏ tinh tế (~2-5%: cúc áo, ruy băng nhỏ, hoa dại). |

---

## 🎯 3. QUY TẮC BẤT BIẾN CHO PROMPT NHÂN VẬT

1. **Kiến trúc Đảo ngược Token (Chống trùng lặp Meta AI):** Mở đầu bằng danh tính cụ thể: `a tall slender [TUỔI]-year-old [QUỐC TỊCH] [NGHỀ NGHIỆP] with narrow oval face`.
2. **Khóa bản thể hoạt hình đất sét ngay vế đầu:** `crafted as a tactile handcrafted claymation figure, stylized character design with gentle exaggerated features`.
3. **Khóa trục dáng thanh mảnh & Da đào ấm mịn màng:** `natural balanced proportions, graceful upright posture, warm peach-toned matte painted clay finish, zero craggy wrinkles, zero photorealistic skin texture`.
4. **Khóa phục trang may đo (CẤM ĐẤT SÉT & CẤM LEN ĐAN TO SỢI):** `wearing tailored woven linen shirt / tailored tweed waistcoat / corduroy jacket / tailored wool trousers` (Tuyệt đối không dùng `chunky knit`, `cable sweater`, `yarn loops`, `crochet`). Luôn có một điểm neo vàng nhỏ tinh tế (`subtle mustard button / small yellow ribbon / tiny wildflower`).
5. **Khóa tóc chống hói 100% cho người già:** `full thick head of wavy silver wool hair completely covering the scalp with zero baldness` HOẶC đội `vintage wool tweed flat cap / newsboy cap`.

---

## 🌲 4. QUY TẮC BẤT BIẾN CHO ĐỒ VẬT & MÔI TRƯỜNG

1. **Rule Thoáng & Không gian mở:** Đa số cảnh là ngoài trời lộng gió hoặc mở toang cửa sổ panoramic nhìn ra ngoài bao la. Tối thiểu 40% diện tích là khoảng nghỉ thị giác (`generous negative space, airy composition`).
2. **Thiên nhiên 100% thật & Nắng tươi sáng:** `real flowing river water with natural ripples, real wisps of steam, bright natural morning sunlight, clear azure sky`. Cấm từ `cinematic`, cấm bóng đổ đen kịt.
3. **Gỗ thủ công chắc nịch (Không mục rỗng):** `hand-planed solid timber with visible grain`, `sturdy carved oak with subtle surface scratches and artisan tool marks`. CẤM dùng `weathered, aged, rustic`.
4. **Đồ gốm men nung:** `solid glazed ceramic pottery with smooth kiln finish`, `smooth glazed terracotta ceramic mug`.
5. **Sinh vật len nỉ sống động (Không làm tượng vô tri):** `lively fluffy needle-felted animals with bright curious eyes and playful organic movements`.

---

## 🏷️ 5. GLOBAL SUFFIX CHUẨN

Ghép vào cuối 100% prompt:
```text
clean daylight stop-motion diorama style, shot on 35mm lens at f/4, gentle organic focus falloff, clean subject separation --ar 16:9
```
*(Tuyệt đối không nhét `needle-felted`, `photorealistic`, `cinematic`, hay `hand-tooled` vào Suffix này).*
