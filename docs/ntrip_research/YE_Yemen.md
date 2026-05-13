# Yemen [YE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (re-verification of 2026-05-06 baseline)

## Status: NO — no public NTRIP RTK infrastructure; civil conflict since 2015 has effectively halted geodetic services; no volunteer bases in rtk2go / centipede / earthscope as of 2026-05-13

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Operator** | General Survey Authority (GAS / هيئة المساحة العامة) — pre-conflict administered geodesy and CORS; GAS website unreachable as of 2026-05-06 |
| **host:port** | Unknown / not public; no NTRIP endpoint identified |
| **VRS** | — |
| **tariff** | — |
| **hobbyist_eligibility** | — |
| **legal_residency_required** | — |
| **last_confirmed_alive** | Unknown — no reachable GAS or geodetic portal found 2026-05-13; stations_by_radius.py 15.36 44.19 200 (Sanaa) returns zero stations across all tracked sourcetables |
| **Most recent project announcement** | None found |

## Volunteer Coverage

- **rtk2go**: No YE-coordinate entries found in rtk2go sourcetable as of 2026-05-06 (curl probe of rtk2go.com:2101; coordinates scan for lat 12°–18°N / lon 42°–50°E returned zero results). A previous entry (mountpoint `s9123A22404`, near Sanaa, 15.29°N/44.24°E, RTCM 3.2, GPS+BDS) has not been confirmed in the current sourcetable.
- **Centipede**: No YE entries.

## Context Notes

- Yemen has been in active civil conflict since 2015. Hostilities between Houthi forces (controlling Sanaa and the north-west) and the internationally recognised government (based in Aden) have severely disrupted all public infrastructure, including geodetic and mapping services.
- The General Survey Authority (GAS), which historically operated geodetic reference stations, has had its website unreachable in all searches conducted 2026-05-06. No active CORS network, NTRIP caster, or public RINEX service was identified.
- WebSearch queries in English ("Yemen NTRIP RTK CORS GNSS General Survey Authority") and Arabic ("هيئة المساحة Yemen GNSS RTK") returned no relevant results referencing any active positioning infrastructure.
- No IGS station confirmed actively streaming in Yemen as of research date; historic IGS site ADEN (Aden) has not appeared in current IGS operational lists.
- No public RINEX download service identified.
- The conflict has also eliminated practical access to commercial RTK networks (no GEODNET, PointOne, or similar coverage). Galileo HAS (~40 cm, no internet) is theoretically usable but of limited practical value in a conflict zone with restricted import of GNSS equipment.

## Post-Processing (RINEX) Fallback

None identified. No public RINEX archive for Yemeni CORS data found.

## Sources Consulted
- WebSearch "Yemen NTRIP CORS RTK GNSS General Survey Authority 2025 2026" — no active services found (2026-05-06; re-run 2026-05-13 — still no results pointing at any Yemeni endpoint)
- WebSearch "Yemen General Survey Authority GNSS geodesy CORS RTK 2024 2025" — no results (2026-05-06)
- WebSearch Arabic: "هيئة المساحة Yemen GNSS RTK 2024 2025" — no results for Yemen; returned results for Saudi Arabia and Oman (2026-05-06)
- curl probe of rtk2go.com:2101 — full sourcetable scanned for Yemen coordinates (lat 12–18°N / lon 42–50°E) and country codes; no YE entries found 2026-05-06
- stations_by_radius.py 15.36 44.19 200 (run 2026-05-13) — zero stations within 200 km of Sanaa across rtk2go / centipede / earthscope sourcetables
- country-survey.md YE entry (for context on pre-conflict status)
