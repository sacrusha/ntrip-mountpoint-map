# Egypt [EG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; original 2026-05-06)

## Status: NO confirmed public NTRIP caster (national CORS exists; stream not publicly available). Re-verified 2026-05-17 — no public ESA NTRIP endpoint, registration portal, or tariff has been announced since the original research; ArduSimple country page still reports "as far as we know Egypt is not among" countries with a National RTK Network.

| Field | Value |
|---|---|
| **caster_status** | No publicly documented NTRIP endpoint found |
| **landing_url** | null — no operator-owned public NTRIP page; ESA homepage (https://www.esa.gov.eg/) does not publish RTK/NTRIP service info |
| **access_url** | null — no signup/conditions page exists |
| **host:port** | null |
| **tariff** | null |
| **num_stations** | 33 per ESA official network description (operational since 2012); academic literature (Saad et al. 2017; subsequent MDPI Remote Sensing 2023 ref) cites 40 stations. Both figures appear in non-operator sources; ESA portal does not publish a current authoritative count. Discrepancy unresolved as of 2026-05-17. |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no public caster confirmed at any date |

## Most Recent Project Announcement

- **2012 (ongoing):** The Egyptian Surveying Authority (ESA / الهيئة المصرية العامة للمساحة, esa.gov.eg) established a national CORS network of 33 stations covering all of Egypt, operational from 2012.
- **2019:** Academic literature (ResearchGate, 2017) documented consistency assessment of the ESA-CORS and NACN networks in Cairo and the Nile Delta — confirming stations are operational for geodetic research. No public NTRIP endpoint referenced.
- **2024:** No announcement of a public NTRIP service from the ESA or any other Egyptian government agency was found.
- ArduSimple explicitly states (as of mid-2024): "Egypt is not among the countries that have established their own National RTK Networks" and invites correction if users know of one.

## Context Notes

- Egypt's national CORS network (operated by ESA since 2012) is used internally for cadastral surveying and geodetic reference frame maintenance — no public NTRIP stream has been confirmed. Station count cited as 33 in early ESA-linked descriptions, 40 in later academic literature; ESA does not publish a current authoritative figure.
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
- MDPI Remote Sensing — Egypt ionosphere model paper (references ESA-CORS, 40-station figure, 2023): https://www.mdpi.com/2072-4292/15/12/3147
- mvarga1989 GitHub GNSS CORS networks list (Egypt not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2go monitor (no Egypt stations observed)
- NTRIP-list.com (no Egyptian NTRIP service listed)
