# Qatar [QA] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

One government NRTK network — QCORS (CGIS, Ministry of Municipality), 9
CORS stations covering the peninsula, runs on a Leica Spider Business
Center portal at `qcors.gisqatar.org.qa`. Subscription is gated to
registered companies / professional users; no published tariff, no
hobbyist tier confirmed. The NTRIP caster on port 2101 TCP times out from
non-QA IPs (probed 2026-05-23). No commercial alternative covers Qatar.
No rtk2go / Centipede / EarthScope / IGS-IP stations in the country
2026-05-23.

## Casters

### QCORS — Qatar Continuously Operating Reference Stations

- operator: CGIS — Centre for GIS, Ministry of Municipality (State of Qatar)
- landing_url: https://www.gisqatar.org.qa/ (CGIS landing; the gisqatar.org.qa
  domain rejects WebFetch with empty body 2026-05-23 — likely SPA / IP-geo
  gated; navigation indexes via WebSearch)
- access_url: http://qcors.gisqatar.org.qa/SBC/ (Leica Spider Business
  Center login portal; "GNSS User Access and Subscription Management
  Solution" — confirmed live 2026-05-23 via WebSearch result listing.
  Direct WebFetch returned ECONNREFUSED from sandbox 2026-05-23, consistent
  with IP-geo gating.)
- access_type: restricted — service description on CGIS profile is
  "government and private survey and mapping communities"; QCORS landing
  is the Spider Business Center login (no self-service registration link
  exposed); rover users are described in academic literature as
  "registered companies" with no individual tier. Tariff is not published
  (checked: gisqatar.org.qa 2026-05-23 WebFetch — empty body; UN-GGIM
  CGIS exchange-forum 2013 PDF 2026-05-23 via WebSearch; geospatialworld
  CGIS profile 2026-05-23; flypix.ai Qatar geospatial directory
  2026-05-23 via WebSearch).
- coverage: full Qatar peninsula (~11,586 km²); ±2 cm horizontal / ±10 cm
  vertical claimed across the territory by CGIS
- num_stations: 9 (per CGIS exchange-forum presentation; reproduced in
  geospatialworld profile)
- hobbyist_eligibility: no — described as serving "government and private
  survey and mapping communities" requiring subscription; no individual /
  hobbyist tier documented or publicly self-serviceable
- residency_required: ? — no explicit residency clause found on the public
  CGIS / QCORS surface (checked: gisqatar.org.qa 2026-05-23 WebFetch
  empty; geospatialworld CGIS profile 2026-05-23 via WebSearch). In
  practice access is via direct application to CGIS and is QA-business-
  oriented.
- datum_epoch: omitted — no citable operator declaration of the NTRIP
  output frame is exposed on the gisqatar.org.qa surface. QND95 (Qatar
  National Datum 1995) is documented as the legacy national projection
  basis but is not the GNSS reference frame; the QCORS modern frame is
  not operator-declared on any accessible page.

NTRIP technical surface — `qcors.gisqatar.org.qa` resolves to
89.211.33.57; direct TCP probe to port 2101 timed out 2026-05-23. The
`qcors.gisqatar.org.qa/SBC/` Spider Business Center login is consistent
with a Leica GNSS Spider caster identical in software to OmanCORSnet
and many HxGN SmartNet affiliates — which on every comparable
deployment expose VRS / MAX / Nearest mountpoints to subscribers — but
no QCORS-specific VRS confirmation is published by CGIS and the
sourcetable cannot be read from outside QA without authentication. The
VRS inference is platform-level, not operator-declared.

CGIS contact: +974 4426 6284 (tel); cgisinfo@gisqatar.org.qa (email);
portal https://www.gisqatar.org.qa/.

## Disqualified / not applicable

- **rtk2go, Centipede, EarthScope, IGS-IP** — 0 QA mountpoints
  2026-05-23: `py scripts/stations_by_country.py QAT` →
  "No stations for 'QAT'". `py scripts/stations_by_radius.py 25.3 51.5 200`
  → no stations within 200 km of Doha on any tracked source.
- **GEODNET, onocoy, PointOne, HxGN SmartNet, Trimble VRS Now** — no
  Qatar coverage advertised in public documentation 2026-05-23.
- **ArduSimple Qatar** — no dedicated country page indexed under
  `ardusimple.com/rtk-correction-services-and-ntrip-casters-in-qatar/`
  2026-05-23 (404).
- **"FIFA 2022 World Cup legacy" CORS** — no open-access NTRIP network
  beyond QCORS announced.

## Post-Processing (RINEX) fallback

| Service | URL | Notes |
|---|---|---|
| CGIS / QCORS RINEX | https://www.gisqatar.org.qa/ | Same Spider Business Center subscription required |
| IGS / EarthScope | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; no IGS station in Qatar 2026-05-23 |

## Sources Consulted

- CGIS landing: https://www.gisqatar.org.qa/ (2026-05-23 WebFetch
  returned empty body — page SPA-rendered or IP-geo gated)
- QCORS Spider Business Center login (confirmed live via WebSearch index
  2026-05-23; direct fetch ECONNREFUSED from sandbox):
  http://qcors.gisqatar.org.qa/SBC/
- CGIS Services (PageId=3): https://www.gisqatar.org.qa/en/page3/test.html
- CGIS About (PageId=1): https://gisqatar.org.qa/en/page1/test.html
- CGIS GeoPortal (web mapping; not QCORS):
  https://geoportal.gisqatar.org.qa/qmape/
- CGIS profile on Geospatial World Resource Platform (2026-05-23 via
  WebSearch): https://resource.geospatialworld.net/user/centre-for-gis-qatar-cgis
- UN-GGIM Exchange Forum 2013 — Qatar GIS Cooperation:
  https://ggim.un.org/ggim_20171012/docs/meetings/Exchange_Forum_2013/Opening%20Remarks/ExchangeForum_CGIS-Qatar_El-WahabHamouda.pdf
- Qatar Survey Manual (community mirror, PDF):
  https://pdfcoffee.com/qatar-survey-manual-pdf-free.html
- flypix.ai — Geospatial Companies in Qatar (2026-05-23 via WebSearch):
  https://flypix.ai/geospatial-companies-in-qatar/
- ArduSimple country listing (no Qatar entry 2026-05-23):
  https://www.ardusimple.com/rtk-correction-services-in-your-country/
- Direct TCP probe 2026-05-23 of `qcors.gisqatar.org.qa:2101`
  (89.211.33.57) → connection timed out after 8 s
- Local data 2026-05-23: `py scripts/stations_by_country.py QAT` →
  no stations; `py scripts/stations_by_radius.py 25.3 51.5 200` → no
  stations within 200 km of Doha.
