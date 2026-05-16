# Chile [CL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: PAID-ONLY — no free public national caster; one paid commercial caster verified alive; national IGM service still RINEX-only

Chile has no free public national NTRIP RTK service in 2026-05. IGM's national SIRGAS-CHILE network distributes RINEX for post-processing only; the 2025 announcement of a future NTRIP/VRS service has not produced a public endpoint, and the language about it has been removed from the sirgaschile.cl homepage. Two commercial casters operate: GEOCOM (Trimble distributor, public sourcetable alive but production mountpoints credential-gated, pricing not published) and KollNET (independent surveying company, caster hostname purchase-gated). One pilot Emlid-brand network (SCS Equipos, Santiago metro) exists but is brand-locked and trial-only.

## Casters

### kollnet_cl — KollNET (Kollner Labraña & Cía. Ltda.)
| Field | Value |
|---|---|
| landing_url | https://www.kollnerlabrana.cl/ |
| access_url | http://www.kollnerlabrana.cl/kollnet.html |
| host:port | not publicly documented (released after purchase). Probes of `kollnerlabrana.cl:2101` and subdomains timed out from external IP 2026-05-15 — consistent with the purchase-gate description and unchanged from 2026-05-06 / 2026-05-12 probes |
| tariff | CLP +IVA (19%), confirmed on access_url 2026-05-15: 7 days CLP 48,000 · 15 days CLP 60,000 · 30 days CLP 85,000 · 3 mo CLP 180,000 · 12 mo CLP 450,000. With IVA the annual is CLP 535,500 ≈ USD 599 at 894 CLP/USD (2026-05-14 close) |
| num_stations | 8 physical (Santiago, Valparaíso, Los Andes, Santa Cruz, Talca, Chillán, Temuco, Frutillar); claimed 1–4 cm HRMS within ~100 km of each |
| vrs | yes — operator states "el servicio VRS […] el primero en implementarse en Chile" on access_url |
| hobbyist_eligibility | yes — brand-agnostic, any NTRIP-capable RTK receiver; prepaid, no annual contract |
| legal_residency_required | unclear — not stated; payment via Webpay/transferencia |
| last_confirmed_alive | 2026-05-15 — access_url HTTP 200, pricing tiers unchanged; caster port still firewalled from outside Chile (purchase-gate) |
| datum_epoch | not stated on access_url; operator describes network as SIRGAS-tied but no formal datum/epoch declaration is published — OMIT |

### geocom_gnss_cl — GEOCOM Red GNSS
| Field | Value |
|---|---|
| landing_url | https://www.geocom.cl/ |
| access_url | https://www.geocom.cl/pages/red-gnss |
| host:port | `ntrip.geocom.cl:2101` — `SOURCETABLE 200 OK` (curl --http0.9, 2026-05-15 21:05 UTC; `Server: Pycaster Ntrip Version 1`). Public sourcetable advertises only one mountpoint `TEST_RTCM` (RTCM 1005/1074/1084/1124, GNSS, country `CL`, network `NET`, 0/0 coords, no nmea, no auth listed). Production mountpoints are credential-gated and not in the public sourcetable |
| tariff | not publicly listed; contact `ventas@geocom.cl` / +562 2480 3600. A separate free "GEOCASTER" portal at `geocaster.geocom.cl` (HTTPS 200, 2026-05-15) is positioned as a free NTRIP connectivity service for GEOCOM-equipment customers — eligibility for non-GEOCOM customers undocumented |
| num_stations | not published; coverage from operator narrative: Calama, Antofagasta, Los Andes, Santiago, Talca, Concepción, Los Ángeles, Temuco, Valdivia, Osorno, Puerto Montt (~23°S–41°S, ~11 named cities) |
| vrs | not stated on access_url |
| hobbyist_eligibility | unclear — sales-led commercial network targeted at Trimble equipment customers; no self-service hobbyist signup pathway documented |
| legal_residency_required | unclear |
| last_confirmed_alive | 2026-05-15 — `ntrip.geocom.cl:2101` `SOURCETABLE 200 OK`; access_url HTTP 200; `geocaster.geocom.cl` HTTPS 200 with `Registrarse` signup link |
| datum_epoch | network described as calculated at epoch 2025.0 and linked to SIRGAS via fiducial stations (per prior research; no operator URL re-confirms this in 2026-05) — OMIT |

