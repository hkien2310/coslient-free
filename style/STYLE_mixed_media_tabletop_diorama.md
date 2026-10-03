# STYLE: Mixed-Media Tabletop Diorama
*Coslient Free · Plugin chất liệu (Stop-motion Sa bàn Đa chất liệu). Storyboard quyết định cảnh, góc, máy, giờ ([`visual_craft.md`](../craft/visual_craft.md)); file này quyết định cảnh đó được làm bằng gì. Cơ chế prompt: Rule 1–6 của [`IMAGE_AVOID_CASES.md`](./IMAGE_AVOID_CASES.md) và bảng bộ lọc kiểm duyệt vẫn áp dụng. Từ điển token ở cuối file này thay thế từ điển của style đất sét.*

Thế giới sa bàn thu nhỏ nghệ thuật: con rối làm thủ công với tỷ lệ người thật thanh thoát, trang phục len dạ nguyên khối ấm áp, đặt giữa thiên nhiên thật thu nhỏ (rêu, sỏi, cỏ khô), chụp macro với độ sâu trường ảnh mỏng (tilt-shift, bokeh).

---

## R1. Hai lớp thế giới
- **Lớp thủ công (Handmade):** người, thú, nhà cửa, xe cộ, đồ vật. Làm từ vật liệu thủ công mộc mạc: len nỉ xù sợi (`needle-felted`), gỗ chạm khắc mờ (`carved wood`), vải len dệt nguyên tấm, dây đay, kim loại đồng/thiếc.
- **Lớp thật (Realistic Nature):** mặt đất sa bàn (rêu thật `real moss`, sỏi đá cuội `pebbles`, hoa cỏ khô `dried grass/heather`), nước thật, mây trời thật, hơi nước, khói thật. Thiên nhiên giữ chất liệu tự nhiên 100%, không làm bằng len hay đất sét.

## R2. Vụng nghệ thuật nhưng trang phục nguyên khối (Solid & Unpatched)
- **Vụng ở hình dáng nhân vật:** tỷ lệ mảnh khảnh tự nhiên, đường nét đẽo gọt mộc, mắt chấm sơn đơn sơ, dáng người hơi xiêu vẹo mang hồn dân gian (`naive folk-art`).
- **TUYỆT ĐỐI KHÔNG CHẮP VÁ TRANG PHỤC:** Quần áo là những mảng màu đơn sắc, nguyên khối liền tấm (`solid single-piece`, `seamless tailored cut`, `clean unpatched garment`). Thô nằm ở thớ len dạ xù tự nhiên (`boiled-wool`, `coarse knit`, `tweed`), không bao giờ là vải vụn chắp vá hay rách rưới.
- **Kỹ thuật chụp chuẩn studio macro:** Bố cục trung tâm, lấy nét chính xác vào chủ thể, tiền cảnh và hậu cảnh tan biến vào hiệu ứng bokeh mềm mại (`shallow depth of field`, `tilt-shift`, `soft warm bokeh`).

## R3. Khối nhân vật (Character Block)
- **Thứ tự:** danh tính → neo sa bàn → tỷ lệ người → mặt mũi tối giản → tóc/râu len thô → trang phục nguyên khối.
  - Danh tính: `[tuổi]-year-old [quốc tịch] [giới] [nghề]`.
  - Neo: `as a handmade miniature figure`. Nhiều người: `both/all as handmade miniature figures`.
  - Tỷ lệ: `tall slender natural human proportions, small head, long thin limbs`.
  - Mặt: `hand-painted figurine face with simple features` (mũi nêm, mắt chấm nhỏ, không tả nếp nhăn/giải phẫu).
  - Tóc, râu: `raw wool [màu]` (sợi len thô tự nhiên).
  - Áo: `solid [màu] [chất liệu] with a clean simple tailored cut` (ví dụ: `solid mustard-yellow felted wool overcoat`, `terracotta ribbed wool knit sweater`, `charcoal tailored tweed trousers`).
- **Thú cưng đồng hành:** `a needle-felted [loài/màu] dog/hound/cat`. Thú có hồn, đôi khi mặc áo len nhỏ liền mảnh (`single-piece knit vest`).
- Cảm xúc thể hiện qua cử chỉ và dáng người (cúi đầu, tựa vai, ngắm trời, vuốt ve chú chó), không phụ thuộc vào biểu cảm cơ mặt.

