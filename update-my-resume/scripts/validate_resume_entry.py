#!/usr/bin/env python3
"""Deterministic validator for the update-my-resume .resume format.

Verifies the structural invariants the skill promises:
  - The [EN]/[English] and [ZH]/[中文] sections both exist, in that order.
  - Every entry starts with a valid YYYY-MM-DD date marker.
  - Every EN entry contains Problem/Approach/Outcome/Reuse in that order.
  - Every ZH entry contains 问题/过程/收获/复用性 in that order.
  - Field values are non-empty and may span multiple lines.
  - When --date is given, an entry with that date exists in both sections.

Numeric-parity mismatches between EN and ZH entries are printed as warnings
(they often indicate real translation drift) but do not fail the run, because
only the user can judge whether a translated fact was intentionally adapted.

Exit codes: 0 = all required checks passed; 1 = at least one check failed.

Usage:
  python3 scripts/validate_resume_entry.py --resume .resume [--date YYYY-MM-DD]
"""

import argparse
import datetime
import re
import sys
from itertools import chain
from pathlib import Path

EN_HEADERS = ("[EN]", "[English]")
ZH_HEADERS = ("[ZH]", "[中文]")

EN_FIELDS = ("Problem", "Approach", "Outcome", "Reuse")
ZH_FIELDS = ("问题", "过程", "收获", "复用性")

DATE_RE = re.compile(r"^---\s*\[(\d{4}-\d{2}-\d{2})\]\s*---\s*$")
DIGIT_RE = re.compile(r"\d+(?:\.\d+)?")


def parse_date(value):
    try:
        return datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def split_sections(lines):
    """Return the line index of the first EN and first ZH section header."""
    en_start = zh_start = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if en_start is None and stripped in EN_HEADERS:
            en_start = i
        elif zh_start is None and stripped in ZH_HEADERS:
            zh_start = i
    return en_start, zh_start


def parse_entries(lines, start, end, fields):
    """Parse entries between line indices [start, end).

    Returns (entries, errors). Each entry is
    (start_line_index, date_string, {field: value}).
    """
    entries = []
    errors = []
    current = None  # (start_line_index, date_string, field_values, active_field)

    def flush():
        nonlocal current
        if current is None:
            return
        start_line, date_val, values, _ = current
        empty = [f for f in fields if not values.get(f, "").strip()]
        if empty:
            errors.append(
                f"line {start_line + 1}: {date_val} entry is missing non-empty "
                f"value(s): {', '.join(empty)}"
            )
        entries.append((start_line, date_val, values))
        current = None

    for i in range(start, end):
        stripped = lines[i].strip()
        m = DATE_RE.match(stripped)
        if m:
            flush()
            date_val = m.group(1)
            if parse_date(date_val) is None:
                errors.append(
                    f"line {i + 1}: invalid date '{date_val}' (expected YYYY-MM-DD)"
                )
            current = (i, date_val, {}, None)
            continue

        if current is None:
            # Section preamble (e.g. "# My Resume", "## Experience & Growth Log")
            # before the first entry is valid; ignore it.
            continue

        label = next(
            (
                f
                for f in fields
                if stripped.startswith(f + ":") or stripped.startswith(f + "：")
            ),
            None,
        )
        _, _, values, active = current
        if label is not None:
            if label in values:
                errors.append(f"line {i + 1}: duplicate field '{label}'")
            values[label] = stripped[len(label) + 1 :].strip()
            current = (current[0], current[1], values, label)
            continue

        if active is None:
            if stripped:
                errors.append(
                    f"line {i + 1}: content appears before the first field of "
                    "the entry"
                )
            continue

        if stripped:
            # Continuation line of the current field (e.g. wrapped text).
            values[active] = (values[active] + " " + stripped).strip()

    flush()
    return entries, errors


def check_field_order(entries, fields, section_label, errors):
    for start_line, date_val, values in entries:
        actual = [f for f in values if f in fields]
        if actual != list(fields):
            errors.append(
                f"line {start_line + 1}: {section_label} entry {date_val} has "
                f"missing or out-of-order fields (expected {' -> '.join(fields)})"
            )


def digits_for(entries):
    return sorted(
        DIGIT_RE.findall(" ".join(v for values in (e[2] for e in entries) for v in values.values()))
    )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate the .resume format written by update-my-resume."
    )
    parser.add_argument(
        "--resume",
        default=".resume",
        help="path to the resume file (default: .resume)",
    )
    parser.add_argument(
        "--date",
        default=None,
        metavar="YYYY-MM-DD",
        help="require an entry with this date in both EN and ZH sections",
    )
    args = parser.parse_args(argv)

    path = Path(args.resume)
    if not path.exists():
        print(f"FAIL: resume file not found: {path}", file=sys.stderr)
        return 1

    lines = path.read_text(encoding="utf-8").splitlines()
    en_start, zh_start = split_sections(lines)
    errors = []

    if en_start is None:
        errors.append("missing [EN]/[English] section header")
    if zh_start is None:
        errors.append("missing [ZH]/[中文] section header")
    if en_start is not None and zh_start is not None and zh_start < en_start:
        errors.append("expected the [EN] section before the [ZH] section")
    if en_start is not None and any(line.strip() for line in lines[:en_start]):
        errors.append("content appears before the [EN] section header")

    if errors:
        for message in errors:
            print(f"FAIL: {message}", file=sys.stderr)
        return 1

    en_entries, en_errors = parse_entries(lines, en_start + 1, zh_start, EN_FIELDS)
    zh_entries, zh_errors = parse_entries(lines, zh_start + 1, len(lines), ZH_FIELDS)
    errors += en_errors + zh_errors

    check_field_order(en_entries, EN_FIELDS, "EN", errors)
    check_field_order(zh_entries, ZH_FIELDS, "ZH", errors)

    if args.date:
        if parse_date(args.date) is None:
            errors.append(f"invalid --date '{args.date}' (expected YYYY-MM-DD)")
        for section_label, entries in (("EN", en_entries), ("ZH", zh_entries)):
            if not any(entry[1] == args.date for entry in entries):
                errors.append(
                    f"no {section_label} entry with date {args.date} "
                    "(run update-my-resume to append one)"
                )

    warnings = []
    en_dates = {entry[1] for entry in en_entries}
    zh_dates = {entry[1] for entry in zh_entries}
    for date_val in sorted(en_dates & zh_dates):
        en_digits = digits_for([e for e in en_entries if e[1] == date_val])
        zh_digits = digits_for([e for e in zh_entries if e[1] == date_val])
        if en_digits != zh_digits:
            warnings.append(
                f"{date_val}: numeric tokens differ between EN ({en_digits}) "
                f"and ZH ({zh_digits}); check the translation for drift"
            )
    for date_val in sorted(en_dates - zh_dates):
        warnings.append(f"{date_val}: date present only in the EN section")
    for date_val in sorted(zh_dates - en_dates):
        warnings.append(f"{date_val}: date present only in the ZH section")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for message in errors:
        print(f"FAIL: {message}", file=sys.stderr)

    if errors:
        return 1

    print(
        f"PASS: validated {len(en_entries)} EN entr{'y' if len(en_entries) == 1 else 'ies'} "
        f"and {len(zh_entries)} ZH entr{'y' if len(zh_entries) == 1 else 'ies'} in {path}"
    )
    if not warnings:
        print("PASS: no EN/ZH parity warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
