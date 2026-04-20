#!/usr/bin/env python3
"""Fetch NTRIP sourcetables, parse them, and write data/stations.json.

Skips the write (and thereby any commit) when the set of parsed stations
is byte-identical to the previous run. If a source fails to fetch, its
previous raw sourcetable on disk is reused so a transient outage does
not wipe known-good data.
"""
from __future__ import annotations

import http.client
import json
import math
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

SOURCES = [
    # registration: URL shown in the map popup as a clickable "Sign up" link.
    # None = no account needed (open access).
    # See docs/networks.md for per-source detail.
    {"id": "rtk2go",      "url": "http://rtk2go.com:2101/",
     "registration": None},                                                    # open; username=any email, pass=none
    {"id": "centipede",   "url": "http://crtk.net:2101/",                     # migrated from caster.centipede.fr 2025-03-18
     "registration": None},                                                    # open; user=centipede pass=centipede
    {"id": "frednet",     "url": "http://gnsscaster.regione.fvg.it:8080/",
     "registration": "https://frednet.crs.ogs.it/"},                          # free email registration
    {"id": "geortk",      "url": "http://geortk.jp:2101/",
     "registration": None},                                                    # open; no auth
    # SAPOS — German federal-state RTK networks. Sourcetables publicly readable;
    # RTCM streams require per-Länder registration. Most Länder free; BY €20/yr
    # flat rate for non-agricultural use. Raw TCP (NTRIP 1.0) fallback required.
    {"id": "sapos_SH_HH", "url": "http://www.sapos.geonord.de:2101/",        # Schleswig-Holstein + Hamburg
     "registration": "https://www.sapos.de"},
    {"id": "sapos_NI",    "url": "http://www.sapos-ni-ntrip.de:2101/",       # Niedersachsen (incl. Bremen)
     "registration": "https://www.sapos.de"},
    {"id": "sapos_NW",    "url": "http://www.sapos-nw-ntrip.de:2101/",       # Nordrhein-Westfalen
     "registration": "https://www.sapos.de"},
    {"id": "sapos_HE",    "url": "http://www.sapos-he-ntrip.de:2101/",       # Hessen
     "registration": "https://www.sapos.de"},
    {"id": "sapos_RP",    "url": "http://www.sapos-ntrip.rlp.de:2101/",      # Rheinland-Pfalz; confirmed free (LVermGeo)
     "registration": "https://www.sapos.de"},
    {"id": "sapos_BW",    "url": "http://www.sapos-bw-ntrip.de:2101/",       # Baden-Württemberg
     "registration": "https://www.sapos.de"},
    {"id": "sapos_BY",    "url": "http://www.sapos-by-ntrip.de:2101/",       # Bayern (€20/yr non-agri flat rate)
     "registration": "https://www.sapos.de"},
    {"id": "sapos_SN",    "url": "http://ntrip.sachsen.de:2101/",             # Sachsen (GeoSN)
     "registration": "https://www.sapos.de"},
    {"id": "sapos_SL",    "url": "http://www.sapos-sl-ntrip.de:2101/",       # Saarland
     "registration": "https://www.sapos.de"},
    {"id": "sapos_BE",    "url": "http://www.sapos-be-ntrip.de:2101/",       # Berlin
     "registration": "https://www.sapos.de"},
    {"id": "sapos_BB",    "url": "http://www.sapos-bb-ntrip.de:2101/",       # Brandenburg
     "registration": "https://www.sapos.de"},
    {"id": "sapos_MV",    "url": "http://www.sapos-mv-ntrip.de:2101/",       # Mecklenburg-Vorpommern
     "registration": "https://www.sapos.de"},
    {"id": "sapos_LSA",   "url": "http://www.sapos-lsa-ntrip.de:2101/",      # Sachsen-Anhalt
     "registration": "https://www.sapos.de"},
    {"id": "sapos_TH",    "url": "http://www.sapos-th-ntrip.de:2101/",       # Thüringen
     "registration": "https://www.sapos.de"},
    {"id": "ergnss",      "url": "http://ergnss-ip.ign.es:2101/",
     "registration": "https://ergnss.ign.es/gnuserportal/"},                  # free, immediate; attribute IGN
    {"id": "auscors",     "url": "http://ntrip.data.gnss.ga.gov.au:2101/",
     "registration": "https://gnss.ga.gov.au/registration"},                  # CC BY 4.0
    {"id": "positionz",   "url": "http://positionz-rt.linz.govt.nz:2101/",
     "registration": "https://www.linz.govt.nz/"},                            # LINZ account; CC BY 4.0 NZ
    {"id": "satref",      "url": "http://ntrip.geodetic.gov.hk:2101/",
     "registration": "https://www.geodetic.gov.hk/"},                         # mountpoint VRS32G; open data
    {"id": "inacors",     "url": "http://nrtk.big.go.id:2001/",               # NOTE: port 2001, not 2101
     "registration": "https://nrtk.big.go.id"},
    {"id": "trignet",     "url": "http://trignet.co.za:2101/",
     "registration": "https://www.trignet.co.za"},
    {"id": "rbmc_ip",     "url": "http://gps-ntrip.ibge.gov.br:2101/",
     "registration": "https://gps-ntrip.ibge.gov.br"},                        # gov.br signup; 5-station limit
    {"id": "ramsac",      "url": "http://ntrip.ign.gob.ar:2101/",
     "registration": "https://www.ign.gob.ar"},                               # 8-hr session cap
    {"id": "flepos",      "url": "http://flepos.vlaanderen.be:2101/",         # ntrip.flepos.be NXDOMAIN as of 2026-04
     "registration": "https://flepos.vlaanderen.be"},
    {"id": "walcors",     "url": "http://gnss.wallonie.be:2101/",
     "registration": "https://gnss.wallonie.be"},
    {"id": "spslux",      "url": "http://stream.spslux.lu:5005/",             # NOTE: port 5005, not 2101
     "registration": "https://www.spslux.lu/SBC/Account/Register"},
    {"id": "asg_eupos",   "url": "http://system.asgeupos.pl:2101/",
     "registration": "https://system.asgeupos.pl"},                           # admin approval 1–2 working days
    {"id": "cropos",      "url": "http://gnss.cropos.hr:2101/",
     "registration": "https://www.cropos.hr"},
    {"id": "estpos",      "url": "http://gnss-rtk.maaamet.ee:8083/",          # NOTE: port 8083; free until Aug 2026
     "registration": "https://geoportaal.maaamet.ee"},
    {"id": "latpos",      "url": "http://latpos.lgia.gov.lv:5001/",           # NOTE: port 5001, not 2101
     "registration": "https://latpos.lgia.gov.lv/SBC"},
    {"id": "igac",        "url": "http://sbc.igac.gov.co:2101/",
     "registration": "https://redgeodesica-sbc.igac.gov.co/sbc"},
    {"id": "earthscope",  "url": "http://ntrip.earthscope.org:2101/",
     "registration": "https://www.earthscope.org/data/gnss-realtime/"},       # non-commercial NULA; annual renewal
    {"id": "mirai",       "url": "http://ntrip.go.gnss.go.jp:2101/",
     "registration": "https://go.gnss.go.jp"},                                # + separate NtripCaster auth form
    {"id": "cors_korea",  "url": "http://www.gnssdata.or.kr:2101/",
     "registration": "https://www.gnssdata.or.kr"},                           # Korean portal; national ID may be required
    {"id": "icecors",     "url": "http://178.19.53.126:2101/",
     "registration": "https://www.natt.is/is/landmaelingar/jardstodvakerfi"},
    {"id": "ksa_cors",    "url": "http://ksacors.geoportal.sa:2101/",
     "registration": "https://ksacors.geoportal.sa"},                         # old gcs.gov.sa domain is NXDOMAIN
    # GEODNET (HYFIX.AI): paid; $40/month. Testing whether sourcetable is publicly
    # readable without auth. If stations returned, display as paid-service layer.
    {"id": "geodnet_usa", "url": "http://rtk.geodnet.com:2101/",    "registration": None},
    {"id": "geodnet_eu",  "url": "http://eu.geodnet.com:2101/",     "registration": None},
    {"id": "geodnet_aus", "url": "http://aus.geodnet.com:2101/",    "registration": None},
    {"id": "geodnet_sa",  "url": "http://sa.geodnet.com:2101/",     "registration": None},
]
# RTKdata.online removed 2026-04-20: server unreachable since launch (RemoteDisconnected);
# 0 stations ever collected. Operated by Kansi Solutions GmbH (same parent as paid
# rtkdata.com); aggregates rtk2go/Centipede visually — no independent value.

