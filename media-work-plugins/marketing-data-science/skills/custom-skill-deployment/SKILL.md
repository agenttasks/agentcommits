---
name: custom-skill-deployment
description: |
  Deploys marketing-data-science plugin skills as Custom API Skills via the
  Anthropic Skills API. Manages skill registration, versioning, and composition
  with xlsx/pptx/pdf managed skills for report generation.
allowed-tools: Read, Write, Bash
---

# Custom Skill Deployment

Deploy plugin skills from this workspace as Custom API Skills via the Anthropic
Skills API, enabling use in API-based workflows outside of Claude Code sessions.

## Skill Registry

Register each plugin skill with its API display title and composable managed skills:

| Plugin Skill | API Display Title | Composable With |
|---|---|---|
| `changelog-content` | CHANGELOG Content Extractor | pdf |
| `content-strategy` | Social Media Content Strategy | pptx, pdf |
| `cold-start-strategy` | Social Media Cold Start Strategy | pptx, pdf |
| `ab-experiment-measurement` | A/B Experiment Measurement | xlsx |
| `research-account-setup` | Social Media Account Setup | pdf |
| `api-skills-reports` | Content Pipeline Report Generator | xlsx, pptx, pdf |

## Deployment Steps

1. Read the SKILL.md content for the target plugin skill.
2. Register it as a Custom API Skill via the Anthropic Skills API endpoint.
3. Record the returned `skill_id` for use in composition requests.
4. Verify the skill appears in the workspace skill listing.

For detailed API registration steps, see [references/api-registration.md](references/api-registration.md).

## Skill Composition

Compose custom skills with Anthropic managed skills (xlsx, pptx, pdf) in a
single API request by including both custom and managed skill IDs in the
`container.skills` array.

- Include the `code_execution` tool for report generation workflows.
- Use `betas` flags for code-execution, files-api, and skills features.

## Versioning

- Prefer `"latest"` version references in API requests.
- Pin specific versions for production stability when needed.
- Re-registering an existing skill creates a new version automatically.
- All versions are retained until explicitly deleted.

## Progressive Disclosure

Custom API Skills follow three-tier loading:

1. **Metadata** (~64 chars name + ~1024 chars description): always in context.
2. **Full instructions** (SKILL.md content, under 5k tokens): loaded when relevant.
3. **Resources**: loaded during code execution.

## Security

- Never include API keys in skill files.
- Skills are workspace-scoped (private to the API key).
- Store all credentials in environment variables.
