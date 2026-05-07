# Colombia [CO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07 (initial 2026-05-06)

## Status: YES — free national NTRIP caster (IGAC MAGNA-ECO) operational on two ports; VRS via Leica Spider Business Center; ~127 unique CORS coordinates advertised on physical-stations port; registration required; no commercial alternatives identified beyond cross-border Topored

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | IGAC — Instituto Geográfico Agustín Codazzi, Centro de Control Geodésico Nacional |
| **Network name** | MAGNA-ECO — Estaciones Continuas Operativas del Marco Geocéntrico Nacional MAGNA-SIRGAS (Red Geodésica Nacional Activa) |
| **Mandate basis** | Resolución IGAC 1771 de 2024 (officializing the redgeodesica.igac.gov.co portal as the National Geodetic Network web service); Law 1955/2019 PND Art. 281 (free public access mandate); Centro de Control Geodésico Nacional formally launched April 2024 |
| **host:port — VRS / network solution** | `sbc.igac.gov.co:2101` (Server: NTRIP Spider/7.11.0.96, confirmed via direct sourcetable fetch 2026-05-07; HTTP 200 OK, Content-Length 1989) — 20 mountpoints offering MSM, RTCM 2/3, CMR, CMR+, Leica4G formats with NEAR/IMAX/VIRS variants |
| **host:port — single-base / physical stations** | `sbc.igac.gov.co:2102` (Server: NTRIP Spider/7.11.0.96, confirmed via direct sourcetable fetch 2026-05-07; HTTP 200 OK, Content-Length 15621) — 143 mountpoints, 127 unique physical coordinates |
| **VRS** | Yes — `MSM_VIRS`, `MSM_IMAX`, `MSM_NEAR` (all RTCM 3, GPS+GLO+GAL+BDS, network solution flags 1/1 for VIRS/IMAX, NEAR is solution=0); legacy variants `RTCM3_VIRS`, `RTCM3_IMAX`, `RTCM3_NEAR`, `RTCM2_VIRS`, `RTCM2_IMAX`, `RTCM2_NEAR`, `RTCM2_DGPS`, `RTCM2_DGPS_VIRS`, `RTCM2_DGPS_IMAX`, `CMR_NEAR`, `CMRP_NEAR`, `CMRP_IMAX`, `CMRP_VIRS`, `Leica4G_NEAR`, plus regional cells `LLANOS_RTCM3`, `SUR_OESTE_RTCM3`, `NOROESTE_RTCM3` (regional sub-network mounts on port 2101) |
| **Mountpoints (port 2102, single-base, sample)** | `AEFO_RTCM3` (1.59°N/75.56°W), `AEMO_RTCM3` (9.26°N/74.44°W), `BOGT_RTCM3`, `CALI_RTCM3` (3.38°N/76.53°W), `CART_RTCM3` (10.39°N/75.53°W) Cartagena, `CUCU_RTCM3` (7.90°N/72.49°W) Cúcuta, `IBAG_RTCM3` (4.43°N/75.21°W) Ibagué, `INIR_RTCM3` (3.87°N/67.93°W) Inírida, `BUEN_RTCM3` (3.88°N/77.01°W) Buenaventura, etc. — 143 station-RTCM3 mountpoints; 127 unique lat/lon pairs |
| **Constellations** | GPS+GLO+GAL+BDS on MSM mountpoints; GPS+GLO on most legacy RTCM3 single-base mountpoints; GPS-only on some RTCM2 / DGPS legacy variants |
| **RTCM format** | RTCM 3 (MSM and legacy), RTCM 2, CMR, CMR+, Leica 4G; software stack Leica GNSS Spider 7.11.0.96 |
| **tariff** | **Free — COP 0 / $0.00.** Mandated by Law 1955/2019 (Plan Nacional de Desarrollo, Art. 281) as part of national spatial data infrastructure. No subscription, no per-minute charges. Source: https://redgeodesica.igac.gov.co/herramientas/servicios.html and IGAC Geodesia FAQ; observed 2026-05-07. |
| **VAT status** | N/A — service is free of charge |
| **hobbyist_eligibility** | Yes — open registration via Spider Business Center; no professional licence requirement; account types include individuals (personas naturales) |
| **legal_residency_required** | Unclear — registration form requests national ID (cédula) by default; foreign passports may be accepted via the SBC's international ID-type dropdown; no explicit international block found, but no official statement of openness to non-residents either. The SBC platform itself supports 31+ languages including English, Spanish, Portuguese — suggesting non-resident access is technically possible. |
| **last_confirmed_alive** | 2026-05-07 — both ports 2101 (network/VRS) and 2102 (single-base) returned valid sourcetables; redgeodesica.igac.gov.co portal HTTP 200; Spider Business Center login portal at redgeodesica-sbc.igac.gov.co/sbc HTTP 200 |

## Registration Process

