---
name: integration-platform
description: >
  Orchestrates cross-service pipelines from Higgsfield video generation through
  social media publishing and measurement setup for platform-engineering.
allowed-tools: Read, Write, Bash, Grep, Glob
---

# Orchestrate Integration Pipelines

Coordinate end-to-end workflows that span video generation, content processing, upload, and measurement.

## Verify Service Health

At session start, confirm connectivity to all required services:

1. Check Higgsfield MCP availability via `.mcp.json` configuration
2. Verify TikTok API credentials are present
3. Verify Instagram/Meta API credentials are present
4. Verify YouTube/Google API credentials are present

Report any failures before processing requirements.

## Run the Pipeline

For each accepted requirement, execute these stages in order:

### 1. Video Generation
- Delegate to the `higgsfield-mcp` skill with script and style parameters
- Wait for video file and metadata output

### 2. Content Processing
- Validate video specs (duration, resolution, codec) against platform requirements
- Generate platform-specific thumbnails
- Prepare metadata per target platform

### 3. Upload
- Delegate to the appropriate platform skill (`tiktok-integration`, `instagram-integration`, or `youtube-integration`)
- Respect rate limits (see `references/pipeline-architecture.md`)

### 4. Measurement Setup
- Configure analytics tracking for the published content
- Initialize experiment tracking parameters if an experiment ID is present

## Manage Rate Limits

Queue work to stay within platform rate limits:

- **Higgsfield** -- varies by plan; queue with backoff
- **TikTok** -- 6 videos/day for unverified apps; batch and schedule
- **Instagram** -- 25 publishing API calls/day; use priority queue
- **YouTube** -- 10,000 quota units/day; cost-aware scheduling

## Recover from Errors

- Transient failures -- retry with exponential backoff, max 3 attempts
- Auth failures -- alert the user, block the requirement, log to telemetry
- Rate limit exceeded -- queue and schedule for next available window
- Content policy violation -- block requirement, notify marketing-data-science plugin

## Configuration

Read platform configuration from:
- `.mcp.json` for MCP server connections
- `.env.platform` for API credentials
