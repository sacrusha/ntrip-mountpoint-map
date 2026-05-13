# Niger [NE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (re-verified; status unchanged from 2026-05-06)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Most Recent Project Announcement

No formal project announcement for a Niger national NTRIP/RTK caster was found in any development-bank (World Bank, AfDB), UN, or geospatial trade press source as of 2026-05-12.

## Context Notes

- **Only known GNSS station**: NIAM (Niamey International Airport, 13.4793°N / 2.1832°E), installed 2005–2006 by IGN France under the AMMA (African Monsoon Multidisciplinary Analysis) project. Purpose is atmospheric water-vapor monitoring (3 years of data 2006–2008 cited as most complete). Per AMMA documentation, data is hosted at http://amma-gps.ign.fr and the station is **not an RTK/NTRIP corrections source**. Station also archived at EarthScope/UNAVCO Spotlight (https://spotlight.unavco.org/station-pages/niam/niam.html) and SONEL (https://www.sonel.org/spip.php?page=gps&idStation=2570).
- **IGNN** (Institut Géographique National du Niger, ignn.ne): Website was defaced/unreachable at time of research (2026-05-06; 2026-05-12 re-check confirms no published GNSS or RTK service).
- **AFREF**: Niger noted in older literature as having at least one CORS that "could be available for AFREF purposes" — no real-time NTRIP stream from Niger appears in any AFREF or BKG sourcetable.
- **Cross-border alternatives within ~50 km**: None. Nearest rtk2go base is `fssoyo` (Oyo, Nigeria) ~661 km south of Niamey — far beyond any RTK baseline.
- Global commercial networks (GEODNET, ONOCOY, PointOne, Centipede-RTK): No Niger coverage confirmed.
- Practical workaround: Deploy a local base station for single-base RTK, or use satellite-based PPP (Trimble RTX, Fugro StarFix) or free Galileo HAS (~40 cm).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — NIAM station (Niamey); archival RINEX from AMMA/IGN France project | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

## Sources Consulted
- RTK2GO monitor (monitor.use-snip.com)
- NTRIP-list.com Africa page
- UNAVCO/GAGE real-time GNSS data
- GAGE Spotlight (NIAM station): https://spotlight.unavco.org/station-pages/niam/niam.html
- SONEL NIAMEY GPS: https://www.sonel.org/spip.php?page=gps&idStation=2570
- AMMA GPS network at IGN: http://amma-gps.ign.fr
- IGS real-time product server (products.igs-ip.net)
- BKG NTRIP streams
- AFREF (ResearchGate figure)
- IGNN / UNCCD entry
- ArduSimple country selector
- CORSstations.com, GitHub mvarga1989 list
- GEODNET, ONOCOY
- Local data: `py scripts/stations_by_radius.py 13.5 2.1 800` — nearest result is fssoyo (NGA) at 661 km, no NE station present (2026-05-12)
