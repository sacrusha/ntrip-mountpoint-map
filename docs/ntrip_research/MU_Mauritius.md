# Mauritius [MU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (re-verified; no operational caster found; status unchanged from 2026-05-06)

## Status: NO confirmed public NTRIP caster; CORS feasibility studied 2016; no operational deployment found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — no public host:port found; feasibility workshop held 2016 but no operational caster confirmed since |
| **Operator** | Survey Division, Ministry of Housing and Land Use Planning, Ebène (`housing.govmu.org`) |
| **host:port** | Not publicly listed |
| **tariff** | n/a (no public service) |
| **hobbyist_eligibility** | n/a |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | housing.govmu.org reachable 2026-05-12; no MU mountpoint in any public NTRIP sourcetable; nearest Centipede stations are in Réunion (~220 km east, FR territory) and Madagascar (>1000 km west) — both too far for RTK from Mauritius |

## Operator

**Survey Division**
Ministry of Housing and Land Use Planning
7th Floor, Emmanuel Anquetil Building, Port Louis / Ebène, Mauritius
Website: https://housing.govmu.org/Pages/Dept%20and%20Org/Divisions/Survey/Survey.aspx

## Context

- **National geodetic authority:** The Survey Division is responsible for land survey, cadastral implementation, and cartography for Mauritius (main island + Rodrigues, Agaléga, etc.).
- **2016 RCMRD feasibility workshop:** A May 2016 workshop hosted at the Ministry in Ebène, facilitated by RCMRD (Regional Centre for Mapping of Resources for Development, Nairobi), examined establishing a CORS network. Approximately 40 participants from government ministries and private sector attended. The workshop assessed infrastructure requirements, standards, and funding pathways for a national GNSS reference network. No evidence of an operational public NTRIP caster has been confirmed since.
- **IGS stations:** No IGS continuously operating reference station is confirmed in Mauritius proper. The closest IGS stations are in Réunion (REUN00REU) and the Seychelles (SEY200SYC) — both ~1,000+ km away, too far for RTK corrections.
- **Territory size:** Main island ~2,040 km² — a single well-positioned station would theoretically provide full-island RTK coverage; the infrastructure investment threshold is low. The absence of a caster despite the 2016 feasibility study suggests funding or political prioritisation barriers rather than technical ones.
- **GIS platform:** Mauritius has an operational GIS portal (`gis.govmu.org`) suggesting geospatial data infrastructure exists; no GNSS correction service is listed there.
- **RCMRD / AFREF:** No Mauritius-hosted streaming NTRIP endpoint found in RCMRD or AFREF documentation.

## Negative Findings

- RTK2GO / Centipede: Zero MU mountpoints in any public sourcetable (verified 2026-05-12 via `py scripts/stations_by_radius.py -20.2 57.5 1500`; nearest stations are 222 km away on Réunion)
- NTRIP-list.com Africa/Indian Ocean: Mauritius not listed
- ArduSimple country directory: Mauritius not listed with any NTRIP service
- mvarga1989 GNSS CORS list (GitHub): No Mauritius NTRIP endpoint
- No public caster address found in any indexed source as of 2026-05-12

## Most Recent Project Reference

**May 2016 RCMRD CORS feasibility workshop** — the last confirmed public event related to a potential Mauritius CORS. No subsequent launch announcement, tender, or operational caster has been found.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS / EarthScope** — nearest stations: REUN (Réunion) or SEY2 (Seychelles); not practical for RTK | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |

## Sources Consulted
- Survey Division, Ministry of Housing and Lands (Mauritius): https://housing.govmu.org/Pages/Dept%20and%20Org/Divisions/Survey/Survey.aspx
- Mauritius GIS portal: https://gis.govmu.org/SitePages/Index.aspx
- RCMRD — Regional Centre for Mapping of Resources for Development: https://www.rcmrd.org/
- RTK2GO monitor (monitor.use-snip.com) — no MU mountpoints visible
- NTRIP-list.com/africa — Mauritius not listed
- ArduSimple RTK correction services directory — Mauritius not listed
- networks.md entry `survey_mu` (internal): 2016 RCMRD workshop documented, no operational caster since
