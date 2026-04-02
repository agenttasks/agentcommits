"""Tests for pull request template compliance with Agent Commits spec.

Validates that .github/pull_request_template.md:
- Exists and is well-formed
- References the correct conventional commit types from the spec
- References the correct scopes from the project
- Includes required sections for agent attribution
- Renders deterministically across GitHub surfaces (no conditional blocks,
  no HTML that varies by client)
"""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = REPO_ROOT / ".github" / "pull_request_template.md"

# Allowed types from CLAUDE.md and the Agent Commits spec
ALLOWED_TYPES = {
    "feat", "fix", "docs", "style", "refactor",
    "perf", "test", "build", "ci", "chore", "revert",
}

# Scopes defined in CLAUDE.md for this project
PROJECT_SCOPES = {"docs", "skills-ref"}


@pytest.fixture
def template_content():
    """Read the PR template content."""
    assert TEMPLATE_PATH.exists(), (
        f"PR template not found at {TEMPLATE_PATH}. "
        "GitHub requires .github/pull_request_template.md for deterministic "
        "rendering across web, mobile, CLI, and API surfaces."
    )
    return TEMPLATE_PATH.read_text()


class TestTemplateExists:
    """Verify the template file exists in the canonical location."""

    def test_template_file_exists(self):
        assert TEMPLATE_PATH.exists(), (
            "PR template must be at .github/pull_request_template.md "
            "(not PULL_REQUEST_TEMPLATE/ directory) for deterministic "
            "auto-population across all GitHub surfaces."
        )

    def test_template_is_not_empty(self, template_content):
        assert len(template_content.strip()) > 0

    def test_template_uses_canonical_path(self):
        """The single-file path auto-loads on web, mobile, CLI, and API.
        Multiple templates in PULL_REQUEST_TEMPLATE/ require query params
        and don't work on mobile — avoid that pattern."""
        multi_template_dir = REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE"
        assert not multi_template_dir.exists(), (
            "Using PULL_REQUEST_TEMPLATE/ directory breaks deterministic "
            "loading on GitHub mobile and CLI. Use a single "
            "pull_request_template.md file instead."
        )


class TestConventionalCommitTypes:
    """Verify the template references the correct commit types."""

    def test_type_field_present(self, template_content):
        assert "**Type**:" in template_content, (
            "Template must include a Type field to guide PR authors "
            "toward conventional commit types."
        )

    def test_all_allowed_types_listed(self, template_content):
        """The template should list all allowed types so authors can pick."""
        for commit_type in ALLOWED_TYPES:
            assert commit_type in template_content, (
                f"Allowed type '{commit_type}' is missing from the template. "
                f"All types from the spec must be listed."
            )

    def test_no_unknown_types_in_type_field(self, template_content):
        """Extract the Type field line and verify no rogue types snuck in."""
        type_line_match = re.search(
            r"\*\*Type\*\*:\s*<!--\s*(.+?)\s*-->", template_content
        )
        assert type_line_match, "Could not parse the Type field comment"
        type_comment = type_line_match.group(1)
        # Extract words that look like commit types (lowercase, separated by / or space)
        mentioned_types = set(re.findall(r"\b([a-z]+)\b", type_comment))
        # Filter to only words that could be types (exclude filler words)
        filler = {"or", "a", "the", "of", "in", "and", "for", "leave", "blank", "level", "changes", "root"}
        mentioned_types -= filler
        unknown = mentioned_types - ALLOWED_TYPES
        assert not unknown, (
            f"Unknown types in template Type field: {unknown}. "
            f"Allowed types: {ALLOWED_TYPES}"
        )


class TestScopes:
    """Verify the template references the correct project scopes."""

    def test_scope_field_present(self, template_content):
        assert "**Scope**:" in template_content, (
            "Template must include a Scope field."
        )

    def test_project_scopes_listed(self, template_content):
        """All project scopes should appear in the template."""
        for scope in PROJECT_SCOPES:
            assert scope in template_content, (
                f"Project scope '{scope}' is missing from the template."
            )


class TestRequiredSections:
    """Verify the template includes all required sections."""

    def test_summary_section(self, template_content):
        assert "## Summary" in template_content

    def test_changes_section(self, template_content):
        assert re.search(r"##[#]?\s*Changes", template_content), (
            "Template must include a Changes section."
        )

    def test_breaking_changes_section(self, template_content):
        assert "## Breaking changes" in template_content, (
            "Template must include a Breaking changes section per the "
            "Agent Commits spec's breaking-changes field."
        )

    def test_test_plan_section(self, template_content):
        assert "## Test plan" in template_content

    def test_attribution_section(self, template_content):
        assert re.search(r"##\s*(Attribution|Agent)", template_content), (
            "Template must include an Attribution section per the "
            "Agent Commits spec's attribution field."
        )


