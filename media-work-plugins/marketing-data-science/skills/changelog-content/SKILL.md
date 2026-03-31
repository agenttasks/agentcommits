---
name: changelog-content
description: >
  Parses the anthropics/claude-code CHANGELOG.md to extract recent updates and
  transforms them into social media content briefs for Instagram, TikTok, and
  YouTube Shorts. Triggered when users ask to create content from changelog entries.
---

# CHANGELOG Content Extraction

Parse the official `anthropics/claude-code` CHANGELOG.md and produce daily content briefs.

## Fetch Source

Retrieve the latest CHANGELOG from the upstream repository:

```
https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
```

Read the raw markdown and pass it to the extraction steps below.

## Extract and Prioritize

1. Parse entries by date, grouping into: new features, bug fixes, breaking changes, performance improvements
2. Rank each entry by user impact:
   - **HIGH** — New capabilities, major UX changes
   - **MEDIUM** — Performance improvements, new integrations
   - **LOW** — Bug fixes, minor tweaks
3. Generate a content brief for each high or medium impact entry using the schema in `references/content-brief-schema.md`

## Build Content Calendar

- Produce a 7-day rolling content calendar from extracted entries
- Map entries to optimal posting times per platform
- Prevent duplicate coverage across platforms on the same day
- Stagger platform posts: TikTok (morning), Instagram (midday), YouTube (evening)

## Quality Gates

- Verify every brief includes a hook under 3 seconds read time
- Confirm scripts are under 60 seconds for Shorts, Reels, and TikToks
- Trace all technical claims to a specific CHANGELOG entry
- Include source commit or PR reference for accuracy
