# Belize [BZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (CN23_RTCM3P3 still the sole BLZ-tagged stream; EarthScope direct probe still timing out from sandbox, IGS-IP rebroadcast not present for CN23; no operator-side change since 2026-05-17)

## Status: PARTIAL — single EarthScope NOTA station live in central Belize (CN23_RTCM3P3, free non-commercial via NULA). No Belize-operated national CORS or public caster.

| Field | Value |
|---|---|
| Belize-operated public NTRIP RTK caster | No |
| Real-time NTRIP mountpoint physically in BLZ | Yes — `ntrip.earthscope.org:2101/CN23_RTCM3P3` (single NOTA station, 17.26°N -88.78°W, Cayo District near Belmopan) |
| landing_url | https://www.earthscope.org/data/gnss-realtime/ (EarthScope NOTA service description) |
| access_url | https://data.earthscope.org/ (account + NULA acceptance + seat request) |
| host:port | `ntrip.earthscope.org:2101` (TCP) / `:443` (TLS); legacy `rtgpsout.unavco.org:2101` retired 2025-07-29 |
| mountpoint | `CN23_RTCM3P3` |
| format | RTCM 3.3, msg 1005(60)/1007(60)/1013(1)/1029(60)/1033(60) + MSM7 1077/1087/1097/1107/1117(1) |
| constellations | GPS + GLONASS + BeiDou + Galileo + SBAS + QZSS |
| receiver | Septentrio POLARX5 |
| num_stations | 0 BLZ-operated; 1 EarthScope NOTA in BLZ territory (CN23) per `py scripts/stations_by_country.py BLZ` 2026-05-22 |
| vrs | No — single-base raw RTCM 3.3 |
| tariff | **Non-commercial: Free** (NULA acceptance required, account at https://data.earthscope.org/). **Commercial: USD 1,000/seat/yr**, 5-seat minimum for direct billing; 2-week 5-seat trial free. EarthScope is a US 501(c)(3) — no VAT. NULA terms: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |
| hobbyist_eligibility | Yes (non-commercial use under NULA) |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-22 — EarthScope NOTA realtime page reachable; CN23_RTCM3P3 still the sole BLZ-tagged station in local pipeline cache (`py scripts/stations_by_country.py BLZ`); direct `curl ntrip.earthscope.org:2101` continues to time out from this sandbox (sandbox-side network path; same behaviour 2026-05-15 / 2026-05-17 / 2026-05-22, not an operator outage). EarthScope has not announced CN23 decommissioning. Prior 2026-05-15 sourcetable capture: `STR;CN23_RTCM3P3;CN23_RTCM3P3;RTCM 3.3;1005(60),1007(60),1013(1),1029(60),1033(60),1077(1),1087(1),1097(1),1107(1),1117(1);2;GPS+GLO+BDS+GAL+SBAS+QZS;EARTHSCOPE;BLZ;17.26;-88.78;0;0;SEPT POLARX5;None;N;Y;0;SEAT_REQUIRED;` |
| datum_epoch | **ITRF2014, NOTA epoch 2026-03-30** — declared on https://www.earthscope.org/data/gnss-realtime/ ("All raw data streams use the ITRF2014 reference frame. For NOTA stations, the epoch date is 2026-03-30") |

CN23 first appeared in pipeline data on 2026-05-12; absent from the 2026-05-06 EarthScope sourcetable observation. The station sits ~17 km west of Belmopan, providing single-base RTK reach across Cayo, Belize and Orange Walk districts (Belmopan, Belize City, San Ignacio).

## Belize-side context

- **Surveys and Mapping Section** (Ministry of Natural Resources, https://naturalresources.gov.bz/index.php/surveys-and-mappings-section/): horizontal/vertical control + cadastral surveys; no CORS, no NTRIP mentioned.
- **Belize NSDI** (https://portal.bnsdi.gov.bz/): static map data only.
- **rtk2go / Centipede**: 0 BLZ-coded stations 2026-05-22.
- **ArduSimple country directory**: no Belize entry.
- **Cross-border**: Mexico (Quintana Roo) and Guatemala (Petén) — Mexico has only commercial NTRIP; Guatemala has no public caster (see `MX_Mexico.md` / `GT_Guatemala.md`). CN23 in central Belize is the primary practical option.

## Post-Processing (RINEX) Fallback

EarthScope GNSS Data Archive — CN23 RINEX is available alongside the real-time feed under the same NOTA account at https://www.earthscope.org/data/gnss-data/. No Belize-operated national RINEX archive.

## Sources

- Surveys and Mapping Section, Ministry of Natural Resources: https://naturalresources.gov.bz/index.php/surveys-and-mappings-section/
- Belize NSDI: https://portal.bnsdi.gov.bz/
- EarthScope NOTA service: https://www.earthscope.org/data/gnss-realtime/ (datum ITRF2014 / NOTA epoch 2026-03-30 declaration)
- EarthScope account portal: https://data.earthscope.org/
- EarthScope NULA: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf
- EarthScope commercial licence: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- Local pipeline `py scripts/stations_by_country.py BLZ` 2026-05-22: 1 station (CN23_RTCM3P3) on `earthscope`
- ArduSimple RTK correction services by country: https://www.ardusimple.com/rtk-correction-services-in-your-country/ (no Belize entry)
