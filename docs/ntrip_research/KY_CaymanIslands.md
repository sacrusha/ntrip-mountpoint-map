# Cayman Islands [KY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: RTK subscription service exists (Lands & Survey Department); no published host:port, no published price, gated through Chief Surveyor

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | Yes (subscription-only; surveyor-oriented; not self-service) |
| Operator | Lands & Survey Department, Government of Cayman Islands |
| landing_url | https://www.caymanlandinfo.ky/services/survey/geodetic-system (operator-owned page describing CORS + CIGD11 + RTK subscription) |
| access_url | https://www.caymanlandinfo.ky/services/survey/geodetic-system — RTK access workflow is "contact the Chief Surveyor" (email `landsurv.info@gov.ky`, Grand Cayman +1 345-244-3420, Brac +1 345-244-3637/3639). The `subscription/pricing` page lists mapping-only tiers and does not cover RTK. |
| num_stations | 4 physical CORS — **CBMD** (Cayman Brac), **LCSB** (Little Cayman), **GCFS** + **GCEA** (Grand Cayman). Operator figure on the geodetic-system page. |
| vrs | ? — geodetic-system page describes "RTK surveying" without stating VRS / single-base / network solution. With 4 stations across 3 islands and inter-island gaps >100 km, the practical mode is likely single-base per-island, but unconfirmed. |
| host:port | not publicly published — issued via Chief Surveyor |
| tariff | RTK price not on public pages. The four `caymanlandinfo.ky/subscription/pricing` tiers (Bronze KYD 3,300 / Silver 4,950 / Gold 7,150 / Platinum 12,100 per year, observed 2026-05-22) are **mapping/registry-only** and do not include CORS RTK access. RTK tariff issued post-contact. |
| hobbyist_eligibility | ? — geodetic-system page describes service for "RTK surveying" without specifying surveyor-licence restriction; hobbyist access not addressed |
| legal_residency_required | ? — no restriction stated on public pages |
| last_confirmed_alive | 2026-05-22 — caymanlandinfo.ky/services/survey/geodetic-system WebFetch HTTP 200 (4 stations + CIGD11 + RTK subscription text confirmed); pricing page HTTP 200 with 4 mapping tiers unchanged |
| datum_epoch | **CIGD11 = ITRF05(2011.0)** — operator-declared on caymanlandinfo.ky geodetic-system page: "CIGD11 is based on ITRF05(2011.0) positions". Local datums vary by island (GCGD59 Grand Cayman; SIGD61 Sister Islands). Cited 2026-05-22. |

## Lands & Survey CORS network

4 physical CORS:
- **CBMD** (Cayman Brac)
- **LCSB** (Little Cayman)
- **GCFS**, **GCEA** (Grand Cayman, 2 stations)

Per the geodetic-system page: real-time RTK corrections are available "as a subscription package"; RINEX archive is free; subscription terms issued via the Chief Surveyor. No NTRIP mountpoint list, no host:port, and no RTK tariff are on public pages. Cayman Land Info portal upgrade 2024–2025 (beta.caymanlandinfo.ky, new.caymanlandinfo.ky) refreshed the mapping/registry tiers above — no RTK pricing added.

Seven-parameter transformation + UTM Zone 17N projection parameters between CIGD11 and the legacy island datums (GCGD59 Grand Cayman; SIGD61 Sister Islands) are published on caymanlandinfo.ky.

## Volunteer / commercial overlay (2026-05-22)

Zero KY mountpoints on rtk2go, Centipede, GEODNET, ONOCOY. `stations_by_country.py CYM` → no stations; `stations_by_radius.py 19.31 -81.25 250` → no stations within 250 km. The Lands & Survey CORS is the only known RTK option.

## Sources
- Cayman Islands Lands & Survey — Geodetic System page: https://www.caymanlandinfo.ky/services/survey/geodetic-system (WebFetch 2026-05-22 — CBMD/LCSB/GCFS/GCEA listed; "CIGD11 is based on ITRF05(2011.0) positions"; "Real time corrections for RTK surveying are available as a subscription package"; "For more information on subscribing for real time corrections, please contact the Chief Surveyor")
- Cayman Land Info subscription pricing: https://www.caymanlandinfo.ky/subscription/pricing (WebFetch 2026-05-22 — Bronze $3,300 / Silver $4,950 / Gold $7,150 / Platinum $12,100 per year; **no RTK/NTRIP/GNSS/CORS service in any tier**)
- Cayman Islands Lands & Survey — Survey section: https://www.caymanlandinfo.ky/About-Us/Lands-and-Survey-Sections/Survey
- Cayman Independent — "Cayman Land Info to undergo major digital upgrade" (2024–2025): https://caymanindependent.com/cayman-land-info-to-undergo-major-digital-upgrade/
- Local pipeline 2026-05-22: `stations_by_country.py CYM` → no stations; `stations_by_radius.py 19.31 -81.25 250` → 0 hits
