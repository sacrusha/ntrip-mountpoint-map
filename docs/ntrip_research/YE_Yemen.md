# Yemen [YE] — NTRIP RTK Caster Research

## Status
NO — no public NTRIP RTK. Civil conflict since 2015 collapsed geodetic services. No volunteer bases in any ingested global caster.

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

General Survey Authority (هيئة المساحة العامة, GAS) — historically administered geodesy + CORS. Website unreachable across multiple probes 2026-05.

## Context

- Active civil conflict since 2015. Houthi-controlled north-west (Sanaa) vs IRG (Aden) split disrupted all public infrastructure incl. mapping.
- Historic IGS site ADEN (Aden) absent from current IGS operational lists; no real-time stream confirmed.
- No public RINEX archive identified for YE CORS data.
- Commercial alternatives (GEODNET, PointOne, HxGN, Trimble VRS Now): zero YE coverage.
- Prior anecdotal rtk2go entry `s9123A22404` (Sanaa, 15.29N/44.24E, 2024–early 2025): not in current ingested sourcetable.
- Practical hobbyist path: local GNSS base for self-supplied RTK. RTK over NTRIP unavailable.

## Volunteer / Global Coverage

- rtk2go / Centipede / EarthScope NOTA / EUREF-IP / IGS-IP: zero YE.
- `py scripts/stations_by_radius.py 15.36 44.19 200` (Sanaa): zero stations across all ingested sources.
- `py scripts/stations_by_country.py YE` / `YEM`: "No stations".

## Post-Processing (RINEX) Fallback

None identified.

## Sources
- IGS network list (no operational ADEN): https://network.igs.org/
- WebSearch "Yemen GNSS CORS RTK NTRIP 2026" — null (only generic NTRIP technology content)
- WebSearch Arabic "هيئة المساحة Yemen GNSS RTK" — null for YE
