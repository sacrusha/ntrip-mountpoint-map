# Chile [CL] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status

PAID-ONLY for the cm-accurate hobbyist; no free public national NTRIP caster.
National IGM service remains RINEX-only. KollNET (independent) is the
cheapest accessible paid caster with transparent pricing and self-service
prepaid hobbyist signup. GEOCOM (Trimble distributor) operates a sales-led
commercial caster + a "GEOCASTER" free portal for GEOCOM-equipment customers
only. SCS Equipos pilot is Emlid-brand-locked and trial-only. ArduSimple
(updated 2026-05-23) still states "as far as we know Chile is not among"
countries with a national RTK network.

## kollnet_cl — KollNET (Kollner Labraña & Cía. Ltda.)

| Field | Value |
|---|---|
| operator | Kollner Labraña & Cía. Ltda. |
| landing_url | https://www.kollnerlabrana.cl/ |
| access_url | http://www.kollnerlabrana.cl/kollnet.html |
| access_type | paid (prepaid, brand-agnostic, self-service) |
| sourcetable | host:port not publicly documented (released after purchase) (checked: kollnerlabrana.cl/kollnet.html 2026-05-23; TCP probes of `kollnerlabrana.cl:2101` and `ntrip.kollnerlabrana.cl:2101` time out 2026-05-23; no host:port returned by `site:kollnerlabrana.cl` searches 2026-05-23) |
| coverage | 8 physical CORS: Santiago, Valparaíso, Los Andes, Santa Cruz, Talca, Chillán, Temuco, Frutillar. Operator claims 1–4 cm HRMS within ~100 km of each. |
| num_stations | 8 physical |
| vrs | yes — operator: "el servicio VRS [...] el primero en implementarse en Chile" (access_url) |
| tariff | CLP excluding IVA (19%), verified 2026-05-23 on access_url: 7 days CLP 48,000 · 15 days CLP 60,000 · 30 days CLP 85,000 · 3 months CLP 180,000 · 12 months CLP 450,000. Annual incl. IVA = CLP 535,500 ≈ USD 599 (at 894 CLP/USD, 2026-05-14 close). Source: http://www.kollnerlabrana.cl/kollnet.html |
| hobbyist_eligibility | yes — brand-agnostic, any NTRIP-capable RTK receiver, prepaid, no annual contract |
| residency_required | ? — not stated; payment via Webpay / transferencia, both Chile-resident-friendly but no documented foreign-customer rejection (checked: kollnerlabrana.cl/kollnet.html 2026-05-23; kollnerlabrana.cl landing 2026-05-23) |
| datum_epoch | omitted — operator describes network as SIRGAS-tied on access_url but publishes no formal datum/epoch declaration |
| stations_source | http://www.kollnerlabrana.cl/kollnet.html (operator narrative; no machine-readable map) |

## geocom_gnss_cl — GEOCOM Red GNSS (sales-led commercial)

| Field | Value |
|---|---|
| operator | GEOCOM SpA (Trimble distributor) |
| landing_url | https://www.geocom.cl/ |
| access_url | https://www.geocom.cl/pages/red-gnss |
| access_type | paid (sales-quote) for Red GNSS; "GEOCASTER" portal is free **only for GEOCOM-equipment customers** per operator phrasing |
| sourcetable | `ntrip.geocom.cl:2101` — live 2026-05-23, `SOURCETABLE 200 OK`, `Server: Pycaster Ntrip Version 1`, 281 bytes, single mountpoint `TEST_RTCM` (RTCM 1005/1074/1084/1124, country CL, 0/0 coords, nmea=1). Production mountpoints are credential-gated and not in the public sourcetable. |
| coverage | Operator narrative names 11 cities Calama → Puerto Montt (~23°S–41°S). |
| num_stations | 27 physical per GEOCOM 2021-00 processing note (15 also belong to SIRGAS). https://www.geocom.cl/blogs/news/red-gnss-geocom-2021-00 |
| vrs | ? — 27 stations / ~100 km median spacing is technically plausible for VRS; no operator page declares VRS / MAC / FKP / iMAX / NEAR; public sourcetable too small to confirm (checked: geocom.cl/pages/red-gnss 2026-05-23; geocom.cl 2021-00 note 2026-05-23; `ntrip.geocom.cl:2101` sourcetable 2026-05-23 — single TEST_RTCM mountpoint, no VRS keywords) |
| tariff | not publicly listed; contact `ventas@geocom.cl` / +562 2480 3600. GEOCASTER portal positioned by operator as free NTRIP connectivity for GEOCOM customers (Dec 2025 announcement); non-GEOCOM eligibility undocumented |
| hobbyist_eligibility | ? — sales-led, Trimble-customer-aligned; no self-service hobbyist signup pathway documented (checked: geocom.cl/pages/red-gnss 2026-05-23; geocaster.geocom.cl 2026-05-23) |
| residency_required | ? (checked: geocom.cl/pages/red-gnss 2026-05-23; geocom.cl landing 2026-05-23 — no residency clause either way) |
| datum_epoch | omitted — GEOCOM 2021-00 note anchors a 2021-01-01 solution to GPS week 2138 via SIRGAS SIR20P2138 (internal processing reference, not an operator-published frame declaration for the live NTRIP feed) |
| stations_source | https://www.geocom.cl/blogs/news/red-gnss-geocom-2021-00 (narrative); no public station map |

