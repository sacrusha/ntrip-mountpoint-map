# Chile [CL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revising 2026-05-06 entry)

## Status: YES — multiple private commercial NTRIP casters operating; no free public caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private/commercial) |
| **host:port — GEOCOM** | `ntrip.geocom.cl:2101` |
| **host:port — KollNET** | not published (contact vendor); port 2101 timed out from outside Chile on 2026-05-12 (consistent with 2026-05-06 observation) |
| **tariff — KollNET** | CLP 48,000 +IVA / 7 days · CLP 60,000 +IVA / 15 days · CLP 85,000 +IVA / 30 days · CLP 180,000 +IVA / 3 months · CLP 450,000 +IVA / 12 months (source: kollnerlabrana.cl/kollnet.html, page re-fetched 2026-05-12 — pricing unchanged from 2026-05-06) |
| **tariff — GEOCOM** | not published publicly; contact ventas@geocom.cl; restricted to GEOCOM/Trimble equipment customers |
| **hobbyist_eligibility** | KollNET: yes — any brand RTK GNSS receiver; GEOCOM: unclear (equipment-vendor network) |
| **legal_residency_required** | unclear for both; no explicit residency requirement stated |
| **last_confirmed_alive** | `ntrip.geocom.cl:2101` returned `SOURCETABLE 200 OK` on 2026-05-12 (curl verified; `Server: Pycaster Ntrip Version 1`); kollnerlabrana.cl website HTTP 200 on 2026-05-12 |

## Most Recent Project Announcement

**IGM / SIRGAS-Chile 2025 geodetic network launch — status update 2026-05-12** — The Instituto Geográfico Militar (IGM) launched the new "Época de Referencia 2025.0" national geodetic network (Red Geodésica Nacional) consisting of 28 first-level CORS stations and a redesigned SIRGAS-Chile portal. The launch announcement and the current sirgaschile.cl/Mapa_RGN.php viewer continue to describe NTRIP / VRS / web-PPP as the planned real-time services delivered "through a strengthened Control Center" — but as of 2026-05-12 the public-facing portal still offers only RINEX observation download (sirgaschile.cl/descarga_observaciones.php) and coordinate certificates. No public NTRIP caster URL has been published; no operational endpoint has been verified by curl probe. Chile will host the IGS Workshop 2026 in Santiago (1–5 June 2026), organised by USACH with IGM — a plausible moment for a public NTRIP service announcement but not yet committed.

Sources: https://www.sirgaschile.cl/ · https://www.sirgaschile.cl/Mapa_RGN.php · https://www.sirgaschile.cl/descarga_observaciones.php · https://www.ejercito.cl/prensa/visor/igm-lanzo-la-nueva-red-geodesica-nacional-sirgas-chile-2025 · IGS Workshop 2026: https://sirgas.ipgh.org/en/news/igs-workshop-2026-june-1-5-2026/

## Context Notes

