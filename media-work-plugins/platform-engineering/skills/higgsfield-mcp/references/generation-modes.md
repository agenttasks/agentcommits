# Higgsfield Generation Modes

## Video Generation

| Mode | Endpoint | Parameters |
|------|----------|------------|
| AI Video Generation | `https://higgsfield.ai/create/video` | prompt, style, scene composition, motion control |
| Talking Avatar (Lip-Sync) | `https://higgsfield.ai/lipsync-studio` | avatar_id, script, voice, motion_style |
| Draw-to-Video | `https://higgsfield.ai/create/video?video-inpaint=true` | sketch/storyboard input, prompt |
| UGC Video | `https://higgsfield.ai/lipsync-studio?ugc-studio=true` | avatar_id, script, voice, casual motion presets |
| Short Ads | `https://higgsfield.ai/ads` | product info, preset template |

## Image Generation

| Mode | Endpoint | Parameters |
|------|----------|------------|
| AI Image Generation | `https://higgsfield.ai/image/nano_banana_2` | prompt, style |
| Character Creation | `https://higgsfield.ai/character` | appearance params, branding constraints |
| Inpainting | `https://higgsfield.ai/edit?model=soul-canvas` | source image, mask, edit prompt |

## Post-Processing

| Mode | Endpoint | Parameters |
|------|----------|------------|
| Upscale | `https://higgsfield.ai/upscale` | source file, target resolution |

## MCP Server Configuration

```json
{
  "mcpServers": {
    "higgsfield": {
      "type": "http",
      "url": "https://mcp.higgsfield.ai/v1"
    }
  }
}
```
