#!/usr/bin/env python3
"""List stations for a country code across ALL ingested sources.

Usage:  py scripts/stations_by_country.py <country_code>
        py scripts/stations_by_country.py          # list all codes per source

Examples:
        py scripts/stations_by_country.py FRA
        py scripts/stations_by_country.py JAM

Country tagging follows each source's own convention (no normalization here).
  rtk2go / centipede / earthscope use ISO 3166-1 alpha-3 (FRA, USA, DEU ...).
  Centipede quirks: CHZ=CZ  ENG=GB  SER=RS  BIH=BA  DAN=DK  ROM=RO  NLD/BEL separate.
    Auto-aliased: querying CZE/GBR/SRB/DNK/ROU also pulls centipede CHZ/ENG/SER/DAN/ROM.
  EarthScope uses USA for US stations; other territories vary.
  EUREF-IP / IGS-IP also alpha-3.
  National casters often leave per-station country empty; this script falls back to the
    source-record country (alpha-2). Query alpha-3 (e.g. COL, URY, UGA) works for these.

Sources walked: every key in data/stations.json[sources] (84 as of 2026-05).

Related tools (in this directory):
    stations_by_radius.py    list stations within a radius of a lat/lon
    stations_inspect.py      schema + per-source summary of stations.json
    sources_list.py          look up source ids defined in fetch_stations.py
    source_health.py         check status of one or all sources
    network_lookup.py        find every mention of a network/source across the repo
"""
import json, sys
from pathlib import Path

STATIONS = Path(__file__).parent.parent / "data" / "stations.json"

# Centipede tags Czech/UK/Serbia/Denmark/Romania stations under non-ISO codes.
# Map ISO alpha-3 -> centipede's internal code so cross-source queries hit them.
_CENTIPEDE_ALIASES = {
    "CZE": "CHZ", "GBR": "ENG", "SRB": "SER",
    "DNK": "DAN", "ROU": "ROM",
}

# Source-record country values are alpha-2; queries are alpha-3.
# Cover countries whose national caster ships station-records with empty country.
_A2_TO_A3 = {
    "CO": "COL", "UY": "URY", "UG": "UGA", "IT": "ITA", "US": "USA",
    # Generic extras (cheap to maintain; covers other national casters):
    "AU": "AUS", "NZ": "NZL", "DE": "DEU", "FR": "FRA", "ES": "ESP",
    "BE": "BEL", "NL": "NLD", "AT": "AUT", "CH": "CHE", "PT": "PRT",
    "PL": "POL", "RO": "ROU", "HR": "HRV", "SI": "SVN", "SK": "SVK",
    "EE": "EST", "LV": "LVA", "LT": "LTU", "LU": "LUX", "SE": "SWE",
    "NO": "NOR", "FI": "FIN", "DK": "DNK", "IE": "IRL", "GB": "GBR",
    "TR": "TUR", "GR": "GRC", "BG": "BGR", "JP": "JPN", "KR": "KOR",
    "CN": "CHN", "HK": "HKG", "MO": "MAC", "TH": "THA", "ID": "IDN",
    "MY": "MYS", "SG": "SGP", "PH": "PHL", "VN": "VNM", "IN": "IND",
    "SA": "SAU", "AE": "ARE", "QA": "QAT", "BH": "BHR", "KW": "KWT",
    "IL": "ISR", "ZA": "ZAF", "BR": "BRA", "AR": "ARG", "CL": "CHL",
    "PE": "PER", "EC": "ECU", "CA": "CAN", "MX": "MEX",
}

data = json.loads(STATIONS.read_text())["sources"]
SOURCES = sorted(data.keys())

if len(sys.argv) < 2:
    untagged = []
    for src in SOURCES:
        stations = data[src]["stations"]
        if not stations:
            continue  # source ingested 0 stations -- skip
        codes = sorted({s["country"] for s in stations if s.get("country")})
        if codes:
            print(f"{src}: {', '.join(codes)}")
        else:
            untagged.append(src)
    if untagged:
        print(f"# no per-station country tag (source-record fallback used): {', '.join(untagged)}")
    sys.exit(0)

tag = sys.argv[1].upper()
alias = _CENTIPEDE_ALIASES.get(tag)
total = 0
matched_sources = 0

for src in SOURCES:
    accepted = {tag}
    if src == "centipede" and alias:
        accepted.add(alias)

    hits = sorted(
        (s for s in data[src]["stations"] if (s.get("country") or "").upper() in accepted),
        key=lambda s: s["name"],
    )
    notes = []
    if src == "centipede" and alias and hits:
        n_via_alias = sum(1 for s in hits if (s.get("country") or "").upper() == alias)
        if n_via_alias:
            notes.append(f"alias: {tag}->{alias} ({n_via_alias})")
    if not hits:
        # Source-record country fallback: per-station tag is empty but source covers this country.
        src_cc = data[src].get("country") or []
        if isinstance(src_cc, str):
            src_cc = [src_cc]
        src_a3 = {_A2_TO_A3.get(c.upper(), c.upper()) for c in src_cc}
        if tag in src_a3:
            tagless = [s for s in data[src]["stations"] if not s.get("country")]
            if tagless:
                hits = sorted(tagless, key=lambda s: s["name"])
                notes.append("country from source record, no per-station tag")
    if hits:
        status = data[src].get("status", "?")
        if status != "ok":
            notes.append(f"status: {status}")
        note_str = "".join(f"  [{n}]" for n in notes)
        print(f"\n{src} -- {len(hits)} station(s):{note_str}")
        for s in hits:
            print(f"  {s['name']:<21} {s['lat']:>9.4f}  {s['lon']:>10.4f}")
        total += len(hits)
        matched_sources += 1

if total:
    print(f"\n# total: {total} station(s) across {matched_sources} source(s)")
else:
    print(f"No stations for '{tag}'. Run without arguments to list available codes.")
