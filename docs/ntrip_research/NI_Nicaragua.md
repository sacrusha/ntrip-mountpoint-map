# Nicaragua [NI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: No NTRIP caster — government CORS is post-processing RINEX only

| Field | Value |
|---|---|
| **Active NTRIP RTK caster** | No |
| **Government CORS network** | Yes — INETER CORS; RINEX post-processing only |
| **hobbyist_eligibility** | N/A — no real-time service exists |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | `consultacf.ineter.gob.ni` portal confirmed reachable 2026-05-06 (search index HTTP 200); RINEX data service only |

---

## Government CORS Network — INETER

The **Instituto Nicaragüense de Estudios Territoriales (INETER)**, through its **Dirección General de Geodesia y Cartografía**, maintains Nicaragua's geodetic infrastructure including a network of continuously operating GNSS stations.

| Field | Value |
|---|---|
| **Portal** | `consultacf.ineter.gob.ni` (Catastro Físico — physical cadastre portal) |
| **Geodesy page** | `ineter.gob.ni/geodesiaycartografia.html` |
| **Service type** | RINEX data download (post-processing); no real-time NTRIP streaming publicly documented |
| **host:port** | None found — no NTRIP caster endpoint is publicly documented |
| **Access** | RINEX data accessible via the Catastro Físico portal |

INETER's Dirección General de Geodesia y Cartografía describes its mandate as collecting and maintaining fundamental geospatial data for the National Coordinate System (Sistema Nacional de Coordenadas) and the national Spatial Data Infrastructure (IDE — Infraestructura de Datos Espaciales). The INETER and IDE portal (`mapserveride.ineter.gob.ni/IDE-BCN/`) provide cartographic data services. No self-service NTRIP registration, caster hostname, or real-time RTK product was found on any INETER or affiliated portal.

INETER also operates a seismic and geophysical monitoring network with GPS-synchronised time reference stations (`webserver2.ineter.gob.ni`) — these are seismic monitoring sensors, not geodetic CORS for positioning.

---

## Volunteer and Commercial Options

| Source | Status |
|---|---|
| **rtk2go** | Zero NI-coded stations as of 2026-05-06 |
| **Centipede** | Zero NI nodes as of 2026-05-06 |
| **Commercial NTRIP** | No commercial NTRIP provider lists Nicaragua coverage on public-facing product pages (NTRIP-list.com, ArduSimple country directory, Point One, GEODNET, RTKdata directories all absent for NI) |

---

## Most Recent Project Announcement

No announcement of a planned Nicaragua NTRIP / real-time RTK service was found as of 2026-05-06. INETER's geodetic pages describe post-processing methodology; no real-time correction roadmap was found.

**Regional context**: El Salvador (commercial Survey3G) and Costa Rica (IGN-CR free national caster) have real-time NTRIP services in the same Central American corridor; Honduras and Nicaragua remain RINEX-only. No SIRGAS real-time stream for NI was found.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **INETER Catastro Físico** — GNSS/RINEX data download | https://consultacf.ineter.gob.ni/ | Free (account/request basis) |
| **INETER IDE/BCN** — national cartographic base | https://mapserveride.ineter.gob.ni/IDE-BCN/ | Free viewer |

---

## Sources Consulted
- INETER Geodesia y Cartografía: https://www.ineter.gob.ni/geodesiaycartografia.html
- INETER Catastro Físico portal: https://consultacf.ineter.gob.ni/
- INETER main site: https://www.ineter.gob.ni/
- INETER IDE Base Cartográfica Nacional: https://mapserveride.ineter.gob.ni/IDE-BCN/
- NTRIP-list.com North America: https://ntrip-list.com/north-america/
- ArduSimple RTK correction services country directory: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2go / Centipede sourcetables — no NI stations found