class TestAgentAttribution:
    """Verify agent attribution fields align with the spec."""

    def test_agent_field_present(self, template_content):
        """The spec defines an Agent footer — template should capture this."""
        assert "**Agent**:" in template_content, (
            "Template must include an Agent field for attribution, "
            "matching the Agent Commits spec's Agent footer."
        )

    def test_ai_disclosure_checkbox(self, template_content):
        """CONTRIBUTING.md requires AI disclosure."""
        assert re.search(
            r"\[[ x]?\]\s*.*AI\s*assistance", template_content, re.IGNORECASE
        ), "Template must include an AI assistance disclosure checkbox."

    def test_conventional_commits_link(self, template_content):
        """Template should link to the conventional commits spec."""
        assert "conventionalcommits.org" in template_content


class TestConventionalCommitCompliance:
    """Verify the compliance checklist covers spec requirements."""

    def test_compliance_section_exists(self, template_content):
        assert "## Agent Commits compliance" in template_content

    def test_commit_message_checkbox(self, template_content):
        assert re.search(
            r"\[[ x]?\]\s*Commit messages follow", template_content
        ), "Must have a checkbox for commit message format compliance."

    def test_types_checkbox(self, template_content):
        assert re.search(
            r"\[[ x]?\]\s*Commit types are from", template_content
        ), "Must have a checkbox for type compliance."

    def test_scopes_checkbox(self, template_content):
        assert re.search(
            r"\[[ x]?\]\s*Scopes", template_content
        ), "Must have a checkbox for scope compliance."


class TestDeterministicRendering:
    """Verify the template renders deterministically across GitHub surfaces.

    GitHub auto-populates pull_request_template.md on:
    - github.com web UI (desktop and mobile browsers)
    - GitHub Mobile app (iOS/Android)
    - `gh pr create` CLI
    - GitHub API (POST /repos/{owner}/{repo}/pulls)

    For deterministic behavior:
    - Use standard Markdown only (no GitHub-specific extensions that vary)
    - Use HTML comments for guidance (rendered identically everywhere)
    - Avoid <details>/<summary> for critical content (collapsed by default
      varies across clients)
    - Avoid images/media that may not render on all surfaces
    """

    def test_no_github_specific_blocks(self, template_content):
        """Avoid blocks that render differently across surfaces."""
        # Note blocks (> [!NOTE]) render differently on mobile vs web
        assert "> [!NOTE]" not in template_content
        assert "> [!WARNING]" not in template_content
        assert "> [!IMPORTANT]" not in template_content

    def test_no_collapsed_critical_sections(self, template_content):
        """<details> blocks may be collapsed by default on some surfaces.
        Don't hide critical template sections behind them."""
        # If details is used, it should not wrap required sections
        if "<details>" in template_content:
            required_sections = [
                "## Summary", "## Agent Commits compliance",
                "## Breaking changes", "## Test plan",
            ]
            for section in required_sections:
                # Check the section header is NOT between <details> tags
                pattern = rf"<details>.*?{re.escape(section)}.*?</details>"
                assert not re.search(pattern, template_content, re.DOTALL), (
                    f"Required section '{section}' must not be inside "
                    f"a <details> block — it may be hidden on some surfaces."
                )

    def test_no_images_or_media(self, template_content):
        """Images may not render in CLI or API contexts."""
        assert "![" not in template_content, (
            "Avoid images in PR templates — they don't render in CLI "
            "or API-created PRs."
        )

    def test_uses_html_comments_for_guidance(self, template_content):
        """HTML comments are the standard way to provide inline guidance
        that works identically across all surfaces."""
        assert "<!--" in template_content, (
            "Use HTML comments for template guidance — they render "
            "consistently across all GitHub surfaces."
        )

    def test_no_raw_html_elements(self, template_content):
        """Avoid non-comment HTML that may render differently."""
        # Allow HTML comments but flag other HTML tags
        content_without_comments = re.sub(
            r"<!--.*?-->", "", template_content, flags=re.DOTALL
        )
        html_tags = re.findall(r"<(?!/)(\w+)", content_without_comments)
        # Filter out safe/expected tags
        unsafe = [t for t in html_tags if t.lower() not in ("br",)]
        assert not unsafe, (
            f"Avoid raw HTML elements {unsafe} — they may render "
            f"differently across GitHub surfaces. Use Markdown instead."
        )

    def test_checkboxes_are_unchecked(self, template_content):
        """All checkboxes should start unchecked for a clean template."""
        checked = re.findall(r"\[x\]", template_content, re.IGNORECASE)
        assert not checked, (
            "Template checkboxes must start unchecked ([ ]) so PR authors "
            "actively opt in. Pre-checked boxes are misleading."
        )

    def test_template_is_valid_utf8(self):
        """Ensure the file is valid UTF-8 (no encoding issues across surfaces)."""
        raw = TEMPLATE_PATH.read_bytes()
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError:
            pytest.fail("Template must be valid UTF-8.")

    def test_line_endings_are_unix(self):
        """Use LF line endings for consistent rendering."""
        raw = TEMPLATE_PATH.read_bytes()
        assert b"\r\n" not in raw, (
            "Use Unix (LF) line endings, not Windows (CRLF). "
            "CRLF can cause rendering differences in some contexts."
        )
