# Barbados [BB] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO public NTRIP caster; no dedicated Barbados RTK stream identified; RINEX only via EarthScope if Barbados station participates in NOTA

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Free RINEX / post-processing** | Unclear — no confirmed Barbados station in EarthScope/NOTA real-time stream as of 2026-05-06 |
| **Volunteer rtk2go coverage** | No confirmed BRB-coded stations |
| **hobbyist_eligibility** | n/a (no caster) |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | n/a |
| **Most recent project announcement** | None found as of 2026-05-06 |

## Context Notes

- **No public RTK correction service operates in Barbados.** Extensive search across government geodesy portals, Caribbean GNSS networks (COCONet/NOTA), and hobbyist/professional forums found no active NTRIP caster with Barbados-origin streams.
- **Lands & Surveys Department, Barbados:** Responsible for cadastral and geodetic surveying. No CORS infrastructure or NTRIP service was found on any associated public portal. (barbados.gov.bb).
- **COCONet / EarthScope NOTA:** The Caribbean GPS Observational Network (COCONet) integrated into EarthScope's Network of the Americas (NOTA) covers many Caribbean island stations. The EarthScope real-time NTRIP caster (`ntrip.earthscope.org:2101`) confirmed live on 2026-05-06. A query for Barbados-coded mountpoints (BRB, BARB, BDOS, BIMK) returned no results, suggesting either Barbados has no COCONet station, or its station is not in the real-time stream.
- **No volunteer rtk2go or Centipede coverage** for Barbados was found in current sourcetables.
- **Practical RTK in Barbados:** Field practitioners rely on a local base station setup (owned rover + base pair) or global commercial correction services (PointPerfect, StarFire). No free NTRIP path has been identified.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **Barbados Lands & Surveys Dept** | https://www.barbados.gov.bb/ministries-departments/lands-surveys-department | Unknown — contact department directly |
| **EarthScope / NOTA** (if Barbados station exists) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- EarthScope NOTA real-time NTRIP caster (`ntrip.earthscope.org:2101`) — confirmed live, no BRB mountpoints found 2026-05-06
- EarthScope GNSS real-time data: https://www.earthscope.org/data/gnss-realtime/ (observed 2026-05-06)
- NOTA network description: https://www.earthscope.org/nota/ (observed 2026-05-06)
- EarthScope new streaming platform announcement: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/ (observed 2026-05-06)
- Barbados government services: https://www.barbados.gov.bb/ (observed 2026-05-06) — no GNSS/NTRIP service found
