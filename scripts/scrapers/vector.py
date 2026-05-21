"""Vermont VECTOR — VTrans Geodetic CORS ArcGIS FeatureServer scraper.

Source: VTrans GIS layer for Vermont CORS stations (~19 features as of
2026-05-21). All entries are Vermont-owned receivers; no cross-border
filter needed.

Station identifier: 4-letter code in the `ID` attribute (e.g. `VTBE`,
`VCAP`); `NAME` field carries the long human name.
"""
from __future__ import annotations

from . import _arcgis

LAYER_URL = (
    "https://maps.vtrans.vermont.gov/arcgis/rest/services/"
    "Geodetic/CORS/FeatureServer/0"
)


def scrape() -> dict:
    return _arcgis.scrape_layer(
        layer_url=LAYER_URL,
        name_field="ID",
        country="USA",
    )
