# VISUAL CRAFT — NGHỆ THUẬT DÀN DỰNG CHUỖI ẢNH

> **Phân định ranh giới cốt lõi:**
> - **Style (`style/STYLE_*.md`):** Quy định *chất liệu & cách render của từng pixel* (da mịn không gỗ, chân không khớp, không len, ánh sáng ấm). Đó là "luật vẽ 1 bức ảnh".
> - **Visual Craft (file này):** Quy định *sự chuyển động, nhịp điệu, câu chuyện và sự đa dạng giữa 50–70 bức ảnh*. Làm sao để chuỗi ảnh không bao giờ gây chán hay đơ cứng.

Viết thẳng prompt vào `image.txt`. Số lượng prompt tùy theo độ dài bài hát (trung bình 45–65 prompts cho bài 3–4 phút). Bẫy từ khóa tra cứu tại `style/IMAGE_AVOID_CASES.md`.

---

## 1. Nguyên Tắc Tranh Khảm Lát Cắt (The Mosaic / Vignette Principle)
- **Mở rộng thế giới, không tịnh tiến tuyến tính:** Mỗi prompt là một lát cắt đời sống độc lập (vignette) của cả một thế giới thu nhỏ, không bị trói buộc vào hành trình tuyến tính (A $\rightarrow$ B $\rightarrow$ C) của một nhân vật duy nhất.
- **Tính tự thân của mỗi frame (Self-contained Micro-story):** Mỗi bức ảnh tự thân nó chứa đựng một câu chuyện nhỏ hoàn chỉnh (một khoảnh khắc dở dang, một góc sinh hoạt, một tương tác bất ngờ), biến video thành một hành trình khám phá thế giới phong phú thay vì bám đuổi 1 nhân vật đi bộ.
- **Tiêu chuẩn "Frame tự đứng vững" (Standalone Frame):** Khi tách bất kỳ bức ảnh nào ra khỏi video, người xem vẫn cảm nhận được trọn vẹn sức sống, cảm xúc và câu chuyện ẩn chứa bên trong mà không cần phải xem bức ảnh trước hay sau đó mới hiểu được.
- **Tự do tối đa cho phòng dựng Montage:** Khi mỗi ảnh là một lát cắt độc lập, phòng dựng có thể tự do xáo trộn, sắp đặt và tạo sự va chạm hình ảnh (juxtaposition) theo nhịp nhạc (`timestamps.txt`) mà không sợ bị đứt gãy mạch truyện hay ngược dòng thời gian.

### 💡 Bảng đối chiếu tư duy dàn dựng:

| Tiêu chí | ❌ Bẫy Tịnh Tiến Tuyến Tính (Linear Railroad) |  Tranh Khảm Lát Cắt Thế Giới (Mosaic Principle) |
|---|---|---|
| **Mạch hình ảnh** | Bám riết lấy 1 nhân vật: thức dậy $\rightarrow$ bước ra cửa $\rightarrow$ đi trên đường $\rightarrow$ lên đồi $\rightarrow$ ngắm hoàng hôn. | Mở rộng biên độ thế giới: thợ rèn gõ búa $\rightarrow$ chú mèo sưởi nắng $\rightarrow$ bà cụ nướng bánh $\rightarrow$ lũ trẻ thả thuyền giấy $\rightarrow$ đàn chim bay về tổ. |
| **Gắn kết với bài hát** | Minh họa thô kệch từng chữ trong lời hát như từ điển tranh. | Cộng hưởng không gian & cảm xúc: lời hát ngân lên một nốt êm đềm, hình ảnh đưa người xem chạm vào một khoảnh khắc bình yên của thế giới. |
| **Cảm giác người xem** | Đơn điệu, dễ đoán, nhàm chán sau 15–20 giây đầu. | Bất ngờ, lôi cuốn, luôn tò mò muốn biết góc tiếp theo của thế giới này có gì kỳ diệu. |

---

## 2. Hệ Thống 7 Trục Đa Dạng Hóa (The 7 Diversity Axes)

