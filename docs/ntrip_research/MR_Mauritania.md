# Mauritania [MR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-17 — still no public caster)

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

No formal project announcement for a Mauritanian national NTRIP/RTK caster was found in any development-bank (World Bank, AfDB), UN, or geospatial trade press source as of 2026-05-06.

A 2018 case study (Spectra Geospatial) documented that a power-transmission infrastructure survey in Mauritania used Trimble RTX satellite-delivered PPP corrections for the SP60 GNSS receiver — implying that no ground-based NTRIP caster was available to that surveying team.

## Context Notes

- **No national CORS found**: Searches in Arabic, French, and English found no Mauritanian national CORS network or RTK caster. The national geodetic/mapping authority (Direction de la Géodésie, Topographie et de la Cartographie — DGTC, sometimes referenced as GDGTA) has no publicly documented GNSS correction service.
- **AFREF**: Mauritania is referenced in AFREF context as needing at least one high-order CORS station for continental frame inclusion, but no confirmed operational Mauritanian CORS appears in published AFREF station lists or in the BKG NTRIP caster sourcetable.
- **IGS**: No Mauritanian IGS station is confirmed to provide a public real-time NTRIP stream.
- **Survey practice**: Commercial surveys in Mauritania (oil/gas, infrastructure) rely on satellite PPP (Trimble RTX, Fugro StarFix) or shipping a base station to site.
- **Global commercial networks**: GEODNET, ONOCOY, PointOne — no confirmed Mauritania coverage.
- **Practical workaround**: Deploy a local base station for single-base RTK, or use satellite-based PPP (Galileo HAS, Trimble RTX).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — check for any Mauritania-area IGS campaign stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |

## Sources Consulted
- ArduSimple country selector — no Mauritania page found
- RTK2go monitor (monitor.use-snip.com) — no Mauritanian streams
- NTRIP-list.com Africa page — no Mauritania entry
- AFREF 2024 Workshop proceedings: https://ric2024.rcmrd.org/afref
- GIM International — "Developing a Fully Fledged CORS Map for Africa"
- GitHub mvarga1989 — GNSS CORS RTK networks list (no Mauritania entry)
- Spectra Geospatial — SP60 Mauritania survey case study
- BRGM InfoTerre — SIGAfrique project (2005 reference only; no RTK)
- General searches in Arabic (موريتانيا GNSS RTK) and French
- py scripts/stations_by_radius.py 20.0 12.0 800 (2026-05-12) — zero rtk2go/Centipede/EarthScope volunteer stations within 800 km of central Mauritania; nearest free alternatives are in Morocco (ANCFCC, paid) and Senegal (planned JICA CORS, 2024 announcement)
- Re-verified 2026-05-12 via WebSearch: no announcement of a Mauritanian national NTRIP/CORS network found
