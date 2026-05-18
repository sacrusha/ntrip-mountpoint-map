# Sweden [SE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-13)

## Status: YES — paid government NTRIP caster (SWEPOS Network RTK, Lantmäteriet) operating; no free hobbyist tier

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (SWEPOS Network RTK — paid) |
| **host:port — SWEPOS** | `nrtk-swepos.lm.se:80` or `nrtk-swepos.lm.se:8500` (IP: 192.71.188.212) |
| **VRS** | Yes — VRS product with RTCM message 1005 (position) + 1007 (antenna); network corrections from 480 reference stations |
| **tariff — Annual (unlimited)** | 12,000 SEK /subscription/yr (1–3 subscriptions); volume discount for 4+ · (source: Lantmäteriet abonnemangsformer page, re-checked 2026-05-13) |
| **tariff — 90-day** | 5,000 SEK /subscription |
| **tariff — 30-day** | 2,000 SEK /subscription |
| **tariff — Network RTK Pot (1,000 min)** | 5,000 SEK /pot; valid max 12 months from start; unused minutes carry forward on renewal |
| **tariff — Nordic extension (Finland)** | 7,000 SEK /yr (add-on to existing Swedish subscription) |
| **tariff — Nordic extension (Norway)** | 5,000 SEK /yr (add-on; uses same credentials as CPOS) |
| **tariff — Trial** | Free 10-day trial for new customers |
| **VAT** | ? — not specified on operator subscription page; no operator citation found. Inclusive/exclusive status unknown — confirm with Lantmäteriet before relying on listed SEK figures. |
| **hobbyist_eligibility** | unclear — no explicit individual/hobbyist tier or restriction; 1,000-minute pot (~17 hours) at SEK 5,000 is the most practical entry point for occasional users |
| **legal_residency_required** | no explicit residency requirement stated; international access not restricted in documentation |
| **last_confirmed_alive** | `nrtk-swepos.lm.se:80` `SOURCETABLE 200 OK` 2026-05-13 (TCP probe; 7 STR: MSM_GNSS, MSM_GEC, MSM_GRE, RTCM3_GNSS, RTCM3_GPS, RTCM2_GPS, DGNSS); price page re-fetched 2026-05-17 — "12000 kr per abonnemang/år" unchanged for 1–3 subscriptions |
| **datum / epoch** | SWEREF 99 — operator declaration at https://www.lantmateriet.se/sv/geodata/gps-geodesi-och-swepos/referenssystem/tredimensionella-system/sweref-99/ : "SWEREF 99 är en realisering av det europeiska systemet ETRS89", plate-tectonic epoch 1989.0, internal epoch 1999.5 (ITRF97 epoch 1999.5 transformed back to ETRS89 per EUREF spec). |

## Mountpoints Available

| Mountpoint | Format | Satellites |
|---|---|---|
| MSM_GNSS | RTCM 3.4 MSM4 | GPS, GLONASS, Galileo, BeiDou |
| MSM_GEC | RTCM 3.4 MSM4 | GPS, Galileo, BeiDou |
| MSM_GRE | RTCM 3.4 MSM4 | GPS, GLONASS, Galileo |
| RTCM3_GNSS | RTCM 3.1 | GPS + GLONASS L1+L2 |
| RTCM3_GPS | RTCM 3.1 | GPS L1+L2 |
| RTCM2_GPS | RTCM 2.3 | GPS L1+L2 |

(The caster sourcetable also exposes one DGNSS mountpoint — pseudorange, out-of-scope per project primer; see Context Notes.)

## Context Notes

- **SWEPOS**: Operated by Lantmäteriet (Swedish National Land Survey). ~480 reference stations nationwide; one of Europe's densest CORS networks. Continuous 24/7 operation. Reference system: SWEREF 99 (= ETRS89-compatible).
- **Accuracy**: Centimetre-level horizontal positioning under good GNSS conditions.
- **DGNSS sub-service (out-of-scope)**: The sourcetable carries one Network-DGNSS stream (RTCM 2.3, ~0.2 m horizontal). Excluded from the main mountpoint table per project primer [scope] (DGNSS-only = out); noted here for completeness only.
- **IoT / M2M**: Annual subscriptions include an IoT/M2M SIM card option (not included in shorter plans); separate mobile data arrangement required for the receiver.
- **No free public tier**: Hobbyists face SEK 12,000/yr (~€1,050/yr at current exchange) for full annual access, or SEK 5,000 for a 1,000-minute pot or 90-day subscription. Annual cost is high relative to the ~$200/yr hobbyist benchmark. The 10-day free trial is useful for evaluation.
- **Free fallbacks (verified 2026-05-17)**: `py scripts/stations_by_country.py SWE` → 54 stations across 5 sources. **IGS-IP (BKG)**: 8 SE streams — KIR0 (Kiruna 67.88°N — fills Norrland gap!), MAR6/MAR7 (Mårtsbo), ONS100/ONSA00 (Onsala), SPT0/SPT7 (Sätila), VIS0 (Visby). **EUREF-IP**: 13 SE streams (same + SKE000 Skellefteå, SUN6 Sundsvall). **AUSCORS rebroadcast**: 4 SE (KIR800, MAR6/MAR7, ONS100). **rtk2go**: 28 volunteer bases, mostly south of ~60°N (north-most OVIK 63.31°N, Solbacka 62.5°N). **Centipede**: 1 SE node (VISBY, Gotland). Key insight: IGS-IP / EUREF-IP / AUSCORS cover Norrland gap (KIR0 Kiruna, SKE0 Skellefteå) where rtk2go has no nodes — these are free with BKG / AUSCORS registration, single-base only, raw 1 Hz RTCM.
- **Price trend note**: Search results reference SEK 12,000/yr for 1–3 subscriptions (Lantmäteriet official page) and SEK 15,000/yr (older commercial re-seller listing); the official Lantmäteriet figure of 12,000 SEK is used here.
- **Operator contact**: swepos@lm.se / +46 (0)26 633753; Monday–Friday 07:00–17:00

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SWEPOS online GNSS post-processing** — automated PPP/PPK service | https://www.lantmateriet.se/sv/geodata/gps-geodesi-och-swepos/swepos/swepos-tjanster/efterberakning/ | Free (included with subscription or separately) |
| **EUREF Permanent Network** — selected Swedish stations | https://epncb.oma.be/ | Free |

## Sources Consulted
- SWEPOS Lantmäteriet overview: https://www.lantmateriet.se/en/geodata/gps-geodesy-and-swepos/swepos/
- SWEPOS Network RTK product: https://www.lantmateriet.se/en/geodata/our-products/product-list/swepos-network-rtk/
- SWEPOS subscription types (Swedish): https://www.lantmateriet.se/sv/geodata/gps-geodesi-och-swepos/swepos/swepos-tjanster/natverks-rtk/abonnemangsformer/
- SWEPOS connection information (host:port and mountpoints): https://www.lantmateriet.se/sv/geodata/gps-geodesi-och-swepos/swepos/swepos-tjanster/natverks-rtk/uppkopplingsinformation/
- Swedron SWEPOS subscription listing: https://swedron.se/produkt/8403018056020/swepos-ntrip-abonnemang
- ArduSimple Sweden RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-sweden/
- TCP probe of `nrtk-swepos.lm.se:80` — SOURCETABLE 200 OK confirmed 2026-05-13; 7 mountpoints visible
