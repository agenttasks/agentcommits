---
name: tiktok-integration
description: >
  Uploads video content to TikTok using the Content Posting API v2.
  Handles OAuth authentication, chunked video upload, metadata configuration,
  and post scheduling for short-form vertical video.
allowed-tools: Read, Write, Bash
---

# TikTok Video Upload

Upload and publish short-form video content to TikTok via the Content Posting API v2.

## Steps

1. Authenticate with the TikTok API using OAuth 2.0 with PKCE
   - Request scopes: `video.publish`, `video.upload`, `video.list`
   - Refresh the access token automatically before expiry
2. Validate the video file against TikTok content requirements
   - Confirm MP4 or WebM format with H.264 codec
   - Confirm vertical aspect ratio (9:16) and minimum 720x1280 resolution
   - Confirm duration is between 3 and 600 seconds
3. Initialize an upload session via `POST /post/publish/inbox/video/init/`
4. Upload the video in chunks using the returned `upload_url`
   - Use `Content-Range` headers for chunked transfer
5. Publish the video via `POST /post/publish/video/init/` with post metadata
   - Set the caption (include hashtags from the content brief)
   - Set privacy level, duet/comment/stitch permissions, and cover timestamp
6. Record the returned `publish_id` for analytics tracking
7. Update the requirement status to completed

## Platform Requirements

- Base URL: `https://open.tiktokapis.com/v2`
- Resolution: 1080x1920 recommended, 720x1280 minimum
- Duration: 3-600 seconds (15-60 seconds for Shorts-style content)
- File size: max 4 GB
- Rate limits: 6 videos/day (unverified), 100 API requests/minute

See `references/api-details.md` for full endpoint specs, request/response schemas,
rate limit tiers, and error code reference.

## Error Handling

- On `spam_risk_too_many_posts`: queue the upload for the next day
- On `video_file_wrong_format`: re-encode with ffmpeg to MP4/H.264
- On `access_token_invalid`: refresh the OAuth token and retry
- On `scope_not_authorized`: alert the user to reauthorize the app
