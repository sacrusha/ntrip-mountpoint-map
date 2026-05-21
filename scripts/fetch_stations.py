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
import json
import os
import math
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
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
    out = []
    for net in networks:
        for idx, ep in enumerate(net["endpoints"]):
            creds = ep.get("credentials") or {}
            out.append({
                "id":              _endpoint_id(net, idx),
                "network_id":      net["id"],
                "endpoint_idx":    idx,
                "url":             ep["url"],
                "credentials":     ep.get("credentials"),
                "near":            ep.get("near", False),
                "user":            creds.get("user"),
                "pass":            creds.get("pass"),
                "userNote":        creds.get("userNote"),
                "nmea_filter":     ep.get("nmea_filter", True),
                "solution_filter": ep.get("solution_filter", True),
                "vrs_required":    ep.get("vrs_required", False),
            })
    return out


NETWORKS = load_networks()
SOURCES = _flatten_endpoints(NETWORKS)  # legacy flat per-endpoint view


FETCH_TIMEOUT = 5
STALE_GREY_DAYS = 3   # sources offline this long shown as grey dots, excluded from coverage raster
STALE_HIDE_DAYS = 7   # sources offline this long hidden entirely


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
         s.get("vrsRequired", False)]
        for s in source.get("stations", [])
    ]


def fetch_source(src: dict) -> tuple[str, dict, bool]:
    """Fetch and parse a single NTRIP source. Returns (sid, result, was_fresh)."""
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
