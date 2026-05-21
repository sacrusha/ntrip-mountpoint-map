"""West Virginia Real-Time Network — WVU ArcGIS MapServer scraper.

Source: WVGIS layer hosted at WVU for WV CORS stations. Layer returns
~24 features 2026-05-21 (operator portal claims 32; GIS layer may be a
subset). All names use the WV-prefix NGS-style convention (e.g. WVAT,
WVCH).

Station identifier: `Name` attribute. Note casing — this MapServer uses
mixed-case field names, distinct from the IA/VT FeatureServers.
"""
from __future__ import annotations

from . import _arcgis

LAYER_URL = (
    "https://services.wvgis.wvu.edu/arcgis/rest/services/"
    "Location/wv_CORS/MapServer/0"
)


def scrape() -> dict:
    return _arcgis.scrape_layer(
        layer_url=LAYER_URL,
        name_field="Name",
        country="USA",
    )
