# Netherlands [NL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (re-verified; no material change since 2026-05-01)

## Status: YES — free public NTRIP caster (AGRS.NL + AGRS.BES) and paid professional raw-stream tier (NETPOS); no public VRS product

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | NSGI (Nationaal Samenwerkingsverband voor de Geo-informatie-infrastructuur) / Kadaster |
| **host:port — free tier** | `ntrip.kadaster.nl:2101` (plain TCP) · `ntrip.kadaster.nl:443` (TLS) |
| **host:port — paid tier** | `ntrip.cloud.kadaster.nl:443` (TLS only; credentials required) |
| **host:port — TU Delft mirror** | `gnss1.tudelft.nl:2101` (independent relay, same anonymous access, confirmed 2026-05-01) |
| **VRS** | No public VRS product. NETPOS VRS is used internally by Kadaster/Rijkswaterstaat only |
| **tariff — free tier (AGRS.NL + AGRS.BES)** | €0.00 — no registration required; anonymous access (email as username recommended for outage notices, not mandatory). Legal basis: Tarievenregeling Kadaster BWBR0037196 art. 19 lid 4 |
| **tariff — paid tier (NETPOS raw streams, NL mainland only)** | €475 / station / year (1–5 stations) · €380 (6–10) · €285 (11–15) · €190 (16–20) · €95 (21+). VAT-exempt ("vrij van btw", confirmed NSGI FAQ). USD equiv. at 1 EUR = 1.133 (2026-05-01): $538 / $430 / $323 / $215 / $108 per station/year. Rate history: €445/356/267/178/89 at launch 1 Jul 2024 (Stcrt-2024-19381) → €460/368/276/184/92 (2025) → €475/380/285/190/95 (2026-01-01, BWBR0037196/2026-01-01) |
| **hobbyist_eligibility — free tier** | Yes — no registration, no licence check, fully anonymous |
| **hobbyist_eligibility — paid tier** | Unclear / conditionally yes — registration form requires eHerkenning (Dutch business identity); however NSGI states individuals and foreign users may apply via contact form (not blocked, just redirected to manual route) |
| **legal_residency_required** | No — free tier globally accessible with no credentials; paid tier explicitly accommodates foreign users via contact form |
| **last_confirmed_alive** | 2026-05-01 (sourcetable fetched live; wire-protocol curl confirmed N;N auth/fee on all 49 streams) |

## Mountpoints (sample)

**AGRS.NL (mainland, ~30 stations):** APEL00NLD0, CBW100NLD0, WSRA00NLD0, WSRT00NLD0 and others. Format: RTCM 3.2 MSM; legacy RTCM 3.1 GPS/GLONASS-only mountpoints also available for some stations.

**AGRS.BES (BES islands — Bonaire, Saba, Sint Eustatius — 7 streams, free):** BON200BES0, BONK00BES0, SABY0, SABY00BES0, SABY00BES1, SEUS0, SEUS00BES0.

## Context Notes

- The free AGRS.NL service provides raw RTCM observations from individual physical reference stations (single-base corrections), not computed network-RTK / VRS corrections. Suitable for RTK with a known baseline to the nearest reference station.
- The paid NETPOS tier also provides raw reference station streams (not VRS). NETPOS VRS computed corrections are internal to Kadaster/Rijkswaterstaat and are not sold at any public price point.
- BES island streams (AGRS.BES) are part of the free tier and are covered in detail in the Dutch Caribbean entry (BQ).
- No public NTRIP caster exists for the autonomous countries Curaçao (CW), Aruba (AW), or Sint Maarten (SX); see `CW_Dutch_Caribbean.md`.

## Volunteer Coverage

Substantial volunteer coverage exists alongside the official services:
- **Centipede**: 26 NLD-tagged stations (Belgian/Dutch border area, Friesland, Twente, etc.); dense coverage of southern/eastern NL, sparse north of Amsterdam.
- **rtk2go**: 22 NLD-tagged stations spread across the country (Limburg, Brabant, Friesland, Drenthe, Groningen). Free with no auth, but per-station coverage radius ≈30 km and quality varies.
Combined: a hobbyist anywhere on the Dutch mainland has free real-time RTK options at multiple tiers (AGRS.NL official + Centipede + rtk2go + TU Delft mirror).

## Sources Consulted
- NSGI real-time streams page: https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams (observed 2026-05-12)
- Tarievenregeling Kadaster BWBR0037196/2026-01-01: https://wetten.overheid.nl/BWBR0037196/2026-01-01
- Staatscourant 2024-19381 (NETPOS launch tariff): https://www.officielebekendmakingen.nl/stcrt-2024-19381
- Live sourcetable: https://ntrip.kadaster.nl/streamtable (fetched 2026-05-01; re-confirmed 2026-05-12 via search)
- TU Delft DPGA GNSS mirror: gnss1.tudelft.nl:2101 (confirmed 2026-05-01)
- NSGI FAQ on BTW / foreign users (observed 2026-05-01)
- Local data: `py scripts/stations_by_country.py NLD` — 22 rtk2go + 26 Centipede NLD stations (snapshot 2026-05-12)
