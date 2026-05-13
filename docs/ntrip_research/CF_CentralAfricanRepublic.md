# Central African Republic [CF] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revising 2026-05-06 entry — no material changes; volunteer counts re-verified)

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

None found. No published project timeline for any CAR CORS/NTRIP service.

**AFREF Workshop 2024** (RCMRD, Nairobi, August 2024): Renewed push for station deployment across Africa — CAR not specifically mentioned as active or imminent participant.
URL: https://ric2024.rcmrd.org/afref

## Context Notes

- **No GNSS CORS infrastructure**: CAR has no IGS-affiliated permanent GNSS station, no CORS, no NTRIP caster of any kind.
- **BANGA/Bangui**: Appears in legacy UNAVCO/GAGE DAI as a historical campaign-mode GPS monument (one-time ITRF/plate motion survey) — NOT a continuously operating CORS. Not in IGSNetwork.json or IGS station log archive. No NTRIP mountpoint.
- **No CF entry** in: IGS network, ITRF2020, SONEL, AFREF 25-country list, RTKdata Africa coverage, GitHub mvarga1989 list.
- **Enabling condition deficits**: Electricity access ~8% of households (2024); limited internet penetration; ongoing security instability — all impede fixed-infrastructure investment.
- Global commercial networks (GEODNET, ONOCOY, Centipede-RTK, RTKdata): No CF coverage.
- **Local pipeline data (verified 2026-05-12)**: rtk2go CAF = 0, centipede CAF = 0 in `data/stations.json` (fetched 2026-05-12T18:17Z). No change.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — legacy BANGA/Bangui campaign-mode monument may have limited RINEX data; not confirmed in current archive | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) — availability of CAR data uncertain |

## Sources Consulted
- IGS network.igs.org — 0 results for CF
- IGSNetwork.json, IGS station log archive
- UNAVCO/GAGE Data Archive Interface
- ITRF2020 network list
- SONEL GNSS database
- AFREF (UN-SPIDER, RCMRD apps portal)
- GitHub mvarga1989 CORS list
- GIM International CORS Africa map
- RTKdata, RTK2GO, Centipede-RTK
- BKG NTRIP, EarthScope/GAGE real-time
