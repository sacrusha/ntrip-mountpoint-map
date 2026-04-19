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
    {"id": "rtk2go",    "url": "http://rtk2go.com:2101/"},
    {"id": "centipede", "url": "http://caster.centipede.fr:2101/"},
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


def parse_sourcetable(text: str) -> list[dict]:
    stations: list[dict] = []
    for line in text.splitlines():
        if not line.startswith("STR;"):
            continue
        fields = line.split(";")
        if len(fields) < 11:
            continue
        name = fields[1].strip()
        lat_str = fields[9].strip()
        lon_str = fields[10].strip()
        try:
            lat = float(lat_str)
            lon = float(lon_str)
        except ValueError:
            continue
        if lat == 0 and lon == 0:
            continue
        stations.append({
            "name": name,
            "lat": lat,
            "lon": lon,
            "latStr": lat_str,
            "lonStr": lon_str,
        })
    stations.sort(key=lambda s: (s["name"], s["latStr"], s["lonStr"]))
    return stations


def load_existing(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return None


def station_fingerprint(source: dict) -> list[list[str]]:
    return [
        [s["name"], s["latStr"], s["lonStr"]]
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
                "stations": parse_sourcetable(text),
            }
            print(f"[{sid}] fetched {len(fetched[sid]['stations'])} stations")
        except (URLError, socket.timeout, OSError, TimeoutError) as e:
            print(f"[{sid}] fetch failed: {e!r}", file=sys.stderr)
            if raw_path.exists():
                text = raw_path.read_text()
                fetched[sid] = {
                    "url": url,
                    "status": f"stale (fetch failed: {e!r})",
                    "fetched_at": None,
                    "raw_path": raw_path,
                    "text": text,
                    "stations": parse_sourcetable(text),
                }
                print(f"[{sid}] reusing cached sourcetable ({len(fetched[sid]['stations'])} stations)")
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
        "sources": payload_sources,
    }
    out_path.write_text(json.dumps(payload, indent=2) + "\n")
    total = sum(len(s["stations"]) for s in payload_sources.values())
    print(f"Wrote {out_path} with {total} stations total.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
