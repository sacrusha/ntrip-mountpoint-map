# Croatia [HR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (updated 2026-05-12: live sourcetable captured at `195.29.198.194:2101`; EUR pricing confirmed under Regulation NN 56/2023 + NN 106/2025)

## Status: YES — national government NTRIP RTK caster operating (CROPOS); registration required; real-time RTK (VPPS / DPS) free since April 2022

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | CROPOS (CROatian POsitioning System) |
| **Operator** | Državna geodetska uprava (DGU) — State Geodetic Administration of Croatia |
| **landing_url** | https://www.cropos.hr/ (operator-owned) |
| **access_url** | https://www.cropos.hr/o-sustavu/naknade-za-koristenje-podataka-cropos-sustava (fees + registration procedure; no self-service signup form — registration is by email to cropos@dgu.hr) |
| **host:port** | `195.29.198.194:2101` (live `SOURCETABLE 200 OK` from `NTRIP Trimble Ntrip Caster 5.2` confirmed 2026-05-12; alt portal `gnss.cropos.hr:2101` also returns same sourcetable) |
| **num_stations** | ~35 physical CORS (per DGU CROPOS overview after Feb-2023 + Apr-2025 densification; not enumerated as STR rows since caster exposes only network VRS streams) |
| **vrs** | yes — VPPS (Network RTK / VRS) confirmed; ≤2 cm horizontal, ≤4 cm vertical |
| **datum_epoch** | omitted — no citable operator declaration of frame+epoch on cropos.hr or DGU pages. HTRS96 (Croatian Terrestrial Reference System 1996) ≡ ETRS89 is the network's national frame per geodetic literature, and `CROPOS_VRS_HTRS96` / `CROPOS_VRS_GGG_HTRS96` mountpoints are exposed, but no operator URL declares epoch. |
| **VRS** | Yes — High-Precision Positioning Service (VPPS) provides Network RTK / VRS corrections; ≤2 cm horizontal, ≤4 cm vertical |
| **tariff — DPS (Differential Positioning Service)** | Free (no charge since April 2022 law amendment; ~0.5 m accuracy) |
| **tariff — VPPS (Network RTK / VRS)** | Free (no charge since April 2022 law amendment; ≤2 cm accuracy) — confirmed free in 2026 per CROPOS pricing page; only registration + GPPS now have a fee |
| **tariff — GPPS (Geodetic Precision Positioning Service)** | 0,06 EUR / minute (post-processing data, per current Regulation NN 56/2023, NN 106/25; observed 2026-05-12 on cropos.hr `naknade-za-koristenje-podataka-cropos-sustava`) |
| **tariff — registration fee** | 40,00 EUR one-time per registration request (per Regulation NN 56/2023, NN 106/25; observed 2026-05-12) |
| **tariff — archived data** | 0,06 EUR/min retrieval + 30,00 EUR/hour preparation fee |
| **VAT** | Croatian standard VAT 25% — prices on the regulation page are stated in EUR; VAT treatment per Croatian tax rules |
| **hobbyist_eligibility** | Yes — registration open to individuals; no professional licence requirement stated; one-time 40 EUR registration covers free RTK services |
| **legal_residency_required** | Unclear — registration is via email to cropos@dgu.hr or postal/fax to DGU Zagreb; no explicit residency restriction found |
| **last_confirmed_alive** | 2026-05-12 — `195.29.198.194:2101` returned `SOURCETABLE 200 OK Server: NTRIP Trimble Ntrip Caster 5.2`, 15 STR rows enumerated (see catalogue below); `gnss.cropos.hr:2101` returned identical sourcetable |

## Mountpoint Catalogue — CROPOS (sourcetable 2026-05-12)

`SOURCETABLE 200 OK` from `NTRIP Trimble Ntrip Caster 5.2` listed 15 STR rows — all are network VRS streams (no per-station single-base mounts exposed). The published coordinates are zeroed (`HRV;0;0`) per Trimble Pivot convention:

