---
name: api-skills-reports
description: |
  Generates downloadable reports using Anthropic API Skills (xlsx, pptx, pdf).
  Creates experiment reports, content calendars, and strategy decks via code execution.
allowed-tools: Read, Write, Bash, Grep
---

# API Skills Report Generation

Uses Anthropic's managed API Skills to generate professional documents for the content pipeline.

## Available API Skills

| Skill ID | Output | Use Case |
|----------|--------|----------|
| `xlsx` | Excel spreadsheets | Experiment metrics, content calendars, budget tracking |
| `pptx` | PowerPoint decks | Strategy presentations, weekly reviews, stakeholder updates |
| `pdf` | PDF documents | Experiment reports, content briefs, requirement specs |

## API Configuration

```python
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# All API Skills requests use this pattern:
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "<skill-id>", "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": "<prompt>"}],
    betas=[
        "code-execution-2025-08-25",
        "files-api-2025-04-14",
        "skills-2025-10-02",
    ],
)
```

## Report Types

### 1. Weekly Experiment Report (Excel)

Generated every Friday from `ab-experiment-measurement` data.

```python
prompt = f"""Create an A/B experiment tracking spreadsheet with:

Sheet 1: Experiment Overview
- Experiment ID: {experiment.experiment_id}
- Week: {experiment.week_number}
- Hypothesis: {experiment.hypothesis}
- Variable: {experiment.variable}
- Status: {experiment.status}

Sheet 2: Variant A Metrics
| Platform | Views | Completions | Likes | Comments | Shares | Completion Rate | Engagement Rate | Composite Score |
{format_variant_metrics(experiment.results.variant_a_results)}

Sheet 3: Variant B Metrics
{format_variant_metrics(experiment.results.variant_b_results)}

Sheet 4: Statistical Analysis
- p-value: {experiment.results.statistical_result.p_value}
- Effect size (Cohen's h): {experiment.results.statistical_result.effect_size}
- Significant: {experiment.results.statistical_result.significant}
- Winner: {experiment.results.statistical_result.winner}

Include:
- Conditional formatting (green for winner, red for loser)
- Column charts comparing variants per platform
- Summary formulas for totals and averages
- Professional formatting with headers
"""
```

Skill config: `{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}`

### 2. Content Calendar (Excel)

Generated weekly from `content-strategy` output.

```python
prompt = f"""Create a 7-day content calendar spreadsheet:

Columns: Day | Platform | Content Pillar | Headline | Hook | Duration | Posting Time | Status

Data:
{format_calendar_rows(content_calendar)}

Include:
- Color-coded platforms (TikTok=pink, Instagram=purple, YouTube=red)
- Data validation dropdowns for Status (Draft, Ready, Published, Scheduled)
- Conditional formatting for overdue items
- Summary row with post counts per platform
"""
```

### 3. Strategy Deck (PowerPoint)

Generated for stakeholder updates and monthly reviews.

```python
prompt = f"""Create a content strategy presentation:

Slide 1: Title
- "Social Media Content Report - Week {week_number}"
- Subtitle: "Claude Code CHANGELOG Updates"

Slide 2: Performance Summary
- Column chart: Views by platform (TikTok, Instagram, YouTube)
- Key metrics: Total views, avg engagement rate, follower growth

Slide 3: Top Performing Content
- Table of top 3 posts with metrics
- What worked and why

Slide 4: A/B Experiment Results
- Current experiment: {experiment.hypothesis}
- Winner: {experiment.results.statistical_result.winner}
- Bar chart comparing variant scores

Slide 5: Next Week Plan
- Upcoming CHANGELOG features to cover
- Next experiment hypothesis
- Content calendar preview

Use clean, professional formatting with consistent branding.
"""
```

Skill config: `{"type": "anthropic", "skill_id": "pptx", "version": "latest"}`

### 4. Requirement Specification (PDF)

Generated per requirement handoff to platform-engineering.

```python
prompt = f"""Create a requirement specification PDF:

REQUIREMENT SPECIFICATION
ID: {requirement.requirement_id}
Priority: {requirement.priority}
Type: {requirement.type}
Source: {requirement.source_skill}
Date: {requirement.created_at}

CONTENT SPECIFICATION
Platform: {requirement.content_spec.platform}
Duration: {requirement.content_spec.duration_seconds}s
Resolution: {requirement.content_spec.resolution}
Script: {requirement.content_spec.script}

VIDEO GENERATION
Provider: {requirement.video_generation.provider}
Style: {requirement.video_generation.style}
Avatar: {requirement.video_generation.avatar_id or 'None'}
Lip Sync: {requirement.video_generation.lip_sync}

UPLOAD SPECIFICATION
Title: {requirement.upload_spec.title}
Hashtags: {', '.join(requirement.upload_spec.hashtags)}
Scheduled: {requirement.upload_spec.scheduled_time}
Visibility: {requirement.upload_spec.visibility}

ACCEPTANCE CRITERIA
{format_acceptance_criteria(requirement.acceptance_criteria)}

Use clean formatting with clear sections and professional layout.
"""
```

Skill config: `{"type": "anthropic", "skill_id": "pdf", "version": "latest"}`

## File Download Pattern

After generating any report, extract and download the file:

```python
from file_utils import download_all_files, extract_file_ids

file_ids = extract_file_ids(response)
if file_ids:
    results = download_all_files(
        client, response,
        output_dir="output/reports/",
        prefix=f"experiment_week{week}_"
    )
```

## Integration with Hooks

Reports can be auto-generated via hooks:

```json
{
  "PostToolUse": [
    {
      "matcher": "Write(requirements/completed/*)",
      "hooks": [{
        "type": "command",
        "command": "python scripts/generate_completion_report.py"
      }]
    }
  ]
}
```

## Token Optimization

- Use `"latest"` version for automatic optimization
- Batch multiple sheets/slides in a single request
- Reuse `container.id` from previous responses to avoid reloading skills
- Keep prompts specific — clear instructions reduce iterations
