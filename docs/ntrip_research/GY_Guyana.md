# Guyana [GY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (CORS infrastructure present, no public NTRIP endpoint) |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has been confirmed alive |

## Most Recent Project Announcement

**GLSC CORS network (2018–2019)** — Guyana Lands and Surveys Commission engaged Ordnance Survey International on a GYD 93M (~USD 443k at 2018 exchange rate) contract to build an 8-station national CORS network connected to ITRF2014/SIRGAS, with a Network Operations Centre. Stations commissioned across Regions 1, 2, 4, 6, 7, 9, and 10 (Eclipse Falls, Supenaam, Georgetown, New Amsterdam, Olive Creek, Lethem, Linden). No public NTRIP host:port has ever been published; no announcement of a public real-time service has appeared since commissioning.

Source: https://guyanachronicle.com/2018/07/12/93m-contract-signed-to-get-reference-stations-on-stream/ · https://dpi.gov.gy/reference-stations-to-assist-land-surveys/

## Context Notes

- **GLSC CORS**: 8-station network operated by the Guyana Lands and Surveys Commission (Regions 1, 2, 4, 6, 7, 9, 10). Connected to ITRF2014/SIRGAS reference frame. Equipment installation and Network Operations Centre delivered by Ordnance Survey International. Used internally for cadastre and geodetic reference; not exposed as a public NTRIP RTK service. Individual station 4-character IDs have not been published publicly; the network does not appear in the SIRGAS-CON analysis centre station list as of 2026-05-06.
- **No public sourcetable** has been observed; absent from NTRIP-list.com Caribbean/South-America tables and from RTK2go community casters.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede-RTK, PointOne): no Guyana coverage confirmed.
- Practical workaround for hobbyists: deploy a local base station for single-base RTK, or use satellite-based PPP services (Trimble RTX, u-blox PointPerfect where available).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / GAGE** — no GLSC CORS stations confirmed in SIRGAS-CON or EarthScope archive as of 2026-05-06; DGFI-TUM SIRGAS analysis centre station list has no Guyana entries | https://www.earthscope.org/data/gnss-data/ | N/A |
| **GLSC NOC** — RINEX from the 8-station network is not published via any known portal; request via glsc.gov.gy or the GLSC Network Operations Centre directly | https://glsc.gov.gy/ | Unknown (direct contact) |

## Sources Consulted
- GLSC official site (HTTP 200 confirmed 2026-05-06): https://glsc.gov.gy/
- GLSC Lands portal: https://lands.glsc.gov.gy/
- Guyana Chronicle — GYD $93M OS International CORS contract (2018-07-12): https://guyanachronicle.com/2018/07/12/93m-contract-signed-to-get-reference-stations-on-stream/
- DPI Guyana — Reference stations article (station locations listed): https://dpi.gov.gy/reference-stations-to-assist-land-surveys/
- Ordnance Survey International — Guyana case study: https://www.ordnancesurvey.co.uk/customers/case-studies/empowering-guyanas-national-mapping-agency
- SIRGAS-CON station list (Guyana absent): https://www.sirgas.org/en/stations/station-list/
- NTRIP-list.com Caribbean/South America: https://ntrip-list.com/
- GEODNET coverage map: https://geodnet.com/