Khi viết prompt thứ $N$, phải chủ động xoay vòng tối thiểu **3 trong 7 trục** so với prompt $N-1$:

### Trục 1 — Nhân vật & Số lượng:
- Xoay vòng linh hoạt: 1 người làm việc một mình $\leftrightarrow$ 2 người tương tác thân tình $\leftrightarrow$ Trẻ con/người già $\leftrightarrow$ Muông thú/thú cưng làm nhân vật chính $\leftrightarrow$ Hoàn toàn không có người (tĩnh vật/cảnh vật).
- Đa dạng tạng người theo 4 nhóm trong Style: Thợ đĩnh đạc (1:6) $\leftrightarrow$ Thanh mảnh cao ráo (1:6.5) $\leftrightarrow$ Cụ già phong sương $\leftrightarrow$ Trẻ nhỏ nhanh nhẹn (1:5.5).

### Trục 2 — Bối cảnh & Không gian (Ưu tiên ngoài trời):
- **Ưu tiên ngoại thất khoáng đạt:** Tận dụng tối đa không gian ngoài trời rộng mở (sân phơi, bờ suối, triền đồi, mỏm đá, cầu uốn lượn) gắn với hoạt động thực tế.
- **Nội thất phải mở toang:** Khi nhân vật ở trong xưởng nghề hay studio cá nhân, căn phòng luôn có vòm kính panorama hoặc ban công mở toang nhìn ra cảnh quan hùng vĩ bên ngoài. Không bao giờ nhốt nhân vật vào phòng kín tối tăm.

### Trục 3 — Thông số máy ảnh & Góc quay:
- **Cỡ cảnh:** Cận cảnh macro (đôi bàn tay, đồ vật) $\leftrightarrow$ Trung cảnh (nhân vật thao tác) $\leftrightarrow$ Viễn cảnh (đại cảnh thiên nhiên/thị trấn).
- **Góc máy:** Ngước nhìn lên tôn dáng (`low-angle`) $\leftrightarrow$ Ngang tầm mắt (`eye-level`) $\leftrightarrow$ Nhìn từ trên cao xuống (`high-angle bird's-eye diorama view`).
- **Khẩu độ:** Luôn giữ `moderate depth of field, background softly readable` để hậu cảnh mờ êm dịu nhưng vẫn đọc rõ kiến trúc, tránh bẫy xóa phông nhòe nhoẹt của tilt-shift.

### Trục 4 — Hành vi vi mô & Khoảnh khắc lỡ cỡ (Micro-actions):
- Bắt lấy những khoảnh khắc sinh hoạt tự nhiên, dở dang thay vì tạo dáng chụp ảnh:
  + Người thợ lấy mu bàn tay quệt mồ hôi, xỏ sợi chỉ qua kim, kiễng chân với hũ gia vị trên kệ cao.
  + Chú mèo giẫm lên góc bản vẽ, chim sẻ mổ vụn bánh trên mũi giày, chú chó thò mũi ngửi vạt tạp dề dính bột.
  + Bột mì bay trong vệt nắng, giọt trà vừa rỏ xuống mặt tách, cuộn len đang lăn dở trên sàn.

### Trục 5 — Tiêu điểm thị giác (Subject Hierarchy):
Ai hoặc cái gì là "nhân vật chính" của frame ảnh này?
- **Gương mặt:** Thần thái trầm tĩnh, an nhiên, ánh mắt có hồn (không cười đông cứng).
- **Bộ phận cơ thể:** Đôi bàn tay gân guốc đang chuốt gỗ, nắn gốm, xâu kim (không thấy mặt).
- **Đồ vật có linh hồn (Still-life with Soul):** Chiếc ghế trống có vệt nắng rọi qua, đôi ủng để góc cửa, chiếc đàn cũ (người chỉ là bóng mờ lướt qua).
- **Thiên nhiên bao la (Negative Space):** Cả khung hình là triền cỏ rêu và bầu trời mở, con người chỉ là một chấm nhỏ thanh thản ở góc 1/3.

