# Lebanon [LB] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06; reverified 2026-05-12 (no new public endpoint surfaced)

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
- **Cadastre Directorate (Direction des Affaires Géographiques):** The Lebanese state cadastre authority handles land mapping; no GNSS correction service has been published.
- **Lebanon's ongoing economic and political crisis** (since 2019) and the August 2020 Beirut port explosion have severely constrained government capacity for geodetic infrastructure investment.

## Context Notes

- No Lebanese government or commercial NTRIP RTK service was found in any surveying-industry directory, ArduSimple country pages, mvarga1989 GNSS list, NTRIP-list.com, or RTK2go monitor (reverified 2026-05-12).
- IGS reference station data: GNSS data from BEYS (Beirut, via European EPN or SONEL networks) may exist for post-processing, but is not confirmed as a real-time NTRIP stream.
- The Lebanon-adjacent Israeli CORS network (MABAT, operated by the Survey of Israel) offers dense coverage reaching near the border, but is not accessible from Lebanon.
- **Cross-border alternative (out of project ~50 km threshold)**: `centipede` station **`ARKG`** at 32.65 N / 35.29 E (Israel) is the closest tracked NTRIP source at ~140 km from Beirut — too far for single-base RTK and the network membership is Israeli. Not a viable cross-border option.
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
