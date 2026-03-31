# Content Brief Schema

Schema for a single content brief generated from a CHANGELOG entry.

| Field | Type | Description |
|-------|------|-------------|
| changelog_date | string (YYYY-MM-DD) | Date of the CHANGELOG entry |
| headline | string | Attention-grabbing one-liner |
| hook | string | First 3 seconds script for short-form video |
| key_points | list[string] | 2-4 bullet points summarizing the update |
| talking_points | string | 30-second narration script |
| cta | string | Call to action |
| hashtags | list[string] | e.g. #ClaudeCode, #AI, #CodingWithAI |
| platforms | PlatformAdaptations | Platform-specific script adaptations |

## PlatformAdaptations

| Field | Type | Description |
|-------|------|-------------|
| instagram_reel | string | Script adapted for Instagram Reels format |
| tiktok | string | Script adapted for TikTok format |
| youtube_short | string | Script adapted for YouTube Shorts format |
