---
name: higgsfield-mcp
description: |
  Integrates with Higgsfield AI MCP server for video and image generation.
  Supports talking avatars, lip-sync, camera controls, upscaling, and short ad creation.
allowed-tools: Read, Write, Bash
---

# Higgsfield MCP Integration

Manage all interactions with the Higgsfield AI platform via the MCP server at `https://mcp.higgsfield.ai/v1`.

## Core Operations

### Generate Video

Use the Higgsfield MCP tools to generate video content:

1. Select the generation mode based on visual style requirements.
2. Pass the text prompt, style parameters, and any avatar or voice settings.
3. Poll for completion and retrieve the output file URL.

Refer to `references/generation-modes.md` for the full list of supported modes, endpoints, and parameters.

### Generate Images

Call the image generation endpoint for static assets:

1. Provide a text prompt and desired style.
2. Use character creation for branded, consistent avatars.
3. Apply inpainting to edit existing images.

### Post-Process Output

Apply post-processing after initial generation:

- Upscale video or image quality via the upscale endpoint.
- Add camera controls (zoom, pan, orbit, dolly) to generated video.
- See `references/camera-controls.md` for supported camera movements and parameters.

### Create Short Ads

Generate product placement ad clips using predefined presets via the ads endpoint.

## Workflow

1. Receive a content requirement with `content_spec` and `video_generation` params.
2. Select the appropriate generation mode from `references/generation-modes.md`.
3. Call the Higgsfield MCP server to generate content.
4. Post-process: apply camera controls, upscale if requested.
5. Validate output against spec (duration, resolution, file size).
6. Return the video file path and metadata.

## Branding Consistency

- Create a persistent character/avatar using the character creation endpoint.
- Store `avatar_id` and style presets in `config/brand.yaml`.
- Reuse the same avatar and style parameters across all generations.

## Cost Tracking

Log Higgsfield credit usage per generation to session telemetry. See `references/credit-costs.md` for per-operation cost estimates.
