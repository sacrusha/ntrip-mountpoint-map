# Suriname [SR] — NTRIP RTK Caster Research
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

## Most Recent Relevant Project

**IDB project SU-L1067** (Spatial Planning Suriname, signed December 2024): Covers spatial planning and environmental management — no geodetic/GNSS positioning component identified.
URL: https://www.iadb.org/en/project/SU-L1067

No project explicitly plans an NTRIP/CORS network for Suriname.

## Context Notes

- **SIRGAS-CON**: Suriname has at least one static GNSS monument processed by IBGE's SIRGAS-CON analysis centre — **post-processing RINEX only**, not a public NTRIP RTK stream. Not in SIRGAS-RT real-time tier.
- **MI-GLIS** (land registry/cadastral authority): No mention of GNSS correction service or CORS infrastructure on website.
- **GISsat NV** (Esri/Trimble distributor, Suriname): Resells Trimble Catalyst (PPP/SSR, not NTRIP CORS). No NTRIP caster operated.
- **Brazil RBMC-IP** (rtk.ibge.gov.br:2101): Northernmost stations ~700–900 km from Paramaribo — too distant for single-baseline RTK.
- **Kadaster International** (Dutch) involvement in land administration modernisation: Registry focus only, no GNSS infrastructure.
- Global commercial networks (GEODNET, ONOCOY, HxGN SmartNet, Topcon, Centipede-RTK, RTKdata, ArduSimple): No Suriname coverage confirmed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive / SIRGAS-CON** — Suriname has at least one GNSS monument processed by IBGE's SIRGAS-CON analysis centre; RINEX retrievable via EarthScope archive | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

## Sources Consulted
- RTK2GO SNIP monitor
- SIRGAS station list, SIRGAS-RT project paper
- NTRIP-list.com South America
- MI-GLIS (miglis.sr)
- GISsat Suriname (gissatcloud.com)
- ArduSimple country directory
- corsstations.com, GitHub mvarga1989 CORS list
- IGS Real-Time Service
- HxGN SmartNet, GEODNET, Centipede-RTK, RTKdata
- IDB projects SU-T1146 and SU-L1067
- gov.sr GEO Spatial Intelligence Hub
