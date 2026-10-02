# 🎬 STORYBOARD CRAFT — ĐƠN GIẢN & THỰC CHIẾN (PONYTAIL)
> *"Cảnh này là gì, rộng hay hẹp, tại sao, đem lại tác dụng gì, và chuyển cảnh Hard Cut thế nào để mắt người xem êm như ru."*

---

## 1. BẢN CHẤT CỦA STORYBOARD
Storyboard là danh sách các cảnh trôi theo nhịp bài hát.
* **ĐỊNH VỊ TÂM HỒN, KHÔNG MINH HỌA NGHĨA ĐEN:** Kịch bản phản ánh trạng thái tâm hồn (bình an, buông bỏ hối hả, kết nối). Tuyệt đối cấm bẫy minh họa nghĩa đen ("hát gì vẽ nấy" - hát tua-vít vẽ tua-vít, hát ngồi yên vẽ ngồi lì trên ghế).
* **LUẬT KHÔNG GIAN MỞ (OPEN HORIZON LAW):** Tối thiểu 70%–80% thời lượng là ngoại cảnh rộng lớn (biển, vách đá, bầu trời, đường đèo, bờ kè, quán cóc ngoài trời, đồng cỏ). Tuyệt đối cấm bẫy giam cầm trong phòng (Domestic Trap) và bẫy cô độc (Isolation Trap). Nội cảnh chỉ dùng khi cửa sổ mở toang ra đại dương hoặc khi có sự kết nối cộng đồng rực rỡ (hội bạn già cười vui, khiêu vũ).
* **POSTER ART ĐỘC BẢN:** Mỗi shot là một khung hình có bố cục mỹ thuật và chiều sâu cảm xúc, không chụp bừa bãi hay dựng slideshow cơ học.
* **HỆ THỐNG PLUGIN MỞ RỘNG (OPTIONAL PLUGINS):** Khi kịch bản cần chất thơ kỳ lạ hoặc viral hook, cắm thêm plugin tương ứng trong thư mục `craft/plugins/`:
  - [`plugin_surreal_whimsy.md`](./plugins/plugin_surreal_whimsy.md): Bơm 4 động cơ siêu thực vào 10%–20% số shot (ngồi cọc gỗ giữa biển, đọc báo ngâm chân dưới sóng, giường treo trên cây, xe Vespa vi vu mép vực).
* **Mỗi cảnh bắt buộc trả lời thẳng 4 câu hỏi thực chiến:**
  1. **Cảnh này là gì?** (Khung hình vẽ gì, chuyển động ra sao để đưa sang prompt).
  2. **Rộng hay hẹp?** (Cỡ cảnh: Toàn / Trung / Cận).
  3. **Tại sao & Đem lại tác dụng gì?** (Dụng ý cảm xúc: mở màn, sưởi ấm, lắng đọng, thư giãn...).
  4. **Chuyển cảnh từ cảnh trước thế nào? Có mượt mà chưa và TẠI SAO mượt?** (Vì video dùng **Hard Cut 100%**, phải chỉ rõ điểm neo mắt, hướng chuyển động hoặc ánh sáng nối tiếp. Cấm viết nịnh bợ hay qua loa).

---

## 2. QUY TẮC NHỊP CẮT & LOGIC HARD CUT CHUẨN ĐIỆN ẢNH

### 2.1 Nhịp cắt thời lượng
* **Điểm ngọt ~5.0 giây (3.5s – 5.5s):** Nhịp thở tự nhiên của mắt người xem.
* **Shot tĩnh lặng (6–8s):** Cho phép kéo dài ở Solo, Bridge, hoặc Outro (`[HOLD]` / `[STILLNESS]`).
* **Trần kỹ thuật AI:** Thời lượng mỗi shot **$\le 8.0\text{s}$**.
* **Mili-giây chỉ để tham khảo:** Lấy mốc từ `timestamps.txt` để không bị lệch bài hát. Dựng thực tế co kéo $\pm 0.5\text{s}$ theo nhạc.

