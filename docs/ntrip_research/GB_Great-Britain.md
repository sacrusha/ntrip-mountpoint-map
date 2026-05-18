# Great Britain [GB] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-12 entry; SCCS SmartNet tariff unchanged on WebFetch; Drone Pilot Academy TopNet Live page still shows £100–£1,900 +VAT bracket range with same tier list; Korec VRS Now still £POA)

## Status: YES — multiple commercial NTRIP casters operating via OS Net reseller partners; no free public caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (commercial, via OS Net licensed resellers) |
| **Infrastructure** | OS Net — 110–120 CORS base stations across Great Britain, operated by Ordnance Survey (sources cluster 110–115; "~120" is the headline figure on OS marketing pages — range carried with downgrade note) |
| **num_stations** | 110–120 (downgraded from prior "~120"; OS Net overview page advertises "around 120", historical published counts and reseller pages cluster 110–115) |
| **landing_url — OS Net** | https://www.ordnancesurvey.co.uk/geodesy-positioning/os-net (operator-owned overview + reseller list) |
| **access_url — OS Net** | https://www.ordnancesurvey.co.uk/geodesy-positioning/os-net (same page — OS does not sell direct; routes to authorised reseller list) |
| **Direct OS Net subscriptions** | Not sold by Ordnance Survey directly; access is via 7 authorised resellers |
| **VRS** | Yes (all major resellers offer Network RTK / VRS) |
| **datum_epoch** | omitted — no citable declaration on an OS Net operator URL retrievable this pass. ETRS89 (with OSGB36 mapping projection via OSTN15 / OSGM15 transformation) is universally documented for OS Net by OS and third-party sources, but a direct datum/epoch declaration on an os.uk operator page (with epoch year) has not been verified this pass; defer rather than infer. |
| **hobbyist_eligibility** | Yes (TopNet Live, HxGN SmartNet via SCCS — no surveying licence required) |
| **legal_residency_required** | No (verified on Partner 1 SCCS SmartNet and Partner 3 Drone Pilot Academy TopNet Live product pages); for Partners 2–7 this is **carry-forward from the OS-Net-export-friendly default**, not individually re-verified per reseller this pass |
| **last_confirmed_alive** | 2026-05-12 (reseller product pages active and selling licences) |
| **Volunteer fallback** | rtk2go: 60 GBR-coded volunteer bases on 2026-05-12 (data/stations.json); Centipede: 45 `ENG`-coded bases on 2026-05-12 (crtk.net:2101 sourcetable). **`ENG` is Centipede's non-ISO label for the entire UK** — the 45 nodes cover England *plus* Scotland (e.g. BALL, BRACO, CRAG, DRUM, FRAS, HRVA, LARL, MLLC, TYRI, WOCF, CHAP, FHL1), Northern Ireland (DJAM, DYFM, GWMD, OATS), and Wales (PEMBS). See `_centipede_country_codes.md`. |

## Reseller Tariffs

### Partner 1 — Leica HxGN SmartNet (via SCCS Survey)
- **landing_url**: https://www.sccssurvey.co.uk/leica-smartnet.html (reseller product page)
- **access_url**: https://www.sccssurvey.co.uk/leica-smartnet.html (same — sale + tariff disclosed inline)

Source: sccssurvey.co.uk/leica-smartnet.html, observed 2026-05-12 (unchanged since 2026-04-30). All prices **include** 20% UK VAT.

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
- **landing_url**: https://www.korecgroup.com/product/trimble-vrs-now/ (reseller product page)
- **access_url**: https://www.korecgroup.com/product/trimble-vrs-now/ (POA — contact form on same page)

Source: korecgroup.com/product/trimble-vrs-now/, observed 2026-05-12 (still £POA, unchanged).

- tariff: **£POA** (Price On Application) — no public tariff published for GB.
- Korec contacts: +44 (0)345 603 1214 (UK Sales), +353 (0)1 456 4702 (Ireland).
- Market estimates from forum data (2020): annual costs of £600–£2,600/yr for formal UK NTRIP; Trimble VRS Now likely falls in that range but no current public GB figure is confirmed.
- hobbyist_eligibility: **unclear** — Korec primarily markets to survey/construction professionals but states no formal restrictions.
- legal_residency_required: **no** — UK + Ireland coverage, international exports available.

### Partner 3 — Topcon TopNet Live (via Drone Pilot Academy)
- **landing_url**: https://www.dronepilotacademy.co.uk/product/topnet-live-vrs-license/ (reseller product page)
- **access_url**: https://www.dronepilotacademy.co.uk/product/topnet-live-vrs-license/ (same — buy + tier dropdown inline)

