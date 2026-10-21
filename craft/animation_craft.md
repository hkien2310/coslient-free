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

1. **Lớp 1 — Chín kỹ thuật ống kính một trục có đích ngắm (`Motivated 1-Axis Camera & Focus`) và nhịp thở khung hình:**
   - **Nguyên tắc chọn máy một trục và định rõ đích khung hình (`Target Framing`):** Mỗi câu chọn **1 kỹ thuật ống kính đơn nhất** khớp với hoạt động trong ảnh, chỉ rõ điểm neo hoặc đích mở khung hình (`from [X] to [Y]`, `keeping [X] centered`, `at the same pace`, `until [Y] comes into view`) và luân chuyển đa dạng giữa các cảnh liền kề ($N \to N+1$):
     1. **Giữ khung quan sát (`holds on X` / `lingers on X`):** Máy giữ nguyên vị trí như ánh mắt người quan sát, dành trọn sự tập trung cho cử chỉ tương tác và biểu cảm của chủ thể.
     2. **Chuyển điểm lấy nét chiều sâu (`Rack focus: focus shifts smoothly from [near X] to [far Y]`):** Máy giữ nguyên vị trí và dịch chuyển mặt phẳng lấy nét mượt mà giữa lớp tiền cảnh và hậu cảnh để kết nối hai tầng không gian.
     3. **Lia ngang trên trục cố định (`Pan: pans slowly across from [X] to [Y]`):** Thân máy đứng tại chỗ và xoay trục ngang êm ái để mở lộ không gian kế cận hoặc kết nối hai chủ thể trong cảnh.
     4. **Ngẩng hoặc hạ dọc trên trục cố định (`Tilt: tilts gently up / down from [X] to [Y]`):** Thân máy đứng tại chỗ và xoay trục dọc mượt mà từ thao tác chi tiết lên gương mặt hoặc vòm không gian phía trên.
     5. **Tiến lại gần (`Dolly in: moves closer to X` / `slow dolly in toward X`):** Thân máy tiến nhẹ về phía thần thái gương mặt hoặc thao tác tay của chủ thể.
     6. **Lùi ra xa (`Dolly out: pulls back from X` / `slow dolly out from X`):** Thân máy lùi dần để mở rộng không gian cảnh quan bao quanh chủ thể.
     7. **Trượt ngang tạo chiều sâu (`Truck: glides sideways past X` / `drifts laterally past X`):** Thân máy trượt ngang qua chủ thể để làm nổi bật độ sâu thị sai giữa tiền cảnh và hậu cảnh.
     8. **Nâng theo chiều dọc (`Crane: rises alongside X` / `cranes up until the wider [Y] comes into view`):** Thân máy nâng lên theo nhịp mở của không gian cảnh quan.
     9. **Xoay vòng cung hoặc bám song song (`Arc & Tracking: arcs around X keeping them centered` / `moves alongside X at the same pace`):** Thân máy đi vòng cung giữ chủ thể ở tâm khung hình để mở góc nhìn ba chiều, hoặc đi kèm cùng tốc độ khi chủ thể đang di chuyển trên tuyến đường cảnh quan.
   - **Nhịp thở khung hình linh hoạt theo trạng thái máy (`Flexible Camera Opening & Natural Breathing`):** Mở đầu câu lệnh linh hoạt bằng tên kỹ thuật ống kính trực tiếp hoặc cụm `Unstabilized camera`, kết hợp nhịp thở vật lý tự nhiên tương ứng:
     - *Khi giữ khung, chuyển nét (`Rack focus`) hoặc xoay trục tại chỗ (`Pan` / `Tilt`):* `[Unstabilized camera / Steady camera] [holds on X / shifts focus smoothly from X to Y / pans slowly from X to Y / tilts gently up from X to Y], the frame breathing with natural motion.`
     - *Khi tịnh tiến thân máy một trục (`Dolly` / `Truck` / `Crane` / `Arc`):* `[Unstabilized camera / Slow dolly / Gentle crane / Smooth arc] [1-axis verb + target framing], the frame swaying with natural motion.`
     - *Khi bám song song theo chủ thể đang bước đi hoặc di chuyển (`Tracking`):* `[Unstabilized tracking camera / Smooth side-tracking shot] moves alongside [X] at the same pace, the frame visibly bobbing and swaying.`

