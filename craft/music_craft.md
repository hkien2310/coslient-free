# Music craft

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` để thiết kế âm nhạc (`Style prompt`), sáng tác lời bài hát theo đúng Chế độ Kể chuyện đã chọn và xuất ra `2-music.md`, `3-lyrics.txt` cùng cập nhật `ref/lyrics-index.md`. Không chứa quy tắc tạo hình nhân vật (`character.md`), chia cảnh (`storyboard.md`) hay câu lệnh sinh ảnh (`image.txt`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## 1. Đầu vào, Đầu ra & Định danh

- **Input:** `1-idea.md`, `ref/lyrics-index.md`, `ref/banned_lyrics_motifs.md`, `ref/doi-thu/RANKING.md`, `ref-real-music/index.md` (tùy chọn).
- **Output:**
  1. `projects/XXX/2-music.md`: Gồm tên bài, `Style prompt`, `Exclude` và `Lyrics` kèm thẻ điều phối (mặc định 1 bài độc lập, hoặc 2 bài liên kết khi làm dự án đa bài).
  2. `3-lyrics.txt` (hoặc `track-N-<track-title-slug>/3-lyrics.txt` với dự án đa bài): Bản lời sạch chuẩn DistroKid (chỉ giữ lời được hát thành tiếng, viết hoa chữ cái đầu dòng, để trống dấu câu cuối dòng, ngăn cách các khổ bằng đúng 1 dòng trống).
  3. `ref/lyrics-index.md`: Cập nhật bài hát mới, đảm bảo câu chủ đề (`Hook`) và hình ảnh trung tâm độc bản trong toàn bộ kho nhạc.
- **Tên bài hát (`Track Title`):** Đặt tên tiếng Anh ngắn gọn (3 đến 6 từ) bằng từ vựng đời sống giản dị, giàu chất thơ Folk và gợi mở ngay không gian, lời tâm tình gắn kết hoặc nhịp sống của `1-idea.md`. Đồng bộ 1:1 giữa `1-idea.md`, tiêu đề `## Track N: [Track Title]` trong `2-music.md`, tên thư mục `track-N-<track-title-slug>/` và bảng `ref/lyrics-index.md`.

## 2. Thiết kế Âm nhạc cho Suno (`Style prompt` & `Exclude`)

- **Bản sắc âm học êm dịu cho khán giả 45-85+:**
  - **Thể loại & Nhịp điệu:** Lấy Acoustic Folk mộc mạc (thuần mộc hoặc giao thoa tự nhiên với một nhánh âm nhạc phù hợp bối cảnh `1-idea.md`) làm gốc. Vận hành ở nhịp độ thư thả tương ứng nhịp tim nghỉ ngơi và bước chân đi dạo (`58-86 BPM` cảm nhận), mở đầu bằng cảm giác ấm áp và an toàn ngay từ những giây đầu tiên.
  - **Không gian & Tần số:** Ưu tiên âm sắc gỗ mộc trầm ấm, giọng hát thu sát mic đặt ở trung tâm gần gũi như trong căn phòng nhỏ, tiết chế bộ gõ mềm mại, làm dịu mượt dải tần số cao và giữ khoảng thở động lực học rộng rãi để nghe lâu vẫn êm tai.
- **Biến đổi màu âm qua các phân đoạn (Tạo độ sống động):**
  - **Sự bầu bạn trong giọng hát:** Tạo sức sống và sự sẻ chia qua cách phối giọng phù hợp với câu chuyện: đối đáp Nam trầm ấm và Nữ trong trẻo (đổi vai theo khổ hoặc từng cặp câu, hòa bè ấm ở điệp khúc), đánh thức giọng thứ hai bước vào ở nửa sau bài, hoặc giọng đơn tự sự kết hợp bè hòa âm và tiếng ngân con người (`humming / whistling`).
  - **Nhạc cụ kể chuyện & Điểm lắng cảm xúc:** Chọn bộ nhạc cụ mộc gắn liền với không gian văn hóa của `1-idea.md`, trong đó có nhạc cụ đóng vai trò đối đáp giai điệu với giọng hát và dẫn dắt đoạn độc tấu khí nhạc (`Instrumental Solo`). Tạo sự biến thiên năng lượng tự nhiên giữa các đoạn và thiết kế một khoảng lắng rút gọn nhạc cụ về trạng thái mộc tĩnh lặng ở nửa sau bài (`Bridge` hoặc trước câu kết) để tôn lời hát tâm tình.
