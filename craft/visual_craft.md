# 🎬 VISUAL CRAFT — Storyboard & lắp prompt
v12.0 — Ponytail Edition

> Storyboard quyết định video trông thế nào. Style là plugin chất liệu: đổi file style, storyboard vẫn chạy. `image.txt` chỉ là lắp storyboard với style.

**Ba tầng, không chồng việc:**
- **Storyboard** (`4-storyboard.md`, luật ở file này): ai, ở đâu, làm gì, cỡ cảnh, góc, chuyển động máy, giờ, thời lượng, chuyển cảnh.
- **Style** (`style/STYLE_*.md`): chất liệu, khối mô tả nhân vật, khe bắt buộc, chất ánh sáng, suffix, ràng buộc của style lên khung hình.
- **Cơ chế prompt** ([`IMAGE_AVOID_CASES.md`](../style/IMAGE_AVOID_CASES.md)): cách model ảnh đọc chữ.

---

## 1. Đầu vào → Đầu ra
**Đầu vào:** `1-idea.md` (không gian, cảm xúc, móc neo) · `2-music.md` (cấu trúc, nhạc cụ) · `3-lyrics.txt` · `timestamps.txt` · `characters.txt` (nếu có) · storyboard của video liền trước · ràng buộc khung hình của style đang dùng.

**Đầu ra:** `4-storyboard.md`, tiếng Việt.
```text
Ý chính: [một câu: video này kể gì]
Trục: [...] · Điểm nhìn: [...] · Khép: [vòng | mở] · Lớp: [kể chuyện | kể chuyện + người chơi nhạc] · Nhân vật: [@tên… | không]
Nơi chốn: [nơi chính] + [nơi phụ]
Motif: [vật hoặc hành động lặp lại]
Sync: [giây · sự kiện nhạc] …

## Chuỗi A · [đoạn bài] · [giờ]
| # | Giây | Cỡ · Góc · Máy | Ai làm gì, ở đâu | Chuyển → | Bài |
```
- **Máy:** chuyển động máy trong clip (tĩnh, dolly, parallax, pedestal, orbit). Cột này và cột hành động dùng thẳng cho `prompt-animate.txt`.
- **Chuyển →:** cách cảnh này nối sang cảnh sau.
- **Bài:** `khớp lời "..."`, `khớp cảm xúc`, hoặc `sync`.

## 2. Biến số — chống 10 video như 1
Phần đầu chốt 5 lựa chọn, ít nhất 2 cái khác video liền trước:
- **Trục thời gian:** video trải qua bao lâu, từ một khoảnh khắc tới nhiều năm.
- **Điểm nhìn:** theo một người, theo nhiều người cùng một nơi, hoặc chính nơi chốn làm nhân vật.
- **Khép:** cảnh cuối quay về cảnh đầu (vòng) hoặc dừng ở chỗ mới (mở).
- **Lớp:** chỉ kể chuyện, hoặc thêm một người chơi nhạc trong thế giới của video (đàn bên hiên, hát khi làm việc).
- **Nhân vật xuyên suốt:** có hoặc không.

## 3. Luật storyboard

### Nhịp
- Mỗi cảnh mặc định 5 giây, dao động 3–8 giây. Dưới 3 giây người xem chưa kịp đọc hình; trên 8 giây clip AI không render được.
- Tổng các cảnh của một đoạn bằng đúng độ dài đoạn đó. Số cảnh suy ra từ đây, không đặt trước.
- **Sync point:** liệt kê trước khi chia cảnh. Lấy từ `timestamps.txt` (đầu mỗi đoạn, khoảng trống giữa câu là đoạn không lời) và `2-music.md` (nhạc cụ vào, nhạc lặng, đổi tông, nốt cuối). Sự kiện nhạc không có trong file thì người dùng bổ sung lúc duyệt.
- **Thứ bậc cắt:** mỗi sync point có một sự kiện hình rõ (cắt, đổi cỡ mạnh, đổi giờ, lộ ra cảnh mới). Ngoài sync point thì cắt ở đầu câu hát hoặc giữa động tác, không cắt đều theo phách. Cắt đúng phách mọi chỗ thì các điểm quan trọng mất lực.
- **Năng lượng nhạc:** nhạc thưa thì cảnh dài, rộng, ít người, máy tĩnh hoặc rất chậm; cao trào thì cảnh ngắn, ấm nhất, đầy đủ nhất, máy chuyển động; đoạn lắng thì dài lại, vắng lại, đổi kiểu máy.
- Mỗi đoạn bài là một hoặc vài chuỗi. Chuỗi không vắt qua chỗ nhạc đổi đoạn.