1. Go to `https://redgeodesica-sbc.igac.gov.co/sbc/Account/Register` (Spider Business Center registration form)
2. Confirm account via email (`Spider Business Center` issues automated confirmation)
3. Log in to the SBC portal and request a new NTRIP subscription ("Solicitar nueva suscripción")
4. After IGAC approves the subscription, connect rover to:
   - `sbc.igac.gov.co:2101` for network solutions (VRS, IMAX, NEAR network)
   - `sbc.igac.gov.co:2102` for single-base / per-station mountpoints
5. Use issued username/password and standard NTRIP client (with NMEA GGA upstream for VRS/IMAX mountpoints flagged NMEA=1)

## Network Details

- **Platform**: Leica Spider Business Center (SBC) — Leica's CORS network management software, version 7.11.0.115 (login portal); NTRIP caster software Spider 7.11.0.96
- **Reference frame**: MAGNA-SIRGAS (Colombia's national geodetic reference frame; ITRF-aligned; ECO = Estaciones Continuas Operativas)
- **Stations (current 2026)**: 143 single-station mountpoints active on port 2102 (127 unique physical coordinates after deduplication of variants); IGAC publicly cites ~237 CORS as of late 2023, ~260 by end-2024 (expansion ongoing). The discrepancy between 237 declared and 127 unique-on-port-2102 reflects a mix of (a) IGAC + SGC GeoRED + densification stations not all advertised on the public NTRIP caster, (b) some stations listed in metadata but not yet streaming, and (c) duplicates per mountpoint format. The public NTRIP service reflects ~127 streaming stations as of 2026-05-07.
- **Coverage**: Three regional network cells advertised — `LLANOS_RTCM3` (eastern plains, ~3.38°N/74.05°W), `SUR_OESTE_RTCM3` (southwest, ~1.21°N/77.28°W around Pasto/Nariño), `NOROESTE_RTCM3` (northwest, ~10.11°N/74.52°W around Caribbean coast); plus the main VRS network at the Bogotá control centre (~4.69°N/74.14°W). Coverage is denser in the Andean corridor (Bogotá–Medellín–Cali) and Caribbean coast; sparser in Amazon/Orinoco basins.
- **Constellations**: GPS, GLONASS, Galileo, BeiDou (Leica GR50 multi-constellation receivers; AR20 antennas on 2024 densification batch)
- **Services offered**: Real-time NTRIP, VRS (network RTK), online PPP via Centro de Control Geodésico, RINEX post-processing download

## Most Recent Public Announcement (date + URL)

- **Resolución IGAC 1771 de 2024** — officialized `redgeodesica.igac.gov.co` as the National Geodetic Network portal (https://www.igac.gov.co/transparencia-y-acceso-a-la-informacion-publica/normograma/resolucion-1771-de-2024)
- **April 2024** — Centro de Control Geodésico Nacional formally launched at SIRGAS conference (presentation: `https://sirgas.ipgh.org/wp-content/uploads/2024/05/IGAC-Colombia-RT.pdf`)
- **December 2023** — IGAC announcement of 23 new CORS stations for cadastral support: `https://www.igac.gov.co/noticias/hay-23-nuevas-estaciones-para-la-red-geodesica-del-pais-su-informacion-es-util-para-el-catastro-multiproposito`
- **2022–2024** — 39 new stations materialized via Cuatro Conceptos contract; 26 stations installed in priority cadastral-deficient municipalities (Revista Geodata edición 5)

## Context Notes

- **Free since 2024**: IGAC formally launched the Centro de Control Geodésico Nacional in April 2024, consolidating real-time NTRIP/VRS services under a single Leica SBC platform. Corrections are explicitly free of charge, mandated by Law 1955/2019 as part of national spatial data infrastructure. Status as the first confirmed free national VRS in Latin America stands as of 2026-05-07.
- **Independent network — Servicio Geológico Colombiano GeoRED**: SGC operates 105+ permanent GNSS stations under the GeoRED program (geored2.sgc.gov.co), used for geodynamic monitoring (volcano/earthquake research). GeoRED data is processed in ITRF2014 via NASA Gipsy-X but is **post-processing only** — no real-time NTRIP service is publicly documented for GeoRED. Some SGC stations may feed into the IGAC SBC network as part of the "237 stations IGAC + SGC property" total.
- **Cross-border commercial — Topored (rejected for hobbyist)**: Casa del Topógrafo's Topored network (28 stations across Panama and Colombia, control centre in Bogotá) emits commercial NTRIP corrections covering parts of Colombian territory. Pricing not publicly listed; documented in `docs/networks.md` as `topored_pa` with status=rejected. Not a free hobbyist alternative.
- **No volunteer alternative**: rtk2go has zero confirmed CO-coded bases (verified against `data/rtk2go.sourcetable` 2026 archives); Centipede has zero CO nodes. Two CO-coded stations appear via EarthScope NOTA cross-listing but are not RTK-streaming for public use.
- **Hobbyist hardware compatibility**: VRS mountpoints require RTCM 3 MSM (preferred) or legacy RTCM 3 — supported by all modern dual-frequency GNSS receivers (u-blox ZED-F9P, Septentrio mosaic-X5, Trimble, Leica, Topcon, ArduSimple kits). DGPS-only legacy mountpoints (RTCM 2 GPS-only) are usable by older single-frequency rovers but only deliver decimeter accuracy.
- **NMEA GGA**: Network-solution mountpoints (`MSM_VIRS`, `MSM_IMAX`, `RTCM3_VIRS`, `RTCM3_IMAX`, etc.) require the rover to upstream periodic NMEA GGA position messages — standard NTRIP behavior. Single-station mountpoints on port 2102 do not require NMEA upstream.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost | Notes |
|---|---|---|---|
| **IGAC CORS RINEX archive** — daily 30-second RINEX 2.11 and 3.0 files from MAGNA-ECO stations, available via SBC portal after login | https://redgeodesica-sbc.igac.gov.co/sbc | Free (account required) | 15-second sampling for some stations |
| **SIRGAS regional archive** — includes Colombian CORS stations contributed to SIRGAS-CON | https://sirgas.ipgh.org/ | Free | Wider Latin American context |
| **SGC GeoRED archive** — separate SGC network for geodynamic monitoring | https://geored2.sgc.gov.co/ | Free | Post-processing only; ITRF2014 |
| **EarthScope NOTA** — handful of CO stations cross-listed | https://www.unavco.org/data/ | Free | Limited to NOTA-affiliated stations |

## Sources Consulted
- IGAC Red Geodésica Nacional portal: https://redgeodesica.igac.gov.co/ (observed 2026-05-07; HTTP 200)
- IGAC NTRIP services description: https://redgeodesica.igac.gov.co/herramientas/servicios.html (observed 2026-05-07; states host:port and free access)
- IGAC Centro de Control Geodésico (Azure-hosted mirror): https://igac-cc.azurewebsites.net/ (observed 2026-05-07; ECONNREFUSED from research env, but listed via search results)
- Spider Business Center login: https://redgeodesica-sbc.igac.gov.co/sbc (Leica SBC v7.11.0.115; HTTP 200; 31+ language UI)
- Spider Business Center registration: https://redgeodesica-sbc.igac.gov.co/sbc/Account/Register
- Direct sourcetable fetches (research env, 2026-05-07): `http://sbc.igac.gov.co:2101/` (20 STR mountpoints, network/VRS) and `http://sbc.igac.gov.co:2102/` (143 STR mountpoints, single-base; 127 unique coords)
- Resolución IGAC 1771 de 2024: https://www.igac.gov.co/transparencia-y-acceso-a-la-informacion-publica/normograma/resolucion-1771-de-2024
- IGAC Geodesia FAQ: https://www.igac.gov.co/el-igac/areas-estrategicas/direccion-de-gestion-de-informacion-geografica/geodesia/preguntas-frecuentes-geodesia
- SIRGAS Colombia RT presentation (Apr 2024): https://sirgas.ipgh.org/wp-content/uploads/2024/05/IGAC-Colombia-RT.pdf
- Revista Geodata — MAGNA-ECO densification: https://revistageodata.icde.gov.co/edicion-5/red-geodesica-nacional-activa-magna-eco-densificacion-y-cobertura-de-estaciones-cors-en
- IGAC 23 nuevas estaciones (2023-12 announcement): https://www.igac.gov.co/noticias/hay-23-nuevas-estaciones-para-la-red-geodesica-del-pais-su-informacion-es-util-para-el-catastro-multiproposito
- IGAC MAGNA-ECO procedure manual (PDF): https://www.igac.gov.co/sites/default/files/listadomaestro/p30100-05-18.v4_red_estaciones_contin_marco_geocentrico_nal_magna_eco_0.pdf
- Servicio Geológico Colombiano GeoRED: https://geored2.sgc.gov.co/
- ArduSimple Colombia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-colombia/
- Contact: contactenos@igac.gov.co / +57 601 653 18 88

## Known Data Gaps
- **Foreign-resident registration outcome**: The SBC registration form accepts non-Colombian ID types in principle, but no public confirmation that IGAC approves foreign-passport-only subscriptions. Worth a real-world test or direct contact with `contactenos@igac.gov.co`.
- **GeoRED real-time**: Whether SGC plans to expose any GeoRED stations via NTRIP (rather than post-processing only) is not publicly documented. SGC has not announced an NTRIP caster.
- **Station count reconciliation**: IGAC documents cite ~237 CORS (IGAC + SGC) but only ~127 unique physical coordinates are advertised on the public NTRIP caster (port 2102). The gap likely reflects post-processing-only stations and SGC stations not piped into the IGAC RTK service.
