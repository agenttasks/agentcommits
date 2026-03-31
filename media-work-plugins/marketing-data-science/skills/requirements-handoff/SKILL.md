---
name: requirements-handoff
description: >
  Generates structured requirements from marketing-data-science outputs and hands them off
  to platform-engineering as actionable tasks via the shared requirements directory.
allowed-tools: Read, Write, Bash, Grep, Glob
---

# Requirements Handoff to Platform Engineering

Bridge marketing-data-science decisions into actionable platform-engineering tasks.

## Handoff Process

1. Build a requirement document from the originating skill output.
   Refer to `references/requirement-schemas.md` for the full specification.
2. Validate all required fields are populated and conform to the schema.
3. Write the requirement file to `requirements/pending/<requirement_id>.yaml`.
4. Log the handoff event to telemetry.
5. Mark the requirement as `pending` in the requirements tracker.

## Requirement Types

Select the appropriate type based on the originating workflow:

- **video_generation** -- Content-strategy produced a finalized brief.
  Platform-engineering uses Higgsfield MCP to generate video.
- **content_upload** -- Video is ready for publishing.
  Platform-engineering handles platform-specific upload APIs.
- **integration_setup** -- research-account-setup identified new platform needs.
  Platform-engineering configures MCP servers and API connections.
- **measurement_pipeline** -- ab-experiment-measurement needs analytics data.
  Platform-engineering configures data collection from platform APIs.

## Requirement ID Format

Generate IDs as `REQ-<YYYY-MM-DD>-<sequence>` where sequence is zero-padded (001, 002, ...).

## Cross-Plugin Communication

Write requirements to the shared directory that platform-engineering monitors:

- `media-work-plugins/requirements/pending/` -- new requirements
- `media-work-plugins/requirements/accepted/` -- acknowledged by platform-engineering
- `media-work-plugins/requirements/completed/` -- delivered by platform-engineering

## Status Tracking

Track requirement status transitions as documented in `references/requirement-schemas.md`.
