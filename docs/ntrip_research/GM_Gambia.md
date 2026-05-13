# Gambia [GM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry; no new CORS / NTRIP activity surfaced)

## Status: NO — no public NTRIP RTK caster found; no national CORS network identified

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **National CORS / GNSS reference network** | None identified |
| **Post-processing RINEX** | None publicly available from national agency |
| **last_confirmed_alive** | N/A |

## Context Notes

- **No national RTK network**: Extensive searching found no evidence of a Gambian national CORS network, NTRIP caster, or real-time GNSS correction service as of 2026-05-12. The Gambia has no entry in ntrip-list.com, EUREF, or any CORS registry.
- **Survey and Mapping agency**: The Gambia's geospatial authority is the Department of Lands and Regional Planning under the Ministry of Lands and Regional Government. Public evidence of geodetic CORS infrastructure is absent.
- **GIS capacity building**: The UN Technology Bank for LDCs delivered GIS/Earth Observation training in Serrekunda in 2022–2023 (disaster risk reduction focus), but this did not include RTK or CORS deployment.
- **Continental context**: West Africa has very sparse public RTK infrastructure. Regional neighbors (Senegal, etc.) also lack a free public NTRIP caster. The nearest IGS tracking station is DAKA (Dakar, Senegal, ~160 km from Banjul), which provides RINEX data for post-processing but no real-time NTRIP stream accessible to public users.
- **Volunteer / hobbyist casters**: No RTK2go, Centipede, or EarthScope stations were found in the Gambia sourcetable as of 2026-05-12 (verified via local `data/stations.json`). No GMB country code present in any source.
- **GNSS for agriculture / development**: QZSS MADOCA and Galileo HAS provide free globally broadcast corrections at sub-meter level, usable in the Gambia with appropriate receivers, but these are not network RTK casters.

## Most Recent Project Announcement

No project announcement for a Gambian RTK or CORS network was found. The most recent geospatial infrastructure activity identified is the UN Technology Bank GIS training programme (2023):
- Source: https://www.un.org/technologybank/node/977

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGS / EarthScope** — DAKAR (DAKA) station, Senegal (~160 km) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **UNAVCO / IGS** — global archive | https://www.unavco.org/ | Free non-commercial |

## Sources Consulted
- NTRIP-list.com Africa: https://ntrip-list.com/africa/ (no Gambia entry)
- RTK2go sourcetable — no GM stations confirmed 2026-05-12
- UN Technology Bank GIS training Gambia: https://www.un.org/technologybank/node/977
- HDX Gambia administrative boundaries: https://data.humdata.org/dataset/cod-ab-gmb
- IGS station search (REYK, DAKA): https://www.igs.org/
- WebSearch 2026-05-12 ("Gambia CORS GNSS NTRIP reference station Department of Lands 2025 2026") — no project or operational caster surfaced
