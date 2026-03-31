---
name: generate-video
description: >
  Generate video content using Higgsfield AI from a requirement specification.
  Use when users want to create videos, generate content with AI avatars,
  produce talking-head clips, or make UGC-style content.
---

# Generate Video via Higgsfield

Create video content from a requirement specification using the Higgsfield AI MCP server.

## Steps

1. Read requirement from `requirements/accepted/` directory
2. Use the `higgsfield-mcp` skill to select the appropriate generation mode
3. Call Higgsfield MCP server to generate video
4. Post-process with camera controls and upscaling if requested
5. Validate output against content spec requirements (duration, resolution, aspect ratio)
6. Store generated video and update requirement status

## Arguments

- Requirement ID or path to requirement YAML file

## Generation Modes

| Visual Style | Higgsfield Mode | Use Case |
|-------------|-----------------|----------|
| talking_avatar | Lip-Sync Studio | Script narration with branded avatar |
| text_overlay | AI Video Generation | Feature announcements |
| ugc_style | UGC Video Studio | Casual social media content |
| short_ad | Short Ads preset | Product placement clips |
| screen_recording | Local capture (not Higgsfield) | Demo walkthroughs |
