# Norway [NO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid government NTRIP caster (CPOS, Kartverket) operating; no free hobbyist tier

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (CPOS — paid) |
| **host:port — CPOS** | `159.162.103.14:2101` |
| **VRS** | Yes — VRS is the primary delivery method; system calculates a virtual reference station near the user's position from 280+ permanent geodetic stations nationwide |
| **tariff — CPOS Standard (Surveying)** | NOK 11,000 /yr excl. VAT (1–3 subscriptions); NOK 8,000 /yr excl. VAT (4th+ subscription) · (source: Kartverket price list, observed 2026-05-06) |
| **tariff — CPOS Fast (Fixed Installation)** | NOK 8,000 /yr excl. VAT |
| **tariff — CPOS Landbruk (Agriculture)** | NOK 5,000 /yr excl. VAT |
| **tariff — CPOS Undervisning (Teaching)** | Free (for accredited educational institutions) |
| **tariff — CPOS Forskning (Research)** | Free for approved research organisations (Research Council-approved); max 2-year term |
| **tariff — CPOS Innovasjon (Innovation)** | Free for startups in pre-commercial phase; max 1-year term |
| **tariff — CPOS test** | Free 1-month trial for new customers |
| **hobbyist_eligibility** | unclear — no explicit hobbyist tier; subscriptions appear business/organisation-oriented; no explicit block on individuals; 1-month free trial available |
| **legal_residency_required** | unclear — not explicitly stated; billing address required; no residency restriction found in public terms |
| **last_confirmed_alive** | `159.162.103.14:2101` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl verified) |

## Context Notes

- **CPOS** (Continuously Operating Positioning Service): Operated by Kartverket (Norwegian Mapping Authority). ~280 permanent geodetic stations covering mainland Norway. ~5,000 active users. 24/7 operation with weekday monitoring. Coverage is mainland Norway only — Svalbard and Jan Mayen are explicitly excluded (see SJ_Svalbard entry for details).
- **Subscription types**: CPOS Standard is the main commercial offering. CPOS Fast is for fixed/mobile installations (excavators, drones). CPOS Landbruk targets precision agriculture at a lower price point. Drone operators sourced this at ~NOK 7,980 /yr via resellers (e.g., Scandinavian Drone).
- **ETPOS included**: All CPOS subscriptions include ETPOS (post-processing correction service).
- **Nordic interoperability**: Existing CPOS subscribers can add SWEPOS (Sweden) access for NOK 5,000/yr on the same username.
- **No free public tier**: Hobbyists must pay at minimum CPOS Landbruk (NOK 5,000/yr) or use the 1-month free trial. No ongoing free access for private individuals.
- **Volunteer coverage**: rtk2go hosts ~29 Norwegian bases; Centipede has minimal Norwegian presence. Volunteer coverage is adequate south of ~63°N but sparse further north.
- **Operator contact**: kundesenter@kartverket.no / +47 32 11 80 00

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ETPOS** — post-processing; included with any CPOS subscription | https://www.kartverket.no/en/on-land/posisjon/guide-to-etpos | With CPOS subscription |
| **EUREF Permanent Network** — selected Norwegian CORS (ETRF89) | https://epncb.oma.be/ | Free |

## Sources Consulted
- Kartverket CPOS guide: https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos
- Kartverket price list for positioning services: https://www.kartverket.no/en/on-land/posisjon/price-list-for-positioning-services
- Kartverket ordering page: https://www.kartverket.no/en/on-land/posisjon/ordering-positioning-services
- Kartverket user guide: https://www.kartverket.no/en/on-land/posisjon/user-guide-positioning-services
- Scandinavian Drone CPOS subscription listing (~NOK 7,980): https://www.scandinaviandrone.no/produkt/kartverket-cpos-abonnement-for-droner/
- ArduSimple Norway RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-norway/
- curl probe of `159.162.103.14:2101` — SOURCETABLE 200 OK confirmed 2026-05-06
