---
name: upload-content
description: >
  Upload generated video content to social media platforms (TikTok, Instagram, YouTube).
  Use when users want to publish videos, upload content, schedule posts,
  or distribute content across social platforms.
---

# Upload Content to Social Platforms

Upload video content to TikTok, Instagram, and YouTube using platform-specific APIs.

## Steps

1. Read requirement from `requirements/accepted/` with upload spec
2. Validate video meets platform-specific requirements
3. Route to appropriate integration skill:
   - TikTok: `tiktok-integration` (Content Posting API v2)
   - Instagram: `instagram-integration` (Graph API v19.0, Reels)
   - YouTube: `youtube-integration` (Data API v3, Shorts)
4. Execute platform upload flow
5. Record publish IDs for analytics tracking
6. Update requirement status to completed

## Arguments

- Requirement ID or path to requirement YAML file
- Platform override (optional): tiktok, instagram, youtube

## Platform Requirements

| Platform | Format | Resolution | Duration | Max Size |
|----------|--------|-----------|----------|----------|
| TikTok | MP4/WebM | 1080x1920 | 15-60s | 4GB |
| Instagram | MP4/MOV | 1080x1920 | 3-90s | 1GB |
| YouTube | MP4 | 1080x1920 | Up to 60s | 100MB |
