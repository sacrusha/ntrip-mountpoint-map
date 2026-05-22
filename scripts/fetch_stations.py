#!/usr/bin/env python3
"""Fetch NTRIP sourcetables, parse them, and write data/stations.json.

Operational config (which networks to fetch, their endpoints, credentials,
filter overrides) lives in `data/rtk_map.json` — each marker entry with a
non-empty `endpoints[]` is a fetch target. Multi-endpoint networks (e.g.
`ergnss` mainland + Canary SPTR) merge into one stations.json record.

Skips the write (and thereby any commit) when the set of parsed stations
is byte-identical to the previous run. If an endpoint fails to fetch, its
previous raw sourcetable on disk is reused so a transient outage does not
wipe known-good data.

Process / network-config editing rules: see fetch_stations.proc.md
(same dir) and `../data/rtk_map.proc.md`. Pipeline context:
`../docs/pipeline.md`.
"""
from __future__ import annotations

import http.client
import importlib
import inspect
import json
import os
import math
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

# Re-exec with UTF-8 mode on platforms (Windows) where the default locale
# encoding is not UTF-8, so all file I/O uses UTF-8 without per-call overrides.
if not sys.flags.utf8_mode:
    os.execv(sys.executable, [sys.executable, "-X", "utf8", *sys.argv])

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def _load_coord_overrides() -> dict[tuple[str, float, float], dict]:
    """Read `data/coord_overrides.json` into a lookup keyed by
    `(mountpoint_name, bad_lat, bad_lon)`. An override only fires when all
    three match the parsed station record exactly; this guards against
    stale entries silently rewriting good data after an operator fixes the
    upstream sourcetable. Missing file -> empty dict (pipeline continues
    untouched)."""
    path = DATA_DIR / "coord_overrides.json"
    if not path.exists():
        return {}
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"[coord_overrides] parse error: {e!r}", file=sys.stderr)
        return {}
    out = {}
    for entry in raw.get("overrides", []):
        key = (entry["mountpoint"], entry["bad"]["lat"], entry["bad"]["lon"])
        out[key] = entry["fix"]
    return out


# Loaded once at import time. Add/edit entries in data/coord_overrides.json,
# not here.
COORD_OVERRIDES = _load_coord_overrides()


def _atomic_write_text(path: Path, content: str) -> None:
    """Write content to path via tmp+replace. os.replace is atomic on
    POSIX and on Windows (NTFS); leaves the target either intact (on
    crash mid-write) or fully replaced. Tmp file lives in the same dir
    so the rename stays on one filesystem."""
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(content)
    os.replace(tmp, path)


def _dec_places(s: str) -> int:
    """Decimal places in a coordinate string, used for accuracy-rectangle sizing."""
    dot = s.find('.')
    return 0 if dot == -1 else len(s) - dot - 1


def load_networks() -> list[dict]:
    """Read operational network config from data/rtk_map.json.

    Returns the subset of marker entries with a non-empty endpoints[] array.
    Each network entry: {id, endpoints: [{url, id?, credentials?, near?,
    nmea_filter?, solution_filter?}, ...]}.
    """
    data = json.loads((DATA_DIR / "rtk_map.json").read_text(encoding="utf-8"))
    return [
        {"id": m["id"], "endpoints": m["endpoints"]}
        for m in data["markers"] if m.get("endpoints")
    ]


def _endpoint_id(net: dict, idx: int) -> str:
    """Cache-file basename for the endpoint at idx within a network.
    Explicit endpoint.id wins; otherwise network.id for the first endpoint
    and "{network.id}_{idx}" for subsequent ones."""
    ep = net["endpoints"][idx]
    if ep.get("id"):
        return ep["id"]
    return net["id"] if idx == 0 else f"{net['id']}_{idx}"


