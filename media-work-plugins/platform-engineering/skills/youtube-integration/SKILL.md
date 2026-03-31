---
name: youtube-integration
description: >
  Uploads Shorts content to YouTube using the Data API v3 with resumable uploads.
  Handles Google OAuth authentication, chunked video upload, metadata optimization,
  and analytics retrieval.
allowed-tools: Read, Write, Bash
---

# YouTube Shorts Upload

Upload and publish Shorts content to YouTube via the Data API v3.

## Steps

1. Authenticate with Google OAuth 2.0
   - Request scopes: `youtube.upload`, `youtube.readonly`, `youtube.force-ssl`
   - Use a refresh token for long-lived access
2. Validate the video file against YouTube Shorts requirements
   - Confirm vertical aspect ratio (9:16) -- required for Shorts classification
   - Confirm duration is 60 seconds or less
   - Confirm reasonable file size (under 100 MB recommended for Shorts)
3. Prepare metadata with Shorts optimization
   - Include `#Shorts` in the title or description for Shorts shelf placement
   - Set keyword-rich title (under 100 characters), description, and tags
   - Set category to Science & Technology (ID: 28) unless otherwise specified
4. Initialize a resumable upload via `POST /upload/youtube/v3/videos?uploadType=resumable`
   - Include snippet, status, and contentDetails in the `part` parameter
5. Upload the video in 5 MB chunks using the resumable upload URI
6. Poll processing status via `GET /youtube/v3/videos?part=status&id={video-id}`
   - Wait until `uploadStatus` is `processed`
7. Record the `video_id` for analytics tracking
8. Update the requirement status to completed

## Platform Requirements

- Base URL: `https://www.googleapis.com/youtube/v3`
- Resolution: 1080x1920 recommended
- Duration: up to 60 seconds for Shorts
- Format: MP4, MOV, AVI, WMV, FLV, 3GPP, MPEG4, WebM
- File size: max 256 GB (keep under 100 MB for Shorts)
- Quota: 10,000 units/day; each upload costs 1,600 units (~6 uploads/day)

See `references/api-details.md` for full endpoint specs, request/response schemas,
quota costs, analytics endpoints, and error code reference.

## Error Handling

- On `quotaExceeded`: queue the upload for the next day
- On `uploadLimitExceeded`: wait and retry after the rate limit window
- On `forbidden`: refresh credentials and verify channel permissions
- On `videoRejected`: review content against YouTube policies, notify marketing
- On `processingFailure`: retry the upload from the beginning
