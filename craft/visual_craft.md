# VISUAL CRAFT: NGHỆ THUẬT ĐẠO DIỄN STORYBOARD & CHUỖI KHUNG HÌNH (`character.md` & `storyboard.md`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` và `timestamps.txt` để thiết lập hồ sơ nhân vật `character.md` và đạo diễn bảng phân cảnh `storyboard.md` (ý niệm thị giác, đường cong năng lượng theo cấu trúc nhạc, tỷ lệ 70/30 cùng 4 động cơ thăng hoa, bố cục không gian, ma trận góc máy và luật đảo nhịp $N \to N+1$). Toàn bộ thông số chất ảnh, giải phẫu tạo hình chi tiết và khung câu lệnh tiếng Anh cho `character.md` / `image.txt` nằm độc lập tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. **Ưu tiên dùng khẳng định hơn phủ định:** Hướng dẫn trực tiếp những gì cần thiết kế, cần vẽ và cần đạt được bằng câu khẳng định rõ ràng. Chỉ liệt kê từ khóa cần tránh đối với các trường hợp lỗi kỹ thuật đặc thù của AI không thể xử lý bằng cách khác.
>   2. **Luôn Rule hóa thông tin (`Rule-First`) & Hạn chế tối đa thiên kiến liệt kê:** Khái quát hóa mọi ý tưởng thành quy tắc chung hoạt động cho mọi video và mọi bối cảnh. Hạn chế tối đa việc liệt kê danh sách sự vật, chủ đề hay sự kiện cụ thể (vì liệt kê chính là một dạng của `Use Case` gây thiên kiến lặp lại cho AI); chỉ nêu trường hợp cụ thể (`Use Case`) khi đó là ngoại lệ đặc biệt không thể làm khác.
>   3. **Ưu tiên thêm mới và làm giàu quy tắc, hạn chế tối đa việc xóa / mất dữ liệu:** Khi nâng cấp quy trình, luôn bảo toàn các quy tắc kỹ thuật, bố cục, động cơ sáng tạo và từ vựng cấu trúc đã đúc kết; chỉ chỉnh sửa cục bộ đúng chỗ cần thiết (`/ponytail`, `/humanizer`).

---

## 1. Quy trình đạo diễn `character.md` và `storyboard.md`

### Bước 1: Thiết lập `character.md` theo hai chế độ kể chuyện
Dựa vào chế độ đã chốt tại `1-idea.md`, lập file `character.md` trước khi chia cảnh (mẫu câu lệnh tiếng Anh quy định tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md)):
1. **Chế độ 1 (Kể chuyện cá nhân):**
   - `character.md` định nghĩa các nhân vật trung tâm xuyên suốt bằng mã `@Tên_nhân_vật`, kèm một câu lệnh tạo hình tham chiếu gốc (ví dụ mặc định) chuẩn stop-motion cho mỗi người. Khi đi vào mạch chuyện dài trong `storyboard.md` và `image.txt`, chỉ giữ cố định **vóc dáng hình thể** và **đường nét cấu trúc gương mặt nhận diện**; **biểu cảm nét mặt tuyệt đối không khóa cứng** mà phải biến chuyển tự nhiên theo cảm xúc từng cảnh, đồng thời **trang phục, kiểu tóc (nếu có) và phụ kiện có thể thay đổi linh hoạt** tùy theo diễn biến câu chuyện và từng prompt.
   - Khi kịch bản có thêm nhân vật phụ ngoài luồng hoặc đám đông cư dân trong không gian chung, mô tả trực tiếp ngoại hình của họ ngay trong dòng kịch bản của cảnh đó. Đan xen nhịp nhàng giữa cảnh có `@Tên_nhân_vật`, cảnh có nhân vật ngoài luồng và cảnh tĩnh vật (`B-roll`) theo mạch chuyện.
2. **Chế độ 2 (Ý niệm đa diện, 100% lát cắt độc lập):**
   - `character.md` ghi chú bài hát thuộc Chế độ 2, không có nhân vật cố định.
   - Toàn bộ 50 đến 70 cảnh trong `storyboard.md` là các lát cắt độc lập mở rộng ra nhiều con người, độ tuổi, nghề nghiệp và gia đình khác nhau cùng sống trong một đại địa điểm, được mô tả trực tiếp ở từng dòng lệnh. Khi lời hát lặp lại từ khóa hoặc điệp khúc, chuyển hóa cảm xúc câu hát sang những con người mới, tiểu bối cảnh mới và ý tưởng thị giác mới.

