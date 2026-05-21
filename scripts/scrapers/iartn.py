"""Iowa Real-Time Network — ArcGIS FeatureServer scraper.

Source: Iowa DOT GIS layer for RTN base stations. Layer returns ~105
features (85 Iowa-prefix + ~20 cross-state from MN, MO, WI, SD that
contribute to the IaRTN solution). We keep them all — cross-border
stations are real receivers that show up in the IaRTN sourcetable.

Station identifier: NGS-style 4-letter code in the `NGS_ID` attribute
(e.g. `IAAM` for Ames). Features with a blank `NGS_ID` are dropped by
the ArcGIS helper — Iowa DOT's data consistently populates the field.
"""
from __future__ import annotations

from . import _arcgis

LAYER_URL = (
    "https://gis.iowadot.gov/agshost/rest/services/Survey/"
    "RTN_Base_Stations/FeatureServer/0"
)


def scrape() -> dict:
    return _arcgis.scrape_layer(
        layer_url=LAYER_URL,
        name_field="NGS_ID",
        country="USA",
    )