| Mount | Format | Constellations |
|---|---|---|
| `CROPOS_VRS_RTCM31` | RTCM 3.1 | GPS+GLO |
| `CROPOS_VRS_DGNSS` | RTCM 2.3 | GPS+GLO (DPS / sub-metre) |
| `CROPOS_VRS_HTRS96` | RTCM 3.1 | GPS+GLO (native HTRS96 ETRF) |
| `CROPOS_VRS_HDKS` | RTCM 3.1 | GPS+GLO (Croatian datum) |
| `CROPOS_VRS_HDKS_NE` | RTCM 3.1 | GPS+GLO (HDKS NE zone) |
| `CROPOS_VRS_HDKS_NW` | RTCM 3.1 | GPS+GLO (HDKS NW zone) |
| `CROPOS_VRS_CMRx` | RTCM 3.1 | GPS+GLO (CMRx framing) |
| `CROPOS_VRS_GGG_CMRx` | CMRx | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_DGNSS` | RTCM 2.4 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_HDKS` | RTCM 3.2 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_HDKS_NE` | RTCM 3.2 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_HDKS_NW` | RTCM 3.2 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_HTRS96` | RTCM 3.2 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_RTCM32` | RTCM 3.2 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_RTCM23` | RTCM 2.3 | GPS+GLO |

The `_GGG_` prefix denotes the full-GNSS quad-constellation network solution; non-`GGG_` streams remain GPS+GLO only.

## Context Notes

- **CROPOS overview**: Croatia's national CORS network operated by the State Geodetic Administration (DGU). ~35 reference stations following the February 2023 expansion (5 new stations added in Split, Zagreb, Jastrebarsko, Glina, Pazin; further densification through 2025) covering the entire territory including islands. Launched 2008; part of the EUPOS network.
- **Free RTK since 2022**: The Law on Amendments to the Law on State Survey and Real Estate Cadastre (NN 39/2022, effective 7 April 2022) abolished charges for the DPS and VPPS real-time services. The VPPS (Network RTK / VRS) service — the main RTK product — is now free of charge for all registered users. Only registration and the GPPS high-accuracy post-processing service remain charged.
- **EUR pricing schedule (NN 56/2023, NN 106/25)**: Current regulation on costs and conditions of use for CROPOS data establishes GPPS at 0,06 EUR/min and a one-time registration fee of 40,00 EUR. Cited regulation references on the cropos.hr fees page on 2026-05-12 confirm euro pricing; the kuna-era figures previously documented (0,5 HRK/min, 300 HRK) are superseded.
- **2023 / 2025 expansions**: DGU added five new reference stations (Split, Zagreb, Jastrebarsko, Glina, Pazin) in February 2023, then two further stations in early April 2025 as part of ongoing densification activities.
- **Reference system**: HTRS96 (Croatian Terrestrial Reference System 1996), the Croatian realization of ETRS89. Sourcetable also exposes HDKS (Hrvatski Državni Koordinatni Sustav — legacy Croatian state grid) streams for legacy applications.
- **Access procedure**: Submit registration request to `cropos@dgu.hr` or by post to Državna geodetska uprava, Gruška ulica 20, 10 000 Zagreb, or by fax +385 (0)1 6165 430. Pay the 40 EUR registration fee; credentials issued after approval.
- **Portal**: `gnss.cropos.hr` provides a web-based GNSS processing portal and station status monitoring (Trimble Pivot Platform; the caster identifies as Trimble Ntrip Caster 5.2 in its banner).

## Volunteer Coverage

- **rtk2go (HRV in stations.json fetch 2026-05-12)**: 2 community bases — `Tiho1234` (46.05 N, 16.44 E) and `VargaRTKhr` (46.44 N, 16.50 E), both in northern Croatia near the Slovenian/Hungarian border. Effective free supplement only for that corner; rest of Croatia is fully covered by free CROPOS VPPS in any case.
- **Centipede-RTK**: No HRV nodes in the data/stations.json fetch 2026-05-12 (closest are HUN clusters across the border).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **CROPOS RINEX download (GPPS)** | https://gnss.cropos.hr/ (login required) | 0,06 EUR/min (current regulation NN 56/2023, NN 106/25); archived data 0,06 EUR/min + 30 EUR/h preparation |
| **EUREF / EPN** — Croatian EPN stations (DUBR, OSIJ, PORE, RIJE, ZADA, etc.) | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- CROPOS main site: https://www.cropos.hr/
- CROPOS fees page (EUR pricing under NN 56/2023, NN 106/25, observed 2026-05-12): https://www.cropos.hr/o-sustavu/naknade-za-koristenje-podataka-cropos-sustava
- CROPOS VPPS service: https://www.cropos.hr/servisi/vpps
- CROPOS DPS service: https://www.cropos.hr/servisi/dps
- DGU new CROPOS services announcement (IP 195.29.198.194:2101): https://dgu.gov.hr/vijesti/nove-usluge-sustava-cropos/5224
- CROPOS GNSS web portal: https://gnss.cropos.hr/
- Live caster sourcetable: `curl http://195.29.198.194:2101/` and `http://gnss.cropos.hr:2101/` → `SOURCETABLE 200 OK Server: NTRIP Trimble Ntrip Caster 5.2` (15 STR rows, 2026-05-12)
- HKOIG law amendment note: https://www.hkoig.hr/novo-dodano/vijesti-iz-struke/uvjeti-koristenja-cropos-sustava-vezano-za-donesene-izmjene-zakona-o-drzavnoj-izmjeri-i-katastru-nekretnina
- corsstations.com CROPOS profile: https://corsstations.com/networks/croatia-cors-network-cropos-gnss-rtk-service/
- ArduSimple Croatia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-croatia/