### 2.2 Bộ kỹ thuật Hard Cut chuẩn Điện ảnh (Ưu tiên theo thứ tự độ mượt)
Video Coslient dùng **Hard Cut 100%** (cắt thẳng không hiệu ứng mờ nhòe lòe loẹt). Đẹp nhất và mượt nhất là dùng 3 kỹ thuật cắt kinh điển của điện ảnh, nếu không có chuyển động thì dùng logic ánh sáng/điểm nhìn:
1. **Cut on Action (Cắt trên chuyển động — Đẹp & Tự nhiên nhất):** Cắt ngay giữa một nhịp chuyển động đang diễn ra. Cảnh trước tay người bắt đầu với lấy tách trà $\to$ cảnh sau cắt cận cảnh bàn tay nhấc tách lên; cảnh trước bước chân chuẩn bị bước qua cửa $\to$ cảnh sau bước tiếp xuống bậc thềm đá. Mắt người xem mải đuổi theo hành động nên quên mất cú cắt.
2. **Match Cut (Cắt đồng dạng — Đẳng cấp & Giàu chất thơ):** Cắt nối 2 hình ảnh có sự tương đồng về hình khối, hướng chuyển động hoặc ý niệm. Ví dụ: Khói từ ống khói nhà gỗ $\to$ khói bốc lên từ tách trà nóng; bóng lưng chú chó nhìn ra biển $\to$ bóng lưng ông lão nhìn về phía chân trời; bánh xe lăn $\to$ cuộn len lăn trên thảm.
3. **Continuity Cut / Eye-Trace (Cắt nối tiếp dòng chảy & Điểm nhìn):** Trọng tâm thị giác mà mắt người xem vừa dừng lại ở cảnh trước (ví dụ ô cửa sổ góc 1/3 phải) chính là nơi chủ thể cảnh sau xuất hiện (chú mèo bên bậu cửa). Cấm bắt mắt người xem nhảy giật cục từ mép trái sang mép phải màn hình.
4. **Logic bổ trợ (Scale Ladder & Light Match):** Khi là shot tĩnh không có chuyển động để match, bắt buộc phải có logic bù đắp: Bước nhảy cỡ cảnh theo bậc thang (*Toàn $\to$ Vừa $\to$ Hẹp*) và đồng điệu về nhiệt độ màu ánh sáng (cùng tông nắng vàng ấm, không cắt đột ngột sang cảnh chói lòa hoặc tối đen).

---

## 3. BẢNG STORYBOARD CHUẨN (`storyboard.md`)

| Shot | Thời gian | Ca từ | Cỡ cảnh (Rộng/Hẹp) | Cảnh này là gì (→ image.txt) | Chuyển động (→ animation.txt) | Tại sao & Tác dụng gì | Chuyển cảnh từ shot trước (Hard Cut Logic) |
|:---:|:---|:---|:---|:---|:---|:---|:---|
| **01** | 00:00–00:04.60 (4.6s) | *[Intro]* | **Rộng (Toàn)** | Toàn cảnh ngôi làng mờ sương sớm, khói mỏng bốc lên từ mái nhà gỗ bên sườn đồi... | Camera tiến chậm nhẹ nhàng về phía ngôi làng... | Hook mở màn, thiết lập chốn bình yên tĩnh lặng, định hình không gian | *(Khởi đầu video - Mở màn êm ái)* |
| **02** | 00:04.60–00:09.20 (4.6s) | *[Intro]* | **Hẹp (Cận)** | Một chú mèo cam nằm vươn vai sưởi nắng bên bậu cửa sổ gỗ cũ đầy hoa dại... | Mèo cựa mình nhẹ nhàng, rèm thô lay khẽ... | Chi tiết đời thường ấm áp, tạo cảm giác thân thuộc, kéo người xem lại gần | **MƯỢT (Eye-Trace + Scale Ladder):** Ở Shot 01 mắt người xem tụ vào ô cửa sổ nhà gỗ ở góc 1/3 phải, Shot 02 cắt thẳng vào cận cảnh chú mèo đúng góc đó. Bước nhảy từ Rộng $\to$ Hẹp theo bậc thang, cùng tông nắng vàng nhạt nên êm mắt tuyệt đối. |
| **03** | 00:09.20–00:14.00 (4.8s) | *"Morning comes..."* | **Vừa (Trung)** | Một người thợ làm bánh kéo khay bánh mì nướng nóng hổi ra khỏi lò củi rực than hồng... | Khói bánh bốc lên, tay đặt khay bánh xuống bàn gỗ... | Khởi đầu ngày mới, gợi mùi vị và sinh khí lao động bình dị | **MƯỢT (Motion + Light Match):** Shot 02 rèm và mèo chuyển động êm dịu, Shot 03 tiếp nối nhịp đặt khay bánh êm ái. Ánh than hồng trong lò nướng ăn khớp với tông nắng ấm của cảnh trước, cỡ cảnh nâng từ Hẹp $\to$ Vừa tự nhiên. |

---

## 4. BỘ 3 NGUYÊN TẮC KỸ THUẬT AN TOÀN
1. **Không Lip-sync:** Không để nhân vật mấp máy môi hát theo lời ca.
2. **Không ép chụp cận mặt trực diện:** Càng ít soi mặt cận cảnh, AI gen càng đẹp và không bao giờ bị méo hay đơ.
3. **Cắt trên chuyển động (Cut on Action):** Cắt cảnh khi vật thể hoặc camera đang trong nhịp chuyển động êm, không cắt lúc chuyển động bị dừng khựng.