2. **Lớp 2 — Triển khai hành động từ tư thế khởi đầu và biểu cảm điềm tĩnh tự nhiên (`Action Execution from Onset & Calm Natural Tail`):**
   - **Với cảnh có người:** Gọi chủ thể bằng danh từ chỉ người ngắn gọn khớp với ảnh gốc. Từ tư thế khởi đầu ở giây 0 trong ảnh, mô tả trực tiếp quá trình thực hiện mượt mà thao tác thực tế và tương tác phối hợp đó diễn ra suốt 5 giây tiếp theo, kết hợp động từ biểu cảm điềm đạm, ấm áp và khép câu bằng đuôi cố định: **`, while facial expressions and everything around move naturally.`**
   - **Với cảnh cận cảnh tĩnh vật (`B-roll`):** Lấy vật thể trung tâm trong ảnh làm chủ thể, mô tả chuyển động vật lý tự nhiên phát triển từ trạng thái mở đầu của vật thể cùng môi trường và khép câu bằng đuôi: **`, while everything around moves naturally.`**

---

## 2. Nguyên lý bảo toàn hình thái và tính liên tục 5 giây

1. **Ngôn ngữ chuyển động trực tiếp và rõ lực:** Sử dụng các động từ hành động trực diện ở thì hiện tại đơn để duy trì nhịp chuyển động sống động, ổn định từ giây đầu đến giây thứ 5.
2. **Duy trì hoạt động tại không gian hiện hữu:** Giữ các chủ thể tương tác và cử động liên tục ngay trong vùng không gian của bức ảnh gốc, đảm bảo dòng chảy thị giác liền mạch xuyên suốt thời lượng cảnh.
3. **Tập trung thuần túy vào động học:** Dành toàn bộ dung lượng câu lệnh cho quỹ đạo máy quay và chuyển động vật lý của chủ thể, để bức ảnh gốc trong `image.txt` tự đảm nhận toàn bộ thông tin về chất liệu, trang phục và ánh sáng.

---

## 3. Khung câu lệnh chuẩn cho `prompt-animate.txt`

Mỗi dòng trong `prompt-animate.txt` gói gọn trong `25–38 từ` theo 3 nhóm trạng thái ống kính:

```text
# 1. Giữ khung quan sát, chuyển nét chiều sâu (Rack focus) hoặc xoay trục tại chỗ (Pan / Tilt):
[Unstabilized camera / Steady camera] [holds on X / lingers on X / shifts focus smoothly from near X to far Y / pans slowly across from X to Y / tilts gently up from X to Y], the frame breathing with natural motion. [Chủ thể tiếp tục hoạt động tương tác thực tế], while [facial expressions and ]everything around move[s] naturally.

# 2. Tịnh tiến thân máy 1 trục có đích ngắm (Dolly / Truck / Crane / Arc):
[Unstabilized camera / Slow dolly / Gentle crane / Smooth arc] [moves closer to X / pulls back from X / glides sideways past X / rises alongside X until Y comes into view / arcs around X keeping them centered], the frame swaying with natural motion. [Chủ thể tiếp tục hoạt động tương tác thực tế], while [facial expressions and ]everything around move[s] naturally.

# 3. Bám song song cùng nhịp di chuyển của chủ thể (Tracking):
[Unstabilized tracking camera / Smooth side-tracking shot] moves alongside [X] at the same pace, the frame visibly bobbing and swaying. [Chủ thể tiếp tục di chuyển và tương tác], while [facial expressions and ]everything around move[s] naturally.
```
