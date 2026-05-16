# Belize [BZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: PARTIAL — one EarthScope NOTA station live in central Belize (CN23_RTCM3P3, free non-commercial NULA). No national CORS, no Belize-operated public caster.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (Belize-operated)** | No |
| **Active public NTRIP RTK mountpoint physically in Belize** | Yes — `ntrip.earthscope.org:2101/CN23_RTCM3P3` (single NOTA station, 17.26°N, -88.78°E, Belmopan area) |
| **hobbyist_eligibility (EarthScope NOTA)** | Yes for non-commercial use — requires EarthScope account + signed NULA (Non-commercial User License Agreement) |
| **legal_residency_required** | No |
| **last_confirmed_alive (EarthScope CN23)** | 2026-05-15 — curl probe of `ntrip.earthscope.org:2101` returned the sourcetable with STR row: `STR;CN23_RTCM3P3;CN23_RTCM3P3;RTCM 3.3;1005(60),1007(60),1013(1),1029(60),1033(60),1077(1),1087(1),1097(1),1107(1),1117(1);2;GPS+GLO+BDS+GAL+SBAS+QZS;EARTHSCOPE;BLZ;17.26;-88.78;0;0;SEPT POLARX5;None;N;Y;0;SEAT_REQUIRED;` |

## EarthScope NOTA — CN23

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
| **access_url** | https://data.earthscope.org/ — create account, accept NULA, request real-time GNSS data access |
| **datum_epoch** | OMIT (not stated on STR row; EarthScope NOTA stations are typically referenced to IGS14 / current ITRF — confirm per-station via station log) |

CN23 first appeared in pipeline data on 2026-05-12; it was absent from the 2026-05-06 EarthScope sourcetable observation. Re-confirmed 2026-05-15.

## Other Status

No Belize-operated national NTRIP caster has been published as of 2026-05-15. The Surveys and Mapping Section (Ministry of Natural Resources, `naturalresources.gov.bz`) maintains horizontal and vertical control networks and supervises cadastral surveys but does not publish a CORS or NTRIP service. The Belize National Spatial Data Infrastructure portal (`portal.bnsdi.gov.bz`) provides only static map data.

## Context Notes

- **Surveys and Mapping Section** (Ministry of Natural Resources, `naturalresources.gov.bz/index.php/surveys-and-mappings-section/`): Responsible for all aspects of mapping including horizontal and vertical control. No CORS or NTRIP infrastructure is mentioned on the website or in indexed technical publications.
- **BNSDI** (`portal.bnsdi.gov.bz`): Belize National Spatial Data Infrastructure portal — only static map data and cadastral layers.
- **rtk2go / Centipede**: Zero BLZ-coded stations in either sourcetable as of 2026-05-15 (curl probes returned no Belize STR rows).
- **Border proximity**: Mexico (INEGI CORS, `ntrip.inegi.org.mx:2101`) and Guatemala (IGN-Guatemala, `rtk.igntopo.gob.gt:2101`) are the nearest non-NOTA options; useful where CN23 baseline exceeds practical reach (deep south / far north of Belize). With CN23 in central Belize, cross-border baselines are secondary.
- **IGS / AFREF**: No IGS core or AFREF-affiliated station in Belize.
- **Gap assessment**: Belize is a small country (~23,000 km²) with a population of ~400,000. With CN23 operational, single-base RTK is achievable across most of populated central Belize. No evidence of a Belize-operated CORS programme; EarthScope NOTA is the de-facto free option.

## Post-Processing (RINEX) Fallback

EarthScope GNSS Data Archive — CN23 RINEX should be available alongside the real-time feed under the same NOTA account. No national Belize RINEX archive.

## Sources Consulted
- Surveys and Mapping Section, Ministry of Natural Resources: https://naturalresources.gov.bz/index.php/surveys-and-mappings-section/
- BNSDI portal: https://portal.bnsdi.gov.bz/
- EarthScope NOTA sourcetable: `ntrip.earthscope.org:2101` — STR record for `CN23_RTCM3P3` country `BLZ` confirmed 2026-05-15
- EarthScope Network of the Americas: https://www.earthscope.org/nota/
- EarthScope GNSS Realtime: https://www.earthscope.org/data/gnss-realtime/
- Local pipeline data: `data/stations.json` (earthscope BLZ count = 1; verified via `scripts/stations_by_country.py BLZ` on 2026-05-15)
- rtk2go / Centipede sourcetables — zero BLZ stations as of 2026-05-15
- ArduSimple RTK correction services by country: https://www.ardusimple.com/rtk-correction-services-in-your-country/ (no Belize entry)
