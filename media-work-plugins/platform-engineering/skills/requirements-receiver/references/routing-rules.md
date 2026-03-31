# Requirement Routing Rules

## Requirement Types and Destinations

| Requirement Type | Route To | Priority Handling |
|---|---|---|
| `video_generation` | `higgsfield-mcp` skill | P0: immediate, P1: queue, P2: batch |
| `content_upload` | platform-specific upload skill | P0: immediate, P1: scheduled |
| `integration_setup` | `integration-platform` skill | Always P1 |
| `measurement_pipeline` | `integration-platform` skill | P2 unless experiment is currently running |

## Required Fields by Type

### video_generation
- `content_spec.platform`
- `content_spec.duration_seconds`
- `content_spec.script`
- `video_generation.provider` (must be "higgsfield")
- `video_generation.parameters.style`

### content_upload
- `upload_spec.platform`
- `upload_spec.title`
- `upload_spec.description`
- `upload_spec.visibility`

### integration_setup
- `content_spec.platform`
- `acceptance_criteria` (at least one)

### measurement_pipeline
- `experiment.experiment_id`
- `content_spec.platform`

## Status Lifecycle

```
pending -> accepted -> in_progress -> completed -> verified
                    -> blocked (with reason)
                    -> rejected (with reason)
```
