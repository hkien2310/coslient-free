# Music craft

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` để thiết kế âm nhạc (`Style prompt`), sáng tác lời bài hát theo đúng Chế độ Kể chuyện đã chọn và xuất ra `2-music.md`, `3-lyrics.txt` cùng cập nhật `ref/lyrics-index.md`. Không chứa quy tắc tạo hình nhân vật (`character.md`), chia cảnh (`storyboard.md`) hay câu lệnh sinh ảnh (`image.txt`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## Nguyên tắc ngôn ngữ & Độ mở cảm xúc

1. **Khẩu ngữ văn nói đời thường:** Ca từ vận hành theo lời ăn tiếng nói tự nhiên của cuộc trò chuyện thân tình. Tùy mạch cảm xúc từng bài, chọn lọc điểm xuyết các nét khẩu ngữ như nhịp lấy đà hội thoại đầu câu, tỉnh lược chủ ngữ theo thói quen nói, cấu trúc nêu danh từ trước rồi nhắc lại bằng đại từ, hoặc câu lời thoại trực tiếp ngắn gọn.
2. **Lược âm mềm và Từ vựng giàu nguyên âm mở:** Ưu tiên từ đơn âm tiết hoặc hai âm tiết thông dụng và giàu nguyên âm mở để giọng hát dễ ngân nga; điểm xuyết vừa phải các dạng rút gọn âm tiết khẩu ngữ tự nhiên tại vị trí cần lướt nhịp mềm mại.
3. **Nhịp thở hội thoại và Điệp từ nhấn nhịp:** Giữ trật tự từ thuận theo lời nói và nhịp lấy hơi tự nhiên; tùy giai điệu từng bài, chọn dùng câu vắt dòng, cụm đoản ngữ song hành, điệp từ nhịp bước hoặc lặp đúp cụm từ ngắn tại điểm rơi thích hợp.
4. **Điểm nhìn ca từ theo Hai Chế độ Kể chuyện:**
   - **Chế độ 1 — Kể chuyện Cá nhân:** Ca từ xuất phát từ điểm nhìn tự sự trực tiếp hoặc đối thoại tâm tình ở ngôi thứ nhất và ngôi thứ hai, neo vào mối gắn kết bền bỉ qua các chặng thời gian hoặc thói quen sinh hoạt quen thuộc, đồng thời gợi mở ký ức qua tín hiệu giác quan tinh tế để bồi đắp tầng ý nghĩa mới cho điệp khúc sau mỗi lần lặp.
   - **Chế độ 2 — Ý niệm / Đa diện:** Ca từ xoay quanh một hạt nhân ý niệm, dấu ấn thời gian hoặc trạng thái tâm hồn chung với góc nhìn thấu cảm rộng mở ở ngôi thứ ba, đại từ phiếm chỉ hoặc điểm nhìn bao dung của không gian gắn bó; khắc họa các lát cắt đời sống độc lập và suy ngẫm phổ quát ở từng phân đoạn để cùng hội tụ về câu chủ đề ở điệp khúc.
5. **Độ hạt ký ức và Dấu vết vật lý:** Truyền tải tình cảm, sự gắn bó và bước đi của năm tháng qua danh từ vật lý xác thực, độ mòn tự nhiên của chất liệu theo thời gian, nhịp vận động cơ thể đặc trưng của tuổi xế chiều và khoảng lặng âm nhạc giàu sức gợi.
6. **Tương phản giác quan tôn vinh sự ấm áp:** Đặt hơi ấm, ánh sáng dịu và sự tĩnh tại của không gian bên trong song hành cùng nhịp chuyển động của thời tiết, khoảng rộng đất trời hoặc dòng thời gian bên ngoài để làm nổi bật cảm giác bình yên, che chở.
7. **Chiêm nghiệm nghịch lý dịu dàng & Định nghĩa mới về thời gian:** Tái định nghĩa dấu vết tuổi tác và nhịp sống chậm rãi thành sự chín muồi, lòng thủy chung và sự bình yên tự chủ thông qua đối sánh tương quan giữa quy luật tự nhiên với đời người, góc nhìn đảo chiều giàu chất thơ và các cặp mệnh đề cân xứng.
8. **Phân bổ vai trò giữa Lời hát và Hình ảnh:** Đặt tâm tình, nhịp sống, tín hiệu gợi mở và chiêm nghiệm phổ quát vào lời bài hát; giao phần diễn giải trực diện hoạt cảnh và chuỗi thao tác cụ thể cho bảng phân cảnh hình ảnh (`storyboard.md`).
9. **Bộ chuẩn hóa văn phong:** Áp dụng bắt buộc [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md) và [`ref/banned_lyrics_motifs.md`](file:///Users/hoangkien/Youtube/coslient-free/ref/banned_lyrics_motifs.md).

## Input / Output & Quy tắc Định danh Bài hát

- **Input:** `1-idea.md`, `ref/lyrics-index.md`, `ref/banned_lyrics_motifs.md`, `ref-real-music/index.md` (tùy chọn tham khảo).
- **Output:**
  - `projects/XXX/2-music.md`: 2 track, mỗi track gồm tên bài, style prompt, exclude, lyrics có thẻ điều phối.
  - `track-N-<track-title-slug>/3-lyrics.txt`: lời sạch cho DistroKid.
  - Cập nhật `ref/lyrics-index.md`.
- **Quy tắc Đặt tên Bài hát & Đồng bộ Định danh:**
  1. **Tên bài hát:** Đặt tên tiếng Anh từ 3 đến 6 từ bằng từ vựng giản dị, giàu chất thơ; trích xuất từ mệnh đề trọng tâm của câu chủ đề trong điệp khúc hoặc đặt bằng mệnh đề bao quát linh hồn bài hát.
  2. **Đồng bộ Định danh 1:1:** Tên bài hát tại `1-idea.md`, tiêu đề `## Track N: [Track Title]` trong `2-music.md`, tên thư mục con `track-N-<track-title-slug>/` (chữ thường nối gạch ngang) và cột tên bài trong `ref/lyrics-index.md` đồng nhất hoàn toàn với nhau.

