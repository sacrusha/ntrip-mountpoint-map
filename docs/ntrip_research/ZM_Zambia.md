# Zambia [ZM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (re-verification of 2026-05-06 baseline)

## Status: NO public NTRIP caster — CORS exists (ZAMB / IGS) but RINEX-only; no change since 2026-05-06

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | None found |
| **tariff** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster identified; stations_by_radius.py -15.41 28.28 200 (Lusaka) returns zero results across rtk2go/centipede/earthscope sourcetables on 2026-05-13 |

## Most Recent Project Announcement

No NTRIP service launch or CORS expansion announcement found for Zambia as of 2026-05-13. Repeat WebSearch ("Zambia Survey Department CORS NTRIP RTK GNSS 2025 2026") on 2026-05-13 returned only generic global RTK content; nothing Zambia-specific. The Zambia Survey Department (ZSD), under the Ministry of Lands and Natural Resources, participates in the AFREF/SAFREF continental geodetic reference framework. IGS station ZAMB (Lusaka) archives RINEX data to HartRAO but does not stream real-time NTRIP corrections.

## Context Notes

- **National authority:** Zambia Survey Department (ZSD), Ministry of Lands and Natural Resources. The University of Zambia Department of Surveying (UNZA) has collaborated with ZSD and HartRAO on geodetic infrastructure.
- **ZAMB — IGS station, Lusaka:** An IGS-class GNSS receiver was installed at the Zambia Survey Department in Lusaka under the Space Geodesy Programme of HartRAO (Hartebeesthoek Radio Astronomy Observatory, South Africa), in collaboration with ZSD and UNZA. ZAMB contributes 24-hour RINEX files to HartRAO's regional data centre and to the RCMRD AFREF archive. Data is available via IGS/EarthScope download; no NTRIP real-time stream has been documented. → networks.md: no entry yet (RINEX-only, out of scope)
- **SAFREF participation:** Zambia is within the SAFREF (Southern Africa Geodetic Reference Frame) scope alongside Botswana, Lesotho, Malawi, Namibia, South Africa, Swaziland, and Zimbabwe. SAFREF focuses on geodetic reference realisation, not NTRIP services.
- **AFREF status:** Zambia is listed among countries that have established at least one operational CORS contributing to AFREF's Operational Data Centre (~22 countries as of 2024). However, AFREF CORS stations are geodetic-grade RINEX archives, not RTK/NTRIP streaming services.
- **No entries on rtk2go or Centipede:** Zero ZM mountpoints in either public sourcetable.
- **No entry on ntrip-list.com:** Zambia absent from ntrip-list.com Africa listing.
- **No commercial NTRIP providers found:** GEODNET, ONOCOY, PointOne, HxGN SmartNet — none list Zambia coverage. No Zambia-based commercial NTRIP provider found.
- **Regional context:** Neighbouring Zimbabwe has ZINGSA CORS (gated, contact required). Tanzania has a partially functional CORS (TanRef) — endpoint not publicly confirmed. No cross-border RTK coverage applicable to Zambia.
- **Practical hobbyist guidance:** Deploy a local GNSS base station for single-base RTK; use Galileo HAS / PPP for sub-metre work. EarthScope RINEX download is available for post-processing.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **ZAMB (Lusaka) RINEX — HartRAO data centre** — IGS station at Zambia Survey Dept; daily RINEX archives | https://geodesy.hartrao.ac.za/site/en/data-and-products/gnss.html | Free (account/request basis) |
| **RCMRD AFREF archive** — AFREF-contributed RINEX; Zambia station(s) included | https://www.rcmrd.org/ | Unknown; contact RCMRD |
| **EarthScope / IGS RINEX archive** — global IGS station RINEX download; ZAMB may be accessible | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

## Negative Findings

- rtk2go monitor: zero ZM mountpoints
- Centipede: zero ZM nodes
- ntrip-list.com/africa: no Zambia entry
- GEODNET, ONOCOY, PointOne, HxGN SmartNet: no Zambia coverage
- No Zambia-specific NTRIP caster address found in any academic paper, government publication, or vendor page as of 2026-05-06

## Sources Consulted
- HartRAO — IGS station in Zambia: http://www.hartrao.ac.za/geodesy/THEIGSST.htm
- HartRAO GNSS data centre: https://geodesy.hartrao.ac.za/site/en/data-and-products/gnss.html
- HartRAO / SARAO geodata programme: https://www.sarao.ac.za/about/hartrao/hartrao-research-programmes/hartrao-geodata/
- AFREF station map / CORS status (GIM International): https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- AFREF newsletter No. 6 (RCMRD): https://rcmrd.org/images/AFREF-Newslettes/6-AFREF-Newsletter-No.-6A.pdf
- AFREF background (UN-SPIDER): https://un-spider.org/space-application/space-application-matrix/african-geodetic-reference-frame-afref
- AFREF workshop 2024 (RCMRD): https://ric2024.rcmrd.org/afref
- ntrip-list.com Africa: https://ntrip-list.com/africa/
- rtk2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- ArduSimple RTK in South Africa (regional context): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-south-africa/
