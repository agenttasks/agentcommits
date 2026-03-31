# Report Templates

Prompt templates for generating reports via Anthropic API Skills.

## Weekly Experiment Report (Excel)

```
Create an A/B experiment tracking spreadsheet with:

Sheet 1: Experiment Overview
- Experiment ID, week number, hypothesis, variable, status

Sheet 2: Variant A Metrics
| Platform | Views | Completions | Likes | Comments | Shares | Completion Rate | Engagement Rate | Composite Score |

Sheet 3: Variant B Metrics
(same columns as Variant A)

Sheet 4: Statistical Analysis
- p-value, effect size (Cohen's h), significance, winner

Include conditional formatting (green for winner), column charts, and summary formulas.
```

## Content Calendar (Excel)

```
Create a 7-day content calendar spreadsheet:

Columns: Day | Platform | Content Pillar | Headline | Hook | Duration (s) | Posting Time | Status

Include:
- Color-coded platforms (TikTok=pink, Instagram=purple, YouTube=red)
- Data validation dropdowns for Status (Draft, Ready, Published, Scheduled)
- Summary row with post counts per platform
```

## Strategy Deck (PowerPoint)

```
Create a content strategy presentation:

Slide 1: Title - "Social Media Content Report - Week {N}"
Slide 2: Performance Summary - Column chart of views by platform
Slide 3: A/B Experiment Results - Bar chart comparing variant scores
Slide 4: Next Week Plan - Content themes and next experiment hypothesis

Use clean, professional formatting.
```

## Requirement Specification (PDF)

```
Create a requirement specification PDF:

REQUIREMENT SPECIFICATION
- ID, Priority, Type, Source, Date

CONTENT SPECIFICATION
- Platform, Duration, Resolution, Script

VIDEO GENERATION
- Provider, Style, Avatar, Lip Sync

UPLOAD SPECIFICATION
- Title, Hashtags, Scheduled Time, Visibility

ACCEPTANCE CRITERIA
- Numbered list of criteria

Use clean formatting with clear sections.
```

## Token Optimization Notes

- Use `"latest"` version for automatic optimization
- Batch multiple sheets/slides in a single request
- Reuse `container.id` from previous responses to avoid reloading skills
- Keep prompts specific to reduce iterations
- Expected generation times: Excel ~2min, PowerPoint ~1-2min, PDF ~40-60s
