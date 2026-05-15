# Honduras [HN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (updated 2026-05-12: `cors.ip.gob.hn` re-verified HTTP 200; portal links only to `ftp://ceiba.ip.gob.hn` for archive download — no NTRIP endpoint)

## Status: No NTRIP caster — government CORS is post-processing RINEX only (FTP archive)

| Field | Value |
|---|---|
| **Active NTRIP RTK caster** | No |
| **landing_url — IP/DGCG CORS** | `https://cors.ip.gob.hn/` — operator-owned portal (Instituto de la Propiedad / Dirección General de Cartografía y Geografía). Describes the 5-station network and the FTP RINEX archive (not a bare login). Self-signed cert — TLS verification fails on some Windows stacks; HTTP works. |
| **access_url — IP/DGCG CORS** | Skip — landing_url already conveys the (FTP archive) access path; no separate registration page exists. The IP parent dir's cartography services page `https://www.ip.gob.hn/direcciones/cartografia-geografia/tramites-cartografia-y-geografia` is an alternative if a non-cors.ip.gob.hn URL is preferred. |
| **Government CORS network** | Yes — IP/DGCG 5-station network; RINEX post-processing only via FTP archive `ftp://ceiba.ip.gob.hn` (linked from the cors.ip.gob.hn "Descargar Archivos" portal; the portal even instructs users to enable browser FTP downloads — `chrome://flags/#enable-ftp` / `edge://flags/#enable-ftp`) |
| **hobbyist_eligibility** | N/A — no real-time service exists |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | 2026-05-12 — `http://cors.ip.gob.hn/` returned HTTP 200 (Content-Length 35349; Last-Modified 2022-05-26 — portal HTML has not changed in ~4 years, suggesting stable but stagnant operation); RINEX data service only via FTP |

---

## Government CORS Network — IP/DGCG

The **Instituto de la Propiedad (IP)**, through its sub-directorate the **Dirección General de Cartografía y Geografía (DGCG)**, operates Honduras's national CORS network and geodetic infrastructure. The same institution is also marketed under the brand **IGN Honduras** (`ign.hn`) — this is not a separate agency; both IP/DGCG and IGN Honduras refer to the same 5-station network.

| Field | Value |
|---|---|
| **Portal** | `https://cors.ip.gob.hn/` (self-signed certificate — connection works on the open Internet but the certificate verification fails on common Windows TLS stacks) |
| **Archive endpoint** | `ftp://ceiba.ip.gob.hn` — anonymous FTP for RINEX download; the portal explicitly tells users to enable FTP in Chrome (`chrome://flags/#enable-ftp`) or Edge (`edge://flags/#enable-ftp`) before clicking "Descargar Archivos" |
| **Stations** | 5 — Tegucigalpa, San Pedro Sula, Juticalpa, Siguatepeque, La Ceiba (per prior research; portal HTML lists no station-by-station metadata) |
| **Service type** | RINEX data download (post-processing) via FTP only; no real-time NTRIP streaming |
| **host:port** | None found — no NTRIP caster endpoint is publicly documented |
| **Access** | Free RINEX download via FTP; no account registration evidenced in current portal HTML (FTP is openly reachable per portal instructions) |
| **Datum** | WGS 84 (legislated since 2000 cartographic conventions) |

The IP/DGCG portal explicitly lists RINEX file download as the service; no self-service NTRIP registration, caster hostname, or credentials were found on the IP, DGCG, or IGN Honduras websites. The IP FAQ for Cartography and Geography (`ip.gob.hn/preguntas_frecuente_catastro`) describes geodetic inquiry procedures but makes no mention of real-time RTK corrections.

---

## Volunteer and Commercial Options

| Source | Status |
|---|---|
| **rtk2go** | Zero HN-coded stations as of 2026-05-12 (`stations_by_country.py HND` returns "No stations") |
| **Centipede** | Zero HN nodes as of 2026-05-12 |
| **EarthScope (COCONet)** | 4 stations in `earthscope` source, all archive-only RINEX (CN18, CN21, ROA0, TEG2 — Bay Islands and Tegucigalpa); not a real-time RTK service |
| **Commercial NTRIP** | No commercial NTRIP provider lists Honduras coverage on public-facing product pages (NTRIP-list.com, ArduSimple country directory, Point One, GEODNET, RTKdata directories all absent for HN) |

---

## Most Recent Project Announcement

No announcement of a planned Honduras NTRIP / real-time RTK service was found. The 5-station IP/DGCG network appears to have operated as a post-processing RINEX service since its establishment; the most recent public information confirms this RINEX-only status.

**Regional context**: Central American neighbours El Salvador (Survey3G commercial network) and Costa Rica (IGN-CR free national caster) have real-time services; Honduras has no equivalent. Guatemala and Nicaragua are similarly RINEX-only as of 2026-05-06. No SIRGAS real-time stream for HN was found.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IP/DGCG CORS** — 5-station RINEX archive (FTP) | https://cors.ip.gob.hn/ → `ftp://ceiba.ip.gob.hn` | Free; FTP must be enabled in browser flags |
| **EarthScope COCONet** — CN18, CN21, ROA0, TEG2 (Honduras archival RINEX) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

---

## Sources Consulted
- IP/DGCG CORS portal: https://cors.ip.gob.hn/
- Instituto de la Propiedad main site: https://www.ip.gob.hn/
- IP Cartography and Geography FAQ: https://www.ip.gob.hn/preguntas_frecuente_catastro
- IP Cartography and Geography services: https://www.ip.gob.hn/direcciones/cartografia-geografia/tramites-cartografia-y-geografia
- NTRIP-list.com North America: https://ntrip-list.com/north-america/
- ArduSimple RTK correction services country directory: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2go / Centipede sourcetables — no HN stations found
