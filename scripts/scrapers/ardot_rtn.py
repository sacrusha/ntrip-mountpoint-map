"""Arkansas DOT RTN — NGS bulk file scraper, filtered to AR-prefix stations.

Source: https://geodesy.noaa.gov/corsdata/coord/coord_20/nad83_2011_geo.comp.txt

ARDOT does not publish a per-station coord list on its operator portal
(login-gated Trimble Pivot sensor map). The AR-state CORS stations are
all on the NGS NSRS, so the NGS bulk file is the authoritative public
source for their NAD83(2011) coordinates.
"""
from __future__ import annotations

from . import _ngs_bulk


def scrape() -> dict:
    stations = _ngs_bulk.filter_by_state("AR")
    if not stations:
        raise ValueError("NGS bulk file matched 0 AR-state stations")
    return {"source_url": _ngs_bulk.NGS_BULK_URL, "stations": stations}
