# Slovenia [SI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid national NTRIP (SIGNAL); free for public bodies; individuals can subscribe; port 8080

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | GURS via Geodetski inštitut Slovenije (Surveying and Mapping Authority of the Republic of Slovenia) |
| **Service name** | Omrežje SIGNAL |
| **host:port** | `178.172.26.131:8080` |
| **VRS** | Yes — VRSSLO(2_3), VRSSLO(3_1), VRSMSM5, VRSCMRx, VRSCMRp |
| **Network type** | VRS, MAC/MAX (MacSLO), individual station streams |
| **Constellations** | GPS+GLO (RTCM 2.3/3.1); GPS+GLO+GAL+BDS (CMRx, MSM5) |
| **Number of reference stations** | 16 stations across Slovenia (Bovec, Brežice, Celje, Črnomelj, Idrija, Ilirska Bistrica, Koper, Lendava, Ljubljana, Maribor, Nova Gorica, Ptuj, Radovljica, Slovenj Gradec, Trebnje + foreign-adjacent stations) |
| **tariff — flat rate (annual)** | €829.44/year excl. VAT (April 2025–March 2026); €622.08 with 25% early-bird discount if contracted before 2025-07-31 |
| **tariff — pay-per-use** | €0.12/connected minute excl. VAT |
| **tariff — public bodies** | Free (requires documentation to gps@gis.si) |
| **tariff — students/civil society** | Free with institutional verification |
| **VAT** | Slovenian standard rate 22%; prices above are excl. VAT |
| **hobbyist_eligibility** | Yes — individuals (fizična oseba) can register; no professional licence required |
| **legal_residency_required** | Unclear — no explicit restriction for non-Slovenian EU users; registration requires postal mail of signed contract to Geodetski inštitut Slovenije |
| **last_confirmed_alive** | `178.172.26.131:8080` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl probe); Trimble Ntrip Caster 5.2 |

## Context Notes

- Sourcetable confirmed 16 Slovenian reference stations plus foreign-adjacent stations (Austria, Croatia, Italy, Hungary) accessible via the same caster.
- RTCM formats: 2.3 (GPS), 3.1 (GPS+GLONASS), 3.2 MSM5/MSM7 (multi-constellation), CMR+, CMRx.
- Registration requires: completing online form → receiving contract by email → signing 4 copies → posting to Geodetski inštitut Slovenije → receiving credentials by email. Allow ~2 business days.
- Non-commercial eligibility (public administration, students, civil societies) requires supporting documentation submitted to gps@gis.si within one week of application.
- The SIGNAL portal (gu-signal.si) is in Slovenian; English support available via phone 01 200 29 29 or email gps@gis.si.
- rtk2go contains sparse Slovenian volunteer mountpoints but sparse; SIGNAL is the primary RTK source.
- Tariff observed on gu-signal.si/postopek-registracije/ on 2026-05-06.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SIGNAL RINEX/post-processing** | https://gu-signal.si/ | €0.26/s server processing time (€4.21/hr of data); free for public bodies |
| **SIGNAL open data (OPSI)** | https://podatki.gov.si/dataset/podatki-omrezja-signal | Free (historic GNSS observations) |

## Sources Consulted
- GURS SIGNAL portal: https://gu-signal.si/ (observed 2026-05-06)
- SIGNAL NTRIP access page: https://gu-signal.si/dostop-do-ntrip-streznika/ (IP 178.172.26.131, port 8080)
- SIGNAL RTK mountpoints: https://gu-signal.si/rtk-dostopne-tocke-in-stevilke/
- SIGNAL registration & pricing: https://gu-signal.si/postopek-registracije/
- curl probe of `178.172.26.131:8080` — SOURCETABLE 200 OK confirmed 2026-05-06; Trimble Ntrip Caster 5.2; 16 SI stations visible
