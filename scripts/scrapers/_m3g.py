"""M3G master GeoJSON shared helper.

The M3G map at https://gnss-metadata.eu/site/index POSTs to itself with
no body and gets back a single GeoJSON FeatureCollection holding every
M3G-registered station across every network (~3.6k features). One
master fetch lets any number of per-network scrapers (`estpos`,
`walcors`, ...) resolve coordinates by 9-char ID without per-station
HTTP cost.

Politeness: this helper is hit once per pipeline run *across* all M3G-
backed scrapers, and the response is disk-cached at
`data/_m3g_features.json` for `CACHE_TTL_DAYS` (default 7). Delete the
cache file to force a re-fetch on the next run, or pass `force=True`.
Disk cache is gitignored — it's a private optimisation, not pipeline
output.

In-process memoisation on top so concurrent stale-cache scrapers in the
same pipeline run never trigger more than one HTTP call.
"""
from __future__ import annotations

import datetime as _dt
import json
import threading
import urllib.request
from pathlib import Path

URL = "https://gnss-metadata.eu/site/index"
CACHE_PATH = Path(__file__).resolve().parents[2] / "data" / "_m3g_features.json"
CACHE_TTL_DAYS = 7
TIMEOUT = 30
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (helper _m3g)"

_lock = threading.Lock()
_cache: dict[str, tuple[float, float]] | None = None


def _http_post() -> bytes:
    req = urllib.request.Request(
        URL, data=b"", method="POST",
        headers={
            "User-Agent": USER_AGENT,
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


def _read_disk_cache() -> dict[str, tuple[float, float]] | None:
    if not CACHE_PATH.exists():
        return None
    try:
        d = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        ts = _dt.datetime.fromisoformat(d["fetched_at"])
    except (OSError, KeyError, ValueError, json.JSONDecodeError):
        return None
    if _dt.datetime.now(_dt.timezone.utc) - ts > _dt.timedelta(days=CACHE_TTL_DAYS):
        return None
    return {sid: (lat, lon) for sid, (lat, lon) in d["features"].items()}


def _write_disk_cache(features: dict[str, tuple[float, float]]) -> None:
    payload = {
        "fetched_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "source_url": URL,
        "feature_count": len(features),
        "features": {sid: [lat, lon] for sid, (lat, lon) in features.items()},
    }
    CACHE_PATH.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")


def _fetch_remote() -> dict[str, tuple[float, float]]:
    geo = json.loads(_http_post().decode("utf-8"))
    out: dict[str, tuple[float, float]] = {}
    for f in geo:
        sid = (f.get("properties") or {}).get("id")
        coords = (f.get("geometry") or {}).get("coordinates")
        if not sid or not coords or len(coords) < 2:
            continue
        out[sid] = (coords[1], coords[0])  # GeoJSON is [lon, lat, height]
    if not out:
        raise ValueError("M3G master GeoJSON returned 0 features")
    return out


def fetch_features(force: bool = False) -> dict[str, tuple[float, float]]:
    """Return `{9-char-id: (lat, lon)}` for every M3G-registered station.

    Resolution order: in-process memo → disk cache (if fresh) → remote.
    `force=True` skips both caches and forces a fresh remote fetch
    (then overwrites the disk cache).
    """
    global _cache
    with _lock:
        if _cache is not None and not force:
            return _cache
        if not force:
            disk = _read_disk_cache()
            if disk is not None:
                _cache = disk
                return _cache
        features = _fetch_remote()
        _write_disk_cache(features)
        _cache = features
        return _cache
