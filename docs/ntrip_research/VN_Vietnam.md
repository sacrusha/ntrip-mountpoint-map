# Vietnam [VN] — NTRIP RTK
**Date:** 2026-05-17 (re-verify of 2026-05-13 baseline; ops portal `gddt.vngeonet.vn` known slow — timed out today, no contradicting facts. AUSCORS publishes IGS station `HUMG00VNM0` (21.07N, 105.77E, Hanoi University of Mining and Geology) — single IGS-tier MP, free under AUSCORS terms. Not part of VNGEONET caster.).

## Status
YES. Single national caster VNGEONET, paid + sparse-zone free tier. Sourcetable last probed 2026-05-12 (no shell access today; portal HTML timed out).

## VNGEONET — sole caster

| Field | Value |
|---|---|
| landing_url | https://gddt.vngeonet.vn/ |
| access_url | https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-ket-noi-su-dung?culture=en-US (EN connection guide) |
| operator | DoSM (Cục Đo đạc, Bản đồ và Thông tin địa lý) under Ministry of Agriculture and Environment (post-2026 merger; ex-MONRE). Sourcetable operator string: `DoSM`. |
| host:port | `vngeonet.vn:2101` (VRS); `:2102`, `:2103` alt ports. IP `14.238.1.125`. Leica GNSS Spider 7.7.1.9072. |
| num_stations | 65 (24 Geodetic CORS + 41 NRTK CORS). |
| Mountpoints | 20 VRS streams, RTCM3, GPS+GLO+GAL+BDS+QZSS, NMEA=Y. Names `VRS.WGS84`, `VRS.10xM3`, `VRS.10x_yyM3`, `VRS.105M6`, `VRS.111M6`. All listed at network ref pt 20.67N,105.53E (single VRS entry — physical stations hidden). |
| vrs | yes |
| tariff — 1 mo | VND 750,000 (~USD 29) |
| tariff — 6 mo | VND 4,280,000 (~USD 168) |
| tariff — 12 mo | VND 6,750,000 (~USD 266) |
| tariff — 12 mo, sparse | Free (zones with >80 km station spacing). |
| VAT | Not stated. Fee schedule = Circular 47/2024/TT-BTC (MoF); original auth Circular 03/2020/TT-BTNMT (MONRE, 2020-05-29). |
| hobbyist_eligibility | yes — "tổ chức và cá nhân"; ID scan (Citizen ID or Passport) required. |
| legal_residency_required | no — passport explicitly accepted. |
| last_confirmed_alive | 2026-05-12 — TCP sourcetable probe returned 20 VRS MPs, server `GNSS Spider 7.7.1.9072/1.0`. Portal HTTP HEAD 200 on 2026-05-13. 2026-05-17 WebFetch timed out (known slow). |
| datum_epoch | omitted — no citable operator declaration. (VRS.WGS84 MP name implies WGS84 broadcast but operator portal carries no explicit datum/epoch statement; VN-2000 is national static datum but not declared on VNGEONET pages.) |

## Notes

- MP naming: `M3`/`M6` = Leica Spider MAX (RTCM3 / RTCM3+MSM6); `_15/_30/_45` likely msg-rate or msg-set variant. Foreign rovers: try `VRS.WGS84` first.
- Free tier: areas where station spacing exceeds 80 km (remote/rural) get 12-mo free access.
- Pricing source = JS-rendered service cards on gddt.vngeonet.vn; legal auth = Circular 47/2024/TT-BTC.

## Coverage in project sources

- `stations_by_country.py VNM` 2026-05-17: 1 station — `HUMG00VNM0` (AUSCORS), Hanoi.
- Zero VN MPs in rtk2go/centipede/earthscope. No GEODNET/ONOCOY public VN coverage. No commercial alternative.
- HUMG = IGS station hosted by Hanoi University of Mining and Geology, re-broadcast by AUSCORS under CC BY 4.0 (same terms as AUSCORS Australia stations). Useful single-base for ~30 km around Hanoi for foreign rovers who can register AUSCORS but not VNGEONET.

## Post-processing (RINEX)

Not a primary VNGEONET offering. RINEX requests via DoSM / gddt.vngeonet.vn.

## Sources
- https://gddt.vngeonet.vn/ (operator portal; HEAD 200 2026-05-13; WebFetch timed out 2026-05-17)
- EN connection guide: https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-ket-noi-su-dung?culture=en-US
- Account guide: https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-tao-tai-khoan-sbc
- Leica case study: https://leica-geosystems.com/case-studies/surveying-and-engineering/advancing-vietnam-geodetic
- Circular 47/2024/TT-BTC (MoF); Circular 03/2020/TT-BTNMT (MONRE)
- Sourcetable TCP probe 2026-05-12: `vngeonet.vn:2101` → 200 OK, 20 VRS MPs.
