# Libya [LY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster confirmed alive |

## Most Recent Project Announcement

No formal announcement for a Libyan national NTRIP/RTK caster was found in any development-bank, UN, or geospatial trade press source as of 2026-05-12. A private geospatial consultancy, **Geospatial Libya** (`geospatiallibya.ly`), advertises GIS, mapping and surveying services but no CORS / RTK / NTRIP network. Libya's ongoing civil conflict and institutional fragmentation have severely constrained geospatial infrastructure investment since 2011.

## Context Notes

- **Institutional landscape:** Libya's cadastral and geodetic functions are nominally under the General Authority for Information and Communication Technology (GAICT) and the National Centre for Remote Sensing and Space Sciences. Effective operations have been severely disrupted since the 2011 revolution and subsequent conflict.
- **IGS stations:** No confirmed IGS reference station exists in Libya. Libya falls within a documented coverage gap in the North African IGS network; no station code or EarthScope archive entry for a Libyan site was found as of 2026-05-06.
- **AFREF:** Libya is noted in AFREF literature as lacking functional CORS contributing to the African geodetic reference frame.
- **Neighbouring networks:** Tunisia (OTC, 23 stations) to the northwest and Egypt (EgyptCORS) to the east could theoretically provide partial coverage near borders, but baselines would be far too long (hundreds of km) for reliable RTK.
- **Global commercial networks:** No Libya coverage confirmed for GEODNET, ONOCOY, or PointOne.
- **Security/access:** The security situation makes field installation of new CORS infrastructure practically difficult for international partners.
- **No volunteer presence**: `py scripts/stations_by_radius.py 26.0 17.0 500` returns zero stations within 500 km of central Libya across rtk2go, Centipede and EarthScope. `py scripts/stations_by_country.py` lists no LBY / LY entries in any source as of 2026-05-12. Tunisian/Egyptian sub-net are >500 km from most of populated Libya.
- Practical workaround: Deploy a local base station for single-base RTK, or use satellite-based PPP (Trimble RTX, Fugro StarFix, Galileo HAS ~20 cm).

## Post-Processing (RINEX) Fallback

No confirmed operational CORS station in Libya with public RINEX archive found.

## Sources Consulted
- RTK2GO monitor (monitor.use-snip.com) — no Libya mount points
- NTRIP-list.com Africa page — no Libya entries
- ArduSimple country selector — Libya not listed as having national RTK network
- AFREF literature (ResearchGate)
- BKG NTRIP streams — no Libya entries
- GEODNET, ONOCOY — no Libya coverage confirmed
- English and Arabic web searches — no NTRIP caster found
- Geospatial Libya (private consultancy, no CORS): https://geospatiallibya.ly/en/our-services/
- IGN FI / Libya cartography references (no CORS context): https://en.wikipedia.org/wiki/IGN_FI
- Local pipeline check (2026-05-12): `py scripts/stations_by_radius.py 26.0 17.0 500` → no stations within 500 km; `py scripts/stations_by_country.py` → no LBY/LY codes
