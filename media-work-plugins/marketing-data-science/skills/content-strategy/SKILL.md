---
name: content-strategy
description: >
  Provides multi-platform content strategy for daily social media shorts
  on Instagram Reels, TikTok, and YouTube Shorts. Use when planning content
  calendars, adapting messaging per platform, or defining content pillars
  for Claude Code CHANGELOG updates.
---

# Content Strategy

## Core Workflow

1. Identify the CHANGELOG entries or feature updates to promote
2. Classify each entry under a content pillar (see below)
3. Create a platform-specific content calendar using specs from `references/platform-specs.md`
4. Write a script for each piece using the script framework below
5. Define cross-platform adaptation notes for each script
6. Hand off finalized strategy to `requirements-handoff` for platform-engineering delivery

## Content Pillars

Distribute content across these pillars:

- **Feature Drops** (40%) -- New Claude Code capabilities
- **Tips & Tricks** (25%) -- Power user workflows
- **Before/After** (20%) -- Productivity comparisons
- **Community Wins** (15%) -- User stories and use cases

## Script Framework

Structure each script as:

1. **Hook** (0-3s): Question or surprising statement drawn from the CHANGELOG
2. **Context** (3-10s): What changed and why it matters
3. **Demo** (10-35s): Show the feature in action (screen recording or avatar)
4. **CTA** (35-45s): Try it yourself + follow for more

## Cross-Platform Adaptation

Apply these rules when adapting a single message across platforms:

- Deliver the same core message with platform-appropriate style
- TikTok: Use informal tone and trending sounds
- Instagram: Add text overlays and branded templates
- YouTube: Include chapter markers in description and keyword-rich titles

Refer to `references/platform-specs.md` for detailed per-platform duration, aspect ratio, audience, tone, and posting windows.

## Handoff to Platform Engineering

When content strategy is finalized, create a structured requirement for platform-engineering containing:

- Video generation specs (Higgsfield parameters)
- Upload metadata per platform
- Scheduling requirements
- A/B variant specifications if applicable
