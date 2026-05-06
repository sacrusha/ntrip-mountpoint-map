# Croatia [HR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — national government NTRIP RTK caster operating (CROPOS); registration required; real-time RTK free since 2022

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | CROPOS (CROatian POsitioning System) |
| **Operator** | Državna geodetska uprava (DGU) — State Geodetic Administration of Croatia |
| **host:port** | `195.29.198.194:2101` (confirmed active IP per DGU announcement; domain `gnss.cropos.hr` used for web portal) |
| **VRS** | Yes — High-Precision Positioning Service (VPPS) provides Network RTK / VRS corrections; ≤2 cm horizontal, ≤4 cm vertical |
| **tariff — DPS (Differential Positioning Service)** | Free (no charge since April 2022 law amendment; ~0.5 m accuracy) |
| **tariff — VPPS (Network RTK / VRS)** | Free (no charge since April 2022 law amendment; ≤2 cm accuracy) |
| **tariff — GPPS (Geodetic Precision Positioning Service)** | Charged per minute: 0.5 HRK/min at time of research (kuna-era pricing; Croatia adopted EUR 1 Jan 2023 — current EUR equivalent not confirmed; contact DGU for updated tariff) |
| **tariff — registration fee** | 300 HRK one-time (kuna-era; current EUR equivalent not confirmed) |
| **VAT** | Croatian standard VAT 25% |
| **hobbyist_eligibility** | Yes — registration open to individuals; no professional licence requirement stated |
| **legal_residency_required** | Unclear — registration is via email to cropos@dgu.hr; no explicit residency restriction found |
| **last_confirmed_alive** | 2026-05-06 (cropos.hr website HTTP 200; DGU notice confirming IP 195.29.198.194:2101 and April 2025 network expansion found in search results) |

## Context Notes

- **CROPOS overview**: Croatia's national CORS network operated by the State Geodetic Administration (DGU). ~30 reference stations spaced ~50 km apart covering the entire territory including islands. Launched 2008; part of the EUPOS network.
- **Free RTK since 2022**: The Law on Amendments to the Law on State Survey and Real Estate Cadastre (NN 39/2022, effective 7 April 2022) abolished charges for the DPS and VPPS real-time services. The VPPS (Network RTK / VRS) service — the main RTK product — is now free of charge for all registered users. Only the GPPS high-accuracy geodetic service (post-processing grade, per-minute billing) remains charged.
- **April 2025 expansion**: DGU added two new reference station locations to the CROPOS network solution in early April 2025 as part of ongoing densification activities.
- **Currency note**: Croatia adopted the euro on 1 January 2023, replacing the kuna. Pricing documents on the CROPOS website citing kuna amounts (kn) are outdated. Updated EUR pricing for GPPS and registration fees was not confirmed as of 2026-05-06; contact DGU at cropos@dgu.hr for current EUR tariffs.
- **Reference system**: HTRS96 (Croatian Terrestrial Reference System 1996), the Croatian realization of ETRS89.
- **Access procedure**: Submit registration request to `cropos@dgu.hr` or by post to Državna geodetska uprava, Gruška ulica 20, 10 000 Zagreb, or by fax +385 (0)1 6165 430. Credentials issued after approval.
- **Portal**: gnss.cropos.hr provides a web-based GNSS processing portal and station status monitoring (uses Trimble Pivot software).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **CROPOS RINEX download (GPPS)** | https://gnss.cropos.hr/ (login required) | Per-minute charge (GPPS rate; see above) |

## Sources Consulted
- CROPOS main site: https://www.cropos.hr/
- CROPOS fees page: https://www.cropos.hr/o-sustavu/naknade-za-koristenje-podataka-cropos-sustava
- CROPOS VPPS service: https://www.cropos.hr/servisi/vpps
- DGU new CROPOS services announcement (IP 195.29.198.194:2101): https://dgu.gov.hr/vijesti/nove-usluge-sustava-cropos/5224
- CROPOS GNSS web portal: https://gnss.cropos.hr/
- HKOIG law amendment note: https://www.hkoig.hr/novo-dodano/vijesti-iz-struke/uvjeti-koristenja-cropos-sustava-vezano-za-donesene-izmjene-zakona-o-drzavnoj-izmjeri-i-katastru-nekretnina
- corsstations.com CROPOS profile: https://corsstations.com/networks/croatia-cors-network-cropos-gnss-rtk-service/
- ArduSimple Croatia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-croatia/