## Dự án & Kiến trúc thời lượng

- **Quy mô:** 2 bài / project, chung chủ đề và chung nền tảng âm nhạc.
- **Thời lượng mục tiêu:** Mỗi bài đạt từ 4 phút trở lên thông qua kiến trúc âm nhạc và các khoảng thở khí nhạc.
- **Khung cấu trúc tự do 4 phút+:** Linh hoạt lựa chọn theo mạch cảm xúc từng bài giữa:
  - **Cấu trúc Điệp khúc Mở rộng:** `Intro (12–20s mở không gian ấm áp) -> Verse 1 -> (Pre-Chorus tùy chọn) -> Chorus 1 -> Interlude -> Verse 2 -> (Pre-Chorus tùy chọn) -> Chorus 2 -> Instrumental Solo (15–30s nhạc cụ đối thoại) -> Bridge -> Final Chorus -> Outro (20–35s ngân nga và nhạc cụ mộc lắng dần)`.
  - **Cấu trúc Khổ thơ Câu chốt Dân gian:** Các khổ thơ tự sự nối tiếp nhau qua những khoảng thở khí nhạc, mỗi khổ tự khép lại bằng câu điệp chủ đề ở dòng cuối và mở rộng hòa âm tại đoạn chuyển hoặc điệp khúc kết tinh.

## Thể loại, Hòa âm & Giọng hát

