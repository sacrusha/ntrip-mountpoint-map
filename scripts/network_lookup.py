#!/usr/bin/env python3
"""Find everywhere a network / source is referenced across the repo.

Today's session logs show agents running multi-alternation grep like
    `frednet|FReDNet|Marussi|Re\\.M\\.FVG|rem_fvg`
across the repo (with manual exclusions for data/*.sourcetable) when renaming
or auditing a network. This tool consolidates that into one call: it picks the
right scopes automatically, skips the noisy bulk-data files, and pulls the
matching section of docs/rtk_inventory.md (instead of paging by line offset).

Searched locations:
    docs/rtk_inventory.md                      (prints the matching ## section)
    docs/global-survey.md
    docs/ntrip_research/*.md
    data/rtk_map.json             (by substring)
    data/stations.json                    (source record + station name match)
    scripts/fetch_stations.py             (SOURCES entry)

Skipped: data/*.sourcetable (raw caster archives, too noisy to be useful).

Usage:
    py scripts/network_lookup.py <term> [<alias> ...]
    py scripts/network_lookup.py --section-only <id>     # only the rtk_inventory.md section

Examples:
    py scripts/network_lookup.py rem_fvg frednet FReDNet Marussi
    py scripts/network_lookup.py natt.is
    py scripts/network_lookup.py --section-only rtk2go
"""
import json, os, re, subprocess, sys
from pathlib import Path

# repo files contain non-cp1252 characters (en-dash, arrows). Re-launch in utf8
# mode if we're not there yet, so prints don't crash on Windows.
if not sys.flags.utf8_mode:
    r = subprocess.run([sys.executable, "-X", "utf8", *sys.argv])
    sys.exit(r.returncode)

ROOT = Path(__file__).resolve().parent.parent


def grep_file(path: Path, patterns):
    if not path.exists():
        return []
    rx = re.compile("|".join(patterns), re.IGNORECASE)
    out = []
    try:
        for i, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if rx.search(line):
                out.append((i, line.rstrip()))
    except Exception as e:
        print(f"  (could not read {path}: {e})", file=sys.stderr)
    return out


def networks_md_section(network_id: str):
    """Return (line_no, lines) for the ## <id> section in docs/rtk_inventory.md, or None."""
    p = ROOT / "docs" / "rtk_inventory.md"
    if not p.exists():
        return None
    lines = p.read_text(encoding="utf-8").splitlines()
    head_re = re.compile(rf"^##\s+{re.escape(network_id)}\b", re.IGNORECASE)
    start = None
    for i, line in enumerate(lines):
        if head_re.match(line):
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    return start + 1, lines[start:end]


def main():
    if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) < 2:
        print(__doc__)
        return 0 if "-h" in sys.argv or "--help" in sys.argv else 1

    section_only = False
    argv = sys.argv[1:]
    if argv[0] == "--section-only":
        section_only = True
        argv = argv[1:]
    if not argv:
        print("error: --section-only needs a network id", file=sys.stderr)
        return 1

    terms = argv
    patterns = [re.escape(t) for t in terms]

    if section_only:
        res = networks_md_section(terms[0])
        if res is None:
            print(f"no ## {terms[0]} section in docs/rtk_inventory.md")
            return 1
        start, lines = res
        print(f"--- docs/rtk_inventory.md (section starts at line {start}) ---")
        for ln in lines:
            print(ln)
        return 0

    print(f"searching for: {' | '.join(terms)}\n")

    # docs/rtk_inventory.md - section + scattered mentions
    print("=== docs/rtk_inventory.md ===")
    res = networks_md_section(terms[0])
    if res:
        start, lines = res
        print(f"(matching section at line {start})")
        for ln in lines:
            print(f"  {ln}")
    else:
        hits = grep_file(ROOT / "docs" / "rtk_inventory.md", patterns)
        if hits:
            print(f"(no ## section; {len(hits)} line match(es))")
            for ln, txt in hits[:50]:
                print(f"  {ln}: {txt}")
        else:
            print("  (no matches)")

    # other docs
    for sub in ("global-survey.md",):
        p = ROOT / "docs" / sub
        hits = grep_file(p, patterns)
        if hits:
            print(f"\n=== docs/{sub} ===")
            for ln, txt in hits[:30]:
                print(f"  {ln}: {txt}")

    # ntrip_research/
    research_hits = []
    for md in sorted((ROOT / "docs" / "ntrip_research").glob("*.md")):
        h = grep_file(md, patterns)
        if h:
            research_hits.append((md, h))
    if research_hits:
        print("\n=== docs/ntrip_research/ ===")
        for md, hits in research_hits:
            print(f"  {md.relative_to(ROOT)} - {len(hits)} match(es)")
            for ln, txt in hits[:3]:
                print(f"    {ln}: {txt}")

    # data/rtk_map.json
    rx = re.compile("|".join(patterns), re.IGNORECASE)
    cm = ROOT / "data" / "rtk_map.json"
    if cm.exists():
        text = cm.read_text(encoding="utf-8")
        if rx.search(text):
            print("\n=== data/rtk_map.json ===")
            for i, line in enumerate(text.splitlines(), 1):
                if rx.search(line):
                    print(f"  {i}: {line.strip()}")

    # data/stations.json - source record + station names
    sj = ROOT / "data" / "stations.json"
    if sj.exists():
        data = json.loads(sj.read_text(encoding="utf-8"))
        src_hits = [sid for sid in data["sources"] if rx.search(sid)]
        station_hits = []
        for sid, s in data["sources"].items():
            for st in s.get("stations", []):
                if rx.search(st.get("name", "")):
                    station_hits.append((sid, st["name"]))
        if src_hits or station_hits:
            print("\n=== data/stations.json ===")
            for sid in src_hits:
                n = len(data["sources"][sid].get("stations", []))
                print(f"  source: {sid}  ({n} stations)")
            if station_hits:
                print(f"  station-name matches: {len(station_hits)}")
                for sid, name in station_hits[:10]:
                    print(f"    {sid}: {name}")
                if len(station_hits) > 10:
                    print(f"    ... and {len(station_hits)-10} more")

    # scripts/fetch_stations.py
    fs = ROOT / "scripts" / "fetch_stations.py"
    hits = grep_file(fs, patterns)
    if hits:
        print("\n=== scripts/fetch_stations.py ===")
        for ln, txt in hits[:30]:
            print(f"  {ln}: {txt.strip()}")

    print("\n(skipped: data/*.sourcetable - raw caster archives, too noisy)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
