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


def _dec_places(s: str) -> int:
    """Decimal places in a coordinate string, used for accuracy-rectangle sizing."""
    dot = s.find('.')
    return 0 if dot == -1 else len(s) - dot - 1


SOURCES = [
    # access: "open"        = connect immediately, no account needed
    #         "registration" = free for everyone; sign up required
    #         "conditions"   = free but may not apply to you (national ID,
    #                          non-commercial only, fee for some uses, expiring)
    # type: "single-base"  = physical antennas, each with a distinct coordinate
    #       "physical-vrs" = physical coords in sourcetable; rover uses VRS/NRTK mounts
    #       "vrs-only"     = sourcetable exposes only virtual/single-coord mountpoints
    # country: list of ISO 3166-1 alpha-2 codes; "global" for volunteer aggregators
    # region: sub-national coverage string (optional)
    # group: logical key for multi-source networks, e.g. "sapos" (optional)
    # credentials: {user, pass} for open-access casters with default creds (optional)
    # registration: URL shown in popup as "Sign up" link. None = no account needed.
    # color/label: consumed by the frontend; single source of truth here.
    # See docs/networks.md for per-source detail.
    {"id": "rtk2go",      "url": "http://rtk2go.com:2101/",
     "color": "#d00000", "label": "rtk2go",
     "type": "single-base", "country": ["global"],
     "credentials": {"user": "(any email address)", "pass": "none"},
     "access": "open",         "registration": None,
     "near": True, "userNote": "your email address", "pass": "none",
     "nmea_filter": False},                                                       # caster tags all physical stations nmea=1; NEAR-xxx caught by solution_filter
    {"id": "centipede",   "url": "http://crtk.net:2101/",                       # migrated from caster.centipede.fr 2025-03-18
     "color": "#e87500", "label": "Centipede",
     "type": "single-base", "country": ["global"],
     "credentials": {"user": "centipede", "pass": "centipede"},
     "access": "open",         "registration": None,
     "near": True, "user": "centipede", "pass": "centipede"},
    # Re.M.FVG (Marussi) — Regione Autonoma FVG positioning service. Caster is the Marussi
    # caster, not FReDNet. Renamed from id 'frednet' 2026-05-13 — the previous label
    # mis-attributed Marussi infrastructure to OGS FReDNet. Sourcetable cross-relays
    # 11 OGS_* mounts from the real FReDNet caster at 158.110.30.81:2110.
    {"id": "rem_fvg",     "url": "http://gnsscaster.regione.fvg.it:8080/",
     "color": "#2e6fb0", "label": "Re.M.FVG",
     "type": "physical-vrs", "country": ["IT"], "region": "Friuli-Venezia Giulia",
     "access": "registration", "registration": "https://rem.regione.fvg.it/rem-fvg/servizi/correzioni-differenziali", "openNote": 'Free registration form required'},
    {"id": "geortk",      "url": "http://geortk.jp:2101/",
     "color": "#1a7a4a", "label": "GeoRTK",
     "type": "single-base", "country": ["JP"],
     "access": "open",         "registration": None,
     "nmea_filter": False,                                                        # caster tags physical stations nmea=1
     "solution_filter": False, "openNote": 'No authentication required'},                                                   # caster tags physical stations solution=1
    # SAPOS — German federal-state RTK networks. Sourcetables publicly readable;
    # RTCM streams require per-Länder registration. Most Länder free; BY €20/yr
    # flat rate for non-agricultural use. Raw TCP (NTRIP 1.0) fallback required.
    {"id": "sapos_SH_HH", "url": "http://www.sapos.geonord.de:2101/",
     "color": "#2d6e6e", "label": "sapos SH HH",
     "type": "vrs-only", "country": ["DE"],
     "region": "Schleswig-Holstein + Hamburg", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_NI",    "url": "http://www.sapos-ni-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos NI",
     "type": "vrs-only", "country": ["DE"],
     "region": "Niedersachsen + Bremen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_NW",    "url": "http://www.sapos-nw-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos NW",
     "type": "vrs-only", "country": ["DE"],
     "region": "Nordrhein-Westfalen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_HE",    "url": "http://www.sapos-he-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos HE",
     "type": "physical-vrs", "country": ["DE"],
     "region": "Hessen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    # sapos_RP removed 2026-05-07: paid-only state (€120/yr/credential HEPS/GPPS
    # + €100 setup), most restrictive in DE. Surfaced via the paid-affordable
    # country marker in data/country_markers.json instead.
    {"id": "sapos_BW",    "url": "http://www.sapos-bw-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos BW",
     "type": "vrs-only", "country": ["DE"],
     "region": "Baden-Württemberg", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_BY",    "url": "http://www.sapos-by-ntrip.de:2101/",          # free agri; €20/yr otherwise
     "color": "#2d6e6e", "label": "sapos BY",
     "type": "vrs-only", "country": ["DE"],
     "region": "Bayern", "group": "sapos",
     "access": "conditions",   "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_SN",    "url": "http://www.ntrip.sachsen.de:2101/",
     "color": "#2d6e6e", "label": "sapos SN",
     "type": "physical-vrs", "country": ["DE"],
     "region": "Sachsen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_SL",    "url": "http://www.sapos-sl-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos SL",
     "type": "physical-vrs", "country": ["DE"],
     "region": "Saarland", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_BE",    "url": "http://www.sapos-be-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos BE",
     "type": "vrs-only", "country": ["DE"],
     "region": "Berlin", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_BB",    "url": "http://www.sapos-bb-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos BB",
     "type": "vrs-only", "country": ["DE"],
     "region": "Brandenburg", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_MV",    "url": "http://www.sapos-mv-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos MV",
     "type": "vrs-only", "country": ["DE"],
     "region": "Mecklenburg-Vorpommern", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_LSA",   "url": "http://www.sapos-lsa-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos LSA",
     "type": "vrs-only", "country": ["DE"],
     "region": "Sachsen-Anhalt", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    {"id": "sapos_TH",    "url": "http://www.sapos-th-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "sapos TH",
     "type": "vrs-only", "country": ["DE"],
     "region": "Thüringen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de", "openNote": 'Free registration required — select your federal state'},
    # APOS (AT) removed from pipeline — paid for hobbyists; represented by a country_markers.json paid-tier marker.
    {"id": "ergnss",      "url": "http://ergnss-ip.ign.es:2101/",
     "color": "#b05000", "label": "ERGNSS",
     "type": "physical-vrs", "country": ["ES"],
     "access": "registration", "registration": "https://ergnss.ign.es/gnuserportal/", "openNote": 'Free registration, approved immediately'},
    {"id": "catnet",      "url": "http://catnet-ip.icgc.cat:2101/",              # CATNET — ICGC Catalonia; separate caster and registration from ERGNSS
     "color": "#a00020", "label": "CATNET",
     "type": "physical-vrs", "country": ["ES"], "region": "Catalonia",
     "access": "registration", "registration": "https://catnet-ip.icgc.cat/", "openNote": 'Free ICGC account required'},
    {"id": "ergnss_sptr", "url": "http://ergnss-tr.ign.es:2101/",               # ERGNSS SPTR — Canary Islands VRS sub-service (CERCANA3M/VRS3M/FKP3M); physical Canary pins on ergnss (ergnss-ip:2101)
     "color": "#b05000", "label": "ERGNSS",
     "type": "vrs-only", "country": ["ES"],
     "access": "registration", "registration": "https://ergnss.ign.es/gnuserportal/", "openNote": 'Free registration, approved immediately (Canary Islands VRS service)'},
    {"id": "renep",       "url": "http://193.137.94.71:2101/",                     # port 2101 = physical single-base RTCM3; 2102 = same + MSM5; 2106/2108 = VRS
     "color": "#006b3c", "label": "ReNEP",
     "type": "single-base", "country": ["PT"],
     "access": "registration", "registration": "https://renep.dgterritorio.gov.pt",
     "nmea_filter": False, "openNote": 'Free registration required (DGT — Direção-Geral do Território)'},                                                       # caster tags 39 of 47 physical stations nmea=1; VRS mounts are on separate ports (2106/2108)
    {"id": "auscors",     "url": "http://ntrip.data.gnss.ga.gov.au:2101/",
     "color": "#b8860b", "label": "AUSCORS",
     "type": "single-base", "country": ["AU"],
     "access": "registration", "registration": "https://gnss.ga.gov.au/registration",
     "solution_filter": False, "openNote": 'Free registration required — CC BY 4.0'},                                                   # caster tags 42 IGS partner stations solution=1; all are physical with fixed coords
    {"id": "positionz",   "url": "http://positionz-rt.linz.govt.nz:2101/",
     "color": "#2e8b57", "label": "PositioNZ",
     "type": "single-base", "country": ["NZ"],
     "access": "registration", "registration": "https://www.linz.govt.nz/", "openNote": 'LINZ account required — CC BY 4.0 NZ'},
    {"id": "satref",      "url": "http://ntrip.geodetic.gov.hk:2101/",
     "color": "#8b008b", "label": "SatRef",
     "type": "single-base", "country": ["HK"],
     "access": "registration", "registration": "https://www.geodetic.gov.hk/en/satref/ntrip.htm", "openNote": 'Free registration required (Survey and Mapping Office application form)'},
    {"id": "mosref",      "url": "http://mosref.dscc.gov.mo:2101/",
     "color": "#8b0057", "label": "MoSRef",
     "type": "physical-vrs", "country": ["MO"],
     "access": "registration", "registration": "https://mosref.dscc.gov.mo", "openNote": 'Free registration required — GPS+GLONASS+BeiDou; single-base and VRS available'},
    {"id": "inacors",     "url": "http://nrtk.big.go.id:2001/",                 # port 2001, not 2101
     "color": "#1a5fa0", "label": "InaCORS",
     "type": "physical-vrs", "country": ["ID"],
     "access": "registration", "registration": "https://nrtk.big.go.id", "openNote": 'Free registration required'},
    {"id": "thailand_dol", "url": "http://122.155.131.34:2101/",                # Central zone IP; other-zone ports unpublished; sourcetable not yet parseable from CI as of 2026-05-13
     "color": "#cc6600", "label": "DOL LandGNSS",
     "type": "physical-vrs", "country": ["TH"],
     "access": "conditions", "registration": "https://dol-rtknetwork.com/index.php/register_gnss_beta",
     "openNote": 'Free trial; Thai national ID required to self-register — foreign users blocked at registration form'},
    {"id": "trignet",     "url": "http://trignet.co.za:2101/",                  # Trimble Ntrip Caster 5.2; ~83 STR entries in 2026-05-12 sourcetable mix single-base (Pret-SB, Ctwn-SB...) with Network RTK clusters (RTKNetWCape, Gauteng, KZN) — migrated single-base → physical-vrs 2026-05-14
     "color": "#556b2f", "label": "TrigNet",
     "type": "physical-vrs", "country": ["ZA"],
     "access": "registration", "registration": "https://www.trignet.co.za", "openNote": 'Free registration required'},
    {"id": "ugrf",        "url": "http://ugrf.mlhud.go.ug:2101/",                   # Leica GNSS Spider 7.10.1.168; 38 physical single-base + 6 network mounts; SOURCETABLE 200 OK 2026-05-13
     "color": "#b07000", "label": "UGRF CORS",
     "type": "physical-vrs", "country": ["UG"],
     "access": "registration", "registration": "https://ugrf.mlhud.go.ug/SBC",
     "near": True, "userNote": "your registered username",
     "openNote": "Free registration required (UGRF portal — MLHUD)"},
    {"id": "rbmc_ip",     "url": "http://gps-ntrip.ibge.gov.br:2101/",
     "color": "#008b8b", "label": "RBMC-IP",
     "type": "single-base", "country": ["BR"],
     "access": "registration", "registration": "https://gps-ntrip.ibge.gov.br", "openNote": 'Free registration required (5-station limit per user)'},
    {"id": "ramsac",      "url": "http://ntrip.ign.gob.ar:2101/",
     "color": "#7b3f9e", "label": "RAMSAC",
     "type": "single-base", "country": ["AR"],
     "access": "registration", "registration": "https://www.ign.gob.ar", "openNote": 'Free registration required (8-hr session cap)'},
    {"id": "regna_rou",   "url": "http://rtk.igm.gub.uy:2101/",
     "color": "#1a9e5c", "label": "REGNA-ROU",
     "type": "physical-vrs", "country": ["UY"],
     "access": "registration", "registration": "https://rtk.igm.gub.uy/SBC/Account/Register", "openNote": 'Free registration required'},
    {"id": "flepos",      "url": "http://flepos.vlaanderen.be:2101/",           # ntrip.flepos.be NXDOMAIN as of 2026-04
     "color": "#3a7ca5", "label": "FLEPOS",
     "type": "vrs-only", "country": ["BE"], "region": "Flanders",
     "access": "registration", "registration": "https://flepos.vlaanderen.be", "openNote": 'Free registration required'},
    {"id": "walcors",     "url": "http://gnss.wallonie.be:8081/",                # port 8081 confirmed 2026-05-06; port 2101 not used
     "color": "#1e88c7", "label": "WALCORS",
     "type": "vrs-only", "country": ["BE"], "region": "Wallonia",
     "access": "registration", "registration": "https://gnss.wallonie.be", "openNote": 'Free registration required'},
    {"id": "spslux",      "url": "http://stream.spslux.lu:5005/",               # port 5005, not 2101
     "color": "#5c6bc0", "label": "SPSLux",
     "type": "physical-vrs", "country": ["LU"],
     "access": "registration", "registration": "https://www.spslux.lu/SBC/Account/Register", "openNote": 'Free registration required'},
    {"id": "asg_eupos",   "url": "http://system.asgeupos.pl:2101/",
     "color": "#7b5ea7", "label": "ASG-EUPOS",
     "type": "vrs-only", "country": ["PL"],
     "access": "registration", "registration": "https://system.asgeupos.pl", "openNote": 'Free registration required (approval 1–2 working days)'},
    {"id": "cropos",      "url": "http://gnss.cropos.hr:2101/",
     "color": "#c0392b", "label": "CROPOS",
     "type": "vrs-only", "country": ["HR"],
     "access": "registration", "registration": "https://www.cropos.hr", "openNote": 'Free registration required'},
{"id": "latpos",      "url": "http://latpos.lgia.gov.lv:5001/",             # port 5001 confirmed SOURCETABLE 200 OK 2026-05-06; may timeout on blocked egress firewalls
     "color": "#1a6b3c", "label": "LatPos",
     "type": "vrs-only", "country": ["LV"],
     "access": "registration", "registration": "https://latpos.lgia.gov.lv/SBC", "openNote": 'Free registration required'},
    {"id": "litpos",      "url": "http://193.219.10.2:2101/",                    # bare IP — no DNS hostname published; VilniusTech/GIS-Centras primary
     "color": "#0d47a1", "label": "LitPOS",
     "type": "vrs-only", "country": ["LT"],
     "access": "registration", "registration": "https://www.geoportal.lt/geoportal/web/litpos-en/registration", "openNote": 'Free registration required'},
    {"id": "estpos",      "url": "http://gnss-rtk.maaamet.ee:8083/",             # free until 31 Aug 2026 per Maa- ja Ruumiamet directive; possible geo-IP filter — monitor
     "color": "#003580", "label": "ESTPOS",
     "type": "vrs-only", "country": ["EE"],
     "access": "conditions",
     "registration": "https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html",
     "openNote": 'Free until 31 Aug 2026; portal account + service agreement required'},
    {"id": "igac",        "url": "http://sbc.igac.gov.co:2102/",               # :2101 is VRS-only; :2102 has physical stations (nmea=1 mislabelled)
     "color": "#d4a017", "label": "IGAC",
     "type": "physical-coord-vrs", "country": ["CO"],
     "nmea_filter": False,
     "access": "registration", "registration": "https://redgeodesica-sbc.igac.gov.co/sbc", "openNote": 'Free registration required'},
    {"id": "earthscope",  "url": "http://ntrip.earthscope.org:2101/",
     "color": "#8b4513", "label": "EarthScope",
     "type": "single-base", "country": ["americas"],
     "access": "conditions",   "registration": "https://www.earthscope.org/data/gnss-realtime/", "openNote": 'Non-commercial annual license (NULA) required'},
    {"id": "euref_ip",    "url": "http://euref-ip.net:2101/",                # BKG broadcaster (primary of the 3-member EUREF-IP federation; ROB + ASI mirror); ~218 STR, ~206 physical EPN stations after solution_filter; all rows NMEA=0; raw 1 Hz RTCM single-base
     "color": "#1f4e79", "label": "EUREF-IP",
     "type": "single-base", "country": ["europe"],
     "access": "registration", "registration": "http://register.rtcm-ntrip.org/cgi-bin/registration.cgi", "openNote": 'Free with BKG registration (per-broadcaster account; no SSO across BKG/ROB/ASI)'},
    {"id": "igs_ip",      "url": "http://www.igs-ip.net:2101/",              # BKG-operated global IGS observation caster; same BKG account as EUREF-IP; raw 1 Hz RTCM single-base
     "color": "#7d3c98", "label": "IGS-IP",
     "type": "single-base", "country": ["global"],
     "access": "registration", "registration": "http://register.rtcm-ntrip.org/cgi-bin/registration.cgi", "openNote": 'Free with BKG registration (shared with EUREF-IP)'},
    {"id": "mirai",       "url": "http://ntrip.go.gnss.go.jp:2101/",
     "color": "#2471a3", "label": "MIRAI",
     "type": "single-base", "country": ["JP"],
     "access": "registration", "registration": "https://go.gnss.go.jp", "openNote": 'Free registration required (+ NtripCaster auth form)'},
    {"id": "cors_korea",  "url": "http://www.gnssdata.or.kr:2101/",             # Network 1 — GNSS Data Center; aggregates 8 KR agencies (NGII, KASI, SMG, etc.); email reg only; no Korean ID; NTRIP password literal "gnss"; 167 unique base codes / 546 STR rows / 493 parsed mountpoints (2026-05-08)
     "color": "#a93226", "label": "CORS-KOREA",
     "type": "single-base", "country": ["KR"],
     "access": "registration", "registration": "https://www.gnssdata.or.kr/user/agree.do", "openNote": 'Free registration required'},
    {"id": "almgg_mn",    "url": "http://rtk.gazar.gov.mn:2101/",            # MonPOS; SNIP R3.14; alt IP 66.181.168.80:2101; curl-confirmed 2026-04-30
     "color": "#9e6b00", "label": "MonPOS",
     "type": "physical-vrs", "country": ["MN"],
     "credentials": {"user": "rover", "pass": "262461"},
     "openNote": 'Free; shared public credentials: username rover, password 262461',
     "access": "open",         "registration": None,
     "solution_filter": False},                                                   # caster tags 6 physical stations solution=1
    {"id": "icecors",     "url": "http://178.19.53.126:2101/",
     "color": "#1e6b8c", "label": "IceCORS",
     "type": "physical-vrs", "country": ["IS"],
     "access": "registration", "registration": "https://ggn01.lmi.is/", "openNote": 'Free registration required',
     "nmea_filter": False},                                                   # GNSMART tags 4 physical Reykjanes mounts (AUSV/GEVK/SENG/VOGC) nmea=1, solution=0
    {"id": "ksa_cors",    "url": "http://ksacors.geoportal.sa:2101/",
     "color": "#a0522d", "label": "KSA-CORS",
     "type": "vrs-only", "country": ["SA"],
     "access": "conditions",   "registration": "https://ksacors.geoportal.sa", "openNote": 'Free registration required'},
    # Italy — regional networks
    {"id": "spin3",       "url": "http://158.102.7.10:2101/",                   # bare IP; spingnss.it hostname times out; IP confirmed SOURCETABLE 200 OK 2026-05-07
     "color": "#1565c0", "label": "SPIN3 GNSS",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Piemonte, Lombardia, Valle d'Aosta", "group": "italy-regional",
     "access": "registration", "registration": "https://www.spingnss.it", "openNote": 'Free registration required (CSI Piemonte portal)'},
    {"id": "gpsumbria",   "url": "http://gpsumbria.regione.umbria.it:2101/",
     "color": "#2e7d32", "label": "GPS-UMBRIA",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Umbria", "group": "italy-regional",
     "access": "registration", "registration": "https://gpsumbria.regione.umbria.it", "openNote": 'Free registration required'},
    {"id": "sit_puglia",  "url": "http://gps.sit.puglia.it:2101/",
     "color": "#0288d1", "label": "SIT Puglia",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Puglia", "group": "italy-regional",
     "access": "registration", "registration": "https://sit.puglia.it", "openNote": 'Free registration required (SIT Puglia geoportal)'},
    {"id": "gnss_campania", "url": "http://gps.sit.regione.campania.it:2101/",  # public creds: user=Campania pass=GNSS (30-sec VRS); 1-sec requires SPID
     "color": "#6a1b9a", "label": "GNSS Campania",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Campania", "group": "italy-regional",
     "credentials": {"user": "Campania", "pass": "GNSS"},
     "access": "open",         "registration": None, "openNote": 'Free; public credentials (user: Campania, pass: GNSS) for 30-sec VRS; 1-sec requires SPID'},
    {"id": "tpos",        "url": "http://194.105.50.232:2101/",                  # bare IP; tpos.provincia.tn.it is portal domain, does not resolve as NTRIP caster
     "color": "#00695c", "label": "TPOS",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Trentino", "group": "italy-regional",
     "access": "registration", "registration": "https://www.tpos.provincia.tn.it"},
    {"id": "stpos",       "url": "http://62.101.0.40:2109/",               # SOURCETABLE 200 OK on port 2109; port 2101 refused; domain www.stpos.it
     "color": "#ad1457", "label": "STPOS",
     "type": "physical-vrs", "country": ["IT"],
     "region": "South Tyrol", "group": "italy-regional",
     "access": "registration", "registration": "https://www.stpos.it"},
    {"id": "gnss_veneto", "url": "http://147.162.229.53:2101/",
     "color": "#4527a0", "label": "Rete GNSS Veneto",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Veneto", "group": "italy-regional",
     "access": "registration", "registration": "https://retegnssveneto.cisas.unipd.it"},
    {"id": "gnss_liguria", "url": "http://81.23.86.70:2101/",
     "color": "#0277bd", "label": "Rete GNSS Liguria",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Liguria", "group": "italy-regional",
     "access": "registration", "registration": "https://geoportal.regione.liguria.it/servizi/rete-gnss-liguria"},
    {"id": "sicilianet",  "url": "http://193.206.223.39:2101/",
     "color": "#e65100", "label": "Sicili@net",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Sicily", "group": "italy-regional",
     "access": "registration", "registration": "https://www.ct.ingv.it/index.php/risorse-e-servizi/sicil-net"},
    {"id": "gnss_abruzzo_lazio", "url": "http://gnss-rtk.regione.abruzzo.it:2101/",  # times out from external IPs (firewalled); service confirmed operational via portal HTTP 200; add 2026-05-13
     "color": "#c62828", "label": "GNSS Abruzzo+Lazio",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Abruzzo + Lazio", "group": "italy-regional",
     "access": "registration", "registration": "https://gnssnet.regione.abruzzo.it/accesso.php", "openNote": "Free registration required (Regione Abruzzo)"},
    # US state DOT / CORS networks — physical-coordinate stations
    {"id": "acorn",       "url": "http://www.acorn-gnss.net:2101/",    # Trimble Pivot Web; anonymous sourcetable exposes VRS + MS_RTCM3 (nearest single-base) + named VRS solutions
     "color": "#2e5b8a", "label": "ACORN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Alaska", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.acorn-gnss.net",
     "openNote": "Free registration required (Alaska DNR / DOTPF)"},
    {"id": "nps_cors",    "url": "http://rtk.nps.gov:2101/",
     "color": "#4a7c59", "label": "NPS CORS",
     "type": "single-base", "country": ["US"],
     "access": "conditions", "registration": "https://ntrip.nps.gov",
     "openNote": "Free*; credentials via gnss_posnav@nps.gov — access scope unclear"},
    {"id": "wiscors",     "url": "http://wiscors.dot.wi.gov:2101/",
     "color": "#bf360c", "label": "WISCORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Wisconsin", "group": "us-state-dot",
     "access": "registration", "registration": "https://wiscors.dot.wi.gov", "openNote": 'Free registration required (Wisconsin DOT)'},
    {"id": "fprn",        "url": "http://www.myfloridagps.com:10000/",             # port 10000 (Leica); standard 2101 not used
     "color": "#f57f17", "label": "FPRN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Florida", "group": "us-state-dot",
     "access": "registration", "registration": "https://myfloridagps.com", "openNote": 'Free registration required (Florida DOT)'},
    {"id": "ardot_rtn",   "url": "http://gps.ardot.gov:2101/",
     "color": "#827717", "label": "ARDOT RTN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Arkansas", "group": "us-state-dot",
     "access": "registration", "registration": "https://gps.ardot.gov", "openNote": 'Free registration required (Arkansas DOT)'},
{"id": "vector",      "url": "http://vector.vermont.gov:2101/",            # VTrans Geodetic Survey; canonical hostname (resolves to 20.185.11.35)
     "color": "#1b5e20", "label": "VECTOR VT",
     "type": "physical-vrs", "country": ["US"],
     "region": "Vermont", "group": "us-state-dot",
     "access": "registration", "registration": "https://vector.vermont.gov", "openNote": 'Free registration required (VTrans Geodetic Survey)'},
{"id": "gcgc_rtn",    "url": "http://rtn.usm.edu:2101/",
     "color": "#01579b", "label": "GCGC RTN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Mississippi (Gulf Coast)", "group": "us-state-dot",
     "access": "registration", "registration": "https://rtn.usm.edu", "openNote": 'Free registration required (Gulf Coast Geospatial Center / USM)'},
{"id": "orgn",        "url": "http://orgn.odot.state.or.us:9881/",          # hostname; port 9881 (Leica); SOURCETABLE 200 OK 2026-05-13 (6 STR)
     "color": "#004d40", "label": "ORGN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Oregon", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.oregon.gov/odot/orgn", "openNote": 'Free registration required (Oregon DOT)'},
    {"id": "msrn",        "url": "http://mdotcors.michigan.gov:10010/",         # port 10010 free RTCM3 MSM4 (per MSRN Port Scheme); 10011 = CMRx
     "color": "#006064", "label": "MSRN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Michigan", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.michigan.gov/mdot", "openNote": 'Free registration required (Michigan DOT)'},
{"id": "ct_acorn",    "url": "http://acorn.uconn.edu:2101/",               # SOURCETABLE 200 OK 2026-05-13 (48 STR)
     "color": "#1a237e", "label": "ACORN CT",
     "type": "physical-vrs", "country": ["US"],
     "region": "Connecticut", "group": "us-state-dot",
     "access": "registration", "registration": "https://acorn.uconn.edu", "openNote": 'Free registration required (CTDOT + UConn)'},
    {"id": "macors",      "url": "http://macorsrtk.massdot.state.ma.us:2101/",  # MassDOT Leica SpiderNet; port 2101 firewalled from external probes — account-gated; add 2026-05-13
     "color": "#283593", "label": "MaCORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Massachusetts", "group": "us-state-dot",
     "access": "registration", "registration": "https://macors.massdot.state.ma.us", "openNote": 'Free registration required (MassDOT)'},
    {"id": "nysnet",      "url": "http://rtn.dot.ny.gov:8080/",                 # NYSDOT Leica SpiderNet; port 8080 confirmed SOURCETABLE 200 OK 2026-05-13 (18 STR); port 2101 firewalled; add 2026-05-13
     "color": "#0d47a1", "label": "NYSNet",
     "type": "physical-vrs", "country": ["US"],
     "region": "New York", "group": "us-state-dot",
     "access": "registration", "registration": "https://cors.dot.ny.gov", "openNote": 'Free registration required (NYSDOT)'},
    {"id": "alcors",      "url": "http://aldotcors.dot.state.al.us:10099/",    # ALDOT Leica SBC; port 10099 = physical single-base (158 STR confirmed 2026-05-13); port 10011 = network mounts; port 2101 firewalled; add 2026-05-13
     "color": "#1565c0", "label": "AlCORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Alabama", "group": "us-state-dot",
     "access": "registration", "registration": "https://aldotcors.dot.state.al.us/SBC/Account/Register", "openNote": 'Free registration required (Alabama DOT)'},
    {"id": "iartn",       "url": "http://165.206.203.10:10000/",                  # bare IP:port; iartnsbc.iowadot.gov:2101 dead 2026-05-07; sourcetable open, per-station streams require credentials (Emlid/DJI flow documented at e38surveysolutions.com)
     "color": "#37474f", "label": "IARTN",
     "type": "physical-coord-vrs", "country": ["US"],
     "region": "Iowa", "group": "us-state-dot",
     "access": "registration", "registration": "https://iowadot.gov", "openNote": 'Free registration required (Iowa DOT)'},
    # US state DOT — VRS-only (filter_vrs drops all pins; shown as stopgap circles)
    {"id": "kycors",      "url": "http://kycors.ky.gov:2101/",
     "color": "#546e7a", "label": "KyCORS",
     "type": "vrs-only", "country": ["US"],
     "region": "Kentucky", "group": "us-state-dot",
     "access": "registration", "registration": "https://kycors.ky.gov", "openNote": 'Free registration required (Kentucky Transportation Cabinet)'},
    {"id": "mncors",      "url": "http://mncors.dot.state.mn.us:9000/",         # port 9000; VRS-only
     "color": "#455a64", "label": "MnCORS",
     "type": "vrs-only", "country": ["US"],
     "region": "Minnesota", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.mndot.gov", "openNote": 'Free registration required (Minnesota DOT)'},
    {"id": "odot_rtn",    "url": "http://156.63.133.115:2101/",                 # bare IP; VRS-only
     "color": "#607d8b", "label": "ODOT RTN",
     "type": "vrs-only", "country": ["US"],
     "region": "Ohio", "group": "us-state-dot",
     "access": "registration", "registration": "https://transportation.ohio.gov", "openNote": 'Free registration required (Ohio DOT)'},
    {"id": "modot_rtn",   "url": "http://rtk3.modot.mo.gov:2101/",              # VRS-only; notarized agreement
     "color": "#78909c", "label": "MoDOT RTN",
     "type": "vrs-only", "country": ["US"],
     "region": "Missouri", "group": "us-state-dot",
     "access": "conditions",   "registration": "https://modot.mo.gov", "openNote": 'Notarized access agreement required (Missouri DOT); free once approved'},
    {"id": "wvrtn",       "url": "http://wvrtn.cors.us:2101/",                  # VRS-only
     "color": "#90a4ae", "label": "WVRTN",
     "type": "vrs-only", "country": ["US"],
     "region": "West Virginia", "group": "us-state-dot",
     "access": "registration", "registration": "https://transportation.wv.gov", "openNote": 'Free registration required (WVDOT — IT Division)'},
    {"id": "mainedot",    "url": "http://medotrtn.maine.gov:2101/",             # VRS-only; migrated from mdotcors.maine.gov Oct 2025
     "color": "#b0bec5", "label": "MaineDOT",
     "type": "vrs-only", "country": ["US"],
     "region": "Maine", "group": "us-state-dot",
     "access": "registration", "registration": "https://medotrtn.maine.gov", "openNote": 'Free registration required (Maine DOT)'},
    {"id": "azcors",      "url": "http://azcors.azwater.gov:2101/",              # Arizona CORS; ADWR (Arizona Dept of Water Resources); pipeline-access: registration
     "color": "#c2692e", "label": "AZ CORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Arizona", "group": "us-state-dot",
     "access": "registration", "registration": "https://azcors.azwater.gov", "openNote": 'Free registration required (ADWR — Arizona Dept of Water Resources)'},
    {"id": "mesa_rtvrn",  "url": "http://rtvrn.mesacounty.us:2101/",            # VRS-only; western Colorado
     "color": "#8d6e63", "label": "Mesa County RTVRN",
     "type": "vrs-only", "country": ["US"],
     "region": "Colorado (western)",
     "access": "registration", "registration": "https://rtvrn.mesacounty.us/RegisterAccount.aspx"},
    {"id": "agrs_nl",    "url": "http://ntrip.kadaster.nl:2101/",
     "color": "#0288d1", "label": "AGRS.NL / AGRS.BES",
     "type": "single-base", "country": ["NL", "BQ"],
     "access": "open",         "registration": None},                            # free, anonymous; covers NL mainland + BES islands
    {"id": "regme_ec",   "url": "http://ntrip.igm.gob.ec:2101/",
     "color": "#558b2f", "label": "REGME-IP",
     "type": "single-base", "country": ["EC"],
     "access": "registration", "registration": "https://www.geoportaligm.gob.ec/ntrip/"},
    {"id": "ign_cr_cors", "url": "http://igncaster.snitcr.go.cr:2101/",  # BKG NtripCaster 2.0.44; SOURCETABLE 200 OK 2026-05-12; 14 physical stations; SNIT account required
     "color": "#1b7837", "label": "IGN-CR / SNIT",
     "type": "single-base", "country": ["CR"],
     "access": "registration", "registration": "https://www.snitcr.go.cr/",
     "openNote": "Free SNIT account required; credentials activated at noon and midnight CR time"},
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
    registration = src.get("registration")
    access = src.get("access", "registration")
    color = src.get("color", "")
    label = src.get("label", "")
    src_type = src.get("type", "")
    src_country = src.get("country", [])
    src_region = src.get("region")
    src_group = src.get("group")
    src_credentials = src.get("credentials")
    prev_last_ok = src.get("_prev_last_ok")
    nmea_filter = src.get("nmea_filter", True)
    solution_filter = src.get("solution_filter", True)
    raw_path = DATA_DIR / f"{sid}.sourcetable"
    _meta = {
        "url": url, "color": color, "label": label,
        "type": src_type, "country": src_country, "region": src_region,
        "group": src_group, "credentials": src_credentials,
        "registration": registration, "access": access,
        "openNote": src.get("openNote"),
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
            "label": data.get("label", ""),
            "type": data.get("type", ""),
            "country": data.get("country", []),
            "region": data.get("region"),
            "group": data.get("group"),
            "credentials": data.get("credentials"),
            "registration": data.get("registration"),
            "access": data.get("access", "registration"),
            "openNote": data.get("openNote"),
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
    health_path.write_text(json.dumps(health, indent=2) + "\n")
    print(f"Wrote {health_path}.")

    if not write_stations:
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
