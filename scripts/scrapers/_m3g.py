"""M3G shared helpers — master GeoJSON + project membership + per-station sitelog attrs.

M3G (gnss-metadata.eu) is a friendly, programmatically-readable GNSS
metadata catalogue. Four endpoints in use:

| endpoint | shape | use |
|---|---|---|
| `POST /site/index` | GeoJSON list, ~3.6k features | id → (lat, lon) for every M3G-registered station |
| `GET /v1/sitelog/metadata-list?downloadFormat=log&validMetadata=1` | text table | id → (update_ts, sitelog_url); the `update(system-time)` column is the incremental-fetch cursor for per-station attrs |
| `GET /MOID/projnet.<moid>` | HTML | universe of 9-char IDs ever assigned to this network (incl. retired) |
| `GET /v1/sitelog/exportlog?id=<id>` | IGS sitelog text | per-station attrs: retirement status, agency |

**Removal detection** is split across two signals because M3G has no
first-class "currently active" flag:
- Project page is **sticky on removals** — retired IDs linger forever
  (verified: 7 ESTPOS predecessors still listed alongside successors).
- Per-station sitelog **does** carry retirement: the last non-template
  receiver block (Section 3.N, not the 3.x template) has a concrete
  `Date Removed` when the station is permanently retired; a placeholder
  (`CCYY-MM-DDThh:mmZ` or `(CCYY-...)`) means current equipment is
  still installed.
So the architecture is: project page gives the universe; per-station
sitelog gives the retirement filter.

**Incremental cache**: per-station sitelog fetches use the metadata-list's
`update(system-time)` as a cursor. Stations whose `update_ts` matches the
cached value are skipped (`fetch_station_attrs` does the comparison and
only re-fetches sitelogs that changed since last run). Initial bootstrap
cost is N per referenced ID; steady-state is near zero.

All caches are disk-persisted under `data/_m3g_*.json` (gitignored —
private optimisation, not pipeline output).
"""
from __future__ import annotations

import datetime as _dt
import json
import re
import threading
import urllib.request
from pathlib import Path
from typing import Iterable

URL_FEATURES = "https://gnss-metadata.eu/site/index"
URL_METADATA = "https://gnss-metadata.eu/v1/sitelog/metadata-list?downloadFormat=log&validMetadata=1"
URL_PROJECT  = "https://gnss-metadata.eu/MOID/projnet.{moid}"
URL_SITELOG  = "https://gnss-metadata.eu/v1/sitelog/exportlog?id={id}"

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
CACHE_FEATURES     = DATA_DIR / "_m3g_features.json"
CACHE_METADATA     = DATA_DIR / "_m3g_metadata.json"
CACHE_PROJECTS     = DATA_DIR / "_m3g_projects.json"
CACHE_STATION_ATTRS = DATA_DIR / "_m3g_station_attrs.json"

CACHE_TTL_DAYS = 7
# metadata-list renders ~900 KB and routinely takes ~60 s server-side.
# Set generously; per-call latency is amortised by the 7-day disk cache.
TIMEOUT = 120
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (helper _m3g)"

# 9-char IGS station ID: 4 alnum + "00" + 3 letters (ISO3).
NINECHAR_RE = re.compile(r"\b([A-Z0-9]{4}00[A-Z]{3})\b")

_lock = threading.Lock()
_mem: dict[str, object] = {}


# ---- HTTP / cache utilities --------------------------------------------------

def _http(
    url: str, *, method: str = "GET", data: bytes | None = None,
    accept: str | None = None, xhr: bool = False,
) -> bytes:
    """HTTP helper. M3G's `Accept` handling is endpoint-specific — the
    sitelog endpoint 424s on `Accept: application/json` (it can only
    render text), the metadata-list endpoint switches output format
    based on Accept. Default omits the header; callers opt in.
    """
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    if xhr:
        headers["X-Requested-With"] = "XMLHttpRequest"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


def _now() -> _dt.datetime:
    return _dt.datetime.now(_dt.timezone.utc)


