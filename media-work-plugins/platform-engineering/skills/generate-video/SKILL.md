---
name: generate-video
description: |
  Generates video content using Higgsfield AI from a requirement specification.
  Produces AI avatar clips, talking-head videos, UGC-style content, and short ads.
---

# Generate Video

Create video content from a requirement specification using the Higgsfield AI MCP server.

## Inputs

Accept a requirement ID or path to a requirement YAML file from `requirements/accepted/`.

## Steps

1. Read the requirement from the `requirements/accepted/` directory.
2. Parse `content_spec` and `video_generation` parameters from the requirement.
3. Select the appropriate Higgsfield generation mode based on the `visual_style` field.
4. Call the Higgsfield MCP server to generate video.
5. Post-process with camera controls and upscaling if specified.
6. Validate output against content spec requirements (duration, resolution, aspect ratio).
7. Store generated video and update requirement status.

## Mode Selection

Map the `visual_style` field to a Higgsfield generation mode:

- `talking_avatar` -- use Lip-Sync Studio for script narration with branded avatar.
- `text_overlay` -- use AI Video Generation for feature announcements.
- `ugc_style` -- use UGC Video Studio for casual social media content.
- `short_ad` -- use Short Ads preset for product placement clips.
- `screen_recording` -- capture locally, not via Higgsfield.

Refer to `../higgsfield-mcp/references/generation-modes.md` for full endpoint details and parameters.

## Validation

Check all generated output against the requirement spec:

- Duration matches `content_spec.duration_seconds`.
- Resolution meets or exceeds `content_spec.resolution`.
- Aspect ratio matches `content_spec.aspect_ratio`.
- File size is within platform upload limits.

Refer to `references/validation-rules.md` for platform-specific constraints.
