#!/usr/bin/env python3
"""Deterministic field-compliance linter for `docs/ntrip_research/*.md`.

Replaces the mechanical part of the ntrip-research agent's Step 8 self-review
(see `.claude/agents/ntrip-research.md`, v0.1). LLM-driven review keeps
missing the field-presence and negative-evidence-trail rules; this script
makes them machine-checkable.

Checks (each cross-referenced to the spec section it derives from):

  [Fields per file] - per-file header block must declare:
    - last_verified_date           (ISO YYYY-MM-DD)
    - last_gap_fill_date           (ISO YYYY-MM-DD)
    - last_caster_search_date      (ISO YYYY-MM-DD)
    - agent_version: 0.1

  [Default fields] - every per-caster block (a markdown table with header
  `| Field | Value |` that contains an `operator` row) must carry these:
    operator, landing_url, access_url, access_type, coverage,
    num_stations, hobbyist_eligibility
  Spec-permitted absences (NOT flagged):
    - tariff       (spec: "omit if free")
    - datum_epoch  (spec: "Omit if not found")

  [Default fields - access_type enum]
    access_type value must be one of: free, free-signup, paid, restricted
    (case-insensitive; ignores trailing parenthetical commentary).

  [Required on free, opportunistic pick up otherwise]
    When access_type == free OR free-signup, the block must also declare:
    sourcetable, vrs, residency_required, stations_source

  [Negative-evidence trail]
    Per spec: "Any field marked ? or 'not published / not found' require
    a one-line negative-evidence trail next to it, format
    (checked: <channel> <date>; <channel> <date>; ...)".
    Triggered when the field value contains a bare `?`, or the phrases
    "not published" or "not found". The trail satisfies the requirement
    if EITHER (a) a `(checked: ... YYYY-MM-DD ...)` block is present in
    the same value cell, OR (b) the trigger is `?` and is immediately
    followed by an em-dash / hyphen / paren clause carrying a non-empty
    inline explanation - matching the spec's own worked example
    `"? - 2-day survey license course mandatory, EUR 500"`. The strict
    `(checked: ...)` form is required for "not published" / "not found"
    triggers since those phrases by themselves carry no explanation.

Disqualified / placeholder blocks (per spec: "Disqualified casters:
Include only enough to understand why they are disqualified") are
detected and skipped: a table without an `operator` field is treated as
narrative scaffolding, not a caster declaration.

Usage:
    py scripts/check_ntrip_research.py docs/ntrip_research/AR_Argentina.md
    py scripts/check_ntrip_research.py docs/ntrip_research/*.md
    py scripts/check_ntrip_research.py -h

Exit code: 0 if every file is OK, 1 if any file has >=1 violation, 2 on
argument / IO error.

Output: human-readable per-violation lines, plus a single trailing summary
line per file in the form `<path>: OK` or `<path>: N violations` so callers
can grep results.
"""
from __future__ import annotations

import glob
import re
import sys
from pathlib import Path
from typing import Iterable

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# File-level header fields. Surfaced as plain `key: value` lines anywhere
# in the first ~30 lines of the file (top header block).
FILE_HEADER_FIELDS = (
    "last_verified_date",
    "last_gap_fill_date",
    "last_caster_search_date",
    "agent_version",
)

# Per-caster default fields the spec requires regardless of access_type.
# `tariff` and `datum_epoch` are spec-permitted to be omitted in the
# stated cases ("omit if free", "Omit if not found"); we never flag them
# absent.
DEFAULT_FIELDS_REQUIRED = (
    "operator",
    "landing_url",
    "access_url",
    "access_type",
    "coverage",
    "num_stations",
    "hobbyist_eligibility",
)

# Required when caster is free / free-signup (free in the spec's sense
# of "anyone or local signup can use, no payment"). For paid /
# restricted, spec marks these as "opportunistic pick up otherwise" -
# we do NOT flag their absence.
REQUIRED_ON_FREE = (
    "sourcetable",
    "vrs",
    "residency_required",
    "stations_source",
)

ACCESS_TYPE_VALUES = {"free", "free-signup", "paid", "restricted"}
FREE_ACCESS_VALUES = {"free", "free-signup"}

# Triggers for the negative-evidence-trail requirement. Spec: "? or
# 'not published / not found'". `omitted`, `n/a`, `not applicable`,
# `none confirmed`, plain `no`/`yes` do NOT trigger; those are
# definite states, not unknowns.
NEG_TRAIL_PHRASES = ("not published", "not found")
NEG_TRAIL_PATTERN = re.compile(
    r"\(checked:[^)]*\d{4}-\d{2}-\d{2}[^)]*\)", re.IGNORECASE
)

TABLE_HEADER_RE = re.compile(
    r"^\s*\|\s*Field\s*\|\s*Value\s*\|\s*$", re.IGNORECASE
)
TABLE_SEP_RE = re.compile(r"^\s*\|[\s\-:|]+\|\s*$")
TABLE_ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$")


