"""Per-source scraper modules for the `scraped` source type.

Each module exposes a `scrape() -> dict` callable returning:
    {"source_url": "...", "stations": [{"name": str, "lat": float, "lon": float,
                                         "country": str?}, ...]}

Raises any exception on failure — `_fetch_scraped_source` in
`scripts/fetch_stations.py` catches and falls back to the on-disk cache.

Module discovery: the endpoint's `scraper` field names the module
(`sapos_bb` -> `scripts.scrapers.sapos_bb`). Add a new scraper by writing
a module here and registering the endpoint in `data/rtk_map.json`.
"""
