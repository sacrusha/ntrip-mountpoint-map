# Guinea-Bissau [GW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-verified; `py scripts/stations_by_country.py GNB` → empty; status unchanged. Nearest hits within 500 km of Bissau: 2 SEN Centipede nodes (NKHR 304 km, GORA 375 km) + IGS-IP DAKR (376 km) + rtk2go Gine-Albrk in Guinea-Conakry 331 km — all beyond RTK range.)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Most Recent Project Announcement

No Guinea-Bissau-specific CORS/NTRIP project announcement found in any public source.

**EGNOS-Africa / ASECNA SBAS** (excluded — SBAS only, not RTK):
ESA–ASECNA agreement signed 2022-06-30; Guinea-Bissau is one of 18 ASECNA member states in scope. Delivers metre-class SBAS for aviation only — out of scope.
URL: https://www.esa.int/Applications/Satellite_navigation/EGNOS_technology_for_Africa_ESA_signs_deal_with_ASECNA

**World Bank / Spatial Dimension mining cadastre** (Apr 2015): Established mining cadastre software for Guinea-Bissau — no CORS/NTRIP component.
URL: https://spatialdimension.com/projects/guinea-bissau-ministry-of-energy-industry-natural-resources/

## Context Notes

- No known continuously operating GNSS reference station of any kind in Guinea-Bissau — neither IGS-affiliated, community-hosted, nor commercially operated.
- No GW station in: IGS network, EarthScope/GAGE archive, M³G metadata registry, AFREF/WAFREF.
- Country's geodetic infrastructure remains based on legacy Bissau datum (EPSG:4165).
- GIM International 25-country CORS Africa map does not include Guinea-Bissau.
- Global commercial networks (GEODNET, ONOCOY, Centipede-RTK, RTKdata): No GW coverage.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| None — no GNSS CORS station of any kind exists in Guinea-Bissau. No RINEX archive available from any source. | — | — |

## Sources Consulted
- IGS network.igs.org — 0 results for GW
- RTK2GO, M³G metadata registry (gnss-metadata.eu)
- EarthScope/GAGE archive
- AFREF/WAFREF published networks
- ArduSimple country directory, corsstations.com
- GIM International CORS Africa map
- GitHub mvarga1989 CORS list
- ESA/ASECNA EGNOS-Africa
- Local data 2026-05-21: `py scripts/stations_by_country.py GNB` → 0; `py scripts/stations_by_radius.py 11.86 -15.59 500` → 4 stations all in SEN/GIN, none in GW
- WebSearch 2026-05-21 (Bissau / Guinea-Bissau CORS GNSS NTRIP 2024–2026) — no project surfaced
