---
name: generate-content
description: >
  Generate social media content briefs from Claude Code CHANGELOG updates.
  Use when users want to create content, generate briefs, plan posts,
  or produce platform-specific scripts for Instagram Reels, TikTok, and YouTube Shorts.
---

# Generate Content from CHANGELOG

Fetch and parse the latest anthropics/claude-code CHANGELOG.md, then produce platform-specific content briefs.

## Steps

1. Use the `changelog-content` skill to fetch and parse the latest CHANGELOG.md
2. Use the `content-strategy` skill to create platform-specific adaptations
3. Validate all outputs against the content brief schema (see `references/content-schemas.md`)
4. Present content briefs organized by platform and posting schedule
5. If ready for production, use `requirements-handoff` to send to platform-engineering

## Arguments

- Days to look back (default: 7)
- Platform filter (default: all) — instagram, tiktok, youtube

## Output Format

For each CHANGELOG entry, produce a brief with:
- Headline, hook (under 20 words), talking points
- Platform-specific script adaptations (Instagram, TikTok, YouTube)
- Hashtags, posting time, content pillar classification
- Source reference to the original CHANGELOG entry
