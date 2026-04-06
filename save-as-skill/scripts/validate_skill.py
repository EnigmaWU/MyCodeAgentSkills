#!/usr/bin/env python3
"""Validate a SKILL.md against the SIMPLE, COMPLICATED, or COMPLEX template tiers.

Usage:
    python validate_skill.py path/to/SKILL.md --tier complex
    python validate_skill.py path/to/SKILL.md --tier auto
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TIER_SECTIONS = {
    "simple": [
        "Who",
        "What",
        "When",
        "Where",
        "Why",
        "How",
        "One More Thing",
    ],
    "complicated": [
        "Who",
        "What",
        "When",
        "Where",
        "Why",
        "Inputs",
        "Output",
        "Constraints",
        "One More Thing",
        "How",
    ],
    "complex": [
        "Who",
        "What",
        "When",
        "Where",
        "Why",
        "Inputs",
        "Output",
        "Constraints",
        "One More Thing",
        "How",
        "Resources",
        "Validation",
    ],
}

TIER_PRIORITY = ["complex", "complicated", "simple"]
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FRONTMATTER_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$")


def normalize_heading(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).lower()


def split_frontmatter(text: str) -> tuple[dict[str, str], dict[str, str], list[str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("Missing YAML frontmatter opening '---' on line 1")

    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break

    if end_index is None:
        raise ValueError("Missing YAML frontmatter closing '---'")

    frontmatter_lines = lines[1:end_index]
    body_lines = lines[end_index + 1 :]
    fields: dict[str, str] = {}
    raw_fields: dict[str, str] = {}

    for line in frontmatter_lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = FRONTMATTER_RE.match(line)
        if not match:
            continue
        key = match.group(1)
        value = match.group(2)
        fields[key] = value.strip().strip("\"'")
        raw_fields[key] = value.strip()

    return fields, raw_fields, lines, body_lines


def extract_headings(lines: list[str]) -> list[dict[str, object]]:
    headings: list[dict[str, object]] = []
    inside_fence = False

    for index, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            inside_fence = not inside_fence
            continue
        if inside_fence:
            continue

        match = HEADING_RE.match(line)
        if not match:
            continue

        headings.append(
            {
                "level": len(match.group(1)),
                "text": match.group(2).strip(),
                "line": index,
            }
        )

    return headings


def sections_in_order(actual: list[str], expected: list[str]) -> bool:
    position = -1
    lowered = [normalize_heading(section) for section in actual]

    for required in expected:
        required_normalized = normalize_heading(required)
        try:
            position = next(
                index
                for index in range(position + 1, len(lowered))
                if lowered[index] == required_normalized
            )
        except StopIteration:
            return False

    return True


def infer_tier(actual_sections: list[str]) -> str | None:
    for tier in TIER_PRIORITY:
        if sections_in_order(actual_sections, TIER_SECTIONS[tier]):
            return tier
    return None


def collect_section_bodies(lines: list[str], headings: list[dict[str, object]]) -> dict[str, str]:
    h2_sections = [heading for heading in headings if heading["level"] == 2]
    section_bodies: dict[str, str] = {}

    for index, heading in enumerate(h2_sections):
        start_line = int(heading["line"]) + 1
        if index + 1 < len(h2_sections):
            end_line = int(h2_sections[index + 1]["line"]) - 1
        else:
            end_line = len(lines)
        body = "\n".join(lines[start_line - 1 : end_line]).strip()
        section_bodies[str(heading["text"])] = body

    return section_bodies


def validate_skill(skill_path: Path, requested_tier: str) -> tuple[str, list[str], list[str]]:
    text = skill_path.read_text(encoding="utf-8")
    fields, raw_fields, lines, _body_lines = split_frontmatter(text)
    headings = extract_headings(lines)

    errors: list[str] = []
    warnings: list[str] = []

    if "name" not in fields or not fields["name"]:
        errors.append("Missing required frontmatter field: name")
    if "description" not in fields or not fields["description"]:
        errors.append("Missing required frontmatter field: description")

    raw_description = raw_fields.get("description", "")
    if raw_description and ":" in raw_description and raw_description[:1] not in {"'", '"'}:
        errors.append("Frontmatter description should be quoted when it contains colons")

    if skill_path.name == "SKILL.md" and "name" in fields:
        expected_name = skill_path.parent.name
        if fields["name"] != expected_name:
            errors.append(
                f"Frontmatter name '{fields['name']}' does not match folder name '{expected_name}'"
            )

    h1_headings = [heading for heading in headings if heading["level"] == 1]
    if not h1_headings:
        errors.append("Missing required level-1 title heading")
    elif len(h1_headings) > 1:
        warnings.append("More than one level-1 heading found")

    h2_headings = [heading for heading in headings if heading["level"] == 2]
    actual_sections = [str(heading["text"]) for heading in h2_headings]

    if requested_tier == "auto":
        inferred_tier = infer_tier(actual_sections)
        if inferred_tier is None:
            errors.append("Could not infer a matching template tier from the level-2 section layout")
            tier = "simple"
        else:
            tier = inferred_tier
    else:
        tier = requested_tier

    expected_sections = TIER_SECTIONS[tier]
    expected_lookup = {normalize_heading(section) for section in expected_sections}
    actual_lookup = [normalize_heading(section) for section in actual_sections]

    if not sections_in_order(actual_sections, expected_sections):
        for section in expected_sections:
            if normalize_heading(section) not in actual_lookup:
                errors.append(f"Missing required section for {tier}: {section}")

        matched_positions = []
        position = -1
        for section in expected_sections:
            normalized = normalize_heading(section)
            try:
                position = next(
                    index
                    for index in range(position + 1, len(actual_lookup))
                    if actual_lookup[index] == normalized
                )
                matched_positions.append(position)
            except StopIteration:
                break
        if len(matched_positions) >= 2 and matched_positions != sorted(matched_positions):
            errors.append(f"Required sections are out of order for {tier}")
    else:
        for section in expected_sections:
            if normalize_heading(section) not in actual_lookup:
                errors.append(f"Missing required section for {tier}: {section}")

    seen_sections: dict[str, int] = {}
    for heading in h2_headings:
        normalized = normalize_heading(str(heading["text"]))
        if normalized in seen_sections:
            warnings.append(
                f"Duplicate level-2 section: {heading['text']} (line {heading['line']})"
            )
        seen_sections[normalized] = int(heading["line"])
        if normalized not in expected_lookup:
            warnings.append(
                f"Extra level-2 section not in the {tier} template: {heading['text']} (line {heading['line']})"
            )

    section_bodies = collect_section_bodies(lines, headings)
    one_more_thing = section_bodies.get("One More Thing", "")
    if one_more_thing:
        lowered = one_more_thing.lower()
        if "stop" not in lowered or "ask" not in lowered:
            errors.append("The 'One More Thing' section must tell the reader to stop and ask")

    if tier == "complex":
        how_heading = next(
            (heading for heading in h2_headings if normalize_heading(str(heading["text"])) == "how"),
            None,
        )
        next_h2_line = len(lines) + 1
        if how_heading is not None:
            for heading in h2_headings:
                if int(heading["line"]) > int(how_heading["line"]):
                    next_h2_line = int(heading["line"])
                    break
            phase_headings = [
                heading
                for heading in headings
                if heading["level"] == 3
                and int(how_heading["line"]) < int(heading["line"]) < next_h2_line
                and str(heading["text"]).lower().startswith("phase ")
            ]
            if not phase_headings:
                warnings.append("COMPLEX tier usually expects phase subheadings inside the How section")

    if len(lines) > 500:
        warnings.append(f"File is {len(lines)} lines long; consider moving overflow into references/")

    return tier, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a SKILL.md against template tiers")
    parser.add_argument("skill_file", type=Path, help="Path to the SKILL.md file to validate")
    parser.add_argument(
        "--tier",
        choices=["simple", "complicated", "complex", "auto"],
        default="auto",
        help="Template tier to validate against. Use auto to infer from headings.",
    )
    args = parser.parse_args()

    skill_path = args.skill_file.resolve()
    if not skill_path.is_file():
        print(f"FAIL: {skill_path} does not exist or is not a file", file=sys.stderr)
        return 1

    try:
        tier, errors, warnings = validate_skill(skill_path, args.tier)
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"FAIL: Could not read {skill_path}: {exc}", file=sys.stderr)
        return 1

    if errors:
        print(f"FAIL: {skill_path} does not match the {tier} template")
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        if warnings:
            print("Warnings:")
            for warning in warnings:
                print(f"- {warning}")
        return 1

    print(f"PASS: {skill_path} matches the {tier} template")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())