def _flatten_endpoints(networks: list[dict]) -> list[dict]:
    """Flatten networks into per-endpoint fetch configs.

    Each entry carries the parent network_id + endpoint_idx so main() can
    merge fetched results back per-network. Legacy fields user/pass/userNote
    are surfaced from endpoint.credentials for backward compat with
    sources_list.py / popup-credential rendering."""
    # Endpoint keys re-shaped by the flattener (renamed, defaulted, or
    # unpacked from sub-objects). Anything not in this set is forwarded
    # verbatim so handlers can pick up scraper-specific config without
    # editing this function.
    reshaped = {"type", "url", "credentials", "near",
                "nmea_filter", "solution_filter", "vrs_required"}
    out = []
    for net in networks:
        for idx, ep in enumerate(net["endpoints"]):
            creds = ep.get("credentials") or {}
            entry = {
                "id":              _endpoint_id(net, idx),
                "network_id":      net["id"],
                "endpoint_idx":    idx,
                "type":            ep.get("type", "ntrip"),
                "url":             ep.get("url"),
                "credentials":     ep.get("credentials"),
                "near":            ep.get("near", False),
                "user":            creds.get("user"),
                "pass":            creds.get("pass"),
                "userNote":        creds.get("userNote"),
                "nmea_filter":     ep.get("nmea_filter", True),
                "solution_filter": ep.get("solution_filter", True),
                "vrs_required":    ep.get("vrs_required", False),
            }
            for k, v in ep.items():
                if k not in reshaped:
                    entry.setdefault(k, v)
            out.append(entry)
    return out


NETWORKS = load_networks()
SOURCES = _flatten_endpoints(NETWORKS)  # legacy flat per-endpoint view


FETCH_TIMEOUT = 5
STALE_GREY_DAYS = 8   # sources offline this long shown as grey dots, excluded from coverage raster
STALE_HIDE_DAYS = 16  # sources offline this long hidden entirely
# Sized for weekly external-coord scrapes (8 = one week + a day of grace);
# NTRIP fetches at 4×/day rarely bump up against these thresholds anyway.


def _fetch_ntrip1(host: str, port: int) -> str:
    """Raw-TCP fetch for NTRIP 1.0 casters (respond SOURCETABLE 200 OK, not HTTP)."""
    with socket.create_connection((host, port), timeout=FETCH_TIMEOUT) as sock:
        sock.sendall(
            b"GET / HTTP/1.0\r\n"
            b"User-Agent: NTRIP ntrip-mountpoint-map/1.0\r\n"
            b"Ntrip-Version: Ntrip/1.0\r\n"
            b"\r\n"
        )
        chunks: list[bytes] = []
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
            if b"ENDSOURCETABLE" in chunk:
                break
    return b"".join(chunks).decode("utf-8", errors="replace")


def fetch(url: str) -> str:
    req = Request(url, headers={
        "User-Agent": "NTRIP ntrip-mountpoint-map/1.0",
        "Ntrip-Version": "Ntrip/2.0",
        "Accept": "*/*",
    })
    try:
        with urlopen(req, timeout=FETCH_TIMEOUT) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except http.client.BadStatusLine:
        parsed = urlparse(url)
        return _fetch_ntrip1(parsed.hostname, parsed.port or 2101)


