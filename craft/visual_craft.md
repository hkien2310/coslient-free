# VISUAL CRAFT
Viết thẳng prompt vào `image.txt`. Số lượng tùy độ dài bài. Chất liệu, khung hình, suffix: theo file style trong `style/`. Bẫy từ khóa: `style/IMAGE_AVOID_CASES.md`.

Chỉ có hai tiêu chí. Mọi thứ khác (cảnh nào, thứ tự nào, bám lời bao nhiêu) tự quyết.

## 1. Không chán (đa dạng)
- Nguồn cảnh: idea, lời bài, nhạc. Với mỗi thứ được nhắc trong lời, nghĩ thêm thế giới quanh nó (cạnh, trước, sau, ngoài cửa) để có thêm cảnh.
- Đổi nhiều trục giữa các ảnh: cỡ cảnh, độ cao và hướng máy, bố cục, chủ thể (người, thú, đồ vật, cảnh vắng), nơi chốn, hành động, giờ và thời tiết. Thỉnh thoảng phá tỷ lệ.
- Một vật hoặc một chỗ xuất hiện tối đa 2 lần trong video. Không ba ảnh liền giống nhau ở cùng một trục.
- Khác video liền trước về nơi chốn chính, giờ chủ đạo và nhân vật chính.

## 2. Không đánh nhau với nhạc (xịn)
- Ảnh phải hợp cảm xúc và nhịp của bài, không gây giật mình hay lạc tông. Ảnh ồn ào, sắc, tối gắt thì tránh khi bài êm.
- Chất lượng theo style: đúng chất liệu, ánh sáng có hướng, nét đúng chỗ.

Format cho tool: mỗi prompt một dòng, giữa hai prompt một dòng trống, không `--no`, kết thúc bằng `--ar 16:9`.
