# TikTok Content Posting API v2 -- Reference

## Authentication

- OAuth 2.0 flow with PKCE
- Scopes: `video.publish`, `video.upload`, `video.list`
- Token refresh: automatic before expiry
- Base URL: `https://open.tiktokapis.com/v2`

## Endpoints

### Initialize Upload

```
POST /post/publish/inbox/video/init/
Headers:
  Authorization: Bearer {access_token}
  Content-Type: application/json
Body:
  {
    "source_info": {
      "source": "FILE_UPLOAD",
      "video_size": <bytes>,
      "chunk_size": <bytes>,
      "total_chunk_count": <int>
    }
  }
Response: { "publish_id": "...", "upload_url": "..." }
```

### Upload Video Chunks

```
PUT {upload_url}
Headers:
  Content-Range: bytes {start}-{end}/{total}
  Content-Type: video/mp4
Body: <binary video data>
```

### Publish Video

```
POST /post/publish/video/init/
Body:
  {
    "post_info": {
      "title": "<caption with hashtags>",
      "privacy_level": "PUBLIC_TO_EVERYONE",
      "disable_duet": false,
      "disable_comment": false,
      "disable_stitch": false,
      "video_cover_timestamp_ms": 1000
    },
    "source_info": {
      "source": "PULL_FROM_URL",
      "video_url": "<hosted-video-url>"
    }
  }
```

## Content Requirements

| Property | Value |
|----------|-------|
| Format | MP4, WebM |
| Codec | H.264 |
| Resolution (min) | 720x1280 |
| Resolution (recommended) | 1080x1920 |
| Duration | 3-600 seconds |
| Duration (Shorts-style) | 15-60 seconds |
| File size (max) | 4 GB |
| Aspect ratio | 9:16 (vertical) |

## Rate Limits

| Tier | Limit |
|------|-------|
| Unverified apps | 6 videos/day |
| Verified apps | Higher limits (varies by approval) |
| API calls | 100 requests/minute |

## Error Codes

| Error Code | Meaning | Recovery Action |
|-----------|---------|-----------------|
| `spam_risk_too_many_posts` | Rate limited | Queue for next day |
| `video_file_wrong_format` | Invalid format | Re-encode with ffmpeg to MP4/H.264 |
| `access_token_invalid` | Auth expired | Refresh token and retry |
| `scope_not_authorized` | Missing permissions | Alert user to reauthorize |
