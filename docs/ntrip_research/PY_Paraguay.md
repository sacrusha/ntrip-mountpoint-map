# Paraguay [PY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

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
- **SIRGAS**: Paraguay has at least one SIRGAS station (specific 4-character station code not confirmed via public search — check sirgas.ipgh.org station list) but is not listed as a SIRGAS-RT caster node. The SIRGAS-RT network (casters in Argentina, Brazil, Uruguay, Venezuela) does not extend to Paraguay as of 2026.
- No commercial CORS/RTK network has been identified for Paraguay in surveying industry directories, ArduSimple country pages, NTRIP-list.com, rtcm-ntrip.org, RTK2go, or Centipede-RTK sourcetables.
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
