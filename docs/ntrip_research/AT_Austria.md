# Austria [AT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (originally 2026-05-06)

## Status: YES — one national NTRIP caster (APOS/BEV); free tier for agriculture/forestry via eAMA; paid for all others

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | BEV (Bundesamt für Eich- und Vermessungswesen / Federal Office of Metrology and Surveying) |
| **Service name** | APOS (Austrian POsitioning Service) |
| **host:port** | `aposrtk.bev.gv.at:2101` |
| **VRS** | Yes — VRS computed nationwide; multiple mountpoints |
| **tariff — standard (RTK, non-farmer)** | €50 setup fee + €0.0015/s · €20/day · €200/month (all fees net, VAT not specified in docs; assumed 20% AT VAT applies to commercial users) |
| **tariff — standard (DGPS, non-farmer)** | €0.00015/s · €2/day · €20/month |
| **tariff — eAMA (agriculture/forestry)** | Free — open to agricultural/forestry businesses, contract operators, machinery rings, and publicly funded agri-research institutions registered in eAMA |
| **tariff — APOS RAW** | €50,000/year for all-of-Austria raw data access (professional/institutional) |
| **hobbyist_eligibility** | Yes — paid standard tier available to any individual without licence requirement; eAMA free tier requires Austrian agricultural registration |
| **legal_residency_required** | No for paid tier; eAMA free tier requires Austrian agricultural enterprise (LFBIS-Nr. or equivalent) |
| **last_confirmed_alive** | `aposrtk.bev.gv.at:2101` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl confirmed) |

## Mountpoints (VRS)

| Mountpoint | Format | Constellations | Notes |
|---|---|---|---|
| `APOS_VRS` | RTCM 2.3 | GPS+GLO | Legacy; older receivers |
| `APOS_VRS3` | RTCM 3.1 | GPS+GLO | Standard |
| `APOS_VRS32_MSM` | RTCM 3.2 MSM | GPS+GLO+GAL | Multi-constellation |
| `APOS_VRS32_MSM_3D` | RTCM 3.2 MSM | GPS+GLO+GAL | 3D network interpolation |
| `APOS_DGPS` | RTCM 2.x | GPS | Sub-metre DGNSS |

Additional mountpoints (e.g. `APOS_NET3`, `APOS_Extended`, `APOS_Extended_plus`) referenced in BEV documentation; `APOS_Extended_plus` planned 2025 (RTCM 3.2 MSM4 + BeiDou).

## eAMA Free Tier — Details

Since 1 February 2021 the Austrian federal government (BEV + Federal Ministry of Agriculture) provides APOS RTK corrections at no cost to eligible users. Registration:
1. Log in to the eAMA portal (services.ama.at or ama.at) with your Betriebsnummer (LFBIS-Nr.) and PIN.
2. eAMA auto-redirects to the BEV registration form; credentials issued within 48 business hours.
3. The free-tier subsidy equivalence is stated at €400/year per enrolled operation.
Eligible non-farm user groups (research, advisory bodies in agriculture) may request eAMA credentials via ama.at.

## Context Notes

- APOS is a nationwide VRS network, not single-base, so there is no baseline-distance degradation across Austria. Signal covers the full national territory and selected cross-border zones.
- A fixed IPv4 address must be registered with BEV for each device; dynamic IPs are not accepted for the standard paid tier.
- The eAMA tier uses the same `aposrtk.bev.gv.at:2101` endpoint; credentials differ.
- No free public anonymous-access NTRIP tier exists. Paid standard tier requires registration at kundenservice@bev.gv.at or +43 1 21110-822160.
- **Station-count nuance**: project pipeline observes 37 physical Austrian stations from the public sourcetable; BEV public materials cite "75 reference stations domestically and abroad" — the higher figure includes partner / neighbouring-country stations integrated for VRS edge coverage (e.g., SAPOS Bavaria, FReDNet Friuli, swipos AGNES).
- **Volunteer**: 15 AUT-coded rtk2go bases (e.g., AUT00OBDA0, AUT_A-GLAS, AUT_VIE_27 in/near Vienna, AUT_STY_AVL Styria, HalleinANDATA Salzburg, ibk-thabest Innsbruck) + 1 Centipede AT node (BOKU university campus). Confirmed via `scripts/stations_by_country.py AUT` on 2026-05-12. Coverage is reasonable in eastern Austria (Vienna, Lower Austria, Styria) and weaker in the western Alps.
- Liechtenstein (LI) has no independent caster; relies on APOS (free for agri/forestry via eAMA) or Swiss swipos cross-border coverage.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **APOS RAW** (raw station RINEX) | Via BEV portal after paid subscription | €50,000/yr for full network |
| **EUREF EPN** (stations GRAZ, WIEN, LINZ, SBGZ, etc.) | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- BEV APOS products page: https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html (observed 2026-05-06)
- BEV APOS portal (pricing table): https://portal.bev.gv.at/portal/page?_pageid=713,3175360&_dad=portal&_schema=PORTAL (observed 2026-05-06)
- BEV APOS overview: https://www.bev.gv.at/en/Topics/APOS.html (observed 2026-05-06)
- Landwirtschaftskammer Österreich — eAMA FAQ: https://www.lko.at/faqs-apos-rtk-f%C3%BCr-die-land-und-forstwirtschaft+2400+4213915 (observed 2026-05-06)
- LKÖ press release (free RTK launch Feb 2021): https://www.ots.at/presseaussendung/OTS_20201209_OTS0087/lk-oesterreich-begruesst-kostenfreies-rtk-fuer-die-land-und-forstwirtschaft (observed 2026-05-06)
- AMA eAMA APOS registration: https://www.ama.at/fachliche-informationen/kundendaten/apos-stammdatenerhebung (observed 2026-05-06)
- EuroGeographics precision farming case study: https://eurogeographics.org/news/precision-farming-with-the-austrian-positioning-service/ (observed 2026-05-06)
- BEV APOS brochure (PDF) — cites "75 reference stations domestic + abroad": https://www.bev.gv.at/dam/jcr:557736c5-bac5-42c6-8445-25b1ffee3c27/AustrianPOsitioningService-Broschuere.pdf
- curl probe of `aposrtk.bev.gv.at:2101` — SOURCETABLE 200 OK confirmed 2026-05-06
- Local data verification (2026-05-12): `scripts/stations_by_country.py AUT` — 15 rtk2go + 1 Centipede stations enumerated
