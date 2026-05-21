# Faroe Islands [FO] — NTRIP RTK Caster Research

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
| **last_confirmed_alive** | `us.fo/kort/geodesi`: 2026-05-21 (agency geodesy page HTTP 200) |
| **datum_epoch** | FOTM in ETRS89 datum; realised as ITRF2005 epoch 2008.75, transformed to ETRF2000 per EUREF convention. Source: https://us.fo/kort/geodesi |

## Context Notes

- Umhvørvisstovan's geodesy page (`us.fo/kort/geodesi`, re-confirmed 2026-05-17 HTTP 200) explicitly states the agency operates **4 permanent GNSS reference stations** (Klaksvík, Vestmanna, Trongisvágur, Argir) and offers centimetre-level RTK access to surveying firms and construction companies. Access requires direct contact — no caster hostname, port, sourcetable URL, or tariff is published. Page also declares the local FOTM frame (see datum_epoch above).
- **Landsverk** (`landsverk.fo`, the Faroese Roads/Public Works directorate) has no GNSS or NTRIP content.
- No Faroe Islands entry on ntrip-list.com/europe, RTK2go, or other aggregators. Centipede sourcetable 2026-05-19: 0 FRO-coded mountpoints. No volunteer NTRIP alternative.
- The agency was formerly at `umhvorvisstovan.fo`; current domain is `us.fo`.
- **University of the Faroe Islands "Geospatial Centre"** (Setur / setur.fo) — initial funding from Landsverk and Umhvørvisstovan; hosts the HARMONISE GNSS+FBG research project. No public RTK / NTRIP product as of 2026-05-17.

## Most Recent Confirmed Information

Umhvørvisstovan geodesy page (`us.fo/kort/geodesi`) states the 4-station network is operational and available for RTK use by professionals. Page confirmed reachable 2026-05-17.

## Contact for Access
- Geodesist: Stein Fossá (Dátufrøðingur / Geodesist), SteinF@us.fo, +298 342450

## Sources Consulted
- Umhvørvisstovan geodesy page: https://us.fo/kort/geodesi (2026-05-17, HTTP 200; FOTM/ETRS89 datum declaration found here)
- Setur Geospatial Centre announcement: https://www.setur.fo/en/the-university/news/geospatial-centre-of-the-faroe-islands/
- Landsverk: https://landsverk.fo (no GNSS content)
- ntrip-list.com/europe (2026-05-17, no FO entry)
- RTK2go map (2026-05-17, no FO entry)
- Centipede sourcetable (data/centipede.sourcetable 2026-05-19) — 0 FRO-coded mountpoints
