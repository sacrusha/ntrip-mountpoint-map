# Djibouti [DJ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: NO — no NTRIP RTK caster, no national CORS programme, no volunteer coverage. One scientific IGS station (DJIG, operated by CNES France's REGINA programme) exists in Djibouti City for post-processing only

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Operator** | — |
| **host:port** | — |
| **VRS** | — |
| **tariff** | — |
| **hobbyist_eligibility** | — |
| **legal_residency_required** | — |
| **last_confirmed_alive** | — |
| **Most recent project announcement** | None found |

## Context Notes

- **National geodetic authority:** CERD (Centre d'Études et de Recherche de Djibouti) handles geodetic and geophysical matters. No GNSS CORS programme or NTRIP service has been identified on their website or in search results as of 2026-05-12.
- **IGS scientific station DJIG (Djibouti City)**: Site name `DJIBOUTI`, four-character ID `DJIG`, full code `DJIG00DJI`, DOMES 39901M005. Located in Djibouti, Republic of Djibouti at **11.52628757°N, 42.84706445°E**. **Operated by CNES** (Centre National d'Études Spatiales, France) as part of CNES/IGN France's **REGINA** programme (Receiver GNSS Network for IGS and Navigation). Installed 2001-01-01; current equipment Septentrio PolaRx5 (firmware 5.3.2) since 2020-02-26, tracking GPS+GLO+GAL+BDS+SBAS+IRNSS. **Post-processing data only** via CDDIS / IGN-IGS / SONEL — no public real-time NTRIP RTK stream. *(Earlier draft attributed operation to IPGP; the SONEL station record confirms CNES.)*
- **Volunteer alternatives**: zero DJI-coded bases on rtk2go and Centipede (verified 2026-05 archives). `stations_by_radius.py 11.6 43.1 200` returns no project-tracked stations within 200 km of Djibouti City.
- **Regional African CORS initiatives**: Djibouti is not part of AFREF operational stations, TrigNet, or any other regional public-NTRIP programme. The country's geodetic infrastructure development is at an early stage and likely dependent on bilateral cooperation (France via CNES; possibly Japan via JICA or China via cooperation programmes).
- No project announcement for a future national RTK/CORS service found as of 2026-05-12.
- **Connectivity & physical context**: Internet connectivity in Djibouti is provided primarily via submarine cable landing points (Djibouti hosts six landing stations and is a major regional internet hub); mobile broadband is growing but coverage remains limited outside Djibouti City. A future CORS programme would benefit from this connectivity, but no public plan is documented.
- **Cross-border alternative within ~50 km**: None. The nearest national RTK networks across the Bab-el-Mandeb / Gulf of Aden are still hundreds of km distant; Ethiopian and Somalian CORS programmes are not publicly operational for hobbyist NTRIP either. Practical workaround: deploy a local single-base RTK setup, or use satellite-based PPP (Galileo HAS, Trimble RTX).

## Post-Processing (RINEX) Fallback

No nationally operated RINEX service found. The CNES-operated DJIG station data is available via the IGS/CDDIS and IGN-IGS archives for research purposes.

| Service | URL | Cost |
|---|---|---|
| **IGS CDDIS** — DJIG station daily/hourly RINEX | https://cddis.nasa.gov/archive/gnss/data/daily/ | Free (NASA Earthdata account required) |
| **IGN-IGS / REGINA archive** | https://igs.ign.fr/ | Free |
| **SONEL** — DJIG height time-series and metadata | https://www.sonel.org/spip.php?page=gps&idStation=3644 | Free |

## Sources Consulted
- WebSearch "Djibouti NTRIP CORS RTK GNSS" — no national service results (2026-05-06, re-checked 2026-05-12)
- WebSearch "Djibouti IGN GNSS geodesy CORS 2024 2025" — no national service results
- CERD website: https://www.cerd.dj/ (no GNSS/NTRIP content found)
- IGS network: https://network.igs.org/ (DJIG station confirmed)
- SONEL DJIG record: https://www.sonel.org/spip.php?page=gps&idStation=3644 — confirms CNES operator and coordinates
- GNSS-Africa map: https://www.gnss-africa.org/ (Djibouti not listed)
- `data/rtk2go.sourcetable` and `data/centipede.sourcetable` — zero DJI-coded streams
- `scripts/stations_by_radius.py 11.6 43.1 200` — no project-tracked stations within 200 km
