# Music craft

> 🔒 **GHI CHÚ CỐ ĐỊNH — CHỨC NĂNG FILE & QUY TẮC BẤT BIẾN (TUYỆT ĐỐI KHÔNG CHỈNH SỬA / XÓA MỤC NÀY):**
> - **Chức năng duy nhất của file:** Nhận đầu vào từ `1-idea.md` để thiết kế âm nhạc (`Style prompt`), sáng tác lời bài hát theo đúng Chế độ Kể chuyện đã chọn và xuất ra `2-music.md`, `3-lyrics.txt` cùng cập nhật `ref/lyrics-index.md`. Không chứa quy tắc tạo hình nhân vật (`character.md`), chia cảnh (`storyboard.md`) hay câu lệnh sinh ảnh (`image.txt`).
> - **Quy tắc chỉnh sửa tài liệu này:**
>   1. Không liệt kê lẻ tẻ sự vật sự kiện.
>   2. Không dùng phủ định.
>   3. Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

## Nguyên tắc ngôn ngữ & Độ mở cảm xúc

1. **Khẩu ngữ tâm tình tự nhiên:** Ca từ phản ánh giọng điệu trò chuyện mộc mạc, chân phương và giàu sự thấu cảm trong cuộc sống hàng ngày.
2. **Trường từ vựng giản dị, giàu nhạc tính:** Ưu tiên các từ đơn âm tiết hoặc hai âm tiết thông dụng, mềm mại, nhiều nguyên âm mở để giọng hát dễ ngân nga và người nghe dễ thuộc.
3. **Cấu trúc ngữ pháp thuận:** Giữ trật tự câu theo thói quen nói tự nhiên, rõ ràng, rành mạch. Mỗi dòng gói trọn một cụm ngữ pháp hoàn chỉnh và tương ứng với một nhịp thở tự nhiên.
4. **Điểm nhìn ca từ theo Hai Chế độ Kể chuyện (`Chế độ 1` & `Chế độ 2`):**
   - **Chế độ 1 — Kể chuyện Cá nhân (Hiện tại quen thuộc & Tín hiệu gợi mở / `Familiar Present & Subtle Cues`):** Lời hát đi từ điểm nhìn cá nhân hoặc cuộc trò chuyện tâm tình gần gũi (*I, You, We*), neo vào nhịp sinh hoạt quen thuộc (*now, still, same old, like back then*) và gợi mở câu chuyện, kỷ niệm qua những tín hiệu âm thanh, ánh sáng hoặc cử chỉ gián tiếp.
   - **Chế độ 2 — Ý niệm / Đa diện (Góc nhìn Chiêm nghiệm & Độ mở Đa chiều / `Reflective & Multi-Faceted Perspective`):** Lời hát xoay quanh một ý niệm cảm xúc, vật chứng thời gian hoặc trạng thái tâm hồn chung với góc nhìn thấu cảm rộng mở; ca từ tự do gợi lên những lát cắt đời sống, hình ảnh ẩn dụ hoặc suy ngẫm phổ quát (linh hoạt qua từng câu, từng đoạn hoặc từng khổ tùy theo mạch cảm xúc của bài hát, ưu tiên các đại từ mở *They, We, You, Someone...*) để người nghe ở nhiều hoàn cảnh đều tìm thấy sự đồng điệu và cùng hội tụ về câu `Chorus / Hook` chủ đề.
