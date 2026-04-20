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
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

SOURCES = [
    # access: "open"        = connect immediately, no account needed
    #         "registration" = free for everyone; sign up required
    #         "conditions"   = free but may not apply to you (national ID,
    #                          non-commercial only, fee for some uses, expiring)
    # registration: URL shown in the map popup as a clickable "Sign up" link.
    # None = no account needed (open access).
    # color/label: consumed by the frontend; single source of truth here.
    # See docs/networks.md for per-source detail.
    {"id": "rtk2go",      "url": "http://rtk2go.com:2101/",
     "color": "#d00000", "label": "rtk2go",
     "access": "open",         "registration": None},                            # username=any email, pass=none
    {"id": "centipede",   "url": "http://crtk.net:2101/",                       # migrated from caster.centipede.fr 2025-03-18
     "color": "#e87500", "label": "Centipede",
     "access": "open",         "registration": None},                            # user=centipede pass=centipede
    {"id": "frednet",     "url": "http://gnsscaster.regione.fvg.it:8080/",
     "color": "#2e6fb0", "label": "FReDNet",
     "access": "registration", "registration": "https://frednet.crs.ogs.it/"},  # free email registration
    {"id": "geortk",      "url": "http://geortk.jp:2101/",
     "color": "#1a7a4a", "label": "GeoRTK",
     "access": "open",         "registration": None},                            # no auth
    # SAPOS — German federal-state RTK networks. Sourcetables publicly readable;
    # RTCM streams require per-Länder registration. Most Länder free; BY €20/yr
    # flat rate for non-agricultural use. Raw TCP (NTRIP 1.0) fallback required.
    {"id": "sapos_SH_HH", "url": "http://www.sapos.geonord.de:2101/",          # Schleswig-Holstein + Hamburg
     "color": "#2d6e6e", "label": "SAPOS (Schleswig-Holstein + Hamburg)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_NI",    "url": "http://www.sapos-ni-ntrip.de:2101/",         # Niedersachsen (incl. Bremen)
     "color": "#2d6e6e", "label": "SAPOS (Niedersachsen)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_NW",    "url": "http://www.sapos-nw-ntrip.de:2101/",         # Nordrhein-Westfalen
     "color": "#2d6e6e", "label": "SAPOS (Nordrhein-Westfalen)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_HE",    "url": "http://www.sapos-he-ntrip.de:2101/",         # Hessen
     "color": "#2d6e6e", "label": "SAPOS (Hessen)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_RP",    "url": "http://www.sapos-ntrip.rlp.de:2101/",        # Rheinland-Pfalz; confirmed free (LVermGeo)
     "color": "#2d6e6e", "label": "SAPOS (Rheinland-Pfalz)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_BW",    "url": "http://www.sapos-bw-ntrip.de:2101/",         # Baden-Württemberg
     "color": "#2d6e6e", "label": "SAPOS (Baden-Württemberg)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_BY",    "url": "http://www.sapos-by-ntrip.de:2101/",         # Bayern: free agri, €20/yr otherwise
     "color": "#2d6e6e", "label": "SAPOS (Bayern)",
     "access": "conditions",   "registration": "https://www.sapos.de"},
    {"id": "sapos_SN",    "url": "http://ntrip.sachsen.de:2101/",               # Sachsen (GeoSN)
     "color": "#2d6e6e", "label": "SAPOS (Sachsen)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_SL",    "url": "http://www.sapos-sl-ntrip.de:2101/",         # Saarland
     "color": "#2d6e6e", "label": "SAPOS (Saarland)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_BE",    "url": "http://www.sapos-be-ntrip.de:2101/",         # Berlin
     "color": "#2d6e6e", "label": "SAPOS (Berlin)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_BB",    "url": "http://www.sapos-bb-ntrip.de:2101/",         # Brandenburg
     "color": "#2d6e6e", "label": "SAPOS (Brandenburg)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_MV",    "url": "http://www.sapos-mv-ntrip.de:2101/",         # Mecklenburg-Vorpommern
     "color": "#2d6e6e", "label": "SAPOS (Mecklenburg-Vorpommern)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_LSA",   "url": "http://www.sapos-lsa-ntrip.de:2101/",        # Sachsen-Anhalt
     "color": "#2d6e6e", "label": "SAPOS (Sachsen-Anhalt)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_TH",    "url": "http://www.sapos-th-ntrip.de:2101/",         # Thüringen
     "color": "#2d6e6e", "label": "SAPOS (Thüringen)",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "ergnss",      "url": "http://ergnss-ip.ign.es:2101/",
     "color": "#b05000", "label": "ERGNSS",
     "access": "registration", "registration": "https://ergnss.ign.es/gnuserportal/"},   # free, immediate; attribute IGN
    {"id": "auscors",     "url": "http://ntrip.data.gnss.ga.gov.au:2101/",
     "color": "#b8860b", "label": "AUSCORS",
     "access": "registration", "registration": "https://gnss.ga.gov.au/registration"},   # CC BY 4.0
    {"id": "positionz",   "url": "http://positionz-rt.linz.govt.nz:2101/",
     "color": "#2e8b57", "label": "PositioNZ",
     "access": "registration", "registration": "https://www.linz.govt.nz/"},             # LINZ account; CC BY 4.0 NZ
    {"id": "satref",      "url": "http://ntrip.geodetic.gov.hk:2101/",
     "color": "#8b008b", "label": "SatRef",
     "access": "registration", "registration": "https://www.geodetic.gov.hk/"},          # mountpoint VRS32G; open data
    {"id": "inacors",     "url": "http://nrtk.big.go.id:2001/",                 # NOTE: port 2001, not 2101
     "color": "#1a5fa0", "label": "InaCORS",
     "access": "registration", "registration": "https://nrtk.big.go.id"},
    {"id": "trignet",     "url": "http://trignet.co.za:2101/",
     "color": "#556b2f", "label": "TrigNet",
     "access": "registration", "registration": "https://www.trignet.co.za"},
    {"id": "rbmc_ip",     "url": "http://gps-ntrip.ibge.gov.br:2101/",
     "color": "#008b8b", "label": "RBMC-IP",
     "access": "registration", "registration": "https://gps-ntrip.ibge.gov.br"},         # gov.br signup; 5-station limit
    {"id": "ramsac",      "url": "http://ntrip.ign.gob.ar:2101/",
     "color": "#7b3f9e", "label": "RAMSAC",
     "access": "registration", "registration": "https://www.ign.gob.ar"},                # 8-hr session cap
    {"id": "flepos",      "url": "http://flepos.vlaanderen.be:2101/",           # ntrip.flepos.be NXDOMAIN as of 2026-04
     "color": "#3a7ca5", "label": "FLEPOS",
     "access": "registration", "registration": "https://flepos.vlaanderen.be"},
    {"id": "walcors",     "url": "http://gnss.wallonie.be:2101/",
     "color": "#2c6e8a", "label": "WALCORS",
     "access": "registration", "registration": "https://gnss.wallonie.be"},
    {"id": "spslux",      "url": "http://stream.spslux.lu:5005/",               # NOTE: port 5005, not 2101
     "color": "#5c6bc0", "label": "SPSLux",
     "access": "registration", "registration": "https://www.spslux.lu/SBC/Account/Register"},
    {"id": "asg_eupos",   "url": "http://system.asgeupos.pl:2101/",
     "color": "#7b5ea7", "label": "ASG-EUPOS",
     "access": "registration", "registration": "https://system.asgeupos.pl"},            # admin approval 1–2 working days
    {"id": "cropos",      "url": "http://gnss.cropos.hr:2101/",
     "color": "#c0392b", "label": "CROPOS",
     "access": "registration", "registration": "https://www.cropos.hr"},
    {"id": "estpos",      "url": "http://gnss-rtk.maaamet.ee:8083/",            # NOTE: port 8083; free until Aug 2026
     "color": "#16a085", "label": "ESTPOS",
     "access": "conditions",   "registration": "https://geoportaal.maaamet.ee"},
    {"id": "latpos",      "url": "http://latpos.lgia.gov.lv:5001/",             # NOTE: port 5001, not 2101
     "color": "#1a6b3c", "label": "LatPos",
     "access": "registration", "registration": "https://latpos.lgia.gov.lv/SBC"},
    {"id": "igac",        "url": "http://sbc.igac.gov.co:2101/",
     "color": "#d4a017", "label": "IGAC",
     "access": "registration", "registration": "https://redgeodesica-sbc.igac.gov.co/sbc"},
    {"id": "earthscope",  "url": "http://ntrip.earthscope.org:2101/",
     "color": "#8b4513", "label": "EarthScope",
     "access": "conditions",   "registration": "https://www.earthscope.org/data/gnss-realtime/"},  # non-commercial NULA
    {"id": "mirai",       "url": "http://ntrip.go.gnss.go.jp:2101/",
     "color": "#2471a3", "label": "MIRAI",
     "access": "registration", "registration": "https://go.gnss.go.jp"},                 # + separate NtripCaster auth form
    {"id": "cors_korea",  "url": "http://www.gnssdata.or.kr:2101/",
     "color": "#a93226", "label": "CORS-KOREA",
     "access": "conditions",   "registration": "https://www.gnssdata.or.kr"},            # national ID may be required
    {"id": "icecors",     "url": "http://178.19.53.126:2101/",
     "color": "#1e6b8c", "label": "IceCORS",
     "access": "registration", "registration": "https://www.natt.is/is/landmaelingar/jardstodvakerfi"},
    {"id": "ksa_cors",    "url": "http://ksacors.geoportal.sa:2101/",
     "color": "#a0522d", "label": "KSA-CORS",
     "access": "conditions",   "registration": "https://ksacors.geoportal.sa"},          # old gcs.gov.sa domain is NXDOMAIN
]
# RTKdata.online removed 2026-04-20: server unreachable since launch (RemoteDisconnected);
# 0 stations ever collected. Operated by Kansi Solutions GmbH (same parent as paid
# rtkdata.com); aggregates rtk2go/Centipede visually — no independent value.
# GEODNET (HYFIX.AI) removed 2026-04-20: paid service ($40/month); sourcetable is
# publicly readable but returns 0 free stations after filter. Not in scope.

