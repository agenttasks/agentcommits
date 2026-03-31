# Pipeline Architecture

## End-to-End Flow

```
Requirement Received
    |
    +-- Video Generation (Higgsfield MCP)
    |       |-- Generate video from script + style params
    |       |-- Apply camera controls and effects
    |       |-- Upscale if requested
    |       +-- Output: video file + metadata
    |
    +-- Content Processing
    |       |-- Validate video specs (duration, resolution, codec)
    |       |-- Generate platform-specific thumbnails
    |       |-- Prepare metadata per platform
    |       +-- Output: platform-ready packages
    |
    +-- Upload Pipeline
    |       |-- TikTok Content Posting API
    |       |-- Instagram Graph API (Reels)
    |       +-- YouTube Data API v3 (Shorts)
    |
    +-- Measurement Setup
            |-- Configure analytics tracking
            |-- Set up webhook listeners (if available)
            +-- Initialize experiment tracking params
```

## Rate Limits by Service

| Service | Rate Limit | Strategy |
|---|---|---|
| Higgsfield | Varies by plan | Queue with backoff |
| TikTok | 6 videos/day (unverified app) | Batch and schedule |
| Instagram | 25 API calls/day (publishing) | Priority queue |
| YouTube | 10,000 units/day | Cost-aware scheduling |

## Error Recovery Matrix

| Error Type | Action | Notify |
|---|---|---|
| Transient failure | Retry with exponential backoff (max 3) | No |
| Auth failure | Block requirement | User |
| Rate limit exceeded | Queue for next window | No |
| Content policy violation | Block requirement | marketing-data-science |
