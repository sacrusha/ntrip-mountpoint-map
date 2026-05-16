# Côte d'Ivoire [CI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: One public NTRIP mountpoint live (Centipede `INP02`, Yamoussoukro). National RECI CORS remains non-public.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Centipede-RTK `INP02` (single volunteer base, 6.873°N -5.238°W — Yamoussoukro). National RECI CORS (BNETD-CIGN, 5 stations) is operational but not publicly addressable. |
| **landing_url** | https://www.centipede-rtk.org/ |
| **access_url** | https://docs.centipede.fr (anonymous; no registration required for caster.centipede.fr:2101) |
| **host:port** | caster.centipede.fr:2101 (alias crtk.net:2101) — mountpoint `INP02` |
| **tariff** | free |
| **num_stations** | 1 (Centipede INP02). RECI = 5 institutional stations, no public endpoint. |
| **vrs** | No — single physical base, RTCM3 MSM (1004/1005/1006/1008/1012/1019/1020/1033/1042/1045/1046/1077/1087/1097/1107/1127/1230); GPS+GLO+GAL+BDS+SBAS. |
| **hobbyist_eligibility** | Yes for Centipede INP02 (open access, anonymous). No for RECI (institutional channel only). |
| **legal_residency_required** | No (Centipede). Unclear / likely yes for RECI. |
| **last_confirmed_alive** | 2026-05-15 — `STR;INP02;CIV;RTCM3;...;CentipedeRTK` returned by `curl --http0.9 http://caster.centipede.fr:2101/` (three consecutive probes). |
| **datum_epoch** | Centipede stations stream raw RTCM3 referenced to ITRF / IGS realisation; Centipede docs do not pin a published epoch for individual volunteer bases. https://docs.centipede.fr |

## Operational NTRIP Endpoint

**Centipede-RTK `INP02`** — Yamoussoukro region (lat 6.873, lon -5.238). Receiver: Unicore UM980 running RTKBase 2.7.0; full multi-GNSS RTCM3 MSM message set. Country code in sourcetable: `CIV`. Caster identity line: `CAS;crtk.net;2101;Millipede-caster;Centipede-RTK;0;FRA;...`. The node was not present in earlier 2026-05-12 fetches and is absent from the local 2026-05-15 18:22Z pipeline snapshot (`data/centipede.sourcetable`); it is present in three live probes on 2026-05-15 — likely added between pipeline runs. Next scheduled fetch should ingest it.

Connect example: `host=caster.centipede.fr port=2101 mount=INP02 user=centipede pass=centipede` (Centipede uses a shared anonymous credential per https://docs.centipede.fr).

## National CORS (Non-Public): RECI

**RECI (Réseau CORS Ivoirien)** — operated by **BNETD-CIGN** (Bureau National d'Études Techniques et de Développement — Centre d'Information Géographique National). Five permanent GNSS stations plus one IGS site (YKRO, Yamoussoukro). RTK NTRIP mode enabled 2022. The four-tier national geodetic framework:

- **RECI** — 5 active CORS + IGS YKRO (continuous-operation tier)
- **RGIR** (Réseau Géodésique de Référence Ivoirien) — 43 markers at ~1 point per 100 km, established 1998
- **RGIO** (Réseau Géodésique Opérationnel Ivoirien) — 716 markers
- **RGID** (Réseau Géodésique de Détail Ivoirien) — densification tier

**No public NTRIP caster host:port has been published for RECI.** Access is institutional only — contact BNETD-CIGN via CNTIG (Comité National de Télédétection et d'Information Géographique, https://cntig.net/). Confirmed operational in the September 2025 FGF congress presentation "Le Réseau Géodésique de la Côte d'Ivoire" (Fernand BALE, Directeur CIGN). Modernisation supported by Toposat.

Sources:
- FGF 2025 congress: https://www.geometres-francophones.org/5e8sef5sdgf/uploads/2025/09/S3-2_BALE.pdf
- Toposat project page: https://toposat.com/modernization-of-the-geodetic-infrastructure-of-ivory-coast/?lang=en
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
- **Global commercial networks**: GEODNET, ONOCOY, PointOne, Skylark — no CI coverage identified as of 2026-05-15.

## Probes (2026-05-15)

- `curl --http0.9 --max-time 10 http://caster.centipede.fr:2101/` → returned full sourcetable; `STR;INP02;CIV;RTCM3;1004,...,1230;3;GLO+GAL+SBS+BDS+GPS;NONE;CIV;6.873;-5.238;0;0;NTRIP RTKBase Unicore_UM980 2.7.0 R4.10Build17548;none;N;N;15200;CentipedeRTK` (consistent across 3 probes).
- `curl --http0.9 --max-time 10 http://crtk.net:2101/` → same INP02 entry (DNS alias).
- `curl http://rtk2go.com:2101/` → zero CI/CIV mountpoints (one false-positive `INGLOCIVIL;Cuenca` in Ecuador).
- IGS API `https://network.igs.org/api/public/stations/?country=CIV` → 1 station: `YKRO00CIV`, status 4, last data 2026-05-13, `real_time_systems: []`.

## Sources Consulted

- Live caster probes: `caster.centipede.fr:2101`, `crtk.net:2101`, `rtk2go.com:2101`
- IGS Network API: https://network.igs.org/api/public/stations/?country=CIV
- IGS station page: https://network.igs.org/YKRO00CIV
- FGF 2025 congress — "Le Réseau Géodésique de la Côte d'Ivoire" (BALE, CIGN): https://www.geometres-francophones.org/5e8sef5sdgf/uploads/2025/09/S3-2_BALE.pdf
- Toposat — Modernisation of geodetic infrastructure of Ivory Coast: https://toposat.com/modernization-of-the-geodetic-infrastructure-of-ivory-coast/?lang=en
- CNTIG: https://cntig.net/
- ArcGIS Africa GeoPortal — RGCI dataset: https://cotedivoire.africageoportal.com/items/004575bd810f47b39e7e4f0f3d73f885
- Centipede-RTK: https://www.centipede-rtk.org/ · docs https://docs.centipede.fr
- Local pipeline: `data/centipede.sourcetable` (snapshot 2026-05-15 18:22Z — INP02 not yet captured), `data/stations.json` (CIV count = 0 in current snapshot)
- mvarga1989/The-list-of-GNSS-CORS-RTK-networks — no public CI entry
- AFREF 2024 / RCMRD: https://ric2024.rcmrd.org/afref
