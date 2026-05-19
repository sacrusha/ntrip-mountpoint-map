#!/usr/bin/env python3
"""Fetch NTRIP sourcetables, parse them, and write data/stations.json.

Skips the write (and thereby any commit) when the set of parsed stations
is byte-identical to the previous run. If a source fails to fetch, its
previous raw sourcetable on disk is reused so a transient outage does
not wipe known-good data.

Process / SOURCES editing rules: see fetch_stations.proc.md (same dir).
Pipeline context: ../docs/pipeline.md.
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


SOURCES = [
    # Operational-only SOURCES schema. Editorial fields (label, region, access,
    # registration, note, tier, vrs, country) live in data/country_markers.json
    # — joined by id. See docs/networks.md for per-network research detail.
    #
    # color: per-source dot/marker hex; single source of truth here.
    # group: logical key for multi-source families, e.g. "sapos" (optional).
    # credentials: {user, pass} for open-access casters with default creds (optional).
    # near / user / pass / userNote: popup-credential hints (optional).
    # nmea_filter / solution_filter: parse-time override flags (default True).
    {"id": "rtk2go", "url": "http://rtk2go.com:2101/", "color": "#d00000", "credentials": {"user": "(any email address)", "pass": "none"}, "near": True, "pass": "none", "userNote": "your email address", "nmea_filter": False},                                                       # caster tags all physical stations nmea=1; NEAR-xxx caught by solution_filter
    {"id": "centipede", "url": "http://crtk.net:2101/", "color": "#e87500", "credentials": {"user": "centipede", "pass": "centipede"}, "near": True, "user": "centipede", "pass": "centipede"},  # migrated from caster.centipede.fr 2025-03-18
    # Re.M.FVG (Marussi) — Regione Autonoma FVG positioning service. Caster is the Marussi
    # caster, not FReDNet. Renamed from id 'frednet' 2026-05-13 — the previous label
    # mis-attributed Marussi infrastructure to OGS FReDNet. Sourcetable cross-relays
    # 11 OGS_* mounts from the real FReDNet caster at 158.110.30.81:2110.
    {"id": "rem_fvg", "url": "http://gnsscaster.regione.fvg.it:8080/", "color": "#2e6fb0"},
    {"id": "geortk", "url": "http://geortk.jp:2101/", "color": "#1a7a4a", "nmea_filter": False, "solution_filter": False},  # caster tags physical stations nmea=1                                                   # caster tags physical stations solution=1
    # SAPOS — German federal-state RTK networks. Sourcetables publicly readable;
    # RTCM streams require per-Länder registration. Most Länder free; BY €20/yr
    # flat rate for non-agricultural use. Raw TCP (NTRIP 1.0) fallback required.
    {"id": "sapos_SH_HH", "url": "http://www.sapos.geonord.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_NI", "url": "http://www.sapos-ni-ntrip.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_NW", "url": "http://www.sapos-nw-ntrip.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_HE", "url": "http://www.sapos-he-ntrip.de:2101/", "color": "#2d6e6e"},
    # sapos_RP removed 2026-05-07: paid-only state (€120/yr/credential HEPS/GPPS
    # + €100 setup), most restrictive in DE. Surfaced via the paid country
    # marker in data/country_markers.json instead.
    {"id": "sapos_BW", "url": "http://www.sapos-bw-ntrip.de:2101/", "color": "#2d6e6e"},
    # sapos_BY removed 2026-05-20: reclassified status:paid per networks.proc.md
    # (€20/yr non-agricultural since June 2024, free for registered Bavarian
    # farms). Surfaced as paid-affordable marker in data/country_markers.json.
    {"id": "sapos_SN", "url": "http://www.ntrip.sachsen.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_SL", "url": "http://www.sapos-sl-ntrip.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_BE", "url": "http://www.sapos-be-ntrip.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_BB", "url": "http://www.sapos-bb-ntrip.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_MV", "url": "http://www.sapos-mv-ntrip.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_LSA", "url": "http://www.sapos-lsa-ntrip.de:2101/", "color": "#2d6e6e"},
    {"id": "sapos_TH", "url": "http://www.sapos-th-ntrip.de:2101/", "color": "#2d6e6e"},
    # APOS (AT) removed from pipeline — paid for hobbyists; represented by a country_markers.json paid-tier marker.
    {"id": "ergnss", "url": "http://ergnss-ip.ign.es:2101/", "color": "#b05000"},
    {"id": "catnet", "url": "http://catnet-ip.icgc.cat:2101/", "color": "#a00020"},  # CATNET — ICGC Catalonia; separate caster and registration from ERGNSS
    {"id": "ergnss_sptr", "url": "http://ergnss-tr.ign.es:2101/", "color": "#b05000"},  # ERGNSS SPTR — Canary Islands VRS sub-service (CERCANA3M/VRS3M/FKP3M); physical Canary pins on ergnss (ergnss-ip:2101)
    {"id": "renep", "url": "http://193.137.94.71:2101/", "color": "#006b3c", "nmea_filter": False},  # port 2101 = physical single-base RTCM3; 2102 = same + MSM5; 2106/2108 = VRS                                                       # caster tags 39 of 47 physical stations nmea=1; VRS mounts are on separate ports (2106/2108)
    {"id": "auscors", "url": "http://ntrip.data.gnss.ga.gov.au:2101/", "color": "#b8860b", "solution_filter": False},                                                   # caster tags 42 IGS partner stations solution=1; all are physical with fixed coords
    {"id": "positionz", "url": "http://positionz-rt.linz.govt.nz:2101/", "color": "#2e8b57"},
    {"id": "satref", "url": "http://ntrip.geodetic.gov.hk:2101/", "color": "#8b008b"},
    {"id": "mosref", "url": "http://mosref.dscc.gov.mo:2101/", "color": "#8b0057"},
    {"id": "inacors", "url": "http://nrtk.big.go.id:2001/", "color": "#1a5fa0"},  # port 2001, not 2101
    {"id": "thailand_dol", "url": "http://122.155.131.34:2101/", "color": "#cc6600"},  # Central zone IP; other-zone ports unpublished; sourcetable not yet parseable from CI as of 2026-05-13
    {"id": "trignet", "url": "http://trignet.co.za:2101/", "color": "#556b2f"},  # Trimble Ntrip Caster 5.2; ~83 STR entries in 2026-05-12 sourcetable mix single-base (Pret-SB, Ctwn-SB...) with Network RTK clusters (RTKNetWCape, Gauteng, KZN) — migrated single-base → physical-vrs 2026-05-14
    {"id": "ugrf", "url": "http://ugrf.mlhud.go.ug:2101/", "color": "#b07000", "near": True, "userNote": "your registered username"},  # Leica GNSS Spider 7.10.1.168; 38 physical single-base + 6 network mounts; SOURCETABLE 200 OK 2026-05-13
    {"id": "rbmc_ip", "url": "http://gps-ntrip.ibge.gov.br:2101/", "color": "#008b8b"},
    {"id": "ramsac", "url": "http://ntrip.ign.gob.ar:2101/", "color": "#7b3f9e"},
    {"id": "regna_rou", "url": "http://rtk.igm.gub.uy:2101/", "color": "#1a9e5c"},
    {"id": "flepos", "url": "http://flepos.vlaanderen.be:2101/", "color": "#3a7ca5"},  # ntrip.flepos.be NXDOMAIN as of 2026-04
    {"id": "walcors", "url": "http://gnss.wallonie.be:8081/", "color": "#1e88c7"},  # port 8081 confirmed 2026-05-06; port 2101 not used
    {"id": "spslux", "url": "http://stream.spslux.lu:5005/", "color": "#5c6bc0"},  # port 5005, not 2101
    {"id": "asg_eupos", "url": "http://system.asgeupos.pl:2101/", "color": "#7b5ea7"},
    {"id": "cropos", "url": "http://gnss.cropos.hr:2101/", "color": "#c0392b"},
{"id": "latpos", "url": "http://latpos.lgia.gov.lv:5001/", "color": "#1a6b3c"},  # port 5001 confirmed SOURCETABLE 200 OK 2026-05-06; may timeout on blocked egress firewalls
    {"id": "litpos", "url": "http://193.219.10.2:2101/", "color": "#0d47a1"},  # bare IP — no DNS hostname published; VilniusTech/GIS-Centras primary
    {"id": "estpos", "url": "http://gnss-rtk.maaamet.ee:8083/", "color": "#003580"},  # free until 31 Aug 2026 per Maa- ja Ruumiamet directive; possible geo-IP filter — monitor
    {"id": "igac", "url": "http://sbc.igac.gov.co:2102/", "color": "#d4a017", "nmea_filter": False},  # :2101 is VRS-only; :2102 has physical stations (nmea=1 mislabelled)
    {"id": "earthscope", "url": "http://ntrip.earthscope.org:2101/", "color": "#8b4513"},
    {"id": "euref_ip", "url": "http://euref-ip.net:2101/", "color": "#1f4e79"},  # BKG broadcaster (primary of the 3-member EUREF-IP federation; ROB + ASI mirror); ~218 STR, ~206 physical EPN stations after solution_filter; all rows NMEA=0; raw 1 Hz RTCM single-base
    {"id": "igs_ip", "url": "http://www.igs-ip.net:2101/", "color": "#7d3c98"},  # BKG-operated global IGS observation caster; same BKG account as EUREF-IP; raw 1 Hz RTCM single-base
    {"id": "mirai", "url": "http://ntrip.go.gnss.go.jp:2101/", "color": "#2471a3"},
    {"id": "cors_korea", "url": "http://www.gnssdata.or.kr:2101/", "color": "#a93226"},  # Network 1 — GNSS Data Center; aggregates 8 KR agencies (NGII, KASI, SMG, etc.); email reg only; no Korean ID; NTRIP password literal "gnss"; 167 unique base codes / 546 STR rows / 493 parsed mountpoints (2026-05-08)
    {"id": "almgg_mn", "url": "http://rtk.gazar.gov.mn:2101/", "color": "#9e6b00", "credentials": {"user": "rover", "pass": "262461"}, "solution_filter": False},  # MonPOS; SNIP R3.14; alt IP 66.181.168.80:2101; curl-confirmed 2026-04-30                                                   # caster tags 6 physical stations solution=1
    {"id": "icecors", "url": "http://178.19.53.126:2101/", "color": "#1e6b8c", "nmea_filter": False},                                                   # GNSMART tags 4 physical Reykjanes mounts (AUSV/GEVK/SENG/VOGC) nmea=1, solution=0
    {"id": "ksa_cors", "url": "http://ksacors.geoportal.sa:2101/", "color": "#a0522d"},
    # Italy — regional networks
    {"id": "spin3", "url": "http://158.102.7.10:2101/", "color": "#1565c0"},  # bare IP; spingnss.it hostname times out; IP confirmed SOURCETABLE 200 OK 2026-05-07
    {"id": "gpsumbria", "url": "http://gpsumbria.regione.umbria.it:2101/", "color": "#2e7d32"},
    {"id": "sit_puglia", "url": "http://gps.sit.puglia.it:2101/", "color": "#0288d1"},
    {"id": "gnss_campania", "url": "http://gps.sit.regione.campania.it:2101/", "color": "#6a1b9a", "credentials": {"user": "Campania", "pass": "GNSS"}},  # public creds: user=Campania pass=GNSS (30-sec VRS); 1-sec requires SPID
    {"id": "tpos", "url": "http://194.105.50.232:2101/", "color": "#00695c"},  # bare IP; tpos.provincia.tn.it is portal domain, does not resolve as NTRIP caster
    {"id": "stpos", "url": "http://62.101.0.40:2109/", "color": "#ad1457"},  # SOURCETABLE 200 OK on port 2109; port 2101 refused; domain www.stpos.it
    {"id": "gnss_veneto", "url": "http://147.162.229.53:2101/", "color": "#4527a0"},
    {"id": "gnss_liguria", "url": "http://81.23.86.70:2101/", "color": "#0277bd"},
    {"id": "sicilianet", "url": "http://193.206.223.39:2101/", "color": "#e65100"},
    {"id": "gnss_abruzzo_lazio", "url": "http://gnss-rtk.regione.abruzzo.it:2101/", "color": "#c62828"},  # times out from external IPs (firewalled); service confirmed operational via portal HTTP 200; add 2026-05-13
    # US state DOT / CORS networks — physical-coordinate stations
    {"id": "acorn", "url": "http://www.acorn-gnss.net:2101/", "color": "#2e5b8a"},  # Trimble Pivot Web; anonymous sourcetable exposes VRS + MS_RTCM3 (nearest single-base) + named VRS solutions
    {"id": "nps_cors", "url": "http://rtk.nps.gov:2101/", "color": "#4a7c59", "nmea_filter": False},  # Trimble Pivot tags all 141 physical stations nmea=1
    {"id": "wiscors", "url": "http://wiscors.dot.wi.gov:2101/", "color": "#bf360c"},
    {"id": "fprn", "url": "http://www.myfloridagps.com:10000/", "color": "#f57f17"},  # port 10000 (Leica); standard 2101 not used
    {"id": "ardot_rtn", "url": "http://gps.ardot.gov:2101/", "color": "#827717"},
{"id": "vector", "url": "http://vector.vermont.gov:2101/", "color": "#1b5e20"},  # VTrans Geodetic Survey; canonical hostname (resolves to 20.185.11.35)
{"id": "gcgc_rtn", "url": "http://rtn.usm.edu:2101/", "color": "#01579b"},
{"id": "orgn", "url": "http://orgn.odot.state.or.us:9881/", "color": "#004d40"},  # hostname; port 9881 (Leica); SOURCETABLE 200 OK 2026-05-13 (6 STR)
    {"id": "msrn", "url": "http://mdotcors.michigan.gov:10010/", "color": "#006064"},  # port 10010 free RTCM3 MSM4 (per MSRN Port Scheme); 10011 = CMRx
{"id": "ct_acorn", "url": "http://acorn.uconn.edu:2101/", "color": "#1a237e"},  # SOURCETABLE 200 OK 2026-05-13 (48 STR)
    {"id": "macors", "url": "http://macorsrtk.massdot.state.ma.us:2101/", "color": "#283593"},  # MassDOT Leica SpiderNet; port 2101 firewalled from external probes — account-gated; add 2026-05-13
    {"id": "nysnet", "url": "http://rtn.dot.ny.gov:8080/", "color": "#0d47a1"},  # NYSDOT Leica SpiderNet; port 8080 confirmed SOURCETABLE 200 OK 2026-05-13 (18 STR); port 2101 firewalled; add 2026-05-13
    {"id": "alcors", "url": "http://aldotcors.dot.state.al.us:10099/", "color": "#1565c0"},  # ALDOT Leica SBC; port 10099 = physical single-base (158 STR confirmed 2026-05-13); port 10011 = network mounts; port 2101 firewalled; add 2026-05-13
    {"id": "iartn", "url": "http://165.206.203.10:10000/", "color": "#37474f"},  # bare IP:port; iartnsbc.iowadot.gov:2101 dead 2026-05-07; sourcetable open, per-station streams require credentials (Emlid/DJI flow documented at e38surveysolutions.com)
    # US state DOT — VRS-only (filter_vrs drops all pins; shown as stopgap circles)
    {"id": "kycors", "url": "http://kycors.ky.gov:2101/", "color": "#546e7a"},
    {"id": "mncors", "url": "http://mncors.dot.state.mn.us:9000/", "color": "#455a64"},  # port 9000; VRS-only
    {"id": "odot_rtn", "url": "http://156.63.133.115:2101/", "color": "#607d8b"},  # bare IP; VRS-only
    {"id": "modot_rtn", "url": "http://rtk3.modot.mo.gov:2101/", "color": "#78909c"},  # VRS-only; notarized agreement
    {"id": "wvrtn", "url": "http://wvrtn.cors.us:2101/", "color": "#90a4ae"},  # VRS-only
    {"id": "mainedot", "url": "http://medotrtn.maine.gov:2101/", "color": "#b0bec5"},  # VRS-only; migrated from mdotcors.maine.gov Oct 2025
    {"id": "azcors", "url": "http://azcors.azwater.gov:2101/", "color": "#c2692e"},  # Arizona CORS; ADWR (Arizona Dept of Water Resources); pipeline-access: registration
    {"id": "mesa_rtvrn", "url": "http://rtvrn.mesacounty.us:2101/", "color": "#8d6e63"},  # VRS-only; western Colorado
    {"id": "agrs_nl", "url": "http://ntrip.kadaster.nl:2101/", "color": "#0288d1"},                            # free, anonymous; covers NL mainland + BES islands
    {"id": "regme_ec", "url": "http://ntrip.igm.gob.ec:2101/", "color": "#558b2f"},
    {"id": "ign_cr_cors", "url": "http://igncaster.snitcr.go.cr:2101/", "color": "#1b7837"},  # BKG NtripCaster 2.0.44; SOURCETABLE 200 OK 2026-05-12; 14 physical stations; SNIT account required
]
# RTKdata.online removed 2026-04-20: server unreachable since launch (RemoteDisconnected);
# 0 stations ever collected. Operated by Kansi Solutions GmbH (same parent as paid
# rtkdata.com); aggregates rtk2go/Centipede visually — no independent value.
# GEODNET (HYFIX.AI) removed 2026-04-20: paid service ($40/month); sourcetable is
# publicly readable but returns 0 free stations after filter. Not in scope.

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
                      solution_filter: bool = True) -> tuple[list[dict], dict]:
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
        stations.append({
            "name": name,
            "lat": lat,
            "lon": lon,
            "latPrec": _dec_places(lat_str),
            "lonPrec": _dec_places(lon_str),
            "dualFreq": carrier >= 2,
            "tripleFreq": carrier >= 3,
            "format": fmt,
            "constellations": nav_sys,
            "country": country,
        })
    stations.sort(key=lambda s: (s["name"], s["lat"], s["lon"]))
    stats = {"kept": len(stations), "dropped_dgnss": dropped_dgnss,
             "dropped_net": dropped_net, "dropped_bad": dropped_bad}
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
         s.get("dualFreq"), s.get("tripleFreq"), s.get("format", ""), s.get("constellations", "")]
        for s in source.get("stations", [])
    ]


def fetch_source(src: dict) -> tuple[str, dict, bool]:
    """Fetch and parse a single NTRIP source. Returns (sid, result, was_fresh)."""
    sid, url = src["id"], src["url"]
    color = src.get("color", "")
    src_credentials = src.get("credentials")
    prev_last_ok = src.get("_prev_last_ok")
    nmea_filter = src.get("nmea_filter", True)
    solution_filter = src.get("solution_filter", True)
    raw_path = DATA_DIR / f"{sid}.sourcetable"
    _meta = {
        "url": url, "color": color,
        "credentials": src_credentials,
        "near": src.get("near", False),
        "user": src.get("user"),
        "pass": src.get("pass"),
        "userNote": src.get("userNote"),
    }
    try:
        text = fetch(url)
        stations, stats = parse_sourcetable(text, nmea_filter=nmea_filter, solution_filter=solution_filter)
        stations, dropped_vrs = filter_vrs(stations)
        net_note = f", {stats['dropped_net']} net-sol" if stats["dropped_net"] else ""
        vrs_note = f", {dropped_vrs} VRS" if dropped_vrs else ""
        now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
        print(f"[{sid}] fetched {len(stations)} stations "
              f"(dropped {stats['dropped_dgnss']} DGNSS, {stats['dropped_bad']} invalid{net_note}{vrs_note})")
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
                stations, stats = parse_sourcetable(text, nmea_filter=nmea_filter, solution_filter=solution_filter)
                stations, dropped_vrs = filter_vrs(stations)
                net_note = f", {stats['dropped_net']} net-sol" if stats["dropped_net"] else ""
                vrs_note = f", {dropped_vrs} VRS" if dropped_vrs else ""
                print(f"[{sid}] reusing cached sourcetable ({len(stations)} stations{net_note}{vrs_note})")
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

    # Inject prev_last_ok so fetch_source can propagate staleness across runs.
    sources_with_meta = [
        {**src, "_prev_last_ok": existing_sources.get(src["id"], {}).get("last_ok")}
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
        print("All sources failed and no cached data was refreshed; exiting without changes.")
        return 0

    payload_sources = {}
    for sid, data in fetched.items():
        payload_sources[sid] = {
            "url": data["url"],
            "color": data.get("color", ""),
            "credentials": data.get("credentials"),
            "near": data.get("near", False),
            "user": data.get("user"),
            "pass": data.get("pass"),
            "userNote": data.get("userNote"),
            "status": data["status"],
            "fetched_at": data["fetched_at"],
            "last_ok": data.get("last_ok"),
            "stations": data["stations"],
        }

    # Compare against previous JSON, ignoring the "updated" wall clock so an
    # unchanged station list produces no diff (and therefore no commit).
    # Source-level color is included so that editing SOURCES in this file
    # triggers a re-write on the next pipeline run without requiring a station
    # change. Editorial fields (label/region/access/registration/note) live in
    # data/country_markers.json and don't drive stations.json regeneration.
    if existing is not None:
        ex_sources = existing.get("sources", {})
        unchanged = (
            all(
                station_fingerprint(ex_sources.get(sid, {}))
                == station_fingerprint(payload_sources[sid])
                and ex_sources.get(sid, {}).get("color") == payload_sources[sid].get("color")
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
