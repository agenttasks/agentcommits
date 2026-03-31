# Experiment Schemas

Structured schemas for A/B experiment design, tracking, and reporting.

## VariantConfig

| Field | Type | Constraints |
|-------|------|-------------|
| label | string | 1-50 characters |
| description | string | Required |
| parameters | dict | Keys: string, values: string/int/float/bool |

## PlatformMetrics

| Field | Type | Description |
|-------|------|-------------|
| platform | enum | instagram, tiktok, youtube |
| views | int | >= 0 |
| completions | int | >= 0 |
| likes | int | >= 0 |
| comments | int | >= 0 |
| shares | int | >= 0 |
| new_followers | int | >= 0 |
| link_clicks | int | >= 0 |

### Derived Metrics

| Metric | Formula | Weight |
|--------|---------|--------|
| completion_rate | completions / views | 0.30 |
| engagement_rate | (likes + comments + shares) / views | 0.25 |
| share_rate | shares / views | 0.20 |
| follower_conversion | new_followers / views | 0.15 |
| ctr | link_clicks / views | 0.10 |
| **composite_score** | Weighted sum of above | 1.00 |

## StatisticalResult

| Field | Type | Constraints |
|-------|------|-------------|
| p_value | float | 0.0-1.0 |
| effect_size | float | Cohen's h |
| significant | bool | True if p < 0.05 |
| confidence_level | float | Default 0.95 |
| winner | string or null | Label of winning variant |

## Experiment

| Field | Type | Constraints |
|-------|------|-------------|
| experiment_id | UUID | Auto-generated |
| week_number | int | 1-53 (ISO week) |
| week_start | date | Required |
| hypothesis | string | At least 10 characters |
| variable | enum | hook_type, duration, style, posting_time, cta_type, audio |
| variant_a | VariantConfig | Control |
| variant_b | VariantConfig | Treatment |
| platforms | list | At least 1 platform |
| status | enum | planned, running, completed, archived |
| results | ExperimentResults or null | Required when status is completed |

**Validation rules:**
- Results can only be set when status is "completed"
- Completed experiments must have results
- Minimum 200 views per variant before statistical analysis

## WeeklyReport

| Field | Type |
|-------|------|
| experiment | Experiment |
| report_date | date |
| summary | string |
| next_experiment_hypothesis | string or null |
