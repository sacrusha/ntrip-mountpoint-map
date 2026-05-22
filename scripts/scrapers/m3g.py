"""Generic M3G scraper — one impl for every M3G-backed network.

Endpoint config in `data/rtk_map.json` carries the per-network spec:

```json
{
  "type": "scraped",
  "id": "estpos_ext",
  "scraper": "m3g",
  "country": "EST",
  "ids": ["AJOE", "ALAK", ...],
  "interval_days": 7,
  "pin_origin": "register"
}
```

`country` is the ISO3 suffix that M3G appends to the 9-char IDs (so
the lookup key is `f"{sid}00{country}"`). `ids` is the operator's
active 4-char station list. The shared `_m3g` helper fetches the
master GeoJSON once per pipeline run (and disk-caches it 7d), then
this scraper filters down to the network's IDs.
"""
from __future__ import annotations

from . import _m3g


def scrape(src: dict) -> dict:
    ids = src.get("ids")
    country = src.get("country")
    if not ids:
        raise ValueError("m3g scraper requires endpoint 'ids' array")
    if not country or len(country) != 3:
        raise ValueError(f"m3g scraper requires 3-char 'country' code, got {country!r}")

    feats = _m3g.fetch_features()
    stations: list[dict] = []
    missing: list[str] = []
    for sid in ids:
        coords = feats.get(f"{sid}00{country}")
        if coords is None:
            missing.append(sid)
            continue
        lat, lon = coords
        stations.append({"name": sid, "lat": lat, "lon": lon, "country": country})

    if missing:
        print(f"[m3g/{src.get('id')}] missing from M3G master: {missing}", flush=True)
    if not stations:
        raise ValueError(
            f"m3g scraper resolved 0 of {len(ids)} IDs from M3G master "
            f"(country={country})"
        )

    stations.sort(key=lambda s: s["name"])
    return {
        "source_url": "https://gnss-metadata.eu/site/index (M3G master GeoJSON)",
        "stations": stations,
    }
