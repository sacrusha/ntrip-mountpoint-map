# Panama [PA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (TOPORED page reachable today and confirms 28-station network covering PA+CO with no public host:port; IGNTG ignpanama.anati.gob.pa returning 520 from sandbox — same condition since 2026-05-12; EarthScope local pipeline now shows 4 PAN streams + 1 MIRAI rebroadcast — CN55 dropped between 2026-05-17 and 2026-05-22)

## Status: One private commercial NTRIP caster (TOPORED, equipment-gated) + government IGNTG CORS being modernised (no public NTRIP exposed) + 4 EarthScope NOTA streams + 1 MIRAI rebroadcast in PA territory.

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | TOPORED (commercial, equipment-gated — see Service A) |
| Free real-time NTRIP in PA territory | EarthScope NOTA 4 streams + MIRAI 1 stream (see Service C) |
| Government NTRIP (IGNTG) | Not publicly exposed; modernisation in progress 2025–2026 |
| Local pipeline snapshot | `py scripts/stations_by_country.py PAN` 2026-05-22: 4 earthscope (ACHO, CN20, CN60, PTPP) + 1 mirai (QPNP00PAN) = 5 stations across 2 sources. CN55_RTCM3P3 (8.24°N -80.54°W) was present 2026-05-17 and absent 2026-05-22 — recent dropout |

## Service A — TOPORED (Casa del Topógrafo Panama)

| Field | Value |
|---|---|
| landing_url | https://panama.casadeltopografo.com/topored/ (operator page; HTTP 200 2026-05-22, Cloudflare-fronted; previously blocked the sandbox 2026-05-12 / 2026-05-17 — now responding) |
| access_url | Skip — no standalone subscription page; account/credentials require equipment purchase or business contact via the same page. Email/phone from Casa del Topógrafo: +507 261-4686. Account-gated RINEX download referenced on page ("Para poder descargar los archivos RINEX debes tener una cuenta") |
| operator | Casa del Topógrafo Panama (control centre Bogotá, Colombia) |
| host:port | Not published — disclosed to subscribers after account setup |
| num_stations | 6 Panama-located CORS within a 28-station Panama+Colombia network (operator declaration on TOPORED page: "compuesta por 28 estaciones de referencia"; per-station list not on the public page) |
| vrs | ? — operator page describes "correcciones diferenciales usando el protocolo Ntrip" + "método RTK" with a single rover, without VRS/NRTK product language. Sourcetable not retrievable to verify |
| tariff | Not published; access bundled with GNSS equipment purchase from Casa del Topógrafo. No standalone NTRIP-only subscription tariff found on public pages |
| hobbyist_eligibility | Unclear — equipment-purchase access gate effectively excludes rover-only hobbyists. No open subscription path found |
| legal_residency_required | Unclear — equipment-purchase gate applies |
| last_confirmed_alive | 2026-05-22 — page HTTP 200. No public host:port to TCP-probe |
| datum_epoch | omitted — no operator-side declaration on the public page |

## Service B — IGNTG (government CORS, no public NTRIP yet)

Instituto Geográfico Nacional "Tommy Guardia" (IGNTG), a division of ANATI, operates a 19-station national CORS network. 7 of those (IGN1, AZUE, DAVI, DARI, PUAR, PMEC, CHEP) are part of SIRGAS-CON and have internet connectivity.

