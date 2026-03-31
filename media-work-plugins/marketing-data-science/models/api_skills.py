"""
Python SDK helpers for generating reports using Anthropic API Skills.

Provides utilities for creating Excel, PowerPoint, and PDF reports
from Pydantic model data using the Anthropic beta Skills API.
"""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Any

from anthropic import Anthropic


# Beta flags required for API Skills
SKILLS_BETAS = [
    "code-execution-2025-08-25",
    "files-api-2025-04-14",
    "skills-2025-10-02",
]

# Code execution tool required by all Skills requests
CODE_EXECUTION_TOOL = {"type": "code_execution_20250825", "name": "code_execution"}


def get_client() -> Anthropic:
    """Initialize Anthropic client from environment."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is required")
    return Anthropic(api_key=api_key)


def generate_with_skill(
    client: Anthropic,
    skill_id: str,
    prompt: str,
    model: str = "claude-sonnet-4-6",
    max_tokens: int = 4096,
) -> Any:
    """
    Generate a file using an Anthropic API Skill.

    Args:
        client: Anthropic client instance
        skill_id: One of 'xlsx', 'pptx', 'pdf'
        prompt: Instructions for file generation
        model: Model to use
        max_tokens: Max tokens for response

    Returns:
        Beta Messages response with file content
    """
    return client.beta.messages.create(
        model=model,
        max_tokens=max_tokens,
        container={
            "skills": [
                {"type": "anthropic", "skill_id": skill_id, "version": "latest"}
            ]
        },
        tools=[CODE_EXECUTION_TOOL],
        messages=[{"role": "user", "content": prompt}],
        betas=SKILLS_BETAS,
    )


def extract_file_ids(response: Any) -> list[str]:
    """Extract file IDs from a Skills API response."""
    file_ids = []
    for block in response.content:
        if hasattr(block, "content"):
            # Code execution result blocks
            for item in block.content:
                if hasattr(item, "file_id"):
                    file_ids.append(item.file_id)
        if hasattr(block, "file_id"):
            file_ids.append(block.file_id)
    return file_ids


def download_file(
    client: Anthropic,
    file_id: str,
    output_dir: str,
    filename: str | None = None,
) -> Path:
    """
    Download a file from the Anthropic Files API.

    Args:
        client: Anthropic client instance
        file_id: File ID from API response
        output_dir: Directory to save file
        filename: Optional override filename

    Returns:
        Path to downloaded file
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Get file metadata
    file_metadata = client.beta.files.retrieve(file_id=file_id)
    save_name = filename or file_metadata.filename

    file_path = output_path / save_name

    # Download file content
    content = client.beta.files.content(file_id=file_id)
    file_path.write_bytes(content.read())

    return file_path


def download_all_files(
    client: Anthropic,
    response: Any,
    output_dir: str,
    prefix: str = "",
) -> list[dict[str, Any]]:
    """
    Download all files from a Skills API response.

    Args:
        client: Anthropic client instance
        response: Skills API response
        output_dir: Directory to save files
        prefix: Filename prefix

    Returns:
        List of dicts with download results
    """
    results = []
    file_ids = extract_file_ids(response)

    for file_id in file_ids:
        try:
            file_metadata = client.beta.files.retrieve(file_id=file_id)
            filename = f"{prefix}{file_metadata.filename}" if prefix else file_metadata.filename
            path = download_file(client, file_id, output_dir, filename)
            results.append({
                "success": True,
                "file_id": file_id,
                "output_path": str(path),
                "size": path.stat().st_size,
            })
        except Exception as e:
            results.append({
                "success": False,
                "file_id": file_id,
                "error": str(e),
            })

    return results


# --- Report generators using Pydantic models ---


