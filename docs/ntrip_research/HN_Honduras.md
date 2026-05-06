# Honduras [HN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: No NTRIP caster — government CORS is post-processing RINEX only

| Field | Value |
|---|---|
| **Active NTRIP RTK caster** | No |
| **Government CORS network** | Yes — IP/DGCG 5-station network; RINEX post-processing only |
| **hobbyist_eligibility** | N/A — no real-time service exists |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | `cors.ip.gob.hn` web portal confirmed reachable 2026-05-06 (HTTP 200 via search index); RINEX data service only |

---

## Government CORS Network — IP/DGCG

The **Instituto de la Propiedad (IP)**, through its sub-directorate the **Dirección General de Cartografía y Geografía (DGCG)**, operates Honduras's national CORS network and geodetic infrastructure. The same institution is also marketed under the brand **IGN Honduras** (`ign.hn`) — this is not a separate agency; both IP/DGCG and IGN Honduras refer to the same 5-station network.

| Field | Value |
|---|---|
| **Portal** | `cors.ip.gob.hn` |
| **Stations** | 5 — Tegucigalpa, San Pedro Sula, Juticalpa, Siguatepeque, La Ceiba |
| **Service type** | RINEX data download (post-processing); no real-time NTRIP streaming |
| **host:port** | None found — no NTRIP caster endpoint is publicly documented |
| **Access** | Free RINEX download with account registration at the portal |
| **Datum** | WGS 84 (legislated since 2000 cartographic conventions) |

The IP/DGCG portal explicitly lists RINEX file download as the service; no self-service NTRIP registration, caster hostname, or credentials were found on the IP, DGCG, or IGN Honduras websites. The IP FAQ for Cartography and Geography (`ip.gob.hn/preguntas_frecuente_catastro`) describes geodetic inquiry procedures but makes no mention of real-time RTK corrections.

---

## Volunteer and Commercial Options

| Source | Status |
|---|---|
| **rtk2go** | Zero HN-coded stations as of 2026-05-06 |
| **Centipede** | Zero HN nodes as of 2026-05-06 |
| **Commercial NTRIP** | No commercial NTRIP provider lists Honduras coverage on public-facing product pages (NTRIP-list.com, ArduSimple country directory, Point One, GEODNET, RTKdata directories all absent for HN) |

---

## Most Recent Project Announcement

No announcement of a planned Honduras NTRIP / real-time RTK service was found. The 5-station IP/DGCG network appears to have operated as a post-processing RINEX service since its establishment; the most recent public information confirms this RINEX-only status.

**Regional context**: Central American neighbours El Salvador (Survey3G commercial network) and Costa Rica (IGN-CR free national caster) have real-time services; Honduras has no equivalent. Guatemala and Nicaragua are similarly RINEX-only as of 2026-05-06. No SIRGAS real-time stream for HN was found.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IP/DGCG CORS** — 5-station RINEX archive | https://cors.ip.gob.hn/ | Free with account registration |

---

## Sources Consulted
- IP/DGCG CORS portal: https://cors.ip.gob.hn/
- Instituto de la Propiedad main site: https://www.ip.gob.hn/
- IP Cartography and Geography FAQ: https://www.ip.gob.hn/preguntas_frecuente_catastro
- IP Cartography and Geography services: https://www.ip.gob.hn/direcciones/cartografia-geografia/tramites-cartografia-y-geografia
- NTRIP-list.com North America: https://ntrip-list.com/north-america/
- ArduSimple RTK correction services country directory: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2go / Centipede sourcetables — no HN stations found
