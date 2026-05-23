# Egypt [EG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-23 (re-verified; original 2026-05-06, prior refresh 2026-05-17)
last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-17
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: NO confirmed public NTRIP caster (national CORS exists; stream not publicly available). Re-verified 2026-05-23 — `esa.gov.eg` homepage re-fetched, no CORS / NTRIP / RTK / GNSS service section published (only traditional surveying products and a weather-related "fixed stations" project). No public ESA NTRIP endpoint, registration portal, or tariff has been announced since the original research; ArduSimple country page still reports "as far as we know Egypt is not among" countries with a National RTK Network. Radius probe Cairo 30.0/31.2 within 250 km returns zero ingested-pipeline stations.

| Field | Value |
|---|---|
| **caster_status** | No publicly documented NTRIP endpoint found |
| **landing_url** | null — no operator-owned public NTRIP page; ESA homepage (https://www.esa.gov.eg/) does not publish RTK/NTRIP service info |
| **access_url** | null — no signup/conditions page exists |
| **host:port** | null |
| **tariff** | null |
| **num_stations** | ESA-CORS = ~40 stations covering Nile valley + delta, established January 2012 (multiple peer-reviewed sources including Saad et al. 2017 and MDPI Remote Sensing 2023). The "33-station" figure in earlier ESA-linked descriptions appears to refer to a subset used in specific tectonic-coordinate studies rather than the full deployment. A separate research network NACN (National Agricultural Cadastral Network, established 1997) operates ~30 stations at 30–40 km spacing. ESA portal publishes no current authoritative count, but academic literature treats 40 as the operational ESA-CORS figure. |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no public caster confirmed at any date |

## Most Recent Project Announcement

- **2012 (ongoing):** The Egyptian Surveying Authority (ESA / الهيئة المصرية العامة للمساحة, esa.gov.eg) established a national CORS network of 33 stations covering all of Egypt, operational from 2012.
- **2019:** Academic literature (ResearchGate, 2017) documented consistency assessment of the ESA-CORS and NACN networks in Cairo and the Nile Delta — confirming stations are operational for geodetic research. No public NTRIP endpoint referenced.
- **2024:** No announcement of a public NTRIP service from the ESA or any other Egyptian government agency was found.
- ArduSimple explicitly states (as of mid-2024): "Egypt is not among the countries that have established their own National RTK Networks" and invites correction if users know of one.

## Context Notes

- Egypt's national CORS network (ESA-CORS, operated by the Egyptian Surveying Authority since January 2012, ~40 stations covering the Nile valley and delta) is used internally for cadastral surveying and geodetic reference frame maintenance — no public NTRIP stream has been confirmed. Academic literature on the network adjusts to ITRF2008 epoch 2011.8096 (initial adjustment) and ITRF2014 epoch 2019.5833 (later re-adjustment), per the ResearchGate "ITRF-Based Tectonic Coordinates Changes using GNSS-CORS Networks: A Case Study of Egypt" paper.
- The ESA website (esa.gov.eg) is the official portal; no RTK or NTRIP service information is published there in English or Arabic web-accessible documentation.
- A separate ESA-operated research network NACN (National Agricultural Cadastral Network, established 1997, ~30 stations at 30–40 km spacing covering the green-area Nile valley and delta) is used for geodetic research; data is not publicly streamed via NTRIP.
- Egypt's national geodetic frame is published in ITRF realisations (ITRF2008 originally, ITRF2014 in recent literature) per academic ESA-linked publications; this is not an operator real-time-service declaration for any caster — included as geodetic context only.
- Global commercial networks: GEODNET and ONOCOY coverage in Egypt has not been confirmed in public station maps as of research date.
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS, NRCAN PPP). Free global community NTRIP streams (RTK2go) have no Egyptian base stations listed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS / EarthScope archive** — IGS does not currently list Egypt-located stations in the active core network (network.igs.org, 2026-05-23). The Egyptian Permanent GPS Network (EPGN, operated by NRIAG; stations include HELW Helwan and an Alexandria CEALX site) is a national research archive, not an IGS-tier real-time NTRIP source. Nearest IGS-tier RINEX archives are in Israel (RAMO Ramon Crater ~780 km from Cairo) and across the Mediterranean. | https://www.unavco.org/data/gps-gnss/ | Free non-commercial |
| **Egyptian Survey Authority (ESA)** — CORS RINEX may be available on request; not publicly confirmed | https://www.esa.gov.eg/ | Unknown |

## Sources Consulted
- ArduSimple — RTK correction services in Egypt: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-egypt/
- Egyptian Survey Authority: https://www.esa.gov.eg/
- MDPI Remote Sensing — Egypt ionosphere model paper (references ESA-CORS, 40-station figure, 2023): https://www.mdpi.com/2072-4292/15/12/3147
- mvarga1989 GitHub GNSS CORS networks list (Egypt not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2go monitor (no Egypt stations observed)
- NTRIP-list.com (no Egyptian NTRIP service listed)
- ResearchGate "ITRF-Based Tectonic Coordinates Changes using GNSS-CORS Networks: A Case Study of Egypt" (ESA-CORS adjusted to ITRF2008 epoch 2011.8096; updated to ITRF2014 epoch 2019.5833): https://www.researchgate.net/publication/356716765_ITRF-Based_Tectonic_Coordinates_Changes_using_GNSS-CORS_Networks_A_Case_Study_of_Egypt
- IGS Network browser (network.igs.org, 2026-05-23): no Egypt-located stations in the active core station list — confirms RAMO (Israel) as nearest IGS-tier RINEX source for Egyptian users
