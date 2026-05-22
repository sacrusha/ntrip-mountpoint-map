# Lebanon [LB] — NTRIP RTK Caster Research
**Date researched:** 2026-05-23 (reverified from 2026-05-17; no new public endpoint surfaced; radius probe at Beirut 33.89 N / 35.5 E within 200 km re-confirms only ISR-side `ARKG` (centipede, 140 km) + `BSHM00ISR0` (IGS-IP, 131 km) — neither cross-border-usable)
last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-17
last_caster_search_date: 2026-05-23

## Status: NO confirmed public NTRIP caster in Lebanon. Centipede station ARKG operates 140 km away in northern Israel — outside the project's ~50 km cross-border useful-coverage threshold.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — no publicly documented NTRIP endpoint found |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no public caster confirmed at any date |

## Most Recent Project Announcement

No formal project announcement for a Lebanese national NTRIP/RTK caster or CORS network was found in any development-bank, UN, academic, or geospatial trade press source as of 2026-05-06.

- **CNRS-L (Conseil National de la Recherche Scientifique du Liban):** Lebanon's national research council (cnrs.edu.lb, founded 1962) conducts scientific research including some earth-science activities. No GNSS CORS or NTRIP RTK service from CNRS-L has been documented.
- **Cadastre / Direction des Affaires Géographiques (DAG):** The DAG sits under the Lebanese Army and is the national topographic-mapping and geodetic authority, responsible for the Lebanese map projection and cadastral reference framework. Its mandate covers traditional topographic surveying products; no GNSS CORS, NTRIP caster, or real-time corrections service is published on any public Lebanese government portal.
- **Lebanon's ongoing economic and political crisis** (since 2019) and the August 2020 Beirut port explosion have severely constrained government capacity for geodetic infrastructure investment.

## Context Notes

- No Lebanese government or commercial NTRIP RTK service was found in any surveying-industry directory, ArduSimple country pages, mvarga1989 GNSS list, NTRIP-list.com, or RTK2go monitor (reverified 2026-05-23).
- `datum_epoch`: omitted -- no Lebanese operator caster exists; no operator declaration to cite.
- **GNSS spoofing**: Lebanon is within the core area affected by Israeli military GPS/GNSS spoofing operating continuously since Oct 2023 (Breaking Defense Apr 2024 "GPS jamming spreads in Lebanon"; cross-referenced in IL_Israel.md). Even if a Lebanese caster were to come online, raw-observable spoofing would corrupt RTK fixes regardless of correction-stream quality. This is the dominant operational hazard for any rover work in Lebanon.
- IGS reference station BEYS00LBN (Beirut, American University of Beirut campus): IGS network browser (network.igs.org/BEYS00LBN, 2026-05-23) returned HTTP 404, indicating the station is no longer in the active IGS station list. SONEL and historical archives may still hold legacy observations, but BEYS is not a current real-time NTRIP or live RINEX source.
- The Lebanon-adjacent Israeli CORS network (MABAT, operated by the Survey of Israel) offers dense coverage reaching near the border, but is not accessible from Lebanon.
- **Cross-border alternative (out of project ~50 km threshold)**: `centipede` station **`ARKG`** at 32.65 N / 35.29 E (Israel) ~140 km from Beirut and `igs_ip` station **`BSHM00ISR0`** at 32.78 N / 35.02 E ~131 km are the closest tracked NTRIP sources (stations_by_radius.py 33.89 35.5 200 → 2 hits, 2026-05-23). Both far beyond useful single-base RTK range; both Israeli network membership — not viable cross-border options for Lebanon.
- Global commercial networks (GEODNET, ONOCOY, PointOne): no Lebanon coverage confirmed.
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS, NRCAN PPP).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope/GAGE / IGS archive** — regional stations (nearest is in Cyprus or Jordan) | https://www.unavco.org/data/gps-gnss/ | Free non-commercial |
| **SONEL** — sea-level / tide-gauge linked GNSS (BEYS if active) | https://www.sonel.org/ | Free |

## Sources Consulted
- CNRS Lebanon: https://cnrs.edu.lb/
- ArduSimple country RTK list (Lebanon not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- mvarga1989 GitHub GNSS CORS networks list (Lebanon not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2go monitor (no Lebanon stations observed)
- NTRIP-list.com (no Lebanese service listed)
- SONEL sea-level portal: https://www.sonel.org/
- GEODNET (no Lebanon coverage)
- IGS Network browser BEYS00LBN: https://network.igs.org/BEYS00LBN — HTTP 404 (2026-05-23), station absent from current IGS active list
- Breaking Defense (Apr 2024) "GPS jamming spreads in Lebanon, civil aviation caught in the electronic crossfire": https://breakingdefense.com/2024/04/gps-jamming-spreads-in-lebanon-civil-aviation-caught-in-the-electronic-crossfire-experts/
