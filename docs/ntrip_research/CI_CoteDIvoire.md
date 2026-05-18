# Côte d'Ivoire [CI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17

## Status: One public NTRIP mountpoint live (Centipede `INP02`, Yamoussoukro). National RECI CORS (5 stations + IGS YKRO) operational but institutional-only; 15-station expansion under BM/PRESFOR funding announced Sept 2025.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Centipede-RTK `INP02` (single volunteer base, 6.873°N -5.238°W — Yamoussoukro). National RECI CORS (BNETD-CIGN, 5 stations + IGS YKRO) is operational but not publicly addressable. |
| **landing_url** | https://www.centipede-rtk.org/ |
| **access_url** | https://docs.centipede.fr (anonymous; no registration required for caster.centipede.fr:2101) |
| **host:port** | caster.centipede.fr:2101 (alias crtk.net:2101) — mountpoint `INP02` |
| **tariff** | free |
| **num_stations** | 1 (Centipede INP02). RECI = 5 institutional CORS + IGS YKRO; 15-station expansion planned 2025 per CIGN. |
| **vrs** | No — single physical base, RTCM3 MSM (1004/1005/1006/1008/1012/1019/1020/1033/1042/1045/1046/1077/1087/1097/1107/1127/1230); GPS+GLO+GAL+BDS+SBAS. |
| **hobbyist_eligibility** | Yes for Centipede INP02 (open access, anonymous). No for RECI (institutional channel only). |
| **legal_residency_required** | No (Centipede). Unclear / likely yes for RECI. |
| **last_confirmed_alive** | 2026-05-17 — `STR;INP02;CIV;RTCM3;...;CentipedeRTK` returned by live probe of `http://caster.centipede.fr:2101/`. |
| **datum_epoch** | RECI/national framework: **ITRF2014**, national projection TMCI-5.5 — declared by CIGN director Fernand BALE, FGF 2025 congress (Sept 2025). https://www.geometres-francophones.org/5e8sef5sdgf/uploads/2025/09/S3-2_BALE.pdf · Centipede INP02 is a volunteer base — Centipede docs do not pin a published epoch per node. |

## Operational NTRIP Endpoint

**Centipede-RTK `INP02`** — Yamoussoukro region (lat 6.873, lon -5.238). Receiver: Unicore UM980 running RTKBase 2.7.0; full multi-GNSS RTCM3 MSM message set. Country code in sourcetable: `CIV`. Caster identity line: `CAS;crtk.net;2101;Millipede-caster;Centipede-RTK;0;FRA;...`. Confirmed alive 2026-05-17 via live probe of `caster.centipede.fr:2101`.

