# Paraguay [PY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (prior version: 2026-05-06)

## Status: NO confirmed active NTRIP caster for Paraguay

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No confirmed caster found |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no caster has been confirmed alive |

## Most Recent Project Announcement

No formal project announcement for a Paraguay national NTRIP/RTK caster was found in any government, development-bank, UN, SIRGAS, or geospatial trade-press source as of 2026-05-06.

## Context Notes

- **GEOEQUIPOS SRL correction:** The prior research version of this file listed GEOEQUIPOS SRL (geoequipossrl.com) as a Paraguayan CORS/NTRIP operator. This is incorrect. WebFetch of geoequipossrl.com confirmed the company address is Calle Pinilla 2588, La Paz, **Bolivia** (+591 78866188). The company is a Bolivian geomatics equipment and services firm and is not a Paraguay NTRIP provider. Their Red CORS page exists but refers to Bolivia.
- **Geodesical Paraguay** (geodesicalparaguay.com; Ruta 3 esq. Capitán Meza, Limpio, Paraguay): Equipment retailer and reseller (GPS receivers, total stations, software). No CORS network or NTRIP correction service operated. Contact: info@geodesicalparaguay.com / (021) 781 031.
- **DINAC** (Dirección Nacional de Aeronáutica Civil): Manages aviation GNSS reference stations in Paraguay; no public NTRIP stream found in any registry.
- **STP / DGEEC**: Paraguay's Secretaría Técnica de Planificación operates geo.stp.gov.py for statistical geodata; no CORS or NTRIP service.
- **SNC (Servicio Nacional de Catastro)**: Under the Ministry of Economy and Finance; responsible for the national cadastre. Adopts the cartographic system based on military Geographic Service products. No CORS/NTRIP service operated; no public reference station network announcement found (websearch 2026-05-12 — catastro.gov.py).
- **SIRGAS**: Paraguay has at least one SIRGAS-CON-affiliated station (Asunción, 4-character code typically rendered as ASUN in IGS/SIRGAS publications) but is not listed as a SIRGAS-RT caster node. The SIRGAS-RT network (casters in Argentina, Brazil, Uruguay, Venezuela) does not extend to Paraguay as of May 2026.
- No commercial CORS/RTK network has been identified for Paraguay in surveying industry directories, ArduSimple country pages, NTRIP-list.com, rtcm-ntrip.org, RTK2go, or Centipede-RTK sourcetables (re-checked 2026-05-12).
- Local project data: `py scripts/stations_by_country.py PRY` returns 3 rtk2go bases (NPPCentralTorre at -21.08, -60.32; NPPPetronaTorre at -21.07, -60.21; SenioRTK at -25.23, -54.70). All three are volunteer single-base streams — no Centipede / EarthScope PY stations.
- Paraguay's RTK infrastructure is underdeveloped relative to neighboring Argentina, Brazil, and Uruguay, which have mature national CORS networks.
- **curl probe of geoequipossrl.com:2101** — not executable: shell tools unavailable in this session (would expect timeout or refused for a Bolivian host).
- **Practical workaround for hobbyists:** Deploy a local base station, or use satellite-based PPP (Galileo HAS ~40 cm, Trimble RTX). GEODNET and Onocoy: no confirmed Paraguay coverage in public station maps.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SIRGAS station data** | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |
| **IGS / EarthScope GNSS archive** (any IGS stations in Paraguay) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

## Sources Consulted
- GEOEQUIPOS SRL website: https://geoequipossrl.com/ — confirmed address La Paz, Bolivia; not a Paraguay company (2026-05-06)
- GEOEQUIPOS SRL Red CORS page: https://geoequipossrl.com/red-cors/ — contact info@geoequipossrl.com; no pricing or host:port published (2026-05-06)
- curl probe of `geoequipossrl.com:2101` — not executable: shell tools unavailable in this session
- Geodesical Paraguay: https://geodesicalparaguay.com/ — equipment retailer only; no NTRIP service (2026-05-06)
- SIRGAS-RT bulletins (sirgas.ipgh.org)
- NTRIP-list.com South America (no Paraguay entries)
- rtcm-ntrip.org (no Paraguay entries)
- RTK2go monitor (monitor.use-snip.com) — no Paraguay stations
- ArduSimple country search — no Paraguay-specific page found
- WebSearch queries in Spanish: "Paraguay CORS GNSS NTRIP correcciones tiempo real" — no active provider identified (2026-05-06)
- WebSearch "Paraguay red CORS estaciones permanentes GNSS MOPC SNC IPA 2025 2026" — no result identifying any Paraguay national CORS network (2026-05-12)
- SNC (Servicio Nacional de Catastro): https://www.catastro.gov.py/ — no CORS or NTRIP service mentioned (2026-05-12)
- SIRGAS station list: https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ — Asunción SIRGAS-CON station referenced; no SIRGAS-RT caster in Paraguay (2026-05-12)
- Local: `py scripts/stations_by_country.py PRY` — 3 rtk2go bases (2026-05-12)
