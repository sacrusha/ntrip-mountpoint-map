# Papua New Guinea [PG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh; prior pass 2026-05-06)

## Status: NO confirmed public NTRIP caster (re-confirmed 2026-05-12 — no new announcements found)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster confirmed alive |

## Most Recent Project Announcement

**PNG2020 geodetic datum — Government approval and funding May 2024** — The PNG Government approved and funded development of PNG2020, a new national geodetic datum replacing PNG94. Geoscience Australia, PNGUoT (PNG University of Technology), and the OSG (Office of the Surveyor General) are completing static GNSS reobservations of ~100 stations by mid-2026. The new datum plus PNGMG2020 projected CRS will be submitted to EPSG/ISO TC211. RTCM streaming is described as a future access pathway once the datum is published, but no operational NTRIP caster has been announced. OSG budget for a live RT network remains constrained.

Source: https://link.springer.com/chapter/10.1007/1345_2026_309 · https://ggim.un.org/UNGGCE/documents/CDWA-PAC/Stanaway_DLPP_PNG2020_Bangkok.pdf

## Context Notes

- **CORS in country**: Sparse permanent stations — IGS: LAE1, PNGM. APREF: WAIG, RVO, PORG, HIDE. No real-time NTRIP exposure.
- **OSG / DLPP**: Acknowledged budget constraint for RT networks; PNG2020 datum work is the active geodetic programme.
- **ASPNG**: Identified as potential operator/host for a future subscription CORS; nothing operational yet.
- **No public NTRIP endpoint** has been published by any PNG agency.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede-RTK): no PNG coverage confirmed.
- **Local indexes** (`scripts/stations_by_country.py PNG` 2026-05-12): no rtk2go, Centipede or EarthScope mountpoints tagged PNG.
- **Nearest viable cross-border alternative**: AUSCORS (Geoscience Australia) covers Torres Strait / Cape York side but the PNG mainland sits 150+ km from the nearest active AUSCORS site — outside the practical single-base baseline.
- Practical workaround for hobbyists: deploy a local base station for single-base RTK, or use satellite-based PPP services (Trimble RTX, u-blox PointPerfect where available, Galileo HAS — note HAS service area covers Australasia).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGS / EarthScope** — LAE1, PNGM stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial; USD 1,000/seat/yr commercial |
| **APREF / Geoscience Australia** — WAIG, RVO, PORG, HIDE | https://gnss.ga.gov.au/ | Free |

## Sources Consulted
- PNG2020 datum — UN-GGIM CDWA-PAC presentation (Stanaway, DLPP): https://ggim.un.org/UNGGCE/documents/CDWA-PAC/Stanaway_DLPP_PNG2020_Bangkok.pdf
- PNG2020 — Springer Nature (2026): https://link.springer.com/chapter/10.1007/1345_2026_309
- FIG 2022 PNG geodetic case study (Stanaway): https://www.fig.net/resources/proceedings/fig_proceedings/fig2022/ppt/rfip/10_rfip_2022_stanaway.pdf
- ASPNG (Association of Surveyors of PNG) — PNG94 technical manual: https://www.aspng.org/techinfopng94.htm
- Emlid Flow — Papua New Guinea CS setup: https://docs.emlid.com/emlid-flow/preparing-projects/cs-setup/countries/papua-new-guinea/
- IGS / EarthScope station list: https://www.earthscope.org/data/gnss-data/
- APREF / Geoscience Australia GNSS: https://gnss.ga.gov.au/
- NTRIP-list.com Pacific: https://ntrip-list.com/
