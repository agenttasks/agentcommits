"""
Skill management utilities for deploying, versioning, and testing
marketing-data-science plugin skills as Custom API Skills.

Custom API Skills are registered via the Anthropic beta Skills API and
enable Claude to use the plugin's expertise in API-based workflows
(not just Claude Code sessions).
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from anthropic import Anthropic
from anthropic.lib import files_from_dir


# Beta flags
SKILLS_BETAS = [
    "code-execution-2025-08-25",
    "files-api-2025-04-14",
    "skills-2025-10-02",
]

CODE_EXECUTION_TOOL = {"type": "code_execution_20250825", "name": "code_execution"}

# Skill registry: maps plugin skill names to display titles
SKILL_REGISTRY = {
    "changelog-content": {
        "display_title": "CHANGELOG Content Extractor",
        "path": "skills/changelog-content",
    },
    "content-strategy": {
        "display_title": "Social Media Content Strategy",
        "path": "skills/content-strategy",
    },
    "cold-start-strategy": {
        "display_title": "Social Media Cold Start Strategy",
        "path": "skills/cold-start-strategy",
    },
    "ab-experiment-measurement": {
        "display_title": "A/B Experiment Measurement",
        "path": "skills/ab-experiment-measurement",
    },
    "research-account-setup": {
        "display_title": "Social Media Account Setup",
        "path": "skills/research-account-setup",
    },
    "api-skills-reports": {
        "display_title": "Content Pipeline Report Generator",
        "path": "skills/api-skills-reports",
    },
}


def get_client() -> Anthropic:
    """Initialize Anthropic client with Skills beta."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable required")
    return Anthropic(
        api_key=api_key,
        default_headers={"anthropic-beta": "skills-2025-10-02"},
    )


def get_plugin_root() -> Path:
    """Get the marketing-data-science plugin root directory."""
    # Try relative to this script
    script_dir = Path(__file__).parent
    plugin_root = script_dir.parent
    if (plugin_root / ".claude-plugin" / "plugin.json").exists():
        return plugin_root
    # Fallback: try current directory
    cwd = Path.cwd()
    if (cwd / ".claude-plugin" / "plugin.json").exists():
        return cwd
    raise FileNotFoundError(
        "Cannot find plugin root. Run from marketing-data-science directory."
    )


# --- CRUD Operations ---