def parse_sourcetable(text: str, nmea_filter: bool = True,
                      solution_filter: bool = True,
                      vrs_required: bool = False) -> tuple[list[dict], dict]:
    """Parse an NTRIP sourcetable.

    NTRIP STR line fields (0-based after splitting on ';'):
      0 STR, 1 mountpoint, 2 identifier, 3 format, 4 format-details,
      5 carrier, 6 nav-system, 7 network, 8 country,
      9 latitude, 10 longitude, 11 nmea, 12 solution, ..., 15 auth, 16 fee.

    Drops DGNSS-only mountpoints (carrier == 0) — out of the site's
    sub-50-cm scope.

    When nmea_filter is True (default), also drops mountpoints where the NMEA
    field is "1".  NMEA=1 means the caster requires the rover to send its
    position, which is the defining trait of VRS/network-solution streams
    (iMAX, MAC, FKP, NEAREST, etc.) — they have no fixed antenna location and
    report a fake reference coordinate.  Physical single-base stations always
    have NMEA=0.  Set nmea_filter=False in SOURCES for any caster that
    incorrectly tags real physical stations with NMEA=1.

    When solution_filter is True (default), also drops mountpoints where the
    solution field is "1".  Solution=1 means "network solution" per the NTRIP
    spec — a computed VRS/iMAX/NEAREST position, not a real receiver.
    Physical single-base stations have solution=0.  This is a second guard for
    casters like rtk2go that disable nmea_filter but still correctly tag their
    NEAR-xxx network streams as solution=1.  Set solution_filter=False for
    casters that misapply solution=1 to real physical stations.
    """
    stations: list[dict] = []
    dropped_dgnss = 0
    dropped_net = 0
    dropped_bad = 0
    dropped_postproc = 0
    corrected = 0
    for line in text.splitlines():
        if not line.startswith("STR;"):
            continue
        fields = line.split(";")
        if len(fields) < 11:
            dropped_bad += 1
            continue
        name = fields[1].strip()
        fmt = fields[3].strip() if len(fields) > 3 else ""
        fmt_details = fields[4].strip() if len(fields) > 4 else ""
        carrier_raw = fields[5].strip() if len(fields) > 5 else ""
        nav_sys = fields[6].strip() if len(fields) > 6 else ""
        country = fields[8].strip() if len(fields) > 8 else ""
        lat_str = fields[9].strip()
        lon_str = fields[10].strip()
        nmea = fields[11].strip() if len(fields) > 11 else ""
        solution = fields[12].strip() if len(fields) > 12 else ""
        # rtk2go leaves the carrier field blank for most entries even though
        # they broadcast RTCM 3.x carrier-phase observations. Trust the
        # format string as a fallback: RTCM 3.x MSM streams are cm-capable.
        if carrier_raw == "":
            if fmt.startswith("RTCM 3"):
                carrier = 2
            else:
                carrier = -1
        else:
            try:
                carrier = int(carrier_raw)
            except ValueError:
                carrier = -1
        if carrier == 0:
            dropped_dgnss += 1
            continue
        if carrier not in (1, 2, 3):
            dropped_bad += 1
            continue
        # RAW = post-process-only raw observation stream (RINEX-equivalent),
        # no standard rover can consume it for real-time RTK. Trimble Pivot
        # casters routinely publish *_RAW variants alongside RTCM 3.x.
        # Trimble's DGPS-targeted variant declares format as RTCM 2.x but
        # carries the Position Broadcast Service (PBS) auxiliary message,
        # which contradicts the RTCM 2.x convention (real RTCM 2.x RTK uses
        # messages 18/19/22/23/24/59, never PBS). CROPOS *_DPS_23 fits this
        # pattern. PBS *alongside* RTCM 3.x is the normal Trimble Pivot
        # config (nps_cors, kycors, sapos_*) — keep those.
        if fmt == "RAW":
            dropped_postproc += 1
            continue
        if fmt.startswith("RTCM 2") and "PBS" in fmt_details:
            dropped_postproc += 1
            continue
        if nmea_filter and nmea == "1":
            dropped_net += 1
            continue
        if solution_filter and solution == "1":
            dropped_net += 1
            continue
        try:
            lat = float(lat_str)
            lon = float(lon_str)
        except ValueError:
            dropped_bad += 1
            continue
        # Normalize 0-360 longitude to ±180 (some casters, e.g. ERGNSS, report
        # western longitudes as e.g. 353.65 instead of -6.35).
        if lon > 180:
            lon -= 360
        elif lon < -180:
            lon += 360
        if lat == 0 and lon == 0:
            dropped_bad += 1
            continue
        if not (math.isfinite(lat) and math.isfinite(lon)):
            dropped_bad += 1
            continue
        lat_prec = _dec_places(lat_str)
        lon_prec = _dec_places(lon_str)
        fix = COORD_OVERRIDES.get((name, lat, lon))
        if fix is not None:
            lat = fix["lat"]
            lon = fix["lon"]
            lat_prec = fix.get("latPrec", lat_prec)
            lon_prec = fix.get("lonPrec", lon_prec)
            corrected += 1
        rec = {
            "name": name,
            "lat": lat,
            "lon": lon,
            "latPrec": lat_prec,
            "lonPrec": lon_prec,
            "dualFreq": carrier >= 2,
            "tripleFreq": carrier >= 3,
            "format": fmt,
            "constellations": nav_sys,
            "country": country,
        }
        if vrs_required:
            rec["vrsRequired"] = True
        stations.append(rec)
    stations.sort(key=lambda s: (s["name"], s["lat"], s["lon"]))
    stats = {"kept": len(stations), "dropped_dgnss": dropped_dgnss,
             "dropped_net": dropped_net, "dropped_bad": dropped_bad,
             "dropped_postproc": dropped_postproc, "corrected": corrected}
    return stations, stats


def filter_vrs(stations: list[dict]) -> tuple[list[dict], int]:
    """Drop all stations when every entry shares the same coordinate.

    VRS casters report all virtual mountpoints at a single reference point
    (often a rounded city centre). Real CORS networks have distinct lat/lon
    per antenna.  Returning an empty list causes the source to be treated as
    0-station so the UI hides it automatically.
    """
    if len(stations) < 2:
        return stations, 0
    if len({(s["lat"], s["lon"]) for s in stations}) == 1:
        return [], len(stations)
    return stations, 0