def generate_experiment_report_xlsx(
    client: Anthropic,
    experiment_data: dict[str, Any],
    output_dir: str = "output/reports",
) -> list[dict[str, Any]]:
    """Generate an Excel experiment report from experiment data."""
    prompt = f"""Create an A/B experiment tracking spreadsheet with:

Sheet 1: Experiment Overview
- Experiment ID: {experiment_data.get('experiment_id', 'N/A')}
- Week: {experiment_data.get('week_number', 'N/A')}
- Hypothesis: {experiment_data.get('hypothesis', 'N/A')}
- Variable: {experiment_data.get('variable', 'N/A')}
- Status: {experiment_data.get('status', 'N/A')}

Sheet 2: Variant Comparison
Create a comparison table with columns for each metric and rows for each variant.
Use the following data: {experiment_data.get('results', {})}

Include:
- Conditional formatting (green for better, red for worse)
- Column charts comparing variants
- Summary formulas
- Professional formatting with headers
"""
    response = generate_with_skill(client, "xlsx", prompt)
    return download_all_files(client, response, output_dir, prefix="experiment_")


def generate_content_calendar_xlsx(
    client: Anthropic,
    calendar_data: dict[str, Any],
    output_dir: str = "output/reports",
) -> list[dict[str, Any]]:
    """Generate an Excel content calendar from calendar data."""
    prompt = f"""Create a 7-day content calendar spreadsheet:

Columns: Day | Platform | Content Pillar | Headline | Hook | Duration (s) | Posting Time | Status

Data: {calendar_data.get('briefs', [])}
Week starting: {calendar_data.get('week_start', 'N/A')}

Include:
- Color-coded platforms (TikTok=pink, Instagram=purple, YouTube=red)
- Data validation dropdowns for Status (Draft, Ready, Published, Scheduled)
- Conditional formatting for status
- Summary row with post counts per platform
"""
    response = generate_with_skill(client, "xlsx", prompt)
    return download_all_files(client, response, output_dir, prefix="calendar_")


def generate_strategy_deck_pptx(
    client: Anthropic,
    report_data: dict[str, Any],
    output_dir: str = "output/reports",
) -> list[dict[str, Any]]:
    """Generate a PowerPoint strategy deck from report data."""
    prompt = f"""Create a content strategy presentation:

Slide 1: Title
- "Social Media Content Report - Week {report_data.get('week_number', 'N/A')}"
- Subtitle: "Claude Code CHANGELOG Updates"

Slide 2: Performance Summary
- Column chart: Views by platform
- Key metrics from: {report_data.get('metrics', {})}

Slide 3: A/B Experiment Results
- Experiment: {report_data.get('experiment', {})}
- Include bar chart comparing variant scores

Slide 4: Next Week Plan
- Upcoming content themes
- Next experiment hypothesis: {report_data.get('next_hypothesis', 'TBD')}

Use clean, professional formatting.
"""
    response = generate_with_skill(client, "pptx", prompt)
    return download_all_files(client, response, output_dir, prefix="strategy_")


def generate_requirement_pdf(
    client: Anthropic,
    requirement_data: dict[str, Any],
    output_dir: str = "output/reports",
) -> list[dict[str, Any]]:
    """Generate a PDF requirement specification from requirement data."""
    prompt = f"""Create a requirement specification PDF:

REQUIREMENT SPECIFICATION
ID: {requirement_data.get('requirement_id', 'N/A')}
Priority: {requirement_data.get('priority', 'N/A')}
Type: {requirement_data.get('type', 'N/A')}
Source: {requirement_data.get('source_skill', 'N/A')}
Date: {requirement_data.get('created_at', 'N/A')}

CONTENT SPECIFICATION
{_format_dict(requirement_data.get('content_spec', {}))}

VIDEO GENERATION
{_format_dict(requirement_data.get('video_generation', {}))}

UPLOAD SPECIFICATION
{_format_dict(requirement_data.get('upload_spec', {}))}

ACCEPTANCE CRITERIA
{_format_list(requirement_data.get('acceptance_criteria', []))}

Use clean formatting with clear sections and professional layout.
"""
    response = generate_with_skill(client, "pdf", prompt)
    return download_all_files(client, response, output_dir, prefix="requirement_")


def _format_dict(data: dict[str, Any]) -> str:
    """Format a dict as key-value lines."""
    if not data:
        return "N/A"
    return "\n".join(f"- {k}: {v}" for k, v in data.items())


def _format_list(items: list[str]) -> str:
    """Format a list as numbered items."""
    if not items:
        return "- None specified"
    return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))
