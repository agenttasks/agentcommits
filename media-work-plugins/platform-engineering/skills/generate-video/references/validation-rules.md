# Video Validation Rules

Validate all generated video output against the requirement content spec.

## Required Checks

| Field | Source | Rule |
|-------|--------|------|
| Duration | `content_spec.duration_seconds` | Must match within 1 second tolerance |
| Resolution | `content_spec.resolution` | Must meet or exceed specified resolution |
| Aspect ratio | `content_spec.aspect_ratio` | Must match exactly (e.g., 9:16, 16:9, 1:1) |
| File size | Platform upload limits | Must not exceed platform max |

## Platform Upload Limits

| Platform | Max File Size | Max Duration | Preferred Aspect Ratio |
|----------|--------------|-------------|----------------------|
| TikTok | 287.6 MB | 10 min | 9:16 |
| Instagram Reels | 650 MB | 15 min | 9:16 |
| YouTube Shorts | 256 GB | 60 sec | 9:16 |
