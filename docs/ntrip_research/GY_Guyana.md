# Guyana [GY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior: 2026-05-12)

## Status

National CORS infrastructure exists and has expanded since the original 2018-2019 build, but no public NTRIP host:port, sourcetable, or self-service registration portal is published. The Guyana Lands and Surveys Commission (GLSC) operates the network internally for cadastre, surveyors, and licensed professionals. No volunteer (rtk2go / Centipede) or commercial (GEODNET / ONOCOY / Trimble VRS Now / Topcon TopNETlive) coverage in Guyana has been found.

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | No (CORS infrastructure present, no public NTRIP endpoint) |
| landing_url | https://glsc.gov.gy/ (operator; no GNSS-correction page on site) |
| access_url | n/a (no public self-service portal); credentials via GLSC Head Office, Georgetown |
| host:port | not published |
| num_stations | 11 (current operator-reported count under the FAO/GRIF Sustainable Land Development and Management project that closes Dec 2025 — News Room Guyana 2025-08-04, attributing "grew from 5 to 11" to the Lands & Surveys Commission). The 2018-2019 build delivered 8 stations (Eclipse Falls, Supenaam, Georgetown, New Amsterdam, Olive Creek, Mahdia, Lethem, Linden); the discrepancy with the 2025 "from 5" baseline is not explained in the news source — possibilities are that some of the 2018 stations had fallen out of service before the SLDM expansion, or the reporter mis-stated the baseline. The 11-station figure is consistent across the news article and the GRIF Port Kaituma deliverables write-up. |
| vrs | unknown |
| hobbyist_eligibility | unknown — likely restricted to licensed surveyors via GLSC Head Office invitation |
| legal_residency_required | unknown |
| last_confirmed_alive | 2026-05-21 — GLSC site reachable; SLDM-project News Room article (2025-08-04) confirms the 11-station CORS is operating for surveyors. No external NTRIP-port probe is possible because no host:port is published. |
| datum_epoch | omitted — operator (GLSC) does not publicly declare; SIRGAS-CON station list shows no Guyana entry, so even regional context is absent (citation rule: only operator declaration is citable). The 2018 DPI Guyana government press release (third-party, not operator portal) describes the network as "connected to ITRF 2014, Geocentric Reference Systems of the Americas (SIRGAS)" but no epoch is given and the operator's own GLSC site does not republish a frame statement. |

## Most Recent Project Announcement

- **2025-08-04 — News Room Guyana**: "The Continuously Operating Reference Stations (CORS) system has grown from 5 to 11 stations nationwide, providing centimetre-level accuracy for cadastral surveys, which can now be rapidly completed in days rather than months." Expansion delivered under the GLSC-FAO-GRIF Sustainable Land Development and Management (SLDM) project, scheduled to close December 2025. Equipment used by surveyors: Leica GNSS kits + Total Stations + ESRI Software. Public NTRIP-service status is not addressed. https://newsroom.gy/2025/08/04/guyana-seeing-historic-shift-in-land-surveying-administration-and-use/
- **2018-2019 — GLSC build-out**: 8-station network installed by Ordnance Survey International under a GYD 93M (~USD 443k 2018) contract; commissioned 2018-09-07 ("Land mapping, surveying made easier", Guyana Chronicle). DPI Guyana page enumerates the 8 stations: Eclipse Falls (Region 1), Supenaam (2), Georgetown (4), New Amsterdam (6), Olive Creek (7), Mahdia (8), Lethem (9), Linden (10) — "connected to ITRF 2014, Geocentric Reference Systems of the Americas (SIRGAS)". https://dpi.gov.gy/reference-stations-to-assist-land-surveys/

## Context Notes

- **GLSC operates the CORS network from the Network Operations Centre at the Commission's Head Office in Georgetown.** Surveyor enrolment is by direct contact; no online self-service portal observed on `glsc.gov.gy` or `lands.glsc.gov.gy`.
- **No public sourcetable** has been observed; absent from NTRIP-list.com Caribbean / South-America tables and from RTK2go community casters.
- **SIRGAS-CON analysis-centre station list**: still no Guyana entry as of 2026-05-21 — the 8-station (now 11-station) GLSC network is internally consumed and has not been published to SIRGAS-CON.
- **SLDM project page (GRIF)**: fetched 2026-05-21 — references LIDAR, national topographic base mapping, and spatial data systems; does not enumerate the 3 additional CORS stations or publish an equipment list. Specific names of the new SLDM-funded CORS stations have not been found in any operator-side or funder-side public document.
- **Practical workaround for hobbyists**: deploy a local base station for single-base RTK, or use satellite-based PPP services (Trimble RTX, u-blox PointPerfect where available). Galileo HAS is another no-internet option (~40 cm).

## Volunteer / Global Coverage (2026-05-21)

- `py scripts/stations_by_country.py GUY` — zero stations across all ingested globals (rtk2go, earthscope, igs_ip, centipede).
- GEODNET / ONOCOY: no Guyana stations on public coverage maps.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| EarthScope / SIRGAS-CON | https://www.earthscope.org/data/gnss-data/ | No Guyana GLSC CORS station confirmed in SIRGAS-CON or EarthScope archive as of 2026-05-21 |
| GLSC NOC (direct request) | https://glsc.gov.gy/ | Unknown — request via GLSC directly |

## Sources

- News Room Guyana, "Guyana seeing historic shift in land surveying, administration and use" (2025-08-04; 5 to 11 CORS, SLDM project): https://newsroom.gy/2025/08/04/guyana-seeing-historic-shift-in-land-surveying-administration-and-use/
- DPI Guyana, "Reference stations to assist land surveys" (8 station locations, ITRF 2014/SIRGAS context): https://dpi.gov.gy/reference-stations-to-assist-land-surveys/
- Guyana Chronicle, "$93M contract signed to get reference stations on stream" (2018-07-12): https://guyanachronicle.com/2018/07/12/93m-contract-signed-to-get-reference-stations-on-stream/
- Ordnance Survey International — Guyana case study: https://www.ordnancesurvey.co.uk/customers/case-studies/empowering-guyanas-national-mapping-agency
- GLSC official site: https://glsc.gov.gy/ (HTTP 200; no GNSS-service sub-page); GL&SC services: https://lands.glsc.gov.gy/
- GuyNode blog (2019-08-05): https://guynode.com/blog/2019/08/05/guyanas-new-cors-network/
- SIRGAS station list (Guyana absent): https://sirgas.ipgh.org/en/gnss-network/stations/station-list/
- FAO SLDM Project profile: https://www.fao.org/americas/news/news-detail/Mainstreaming-Sustainable-Land-Development-and-Management-(SLDM)-Project-in-Guyana/en
- GRIF SLDM page: https://www.guyanareddfund.org/project/mainstreaming-sustainable-land-development-and-management/