## scs_emlid_cl — SCS Equipos Red Colaborativa NTRIP (pilot, brand-locked)

| Field | Value |
|---|---|
| operator | SCS Equipos (Emlid distributor Chile) |
| landing_url | https://www.scsequipos.com/ |
| access_url | https://www.scsequipos.com/cinco-nuevas-estaciones-ntrip-instaladas-en-santiago-por-scs-equipos/ |
| access_type | restricted (Emlid hardware required; trial credentials issued by email) |
| sourcetable | host:port not published; credentials issued by email |
| coverage | 5 stations in Santiago metro (Providencia, Tiltil, Colina, La Reina, San Bernardo) + 1 Quillota (Valparaíso) — Santiago metro only, operator-claimed <20 km baselines |
| num_stations | 6 |
| vrs | no — single-base, nearest-station |
| tariff | free during pilot; no commercial pricing announced — pilot post text "están operativas en fase de prueba" still on access_url 2026-05-23 |
| hobbyist_eligibility | yes during pilot, **but Emlid Reach RX / RS2 / RS2+ hardware required**; brand-locked, non-Emlid receivers (ZED-F9P, Septentrio, Trimble, …) excluded |
| residency_required | ? — Emlid-hardware gating is the binding restriction; residency not addressed (checked: scsequipos.com access_url 2026-05-23; scsequipos.com landing 2026-05-23) |
| datum_epoch | omitted — not declared on access_url or operator landing |
| stations_source | access_url (narrative only) |

## Most Recent National Project (no operational endpoint)

**IGM / SIRGAS-CHILE national NTRIP** — IGM launched "Época de Referencia
2025.0" in 2025 with 28 new first-level CORS (~180 including seismological
partners) and a redesigned `sirgaschile.cl` portal. The 2025 launch described
NTRIP / VRS / web-PPP as planned. As of 2026-05-23:

- `sirgaschile.cl` homepage no longer mentions NTRIP / real-time / RTK / caster / streaming;
- portal still offers only RINEX download + paid coordinate certificates (Webpay);
- no caster host:port published; `ntrip.igm.cl` no longer resolves in DNS (prior research checkpoint);
- legacy `/Mapa_RGN.php` returns HTTP 404 (site now under "SIRGAS-CHILE 2026" branding, no NTRIP service link anywhere on the redesigned portal);
- IGS Workshop 2026 Santiago (1–5 June 2026, USACH + IGM) is the next plausible launch window — not committed.

**Ministerio de Bienes Nacionales — RINEX-only portal (2025-03-25)**: MBN
publishes RINEX 3.0 daily files from 18 CORS distributed nationwide + IGM-
certified coordinate sheets via a SharePoint banner. Free, open public.
Post-processing only — **no NTRIP / real-time stream**.

## Other operators investigated (excluded)

- **Geoland / SingularXYZ** (geoland.cl): SingularCaster / SV100 / N1 product pages; previously-referenced `geoland.cl/ntrip-correccion-semanal` returns HTTP 404. Sells SingularCaster software and CORS hardware to network operators; no public caster endpoint or hobbyist pricing.
- **INGEO / GeoBee** (ingeo.cl): Hardware product (Tersus David receiver, CLP 5,490,000) sold as a self-host reference station kit. Not a correction service.
- "IngeoSatellite" / "Pisagua": no operator by either name found in 2026-05 searches. Pisagua = Chilean town placename.

## Cross-Border / Free Alternatives

