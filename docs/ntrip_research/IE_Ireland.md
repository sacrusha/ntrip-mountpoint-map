# Ireland [IE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-04-30 entry)

## Status: NO — no national public real-time NTRIP RTK caster; national CORS network's raw NRTK stream is wholesaled exclusively to commercial third-party operators

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — national CORS network (Tailte Éireann + OSNI) exposes only RINEX (post-processing) to end users; its NRTK raw stream is wholesaled to Trimble (VRS Now), Leica (SmartNet), and Topcon |
| **host:port** | null — no public NTRIP caster endpoint exists for the national network |
| **tariff** | null (no real-time service direct from operator) |
| **VRS** | N/A directly (commercial resellers offer VRS via NRTK wholesale) |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | 2026-05-12 — `https://gnss.osi.ie` returns HTTP 200 with redirect notice to `https://gnss.tailte.ie`; `tailte.ie/services/geodetic/` returns HTTP 200 (RINEX post-processing service; no NTRIP endpoint documented); rtk2go shows 10 IE volunteer bases; Centipede shows 8 IE bases |

## Context Notes

- **OSi → Tailte Éireann Active GNSS Network**: The legacy OSi portal at `gnss.osi.ie` now serves a redirect notice pointing to `gnss.tailte.ie` (verified 2026-05-12 — *"This website has moved to a new location. Please bookmark the new Tailte Éireann GNSS website at: https://gnss.tailte.ie"*). The Tailte Éireann geodetic service page (`tailte.ie/services/geodetic/`) confirms the offering is **hourly RINEX (30-day archive) + monitoring/coordinate-converter tools — post-processing only**. No NTRIP caster URL or real-time stream is published direct-to-user.
- **Wholesale arrangement (per Tailte Éireann + OSNI cooperative model, restated 2026)**: The raw streamed data from the national CORS network is supplied to **Trimble (VRS Now Ireland)**, **Leica (HxGN SmartNet)**, and **Topcon (TopNET Live)**, who each operate their own paid NRTK casters covering the island. There is no direct-from-government NTRIP caster.
- **ArduSimple's Ireland page** (ardusimple.com/rtk-correction-services-and-ntrip-casters-in-ireland/) explicitly states: *"as far as we know Ireland is not among"* the countries with a national free RTK network.
- **Trimble VRS Now (Ireland)** via **Hitechniques** (IE Trimble reseller, hitechniques.ie):
  - 1-year / **100h** subscription: **€980 excl. VAT** (€1,205.40 incl. 23% VAT) — observed 2026-05-12.
  - 1-year / **600h** subscription: **€1,390 excl. VAT** (€1,709.70 incl. VAT) — observed 2026-05-12.
  - The previously-noted **€590/yr/600h** tariff is stale; current pricing has moved up materially.
  - Availability: Republic of Ireland + Northern Ireland; UK/EU/US/AU available as add-ons.
- **Trimble VRS Now via Korec Group**: same product, UK + Ireland coverage; Korec IE office +353 (0)1 456 4702; pricing on application (£POA).
- **HxGN SmartNet** (Hexagon/Leica): coverage extends to Ireland through partnership/integration with the Tailte Éireann CORS feed; no dedicated Irish tariff published; contact Leica Geosystems Ireland.
- **TopNET Live** (Topcon): noted as a continuing service for former gpsemiliaromagna users and as a regional NTRIP option but no Ireland-specific public tariff found.
- **rtk2go volunteer coverage** (2026-05-12 pipeline snapshot): 10 volunteer bases in IE — BallyAgopen (Wexford), ClagganRTK (Donegal), DCU_Alpha (Dublin), Grange, MCNKILL1985, OCLB, SUBSEA_NETR5_01 (Cork), ValeduneRTK, owow, tully_engineering. Coverage is patchy and operator-dependent; free.
- **Centipede volunteer coverage** (2026-05-12 pipeline snapshot): 8 IE bases — CNIE, CRNF, CWAA, LRBC, MFUR, MOLL, TJMM, WOOD. Coverage clustered on the east coast.
- Ireland remains absent from NTRIP-list.com's Europe table for a national real-time service.

