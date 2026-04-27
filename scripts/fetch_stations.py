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
     "nmea_filter": False},                                                       # caster tags all physical stations nmea=1
    {"id": "centipede",   "url": "http://crtk.net:2101/",                       # migrated from caster.centipede.fr 2025-03-18
     "color": "#e87500", "label": "Centipede",
     "type": "single-base", "country": ["global"],
     "credentials": {"user": "centipede", "pass": "centipede"},
     "access": "open",         "registration": None},
    {"id": "frednet",     "url": "http://gnsscaster.regione.fvg.it:8080/",
     "color": "#2e6fb0", "label": "FReDNet",
     "type": "physical-vrs", "country": ["IT"], "region": "Friuli-Venezia Giulia",
     "access": "registration", "registration": "https://frednet.crs.ogs.it/"},
    {"id": "geortk",      "url": "http://geortk.jp:2101/",
     "color": "#1a7a4a", "label": "GeoRTK",
     "type": "single-base", "country": ["JP"],
     "access": "open",         "registration": None,
     "nmea_filter": False},                                                       # caster tags physical stations nmea=1
    # SAPOS — German federal-state RTK networks. Sourcetables publicly readable;
    # RTCM streams require per-Länder registration. Most Länder free; BY €20/yr
    # flat rate for non-agricultural use. Raw TCP (NTRIP 1.0) fallback required.
    {"id": "sapos_SH_HH", "url": "http://www.sapos.geonord.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Schleswig-Holstein + Hamburg)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Schleswig-Holstein + Hamburg", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_NI",    "url": "http://www.sapos-ni-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Niedersachsen)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Niedersachsen + Bremen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_NW",    "url": "http://www.sapos-nw-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Nordrhein-Westfalen)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Nordrhein-Westfalen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_HE",    "url": "http://www.sapos-he-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Hessen)",
     "type": "physical-vrs", "country": ["DE"],
     "region": "Hessen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_RP",    "url": "http://www.sapos-ntrip.rlp.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Rheinland-Pfalz)",
     "type": "physical-vrs", "country": ["DE"],
     "region": "Rheinland-Pfalz", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_BW",    "url": "http://www.sapos-bw-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Baden-Württemberg)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Baden-Württemberg", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_BY",    "url": "http://www.sapos-by-ntrip.de:2101/",          # free agri; €20/yr otherwise
     "color": "#2d6e6e", "label": "SAPOS (Bayern)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Bayern", "group": "sapos",
     "access": "conditions",   "registration": "https://www.sapos.de"},
    {"id": "sapos_SN",    "url": "http://ntrip.sachsen.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Sachsen)",
     "type": "physical-vrs", "country": ["DE"],
     "region": "Sachsen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_SL",    "url": "http://www.sapos-sl-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Saarland)",
     "type": "physical-vrs", "country": ["DE"],
     "region": "Saarland", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_BE",    "url": "http://www.sapos-be-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Berlin)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Berlin", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_BB",    "url": "http://www.sapos-bb-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Brandenburg)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Brandenburg", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_MV",    "url": "http://www.sapos-mv-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Mecklenburg-Vorpommern)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Mecklenburg-Vorpommern", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_LSA",   "url": "http://www.sapos-lsa-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Sachsen-Anhalt)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Sachsen-Anhalt", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "sapos_TH",    "url": "http://www.sapos-th-ntrip.de:2101/",
     "color": "#2d6e6e", "label": "SAPOS (Thüringen)",
     "type": "vrs-only", "country": ["DE"],
     "region": "Thüringen", "group": "sapos",
     "access": "registration", "registration": "https://www.sapos.de"},
    {"id": "apos",        "url": "http://aposrtk.bev.gv.at:2101/",              # free agri/forestry (eAMA); paid otherwise
     "color": "#9b0000",  "label": "APOS",
     "type": "physical-vrs", "country": ["AT"],
     "access": "conditions",   "registration": "https://www.bev.gv.at"},
    {"id": "ergnss",      "url": "http://ergnss-ip.ign.es:2101/",
     "color": "#b05000", "label": "ERGNSS",
     "type": "physical-vrs", "country": ["ES"],
     "access": "registration", "registration": "https://ergnss.ign.es/gnuserportal/"},
    {"id": "auscors",     "url": "http://ntrip.data.gnss.ga.gov.au:2101/",
     "color": "#b8860b", "label": "AUSCORS",
     "type": "single-base", "country": ["AU"],
     "access": "registration", "registration": "https://gnss.ga.gov.au/registration"},
    {"id": "positionz",   "url": "http://positionz-rt.linz.govt.nz:2101/",
     "color": "#2e8b57", "label": "PositioNZ",
     "type": "single-base", "country": ["NZ"],
     "access": "registration", "registration": "https://www.linz.govt.nz/"},
    {"id": "satref",      "url": "http://ntrip.geodetic.gov.hk:2101/",
     "color": "#8b008b", "label": "SatRef",
     "type": "physical-vrs", "country": ["HK"],
     "access": "registration", "registration": "https://www.geodetic.gov.hk/"},
    {"id": "inacors",     "url": "http://nrtk.big.go.id:2001/",                 # port 2001, not 2101
     "color": "#1a5fa0", "label": "InaCORS",
     "type": "physical-vrs", "country": ["ID"],
     "access": "registration", "registration": "https://nrtk.big.go.id"},
    {"id": "trignet",     "url": "http://trignet.co.za:2101/",
     "color": "#556b2f", "label": "TrigNet",
     "type": "single-base", "country": ["ZA"],
     "access": "registration", "registration": "https://www.trignet.co.za"},
    {"id": "rbmc_ip",     "url": "http://gps-ntrip.ibge.gov.br:2101/",
     "color": "#008b8b", "label": "RBMC-IP",
     "type": "single-base", "country": ["BR"],
     "access": "registration", "registration": "https://gps-ntrip.ibge.gov.br"},
    {"id": "ramsac",      "url": "http://ntrip.ign.gob.ar:2101/",
     "color": "#7b3f9e", "label": "RAMSAC",
     "type": "single-base", "country": ["AR"],
     "access": "registration", "registration": "https://www.ign.gob.ar"},
    {"id": "regna_rou",   "url": "http://rtk.igm.gub.uy:2101/",
     "color": "#1a9e5c", "label": "REGNA-ROU",
     "type": "physical-vrs", "country": ["UY"],
     "access": "registration", "registration": "https://rtk.igm.gub.uy/SBC/Account/Register"},
    {"id": "flepos",      "url": "http://flepos.vlaanderen.be:2101/",           # ntrip.flepos.be NXDOMAIN as of 2026-04
     "color": "#3a7ca5", "label": "FLEPOS",
     "type": "vrs-only", "country": ["BE"], "region": "Flanders",
     "access": "registration", "registration": "https://flepos.vlaanderen.be"},
    {"id": "walcors",     "url": "http://gnss.wallonie.be:2101/",
     "color": "#2c6e8a", "label": "WALCORS",
     "type": "vrs-only", "country": ["BE"], "region": "Wallonia",
     "access": "registration", "registration": "https://gnss.wallonie.be"},
    {"id": "spslux",      "url": "http://stream.spslux.lu:5005/",               # port 5005, not 2101
     "color": "#5c6bc0", "label": "SPSLux",
     "type": "physical-vrs", "country": ["LU"],
     "access": "registration", "registration": "https://www.spslux.lu/SBC/Account/Register"},
    {"id": "asg_eupos",   "url": "http://system.asgeupos.pl:2101/",
     "color": "#7b5ea7", "label": "ASG-EUPOS",
     "type": "vrs-only", "country": ["PL"],
     "access": "registration", "registration": "https://system.asgeupos.pl"},
    {"id": "cropos",      "url": "http://gnss.cropos.hr:2101/",
     "color": "#c0392b", "label": "CROPOS",
     "type": "vrs-only", "country": ["HR"],
     "access": "registration", "registration": "https://www.cropos.hr"},
    {"id": "estpos",      "url": "http://gnss-rtk.maaamet.ee:8083/",            # port 8083; free until Aug 2026
     "color": "#16a085", "label": "ESTPOS",
     "type": "vrs-only", "country": ["EE"],
     "access": "conditions",   "registration": "https://geoportaal.maaamet.ee"},
    {"id": "latpos",      "url": "http://latpos.lgia.gov.lv:5001/",             # port 5001, not 2101
     "color": "#1a6b3c", "label": "LatPos",
     "type": "vrs-only", "country": ["LV"],
     "access": "registration", "registration": "https://latpos.lgia.gov.lv/SBC"},
    {"id": "igac",        "url": "http://sbc.igac.gov.co:2101/",
     "color": "#d4a017", "label": "IGAC",
     "type": "physical-vrs", "country": ["CO"],
     "access": "registration", "registration": "https://redgeodesica-sbc.igac.gov.co/sbc"},
    {"id": "earthscope",  "url": "http://ntrip.earthscope.org:2101/",
     "color": "#8b4513", "label": "EarthScope",
     "type": "single-base", "country": ["americas"],
     "access": "conditions",   "registration": "https://www.earthscope.org/data/gnss-realtime/"},
    {"id": "mirai",       "url": "http://ntrip.go.gnss.go.jp:2101/",
     "color": "#2471a3", "label": "MIRAI",
     "type": "single-base", "country": ["JP"],
     "access": "registration", "registration": "https://go.gnss.go.jp"},
    {"id": "cors_korea",  "url": "http://www.gnssdata.or.kr:2101/",
     "color": "#a93226", "label": "CORS-KOREA",
     "type": "physical-vrs", "country": ["KR"],
     "access": "conditions",   "registration": "https://www.gnssdata.or.kr"},
    {"id": "icecors",     "url": "http://178.19.53.126:2101/",
     "color": "#1e6b8c", "label": "IceCORS",
     "type": "physical-vrs", "country": ["IS"],
     "access": "registration", "registration": "https://www.natt.is/is/landmaelingar/jardstodvakerfi"},
    {"id": "ksa_cors",    "url": "http://ksacors.geoportal.sa:2101/",
     "color": "#a0522d", "label": "KSA-CORS",
     "type": "vrs-only", "country": ["SA"],
     "access": "conditions",   "registration": "https://ksacors.geoportal.sa"},
    # Italy — regional networks
    {"id": "spin3",       "url": "http://spingnss.it:2101/",
     "color": "#1565c0", "label": "SPIN3 GNSS",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Piemonte, Lombardia, Valle d'Aosta", "group": "italy-regional",
     "access": "registration", "registration": "https://www.spingnss.it"},
    {"id": "gpsumbria",   "url": "http://gpsumbria.regione.umbria.it:2101/",
     "color": "#2e7d32", "label": "GPS-UMBRIA",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Umbria", "group": "italy-regional",
     "access": "registration", "registration": "https://gpsumbria.regione.umbria.it"},
    {"id": "gnss_abruzzo_lazio", "url": "http://gnss-rtk.regione.abruzzo.it:2101/",
     "color": "#558b2f", "label": "GNSS Abruzzo+Lazio",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Abruzzo + Lazio", "group": "italy-regional",
     "access": "registration", "registration": "https://gnss-rtk.regione.abruzzo.it"},
    {"id": "sit_puglia",  "url": "http://gps.sit.puglia.it:2101/",
     "color": "#0288d1", "label": "SIT Puglia",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Puglia", "group": "italy-regional",
     "access": "registration", "registration": "https://sit.puglia.it"},
    {"id": "gnss_campania", "url": "http://gps-sit.regione.campania.it:2101/",  # SPID required for new users
     "color": "#6a1b9a", "label": "GNSS Campania",
     "type": "physical-vrs", "country": ["IT"],
     "region": "Campania", "group": "italy-regional",
     "access": "conditions",   "registration": "https://www.regione.campania.it"},
    # US state DOT / CORS networks — physical-coordinate stations
    {"id": "wiscors",     "url": "http://wiscors.dot.wi.gov:2101/",
     "color": "#bf360c", "label": "WISCORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Wisconsin", "group": "us-state-dot",
     "access": "registration", "registration": "https://wiscors.dot.wi.gov"},
    {"id": "fprn",        "url": "http://ntrip.myfloridagps.com:2101/",
     "color": "#f57f17", "label": "FPRN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Florida", "group": "us-state-dot",
     "access": "registration", "registration": "https://myfloridagps.com"},
    {"id": "ardot_rtn",   "url": "http://gps.ardot.gov:2101/",
     "color": "#827717", "label": "ARDOT RTN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Arkansas", "group": "us-state-dot",
     "access": "registration", "registration": "https://gps.ardot.gov"},
    {"id": "macors",      "url": "http://macorsrtk.massdot.state.ma.us:2101/",
     "color": "#33691e", "label": "MaCORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Massachusetts", "group": "us-state-dot",
     "access": "registration", "registration": "https://macorsrtk.massdot.state.ma.us"},
    {"id": "vector",      "url": "http://20.185.11.35:2101/",                   # VT VCGI; bare IP
     "color": "#1b5e20", "label": "VECTOR VT",
     "type": "physical-vrs", "country": ["US"],
     "region": "Vermont", "group": "us-state-dot",
     "access": "registration", "registration": "https://vcgi.vermont.gov"},
    {"id": "azcors",      "url": "http://azcors.azwater.gov:2101/",
     "color": "#e65100", "label": "AzCORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Arizona", "group": "us-state-dot",
     "access": "registration", "registration": "https://azcors.azwater.gov"},
    {"id": "gcgc_rtn",    "url": "http://rtn.usm.edu:2101/",
     "color": "#01579b", "label": "GCGC RTN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Mississippi (Gulf Coast)", "group": "us-state-dot",
     "access": "registration", "registration": "https://rtn.usm.edu"},
    {"id": "alcors",      "url": "http://aldotcors.dot.state.al.us:10011/",     # port 10011 (Leica)
     "color": "#880e4f", "label": "AlCORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Alabama", "group": "us-state-dot",
     "access": "registration", "registration": "https://dot.state.al.us"},
    {"id": "orgn",        "url": "http://167.131.0.205:9879/",                  # bare IP; port 9879 (Leica)
     "color": "#004d40", "label": "ORGN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Oregon", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.oregon.gov/odot"},
    {"id": "msrn",        "url": "http://mdotcors.michigan.gov:10700/",         # port 10700 (Leica)
     "color": "#006064", "label": "MSRN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Michigan", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.michigan.gov/mdot"},
    {"id": "nysnet",      "url": "http://cors.dot.ny.gov:2101/",
     "color": "#311b92", "label": "NYSNet",
     "type": "physical-vrs", "country": ["US"],
     "region": "New York", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.dot.ny.gov"},
    {"id": "incors",      "url": "http://incors.in.gov:10000/",                 # port 10000
     "color": "#4e342e", "label": "InCORS",
     "type": "physical-vrs", "country": ["US"],
     "region": "Indiana", "group": "us-state-dot",
     "access": "registration", "registration": "https://incors.in.gov"},
    {"id": "iartn",       "url": "http://iartnsbc.iowadot.gov:2101/",
     "color": "#37474f", "label": "IARTN",
     "type": "physical-vrs", "country": ["US"],
     "region": "Iowa", "group": "us-state-dot",
     "access": "registration", "registration": "https://iowadot.gov"},
    # US state DOT — VRS-only (filter_vrs drops all pins; shown as stopgap circles)
    {"id": "kycors",      "url": "http://kycors.ky.gov:2101/",
     "color": "#546e7a", "label": "KyCORS",
     "type": "vrs-only", "country": ["US"],
     "region": "Kentucky", "group": "us-state-dot",
     "access": "registration", "registration": "https://kycors.ky.gov"},
    {"id": "mncors",      "url": "http://mncors.dot.state.mn.us:9000/",         # port 9000; VRS-only
     "color": "#455a64", "label": "MnCORS",
     "type": "vrs-only", "country": ["US"],
     "region": "Minnesota", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.mndot.gov"},
    {"id": "odot_rtn",    "url": "http://156.63.133.115:2101/",                 # bare IP; VRS-only
     "color": "#607d8b", "label": "ODOT RTN",
     "type": "vrs-only", "country": ["US"],
     "region": "Ohio", "group": "us-state-dot",
     "access": "registration", "registration": "https://transportation.ohio.gov"},
    {"id": "modot_rtn",   "url": "http://rtk3.modot.mo.gov:2101/",              # VRS-only; notarized agreement
     "color": "#78909c", "label": "MoDOT RTN",
     "type": "vrs-only", "country": ["US"],
     "region": "Missouri", "group": "us-state-dot",
     "access": "conditions",   "registration": "https://modot.mo.gov"},
    {"id": "wvrtn",       "url": "http://wvrtn.cors.us:2101/",                  # VRS-only
     "color": "#90a4ae", "label": "WVRTN",
     "type": "vrs-only", "country": ["US"],
     "region": "West Virginia", "group": "us-state-dot",
     "access": "registration", "registration": "https://transportation.wv.gov"},
    {"id": "mainedot",    "url": "http://mdotcors.maine.gov:2101/",             # VRS-only (transitioning)
     "color": "#b0bec5", "label": "MaineDOT",
     "type": "vrs-only", "country": ["US"],
     "region": "Maine", "group": "us-state-dot",
     "access": "registration", "registration": "https://www.maine.gov/mdot"},
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


def parse_sourcetable(text: str, nmea_filter: bool = True) -> tuple[list[dict], dict]:
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
         s.get("dualFreq"), s.get("format", ""), s.get("constellations", "")]
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
    raw_path = DATA_DIR / f"{sid}.sourcetable"
    _meta = {
        "url": url, "color": color, "label": label,
        "type": src_type, "country": src_country, "region": src_region,
        "group": src_group, "credentials": src_credentials,
        "registration": registration, "access": access,
    }
    try:
        text = fetch(url)
        stations, stats = parse_sourcetable(text, nmea_filter=nmea_filter)
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
                stations, stats = parse_sourcetable(text, nmea_filter=nmea_filter)
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
            "type": data.get("type", ""),
            "country": data.get("country", []),
            "region": data.get("region"),
            "group": data.get("group"),
            "credentials": data.get("credentials"),
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