### scs_emlid_cl — SCS Equipos Red Colaborativa NTRIP (pilot)
| Field | Value |
|---|---|
| landing_url | https://www.scsequipos.com/ |
| access_url | https://www.scsequipos.com/cinco-nuevas-estaciones-ntrip-instaladas-en-santiago-por-scs-equipos/ |
| host:port | not published; credentials issued by email |
| tariff | free during pilot; commercial pricing not announced |
| num_stations | 5 (Providencia, Tiltil, Colina, La Reina, San Bernardo) + 1 (Quillota, Valparaíso) — Santiago metro only, claimed <20 km baselines |
| vrs | no — single-base, nearest-station |
| hobbyist_eligibility | yes during pilot; brand-locked to Emlid Reach RX / RS2 / RS2+ |
| legal_residency_required | unclear — contacto@scsequipos.com |
| last_confirmed_alive | 2026-05-15 — access_url HTTP 200; original post dates from 2024, operator presents service as still trial-phase ("no recomendado para trabajos profesionales") |
| datum_epoch | not declared — OMIT |

## Most Recent National Project (no operational endpoint)

**IGM / SIRGAS-CHILE national NTRIP** — Instituto Geográfico Militar de Chile launched the "Época de Referencia 2025.0" national geodetic network in 2025 with 28 new first-level CORS stations (180+ stations total when including seismological partners) and a redesigned sirgaschile.cl portal. The 2025 launch announcement described NTRIP / VRS / web-PPP as planned real-time services. As of 2026-05-15: (a) the sirgaschile.cl homepage no longer mentions NTRIP, real-time, RTK, caster, or streaming (grep verified); (b) the portal continues to offer only RINEX observation download (registration required) and paid coordinate certificates via Webpay; (c) no caster host:port has been published; (d) `ntrip.igm.cl` no longer resolves in DNS (curl: "Could not resolve host", 2026-05-15). The IGS Workshop 2026 in Santiago (1–5 June 2026, organised by USACH with IGM) is the next plausible public-launch moment but is not committed. Sources: https://www.sirgaschile.cl/ · https://www.sirgaschile.cl/descarga_observaciones.php · https://sirgas.ipgh.org/en/news/igs-workshop-2026-june-1-5-2026/

## Other Operators Investigated (excluded)

- **Geoland / SingularXYZ** (geoland.cl): Chilean distributor with `singularcaster`, `sv100`, `n1` product pages, but the previously-referenced `geoland.cl/ntrip-correccion-semanal` returns HTTP 404 (2026-05-15). They sell SingularCaster software and CORS hardware to network operators rather than operating a public caster. No public caster endpoint or hobbyist pricing.
- **INGEO / GeoBee** (ingeo.cl): Hardware product (Tersus David receiver, CLP 5,490,000) sold as a "reference station kit" — customer self-hosts NTRIP. Not a correction service.
- **"IngeoSatellite" / "Pisagua"**: no operator by either name found in 2026-05 searches. Pisagua appears only as a Chilean town name (placename, not a caster); "IngeoSatellite" returns no Chilean NTRIP service hits.

## Cross-Border / Free Alternatives

- **No nearest cross-border free caster within ~50 km** of populated Chilean areas. Argentina's RAMSAC-NTRIP (IGN) and Peru's IGN-PE require national accreditation; both Andes-side borders are mountainous and unpopulated within 50 km of the international line.
- **EarthScope / UNAVCO**: hosts archive RINEX for selected Chilean CORS; non-commercial-only real-time stream (USD 1,000/seat/yr commercial). https://www.earthscope.org/data/gnss-data/
- **Global commercial fallbacks with Chile coverage**: GEODNET (partial), PointOne (sparse). Trimble RTX / Starfire are PPP, not network RTK — out of scope per project posture.