def load_existing(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return None


def station_fingerprint(source: dict) -> list[list]:
    return [
        [s["name"], s["lat"], s.get("latPrec"), s["lon"], s.get("lonPrec"),
         s.get("dualFreq"), s.get("tripleFreq"), s.get("format", ""), s.get("constellations", ""),
         s.get("vrsRequired", False), s.get("pin_origin", "ntrip")]
        for s in source.get("stations", [])
    ]


def fetch_source(src: dict) -> tuple[str, dict, bool]:
    """Dispatch a source to its type-specific handler.

    Each handler returns the (sid, result, was_fresh) shape this function's
    callers expect. Default type is 'ntrip' for back-compat with endpoints[]
    entries that pre-date the 'type' field.
    """
    src_type = src.get("type", "ntrip")
    handler = HANDLERS.get(src_type)
    if handler is None:
        raise ValueError(f"[{src['id']}] unknown source type {src_type!r}; "
                         f"known: {sorted(HANDLERS)}")
    return handler(src)


def _fetch_ntrip_source(src: dict) -> tuple[str, dict, bool]:
    """Fetch and parse an NTRIP sourcetable. Returns (sid, result, was_fresh)."""
    sid, url = src["id"], src["url"]
    src_credentials = src.get("credentials")
    prev_last_ok = src.get("_prev_last_ok")
    nmea_filter = src.get("nmea_filter", True)
    solution_filter = src.get("solution_filter", True)
    vrs_required = src.get("vrs_required", False)
    raw_path = DATA_DIR / f"{sid}.sourcetable"
    _meta = {
        "url": url,
        "credentials": src_credentials,
        "near": src.get("near", False),
        "user": src.get("user"),
        "pass": src.get("pass"),
        "userNote": src.get("userNote"),
    }
    try:
        text = fetch(url)
        stations, stats = parse_sourcetable(text, nmea_filter=nmea_filter, solution_filter=solution_filter, vrs_required=vrs_required)
        stations, dropped_vrs = filter_vrs(stations)
        net_note = f", {stats['dropped_net']} net-sol" if stats["dropped_net"] else ""
        vrs_note = f", {dropped_vrs} VRS" if dropped_vrs else ""
        pp_note = f", {stats['dropped_postproc']} post-process" if stats.get("dropped_postproc") else ""
        fix_note = f", {stats['corrected']} corrected" if stats.get("corrected") else ""
        now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
        print(f"[{sid}] fetched {len(stations)} stations "
              f"(dropped {stats['dropped_dgnss']} DGNSS, {stats['dropped_bad']} invalid{net_note}{vrs_note}{pp_note}{fix_note})")
        return sid, {**_meta,
            "status": "ok",
            "fetched_at": now_iso,
            "last_ok": now_iso,
            "raw_path": raw_path,
            "text": text,
            "stations": stations,
            "parse_stats": stats,
        }, True
    except (URLError, OSError, http.client.HTTPException, ValueError) as e:
        print(f"[{sid}] fetch failed: {e!r}", file=sys.stderr)
        if raw_path.exists():
            try:
                text = raw_path.read_text()
                stations, stats = parse_sourcetable(text, nmea_filter=nmea_filter, solution_filter=solution_filter, vrs_required=vrs_required)
                stations, dropped_vrs = filter_vrs(stations)
                net_note = f", {stats['dropped_net']} net-sol" if stats["dropped_net"] else ""
                vrs_note = f", {dropped_vrs} VRS" if dropped_vrs else ""
                pp_note = f", {stats['dropped_postproc']} post-process" if stats.get("dropped_postproc") else ""
                fix_note = f", {stats['corrected']} corrected" if stats.get("corrected") else ""
                print(f"[{sid}] reusing cached sourcetable ({len(stations)} stations{net_note}{vrs_note}{pp_note}{fix_note})")
                return sid, {**_meta,
                    "status": "stale",
                    "fetched_at": None,
                    "last_ok": prev_last_ok,
                    "raw_path": raw_path,
                    "text": text,
                    "stations": stations,
                    "parse_stats": stats,
                }, False
            except Exception as cache_err:
                print(f"[{sid}] cached sourcetable unreadable: {cache_err!r}", file=sys.stderr)
        return sid, {**_meta,
            "status": "error",
            "fetched_at": None,
            "last_ok": prev_last_ok,
            "raw_path": raw_path,
            "text": None,
            "stations": [],
        }, False


def _build_external_records(entries: list[dict], pin_origin: str) -> list[dict]:
    """Build per-station records from a curated/scraped entry list.

    Shared by `_fetch_file_source` and `_fetch_scraped_source` — both
    consume the same `{name, lat, lon, format?, carrier?, constellations?,
    country?}` dict shape. Entries that can't parse lat/lon are dropped
    silently (file is editor-controlled; scrape modules pre-validate)."""
    out = []
    for entry in entries:
        try:
            lat = float(entry["lat"])
            lon = float(entry["lon"])
        except (KeyError, TypeError, ValueError):
            continue
        rec = {
            "name": entry["name"],
            "lat": lat,
            "lon": lon,
            "latPrec": entry.get("latPrec", _dec_places(str(lat))),
            "lonPrec": entry.get("lonPrec", _dec_places(str(lon))),
            "country": entry.get("country", ""),
            "pin_origin": pin_origin,
        }
        # Format / carrier are optional. Omitting them signals "frequency
        # capability unknown" to the UI (vs the L1-default fallthrough that
        # would mislabel as a confirmed single-frequency station).
        if "format" in entry:
            rec["format"] = entry["format"]
        if "constellations" in entry:
            rec["constellations"] = entry["constellations"]
        carrier = entry.get("carrier")
        if isinstance(carrier, int):
            rec["dualFreq"] = carrier >= 2
            rec["tripleFreq"] = carrier >= 3
        out.append(rec)
    out.sort(key=lambda s: (s["name"], s["lat"], s["lon"]))
    return out


def _fetch_file_source(src: dict) -> tuple[str, dict, bool]:
    """Read a curated station list from a JSON file on disk.

    Schema (data/external_<id>.json):
      {
        "last_updated":  "YYYY-MM-DD" or ISO instant,  # drives staleness via last_ok
        "source_url":    "...",                # provenance; displayed in popup
        "pin_origin":    "forum" | "register", # routed to each station record
        "stations": [
          {"name": "X", "lat": 1.23, "lon": 4.56,
           "format": "RTCM 3", "carrier": 2,  # optional; omit if unknown
           "constellations": "GPS+GLO",       # optional
           "country": "ITA"}                  # optional
        ]
      }

    File sources are cheap to read so we don't cache: every run reads fresh.
    Status is 'ok' on read success, 'error' on read/parse failure.
    """
    sid = src["id"]
    path = ROOT / src["path"]
    pin_origin_default = src.get("pin_origin")  # endpoint-level override permitted
    _meta = {
        "url": src.get("url"),  # populated by endpoint config (typically None for file sources)
        "credentials": src.get("credentials"),
        "near": src.get("near", False),
        "user": src.get("user"),
        "pass": src.get("pass"),
        "userNote": src.get("userNote"),
    }
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"[{sid}] file source unreadable ({path}): {e!r}", file=sys.stderr)
        return sid, {**_meta,
            "status": "error",
            "fetched_at": None,
            "last_ok": None,
            "raw_path": path,
            "text": None,
            "stations": [],
        }, False
    pin_origin = raw.get("pin_origin") or pin_origin_default or "external"
    last_updated = raw.get("last_updated")
    last_ok_iso = None
    if last_updated:
        # Accept either a bare date (YYYY-MM-DD, human-friendly) or an ISO
        # instant. Stored uniformly as ISO instant in stations.json so the
        # staleness clock matches NTRIP-source `last_ok`.
        try:
            if "T" in last_updated:
                last_ok_iso = datetime.fromisoformat(last_updated.replace("Z", "+00:00"))\
                    .astimezone(timezone.utc).isoformat(timespec="seconds")
            else:
                last_ok_iso = datetime.strptime(last_updated, "%Y-%m-%d")\
                    .replace(tzinfo=timezone.utc).isoformat(timespec="seconds")
        except ValueError:
            print(f"[{sid}] last_updated not YYYY-MM-DD or ISO instant "
                  f"({last_updated!r}); staleness will read as unknown",
                  file=sys.stderr)
    stations = _build_external_records(raw.get("stations", []), pin_origin)
    src_url = raw.get("source_url")
    print(f"[{sid}] file source: {len(stations)} stations from {path.name} "
          f"(updated {last_updated or '?'}, origin={pin_origin})")
    fetched_at_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return sid, {**_meta,
        "url": src_url or _meta["url"],
        "status": "ok",
        "fetched_at": fetched_at_iso,
        "last_ok": last_ok_iso,
        "raw_path": path,
        "text": None,
        "stations": stations,
    }, True


