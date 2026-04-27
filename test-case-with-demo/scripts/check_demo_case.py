#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "ManualInstruction.md",
    "SETUP.sh",
    "RUN.sh",
    "CLEANUP.sh",
    "demo_manifest.json",
]

MANUAL_SECTIONS = [
    "## Purpose",
    "## Prerequisites",
    "## Setup",
    "## Run",
    "## Expected Result",
    "## Troubleshooting",
    "## Cleanup",
    "## Evidence",
]

MANIFEST_KEYS = [
    "demoName",
    "status",
    "purpose",
    "sourceDocuments",
    "userGuideRefs",
    "acceptanceCriteria",
    "userStoryRefs",
    "scripts",
    "manualInstruction",
]


def has_heading(markdown: str, heading: str) -> bool:
    expected = heading.strip().lower()
    return any(line.strip().lower() == expected for line in markdown.splitlines())


def check_shell_script(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("#!/usr/bin/env bash"):
        issues.append(f"{path.name} should start with #!/usr/bin/env bash")
    if "set -euo pipefail" not in text:
        issues.append(f"{path.name} should use set -euo pipefail")
    return issues


def check_manifest(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"demo_manifest.json is not valid JSON: {exc}"]

    for key in MANIFEST_KEYS:
        if key not in data:
            issues.append(f"demo_manifest.json missing key: {key}")

    scripts = data.get("scripts")
    if isinstance(scripts, dict):
        for key in ("setup", "run", "cleanup"):
            if key not in scripts:
                issues.append(f"demo_manifest.json scripts missing key: {key}")
    else:
        issues.append("demo_manifest.json scripts must be an object")

    user_story_refs = data.get("userStoryRefs")
    if not isinstance(user_story_refs, list) or not user_story_refs:
        issues.append("demo_manifest.json userStoryRefs must be a non-empty array")
    else:
        for index, ref in enumerate(user_story_refs):
            if not isinstance(ref, dict):
                issues.append(f"demo_manifest.json userStoryRefs[{index}] must be an object")
                continue
            for key in ("file", "storyId", "acceptanceCriteria", "requirement"):
                if key not in ref:
                    issues.append(f"demo_manifest.json userStoryRefs[{index}] missing key: {key}")

    return issues


def check_demo_case(demo_dir: Path) -> list[str]:
    issues: list[str] = []

    if not demo_dir.is_dir():
        return [f"Demo directory does not exist: {demo_dir}"]

    for relative_path in REQUIRED_FILES:
        if not (demo_dir / relative_path).is_file():
            issues.append(f"Missing required file: {relative_path}")

    manual_path = demo_dir / "ManualInstruction.md"
    if manual_path.is_file():
        manual_text = manual_path.read_text(encoding="utf-8")
        for heading in MANUAL_SECTIONS:
            if not has_heading(manual_text, heading):
                issues.append(f"ManualInstruction.md missing heading: {heading}")

    for script_name in ("SETUP.sh", "RUN.sh", "CLEANUP.sh"):
        script_path = demo_dir / script_name
        if script_path.is_file():
            issues.extend(check_shell_script(script_path))

    manifest_path = demo_dir / "demo_manifest.json"
    if manifest_path.is_file():
        issues.extend(check_manifest(manifest_path))

    return issues


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: check_demo_case.py <demo-dir>", file=sys.stderr)
        return 2

    demo_dir = Path(argv[1]).resolve()
    issues = check_demo_case(demo_dir)
    if issues:
        print("Demo case validation failed:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print(f"Demo case validation passed: {demo_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