def _read_cache(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _write_cache(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")


def _cache_fresh(cache: dict | None) -> bool:
    if cache is None:
        return False
    try:
        ts = _dt.datetime.fromisoformat(cache["fetched_at"])
    except (KeyError, ValueError):
        return False
    return _now() - ts <= _dt.timedelta(days=CACHE_TTL_DAYS)


# ---- Master GeoJSON: id → (lat, lon) -----------------------------------------

def fetch_features(force: bool = False) -> dict[str, tuple[float, float]]:
    """Return `{9-char-id: (lat, lon)}` for every M3G-registered station."""
    with _lock:
        if not force and "features" in _mem:
            return _mem["features"]  # type: ignore[return-value]
        if not force:
            cache = _read_cache(CACHE_FEATURES)
            if _cache_fresh(cache):
                feats = {sid: tuple(coords) for sid, coords in cache["features"].items()}
                _mem["features"] = feats
                return feats
        feats = _fetch_features_remote()
        _write_cache(CACHE_FEATURES, {
            "fetched_at": _now().isoformat(timespec="seconds"),
            "source_url": URL_FEATURES,
            "feature_count": len(feats),
            "features": {sid: [lat, lon] for sid, (lat, lon) in feats.items()},
        })
        _mem["features"] = feats
        return feats


def _fetch_features_remote() -> dict[str, tuple[float, float]]:
    geo = json.loads(_http(URL_FEATURES, method="POST", data=b"",
                            accept="application/json", xhr=True).decode("utf-8"))
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


# ---- Metadata-list: id → update_ts (incremental cursor) ----------------------

def fetch_metadata_list(force: bool = False) -> dict[str, str]:
    """Return `{9-char-id: update_ts_iso}` from M3G metadata-list.

    The `update(system-time)` column tracks the last M3G-side metadata
    change for each station. Used as the cache cursor for per-station
    sitelog fetches: when this value changes, the cached attrs are stale.
    """
    with _lock:
        if not force and "metadata" in _mem:
            return _mem["metadata"]  # type: ignore[return-value]
        if not force:
            cache = _read_cache(CACHE_METADATA)
            if _cache_fresh(cache):
                _mem["metadata"] = cache["update_ts"]
                return cache["update_ts"]
        body = _http(URL_METADATA, accept="application/json").decode("utf-8", errors="replace")
        update_ts = _parse_metadata_list(body)
        _write_cache(CACHE_METADATA, {
            "fetched_at": _now().isoformat(timespec="seconds"),
            "source_url": URL_METADATA,
            "update_ts": update_ts,
        })
        _mem["metadata"] = update_ts
        return update_ts


def _parse_metadata_list(body: str) -> dict[str, str]:
    rows = json.loads(body)
    out: dict[str, str] = {}
    for r in rows:
        sid = r.get("id")
        ts = r.get("update(system-time)")
        if sid and ts and NINECHAR_RE.fullmatch(sid):
            out[sid] = ts
    if not out:
        raise ValueError("M3G metadata-list returned 0 parseable rows")
    return out


# ---- Project page: moid → universe of 9-char IDs -----------------------------

def fetch_project_ids(moid: str, force: bool = False) -> list[str]:
    """Return all 9-char IDs ever assigned to this network (incl. retired).

    Cached per-moid on disk; refreshed at `CACHE_TTL_DAYS`. Membership
    universe needs the Date Removed filter (`fetch_station_attrs`) to
    drop retired entries.
    """
    with _lock:
        cache = _read_cache(CACHE_PROJECTS) or {"projects": {}}
        proj = cache.get("projects", {}).get(moid)
        if not force and proj and _cache_fresh(proj):
            return list(proj["ids"])
        html = _http(URL_PROJECT.format(moid=moid)).decode("utf-8", errors="replace")
        ids = sorted(set(NINECHAR_RE.findall(html)))
        if not ids:
            raise ValueError(f"M3G project {moid} returned 0 station IDs")
        cache.setdefault("projects", {})[moid] = {
            "fetched_at": _now().isoformat(timespec="seconds"),
            "source_url": URL_PROJECT.format(moid=moid),
            "ids": ids,
        }
        _write_cache(CACHE_PROJECTS, cache)
        return ids


# ---- Per-station sitelog attrs (retirement, agency) --------------------------

_RECEIVER_HEADER_RE = re.compile(r"^3\.([0-9]+|x)\s+Receiver Type", re.MULTILINE)
_DATE_REMOVED_RE   = re.compile(r"^\s*Date Removed\s*:\s*(\S+)", re.MULTILINE)
_AGENCY_LINE_RE    = re.compile(r"^\s*Agency\s*:\s*(\S.*?)\s*$", re.MULTILINE)
_PLACEHOLDER_PREFIXES = ("CCYY", "(CCYY")


def _parse_sitelog_retirement(text: str) -> tuple[bool, str | None]:
    """Return (retired, last_removal_date_iso_or_None).

    Walks Section 3 receiver blocks in order, skipping the `3.x`
    template block. The retirement state is whatever the **last**
    non-template block says: concrete `Date Removed` → retired;
    placeholder → active.
    """
    headers = list(_RECEIVER_HEADER_RE.finditer(text))
    if not headers:
        return False, None
    last_state = "active"
    last_removed: str | None = None
    for i, m in enumerate(headers):
        if m.group(1) == "x":
            continue
        body_end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        body = text[m.end():body_end]
        m_rm = _DATE_REMOVED_RE.search(body)
        if not m_rm:
            last_state, last_removed = "active", None
            continue
        val = m_rm.group(1).strip()
        if val.startswith(_PLACEHOLDER_PREFIXES):
            last_state, last_removed = "active", None
        else:
            last_state, last_removed = "retired", val
    return last_state == "retired", last_removed


def _parse_sitelog_agency(text: str) -> str | None:
    """Operator agency from Section 11 (on-site point of contact).

    Section 11 is the canonical operator; Section 12 ("Responsible Agency
    if different from 11.") is usually left as the IGS template's
    `(multiple lines)` placeholder and is uninformative. Both sections
    can carry placeholder text — reject those values.
    """
    placeholders = {"(multiple lines)", "(A10)", "(A50)", "(A)", ""}
    for section in ("11", "12"):
        block = re.search(rf"^{section}\.\s.*?(?=^\d+\.\s)",
                          text, re.MULTILINE | re.DOTALL)
        if not block:
            continue
        m = _AGENCY_LINE_RE.search(block.group(0))
        if not m:
            continue
        val = m.group(1).strip()
        if val not in placeholders:
            return val
    return None


def fetch_station_attrs(ids: Iterable[str], force: bool = False) -> dict[str, dict]:
    """Per-ID `{retired: bool, retired_at: str|None, agency: str|None, update_ts: str}`.

    Incremental: stations whose `update_ts` (from metadata-list) matches
    the cached value are NOT re-fetched. Force=True bypasses both
    in-process memo and disk cache and re-fetches every requested ID.
    """
    ids = list(ids)
    metadata = fetch_metadata_list(force=force)
    with _lock:
        cache = _read_cache(CACHE_STATION_ATTRS) or {"attrs": {}}
        attrs = cache.setdefault("attrs", {})
        if force:
            stale = list(ids)
        else:
            stale = [
                sid for sid in ids
                if sid in metadata
                and (sid not in attrs or attrs[sid].get("update_ts") != metadata[sid])
            ]
        fetched = 0
        for sid in stale:
            try:
                text = _http(URL_SITELOG.format(id=sid)).decode("utf-8", errors="replace")
            except Exception as e:
                print(f"[_m3g] sitelog fetch failed {sid}: {e!r}", flush=True)
                continue
            retired, retired_at = _parse_sitelog_retirement(text)
            agency = _parse_sitelog_agency(text)
            attrs[sid] = {
                "update_ts": metadata.get(sid),
                "retired": retired,
                "retired_at": retired_at,
                "agency": agency,
            }
            fetched += 1
        if fetched:
            cache["fetched_at"] = _now().isoformat(timespec="seconds")
            _write_cache(CACHE_STATION_ATTRS, cache)
            print(f"[_m3g] refreshed {fetched} sitelog(s)", flush=True)
        return {sid: dict(attrs[sid]) for sid in ids if sid in attrs}
