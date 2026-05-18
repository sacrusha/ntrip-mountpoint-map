# Syria [SY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified from 2026-05-13 — no change in operational status; no NTRIP / CORS announcement; HOT Syria ReMapping 2025-2026 still the only active geospatial effort)

## Status: NO — no public NTRIP infrastructure; pre-conflict geodetic agency (GORS) never operated a CORS/NTRIP service; post-conflict reconstruction in early stages with no GNSS-infrastructure announcement found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Operator** | — (pre-conflict mapping authority: **General Organization of Remote Sensing / GORS**, الهيئة العامة للاستشعار عن بُعد, established 1986 in Damascus; remote-sensing / land-survey remit, but no CORS or NTRIP service ever documented) |
| **host:port** | — |
| **VRS** | — |
| **tariff** | — |
| **num_stations** | 0 |
| **hobbyist_eligibility** | — |
| **legal_residency_required** | — |
| **last_confirmed_alive** | — |
| **datum_epoch** | omitted — N/A (no caster, no operator declaration to cite) |
| **Most recent project announcement** | None found for GNSS / CORS / NTRIP in Syria as of 2026-05-13. The most visible 2025–2026 geospatial activity is OSM-focused: **Humanitarian OpenStreetMap Team (HOT) "Syria ReMapping 2025–2026"** (Nov 2025 – May 2026), which produces vector OSM data for rural Aleppo and Rural Damascus and does **not** establish CORS or NTRIP infrastructure |

## Context Notes

- Syria has been in civil conflict since 2011, with full-scale war devastating most infrastructure. As of 2025–2026 a post-conflict reconstruction period is beginning following regime change in December 2024, but no geodetic CORS or NTRIP infrastructure has been announced.
- **Pre-conflict mapping authority**: the **General Organization of Remote Sensing (GORS)** / الهيئة العامة للاستشعار عن بُعد — Syrian space-research agency established 1986, headquartered in Damascus, remit covers aerospace and land surveying using remote-sensing techniques (LANDSAT, SPOT). The previous research-file mention of a "General Commission for Remote Sensing / GCRS" reflects an alternative English transliteration of the same body (GORS is the spelling used by the IAF and Springer Nature). Citable source for the mandate is the Springer Nature chapter listed under Sources Consulted; the Wikipedia entity page is retained only as a secondary cross-reference per primer guidance (country-specific entity pages borderline-OK). No GNSS CORS or NTRIP service was operated by GORS pre-conflict.
- No volunteer rtk2go or Centipede bases found inside Syria (re-cross-checked 2026-05-13 via `py scripts/stations_by_radius.py 35.0 38.5 200` — no stations within 200 km of central Syria).
- No RINEX download portal found for Syrian CORS data.
- Arabic-language search ("نظام RTK GNSS NTRIP سوريا") returned no Syria-specific real-time services — only generic RTK technology articles.
- Western sanctions still complicate foreign-issued credentials and remittance to Syrian government services; any post-conflict NTRIP service emerging would face this hurdle.

## Most Recent Project Announcement

None identified as of 2026-05-13. Post-conflict reconstruction planning is in early stages; any geodetic-network restoration project would be a multi-year undertaking. The closest currently active geospatial effort is the HOT OSM "Syria ReMapping 2025–2026" (vector OSM data only, not GNSS infrastructure).

## Post-Processing (RINEX) Fallback

None available for Syria specifically. Nearest IGS / EUREF stations: Jordan (JORD class), Turkey (multiple TUSAGA-Aktif sites — paid/residency-gated for real-time, free RINEX archive via TUBITAK and EUREF). Baselines of 200–600 km — usable for PPP / PPK but not RTK.

## Sources Consulted
- WebSearch "Syria NTRIP RTK GNSS correction caster 2025 2026" (2026-05-13) — no active services found
- WebSearch "Syria CORS GNSS 2025 2026 reconstruction geodesy Damascus" (2026-05-13) — only HOT Syria ReMapping 2025–2026 surfaced, no GNSS infrastructure announcements
- WebSearch Arabic "نظام RTK GNSS NTRIP سوريا تحديد المواقع المساحة 2024 2025" — no Syria-specific results
- General Organization of Remote Sensing (GORS): https://en.wikipedia.org/wiki/General_Organization_of_Remote_Sensing ; Springer chapter "A Brief Account of the General Organization of Remote Sensing (GORS) in Syria and its Activities" — confirmed mandate is remote sensing, not GNSS CORS
- HOT Syria ReMapping 2025–2026: https://www.hotosm.org/en/projects/syria-remapping-2025-2026/
- `data/stations.json` cross-check (`py scripts/stations_by_radius.py 35.0 38.5 200`) — zero hits