def create_skill(
    client: Anthropic,
    skill_path: str,
    display_title: str,
) -> dict[str, Any]:
    """
    Create a new custom API skill from a directory.

    Args:
        client: Anthropic client with skills beta
        skill_path: Path to skill directory (must contain SKILL.md)
        display_title: Human-readable name (must be unique in workspace)

    Returns:
        Dict with skill_id, version, and metadata
    """
    try:
        skill = client.beta.skills.create(
            display_title=display_title,
            files=files_from_dir(skill_path),
        )
        return {
            "success": True,
            "skill_id": skill.id,
            "display_title": skill.display_title,
            "latest_version": skill.latest_version,
            "created_at": skill.created_at,
            "source": skill.source,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


def create_skill_version(
    client: Anthropic,
    skill_id: str,
    skill_path: str,
) -> dict[str, Any]:
    """
    Create a new version of an existing custom skill.

    Args:
        client: Anthropic client
        skill_id: Existing skill ID
        skill_path: Path to updated skill directory

    Returns:
        Dict with version info
    """
    try:
        version = client.beta.skills.versions.create(
            skill_id=skill_id,
            files=files_from_dir(skill_path),
        )
        return {
            "success": True,
            "version": version.version,
            "created_at": version.created_at,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


def list_custom_skills(client: Anthropic) -> list[dict[str, Any]]:
    """List all custom skills in the workspace."""
    try:
        response = client.beta.skills.list(source="custom")
        return [
            {
                "skill_id": s.id,
                "display_title": s.display_title,
                "latest_version": s.latest_version,
                "created_at": s.created_at,
                "updated_at": s.updated_at,
            }
            for s in response.data
        ]
    except Exception as e:
        print(f"Error listing skills: {e}")
        return []


def delete_skill(client: Anthropic, skill_id: str) -> bool:
    """Delete a custom skill and all its versions."""
    try:
        versions = client.beta.skills.versions.list(skill_id=skill_id)
        for v in versions.data:
            client.beta.skills.versions.delete(
                skill_id=skill_id, version=v.version
            )
        client.beta.skills.delete(skill_id)
        return True
    except Exception as e:
        print(f"Error deleting skill {skill_id}: {e}")
        return False


def test_skill(
    client: Anthropic,
    skill_id: str,
    test_prompt: str,
    model: str = "claude-sonnet-4-6",
    additional_skills: list[dict[str, Any]] | None = None,
) -> Any:
    """
    Test a custom skill with a prompt.

    Args:
        client: Anthropic client
        skill_id: Skill to test
        test_prompt: Test prompt
        model: Model to use
        additional_skills: Extra skills to compose (e.g. xlsx, pptx, pdf)

    Returns:
        Messages API response
    """
    skills = [{"type": "custom", "skill_id": skill_id, "version": "latest"}]
    if additional_skills:
        skills.extend(additional_skills)

    return client.beta.messages.create(
        model=model,
        max_tokens=4096,
        container={"skills": skills},
        tools=[CODE_EXECUTION_TOOL],
        messages=[{"role": "user", "content": test_prompt}],
        betas=SKILLS_BETAS,
    )


# --- Deployment Operations ---


def deploy_all_skills(
    client: Anthropic | None = None,
    plugin_root: Path | None = None,
    skill_names: list[str] | None = None,
) -> dict[str, Any]:
    """
    Deploy all (or selected) plugin skills as Custom API Skills.

    Args:
        client: Anthropic client (created if None)
        plugin_root: Plugin root directory (detected if None)
        skill_names: Specific skills to deploy (all if None)

    Returns:
        Dict mapping skill names to deployment results
    """
    if client is None:
        client = get_client()
    if plugin_root is None:
        plugin_root = get_plugin_root()

    targets = skill_names or list(SKILL_REGISTRY.keys())
    results = {}

    # Check for existing skills to avoid name conflicts
    existing = {s["display_title"]: s for s in list_custom_skills(client)}

    for name in targets:
        if name not in SKILL_REGISTRY:
            results[name] = {"success": False, "error": f"Unknown skill: {name}"}
            continue

        entry = SKILL_REGISTRY[name]
        skill_path = plugin_root / entry["path"]

        if not skill_path.exists():
            results[name] = {
                "success": False,
                "error": f"Directory not found: {skill_path}",
            }
            continue

        title = entry["display_title"]

        # If skill already exists, create a new version instead
        if title in existing:
            existing_skill = existing[title]
            print(f"  Updating {name} (existing: {existing_skill['skill_id']})...")
            result = create_skill_version(
                client, existing_skill["skill_id"], str(skill_path)
            )
            if result["success"]:
                result["skill_id"] = existing_skill["skill_id"]
                result["action"] = "updated"
        else:
            print(f"  Creating {name}...")
            result = create_skill(client, str(skill_path), title)
            if result["success"]:
                result["action"] = "created"

        results[name] = result

    return results


def undeploy_all_skills(
    client: Anthropic | None = None,
) -> dict[str, bool]:
    """Remove all plugin skills from the Custom API Skills workspace."""
    if client is None:
        client = get_client()

    existing = list_custom_skills(client)
    plugin_titles = {e["display_title"] for e in SKILL_REGISTRY.values()}
    results = {}

    for skill in existing:
        if skill["display_title"] in plugin_titles:
            name = skill["display_title"]
            results[name] = delete_skill(client, skill["skill_id"])

    return results


# --- Composition Helpers ---


def compose_skills(
    custom_skill_ids: list[str],
    anthropic_skill_ids: list[str] | None = None,
) -> list[dict[str, Any]]:
    """
    Build a skills list for composing custom + Anthropic skills.

    Example:
        skills = compose_skills(
            custom_skill_ids=[content_strategy_id],
            anthropic_skill_ids=["xlsx", "pptx"]
        )
        response = client.beta.messages.create(
            container={"skills": skills},
            ...
        )
    """
    skills: list[dict[str, Any]] = []
    for sid in custom_skill_ids:
        skills.append({"type": "custom", "skill_id": sid, "version": "latest"})
    for aid in anthropic_skill_ids or []:
        skills.append({"type": "anthropic", "skill_id": aid, "version": "latest"})
    return skills


# --- CLI Entry Point ---


def main() -> None:
    """CLI for deploying and managing skills."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python skill_manager.py <command> [args]")
        print("")
        print("Commands:")
        print("  deploy [skill_name ...]  Deploy skills as Custom API Skills")
        print("  undeploy                 Remove all deployed plugin skills")
        print("  list                     List all custom skills in workspace")
        print("  test <skill_name>        Test a deployed skill")
        return

    cmd = sys.argv[1]
    client = get_client()

    if cmd == "deploy":
        skill_names = sys.argv[2:] if len(sys.argv) > 2 else None
        print("Deploying skills as Custom API Skills...")
        results = deploy_all_skills(client, skill_names=skill_names)
        print("\nResults:")
        for name, result in results.items():
            status = "OK" if result.get("success") else "FAIL"
            action = result.get("action", "")
            detail = result.get("skill_id", result.get("error", ""))
            print(f"  [{status}] {name} ({action}) - {detail}")

    elif cmd == "undeploy":
        print("Removing deployed plugin skills...")
        results = undeploy_all_skills(client)
        for name, success in results.items():
            status = "OK" if success else "FAIL"
            print(f"  [{status}] {name}")

    elif cmd == "list":
        skills = list_custom_skills(client)
        if skills:
            for s in skills:
                print(f"  {s['display_title']} (v{s['latest_version']}) - {s['skill_id']}")
        else:
            print("  No custom skills found.")

    elif cmd == "test":
        if len(sys.argv) < 3:
            print("Usage: python skill_manager.py test <skill_name>")
            return
        skill_name = sys.argv[2]
        skills = list_custom_skills(client)
        registry_entry = SKILL_REGISTRY.get(skill_name)
        if not registry_entry:
            print(f"Unknown skill: {skill_name}")
            return
        title = registry_entry["display_title"]
        match = next((s for s in skills if s["display_title"] == title), None)
        if not match:
            print(f"Skill '{title}' not deployed. Run: python skill_manager.py deploy {skill_name}")
            return
        print(f"Testing {title}...")
        response = test_skill(
            client, match["skill_id"], f"Demonstrate the {title} skill with a brief example."
        )
        for block in response.content:
            if block.type == "text":
                print(block.text)

    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
