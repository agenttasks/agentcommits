# Requirement Schemas

Structured schemas for cross-plugin requirements handoff.

## Requirement

| Field | Type | Constraints |
|-------|------|-------------|
| requirement_id | UUID | Auto-generated |
| source_skill | string | Originating skill name |
| priority | enum | P0, P1, P2 |
| type | enum | video_generation, content_upload, integration_setup, measurement_pipeline |
| status | enum | pending, accepted, in_progress, completed, verified, blocked, rejected |
| content_spec | ContentSpec | Required for video_generation |
| video_generation | VideoGenerationSpec | Required for video_generation |
| upload_spec | UploadSpec | Required for content_upload |
| experiment | ExperimentTracking | Optional |
| acceptance_criteria | list[string] | At least 1 |
| blocked_reason | string | Required when status is blocked |
| rejected_reason | string | Required when status is rejected |

## ContentSpec

| Field | Type | Constraints |
|-------|------|-------------|
| platform | enum | instagram, tiktok, youtube |
| duration_seconds | int | 15-90 |
| aspect_ratio | string | Default "9:16" |
| resolution | string | WxH format, default "1080x1920" |
| script | string | Non-empty |
| visual_style | string | Optional |
| audio | string | voiceover, trending_sound, original |

## VideoGenerationSpec

| Field | Type | Constraints |
|-------|------|-------------|
| provider | string | Default "higgsfield" |
| style | string | talking_avatar, screen_recording, text_overlay, ugc_style, short_ad |
| avatar_id | string | Optional |
| lip_sync | bool | Default false |
| camera_controls | string | Optional (zoom_in, pan_left, static, etc.) |
| upscale | bool | Default false |

## UploadSpec

| Field | Type | Constraints |
|-------|------|-------------|
| platform | enum | instagram, tiktok, youtube |
| title | string | 1-200 characters |
| description | string | Max 5000 characters |
| hashtags | list[string] | Max 30 |
| scheduled_time | datetime | Optional |
| visibility | enum | public, private, unlisted |

## Status Flow

```
pending → accepted → in_progress → completed → verified
                  → blocked (with reason)
                  → rejected (with reason)
```