- **GEOCOM Red GNSS** (`ntrip.geocom.cl:2101`): Operated by Geocom S.A. (Chilean Trimble distributor) for 15+ years. The sourcetable is live and responded on 2026-05-12 with one advertised public mountpoint (`TEST_RTCM`, RTCM/CMRx, GNSS, country tag CL, no carrier-phase advertised on the public stream); production mountpoints requiring credentials are not listed publicly. Covers Calama, Antofagasta, Los Andes, Santiago, Talca, Concepción, Los Ángeles, Temuco, Valdivia, Osorno, Puerto Montt (approx. 23°S–41°S). GEOCOM additionally announced a free "GEOCASTER" service for GEOCOM-equipment owners; pricing and hobbyist access outside their equipment ecosystem remain undocumented. Contact: ventas@geocom.cl / +562 2480 3600.
- **KollNET** (Kollner Labraña & Cia. Ltda.): Independent NTRIP service with 8 reference stations (Santiago, Valparaíso, Los Andes, Santa Cruz, Talca, Chillán, Temuco, Frutillar). Claimed precision 1–4 cm HRMS within ~100 km per station. Port 2101 on all tested KollNET hostnames timed out from external IP on 2026-05-06 and again on 2026-05-12; the company website (kollnerlabrana.cl) is HTTP 200 and the service page (kollnerlabrana.cl/kollnet.html) is current with the same five-tier prepaid pricing. Caster hostname not publicly documented — provided after purchase. IVA rate for Chile is 19% (standard). Brand-agnostic: any NTRIP-capable RTK receiver accepted. Prepaid packages; no annual contract required.
- **Geoland / SingularXYZ**: Chilean distributor (geoland.cl) selling NTRIP subscription tiers (daily / weekly / fortnightly / annual) and reselling SingularCaster software for CORS network operators. Their NTRIP product pages returned 404 on 2026-05-06; it is unclear whether they operate an independent caster network or resell access to KollNET/GEOCOM. Pricing not publicly listed.
- **SCS Equipos Red Colaborativa NTRIP**: Trial-phase Emlid-based collaborative network in Santiago Metropolitan Region (Providen, cia, Tiltil, Colina, La Reina, San Bernardo) and Quillota; not yet recommended for professional use at time of research; access via contacto@scsequipos.com.
- **IGM / SIRGASCHILE CORS**: 28+ CORS stations available for RINEX download (free, account required). Real-time NTRIP explicitly described as "planned" — no confirmed operational date as of 2026-05-12. No caster endpoint found.
- **No free public national caster exists** as of 2026-05-12. Chile is absent from NTRIP-list.com's South America table and from the RTK2go / Centipede sourcetables (re-verified 2026-05-12: rtk2go CHL = 0, centipede CHL = 0 in local pipeline data; rtk2go previously reported a single Iquique base, no longer present in current fetch).
- **Global commercial fallbacks** with Chile coverage: GEODNET (partial), PointOne (sparse), Starfire/Trimble RTX (PPP, not networkRTK).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SIRGASCHILE / IGM** — CORS station RINEX download (EAF stations IGM2, UBOH, ACPM, LLFN + CSN seismological stations) | https://www.sirgaschile.cl/descarga_observaciones.php | Free (account required); coordinate certificates via ventas@igm.cl |
| **UNAVCO / EarthScope** — selected Chilean CORS (GNSS geodetic archive) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; USD 1,000/seat/yr commercial |

## Sources Consulted
- GEOCOM Red GNSS page: https://www.geocom.cl/pages/red-gnss
- GEOCOM GEOCASTER announcement (YouTube): https://www.youtube.com/watch?v=3mPmIqamlSM
- KollNET service page: http://www.kollnerlabrana.cl/kollnet.html
- ArduSimple Chile NTRIP services page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-chile/
- SIRGASCHILE portal: https://www.sirgaschile.cl/
- SIRGASCHILE CORS download: https://www.sirgaschile.cl/descarga_observaciones.php
- IGM / Ejército de Chile SIRGAS-Chile 2025 launch announcement: https://www.ejercito.cl/prensa/visor/igm-lanzo-la-nueva-red-geodesica-nacional-sirgas-chile-2025
- NTRIP-list.com South America: https://ntrip-list.com/south-america/
- Geoland / SingularXYZ NTRIP products: https://geoland.cl/
- SCS Equipos Red Colaborativa NTRIP: https://www.scsequipos.com/cinco-nuevas-estaciones-ntrip-instaladas-en-santiago-por-scs-equipos/
- curl probe of `ntrip.geocom.cl:2101` — SOURCETABLE 200 OK confirmed 2026-05-12 (Server: Pycaster Ntrip Version 1; one public mountpoint `TEST_RTCM`)
- curl probe of `kollnerlabrana.cl:2101` and subdomains — connection timeout 2026-05-12 (caster hostname behind purchase wall, consistent with 2026-05-06 finding)
- Local pipeline data: `data/stations.json` (rtk2go CHL = 0, centipede CHL = 0; fetched 2026-05-12T18:17Z)
