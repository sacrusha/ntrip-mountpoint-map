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
    {"id": "rtk2go",        "url": "http://rtk2go.com:2101/"},
    {"id": "centipede",     "url": "http://crtk.net:2101/"},        # migrated from caster.centipede.fr 2025-03-18
    # FReDNet (OGS, Italy — north-east): confirmed free, no registration.
    {"id": "frednet",       "url": "http://gnsscaster.regione.fvg.it:8080/"},
    # GeoRTK (Geosense, Japan): free indefinitely (1-yr advance notice if changed).
    # ~338 STR lines; ~200 have valid coords (rest report 0/0 — dropped by parser).
    {"id": "geortk",        "url": "http://geortk.jp:2101/"},
    # SAPOS — German federal-state RTK networks. Sourcetables are publicly readable;
    # RTCM streams require per-Länder registration (most free, BY ~€20/yr, RP paid).
    # SN (Sachsen) omitted — endpoint unconfirmed. Fee field per station reveals
    # paid vs free on first run; paid stations stay in data, marked at display layer.
    {"id": "sapos_SH_HH",   "url": "http://www.sapos.geonord.de:2101/"},     # Schleswig-Holstein + Hamburg
    {"id": "sapos_NI",      "url": "http://www.sapos-ni-ntrip.de:2101/"},    # Niedersachsen (incl. Bremen)
    {"id": "sapos_NW",      "url": "http://www.sapos-nw-ntrip.de:2101/"},    # Nordrhein-Westfalen
    {"id": "sapos_HE",      "url": "http://www.sapos-he-ntrip.de:2101/"},    # Hessen
    {"id": "sapos_RP",      "url": "http://www.sapos-ntrip.rlp.de:2101/"},   # Rheinland-Pfalz
    {"id": "sapos_BW",      "url": "http://www.sapos-bw-ntrip.de:2101/"},    # Baden-Württemberg
    {"id": "sapos_BY",      "url": "http://www.sapos-by-ntrip.de:2101/"},    # Bayern (~€20/yr)
    {"id": "sapos_SL",      "url": "http://www.sapos-sl-ntrip.de:2101/"},    # Saarland
    {"id": "sapos_BE",      "url": "http://www.sapos-be-ntrip.de:2101/"},    # Berlin
    {"id": "sapos_BB",      "url": "http://www.sapos-bb-ntrip.de:2101/"},    # Brandenburg
    {"id": "sapos_MV",      "url": "http://www.sapos-mv-ntrip.de:2101/"},    # Mecklenburg-Vorpommern
    {"id": "sapos_LSA",     "url": "http://www.sapos-lsa-ntrip.de:2101/"},   # Sachsen-Anhalt
    {"id": "sapos_TH",      "url": "http://www.sapos-th-ntrip.de:2101/"},    # Thüringen
    # ERGNSS (IGN, Spain): ~120 stations, VRS. Free, immediate signup.
    # Rover: ergnss.ign.es/gnuserportal/ — attribute IGN per Orden FOM/2807/2015.
    {"id": "ergnss",        "url": "http://ergnss-ip.ign.es:2101/"},
    # AUSCORS (Geoscience Australia): 700+ stations, single-base. CC BY 4.0.
    # Rover: gnss.ga.gov.au/stream
    {"id": "auscors",       "url": "http://ntrip.data.gnss.ga.gov.au:2101/"},
    # PositioNZ-RT (LINZ, New Zealand): 37 stations, single-base. CC BY 4.0 NZ.
    # Rover: linz.govt.nz account + positionz@linz.govt.nz
    {"id": "positionz",     "url": "http://positionz-rt.linz.govt.nz:2101/"},
    # SatRef (Lands Dept, Hong Kong): 19 stations, VRS. Open data policy.
    # Rover: geodetic@landsd.gov.hk · Mountpoint VRS32G (GPS+GLO+GAL+BDS).
    {"id": "satref",        "url": "http://ntrip.geodetic.gov.hk:2101/"},
    # InaCORS (BIG, Indonesia): 200+ stations, VRS. Free (Law 4/2011 mandate).
    # Rover: nrtk.big.go.id — NOTE: port 2001, not 2101.
    {"id": "inacors",       "url": "http://nrtk.big.go.id:2001/"},
    # TrigNet (NGI/DALRRD, South Africa): 55+ stations. All products free.
    # Rover: trignet.co.za
    {"id": "trignet",       "url": "http://trignet.co.za:2101/"},
    # RBMC-IP (IBGE, Brazil): 150 stations, single-base. Free, gov.br signup.
    # Rover: 5-station limit per user.
    {"id": "rbmc_ip",       "url": "http://gps-ntrip.ibge.gov.br:2101/"},
    # RAMSAC-NTRIP (IGN Argentina): ~69 stations, single-base. Free.
    # Rover: ntrip@ign.gob.ar or ign.gob.ar portal; 8-hr session cap.
    {"id": "ramsac",        "url": "http://ntrip.ign.gob.ar:2101/"},
    # FLEPOS (Flanders, BE): free all uses, 45 stations VRS.
    # Rover: flepos.vlaanderen.be
    {"id": "flepos",      "url": "http://ntrip.flepos.be:2101/"},
    # WALCORS (Wallonia, BE): free for positioning, 23 stations VRS.
    # Rover: gnss.wallonie.be  (gnss@spw.wallonie.be)
    {"id": "walcors",     "url": "http://gnss.wallonie.be:2101/"},
    # SPSLux (Luxembourg): free, VRS. Port 5005 — not 2101.
    # Rover: spslux.lu/SBC/Account/Register (subscribe SPSLUX (N)RTK package)
    {"id": "spslux",      "url": "http://stream.spslux.lu:5005/"},
    # ASG-EUPOS (Poland): free since Oct 2022, 130+ stations VRS.
    # Rover: system.asgeupos.pl  (admin approval 1–2 working days)
    {"id": "asg_eupos",   "url": "http://system.asgeupos.pl:2101/"},
    # CROPOS (Croatia): free since Apr 2022, 35 stations VRS.
    # Rover: cropos.hr  (or dgu@dgu.hr). Caster IP changed Nov 2023.
    {"id": "cropos",      "url": "http://gnss.cropos.hr:2101/"},
    # ESTPOS (Estonia): free until Aug 2026, 40 stations VRS.
    # Rover: geoportaal.maaamet.ee
    {"id": "estpos",      "url": "http://gnss-rtk.maaamet.ee:8083/"},
    # LatPos (Latvia): free since 2018, VRS.
    # Rover: latpos.lgia.gov.lv/SBC
    {"id": "latpos",      "url": "http://latpos.lgia.gov.lv:2101/"},
    # IGAC MAGNA-ECO (Colombia): free (law-mandated), 233 stations VRS.
    # Rover: redgeodesica-sbc.igac.gov.co/sbc
    {"id": "igac",        "url": "http://sbc.igac.gov.co:2101/"},
    # EarthScope NOTA (USA/Americas): ~1000 stations; non-commercial NULA.
    # Rover: earthscope.org/data/gnss-realtime/  (annual renewal)
    {"id": "earthscope",  "url": "http://ntrip.earthscope.org:2101/"},
    # MIRAI/Go!GNSS (Japan): free incl. commercial + automated, 300+ stations.
    # Rover: go.gnss.go.jp  (+ separate NtripCaster authorization form)
    {"id": "mirai",       "url": "http://ntrip.go.gnss.go.jp:2101/"},
    # CORS-KOREA (South Korea): free, ~100 stations VRS+FKP.
    # Rover: gnssdata.or.kr  (Korean-only portal; national ID may be required)
    {"id": "cors_korea",  "url": "http://www.gnssdata.or.kr:2101/"},
    # KSA-CORS (Saudi Arabia): free, 209 stations VRS.
    # Rover: ksacors.gcs.gov.sa/RegisterAccount.aspx  (email signed form to info@geosa.gov.sa)
    {"id": "ksa_cors",    "url": "http://KSACORS.gcs.gov.sa:2101/"},
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
        except Exception as e:
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
