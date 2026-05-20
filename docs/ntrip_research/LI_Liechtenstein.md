# Liechtenstein [LI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified swisstopo pricing page + APOS BEV datum; rtk2go/centipede nearby-station count refreshed via stations_by_radius.py)

## Status: NO dedicated LI caster — Liechtenstein relies entirely on Swiss swipos and Austrian APOS/EPOSA, both of which provide coverage across LI territory

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster — LI-specific** | No — no Liechtenstein national caster exists |
| **Effective coverage** | Full — Swiss swipos and Austrian APOS/EPOSA both cover Liechtenstein |
| **Primary network — swipos** | swipos-GIS/GEO (Swiss Federal Office of Topography / swisstopo) |
| **landing_url — swipos** | https://www.swisstopo.admin.ch/en/swipos-gisgeo-for-rtk-and-postprocessing-applications (operator-owned swisstopo service page) |
| **access_url — swipos** | https://www.swisstopo.admin.ch/en/swipos-services-prices-and-ordering (distinct page covering tariffs + ordering/registration workflow) |
| **num_stations — swipos** | ~130 physical CORS across Switzerland (operator figure, swisstopo). 0 stations physically inside LI territory; nearest Swiss stations in Graubünden / St. Gallen 5–25 km from LI. |
| **host:port — swipos** | `www.swipos.ch:2101` (plain TCP) / `:2102` (TLS NTRIP-2) per swisstopo technical docs + rtk_inventory.md `swipos` block. Older alias `swipos.swisstopo.admin.ch:2101` still referenced in some operator material. Credentials issued post-subscription |
| **tariff — swipos flat-rate** | CHF 1,500/year first licence; multi-licence discounts ("from same provider"); all fees net of VAT/MWST. Source: swisstopo.admin.ch/en/swipos-services-prices-and-ordering (WebFetch 200, 2026-05-17) |
| **tariff — swipos pay-per-use** | CHF 0.50/minute VRS corrections; CHF 0.50/minute RINEX (same source, 2026-05-17) |
| **vrs — swipos** | yes — confirmed by CHF 0.50/min VRS pay-per-use tariff line on swisstopo pricing page (2026-05-17) |
| **VRS — swipos** | Yes — Network RTK / VRS corrections; RTCM 3.x MSM; cm-level accuracy |
| **hobbyist_eligibility — swipos** | Yes — individual registration accepted; no professional licence requirement |
| **legal_residency_required — swipos** | No explicit requirement; Swiss VAT (MWST) applies; non-Swiss individuals can subscribe |
| **last_confirmed_alive — swipos** | 2026-05-17 (swisstopo.admin.ch pricing page HTTP 200 via WebFetch; CHF 1,500/yr + CHF 0.50/min unchanged since 1 Apr 2023 administrative simplification) |
| **datum_epoch — swipos** | omitted -- no citable declaration on swisstopo pricing/technical pages fetched 2026-05-17 (LV95 / CHTRS95 widely used in CH but not operator-stated for swipos NTRIP service in pages reviewed) |
| **Secondary network — EPOSA** | EPOSA (Austrian private CORS operated by several Austrian states + Vorarlberg) |
| **Coverage in LI — EPOSA** | Yes — EPOSA explicitly states corrections are available "approximately 80 km beyond the national border" covering Liechtenstein, Germany, Italy, Slovenia, Slovakia, and Hungary |
| **host:port — EPOSA** | `eposa.at:2101` (NTRIP) |
| **tariff — EPOSA** | Contact eposa.at for current rates; commercial pricing |
| **Secondary network — APOS** | APOS (Austrian Positioning Service, BEV) |
| **landing_url — APOS** | https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html (operator-owned BEV service page) |
| **access_url — APOS** | https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html (same page documents conditions, tariffs, registration contact; no separate signup URL) |
| **Coverage in LI — APOS** | Yes — Austrian reference stations in Vorarlberg provide corrections into Liechtenstein territory |
| **num_stations — APOS** | ~40 physical CORS across Austria (BEV operator figure). 0 stations physically in LI; closest stations in Vorarlberg (Feldkirch / Bregenz area) ~10–30 km from LI. |
| **host:port — APOS** | `apos.bev.gv.at:2101` |
| **tariff — APOS** | Agriculture/forestry: free (BEV decision 1 Feb 2021, confirmed 2026-05-17). Other users: setup EUR 50; APOS-RTK EUR 0.0015/s, EUR 20/day, EUR 200/month; APOS-DGPS EUR 0.00015/s / EUR 2/day / EUR 20/month; APOS-PP free; APOS-RAW EUR 50,000/year. Source: bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html (WebFetch 200, 2026-05-17) |
| **vrs — APOS** | yes — confirmed by `APOS_VRS32_GRID2021` mountpoint in apos.bev.gv.at:2101 sourcetable (network RTK / VRS) |
| **datum_epoch — APOS** | ETRS89 realisation `ETRF2000 (Epoch 2002.56), solution Austria 2002` -- operator-declared on bev.gv.at APOS page (cited 2026-05-17) |