## R4. Ràng buộc lên storyboard
Ràng buộc này thắng các luật chung về khung hình khi áp dụng style này:
- **Cỡ cảnh:** Chỉ từ **trung-rộng (medium-wide, thấy toàn thân)** tới **cực rộng (extreme wide)**. Tuyệt đối không close-up/portrait (tránh làm lộ vụng kỹ thuật).
- **Góc máy:** Ưu tiên **máy đặt sát mặt đất ngang tầm sa bàn (`low ground-level shot`)**. Cảnh toàn dùng `extreme wide high-angle shot`. Không dùng top-down 90°.
- **Chủ thể ở trung tâm:** Vùng rìa nhòe tilt-shift, khoảng trống rộng mở xung quanh (`open uncluttered foreground/space`).
- **Phá tỷ lệ mộc mạc (Folk Surrealism):** Cho phép các chi tiết bất thường xuất hiện tự nhiên không cần giải thích (ví dụ: chú chó to gấp đôi người, đoàn tàu nhỏ bằng ấm trà, quả bí làm nhà, cá voi vải trôi trên mây).

## R5. Khe bắt buộc trong prompt
1. **Chất thơ bay lơ lửng trong không khí:** Mỗi khung hình bắt buộc có một yếu tố chuyển động nhẹ: hạt bụi nắng (`golden dust motes`), cánh hoa đào/thạch nam (`drifting petals`), bồ công anh (`dandelion fluff`), hơi nước thật (`real wisps of steam`), đom đóm (`fireflies`), hoặc tàn lửa (`floating embers`).
2. **Điểm nhấn màu ấm (Warm Color Anchor):** Một mảng màu ấm áp nguyên khối (mù tạt `mustard-yellow`, cam gạch `terracotta`, đỏ gỉ `rust-red`, hoặc ánh đèn bão `amber lantern glow`).

## R6. Ánh sáng & Bầu không khí
Tôn vinh chất liệu tự nhiên qua ánh sáng dịu, có hướng ven sáng (rim light) làm nổi bật sợi len xù:
- Sương sớm: `soft misty dawn light`.
- Nắng ban ngày: `clear natural daylight`.
- Chiều tà ngược sáng: `warm low golden-hour backlight`.
- Đêm tối: `blue dusk with warm glowing amber lamps`.

## R7. Công thức lắp Prompt & Suffix
```text
[Cỡ cảnh & Góc máy low ground-level], [Khối nhân vật tỷ lệ người thật + Áo nguyên khối solid/seamless] [Hành động giàu cảm xúc với thú cưng/cảnh vật], [Bối cảnh sa bàn: rêu thật, sỏi, gỗ], [Khe bắt buộc: vật thể bay lơ lửng], [Ánh sáng], handcrafted mixed-media tabletop diorama, macro miniature photography, tilt-shift, very shallow depth of field, sharp focus on the central subject, soft bokeh --ar 16:9
```

**Suffix cố định:**
`handcrafted mixed-media tabletop diorama, macro miniature photography, tilt-shift, very shallow depth of field, sharp focus on the central subject, soft bokeh --ar 16:9`

---

## Từ điển token cấm & thay thế (Avoid Token Dictionary)

| Token BỊ CẤM | Lý do (Model hiểu lệch) | Dùng thay thế |
|---|---|---|
| `patchwork`, `patched`, `scraps`, `rags`, `stitched sacks` | Kéo ra quần áo chắp vá, rách rưới, cái bang | `solid`, `seamless`, `single-piece`, `clean simple tailored cut` |
| `whatever was at hand`, `lopsided clothes` | Kéo ra hình dạng quần áo méo mó, nhăn nheo | `solid felted wool`, `coarse woven wool` |
| `claymation`, `clay`, `plasticine`, `ceramic skin` | Kéo ra hoạt hình 3D đất sét bóng bẩy | `handmade miniature figure`, `needle-felted` |
| `cute`, `chibi`, `cartoon`, `doll`, `puppet` | Kéo ra búp bê đầu to mắt tròn vô hồn | `tall slender natural human proportions` |
| `photorealistic human`, `detailed skin`, `pores`, `wrinkles` | Kéo ra mặt người thật kinh dị | `hand-painted figurine face with simple features` |
| `close-up`, `extreme close-up`, `macro portrait` | Kéo góc quá sát làm vỡ chất liệu | `medium-wide low ground-level shot` |
| `plastic`, `resin`, `shiny`, `glossy` | Kéo ra đồ chơi nhựa công nghiệp | `matte carved wood`, `raw wool`, `coarse linen` |
| `cinematic lighting`, `dark shadows`, `noir` | Kéo ra độ tương phản gắt, mất chất mộc | `warm low golden-hour backlight`, `soft diffused light` |
