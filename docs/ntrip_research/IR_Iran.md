# Iran [IR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — two active government NTRIP RTK casters (SHAMIM / SHAMIM Plus + Hoda Pro); both restricted to Iranian nationals; endpoint IPs geo-blocked from outside Iran

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — SHAMIM (SSAA, free) + Hoda Pro (NCC, paid) |
| **host:port — SHAMIM** | `178.252.173.15:2101` |
| **host:port — SHAMIM Plus** | `178.252.173.75:2101` |
| **host:port — Hoda Pro** | `hodapro.ncc.gov.ir:2101` (IP ~188.4.x.x per practitioner posts; exact octet unconfirmed) |
| **VRS** | SHAMIM / SHAMIM Plus: yes (GEO++ GNSMART, multiple virtual reference station mountpoints) |
| **tariff — SHAMIM** | Free (government-funded under the Cadastre programme; ‌no subscription fee) |
| **tariff — Hoda Pro** | Unknown — e-shop (`eshop.ncc.gov.ir`) requires Iranian account; unreachable from outside Iran; tiers (daily / 3-day / 7-day / 15-day / monthly / 3-month / 6-month / annual) confirmed to exist but no IRR prices recovered |
| **VAT** | Unknown for Hoda Pro; N/A for SHAMIM (free) |
| **hobbyist_eligibility — SHAMIM** | No — requires licensed cadastral surveyor status or SSAA-authorised outsourcing role; receiver serial number must be pre-registered; single concurrent connection per account |
| **hobbyist_eligibility — Hoda Pro** | Unclear — individual surveyors and engineers appear to register without company licence; Iranian national ID (شماره ملی) required; no explicit prohibition on unlicensed individuals found |
| **legal_residency_required** | Yes (both) — Iranian national ID + Iranian banking required for Hoda Pro; Iranian national ID + Iranian mobile number for SHAMIM |
| **last_confirmed_alive** | SHAMIM: 2025-05-04 (Google-indexed, active use confirmed in practitioner content through 2024–2025; direct TCP blocked from outside Iran). Hoda Pro: Google index confirms `hodapro.ncc.gov.ir` active; Raymand article 2024-04-30 describes live service; practitioner content through 2024–2025 confirms active use |

## Context Notes

- **SHAMIM** (شبکه ملی یکپارچه مالکیت‌ها) is operated by the State Land Registration Organization of Iran (سازمان ثبت اسناد و املاک کشور — SSAA, `ssaa.ir`). It uses GEO++ GNSMART software and provides Network-RTK / VRS corrections. **SHAMIM Plus** (`178.252.173.75:2101`) is an expanded-coverage tier of the same system. Both are free to qualified users under the national Cadastre programme (طرح کاداستر). The "تعرفه نقشه‌برداری شمیم" referred to in some practitioner articles is the tariff *surveyors charge clients* for SHAMIM-based fieldwork — not a subscription fee for caster access.
- **Hoda Pro** (سامانه ملی هدی پرو) is the RTK-capable tier of the NCC's (National Cartographic Center / سازمان نقشه‌برداری کشور) national GNSS correction service, built on IPGN infrastructure. The legacy **Hoda** tier (`hoda.ncc.gov.ir:2101`) is DGPS-only (out of scope). Subscriptions are managed via `eshop.ncc.gov.ir`. The IPGN network itself is a post-processing / geodynamics archive, not a direct NTRIP service.
- **SEMT (سمت)** is a third Iranian RTK correction network mentioned in some practitioner material alongside SHAMIM and Hoda; it is not covered here.
- All Iranian NTRIP casters (`shamim.ssaa.ir`, SHAMIM/SHAMIM Plus IPs, `hodapro.ncc.gov.ir`) appear to restrict TCP access to Iranian IP ranges consistent with broader Iranian internet controls. Direct sourcetable queries from outside Iran time out or return connection errors.
- `ipgn.ncc.gov.ir:2101` returned connection-refused on 2026-05-01 — no public NTRIP caster is reachable at that address.
- No Iranian NTRIP operator appears in the BKG/RTCM-NTRIP public caster registry.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IPGN / NCC** — raw RINEX observation archive for researchers (global access) | https://ncc.gov.ir | Free (account required; accessible internationally) |

## Sources Consulted
- SHAMIM portal: https://shamim.ssaa.ir (login required; blocked from outside Iran)
- SSAA main site: https://ssaa.ir
- Raymand article "سامانه شمیم را بشناسیم": https://raymand.net/fa/مقالات/سامانه-شمیم-را-بشناسیم/
- Hadnegar SHAMIM article (2026-02-12): https://hadnegar.com/shamim-system/
- Araddoorbin SHAMIM registration guide (2024-09-25): https://araddoorbin.com
- Hoda Pro portal: https://hodapro.ncc.gov.ir (blocked from outside Iran)
- NCC e-shop: https://eshop.ncc.gov.ir (blocked from outside Iran)
- Raymand Hoda Pro article (2024-04-30): https://raymand.net
- orbitgeo.ir Instagram posts confirming SHAMIM / SHAMIM Plus IPs (2022–2023)
- `ipgn.ncc.gov.ir:2101` — connection refused 2026-05-01
- GPS World NCC domestic GNSS software article (2026-01-26): https://www.gpsworld.com
