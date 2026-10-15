# VISUAL CRAFT: NGHỆ THUẬT DÀN DỰNG ẢNH ĐẸP & ĐẸP LIÊN TỤC

> **GHI CHÚ CỐ ĐỊNH (CẤM XÓA KHI CHỈNH SỬA FILE):**
> 1. **Phân định ranh giới:** File `style/STYLE_*.md` quy định *chất liệu, tỷ lệ, bề mặt, ống kính và cấu trúc JSON của 1 bức ảnh*. File `craft/visual_craft.md` này quy định *cách tạo ra một cảnh có hồn (Ảnh Đẹp) và cách điều phối nhịp điệu giữa 50–70 bức ảnh (Ảnh Đẹp Liên Tục)*.
> 2. **Sửa đúng chỗ (`/ponytail`):** Chỉ sửa đúng dòng cần thay đổi bằng công cụ chỉnh sửa cục bộ, ưu tiên ngắn gọn, không ghi đè toàn bộ file.
> 3. **Chỉ viết quy luật, không đưa use case riêng lẻ:** Rút ra quy tắc chung áp dụng cho mọi bài nhạc, không liệt kê bối cảnh chỉ dùng cho một dự án đơn lẻ.
> 4. **Viết tự nhiên, đi thẳng vào kỹ thuật (`/humanizer` & `stop-slop`):** Bỏ văn phong đao to búa lớn, từ ngữ sáo rỗng và cấu trúc câu rập khuôn của AI.

## 1. Nguyên tắc lát cắt cảm xúc độc lập

- **Xoay quanh trục cảm xúc cốt lõi:** Mỗi prompt trong `image.json` là một lát cắt độc lập phản chiếu câu chuyện và cảm xúc trong `1-idea.md`. Các cảnh tự do đổi nhân vật và không gian theo từng cung bậc của bài nhạc.
- **Khung hình tự đứng vững:** Khi tách bất kỳ bức ảnh nào ra khỏi chuỗi video, người xem nhận ra ngay câu chuyện, cảm xúc và điểm hút thị giác của riêng bức ảnh đó mà không cần xem ảnh trước hay sau.
- **Tự do ghép nhịp khi dựng phim:** Vì mỗi ảnh tự đứng vững trên cùng một mạch cảm xúc, khâu dựng có thể ghép ảnh khớp với nhịp nhạc (`timestamps.txt`) mà vẫn giữ liền mạch cảm xúc.

## 2. Năm điều kiện bắt buộc của một khung hình

Thiếu bất kỳ điều kiện nào dưới đây, bức ảnh sẽ trở nên tầm thường, rối mắt hoặc lỗi giải phẫu:

### 2.1. Đường cong thủ công và một điểm lệch siêu thực duy nhất
Mọi kiến trúc, phương tiện và đạo cụ đều mang đường lượn cong mềm, hơi phồng hoặc nghiêng bất đối xứng của đồ làm tay, loại bỏ hoàn toàn các đường thẳng kẻ thước công nghiệp. Lấy một hành động đời thường tĩnh lặng làm gốc và cài vào cảnh **đúng một điểm lệch siêu thực tinh tế**: mở thông không gian nội thất ra thẳng thiên nhiên, cho vật thể hoặc phương tiện trôi lơ lửng nhẹ nhàng không trọng lực giữa không trung, vật chất hóa khí quyển thành chất liệu thủ công có thể chạm tới, hoặc đảo tỷ lệ và công năng của đồ vật. Tuyệt đối không nhồi từ hai ý tưởng siêu thực trở lên vào cùng một khung hình.

### 2.2. Khoảng thở 60% và tối đa 3 đạo cụ (Chống hổ lốn)
- Vùng nền ngay sau lưng tâm điểm phải thoáng, đồng nhất hoặc xóa phông êm, chiếm tối thiểu 60% diện tích khung hình để tách bật đường viền nhân vật (hoặc dùng một chóp sáng chiếu trực tiếp vào chủ thể giữa vùng biên dìm tối).
- Mỗi khung hình chỉ giữ một tâm điểm thị giác và tối đa 2 đến 3 đạo cụ chính. Cấm rải dây nhợ ngoằn ngoèo dưới sàn, cấm treo nhiều đèn lặt vặt hoặc nhồi nhét chi tiết phụ làm ngạt thở bố cục.

