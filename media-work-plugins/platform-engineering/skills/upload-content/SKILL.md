---
name: upload-content
description: >
  Uploads generated video content to social media platforms (TikTok, Instagram, YouTube).
  Routes to the appropriate platform integration skill based on requirement spec,
  validates content against platform constraints, and records publish IDs for analytics.
---

# Upload Content to Social Platforms

## Workflow

1. Read the requirement from `requirements/accepted/` containing the upload spec
2. Validate the video meets platform-specific constraints
   (see `references/platform-specs.md` for format, resolution, duration, and size limits)
3. Route to the appropriate integration skill:
   - TikTok: invoke `tiktok-integration` (Content Posting API v2)
   - Instagram: invoke `instagram-integration` (Graph API v19.0, Reels)
   - YouTube: invoke `youtube-integration` (Data API v3, Shorts)
4. Execute the platform upload flow via the selected integration skill
5. Record the returned publish ID for downstream analytics tracking
6. Update the requirement status to `completed` and write the result to `requirements/completed/`

## Arguments

- **Requirement ID** -- path or ID for the requirement YAML file in `requirements/accepted/`
- **Platform override** (optional) -- force a specific platform: `tiktok`, `instagram`, or `youtube`

## Error Handling

- If validation fails, reject the requirement with a descriptive error and leave it in `requirements/accepted/`
- If the platform upload fails, retry once; on second failure mark the requirement as `errored` with the platform error response
- If rate limits are hit, log the reset time and defer the upload
