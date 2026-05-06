# Liechtenstein [LI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO dedicated LI caster — Liechtenstein relies entirely on Swiss swipos and Austrian APOS/EPOSA, both of which provide coverage across LI territory

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster — LI-specific** | No — no Liechtenstein national caster exists |
| **Effective coverage** | Full — Swiss swipos and Austrian APOS/EPOSA both cover Liechtenstein |
| **Primary network — swipos** | swipos-GIS/GEO (Swiss Federal Office of Topography / swisstopo) |
| **host:port — swipos** | `swipos.swisstopo.admin.ch:2101` (NTRIP; credentials issued after registration and subscription) |
| **tariff — swipos flat-rate** | CHF 1,500/year (first device); CHF 600 each for 2nd and 3rd devices; CHF 200/device thereafter. Educational institutions: CHF 150/licence. All prices excl. VAT. (source: swisstopo.admin.ch/en/swipos-services-prices-and-ordering, observed 2026-05-06) |
| **tariff — swipos pay-per-use** | CHF 0.50/minute excl. VAT |
| **VRS — swipos** | Yes — Network RTK / VRS corrections; RTCM 3.x MSM; cm-level accuracy |
| **hobbyist_eligibility — swipos** | Yes — individual registration accepted; no professional licence requirement |
| **legal_residency_required — swipos** | No explicit requirement; Swiss VAT (MWST) applies; non-Swiss individuals can subscribe |
| **last_confirmed_alive — swipos** | 2026-05-06 (swisstopo.admin.ch pricing page HTTP 200 confirmed) |
| **Secondary network — EPOSA** | EPOSA (Austrian private CORS operated by several Austrian states + Vorarlberg) |
| **Coverage in LI — EPOSA** | Yes — EPOSA explicitly states corrections are available "approximately 80 km beyond the national border" covering Liechtenstein, Germany, Italy, Slovenia, Slovakia, and Hungary |
| **host:port — EPOSA** | `eposa.at:2101` (NTRIP) |
| **tariff — EPOSA** | Contact eposa.at for current rates; commercial pricing |
| **Secondary network — APOS** | APOS (Austrian Positioning Service, BEV) |
| **Coverage in LI — APOS** | Yes — Austrian reference stations in Vorarlberg provide corrections into Liechtenstein territory |
| **host:port — APOS** | `apos.bev.gv.at:2101` |
| **tariff — APOS** | Agriculture/forestry users: free (since 1 Feb 2021). Other individual users: metered (second-based, daily, monthly flat-rates); contact bev.gv.at for current EUR pricing |

## Context Notes

- **No LI national caster**: Liechtenstein (population ~38,000, area 160 km²) has no surveying authority that operates an independent NTRIP caster. The country is fully served by its larger neighbours.
- **swipos as primary**: swipos-GIS/GEO is the natural choice for Liechtenstein users. The country uses the Swiss coordinate reference system LV95 (CH1903+/LHN95), which swipos directly supports. swipos was simplified administratively on 1 April 2023 (single-account registration replacing earlier Geocat-based process).
- **swipos coverage**: swisstopo operates ~130 reference stations across Switzerland. Liechtenstein has no stations of its own in swipos, but the Swiss stations in Graubünden and St. Gallen (across the Rhine) provide full coverage of the LI territory. Typical baseline from LI to nearest Swiss swipos station: 5–25 km.
- **APOS free agriculture**: Since 1 February 2021, APOS provides RTK corrections free of charge for agriculture and forestry users (Austrian Landwirtschaftskammer announcement). Since Liechtenstein has an active farming sector (wine, dairy, livestock), this may be relevant to Liechtenstein farmers with Austrian APOS accounts.
- **EPOSA**: Operated by Energie Steiermark Technik GmbH for a consortium of Austrian states and Vorarlberg specifically. Coverage extends 80 km across borders by design to serve cross-border users in Liechtenstein, German Bavaria, and beyond.
- **Hobbyist note**: A Liechtenstein-based hobbyist should use swipos-GIS/GEO as the primary service. Pay-per-use at CHF 0.50/minute (no subscription) is the lowest-commitment entry point. Galileo HAS (free satellite-broadcast, ~40 cm) is a zero-cost fallback.

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
