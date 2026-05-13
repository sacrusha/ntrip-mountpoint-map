# Dutch Caribbean [CW / AW / BQ / SX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Summary

| Territory | ISO2 | Caster found? | Free RTK stream? | Status |
|---|---|---|---|---|
| Curaçao | CW | **Partial** | **Yes** (rtk2go) | 3 volunteer rtk2go bases operated by JAJO group's Mijnmaatschappij Curaçao around Willemstad; 1 EarthScope NOTA RTK stream (CN40, Willemstad); no national caster |
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
| **last_confirmed_alive** | 2026-05-12 — direct sourcetable fetch from `http://ntrip.kadaster.nl:2101/` returned the AGRS.BES streams (BON200BES0, BONK00BES0, SABY0, SABY00BES0, SABY00BES1, SEUS0, SEUS00BES0). Confirmed BES mountpoints unchanged from 2026-05-01 snapshot |

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

## [CW] Curaçao — JAJO / Mijnmaatschappij Curaçao (rtk2go) + EarthScope CN40

**Important update vs. 2026-05-06 snapshot:** Three private volunteer base stations operated by **Mijnmaatschappij Curaçao** (Mining Company Curaçao, a JAJO group subsidiary headquartered at the Curaçao limestone quarry) are now visible in the project's rtk2go archive, all around the Willemstad area. EarthScope NOTA also publishes the **CN40** Trimble NetR9 reference stream from Curaçao. The Kadaster Curaçao registry itself still operates no national caster.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (national)** | No |
| **Active third-party RTK streams** | Yes — 3 rtk2go bases (`CWM_JAJO_RTK_RTCM3_X` 12.12°N/-68.91°W Willemstad, `MPA_JAJO_RTK_RTCM3_W` 12.17°N/-68.98°W Gato/Willemstad, `UTE_JAJO_RTK_RTCM3_X` 12.15°N/-68.91°W Willemstad) and 1 EarthScope `CN40_RTCM3P3` (12.18°N/-68.96°W Willemstad) |
| **host:port (rtk2go)** | `rtk2go.com:2101` — anonymous public access; user-agent + arbitrary username accepted |
| **host:port (EarthScope)** | `gnss.earthscope.org:2101` — requires free Earthscope NULA + GNSS data agreement; CN40 mountpoint is the Willemstad/Curaçao stream |
| **VRS** | No — physical single-station streams |
| **tariff** | Free — rtk2go and EarthScope both free at no cost for non-commercial use |
| **hobbyist_eligibility** | Yes — rtk2go fully anonymous; EarthScope requires free GNSS data agreement signup |
| **legal_residency_required** | No |
| **last_confirmed_alive — JAJO rtk2go streams** | 2026-05-06 (per `data/rtk2go.sourcetable` snapshot; all 3 streams present) |
| **last_confirmed_alive — EarthScope CN40** | 2026-05-06 (per `data/earthscope.sourcetable` snapshot) |
| **last_confirmed_alive — registry portal** | `kadaster.cw` — 2026-05-01 |

**Operator notes for JAJO mounts**: Mijnmaatschappij Curaçao (Mining Company Curaçao, `miningcompanycuracao.com`) is the calcium-carbonate quarry operator on Curaçao, part of the Dutch JAJO construction group (`jajo.com`). The three rtk2go streams are clustered tightly around their Willemstad operations (within ~8 km of each other) and provide practical RTK for any project on the Willemstad/Curaçao south coast. Coverage of the western tip (Westpunt) or eastern Oostpunt may degrade to 30+ km baseline.

**Kadaster Curaçao** (`kadaster.cw`, HTTPS 200 confirmed 2026-05-01) publishes only a cadastral parcel map viewer; no GNSS or NTRIP section exists. No `CUW`-coded mountpoint appears on the NSGI Kadaster NL casters (`ntrip.kadaster.nl`, `ntrip.cloud.kadaster.nl`) or EUREF-IP. The NSGI FAQ explicitly states geodetic inquiries for Curaçao must be directed to local authorities. Contact: `kadaster.cw`.

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
- **Direct sourcetable fetch (2026-05-12)**: `http://ntrip.kadaster.nl:2101/` returned all 7 AGRS.BES streams (BON200BES0, BONK00BES0, SABY0, SABY00BES0, SABY00BES1, SEUS0, SEUS00BES0) plus the wider AGRS.NL/GNSS.NL Dutch network
- Kadaster Curaçao: https://kadaster.cw (2026-05-01)
- Mining Company Curaçao (JAJO subsidiary): https://miningcompanycuracao.com/ and https://www.jajo.com/en/companies/mining-company-curacao/ (2026-05-12)
- `data/rtk2go.sourcetable` (project pipeline, 2026-05 snapshot) — 3 CUW-coded streams: `CWM_JAJO_RTK_RTCM3_X` (Willemstad), `MPA_JAJO_RTK_RTCM3_W` (Gato/Willemstad), `UTE_JAJO_RTK_RTCM3_X` (Willemstad)
- `data/earthscope.sourcetable` (project pipeline, 2026-05 snapshot) — 1 CUW-coded stream: `CN40_RTCM3P3` (Willemstad)
- NSGI FAQ on territory scope (2026-05-01)
- `gov.aw` and DC-ANSP aeronautical publications (DLV Aruba)
- VROMI / Kadaster Sint Maarten MOU announcement (LinkedIn, early 2026)
