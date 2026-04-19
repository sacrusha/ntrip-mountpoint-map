#!/usr/bin/env python3
"""Fetch NTRIP sourcetables, parse them, and write data/stations.json.

Skips the write (and thereby any commit) when the set of parsed stations
is byte-identical to the previous run. If a source fails to fetch, its
previous raw sourcetable on disk is reused so a transient outage does
not wipe known-good data.
"""
from __future__ import annotations

import json
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

SOURCES = [
    {"id": "rtk2go",        "url": "http://rtk2go.com:2101/"},
    {"id": "centipede",     "url": "http://caster.centipede.fr:2101/"},
    # FReDNet (OGS, Italy — north-east): confirmed free, no registration.
    {"id": "frednet",       "url": "http://gnsscaster.regione.fvg.it:8080/"},
    # RTKdata.online: community caster, low-confidence operational status;
    # fetch will be attempted best-effort and fall through on failure.
    {"id": "rtkdataonline", "url": "http://rtkdata.online:2101/"},
]

FETCH_TIMEOUT = 60


def fetch(url: str) -> str:
    req = Request(url, headers={
        "User-Agent": "NTRIP ntrip-mountpoint-map/1.0",
        "Ntrip-Version": "Ntrip/2.0",
        "Accept": "*/*",
    })
    with urlopen(req, timeout=FETCH_TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_sourcetable(text: str) -> tuple[list[dict], dict]:
    """Parse an NTRIP sourcetable.

    NTRIP STR line fields (0-based after splitting on ';'):
      0 STR, 1 mountpoint, 2 identifier, 3 format, 4 format-details,
      5 carrier, 6 nav-system, 7 network, 8 country,
      9 latitude, 10 longitude, 11 nmea, 12 solution, ..., 15 auth, 16 fee.

    Drops DGNSS-only mountpoints (carrier == 0) — out of the site's
    sub-50-cm scope.
    """
    stations: list[dict] = []
    dropped_dgnss = 0
    dropped_bad = 0
    for line in text.splitlines():
        if not line.startswith("STR;"):
            continue
        fields = line.split(";")
        if len(fields) < 11:
            dropped_bad += 1
            continue
        name = fields[1].strip()
        fmt = fields[3].strip() if len(fields) > 3 else ""
        carrier_raw = fields[5].strip() if len(fields) > 5 else ""
        country = fields[8].strip() if len(fields) > 8 else ""
        lat_str = fields[9].strip()
        lon_str = fields[10].strip()
        fee = fields[16].strip().upper() if len(fields) > 16 else ""
        # rtk2go leaves the carrier field blank for most entries even though
        # they broadcast RTCM 3.x carrier-phase observations. Trust the
        # format string as a fallback: RTCM 3.x MSM streams are cm-capable.
        carrier_inferred = False
        if carrier_raw == "":
            if fmt.startswith("RTCM 3"):
                carrier = 2
                carrier_inferred = True
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
        try:
            lat = float(lat_str)
            lon = float(lon_str)
        except ValueError:
            dropped_bad += 1
            continue
        if lat == 0 and lon == 0:
            dropped_bad += 1
            continue
        stations.append({
            "name": name,
            "lat": lat,
            "lon": lon,
            "latStr": lat_str,
            "lonStr": lon_str,
            "carrier": carrier,
            "carrierInferred": carrier_inferred,
            "format": fmt,
            "legacyFormat": fmt.startswith("RTCM 2"),
            "country": country,
            "fee": fee or "N",
        })
    stations.sort(key=lambda s: (s["name"], s["latStr"], s["lonStr"]))
    stats = {"kept": len(stations), "dropped_dgnss": dropped_dgnss, "dropped_bad": dropped_bad}
    return stations, stats


def load_existing(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return None


def station_fingerprint(source: dict) -> list[list]:
    return [
        [s["name"], s["latStr"], s["lonStr"], s.get("carrier"), s.get("format", "")]
        for s in source.get("stations", [])
    ]


def main() -> int:
    DATA_DIR.mkdir(exist_ok=True)

    fetched: dict[str, dict] = {}
    any_fresh = False

    for src in SOURCES:
        sid, url = src["id"], src["url"]
        raw_path = DATA_DIR / f"{sid}.sourcetable"
        try:
            text = fetch(url)
            any_fresh = True
            fetched[sid] = {
                "url": url,
                "status": "ok",
                "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "raw_path": raw_path,
                "text": text,
                "stations": None,
            }
            stations, stats = parse_sourcetable(text)
            fetched[sid]["stations"] = stations
            fetched[sid]["parse_stats"] = stats
            print(f"[{sid}] fetched {stats['kept']} stations "
                  f"(dropped {stats['dropped_dgnss']} DGNSS, {stats['dropped_bad']} invalid)")
        except (URLError, socket.timeout, OSError, TimeoutError) as e:
            print(f"[{sid}] fetch failed: {e!r}", file=sys.stderr)
            if raw_path.exists():
                text = raw_path.read_text()
                stations, stats = parse_sourcetable(text)
                fetched[sid] = {
                    "url": url,
                    "status": f"stale (fetch failed: {e!r})",
                    "fetched_at": None,
                    "raw_path": raw_path,
                    "text": text,
                    "stations": stations,
                    "parse_stats": stats,
                }
                print(f"[{sid}] reusing cached sourcetable ({stats['kept']} stations)")
            else:
                fetched[sid] = {
                    "url": url,
                    "status": f"error: {e!r}",
                    "fetched_at": None,
                    "raw_path": raw_path,
                    "text": None,
                    "stations": [],
                }

    if not any_fresh:
        print("All sources failed and no cached data was refreshed; exiting without changes.")
        return 0

    payload_sources = {}
    for sid, data in fetched.items():
        payload_sources[sid] = {
            "url": data["url"],
            "status": data["status"],
            "fetched_at": data["fetched_at"],
            "stations": data["stations"],
        }

    # Compare against previous JSON, ignoring the "updated" wall clock so an
    # unchanged station list produces no diff (and therefore no commit).
    out_path = DATA_DIR / "stations.json"
    existing = load_existing(out_path)
    if existing is not None:
        unchanged = all(
            station_fingerprint(existing.get("sources", {}).get(sid, {}))
            == station_fingerprint(payload_sources[sid])
            for sid in payload_sources
        ) and set(existing.get("sources", {}).keys()) == set(payload_sources.keys())
        if unchanged:
            print("Station data unchanged since last run; leaving files untouched.")
            return 0

    # Data changed — write raw copies (only for sources we fetched fresh) and JSON.
    for sid, data in fetched.items():
        if data["text"] is not None and data["status"] == "ok":
            data["raw_path"].write_text(data["text"])

    payload = {
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scope": "free NTRIP sources delivering better than ~50 cm",
        "sources": payload_sources,
        "networks": existing.get("networks", []) if existing else [],
    }
    out_path.write_text(json.dumps(payload, indent=2) + "\n")
    total = sum(len(s["stations"]) for s in payload_sources.values())
    print(f"Wrote {out_path} with {total} stations total.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
