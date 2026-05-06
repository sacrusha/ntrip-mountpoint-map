# Ireland [IE] — NTRIP RTK Caster Research
**Date researched:** 2026-04-30

## Status: NO — no national public real-time NTRIP RTK caster; CORS network is post-processing only

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — national CORS network (OSi / Tailte Éireann) is post-processing only |
| **host:port** | null — no NTRIP caster endpoint exists for the national network |
| **tariff** | null (no real-time service to price) |
| **VRS** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | gnss.osi.ie accessible on 2026-04-30 (RINEX post-processing service only; migration notice to gnss.tailte.ie displayed for May 2026) |

## Context Notes

- **OSi Active GNSS Network** (gnss.osi.ie, migrating to gnss.tailte.ie in May 2026): Operated by Tailte Éireann (formerly Ordnance Survey Ireland). Provides **RINEX data downloads only** for post-processing — hourly RINEX files, free of charge (account required). No NTRIP caster endpoint has ever been publicly documented for this network.
- ArduSimple's Ireland NTRIP guide (ardusimple.com/rtk-correction-services-and-ntrip-casters-in-ireland/, observed 2026-04-30) explicitly states: *"as far as we know Ireland is not among"* the countries with a national RTK network.
- Real-time NTRIP RTK in Ireland is served commercially by **Trimble VRS Now** (via Korec Group, which covers both UK and Ireland — contact +353 (0)1 456 4702). **Hitechniques** (IE reseller, hitechniques.ie) published a 1-year / 600-hour VRS Now subscription for **€590** (observed 2026-04-30); this is the closest available "Irish" real-time RTK subscription, though it is a commercial third-party service, not a national one.
- **HxGN SmartNet** (Hexagon/Leica) may also cover parts of Ireland via the OS Net / partner extension, but no dedicated Irish tariff was found.
- No free public NTRIP caster exists for Ireland as of 2026-04-30. Ireland is absent from NTRIP-list.com's Europe table for real-time services.

## Most Recent Project / Announcement

No announced project to deploy a national NTRIP RTK caster for Ireland was found as of 2026-04-30. The migration of the existing post-processing portal from gnss.osi.ie to gnss.tailte.ie (Tailte Éireann branding consolidation, scheduled May 2026) is not a real-time service launch — it is an administrative domain migration only.

## Commercial Real-Time Alternative (closest available)

| Provider | Coverage | Tariff | hobbyist_eligibility |
|---|---|---|---|
| **Trimble VRS Now** via Hitechniques IE | Ireland | €590 / yr / 600 hrs (hitechniques.ie, observed 2026-04-30) | unclear (no stated restriction, primarily marketed to surveyors) |
| **Trimble VRS Now** via Korec Group | UK + Ireland | £POA (contact Korec IE: +353 (0)1 456 4702) | unclear |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **OSi Active GNSS Network** — hourly RINEX download | https://gnss.osi.ie / migrating to https://gnss.tailte.ie | Free (account required) |
| **Tailte Éireann geodetic services** | https://www.tailte.ie/services/geodetic/ | Free (RINEX post-processing only) |

## Sources Consulted
- OSi Active GNSS Network portal: https://gnss.osi.ie
- Tailte Éireann geodetic services: https://www.tailte.ie/services/geodetic/
- ArduSimple Ireland NTRIP guide: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-ireland/
- Hitechniques VRS Now subscription: https://www.hitechniques.ie
- Korec Group VRS Now (IE): https://www.korecgroup.com/product/trimble-vrs-now/
