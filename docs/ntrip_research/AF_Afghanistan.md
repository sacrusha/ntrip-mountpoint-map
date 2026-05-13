# Afghanistan [AF] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (originally 2026-05-06)

## Status: NO — no NTRIP caster exists or is plausible under current conditions

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | none |
| **tariff** | n/a |
| **hobbyist_eligibility** | n/a |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | n/a — no endpoint has ever been discovered |

## Most Recent Project Reference

**USGS Geospatial Infrastructure Development programme (pre-2021)** — The U.S. Geological Survey ran a Geospatial Infrastructure Development programme in Afghanistan that trained AGCHO staff and worked toward modernising geodetic infrastructure. This programme was halted following the August 2021 Taliban takeover and the subsequent withdrawal of international development assistance. No geodetic CORS or NTRIP infrastructure from this programme was confirmed operational before the programme ended.

Source: https://www.usgs.gov/special-topics/usgs-projects-in-afghanistan/science/geospatial-infrastructure-development

No post-2021 announcements of geodetic CORS development in Afghanistan have been found in open sources as of 2026-05-06.

## Context Notes

- **AGCHO** (Afghan Geodesy and Cartography Head Office), founded 1958, was the national cartographic agency responsible for geodetic infrastructure. It operated two permanent GNSS reference stations, both decommissioned by 2010–2011 as part of a broader programme transition. No NTRIP caster has ever been associated with AGCHO.
- **Post-2021 situation**: The Taliban government that took power in August 2021 does not appear to have engaged with international geodetic bodies (IGS, AFREF, FIG, ICSM). International development organisations that previously supported geodetic work (World Bank, USAID, USGS) have either withdrawn or suspended Afghanistan operations. AGCHO's operational status under Taliban administration is unknown from open sources.
- **Internet infrastructure**: Afghanistan's internet infrastructure remains fragmented and unreliable in many provinces. Even if a CORS station were operational, reliable NTRIP streaming would require sustained IP connectivity that is not universally available.
- **Volunteer coverage**: zero AF mountpoints on rtk2go; zero nodes on Centipede; zero EarthScope/IGS NTRIP streams. Confirmed via `scripts/stations_by_country.py AFG` (no entries) on 2026-05-12.
- **Security and access environment**: The combination of active conflict in parts of the country, international sanctions, and restricted movement for international geodetic personnel makes CORS deployment and maintenance effectively impossible for the foreseeable future.
- **Global commercial fallbacks**: no international commercial NTRIP provider (GEODNET, PointOne, RTKdata) lists Afghanistan coverage.

## Post-Processing (RINEX) Fallback

No operational GNSS CORS stations in Afghanistan currently archive public RINEX data. Historically, IGS stations in neighbouring countries (Pakistan: ISBD Islamabad; Tajikistan: DUSH Dushanbe; Uzbekistan: TASH Tashkent) are the nearest post-processing fallback, all at 400–800 km from Kabul — too far for meaningful post-processing differential GNSS.

| Service | URL | Notes |
|---|---|---|
| **EarthScope IGS archive** — nearest stations in PK, UZ, TJ | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; nearest station 400+ km |

## Sources Consulted
- Afghan Geodesy and Cartography Head Office (Wikipedia): https://en.wikipedia.org/wiki/Afghan_Geodesy_and_Cartography_Head_Office
- USGS Geospatial Infrastructure Development (Afghanistan): https://www.usgs.gov/special-topics/usgs-projects-in-afghanistan/science/geospatial-infrastructure-development
- Afghanistan Humanitarian Needs and Response Plan 2025 (OCHA): https://www.unocha.org/publications/report/afghanistan/afghanistan-humanitarian-needs-and-response-plan-2025-december-2024
- rtk2go sourcetable — zero AF entries confirmed 2026-05-06
- Centipede sourcetable — zero AF entries confirmed 2026-05-06
- country-survey.md AF stub (2026-04-28)