### Trục 6 — Dòng chảy thời gian & Thời tiết (Temporal Arc):
Cả video phải là một hành trình ánh sáng và thời gian chuyển động, không đóng băng ở một thời điểm:
- **Khởi đầu:** Sáng sớm sương mai (`soft misty dawn light`), hơi lạnh, mở cánh cửa chớp.
- **Phát triển:** Nắng ngày trong trẻo (`clear warm natural daylight`), nhịp sống rộn ràng, bụi phấn hoa bay trong nắng.
- **Chuyển biến thời tiết:** Cơn mưa rào bất chợt vừa tạnh, mặt đá ướt bóng lấp lánh sương mai, gió lộng lay tà áo.
- **Lắng đọng & Trở về:** Hoàng hôn vàng mật (`warm low golden-hour backlight`) $\rightarrow$ Chạng vạng xanh lam (`blue dusk`) $\rightarrow$ Đèn lồng hổ phách bừng sáng trong các ô cửa sổ khi đêm xuống.

### Trục 7 — Đồng bộ nhịp động lực học bài nhạc (Musical Dynamics Sync):
- **Khúc dạo đầu / Verse (Tự sự, nhỏ nhẹ):** Cảnh hẹp, cận cảnh, chuyển động chậm, đồ vật riêng tư, nhịp thở êm đềm.
- **Khúc Điệp khúc / Chorus (Âm nhạc bùng nổ):** Lập tức bung ra **đại cảnh góc rộng (panoramic wide shot)**, gió thổi mạnh, không gian mở toang, bầy chim cất cánh, ánh sáng rực rỡ để thị giác bùng nổ cùng thính giác.
- **Khúc Bridge (Lắng đọng):** Dùng góc máy nhìn từ sau lưng (back-view), hình bóng ngược sáng (silhouette), hoặc cảnh tĩnh lặng không bóng người để tạo khoảng lặng cảm xúc.

---

## 3. Diệt Trừ 3 Bẫy Làm Video Bị Cứng

1. **Bẫy Ma-nơ-canh tạo dáng (Posing Mannequin):** Cấm tuyệt đối nhân vật chỉ đứng nhìn vào máy ảnh hoặc tạo dáng chụp ảnh lưu niệm. Nhân vật phải luôn đắm chìm trong công việc, vận động hoặc có tương tác tự nhiên với môi trường xung quanh.
2. **Bẫy Minh họa nghĩa đen (Literal Illustration):** Lời hát nhắc từ A thì prompt phải mở rộng thế giới xung quanh A (trước, sau, bên cạnh, ngoài cửa sổ), tuyệt đối không vẽ minh họa cơ học từng chữ một như cuốn từ điển tranh.
3. **Bẫy Đóng băng thời gian:** Cấm toàn bộ 50 ảnh đều có chung một ánh hoàng hôn tĩnh lặng. Phải có nhịp thở thời gian từ sáng sớm tới chiều muộn.

---

## 4. Quy Chuẩn Khung & Format Kỹ Thuật

- **Tỷ lệ sinh khí (Vitality Ratio):**
  + Tối thiểu 70% số ảnh có nhân vật chuyển động hoặc tương tác tình cảm.
  + Tối đa 10–15% cảnh tĩnh vật; không xếp 2 cảnh tĩnh vật liên tiếp.
- **Tần suất lặp lại:** Một đồ vật hoặc một góc bối cảnh cụ thể chỉ xuất hiện tối đa 2 lần trong cả video. Không 3 ảnh liên tiếp giống nhau ở cùng một trục.
- **Tâm điểm màu sắc:** Luôn có 1 điểm nhấn màu vàng mù tạt (`saffron mustard`) hoặc ánh hổ phách (`blazing warm amber`) để neo giữ nhận diện.
- **Format cho tool render:** Mỗi prompt một dòng, giữa hai prompt một dòng trống, không dùng `--no`, kết thúc bằng `--ar 16:9`. Suffix phong cách luôn đặt ở đầu prompt.