- **Argentina — RAMSAC-NTRIP (IGN)**: free with self-registration, no surveying licence (see `AR_Argentina.md`). Border is mountainous and unpopulated within 50 km along most of the Andes, **but** the Argentine Cuyo corridor (Mendoza / San Juan) is adjacent to Chilean Norte Chico — settled valleys lie ≤50 km apart in places (Los Andes CL ↔ Uspallata / Mendoza AR). A Norte Chico user can plausibly reach a RAMSAC physical station within single-base range.
- **Peru — IGN-PE / REGGEN**: see `PE_Peru.md`. Chile–Peru border (Arica region) is desert + lightly populated within 50 km.
- **EarthScope / UNAVCO**: archive RINEX for selected Chilean CORS; non-commercial-only real-time stream (USD 1,000/seat/yr commercial). See `EarthScope.md`. https://www.earthscope.org/data/gnss-data/
- **Global commercial PPP**: Trimble RTX, Starfire — out of scope (PPP, not network RTK).

## Local Pipeline Coverage (2026-05-23)

- `py scripts/stations_by_country.py CHL` → 7 mountpoints (igs_ip 6 + mirai 1). igs_ip CHL: ANTC, ANTF, IQQE, SANT, TEJA, USCL. mirai 1: QSTP. No rtk2go / centipede / earthscope CHL.
- `py scripts/stations_by_radius.py -33.45 -70.66 500` (Santiago, 500 km) → 32 stations: ramsac 26 [ARG cross-border], igs_ip 4 [CHL:3, ARG:1], mirai 2 [ARG:1, CHL:1].

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| SIRGAS-CHILE / IGM national CORS RINEX | https://www.sirgaschile.cl/descarga_observaciones.php | RINEX free with registration; coord certificates paid (Webpay) |
| Ministerio de Bienes Nacionales — 18 CORS RINEX 3.0 + IGM-certified coords (2025-03 launch) | https://www.bienesnacionales.cl/informacion-geodesica-de-las-estaciones-cors-se-encuentra-disponible-en-banner-de-acceso-directo/ ; https://ide.bienes.cl/ | Free, open public |
| EarthScope (formerly UNAVCO) Chilean GNSS archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; USD 1,000/seat/yr commercial |

## Sources Consulted (2026-05-23)

- KollNET service page: http://www.kollnerlabrana.cl/kollnet.html (HTTP 200; pricing + VRS claim re-quoted 2026-05-23, IVA exclusion noted)
- GEOCOM Red GNSS: https://www.geocom.cl/pages/red-gnss
- GEOCOM Red GNSS technical note (27 stations, SIR20P2138): https://www.geocom.cl/blogs/news/red-gnss-geocom-2021-00
- GEOCASTER portal: https://geocaster.geocom.cl/
- Ministerio de Bienes Nacionales CORS RINEX banner: https://www.bienesnacionales.cl/informacion-geodesica-de-las-estaciones-cors-se-encuentra-disponible-en-banner-de-acceso-directo/ ; IDE portal https://ide.bienes.cl/
- SIRGAS-CHILE: https://www.sirgaschile.cl/ (no NTRIP text on homepage, 2026-05-23)
- SIRGAS-CHILE RINEX download: https://www.sirgaschile.cl/descarga_observaciones.php
- IGM Chile press release on 2025 launch: https://www.ejercito.cl/prensa/visor/igm-lanzo-la-nueva-red-geodesica-nacional-sirgas-chile-2025
- SCS Equipos pilot post: https://www.scsequipos.com/cinco-nuevas-estaciones-ntrip-instaladas-en-santiago-por-scs-equipos/
- ArduSimple Chile NTRIP overview: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-chile/ (page last updated 2026-05-23: still "Chile is not among" countries with national RTK; ArduSimple does not list KollNET / GEOCOM)
- INGEO GeoBee (hardware, not a service): https://www.ingeo.cl/producto/estacion-de-referencia-geobee/
- GPS World on Tersus GeoCaster software (platform underlying GEOCOM GEOCASTER): https://www.gpsworld.com/tersus-gnss-releases-geocaster-software-for-ntrip-corrections/
- Live probe `curl --http0.9 http://ntrip.geocom.cl:2101/` 2026-05-23 → SOURCETABLE 200 OK, single `TEST_RTCM` mountpoint, 281 bytes
- CLP/USD reference rate: 894 CLP/USD, 2026-05-14 close (TradingEconomics)