FETCH_TIMEOUT = 60
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
        stations.append({
            "name": name,
            "lat": lat,
            "lon": lon,
            "latStr": lat_str,
            "lonStr": lon_str,
            "carrier": carrier,
            "format": fmt,
            "legacyFormat": fmt.startswith("RTCM 2"),
            "country": country,
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
        [s["name"], s["lat"], s["latStr"], s["lon"], s["lonStr"], s.get("carrier"), s.get("format", "")]
        for s in source.get("stations", [])
    ]


def fetch_source(src: dict) -> tuple[str, dict, bool]:
    """Fetch and parse a single NTRIP source. Returns (sid, result, was_fresh)."""
    sid, url = src["id"], src["url"]
    registration = src.get("registration")
    access = src.get("access", "registration")
    color = src.get("color", "")
    label = src.get("label", "")
    prev_last_ok = src.get("_prev_last_ok")
    raw_path = DATA_DIR / f"{sid}.sourcetable"
    try:
        text = fetch(url)
        stations, stats = parse_sourcetable(text)
        stations, dropped_vrs = filter_vrs(stations)
        vrs_note = f", {dropped_vrs} VRS" if dropped_vrs else ""
        now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
        print(f"[{sid}] fetched {len(stations)} stations "
              f"(dropped {stats['dropped_dgnss']} DGNSS, {stats['dropped_bad']} invalid{vrs_note})")
        return sid, {
            "url": url,
            "color": color,
            "label": label,
            "registration": registration,
            "access": access,
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
            text = raw_path.read_text()
            stations, stats = parse_sourcetable(text)
            stations, dropped_vrs = filter_vrs(stations)
            vrs_note = f", {dropped_vrs} VRS" if dropped_vrs else ""
            print(f"[{sid}] reusing cached sourcetable ({len(stations)} stations{vrs_note})")
            return sid, {
                "url": url,
                "color": color,
                "label": label,
                "registration": registration,
                "access": access,
                "status": f"stale (fetch failed: {e!r})",
                "fetched_at": None,
                "last_ok": prev_last_ok,
                "raw_path": raw_path,
                "text": text,
                "stations": stations,
                "parse_stats": stats,
            }, False
        return sid, {
            "url": url,
            "color": color,
            "label": label,
            "registration": registration,
            "access": access,
            "status": f"error: {e!r}",
            "fetched_at": None,
            "last_ok": prev_last_ok,
            "raw_path": raw_path,
            "text": None,
            "stations": [],
        }, False


def main() -> int:
    DATA_DIR.mkdir(exist_ok=True)

    out_path = DATA_DIR / "stations.json"
    existing = load_existing(out_path)
    existing_sources: dict = (existing or {}).get("sources", {})

    fetched: dict[str, dict] = {}
    any_fresh = False

    # Inject prev_last_ok so fetch_source can propagate staleness across runs.
    sources_with_meta = [
        {**src, "_prev_last_ok": existing_sources.get(src["id"], {}).get("last_ok")}
        for src in SOURCES
    ]

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(fetch_source, src): src for src in sources_with_meta}
        for future in as_completed(futures):
            sid, result, was_fresh = future.result()
            fetched[sid] = result
            if was_fresh:
                any_fresh = True

    if not any_fresh:
        print("All sources failed and no cached data was refreshed; exiting without changes.")
        return 0

    payload_sources = {}
    for sid, data in fetched.items():
        payload_sources[sid] = {
            "url": data["url"],
            "color": data.get("color", ""),
            "label": data.get("label", ""),
            "registration": data.get("registration"),
            "access": data.get("access", "registration"),
            "status": data["status"],
            "fetched_at": data["fetched_at"],
            "last_ok": data.get("last_ok"),
            "stations": data["stations"],
        }

    # Compare against previous JSON, ignoring the "updated" wall clock so an
    # unchanged station list produces no diff (and therefore no commit).
    # Source metadata (color/label) is included so that editing SOURCES in this
    # file triggers a re-write on the next pipeline run without requiring a
    # station change.
    if existing is not None:
        ex_sources = existing.get("sources", {})
        unchanged = (
            all(
                station_fingerprint(ex_sources.get(sid, {}))
                == station_fingerprint(payload_sources[sid])
                and ex_sources.get(sid, {}).get("color") == payload_sources[sid].get("color")
                and ex_sources.get(sid, {}).get("label") == payload_sources[sid].get("label")
                for sid in payload_sources
            )
            and set(ex_sources.keys()) == set(payload_sources.keys())
        )
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
