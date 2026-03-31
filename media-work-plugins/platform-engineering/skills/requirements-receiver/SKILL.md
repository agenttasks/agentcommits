---
name: requirements-receiver
description: >
  Receives and triages structured requirements from marketing-data-science,
  validates them, and routes to the appropriate platform-engineering integration skill.
allowed-tools: Read, Write, Bash, Grep, Glob
---

# Receive and Route Requirements

Read incoming requirement files from `media-work-plugins/requirements/pending/`.

## Intake

1. Parse each YAML requirement file in `requirements/pending/`
2. Validate all required fields for the requirement type (see `references/routing-rules.md`)
3. Check that referenced resources exist (avatar IDs, platform credentials)
4. Reject invalid requirements with a detailed error written back to the file

## Route by Type

Route each validated requirement to the correct skill:

- `video_generation` -- hand off to the `higgsfield-mcp` skill
- `content_upload` -- hand off to the platform-specific upload skill (`tiktok-integration`, `instagram-integration`, or `youtube-integration`)
- `integration_setup` -- hand off to the `integration-platform` skill
- `measurement_pipeline` -- hand off to the `integration-platform` skill

Respect priority: P0 requirements are processed immediately, P1 queued in order, P2 batched.

## Accept and Track

1. Move the requirement file from `requirements/pending/` to `requirements/accepted/`
2. Add an `accepted_at` ISO-8601 timestamp to the file
3. Update status as work progresses (`in_progress`, `blocked`, `completed`)
4. Move to `requirements/completed/` when all deliverables are confirmed

## Write Status Updates

Write a status block into the accepted requirement file:

```yaml
status: "accepted | in_progress | completed | blocked"
updated_at: "<ISO-8601>"
notes: "<progress notes>"
blocked_reason: "<if blocked>"
deliverables:
  - path: "<path to generated artifact>"
    type: "video | metadata | analytics_config"
```

## Handle Errors

- Validation failure -- reject with detailed error, leave in `pending/`
- Missing platform credentials -- block and write setup instructions into status
- Higgsfield API unavailable -- block, note retry with exponential backoff
- Upload failure -- block with platform-specific error details
