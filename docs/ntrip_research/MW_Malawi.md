# Malawi [MW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster; AFREF archive station in Lilongwe (RINEX only)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — no public host:port found; AFREF archive station exists but RINEX-only |
| **Operator** | Department of Surveys, Ministry of Lands (`lands.gov.mw`), Lilongwe |
| **host:port** | Not publicly listed |
| **tariff** | n/a (no public service) |
| **hobbyist_eligibility** | n/a |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | lands.gov.mw reachable 2026-05-06; no MW mountpoint in any public NTRIP sourcetable |

## Operator

**Department of Surveys**
Ministry of Lands
P.O. Box 349, Lilongwe 3, Malawi
Website: https://www.lands.gov.mw/

The Department's Geodetic and Topographic Survey Section is responsible for geodetic control, topographic surveys, and remote sensing. The Department also manages the National Spatial Data Center (NSDC) and the Malawi Spatial Data Portal (MASDAP).

## Known GNSS Infrastructure

- **AFREF / UNAVCO station — Lilongwe (Capitol Hill):** At least one AFREF-affiliated CORS at Lilongwe contributes RINEX observation archives to UNAVCO (now EarthScope). Data available via the GAGE facility archive — not an RTK streaming caster.
- **Malawi Rifting GPS Network:** A research network operated in Malawi under UNAVCO auspices for tectonic monitoring of the East African Rift System. Datasets (DOI: 10.7283/T5J38QW6) are archived at EarthScope. Research-grade archive; not a public RTK service.
- **MASDAP:** The Malawi Spatial Data Portal (masdap.mw) launched 2012 provides geospatial datasets but no GNSS correction streaming.
- **RTK practice:** Based on surveying context for the region, Malawi surveyors typically use base-and-rover RTK setups; no networked CORS caster service has been found.

## Negative Findings

- RTK2GO / Centipede: Zero MW mountpoints in any public sourcetable
- NTRIP-list.com Africa: Malawi not listed
- ArduSimple country directory: Malawi not listed with any NTRIP service
- mvarga1989 GNSS CORS list (GitHub): No Malawi NTRIP endpoint
- AFREF documentation: Lilongwe station confirmed as RINEX archive only; no real-time NTRIP stream
- No public caster address found in any indexed source as of 2026-05-06

## Most Recent Project Reference

No public NTRIP launch announcement or CORS network expansion announcement found for Malawi. The most recent traceable reference is the UNAVCO archive datasets from the Malawi Rifting GPS Network (ongoing passive archiving). Department of Surveys website (lands.gov.mw) does not list any GNSS correction service or NTRIP portal.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope / UNAVCO** — Lilongwe AFREF station + Malawi Rifting GPS Network RINEX archives | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |
| **EarthScope GAGE Archive** — Malawi Rifting GPS Network (DOI: 10.7283/T5J38QW6) | https://www.unavco.org/data/doi/10.7283/T5J38QW6 | Free non-commercial |
| **MASDAP** — Malawi Spatial Data Portal (geospatial datasets, not GNSS corrections) | https://www.masdap.mw/ | Free |

## Sources Consulted
- Department of Surveys, Ministry of Lands (Malawi): https://www.lands.gov.mw/index.php/portfolio/departments-functions/department-of-surveys
- MASDAP — Malawi Spatial Data Portal: https://www.masdap.mw/
- EarthScope / UNAVCO — Malawi Rifting GPS Network: https://www.unavco.org/data/doi/10.7283/T5J38QW6
- EarthScope / UNAVCO — GPS/GNSS data access: https://www.unavco.org/data/gps-gnss/gps-gnss.html
- Malawi government portal: https://www.malawi.gov.mw/
- RTK2GO monitor (monitor.use-snip.com) — no MW mountpoints visible
- NTRIP-list.com/africa — Malawi not listed
- ArduSimple RTK correction services directory — Malawi not listed
