# Platform Engineering Plugin

Platform integration plugin for AI video generation via Higgsfield and social media
content upload pipelines (TikTok, Instagram, YouTube).

## Skills

| Skill | Description |
|-------|-------------|
| `requirements-receiver` | Receives and triages requirements from marketing-data-science |
| `integration-platform` | Core orchestration for video generation → upload pipeline |
| `higgsfield-mcp` | Higgsfield AI MCP integration for video/image generation |
| `tiktok-integration` | TikTok Content Posting API for video upload |
| `instagram-integration` | Instagram Graph API for Reels publishing |
| `youtube-integration` | YouTube Data API v3 for Shorts upload |
| `api-skills-delivery` | Delivery reports via Anthropic API Skills (xlsx, pptx, pdf) |
| `generate-video` | Generate video content using Higgsfield AI |
| `upload-content` | Upload video to social media platforms |

## MCP Servers

| Server | Purpose |
|--------|---------|
| Higgsfield | AI video generation, lip-sync avatars, camera controls, upscaling |

## Pipeline

```
Requirement → Higgsfield Video Generation → Platform Upload → Analytics Tracking
                                                 |
                                    TikTok / Instagram / YouTube
```

## Installation

```bash
claude plugin marketplace add agenttasks/media-work-plugins
claude plugin install platform-engineering@media-work-plugins
```

## Required Setup

Configure the following environment variables for platform API access:

- `HIGGSFIELD_API_KEY` — Higgsfield AI
- `TIKTOK_CLIENT_KEY`, `TIKTOK_CLIENT_SECRET`, `TIKTOK_ACCESS_TOKEN` — TikTok
- `META_APP_ID`, `META_APP_SECRET`, `INSTAGRAM_ACCESS_TOKEN`, `INSTAGRAM_BUSINESS_ACCOUNT_ID` — Instagram
- `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `YOUTUBE_REFRESH_TOKEN`, `YOUTUBE_CHANNEL_ID` — YouTube