class Violation:
    __slots__ = ("line", "field", "block", "message")

    def __init__(self, line: int, field: str, block: str, message: str) -> None:
        self.line = line
        self.field = field
        self.block = block
        self.message = message

    def render(self, path: str) -> str:
        prefix = f"{path}:{self.line}"
        block = f" [{self.block}]" if self.block else ""
        field = f" {self.field}:" if self.field else ""
        return f"{prefix}{block}{field} {self.message}"


def value_has_checked_trail(value: str) -> bool:
    return bool(NEG_TRAIL_PATTERN.search(value))


def value_has_question_mark_trigger(value: str) -> bool:
    """`?` as the field value, possibly followed by an inline explainer
    after em-dash / hyphen / paren."""
    head = re.split(r"[—–\-(]", value.strip(), maxsplit=1)[0].strip()
    return head == "?"


def value_has_not_published_trigger(value: str) -> bool:
    """Phrases 'not published' or 'not found' anywhere in the value."""
    low = value.lower()
    return any(p in low for p in NEG_TRAIL_PHRASES)


def value_has_inline_explanation_after_qmark(value: str) -> bool:
    """Spec example: `"? - 2-day survey license course mandatory, EUR 500"`.
    Returns True iff value starts with `?` and is followed by an
    em-dash/hyphen/paren and at least a few chars of non-empty prose."""
    m = re.match(r"^\s*\?\s*[—–\-(]\s*(.{4,})", value)
    return bool(m)


def access_type_token(value: str) -> str:
    """Normalise access_type cell to its leading token. Accepts forms like
    'paid (prepaid, brand-agnostic, self-service)' -> 'paid'."""
    head = re.split(r"[\s(—–;,]", value.strip(), maxsplit=1)[0]
    return head.strip().lower()


def find_tables(lines: list[str]) -> list[tuple[int, int, str]]:
    """Return list of (header_line, end_line, preceding_heading) for each
    `| Field | Value |` table. `header_line` is 1-indexed line number of
    the header row. `end_line` exclusive."""
    out: list[tuple[int, int, str]] = []
    i = 0
    last_heading = ""
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            last_heading = line.lstrip("#").strip()
        if TABLE_HEADER_RE.match(line):
            # Require a separator row after header.
            if i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]):
                start = i  # 0-indexed header row
                j = i + 2
                while j < len(lines) and TABLE_ROW_RE.match(lines[j]):
                    j += 1
                out.append((start + 1, j, last_heading))
                i = j
                continue
        i += 1
    return out


def parse_table_rows(
    lines: list[str], header_line_1idx: int, end_line: int
) -> list[tuple[int, str, str]]:
    """Return [(line_1idx, field, value)] for a table. Field stripped
    lowercase; value stripped, preserving inner content."""
    rows: list[tuple[int, str, str]] = []
    # `header_line_1idx` is 1-indexed; 0-indexed header position is
    # header_line_1idx - 1, separator at header_line_1idx, first data
    # row at header_line_1idx + 1. Walk to end_line (exclusive, 0-idx).
    for idx in range(header_line_1idx + 1, end_line):
        m = TABLE_ROW_RE.match(lines[idx])
        if not m:
            continue
        inner = m.group(1)
        parts = [p.strip() for p in inner.split("|")]
        if len(parts) < 2:
            continue
        field = parts[0].strip().lower()
        value = "|".join(parts[1:]).strip()
        # Drop trailing empty cells gathered from `| field | value |\n`
        # (split gives ['field', 'value', ''] -> we join parts[1:] = 'value|'; trim trailing pipe).
        value = re.sub(r"\|\s*$", "", value).strip()
        rows.append((idx + 1, field, value))
    return rows


def check_file_header(
    lines: list[str], violations: list[Violation]
) -> None:
    """Spec [Fields per file]. Header fields appear as `key: value` near
    the top of the file. We scan the first 40 lines to be tolerant of
    title + blank lines + a Status paragraph."""
    found: dict[str, tuple[int, str]] = {}
    for idx, line in enumerate(lines[:40], start=1):
        m = re.match(r"^([a-z_]+):\s*(.+?)\s*$", line)
        if m:
            key = m.group(1)
            if key in FILE_HEADER_FIELDS and key not in found:
                found[key] = (idx, m.group(2))

    for field in FILE_HEADER_FIELDS:
        if field not in found:
            violations.append(
                Violation(
                    line=1,
                    field=field,
                    block="<file header>",
                    message=f"missing required file-header field `{field}` "
                    f"(spec: 'Fields per file')",
                )
            )
            continue
        line_no, value = found[field]
        if field == "agent_version":
            if value.strip() != "0.1":
                violations.append(
                    Violation(
                        line=line_no,
                        field=field,
                        block="<file header>",
                        message=f"value `{value}` must be `0.1` "
                        f"(spec: 'agent_version: 0.1')",
                    )
                )
        else:
            if not ISO_DATE.match(value.strip()):
                violations.append(
                    Violation(
                        line=line_no,
                        field=field,
                        block="<file header>",
                        message=f"value `{value}` is not ISO YYYY-MM-DD",
                    )
                )


