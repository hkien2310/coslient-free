# VISUAL CRAFT: NGHỆ THUẬT DÀN DỰNG ẢNH ĐẸP & ĐẸP LIÊN TỤC

> **GHI CHÚ CỐ ĐỊNH (CẤM XÓA KHI CHỈNH SỬA FILE):**
> 1. **Phân định ranh giới:** File `style/STYLE_*.md` quy định *chất liệu, tỷ lệ, bề mặt, ống kính và cấu trúc JSON của 1 bức ảnh*. File `craft/visual_craft.md` này quy định *cách tạo ra một cảnh có hồn (Ảnh Đẹp) và cách điều phối nhịp điệu giữa 50–70 bức ảnh (Ảnh Đẹp Liên Tục)*.
> 2. **Sửa đúng chỗ (`/ponytail`):** Chỉ sửa đúng dòng cần thay đổi bằng công cụ chỉnh sửa cục bộ, ưu tiên ngắn gọn, không ghi đè toàn bộ file.
> 3. **Chỉ viết quy luật, không đưa use case riêng lẻ:** Rút ra quy tắc chung áp dụng cho mọi bài nhạc, không liệt kê bối cảnh chỉ dùng cho một dự án đơn lẻ.
> 4. **Viết tự nhiên, đi thẳng vào kỹ thuật (`/humanizer` & `stop-slop`):** Bỏ văn phong đao to búa lớn, từ ngữ sáo rỗng và cấu trúc câu rập khuôn của AI.

## 1. Nguyên tắc lát cắt cảm xúc độc lập

- **Xoay quanh trục cảm xúc cốt lõi:** Mỗi prompt trong `image.json` là một lát cắt độc lập phản chiếu câu chuyện và cảm xúc trong `1-idea.md`. Các lát cắt tự do thay đổi nhân vật và bối cảnh thay vì đi theo hành trình tuyến tính của một nhân vật duy nhất.
- **Khung hình tự đứng vững:** Khi tách bất kỳ bức ảnh nào ra khỏi chuỗi video, người xem vẫn nhận ra ngay câu chuyện, cảm xúc và điểm hút thị giác của riêng bức ảnh đó mà không cần xem ảnh trước hay sau.
- **Tự do ghép nhịp khi dựng phim:** Khi mỗi ảnh tự đứng vững và mang chung mạch cảm xúc, khâu dựng có thể ghép ảnh theo nhịp nhạc (`timestamps.txt`) mà không làm gãy mạch truyện.

## 2. Năm trụ cột tạo nên một bức ảnh đẹp

Mọi khung hình đều phải kết hợp đủ 5 yếu tố dưới đây thay vì chỉ mô tả sinh hoạt đời thường:

### 2.1. Năm thủ pháp siêu thực và đường cong thủ công tại `focal_elements` và `setting`
Mọi kiến trúc, phương tiện và đạo cụ đều ưu tiên đường lượn cong mềm mại, hơi phồng hoặc nghiêng liêu xiêu bất đối xứng của đồ làm tay, loại bỏ hoàn toàn các đường thẳng tắp công nghiệp. Lấy một hành động đời thường làm gốc, sau đó cài vào cảnh ít nhất một trong năm thủ pháp siêu thực:
1. **Nét cắt sa bàn và kiến trúc mất tường giữa thiên nhiên:** Không gian nội thất được cắt mặt phẳng trực diện hoặc mở toang vách tường, đặt trực tiếp giữa thiên nhiên rộng lớn.
2. **Đánh tráo công năng không gian và đồ vật:** Đưa một hoạt động hoặc đồ vật quen thuộc vào một không gian hoàn toàn trái ngược với công năng gốc, hoặc dùng đồ vật này để thực hiện chức năng của đồ vật khác.
3. **Đóng gói và thuần hóa khí quyển:** Các hiện tượng thời tiết, âm thanh hoặc khí quyển vô hình được vật chất hóa bằng chất liệu thủ công để con người có thể cầm nắm, buộc giữ, đóng lọ hoặc gắn lên cơ thể.
4. **Biến hình vật chất và lệch tỷ lệ sinh vật:** Một chất liệu thủ công đang thao tác biến đổi trực tiếp thành sinh vật sống hoặc địa hình thu nhỏ; hoặc các sinh vật tự nhiên mang kích thước lớn bất thường xuất hiện sát cạnh con người.
5. **Lệch pha thời đại:** Đặt các thiết bị âm thanh hoặc cơ khí hiện đại vào trong bối cảnh kiến trúc và trang phục cổ điển.

