# STYLE: Mixed-Media Tabletop Diorama
*Coslient Free · Plugin chất liệu. Cách viết prompt và đa dạng cảnh: [`visual_craft.md`](../craft/visual_craft.md). Bẫy từ khóa: Rule 1–6 và bảng kiểm duyệt của [`IMAGE_AVOID_CASES.md`](./IMAGE_AVOID_CASES.md) (từ điển trong đó viết cho clay, dùng từ điển cuối file này thay).*

Con rối làm tay đa chất liệu đặt giữa thiên nhiên thật thu nhỏ, chụp macro tilt-shift. Kỳ lạ, duyên dáng, thô mộc và vẫn đẹp. Kẻ thù duy nhất là bóng bẩy, hoàn hảo.

## 1. Hai lớp thế giới
- **Làm tay:** người, thú, nhà, xe, đồ vật. Xoay vòng gỗ, giấy bồi, vải lanh, dạ, da, dây đay, len, thiếc, đồng. Len không phủ cả người; hai nhân vật cạnh nhau không dùng cùng bộ chất liệu.
- **Thật:** rêu, sỏi, cỏ khô, hoa dại, nước, trời, khói, núi xa. Không làm bằng len.

## 2. Khối nhân vật
Mỗi lỗi hay gặp có đúng một cụm neo. Ngoài cụm neo, không tả thêm hình dáng. Không tả mắt, mũi, miệng (Meta tự vẽ cách điệu).

```text
a [tuổi]-year-old [giới] [nghề] as a stylized whimsical handmade puppet, slender body, slim limbs, small matte [hình đầu] head, full thick head of [màu] [chất liệu] hair, loose-fitting single-piece [màu] [vải mềm] knee-length [món áo] hanging in soft folds, visible slim legs in trousers and small boots
```
- **Hình đầu:** mỗi nhân vật một từ xoay vòng: `narrow oval` · `broad round` · `pear-shaped` · `squarish` · `heart-shaped`. Nhân vật đứng cạnh nhau không trùng hình. Có thể thay tóc bằng mũ (vải, nỉ, nón rơm) để đổi silhouette.
- **Chân:** áo luôn ghi `knee-length` và chân ghi `visible slim legs … boots`, nếu không áo dài che mất chân. Cảnh trung dùng `full-body`, không `medium` (bị cắt ngang).
- **Tóc/râu/lông:** chất gì cũng được (sợi, len, dây, cỏ khô) miễn đọc ra là tóc. Luôn có tóc hoặc mũ, tránh đầu hói.
- **Áo:** vải mềm rủ được (`linen`, `felt`, `flannel`, `soft leather`, `tweed`). Không vải cứng.
- **Tay:** `simple rounded mitten-shaped hands` nếu cận. Không cận chỉ có tay (ra đôi găng nằm trên bàn); cận vào đồ vật, nhân vật ở xa hoặc mờ.
- **Thú:** `a [chất] [loài]` (`twine-wrapped`, `felted wool`, `shaggy mohair`), đổi chất giữa các con.
- Cảm xúc ở hành động, không ở nét mặt. Nét nhận diện thêm tối đa một (kính, mũ, râu).

## 3. Khung hình
- Phần lớn từ trung tới cực rộng. Cận thỉnh thoảng để nhấn. Cấm `extreme close-up`, `macro portrait`, top-down 90°.
- Nền mờ hẳn khi nhấn nhân vật: `very shallow depth of field, soft bokeh`. Nền đọc được khi kể bối cảnh: `moderate depth of field, background softly readable`.
- Phá tỷ lệ được dùng, không giải thích.

## 4. Màu và ánh sáng
- Một mảng màu nhấn ấm (mù tạt, đất nung, đỏ gỉ, hổ phách) trên nền tông đất.
- Thứ lơ lửng (bụi, cánh hoa, hơi nước, đom đóm, tuyết) chỉ khi cảnh có lý do.
- Ánh sáng có hướng, có viền sáng: `soft misty dawn light` · `clear natural daylight` · `warm low golden-hour backlight` · `blue dusk with warm glowing amber lamps`.

## 5. Công thức & Suffix
```text
[Cỡ + góc], [khối nhân vật], [hành động], [bối cảnh], [thứ lơ lửng nếu có], [màu nhấn nếu thiếu], [ánh sáng], [độ sâu trường ảnh], [suffix]
```
**Suffix:** `handcrafted mixed-media tabletop diorama, visible handmade textures, macro miniature photography, tilt-shift --ar 16:9`

## Từ điển token
| Token | Model hiểu thành | Dùng thay |
|---|---|---|
| Tả mũi, miệng, nếp mặt, `crude`, `chisel marks` | Pinocchio, mặt yêu tinh | Chỉ dùng cụm neo |
| `chubby`, `round`, `plump`, `short`, `stout`, `cute`, `chibi`, `doll` | Lùn tròn, búp bê | `slender body, slim limbs` |
| `figurine`, `realistic`, `detailed face` | Mô hình người thật | `stylized whimsical handmade puppet` |
| `wool`, `knit` cho cả người | Cả người thành đồ len | Len đúng một bộ phận |
| `clean`, `seamless`, `polished`, `plastic`, `resin`, `glossy` | Đồ công nghiệp, nhựa | Tên chất liệu thật |
| `patchwork`, `patched`, `rags`, `whatever was at hand` | Chắp vá, rách | Chỉ ghi chất + màu |
| `jointed`, `carved wooden hands`, `waxed canvas`, `stiff`, `winding` | Tay hình nộm, áo gãy ở khuỷu | `loose-fitting … soft folds`, `mitten-shaped hands`, `holding` |
| `elongated`, `long thin limbs` | Người que, đồ bó sát | `slender body, slim limbs` |
| `claymation`, `clay` | Đất sét bóng | `handmade puppet` |
| `cinematic lighting`, `noir` | Tương phản gắt | Tên giờ ở mục 4 |