### Bước 2: Đạo diễn `storyboard.md` theo cấu trúc âm nhạc
`storyboard.md` tập trung vào ý niệm thị giác, ẩn dụ cảm xúc từ lời hát, động cơ thăng hoa, đường cong năng lượng, móc nối chuyển cảnh, cỡ cảnh, góc máy và bảng màu của từng khung hình:
1. **Intro (0:00 đến 0:15, Cú chặn thị giác 5 giây đầu):** Cảnh 01 (00:00 đến 00:05) mở màn trực tiếp bằng một khoảnh khắc chất ngông thơ mộng hoặc một điểm neo đơn khối có sức hút thị giác tức thì để giữ chân người xem và xác lập không khí đại địa điểm.
2. **Verse (Tự sự gần gũi):** Các lát cắt đời sống ấm áp, nhịp máy chậm rãi, đan cài những chi tiết tinh tế phản chiếu nội tâm bài hát.
3. **Chorus (Mở bừng không gian và giải phóng năng lượng):** Chủ động mở rộng quy mô khung hình bằng các góc toàn cảnh từ điểm nhìn cao xa, góc nghiêng từ trên cao 45 độ hoặc góc thấp ngước lên bầu trời, đẩy mạnh chuyển động của thiên nhiên và giải phóng những cử chỉ tự do, bay bổng.
4. **Bridge / Nhạc dạo (Đỉnh thị giác và bước ngoặt cảm xúc):** Đặt các ý tưởng thị giác táo bạo, tĩnh lặng mà giàu chất thơ ở mốc 2/3 bài, kết hợp bước chuyển pha ánh sáng rõ nét.
5. **Outro (Dư âm và đồng vọng):** Lắng đọng cảm xúc, tạo sự đồng vọng thị giác với khung hình mở đầu ở trạng thái thời gian và ánh sáng đã viên mãn.

Các cảnh liền kề được khâu nối mượt mà bằng sự đồng điệu hình khối, tiếp nối hướng chuyển động của gió và máy quay, hoặc đối cực quy mô từ đại cảnh xuống cận cảnh.

```markdown
# STORYBOARD: [TÊN TRACK]
- Chế độ kể chuyện: [Chế độ 1 (Kể chuyện cá nhân, dùng @Tên_nhân_vật + tả trực tiếp nhân vật ngoài luồng) | Chế độ 2 (Ý niệm đa diện, 100% lát cắt độc lập)]
- Thời lượng: [MM:SS] | Số cảnh: [N] shots (~5s/shot)
- Đại địa điểm: [Không gian lớn bao trùm toàn bài lấy từ 1-idea.md và 3-lyrics.txt]
- Hành trình ánh sáng và bảng màu: [Sự biến thiên tự nhiên của ánh sáng và các gam màu khoáng chất tươi trong qua từng đoạn nhạc]
- Điểm nhấn chữ ký: Mỗi cảnh gài 1 chi tiết nhỏ mang cặp màu Đen than và Vàng nghệ.

| Shot & Giờ | Đoạn nhạc & Lời hát | Thông số đạo diễn (Cỡ cảnh, Độ cao + Hướng máy, Tiểu bối cảnh, I2V) | Ý tưởng thị giác, Động cơ thăng hoa, Biểu cảm & Bảng màu (Móc nối cảnh) |
| :--- | :--- | :--- | :--- |
| 01 (00:00-00:05) | [Intro] | Cỡ: [Cỡ cảnh + Tiêu cự]<br>Góc: [Độ cao trục dọc + Hướng ngang]<br>Bối cảnh: [Tiểu bối cảnh]<br>I2V: [Quỹ đạo máy] | **[Tên ý tưởng / Động cơ]:** [Khoảnh khắc ẩn dụ khớp câu hát, vị trí và hành động của chủ thể hoặc tĩnh vật B-roll, chuyển động hậu cảnh, biểu cảm, chi tiết đen-vàng và bảng màu 70-20-10 của cảnh]. |
```