Source: dronepilotacademy.co.uk/product/topnet-live-vrs-license/, observed 2026-05-12. Prices are **ex VAT** (20% UK VAT applicable). Powered by OS Net data.

Published price range on the product page: **£100 – £1,900 (+VAT)**. Tier list (since 2026-04-30 the line-up has grown with new 51hr/50hr/26hr/25hr brackets; the unlimited annual headline price now reaches £1,900 ex VAT vs the prior £1,700):

| Solution | Tier name on page |
|---|---|
| Unlimited annual | Topcon Unlimited usage annual VRS licence |
| 600 hrs annual | Topcon limited usage annual VRS licence (600 hrs) |
| 51 hrs annual — new customer | Topcon 51 Hours VRS licence (New customer) |
| 50 hrs annual — existing customer | Topcon 50 Hours VRS licence (Existing customer) |
| 26 hrs annual — new customer | Topcon 26 Hours VRS licence (New customer) |
| 25 hrs annual — existing customer | Topcon 25 Hours VRS licence (Existing customer) |
| 11 hrs annual — new customer | Topcon 11 Hours VRS licence (New customer) |
| 10 hrs annual — existing customer | Topcon 10 Hours VRS licence (Existing customer) |
| 6 hrs annual — new customer | Topcon 6 Hours VRS licence (New customer) |
| 5 hrs annual — existing customer | Topcon 5 Hours VRS licence (Existing customer) |

Individual tier prices are presented on the live page via a dropdown selector (and a `VRS-Pricelist.jpg` image asset); the published headline range is £100 (entry-level hourly) to £1,900 (unlimited annual). For exact per-tier prices, see the live product page. Optional SIM card add-ons remain available (EE data SIM, roaming multi-network SIM, no-SIM).

- hobbyist_eligibility: **yes** — marketed explicitly to drone pilots, hobbyists, and agricultural users; no professional licence required.
- legal_residency_required: **no** — no residency restriction stated.

### Partners 4–7 — FarmRTK, EssentialsNet, RTK Premium, Polaris

**Status: work remaining, not resolved this pass.** Listed on the OS Net authorised-resellers page but tariff, landing_url, access_url, hobbyist_eligibility, legal_residency_required, and last_confirmed_alive have **not** been individually researched / re-verified. Treat as an explicit open todo, not as silently-incomplete data:

- **FarmRTK** (AXIO-NET) — agricultural focus. landing_url / tariff: not researched.
- **EssentialsNet** (SoilEssentials) — agricultural focus. landing_url / tariff: not researched.
- **RTK Premium** (Premium Positioning) — pan-European service including UK. landing_url / tariff: not researched.
- **Polaris** (Point One Navigation) — global service including UK via OS Net. landing_url / tariff: not researched.

Per-partner hobbyist_eligibility and legal_residency_required are likewise carry-forward defaults inherited from the OS-Net-reseller-pool overview, **not** individually confirmed against each of these four partner product pages this pass.

## Context Notes

- OS Net was established by Ordnance Survey and consists of approximately 120 continuously operating reference stations (CORS) across Great Britain (England, Scotland, Wales). Northern Ireland is not covered by OS Net (covered separately by OSi/Tailte Éireann infrastructure or reseller extension).
- All resellers provide Network RTK corrections (VRS, MAX, iMAX, or equivalent). Single-base RTK is not the primary product.
- No free public NTRIP caster exists for Great Britain. OS Net data are not streamed publicly.
- Global commercial services with GB coverage: GEODNET (coverage varies), Trimble RTX (PPP, not networkRTK).
- The market range observed is approximately £100 (entry-level hourly bracket on TopNet Live) to £2,592 (1-yr unlimited HxGN SmartNet incl. VAT).
- Volunteer fallback in GB exists at hobbyist density: rtk2go shows 60 GBR-coded bases and Centipede shows 45 `ENG`-coded bases as of 2026-05-12 — usable for individual sites but not a substitute for OS-Net-derived national NRTK. **Centipede's `ENG` code is a non-ISO label that covers the entire UK including Scotland, Wales, and Northern Ireland** (see `_centipede_country_codes.md`); Northern Ireland in particular relies on the Centipede `ENG` nodes since OS Net itself does not cover NI.

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
- Live probe of `crtk.net:2101` (Centipede) 2026-05-12: 45 ENG-coded bases on sourcetable
- Local data/stations.json 2026-05-12: 60 rtk2go GBR-coded volunteer bases
