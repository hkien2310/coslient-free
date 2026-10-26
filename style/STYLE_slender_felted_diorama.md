# Slender Needle-Felted Puppet & Macro Diorama Style (`character.md` & `image.txt`)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Định nghĩa nguyên lý thế giới sa bàn thu nhỏ chân thực quay bằng ống kính tiêu cự cận (`Photorealistic miniature diorama with Macro 85mm shallow depth of field`), tạo hình nhân vật rối len nỉ đâm kim thủ công với tỷ lệ thanh mảnh nghệ thuật (`Handcrafted needle-felted wool puppet with slender artistic stop-motion proportions`), gương mặt nỉ bông ấm áp hồng hào, mái tóc sợi len có kết cấu bắt sáng, trang phục vải dạ/dệt kim thủ công và **khung câu lệnh tiếng Anh trực quan** để viết `character.md` cũng như biên dịch `storyboard.md` sang `image.txt`. Nghệ thuật đạo diễn kịch bản `storyboard.md`, cấu trúc 2 tầng Đại Cảnh – Tiểu Cảnh, bố cục không gian và ma trận góc máy nằm độc lập tại [`craft/visual_craft.md`](../craft/visual_craft.md).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Đầu Vào & Đầu Ra (`character.md` & `image.txt`)

- **Đầu vào:** `1-idea.md`, `storyboard.md` và [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
- **Đầu ra 1 — Cấu trúc file `character.md` *(Tùy chọn)*:**
  - Khóa trực tiếp chất liệu rối len nỉ thủ công, tỷ lệ cơ thể và chất liệu sa bàn ngay trong từng dòng của `image.txt` để mỗi khung hình là một lát cắt độc lập hoàn chỉnh; chỉ tạo `character.md` khi dự án cần lưu mẫu tham chiếu riêng.

- **Đầu ra 2 — Khung câu lệnh tiếng Anh chuẩn hóa cho `image.txt` (1 dòng/cảnh khớp 1:1 với `storyboard.md`):**

```text
# 1. Cảnh Có Nhân vật (Trung-rộng toàn thân, Trung cận bán thân, Bóng lưng, Nhìn xuyên khung):
[Cỡ cảnh & Góc máy] of handcrafted needle-felted wool puppet[s] with [elongated artistic / graceful] stop-motion proportions, [Nhân vật + kiểu mũi nỉ ửng hồng mềm mại (rosy felted nose) + má nỉ ấm áp (warm felt cheeks) + mái tóc sợi len dày rõ phom dáng (textured wool hair) + phụ kiện định danh], [tư thế tự nhiên có trọng tâm thoải mái + khoảnh khắc hành động gắn với đạo cụ hữu hình bên trong không gian sa bàn thu nhỏ + điểm xuyết chất thơ siêu thực nếu ở cảnh Hook]. [Trang phục dệt kim / vải dạ nỉ / tweed khớp cỡ cảnh với đôi giày nỉ tiếp xúc vững chắc trên mặt phẳng đứng ở cảnh toàn thân, hoặc đặt sau mặt phẳng tiền cảnh ở cảnh bán thân]. [Nguồn sáng có chiều sâu và độ tương phản nhiệt độ màu tách khối chủ thể khỏi hậu cảnh]. Macro 85mm, shallow depth of field, stop-motion puppet craft, photorealistic miniature diorama, no text --ar 16:9

# 2. Cảnh Đặc tả Chi tiết / Tĩnh vật / Đại cảnh Sa bàn (Close-up / Detail / Extreme Wide):
[Cỡ cảnh & Góc máy] inside a handcrafted miniature diorama, [Không gian kiến trúc / thiên nhiên thu nhỏ giàu kết cấu vật lý + diễn biến tinh tế của chi tiết/đạo cụ hoặc bóng dáng nhỏ bé của con rối len nỉ ở xa đối với Đại cảnh]. [Nguồn sáng có chiều sâu và độ tương phản màu sắc tạo bầu không khí điện ảnh]. Macro 85mm, shallow depth of field, stop-motion puppet craft, photorealistic miniature diorama, no text --ar 16:9
```

---

## 2. Luật Đầu Ra (`character.md` & `image.txt`)

- **Khóa Chất liệu Rối Len Nỉ ở Đầu Câu (`Felted Puppet Anchor`) & Hậu tố Ống kính Sa bàn ở Cuối Câu (`Macro Diorama Suffix Lock`):**
  - Mở đầu mọi cảnh có người bằng cụm định danh chất liệu rối len nỉ đâm kim thủ công và tỷ lệ cơ thể (`handcrafted needle-felted wool puppet[s] with elongated artistic stop-motion proportions`) để tạo sự tương phản thị giác đắt giá giữa **nhân vật bằng sợi len nỉ ấm áp** và **bối cảnh sa bàn vật lý chân thực**.
  - Khóa cố định hậu tố ống kính và chất liệu thế giới `Macro 85mm, shallow depth of field, stop-motion puppet craft, photorealistic miniature diorama, no text --ar 16:9` ở cuối mỗi dòng câu lệnh trong `image.txt`.
- **Tạo hình Gương mặt Nỉ Thuần khiết & Đa dạng Tỷ lệ theo Độ tuổi (`Clean Felted Features & Proportional Silhouette`):**
  - Kiến tạo thần thái nhân vật ở mọi lứa tuổi hoàn toàn thông qua các đặc trưng thủ công mềm mại của chất liệu nỉ bông: chiếc mũi nỉ ửng hồng (`rosy felted nose`), đôi má nỉ ấm áp (`warm felt cheeks`), mái tóc và râu bằng sợi len dày có phom dáng đa dạng bắt sáng viền (`textured wool hair with glowing flyaway fibers`) kết hợp phụ kiện mũ, khăn hoặc kính gọng mảnh.
  - Linh hoạt điều chỉnh tỷ lệ hình thể theo nhân vật: ưu tiên tỷ lệ cao gầy, thanh mảnh nghệ thuật (`tall slender elongated artistic stop-motion proportions`) làm chủ đạo cho người trưởng thành và người lớn tuổi; kết hợp tỷ lệ cân đối thanh lịch hoặc tỷ lệ tròn trịa đáng yêu khi khắc họa trẻ nhỏ và nhân vật cổ tích.
- **Đồng bộ Cỡ cảnh, Liên kết Giải phẫu & Tư thế Có Điểm tựa (`Grounded Posture & Anatomical Continuity`):**
  - Ưu tiên cỡ cảnh trung-rộng toàn thân (`Full-body medium-wide / Medium shot`) và trung cận bán thân (`Waist-up / Chest-up medium close-up`) với tư thế ngồi, tựa hoặc vận động có trọng tâm thả lỏng tự nhiên, đôi tay gắn kết trực tiếp với đạo cụ hữu hình và có thể điểm xuyết sinh vật nhỏ bằng nỉ đồng hành hợp ngữ cảnh.
  - Ở cảnh thấy mặt sàn hoặc mặt đất, mô tả đầy đủ trang phục vải dạ/len dệt kim cùng đôi giày nỉ tiếp xúc vững chắc với bề mặt; ở cảnh đặc tả cục bộ (`Close-up / Detail shot`), mô tả trọn vẹn sự tiếp nối giải phẫu với phần cơ thể liền kề và điểm tiếp xúc vật lý vững chắc của vật thể trên mặt phẳng tựa.
- **Tương phản Ánh sáng Điện ảnh & Độ sâu Trường ảnh Macro (`Chiaroscuro & Macro Bokeh`):**
  - Thiết lập nguồn sáng có hướng và sự đối lập nhiệt độ màu rõ nét trong từng cảnh (ánh đèn vàng ấm nội thất đối lập với khung cửa chiều mưa hoặc chạng vạng xanh lạnh bên ngoài; nắng vàng ngược sáng làm rực sợi tơ len trên nền sương mù hoặc bóng râm dịu mát), tận dụng độ sâu trường ảnh nông của ống kính Macro 85mm để làm nổi bật kết cấu sợi len và chiều sâu sa bàn, tuân thủ [`ref/banned_lyrics_motifs.md`](../ref/banned_lyrics_motifs.md) (Mục 5).
