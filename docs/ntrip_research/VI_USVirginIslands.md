# US Virgin Islands [VI] — NTRIP RTK
**Date:** 2026-05-17 (delta vs 2026-05-13: NOTA realtime page declares `ITRF2014 @ 2026-03-30` — datum citable; project-source probe surfaces `VIIS_RTCM3` St. John on NPS_CORS @ 19 km, and IGS-IP `CRO100VIR0` St. Croix @ 76 km, both not previously noted).

## Status
NO territory caster. EarthScope NOTA streams 1 USVI MP `STVI_RTCM3P3` (St. Thomas). NPS_CORS publishes `VIIS_RTCM3` Virgin Islands National Park (St. John, ~19 km from STVI). IGS-IP publishes `CRO100VIR0` (Christiansted, St. Croix). NOAA NCN holds 4 USVI CORS (RINEX only). No VRS.

## EarthScope NOTA — STVI (St. Thomas)

| Field | Value |
|---|---|
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://data.earthscope.org/ (NULA acceptance) |
| host:port | `ntrip.earthscope.org:2101` |
| Mountpoint | `STVI_RTCM3P3` — 18.34N, -64.97W. Trimble NETR9. RTCM 3.3 MSM7 (GPS+GLO+BDS+GAL+SBAS+QZS), 1 Hz, single-base. |
| num_stations | 1 (STVI). |
| vrs | no |
| tariff | Free non-commercial (NULA acceptance, annual renewal). Commercial USD 1,000/seat/yr (min 5 seats direct billing). 5-seat × 2-week trial available. |
| hobbyist_eligibility | yes (NULA personal use). |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-12 — TCP probe `STVI_RTCM3P3` line present (TRIMBLE NETR9, USA, 18.34/-64.97). NOTA realtime page HTTP 200 2026-05-17. |
| datum_epoch | ITRF2014 @ 2026-03-30 — cited via operator page https://www.earthscope.org/data/gnss-realtime/ ("For NOTA stations, the epoch date is 2026-03-30"). |

## Other USVI GNSS infra (not NTRIP)

- NOAA NCN CORS in VQ state code: STVI (UNAVPS, Operational), VITH (NGSSTA, Op), CRO1 St. Croix VLBA (JPL, Op), VIKH Kingshill (NGSSTA, Op). RINEX only; no NOAA public caster.
- PRSN/UPRM: ~18 GNSS stations across PR+USVI+BVI; NTRIP academic/gov restricted; public info page ECONNREFUSED 2026-05-06.
- CN03 on Tortola (BVI) ~62 km NE of STVI = useful secondary ref for northern VI waters.

## Coverage in project sources

`stations_by_radius.py 18.34 -64.97 200` (2026-05-17):
- earthscope: STVI_RTCM3P3 [USA] @ 0 km, CUPR_RTCM3P3 [USA, PR] @ 33 km, CN03_RTCM3P3 [VGB] @ 62 km, CN58_RTCM3P3 [AIA] @ 165 km, P780_RTCM3P3 [PRI] @ 173 km, AOPR_RTCM3P3 [USA] @ 188 km.
- nps_cors: VIIS_RTCM3 [USA] @ 19 km (St. John, Virgin Islands NP), SAJU_RTCM3 [USA, PR] @ 122 km.
- igs_ip: CRO100VIR0 [VIR] @ 76 km (St. Croix, RTCM3 raw 1 Hz, BKG creds).

St. Croix (50-80 km S of St. Thomas) covered single-base by CRO1 IGS-IP — outside cm-fix range but workable decimetre/sub-m. Zero VI volunteer (rtk2go/centipede) bases.

## Post-processing (RINEX)

- NOAA NCN: STVI, VITH, CRO1, VIKH — free. https://geodesy.noaa.gov/CORS/
- EarthScope/GAGE: STVI via PRGPS DOI 10.7283/T5VD6WTH — free non-commercial.

## Sources
- EarthScope NOTA realtime: https://www.earthscope.org/data/gnss-realtime/ (page load 200 2026-05-17; ITRF2014 @ 2026-03-30 declared)
- NOTA overview: https://www.earthscope.org/nota/
- STVI DOI: 10.7283/T5VD6WTH
- NOAA NCN station list (VQ): https://geodesy.noaa.gov/CORS/sort_sites.shtml
- PRSN: https://redsismica.uprm.edu/english/our_work/instrumentation.php
- TCP probe `ntrip.earthscope.org:2101` 2026-05-12 (STVI present)
- stations_by_radius.py 18.34 -64.97 200 — 2026-05-17 (STVI, VIIS, CRO1, CUPR, CN03 visible)
