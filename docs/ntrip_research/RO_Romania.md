# Romania [RO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (prior version: 2026-05-06)

## Status: YES — paid government NTRIP caster (ROMPOS, ANCPI) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (ROMPOS — paid) |
| **host:port — ROMPOS** | `rtk.rompos.ro:2101` (network RTK and nearest-station products) · `rtk.rompos.ro:2105` (single-base product) · IP: 94.177.36.200 |
| **VRS** | Yes — `RO_VRS_3.1` mountpoint (RTCM 3.1, GPS+GLONASS); network RTK solution available |
| **tariff** | 100 RON /month/device or 1,000 RON /year/device (VAT included) · GNSS recordings from reference stations: 15 RON/hour (VAT included) · (source: ANCPI Order 16/2019 tariff table, confirmed via epay.ancpi.ro 2026-05-06) |
| **hobbyist_eligibility** | yes — any user may create an ANCPI account and register a rover; no professional licensing stated |
| **legal_residency_required** | unclear — not explicitly required; payment via Romanian bank transfer or epay.ancpi.ro e-payment portal |
| **last_confirmed_alive** | `rtk.rompos.ro:2101` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl verified) |

## Context Notes

- **ROMPOS** (ROmanian MOnitoring and POsitioning System): Operated by ANCPI (Agenția Națională de Cadastru și Publicitate Imobiliară / National Agency for Cadastre and Land Registration). 86 CORS reference stations in ETRS89; covers all Romanian territory.
- **Reference system**: ETRS89 (European Terrestrial Reference System 1989).
- **Constellations**: GPS, GLONASS, Galileo processed.
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
- Wikipedia ROMPOS: https://ro.wikipedia.org/wiki/ROMPOS
- ArduSimple Romania RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-romania/
- curl probe of `rtk.rompos.ro:2101` — SOURCETABLE 200 OK confirmed 2026-05-06
- 2026-05-12 re-check: ANCPI epay portal still lists 100 RON / month for ROMPOS RTK (prodId=312100). VAT inclusion not explicitly stated on the epay product page itself; the ROMPOS Romanian-language "modalitati-de-plata" page describes the tariff schedule under ANCPI Order 16/2019 where TVA is included.
- Local: `py scripts/stations_by_country.py ROM` → 7 Centipede ROM stations (2026-05-12); `py scripts/stations_by_country.py ROU` → 2 Centipede ROU stations (ROMS1, ROMS2) + 6 rtk2go ROU bases (2026-05-13). **Centipede uses both ROM (non-ISO) and ROU (ISO) for Romania in parallel; both must be summed = 9 Centipede Romania stations.** See `_centipede_country_codes.md`.
