# Macao [MO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-17)

## Status: YES — MoSRef (DSCC) active; free of charge; registration required; ITRF2005 datum cited

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — pipeline-ingested as `mosref` (data/stations.json); status `ok`. |
| **Operator** | Direcção dos Serviços de Cartografia e Cadastro (DSCC), Government of the Macao SAR. |
| **Network** | MoSRef — Macao Satellite Positioning Reference Station Service. |
| **landing_url** | https://www.dscc.gov.mo/en/reference_details/article/reference_1.html — DSCC reference-station overview |
| **access_url** | https://mosref.dscc.gov.mo/ — service portal, account signup |
| **host:port** | `mosref.dscc.gov.mo:2101` |
| **num_stations** | 4 physical CORS — FOMO (Macao Peninsula, 2002), COAL (Coloane, 2006), UMAC (Hengqin, 2016), TAGR (Taipa Grande, 2023; relocated/renamed from DSMG-2008). Plus 4 HK partner stations (HKLT, HKSL, HKMW, HKNP) under the 2013 data-sharing agreement, extending VRS over the Pearl River Delta. |
| **vrs** | Yes — single-base + Network RTK (VRS) advertised on DSCC services page. |
| **tariff** | Free — DSCC services page states "the all-weather NTRIP RTK service to public for free of charge." |
| **hobbyist_eligibility** | Yes — online registration at mosref.dscc.gov.mo; no supporting documents, no professional credential check, no Macao residency required. |
| **legal_residency_required** | No. |
| **last_confirmed_alive** | 2026-05-17 — WebFetch of mosref.dscc.gov.mo returned station catalogue (FOMO/COAL/UMAC/TAGR) and NTRIP service description; pipeline source `mosref` last fetched 2026-05-15 (status ok per data/stations.json). Direct sourcetable response over TCP/2101 not independently probed from sandbox. |
| **datum_epoch** | **ITRF2005** — declared by DSCC on the stream-side: RINEX file headers issued by MoSRef carry an ITRF2005 frame tag (operator declaration on the actual data product). The Taipa Grande (TAGR) tripoint control-point page https://www.dscc.gov.mo/en/tripoints1_details/article/T18T.html lists the same control coordinates in ITRF2005 on the International Hayford ellipsoid; DSCC operates the survey control and the caster in one frame, so the two cites form a consistent chain. Epoch not stated. |

## Recent activity
- **2023** — TAGR (Taipa Grande GNSS Reference Station) commissioned on the rebuilt Meteorological and Geophysical Bureau rooftop, replacing DSMG (2008).
- **2021** — BeiDou (BDS) added to GPS+GLONASS tracking across all four stations.
- **2016** — UMAC station added on the Hengqin Island campus.
- **2013** — DSCC + Hong Kong Lands Department joint project "Data Sharing Between Hong Kong and Macao Satellite Positioning Reference Stations" (precursor 2012 joint control survey across 3 MO + 4 HK stations).
- **2012-11** — NTRIP introduced.
- **2009** — MoSRef service launched.
- **2002** — FOMO (Mount Fortress) constructed.

## Context
- All four MoSRef stations track GPS + GLONASS + BeiDou; Galileo reception not confirmed in public documentation. Receivers: Leica GR50. Recording 10 s. RINEX v3.02.
- Services (all free): DGPS, single-base RTK, NRTK (VRS), RINEX download up to 3 months, online coordinate auto-computation.
- Inter-station spacing 2–9 km across ~30 km² → VRS effectively covers all of Macao; HK partner stations extend coverage across HZMB and Pearl River Delta waters.
- DSCC contact: Tel (853) 2834 0040 · mail@dscc.gov.mo. Office hours Mon–Thu 09:00–13:00 and 14:30–17:45; Fri 09:00–13:00 and 14:30–17:30.

## Post-processing (RINEX) fallback
| Service | URL | Cost |
|---|---|---|
| MoSRef RINEX download — 4 stations, sub-daily to daily, up to 3 months | https://mosref.dscc.gov.mo | free (account) |
| MoSRef coordinate auto-computation — static GNSS processing | https://mosref.dscc.gov.mo | free |

## Sources consulted
- DSCC MoSRef overview: https://www.dscc.gov.mo/en/reference_details/article/reference_1.html
- DSCC NTRIP explainer: https://www.dscc.gov.mo/en/reference_details/article/jplzyfch.html
- DSCC services system: https://www.dscc.gov.mo/en/services_system.html
- DSCC Taipa Grande control point T18T (datum cite): https://www.dscc.gov.mo/en/tripoints1_details/article/T18T.html
- MoSRef portal (confirmed active 2026-05-17): https://mosref.dscc.gov.mo/
- EIN Presswire — BeiDou upgrade 2021: https://www.einnews.com/pr_news/558530491/dscc-has-upgraded-macao-satellite-positioning-reference-station-service-to-support-beidou-navigation-satellite-system
- DSCC user guide Part 2 (PDF, 2012): http://mosref.dscc.gov.mo/Help/ref/20121121-Part2.pdf
- data/stations.json source `mosref` — status ok, last_ok 2026-05-15
- docs/rtk_inventory.md `mosref` block
- TCP curl probe `mosref.dscc.gov.mo:2101` — NOT executed from sandbox; verifier = pipeline cron job