Connect example: `host=caster.centipede.fr port=2101 mount=INP02 user=centipede pass=centipede` (Centipede uses a shared anonymous credential per https://docs.centipede.fr).

## National CORS (Non-Public): RECI

**RECI (Réseau CORS Ivoirien)** — operated by **BNETD-CIGN** (Bureau National d'Études Techniques et de Développement — Centre d'Information Géographique National). 5 permanent GNSS stations + IGS YKRO, concentrated SE of country. Four-tier national geodetic framework (per BALE FGF 2025):

- **RECI** (Ordre 0) — 5 CORS + IGS YKRO; ITRF2014 datum, TMCI-5.5 projection
- **RGIR** (Ordre 1, Réseau Géodésique Ivoirien de Référence) — 43 markers, ~1 point per 100 km
- **RGIO** (Ordre 2, Réseau Géodésique Ivoirien Opérationnel) — 716 markers (137 rehabilitated under PAMOFOR contract, July 2020)
- **RGID** (Ordre 3, Réseau Géodésique Ivoirien de Détail) — densification tier, evolutive

**Expansion plan**: 15 additional permanent GNSS stations planned in 2025 under World Bank PRESFOR project funding (covering north and west gaps). 479+ markers re-observed in ITRF2014. CIGN co-chairs UN sub-committee on geodesy and AFREF implementation working group.

**No public NTRIP caster host:port has been published for RECI.** Access is institutional only — contact BNETD-CIGN (fbale@bnetd.ci, +225 01 01 27 29 94) or via CNTIG (https://cntig.net/). Original 5-station deployment was a 2020-2021 Toposat contract under AFOR/World Bank PAMOFOR land-tenure programme.

Sources:
- FGF 2025 congress slides: https://www.geometres-francophones.org/5e8sef5sdgf/uploads/2025/09/S3-2_BALE.pdf
- Toposat project page (2020 PAMOFOR scope): https://toposat.com/modernization-of-the-geodetic-infrastructure-of-ivory-coast/?lang=en
- LinkedIn consultant brief (Boullard): https://fr.linkedin.com/pulse/modernisation-de-linfrastructure-g%C3%A9od%C3%A9sique-c%C3%B4te-divoire-boullard
- CNTIG: https://cntig.net/

## Reference Stations & Post-Processing

| Service | URL | Notes / Cost |
|---|---|---|
| **IGS `YKRO00CIV`** (Yamoussoukro) — operated by JPL, IGS + IGS Multi-GNSS networks, status 4 (operational), last RINEX 2026-05-13 | https://network.igs.org/YKRO00CIV | Free. **Data-archive only** — IGS API reports `real_time_systems: []`. No NTRIP stream. Useful for static post-processing. |
| **RGCI marker dataset** (Réseau Géodésique de Côte d'Ivoire) — passive monument coordinates | https://cotedivoire.africageoportal.com/items/004575bd810f47b39e7e4f0f3d73f885 | Free open data. Post-processing reference only. |
| **EarthScope GNSS Data Archive** — mirrors IGS holdings incl. YKRO | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA). |

## Centipede Catchment & Cross-Border

- **INP02** alone gives sub-cm RTK only within roughly 30–50 km of Yamoussoukro before baseline length degrades the fix. Abidjan (~225 km SE of INP02), San-Pédro, Bouaké, Korhogo all sit well outside that range — local base / NRTK still required there.
- **Nearest cross-border alternatives within ~50 km of CI borders: none.** Ghana's national CORS (Lands Commission, unveiled August 2025) has no public NTRIP caster. IGN Bénin and IGNTOGO Togo CORS are likewise non-public. Burkina Faso, Mali, Liberia, Guinea have no documented public RTK service.
- **Global commercial networks**: GEODNET, ONOCOY, PointOne, Skylark — no CI coverage identified as of 2026-05-17.

## Probes (2026-05-17)

- `curl --max-time 15 http://caster.centipede.fr:2101/` → `STR;INP02;CIV;RTCM3;1004,...,1230;3;GLO+GAL+SBS+BDS+GPS;NONE;CIV;6.873;-5.238;0;0;NTRIP RTKBase Unicore_UM980 2.7.0 R4.10Build17548;none;N;N;15200;CentipedeRTK` — confirmed.
- `curl http://rtk2go.com:2101/` → 0 CIV mountpoints.
- IGS Network: `YKRO00CIV` archive-only, `real_time_systems: []`.

## Sources Consulted

- Live caster probe: `caster.centipede.fr:2101` (2026-05-17)
- FGF 2025 congress — "Le Réseau Géodésique de la Côte d'Ivoire" (BALE, CIGN, Sept 2025): https://www.geometres-francophones.org/5e8sef5sdgf/uploads/2025/09/S3-2_BALE.pdf
- Toposat PAMOFOR project page: https://toposat.com/modernization-of-the-geodetic-infrastructure-of-ivory-coast/?lang=en
- LinkedIn — Boullard consultant note: https://fr.linkedin.com/pulse/modernisation-de-linfrastructure-g%C3%A9od%C3%A9sique-c%C3%B4te-divoire-boullard
- Space in Africa interview with BALE (2021): https://spaceinafrica.com/2021/12/20/mr-fernand-bale-director-of-cote-divoire-geographic-and-digital-information-center-discuss-the-nations-national-geospatial-program/
- IGS station page: https://network.igs.org/YKRO00CIV (archive-only)
- ArcGIS Africa GeoPortal — RGCI passive monuments: https://cotedivoire.africageoportal.com/items/004575bd810f47b39e7e4f0f3d73f885
- CNTIG: https://cntig.net/
- Centipede-RTK: https://www.centipede-rtk.org/ · docs https://docs.centipede.fr