### 2.2. Bốn kỹ thuật khóa tâm điểm thị giác
Không để hậu cảnh tranh chấp chi tiết với chủ thể. Mỗi khung hình phải dùng ít nhất một trong bốn kỹ thuật sau để dẫn mắt người xem vào tâm điểm:
1. **Cô lập trên bệ đỡ giữa khoảng trống âm lớn:** Gom toàn bộ nhân vật và đạo cụ lên một mặt sàn hoặc cấu trúc có ranh giới rõ ràng, bao quanh bởi 60% đến 70% mảng nền đồng nhất và ít chi tiết.
2. **Đặt tại ranh giới nền hoặc lọt trong khung kiến trúc:** Đặt nhân vật ngay ranh giới chuyển tiếp giữa mảng kiến trúc và mảng nền thoáng để tách khối, hoặc dùng chính khung cửa, vòm kiến trúc làm khung phụ bao quanh nhân vật.
3. **Dìm tối xung quanh và gom chóp sáng trực tiếp:** Với cảnh nội thất hoặc cảnh có nhiều chi tiết xung quanh, dìm tối vùng biên và dùng một nguồn sáng chiếu chóp trực tiếp từ trên xuống đúng vị trí nhân vật và vật thể siêu thực.
4. **Hội tụ hướng nhìn và đường dẫn vật lý:** Điều hướng ánh mắt của sinh vật và các đường dẫn vật lý trong cảnh chỉ về tâm điểm.

### 2.3. Hai chế độ dàn dựng, phân hóa hình khối và biểu cảm hiền từ
Nhân vật luôn có mái tóc dày bồng bềnh (không bao giờ bị hói) và nét mặt hiền từ, ấm áp, bình yên hoặc vui vẻ nhẹ nhàng (không bao giờ u buồn, khắc khổ hay hốc hác). Để các nhân vật trong cùng một ảnh không bị giống nhau, phải tạo độ lệch giữa dáng cao thanh mảnh và dáng thấp tròn trịa, bầu bĩnh, kết hợp khác biệt kiểu tóc, râu bông, mũ, kính và chia theo hai chế độ:
- **Chế độ có nhân vật chính (từ 1 đến 4 người trung tâm):** Tách riêng từng nhân vật chính trong `figures[]` với vóc dáng, độ tuổi, góc mặt và màu trang phục đối lập nhau. Nếu có thêm người phụ, đẩy họ ra lớp tiền cảnh hoặc hậu cảnh xóa phông mờ.
- **Chế độ không có nhân vật chính (đại cảnh nhóm đông người):** Lấy cấu trúc không gian siêu thực có đường cong thủ công làm tâm điểm. Đặt toàn bộ nhân vật đứng hoặc ngồi trọn vẹn trên mặt phẳng sàn (không cắt cụt nửa dưới cơ thể trong hộp kín), chia thành các cụm nhỏ bất đối xứng ở các độ cao khác nhau. Các nhân vật tương tác tự nhiên thả lỏng với nhau (trò chuyện mỉm cười, nhắm mắt nghe nhạc, tựa lưng thư giãn) thay vì cùng đứng đơ nhìn cứng nhắc về một điểm.

