# ANIMATION CRAFT — KỸ THUẬT CHUYỂN ĐỘNG VIDEO (I2V)

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào trực tiếp từ `image.txt` để xuất file `prompt-animate.txt`, chỉ điều khiển **chuyển động của ống kính 1 trục và hành động tiếp diễn của chủ thể trong 5 giây tiếp theo**. File `image.txt` đã khóa 100% tạo hình, tư thế gốc, đạo cụ, màu sắc, chất liệu và bối cảnh ở giây 0; file này không can thiệp lại các yếu tố tĩnh đó.
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. **Sửa đúng chỗ (`/ponytail`):** Chỉ sửa đúng dòng cần thay đổi bằng công cụ chỉnh sửa cục bộ, ưu tiên ngắn gọn, không ghi đè toàn bộ file.
>   2. **Chỉ viết quy luật, không đưa ví dụ bối cảnh cụ thể:** Tránh làm mồi nhử khiến AI lặp lại đạo cụ hoặc bối cảnh mẫu.

## 1. Quy chuẩn file `prompt-animate.txt` & 2 Lớp quản lý của I2V

- **Định dạng:** Mỗi prompt nằm trọn vẹn trên **1 dòng duy nhất** trong `prompt-animate.txt` (không đánh số thứ tự, không tiêu đề, không dòng trống), khớp đúng thứ tự các bức ảnh cần tạo chuyển động từ `image.txt`.
- **Chỉ quản lý đúng 2 lớp + 1 câu chốt tự do:**

1. **Lớp 1 — 7 Quỹ đạo Ống kính theo Ý đồ Cảnh (Motivated 1-Axis Camera) & Nhịp thở Khung hình:**
   - **Nguyên tắc chọn máy (Motivated Camera & Cân bằng nhịp điệu):** Mỗi câu chỉ chọn **1 hướng đơn nhất** lấy nhân vật/tâm điểm làm tâm, khớp với hành động trong ảnh. Phân bổ đa dạng các kiểu máy trên toàn video (không lặp cùng 1 kiểu máy ở 2 câu liên tiếp):
     1. **Giữ khung quan sát (`holds on X` / `lingers on X`):** Máy đứng yên tại chỗ như ánh mắt người nhìn, nhường trọn sự chú ý cho cử chỉ và nét mặt của chủ thể.
     2. **Tiến lại gần (`moves closer to X`):** Đẩy vào cảm xúc gương mặt hoặc chi tiết thao tác của chủ thể.
     3. **Lùi ra xa (`pulls back from X`):** Mở rộng không gian xung quanh chủ thể.
     4. **Trượt ngang Parallax (`glides sideways past X` / `drifts laterally past X`):** Trượt ngang qua chủ thể tạo chiều sâu 3D giữa tiền cảnh và hậu cảnh.
     5. **Nâng theo chiều dọc (`rises alongside X` / `cranes up past X`):** Nâng máy lên theo chuyển động hướng lên hoặc mở toàn cảnh.
     6. **Xoay vòng cung (`arcs around X`):** Đi vòng cung quanh chủ thể để mở góc nhìn không gian ba chiều.
     7. **Bám song song (`moves alongside X`):** Đi kèm cùng tốc độ khi chủ thể hoặc phương tiện đang di chuyển.
   - **Nhịp thở khung hình đúng vật lý đời thực (Không dùng từ vựng cơ thể người, không ép cảnh đứng yên phải nhấp nhô `bobbing`):**
     - *Khi giữ khung tại chỗ (`holds on` / `lingers on`):* `Unstabilized camera [holds on / lingers on] [X], the frame breathing with natural motion.`
     - *Khi di chuyển máy 1 trục (`moves closer to` / `pulls back from` / `glides sideways past` / `rises alongside` / `arcs around`):* `Unstabilized camera [động từ 1 trục] [X], the frame swaying with natural motion.`
     - *Khi bám song song theo chủ thể đang di chuyển (`moves alongside`):* `Unstabilized tracking camera moves alongside [X], the frame visibly bobbing and swaying.`
   - **Cấm** gộp 2 trục (`arcs around AND tilts up`, `moves closer AND pans`) và **cấm** lia từ đạo cụ nhỏ sang người (`from [đạo cụ A] to [người B]`).

