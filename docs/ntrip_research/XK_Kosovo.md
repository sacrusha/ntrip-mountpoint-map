# Kosovo [XK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (re-verification of 2026-05-06 baseline)

## Status: YES — paid national NTRIP (KOPOS), VRS; hobbyist-eligible; caster port 2101 again timed out from external IP 2026-05-12 (consistent with geo-firewall hypothesis); SBC web portal HTTPS confirmed reachable 2026-05-13

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | AKK (Agjencia Kadastrale e Kosovës / Kosovo Cadastral Agency) |
| **host:port** | `kopos.rks-gov.net:2101` (IP 91.239.145.45) |
| **VRS** | Yes — RTCM 2.3 FKP and VRS corrections; internet/GPRS delivery |
| **Stations** | 8 permanent CORS + computation centre in Pristina |
| **Platform** | Leica GNSS Spider / Spider Business Center (SBC) v7.8.1.438 (confirmed from SBC login page 2026-05-06) |
| **GNSS** | GPS + GLONASS + Galileo |
| **Accuracy** | ±2 cm horizontal, ±4 cm vertical (stated) |
| **tariff — initial registration** | €20 one-time per user (Shtojca 1, §1.2.2 of Administrative Instruction QRK No. 04/2024) |
| **tariff — RTK annual** | €400/year per user (1-year RTK subscription; confirmed in AKK Administrative Instruction QRK No. 04/2024, issued 2024) |
| **tariff — RTK 6-month** | €250/6 months per user |
| **tariff — RTK 1-month** | €60/month per user |
| **tariff — RINEX + post-processing annual** | €100/year per user |
| **tariff — RINEX + post-processing 6-month** | €70/6 months per user |
| **tariff — RINEX + post-processing 1-month** | €30/month per user |
| **VAT** | Kosovo standard VAT rate 18%; tariff document does not state whether prices are VAT-inclusive or exclusive — verify at AKK |
| **tariff source** | AKK Administrative Instruction QRK No. 04/2024 (PDF: akk.rks-gov.net/storage/app/media/udhezim-administrativ-qrk-nr-04-2024-per-tarifat-per-produktet-cmimorja.pdf), observed 2026-05-06 |
| **hobbyist_eligibility** | Yes — SBC registration form requests rover brand, serial number, address only; no surveying-licence requirement found |
| **legal_residency_required** | Unclear — no confirmed restriction; not explicitly stated on registration form |
| **registration** | https://kopos.rks-gov.net/SBC/Account/Register (Leica Spider Business Center self-service form; requires rover brand/serial/address) |
| **last_confirmed_alive** | `kopos.rks-gov.net:2101` — TCP connection timed out from external IP 2026-05-12 (consistent with 2026-05-06 result; port likely firewalled outside Kosovo). `kopos.rks-gov.net` HTTPS (SBC login) returned HTTP 200 on 2026-05-13 (Leica Spider Business Center v7.8.1.438 still on login page). `akk.rks-gov.net` HTTP 200 on 2026-05-13 |

## Context Notes

- **KOPOS** (Kosovo Positioning System) was established via World Bank-funded International Competitive Bidding; Leica Geosystems and KCA signed the contract in September 2011; the network became operational ca. 2012–2013. Eight AR25 choke-ring antenna reference stations are distributed across Kosovo territory; the control and computation centre is in Pristina.
- **Tariff update**: Administrative Instruction QRK No. 04/2024 (the current pricing decree observed on the AKK website 2026-05-06) confirms the annual RTK subscription at €400/user/year, with a one-time initial registration fee of €20. This is consistent with the figure cited in country-survey.md (date_added 2026-04-30). A second pricing document (CMIMORE.pdf) is available from the AKK website but appeared to be image-based and could not be text-extracted.
- **Port 2101 status**: TCP connection attempts from external IP timed out on 2026-05-06 (both 15s and 20s timeout); IP 91.239.145.45 resolved correctly. The port may be firewalled for connections outside Kosovo; credentials are required anyway and delivered through the SBC portal (kopos.rks-gov.net/SBC/Account/Index). The SBC web interface responded correctly over HTTPS on 2026-05-06.
- **EUREF/EPN**: Kosovo's non-UN-member status has historically complicated participation in EUREF Permanent Network; no confirmed EPN station as of research date.
- **Volunteer coverage**: Zero XK volunteer bases on rtk2go or Centipede.
- **At €400/year**, KOPOS is expensive relative to regional income levels (Kosovo GDP per capita ~€5,500 in 2025); there is no free hobbyist tier. The monthly plan (€60/month) offers a lower-commitment option.
- The KOPOS NTRIP caster provides both RTK (real-time) and RINEX (post-processing) access; the RTK stream uses RTCM 2.3 FKP and VRS; MSM messages are not explicitly documented in older sources.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **KOPOS RINEX** (via SBC portal) — post-processing data from 8 CORS stations | https://kopos.rks-gov.net/SBC/Account/Index | €100/year or €70/6 months or €30/month per user (QRK 04/2024) |

## Sources Consulted
- AKK (Kosovo Cadastral Agency) main portal: https://akk.rks-gov.net/en
- AKK services / KOPOS link: https://akk.rks-gov.net/en/akk (KOPOS product card observed 2026-05-06)
- AKK Administrative Instruction QRK No. 04/2024 — tariff PDF (Shtojca 1, §1.2.2): https://akk.rks-gov.net/storage/app/media/udhezim-administrativ-qrk-nr-04-2024-per-tarifat-per-produktet-cmimorja.pdf (observed 2026-05-06; pdftotext-extracted)
- KOPOS SBC registration form: https://kopos.rks-gov.net/SBC/Account/Register (registration fields confirmed 2026-05-06; no pricing on this page)
- KOPOS SBC login portal: https://kopos.rks-gov.net/SBC/Account/Index (Leica Spider Business Center v7.8.1.438 confirmed alive 2026-05-06)
- ArduSimple Kosovo RTK services: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kosovo/ (KOPOS listed; no pricing detail)
- GIM International — GNSS Reference Network for Kosovo: https://www.gim-international.com/content/news/gnss-reference-network-for-kosovo (Leica GR25, 2011)
- mycoordinates.org — KOPOS overview article: https://mycoordinates.org/kopos-kosovo-positioning-system/ (RTCM 2.3/3.1, VRS, Leica GR15, prepaid management via SpiderWeb SBC)
- curl probe of `kopos.rks-gov.net:2101` — connection timeout 2026-05-06 (x2; both 15s and 20s attempts); re-tested 2026-05-12 with 8s TCP-only probe — still timeout (geo-firewall hypothesis stable)
- HEAD probe `https://kopos.rks-gov.net/SBC/Account/Index` — HTTP 200 2026-05-13
- HEAD probe `https://akk.rks-gov.net/en` — HTTP 200 2026-05-13
- country-survey.md XK entry (date_added 2026-04-30) — tariff €400/yr + €20 registration cross-confirmed by AKK PDF
