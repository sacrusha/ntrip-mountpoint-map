# Gambia [GM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (refresh; `py scripts/stations_by_country.py GMB` → empty. Nearest hits within 500 km of Banjul: 2 SEN Centipede (NKHR 118 km, GORA 164 km) + IGS-IP DAKR (164 km) — all SENCORS-territory Senegal, none in The Gambia. SENCORS network does not extend coverage into GM.)

## Status: NO — no public NTRIP RTK caster found; no national CORS network identified

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **landing_url** | null — no national operator portal identified |
| **access_url** | null — no service exists |
| **host:port** | null |
| **num_stations** | null — no national CORS network identified |
| **vrs** | null — no service exists |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **datum_epoch** | null — no operator declaration to cite |
| **National CORS / GNSS reference network** | None identified |
| **Post-processing RINEX** | None publicly available from national agency |
| **last_confirmed_alive** | N/A |

## Context Notes

- **No national RTK network**: No evidence of a Gambian national CORS network, NTRIP caster, or real-time GNSS correction service as of 2026-05-21. The Gambia has no entry in ntrip-list.com, EUREF, or any CORS registry.
- **Survey and Mapping agency**: The Gambia's geospatial authority is the Department of Lands and Regional Planning under the Ministry of Lands, Regional Government & Religious Affairs (`molrg.gov.gm`, fetched 2026-05-21). The ministry website publishes department pages but no NTRIP / CORS / sourcetable / real-time GNSS service. Public evidence of geodetic CORS infrastructure is absent.
- **GIS capacity building**: The UN Technology Bank for LDCs delivered GIS/Earth Observation training in Serrekunda in 2022–2023 (disaster risk reduction focus), but this did not include RTK or CORS deployment.
- **Continental context**: Senegal now runs SENCORS (`caster.geodesie.sn:2101`, paid subscription, live 2026-05-21); coverage extends to the SN border but no SENCORS station is located inside The Gambia. The nearest IGS tracking station is DAKR (Dakar, Senegal, ~164 km from Banjul), which provides RINEX data and is also published as a real-time mountpoint on the IGS-IP caster.
- **Volunteer / hobbyist casters**: No RTK2go, Centipede, or EarthScope stations in The Gambia (2026-05-21). No GMB country code present in any source.
- **GNSS for agriculture / development**: QZSS MADOCA and Galileo HAS provide free globally broadcast corrections at sub-meter level, usable in the Gambia with appropriate receivers, but these are not network RTK casters.

## Most Recent Project Announcement

No project announcement for a Gambian RTK or CORS network was found. The most recent geospatial infrastructure activity identified is the UN Technology Bank GIS training programme (2023):
- Source: https://www.un.org/technologybank/node/977

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive** — DAKR (Dakar, Senegal, ~164 km from Banjul); global archive (UNAVCO URLs retired 2025-07-29; superseded by EarthScope) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |

## Sources Consulted
- NTRIP-list.com Africa: https://ntrip-list.com/africa/ (no Gambia entry)
- Ministry of Lands, Regional Government & Religious Affairs (Gambia): https://molrg.gov.gm/ — no NTRIP / CORS service page (re-fetched 2026-05-21)
- RTK2go sourcetable — no GM stations 2026-05-21
- UN Technology Bank GIS training Gambia: https://www.un.org/technologybank/node/977
- HDX Gambia administrative boundaries: https://data.humdata.org/dataset/cod-ab-gmb
- IGS station search (DAKR): https://www.igs.org/
- WebSearch 2026-05-21 (Gambia CORS GNSS NTRIP 2025 2026; Bissau/Banjul CORS GNSS) — no project or caster surfaced
- Local data: `py scripts/stations_by_country.py GMB` → empty (2026-05-21)
