"""Generic M3G scraper — one impl for every M3G-backed network.

Endpoint config in `data/rtk_map.json` carries the per-network spec:

```json
{
  "type": "scraped",
  "id":   "estpos_ext",
  "scraper": "m3g",
  "moid":    "6343d5c7870122027e7ee502",
  "country": "EST",
  "affiliation_from": "estpos",         // optional; see below
  "mountpoint_pattern": "^([A-Z0-9]{4})",// optional regex; default shown
  "interval_days": 7,
  "pin_origin": "register"
}
```

Resolution order for the membership universe:
1. `moid` — M3G project page (operator-curated). Universe includes
   retired IDs; the retirement filter (per-station sitelog Date Removed)
   drops them.
2. `ids` — fallback for networks that aren't registered as M3G
   projects. 4-char codes; the 9-char lookup key is
   `f"{sid}00{country}"`. No automatic add-discovery — edits manual.

Optional **sourcetable affiliation**: when `affiliation_from` is set,
the scraper additionally reads the sibling NTRIP endpoint's cached
sourcetable (`data/<affiliation_from>.sourcetable`), extracts physical
mountpoint names via `mountpoint_pattern` (capture group 1 = 4-char
station ID), and intersects against the M3G universe. This catches
**operator-side retirements that M3G hasn't reflected yet** — a station
that stops broadcasting RTCM drops from the sourcetable immediately,
while M3G project pages can lag the retirement by months. Soft fall-back:
when the sourcetable file is missing or no mountpoints match the
pattern (e.g. VRS-only response), the full M3G universe is used.

Coords come from `_m3g.fetch_features()`. Retirement comes from
`_m3g.fetch_station_attrs()` (per-station sitelog Date Removed,
incrementally cached via the metadata-list update cursor).
"""
from __future__ import annotations

import re
from pathlib import Path

from . import _m3g

_DEFAULT_MOUNTPOINT_PATTERN = r"^([A-Z0-9]{4})"
DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _read_sourcetable_mountpoints(sid: str, pattern: re.Pattern) -> set[str]:
    """Extract 4-char station IDs from a cached sourcetable.

    Returns the set of (regex group-1) captures from every STR row whose
    mountpoint name matches `pattern`. Empty set when the cache file is
    missing or no mountpoints match — caller decides fallback policy.
    """
    path = DATA_DIR / f"{sid}.sourcetable"
    if not path.exists():
        return set()
    out: set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("STR;"):
            continue
        cols = line.split(";", 3)
        if len(cols) < 2:
            continue
        m = pattern.match(cols[1])
        if m:
            out.add(m.group(1))
    return out


def scrape(src: dict) -> dict:
    country = src.get("country")
    if not country or len(country) != 3:
        raise ValueError(f"m3g scraper requires 3-char 'country', got {country!r}")

    moid = src.get("moid")
    explicit_ids = src.get("ids")
    if moid:
        all_ids = _m3g.fetch_project_ids(moid)
        # Project pages occasionally reference foreign IDs (cross-network
        # collaborators, EUREF densification etc); drop anything not in
        # this network's country.
        universe = [sid for sid in all_ids if sid.endswith(country)]
    elif explicit_ids:
        universe = [f"{sid}00{country}" for sid in explicit_ids]
    else:
        raise ValueError("m3g scraper requires 'moid' or 'ids'")

    log_tag = f"m3g/{src.get('id')}"

    # Optional sourcetable affiliation: liveness filter against the sibling
    # NTRIP endpoint's cached sourcetable. Stations not currently broadcasting
    # drop immediately; M3G project-page lag stops mattering.
    affiliation_from = src.get("affiliation_from")
    if affiliation_from:
        pat = re.compile(src.get("mountpoint_pattern", _DEFAULT_MOUNTPOINT_PATTERN))
        live_4char = _read_sourcetable_mountpoints(affiliation_from, pat)
        if live_4char:
            live_9char = {f"{m}00{country}" for m in live_4char}
            before = len(universe)
            universe = [sid for sid in universe if sid in live_9char]
            print(f"[{log_tag}] sourcetable affiliation via {affiliation_from}: "
                  f"{before} -> {len(universe)} ({len(live_4char)} live mountpoints)",
                  flush=True)
        else:
            print(f"[{log_tag}] affiliation_from={affiliation_from!r}: "
                  f"sourcetable missing or no mountpoints match pattern; "
                  f"using full M3G universe", flush=True)

    attrs = _m3g.fetch_station_attrs(universe)
    feats = _m3g.fetch_features()
    stations: list[dict] = []
    retired: list[str] = []
    no_coords: list[str] = []
    no_attrs: list[str] = []
    for sid in universe:
        a = attrs.get(sid)
        if a is None:
            no_attrs.append(sid)
            # Conservative default: include the pin (avoid hiding it on
            # transient sitelog fetch failure). Retirement check will
            # take effect once attrs populate on a later run.
        elif a.get("retired"):
            retired.append(sid)
            continue
        coords = feats.get(sid)
        if coords is None:
            no_coords.append(sid)
            continue
        lat, lon = coords
        stations.append({"name": sid[:4], "lat": lat, "lon": lon, "country": country})

    if retired:
        print(f"[{log_tag}] filtered {len(retired)} retired: {sorted(retired)}", flush=True)
    if no_coords:
        print(f"[{log_tag}] no master coords for: {sorted(no_coords)}", flush=True)
    if no_attrs:
        print(f"[{log_tag}] no sitelog attrs (not yet cached) for: {sorted(no_attrs)}", flush=True)
    if not stations:
        raise ValueError(
            f"m3g resolved 0 stations for {src.get('id')} "
            f"(universe={len(universe)}, retired={len(retired)}, "
            f"no_coords={len(no_coords)})"
        )

    stations.sort(key=lambda s: s["name"])
    return {
        "source_url": (URL_PROJECT_FMT.format(moid=moid) if moid
                       else "https://gnss-metadata.eu/site/index"),
        "stations": stations,
    }


URL_PROJECT_FMT = _m3g.URL_PROJECT
