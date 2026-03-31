# YouTube Data API v3 (Shorts) -- Reference

## Authentication

- Google OAuth 2.0
- Scopes: `youtube.upload`, `youtube.readonly`, `youtube.force-ssl`
- Refresh token for long-lived access
- Base URL: `https://www.googleapis.com/youtube/v3`

## Endpoints

### Initialize Resumable Upload

```
POST /upload/youtube/v3/videos?uploadType=resumable&part=snippet,status,contentDetails
Headers:
  Authorization: Bearer {access_token}
  Content-Type: application/json
  X-Upload-Content-Length: <file-size-bytes>
  X-Upload-Content-Type: video/mp4
Body:
  {
    "snippet": {
      "title": "<title with #Shorts>",
      "description": "<description with keywords>",
      "tags": ["ClaudeCode", "AI", "Shorts"],
      "categoryId": "28",
      "defaultLanguage": "en"
    },
    "status": {
      "privacyStatus": "public",
      "selfDeclaredMadeForKids": false,
      "publishAt": "<ISO-8601>" (for scheduled)
    }
  }
Response Headers:
  Location: <resumable-upload-uri>
```

### Upload Video Chunks

```
PUT <resumable-upload-uri>
Headers:
  Content-Length: <chunk-size>
  Content-Range: bytes <start>-<end>/<total>
  Content-Type: video/mp4
Body: <binary video data>
```

Recommended chunk size: 5 MB.

### Verify Upload Status

```
GET /youtube/v3/videos?part=status&id=<video-id>
Response: { "items": [{ "status": { "uploadStatus": "processed" } }] }
```

### Retrieve Analytics (Basic)

```
GET /youtube/v3/videos?part=statistics&id=<video-id>
Response:
  statistics: {
    viewCount, likeCount, commentCount, favoriteCount
  }
```

### Retrieve Analytics (Detailed)

Uses the YouTube Analytics API:

```
GET /youtube/analytics/v2/reports
Dimensions: video
Metrics: views, estimatedMinutesWatched, averageViewDuration,
         averageViewPercentage, likes, shares, subscribersGained
```

## Content Requirements

| Property | Value |
|----------|-------|
| Format | MP4, MOV, AVI, WMV, FLV, 3GPP, MPEG4, WebM |
| Resolution (recommended) | 1080x1920 |
| Duration (Shorts) | Up to 60 seconds |
| Aspect ratio | 9:16 (vertical) -- required for Shorts classification |
| File size (max) | 256 GB (keep under 100 MB for Shorts) |

## Quota System

| Operation | Cost (units) |
|-----------|-------------|
| Video upload | 1,600 |
| List videos | 1 |
| Update video | 50 |
| **Daily quota** | **10,000** |

With the default quota, approximately 6 uploads per day are possible.

## SEO Optimization for Shorts

- Title: keyword-rich, include `#Shorts`, under 100 characters
- Description: include timestamps, links, and keywords
- Tags: mix broad and specific (max 500 characters total)
- Thumbnail: auto-generated from video (custom thumbnails for Shorts in beta)
- Category: Science & Technology (ID: 28)

## Error Codes

| Error Code | Meaning | Recovery Action |
|-----------|---------|-----------------|
| `quotaExceeded` | Daily quota used | Queue for next day |
| `uploadLimitExceeded` | Too many uploads | Wait and retry |
| `forbidden` | Auth/permission issue | Refresh credentials |
| `videoRejected` | Policy violation | Review content, notify marketing |
| `processingFailure` | Server-side error | Retry upload |
