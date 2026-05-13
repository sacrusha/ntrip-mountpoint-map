# Cayman Islands [KY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06; verified + caymanlandinfo subscription tiers added 2026-05-12

## Status: YES — RTK subscription service exists; price not on public page (mapping-tier subscriptions are listed but do not include RTK)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (subscription-only via Lands & Survey Department; surveyor-oriented) |
| **host:port** | not publicly published — contact Chief Surveyor: landsurv.info@gov.ky · +1 345-244-3420 |
| **tariff** | RTK price not on public pages; subscription terms issued via Chief Surveyor. The four caymanlandinfo.ky data-portal tiers (**Bronze KYD 3 300 / yr, Silver KYD 4 950, Gold KYD 7 150, Platinum KYD 12 100**, observed 2026-05-12) are **mapping-only** (parcels, aerial imagery, Land Registers, etc.) and do not include CORS RTK access. |
| **hobbyist_eligibility** | Unclear — geodetic-system page describes the service as for "RTK surveying" without specifying licensed-surveyor restriction; hobbyist access not addressed. |
| **legal_residency_required** | Unclear; no restriction stated on public pages. RTK pricing tier presumably issued in KYD and payable via Cayman bank account. |
| **last_confirmed_alive** | 2026-05-12 — caymanlandinfo.ky/services/survey/geodetic-system HTTPS 200; pricing page HTTPS 200 with four tiers listed. |

## Most Recent Project Announcement

No fresh CORS-specific announcement located. The 4-station CORS network (one each on Cayman Brac and Little Cayman, two on Grand Cayman; previously documented as **CBMD, LCSB, GCFS, GCEA**) operates on the **CIGD11** datum (each island also has a distinct local vertical reference); seven-parameter transformation + UTM Zone 17N projection parameters are published on caymanlandinfo.ky. Subscription RTK access is administered by the Lands & Survey Department.

**Cayman Land Info digital upgrade** (caymanindependent.com 2024–2025) — the cayman​landinfo portal is undergoing a major refresh with new subscription tiers (Bronze / Silver / Gold / Platinum) at beta.caymanlandinfo.ky and new.caymanlandinfo.ky. These tiers are for digital mapping/registry access, not RTK corrections.

## Context Notes

- **Lands & Survey Department CORS**: 4 stations — CBMD, LCSB, GCFS, GCEA — on the CIGD11 / ITRF2005 datum.
- **Real-time RTK**: Available as a subscription via the Chief Surveyor. Host:port and pricing not on public pages. Contact: landsurv.info@gov.ky · +1 345-244-3420. Page confirms service exists but gives no credentials, mount points, or tariff.
- **RINEX post-processing**: Free for download from the Department.
- **No public NTRIP endpoint** is published; access path runs through the Chief Surveyor's office.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede-RTK): no Cayman coverage confirmed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **L&S Department CORS RINEX** — confirmed free per geodetic-system page; no direct download link published; contact landsurv.info@gov.ky | https://www.caymanlandinfo.ky/services/survey/geodetic-system | Free |

## Sources Consulted
- Cayman Islands Lands & Survey — Survey section: https://www.caymanlandinfo.ky/About-Us/Lands-and-Survey-Sections/Survey
- Cayman Islands Lands & Survey — Geodetic System page (CORS, CIGD11, RTK subscription): https://www.caymanlandinfo.ky/services/survey/geodetic-system (HTTPS 200 2026-05-12)
- caymanlandinfo.ky/subscription/pricing — four-tier mapping subscription pricing (HTTPS 200 2026-05-12; Bronze 3 300 / Silver 4 950 / Gold 7 150 / Platinum 12 100 KYD per year)
- Cayman Independent — "Cayman Land Info to undergo major digital upgrade" (2024–2025)
- Cayman Land Registry portal: https://www.caymanlandinfo.ky/
- NTRIP-list.com Caribbean: https://ntrip-list.com/
- GEODNET coverage map: https://geodnet.com/ (no KY coverage)
- stations.json 2026-05-12: 0 KY stations from any tracked source (rtk2go / centipede / earthscope)
