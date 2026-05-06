# Egypt [EG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster (national CORS exists; stream not publicly available)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — no publicly documented NTRIP endpoint found |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no public caster confirmed at any date |

## Most Recent Project Announcement

- **2012 (ongoing):** The Egyptian Surveying Authority (ESA / الهيئة المصرية العامة للمساحة, esa.gov.eg) established a national CORS network of 33 stations covering all of Egypt, operational from 2012.
- **2019:** Academic literature (ResearchGate, 2017) documented consistency assessment of the ESA-CORS and NACN networks in Cairo and the Nile Delta — confirming stations are operational for geodetic research. No public NTRIP endpoint referenced.
- **2024:** No announcement of a public NTRIP service from the ESA or any other Egyptian government agency was found.
- ArduSimple explicitly states (as of mid-2024): "Egypt is not among the countries that have established their own National RTK Networks" and invites correction if users know of one.

## Context Notes

- Egypt's national CORS network (33 stations as of 2019, operated by ESA) is used internally for cadastral surveying and geodetic reference frame maintenance — no public NTRIP stream has been confirmed.
- The ESA website (esa.gov.eg) is the official portal; no RTK or NTRIP service information is published there in English or Arabic web-accessible documentation.
- A research-focused CORS network (NACN — National Active Control Network) is operated for geodetic research; data is not publicly streamed via NTRIP.
- Global commercial networks: GEODNET and ONOCOY coverage in Egypt has not been confirmed in public station maps as of research date.
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS, NRCAN PPP). Free global community NTRIP streams (RTK2go) have no Egyptian base stations listed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS / EarthScope archive** — GNSS stations in/near Egypt (RAMO in Israel is nearest IGS quality station) | https://www.unavco.org/data/gps-gnss/ | Free non-commercial |
| **Egyptian Survey Authority (ESA)** — CORS RINEX may be available on request; not publicly confirmed | https://www.esa.gov.eg/ | Unknown |

## Sources Consulted
- ArduSimple — RTK correction services in Egypt: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-egypt/
- Egyptian Survey Authority: https://www.esa.gov.eg/
- ResearchGate — "Consistency between CORS and NACN Egyptian Networks" (2017): https://www.researchgate.net/publication/317182787_Consistency_between_CORS_and_NACN_Egyptian_Networks_in_Cairo_and_Nile_Delta
- MDPI Remote Sensing — Egypt ionosphere model paper (references ESA-CORS, 2023): https://www.mdpi.com/2072-4292/15/12/3147
- mvarga1989 GitHub GNSS CORS networks list (Egypt not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2go monitor (no Egypt stations observed)
- NTRIP-list.com (no Egyptian NTRIP service listed)
