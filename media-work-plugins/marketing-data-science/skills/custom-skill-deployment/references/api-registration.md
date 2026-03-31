# API Registration Steps

## Registering a Plugin Skill as a Custom API Skill

1. Read the target plugin skill's `SKILL.md` file from the skills directory.
2. Extract the `name`, `description`, and body content.
3. Call the Anthropic Skills API to create a new custom skill:
   - Set `display_name` to the API Display Title from the skill registry.
   - Set `instructions` to the SKILL.md body content.
   - Set `description` to the frontmatter description.
4. Store the returned `skill_id` for composition use.

## Composing Skills in API Requests

Include both custom and managed skill IDs in the `container.skills` array:

- `custom_skill_ids`: list of registered custom skill IDs.
- `anthropic_skill_ids`: list of managed skill names (e.g., `"pptx"`, `"xlsx"`, `"pdf"`).

Required beta flags:
- `code-execution-2025-08-25`
- `files-api-2025-04-14`
- `skills-2025-10-02`

Required tools:
- `code_execution` (type: `code_execution_20250825`)

## Updating Existing Skills

Re-registering a skill that already exists creates a new version. The API
returns status `"updated"` for existing skills and `"created"` for new ones.

## Listing Deployed Skills

Query the Anthropic Skills API workspace listing endpoint to see all registered
custom skills, their versions, and creation timestamps.

## Removing Skills

Delete skills via the Anthropic Skills API using the `skill_id`. All versions
of the skill are removed.

## Token Optimization

- Deploy only skills that are composed frequently.
- Batch multiple skill compositions per request when possible.
- Reuse `container.id` from previous responses to avoid reloading skill content.