FETCH_TIMEOUT = 60


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
        if not (math.isfinite(lat) and math.isfinite(lon)):
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
        [s["name"], s["latStr"], s["lonStr"], s.get("carrier"), s.get("format", "")]
        for s in source.get("stations", [])
    ]


def main() -> int:
    DATA_DIR.mkdir(exist_ok=True)

    fetched: dict[str, dict] = {}
    any_fresh = False

    for src in SOURCES:
        sid, url = src["id"], src["url"]
        registration = src.get("registration")
        raw_path = DATA_DIR / f"{sid}.sourcetable"
        try:
            text = fetch(url)
            any_fresh = True
            fetched[sid] = {
                "url": url,
                "registration": registration,
                "status": "ok",
                "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "raw_path": raw_path,
                "text": text,
                "stations": None,
            }
            stations, stats = parse_sourcetable(text)
            stations, dropped_vrs = filter_vrs(stations)
            fetched[sid]["stations"] = stations
            fetched[sid]["parse_stats"] = stats
            vrs_note = f", {dropped_vrs} VRS" if dropped_vrs else ""
            print(f"[{sid}] fetched {len(stations)} stations "
                  f"(dropped {stats['dropped_dgnss']} DGNSS, {stats['dropped_bad']} invalid{vrs_note})")
        except Exception as e:
            print(f"[{sid}] fetch failed: {e!r}", file=sys.stderr)
            if raw_path.exists():
                text = raw_path.read_text()
                stations, stats = parse_sourcetable(text)
                stations, dropped_vrs = filter_vrs(stations)
                fetched[sid] = {
                    "url": url,
                    "registration": registration,
                    "status": f"stale (fetch failed: {e!r})",
                    "fetched_at": None,
                    "raw_path": raw_path,
                    "text": text,
                    "stations": stations,
                    "parse_stats": stats,
                }
                vrs_note = f", {dropped_vrs} VRS" if dropped_vrs else ""
                print(f"[{sid}] reusing cached sourcetable ({len(stations)} stations{vrs_note})")
            else:
                fetched[sid] = {
                    "url": url,
                    "registration": registration,
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
            "registration": data.get("registration"),
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
