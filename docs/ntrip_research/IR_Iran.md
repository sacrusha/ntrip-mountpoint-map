# Iran [IR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-23 (refresh of 2026-05-17 entry; geo-block status unchanged — Iranian caster IPs continue to refuse external probes; no Persian-language source-of-truth updates published since 2026-05-17; no IR-tagged stations in any ingested source per `stations_by_country.py IRN`; radius probe Tehran 35.7/51.4 within 250 km returns zero ingested stations)
last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-17
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: YES — three government NTRIP RTK services (SHAMIM / SHAMIM Plus, Hoda Pro, SEMT Tehran); all restricted to Iranian nationals; endpoint IPs geo-blocked from outside Iran

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
| **last_confirmed_alive** | SHAMIM: TCP probe of `178.252.173.15:2101` timed out from sandbox 2026-05-12 (geo-block); 2026-05-23 sandbox vantage unchanged. Service remains referenced in practitioner content through 2024–2026 (raymand.net, hadnegar.com, apsis.ir, hiromap.com — all still indexed). Hoda Pro: Google index confirms `hodapro.ncc.gov.ir` active; Raymand article 2024-04-30 describes live service; practitioner content through 2024–2025 confirms active use |
| **datum_epoch** | omitted — no citable operator declaration. Operator portals (`shamim.ssaa.ir`, `hodapro.ncc.gov.ir`) geo-blocked from sandbox; no Persian-language operator pricing/spec document with datum statement located. Iran's NCC IPGN network is published in ITRF (ITRF2000 originally, ITRF2014 in more recent literature — see Geospatial World "Transformation from ITRF2000 to WGS84" IPGN case study and Springer 2020 "Water Depletion and Land Subsidence in Iran" using IPGN/ITRF2014), but no real-time-service declaration from SHAMIM / Hoda Pro / SEMT was obtained (checked: geospatialworld.net 2026-05-23; Springer chapter 1345_2020_125 2026-05-23) |

## Context Notes

