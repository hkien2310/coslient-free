# YouTube SEO Playbook Reference

## 1. Title Optimization

| Property | Value |
|----------|-------|
| Hard character limit | 100 characters |
| Desktop truncation | ~60-70 characters |
| Mobile truncation | ~40-50 characters |
| Front-load keyword | First 40-50 characters |

### Performance Benchmarks
- **70-100 character titles** outperform shorter titles by **10-14%** (analyzed across 3M+ videos).
- **Mobile viewports cut off at 40-50 chars** — the primary emotional hook or search keyword must sit in the first 40 characters.
- **Numbers & Brackets** add clarity and contextual anchors (`[Official Visualizer]`, `[Acoustic Version]`).

### Gemini AI Multimodal Clickbait Penalty
- YouTube uses multimodal Gemini AI to compare actual video frames, audio/speech, and lyrics against metadata.
- Misleading titles or clickbait that doesn't match content get suppressed automatically.

---

## 2. Description Architecture

| Property | Value |
|----------|-------|
| Max length | 5,000 characters |
| Visible before "Show more" | First 150-200 characters |
| Primary keyword placement | First 25 words |
| Keyword density | 2-4x in body copy (200-350 words) |

### Structure Blueprint
1. **Lines 1-2 (First 150-200 chars):** Emotional hook + Primary keyword (visible in search preview).
2. **Timestamps/Chapters:** Start at 0:00, minimum 3 chapters, keyword-rich labels.
3. **Lyrics (Full text):** Natural, high-authority semantic anchor for audio-video indexing.
4. **Body / Story Context:** 150-250 words naturally weaving secondary keywords.
5. **Credits & Streaming Links:** Clean and structured.
6. **Closing:** 3-5 hashtags at the bottom.

- **Google AI Overviews:** ~30% of Google AI Overviews cite YouTube videos. Optimize descriptions for search engines, not just the YouTube feed.

---

## 3. Tags

- **Status:** Vestigial — minimal direct ranking weight.
- **Limit:** 500 characters, spend max 30 seconds.
- **Purpose:** Disambiguation, artist sound-alikes, and common misspellings.

---

## 4. Chapters & Google Key Moments

| Requirement | Value |
|-------------|-------|
| Must start at | 0:00 |
| Minimum chapters | 3 |
| Minimum chapter length | 10 seconds each |

- Enables **Google Key Moments** rich snippets on Google Search.
- Increases Average View Duration (AVD) by ~4% and retention up to 50%.

---

## 5. Hashtags

| Context | Optimal Count | Max Allowed |
|---------|--------------|-------------|
| Standard Videos | 3-5 | 15 (Exceeding 15 = ALL ignored) |
| Position | Description bottom | Never in Title |

---

## 6. VideoObject Schema (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Video Title",
  "description": "First 150 characters of description",
  "thumbnailUrl": "https://example.com/thumb.jpg",
  "uploadDate": "2026-01-01",
  "duration": "PT4M15S",
  "contentUrl": "https://www.youtube.com/watch?v=VIDEO_ID",
  "embedUrl": "https://www.youtube.com/embed/VIDEO_ID"
}
```
