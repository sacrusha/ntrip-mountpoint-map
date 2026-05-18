# Romania [RO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-12)

## Status: YES — paid gov NTRIP caster (ROMPOS, ANCPI) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (ROMPOS — paid) |
| **landing_url** | `https://rompos.ro/index.php/en/` |
| **access_url** | `https://app.rompos.ro` (subscription portal + NTRIP creds issued per rover) |
| **host:port — ROMPOS** | `rtk.rompos.ro:2101` (network RTK + nearest-station products) · `rtk.rompos.ro:2105` (single-base) · IP 94.177.36.200 |
| **VRS** | Yes — `RO_VRS_3.1`, `RO_VRS_MSM5` (GPS+GLO+GAL+BDS multi-constellation), `RO_MAX_3.1`, `RO_iMAX_3.1`, `i-MAX_MSM5`, `RO_FKP_3.1`, plus Nearest_3.1, Nearest_2.3, Nearest_4G, Nearest_CMR+, VRS_CMR+. NRTK (VRS+MAX+MAC+iMAX+FKP) all present per :2101 ST 2026-05-17. |
| **tariff** | 100 RON/month/device or 1,000 RON/year/device (VAT incl.) · GNSS recordings: 15 RON/hour (VAT incl.) · source: ANCPI Order 16/2019, confirmed epay.ancpi.ro prodId=312100 2026-05-17 |
| **datum_epoch** | ETRS89 (mainland) — operator-declared on rompos.ro FAQ (en/f-a-q/rompos-f-a-q): "Coordinates obtained via ROMPOS are expressed in ETRS89". Epoch not stated. Citable. |
| **hobbyist_eligibility** | yes — any user may create ANCPI account + register rover; no professional licence stated |
| **legal_residency_required** | unclear — not explicit; payment via Romanian bank transfer or epay.ancpi.ro |
| **last_confirmed_alive** | `rtk.rompos.ro:2101` SOURCETABLE 200 OK 2026-05-17 (Leica GNSS Spider 7.11.1.109; 13 STR records incl. 4G/MSM5 multi-constellation streams). |

## Context Notes

- **ROMPOS** (ROmanian MOnitoring and POsitioning System): Operated by ANCPI (Agenția Națională de Cadastru și Publicitate Imobiliară / National Agency for Cadastre and Land Registration). 86 CORS reference stations in ETRS89; covers all Romanian territory.
- **Reference system**: ETRS89 (Stereographic 1970 transform via free TransDatRo). For cadastre, Stereographic 1970 required.
- **Constellations**: GPS+GLO on RTCM3.1 streams; GPS+GLO+GAL+BDS on MSM5/4G streams (RO_VRS_MSM5, Nearest_4G, i-MAX_MSM5).
- **Accuracy**: ±3 cm positional accuracy stated for RTK products.
- **Subscription management**: Activate rover subscriptions at app.rompos.ro; select activation date and number of months; NTRIP credentials issued per device.
- **Payment**:
  - Online via epay.ancpi.ro (e-payment system)
  - Bank transfer to National Cartography Center (Bucharest), IBAN RO57TREZ701501503X017556; upload receipt in "Înregistrare OP" section at app.rompos.ro; activation within 1 business day
- **Tariff note**: ANCPI Order 16/2019 tariffs have been in force since 4 Feb 2019; as of 2026-05-06 the monthly fee observed at epay.ancpi.ro is 100 RON. VAT (TVA) is included. ~€20/month or ~€200/year at current exchange (approx).
- **Private commercial alternative**: RTK Premium (rtkpremium.ro) offers RTK correction services; pricing not publicly listed.
- **Volunteer presence**: Centipede uses **both** non-ISO `ROM` (7 stations) **and** ISO `ROU` (2 stations: `ROMS1`, `ROMS2`) in parallel for Romania — **total Centipede Romania = 9 stations** (must sum both codes). rtk2go uses `ROU` only (6 bases including `ROMS2`, which is also listed under Centipede). Modest cluster around major cities. See `_centipede_country_codes.md`.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ROMPOS RINEX download** — raw data from 86 CORS | https://app.rompos.ro | 15 RON/hour (VAT included) |
| **EUREF Permanent Network** — selected Romanian stations | https://epncb.oma.be/ | Free |

## Sources Consulted
- ROMPOS homepage: https://rompos.ro/index.php/en/
- ROMPOS FAQ (host/port details): https://rompos.ro/index.php/en/f-a-q/rompos-f-a-q
- ROMPOS communications/NTRIP page: https://rompos.ro/index.php/informatii-tehnice/comunicatii
- ROMPOS payment/tariff page: https://rompos.ro/index.php/acasa/modalitati-de-plata
- ANCPI e-payment portal (100 RON/month observed): https://epay.ancpi.ro/epay/SelectProd.action?prodId=312100
- ArduSimple Romania RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-romania/
- curl probe `rtk.rompos.ro:2101` — SOURCETABLE 200 OK 2026-05-17 (13 STR; multi-constellation streams confirmed)
- Local `scripts/stations_by_country.py` (2026-05-17): ROM → 7 Centipede (MAVERICK, MRTN, ROBU1, ROCL1, SIAG, VASLUI, ZSZ1); ROU → 9 Centipede total via alias (incl. ROMS1, ROMS2) + 6 rtk2go + 1 EUREF-IP (BUCU) + 1 IGS-IP (BUCU) + 1 AUSCORS (BUCU mirror). **Centipede uses ROM (non-ISO) + ROU (ISO) in parallel = 9 Centipede stations.**