5. **Diễn tả cảm xúc qua dấu vết vật lý và khoảng lặng (`Tactile & Negative-Space Storytelling`):** Truyền tải tình cảm, sự gắn bó và bước đi của năm tháng thông qua độ mòn của vật thể, thói quen cơ thể và sự tĩnh lặng giàu sức gợi trong không gian sống.
6. **Tương phản giác quan tôn vinh sự ấm áp (`Sensory Contrast`):** Đặt hơi ấm, ánh sáng dịu và sự tĩnh tại của không gian bên trong song hành cùng nhịp chuyển động của thời tiết, khoảng rộng đất trời hoặc dòng thời gian bên ngoài để làm nổi bật cảm giác bình yên, che chở.
7. **Chuyển hóa giá trị tuổi già bằng chiêm nghiệm cân xứng (`Poetic Reframing of Time`):** Tái định nghĩa dấu vết thời gian và nhịp sống chậm rãi thành sự chín muồi, lòng thủy chung và sự bình yên tự chủ thông qua các cặp mệnh đề đối xứng, cô đọng.
8. **Phân bổ vai trò giữa Lời hát và Hình ảnh:** Đặt tâm tình, nhịp sống, tín hiệu gợi mở và những câu chiêm nghiệm phổ quát vào lời bài hát, đồng thời giao phần diễn giải trực diện hoạt cảnh và chuỗi thao tác cụ thể cho bảng phân cảnh hình ảnh (`storyboard.md`).
9. **Bộ chuẩn hóa văn phong:** Áp dụng bắt buộc các nguyên lý từ [humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md), [stop-slop](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/stop-slop/SKILL.md), [avoid-ai-writing](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/avoid-ai-writing/SKILL.md) và [`ref/banned_lyrics_motifs.md`](file:///Users/hoangkien/Youtube/coslient-free/ref/banned_lyrics_motifs.md) nhằm giữ trọn thanh âm mộc mạc và nhịp điệu chân thực của con người.

## Input / Output

- **Input:** `1-idea.md`, `ref/lyrics-index.md`, `ref/banned_lyrics_motifs.md`.
- **Output:**
  - `projects/XXX/2-music.md`: 2 track, mỗi track gồm tên bài, style prompt, exclude, lyrics có thẻ điều phối.
  - `track-N-<slug>/3-lyrics.txt`: lời sạch cho DistroKid.
  - Cập nhật `ref/lyrics-index.md`.

## Dự án & Kiến trúc thời lượng

- **Quy mô:** 2 bài / project, chung chủ đề và chung nền tảng âm nhạc.
- **Thời lượng mục tiêu:** Mỗi bài đạt từ 4 phút trở lên thông qua kiến trúc âm nhạc và các khoảng thở khí nhạc.
- **Khung cấu trúc chuẩn 4 phút+:** `Intro (nhạc dạo mở không gian) -> Verse 1 -> Pre-Chorus -> Chorus -> Interlude -> Verse 2 -> Pre-Chorus -> Chorus -> Instrumental Break / Solo -> Bridge (lắng dịu nhạc cụ) -> Chorus -> Final Chorus -> Outro (kết gọn)`.

## Thể loại, Hòa âm & Giọng hát

- **Thể loại:** Nền Acoustic Folk chủ đạo ở giọng trưởng (`Major key`), kết hợp tối đa 1 nhánh phụ tùy theo cảm xúc của ý tưởng (Americana, Pastoral Folk, Country-Folk, Country Soul, Chamber Folk, Celtic, Cinematic Folk-Pop, Acoustic Folk Blues).
- **Nhánh Acoustic Blues:** Sử dụng kỹ thuật mộc (`acoustic`, Piedmont fingerpicking, slide, harmonica) ở giọng trưởng với nhịp điệu thong thả để bảo toàn cảm giác ấm áp ngay từ đầu bài.
- **Nhịp điệu & Độ trôi tự nhiên (Human Groove & Flow):** Tempo từ 60 đến 95 BPM (hoặc kỹ thuật chia đôi nhịp trống `120 BPM with half-time drums, feels like 60`). Kết hợp nhạc cụ mộc dẫn dắt có độ biến thiên nhịp tự nhiên như người thật chơi (`fingerpicked acoustic guitar with natural timing variations, layered with gentle strummed accents`), bass gỗ ấm đi đằm phía sau phách (`warm upright bass sitting slightly behind the beat`) và bộ gõ mềm giữ dòng chảy êm ái, vững chãi (`light kick and brushed snare maintaining a steady, grounded flow`).
- **Chiều sâu hòa âm & Âm thanh bối cảnh (Harmonic Space & Organic Textures):** Mở rộng không gian hoài niệm bằng các lớp nhạc cụ ngân dài và điểm xuyết tinh tế tùy theo tính chất bài (`sparse piano chords`, `distant harmonica phrases`, `sweeping cello pads`, `subtle slide and swell textures`, `singing fiddle`, `mandolin`, hoặc một motif âm thanh đóng vai trò `light melodic hook`), kết hợp hòa trộn nhẹ nhàng các âm thanh hữu cơ của đời sống vào nhịp nhạc (`organic textures blended subtly into the rhythm`).
- **Giọng hát & Hòa âm giọng:** Nam trầm từng trải (`mature male baritone`), nữ mộc (`female alto`), hoặc song ca (`male and female duet`). Giọng hát thu gần, ấm áp, thư thái, giàu biểu cảm với sự tiết chế tự nhiên (`warm, slightly weathered, intimate and close, calm and content, expressive phrasing with controlled dynamics and restrained delivery`), kết hợp lớp bè mềm mại ở phần điệp khúc (`soft harmonies in choruses`) khi cần mở rộng biên độ cảm xúc.

## Style prompt

- **Độ dài và trọng tâm:** Viết thành đoạn văn mô tả bản thu tự nhiên dưới 120 từ. Đặt thể loại, tempo và nhạc cụ nền tảng ngay phần mở đầu.
- **5 thành phần định hình cốt lõi (tùy biến linh hoạt theo từng bài):**
  1. **Thể loại, Tempo & Bầu không khí:** Nêu rõ nhánh Folk, giọng trưởng, BPM và cảm giác không gian (`warm open-air feel`, `timeless reflective atmosphere`, `gentle pastoral feel`).
  2. **Nhạc cụ nền & Độ trôi của nhịp:** Mô tả cách chơi guitar mộc (`natural timing variations`, `soft strummed layers`), độ đằm của upright bass (`slightly behind the beat`) và bộ gõ mềm (`light kick and brushed snare maintaining a steady, grounded flow`).
  3. **Lớp nhạc cụ chiều sâu & Móc câu âm thanh:** Lựa chọn nhạc cụ tạo khoảng thở hoài niệm (`sparse piano chords`, `distant harmonica`, `sweeping cello pads`, `fiddle`, `subtle slide textures`), motif giai điệu (`light melodic hook`) và âm thanh hữu cơ (`organic textures blended subtly into the rhythm`).
  4. **Động lực học & Giọng hát:** Mô tả cách bản phối lớn dần có tiết chế ở điệp khúc (`arrangement builds gradually with stronger choruses for memorability while remaining restrained`), chất giọng ấm gần gũi (`intimate, warm, calm and content, restrained delivery, clear diction`) và hình dáng giai điệu dễ nhớ (`simple, hummable, soothing melody`).
  5. **Chất liệu sản xuất (Production):** Luân chuyển linh hoạt chất liệu thu âm mộc mạc, vượt thời gian giữa các dự án (`clean, organic, timeless production` / `warm dusty analog production, filmic room tone` / `intimate living-room ribbon mic recording` / `close-mic wood cabin acoustics`) để đa dạng hóa hạt giống giọng hát.
- **Tính thống nhất trong project:** Hai bài trong cùng project dùng chung nền chất liệu âm thanh và màu giọng, điều chỉnh 1 đến 2 thông số (tempo, groove, nhạc cụ điểm xuyết hoặc độ mở của dàn nhạc) theo thời điểm câu chuyện.
- **Exclude:** Khai báo 4 đến 6 thành phần âm thanh điện tử hoặc kỹ xảo tại mục Exclude, ngăn cách bằng dấu phẩy. Khi đưa một nhạc cụ vào mục Exclude, nêu rõ nhạc cụ mộc đóng vai trò dẫn dắt trong style prompt.

```text
EDM, glossy pop, aggressive drums, autotune, synths, electronic drums
```

## Lời và Thẻ điều phối (Lyrics, Prosody & Metatags)

- **Thẻ cấu trúc `[...]` và Chỉ dẫn `(...)`:** Dùng thẻ cấu trúc (`[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Interlude]`, `[Break]`, `[Solo]`, `[Bridge]`, `[Final Chorus]`, `[Outro]`) độc lập hoặc kèm chỉ dẫn diễn tiến âm nhạc tự nhiên để dẫn dắt dàn nhạc đi theo đường cong cảm xúc của bài hát (tinh giản ở đầu bài, bồi đắp dần nhịp điệu và chiều sâu ở thân bài, mở rộng vừa phải ở điệp khúc, lắng dịu ở cầu nối và thu gọn về âm sắc mộc ở đoạn kết).
- **Hát bè `(...)` và Luân chuyển giọng hát (`Vocal Interplay`):** Đặt phần lời hát phụ, tiếng ngân (`Mmm...`, `Ooh...`) hoặc câu bè vọng lại trong ngoặc đơn. Với các bản song ca, phân bổ câu hát đối đáp luân phiên ở `Verse` và hòa giọng đồng thanh quãng 3/quãng 6 ở `Chorus` để tạo sự gắn kết tâm tình.
- **Trục tiến triển thời gian và Tịnh tiến cảm xúc (`Chronological Spine & Chorus Evolution`):**
  - Tổ chức mạch lời tiến triển tự nhiên theo một trục vận động xuyên suốt (nhịp chuyển của ánh sáng trong ngày, nhịp đổi mùa hoặc độ mở từ không gian chung về tâm thức riêng).
  - Giữ vững câu `Hook` định danh qua các lần lặp, đồng thời nâng cấp nhẹ nhàng những dòng khép lại của `Final Chorus` từ sự vỗ về ban đầu sang trạng thái thấu suốt, trân trọng và làm chủ bình yên.
- **Kiến trúc vần và Tương phản nhịp điệu (`Rhyme Architecture & Prosodic Contrast`):**
  - **Sơ đồ vần và Mật độ từ:** Giữ mật độ ca từ thư thả (`75–105 WPM` khi hát), dành tối thiểu `25%–35%` tổng thời lượng bài hát cho nhạc dạo và khoảng ngân khí nhạc. Lựa chọn sơ đồ vần `ABCB` hoặc vần gần âm (`slant rhyme`) ở `Verse` để giữ mạch kể tự nhiên, kết hợp vần đôi `AABB` ở `Chorus` để gia tăng độ bắt tai và sức nặng ghi nhớ.
  - **Verse:** Giữ mật độ 6 đến 10 âm tiết mỗi dòng (độ lệch giữa các dòng trong cùng khổ tối đa 2 âm tiết). Triển khai mạch lời tự nhiên theo chế độ của bài hát: đi sâu vào tâm tình, kỷ niệm và tín hiệu đời sống gần gũi (ở **Chế độ 1**) hoặc mở rộng qua các lát cắt cảm xúc, hình ảnh đời thường đa diện xoay quanh ý niệm chủ đạo (ở **Chế độ 2**).
  - **Pre-Chorus:** Co gọn trong 2 đến 4 dòng ngắn, tạo điểm tựa lắng đọng và chuyển hóa góc nhìn trước khi mở vào điệp khúc.
  - **Chorus & Hook:** Linh hoạt từ 5 đến 8 dòng tùy bài. Tạo độ bật và tính dễ nhớ bằng cách đặt câu `Hook` chủ đề ở vị trí trọng tâm (khép lại ở dòng cuối, hoặc lặp lại ở cả dòng mở đầu và dòng kết thúc theo cấu trúc **Bookend Hook**), ưu tiên mở đầu bằng cụm từ vỗ về ngắn gọn (4 đến 6 âm tiết) có nguyên âm mở hoặc phụ âm vang (`-m, -n, -l, -r`) để mở khoảng ngân cho giọng hát.
  - **Bridge:** Cô đọng từ 2 đến 6 dòng trên nền nhạc cụ lắng dịu, kết tinh triết lý trung tâm của bài hát bằng một nhận thức sâu sắc hoặc câu đối thoại tâm tình tạo điểm bừng sáng trước điệp khúc cuối.
- **Điểm mở và điểm kết:**
  - Câu đầu tiên của `Verse 1` mở trực tiếp vào một khung cảnh, âm thanh quen thuộc hoặc lời tâm tình gần gũi.
  - Đoạn `Outro` thu gọn trong 1 đến 2 dòng lời cực ngắn (từ 2 đến 6 từ mỗi dòng) kết hợp tiếng ngân nhẹ để nhạc cụ và cảm xúc lắng đọng tự nhiên đến giây cuối cùng.
- **Dấu câu:** Giữ dấu câu tự nhiên trong `2-music.md`. Viết toàn bộ con số thành chữ tiếng Anh chuẩn.

## 3-lyrics.txt (DistroKid)

- Chỉ giữ lại phần lời được hát thành tiếng.
- Viết hoa chữ cái đầu mỗi dòng.
- Để trống ký tự dấu câu ở cuối dòng.
- Ngăn cách giữa các khổ bằng đúng 1 dòng trống.

## Quản lý Catalog

- Đối chiếu `ref/lyrics-index.md` trước khi sáng tác để đảm bảo tính độc bản của câu Hook và đạo cụ trung tâm. Cập nhật đầy đủ cả 2 bài vào bảng index sau khi hoàn thành.