### Cấu trúc MV
- **Điệp khúc lặp hình:** mỗi lần điệp khúc quay lại cùng nơi chính và cùng kiểu khung, nhưng đổi một yếu tố (giờ, người, cỡ cảnh). Người xem nhận ra điệp khúc bằng mắt như bằng tai.
- **Điệp khúc cuối** là bản đầy đủ nhất: ấm nhất, gom đủ nhân vật, motif và nơi chốn của video, chứa **hero shot**, tức cảnh đắt nhất video.
- **Motif:** một vật hoặc hành động xuất hiện ở đầu, giữa và cuối, mỗi lần ở trạng thái khác. Có thể trùng với khe bắt buộc của style.
- **Đoạn không lời** (intro, solo, outro) dài trên 15 giây phải có một sự kiện: lộ ra nơi mới, motif được trả lời, hoặc một hành động có kết quả. Chỉ có môi trường thì người xem bỏ đi. Có lớp người chơi nhạc thì người đó xuất hiện ở đây.
- **Bridge:** đổi một thứ lớn (giờ, nơi phụ, kiểu máy) để mắt cũng thấy bài vừa rẽ hướng.
- **Outro:** phần thưởng cuối (khép vòng, motif lần cuối) đặt ngay đầu outro. Khoảng 20 giây cuối là một khung rộng ít đổi, chừa chỗ cho end screen: các cảnh ở đây giữ cùng góc, nối bằng chuyển động máy liên tục.
- **Nơi chốn:** nơi chính là không gian thoáng ngoài trời hoặc nửa ngoài trời (hiên, sân, bến, đồi, đường làng), theo Rule Thoáng của `idea_craft.md`. Trong nhà chỉ là nơi phụ. Ít nhất một nửa số cảnh ở ngoài trời (tính cả hiên). Điệp khúc về nơi chính.
- Hai chuỗi liền nhau không được cùng nơi và cùng giờ.

### Chuyển cảnh
Mỗi lần cắt là một trong bốn kiểu:
- **Nối tiếp:** cảnh sau là bước kế tiếp trong cùng không gian và thời gian.
- **Cut on action:** động tác bắt đầu ở cảnh trước, cảnh sau làm tiếp ở cỡ hoặc góc khác.
- **Match cut:** hai cảnh khác nơi hoặc khác giờ nhưng trùng hình khối, hướng chuyển động hoặc vị trí trong khung.
- **Cắt thẳng:** chỉ ở chỗ nhạc đổi đoạn.

Luật:
- Trong chuỗi chỉ dùng nối tiếp và cut on action. Giữa hai chuỗi ưu tiên match cut.
- Mỗi lần cắt đổi cỡ cảnh, và đổi thêm độ cao hoặc hướng. Cùng cỡ chỉ được khi đổi chủ thể (cảnh đối đáp: người này → người kia) hoặc là match cut (giữ nguyên khung, vì nơi hoặc giờ đã đổi).
- Một bố cục (cùng cỡ, cùng góc, cùng loại hành động) không dùng lại ở chỗ khác trong video, trừ khung điệp khúc và cảnh khép vòng.
- Mỗi clip chỉ chứa một chuyển động liên tục. Đổi tư thế hay đổi trạng thái (đứng dậy, cửa đã mở, đã tới nơi) xảy ra ở điểm cắt, không xảy ra trong clip.
- Trong chuỗi giữ hướng di chuyển và hướng nhìn (không vượt trục 180°), giữ giờ và trang phục.

### Khung hình
- **Góc = độ cao × hướng.** Độ cao: eye-level · low-angle ngước lên · high-angle bird's-eye nhìn xuống · top-down 90° (không có trục hướng). Hướng: chính diện · ba phần tư 45° · ngang cạnh · qua vai/POV.
- **Cỡ cảnh:** extreme wide tới close-up, trong giới hạn style cho phép.
- Không quá 2 cảnh liền nhau cùng độ cao. Mỗi chuỗi có ít nhất 2 độ cao. Cả video dùng đủ 4 độ cao và 4 hướng, trừ thứ style đang dùng cấm.
- Mô tả trong cảnh chỉ gồm thứ góc máy thấy được (Rule 1 trong AVOID).

