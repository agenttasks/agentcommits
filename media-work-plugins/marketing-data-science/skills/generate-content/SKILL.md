---
name: generate-content
description: >
  Generates social media content briefs from Claude Code CHANGELOG updates,
  producing platform-specific scripts for Instagram Reels, TikTok, and YouTube Shorts.
---

# Generate Content from CHANGELOG

## Workflow

1. Invoke the `changelog-content` skill to fetch and parse the latest CHANGELOG.md.
2. Invoke the `content-strategy` skill to create platform-specific adaptations.
3. Validate all outputs against the content brief schema.
   Refer to `references/content-schemas.md` for the full specification.
4. Present content briefs organized by platform and posting schedule.
5. When content is ready for production, invoke `requirements-handoff` to send briefs
   to platform-engineering for video generation and upload.

## Arguments

Accept the following optional parameters from the user:

- **Days to look back** (default: 7) -- number of days of CHANGELOG history to cover.
- **Platform filter** (default: all) -- one or more of: instagram, tiktok, youtube.

## Output Format

For each CHANGELOG entry, produce a brief containing:

- Headline and hook (under 20 words)
- Talking points (3-5 bullets)
- Platform-specific script adaptations (Instagram, TikTok, YouTube)
- Hashtags, posting time, and content pillar classification
- Source reference to the original CHANGELOG entry

Validate every brief against the `ContentBrief` schema in `references/content-schemas.md`
before presenting results.
