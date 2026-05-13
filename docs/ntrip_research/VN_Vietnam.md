# Vietnam [VN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (re-verification of 2026-05-06 baseline; new sourcetable probe)

## Status: YES — national government NTRIP caster operating (VNGEONET); paid subscription; caster sourcetable retrieved live 2026-05-12

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | VNGEONET |
| **Operator** | Department of Survey, Mapping and Geographic Information (Cục Đo đạc, Bản đồ và Thông tin địa lý — DoSM); operator string in sourcetable: `DoSM`. Parent ministry: Ministry of Natural Resources and Environment (MONRE) until late 2025 merger; from 2026 the merged Ministry of Agriculture and Environment |
| **host:port** | `vngeonet.vn:2101` confirmed live 2026-05-12 (IP 14.238.1.125; ports 2102 and 2103 published as alternates) |
| **Caster software** | Leica GNSS Spider 7.7.1.9072 (server header in 2026-05-12 sourcetable) |
| **num_stations** | 65 stations total (24 Geodetic CORS + 41 NRTK CORS) — figure published by VNGEONET; commissioning completed 2019 |
| **Mountpoints (sourcetable 2026-05-12)** | 20 VRS-style products, all RTCM 3, GPS+GLO+GAL+BDS+QZSS, NMEA=Y (rover GGA required): VRS.WGS84, VRS.103M3, VRS.104M3, VRS.104_30M3, VRS.104_45M3, VRS.105M3, VRS.105M6, VRS.105_30M3, VRS.105_45M3, VRS.106M3, VRS.106_15M3, VRS.106_30M3, VRS.107M3, VRS.107_15M3, VRS.107_30M3, VRS.107_45M3, VRS.108M3, VRS.108_15M3, VRS.108_30M3, VRS.111M6. All listed at the network reference point 20.67°N, 105.53°E (single VRS — physical CORS not advertised individually). |
| **VRS** | Yes (network RTK / VRS corrections — confirmed by sourcetable; NMEA-driven) |
| **tariff — RTK 1 month** | VND 750,000 / rover (~$29.5 USD @ 25,420 VND/USD) |
| **tariff — RTK 6 months** | VND 4,280,000 / rover (~$168.4 USD) |
| **tariff — RTK 12 months** | VND 6,750,000 / rover (~$265.6 USD) |
| **tariff — RTK 12 months (sparse zones)** | Free (stations >80 km spacing zones) |
| **VAT status** | Not explicitly stated on public page; Vietnamese government data services subject to state-set fee schedule under Circular TT47/2024; VAT applicability unclear |
| **Fee authority** | Circular No. 47/2024/TT-BTC (Ministry of Finance); original authority Circular No. 03/2020/TT-BTNMT (MONRE, 29 May 2020) |
| **hobbyist_eligibility** | Yes — registration explicitly open to "organizations and individuals" (tổ chức và cá nhân); registration requires scan of Citizen Identity Card or Passport; no surveying licence required |
| **legal_residency_required** | No — Passport-based registration accepted (passport explicitly listed alongside Citizen ID); foreign nationals can register |
| **registration** | https://gddt.vngeonet.vn/ → "Đăng ký tài khoản" (Create Account). English connection guide: https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-ket-noi-su-dung?culture=en-US. Contact: (+84) 24-66603032, vngeonet.vn@gmail.com |
| **last_confirmed_alive** | 2026-05-12 — direct TCP/sourcetable probe of `vngeonet.vn:2101` returned SOURCETABLE 200 OK, 20 VRS mountpoints, Content-Length 2322; HEAD probe of `https://gddt.vngeonet.vn/` returned HTTP 200 on 2026-05-13 |

## Context Notes

- **VNGEONET** (`vngeonet.vn:2101`): Operated by the Vietnamese government under the geodesy/mapping department (DoSM, formerly under MONRE). The connection guide at `gddt.vngeonet.vn` documents the endpoint as "IP máy chủ (Host IP): 14.238.1.125 (hoặc vngeonet.vn). Cổng (Port): 2101 hoặc 2102 hoặc 2103." Provides nationwide RTK corrections.
- **Mountpoint naming**: The `VRS.NNNxxx` pattern almost certainly encodes Leica Spider VRS solution variants (e.g. `M3` = MAX RTCM 3, `M6` = MAX RTCM 3 with MSM6, `_15/_30/_45` likely encode update-rate or message-set variants). Confirmed via Leica GNSS Spider 7.7.1.9072 server header. Foreign-receiver users should test `VRS.WGS84` first.
- **Free tier**: Areas with reference station spacing exceeding 80 km qualify for free 12-month access; this likely applies to remote/rural regions where the network is less dense.
- **Registration**: Requires a scan of national ID or passport submitted through the registration portal. Individual access explicitly supported.
- **Pricing source**: Tariff figures published on the gddt.vngeonet.vn homepage service cards (loaded via JavaScript); the authoritative legal schedule is Circular No. 47/2024/TT-BTC.
- **No volunteer/global coverage in project sourcetables**: stations_by_radius.py 21.03 105.85 200 (Hanoi) returns zero rtk2go/centipede/earthscope mountpoints; same in the south (no Centipede / GEODNET / ONOCOY public coverage of Vietnam confirmed 2026-05-13).

## Post-Processing (RINEX) Fallback

Post-processing RINEX data is not described as a primary offering; the VNGEONET service is focused on real-time correction delivery. Contact MONRE / gddt.vngeonet.vn for RINEX data availability.

## Sources Consulted
- VNGEONET portal: https://gddt.vngeonet.vn/ (homepage service cards, 2026-04-30; HTTP 200 re-confirmed 2026-05-13)
- VNGEONET connection guide (EN): https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-ket-noi-su-dung?culture=en-US
- VNGEONET account creation guide: https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-tao-tai-khoan-sbc
- ArduSimple country page (mirrors VNGEONET details): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-vietnam/
- Leica Geosystems case study — VNGEONET design and build: https://leica-geosystems.com/case-studies/surveying-and-engineering/advancing-vietnam-geodetic
- Circular No. 47/2024/TT-BTC (Ministry of Finance fee schedule)
- Circular No. 03/2020/TT-BTNMT (MONRE, original authority)
- Direct TCP sourcetable probe `vngeonet.vn:2101` 2026-05-12 — SOURCETABLE 200 OK, 20 VRS mountpoints listed, server `GNSS Spider 7.7.1.9072/1.0`
