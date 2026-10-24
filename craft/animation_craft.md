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

1. **Lớp 1 — Tám kỹ thuật ống kính một trục với chủ ngữ `The camera` rõ ràng (`Explicit Camera Subject & Motivated 1-Axis Motion`):**
   - **Nguyên tắc chủ ngữ máy quay tường minh và đích khung hình (`Explicit Camera Subject & Target Framing`):** Luôn mở đầu câu lệnh bằng chủ ngữ tường minh `The camera` hoặc `Unstabilized camera` kết hợp động từ di chuyển một trục trực diện và đích mở khung hình (`from [X] to [Y]`, `keeping [X] centered`, `at the same pace`, `until [Y] comes into view`), luân chuyển đa dạng giữa các cảnh liền kề ($N \to N+1$) với tiêu cự ổn định xuyên suốt cảnh:
     1. **Giữ khung quan sát ổn định (`The camera holds steady on X` / `The camera lingers on X`):** Máy giữ nguyên vị trí và mặt phẳng nét như ánh mắt người quan sát, dành trọn sự tập trung cho cử chỉ tương tác và biểu cảm của chủ thể.
     2. **Lia ngang trên trục cố định (`The camera pans slowly across from [X] to [Y]`):** Thân máy đứng tại chỗ và xoay trục ngang êm ái để mở lộ không gian kế cận hoặc kết nối hai chủ thể trong cảnh.
     3. **Ngẩng hoặc hạ dọc trên trục cố định (`The camera tilts gently up / down from [X] to [Y]`):** Thân máy đứng tại chỗ và xoay trục dọc mượt mà từ thao tác chi tiết lên gương mặt hoặc vòm không gian phía trên.
     4. **Tiến lại gần (`The camera moves slowly closer to X`):** Thân máy tiến nhẹ về phía thần thái gương mặt hoặc thao tác tay của chủ thể.
     5. **Lùi ra xa (`The camera pulls slowly back from X to reveal Y`):** Thân máy lùi dần để mở rộng không gian cảnh quan bao quanh chủ thể.
     6. **Trượt ngang tạo chiều sâu (`The camera glides laterally past X`):** Thân máy trượt ngang qua chủ thể để làm nổi bật độ sâu thị sai giữa tiền cảnh và hậu cảnh.
     7. **Nâng theo chiều dọc (`The camera rises gently alongside X until [Y] comes into view`):** Thân máy nâng lên êm ái theo nhịp mở của không gian cảnh quan.
     8. **Đi vòng quanh hoặc bám song song (`The camera circles gently around X keeping them centered` / `Unstabilized camera moves alongside X at the same pace`):** Thân máy đi theo đường cong nhẹ quanh chủ thể để mở góc nhìn ba chiều, hoặc đi kèm cùng tốc độ khi chủ thể đang di chuyển trên tuyến đường cảnh quan.
   - **Nhịp thở khung hình linh hoạt theo trạng thái máy (`Natural Frame Breathing`):**
     - *Khi giữ khung hoặc xoay trục tại chỗ:* `The camera [holds steady on X / lingers on X / pans slowly across from X to Y / tilts gently up from X to Y], the frame breathing with natural motion.`
     - *Khi tịnh tiến thân máy một trục:* `The camera [moves slowly closer to X / pulls slowly back from X to reveal Y / glides laterally past X / rises gently alongside X until Y comes into view / circles gently around X keeping them centered], the frame swaying with natural motion.`
     - *Khi bám song song theo chủ thể đang bước đi hoặc di chuyển:* `Unstabilized camera moves alongside [X] at the same pace, the frame visibly bobbing and swaying.`

2. **Lớp 2 — Động học cơ thể mềm mại, tương tác cảm xúc hai chiều và biểu cảm tự nhiên (`Fluid Human Kinematics, Reciprocal Affection & Calm Natural Tail`):**
   - **Với cảnh có người:** Gọi chủ thể bằng danh từ chỉ người ngắn gọn khớp với ảnh gốc. Từ tư thế khởi đầu ở giây 0 trong ảnh, mô tả một chuyển động tiếp diễn liền mạch với trọng lượng cơ thể tự nhiên, bờ vai thả lỏng và khớp tay uyển chuyển như người thật (`with fluid, unhurried motion`, `gently shifting weight`, `smoothly`). Khi cảnh có từ hai nhân vật trở lên, diễn tả rõ sự giao cảm và hưởng ứng qua lại giữa họ trong 5 giây (ánh mắt nhìn nhau ấm áp, nghiêng đầu lắng nghe rồi mỉm cười gật đầu thấu hiểu, bàn tay vỗ nhẹ hoặc cử chỉ yêu thương chăm sóc tiếp diễn êm ái), và khép câu bằng đuôi cố định: **`, while facial expressions and everything around move naturally.`**
   - **Với cảnh cận cảnh tĩnh vật (`B-roll`):** Lấy vật thể trung tâm trong ảnh làm chủ thể, mô tả chuyển động vật lý tự nhiên phát triển êm ái từ trạng thái mở đầu của vật thể cùng môi trường và khép câu bằng đuôi: **`, while everything around moves naturally.`**

---

## 2. Nguyên lý bảo toàn hình thái và tính liên tục 5 giây

1. **Ngôn ngữ chuyển động mềm mại và liền mạch:** Sử dụng các động từ hành động ở thì hiện tại đơn đi kèm trạng từ chỉ sự khoan thai, uyển chuyển để dẫn dắt một hành động xuyên suốt 5 giây với quán tính tự nhiên của cơ thể người.
2. **Duy trì hoạt động tại không gian hiện hữu:** Giữ các chủ thể tương tác và cử động liên tục ngay trong vùng không gian và mặt phẳng lấy nét ổn định của bức ảnh gốc, đảm bảo dòng chảy thị giác liền mạch xuyên suốt thời lượng cảnh.
3. **Tập trung thuần túy vào động học:** Dành toàn bộ dung lượng câu lệnh cho chuyển động của `The camera` và cử chỉ mềm mại của chủ thể, để bức ảnh gốc trong `image.txt` tự đảm nhận toàn bộ thông tin về chất liệu, trang phục và ánh sáng.

---

## 3. Khung câu lệnh chuẩn cho `prompt-animate.txt`

Mỗi dòng trong `prompt-animate.txt` viết súc tích theo 3 nhóm trạng thái ống kính:

```text
# 1. Giữ khung quan sát ổn định hoặc xoay trục tại chỗ:
The camera [holds steady on X / lingers on X / pans slowly across from X to Y / tilts gently up from X to Y], the frame breathing with natural motion. [Chủ thể thực hiện hành động liền mạch với chuyển động cơ thể mềm mại, khoan thai], while [facial expressions and ]everything around move[s] naturally.

# 2. Tịnh tiến thân máy 1 trục có đích ngắm:
The camera [moves slowly closer to X / pulls slowly back from X to reveal Y / glides laterally past X / rises gently alongside X until Y comes into view / circles gently around X keeping them centered], the frame swaying with natural motion. [Chủ thể thực hiện hành động liền mạch với chuyển động cơ thể mềm mại, khoan thai], while [facial expressions and ]everything around move[s] naturally.

# 3. Bám song song cùng nhịp di chuyển của chủ thể:
Unstabilized camera moves alongside [X] at the same pace, the frame visibly bobbing and swaying. [Chủ thể di chuyển và tương tác với nhịp cơ thể mềm mại, khoan thai], while [facial expressions and ]everything around move[s] naturally.
```