2. **Lớp 2 — Hành động Tiếp diễn, Biểu cảm Điềm tĩnh Tự nhiên & Đuôi Tự nhiên (Mid-Action & Natural Tail):**
   - **Với cảnh có người:** Gọi chủ thể bằng danh từ chỉ người thật theo đúng ảnh gốc (`the man`, `the woman`, `the artisan`, `the couple`). Chỉ tả sự tiếp diễn của đúng hành động và đạo cụ/phương tiện mà nhân vật đang trực tiếp thao tác trong ảnh, kết hợp động từ biểu cảm điềm đạm, chừng mực (`nods warmly`, `watches attentively`, `glances over and smiles`, `gazes out serenely`, `shares a calm smile` — tránh các động từ biểu cảm lố gây méo miệng). Kết câu bằng đuôi cố định: **`, while facial expressions and everything around move naturally.`**
   - **Với cảnh tĩnh vật / không gian không người:** Lấy vật thể trung tâm hoặc khung cảnh thiên nhiên trong ảnh làm chủ thể. Tả chuyển động vật lý tự nhiên đang diễn ra của vật thể đó và đóng lại bằng đuôi: **`, while everything around moves naturally.`** (bỏ chữ `facial expressions` vì cảnh không có người).
   - **Cấm** bịa thêm đạo cụ/nhân vật không có trong ảnh gốc, **cấm** hành động tuần tự đổi đạo cụ (*làm việc A rồi chuyển sang làm việc B*), và **cấm** tả lại từ đầu một trạng thái đã hoàn tất trong ảnh.

## 2. Khu vực cấm tối thiểu (Hard Bans)

- **Cấm từ vựng cơ thể người trong Camera & Cấm chỉ đạo chi tiết tay / ngón tay (Chặn lỗi thò tay POV & mọc thêm tay):** Tuyệt đối không dùng `hand`, `hands`, `handheld`, `hand-in-hand`, `hand over hand`, `raw hand movement`, `with one hand`, `with the other`, `with both hands`, `fingers`, `palms`, `thumb`, `arm`, `arms`, `arm-in-arm`, `left arm`, `right arm`, `elbow`, `elbows`, `footstep`, `footsteps`.
- **Cấm từ khóa biểu cảm lố / cường điệu làm biến dạng miệng và hàm trong I2V:** Không dùng `laughs aloud`, `laughs heartily`, `laughs cheerfully`, `grins wide`, `wide grin`, `beams with joy`, `cheers`, `shouts`, `screams`, `excitedly`, `wildly`, `throws head back`.
- **Cấm động từ biến hình trong I2V (Chặn lỗi chảy nhão vật thể có sẵn):** Tuyệt đối không dùng `transforms into`, `unfurls into`, `unfolds into`, `folds into`, `shapes itself into`, `blossoms into`, `materializes into`, `forms`, `turns into`.
- **Cấm từ giảm lực làm đơ ảnh & Cấm từ rung giật cực đoan gây nhòe nét:** Không dùng `light`, `very light`, `slightly`, `subtly`, `subtle`, `gently`, `slowly`, `quietly`, `standing still`, `steady`, `smooth`, `smoothly`; không dùng `shaking heavily`, `tilting heavily`, `shaky`, `shaking`.
- **Cấm tả lại chất liệu & màu sắc tĩnh của ảnh:** Không nhắc lại chất liệu thủ công (`paper-pulp`, `clay`, `felt`, `cotton-fiber`, `linen`, `oak`, `brass`, `wooden`, `ceramic`, `leather`, `stone`, `canvas`, `silk`) hay màu sắc trong prompt animation.
- **Cấm thiết bị điện tử & công nghệ cao:** Không dùng `smartphone, tablet, iPad, laptop, digital, electronic, headphones, microphone, espresso machine, laser, wireless`.
- **Cấm trượt ray máy móc, con rối, ánh sáng phép thuật & câu phủ định:** Không dùng `steadycam, dolly, drone`; không dùng `puppet, figurine, doll, statue, stop-motion`; không dùng `glowing, sparkles, fairy dust, magical aura, bioluminescent`; không viết câu phủ định (`no cuts, no morphing`).

## 3. Công thức Prompt Chuẩn I2V (Bắt buộc)

Mỗi dòng trong `prompt-animate.txt` gói gọn trong 25–35 từ theo đúng mẫu vật lý ống kính:

```text
# 1. Giữ khung quan sát tại chỗ:
Unstabilized camera [holds on / lingers on] [X], the frame breathing with natural motion. [Chủ thể tiếp tục chuyển động], while [facial expressions and ]everything around move[s] naturally.

# 2. Di chuyển máy 1 trục (Tiến / Lùi / Trượt ngang / Nâng dọc / Xoay vòng):
Unstabilized camera [moves closer to / pulls back from / glides sideways past / rises alongside / arcs around] [X], the frame swaying with natural motion. [Chủ thể tiếp tục chuyển động], while [facial expressions and ]everything around move[s] naturally.

# 3. Bám song song theo chủ thể đang di chuyển:
Unstabilized tracking camera moves alongside [X], the frame visibly bobbing and swaying. [Chủ thể tiếp tục di chuyển], while [facial expressions and ]everything around move[s] naturally.
```
