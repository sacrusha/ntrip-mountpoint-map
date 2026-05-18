# Yemen [YE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verification of 2026-05-16 baseline)

## Status: NO — no public NTRIP RTK. Civil conflict since 2015 collapsed geodetic services. No volunteer bases in any ingested global caster as of 2026-05-17.

## Caster (none)

| Field | Value |
|---|---|
| landing_url | — |
| access_url | — |
| host:port | — none identified |
| tariff | — |
| num_stations | 0 |
| vrs | — |
| hobbyist_eligibility | — |
| legal_residency_required | — |
| last_confirmed_alive | n/a — no caster found |
| datum_epoch | omitted — no citable declaration |

## Operator (pre-conflict, status unknown)

General Survey Authority (هيئة المساحة العامة, GAS) — historically administered geodesy + CORS. Website unreachable in all searches 2026-05-06 → 2026-05-16.

## Most Recent Project Announcement

None. Repeat WebSearch 2026-05-17 ("Yemen GNSS CORS RTK 2026 General Survey Authority") returned only generic global CORS content (NOAA, Survey of India, AUSCORS); zero YE-specific result. Arabic-query parallel (2026-05-13) returned KSA/Oman results, no YE.

## Volunteer / Global Coverage

- rtk2go: zero YE-tagged mountpoints (ingested sourcetable; primer rule — no online rtk2go probe).
- Centipede: zero YE.
- EarthScope NOTA, EUREF-IP, IGS-IP: zero YE.
- `py scripts/stations_by_radius.py 15.36 44.19 200` (Sanaa, 2026-05-16): zero stations across all ingested sources.
- `py scripts/stations_by_country.py YEM` 2026-05-17: "No stations for 'YEM'".
- Prior anecdotal rtk2go entry `s9123A22404` (Sanaa, 15.29N/44.24E, 2024–early 2025): not in current ingested sourcetable.

## Context

- Active civil conflict since 2015. Houthi-controlled north-west (Sanaa) vs IRG (Aden) split disrupted all public infrastructure incl. mapping.
- Historic IGS site ADEN (Aden) absent from current IGS operational lists; no real-time stream confirmed.
- No public RINEX archive identified for YE CORS data.
- Commercial alternatives (GEODNET, PointOne, HxGN, Trimble VRS Now): zero YE coverage.
- Practical hobbyist path: local GNSS base for self-supplied RTK. RTK over NTRIP unavailable.

## Post-Processing (RINEX) Fallback

None identified.

## Sources
- WebSearch "Yemen NTRIP CORS RTK GNSS General Survey Authority 2025 2026" — null result 2026-05-16
- WebSearch Arabic "هيئة المساحة Yemen GNSS RTK" — null for YE 2026-05-13
- `py scripts/stations_by_radius.py 15.36 44.19 200` 2026-05-16 — zero results across rtk2go / centipede / earthscope / euref_ip / igs_ip
- `py scripts/stations_by_country.py YE` 2026-05-16 — "No stations for 'YE'"
- `py scripts/stations_by_country.py YEM` 2026-05-17 — "No stations for 'YEM'"
- WebSearch "Yemen GNSS CORS RTK 2026 General Survey Authority" 2026-05-17 — null
