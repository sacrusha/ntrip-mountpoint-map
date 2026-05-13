# Barbados [BB] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: NO public NTRIP caster; no dedicated Barbados real-time stream identified; no free volunteer base; nearest EarthScope CN station ~160 km away on Saint Lucia

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Free RINEX / post-processing** | No confirmed Barbados-resident station in current EarthScope/NOTA stream listing |
| **Volunteer rtk2go coverage** | Zero BRB-coded stations (verified via `data/stations.json` 2026-05-12) |
| **Centipede coverage** | None |
| **EarthScope / NOTA coverage** | No BRB station in current snapshot; nearest NOTA streams are `CN47_RTCM3P3` (~162 km, St. Lucia) and `CN04_RTCM3P3` (~181 km, St. Lucia) — both well beyond usable RTK baseline |
| **hobbyist_eligibility** | n/a (no caster) |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | n/a |
| **Most recent project announcement** | None found 2024–2026 |

## Context Notes

- **No public RTK correction service operates in Barbados.** Extensive search across government geodesy portals, Caribbean GNSS networks (COCONet/NOTA), and hobbyist/professional forums found no active NTRIP caster with Barbados-origin streams.
- **Lands & Surveys Department, Barbados** (`barbados.gov.bb/ministries-departments/lands-surveys-department`): responsible for cadastral and geodetic surveying. No CORS infrastructure or NTRIP service on any associated public portal.
- **COCONet / EarthScope NOTA**: The Caribbean GPS Observational Network (COCONet) integrated into EarthScope's Network of the Americas (NOTA) covers many Caribbean island stations. The EarthScope real-time NTRIP caster (`ntrip.earthscope.org:2101`) is confirmed live. A check for Barbados-coded mountpoints (BRB, BARB, BDOS, BIMK) in the current `data/stations.json` snapshot returned no results, suggesting either Barbados has no COCONet station, or any existing station is not in the public real-time stream.
- **Nearest free streams** within ~200 km: two EarthScope NOTA stations on Saint Lucia (`CN47_RTCM3P3` at 13.71°N −60.94°W, ~162 km; `CN04_RTCM3P3` at 14.02°N −60.97°W, ~181 km). Both are well beyond reliable RTK baseline (~30 km) — useful only for low-precision DGNSS or post-processing reference.
- **No volunteer rtk2go or Centipede coverage** for Barbados in current sourcetables.
- **Practical RTK in Barbados**: field practitioners rely on a local base station setup (owned rover + base pair) or global commercial services (PointPerfect, StarFire, Skylark — coverage in BB not confirmed). Galileo HAS (~40 cm) is the only no-infrastructure free option.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **Barbados Lands & Surveys Dept** | https://www.barbados.gov.bb/ministries-departments/lands-surveys-department | Unknown — contact department directly |
| **EarthScope / NOTA** (Saint Lucia stations CN04, CN47) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |

## Sources Consulted
- EarthScope real-time NTRIP caster `ntrip.earthscope.org:2101` — checked via `data/stations.json` 2026-05-12, no BRB mountpoints
- EarthScope GNSS real-time data: https://www.earthscope.org/data/gnss-realtime/
- NOTA network description: https://www.earthscope.org/nota/
- EarthScope streaming platform transition: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- Barbados government services: https://www.barbados.gov.bb/
- `data/stations.json` 2026-05-12 — zero BRB entries on rtk2go, Centipede, or EarthScope; nearest stations CN47 (~162 km) and CN04 (~181 km) on St. Lucia
