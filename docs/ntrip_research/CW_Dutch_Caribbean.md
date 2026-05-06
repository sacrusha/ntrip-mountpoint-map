# Dutch Caribbean [CW / AW / BQ / SX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Summary

| Territory | ISO2 | Caster found? | Free RTK stream? | Status |
|---|---|---|---|---|
| Curaçao | CW | No | — | No public caster |
| Aruba | AW | No | — | No public caster |
| Bonaire / Sint Eustatius / Saba (BES) | BQ | **Yes** | **Yes (free)** | AGRS.BES via Kadaster NL / NSGI |
| Sint Maarten | SX | No | — | No public caster |

---

## [BQ] Bonaire / Sint Eustatius / Saba — AGRS.BES (Kadaster Netherlands / NSGI)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | NSGI / Kadaster Netherlands on behalf of Kadaster BES |
| **host:port** | `ntrip.kadaster.nl:2101` (plain TCP) · `ntrip.cloud.kadaster.nl:443` (TLS) |
| **VRS** | No — single-station raw reference streams only |
| **tariff** | Free / €0. Explicitly listed as free on the NSGI pricing page. Anonymous access — no username/password required (email as username recommended for outage notices, optional). No VAT applies. USD equivalent: $0 |
| **hobbyist_eligibility** | Yes — fully anonymous, no corporate or surveyor registration required |
| **legal_residency_required** | No — open globally |
| **last_confirmed_alive** | 2026-05-01 (both casters; sourcetable fetched directly) |

### Active BES Mountpoints (AGRS.BES network, RTCM 3.3 MSM, country code BES)

| Mountpoint | Station | Island | GNSS systems |
|---|---|---|---|
| BON200BES0 | Bonaire Kadaster (Stonex SC2200) | Bonaire | GPS + GLO + GAL + BDS |
| BONK00BES0 | Bonaire Kadaster (Leica GR30) | Bonaire | GPS + GLO + GAL + BDS |
| SABY0 | Saba (legacy RTCM 3.1) | Saba | GPS + GLO |
| SABY00BES0 | Saba (Septentrio PolRX5E) | Saba | GPS + GLO + GAL + BDS |
| SABY00BES1 | Saba (raw SBF format) | Saba | GPS + GLO + GAL + BDS |
| SEUS0 | Sint Eustatius (legacy RTCM 3.1) | Sint Eustatius | GPS + GLO |
| SEUS00BES0 | Sint Eustatius (Septentrio PolRX5) | Sint Eustatius | GPS + GLO + GAL + BDS |

Source: `https://ntrip.kadaster.nl/streamtable` (2026-05-01); `https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams` (2026-05-01).

---

## [CW] Curaçao — Kadaster en Openbare Registers Curaçao

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null |
| **legal_residency_required** | null |
| **last_confirmed_alive — caster** | null (none found) |
| **last_confirmed_alive — registry portal** | `kadaster.cw` — 2026-05-01 |

The Kadaster Curaçao website (`kadaster.cw`, confirmed reachable 2026-05-01) publishes only a cadastral parcel map viewer; no GNSS or NTRIP section exists. Neither the NSGI casters (`ntrip.kadaster.nl`, `ntrip.cloud.kadaster.nl`) nor EUREF-IP, RTK2go, or any other aggregator carry a mountpoint with country code `CUW` or coordinates consistent with Curaçao. The NSGI FAQ explicitly states geodetic inquiries for Curaçao must be directed to local authorities. Contact: `kadaster.cw`.

---

## [AW] Aruba — Dienst Landmeetkunde en Vastgoedregistratie (DLV)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null |
| **legal_residency_required** | null |
| **last_confirmed_alive — caster** | null (none found) |

DLV (Sabana Blanco 68, Oranjestad; +297 528-8359) has no publicly accessible GNSS correction stream. Neither NSGI's casters nor any other known NTRIP directory carry an Aruba mountpoint. A 2025 LinkedIn post from the acting DLV director references a geospatial imaging project but makes no mention of RTK/NTRIP. DLV falls outside the NSGI mandate (confirmed by NSGI FAQ). `dlv.aw` returns no live result; `gov.aw` contains only civil aviation GNSS references. Contact: DLV +297 528-8359 or Government of Aruba contact portal.

---

## [SX] Sint Maarten — Kadaster Sint Maarten / VROMI

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null |
| **legal_residency_required** | null |
| **last_confirmed_alive — caster** | null (none found) |

No NTRIP caster or `SXM` country-code mountpoint found in AGRS.BES, any other network sourcetable, or any aggregator. An early-2026 announcement confirms VROMI and Kadaster Sint Maarten signed an MOU with Kadaster Netherlands "to enhance cooperation," but this is institutional cooperation only, not evidence of an operational NTRIP service. Sint Maarten governance falls outside NSGI's mandate (confirmed by NSGI FAQ). Contact: Ministry VROMI (Philipsburg, Sint Maarten) or Kadaster Sint Maarten.

## Sources Consulted
- NSGI real-time streams page: https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams (2026-05-01)
- Live sourcetable: https://ntrip.kadaster.nl/streamtable (2026-05-01)
- Kadaster Curaçao: https://kadaster.cw (2026-05-01)
- NSGI FAQ on territory scope (2026-05-01)
- `gov.aw` and DC-ANSP aeronautical publications (DLV Aruba)
- VROMI / Kadaster Sint Maarten MOU announcement (LinkedIn, early 2026)
