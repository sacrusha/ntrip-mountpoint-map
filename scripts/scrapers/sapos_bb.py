"""SAPOS Brandenburg sitelog scraper.

Source: https://monitor.sapos-bb.de/station/sitelogs/

The directory page lists `00XXXX DEU_YYYYMMDD.log` IGS-format sitelogs,
one per physical reference station. Section 2 of each sitelog carries
the operator-declared antenna position in DMS strings:

    Latitude (N is +)      : +DDMMSS.ss
    Longitude (E is +)     : +DDDMMSS.ss

The Site Name in Section 1 is the human-readable station name (e.g.
WUENSDORF, POTSDAM); we use that as the pin label.
"""
from __future__ import annotations

import re
import urllib.request
from urllib.parse import urljoin

INDEX_URL = "https://monitor.sapos-bb.de/station/sitelogs/"
TIMEOUT = 15
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper sapos_bb)"

# Sitelog filenames look like `000300DEU_20260310.log`. Match the basename
# rather than scraping the directory HTML for `<a href>` so a future
# directory-listing rewrite doesn't break the scraper.
_LOG_RE = re.compile(r"\b(\d{6}DEU_\d{8}\.log)\b")

# Section 1 - Site Identification: "Site Name : <NAME>"
_SITE_NAME_RE = re.compile(r"^\s*Site Name\s*:\s*(\S.*?)\s*$", re.MULTILINE)
# Section 2 - Approximate Position (ITRF): "+DDMMSS.ss" / "+DDDMMSS.ss"
_LAT_RE = re.compile(r"Latitude\s*\(N is \+\)\s*:\s*([+-]\d+\.\d+)")
_LON_RE = re.compile(r"Longitude\s*\(E is \+\)\s*:\s*([+-]\d+\.\d+)")


def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _dms_to_decimal(s: str, deg_digits: int) -> float:
    """Convert IGS sitelog "+DDMMSS.ss" / "+DDDMMSS.ss" to signed decimal.

    `deg_digits` is 2 for latitude (DDMMSS.ss) and 3 for longitude
    (DDDMMSS.ss). The leading sign carries hemisphere (+N, +E)."""
    sign = -1 if s.startswith("-") else 1
    body = s.lstrip("+-")
    dd = int(body[:deg_digits])
    mm = int(body[deg_digits:deg_digits + 2])
    ss = float(body[deg_digits + 2:])
    return sign * round(dd + mm / 60.0 + ss / 3600.0, 6)


def _parse_sitelog(text: str) -> tuple[str, float, float]:
    """Return (site_name, lat, lon) from a single IGS sitelog."""
    name_match = _SITE_NAME_RE.search(text)
    lat_match = _LAT_RE.search(text)
    lon_match = _LON_RE.search(text)
    if not (name_match and lat_match and lon_match):
        raise ValueError("sitelog missing Site Name or DMS coordinates")
    name = name_match.group(1).strip()
    lat = _dms_to_decimal(lat_match.group(1), 2)
    lon = _dms_to_decimal(lon_match.group(1), 3)
    return name, lat, lon


def scrape() -> dict:
    """Return parsed station list. Raises on fetch/parse failure."""
    index_html = _http_get(INDEX_URL)
    # de-duplicate while preserving discovery order; sorted() at the end
    # gives a stable cache so unchanged scrapes produce no diff.
    logs = sorted(set(_LOG_RE.findall(index_html)))
    if not logs:
        raise ValueError(f"no sitelog filenames matched at {INDEX_URL}")

    stations = []
    for log_name in logs:
        text = _http_get(urljoin(INDEX_URL, log_name))
        try:
            name, lat, lon = _parse_sitelog(text)
        except ValueError as e:
            # Skip individual broken sitelogs rather than failing the whole
            # scrape — operator occasionally publishes a half-written file
            # during maintenance windows.
            print(f"[sapos_bb] skipping {log_name}: {e}", flush=True)
            continue
        stations.append({"name": name, "lat": lat, "lon": lon, "country": "DEU"})

    if not stations:
        raise ValueError("scraped 0 stations from sapos-bb sitelog index")

    stations.sort(key=lambda s: s["name"])
    return {"source_url": INDEX_URL, "stations": stations}
