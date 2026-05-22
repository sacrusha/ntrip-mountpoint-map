# Cameroon [CM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (re-verified — no operational change since 2026-05-15)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **landing_url** | null — no operator portal exists |
| **access_url** | null — no service exists |
| **host:port** | null |
| **tariff** | null |
| **num_stations** | 0 |
| **vrs** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster has ever been confirmed alive |

## Verification (2026-05-22)

- `py scripts/stations_by_country.py CMR` → `No stations for 'CMR'`.
- `py scripts/stations_by_radius.py 3.85 11.50 600` (Yaoundé) → no stations within 600 km of Yaoundé.
- Live rtk2go sourcetable probe → zero country-tagged Cameroon mountpoints (only false positive is `LACCMR`, a Trimble CMR-format mount in Manitoba, Canada).
- Live Centipede sourcetable probe → zero CMR mountpoints.
- IGS network (network.igs.org, 534 stations as of 2026-05-21) → no IGS station in CM. Nearest IGS reference is **NKLG (Libreville, Gabon)** at (0.354, 9.672), ~439 km SSW of Yaoundé (haversine; bearing 207°). NKLG is rebroadcast on AUSCORS, IGS-IP, and MIRAI casters (verified via local `data/stations.json`, `stations_by_country.py GAB` returns 1 entry per rebroadcaster). Single-base only; ~439 km baseline is far beyond useful RTK range (single-base degrades past ~30 km), but the stream is usable as a long-baseline PPP / static post-processing anchor.

## Most Recent Project / Announcement

**FUGRO / MINDCAF national geodetic network (2010–2012)**: Fugro delivered a national geodetic network of 525 points covering all 10 regions — 25 first-order reference pillars (~1 per 200 km) and 500 second-order points. IGN FI provided technical audit and supervision. This is a **passive monument network**, not a CORS network; no NTRIP caster was deployed.
- https://www.fugro.com/expertise/case-studies/national-geodetic-network-cameroon-fugro
- https://www.ignfi.fr/en/portfolio-item/supervision-des-travaux-du-reseau-geodesique-cameroun/

**IGN FI / GEOFIT / GEODESIGN & BIZ — Land Registration and Estates Modernisation, 2019–ongoing**: consortium awarded delegated project management for Module 1 of MINDCAF's "Modernisation du Cadastre et des Domaines" project (AfDB-financed, ~EUR 1.47 M, 12 months from 2019). Cadastral reform — not CORS/NTRIP.
- https://www.ignfi.fr/en/2019/09/26/cameroun-demarrage-du-projet-de-modernisation-du-cadastre-et-des-domaines/

**AFREF / GIM International "Fully-Fledged CORS Map for Africa" (2026-05-22 re-check)**: Cameroon is not among the 25 African countries with mapped operational CORS networks reported by Corsmap (verified, unverified-but-data-sourced, or unmapped-with-known-network). Cameroon remains in the implicit "no public CORS infrastructure identified" set.
- https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa

**Yaoundé "first CORS antenna" pilot (Doungmo, August 2019)**: A LinkedIn Pulse article by Yannick A. Doungmo, M.Eng describes the Yaoundé antenna as "the first antenna of the project to implement a CORS network in Cameroon", attached to a benchmark of the national geodetic network. The article is a technical reflection on CORS setup (1 cm planimetry at 29 km baseline reported), not an operational service announcement: no host:port, no operator, no NTRIP credentials are published. No subsequent public deployment has surfaced as of 2026-05-22.
- https://fr.linkedin.com/pulse/fonctionnement-dune-station-cors-yannick-arthur-doungmo-m-eng-cspo-

## Context Notes

- **INC** (Institut National de Cartographie), under MINRESI, is the national geodetic and cartographic authority. The 2026-05-22 re-review of `inc-cameroon.cm` content reconfirms a Geodesy Research Laboratory but no mention of CORS, NTRIP, RTK, real-time corrections, or permanent streaming stations.
  - https://minresi.gov.cm/en/national-institute-of-cartography/
  - https://www.inc-cameroon.cm/
- **MINDCAF** manages cadastral infrastructure and commissioned the FUGRO passive monument network (525 reference/base points, no streaming). No public NTRIP service operates from MINDCAF infrastructure.
- **Volunteer networks (RTK2go, Centipede)**: zero CM/CMR stations (re-verified 2026-05-22 via live sourcetable probes).
- **Commercial global networks (GEODNET, ONOCOY, RTKdata)**: no CM stations in published maps as of 2026-05-22.
- **EagleCORS / regional integration plans**: no operational Cameroon node has been published; aspirational only.
- **Hobbyist access**: not applicable — no caster exists.

## Cross-Border Alternative

**None within ~50 km.** Neighbours: Nigeria (NG), Chad (TD), CAR (CF), Republic of the Congo (CG), Gabon (GA), Equatorial Guinea (GQ). None operates a public free NTRIP caster reachable from CM territory. Nearest rtk2go volunteer base is `fssoyo` in south-western Nigeria at (7.84, 3.95), ~500 km from the nearest CM-Nigeria border point — well beyond single-base RTK range. The nearest public-rebroadcast IGS reference is NKLG (Gabon) at ~439 km SSW of Yaoundé, available via AUSCORS / IGS-IP / MIRAI; useful only for long-baseline post-processing, not RTK.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — no confirmed continuously-operated CM station in current archive; sparse legacy campaign data only | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA); CM data availability unconfirmed |
| **IGS NKLG (Gabon, ~439 km SSW of Yaoundé)** — nearest IGS continuous station; useful only for PPP, not RTK. Rebroadcast in real time on AUSCORS, IGS-IP and MIRAI casters | https://network.igs.org/ | Free |

## Sources Consulted (2026-05-22)
- INC / MINRESI: https://minresi.gov.cm/en/national-institute-of-cartography/
- INC operator site: https://www.inc-cameroon.cm/ (2026-05-22: live, no GNSS streaming reference)
- Fugro Cameroon case study: https://www.fugro.com/expertise/case-studies/national-geodetic-network-cameroon-fugro (passive monument network, confirmed)
- IGN FI portfolio — Cameroon geodetic network supervision: https://www.ignfi.fr/en/portfolio-item/supervision-des-travaux-du-reseau-geodesique-cameroun/
- IGN FI — Cadastre & Domaines modernisation: https://www.ignfi.fr/en/2019/09/26/cameroun-demarrage-du-projet-de-modernisation-du-cadastre-et-des-domaines/
- Doungmo LinkedIn Pulse (Aug 2019): https://fr.linkedin.com/pulse/fonctionnement-dune-station-cors-yannick-arthur-doungmo-m-eng-cspo-
- GIM International — Africa CORS map (re-checked 2026-05-22): https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- AFREF 2024 / RCMRD: https://ric2024.rcmrd.org/afref (URL retains historical value but agenda page may 404 post-event)
- IGS network: https://network.igs.org/ — 0 CM stations
- SONEL GNSS — 0 CM confirmed-continuous stations
- rtk2go live sourcetable probe (2026-05-22) — 0 CM mountpoints
- Centipede live sourcetable probe (2026-05-22) — 0 CM mountpoints
- GitHub mvarga1989 CORS list — no CM entry
- ntrip-list.com/africa/ — no CM entry