## Most Recent Project / Announcement

No announced project to deploy a public direct-to-user NTRIP RTK caster for Ireland was found as of 2026-05-12. The administrative migration `gnss.osi.ie` → `gnss.tailte.ie` (Tailte Éireann branding consolidation, originally signalled for May 2026) is **complete**: the legacy URL now displays only a static redirect notice. The migration is not a real-time service launch — it is an administrative domain change only.

## Commercial Real-Time Alternative (closest available)

| Provider | Coverage | Tariff (observed 2026-05-12) | hobbyist_eligibility |
|---|---|---|---|
| **Trimble VRS Now** via Hitechniques IE — 100h/yr | Ireland | €980 excl. VAT (~€1,205 incl. 23% VAT) | unclear — no stated ban, primarily marketed to surveyors |
| **Trimble VRS Now** via Hitechniques IE — 600h/yr | Ireland | €1,390 excl. VAT (~€1,710 incl. VAT) | same |
| **Trimble VRS Now** via Korec Group | UK + Ireland | £POA (contact +353 (0)1 456 4702) | unclear |
| **HxGN SmartNet Ireland** (Leica) | Ireland (uses Tailte Éireann feed) | Not publicly published | unclear |
| **TopNET Live** (Topcon) | EU (incl. Ireland) | EU-tier from rtk.topnetlive.com — see IT entry (~€90/mo, €360/yr +VAT; partita IVA / VAT-ID required) | No (VAT-ID required) |

## Free Volunteer Bases (rtk2go + Centipede)

| Source | IE base count | Coverage character |
|---|---|---|
| **rtk2go** | 10 (2026-05-12 pipeline) | Volunteer single-base mounts scattered nationwide; uptime not guaranteed |
| **Centipede-RTK** | 8 (2026-05-12 pipeline) | Volunteer single-base mounts, mostly east coast |

These are the only free real-time RTK options in Ireland aside from rolling your own base. No VRS/NRTK product is free.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **Tailte Éireann GNSS** — hourly RINEX (30-day archive), monitoring, coordinate conversion | https://gnss.tailte.ie / https://tailte.ie/services/geodetic/ | Free (account required) |
| **Legacy OSi portal** (now a redirect) | https://gnss.osi.ie → https://gnss.tailte.ie | n/a |

## Sources Consulted
- Tailte Éireann geodetic services: https://tailte.ie/services/geodetic/ (HTTP 200, 2026-05-12 — post-processing/RINEX only; no NTRIP/real-time service published)
- OSi legacy portal (redirect notice 2026-05-12): https://gnss.osi.ie
- New Tailte Éireann GNSS portal: https://gnss.tailte.ie (HTTP unreachable from this sandbox 2026-05-12; per OSi redirect notice + ArduSimple it is the active service URL)
- ArduSimple Ireland NTRIP guide: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-ireland/
- Hitechniques VRS Now 100h: https://hitechniques.ie/trimble-vrsnow-network-rtk-1y-100h-subscription-5 (€980 excl. VAT, 2026-05-12)
- Hitechniques VRS Now 600h: https://hitechniques.ie/trimble-vrsnow-rtk-network-1y-600h-subscription-5 (€1,390 excl. VAT, 2026-05-12)
- Korec Group VRS Now: https://www.korecgroup.com/product/trimble-vrs-now/ (£POA, IE phone +353 (0)1 456 4702)
- TU Dublin Network RTK evaluation paper: https://arrow.tudublin.ie/dsiscon/2/ (background context)
- rtk2go IE station list: 10 bases (2026-05-12 pipeline snapshot via `scripts/stations_by_country.py IRL`)
- Centipede IE station list: 8 bases (2026-05-12 pipeline snapshot via `scripts/stations_by_country.py IRL`)
- NTRIP-list Europe (Ireland absent): https://ntrip-list.com/europe/
