# ANIMATION CRAFT — KỸ THUẬT CHUYỂN ĐỘNG VIDEO (I2V)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào trực tiếp từ `image.txt` để xuất file `prompt-animate.txt`, điều khiển **chuyển động của ống kính một trục và hành động tiếp diễn của chủ thể trong 5 giây tiếp theo**. File `image.txt` đã khóa trọn vẹn tạo hình, tư thế gốc, vật dụng, màu sắc, chất liệu và bối cảnh ở giây 0.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

---

## 1. Quy chuẩn file `prompt-animate.txt` và 2 lớp điều khiển I2V

- **Định dạng xuất bản:** Mỗi câu lệnh nằm trọn vẹn trên **1 dòng duy nhất** trong `prompt-animate.txt`, xếp khớp đúng thứ tự từng bức ảnh tương ứng trong `image.txt`.
- **Cấu trúc hai lớp chuyển động:**

1. **Lớp 1 — Bảy quỹ đạo ống kính một trục theo ý đồ cảnh (`Motivated 1-Axis Camera`) và nhịp thở khung hình:**
   - **Nguyên tắc chọn máy một trục:** Mỗi câu chọn **1 hướng chuyển động đơn nhất** lấy chủ thể hoặc tâm điểm tương tác làm tâm, khớp với hoạt động trong ảnh và luân chuyển đa dạng giữa các cảnh liền kề ($N \to N+1$):
     1. **Giữ khung quan sát (`holds on X` / `lingers on X`):** Máy đứng tại chỗ như ánh mắt người quan sát, dành trọn sự tập trung cho cử chỉ tương tác và biểu cảm của chủ thể.
     2. **Tiến lại gần (`moves closer to X`):** Đẩy nhẹ vào thần thái gương mặt hoặc thao tác tay của chủ thể.
     3. **Lùi ra xa (`pulls back from X`):** Mở rộng không gian cảnh quan xung quanh chủ thể.
     4. **Trượt ngang tạo chiều sâu (`glides sideways past X` / `drifts laterally past X`):** Trượt ngang qua chủ thể để làm nổi bật độ sâu giữa tiền cảnh và hậu cảnh.
     5. **Nâng theo chiều dọc (`rises alongside X` / `cranes up past X`):** Nâng máy lên theo nhịp mở của không gian.
     6. **Xoay vòng cung (`arcs around X`):** Đi vòng cung quanh chủ thể để mở góc nhìn ba chiều.
     7. **Bám song song (`moves alongside X`):** Đi kèm cùng tốc độ khi chủ thể đang di chuyển trên tuyến đường cảnh quan.
   - **Nhịp thở khung hình tự nhiên theo trạng thái máy:**
     - *Khi giữ khung tại chỗ:* `Unstabilized camera [holds on / lingers on] [X], the frame breathing with natural motion.`
     - *Khi di chuyển máy một trục:* `Unstabilized camera [1-axis verb] [X], the frame swaying with natural motion.`
     - *Khi bám song song theo chủ thể đang bước đi hoặc di chuyển:* `Unstabilized tracking camera moves alongside [X], the frame visibly bobbing and swaying.`

2. **Lớp 2 — Hành động tiếp diễn liên tục và biểu cảm điềm tĩnh tự nhiên (`Continuous Mid-Action & Calm Natural Tail`):**
   - **Với cảnh có người:** Gọi chủ thể bằng danh từ chỉ người ngắn gọn khớp với ảnh gốc. Mô tả trực tiếp sự tiếp diễn mượt mà của đúng hoạt động thực tế và tương tác nhân-quả đang diễn ra tại vị trí hiện tại suốt 5 giây, kết hợp động từ biểu cảm điềm đạm, ấm áp và khép câu bằng đuôi cố định: **`, while facial expressions and everything around move naturally.`**
   - **Với cảnh cận cảnh tĩnh vật (`B-roll`):** Lấy vật thể trung tâm trong ảnh làm chủ thể, mô tả chuyển động vật lý tự nhiên tại chỗ của vật thể cùng môi trường và khép câu bằng đuôi: **`, while everything around moves naturally.`**

---

## 2. Nguyên lý bảo toàn hình thái và tính liên tục 5 giây

1. **Ngôn ngữ chuyển động trực tiếp và rõ lực:** Sử dụng các động từ hành động trực diện ở thì hiện tại đơn để duy trì nhịp chuyển động sống động, ổn định từ giây đầu đến giây thứ 5.
2. **Duy trì hoạt động tại không gian hiện hữu:** Giữ các chủ thể tương tác và cử động liên tục ngay trong vùng không gian của bức ảnh gốc, đảm bảo dòng chảy thị giác liền mạch xuyên suốt thời lượng cảnh.
3. **Tập trung thuần túy vào động học:** Dành toàn bộ dung lượng câu lệnh cho quỹ đạo máy quay và chuyển động vật lý của chủ thể, để bức ảnh gốc trong `image.txt` tự đảm nhận toàn bộ thông tin về chất liệu, trang phục và ánh sáng.

---

## 3. Khung câu lệnh chuẩn cho `prompt-animate.txt`

Mỗi dòng trong `prompt-animate.txt` gói gọn trong `25–35 từ` theo 3 mẫu quỹ đạo ống kính:

```text
# 1. Giữ khung quan sát tại chỗ:
Unstabilized camera [holds on / lingers on] [X], the frame breathing with natural motion. [Chủ thể tiếp tục hoạt động tương tác thực tế], while [facial expressions and ]everything around move[s] naturally.

# 2. Di chuyển máy 1 trục (Tiến / Lùi / Trượt ngang / Nâng dọc / Xoay vòng):
Unstabilized camera [moves closer to / pulls back from / glides sideways past / rises alongside / arcs around] [X], the frame swaying with natural motion. [Chủ thể tiếp tục hoạt động tương tác thực tế], while [facial expressions and ]everything around move[s] naturally.

# 3. Bám song song theo chủ thể đang di chuyển:
Unstabilized tracking camera moves alongside [X], the frame visibly bobbing and swaying. [Chủ thể tiếp tục di chuyển và tương tác], while [facial expressions and ]everything around move[s] naturally.
```
