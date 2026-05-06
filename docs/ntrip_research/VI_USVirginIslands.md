# US Virgin Islands [VI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO territory-operated NTRIP — EarthScope NOTA streams one station on St. Thomas (STVI); NOAA NCN has two USVI CORS stations (RINEX only); no VRS service; distances impractical for RTK

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — territory-operated; no VRS |
| **EarthScope NOTA NTRIP** | `ntrip.earthscope.org:2101` — mounts STVI_RTCM3P3 (St. Thomas, 18.34°N/−64.97°W); RTCM 3.3, GPS+GLO+BDS+GAL+SBAS+QZS at 1 Hz; Trimble NETR9; confirmed in sourcetable 2026-05-06 |
| **EarthScope NOTA tariff** | Free for non-commercial scientific/educational/humanitarian use; USD $1,000/seat/year commercial (one concurrent stream per seat); two-week trial (5 seats) available |
| **VRS** | No — single-base 1 Hz RTCM 3.3 streams only; no network RTK engine |
| **hobbyist_eligibility — NOTA** | Yes — non-commercial account required; EarthScope account registration free |
| **legal_residency_required** | No |
| **last_confirmed_alive** | `ntrip.earthscope.org:2101` returned SOURCETABLE 200 OK with STVI_RTCM3P3 confirmed live 2026-05-06 (curl probe) |
| **NOAA NCN CORS in USVI** | STVI (St. Thomas, VQ state code, Operational, UNAVPS); VITH (St. Thomas, NGSSTA, Operational); CRO1 (St. Croix VLBA, JPL, Operational); VIKH (Kingshill St. Croix, NGSSTA, Operational) — all RINEX download only, no public NTRIP caster |
| **PRSN/UPRM** | Puerto Rico Seismic Network (UPRM) operates 18 permanent GNSS stations covering PR + USVI + BVI; NTRIP endpoint restricted to academic/government users; contact redsismica.uprm.edu |

## Context Notes

- **STVI (St. Thomas, VI)** is the only confirmed EarthScope NOTA mountpoint with an on-island USVI location. It is part of the Puerto Rico GPS Network (PRGPS) sub-network, with data archived since 2008-10-27 (DOI: 10.7283/T5VD6WTH, GAGE Facility). At 18.34°N / −64.97°W it is approximately 5 km south-west of Charlotte Amalie.
- **Practical RTK limitation**: NOTA streams raw 1 Hz GNSS data (science/geodetic grade). A rover must compute its own baseline to STVI; this is real-time RTK only if the rover NTRIP client can use single-station RTCM 3.3. Useful for short-baseline RTK within ~30–50 km (St. Thomas, St. John, BVI area) but requires GNSS receiver capable of accepting raw RTCM3 from a remote reference. No VRS or FKP service exists.
- **NOAA NCN CORS in USVI**: Four stations confirmed in NCN station list (VQ state code) — STVI (Operational, UNAVPS operator), VITH (Operational, NGSSTA), CRO1 St. Croix VLBA (Operational, JPL), and VIKH Kingshill (Operational, NGSSTA). NCN provides RINEX download only; no public NTRIP stream is offered by NOAA/NGS.
- **CN03 on Tortola (BVI)**: EarthScope NOTA also streams CN03_RTCM3P3 (18.49°N / −64.40°W, country code VGB) — approximately 30 km north-east of St. Thomas; this gives a useful second reference point for northern VI waters.
- **PRSN/UPRM**: The Puerto Rico Seismic Network operates ~18 GNSS stations across PR, USVI, and BVI; their NTRIP service (formerly at prsn.uprm.edu) is academic/government-restricted; the public NTRIP info page (http://www.prsn.uprm.edu/English/research/geodesy/NTRIP_info.php) returns ECONNREFUSED (2026-05-06).
- **rtk2go / Centipede**: Zero USVI bases in either caster sourcetable as of 2026-05-06.
- **No commercial RTK network** (Trimble VRS Now, Hexagon SmartNet, GEODNET) confirmed to cover USVI.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **NOAA NCN RINEX** — STVI, VITH, CRO1, VIKH (all USVI stations) | https://geodesy.noaa.gov/CORS/ | Free |
| **EarthScope / GAGE GNSS archive** — STVI via PRGPS DOI | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- EarthScope GNSS real-time data (NTRIP access, licensing): https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA network overview: https://www.earthscope.org/nota/
- GAGE Facility STVI dataset DOI 10.7283/T5VD6WTH: https://www.unavco.org/data/doi/10.7283/T5VD6WTH (data collected from 2008-10-27; active as of 2026-05-05)
- SONEL sea-level / GNSS station VITH00VIR (St. Thomas, UVI operator): https://www.sonel.org/spip.php?page=gps&idStation=1899
- NOAA NCN station list (sort_sites.shtml) — VQ state code entries STVI, VITH, CRO1, VIKH confirmed: https://geodesy.noaa.gov/CORS/sort_sites.shtml
- PRSN GNSS network overview: https://redsismica.uprm.edu/english/our_work/instrumentation.php
- St Thomas Source / PRSN USVI monitoring article (Jan 2024): https://stthomassource.com/content/2024/01/30/puerto-rico-seismic-network-monitoring-the-u-s-virgin-islands-for-earthquakes/
- curl probe of `ntrip.earthscope.org:2101` — SOURCETABLE 200 OK, STVI_RTCM3P3 confirmed present 2026-05-06
- curl probe of CN03_RTCM3P3 (VGB/Tortola BVI, 18.49°N/−64.40°W) — also confirmed in sourcetable 2026-05-06
