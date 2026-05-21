"""Shared helper for ArcGIS FeatureServer / MapServer station-layer scrapes.

ArcGIS REST exposes a per-layer `query` endpoint that returns features
as JSON. The same response shape works for FeatureServer and MapServer
layers — fields metadata + per-feature `attributes` and `geometry`.

This module hides the URL/paging plumbing so each scraper only declares
the layer URL, which attribute is the station name, and (optionally) a
filter callable. The module is internal to `scripts/scrapers/`; concrete
per-source scrapers (`iartn.py`, `vector.py`, `wvrtn.py`) re-export
`scrape()` by parameterising it.
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from typing import Callable, Iterable

TIMEOUT = 20
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper arcgis)"
PAGE_SIZE = 1000  # ArcGIS default maxRecordCount; well above any of our layers.


def _http_get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


def _query_features(layer_url: str) -> list[dict]:
    """Fetch all features from an ArcGIS layer in WGS84 (EPSG:4326).

    Pages via `resultOffset` until the server stops returning features.
    Returns the raw list of feature dicts (`{attributes: {...}, geometry: {x, y}}`).
    """
    base = layer_url.rstrip("/") + "/query"
    out: list[dict] = []
    offset = 0
    while True:
        params = urllib.parse.urlencode({
            "where": "1=1",
            "outFields": "*",
            "f": "json",
            "outSR": "4326",
            "resultOffset": str(offset),
            "resultRecordCount": str(PAGE_SIZE),
        })
        body = _http_get(f"{base}?{params}")
        payload = json.loads(body.decode("utf-8", errors="replace"))
        if "error" in payload:
            raise ValueError(f"ArcGIS error: {payload['error']}")
        features = payload.get("features", [])
        if not features:
            break
        out.extend(features)
        # The server stops paging when fewer than PAGE_SIZE come back.
        if len(features) < PAGE_SIZE:
            break
        offset += len(features)
    return out


def scrape_layer(
    *,
    layer_url: str,
    name_field: str,
    country: str,
    keep: Callable[[dict], bool] | None = None,
    name_transform: Callable[[str], str] | None = None,
) -> dict:
    """Return parsed station list from an ArcGIS layer.

    Parameters
    ----------
    layer_url
        Full URL of the FeatureServer or MapServer layer (no `/query`).
    name_field
        Key inside `feature["attributes"]` that carries the station
        identifier used as the pin label.
    country
        ISO 3166-1 alpha-3 written into every station record.
    keep
        Optional predicate(feature) -> bool to filter features.
    name_transform
        Optional function applied to the name string before storing.

    Raises on any HTTP or parse failure — the caller's `_fetch_scraped_source`
    falls back to the on-disk cache.
    """
    features = _query_features(layer_url)
    if not features:
        raise ValueError(f"ArcGIS layer returned 0 features: {layer_url}")

    stations: list[dict] = []
    for feat in features:
        if keep is not None and not keep(feat):
            continue
        attrs = feat.get("attributes") or {}
        geom = feat.get("geometry") or {}
        name = attrs.get(name_field)
        if name is None:
            continue
        name = str(name).strip()
        if name_transform is not None:
            name = name_transform(name)
        if not name:
            continue
        try:
            lon = float(geom["x"])
            lat = float(geom["y"])
        except (KeyError, TypeError, ValueError):
            continue
        # ArcGIS occasionally emits null-island sentinels for unconfigured
        # rows; skip rather than commit garbage to the cache.
        if lat == 0 and lon == 0:
            continue
        stations.append({
            "name": name,
            "lat": round(lat, 6),
            "lon": round(lon, 6),
            "country": country,
        })

    if not stations:
        raise ValueError(f"ArcGIS layer matched 0 stations after filter: {layer_url}")

    # Stable order so unchanged scrapes produce no cache diff.
    stations.sort(key=lambda s: s["name"])
    return {"source_url": layer_url, "stations": stations}
