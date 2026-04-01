# Agent Commits

A specification for how AI agents format, attribute, and structure commit messages.

## What is Agent Commits?

Agent Commits defines a standard file format (`COMMIT.md`) that tells any AI agent how a project wants commits formatted. It extends [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) with agent-specific concerns: attribution, commit splitting, and per-project configuration.

Just as [Agent Skills](https://agentskills.io) defines how agents learn specialized workflows through `SKILL.md` files, Agent Commits defines how agents produce structured commit messages through `COMMIT.md` files.

## The problem

Every AI coding agent handles commits differently. There is no agent-agnostic standard for:

- How agents should format commit messages in a given project
- How to attribute AI-generated commits (which agent, which model, which human prompted it)
- When agents should split work into multiple commits
- How projects declare their commit conventions in a way any agent can read

## The solution

A `COMMIT.md` file — placed at `.agents/commits/COMMIT.md` or at the project root — declares commit conventions with YAML frontmatter and Markdown instructions:

```markdown
---
name: my-project
spec: agent-commits/1.0
types: [feat, fix, docs, chore, refactor, test]
scopes: [api, cli, docs]
attribution:
  require-agent-footer: true
---

# Commit Conventions

Keep descriptions under 72 characters. Scope is required for package-specific changes.
```

Any agent that supports Agent Commits can discover this file, parse the frontmatter, and follow the conventions — no tool-specific configuration needed.

## Documentation

Read the full specification at the [documentation site](https://agentcommits.io) (coming soon), or browse the `docs/` directory.

## Structure

- `docs/` — Specification documentation site (Mintlify)
- `skills-ref/` — Reference SDK for skill parsing and validation (Python, managed with `uv`)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. This project uses conventional commits — see the commit message conventions section.

## License

Code in this repository is licensed under [Apache 2.0](LICENSE).