## Context Notes

- **No LI national caster**: Liechtenstein (population ~38,000, area 160 km²) has no surveying authority that operates an independent NTRIP caster. The country is fully served by its larger neighbours.
- **swipos as primary**: swipos-GIS/GEO is the natural choice for Liechtenstein users. The country uses the Swiss coordinate reference system LV95 (CH1903+/LHN95), which swipos directly supports. swipos was simplified administratively on 1 April 2023 (single-account registration replacing earlier Geocat-based process).
- **swipos coverage**: swisstopo operates ~130 reference stations across Switzerland. Liechtenstein has no stations of its own in swipos, but the Swiss stations in Graubünden and St. Gallen (across the Rhine) provide full coverage of the LI territory. Typical baseline from LI to nearest Swiss swipos station: 5–25 km.
- **APOS free agriculture**: Since 1 February 2021, APOS provides RTK corrections free of charge for agriculture and forestry users (Austrian Landwirtschaftskammer announcement). Since Liechtenstein has an active farming sector (wine, dairy, livestock), this may be relevant to Liechtenstein farmers with Austrian APOS accounts.
- **EPOSA**: Operated by Energie Steiermark Technik GmbH for a consortium of Austrian states and Vorarlberg specifically. Coverage extends 80 km across borders by design to serve cross-border users in Liechtenstein, German Bavaria, and beyond.
- **Hobbyist note**: A Liechtenstein-based hobbyist should use swipos-GIS/GEO as the primary service. Pay-per-use at CHF 0.50/minute (no subscription) is the lowest-commitment entry point. Galileo HAS (free satellite-broadcast, ~40 cm) is a zero-cost fallback.
- **Local geodetic authority**: As of 1 April 2022 the Liechtenstein cadastral/geoinformation authority was renamed **Amt für Tiefbau und Geoinformation** (ATG, Städtle 38, 9490 Vaduz). ATG provides the national geoportal `geodaten.llv.li` but does not operate an NTRIP caster.
- **Centipede/rtk2go presence in/near LI** (radius probe 47.14 N / 9.52 E within 60 km, stations.json 2026-05-17): 4 Centipede CHZ bases — `SEGA` Sevelen 14.3 km, `LT06` 45.6 km, `LABA` 54.5 km, `UELI` 59.6 km; 3 rtk2go CHE bases — `suedostschweiz` 28.9 km, `ICOMOST` 53.6 km, `eid_genoss` 56.9 km; 1 EUREF-IP AUT `PFA300AUT0` 46.6 km. SEGA (Centipede) is the closest free volunteer base; suedostschweiz (rtk2go) is the closest free base south of Vaduz. Unaffiliated volunteer / unstable.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **swipos online RINEX (swipos-PP)** | https://www.swisstopo.admin.ch/ | Separate subscription or per-session |
| **APOS post-processing** | https://apos.bev.gv.at/ | Free (agriculture); paid (others) |
| **EUREF-SAT / EPN archive** | https://epncb.oma.be/ | Free |

## Sources Consulted
- swipos pricing and ordering: https://www.swisstopo.admin.ch/en/swipos-services-prices-and-ordering
- swipos GIS/GEO RTK page: https://www.swisstopo.admin.ch/en/swipos-gisgeo-for-rtk-and-postprocessing-applications
- swipos FAQ: https://www.swisstopo.admin.ch/en/swipos-frequently-asked-questions
- swipos admin simplification (1 Apr 2023): https://www.swisstopo.admin.ch/en/administrative-simplifications-of-the-swiss-positioning-service-swipos-as-of-1-april-2023
- APOS BEV service page: https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html
- EPOSA service page: https://www.eposa.at/en/englisch
- Austrian Landwirtschaftskammer free APOS announcement: https://www.lko.at/kostenfreier-rtk-korrekturdatendienst-hier-geht-s-zu-allen-infos-und-zur-registrierung+2400+3309904
- ArduSimple Austria: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-austria/
- NTRIP-list Europe: https://ntrip-list.com/europe/