- **Quy cách `Style prompt` & `Exclude`:**
  - `Style prompt` (55 đến 85 từ tiếng Anh): Viết bằng các cụm danh từ âm học trực quan mà Suno nhận diện tốt nhất; đặt nhánh Folk, điệu thức, BPM, màu giọng/cách phối giọng và nhạc cụ chủ đạo ngay ở câu đầu. Khi dự án gồm 2 bài, giữ chung thế giới âm thanh mộc và tạo nét chuyển dịch tự nhiên về nhịp độ hoặc màu giọng giữa hai bài.
  - `Exclude` (4 đến 6 thành phần): Khai báo các yếu tố âm thanh điện tử, trống đập mạnh, kỹ xảo giọng hát hoặc tần số chói gắt cần loại trừ, ngăn cách bằng dấu phẩy; khi loại trừ một nhạc cụ, nêu rõ nhạc cụ mộc dẫn dắt trong `Style prompt`.

## 3. Sáng tác Ca từ & Thẻ điều phối (`Lyrics`)

- **Cấu trúc & Thẻ điều phối `[...]` chuẩn Suno:**
  - Tổ chức cấu trúc bài hát, số khổ hát (`Verse` thường 4 dòng, hoặc mở rộng 6 đến 8 dòng) và các khoảng thở khí nhạc (`Intro`, `Interlude`, `Instrumental Solo`, `Outro`) theo độ dài tự nhiên của câu chuyện (`2:30` đến `3:30` với khoảng 24 đến 34 dòng lời, hoặc mở rộng khi mạch tự sự cần thêm không gian).
  - Đặt một thẻ ngoặc vuông `[...]` tiếng Anh ngắn gọn (3 đến 10 từ) ở đầu mỗi phân đoạn ghi rõ tên đoạn, nhạc cụ dẫn dắt, người hát (`Male vocal / Female vocal / Duet`) và sắc thái động lực học để dẫn dắt Suno đổi màu âm theo từng đoạn.
  - Dành riêng dấu ngoặc đơn `(...)` cho những tiếng ngân (`"Mmm...", "Ooh..."`) hoặc cụm từ bè thực sự được hát thành tiếng.
- **Mạch truyện: Tự sự đời thường ở `Verse` -> Chiêm nghiệm nhân sinh ở `Chorus`:**
  - Giữ vững ngôi kể theo Chế độ đã chọn tại `1-idea.md` (**Chế độ 1**: tự sự hoặc đối thoại gắn với tuyến nhân vật xuyên suốt; **Chế độ 2**: khắc họa các lát cắt đời sống độc lập cùng hội tụ về ý niệm trung tâm ở điệp khúc).
  - **Khổ hát (`Verse`):** Câu đầu tiên mở trực tiếp vào một hành động, lời nói thân tình hoặc khung cảnh sinh hoạt cụ thể. Dùng chi tiết đời thực (vật dụng, không gian và ký ức của thế hệ trưởng thành 1945-1975) cùng 2 đến 3 móc neo từ `1-idea.md` để đẩy câu chuyện tiến triển tự nhiên qua từng khổ.
  - **Điệp khúc (`Chorus`) & Câu `Hook`:** Nâng câu chuyện đời thường ở `Verse` lên thành một lời vỗ về, một chiêm nghiệm nhân sinh giản dị hoặc sự nhẹ lòng khi nhìn lại năm tháng. Đặt câu chủ đề (`Hook`) ngắn gọn, vừa vặn một hơi thở nhẹ ở vị trí trọng tâm điệp khúc để người nghe dễ nhẩm thuộc ngay lần đầu; giữ thời gian và ánh sáng ở điệp khúc cuối khớp logic với bước chuyển của `Bridge`.
- **Nhịp thở ca từ, Vần tự nhiên & Chuẩn văn phong:**
  - Viết câu chữ mộc mạc như lời trò chuyện đời thực, vừa vặn hơi thở hát (3 đến 4 nhịp nhấn tự nhiên mỗi dòng), có sự đan xen uyển chuyển giữa câu dài kể chuyện và câu ngắn nghỉ hơi; gieo vần tự nhiên theo mạch nghĩa và chủ động làm mới cặp từ gieo vần ở mỗi bài.
  - Đặt tâm tình, tín hiệu gợi mở và chiêm nghiệm vào lời bài hát; giao phần diễn giải trực diện hoạt cảnh và thao tác vật lý cụ thể cho `storyboard.md`.
  - Tuân thủ [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md) và [`ref/banned_lyrics_motifs.md`](file:///Users/hoangkien/Youtube/coslient-free/ref/banned_lyrics_motifs.md). Giữ dấu câu tự nhiên trong `2-music.md` và viết toàn bộ con số thành chữ tiếng Anh chuẩn.
