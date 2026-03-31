---
name: base-session
description: >
  Provides foundational session context for all marketing-data-science skills.
  Activated automatically at session start to initialize telemetry, cost tracking,
  logging, and device surface detection.
---

# Base Session Context

Initialize session context at the start of every marketing-data-science workflow.
All other skills in this plugin inherit this context.

## Session Start

1. Capture `${CLAUDE_SESSION_ID}` and record the current UTC timestamp
2. Detect the device surface: available MCP servers, local tools, configured API keys
3. Load environment configuration from `.env.marketing` if present
4. Initialize telemetry and cost tracking counters at zero

## Runtime Tracking

- Track token usage and API costs per skill invocation
- Log structured events for content generation, publishing, and measurement
- Maintain session state across multi-step workflows

## Branch and PR Lifecycle

- Create feature branches for content batches using the pattern `content/<platform>/<date>`
- Version control all generated content plans and structured outputs
- On PR creation, trigger content review workflows and run data quality checks before merge

## Telemetry

Emit structured telemetry events for every skill invocation.
See `references/telemetry-schemas.md` for the full TelemetryEvent, DeviceSurface,
and BaseSessionContext schemas.

## Logging

- Write structured JSON logs to `.claude/logs/marketing-data-science/`
- Use log levels: DEBUG, INFO, WARN, ERROR
- Rotate logs per session

## Cost Tracking

- Track per-skill invocation costs
- Aggregate daily and weekly cost reports
- Alert on budget threshold breaches

## Device Surface Detection

At session start, detect and record:
- Available MCP servers (Higgsfield, social media connectors)
- Local tools (ffmpeg, imagemagick for media processing)
- API keys configured in the environment
- Whether the platform-engineering plugin is loaded