- **Thể loại & Giao thoa Điệu thức:** Nền Acoustic Folk chủ đạo kết hợp tối đa 1 nhánh phụ phù hợp với ý tưởng (khi kết hợp nhánh Acoustic Blues, luôn triển khai kỹ thuật mộc ở giọng trưởng cùng nhịp điệu thong thả để bảo toàn cảm giác ấm áp ngay từ đầu bài). Linh hoạt vận dụng giọng trưởng ấm áp, hệ dây mở giàu âm bồi hoặc thủ pháp giao thoa Thứ – Trưởng tương đương cùng các hợp âm mở rộng để chuyển hóa chiều sâu hoài niệm ở khổ hát sang độ mở hòa âm tươi sáng, bình yên ở điệp khúc.
- **Nhịp điệu Hai Tầng, Độ đung đưa Waltz & Phổ tần Trầm Ấm:**
  - **Tương tác nhịp hai tầng:** Thiết kế nhịp điệu như sự đối thoại giữa **tầng nhịp nền bên dưới** (quyết định sinh khí và chuyển động không gian) và **tầng giai điệu lời hát phía trên** (dẫn dắt tâm thức người nghe) trên dải tempo linh hoạt (`58–92 BPM` hoặc nhịp nền chạy ở `112–140 BPM`). Tùy cảm xúc từng bài để chọn cấu trúc tương tác: đối sánh nhịp đàn rải ngón và bộ gõ chổi lông lăn đều nhanh nhạy bên dưới với giọng hát cùng đàn dây ngân chậm gấp đôi ở phía trên; vận hành theo nhịp đung đưa `3/4` hoặc `6/8` có độ nhún duyên dáng; hoặc đồng bộ theo nhịp bước khoan thai. Điều tiết thời điểm nhập cuộc và độ co giãn của tầng nhịp nền thuận theo diễn tiến cảm xúc giữa các phân đoạn.
  - **Phổ tần 80% trầm-trung ấm áp:** Tập trung khoảng 80% năng lượng âm thanh vào dải trầm và trung trầm ấm áp, làm dịu dải cao để bảo vệ thính giác người lớn tuổi thông qua tiếng guitar thùng gảy bằng thịt ngón tay hoặc bịt nhẹ lòng bàn tay, lớp đệm đàn dây trầm kéo ngân dài, tiếng contrabass gỗ đi đằm phía sau phách, bộ gõ mềm mại (trống chân bọc nỉ, shaker nhẹ, chổi snare) và các điểm sáng âm sắc trong trẻo điểm xuyết cực khẽ ở quãng cao.
- **Nhạc cụ Đối thoại & Móc câu Ngân Giai điệu:** Chọn 1 đến 2 nhạc cụ mộc đặc trưng theo đúng nhánh Folk của bài hát (thuộc nhóm dây kéo, dây gảy, hơi gỗ hoặc phím nỉ) đóng vai trò "người kể chuyện thứ ba" luyến trả lời cuối mỗi câu hát và dẫn dắt đoạn độc tấu khí nhạc. Kết hợp điểm xuyết các móc câu ngân giai điệu bằng hơi thở con người (ngân nga, huýt sáo mộc) và thanh âm không gian sống hòa quyện tinh tế vào nhịp nhạc.
- **Biên đạo Giọng hát & Động lực học Tương phản:**
  - **Màu giọng, Tương phản Âm sắc và Độ mở Giai điệu:** Nam trầm từng trải dày ngực tạo điểm tựa mặt đất, nữ mộc trong trẻo thanh thoát giàu độ ngân mở rộng không gian, hoặc song ca đối sánh hai cực âm sắc. Thu âm sát mic với hơi thở tự nhiên, giữ giai điệu hát rõ nét ngay từ câu đầu tiên, nâng cao độ mở hòa âm ở điệp khúc, và điểm xuyết lối nói-hát thủ thỉ sát mic tại điểm lắng chuyển tiếp hoặc câu kết trước khi nhường không gian cho nhạc cụ ngân vang.
  - **Phương thức phối giọng:** Lựa chọn 1 trong 3 cấu trúc theo tính chất bài hát: **(1) Giọng đơn tự sự xuyên suốt** cho mạch chiêm nghiệm nội tâm thống nhất; **(2) Song ca đối thoại** luân phiên chia sẻ các cụm câu ở khổ hát, hội tụ hòa bè quãng 3/quãng 6 ở tiền điệp khúc cùng điệp khúc, và kết đọng bằng một giọng đơn ở câu chốt; hoặc **(3) Đánh thức giọng thứ hai** để một giọng đơn dẫn dắt phần mở đầu trước khi giọng thứ hai nhập cuộc ở nửa sau bài hát nhằm mở rộng chiều kích cảm xúc.
  - **Động lực học Tương phản:** Điều phối mật độ dàn nhạc co giãn theo đường cong cảm xúc; linh hoạt duy trì dòng chảy êm đềm xuyên suốt hoặc thu gọn lớp đệm về trạng thái mộc sát mic tại phân đoạn lắng đọng trước khi mở rộng hòa âm và để nhạc cụ mộc lắng dần ở đoạn kết.

## Style prompt

