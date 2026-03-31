# Content Schemas

Structured schemas for content extraction, briefs, and calendar management.

## ChangelogEntry

| Field | Type | Constraints |
|-------|------|-------------|
| changelog_date | date | Required |
| category | string | One of: feature, bugfix, breaking, performance |
| title | string | 1-200 characters |
| description | string | Required |
| impact_level | enum | high, medium, low |
| source_reference | string | Optional — commit SHA or PR number |

## ScriptFramework (HOOK-CONTEXT-DEMO-CTA)

| Section | Duration | Max Length |
|---------|----------|-----------|
| hook | 0-3 seconds | 20 words (100 chars) |
| context | 3-10 seconds | Free |
| demo | 10-35 seconds | Free |
| cta | 35-45 seconds | 150 chars |

## PlatformAdaptation

| Field | Type | Constraints |
|-------|------|-------------|
| platform | string | instagram, tiktok, youtube |
| script | string | Non-empty |
| duration_seconds | int | 15-90 |
| style_notes | string | Optional |
| hashtags | list[string] | Each must start with # |
| posting_time | time | Optional |

## ContentBrief

| Field | Type | Constraints |
|-------|------|-------------|
| changelog_entry | ChangelogEntry | Required |
| headline | string | 1-100 characters |
| content_pillar | enum | feature_drops, tips_and_tricks, before_after, community_wins |
| script | ScriptFramework | Required |
| platforms | dict | Must include instagram, tiktok, youtube keys |
| hashtags | list[string] | At least 1, each starts with # |

## ContentCalendar

| Field | Type | Constraints |
|-------|------|-------------|
| week_start | date | Required |
| briefs | list[ContentBrief] | At least 1 |
| posting_schedule | dict | Platform → list of {brief_index, scheduled_time} |

**Validation rule:** No duplicate posts on the same platform on the same day.
