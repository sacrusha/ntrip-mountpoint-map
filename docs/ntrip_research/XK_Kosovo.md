# Kosovo [XK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verification of 2026-05-16 baseline)

## Status: YES — paid national NTRIP (KOPOS), VRS/FKP; hobbyist-eligible; port 2101 still timing out from external IP (geo-firewall hypothesis stable across 2026-05-06/-12/-16/-17). SBC web portal HTTPS reachable.

## Caster: KOPOS / Kosovo Positioning System

| Field | Value |
|---|---|
| landing_url | https://akk.rks-gov.net/en (AKK portal, KOPOS product card) |
| access_url | https://kopos.rks-gov.net/SBC/Account/Register (Leica SBC self-service registration) |
| host:port | `kopos.rks-gov.net:2101` (IP 91.239.145.45) — TCP timeout from external IP 2026-05-06, -12, -16, -17 (geo-firewall hypothesis); SBC portal HTTPS reachable; credentials + MP list issued post-login |
| tariff | **Initial registration:** €20 one-time per user. **RTK annual:** €400/yr. **RTK 6-mo:** €250. **RTK 1-mo:** €60. **RINEX annual:** €100/yr. **RINEX 6-mo:** €70. **RINEX 1-mo:** €30. VAT: Kosovo standard 18%; tariff document does NOT state whether prices inclusive/exclusive — verify at AKK. Source: AKK Administrative Instruction QRK No. 04/2024, Shtojca 1 §1.2.2 (PDF, observed 2026-05-06; pdftotext-extracted). Pricing unchanged through 2025 Annual Report (issued 2026-03-25). |
| num_stations | 8 permanent CORS + computation centre in Pristina (Leica AR25 choke-ring antennas) |
| vrs | yes — RTCM 2.3 FKP + VRS; GPS+GLONASS+Galileo; stated accuracy ±2 cm horiz / ±4 cm vert |
| hobbyist_eligibility | yes — SBC registration form requests rover brand, serial, address only; no surveying-licence requirement found |
| legal_residency_required | ? — not explicitly stated on registration form; no confirmed restriction |
| last_confirmed_alive | 2026-05-17 — TCP probe `kopos.rks-gov.net:2101` timeout (external IP; stable since 2026-05-06); `https://kopos.rks-gov.net/SBC/Account/Index` HTTP 200 (Leica SBC); `https://akk.rks-gov.net/en` HTTP 200 |
| datum_epoch | omitted — no citable declaration. KOSOVAREF01 / ETRS89 widely cited but only on third-party (FIG, ResearchGate, academia.edu, epsg.io). AKK + KOPOS portals do not state datum on accessible pages; not citable per project rule. |

## Operator

AKK — Agjencia Kadastrale e Kosovës (Kosovo Cadastral Agency)
Platform: Leica GNSS Spider / Spider Business Center v7.8.1.438 (login page unchanged 2026-05-16)

## Context

- **Network history:** World-Bank-funded ICB; Leica + KCA contract Sep 2011. Operational ~2012–2013. 8 AR25 choke-ring stations; control centre in Pristina.
- **Tariff:** QRK 04/2024 still current 2026-05-16. €400/yr RTK + €20 registration confirmed against AKK PDF + 2025 Annual Report.
- **Port 2101 geo-firewall:** TCP attempts from external IP timed out 2026-05-06, -12, -16, -17 (15-20s). IP resolves correctly (91.239.145.45). SBC HTTPS portal responsive externally; credentials + MP list distributed via SBC post-login.
- **EUREF/EPN:** Kosovo's non-UN-member status complicated participation; no confirmed EPN station.
- **Volunteer coverage:** zero XK on rtk2go / Centipede (ingested).
- **Economics:** €400/yr expensive vs Kosovo GDP/capita ~€5,500 (2025). No free hobbyist tier. €60/mo lower-commitment option.
- **Protocols:** RTCM 2.3 FKP + VRS documented in older sources; MSM messages not explicitly documented.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| KOPOS RINEX (via SBC) | https://kopos.rks-gov.net/SBC/Account/Index | €100/yr or €70/6mo or €30/mo per user (QRK 04/2024) |

## Sources
- AKK portal: https://akk.rks-gov.net/en
- AKK / KOPOS card: https://akk.rks-gov.net/en/akk
- AKK Administrative Instruction QRK No. 04/2024 (tariff PDF, Shtojca 1 §1.2.2): https://akk.rks-gov.net/storage/app/media/udhezim-administrativ-qrk-nr-04-2024-per-tarifat-per-produktet-cmimorja.pdf
- KOPOS SBC register: https://kopos.rks-gov.net/SBC/Account/Register
- KOPOS SBC login: https://kopos.rks-gov.net/SBC/Account/Index (v7.8.1.438; HEAD 200, 2026-05-16)
- ardusimple Kosovo: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kosovo/
- GIM International (network ICB 2011): https://www.gim-international.com/content/news/gnss-reference-network-for-kosovo
- mycoordinates.org KOPOS overview (RTCM 2.3/3.1 VRS, Leica GR15, prepaid SBC): https://mycoordinates.org/kopos-kosovo-positioning-system/
- TCP probes `kopos.rks-gov.net:2101` 2026-05-06, -12, -16, -17 — all timed out (external IP); geo-firewall hypothesis stable
- HEAD `https://kopos.rks-gov.net/SBC/Account/Index` + `https://akk.rks-gov.net/en` 2026-05-16 + 2026-05-17 — HTTP 200
- WebSearch "KOPOS Kosovo AKK GNSS NTRIP 2026 tariff" 2026-05-17 — no new tariff or service announcement beyond QRK 04/2024
- KOSOVAREF01 / ETRS89 cited in FIG + ResearchGate + academia.edu + epsg.io — NOT operator-owned, NOT citable for datum_epoch per project rule