### Nội dung
- **Luôn có thứ đang chuyển động:** nhân vật đang làm việc gì đó, hoặc môi trường đang động (gió, nước, khói, hơi nước, chim, tàu, lửa đèn). Nhân vật đứng lặng thì môi trường phải động. Chuyển động là quá trình kéo dài được vài giây, không phải khoảnh khắc tức thời.
- **Hơi ấm con người:** không có cảnh hoang vắng. Khoảng 80% cảnh có người. Cảnh không người phải có dấu vết người đang sống (cửa sổ sáng đèn, khói bếp, đồ dùng dở, thú nuôi). Cảnh rộng có người thì người đó có bạn đồng hành (người hoặc thú).
- **Nhân vật chính của khung:** ai tham gia hành động chính thì tả riêng. Người làm nền tả gộp thành một cụm.
- **Giờ** đi theo cung cảm xúc của bài, không mặc định ban ngày.
- **Bám bài:** hình kể điều lời chưa nói: chuyện xảy ra giữa các câu hát, hệ quả của nó, hoặc một góc khác của cùng khoảnh khắc. Lời đã nói thì hình không nói lại cùng lúc, vì minh họa từng câu biến MV thành karaoke. Mỗi đoạn bài tối đa một cảnh khớp lời, đặt ở câu đắt nhất hoặc ở sync point.
- Mỗi móc neo giác quan trong idea có ít nhất một cảnh.
- **3 giây đầu** có người và một điều chưa được giải thích. Cảnh không gian không người lùi xuống sau.
- Ngoài nhân vật xuyên suốt, trang phục, loài vật, bối cảnh đổi theo lời bài.

### Nhân vật
- **Nhân vật chính → `characters.txt`:** ai (người hoặc thú) xuất hiện nhận ra được ở từ 2 chuỗi trở lên. Tiêu chí là người xem có cần nhận ra đây vẫn là người đó không. Nạp lên Meta AI một lần, prompt gọi `@tên`.
- **Nhân vật phụ → tả thẳng trong prompt:** xuất hiện trong một chuỗi, hoặc chỉ làm nền. Tả bằng khối nhân vật của style, ngắn gọn, không vào file.
- **Tên:** một từ, viết thường, không trùng và không gần giống tên ở các project trước.
- **Định dạng khối:**
```text
@tên
FIXED: [khối nhân vật đầy đủ theo style: danh tính, neo, nét nhận diện, tỷ lệ, da, tóc]
DEFAULT OUTFIT: [trang phục mặc định]
[TÊN BIẾN THỂ] OUTFIT: [trang phục của chuỗi khác: ký ức, mùa khác…]
```
- Prompt dùng trang phục mặc định thì chỉ cần `@tên`. Khác mặc định thì ghi rõ ngay sau tên: `@tên in [trang phục]`.

## 4. Lắp `image.txt`
- Mỗi hàng storyboard thành một prompt tiếng Anh, cùng thứ tự.
- Thứ tự lắp: `[cỡ + góc]` → `[@tên hoặc khối nhân vật của style]` → `[hành động]` → `[bối cảnh trong tầm nhìn]` → `[khe bắt buộc của style]` → `[giờ, dịch theo chất ánh sáng của style]` → `[suffix của style]`.
- `@tên` thay cả khối nhân vật. Ảnh ra người thật thì thêm neo chất liệu của style ngay sau `@tên`.
- Mỗi prompt một dòng, giữa hai prompt đúng một dòng trống. Không `--no`.

## 5. Kiểm tra
**Storyboard:**
- [ ] Ít nhất 2/5 biến số khác video trước.
- [ ] Mọi cảnh 3–8 giây, tổng mỗi đoạn khớp độ dài đoạn.
- [ ] Mọi sync point có sự kiện hình.
- [ ] Điệp khúc lặp hình có biến tấu; hero shot nằm ở điệp khúc cuối; motif có mặt ở đầu, giữa, cuối.
- [ ] Mỗi lần cắt có kiểu chuyển cảnh khớp với hình (nhảy giờ/nơi không phải nối tiếp; cut on action thì động tác thấy ở cả hai cảnh); có đổi cỡ, trừ đối đáp và match cut; cắt thẳng chỉ ở chỗ đổi đoạn.
- [ ] Không bố cục nào lặp lại ngoài khung điệp khúc và cảnh khép vòng.
- [ ] Không clip nào chứa đổi tư thế hay đổi trạng thái.
- [ ] Mỗi cảnh có nguồn chuyển động.
- [ ] Không quá 2 cảnh liền nhau cùng độ cao; mỗi chuỗi có ít nhất 2 độ cao.
- [ ] Ít nhất một nửa số cảnh ở ngoài trời; hai chuỗi liền nhau không cùng nơi và cùng giờ.
- [ ] Mỗi đoạn bài tối đa một cảnh khớp lời.
- [ ] 3 giây đầu có người và một câu hỏi; đoạn không lời dài trên 15 giây có sự kiện.

**`image.txt`:**
- [ ] Số prompt bằng số cảnh.
- [ ] Đủ 6 rule và từ điển trong AVOID.
- [ ] Đủ khe bắt buộc và ràng buộc của style.