### 2.3. Toàn vẹn đôi chân và đường tương tác thông suốt (Chống mất chân)
- **Thấy trọn vẹn đôi chân:** Nhân vật đứng hoặc ngồi phải lộ rõ toàn bộ phần thân dưới cùng hai bàn chân và đôi giày đặt trên mặt phẳng sàn (hoặc buông tự nhiên trong không trung nếu ngồi trên vật thể bay). Cấm đặt bàn ghế, thùng máy, hộp gỗ hay thanh lan can chắn ngang cẳng chân làm mất chân nhân vật. Cấm góc máy qua vai (`over-the-shoulder`).
- **Tương tác trực diện không bị chia cắt:** Hai chủ thể đang tương tác phải hướng mặt trực tiếp vào nhau qua một khoảng không sạch. Cấm đặt người thứ ba, cột gỗ hay đạo cụ chen vào giữa làm đứt gãy đường truyền hành động.

### 2.4. Thần thái bình yên và phân hóa hình khối giữ nguyên chiều dài chân
- Nhân vật luôn có mái tóc dày bồng bềnh (không bao giờ bị hói) và nét mặt hiền từ, ấm áp, bình yên hoặc mỉm cười nhẹ (không bao giờ u buồn, khắc khổ hay hốc hác).
- Mỗi khung hình giới hạn từ 1 đến tối đa 4 nhân vật (nếu có cảnh rộng nhiều người hơn thì phải chia thành tối đa 2 cụm thoáng đãng). Khi có từ 2 người trở lên, phân hóa ngoại hình qua độ tuổi, kiểu tóc, màu áo và sự đối lập giữa dáng thanh mảnh với dáng đầy đặn tròn trịa, nhưng bắt buộc giữ nguyên tỷ lệ chiều cao và đôi chân dài để không ai bị biến thành người lùn.

### 2.5. Điểm nổ màu 10% và một chuyển động bắt dính
- Đặt 70% màu chủ đạo cho khí quyển và bối cảnh, 20% màu bổ trợ cho kiến trúc và trang phục, và đúng 10% màu tương phản mạnh đặt ngay tại tâm điểm kèm viền sáng ấm để khóa mắt người xem.
- Nhân vật đắm chìm tự nhiên vào khoảnh khắc đang diễn ra (không đứng tạo dáng nhìn vào ống kính), đi kèm một chuyển động vật lý đang diễn ra giữa chừng tại trường `motion`.

## 3. Điều phối nhịp điệu qua 50 đến 70 cảnh

### 3.1. Không lặp lại ý tưởng siêu thực liền kề
Cấm tạo các khung hình chỉ đứng hoặc ngồi sinh hoạt bình thường. Mỗi cảnh kế tiếp phải mang một điểm lệch siêu thực khác biệt với cảnh liền trước.

### 3.2. Luật đảo nhịp tương phản liền kề
Giữa ảnh thứ $N$ và ảnh thứ $N+1$, bắt buộc thay đổi tối thiểu 3 trong 4 yếu tố:
1. **Bảng màu chủ đạo (70%):** Không để quá 2 ảnh liên tiếp dùng chung một tông màu nền.
2. **Quy mô và tổ hợp nhân vật:** Luân chuyển số lượng nhân vật (từ 1 đến 4 người) và đổi cặp độ tuổi, hình khối giữa hai cảnh kế tiếp (tối thiểu 70% tổng số ảnh trong bài có con người).
3. **Không gian và độ cao:** Đảo giữa cảnh mặt đất ngoài trời, cảnh mặt cắt nội thất mở thông thiên nhiên, và cảnh vật thể trôi lơ lửng không trọng lực trên cao.
4. **Thời gian và nguồn sáng:** Luân chuyển hướng nắng và màu ánh sáng theo các thời điểm khác nhau trong ngày và đêm.

### 3.3. Kiểm duyệt trên `image-index.md` trước khi viết JSON
Mỗi cảnh trong `image-index.md` ghi trên 1 dòng gồm 5 cột:
`- **ID** | [Không gian & Thời gian] | [Bảng màu: 70% Nền - 10% Điểm nổ] | [Số lượng & Hình khối nhân vật] | [Điểm lệch siêu thực & Cách lấy khoảng thở]`
Trước khi viết batch mới vào `image.json`, đối chiếu trên `image-index.md` để đảm bảo mỗi cảnh chỉ có 1 điểm lệch siêu thực, giữ đủ 60% khoảng thở, không che khuất chân, và hai dòng liền kề đã đổi tối thiểu 3 yếu tố. Sau khi hoàn thành project, cập nhật tóm tắt vào [`ref/image-index.md`](../ref/image-index.md).