### Bước 3: Biên dịch 1:1 sang `image.txt`
Dịch từng dòng đã duyệt trong `storyboard.md` sang câu lệnh tiếng Anh trong `image.txt` theo khung câu chuẩn của Chế độ 1 hoặc Chế độ 2 tại [`style/STYLE_mixed_media_tabletop_diorama.md`](../style/STYLE_mixed_media_tabletop_diorama.md).

---

## 2. Quy luật tỷ lệ 70/30 và bốn động cơ chất ngông nghệ thuật

- **Nguyên lý làm quá lên một nấc từ hành động có mục đích:** Chất ngông thơ mộng xuất phát từ một hành động con người bình thường, có mục đích cảm xúc rõ ràng, sau đó nâng điểm tựa không gian hoặc độ phiêu lãng của cử chỉ lên một nấc tự do, phóng khoáng hơn ngay trong những cấu trúc kiến trúc và địa hình thuộc về thế giới đó. Luôn dịch ẩn ý cảm xúc của lời hát thành hành động tương tác thực tế với môi trường.
- **Ngôn ngữ cơ thể lãng tử, bất quy tắc:** Nhân vật mang thái độ sống tự do, phóng khoáng, thoát khỏi sự lịch thiệp cứng nhắc. Tư thế cơ thể luôn thả lỏng, bất đối xứng hoặc bung mở theo cảm xúc (ngả lưng tự nhiên, co một chân lên điểm tựa, đung đưa chân trên cao, tháo giày đi chân trần, mở cúc áo đón gió, đội mũ/phụ kiện lệch).
- **Tỷ lệ 70% Đời thường phóng khoáng : 30% Điểm nhấn chất ngông:**
  - **70% số cảnh (tập trung ở Verse và Outro):** Nhân vật sinh hoạt, chế tác thủ công, trò chuyện và di chuyển ở những vị trí tự nhiên với tư thế thoải mái, giàu hơi thở đời sống; vẻ đẹp điện ảnh đến từ dấu ấn thời gian của chất liệu, góc máy, ánh sáng và chiều sâu không gian thoáng đãng.
  - **30% số cảnh (đặt tại Cảnh 01 mở màn, Chorus và Nhạc dạo / Bridge):** Mỗi cảnh chọn **đúng 1 điểm nhấn duy nhất** thuộc 1 trong 4 động cơ dưới đây:

1. **Động cơ 1 (Điểm tựa cao phóng khoáng và cử chỉ phiêu lãng):** Đưa một hoạt động giao tiếp, vui chơi hoặc thưởng thức đời thường lên một điểm tựa kiến trúc hoặc địa hình cao tách biệt khỏi mặt đất thông thường, mở ra đường chân trời rộng lớn để nhân vật thực hiện những cử chỉ tự do, lãng mạn như những nghệ sĩ giữa đất trời.
2. **Động cơ 2 (Kiến trúc hoặc điểm neo đơn khối giữa thiên nhiên bao la):** Đặt một công trình kiến trúc duyên dáng vốn thuộc về cảnh quan hoặc 1 đến 2 vật dụng nghỉ ngơi, sinh hoạt đơn khối nằm tách biệt một mình giữa không gian thiên nhiên lộ thiên rộng lớn để tạo sự đối sánh tỷ lệ tĩnh lặng và giàu chất thơ.
3. **Động cơ 3 (Phóng đại tỷ lệ bóng đổ và đổi công năng đạo cụ):** Dùng ánh nắng chiếu xiên góc thấp để biến bóng đổ của nhân vật và đạo cụ thủ công nhỏ bé thành một hình bóng ẩn dụ khổng lồ in lên bề mặt kiến trúc hoặc mặt đất; hoặc biến một vật dụng, chi tiết tự nhiên gần gũi thành đạo cụ chơi đùa, chỉ huy nhịp điệu thiên nhiên.
4. **Động cơ 4 (Phương tiện hoài niệm lướt gió và tâm thế tự tại):** Đưa các phương tiện di chuyển cổ điển nhỏ nhắn lướt qua địa hình thiên nhiên rộng mở với phục trang bay căng theo luồng gió mạnh; hoặc đặt nhân vật tận hưởng một thói quen đời thường với tâm thái điềm nhiên, tự tại giữa thiên nhiên chuyển động mạnh.

---

## 3. Sáu quy luật bố cục không gian, bảng màu và điều phối nhịp điệu

