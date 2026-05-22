# Grenada [GD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: No national caster — EarthScope NOTA single station (CN46, Carriacou)

| Field | Value |
|---|---|
| National NTRIP RTK caster | No |
| Public scientific caster in GD | EarthScope NOTA — `ntrip.earthscope.org:2101` |
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://www.earthscope.org/data/gnss-realtime/ (sign-up flow + license terms on same page) |
| host:port | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX), port 2108 (PPP) |
| num_stations | 1 — CN46_RTCM3P3, Mount Pleasant, Carriacou (12.49, -61.43) — Grenada dependency, ~36 km north of the main island's nearest tip and ~60 km north of St. George's |
| vrs | No — raw 1 Hz multi-constellation RTCM 3.3 MSM7 single-base |
| tariff — noncommercial | Free (USD $0.00 / XCD $0.00); EarthScope account + annual NULA acceptance required. Observed 2026-05-22. Source: https://www.earthscope.org/data/gnss-realtime/ |
| tariff — commercial | USD $1,000 / XCD ~$2,700 per seat per year (XCD fixed peg 1 USD = 2.70 XCD). EarthScope is a US 501(c)(3) nonprofit; no VAT. Observed 2026-05-22. |
| hobbyist_eligibility | Yes — NULA accepts individuals (scientific / educational / humanitarian) |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-22 — `data/earthscope.sourcetable` refreshed 2026-05-21 (source_health ok), CN46_RTCM3P3 line 143 (country GRD) |
| datum_epoch | ITRF2014; NOTA epoch 2026-03-30 — operator-declared at https://www.earthscope.org/data/gnss-realtime/ ("All raw data streams use the ITRF2014 reference frame"; "For NOTA stations, the epoch date is 2026-03-30"). Cited 2026-05-22. |

## EarthScope CN46 — Carriacou

Single-base RTCM 3.3 stream at Mount Pleasant, Carriacou. Distances to Grenada main island (probed 2026-05-22): ~36 km to the nearest northern tip, ~60 km to St. George's. Both baselines are well beyond reliable single-base cm-grade RTK range (~20–30 km on dual-frequency hardware) — CN46 is useful for cm work on Carriacou and Petite Martinique only; users on the main island need a local base for cm-grade fixes.

Legacy platform: `rtgpsout.unavco.org` retired 2025-07-29; CN46 now on `ntrip.earthscope.org`.

## Volunteer / commercial overlay (2026-05-22)

Zero GD mountpoints on rtk2go, Centipede, GEODNET, ONOCOY. EarthScope is the only public stream.

## National authority + recent projects

No GD-government NTRIP/CORS service. The 2019–2022 World Bank / Fugro LiDAR + aerial survey (national GIS / digital twin) had no CORS component. The 2022 World Bank OECS Data for Decision Making Project (Grenada / Saint Lucia / Saint Vincent) funded GIS capacity but no GNSS CORS. No OECS or CARICOM geodetic CORS/NTRIP project for Grenada identified 2024–2026.

## Sources
- EarthScope GNSS realtime: https://www.earthscope.org/data/gnss-realtime/ (WebFetch 2026-05-22 — `ntrip.earthscope.org:2101`, ITRF2014, NOTA epoch 2026-03-30, $1,000/seat/yr commercial, free noncommercial)
- EarthScope commercial announcement (2024-03-07): https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- Grenada digital twin (LiDAR project, no CORS): https://www.esri.com/about/newsroom/blog/grenada-digital-twin-climate-change
- World Bank OECS Data for Decision Making Project: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/
- Local pipeline 2026-05-22: `data/earthscope.sourcetable` line 143; `stations_by_country.py GRD` returns CN46_RTCM3P3; rtk2go + centipede return zero GD
