# YouTube Algorithm Reference Guide

## 1. Three-System Architecture

YouTube operates three distinct recommendation systems:

| System | Primary Surface | Core Signals |
|--------|----------------|--------------|
| **Browse** | Home feed, Subscriptions | Personalization, satisfaction, freshness |
| **Search** | Search results | Query relevance, metadata, engagement |
| **Shorts** | Shorts feed | Completion rate, loops, freshness |

- Each system ranks independently. A video can perform well in Browse while having low Search volume, or vice versa.
- YouTube is a **per-viewer prediction engine**, weighted heavily by audience satisfaction.

---

## 2. Satisfaction Signal Hierarchy

1. **Shares:** Strongest per-action signal indicating deep resonance.
2. **Repeat Viewing:** Indicates high artistic/utility satisfaction.
3. **Session Continuation:** Keeping the viewer on YouTube / on your channel.
4. **Saves / Playlisting:** Strong bookmarking intent.
5. **Quality Click Ratio:** Clicks that convert to long watch sessions (opposite of clickbait bounce).
6. **Likes & Meaningful Comments:** Standard engagement signals.

---

## 3. Testing Cascade

Videos are tested progressively through audience cohorts:
1. **Core Audience:** Subscribers & frequent listeners.
2. **Expanded Audience:** Similar interest and listening profiles.
3. **Broader Audience:** Wider demographic/topic match.
4. **High Authority / Viral:** General platform distribution.