1. **Thống nhất đại địa điểm và đa dạng hóa công trình:** Mỗi bài hát neo vào một đại địa điểm xuyên suốt lấy từ `1-idea.md` và `3-lyrics.txt`, mang dấu ấn thời gian ấm áp, có hồn. Giữa các cảnh kế tiếp, chủ động biến hóa hình khối, chất liệu và cao độ của các tiểu bối cảnh; kết hợp hài hòa giữa không gian sinh hoạt đời thường gần gũi (ở 70% cảnh đời thường) và các điểm mốc kiến trúc, địa hình cảnh quan khoáng đạt (ở 30% cảnh chất ngông).
2. **Khoảng thở không gian và tiết chế đạo cụ theo bối cảnh:** Giữ bố cục thoáng sạch để tách bật đường viền chủ thể khỏi hậu cảnh (mở rộng 50% đến 70% khoảng thở bầu trời, mặt nước hoặc địa hình ở các đại cảnh ngoài trời; giữ chiều sâu ngăn nắp, không bày biện rối mắt ở các cảnh xưởng nghề, phố thị hoặc trong nhà). Mỗi khung hình tập trung vào 1 tâm điểm thị giác rõ ràng.
3. **Cân bằng không gian trong nhà, bán nội thất và ngoài trời:** Đặt các hoạt động sinh hoạt, chế tác tỉ mỉ trong không gian nội thất hoặc bán nội thất ấm cúng, và bung mở các hoạt động di chuyển, phiêu lãng ra đại cảnh ngoài trời. Cảnh nội thất hoặc hiên nhà luôn có chiều sâu không gian và nguồn sáng rõ hướng qua khung cửa sổ, ô thoáng hoặc cửa mở kết nối với thế giới bên ngoài (không nhốt nhân vật trong phòng kín bức bối không cửa sổ). Chuyển động của môi trường (gió, sóng, mây, lá rơi, nắng) co giãn nhịp nhàng theo âm nhạc: êm dịu ở đoạn tự sự lắng đọng và bung mở mạnh mẽ ở đoạn điệp khúc cao trào.
4. **Một nguồn sáng chính mềm mại và bảng màu khoáng chất 70-20-10 đa sắc thái, có chiều sâu:** Mỗi cảnh sử dụng 1 nguồn sáng chính chiếu từ 1 hướng rõ ràng với độ chuyển sáng êm dịu (nắng chiều ấm áp, nắng hổ phách dịu, ánh sáng tán xạ mềm qua mây, hoàng hôn đỏ cam rực rỡ trên nền biển thẫm, hoặc ánh đèn lồng trong chạng vạng xanh chàm), tránh ánh nắng trưa trắng gắt gây chói lóa. Chủ động biến thiên 70% mảng màu môi trường chủ đạo qua các gam màu khoáng chất có chiều sâu (xanh biển coban đậm, xanh sapphire, xanh da trời cerulean, xanh ngọc bích, xanh lục bảo, xanh đá phiến, cam vàng hoàng hôn đối lập biển xanh thẫm, xanh chàm) và ưu tiên bề mặt đá/gỗ nhuốm màu thời gian tự nhiên thay vì tường đá trắng lốp để khung hình vừa mềm mại, đa dạng vừa trong trẻo.
5. **Bố cục bất đối xứng 1/3, lệch tầng cao thấp và biểu cảm điềm tĩnh chừng mực:** Đặt chủ thể lệch về trục 1/3 khung hình, hướng mặt về phía 2/3 khoảng mở của khung cảnh. Khi có từ 2 nhân vật trở lên, ưu tiên sắp đặt lệch tầng cao thấp theo đường chéo và để các chủ thể hướng mặt trực tiếp vào nhau qua khoảng không sạch. Hiển thị trọn vẹn đôi chân chạm điểm tựa hoặc đung đưa tự nhiên trên cao khi cảnh lộ mặt nền. Mô tả biểu cảm tinh tế, điềm đạm qua ánh mắt lắng đọng, đôi môi thả lỏng tự nhiên hoặc nụ cười mỉm khép môi nhẹ nhàng khớp với tâm trạng từng câu hát (tránh các biểu cảm cường điệu lố như cười ngoác miệng, ngửa cổ cười lớn hay reo hò quá đà).
6. **Luật độc bản ý tưởng toàn bài và đảo nhịp liền kề ($N \to N+1$):** Mỗi ý tưởng chất ngông, mỗi điểm tựa cao, phương tiện hoặc đạo cụ đổi công năng chỉ xuất hiện đúng 1 lần trong toàn bài (trừ cảnh kết đồng vọng với cảnh mở đầu). Giữa hai cảnh liền kề ($N \to N+1$), bắt buộc thay đổi tối thiểu 3 trong 4 yếu tố:
   - *Chủ thể, hành động và biểu cảm:* Ở Chế độ 1, nhân vật `@Tên_nhân_vật` chuyển sang hành động, sự kiện, tư thế và biểu cảm mới, kết hợp tách/gộp nhân vật, đan xen nhân vật ngoài luồng hoặc cảnh tĩnh vật (`B-roll`). Ở Chế độ 2, đổi sang nhân vật mới hoàn toàn cùng số lượng người và trạng thái biểu cảm mới.
   - *Tiểu bối cảnh và độ cao không gian:* Luân chuyển giữa không gian nội thất/bán nội thất thoáng sáng, mặt đất/mép nước ngoài trời và điểm tựa cao nhìn ra chân trời.
   - *Bảng màu chủ đạo (70%) và sắc thái ánh sáng:* Luân chuyển gam màu khoáng chất 70% của môi trường và sắc thái ánh sáng mềm mại sau mỗi 1 đến 2 cảnh.
   - *Cỡ cảnh, độ cao trục dọc của máy và động cơ sáng tạo:* Xoay vòng cỡ cảnh, độ cao đặt máy và trục bố cục 1/3.