### 2.4. Điểm nổ màu 10% trên nền 70%
- Khi 70% màu khí quyển và bối cảnh mang tông lạnh đậm, đặt 10% điểm màu nóng tương phản ngay tại tâm điểm thị giác.
- Khi 70% màu nền mang tông ấm sáng, đặt 10% điểm màu lạnh đậm hoặc đỏ sẫm tại tâm điểm để giữ mắt người xem.
- Kết hợp viền sáng ấm tách khối nhân vật khỏi hậu cảnh.

### 2.5. Trạng thái đắm chìm ấm áp và một chuyển động bắt dính
- **Đắm chìm ấm áp:** Nhân vật không đứng tạo dáng nhìn vào ống kính mà tận hưởng khoảnh khắc với vẻ mặt hiền hòa, mỉm cười nhẹ, nhắm mắt cảm nhận hoặc chăm chú thao tác.
- **Chuyển động bắt dính:** Mỗi bức ảnh tĩnh phải giữ lại một chuyển động vật lý đang diễn ra giữa chừng tại trường `motion`.

## 3. Ba cơ chế giữ ảnh đẹp liên tục qua 50 đến 70 cảnh

### 3.1. Cấm ảnh lấp chỗ trống và xoay vòng 5 thủ pháp siêu thực
Không tạo các khung hình chỉ đứng hoặc ngồi sinh hoạt bình thường. Các cảnh kế tiếp nhau phải luân chuyển qua lại giữa 5 thủ pháp siêu thực ở Mục 2.1.

### 3.2. Luật đảo nhịp tương phản liền kề
Giữa ảnh thứ $N$ và ảnh thứ $N+1$, phải thay đổi tối thiểu 3 trong 5 yếu tố sau:
1. **Bảng màu chủ đạo (70%):** Không để quá 2 ảnh liên tiếp dùng chung một tông màu nền.
2. **Quy mô và chế độ nhân vật:** Luân chuyển giữa cảnh 1 người, cảnh 2 người, cảnh 3 đến 4 người và đại cảnh nhóm đông người (tối thiểu 70% tổng số ảnh có con người).
3. **Độ tuổi và cặp hình khối:** Thay đổi tổ hợp độ tuổi và vóc dáng giữa các cảnh kế tiếp.
4. **Không gian và kỹ thuật khóa tâm điểm:** Đảo giữa cảnh ngoài trời có khoảng trống âm lớn, cảnh kiến trúc mở thông thiên nhiên và cảnh nội thất mặt cắt ngang dùng chóp sáng.
5. **Thời gian và nguồn sáng:** Luân chuyển giữa nắng sớm, nắng trưa, ngược sáng hoàng hôn, chạng vạng và ánh đèn ban đêm.

### 3.3. Đồng bộ cỡ cảnh và kiểm duyệt trên `image-index.md`
- **Thấy gì tả nấy:** Chỉ mô tả những bộ phận cơ thể và vật thể nằm trong khung cắt của máy quay. Cấm góc máy qua vai (`over-the-shoulder`) để tránh biến dạng tỷ lệ.
- **Kiểm duyệt trên `image-index.md` trước khi viết JSON:**
  Mỗi cảnh trong `image-index.md` ghi trên 1 dòng gồm 5 cột:
  `- **ID** | [Cỡ cảnh & Không gian/Thời gian] | [Bảng màu: 70% Nền - 10% Điểm nổ] | [Chế độ nhân vật & Tương phản hình khối] | [Thủ pháp siêu thực & Kỹ thuật khóa tâm điểm]`
  Trước khi viết batch mới vào `image.json`, kiểm tra `image-index.md` để đảm bảo mọi cảnh đều có thủ pháp siêu thực, kỹ thuật khóa tâm điểm rõ ràng, và hai dòng liền kề đã đảo đủ tối thiểu 3 yếu tố. Sau khi hoàn thành project, cập nhật tóm tắt vào [`ref/image-index.md`](../ref/image-index.md).


