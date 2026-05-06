# Macao [MO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — active public NTRIP caster (MoSRef / DSCC); free, registration required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government-operated; free of charge) |
| **Operator** | Cartography and Cadastre Bureau — Direcção dos Serviços de Cartografia e Cadastro (DSCC), Government of the Macao SAR |
| **Network name** | MoSRef (Macao Satellite Positioning Reference Station Service) |
| **host:port** | `mosref.dscc.gov.mo:2101` |
| **tariff** | Free of charge — all services (NTRIP RTK, RINEX download, coordinate auto-computation) are provided free to all registered users |
| **hobbyist_eligibility** | Yes — public service; online registration at mosref.dscc.gov.mo; no professional credentials required |
| **legal_residency_required** | No — Macao resident ID not required; account registration is open internationally based on published policy |
| **last_confirmed_alive** | mosref.dscc.gov.mo login portal returned content (four stations listed, services described) on WebFetch 2026-05-06. curl probe NOT executed — see Sources. |

## Most Recent Project Announcement

- **2023**: Original Taipa Grande station (DSMG, 2008) relocated and renamed to TAGR (Taipa Grande GNSS Reference Station) following a rooftop improvement project at the Macao Meteorological and Geophysical Bureau building. Station code and site name changed; location remains on same rooftop.
- **2021**: DSCC upgraded MoSRef to support BeiDou Navigation Satellite System (BDS) in addition to GPS and GLONASS. All four stations now track GPS + GLONASS + BDS continuously 24 × 7.
- **2016**: University of Macau station (UMAC) added as third full station (Hengqin Island campus), and a data-sharing agreement with Hong Kong GNSS reference stations initiated.
- **November 2012**: NTRIP protocol introduced, enabling real-time mobile RTK access via MoSRef.
- **2009**: MoSRef service established by DSCC.
- **2002**: First reference station (FOMO — Mount Fortress) constructed.

## Context Notes

- **MoSRef** is operated by the DSCC, the Macao SAR government's cartography and cadastre authority.
- **Four Macao GNSS reference stations**:

| Code | Full Name | Location | Year Established |
|---|---|---|---|
| FOMO | Mount Fortress GNSS Reference Station | Macao Peninsula | 2002 |
| COAL | Coloane Alto GNSS Reference Station | Coloane Island | 2006 |
| UMAC | University of Macau GNSS Reference Station | Hengqin Island (UM campus) | 2016 |
| TAGR | Taipa Grande GNSS Reference Station | Taipa Island (Meteorological Bureau rooftop) | 2023 (relocated from DSMG 2008) |

- **Four Hong Kong partner stations** accessible via data-sharing agreement (since 2013): HKLT, HKSL, HKMW, HKNP. These extend VRS coverage across the Pearl River Delta region.
- **Hardware**: Leica GR50 GNSS receivers at most stations. Recording interval: 10 seconds. Data format: RINEX v3.02.
- **Services provided** (all free): DGPS, single-base RTK, Network RTK (VRS), static RINEX download (up to 3 months of observation data), and coordinate automatic computation service for static surveying data.
- **Satellite systems**: GPS (US), GLONASS (Russia), BeiDou/BDS (China). Galileo reception status not confirmed in public documentation.
- **Registration**: Online account at https://mosref.dscc.gov.mo — standard form; no supporting documents required. Login credentials required to access NTRIP stream and RINEX download.
- **Coverage**: Four stations at inter-station spacing of 2–9 km covering the entire Macao SAR (~30 km²). With Hong Kong partner stations, VRS coverage extends across the Pearl River Delta.
- **DSCC explicit statement** (services page): *"DSCC provides … the all-weather NTRIP RTK service to public for free of charge."*
- **Contact**: Telephone (853) 2834 0040 · Email mail@dscc.gov.mo · P.O. Box 3018, Macao. Office hours: Mon–Thu 09:00–13:00, 14:30–17:45; Fri 09:00–13:00, 14:30–17:30.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **MoSRef RINEX download** — all four stations, sub-daily to daily, up to 3 months | https://mosref.dscc.gov.mo | Free (account required) |
| **Coordinate auto-computation** — static GNSS processing service | https://mosref.dscc.gov.mo | Free |

## Sources Consulted
- DSCC MoSRef overview page: https://www.dscc.gov.mo/en/reference_details/article/reference_1.html
- DSCC What is NTRIP: https://www.dscc.gov.mo/en/reference_details/article/jplzyfch.html
- DSCC services introduction: https://www.dscc.gov.mo/en/services_system.html
- MoSRef login portal (WebFetch confirmed active 2026-05-06): https://mosref.dscc.gov.mo/
- EIN Presswire — BeiDou upgrade 2021: https://www.einnews.com/pr_news/558530491/dscc-has-upgraded-macao-satellite-positioning-reference-station-service-to-support-beidou-navigation-satellite-system
- DSCC user guide Part 2 (PDF, 2012): http://mosref.dscc.gov.mo/Help/ref/20121121-Part2.pdf
- DSCC Taipa Grande location page: https://www.dscc.gov.mo/en/tripoints1_details/article/T18T.html
- curl probe of `mosref.dscc.gov.mo:2101` — NOT EXECUTED: sandbox TCP/shell tools blocked during research 2026-05-06. WebFetch of https://mosref.dscc.gov.mo/ returned page content confirming four active stations and NTRIP service description 2026-05-06. Direct SOURCETABLE response NOT independently confirmed.
