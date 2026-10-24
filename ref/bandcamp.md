# 🎹 Bandcamp Music Registry & Kế Hoạch Phát Hành — Coslient

**Trang chính thức:** [https://coslient.bandcamp.com](https://coslient.bandcamp.com)  
**Nguồn sự thật cho việc đóng gói, định giá và theo dõi phát hành trên Bandcamp.**  
**Đối chiếu đồng bộ:** Xem [`distrokid.md`](./distrokid.md) và [`lyrics-index.md`](./lyrics-index.md).

---

## 🎯 QUY TẮC VẬN HÀNH BANDCAMP (KHÁC BIỆT VỚI DISTROKID)

1. **Đóng gói theo Full Album (7–14 bài / Album) thay vì EP nhỏ:**
   - Khán giả 45–85+ trên Bandcamp sẵn sàng chi **$9.00** (hoặc trả thêm tùy tâm — *Name your price / Let fans pay more*) cho một Album trọn vẹn từ 7–14 bài.
   - Từ **Coslient Free V2 (Project 018 trở đi)**: Đồng bộ 1:1 tên Album giữa DistroKid và Bandcamp (gom theo từng Album ~10–12 bài như `Kettle & Light`).
   - Trên Bandcamp **không cần chờ gom đủ 12 bài mới được đăng**: Có thể tạo Album ngay từ khi có 2–3 bài đầu tiên, sau đó mỗi khi ra video YouTube mới thì bấm `Edit` ➔ `add track` để nạp thêm bài mới vào Album ngay lập tức (0 giây chờ duyệt).
2. **Thông số kỹ thuật bắt buộc của Bandcamp (Tránh lỗi `[FATAL]` khi upload):**
   - **Audio:** File gốc `.wav` (16-bit hoặc 24-bit, 44.1kHz/48kHz).
   - **Cover Art:** Tối thiểu **`1400 × 1400 px`** và dung lượng **dưới `10 MB`** (định dạng `.jpg` hoặc `.png`).
     - ⚠️ *Cảnh báo kho ảnh `distrokid/` hiện tại:* Các file `cover.png` gốc chỉ có `1152 × 1152 px` (Bandcamp sẽ từ chối vì quá nhỏ), còn các file `cover_upscayl_3x_upscayl-standard-4x.png` (`3456 × 3456 px`) nặng `15–19 MB` (Bandcamp sẽ từ chối vì vượt quá `10 MB`).
     - **Cách xử lý 1 giây trên Mac trước khi up:** Chạy lệnh chuyển file upscayl sang `.jpg` chuẩn `3000 × 3000 px` (~1.5 MB):
       ```bash
       for f in distrokid/*/*upscayl*.png distrokid/*/coverx4.png; do sips -s format jpeg -s formatOptions 92 -Z 3000 "$f" --out "${f%/*}/cover_bandcamp.jpg"; done
       ```
3. **Cấu hình giá chuẩn & Các ô Per-Track (Giao diện Edit Album Bandcamp):**
   - **Ở phần Album tổng (Trên cùng):**
     - **Album Price:** `$9.00 USD` (Tích ✅ *Let fans pay more if they want*).
     - **About / Tags:** Dán đoạn `About this album` và `Tags` bên dưới vào ô của Album tổng.
   - **Ở phần từng Track lẻ (`Unwound.wav`, v.v.):**
     - **Track Pricing:** Để mặc định `$1.50` (hoặc `$1.00`), tích ✅ *enable individual track purchase* và ✅ *let fans pay more if they want*.
     - **About this track:** Copy-paste câu mô tả tiếng Anh 2 dòng dưới mỗi bài.
     - **Lyrics:** Copy-paste toàn bộ nội dung file `3-lyrics.txt` được gắn link ngay tại bài đó.
     - **CÁC Ô ĐỂ TRỐNG 100% Ở TỪNG TRACK (Không cần nhập vì Bandcamp tự lấy từ Album tổng):** `track credits`, `video`, `artist`, `artwork upload`, `tags` (nếu đã nhập ở Album), `license` (giữ mặc định *All rights reserved*), `publishing rights`, `songwriters/composers`, `track ISWC`, `track ISRC`, `release date`, `bonus track`.
   - **Ô `personal note to the release notification` (Gửi cho Followers ngay trên nút `Publish Album`):**
     ```text
     Thank you so much for listening and supporting our quiet corner of music. Your kindness keeps this little town alive. Wishing you a peaceful day wherever you are.
     ```

---

## 📊 DASHBOARD TỔNG QUAN BANDCAMP

| # | Tên Album | Giai đoạn | Số bài | Giá | Trạng thái Bandcamp | Đối chiếu DistroKid |
|---|---|---|---|---|---|---|
| 1 | **[A Piece of Quiet](https://coslient.bandcamp.com/album/a-piece-of-quiet)** | Coslient Video (Đợt 1) | 13 | $9.00 | 🟢 Đã đăng (25/04/2026) | Các bài lẻ đợt đầu |
| 2 | **[Everything Heavy](https://coslient.bandcamp.com/album/everything-heavy)** | Coslient Video (Đợt 2) | 14 | $9.00 | 🟢 Đã đăng (10/06/2026 — Đã bổ sung About) | Các bài lẻ đợt 2 |
| 3 | **[Slow Light](https://coslient.bandcamp.com/album/slow-light)** | Coslient Video (Đợt 3) | 7 | $9.00 | 🟢 Đã đăng (16/06/2026) | Các bài lẻ đợt 3 |
| 4 | **[Kettle & Light](https://coslient.bandcamp.com/album/kettle-light-4)** | **Coslient Free V2 (020–026)** | **12** | **$9.00** | 🟢 **Đã đăng (23/10/2026 — Đã thêm Track 12)** | Trùng 1:1 Album `Kettle & Light` |
| 5 | **[Porch & Hearth](https://coslient.bandcamp.com/album/porch-hearth)** | **Coslient Free V1 (009–017)** | **9** | **$9.00** | 🟢 **Đã đăng (23/10/2026)** | Gộp `Porch & Hearth` + 5 bài V1 (`009, 011, 015–017`) |
| 6 | **[Meadow & Moss](https://coslient.bandcamp.com/album/meadow-moss)** | **Coslient Free V1 (001–008)** | **11** | **$9.00** | 🟢 **Đã đăng (23/10/2026)** | Gộp `Meadow & Moss` + `Unfolding` + `Dust & Groove` |
| 7 | **[Still Water](https://coslient.bandcamp.com/album/still-water-2)** | **Coslient Video (061–070)** | **17** | **$9.00** | 🟢 **Đã đăng (23/10/2026)** | Gộp toàn bộ 6 EP cuối của `Coslient Video` |
| 8 | **`A Place Back Home`** | **Coslient Free V2 (018–019+)** | **2+** | **$3.00** *(tăng lên $9 khi đủ bài)* | 🟡 **Đang gom thêm bài V2 (hoặc đăng mở đường)** | Trùng 1:1 Album `A Place Back Home` |

---

## 🚀 ALBUM ĐANG GOM BÀI MỚI (COSLIENT FREE V2)

### Album #8 — `A Place Back Home` (Coslient Free V2 — Đang mở nhận thêm bài)
> Hiện có sẵn 2 file `.wav` từ Project `018` và `019`. Có thể đăng lên ngay với giá `$3.00` hoặc chờ gom đủ 8–10 bài thuộc nhánh Folk Pop tươi sáng rồi phát hành đồng bộ cùng DistroKid với giá `$9.00`.

* **Album Title:** `A Place Back Home`
* **Price:** `$3.00` (hoặc `$9.00` khi đủ Full Album)
* **About this album (Copy-paste):**
```text
A Place Back Home is an upbeat acoustic folk collection about keeping a warm chair by the window for old friends and looking back with gratitude on the years a family built together.
```
* **Tracks hiện có trên máy:**
  1. **`A Place Back Home`**
     - **Audio:** [`projects/018/A Place Back Home - SUNO.wav`](../projects/018/A%20Place%20Back%20Home%20-%20SUNO.wav) | **Lyrics:** [`projects/018/3-lyrics.txt`](../projects/018/3-lyrics.txt)
     - **About this track:** `Hot water in the kettle, a wide sunlit room, and an armchair waiting by the window for an old friend coming home from a long road.`
  2. **`We Did It, Me and You`**
     - **Audio:** [`projects/019/We Did It, Me and You_Master.wav`](../projects/019/We%20Did%20It,%20Me%20and%20You_Master.wav) | **Lyrics:** [`projects/019/3-lyrics.txt`](../projects/019/3-lyrics.txt)
     - **About this track:** `An older couple sits on the evening porch watching their grown children and grandchildren laugh in the yard, remembering the winter their truck broke down at twenty-three and smiling because they made it through hand in hand.`
* **Prompt tạo Cover Art `1:1` cho `A Place Back Home`:**
```text
Handcrafted stop-motion animation film still, clean natural morning sunlight, harmonious true-to-life scale. Medium-wide eye-level shot inside a sunlit wooden living room with a wide open timber window overlooking a green hillside lane under an open sky with natural deep focus. Beside the sunlit window sits an inviting armchair with a folded woven throw, a steaming ceramic mug on a small pine table, and a pair of worn leather walking boots resting by the open doorway. Single directional warm morning sunlight casting a single coherent shadow direction --ar 1:1
```

---

## 📚 HỒ SƠ LƯU TRỮ 7 ALBUM ĐANG BÁN TRÊN BANDCAMP (83 BÀI)

### 🟢 1. A Piece of Quiet (Released: 25/04/2026 — 13 Tracks — $9.00)
* **URL:** [https://coslient.bandcamp.com/album/a-piece-of-quiet](https://coslient.bandcamp.com/album/a-piece-of-quiet)
* **Tracks:** `1. Walked Beside Me` · `2. Where the Trees Keep Time` · `3. When the Bells Come Through` · `4. The Sweetest Easter` · `5. Right Where They Are` · `6. We Were Better in the Summer` · `7. The Light Is Still On` · `8. The Doorway Keeps It` · `9. This House Knew My Name` · `10. Through the May` · `11. The Seat We Saved` · `12. What the Old Things Know` · `13. The Words I Never Sent`

### 🟢 2. Everything Heavy (Released: 10/06/2026 — 14 Tracks — $9.00)
* **URL:** [https://coslient.bandcamp.com/album/everything-heavy](https://coslient.bandcamp.com/album/everything-heavy)
* **Tracks:** `1. The Blue Cup by the Window` · `2. Until the Streetlights Came On` · `3. That's How Big Love Can Be` · `4. When Love Walks Tall` · `5. The Water Remembers` · `6. The Stars Still Sing My Name` · `7. The Summer Glass` · `8. The Porch Paw Syndicate` · `9. Dirt on Her Hands` · `10. The Warmest Place in Winter` · `11. Gardeners of the Deep` · `12. The Water Doesn't Ask` · `13. Close the Door Lightly` · `14. The Unplayed Song`

### 🟢 3. Slow Light (Released: 16/06/2026 — 7 Tracks — $9.00)
* **URL:** [https://coslient.bandcamp.com/album/slow-light](https://coslient.bandcamp.com/album/slow-light)
* **Tracks:** `1. The Architecture of Smoke` · `2. Bikes Coasting Over Gravel` · `3. The Sundust Horse` · `4. The Deep Root` · `5. The Biscuit Tin` · `6. The Wooden Floor` · `7. Chapter Five`

### 🟢 4. Kettle & Light (Released: 23/10/2026 — 12 Tracks — $9.00)
* **URL:** [https://coslient.bandcamp.com/album/kettle-light-4](https://coslient.bandcamp.com/album/kettle-light-4)
* **Tracks:** `1. Learning to Sit Still (020)` · `2. Look at Them, Darlin' (021-T1)` · `3. Your Turn on the Swing (021-T2)` · `4. The Sheep Stand Still (022-T1)` · `5. On My Left Side (022-T2)` · `6. The Morning Jubilee (023-T1)` · `7. Dance Like Nobody's Young (023-T2)` · `8. The Cardboard Knight (024-T1)` · `9. Leave the Porch Light On (024-T2)` · `10. Keep a Seat by the Sea (025-T1)` · `11. Where the Evening Water Shines (025-T2)` · `12. The Bus That Waits for You (026)`
* **Track #12 vừa bổ sung (`Project 026`):**
  - **Track Title:** `The Bus That Waits for You`
  - **Audio:** [`projects/026/The Bus That Waits for You.wav`](../projects/026/The%20Bus%20That%20Waits%20for%20You.wav) | **Lyrics:** [`projects/026/3-lyrics.txt`](../projects/026/3-lyrics.txt)
  - **About this track:** `A small cream-and-green valley bus waits by the morning garden gate for an old neighbor with a basket of plums, carries a paper bag of peaches from hand to weathered hand in the afternoon breeze, and keeps its yellow headlights shining up the gravel lane at dusk until an elderly passenger reaches her front porch.`

### 🟢 5. Porch & Hearth (Released: 23/10/2026 — 9 Tracks — $9.00)
* **URL:** [https://coslient.bandcamp.com/album/porch-hearth](https://coslient.bandcamp.com/album/porch-hearth)
* **Tracks:** `1. Unwound (010)` · `2. White Linen Wind (011)` · `3. The Open Air (012)` · `4. Not Another Day (013)` · `5. Shelter (014)` · `6. The Tide Haven (015)` · `7. The Father's Bough (016)` · `8. The Gentle Road (017)` · `9. Tide and Timber (009)`

### 🟢 6. Meadow & Moss (Released: 23/10/2026 — 11 Tracks — $9.00)
* **URL:** [https://coslient.bandcamp.com/album/meadow-moss](https://coslient.bandcamp.com/album/meadow-moss)
* **Tracks:** `1. Sunlit Iron (005)` · `2. Borrow No Wings (006)` · `3. Tales We Were Told (007a)` · `4. Tales of Gold (007b)` · `5. Paper Creases (001)` · `6. Brass Pocket Watch (002)` · `7. Step Into Air (003)` · `8. Unbound (004)` · `9. The Slowest Compass (008a)` · `10. Quiet Things Grow Tall (008b)` · `11. Roots in the Stone (008c)`

### 🟢 7. Still Water (Released: 23/10/2026 — 17 Tracks — $9.00)
* **URL:** [https://coslient.bandcamp.com/album/still-water-2](https://coslient.bandcamp.com/album/still-water-2)
* **Tracks:** `1. Sky in the Puddle (v062)` · `2. Stars Upon The Ground (v062)` · `3. Silver Muzzle, Golden Heart (v068)` · `4. The Mended Thread (v064)` · `5. The Gift of Time (v064)` · `6. The Quiet Fire (v066)` · `7. Seventh Try (v069)` · `8. Storms We Knew (v070-T1)` · `9. Rest Your Mind (v070-T2)` · `10. The Light Is Mine (v065)` · `11. The Soul Is Wide (v065)` · `12. I Walk So Light (v065)` · `13. The Infinite Resonance (v063)` · `14. Colors in the Quiet (v063)` · `15. Outwear the Night (v061)` · `16. The Velvet Meridian (v061)` · `17. The Danger I Love (v067)`
