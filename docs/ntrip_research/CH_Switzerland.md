# Switzerland [CH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (live caster, Centipede, rtk2go probes + swisstopo doc fetches). rtk_inventory.md `last_researched_date: 2026-05-12` is stale relative to this file — the 2026-05-15 probe response `Date: Fri, 15 May 2026 21:04:56 UTC` (and Centipede `crtk.net:2101` probe same day) are the most-recent reliable evidence; rtk_inventory.md should be bumped on next pipeline pass.

## Status: YES — paid national NTRIP/VRS (swipos / swisstopo); no free government tier; ~30 Centipede CHZ nodes + ~20 rtk2go CHE volunteer nodes deliver partial free Plateau / Jura coverage

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid only) |
| **Operator** | swisstopo — Federal Office of Topography (Bundesamt für Landestopografie) |
| **Service name** | swipos (Swiss Positioning Service) — product tier swipos-GIS/GEO |
| **landing_url** | https://www.swisstopo.admin.ch/en/swipos-the-swiss-positioning-service |
| **access_url** | https://shop.swipos.ch/ (signup / order endpoint; live HTTP 200 2026-05-17, Microsoft-IIS/10.0 ASP.NET portal — per rtk_inventory.md). Pricing-and-ordering descriptor page at https://www.swisstopo.admin.ch/en/swipos-services-prices-and-ordering. |
| **host:port** | `www.swipos.ch:2101` (plain TCP; live 2026-05-15 — `SOURCETABLE 200 OK`, `Server: NTRIP Trimble Ntrip Caster 5.2`) · `www.swipos.ch:2102` (encrypted NTRIP-2 over TLS — swisstopo's recommended endpoint since Sep 2025) |
| **num_stations** | **31** physical AGNES CORS (operator-core, swisstopo-owned, all on Swiss territory). The swipos VRS network solution additionally incorporates **neighbouring-country CORS** (FR RGP, IT, AT APOS, DE SAPOS) per swisstopo technical documentation to improve hull coverage near the border, but those are not Swiss stations and are not counted in AGNES. |
| **vrs** | Yes — single VRS product, 4 mountpoints differing only by RTCM version + height frame |
| **tariff — pay-per-use** | CHF 0.50 / minute (VRS or RINEX); all fees net of VAT (currently 8.1% Swiss VAT). Unchanged since 2023-04-01. |
| **tariff — annual flatrate** | CHF 1,500 / yr (1st licence) · CHF 600 / yr (2nd & 3rd licences via same reseller) · CHF 200 / yr (each additional licence). Net of VAT. |
| **tariff — swipos-INFRA** | CHF 310 / month / station (raw CORS access; officially priced from Sep 2025) |
| **tariff — swipos-NAV** | Free — but DGNSS-class (RTCM 2.3 GSM/GPRS, sub-metre), **out of project scope** |
| **hobbyist_eligibility** | Yes — order form open to individuals; no professional licence required |
| **legal_residency_required** | No — FAQ does not impose residency; order form open to international applicants. Coverage is "acceptable within 5–10 km of the border" so rover must be inside or near CH. |
| **last_confirmed_alive** | 2026-05-15 — `curl http://www.swipos.ch:2101/` returned `SOURCETABLE 200 OK` and full 4-mountpoint sourcetable; response carried `Date: Fri, 15 May 2026 21:04:56 UTC` (real probe, not a file-edit timestamp). rtk_inventory.md `last_researched_date: 2026-05-12` lags this file by 3 days. |
| **datum_epoch** | CHTRS95 ≡ ETRS89 @ epoch 1993.0 (horizontal); LHN95 or LN02 (height, mountpoint-selectable). Source: https://www.swisstopo.admin.ch/en/swipos-frequently-asked-questions ("swipos-GIS/GEO VRS corrections are transmitted in the CHTRS95 global system. CHTRS95 corresponds with ETRS89 for epoch 1993.0.") |

## Mountpoints (verified live 2026-05-15)

| Mountpoint | Format | Height frame | Constellations | Bitrate |
|---|---|---|---|---|
| `MSM_GISGEO_LV95LHN95` | RTCM 3.4 (MSM4) | LHN95 (modern orthometric) | GPS+GLO+GAL+BDS | 4000 |
| `MSM_GISGEO_LV95LN02` | RTCM 3.4 (MSM4) | LN02 (1902 levelling, official CH height) | GPS+GLO+GAL+BDS | 4000 |
| `VRS_GISGEO_LV95LHN95` | RTCM 3.1 (legacy) | LHN95 | GPS+GLO | 2500 |
| `VRS_GISGEO_LV95LN02` | RTCM 3.1 (legacy) | LN02 | GPS+GLO | 2500 |

Message profile reported: `1005(5),1007/1033(5),MSM4(1)`. Sourcetable also lists `NET;swipos;swisstopo;B;N,Y;http://www.swisstopo.ch/swipos;...` and `CAS;www.swipos.ch;2101;swipos-GISGEO;swisstopo;1;CHE;46.9;7.5;...`.

## Registration

- Order via online form at https://www.swisstopo.admin.ch/en/swipos-order-form (or PDF). Login issued "typically on the following working day."
- Pay-per-use must be activated before each session; flatrate licences are valid 12 months.
- swipos-INFRA is sold by separate contract (sales.swipos@swisstopo.ch).
- Communication costs (SIM data, ~3 MB/hr per swisstopo docs) are the user's responsibility.

## Context Notes

- **No free government tier.** swipos-GIS/GEO is the only official Swiss RTK VRS. swipos-NAV is free but is DGNSS/sub-metre (RTCM 2.3 via GSM/GPRS), not RTK.
- **2025 service refresh.** swisstopo's 2025-09-15 news item ("Enhanced swipos-GIS/GEO Service") added direct AGNES station access, encrypted NTRIP-2 over port 2102, clearer T&Cs, and first-time public pricing for swipos-INFRA. Pricing for swipos-GIS/GEO has been unchanged since 2023-04-01.
- **AGNES backbone.** 31 permanent stations; selected sites (BERN, ZIMM, DAVO, GENO, PAYE, POTS, SASS) participate in EUREF EPN. Re-measurement campaign on 6-year cycle.
- **Centipede volunteer coverage:** 30 CHZ-coded nodes live on `crtk.net:2101` 2026-05-15 (Centipede uses non-ISO code `CHZ` for Switzerland — *not* Czech Republic; ISO CHE/CZE are used by other sources). Clusters along the Plateau (Bern, Lausanne, Yverdon, Basel/Solothurn corridor, Zürich, Eastern Switzerland) and Jura. Receiver mix predominantly RTKBase + U-blox ZED-F9P. Wayback snapshots of `caster.centipede.fr:2101` show steady multi-year growth (2023-01-01: 7 CHZ · 2024-01-01: 10 · 2025-01-01: 18 · 2026-05-15: 30). Meaningful free alternative to swipos for hobbyists on the Plateau/Jura.
- **rtk2go volunteer coverage:** 20 CHE-coded volunteer bases as of 2026-05-15 fetch — Plateau-heavy (Zürich/Bern/Basel/Solothurn), Jura, Valais, thinner Alpine presence. Cross-checked against `data/stations.json`.
- **Around Bern (100 km radius):** ~14 rtk2go + ~36 centipede stations (the latter including 6 cross-border FRA Doubs/Jura nodes). Sufficient density for short-baseline single-base RTK well below swipos pricing.
- **Liechtenstein (LI):** No independent caster. Cross-border swipos covers the principality directly (AGNES stations in Graubünden/St. Gallen sit 5–25 km away across the Rhine). Austrian APOS reaches the eastern half; free for Austrian farmers via eAMA but not a free path for Liechtensteiners.
- Contact: swipos@swisstopo.ch / +41 58 469 01 21

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| swipos RINEX (AGNES stations) | via swipos portal — CHF 0.50/min or included in flatrate | Paid |
| EUREF EPN (Swiss AGNES participants: BERN, ZIMM, DAVO, GENO, PAYE, POTS, SASS) | https://www.epncb.oma.be/ | Free |

## Sources Consulted

- swisstopo swipos overview: https://www.swisstopo.admin.ch/en/swipos-the-swiss-positioning-service (fetched 2026-05-15)
- swipos prices & ordering: https://www.swisstopo.admin.ch/en/swipos-services-prices-and-ordering (fetched 2026-05-15; pricing unchanged since 2023-04-01)
- swipos-GIS/GEO product page: https://www.swisstopo.admin.ch/en/swipos-gisgeo-for-rtk-and-postprocessing-applications (fetched 2026-05-15)
- swipos technical details: https://www.swisstopo.admin.ch/en/technical-details-for-swipos (fetched 2026-05-15)
- swipos FAQ (authoritative datum/epoch quote): https://www.swisstopo.admin.ch/en/swipos-frequently-asked-questions (fetched 2026-05-15)
- swipos news (2025-09-15 service refresh): https://www.swisstopo.admin.ch/en/swipos-news (fetched 2026-05-15)
- swipos order form: https://www.swisstopo.admin.ch/en/swipos-order-form
- LV95 / LHN95 reference frame: https://www.swisstopo.admin.ch/en/local-swiss-reference-frames
- AGNES network: https://pnac.swisstopo.admin.ch/pages/en/agnes.html
- Live curl probe of `www.swipos.ch:2101` — `SOURCETABLE 200 OK`, 4 mountpoints, 2026-05-15 21:04 UTC
- Live curl probe of `crtk.net:2101` — Centipede `Millipede-caster` header, 30 CHZ stations counted 2026-05-15
- Local pipeline data: `data/stations.json` (rtk2go CHE = 20, centipede CHZ = 30)
- Centipede non-ISO country codes: `docs/ntrip_research/_centipede_country_codes.md`
