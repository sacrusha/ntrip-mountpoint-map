# Belize [BZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revising 2026-05-06 entry)

## Status: PARTIAL — single EarthScope NOTA station now live in central Belize (CN23_RTCM3P3, free non-commercial NULA). No national CORS / no Belize-operated public caster.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (Belize-operated)** | No |
| **Active public NTRIP RTK mountpoint physically in Belize** | Yes — `ntrip.earthscope.org:2101/CN23_RTCM3P3` (single NOTA station, 17.26°N, -88.78°E, Belmopan area) |
| **hobbyist_eligibility (EarthScope NOTA)** | Yes for non-commercial use — requires EarthScope account + signed NULA (Non-commercial User License Agreement) |
| **legal_residency_required** | No |
| **last_confirmed_alive (EarthScope CN23)** | 2026-05-12 — curl probe of `ntrip.earthscope.org:2101` returned `SOURCETABLE 200 OK` and listed `CN23_RTCM3P3` with country tag `BLZ`, position 17.26 / -88.78, RTCM 3.3, multi-constellation (GPS+GLO+BDS+GAL+SBAS+QZS), MSM7 messages 1077/1087/1097/1107/1117 |

## EarthScope NOTA — CN23 (new entry, observed 2026-05-12)

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` |
| **mountpoint** | `CN23_RTCM3P3` |
| **format** | RTCM 3.3 |
| **messages** | 1005(60), 1007(60), 1013(1), 1029(60), 1033(60), 1077(1), 1087(1), 1097(1), 1107(1), 1117(1) — full multi-system MSM7 |
| **constellations** | GPS + GLONASS + BeiDou + Galileo + SBAS + QZSS |
| **receiver** | Septentrio POLARX5 |
| **position** | 17.26°N, -88.78°E (central Belize, near Belmopan / Cayo District) |
| **carrier (Y/N)** | Y (carrier-phase available) |
| **fee (sourcetable field)** | `SEAT_REQUIRED` — requires an EarthScope seat (non-commercial NULA account is the standard free path) |
| **single-base usable radius** | ~30–50 km L1+L2 RTK; reaches most of Belize population centres (Belmopan, Belize City, San Ignacio, parts of Cayo / Belize / Orange Walk districts) |
| **Registration** | https://data.earthscope.org/ — create account, accept NULA, request real-time GNSS data access |

This is the first physically-in-Belize public NTRIP mountpoint to appear in our pipeline data; CN23 was not present in the 2026-05-06 EarthScope sourcetable observation. Consistent with EarthScope's documented NOTA epoch update of 2026-03-30.

## Other Status

No Belize-operated national NTRIP caster has been published as of 2026-05-12. The Surveys and Mapping Section (Ministry of Natural Resources, `naturalresources.gov.bz`) maintains horizontal and vertical control networks and supervises cadastral surveys but does not publish a CORS or NTRIP service. The Belize National Spatial Data Infrastructure portal (`portal.bnsdi.gov.bz`) provides only static map data.

## Context Notes

- **Surveys and Mapping Section** (Ministry of Natural Resources, `naturalresources.gov.bz/index.php/surveys-and-mappings-section/`): Responsible for all aspects of mapping including horizontal and vertical control; Principal Surveyor Kevin Gutierrez heads the section. No CORS or NTRIP infrastructure is mentioned on the website or in any indexed technical publication.
- **BNSDI** (`portal.bnsdi.gov.bz`): Belize National Spatial Data Infrastructure portal — only static map data and cadastral layers.
- **rtk2go / Centipede**: Zero BLZ-coded stations in either sourcetable as of 2026-05-12.
- **Border proximity**: Mexico (INEGI CORS, `ntrip.inegi.org.mx:2101`) and Guatemala (IGN-Guatemala, `rtk.igntopo.gob.gt:2101`) are the nearest non-NOTA options; useful where CN23 baseline exceeds practical reach (deep south / far north of Belize). With CN23 in central Belize, cross-border baselines are now secondary.
- **IGS / AFREF**: No IGS core or AFREF-affiliated station in Belize.
- **Gap assessment**: Belize is a small country (~23,000 km²) with a population of ~400,000. With CN23 now operational, single-base RTK is achievable across most of populated central Belize — the geodetic surveying community is small but no longer infrastructure-blank. No evidence of a Belize-operated CORS programme; EarthScope NOTA is the de-facto free option.

## Post-Processing (RINEX) Fallback

EarthScope GNSS Data Archive — CN23 RINEX should be available alongside the real-time feed under the same NOTA account. No national Belize RINEX archive.

## Sources Consulted
- Surveys and Mapping Section, Ministry of Natural Resources: https://naturalresources.gov.bz/index.php/surveys-and-mappings-section/
- BNSDI portal: https://portal.bnsdi.gov.bz/
- EarthScope NOTA sourcetable: `ntrip.earthscope.org:2101` — `SOURCETABLE 200 OK` + STR record for `CN23_RTCM3P3` country `BLZ` confirmed 2026-05-12
- EarthScope Network of the Americas: https://www.earthscope.org/nota/ (observed 2026-05-12)
- EarthScope GNSS Realtime: https://www.earthscope.org/data/gnss-realtime/ (observed 2026-05-12)
- Local pipeline data: `data/stations.json` (earthscope BLZ count = 1; fetched 2026-05-12T18:17Z)
- rtk2go / Centipede sourcetables — zero BLZ stations as of 2026-05-12
- ArduSimple RTK correction services by country: https://www.ardusimple.com/rtk-correction-services-in-your-country/
