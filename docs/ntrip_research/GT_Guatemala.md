# Guatemala [GT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (IGN geoportal CORS station codes refreshed — 17 markers including GUAT/IGS; new IGN station codes ELEN HUEH CATR TIKA MRLS TAXI CHIS CHIQ TINT BARI COAT COTZ SAYA NARA POPT ZACA — supersedes 2026-05-12 lower-case Webnode names; ign.gob.gt main site HTTP 200 again)

## Status: UNKNOWN — IGN-GT Red Geodésica Activa CORS exists (16 IGN stations + 1 IGS); no public NTRIP caster published. RINEX access procedure undocumented for hobbyists. ArduSimple says "Guatemala does not have a National RTK Network."

| Field | Value |
|---|---|
| Public NTRIP RTK caster | No public host:port published |
| Operator | Instituto Geográfico Nacional (IGN) Guatemala |
| Network name | Red Geodésica Activa CORS — IGN Guatemala |
| landing_url | http://www.ign.gob.gt/redgeodesica.html (operator overview page, HTTP 200 2026-05-22) |
| access_url | Skip — no public registration page exists; RINEX requires institutional contact via Marketing & Sales (info@ign.gob.gt, +502 2248-8100) |
| Stations visible in geoportal (2026-05-22) | 16 IGN-managed: ELEN HUEH CATR TIKA MRLS TAXI CHIS CHIQ TINT BARI COAT COTZ SAYA NARA POPT ZACA + 1 IGS station (GUAT, 14.58 N -90.54 — Guatemala City) marketed separately. The geoportal iframe (`geoportal/index_cors.html`) embeds 17 markers total |
| num_stations | 16 IGN-operated CORS (programmatic target 17 — one station name may be inactive or deferred) |
| host:port | None published — neither IGN nor RIC pages expose a NTRIP caster host, sourcetable URL or mountpoint catalogue |
| vrs | n/a — no caster |
| tariff | RINEX data delivered via Marketing & Sales contact; no public tariff schedule. No NTRIP tariff (no NTRIP product) |
| hobbyist_eligibility | Unknown — institutional/cadastral focus; individual purchase path undocumented |
| legal_residency_required | Unknown |
| last_confirmed_alive | 2026-05-22 — `http://www.ign.gob.gt/` HTTP 200 (Apache/2.4.41 Ubuntu, Last-Modified 2026-02-19); `redgeodesica.html` HTTP 200 (Last-Modified 2025-01-14); `geoportal/index_cors.html` HTTP 200 (Last-Modified 2025-02-25). No NTRIP endpoint advertised on any of these pages |
| datum_epoch | omitted — no citable declaration. IGN's `redgeodesica.html` describes "conversión sencilla al Sistema de Referencia Nacional" for cadastral surveys but does not publish a datum/epoch on the indexed portal pages; GTM / GTRS is the informally referenced national frame but not declared on any operator page for the CORS network |

## Context

- Primary purpose of the IGN CORS network: cadastral surveying (RIC — Registro de Información Catastral — provided technical and financial support for establishment). Data distributed in RINEX 2.11 historically.
- The geoportal iframe lives at `http://www.ign.gob.gt/geoportal/index_cors.html` and embeds 17 Leaflet markers; per-station detail pages (`/sitios-cors.html#<name>`) link back to the legacy lowercase names (`elena`, `huehue`, ...) but the geoportal payload itself now uses the uppercase 4-character codes listed above.
- NOAA NGS / IGS station `GUAT` (Guatemala City) is a single shared international station, not part of the IGN-GT operational caster.
- Registro Nacional (RNP) of Guatemala operates additional GNSS stations for cadastral purposes (rnpdigital.com) — RINEX post-processing only, no NTRIP streaming found.
- ArduSimple Guatemala (https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-guatemala/, fetched 2026-05-16) explicitly states: "as far as we know Guatemala is not among them" (i.e. countries with a national RTK network). No commercial NTRIP reseller publishes Guatemala coverage on indexed product pages.
- **No GT-coded stations in any local pipeline source** — `py scripts/stations_by_country.py GTM` returns "No stations" (2026-05-22). No EarthScope, IGS-IP, rtk2go or Centipede coverage inside GT territory.
- Practical hobbyist alternatives in GT: local own-base RTK, Galileo HAS (~40 cm), GEODNET / Onocoy (coverage uncertain).

## Most Recent Project Announcement

IGN Guatemala Red Geodésica Activa CORS remains the live programme as of 2026-05-22; geoportal still embeds the active CORS map served via GeoServer WMS layer `cartografia_basica:Red Geodesica Activa CORS`. The earlier Webnode mirror (last updated 2013-06-03) is fully superseded by the current IGN site. No announcement of a public NTRIP / real-time RTK caster has been published.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| IGN Guatemala CORS RINEX (via Marketing & Sales: info@ign.gob.gt · +502 2248-8100) | http://www.ign.gob.gt/redgeodesica.html | Unknown (institutional purchase) |
| NOAA NGS CORS — GUAT station (Guatemala City) | https://geodesy.noaa.gov/CORS/ | Free |
| EarthScope GNSS Data Archive (regional Caribbean/Central American IGS sites) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |
| SIRGAS station data | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |

## Sources

- IGN Guatemala official site: http://www.ign.gob.gt (HTTP 200 2026-05-22)
- IGN Red Geodésica page: http://www.ign.gob.gt/redgeodesica.html (HTTP 200 2026-05-22)
- IGN geoportal CORS map (16 IGN + GUAT = 17 markers enumerated 2026-05-22): http://www.ign.gob.gt/geoportal/index_cors.html
- IGN GeoServer WMS (layer `Red Geodesica Activa CORS`): http://www.ign.gob.gt/geoserver/wms
- ArduSimple Guatemala (no national RTK): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-guatemala/
- NOAA NGS CORS — GUAT station: https://geodesy.noaa.gov/CORS/
- SIRGAS station list: https://sirgas.ipgh.org/en/gnss-network/stations/station-list/
- Local pipeline `py scripts/stations_by_country.py GTM` 2026-05-22: no stations
