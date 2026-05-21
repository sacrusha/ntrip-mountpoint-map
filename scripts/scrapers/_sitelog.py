"""IGS sitelog parsing shared across SAPOS / EPN / M3G scrapers.

IGS-format sitelogs are plain-text records produced by GNSS network
operators (template: https://files.igs.org/pub/station/general/sitelog_instr.txt).
Section 1 carries the site identification; Section 2 carries the
approximate position in DMS-packed form `+DDMMSS.ss` (lat) and
`+DDDMMSS.ss` (lon). SAPOS-BB sitelog monitor, SAPOS-NRW refmap
detail pages, and the EPN M3G sitelog API all expose this same shape.

Per-source scrapers (`sapos_bb`, `sapos_nw`, `flepos`) parse the same
five regex patterns and the same DMS-string-to-decimal conversion.
This module owns those primitives so the per-source modules can shrink
to source-specific orchestration (which sitelogs to fetch, what field
to read for the station name, how to tag country).
"""
from __future__ import annotations

import re

# Section 1 — Site Identification
SITE_NAME_RE = re.compile(r"^\s*Site Name\s*:\s*(\S.*?)\s*$", re.MULTILINE)
FOURCHAR_RE  = re.compile(r"Four[- ]?Character ID\s*:\s*([0-9A-Z]{4})", re.IGNORECASE)
NINECHAR_RE  = re.compile(r"Nine Character ID\s*:\s*(\S{9})")

# Section 2 — Approximate Position (ITRF). DMS-packed strings.
LAT_RE = re.compile(r"Latitude\s*\(N is \+\)\s*:\s*([+-]\d+\.\d+)")
LON_RE = re.compile(r"Longitude\s*\(E is \+\)\s*:\s*([+-]\d+\.\d+)")

# Section 2 — Country (free-text, occasionally country code).
COUNTRY_RE = re.compile(r"Country or Region\s*:\s*([A-Za-z][A-Za-z ]+)")


def dms_to_decimal(s: str, deg_digits: int) -> float:
    """Convert IGS packed DMS `[+-]DDMMSS.ss` / `[+-]DDDMMSS.ss` to signed decimal.

    `deg_digits` is 2 for latitude (DDMMSS.ss) and 3 for longitude
    (DDDMMSS.ss). Leading sign carries hemisphere (+N, +E).
    """
    sign = -1 if s.startswith("-") else 1
    body = s.lstrip("+-")
    dd = int(body[:deg_digits])
    mm = int(body[deg_digits:deg_digits + 2])
    ss = float(body[deg_digits + 2:])
    return sign * round(dd + mm / 60.0 + ss / 3600.0, 6)
