"""Connecticut ACORN — NGS bulk file scraper, filtered to CT-prefix stations.

Source: https://geodesy.noaa.gov/corsdata/coord/coord_20/nad83_2011_geo.comp.txt

ACORN's operator FAQ enumerates 13 physical sensors but only 7 of the
CT-prefix names are in the NGS NSRS coordinate file. The non-NGS
stations (CTBK, CTPN, URIL, MASB, MASH, NYRH) are not publicly listed
with coordinates anywhere outside the Trimble Pivot login-gated sensor
map — we pin only what's confirmed.
"""
from __future__ import annotations

from . import _ngs_bulk


def scrape() -> dict:
    stations = _ngs_bulk.filter_by_state("CT")
    if not stations:
        raise ValueError("NGS bulk file matched 0 CT-state stations")
    return {"source_url": _ngs_bulk.NGS_BULK_URL, "stations": stations}
