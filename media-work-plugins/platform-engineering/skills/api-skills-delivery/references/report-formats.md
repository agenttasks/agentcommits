# Report Format Specifications

## 1. Upload Tracking Dashboard (Excel)

### Sheet 1: Upload Queue
| Column         | Description                              |
|----------------|------------------------------------------|
| Requirement ID | ID from `requirements/accepted/`         |
| Platform       | tiktok, instagram, or youtube            |
| Status         | pending, uploading, completed, errored   |
| Scheduled      | Scheduled upload timestamp (UTC)         |
| Uploaded At    | Actual upload timestamp (UTC)            |
| Publish ID     | Platform-assigned content ID             |
| Error          | Error message if failed                  |

### Sheet 2: Platform Rate Limits
| Column      | Description                        |
|-------------|------------------------------------|
| Platform    | Platform name                      |
| Daily Limit | Maximum uploads per day            |
| Used Today  | Uploads consumed today             |
| Remaining   | Uploads available                  |
| Reset Time  | When the limit resets (UTC)        |

### Sheet 3: Weekly Upload History
- Bar chart: uploads per platform per day
- Success/failure rate breakdown
- Average processing time per platform

Include conditional formatting for status columns and embedded charts.

---

## 2. Delivery Confirmation (PDF)

Sections:
- **Header**: Delivery Confirmation title, requirement ID, delivery timestamp
- **Published Content**: platform, publish ID, content URL, title, status
- **Generation Details**: provider (Higgsfield), video duration, resolution, credits used
- **Upload Details**: upload method, processing time, file size
- **Next Steps**: monitor analytics (24h), check engagement (48h), feed to ab-experiment-measurement

---

## 3. Platform Setup Guide (PDF)

Sections:
- **Header**: Platform name, account type, setup date
- **API Configuration**: base URL, auth type, scopes, rate limits
- **Credentials Status**: per-credential validity (no actual secrets -- reference env vars only)
- **Content Specifications**: format, resolution, duration range, max file size
- **Verified Capabilities**: list of tested and confirmed API features
- **Known Limitations**: platform-specific restrictions and workarounds

---

## 4. Pipeline Status Deck (PowerPoint)

### Slide 1: Title
- "Content Pipeline Status - Week {N}"
- "Platform Engineering Report"

### Slide 2: Pipeline Health
| Stage             | Status | Avg Time | Success Rate |
|-------------------|--------|----------|--------------|
| Video Generation  |        |          |              |
| TikTok Upload     |        |          |              |
| Instagram Upload  |        |          |              |
| YouTube Upload    |        |          |              |

### Slide 3: Throughput
- Bar chart: content pieces processed per day
- Line chart: processing time trend

### Slide 4: Issues and Actions
- Current blockers
- Rate limit utilization summary
- Planned improvements
