# Telemetry and Session Schemas

Structured schemas for session context, telemetry, and device surface detection.

## Platform Enum

Values: `instagram`, `tiktok`, `youtube`

## DeviceSurface

Detected at session start.

| Field | Type | Description |
|-------|------|-------------|
| available_mcp_servers | list[string] | MCP servers detected |
| local_tools | list[string] | e.g. ffmpeg, imagemagick |
| configured_api_keys | list[string] | Env var names (not values) |
| platform_engineering_available | bool | Whether platform-engineering plugin is loaded |

## TelemetryEvent

| Field | Type | Description |
|-------|------|-------------|
| session_id | string | Claude Code session ID |
| skill_name | string | Invoking skill |
| event_type | string | content_generated, experiment_measured, quality_check, requirement_created |
| platform | Platform or null | Target platform |
| timestamp | datetime | UTC |
| cost_usd | float | >= 0 |
| tokens_used | int | >= 0 |
| metadata | dict | Additional key-value data |

## BaseSessionContext

All skills inherit this context.

| Field | Type | Description |
|-------|------|-------------|
| session_id | string | Non-empty, trimmed |
| started_at | datetime | Session start time |
| device_surface | DeviceSurface | Detected capabilities |
| total_cost_usd | float | Cumulative cost |
| total_tokens_used | int | Cumulative tokens |
| telemetry_events | list[TelemetryEvent] | Event log |
| log_level | enum | debug, info, warn, error |
