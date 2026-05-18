# Guatemala [GT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (updated 2026-05-12: official IGN site `www.ign.gob.gt` is now reachable on port 80; Red Geodésica Activa CORS interactive map confirms 16 named stations; still no public NTRIP caster) (refresh 2026-05-17: ign.gob.gt now ECONNREFUSED from this sandbox; no change to NTRIP status — still no public caster published)

## Status: UNKNOWN — CORS network exists (16+ named stations); public NTRIP streaming unconfirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — no public host:port published |
| **Operator** | Instituto Geográfico Nacional (IGN) Guatemala |
| **Network name** | Red Geodésica Activa CORS — IGN Guatemala (16 named CORS visible in IGN geoportal as of 2026-05-12; programmatic target 17 stations) |
| **Station list (from `ign.gob.gt/geoportal/index_cors.html`, 2026-05-12)** | `elena`, `huehue`, `mita`, `tikal`, `morales`, `taxisco`, `chisec`, `chicaman`, `tinta`, `barillas`, `coate`, `cotzu`, `sayaxche`, `naranjo`, `poptun`, `gualan` |
| **host:port** | Not publicly documented; the `sitios-cors.html` page on ign.gob.gt that the geoportal links to returns a near-empty body (9 bytes); no NTRIP caster endpoint, sourcetable, or mountpoint catalogue is exposed |
| **tariff** | RINEX data via Marketing & Sales; no NTRIP tariff published. Contact: info@ign.gob.gt · +502 2248-8100 |
| **hobbyist_eligibility** | Unknown — data access requires contacting IGN Marketing & Sales; no individual/hobbyist process described |
| **legal_residency_required** | Unknown |
| **last_confirmed_alive** | 2026-05-12 — `http://www.ign.gob.gt/` returned HTTP 200 (Apache/2.4.41 Ubuntu, Last-Modified 2026-02-19); Red Geodésica page (`redgeodesica.html`) loads and embeds an active CORS map via WMS layer `cartografia_basica:Red Geodesica Activa CORS` served from `ign.gob.gt/geoserver/wms`. The site has clearly been redeveloped since the 2026-05-06 check (was ECONNREFUSED then). No NTRIP caster endpoint advertised. |
| **datum_epoch** | omitted — no citable declaration. IGN's `redgeodesica.html` and the geoportal CORS map describe national reference frame conversion ("conversión al sistema de referencia nacional") for cadastral surveys but do not publish a datum/epoch declaration; GTM / GTRS is known informally but not directly declared by IGN on the portal pages reachable 2026-05-12. |

## Most Recent Project Announcement

**IGN Guatemala Red Geodésica Activa CORS** — 16 named CORS stations visible in the live IGN geoportal map (`ign.gob.gt/geoportal/index_cors.html`) as of 2026-05-12; the underlying GeoServer WMS layer is `cartografia_basica:Red Geodesica Activa CORS`. Per the IGN's own description: "permitirá realizar levantamientos catastrales de manera rápida y eficiente en toda la República de Guatemala" — supporting catastral surveying with conversion to the national reference system. Establishment was technically and financially supported by the Registro de Información Catastral (RIC). The earlier Webnode mirror (last updated 2013-06-03) is now superseded by the live IGN portal; the IGN site itself has been redeveloped (current site copyright 2019, last modified 2026-02-19). No NTRIP caster or real-time service host:port has been announced publicly.

Sources:
- IGN Red Geodésica: http://www.ign.gob.gt/redgeodesica.html (HTTP 200, 2026-05-12)
- IGN geoportal CORS map: http://www.ign.gob.gt/geoportal/index_cors.html (HTTP 200, 2026-05-12; 16 stations enumerated by URL anchors)
- Legacy Webnode mirror (last updated 2013-06-03): https://ignguatemala5.webnode.es/red-cors/

## Context Notes

- **16 named CORS stations** distributed nationally and visible in the live IGN geoportal as of 2026-05-12; the legacy reference of 17 stations remains the programmatic target (one station may be inactive or deferred). Primary purpose is cadastral surveying and relating field measurements to Guatemala's national reference frame (GTM / GTRS). Data distributed in RINEX 2.11.
- NOAA's NGS CORS network lists a Guatemala City station (GUAT) in the CORS catalog — this is a single shared station, not the IGN national CORS network.
- There is **no evidence** in any public NTRIP registry (BKG sourcetable, rtcm-ntrip.org, RTK2go monitor) of a Guatemalan NTRIP caster actively streaming, as of 2026-05-06.
- ArduSimple's Guatemala page explicitly states: "As far as we know, Guatemala does not have a National RTK Network. If you know of any, please contact us." (as of Aug 2025 snapshot).
- **Registro Nacional** (RNP) of Guatemala operates its own GNSS stations for cadastral purposes (rnpdigital.com) — these appear to feed RINEX data for post-processing only; no NTRIP streaming found.
- Practical alternative for hobbyists: Set up a local base station for single-base RTK; Galileo HAS for ~40 cm; GEODNET or Onocoy (global networks, coverage uncertain in Guatemala).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGN Guatemala CORS RINEX** — contact Marketing & Sales: info@ign.gob.gt · +502 2248-8100 | http://www.ign.gob.gt (ECONNREFUSED 2026-05-06) | Unknown (institutional purchase) |
| **NOAA NGS CORS — GUAT station** (Guatemala City) | https://geodesy.noaa.gov/CORS/ | Free |
| **EarthScope GNSS Data Archive** (post-UNAVCO retirement 2025-07-29; regional Caribbean/Central American IGS sites) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |
| **SIRGAS station data** | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |

## Sources Consulted
- IGN Guatemala official site (HTTP 200 2026-05-12, ECONNREFUSED 2026-05-06): http://www.ign.gob.gt
- IGN Guatemala Red Geodésica page (HTTP 200 2026-05-12, lists Red Geodésica Activa CORS): http://www.ign.gob.gt/redgeodesica.html
- IGN Guatemala geoportal CORS map (16 stations enumerated 2026-05-12): http://www.ign.gob.gt/geoportal/index_cors.html
- IGN Guatemala GeoServer WMS legend (`Red Geodesica Activa CORS`): http://www.ign.gob.gt/geoserver/wms
- IGN Guatemala CORS Webnode mirror (last updated 2013-06-03): https://ignguatemala5.webnode.es/red-cors/
- ArduSimple Guatemala (no national RTK listed): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-guatemala/
- NOAA NGS CORS — GUAT station: https://geodesy.noaa.gov/CORS/
- SIRGAS station list: https://sirgas.ipgh.org/en/gnss-network/stations/station-list/
