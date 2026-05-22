# Barbados [BB] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: NO public NTRIP RTK caster

No national caster, no public scientific caster, no volunteer base in Barbados. Nearest free streams are EarthScope NOTA on Saint Lucia and Grenada at >150 km — outside reliable single-base RTK range. Only practical cm-grade path on the island is a private base + rover.

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | No |
| landing_url | n/a |
| access_url | n/a |
| host:port | n/a |
| tariff | n/a |
| num_stations | 0 |
| vrs | n/a |
| hobbyist_eligibility | n/a |
| legal_residency_required | n/a |
| last_confirmed_alive | n/a |
| datum_epoch | omitted — no caster to declare |

## National surveying authority

The **Lands and Surveys Department** (Ministry of Housing, Lands and Maintenance), `landsandsurveys.gov.bb`, is the geodetic authority. Stated remit is the Barbados National Grid and Lamont Datum. No NTRIP / CORS / RTK service published or announced (WebFetch 2026-05-22 — landing page lists surveying, mapping, recording, GIS; no GNSS infrastructure). The **Barbados Geoportal** (ArcGIS Hub) hosts vector/raster only. No 2024–2026 World Bank, CDB, or donor project mentions a Barbados GNSS reference network.

## Historical context

NOAA CORS **BDOS** (2005-06-05 → 2013-12-12) decommissioned. Never replaced. COCONet expansion 2013–2014 installed Saint Lucia / Grenada / Martinique sites but skipped Barbados.

## Nearest free RTK streams (cross-border, beyond reliable single-base range)

| Mountpoint | Network | Country | Distance from Bridgetown |
|---|---|---|---|
| CN47_RTCM3P3 | EarthScope NOTA | Saint Lucia (LCA) | ~158 km |
| CN04_RTCM3P3 | EarthScope NOTA | Saint Lucia (LCA) | ~178 km |
| CN46_RTCM3P3 | EarthScope NOTA | Grenada (GRD) | ~208 km |
| LMMF00MTQ0 | AUSCORS / IGS / MIRAI (same physical antenna, 3 rebroadcasts) | Martinique (MTQ) | ~223 km |
| DEPZ | Centipede | Martinique (MTQ) | ~249 km |

Confirmed 2026-05-22 via `py scripts/stations_by_radius.py 13.10 -59.62 250` — 7 hits across 5 sources, but only 5 distinct physical antennas (LMMF Le Lamentin Martinique is republished by AUSCORS, IGS, and MIRAI). All >150 km. RTK accuracy degrades to dm/m at these baselines (silent extrapolation outside hull). Useful for PPK or DGNSS post-processing only.

## Sources
- Lands and Surveys Department: https://landsandsurveys.gov.bb/ (WebFetch 2026-05-22 — no GNSS/CORS/NTRIP mention)
- NGS All CORS Sites — BDOS decommissioned: https://www.ngs.noaa.gov/CORS/sort_sites.shtml
- Local pipeline: `py scripts/stations_by_country.py BRB` → no stations; `stations_by_radius.py 13.10 -59.62 250` → 7 cross-border hits, none in BRB
