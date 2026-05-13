# Panama [PA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh; prior pass 2026-05-06)

## Status: One private commercial NTRIP caster (TOPORED, equipment-tied) + government IGNTG CORS being modernised (no public NTRIP exposed yet) + 5 EarthScope/NOTA streams in country

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (commercial — TOPORED, equipment-gated; see notes) |
| **EarthScope (NOTA) real-time streams in Panama** | 5 stations served by the EarthScope caster (`rtgpsout.unavco.org:2101`): `ACHO_RTCM3P3` (7.41°N, −80.17°W), `CN20_RTCM3P3` (9.35°N, −82.26°W, near Bocas del Toro), `CN55_RTCM3P3` (8.24°N, −80.54°W), `CN60_RTCM3P3` (8.63°N, −79.03°W, near Panama City), `PTPP_RTCM3P3` (8.20°N, −82.88°W, near David). RTCM 3 MSM5. Free non-commercial via NULA. |
| **host:port — TOPORED** | Not publicly disclosed (port 2101 refused connection on 2026-05-12); website `panama.casadeltopografo.com` was unresponsive to direct curl from the research sandbox 2026-05-12 (timeouts; may be IP-geofenced or Cloudflare-blocking). Per ArduSimple and Casa del Topógrafo Facebook page, credentials are issued to equipment purchasers. |
| **tariff — TOPORED** | Not published; access bundled with GNSS equipment purchase from Casa del Topógrafo; standalone subscription pricing not found as of 2026-05-12 |
| **tariff — EarthScope** | Free non-commercial after NULA; USD 1,000/seat/yr commercial |
| **hobbyist_eligibility** | TOPORED: unclear — exclusive to customers who purchase GNSS equipment from Casa del Topógrafo. EarthScope: yes (non-commercial). |
| **legal_residency_required** | TOPORED: unclear — equipment-purchase gate applies. EarthScope: no. |
| **last_confirmed_alive** | TOPORED web page reported live 2026-05-06; 2026-05-12 fetch from sandbox timed out (inconclusive — not necessarily down). EarthScope NOTA streams in `data/stations.json` (5 PAN stations) as of 2026-05-12. |

## Active Caster: TOPORED (Casa del Topógrafo Panama)

**Operator:** Casa del Topógrafo Panama
**Web:** https://panama.casadeltopografo.com/topored/
**Network size:** 28 reference stations across Panama and Colombia (6 stations specifically covering Panama); control centre in Bogotá, Colombia
**Protocol:** NTRIP with RTCM differential corrections — RTK method supported with a single rover
**RINEX post-processing:** Available to registered account holders
**Access model:** Access to RTK corrections is described as exclusive to customers who purchase GNSS equipment through Casa del Topógrafo; no evidence of an open standalone NTRIP subscription tariff was found in any public source as of 2026-05-06
**Source URL:** https://panama.casadeltopografo.com/topored/ ; Facebook: https://www.facebook.com/Casadeltopografo/

## IGNTG Government CORS Network (post-processing / research — not confirmed as public NTRIP RTK)

The Instituto Geográfico Nacional "Tommy Guardia" (IGNTG), a division of ANATI, operates a 19-station national CORS network. Seven stations (IGN1, AZUE, DAVI, DARI, PUAR, PMEC, CHEP) are part of SIRGAS-CON and have internet connectivity. The 2025 Modernisation Project (announced January 2025) reactivated 8 previously inoperative stations (receiver damage) and planned site inspections at all 19 stations.

- RTK radios were physically installed at stations AZUE and DAVI for real-time positioning.
- **September 2025 update**: IGNTG announced acquisition and installation of 6 new CORS antennas to support the Panama–David railway, Metro de Panamá and other infrastructure works. The Geodesy and Geophysics Department reported software upgrades on TDC600 field controllers. The network is described as "operating almost in its entirety". No NTRIP endpoint, mountpoint list or public registration mechanism was disclosed in the announcement.
- No public NTRIP endpoint (host:port), access registration page, or credential instructions for IGNTG have been published.
- All public references describe IGNTG CORS as serving geodetic reference frame maintenance, cadastre, and scientific research — **not** as a publicly accessible RTK correction service.
- Most Recent Project Announcements:
  - January 2025: "Inició el proceso de mantenimiento, actualización y mejora de la red CORS" — https://ignpanama.anati.gob.pa/index.php/mnoticias/322-proyecto-de-modernizacion-2025-del-instituto-geografico-nacional-tommy-guardia
  - September 2025: "Instituto 'Tommy Guardia' refuerza Red Geodésica de cara a megaproyecto ferroviario" — https://destinopanama.com.pa/2025/09/instituto-tommy-guardia-refuerza-red-geodesica-de-cara-a-megaproyecto-ferroviario/

