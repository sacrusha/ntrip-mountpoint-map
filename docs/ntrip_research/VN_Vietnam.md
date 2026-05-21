# Vietnam [VN] — NTRIP RTK

## Status
YES. Single national caster VNGEONET, paid + sparse-zone free tier. Operator EN connection guide live. AUSCORS also publishes IGS station `HUMG00VNM0` (21.07N, 105.77E, Hanoi University of Mining and Geology) — single IGS-tier MP, free under AUSCORS terms, not part of VNGEONET caster.

## VNGEONET — sole national caster

| Field | Value |
|---|---|
| landing_url | https://gddt.vngeonet.vn/ |
| access_url | https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-ket-noi-su-dung?culture=en-US (EN connection guide) |
| operator | DoSM (Cục Đo đạc, Bản đồ và Thông tin địa lý) under Ministry of Agriculture and Environment (merged 2025-03-01 from MARD + MONRE per Vietnam National Assembly restructuring). Sourcetable operator string: `DoSM`. |
| host:port | `vngeonet.vn:2101` (VRS); `:2102`, `:2103` alt ports. IP `14.238.1.125`. Leica GNSS Spider 7.7.1.9072. |
| num_stations | 65 — 24 Geodetic CORS (~150-200 km spacing, national reference frame) + 41 NRTK CORS (50-80 km spacing, real-time). Source: operator EN portal https://gddt.vngeonet.vn/huong-dan-cung-cap/gttram-cors?culture=en-US ("24 Geodetic CORS ... 41 NRTK CORS stations combined with 24 Geodetic CORS"). |
| vrs | yes — 20 VRS MPs on `:2101`, RTCM3, GPS+GLO+GAL+BDS+QZSS, NMEA=Y |
| tariff — 1 mo | VND 750,000 (~USD 29) |
| tariff — 6 mo | VND 4,280,000 (~USD 168) |
| tariff — 12 mo | VND 6,750,000 (~USD 266) |
| tariff — 12 mo, sparse | Free (zones with >80 km station spacing). |
| VAT | Not stated. Fee schedule = Circular 47/2024/TT-BTC (MoF); original auth Circular 03/2020/TT-BTNMT (MONRE, 2020-05-29). |
| hobbyist_eligibility | yes — "tổ chức và cá nhân"; ID scan (Citizen ID or Passport) required. |
| legal_residency_required | no — passport explicitly accepted. |
| last_confirmed_alive | 2026-05-21 — operator EN connection guide reachable (https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-ket-noi-su-dung?culture=en-US); declares host `14.238.1.125 (or vngeonet.vn)`, ports 2101/2102/2103 (VRS/iMAX/SB). TCP sourcetable last probed 2026-05-12 → 20 VRS MPs, server `GNSS Spider 7.7.1.9072/1.0`. |
| datum_epoch | **VN2000** — declared on operator EN connection guide ("result on coordinate system VN2000 105 degree axis meridian, 3 degree projection zone"; RTCM 3.x msgs 1021 "Helmert / Abridged Molodenski coordinate conversion parameters (WGS84 => VN2000)", 1023 "Residual model represented by geographical coordinate grid", 1025 "Projection parameters and zones"). Epoch not declared. Source: https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-ket-noi-su-dung?culture=en-US. |

## Notes

- **Mountpoints (sourcetable 2026-05-12):** 20 VRS streams — names `VRS.WGS84`, `VRS.10xM3`, `VRS.10x_yyM3`, `VRS.105M6`, `VRS.111M6`. All listed at network ref pt 20.67N,105.53E (single VRS entry — physical stations hidden behind VRS hull).
- MP naming: `M3`/`M6` = Leica Spider MAX (RTCM3 / RTCM3+MSM6); `_15/_30/_45` likely msg-rate or msg-set variant. Foreign rovers: try `VRS.WGS84` first.
- **VN2000 vs WGS84 rover output (user-critical):** Operator pushes datum-transformation messages RTCM 3.x 1021/1023/1025 (Helmert + residual grid + projection params, WGS84→VN2000). Most low-cost rovers (u-blox ZED-F9P, common low-cost receivers) do NOT process msgs 1021-1027 — primer `[datum-epoch]`. Rovers without 1021-1027 support output WGS84-realised coordinates, not VN2000; user must transform separately. Receivers that do process 1021-1027 (some Trimble/Leica) output VN2000 directly.
- **Free tier:** operator page `pham-vi-thu-phi-rtk` defines paid zone = stations with mean spacing ≤80 km; free zone = stations with mean spacing >80 km (remote/rural). Specific provinces in each zone NOT enumerated on operator page — user must determine via map or contact DoSM.
- **Pricing source:** dathop.com regulatory explainer confirms 750k VND/mo, 4.28M VND/6mo, 6.75M VND/yr per receiver, effective 2024-09-01 per Circular 47/2024/TT-BTC.

## Coverage in project sources

- `stations_by_country.py VNM`: 1 station — `HUMG00VNM0` (AUSCORS), Hanoi.
- Zero VN MPs in rtk2go/centipede/earthscope. No GEODNET/ONOCOY public VN coverage. No commercial alternative.
- HUMG = IGS station hosted by Hanoi University of Mining and Geology, re-broadcast by AUSCORS under CC BY 4.0 (same terms as AUSCORS Australia stations). Useful single-base for ~30 km around Hanoi for foreign rovers who can register AUSCORS but not VNGEONET.

## Post-processing (RINEX)

Not a primary VNGEONET offering. RINEX requests via DoSM / gddt.vngeonet.vn.

## Sources
- https://gddt.vngeonet.vn/ (operator portal)
- EN connection guide (host:port + VN2000 datum + RTCM 3.x msgs 1021/1023/1025): https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-ket-noi-su-dung?culture=en-US
- EN station composition (24 Geodetic + 41 NRTK): https://gddt.vngeonet.vn/huong-dan-cung-cap/gttram-cors?culture=en-US
- Fee scope page (paid ≤80 km / free >80 km spacing): https://gddt.vngeonet.vn/huong-dan-cung-cap/pham-vi-thu-phi-rtk
- Account guide: https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-tao-tai-khoan-sbc
- Pricing explainer (regulatory): https://dathop.com/huong-dan-dang-ky-va-dong-phi-su-dung-tram-cors/
- Leica case study: https://leica-geosystems.com/case-studies/surveying-and-engineering/advancing-vietnam-geodetic
- Circular 47/2024/TT-BTC (MoF, effective 2024-09-01); Circular 03/2020/TT-BTNMT (MONRE)
- VidaGIS VNGEONET overview (24 Geodetic + 41 NRTK breakdown): https://www.vidagis.com/2020/02/05/vngeonet-the-first-cors-in-vietnam/
- Vietnam government restructuring (MARD+MONRE merger to Ministry of Agriculture and Environment, 2025-03-01): https://en.mae.gov.vn/Pages/chi-tiet-tin-Eng.aspx?ItemID=8762 ; https://www.fas.usda.gov/data/vietnam-vietnam-government-restructuring-major-changes-and-expected-impacts
- Sourcetable TCP probe 2026-05-12: `vngeonet.vn:2101` → 200 OK, 20 VRS MPs.
