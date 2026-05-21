# Romania [RO] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-12)
**status:** YES — paid government NTRIP (ROMPOS, ANCPI). 100 RON/month or 1,000 RON/year/device — well within hobbyist range (~€200/yr). Strong volunteer mesh: 9 Centipede (across ROM + ROU country codes) + 6 rtk2go bases.

## ROMPOS — ROmanian MOnitoring and POsitioning System

| field | value |
|---|---|
| landing_url | https://rompos.ro/index.php/en/ |
| access_url | https://app.rompos.ro (subscription portal + per-rover NTRIP credential management); buy via https://epay.ancpi.ro |
| operator | ANCPI — Agenția Națională de Cadastru și Publicitate Imobiliară |
| host:port | `rtk.rompos.ro:2101` (IP 94.177.36.200) for network RTK + nearest-station products. `:2105` for single-base products per ROMPOS FAQ — port 2105 documented but not independently confirmed live from sandbox 2026-05-21 (only :2101 probed). Live `SOURCETABLE 200 OK` on `:2101` from `Leica GNSS Spider 7.11.1.109/1.0`, 13 STR rows, 1356 bytes, 2026-05-21. |
| vrs | yes — `RO_VRS_3.1`, `RO_VRS_MSM5` (GPS+GLO+GAL+BDS), `RO_MAX_3.1`, `RO_iMAX_3.1`, `i-MAX_MSM5`, `RO_FKP_3.1`, plus `Nearest_3.1 / 2.3 / 4G / CMR+`, `VRS_CMR+`. NRTK (VRS + MAX + iMAX + FKP) all present per :2101 sourcetable 2026-05-21. |
| num_stations | 86 CORS in ETRS89 covering the whole territory (confirmed on rompos.ro homepage WebFetch 2026-05-21: "a network consisting of 86 CORS") |
| tariff | 100 RON/month/device or 1,000 RON/year/device (VAT incl.) per ANCPI Order 16/2019 — re-confirmed on rompos.ro landing 2026-05-21 ("100 lei monthly", "1000 lei yearly") and on `epay.ancpi.ro` prodId=312100. GNSS recordings 15 RON/hour (VAT incl.). |
| VAT | 100/1,000 RON figures are TVA-inclusive (per ANCPI Order 16/2019) |
| hobbyist_eligibility | yes — any user may create an ANCPI account + register a rover; no professional-licence wall |
| legal_residency_required | ? — not explicitly required; payment via Romanian bank transfer or `epay.ancpi.ro` (card) |
| last_confirmed_alive | 2026-05-21 — `rtk.rompos.ro:2101` SOURCETABLE 200 OK, Leica GNSS Spider 7.11.1.109, 13 STR including multi-constellation MSM5 / 4G streams |
| datum_epoch | **ETRS89** — operator-declared on rompos.ro FAQ (`en/f-a-q/rompos-f-a-q`): "Coordinates obtained via ROMPOS are expressed in ETRS89". Epoch not stated. |

## Context

- **Accuracy**: ±3 cm positional accuracy stated for RTK products.
- **Subscription management**: Activate rover subscriptions at `app.rompos.ro`; select activation date and number of months; NTRIP credentials issued per device.
- **Payment**:
  - Online via `epay.ancpi.ro` (card)
  - Bank transfer to National Cartography Center (Bucharest), IBAN RO57TREZ701501503X017556; upload receipt in the "Înregistrare OP" section at `app.rompos.ro`; activation within 1 business day
- **Reference system**: ETRS89 (Stereographic 1970 transform via free TransDatRo). For cadastre Stereographic 1970 is required.
- **Constellations**: GPS+GLO on RTCM3.1 streams; GPS+GLO+GAL+BDS on MSM5/4G streams (`RO_VRS_MSM5`, `Nearest_4G`, `i-MAX_MSM5`).
- **Private commercial alternative**: RTK Premium (`rtkpremium.ro`) — PRS-type network (Pseudo Reference Station), claims "2000+ base stations all over the continent" (global/European network, Romania-specific station count not disclosed), 30-day free trial. Pricing not publicly listed (requires contact); no sourcetable found. Not a Romania-specific NRTK caster and offers no better price transparency than ROMPOS, so not researched further. Sources: https://www.rtkpremium.ro/en/services/ (WebFetch 2026-05-21).

## Volunteer mesh (2026-05-21)

- **Centipede**: 9 Romanian stations across two parallel country codes used by the Centipede caster (non-ISO legacy code `ROM` for 7 stations, ISO `ROU` for 2):
  - `ROM` (7): `MAVERICK`, `MRTN`, `ROBU1`, `ROCL1`, `SIAG`, `VASLUI`, `ZSZ1`
  - `ROU` (2): `ROMS1`, `ROMS2`
  - Verified in `data/centipede.sourcetable` 2026-05-21. Total = 9.
- **rtk2go**: 6 ROU bases (including `ROMS2` rebroadcast).
- **EUREF** + **IGS-IP**: `BUCU` station, Bucharest.
- **AUSCORS**: 1 BUCU mirror.

Total ~16 free Romanian bases plus EUREF/IGS academic streams.

## Post-processing fallback

| Service | URL | Cost |
|---|---|---|
| ROMPOS RINEX download — raw data from 86 CORS | https://app.rompos.ro | 15 RON/hour (VAT incl.) |
| EUREF Permanent Network — selected Romanian stations | https://epncb.oma.be/ | free |

## Sources

- ROMPOS homepage: https://rompos.ro/index.php/en/ (WebFetch 2026-05-21 — 100/1,000 RON confirmed)
- ROMPOS FAQ (host/port + ETRS89 declaration): https://rompos.ro/index.php/en/f-a-q/rompos-f-a-q
- ROMPOS communications/NTRIP page: https://rompos.ro/index.php/informatii-tehnice/comunicatii
- ROMPOS payment/tariff page: https://rompos.ro/index.php/acasa/modalitati-de-plata
- ANCPI e-payment portal (prodId=312100): https://epay.ancpi.ro/epay/SelectProd.action?prodId=312100
- ArduSimple RO: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-romania/
- Live caster: `curl --http0.9 http://rtk.rompos.ro:2101/` SOURCETABLE 200 OK, Leica GNSS Spider 7.11.1.109, 13 STR (2026-05-21)
- Local: `data/centipede.sourcetable` 2026-05-21 (7 ROM + 2 ROU); `data/rtk2go.sourcetable` 2026-05-21 (6 ROU); `py scripts/stations_by_country.py ROU` → centipede 9 + rtk2go 6 + EUREF 1 + IGS 1 + AUSCORS 1
