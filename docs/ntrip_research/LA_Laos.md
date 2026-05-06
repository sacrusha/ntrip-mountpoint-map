# Laos [LA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster — CORS infrastructure being built (IGN FI project)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (not confirmed) |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no public NTRIP caster confirmed |

## Most Recent Project Announcement

- **IGN FI (IGN France International)** has a live portfolio page titled "Continuously operating reference system (CORS), LAOS" (ignfi.fr/en/portfolio-item/cors-laos/), last updated May 2024. The project involves IGN FI providing and installing permanent GNSS stations for real-time positioning across Laos. Commissioned by an unspecified Lao government body (likely the Department of Land Management or equivalent). No public access endpoint or NTRIP URL is disclosed on the IGN FI page.
- **First CORS station (2013)**: ComNav Technology helped Laos commission its first CORS station in November 2013, using a ComNav M300 receiver with CDC CORS software. This was also the first BeiDou CORS in Laos. Purpose: land surveying, mapping, and forestry management. Source: comnavtech-ag.com.

## Context Notes

- **Lao PDR** has very limited publicly documented GNSS infrastructure. The 2013 ComNav single-station installation appears to have been a government pilot; no follow-up national network announcement was found until the IGN FI project (~2024).
- IGN FI's portfolio page confirms active project work but does not disclose whether a public NTRIP stream is operational or accessible to non-government users.
- The DOL-RTK network at dol-rtknetwork.com is **Thailand's** Department of Lands RTK network (Thai-language interface, 114 CORS covering Thailand), not Laos. Confusion possible due to similar naming.
- Land administration in Laos: as of recent ADB reports, only ~1.5 million of 3–3.5 million land plots registered — highlighting need for RTK-grade positioning, but institutional capacity is still developing.
- Regional context: neighboring Vietnam has a mature national CORS/NTRIP network; Thailand has the DOL-RTK network. Laos is several years behind both.
- RTK2go: no Laos base stations confirmed.
- Practical alternative for hobbyists: deploy a local base station; Galileo HAS (~40 cm, no internet); GEODNET or Onocoy (coverage in LA not confirmed).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGN FI / Lao government CORS data** — contact via IGN FI or Lao DLM | https://www.ignfi.fr | Unknown |
| **IGS/EarthScope archive** (any IGS stations in Laos) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

## Sources Consulted
- IGN FI portfolio: ignfi.fr/en/portfolio-item/cors-laos/ (May 2024 update)
- ComNav Technology: comnavtech-ag.com/comnav-helped-laos-to-build-the-first-cors-station/
- ArcGIS StoryMaps — Towards Enhanced Land Administration in Lao PDR
- ADB Country Partnership Strategy Lao PDR 2024–2028
- DOL-RTK network (dol-rtknetwork.com) — confirmed to be Thailand, not Laos
- RTK2go monitor (monitor.use-snip.com — no LA stations visible)
- rtcm-ntrip.org (no Laos entries found)
- GNSS.asia (gnss.asia/our-services/ — regional GNSS services aggregator; no Laos-specific NTRIP listed)