- **Độ dài và trọng tâm:** Viết thành đoạn văn tiếng Anh từ **55 đến 85 từ** tập trung hoàn toàn vào các cụm danh từ âm học.
- **Thứ tự 5 thành phần bắt buộc (ưu tiên trọng số đầu câu cho mô hình):**
  1. **Thể loại, Điệu thức & Cấu trúc Nhịp Hai Tầng:** Nhánh Folk, điệu thức, chỉ số BPM kèm mối tương quan giữa tầng nhịp nền bên dưới và tầng nhịp ngân của giọng hát bên trên.
  2. **Biên đạo giọng hát & Tương phản âm sắc:** Màu giọng, cực âm sắc, phương thức phối giọng (đơn ca, đối đáp hay hòa bè quãng 3/quãng 6) và lối nhả chữ sát mic.
  3. **Nhạc cụ nền & Đệm trầm cộng hưởng:** Kỹ thuật chơi guitar mộc, lớp đệm đàn dây trầm kéo dài, độ đằm trễ phách của contrabass gỗ và bộ gõ chổi lông mềm.
  4. **Nhạc cụ đối thoại & Điểm sáng âm sắc cao:** Nhạc cụ mộc đối đáp giai điệu theo nhánh Folk, điểm sáng âm sắc cực khẽ ở quãng cao và móc câu ngân giai điệu/huýt sáo.
  5. **Chất liệu sản xuất & Phổ tần:** Thu âm analog ấm áp tập trung 80% vào dải trầm-trung, giữ giọng hát cùng bass ở trung tâm, làm dịu dải cao và mở rộng khoảng thở động lực học.
- **Phối hợp năng lượng giữa 2 bài trong Project:** Hai bài dùng chung hệ chất liệu âm thanh, màu giọng chủ đạo và cùng trục giọng hòa âm (cùng tông hoặc giọng họ hàng bậc IV/V sát cạnh), giữ độ chênh nhịp độ mượt mà trong khoảng **2 đến 6 BPM** theo đường cong lắng đọng dần: **Track 1** thiết lập nhịp điệu có độ chuyển động mở đầu cuốn hút; **Track 2** chuyển tiếp sang nhịp điệu đung đưa sâu lắng và tĩnh tại hơn để dẫn dắt người nghe vào trạng thái an trú trọn vẹn đến cuối phiên nghe.
- **Exclude:** Khai báo 4 đến 6 thành phần âm thanh điện tử, trống gắt, kỹ xảo giọng hát hoặc tần số cao chói gắt tại mục Exclude, ngăn cách bằng dấu phẩy. Khi đưa một nhạc cụ vào mục Exclude, nêu rõ nhạc cụ mộc đóng vai trò dẫn dắt trong style prompt.

## Lời và Thẻ điều phối

- **Thẻ điều phối cấu trúc & nhạc cụ trong ngoặc vuông `[...]`:** Đặt toàn bộ chỉ dẫn phân đoạn, nhạc cụ dẫn dắt, phân vai giọng hát và động lực học gọn trong một thẻ ngoặc vuông duy nhất từ **3 đến 6 từ khóa tiếng Anh** (`[Section: Lead instrument, vocal role, dynamic feel]`).
- **Lời hát bè & tiếng ngân trong ngoặc đơn `(...)`:** Dành riêng dấu ngoặc đơn cho những âm thanh ngân giai điệu và cụm từ bè vọng lại thực sự được hát thành tiếng trên bản thu. Với các bản song ca, ghi chỉ dẫn phân vai giọng hát ngay trong thẻ ngoặc vuông của phân đoạn đó.
- **Trục tiến triển thời gian và Tịnh tiến cảm xúc:**
  - Tổ chức mạch lời tiến triển tự nhiên theo một trục vận động xuyên suốt về thời gian, chu kỳ tự nhiên hoặc độ mở từ không gian bên ngoài vào chiều sâu tâm thức.
  - Giữ vững câu chủ đề qua các lần lặp, đồng thời nâng cấp nhẹ nhàng những dòng khép lại của điệp khúc cuối từ sự vỗ về ban đầu sang trạng thái thấu suốt, trân trọng và làm chủ bình yên.
