# CLAUDE.md

This repository defines the **Agent Commits** specification — a standard for how AI agents format, attribute, and structure commit messages.

## Repository Structure

- `docs/` — Specification documentation site (Mintlify)
- `skills-ref/` — Reference SDK for skill parsing and validation (Python, managed with `uv`)

See `docs/CLAUDE.md` and `skills-ref/CLAUDE.md` for subdirectory-specific guidance.

## Commit Conventions

This project uses [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). All commit messages must follow the format:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Allowed types

`feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

### Scopes

- `docs` — documentation site changes
- `skills-ref` — reference library changes
- Omit scope for root-level or cross-cutting changes

### Examples

```
feat(docs): add COMMIT.md specification page
fix(skills-ref): handle empty frontmatter gracefully
docs: update CONTRIBUTING with commit message guidelines
chore: add pre-commit config for commit message validation
```

### Breaking changes

Use `!` after the type/scope or add a `BREAKING CHANGE:` footer:

```
feat(docs)!: restructure specification navigation

BREAKING CHANGE: page URLs have changed
```

### Pre-commit hooks

This repo uses [pre-commit](https://pre-commit.com/) to validate commit messages. Install with:

```bash
uv run pre-commit install --hook-type commit-msg
```

### GPG signing

Commits in this repository are GPG-signed. Do not disable signing.