**Modernisation 2025–2026** (https://destinopanama.com.pa/2025/09/instituto-tommy-guardia-refuerza-red-geodesica-de-cara-a-megaproyecto-ferroviario/, fetched 2026-05-22):
- January 2025: maintenance/update/improvement of the CORS network announced ("Inició el proceso de mantenimiento, actualización y mejora de la red CORS")
- September 2025: 6 new CORS antennas installed to support Panama–David railway, Metro de Panamá and other infrastructure works. Network described as "operating almost in its entirety". TDC600 field controllers received software upgrades
- 2025–2026: project "Reactivation and Improvement of the RGN-CORS" with UNDP support (per IGNTG / ANATI search results)
- **No public NTRIP endpoint, mountpoint list or self-service registration mechanism has been announced**. ArduSimple Panama (July 2024) explicitly states Panama has no established National RTK Network — consistent with IGNTG not operating a public-facing real-time service
- IGNTG portal `ignpanama.anati.gob.pa` returns 520 (Cloudflare) from this sandbox 2026-05-22; not necessarily down — sandbox-side blocking. Public IGNTG news lives at the ANATI domain `anati.gob.pa`

IGNTG CORS data is useful for post-processing via SIRGAS-CON archives; the 7 SIRGAS-CON stations feed the continental network.

## Service C — EarthScope NOTA + MIRAI (free, in-PA real-time)

| Field | Value |
|---|---|
| landing_url | https://www.earthscope.org/data/gnss-realtime/ (NOTA); MIRAI: see https://mirai.kuwasm.kanazawa-u.ac.jp/ |
| access_url | https://data.earthscope.org/ (EarthScope NULA seat); MIRAI: rebroadcast on https://www.unavco.org → EarthScope path |
| host:port | EarthScope: `ntrip.earthscope.org:2101`. MIRAI: separate caster (see local `data/mirai.sourcetable`) |
| Mountpoints (PAN-tagged 2026-05-22) | EarthScope: `ACHO_RTCM3P3` 7.41°N -80.17°W; `CN20_RTCM3P3` 9.35°N -82.26°W (Bocas del Toro); `CN60_RTCM3P3` 8.63°N -79.03°W (near Panama City); `PTPP_RTCM3P3` 8.20°N -82.88°W (near David). MIRAI: `QPNP00PAN` ~8.95°N -79.56°W (Panama City area) |
| num_stations | 4 EarthScope NOTA + 1 MIRAI = 5 free real-time PA-tagged stations (snapshot 2026-05-22). CN55 dropout reduced count from 5 to 4 EarthScope stations recently |
| vrs | No — single-base streams |
| tariff | EarthScope: Free non-commercial via NULA; USD 1,000/seat/yr commercial (5-seat min, 2-week trial). MIRAI: free (project policy; see primer [national-portals] for rebroadcast nature) |
| hobbyist_eligibility | Yes (EarthScope non-commercial); MIRAI free |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-22 — 5 streams present in `data/stations.json` |
| datum_epoch | **EarthScope NOTA: ITRF2014, NOTA epoch 2026-03-30** (declared at https://www.earthscope.org/data/gnss-realtime/). MIRAI per-mountpoint datum: omitted (not declared per primer rule) |

With most pair-baselines ≤80 km, single-base RTK fixes are realistic for much of central/western Panama. This is the **only free real-time path for hobbyists in Panama**.

## Cross-border post-processing reach

Per `py scripts/stations_by_radius.py 9 -80 800` 2026-05-22, ~64 IGAC (Colombia) stations sit within 800 km of central Panama. The nearest (ACAN, APTO) are 300–400 km from Panama City — too far for single-base RTK but available for post-processing. Bocas del Toro region: nearest IGAC stations PLCO, MOTE ~250 km; closest EarthScope CN20 ~150 km, so far-western Panama has the densest cross-border coverage.

## Context Notes

- **Centipede / rtk2go**: 0 PA stations 2026-05-22 (`py scripts/stations_by_country.py PAN` returns only earthscope and mirai sources)
- **GEODNET / ONOCOY**: no confirmed PA coverage on public-facing product pages
- Practical workaround for hobbyists outside EarthScope baselines: deploy a local base for single-base RTK; satellite PPP (Trimble RTX, u-blox PointPerfect, Galileo HAS)

## Real-Time + Post-Processing Fallback

| Service | URL | Cost |
|---------|-----|------|
| EarthScope/NOTA real-time NTRIP (4 PA streams: ACHO, CN20, CN60, PTPP) | https://www.earthscope.org/data/gnss-realtime/ | Free non-commercial (NULA); USD 1,000/seat/yr commercial |
| EarthScope GNSS Data Archive (SIRGAS-CON: IGN1, AZUE, DAVI, DARI, PUAR, PMEC, CHEP) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |
| TOPORED RINEX (6 PA CORS) | https://panama.casadeltopografo.com/topored/ | Account required; pricing not published |

## Sources

- ArduSimple Panama RTK correction services (July 2024 snapshot): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-panama/
- IGNTG CORS page: https://ignpanama.anati.gob.pa/index.php/cors (sandbox 520; sites cached)
- IGNTG 2025 modernisation announcement: https://ignpanama.anati.gob.pa/index.php/mnoticias/322-proyecto-de-modernizacion-2025-del-instituto-geografico-nacional-tommy-guardia
- IGNTG 6-new-antennas press (Sept 2025): https://destinopanama.com.pa/2025/09/instituto-tommy-guardia-refuerza-red-geodesica-de-cara-a-megaproyecto-ferroviario/
- ANATI press release (Apr 2025) — IGNTG capacity strengthening: https://www.anati.gob.pa/index.php/noticias/801-instituto-geografico-nacional-tommy-guardia-fortalece-sus-capacidades-tecnicas-para-la-generacion-de-informacion-geoespacial
- Casa del Topógrafo TOPORED page: https://panama.casadeltopografo.com/topored/ (HTTP 200 2026-05-22)
- Casa del Topógrafo Facebook: https://www.facebook.com/Casadeltopografo/
- SIRGAS Bulletin 9 — IGNTG Panama CORS: sirgas.org
- SIRGAS Bulletin 12 — Estaciones permanentes Panama Cornejo: sirgas.org
- EarthScope NOTA realtime (datum ITRF2014, NOTA epoch 2026-03-30): https://www.earthscope.org/data/gnss-realtime/
- EarthScope licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- Local pipeline `py scripts/stations_by_country.py PAN` 2026-05-22: earthscope = 4 (ACHO, CN20, CN60, PTPP), mirai = 1 (QPNP00PAN). CN55 dropped between 2026-05-17 and 2026-05-22
- Cross-border IGAC density `py scripts/stations_by_radius.py 9 -80 800` 2026-05-22: ~64 IGAC stations within 800 km