DEFAULT_SCRAPE_INTERVAL_DAYS = 7


def _fetch_scraped_source(src: dict) -> tuple[str, dict, bool]:
    """Refresh a per-source operator-portal scrape, with disk cache fallback.

    Cache layout: `data/<endpoint_id>.scraped.json`, same schema as
    file-source inputs (`source_url`, `pin_origin`, `stations[]`) plus a
    `last_updated` ISO-8601 timestamp tracking when the data was last
    refreshed from upstream. The cache is the on-disk equivalent of the
    `.sourcetable` files NTRIP sources keep — it's the "last known good"
    output that survives a transient operator-portal outage.

    Lifecycle per run:
      1. Load existing cache if present (read once, used for both
         freshness gating and failure fallback).
      2. If cache is fresh (last_updated within `interval_days`), serve
         from cache without re-scraping. Stations come from cache;
         status is 'ok'.
      3. Otherwise, import the scraper module (`scripts.scrapers.<name>`)
         and call `scrape()`. On success, write a new cache and serve
         the freshly scraped stations.
      4. On any scrape exception, fall back to the existing cache and
         tag the source 'stale'. If no cache exists either, status is
         'error' (0 stations) — the next NTRIP-pipeline run will retry.

    `interval_days` is per-endpoint (`data/rtk_map.json`); default 7 — a
    weekly refresh keeps the scrape light on the operator and avoids
    surfacing transient maintenance-window noise.
    """
    sid = src["id"]
    scraper_name = src.get("scraper")
    if not scraper_name:
        raise ValueError(f"[{sid}] scraped source missing 'scraper' field")
    interval_days = src.get("interval_days", DEFAULT_SCRAPE_INTERVAL_DAYS)
    pin_origin_default = src.get("pin_origin")
    prev_last_ok = src.get("_prev_last_ok")
    cache_path = DATA_DIR / f"{sid}.scraped.json"
    _meta = {
        "url": src.get("url"),
        "credentials": src.get("credentials"),
        "near": src.get("near", False),
        "user": src.get("user"),
        "pass": src.get("pass"),
        "userNote": src.get("userNote"),
    }

    def _load_cache() -> dict | None:
        if not cache_path.exists():
            return None
        try:
            return json.loads(cache_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"[{sid}] cache unreadable ({cache_path}): {e!r}", file=sys.stderr)
            return None

    def _last_ok_iso(cached: dict) -> str | None:
        ts = cached.get("last_updated")
        if not ts:
            return None
        try:
            # Accept either an ISO instant (preferred) or a bare date.
            if "T" in ts:
                return datetime.fromisoformat(ts.replace("Z", "+00:00"))\
                    .astimezone(timezone.utc).isoformat(timespec="seconds")
            return datetime.strptime(ts, "%Y-%m-%d")\
                .replace(tzinfo=timezone.utc).isoformat(timespec="seconds")
        except ValueError:
            return None

    cached = _load_cache()
    now = datetime.now(timezone.utc)

    # Step 1: serve from cache if fresh enough — cheap path, no scrape.
    if cached is not None:
        last_iso = _last_ok_iso(cached)
        if last_iso is not None:
            try:
                age = now - datetime.fromisoformat(last_iso)
                if age < timedelta(days=interval_days):
                    pin_origin = cached.get("pin_origin") or pin_origin_default or "external"
                    stations = _build_external_records(cached.get("stations", []), pin_origin)
                    print(f"[{sid}] scraped cache fresh "
                          f"({len(stations)} stations, updated {last_iso}, "
                          f"age {age.days}d < {interval_days}d)")
                    return sid, {**_meta,
                        "url": cached.get("source_url") or _meta["url"],
                        "status": "ok",
                        # fetched_at = when we touched the upstream. Cache served = we didn't.
                        # Matches _fetch_ntrip_source's stale-cache convention.
                        "fetched_at": None,
                        "last_ok": last_iso,
                        "raw_path": cache_path,
                        "text": None,
                        "stations": stations,
                    }, False
            except ValueError:
                pass  # malformed timestamp; treat as needing re-scrape

    # Step 2: re-scrape. Import lazily so unused scrapers don't pay.
    # Module path follows the rest of the codebase: scripts/ is on sys.path
    # (refresh_data.py inserts it; direct `python scripts/fetch_stations.py`
    # adds it as sys.path[0]), so `scrapers.<name>` resolves either way.
    try:
        module = importlib.import_module(f"scrapers.{scraper_name}")
        scrape_fn = getattr(module, "scrape")
    except (ImportError, AttributeError) as e:
        print(f"[{sid}] scraper module 'scrapers.{scraper_name}' "
              f"unavailable: {e!r}", file=sys.stderr)
        scrape_fn = None

    if scrape_fn is not None:
        try:
            # Generic shared scrapers (e.g. `m3g`) read per-network spec
            # off the endpoint dict; single-source scrapers keep the
            # original no-arg signature. Inspect to support both.
            takes_src = bool(inspect.signature(scrape_fn).parameters)
            result = scrape_fn(src) if takes_src else scrape_fn()
            pin_origin = pin_origin_default or "external"
            new_cache = {
                "last_updated": now.isoformat(timespec="seconds"),
                "source_url":   result.get("source_url"),
                "pin_origin":   pin_origin,
                "stations":     result.get("stations", []),
            }
            _atomic_write_text(cache_path, json.dumps(new_cache, indent=2) + "\n")
            stations = _build_external_records(new_cache["stations"], pin_origin)
            print(f"[{sid}] scraped {len(stations)} stations via {scraper_name} "
                  f"(cache -> {cache_path.name})")
            return sid, {**_meta,
                "url": new_cache["source_url"] or _meta["url"],
                "status": "ok",
                "fetched_at": now.isoformat(timespec="seconds"),
                "last_ok": now.isoformat(timespec="seconds"),
                "raw_path": cache_path,
                "text": None,
                "stations": stations,
            }, True
        except Exception as e:
            print(f"[{sid}] scrape failed via {scraper_name}: {e!r}", file=sys.stderr)

    # Step 3: scrape failed (or scraper missing) — fall back to cache if any.
    if cached is not None:
        pin_origin = cached.get("pin_origin") or pin_origin_default or "external"
        stations = _build_external_records(cached.get("stations", []), pin_origin)
        last_iso = _last_ok_iso(cached) or prev_last_ok
        print(f"[{sid}] reusing cached scrape ({len(stations)} stations, "
              f"updated {last_iso or '?'})", file=sys.stderr)
        return sid, {**_meta,
            "url": cached.get("source_url") or _meta["url"],
            "status": "stale",
            "fetched_at": None,
            "last_ok": last_iso,
            "raw_path": cache_path,
            "text": None,
            "stations": stations,
        }, False

    # Step 4: no scrape, no cache, nothing to serve.
    return sid, {**_meta,
        "status": "error",
        "fetched_at": None,
        "last_ok": prev_last_ok,
        "raw_path": cache_path,
        "text": None,
        "stations": [],
    }, False


