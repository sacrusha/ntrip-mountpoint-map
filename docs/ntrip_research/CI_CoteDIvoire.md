# Côte d'Ivoire [CI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21

## Status

One public NTRIP RTK mountpoint live in country: Centipede-RTK `INP02` (Yamoussoukro, single volunteer base). The national RECI CORS network (5 stations + IGS YKRO, operated by BNETD-CIGN) is operational but institutional-only, with no public caster endpoint published. A 15-station World Bank PRESFOR expansion was announced in September 2025.

## Caster — Centipede-RTK `INP02` (volunteer, public)

| Field | Value |
|---|---|
| **landing_url** | https://www.centipede-rtk.org/ |
| **access_url** | https://docs.centipede.fr/ (anonymous; shared credentials `centipede / centipede`) |
| **host:port** | `caster.centipede.fr:2101` (alias `crtk.net:2101`) — mountpoint `INP02`, country tag `CIV`, 6.873 N -5.238 W (Yamoussoukro) |
| **num_stations** | 1 (Centipede INP02) |
| **vrs** | no — single physical base, RTCM3 MSM (1004/1005/1006/1008/1012/1019/1020/1033/1042/1045/1046/1077/1087/1097/1107/1127/1230); GPS+GLO+GAL+BDS+SBAS; receiver Unicore UM980 on RTKBase 2.7.0 |
| **tariff** | free |
| **hobbyist_eligibility** | yes (open community caster) |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-21 — STR row `STR;INP02;CIV;RTCM3;…;CentipedeRTK` returned by live probe of `caster.centipede.fr:2101` |
| **datum_epoch** | omitted — Centipede does not publish a per-volunteer-base epoch declaration; outside its strict French installation track no central post-processing or frame enforcement applies |

Coverage: INP02 supports cm-class single-base RTK within ~30–50 km of Yamoussoukro. Abidjan (~225 km SE), San-Pédro, Bouaké, Korhogo all sit outside that range — local base or NRTK required.

## National Network — RECI (non-public)

**RECI (Réseau CORS Ivoirien)** — operated by **BNETD-CIGN** (Bureau National d'Études Techniques et de Développement / Centre d'Information Géographique National). 5 permanent CORS plus IGS YKRO, concentrated in the south-east. Four-tier national geodetic framework (per BALE / CIGN, FGF 2025 congress):

- RECI (Ordre 0) — 5 CORS + IGS YKRO; declared **ITRF2014** datum, projection **TMCI-5.5**
- RGIR (Ordre 1) — 43 markers, ~1 per 100 km
- RGIO (Ordre 2) — 716 markers (137 rehabilitated under the PAMOFOR contract, July 2020)
- RGID (Ordre 3) — densification, evolutive

**Expansion plan**: 15 additional permanent CORS announced for 2025 under World Bank PRESFOR funding (north and west coverage gaps). 479+ markers re-observed in ITRF2014. Original 5-station deployment was a 2020–2021 Toposat contract under the AFOR/World Bank PAMOFOR land-tenure programme.

**No public NTRIP host:port has been published for RECI.** Access is institutional only — contact BNETD-CIGN (fbale@bnetd.ci, +225 01 01 27 29 94) or via CNTIG (https://cntig.net/). Not in scope for this project as a hobbyist option.

## Volunteer / Free Coverage

- Centipede: 1 station (INP02). `py scripts/stations_by_country.py CIV` → 1.
- rtk2go: 0 CIV mountpoints (probed 2026-05-21).
- EarthScope NOTA: Americas-only.
- GEODNET / ONOCOY / PointOne / Skylark: no CI coverage identified 2026-05-21.

## Post-Processing (RINEX) Fallback

| Service | URL | Notes / Cost |
|---|---|---|
| IGS `YKRO00CIV` (Yamoussoukro, JPL-operated, IGS + Multi-GNSS, status 4 operational) | https://network.igs.org/YKRO00CIV | free; **data-archive only** — IGS API `https://network.igs.org/api/public/stations/YKRO00CIV/` returns `real_time_systems: []`, last RINEX3 2026-05-20 (probed 2026-05-22) |
| RGCI marker dataset (passive monuments) | https://cotedivoire.africageoportal.com/items/004575bd810f47b39e7e4f0f3d73f885 | free open data; post-processing reference only |
| EarthScope GNSS Data Archive (mirrors IGS holdings incl. YKRO) | https://www.earthscope.org/data/gnss-data/ | free non-commercial (account + NULA) |

## Probes (2026-05-22)

- `curl --http0.9 http://caster.centipede.fr:2101/` → `STR;INP02;CIV;RTCM3;1004,1005,1006,1008,1012,1019,1020,1033,1042,1045,1046,1077,1087,1097,1107,1127,1230;3;GLO+GAL+SBS+BDS+GPS;NONE;CIV;6.873;-5.238;0;0;NTRIP RTKBase Unicore_UM980 2.7.0 R4.10Build17548;none;N;N;15200;CentipedeRTK` — confirmed.
- `https://network.igs.org/api/public/stations/YKRO00CIV/` → JSON shows `"real_time_systems":[]`, `"last_data_time":"2026-05-20"`, status 4. Confirms YKRO is archive-only, no real-time NTRIP exposure.
- FGF 2025 congress slides (`geometres-francophones.org/.../S3-2_BALE.pdf`): retrieved, **image-based PDF** — text layer extraction returned no readable strings. Claims that originate from these slides (RECI = 5 CORS + IGS YKRO, declared ITRF2014 / TMCI-5.5, 15-station PRESFOR expansion) cannot be re-verified from the file itself; they are carried into this entry from a Haiku web-search summary of the slides and from BNETD-adjacent reporting. Toposat (2020) confirms only the original 5-CORS scope without a frame or expansion figure. Treat the 15-station 2025 expansion + ITRF2014/TMCI-5.5 declaration as plausible but not first-party verifiable until BNETD-CIGN publishes a text source.

## Sources

- Centipede-RTK: https://www.centipede-rtk.org/ · docs https://docs.centipede.fr/
- Live caster probe: `caster.centipede.fr:2101` (2026-05-21)
- FGF 2025 congress slides — "Le Réseau Géodésique de la Côte d'Ivoire" (BALE, CIGN, Sept 2025): https://www.geometres-francophones.org/5e8sef5sdgf/uploads/2025/09/S3-2_BALE.pdf
- Toposat PAMOFOR project: https://toposat.com/modernization-of-the-geodetic-infrastructure-of-ivory-coast/?lang=en
- Space in Africa interview with BALE (2021): https://spaceinafrica.com/2021/12/20/mr-fernand-bale-director-of-cote-divoire-geographic-and-digital-information-center-discuss-the-nations-national-geospatial-program/
- IGS station page: https://network.igs.org/YKRO00CIV
- ArcGIS Africa GeoPortal RGCI passive monuments: https://cotedivoire.africageoportal.com/items/004575bd810f47b39e7e4f0f3d73f885
- CNTIG: https://cntig.net/
- Local: `py scripts/stations_by_country.py CIV` → 1 (centipede)
