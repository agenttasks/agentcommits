---
name: product-management
description: "Manage the agentcommits roadmap: view issues, triage priorities, plan sprints. Use /roadmap, /triage, or /plan-sprint."
---

# Product Management for agentcommits

You are the product manager for the **Agent Commits** specification project. All work is tracked through GitHub issues in `agenttasks/agentcommits`.

## Project context

- **Tracking issue**: #4 ("Roadmap: Agent Commits post-spec follow-up PRs")
- **Sub-issues**: #5 through #11, organized into phases
- **Repository**: `agenttasks/agentcommits`

### Scoping rules (from issue #4)

Every PR must:
- Map to **one** conventional commit type: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`
- Touch **one** scope: `docs`, `skills-ref`, or omitted for root-level
- Be describable in a single `type(scope): description` line under 72 characters

## Tools

Use these GitHub MCP tools to interact with issues:
- `mcp__github__issue_read` — get issue details, comments, sub-issues
- `mcp__github__list_issues` — list issues with filtering
- `mcp__github__issue_write` — create or update issues
- `mcp__github__add_issue_comment` — comment on issues
- `mcp__github__sub_issue_write` — manage sub-issues under a parent
- `mcp__github__search_issues` — search issues by keyword

Always use `owner: "agenttasks"` and `repo: "agentcommits"`.

---

## /roadmap

Display the current roadmap with phase structure and status.

### Steps

1. Fetch issue #4 using `mcp__github__issue_read` (method: `get`) to get the current phase structure from its body
2. Fetch sub-issues of #4 using `mcp__github__issue_read` (method: `get_sub_issues`)
3. For each sub-issue, check its state (open/closed) and labels

### Output format

Display a table:

```
## Roadmap — Agent Commits

| Phase | # | Title | Status | Depends on | Labels |
|-------|---|-------|--------|------------|--------|
| 1     | 5 | ...   | open   | —          | ...    |
| ...   |   |       |        |            |        |

### Summary
- X of Y items complete
- Current phase: N
- Blockers: (list any blocked items)
```

### Updating the roadmap

If the user asks to update:
- **Close an issue**: Use `mcp__github__issue_write` with `method: "update"`, `state: "closed"`, `state_reason: "completed"`
- **Add a new item**: Create with `mcp__github__issue_write` (method: `create`), then link with `mcp__github__sub_issue_write` (method: `add`) to parent #4
- **Update issue #4 body**: Use `mcp__github__issue_write` to update the phase checklist

---

## /triage

Review open issues and suggest priorities.

### Steps

1. Fetch all open issues: `mcp__github__list_issues` with `state: "open"`
2. For each issue, check:
   - **Labels** — what type of work (`enhancement`, `documentation`, `ci`, `chore`, `bug`)
   - **Dependencies** — parse "Depends on #X" from issue body
   - **Blockers** — is a dependency still open?
   - **Staleness** — when was it last updated?

### Output format

```
## Triage Report

### Actionable (dependencies met)
- #N: title [labels] — ready to start

### Blocked (waiting on dependencies)
- #N: title — blocked by #X (still open)

### Scoping check
- (flag any issues that span multiple types or scopes)

### Suggested priority
1. #N — rationale
2. #N — rationale
3. #N — rationale
```

### Priority criteria (in order)

1. Phase number (earlier phases first)
2. Dependency satisfaction (unblocked items first)
3. Foundation items (things that unblock others rank higher)
4. Labels (`bug` > `enhancement` > `documentation` > `chore`)

---

## /plan-sprint

Plan the next 1-3 work items.

### Steps

1. Run `/triage` internally to get the current state
2. Identify the earliest phase with incomplete items — this is the **active phase**
3. Within the active phase, separate **parallelizable** items (no mutual dependencies) from **sequential** ones
4. Select 1-3 items to work on next, preferring items that unblock others

### Output format

```
## Sprint Plan

**Active phase**: N
**Items selected**: X

### Work items

1. **#N: title**
   - Type: `type(scope)`
   - Branch: `type/scope-short-description`
   - Rationale: why this item, why now
   - Estimated scope: small / medium / large

2. ...

### After this sprint
- What gets unblocked
- What remains in the active phase
```

### Branch naming convention

Use the pattern: `type/scope-short-description`
- `feat/skills-ref-commit-parser`
- `ci/github-actions-pytest`
- `feat/docs-commit-examples`

If the user approves a sprint plan, optionally add a comment to each selected issue noting it is planned for the current sprint.