# Source-type dispatch. Add a new type by writing a handler returning the
# (sid, result, was_fresh) shape and registering it here.
HANDLERS = {
    "ntrip":   _fetch_ntrip_source,
    "file":    _fetch_file_source,
    "scraped": _fetch_scraped_source,
}


def main() -> int:
    DATA_DIR.mkdir(exist_ok=True)

    # Downstream coupling: stations.json + source_health.json filenames are
    # also listed verbatim in scripts/deploy_pages.ps1's $dataFiles. Adding a
    # new visitor-facing output here requires editing that list too, or the
    # file won't ship to Cloudflare Pages.
    out_path = DATA_DIR / "stations.json"
    existing = load_existing(out_path)
    existing_sources: dict = (existing or {}).get("sources", {})

    fetched: dict[str, dict] = {}
    any_fresh = False

    # Inject prev_last_ok per-endpoint so fetch_source can fall back to the
    # previous run's cache. last_ok is tracked per-network (one stations.json
    # record per network), so all endpoints of a network share one prev value.
    sources_with_meta = [
        {**src,
         "_prev_last_ok": existing_sources.get(src["network_id"], {}).get("last_ok")}
        for src in SOURCES
    ]

    with ThreadPoolExecutor(max_workers=len(sources_with_meta)) as executor:
        futures = {executor.submit(fetch_source, src): src for src in sources_with_meta}
        for future in as_completed(futures):
            sid, result, was_fresh = future.result()
            fetched[sid] = result
            if was_fresh:
                any_fresh = True

    if not any_fresh:
        print("All endpoints failed and no cached data was refreshed; exiting without changes.")
        return 0

    # Merge per-endpoint results into one record per network. Status precedence
    # ok > stale > error: if any endpoint succeeded fresh the network is ok.
    payload_sources = {}
    for net in NETWORKS:
        ep_results = [fetched[_endpoint_id(net, i)]
                      for i in range(len(net["endpoints"]))]
        statuses = [r["status"] for r in ep_results]
        status = "ok" if "ok" in statuses else "stale" if "stale" in statuses else "error"
        fetched_ats = [r["fetched_at"] for r in ep_results if r.get("fetched_at")]
        last_oks = [r["last_ok"] for r in ep_results if r.get("last_ok")]
        # Stations: dedupe by (name, lat, lon) across endpoints.
        seen = set()
        merged_stations = []
        for r in ep_results:
            for s in r["stations"]:
                k = (s["name"], s["lat"], s["lon"])
                if k in seen:
                    continue
                seen.add(k)
                merged_stations.append(s)
        # Primary endpoint provides popup-display fields (host:port shown for
        # any station card; multi-endpoint cases default to endpoint[0]).
        #
        # Schema rule: this dict is the COMPLETE source-record shape in
        # stations.json. Do not add editorial fields (label, region, access,
        # registration, note, country, ...) here — those live in rtk_map.json
        # and are read by index.html via markersById[sid] at render time.
        # Adding them re-introduces dual-write drift the schema was cleaned
        # to eliminate.
        primary = ep_results[0]
        payload_sources[net["id"]] = {
            "url":         primary["url"],
            "credentials": primary.get("credentials"),
            "near":        primary.get("near", False),
            "user":        primary.get("user"),
            "pass":        primary.get("pass"),
            "userNote":    primary.get("userNote"),
            "status":      status,
            "fetched_at":  max(fetched_ats) if fetched_ats else None,
            "last_ok":     max(last_oks) if last_oks else None,
            "stations":    merged_stations,
        }

    # Compare against previous JSON, ignoring the "updated" wall clock so an
    # unchanged station list produces no diff (and therefore no commit).
    # Editorial fields (label/region/access/registration/note) live in
    # data/rtk_map.json and don't drive stations.json regeneration; marker
    # colour is computed downstream from data/color_assignments.json + the
    # PALETTE const in index.html.
    if existing is not None:
        ex_sources = existing.get("sources", {})
        unchanged = (
            all(
                station_fingerprint(ex_sources.get(sid, {}))
                == station_fingerprint(payload_sources[sid])
                for sid in payload_sources
            )
            and set(ex_sources.keys()) == set(payload_sources.keys())
        )
        if unchanged:
            print("Station data unchanged since last run; leaving stations.json untouched.")
            write_stations = False
        else:
            write_stations = True
    else:
        write_stations = True

    # Always write source_health.json so the frontend gets fresh last_ok timestamps
    # on every pipeline run, regardless of whether station data changed. This keeps
    # staleness display accurate to the cron interval (±6 h) without committing the
    # full stations.json unnecessarily.
    health_path = DATA_DIR / "source_health.json"
    health = {
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sources": {
            sid: {
                "last_ok": payload_sources[sid].get("last_ok"),
                "status": payload_sources[sid].get("status"),
            }
            for sid in payload_sources
        },
    }
    _atomic_write_text(health_path, json.dumps(health, indent=2) + "\n")
    print(f"Wrote {health_path}.")

    if not write_stations:
        return 0

    # Data changed — write raw copies (only for sources we fetched fresh) and JSON.
    for sid, data in fetched.items():
        if data["text"] is not None and data["status"] == "ok":
            _atomic_write_text(data["raw_path"], data["text"])

    payload = {
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scope": "free NTRIP sources delivering better than ~50 cm",
        "sources": payload_sources,
        "networks": existing.get("networks", []) if existing else [],
    }
    _atomic_write_text(out_path, json.dumps(payload, indent=2) + "\n")
    total = sum(len(s["stations"]) for s in payload_sources.values())
    print(f"Wrote {out_path} with {total} stations total.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
