# Panama [PA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: Active public NTRIP caster — commercial, equipment-tied

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (commercial; see notes) |
| **host:port** | Not publicly disclosed — contact Casa del Topógrafo directly |
| **tariff** | Not published; access bundled with GNSS equipment purchase from Casa del Topógrafo; standalone subscription pricing not found as of 2026-05-06 |
| **hobbyist_eligibility** | Unclear — TOPORED access described as exclusive to customers who purchase GNSS equipment from Casa del Topógrafo; no open individual subscription confirmed |
| **legal_residency_required** | Unclear — no explicit residency requirement found; equipment-purchase gate applies instead |
| **last_confirmed_alive** | 2026-05-06 — TOPORED page live at panama.casadeltopografo.com/topored/ (Cloudflare-proxied, 200 OK) |

## Active Caster: TOPORED (Casa del Topógrafo Panama)

**Operator:** Casa del Topógrafo Panama
**Web:** https://panama.casadeltopografo.com/topored/
**Network size:** 28 reference stations across Panama and Colombia (6 stations specifically covering Panama); control centre in Bogotá, Colombia
**Protocol:** NTRIP with RTCM differential corrections — RTK method supported with a single rover
**RINEX post-processing:** Available to registered account holders
**Access model:** Access to RTK corrections is described as exclusive to customers who purchase GNSS equipment through Casa del Topógrafo; no evidence of an open standalone NTRIP subscription tariff was found in any public source as of 2026-05-06
**Source URL:** https://panama.casadeltopografo.com/topored/ ; Facebook: https://www.facebook.com/Casadeltopografo/

## IGNTG Government CORS Network (post-processing / research — not confirmed as public NTRIP RTK)

The Instituto Geográfico Nacional "Tommy Guardia" (IGNTG), a division of ANATI, operates a 19-station national CORS network. Seven stations (IGN1, AZUE, DAVI, DARI, PUAR, PMEC, CHEP) are part of SIRGAS-CON and have internet connectivity. The 2025 Modernisation Project (announced January 2025) reactivated 8 previously inoperative stations (receiver damage) and plans site inspections at all 19 stations.

- RTK radios were physically installed at stations AZUE and DAVI for real-time positioning.
- No public NTRIP endpoint (host:port), access registration page, or credential instructions for IGNTG were found in any publicly indexed source.
- All public references describe IGNTG CORS as serving geodetic reference frame maintenance, cadastre, and scientific research — **not** as a publicly accessible RTK correction service.
- Most Recent Project Announcement: "Inició el proceso de mantenimiento, actualización y mejora de la red CORS" — January 2025. URL: https://ignpanama.anati.gob.pa/index.php/mnoticias/322-proyecto-de-modernizacion-2025-del-instituto-geografico-nacional-tommy-guardia

## Context Notes

- **TOPORED** is the only positively identified operating NTRIP RTK caster covering Panama territory as of 2026-05-06. It is a private commercial network, not a government public service.
- TOPORED's access gate (equipment purchase) makes it functionally inaccessible to hobbyists who have not bought surveying gear from Casa del Topógrafo. No standalone subscription or open-user program was found.
- **ArduSimple** (July 2024 page) explicitly states Panama has no established National RTK Network — consistent with IGNTG not operating a publicly accessible NTRIP service.
- **IGNTG CORS**: Useful for post-processing geodetic work via SIRGAS-CON data archives; RINEX data retrievable via EarthScope / UNAVCO for stations in the SIRGAS-CON tier.
- **GEODNET / ONOCOY / Centipede-RTK**: No confirmed coverage in Panama found.
- **RTK2go**: No Panama-registered mountpoints found in community caster searches.
- Practical workaround for hobbyists: Deploy a local base station for single-base RTK, or use satellite-based PPP services (Trimble RTX, u-blox PointPerfect where available).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
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