## Context Notes

- **TOPORED** is the only positively identified operating NTRIP RTK caster covering Panama territory as of 2026-05-06. It is a private commercial network, not a government public service.
- TOPORED's access gate (equipment purchase) makes it functionally inaccessible to hobbyists who have not bought surveying gear from Casa del Topógrafo. No standalone subscription or open-user program was found.
- **ArduSimple** (July 2024 page) explicitly states Panama has no established National RTK Network — consistent with IGNTG not operating a publicly accessible NTRIP service.
- **IGNTG CORS**: Useful for post-processing geodetic work via SIRGAS-CON data archives; RINEX data retrievable via EarthScope / UNAVCO for stations in the SIRGAS-CON tier.
- **GEODNET / ONOCOY / Centipede-RTK**: No confirmed coverage in Panama found.
- **RTK2go**: No Panama-registered mountpoints (confirmed via `scripts/stations_by_country.py PAN` 2026-05-12 — no PAN tag under rtk2go).
- **EarthScope/NOTA real-time**: 5 streams in country (ACHO, CN20, CN55, CN60, PTPP — RTCM 3 MSM5 on `rtgpsout.unavco.org:2101`). With baselines mostly ≤80 km between them, single-base RTK fixes are realistic for much of central/western Panama. This is the **only free real-time path for hobbyists in Panama**.
- Practical workaround for hobbyists outside EarthScope baseline: Deploy a local base station for single-base RTK, or use satellite-based PPP services (Trimble RTX, u-blox PointPerfect where available, Galileo HAS).

## Real-Time + Post-Processing Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope/NOTA real-time NTRIP** — 5 PAN mountpoints (ACHO, CN20, CN55, CN60, PTPP — RTCM 3 MSM5) on `rtgpsout.unavco.org:2101` | https://www.earthscope.org/data/gnss-data/real-time/ | Free non-commercial (NULA); USD 1,000/seat/yr commercial |
| **EarthScope GNSS Data Archive / SIRGAS-CON** — IGN1, AZUE, DAVI, DARI, PUAR, PMEC, CHEP stations; archival RINEX from SIRGAS-CON analysis | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |
| **TOPORED (Casa del Topógrafo)** — static RINEX from 6 Panama CORS | https://panama.casadeltopografo.com/topored/ | Requires account; pricing not published |

## Sources Consulted
- ArduSimple Panama RTK correction services page (ardusimple.com/rtk-correction-services-and-ntrip-casters-in-panama/, last updated July 2024)
- IGNTG CORS page (ignpanama.anati.gob.pa/index.php/cors)
- IGNTG CORS densification page (ignpanama.anati.gob.pa/index.php/2-uncategorised/63-densificacion-cors)
- IGNTG 2025 Modernisation Project news (ignpanama.anati.gob.pa/index.php/mnoticias/322-proyecto-de-modernizacion-2025-del-instituto-geografico-nacional-tommy-guardia)
- Casa del Topógrafo Panama — TOPORED page (panama.casadeltopografo.com/topored/)
- Casa del Topógrafo Facebook (facebook.com/Casadeltopografo/)
- SIRGAS Bulletin 9 — IGNTG Panama CORS (sirgas.org)
- SIRGAS Bulletin 12 — Estaciones permanentes Panama Cornejo (sirgas.org)
- SIRGAS-RT NTRIP paper (sirgas.ipgh.org)
- NTRIP-list.com North America / South America pages
- GEODNET coverage map (rtk.geodnet.com/coverage/)
- RTK2go SNIP monitor (monitor.use-snip.com)
- EarthScope/UNAVCO GNSS Data Archive
- Destino Panamá (Sept 2025) — IGNTG 6 new CORS antennas: https://destinopanama.com.pa/2025/09/instituto-tommy-guardia-refuerza-red-geodesica-de-cara-a-megaproyecto-ferroviario/
- ANATI press release (Apr 2025) — IGNTG capacity strengthening: https://www.anati.gob.pa/index.php/noticias/801-instituto-geografico-nacional-tommy-guardia-fortalece-sus-capacidades-tecnicas-para-la-generacion-de-informacion-geoespacial
- curl probe `panama.casadeltopografo.com:443` 2026-05-12 — connection established but no HTTP response within 10s (inconclusive; likely Cloudflare-/geofence-related, not necessarily caster downtime)
- Local pipeline check `scripts/stations_by_country.py PAN` (2026-05-12) — earthscope source returns 5 stations: ACHO, CN20, CN55, CN60, PTPP