## Local Pipeline Coverage (2026-05-15)
- `py scripts/stations_by_country.py CHL` → "No stations for 'CHL'" (rtk2go uses no CHL entries; centipede has no CL/CHL).
- `py scripts/stations_by_radius.py -33.45 -70.66 200` (Santiago, 200 km) → "No stations within 200 km".
- Chile is absent from rtk2go, centipede, and EarthScope public sourcetables in current local data.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| SIRGAS-CHILE / IGM — national CORS RINEX | https://www.sirgaschile.cl/descarga_observaciones.php | RINEX free with registration; coordinate certificates paid via Webpay |
| EarthScope (formerly UNAVCO) — Chilean GNSS geodetic archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; USD 1,000/seat/yr commercial |

## Sources Consulted (2026-05-15)
- KollNET service page: http://www.kollnerlabrana.cl/kollnet.html (HTTP 200; pricing + VRS claim quoted)
- GEOCOM Red GNSS: https://www.geocom.cl/pages/red-gnss (HTTP 200; no public pricing/stations)
- GEOCASTER portal: https://geocaster.geocom.cl/ (HTTPS 200; signup link, no technical detail)
- SIRGAS-CHILE: https://www.sirgaschile.cl/ (HTTP 200; no NTRIP text remains on homepage)
- SIRGAS-CHILE RINEX download: https://www.sirgaschile.cl/descarga_observaciones.php
- IGM Chile press release on 2025 launch: https://www.ejercito.cl/prensa/visor/igm-lanzo-la-nueva-red-geodesica-nacional-sirgas-chile-2025
- SCS Equipos pilot post: https://www.scsequipos.com/cinco-nuevas-estaciones-ntrip-instaladas-en-santiago-por-scs-equipos/
- ArduSimple Chile NTRIP overview: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-chile/ (confirms "Chile lacks a nationwide real-time RTK service"; recommends RTK2GO/IGS/EarthScope as fallback)
- INGEO GeoBee (hardware, not a service): https://www.ingeo.cl/producto/estacion-de-referencia-geobee/
- GPS World on Tersus GeoCaster software (the platform underlying GEOCOM's GEOCASTER): https://www.gpsworld.com/tersus-gnss-releases-geocaster-software-for-ntrip-corrections/
- curl probe `http://ntrip.geocom.cl:2101/` → `SOURCETABLE 200 OK` 2026-05-15 21:05 UTC (`Server: Pycaster Ntrip Version 1`, one mountpoint `TEST_RTCM` RTCM/CMRx)
- curl probe `http://ntrip.igm.cl:2101/` → "Could not resolve host" 2026-05-15 (DNS regression vs. prior research)
- curl probe `geocaster.geocom.cl:2101` → connection refused 2026-05-15 (ports firewalled from outside)
- Local pipeline: `data/stations.json` → rtk2go CHL = 0, centipede CHL = 0 (2026-05-15)
- CLP/USD reference rate: 894 CLP/USD, 2026-05-14 close (TradingEconomics)

## Self-Review
(a) Source diversity — operator first-party pages (KollNET, GEOCOM, SIRGAS, SCS, INGEO), independent press (ArduSimple, GPS World), and live probes. PASS.
(b) Verifications dated — every operator + probe stamped 2026-05-15. PASS.
(c) Removed bad research — dropped vague "Geoland NTRIP subscription tiers" speculation (page now 404); dropped CLP→USD figure of $470 (was based on stale FX, recomputed to ~$599 IVA-inclusive at 894 CLP/USD); clarified that IGM hostname no longer resolves; dropped Pisagua/IngeoSatellite as not found. PASS.
(d) No fluff — facts and dates only. PASS.
(e) Conformance to template (landing_url, access_url, host:port, tariff, num_stations, vrs, hobbyist_eligibility, legal_residency_required, last_confirmed_alive, datum_epoch) — all fields present per caster; datum_epoch OMIT'd where uncited per spec. PASS.
(f) Cross-border / nearest-alternative addressed — Argentina/Peru borders are mountainous + accreditation-gated; no <50 km option. PASS.

SELF-REVIEW: PASS
