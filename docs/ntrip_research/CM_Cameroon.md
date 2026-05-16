# Cameroon [CM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (revising 2026-05-12 entry — no material changes; re-verified zero-coverage status and refactored prose)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Verification (2026-05-15)

- `py scripts/stations_by_country.py CMR` → `No stations for 'CMR'`.
- `py scripts/stations_by_radius.py 3.85 11.50 400` (Yaoundé) → `No stations within 400 km`.
- `py scripts/stations_by_radius.py 3.85 11.50 800` → `No stations within 800 km` — no aggregated stream within reach for single-base RTK.
- `data/rtk2go.sourcetable` and `data/centipede.sourcetable` grep for `;CMR;` and `Cameroon|Cameroun` → zero country-tagged Cameroon mountpoints (all "CMR" hits are the Trimble CMR data format, not the ISO-3 country code).
- IGS network list (network.igs.org, 534 stations as of 2026-05-15) → no IGS station in CM. Nearest IGS reference is **NKLG (Libreville, Gabon)** ~590 km SSW of Yaoundé — archive-only, no public NTRIP.

## Most Recent Project / Announcement

**FUGRO / MINDCAF national geodetic network (2010–2012)**: Fugro delivered a national geodetic network of 525 points covering all 10 regions — 25 first-order reference pillars (~1 per 200 km) and 500 second-order points. IGN FI provided technical audit and supervision. This is a **passive monument network**, not a CORS network; no NTRIP caster was deployed.
- https://www.fugro.com/expertise/case-studies/national-geodetic-network-cameroon-fugro
- https://www.ignfi.fr/en/portfolio-item/supervision-des-travaux-du-reseau-geodesique-cameroun/

**IGN FI / GEOFIT / GEODESIGN & BIZ — Land Registration and Estates Modernisation, 2019–ongoing**: consortium awarded delegated project management for Module 1 of MINDCAF's "Modernisation du Cadastre et des Domaines" project (AfDB-financed, ~EUR 1.47 M, 12 months from 2019). Cadastral reform — not CORS/NTRIP.
- https://www.ignfi.fr/en/2019/09/26/cameroun-demarrage-du-projet-de-modernisation-du-cadastre-et-des-domaines/

**AFREF 2024 Workshop (RCMRD, Nairobi, August 2024)**: Cameroon is not listed among the ~22 African countries confirmed to have at least one operational CORS installation. Cameroon's early-AFREF commitment (~2006) to install at least one CORS remains unfulfilled in public sources as of 2026-05-15.
- https://ric2024.rcmrd.org/afref

## Context Notes

- **INC** (Institut National de Cartographie), under MINRESI, is the national geodetic and cartographic authority — geodesy, photogrammetry, topography, cartographic drafting. The 2026-05-15 review of `inc-cameroon.cm` content surfaced no mention of CORS, NTRIP, RTK, real-time corrections, or permanent stations. Public pages describe RINEX archive activities, not streaming services.
  - https://minresi.gov.cm/en/national-institute-of-cartography/
  - https://www.inc-cameroon.cm/
- **MINDCAF** manages cadastral infrastructure and commissioned the FUGRO passive network. No public NTRIP service operates from MINDCAF infrastructure.
- **Volunteer networks (RTK2go, Centipede)**: zero CM/CMR stations (re-verified 2026-05-15).
- **Commercial global networks (GEODNET, ONOCOY, RTKdata)**: no CM stations in published maps as of 2026-05-15.
- **EagleCORS / regional integration plans (Uganda-based, mentions Cameroon as a future partner country)**: no operational Cameroon node has been published; treated as aspirational.
- **Hobbyist access**: not applicable — no caster exists.

## Cross-Border Alternative

**None within ~50 km.** Neighbours: Nigeria (NG), Chad (TD), CAR (CF), Republic of the Congo (CG), Gabon (GA), Equatorial Guinea (GQ). None operates a public free NTRIP caster reachable from CM territory. Nearest rtk2go volunteer base is `fssoyo` in southern Nigeria, ~330 km from the western CM border — well beyond single-base RTK range.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — no confirmed continuously-operated CM station in current archive; sparse legacy campaign data only | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA); CM data availability unconfirmed |
| **IGS NKLG (Gabon, ~590 km SSW of Yaoundé)** — nearest IGS continuous station; useful only for PPP, not RTK | https://network.igs.org/ | Free |

## Sources Consulted (2026-05-15)
- INC / MINRESI: https://minresi.gov.cm/en/national-institute-of-cartography/
- INC operator site: https://www.inc-cameroon.cm/
- Fugro Cameroon case study: https://www.fugro.com/expertise/case-studies/national-geodetic-network-cameroon-fugro
- IGN FI portfolio — Cameroon geodetic network supervision: https://www.ignfi.fr/en/portfolio-item/supervision-des-travaux-du-reseau-geodesique-cameroun/
- IGN FI — Cadastre & Domaines modernisation: https://www.ignfi.fr/en/2019/09/26/cameroun-demarrage-du-projet-de-modernisation-du-cadastre-et-des-domaines/
- GIM International — Africa CORS map: https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- AFREF 2024 / RCMRD: https://ric2024.rcmrd.org/afref
- IGS network: https://network.igs.org/ — 0 CM stations
- SONEL GNSS — 0 CM confirmed-continuous stations
- rtk2go sourcetable (`data/rtk2go.sourcetable`) — 0 CM mountpoints
- Centipede sourcetable (`data/centipede.sourcetable`) — 0 CM mountpoints
- GitHub mvarga1989 CORS list — no CM entry
- ntrip-list.com/africa/ — no CM entry