- **SHAMIM** (شبکه ملی یکپارچه مالکیت‌ها) is operated by the State Land Registration Organization of Iran (سازمان ثبت اسناد و املاک کشور — SSAA, `ssaa.ir`). It uses GEO++ GNSMART software and provides Network-RTK / VRS corrections. **SHAMIM Plus** (`178.252.173.75:2101`) is an expanded-coverage tier of the same system. Both are free to qualified users under the national Cadastre programme (طرح کاداستر). The "تعرفه نقشه‌برداری شمیم" referred to in some practitioner articles is the tariff *surveyors charge clients* for SHAMIM-based fieldwork — not a subscription fee for caster access.
- **Station count — 144 permanent CORS** verified 2026-05-13 against two independent Persian primary sources. hadnegar.com (refresh dated 1405 / 2026): "تعداد ۱۴۴ ایستگاه دائم بر روی ساختمان واحدهای ثبتی در کل کشور نصب شده است". heyvalaw.com: "144 ایستگاه دائم بر روی ساختمان واحدهای ثبتی این سازمان در سرتاسر کشور نصب گردید". The same 144 figure appears as the project-completion milestone — initial network commissioning in winter 1395 (Dec 2016 – Feb 2017). No expansion is documented in Persian-language secondary sources through 1404/2025. Inter-station spacing reported as 60–90 km. Apsis.ir confirms ongoing operation with an IP-change notice for the SHAMIM caster (date undated but post-2022).
- **Hoda Pro** (سامانه ملی هدی پرو) is the RTK-capable tier of the NCC's (National Cartographic Center / سازمان نقشه‌برداری کشور) national GNSS correction service, built on IPGN infrastructure. **num_stations — Hoda Pro**: the underlying IPGN network reached ~127 permanent stations in its 2013 phase-2 build-out (per IPGN literature and rtk_inventory `ipgn` entry); no separate Hoda-Pro-specific deployment count has been published, so this should be read as the operational ceiling rather than a confirmed Hoda-Pro figure. The legacy **Hoda** tier (`hoda.ncc.gov.ir:2101`) is DGPS-only (out of scope). Subscriptions are managed via `eshop.ncc.gov.ir`. The IPGN network itself is also published as a post-processing / geodynamics archive.
- **SEMT (سمت)** — *سامانه موقعیت‌یابی آنی تهران* (Tehran Real-Time Positioning System), operated by **Tehran Municipality ICT Organization**. Service portal `rtk.tehran.ir` with user/services subdomain `rtkservices.tehran.ir` (IIS Windows Server banner observable in search snippets). Offered services per apsis.ir SEMT registration guide and FAQ: RTK / virtual RTK / Rinex download / virtual Rinex / post-processing — i.e. an NTRIP RTK caster is in scope. Both `rtk.tehran.ir` and `rtkservices.tehran.ir` returned `ECONNREFUSED` from sandbox 2026-05-17 (geo-block consistent with SHAMIM / Hoda Pro). Registration requires Iranian national ID; account activation is email-confirmed and gated on Tehran Municipality–approved user packages. No NTRIP host:port, no IRR tariff figures, no datum/epoch declaration, and no station count were recoverable without an Iranian-IP vantage point (checked: apsis.ir search snippets 2026-05-17; ipinfo.io AS56547 2026-05-17; rtk.tehran.ir + rtkservices.tehran.ir ECONNREFUSED 2026-05-17). Coverage is Tehran metropolitan scope (municipal mandate), not national. Recorded here as a third Iranian government NTRIP RTK service distinct from SHAMIM (SSAA, national cadastre) and Hoda Pro (NCC, national mapping) — same residency/geoblock pattern; treated as out-of-reach for non-Iranian hobbyists.
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
- Hadnegar SHAMIM article (refresh 1405/2026, "144 ایستگاه دائم" — WebFetch 2026-05-13): https://hadnegar.com/shamim-system-raya/
- Heyvalaw SHAMIM article ("144 ایستگاه دائم … در سرتاسر کشور نصب گردید" — WebFetch 2026-05-13): https://www.heyvalaw.com/web/articles/view/2707/%D8%B3%D8%A7%D9%85%D8%A7%D9%86%D9%87-%D8%B4%D9%85%DB%8C%D9%85.html
- Hadnegar SHAMIM article (2026-02-12): https://hadnegar.com/shamim-system/
- Araddoorbin SHAMIM registration guide (2024-09-25): https://araddoorbin.com
- Hoda Pro portal: https://hodapro.ncc.gov.ir (blocked from outside Iran)
- NCC e-shop: https://eshop.ncc.gov.ir (blocked from outside Iran)
- Raymand Hoda Pro article (2024-04-30): https://raymand.net
- orbitgeo.ir Instagram posts confirming SHAMIM / SHAMIM Plus IPs (2022–2023)
- `ipgn.ncc.gov.ir:2101` — connection refused 2026-05-01
- SEMT (سمت) Tehran Municipality service portal: http://rtk.tehran.ir/ (ECONNREFUSED from sandbox 2026-05-17; geo-block)
- SEMT services subdomain: https://rtkservices.tehran.ir/ (IIS Windows Server banner per search index; ECONNREFUSED from sandbox)
- Apsis SEMT registration guide (HU/FA): https://apsis.ir/مراحل-ثبت-نام-در-سامانه-سمت/ (ECONNREFUSED from sandbox 2026-05-17; consulted via search snippet)
- Apsis SEMT FAQ: https://apsis.ir/سوالات-متداول-faq-ارتباط-با-سمت/ (consulted via search snippet)
- Tehran Municipality ICT Organization (AS56547 operator of `tehran.ir` subdomains): https://ipinfo.io/AS56547
- GPS World NCC domestic GNSS software article (2026-01-26): https://www.gpsworld.com
- TCP probe 178.252.173.15:2101 timed out from sandbox 2026-05-12 (geo-block consistent with prior); sandbox vantage unchanged 2026-05-17
- No IR-tagged stations in rtk2go / Centipede / EarthScope / AUSCORS / MIRAI (re-confirmed 2026-05-23 via `scripts/stations_by_country.py IRN`)
- Geospatial World "Transformation from ITRF2000 to WGS84 - A Case Study for Iranian Permanent GPS Network, IPGN": https://geospatialworld.net/article/transformation-from-itrf2000-to-wgs84-a-case-study-for-iranian-permanent-gps-network-ipgn/ — IPGN coords in ITRF2000 (confirms national frame; not operator real-time-service declaration)
- Springer Nature (2020) "Water Depletion and Land Subsidence in Iran Using Gravity, GNSS, InSAR and Precise Levelling Data" — IPGN tied to ITRF2014 in recent literature: https://link.springer.com/chapter/10.1007/1345_2020_125