def is_caster_table(field_map: dict[str, tuple[int, str]]) -> bool:
    """Heuristic: a table is a caster declaration iff it has an
    `operator` field. Disqualified / placeholder / "no caster" blocks
    use ad-hoc field names ('Active public ...', 'host:port', 'Provider')
    and lack `operator` - per spec they need 'only enough to understand
    why they are disqualified', so we skip strict field-presence checks
    on them. (Negative-trail and access_type rules still don't apply
    because access_type also won't be present.)"""
    return "operator" in field_map


def check_caster_table(
    block_name: str,
    header_line: int,
    rows: list[tuple[int, str, str]],
    violations: list[Violation],
) -> None:
    """Apply spec [Default fields], [Required on free], and
    [negative-evidence trail] checks to one caster table."""
    field_map: dict[str, tuple[int, str]] = {}
    for line_no, field, value in rows:
        # First occurrence wins on dup; flag duplicates as a soft issue.
        if field not in field_map:
            field_map[field] = (line_no, value)

    if not is_caster_table(field_map):
        return  # disqualified / placeholder block - skip strict checks

    # Default required fields
    for required in DEFAULT_FIELDS_REQUIRED:
        if required not in field_map:
            violations.append(
                Violation(
                    line=header_line,
                    field=required,
                    block=block_name,
                    message=f"missing required default field `{required}` "
                    f"(spec: 'Default fields')",
                )
            )

    # access_type enum
    access_value: str | None = None
    if "access_type" in field_map:
        _line, val = field_map["access_type"]
        token = access_type_token(val)
        if token not in ACCESS_TYPE_VALUES:
            violations.append(
                Violation(
                    line=_line,
                    field="access_type",
                    block=block_name,
                    message=f"value `{val}` must start with one of "
                    f"{sorted(ACCESS_TYPE_VALUES)} "
                    f"(spec: 'free/free-signup/paid/restricted')",
                )
            )
        else:
            access_value = token

    # Required-on-free fields
    if access_value in FREE_ACCESS_VALUES:
        for required in REQUIRED_ON_FREE:
            if required not in field_map:
                violations.append(
                    Violation(
                        line=header_line,
                        field=required,
                        block=block_name,
                        message=f"missing required-on-free field "
                        f"`{required}` (access_type={access_value}; "
                        f"spec: 'Required on free, opportunistic pick "
                        f"up otherwise')",
                    )
                )

    # Negative-evidence-trail (spec: "Fields per Caster" header rule)
    for line_no, field, value in rows:
        has_qmark = value_has_question_mark_trigger(value)
        has_phrase = value_has_not_published_trigger(value)
        if not (has_qmark or has_phrase):
            continue
        has_checked = value_has_checked_trail(value)
        if has_checked:
            continue
        # `?` accepts an inline explanation after em-dash/hyphen/paren as
        # an alternative trail (per spec's own example
        # "? - 2-day survey license course mandatory").
        if has_qmark and not has_phrase:
            if value_has_inline_explanation_after_qmark(value):
                continue
            violations.append(
                Violation(
                    line=line_no,
                    field=field,
                    block=block_name,
                    message="value is bare `?` with no inline "
                    "explanation and no `(checked: <channel> <date>; ...)` "
                    "trail (spec: 'Fields per Caster' header rule)",
                )
            )
        else:
            violations.append(
                Violation(
                    line=line_no,
                    field=field,
                    block=block_name,
                    message="value contains 'not published'/'not found' "
                    "but no `(checked: <channel> <date>; ...)` trail "
                    "with an ISO date (spec: 'Fields per Caster' "
                    "header rule)",
                )
            )


def lint_file(path: Path) -> tuple[int, list[Violation]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    violations: list[Violation] = []

    check_file_header(lines, violations)

    tables = find_tables(lines)
    for header_line, end_line, heading in tables:
        rows = parse_table_rows(lines, header_line, end_line)
        block_name = heading or f"<table at line {header_line}>"
        check_caster_table(block_name, header_line, rows, violations)

    return len(violations), violations


def expand_args(args: Iterable[str]) -> list[Path]:
    out: list[Path] = []
    for a in args:
        # glob.glob() returns [] on non-globs that match nothing AND on
        # plain paths that don't exist; distinguish so we can report the
        # latter.
        if any(c in a for c in "*?[]"):
            matches = sorted(glob.glob(a, recursive=True))
            if not matches:
                print(f"warning: glob `{a}` matched no files", file=sys.stderr)
            out.extend(Path(m) for m in matches)
        else:
            out.append(Path(a))
    return out


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2

    paths = expand_args(argv)
    if not paths:
        print("error: no input files", file=sys.stderr)
        return 2

    overall_fail = False
    for p in paths:
        if not p.is_file():
            print(f"{p}: ERROR file not found", file=sys.stderr)
            overall_fail = True
            continue
        try:
            count, violations = lint_file(p)
        except OSError as exc:
            print(f"{p}: ERROR {exc}", file=sys.stderr)
            overall_fail = True
            continue

        for v in violations:
            print(v.render(str(p)))
        if count == 0:
            print(f"{p}: OK")
        else:
            print(f"{p}: {count} violations")
            overall_fail = True

    return 1 if overall_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
