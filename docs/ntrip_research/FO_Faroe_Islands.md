# Faroe Islands [FO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry)

## Status: YES (service exists) — but no public endpoint or tariff; access entirely gated behind direct contact with Umhvørvisstovan

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (service confirmed; endpoint not public) |
| **Operator** | Umhvørvisstovan (Faroese Environment Agency) — `us.fo` |
| **host:port** | null — not published |
| **VRS** | Unknown |
| **tariff** | null — no tariff published on `us.fo` or any indexed source |
| **hobbyist_eligibility** | Unclear — geodesy page language implies professional/commercial clients (surveying firms, construction companies with GPS-equipped machines) |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | `us.fo/kort/geodesi`: 2026-05-12 (agency geodesy page HTTP 200 via curl + follow-redirect) |

## Context Notes

- Umhvørvisstovan's geodesy page (`us.fo/kort/geodesi`, re-confirmed 2026-05-12 HTTP 200) explicitly states the agency operates **4 permanent GNSS reference stations** (Klaksvík, Vestmanna, Trongisvágur, Argir) and offers centimetre-level RTK access to surveying firms and construction companies. Access requires contacting the agency directly — no caster hostname, port, sourcetable URL, or tariff is published anywhere online.
- **Landsverk** (`landsverk.fo`, the Faroese Roads/Public Works directorate) has no GNSS or NTRIP content.
- No Faroe Islands entry appears on ntrip-list.com/europe, RTK2go, or any other aggregator surveyed. Centipede sourcetable 2026-05-12 has zero FRO-coded entries.
- The agency was formerly known as Umhvørvisstovan at `umhvorvisstovan.fo`; the current domain is `us.fo`. Google `site:umhvorvisstovan.fo` GNSS search returned 0 results.
- **University of the Faroe Islands "Geospatial Centre"** (Setur / setur.fo) — initial funding from Landsverk and Umhvørvisstovan; hosts the HARMONISE GNSS+FBG research project (Roberts, MEST, Havstovan, TU Graz). No public RTK / NTRIP product surfaced from Setur as of 2026-05-12. setur.fo URL: https://www.setur.fo/en/the-university/news/geospatial-centre-of-the-faroe-islands/

## Most Recent Confirmed Information

Umhvørvisstovan geodesy page (`us.fo/kort/geodesi`) states the 4-station network is operational and available for RTK use by professionals. Page confirmed reachable 2026-05-12.

## Contact for Access
- Geodesist: Stein Fossá (Dátufrøðingur / Geodesist), SteinF@us.fo, +298 342450

## Sources Consulted
- Umhvørvisstovan geodesy page: https://us.fo/kort/geodesi (2026-05-12, HTTP 200)
- Setur Geospatial Centre announcement: https://www.setur.fo/en/the-university/news/geospatial-centre-of-the-faroe-islands/ (2026-05-12)
- Landsverk: https://landsverk.fo (no GNSS content)
- ntrip-list.com/europe (2026-05-12, no FO entry)
- Google site:umhvorvisstovan.fo GNSS search (0 results)
- RTK2go map (2026-05-12, no FO entry)
- Centipede sourcetable probe of `crtk.net:2101` 2026-05-12 — 0 FRO-coded mountpoints
