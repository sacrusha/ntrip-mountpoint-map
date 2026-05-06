# Cameroon [CM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Most Recent Project Announcement

**IGN FI — Land Registration and Estates Modernisation Project, 2019–ongoing**: A consortium of IGN FI / GEOFIT / GEODESIGN & BIZ was awarded the delegated project management contract for Module 1 of the "Modernisation of Land Registration and Estates" project under MINDCAF (Ministry of State Property and Land Affairs), financed by the African Development Bank (AfDB). Budget: ~EUR 1.47 M net of tax; planned duration 12 months from 2019. This project covers land registration modernisation and cadastral reform — not a CORS/NTRIP deployment.

Source: https://www.ignfi.fr/en/2019/09/26/cameroun-demarrage-du-projet-de-modernisation-du-cadastre-et-des-domaines/

**FUGRO / MINDCAF national geodetic network (2010–2012)**: Fugro delivered a national geodetic network of 525 points covering all 10 regions, with 25 first-order reference pillars (~1 per 200 km) and 500 second-order points. IGN FI provided technical audit and supervision. This is a passive monument network, not a CORS network, and no NTRIP caster was deployed.

Sources:
- https://www.fugro.com/expertise/case-studies/national-geodetic-network-cameroon-fugro
- https://www.ignfi.fr/en/portfolio-item/supervision-des-travaux-du-reseau-geodesique-cameroun/

**AFREF Workshop 2024** (RCMRD, Nairobi, August 2024): Cameroon is not listed among the ~22 African countries confirmed to have at least one operational CORS installation.
URL: https://ric2024.rcmrd.org/afref

Note: Cameroon was listed among early AFREF commitments (~2006) to establish at least one CORS — that commitment has not been confirmed as fulfilled in public sources as of 2026-05-06.

## Context Notes

- **INC** (Institut National de Cartographie), under MINRESI (Ministry of Scientific Research and Innovation), is the national geodetic and cartographic authority. INC executes geodesy, photogrammetry, topography, and cartographic drafting. INC's public pages describe RINEX archive activities, not real-time NTRIP streaming.
  Source: https://minresi.gov.cm/en/national-institute-of-cartography/
- **MINDCAF** (Ministry of State Property and Land Affairs) manages cadastral infrastructure and commissioned the FUGRO passive network. No public NTRIP service operates from MINDCAF infrastructure.
- **No streaming CORS confirmed**: The 2010–2012 FUGRO network is a passive monument network only. No CORS station with continuous GNSS logging and real-time/RINEX streaming has been confirmed operational in Cameroon in publicly available sources as of 2026-05-06.
- **RTK2go / Centipede**: Zero CM stations in either sourcetable.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede, RTKdata): No CM coverage identified.
- **Hobbyist access**: Not applicable — no caster exists.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — limited legacy campaign data may exist; no confirmed continuously-operated CM station in current archive | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) — CM data availability unconfirmed |

## Sources Consulted
- INC / MINRESI public page: https://minresi.gov.cm/en/national-institute-of-cartography/
- Fugro case study — Cameroon national geodetic network: https://www.fugro.com/expertise/case-studies/national-geodetic-network-cameroon-fugro
- IGN FI portfolio — supervision of geodetic network Cameroon: https://www.ignfi.fr/en/portfolio-item/supervision-des-travaux-du-reseau-geodesique-cameroun/
- IGN FI — Land Registration and Estates Modernisation Project: https://www.ignfi.fr/en/2019/09/26/cameroun-demarrage-du-projet-de-modernisation-du-cadastre-et-des-domaines/
- GIM International — Developing a Fully Fledged CORS Map for Africa: https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- AFREF 2024 Workshop / RCMRD: https://ric2024.rcmrd.org/afref
- IGS network (network.igs.org) — 0 CM results
- SONEL GNSS database — 0 CM results confirmed-continuous
- RTK2go sourcetable — 0 CM mountpoints
- Centipede-RTK sourcetable — 0 CM mountpoints
- GitHub mvarga1989 CORS list — no CM entry
- ntrip-list.com/africa/ — no CM entry
