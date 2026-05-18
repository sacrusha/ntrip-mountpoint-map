# Cayman Islands [KY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06; reverified 2026-05-17 (geodetic-system + pricing pages still HTTPS 200; CIGD11 / ITRF05(2011.0) datum-epoch operator-cited; KYD tier prices unchanged)

## Status: YES — RTK subscription service exists; price not on public page (mapping-tier subscriptions are listed but do not include RTK)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (subscription-only via Lands & Survey Department; surveyor-oriented) |
| **landing_url** | https://www.caymanlandinfo.ky/services/survey/geodetic-system (operator-owned Lands & Survey geodetic-system page; CORS + CIGD11 + RTK subscription) |
| **access_url** | https://www.caymanlandinfo.ky/subscription/pricing (distinct subscription pricing page — though tiers listed are mapping-only; RTK terms still issued via Chief Surveyor contact) |
| **num_stations** | 4 physical CORS — CBMD (Cayman Brac), LCSB (Little Cayman), GCFS + GCEA (two on Grand Cayman). Operator figure per caymanlandinfo.ky geodetic-system page. |
| **vrs** | ? — Lands & Survey page describes "RTK surveying" but does not state VRS / single-base / network solution; unverified. With 4 stations across 3 islands the practical mode is likely single-base, but unconfirmed. |
| **host:port** | not publicly published — contact Chief Surveyor: landsurv.info@gov.ky · +1 345-244-3420 |
| **tariff** | RTK price not on public pages; subscription terms issued via Chief Surveyor. The four caymanlandinfo.ky data-portal tiers (**Bronze KYD 3 300 / yr, Silver KYD 4 950, Gold KYD 7 150, Platinum KYD 12 100**, observed 2026-05-12) are **mapping-only** (parcels, aerial imagery, Land Registers, etc.) and do not include CORS RTK access. |
| **hobbyist_eligibility** | Unclear — geodetic-system page describes the service as for "RTK surveying" without specifying licensed-surveyor restriction; hobbyist access not addressed. |
| **legal_residency_required** | Unclear; no restriction stated on public pages. RTK pricing tier presumably issued in KYD and payable via Cayman bank account. |
| **last_confirmed_alive** | 2026-05-17 — caymanlandinfo.ky/services/survey/geodetic-system WebFetch HTTPS 200; pricing page HTTPS 200 with four tiers unchanged (Bronze 3,300 / Silver 4,950 / Gold 7,150 / Platinum 12,100 KYD per year). |
| **datum_epoch** | CIGD11 -- "CIGD11 is based on ITRF05(2011.0) positions" -- operator-declared on caymanlandinfo.ky geodetic-system page (cited 2026-05-17). Citation: https://www.caymanlandinfo.ky/services/survey/geodetic-system |

## Most Recent Project Announcement

No fresh CORS-specific announcement located. The 4-station CORS network (Cayman Brac **CBMD**, Little Cayman **LCSB**, Grand Cayman **GCFS** + **GCEA**) operates on **CIGD11** = ITRF05(2011.0) (operator declaration; each island also has a distinct local vertical reference); seven-parameter transformation + UTM Zone 17N projection parameters are published on caymanlandinfo.ky. Subscription RTK access is administered by the Lands & Survey Department.

**Cayman Land Info digital upgrade** (caymanindependent.com 2024–2025) — the cayman​landinfo portal is undergoing a major refresh with new subscription tiers (Bronze / Silver / Gold / Platinum) at beta.caymanlandinfo.ky and new.caymanlandinfo.ky. These tiers are for digital mapping/registry access, not RTK corrections.

## Context Notes

- **Lands & Survey Department CORS**: 4 stations — CBMD, LCSB, GCFS, GCEA — on the CIGD11 datum, realised as ITRF05(2011.0) per operator declaration on the geodetic-system page (WebFetch 2026-05-17).
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
- stations.json 2026-05-17: `py scripts/stations_by_country.py CYM` → no stations from any tracked source; `stations_by_radius.py 19.31 -81.25 200` → 0 hits
