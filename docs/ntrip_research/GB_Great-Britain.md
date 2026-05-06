# Great Britain [GB] — NTRIP RTK Caster Research
**Date researched:** 2026-04-30

## Status: YES — multiple commercial NTRIP casters operating via OS Net reseller partners; no free public caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (commercial, via OS Net licensed resellers) |
| **Infrastructure** | OS Net — ~120 CORS base stations across Great Britain, operated by Ordnance Survey |
| **Direct OS Net subscriptions** | Not sold by Ordnance Survey directly; access is via 7 authorised resellers |
| **VRS** | Yes (all major resellers offer Network RTK / VRS) |
| **hobbyist_eligibility** | Yes (TopNet Live, HxGN SmartNet via SCCS — no surveying licence required) |
| **legal_residency_required** | No — international exports available from listed resellers |
| **last_confirmed_alive** | 2026-04-30 (reseller product pages active, confirmed selling licences) |

## Reseller Tariffs

### Partner 1 — Leica HxGN SmartNet (via SCCS Survey)
Source: sccssurvey.co.uk/leica-smartnet.html, observed 2026-04-30. All prices **include** 20% UK VAT.

| Licence | Price (incl. VAT) | Price (excl. VAT) |
|---|---|---|
| 1 yr NRTK Unlimited | £2,592 | £2,160 |
| 2 yr NRTK Unlimited | £3,828 | £3,190 |
| 3 yr NRTK Unlimited | £5,376 | £4,480 |
| 1 yr NRTK Limited (480 hrs/yr max) | £1,560 | £1,300 |
| 1 yr DGNSS Unlimited | £978 | £815 |
| 1 yr DGNSS Limited (40 hrs/month) | £588 | £490 |

- Free SmartRINEX post-processing included with all NRTK licences.
- Other SCCS resellers (e.g. MGISS) list SmartNet as "request a callback" with no published tariff.
- hobbyist_eligibility: **yes** — no surveying licence requirement mentioned; any individual can purchase directly.
- legal_residency_required: **no** — exports available.

### Partner 2 — Trimble VRS Now (via Korec Group)
Source: korecgroup.com/product/trimble-vrs-now/, observed 2026-04-30.

- tariff: **£POA** (Price On Application) — no public tariff published for GB.
- Korec contacts: +44 (0)345 603 1214 (UK Sales), +353 (0)1 456 4702 (Ireland).
- Market estimates from forum data (2020): annual costs of £600–£2,600/yr for formal UK NTRIP; Trimble VRS Now likely falls in that range but no current public GB figure is confirmed.
- hobbyist_eligibility: **unclear** — Korec primarily markets to survey/construction professionals but states no formal restrictions.
- legal_residency_required: **no** — UK + Ireland coverage, international exports available.

### Partner 3 — Topcon TopNet Live (via Drone Pilot Academy)
Source: dronepilotacademy.co.uk/product/topnet-live-vrs-license/, observed 2026-04-30. Prices are **ex VAT** (20% UK VAT applicable). Powered by OS Net data.

| Solution | Duration | Total cost (ex VAT) |
|---|---|---|
| Unlimited annual | 12 months | £1,700 |
| Limited 600 hrs annual | 12 months | £1,000 |
| Unlimited 6 months | 6 months | £1,000 |
| Unlimited 30 days | 30 days | £300 |
| Unlimited 7 days | 7 days | £100 |
| 11 hrs annual (new customer) | 12 months | £250 |
| 10 hrs annual (existing customer) | 12 months | £200 |
| 6 hrs annual (new customer) | 12 months | £150 |
| 5 hrs annual (existing customer) | 12 months | £100 |

Optional SIM card add-ons: EE data SIM £150/yr; roaming multi-network SIM £200/yr (both incl. 12-month term, annual licences only).

- hobbyist_eligibility: **yes** — marketed explicitly to drone pilots, hobbyists, and agricultural users; no professional licence required.
- legal_residency_required: **no** — no residency restriction stated.

### Partners 4–7 — FarmRTK, EssentialsNet, RTK Premium, Polaris
Listed on the OS Net authorised-resellers page but tariffs not researched in this task:
- **FarmRTK** (AXIO-NET) — agricultural focus.
- **EssentialsNet** (SoilEssentials) — agricultural focus.
- **RTK Premium** (Premium Positioning) — pan-European service including UK.
- **Polaris** (Point One Navigation) — global service including UK via OS Net.

## Context Notes

- OS Net was established by Ordnance Survey and consists of approximately 120 continuously operating reference stations (CORS) across Great Britain (England, Scotland, Wales). Northern Ireland is not covered by OS Net (covered separately by OSi/Tailte Éireann infrastructure or reseller extension).
- All resellers provide Network RTK corrections (VRS, MAX, iMAX, or equivalent). Single-base RTK is not the primary product.
- No free public NTRIP caster exists for Great Britain. OS Net data are not streamed publicly.
- Global commercial services with GB coverage: GEODNET (coverage varies), Trimble RTX (PPP, not networkRTK).
- The market range observed is approximately £100 (7-day trial, TopNet) to £2,592 (1-yr unlimited HxGN SmartNet incl. VAT), with the lowest ongoing annual subscription approximately £1,000 ex VAT (1-yr/600 hr TopNet).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **OS Net RINEX** (via NRCAN CSRS-PPP or AUSPOS) | https://www.ordnancesurvey.co.uk/geodesy-positioning/os-net | Free (coordinate download via OS Net / SmartRINEX included with some reseller licences) |
| **EUREF Permanent GNSS Network** — selected UK CORS | https://www.epncb.oma.be/ | Free non-commercial |

## Sources Consulted
- OS Net resellers page: https://www.ordnancesurvey.co.uk/geodesy-positioning/os-net
- SCCS Survey HxGN SmartNet tariff: https://www.sccssurvey.co.uk/leica-smartnet.html
- Korec Group VRS Now product page: https://www.korecgroup.com/product/trimble-vrs-now/
- Drone Pilot Academy TopNet Live: https://www.dronepilotacademy.co.uk/product/topnet-live-vrs-license/
- Ordnance Survey OS Net overview: https://www.ordnancesurvey.co.uk/geodesy-positioning/os-net
