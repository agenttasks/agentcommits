# Marketing Data Science Plugin

Content strategy and data science plugin for creating daily social media shorts from the
[Anthropic Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).

## Skills

| Skill | Description |
|-------|-------------|
| `base-session` | Base session context with telemetry, costs, logging, device surface detection |
| `changelog-content` | Parses CHANGELOG.md and generates content briefs |
| `content-strategy` | Multi-platform content strategy for Instagram, TikTok, YouTube Shorts |
| `cold-start-strategy` | 30-day cold start plan for launching from zero |
| `ab-experiment-measurement` | Week-based A/B experiment framework with statistical analysis |
| `research-account-setup` | Platform account and API setup guide |
| `requirements-handoff` | Structured requirements handoff to platform-engineering |
| `api-skills-reports` | Report generation using Anthropic API Skills (xlsx, pptx, pdf) |
| `custom-skill-deployment` | Deploy plugin skills as Custom API Skills |
| `generate-content` | Generate content briefs from CHANGELOG updates |
| `run-experiment` | Create and manage A/B experiments |
| `generate-report` | Generate downloadable reports (Excel, PowerPoint, PDF) |

## Content Pipeline

```
CHANGELOG.md → changelog-content → content-strategy → requirements-handoff → platform-engineering
                                         |
                                  cold-start-strategy (phase adjustment)
                                         |
                                  ab-experiment-measurement (variant tracking)
```

## Installation

```bash
claude plugin marketplace add agenttasks/media-work-plugins
claude plugin install marketing-data-science@media-work-plugins
```