---

## 4. Năm cỡ cảnh và ma trận góc máy hai chiều

### 4.1. Năm cỡ cảnh linh hoạt
1. **Siêu rộng:** Đại cảnh thiên nhiên và kiến trúc rộng lớn, luôn có sinh khí của các bóng người nhỏ thấy trọn từ đầu đến giày cùng chuyển động của môi trường (ống kính 35mm nét sâu).
2. **Rộng và trung rộng toàn thân:** Lấy trọn toàn thân từ đầu đến giày đặt trên điểm tựa trước không gian thoáng mở (ống kính 35mm nét sâu).
3. **Trung cảnh:** Lấy nhân vật ở mặt phẳng trung cảnh khi phần chân được che tự nhiên bởi địa hình hoặc điểm tựa phía trước.
4. **Trung cận:** Lấy từ thắt lưng hoặc ngực trở lên để đặc tả biểu cảm gương mặt, ánh mắt và đôi tay cắt trực tiếp qua eo trước hậu cảnh mở thoáng mờ dịu (ống kính 50mm).
5. **Cận cảnh:** Đặc tả chi tiết chủ thể, bước chân, cử chỉ hoặc 1 đến 2 đồ vật thủ công đơn khối (`B-roll`) ở cự ly gần đặt trước hậu cảnh thoáng mở (ống kính 50mm; dừng ở mức cận cảnh, không dùng siêu cận).

### 4.2. Ma trận góc máy: 4 Độ cao trục dọc $\times$ 4 Hướng xoay ngang
Mọi cảnh trong `storyboard.md` và `image.txt` luôn ghép rõ **1 Độ cao trục dọc** với **1 Hướng xoay ngang**, luân chuyển linh hoạt để hai cảnh liền kề ($N \to N+1$) không trùng góc đặt máy (không dùng góc thẳng đứng 90 độ từ đỉnh đầu xuống vì gây rối mắt và mất đường chân trời):
- **4 Độ cao trục dọc:**
  1. Từ trên cao chúc xuống 35-45 độ (`Elevated high-angle`).
  2. Toàn cảnh từ điểm nhìn cao xa (`High-vantage panoramic`).
  3. Góc thấp sát mặt nền ngước lên (`Low-angle`).
  4. Ngang tầm mắt (`Eye-level`).
- **4 Hướng xoay ngang:** Góc chéo 3/4, góc nghiêng 90 độ, nhìn từ sau lưng cùng hướng về phía chân trời, hoặc nhìn xuyên qua khung cửa mở / lớp tiền cảnh mờ. Khi hai nhân vật tương tác, đặt cả hai trên cùng mặt phẳng trung cảnh ở góc chéo 3/4 hoặc góc nghiêng 90 độ.

