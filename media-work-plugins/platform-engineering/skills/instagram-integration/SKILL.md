---
name: instagram-integration
description: >
  Publishes Reels content to Instagram using the Graph API v19.0
  via Meta Business Suite. Handles media container creation, status polling,
  publishing, and insights collection.
allowed-tools: Read, Write, Bash
---

# Instagram Reels Upload

Publish Reels content to Instagram via the Graph API v19.0 (Meta Business Suite).

## Steps

1. Authenticate with Meta OAuth 2.0
   - Use a long-lived access token (60-day expiry, auto-refresh)
   - Require permissions: `instagram_content_publish`, `instagram_basic`, `pages_read_engagement`
2. Validate the video file against Instagram Reels requirements
   - Confirm MP4 or MOV format with H.264 or H.265 codec
   - Confirm vertical aspect ratio (9:16) and minimum 540x960 resolution
   - Confirm duration is between 3 and 90 seconds
3. Host the video at a publicly accessible URL (or use a presigned URL)
4. Create a media container via `POST /{ig-user-id}/media`
   - Set `media_type` to `REELS`
   - Set the `video_url`, `caption`, and optional fields (cover, location, collaborators)
5. Poll the container status via `GET /{creation-id}?fields=status_code`
   - Wait until `status_code` is `FINISHED` (typically 30-120 seconds)
6. Publish the container via `POST /{ig-user-id}/media_publish`
7. Record the returned `media_id` for insights tracking
8. Update the requirement status to completed

## Platform Requirements

- Base URL: `https://graph.facebook.com/v19.0`
- Resolution: 1080x1920 recommended, 540x960 minimum
- Duration: 3-90 seconds for Reels
- File size: max 1 GB
- Frame rate: 30 fps recommended
- Rate limits: 25 publish calls/day, 200 API calls/hour, 50 container creations/hour

See `references/api-details.md` for full endpoint specs, request/response schemas,
rate limits, insights metrics, and error code reference.

## Error Handling

- On `EXPIRED` status: recreate the media container
- On `ERROR` status: check video specs against requirements and retry
- On `OAuthException`: refresh the access token
- On `RATE_LIMIT`: back off exponentially and retry
