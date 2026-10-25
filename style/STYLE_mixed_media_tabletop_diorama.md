# Handcrafted Stop-Motion Style (`character.md` & `image.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Định nghĩa nguyên lý thế giới sa bàn thủ công stop-motion trực quan (`Handcrafted stop-motion miniature diorama`), tạo hình nhân vật cách điệu (da giấy bồi mờ, mũi tròn cách điệu, tỷ lệ thanh mảnh kéo dài, tóc và râu sợi bông xù, trang phục vải dệt đủ bộ áo-quần dài-giày kèm điểm nhấn nhận diện độc bản), công thức nén nhận diện trực quan, tư thế khởi đầu hành động ở giây 0 và **khung câu lệnh 4 khối tiếng Anh trực quan** để viết `character.md` cũng như biên dịch `storyboard.md` sang `image.txt`. Nghệ thuật đạo diễn kịch bản `storyboard.md`, tỷ lệ 70/30, bố cục không gian và ma trận góc máy nằm độc lập tại [`craft/visual_craft.md`](../craft/visual_craft.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra (`image.txt`)

- **Đầu vào:** `1-idea.md`, `storyboard.md` và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
- **Đầu ra — Khung câu lệnh tiếng Anh cho `image.txt` theo 3 mẫu cỡ cảnh (1 dòng/cảnh khớp 1:1 với `storyboard.md`):**

```text
# Mẫu 1 — Cảnh Trung & Cận tập trung vào Nhân vật (Medium-wide / Medium / Medium close-up / Waist-up — 1 đến 2 người):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], [time-of-day] light, asymmetric rule-of-thirds composition, harmonious character-to-object scale, shallow depth of field with a softly blurred warm background. [Medium-wide / Medium close-up waist-up + Góc máy điện ảnh luân phiên] shot at/inside [công trình kiến trúc, phương tiện hoặc không gian siêu thực đặt lệch tâm tự nhiên] with stylized stop-motion figure(s) with matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown: [Mô tả nhân vật 4 trục tinh gọn phù hợp cỡ cảnh + biểu cảm ánh mắt, nụ cười + hành động gắn kết/chiêm nghiệm]. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9

# Mẫu 2 — Đại cảnh & Toàn cảnh Kiến trúc/Địa hình Siêu thực có Người ở xa hoặc Đông người (Extreme wide / Wide):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], [time-of-day] light, asymmetric rule-of-thirds composition with a winding diagonal layout, monumental architectural scale, expansive scenic focus with generous open negative space on one side and gentle atmospheric depth. [Extreme wide panoramic / Wide + Góc máy] shot showcasing [công trình kiến trúc, kết cấu hoặc địa hình siêu thực kỳ vĩ bố trí lệch một bên khung hình], where tiny distant miniature townspeople in varied warm clothing [hoạt động sinh hoạt hoặc lễ hội nhìn từ xa hòa vào không gian]. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9

# Mẫu 3 — Cảnh Tĩnh vật B-Roll hoặc Cảnh Sắc Không Gian (Vắng bóng người):
2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], [time-of-day] light, asymmetric rule-of-thirds composition, [shallow depth of field with a softly blurred warm background | expansive scenic focus with generous open negative space]. [Close-up / Extreme wide + Góc máy] shot of [1 chi tiết vật dụng đời thường bo tròn sơn mờ đặt lệch tâm hoặc 1 công trình/cảnh quan siêu thực uốn lượn thoáng rộng], completely without people. Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9
```

---

## 2. Luật Đầu Ra (`image.txt`)

- **Thế giới, Bố cục Bất đối xứng & Độ sâu trường ảnh (`Khối 1`):**
  - Mở đầu bằng `2.5D handcrafted stop-motion animation film still set in a warm poetic surreal town where [đặc điểm kỳ lạ định danh của thị trấn], [time-of-day] light, asymmetric rule-of-thirds composition`.
  - Mỗi Đại Cảnh đưa vào các công trình kiến trúc, phương tiện và địa hình siêu thực kỳ vĩ đặt lệch tâm theo đường chéo hoặc đường cong chữ S tự nhiên (`winding diagonal or S-curve layout`), dành một bên khung hình cho khoảng thở thoáng rộng (`generous open negative space on one side`), tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
  - Chọn `shallow depth of field with a softly blurred warm background` cho Cảnh Trung/Cận (`Mẫu 1` & `Mẫu 3 Close-up`); chọn `expansive scenic focus with generous open negative space and gentle atmospheric depth` cho Đại cảnh/Toàn cảnh (`Mẫu 2` & `Mẫu 3 Wide`).
- **Phân cấp mô tả Con người theo Cỡ cảnh (`Mẫu 1` vs `Mẫu 2`):**
  - **Ở Đại cảnh & Toàn cảnh (`Extreme wide / Wide` — `Mẫu 2`):** Dành trọn trọng tâm mô tả cho kiến trúc và cảnh quan siêu thực đồ sộ; chỉ gọi tên con người bằng cụm từ quy mô nhỏ ở xa (`tiny distant miniature townspeople in varied warm clothing`) để giữ đúng tỷ lệ con người nhỏ bé trước công trình lớn và tạo sự đa dạng tự nhiên cho đám đông.
  - **Ở Cảnh Trung & Cận (`Medium / Medium close-up` — `Mẫu 1`):** Dùng phôi rối cách điệu (`matte paper-pulp skin, soft rounded noses, slender elongated proportions, and thick full fluffy cotton-fiber hair covering the crown`) kết hợp mô tả 4 trục (Dáng vóc, Phụ kiện vùng đầu, Tóc sợi bông, Trang phục vải dệt); mô tả đủ đến giày chạm sàn khi lấy toàn thân cự ly trung (`Medium-wide full-body`) hoặc chỉ mô tả phần thân trên khi lấy bán thân có vách che (`Medium close-up waist-up`).
- **Một nguồn sáng chính duy nhất (`Khối cuối`):** Khóa ở cuối mỗi câu lệnh một nguồn sáng tự nhiên duy nhất chiếu theo một hướng bóng đổ thống nhất (`Single directional [time-of-day] light casting a single coherent shadow direction --ar 16:9`).
