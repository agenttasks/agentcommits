# Platform Content Specifications

## Video Format Requirements by Platform

| Platform  | Format   | Resolution | Duration   | Max Size |
|-----------|----------|------------|------------|----------|
| TikTok    | MP4/WebM | 1080x1920  | 15-60s     | 4GB      |
| Instagram | MP4/MOV  | 1080x1920  | 3-90s      | 1GB      |
| YouTube   | MP4      | 1080x1920  | Up to 60s  | 100MB    |

## Platform API References

- **TikTok**: Content Posting API v2
- **Instagram**: Graph API v19.0 (Reels endpoint)
- **YouTube**: Data API v3 (Shorts upload)

## Rate Limits

| Platform  | Daily Upload Limit | Notes                          |
|-----------|--------------------|--------------------------------|
| TikTok    | 6                  | Per app, resets at UTC midnight |
| Instagram | 25                 | Per account, rolling 24h       |
| YouTube   | 6                  | Per channel, resets at UTC midnight |
