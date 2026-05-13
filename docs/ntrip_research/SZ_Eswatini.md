# Eswatini [SZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (revised from 2026-05-06 — Surveyor General status unchanged; one volunteer rtk2go base inside SZ territory now confirmed)

## Status: NO national caster; Surveyor General maintains only a passive trigonometric network. ONE volunteer rtk2go base (`mabuda_farm`) is operating inside Eswatini at -26.47°, 31.94°; nearest national network (South Africa TrigNet) does not extend into SZ

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (government)** | No |
| **Operator** | Surveyor General's Department (Ministry of Natural Resources and Energy) — traditional trigonometric control network only; no GNSS CORS programme identified |
| **host:port** | — |
| **VRS** | — |
| **tariff** | — |
| **hobbyist_eligibility** | — for government caster (none); see Volunteer below for rtk2go |
| **legal_residency_required** | — |
| **last_confirmed_alive** | — for government caster (none); rtk2go `mabuda_farm` station coordinates last confirmed 2026-05-13 in `data/stations.json` |
| **Most recent project announcement** | None found for GNSS CORS; geological mapping programme with South Africa's Council for Geoscience announced 2023-12, concluded mid-2024 — no CORS component. Ministry annual budget performance report for 2024/25 mentions Deeds Registry document volumes only, no GNSS-infrastructure line items |

## Volunteer Option Inside Eswatini

A single community-operated rtk2go base is registered inside Eswatini territory:

| Field | Value |
|---|---|
| **host:port** | `rtk2go.com:2101` |
| **Mountpoint** | `mabuda_farm` |
| **Location** | –26.47°, 31.94° (Lubombo region, ~10 km W of the Mozambique border, ~6 km S of Siteki) |
| **Coverage radius** | ~30 km useful single-base RTK from the antenna (terrain dependent) |
| **Stream type** | Single-base RTCM 3 (typical rtk2go community-base profile; constellations / cadence depend on the operator's receiver) |
| **tariff** | Free — register an email at rtk2go.com for credentials, abide by SNIP fair-use rules |
| **hobbyist_eligibility** | Yes (rtk2go's entire raison d'être) |
| **legal_residency_required** | No — global free service |
| **Reliability caveat** | Uptime, antenna model, and continuity are at the volunteer operator's discretion; SNIP "reliability" star rating on `monitor.use-snip.com` should be checked before fieldwork |

The next-nearest base is `LouwNPP` on the South African side at –27.34°, 30.90°, 130 km from the SZ centroid — beyond single-base RTK working range from most of Eswatini but usable from the southwestern Shiselweni corner.

## Context Notes

- Eswatini (formerly Swaziland) is a small landlocked kingdom (~17,400 km²) in southern Africa, bordered by South Africa and Mozambique.
- The Surveyor General's Department under the Ministry of Natural Resources and Energy handles geodetic controls, cadastral survey approval, and trigonometric network maintenance. Functions are traditional (trigonometric network, cadastral survey approval, boundary demarcation) with no mention of CORS or RTK real-time services. The Deeds Registry, also under this ministry, handles cadastral documentation but operates no GNSS service.
- The national datum is Hartebeesthoek94 (shared with South Africa, Lesotho, Zimbabwe).
- **South Africa TrigNet:** The South African National Geo-spatial Information (NGI) TrigNet network (`trignet.co.za`) is free and covers South Africa with NTRIP RTK, but does not extend into Eswatini territory. The nearest TrigNet station is near the South African border, approximately 10–30 km outside Eswatini. From border areas (Lavumisa, Nhlangano), a single-base TrigNet connection to a near-border SA station may be possible; full Network RTK (VRS / iMAX) coverage does not extend over SZ.
- No IGS permanent station on Eswatini territory.
- A joint geoscience mapping programme between Eswatini Geological Survey and South Africa's Council for Geoscience was active 2023–2024, using AI for mineral resource mapping — no GNSS CORS component identified.
- **No commercial network** (HxGN SmartNet ZA, TPG ZA, Trimble VRS Now, GEODNET, ONOCOY, Centipede-RTK) has confirmed Eswatini coverage. Most SA-resident commercial casters do extend service across the border on a single-base basis but require contractual coverage outside SA.

## Most Recent Project Announcement

**Geological mapping with Council for Geoscience (South Africa) — 2023-12 to 2024**
Phase II of joint geoscience / AI-based critical mineral mapping; no CORS component.
Source: https://www.esi-africa.com/research-and-development/eswatini-mapping-project-searching-for-mineral-and-energy-opportunities/

**Ministry of Natural Resources & Energy 2024/25 Annual Budget Performance Report** (parliament.gov.sz) — Deeds Registry produced 110 deeds in the period to December 2024; no CORS/GNSS infrastructure spend line identified.

## Post-Processing (RINEX) Fallback

None available for Eswatini directly. Nearest options:
- South Africa TrigNet RINEX (free with registration): http://www.trignet.co.za/ — nearest stations on the SA side of border, ~10–30 km baseline
- African Geodetic Reference Frame (AFREF) archive — very sparse in this region; no Eswatini station yet contributes
- IGS HARB (Hartebeesthoek, ZA) — ~360 km west, suitable for PPP / PPK

## Sources Consulted
- Surveyor General's Department — Eswatini Government: https://www.gov.sz/index.php/ministries-departments/ministry-of-natural-resources/surveyor-general (404 on direct fetch, but listed in the ministry tree)
- Surveyor General page (alternate route): https://www.gov.sz/index.php/departments-sp-623334762/surveyor-general
- Ministry of Natural Resources and Energy — About Us: https://www.gov.sz/index.php/ministries-departments/ministry-of-natural-resources
- Deeds Registry: https://www.gov.sz/index.php/ministries-departments/ministry-of-natural-resources/deeds
- Ministry of Natural Resources and Energy 2024/25 Annual Budget Performance Report (PDF): https://parliament.gov.sz/publications/parliament_reports/docs/ANNUAL%20REPORT%20NATURAL%202025.pdf
- WebSearch "Eswatini CORS geodesy GNSS RTK 2024 2025 2026" (2026-05-13) — no CORS services found
- TrigNet South Africa: https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network
- Eswatini geological mapping project: https://www.esi-africa.com/research-and-development/eswatini-mapping-project-searching-for-mineral-and-energy-opportunities/
- `data/stations.json` cross-check (`py scripts/stations_by_radius.py -26.3 31.5 200`) — `mabuda_farm` (rtk2go, country tag SWZ) at 47.7 km, `LouwNPP` (rtk2go, ZAF) at 130.1 km
