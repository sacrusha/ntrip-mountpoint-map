"""Generic M3G scraper — one impl for every M3G-backed network.

Endpoint config in `data/rtk_map.json` carries the per-network spec:

```json
{
  "type": "scraped",
  "id":   "estpos_ext",
  "scraper": "m3g",
  "moid":    "6343d5c7870122027e7ee502",
  "country": "EST",
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

Coords come from `_m3g.fetch_features()` (single master fetch, shared
across all M3G-backed endpoints). Retirement comes from
`_m3g.fetch_station_attrs()` (per-station sitelog with `update_ts`
incremental cache — near-zero steady-state cost).
"""
from __future__ import annotations

from . import _m3g


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

    attrs = _m3g.fetch_station_attrs(universe)
    feats = _m3g.fetch_features()

    log_tag = f"m3g/{src.get('id')}"
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
