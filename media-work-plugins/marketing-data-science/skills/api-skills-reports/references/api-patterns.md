# API Patterns for Report Generation

## Endpoint structure

Use the Anthropic API Skills endpoint for report generation:

```
POST /v1/skills/reports/generate
```

## Request parameters

| Parameter       | Type     | Required | Description                                      |
|-----------------|----------|----------|--------------------------------------------------|
| `report_type`   | string   | yes      | One of: `campaign_performance`, `audience_segmentation`, `ab_test_results`, `attribution`, `spend_summary` |
| `date_range`    | object   | yes      | `{ "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }` |
| `campaign_ids`  | string[] | no       | Filter to specific campaigns; omit for all        |
| `metrics`       | string[] | no       | Filter to specific metrics; omit for all defaults  |
| `output_format` | string   | yes      | One of: `xlsx`, `csv`, `pdf`                       |
| `group_by`      | string   | no       | Grouping dimension: `day`, `week`, `month`, `campaign` |

## Response structure

A successful response returns:

| Field           | Type   | Description                        |
|-----------------|--------|------------------------------------|
| `status`        | string | `completed` or `processing`        |
| `download_url`  | string | Temporary URL to fetch the file    |
| `expires_at`    | string | ISO 8601 expiration timestamp      |
| `row_count`     | int    | Number of data rows in the report  |
| `file_size_bytes` | int  | Size of the generated file         |

## Report types

### Campaign performance
Metrics: impressions, clicks, conversions, spend, CPC, CPM, CTR, ROAS.
Default grouping: by campaign, then by day.

### Audience segmentation
Metrics: segment size, overlap percentage, conversion rate per segment.
Default grouping: by segment.

### A/B test results
Metrics: variant impressions, variant conversions, conversion rate, statistical significance, lift.
Default grouping: by variant.

### Attribution
Metrics: touchpoints, assisted conversions, last-touch conversions, attribution weight.
Default grouping: by channel.

### Spend summary
Metrics: total spend, daily spend, budget utilization, pacing.
Default grouping: by campaign, then by month.

## Pagination

Reports with more than 100,000 rows are automatically split into multiple files. The response includes a `parts` array with individual download URLs when this occurs.

## Rate limits

- Maximum 10 concurrent report generation requests.
- Reports exceeding 1M rows require the `large_report: true` flag and may take up to 5 minutes.
