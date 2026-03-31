---
name: custom-skill-deployment
description: |
  Deploys marketing-data-science plugin skills as Custom API Skills via the Anthropic
  beta Skills API. Enables skill composition with xlsx/pptx/pdf for report generation.
allowed-tools: Read, Write, Bash
---

# Custom Skill Deployment

This skill manages the deployment of marketing-data-science plugin skills as
Custom API Skills, enabling them to be used in API-based workflows outside
of Claude Code sessions.

## Architecture

```
Plugin Skills (SKILL.md)          Custom API Skills (Anthropic API)
─────────────────────────         ──────────────────────────────────
Claude Code sessions              API-based workflows
Local/project scope               Workspace-wide scope
Progressive disclosure            Progressive disclosure
Free (included in Claude Code)    Token-based pricing

                    ┌─────────────────┐
Plugin Skills ───►  │  skill_manager  │ ───► Custom API Skills
                    │   .py deploy    │
                    └─────────────────┘
```

## Deployment

### Deploy All Skills
```bash
cd marketing-data-science
python scripts/skill_manager.py deploy
```

### Deploy Specific Skills
```bash
python scripts/skill_manager.py deploy content-strategy ab-experiment-measurement
```

### List Deployed Skills
```bash
python scripts/skill_manager.py list
```

### Remove All Deployed Skills
```bash
python scripts/skill_manager.py undeploy
```

## Skill Registry

| Plugin Skill | API Display Title | Composable With |
|-------------|-------------------|-----------------|
| `changelog-content` | CHANGELOG Content Extractor | pdf |
| `content-strategy` | Social Media Content Strategy | pptx, pdf |
| `cold-start-strategy` | Social Media Cold Start Strategy | pptx, pdf |
| `ab-experiment-measurement` | A/B Experiment Measurement | xlsx |
| `research-account-setup` | Social Media Account Setup | pdf |
| `api-skills-reports` | Content Pipeline Report Generator | xlsx, pptx, pdf |

## Skill Composition

Custom skills can be composed with Anthropic managed skills in a single request:

```python
from scripts.skill_manager import compose_skills, get_client, test_skill

client = get_client()

# Compose content strategy with PowerPoint generation
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    container={
        "skills": compose_skills(
            custom_skill_ids=[content_strategy_skill_id],
            anthropic_skill_ids=["pptx"],
        )
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{
        "role": "user",
        "content": "Create a content strategy deck for next week's CHANGELOG updates"
    }],
    betas=[
        "code-execution-2025-08-25",
        "files-api-2025-04-14",
        "skills-2025-10-02",
    ],
)
```

## Versioning

When plugin skills are updated, create new API skill versions:

```python
from scripts.skill_manager import deploy_all_skills

# Re-deploying automatically creates new versions for existing skills
results = deploy_all_skills()
# Results show "updated" for existing skills, "created" for new ones
```

### Version Strategy
- Use `"latest"` in API requests (recommended)
- Pin specific versions for production stability
- Versions use epoch timestamps
- All versions are retained until explicitly deleted

## Progressive Disclosure

Custom API Skills follow the same three-tier loading:

1. **Metadata** (~64 chars name + ~1024 chars description): Always in context
2. **Full instructions** (SKILL.md content, <5k tokens): Loaded when relevant
3. **Scripts and resources**: Loaded during code execution

This means deploying all 6 skills adds minimal overhead — Claude only loads
the full content when a skill is actually needed.

## Token Optimization

- Deploy skills you'll compose frequently
- Use `"latest"` version for automatic optimization
- Batch operations: compose multiple skills per request
- Reuse `container.id` from previous responses to avoid reloading

## Security Notes

- API keys: Never included in skill files
- Skills are workspace-scoped (private to your API key)
- Skill content is not shared across workspaces
- Use environment variables for all credentials