- **Kiến trúc vần, Độ uyển chuyển và Cấu trúc Dễ Hát Theo:**
  - **Sơ đồ vần linh hoạt theo cảm xúc bài hát:** Giữ mật độ ca từ thư thả (`75–105 từ/phút` khi hát), dành tối thiểu `25%–35%` tổng thời lượng bài hát cho nhạc dạo và khoảng ngân khí nhạc. Linh hoạt lựa chọn sơ đồ vần phù hợp với tính chất từng bài (vần cách `ABCB`, vần gần âm, vần chéo `ABAB` hoặc vần đôi `AABB`), tạo sự phân tách tự nhiên giữa nhịp tự sự ở khổ hát và độ bắt tai ở điệp khúc.
  - **Đồng bộ trọng âm, Từ nối mềm và Câu rơi ngắn cuối khổ:** Giữ số phách nhấn tự nhiên đồng đều giữa các dòng đối xứng, kết hợp các từ nối chuyển ý mềm mại, vần lưng và điệp cấu trúc ở đầu câu để dòng sau nâng đỡ dòng trước liền mạch. Linh hoạt đan xen các dòng tự sự đầy đặn với một câu rơi ngắn cô đọng (3 đến 6 âm tiết) ở cuối khổ để tạo khoảng ngân sâu cho nhạc cụ; ưu tiên đặt các từ có nguyên âm mở hoặc phụ âm vang (`-m, -n, -l, -r`) ở cuối câu.
  - **Khổ hát:** Độ dài dòng co giãn theo nhịp thở trò chuyện tự nhiên (6 đến 11 âm tiết, kết hợp linh hoạt với câu chốt ngắn cuối khổ). Mỗi khổ hát duy trì một mạch không gian và cảm xúc thống nhất: nửa đầu neo vào hành động thực tế, tín hiệu giác quan hoặc lời tâm tình gần gũi; nửa sau mở rộng tầm nhìn hoặc bồi đắp chiều sâu chiêm nghiệm để nâng tự nhiên vào điệp khúc hoặc câu điệp cuối khổ.
  - **Tiền điệp khúc (Tùy chọn):** Co gọn trong 2 đến 4 dòng ngắn, tạo điểm tựa lắng đọng và chuyển hóa góc nhìn trước khi mở vào điệp khúc.
  - **Điệp khúc & Câu chủ đề:** Từ 4 đến 6 dòng (tối đa 8 dòng), vừa vặn với một hơi thở thư thả. Tạo độ bật bằng cách kết tinh một chiêm nghiệm nhân sinh, một nghịch lý dịu dàng hoặc một định nghĩa giàu chất thơ về tuổi già bằng từ vựng giản dị tại vị trí trọng tâm (khép lại ở dòng cuối, đặt làm câu điệp cuối mỗi khổ thơ, hoặc lặp lại ở cả dòng mở đầu và dòng kết thúc của điệp khúc).
  - **Đoạn chuyển:** Cô đọng từ 2 đến 6 dòng trên nền nhạc cụ lắng dịu, kết tinh triết lý trung tâm của bài hát bằng một nhận thức sâu sắc hoặc câu đối thoại tâm tình tạo điểm bừng sáng trước điệp khúc cuối.
- **Điểm mở trực diện và Điểm kết lắng đọng:**
  - Câu đầu tiên của bài hát mở trực diện vào một hành động đang diễn ra, tín hiệu giác quan hữu hình hoặc lời trò chuyện thân tình.
  - Đoạn kết thu gọn trong 1 đến 2 dòng lời cực ngắn (2 đến 6 từ mỗi dòng) kết hợp tiếng ngân nhẹ để nhạc cụ và cảm xúc lắng đọng tự nhiên đến giây cuối cùng.
- **Dấu câu:** Giữ dấu câu tự nhiên trong `2-music.md`. Viết toàn bộ con số thành chữ tiếng Anh chuẩn.

## 3-lyrics.txt (DistroKid)

- Chỉ giữ lại phần lời được hát thành tiếng.
- Viết hoa chữ cái đầu mỗi dòng.
- Để trống ký tự dấu câu ở cuối dòng.
- Ngăn cách giữa các khổ bằng đúng 1 dòng trống.

## Quản lý Catalog

- Đối chiếu `ref/lyrics-index.md` trước khi sáng tác để đảm bảo tính độc bản của câu chủ đề và đạo cụ trung tâm. Cập nhật đầy đủ cả 2 bài vào bảng index sau khi hoàn thành.
