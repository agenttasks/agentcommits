# Instagram Graph API v19.0 (Reels) -- Reference

## Authentication

- Facebook/Meta OAuth 2.0
- Long-lived access token (60-day expiry, auto-refresh)
- Required permissions: `instagram_content_publish`, `instagram_basic`, `pages_read_engagement`
- Base URL: `https://graph.facebook.com/v19.0`

## Endpoints

### Create Media Container

```
POST /{ig-user-id}/media
Parameters:
  media_type: REELS
  video_url: <publicly-accessible-url>
  caption: <text with hashtags and mentions>
  share_to_feed: true
  cover_url: <thumbnail-url> (optional)
  thumb_offset: <ms> (optional)
  location_id: <location-id> (optional)
  collaborators: [<username>] (optional)
  audio_name: <audio-track-name> (optional)
Response: { "id": "<creation-id>" }
```

### Check Container Status

```
GET /{creation-id}?fields=status_code
Response: { "status_code": "FINISHED" | "IN_PROGRESS" | "ERROR" }
```

Poll until `FINISHED` (typically 30-120 seconds).

### Publish

```
POST /{ig-user-id}/media_publish
Parameters:
  creation_id: <creation-id>
Response: { "id": "<media-id>" }
```

### Scheduled Publishing

```
POST /{ig-user-id}/media
Parameters:
  media_type: REELS
  video_url: <url>
  caption: <text>
  is_carousel_item: false
  published: false  # Creates draft
```

Note: Scheduling requires Meta Business Suite UI or a separate scheduling service.

### Insights Collection

```
GET /{media-id}/insights
Metrics: impressions, reach, plays, likes, comments, shares, saved
Period: lifetime
```

## Content Requirements

| Property | Value |
|----------|-------|
| Format | MP4, MOV |
| Codec | H.264, H.265 |
| Resolution (min) | 540x960 |
| Resolution (recommended) | 1080x1920 |
| Duration | 3-90 seconds |
| File size (max) | 1 GB |
| Frame rate | 30 fps recommended |
| Aspect ratio | 9:16 (vertical); 1:1, 4:5 also supported |

## Rate Limits

| Scope | Limit |
|-------|-------|
| Content publishing API calls | 25 per 24-hour period |
| General API calls | 200 per hour |
| Media container creation | 50 per hour |

## Caption Best Practices

- Front-load the hook in the first line (visible before "...more")
- Include 20-30 relevant hashtags (mix of sizes)
- Add a CTA in the caption body
- Tag relevant accounts
- Use line breaks for readability

## Error Codes

| Error Code | Meaning | Recovery Action |
|-----------|---------|-----------------|
| `EXPIRED` | Container expired | Recreate container |
| `ERROR` | Processing failed | Check video specs, retry |
| `OAuthException` | Auth issue | Refresh token |
| `RATE_LIMIT` | Too many calls | Back off exponentially and retry |
