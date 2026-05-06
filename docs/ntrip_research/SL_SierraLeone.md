# Sierra Leone [SL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no public NTRIP RTK caster found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | None found |
| **tariff** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster identified |

## Most Recent Project Announcement

No CORS programme or NTRIP project announcement found for Sierra Leone as of 2026-05-06.

The Directorate of Surveys and Lands (DSL), under the Ministry of Lands, Housing and Country Planning (`molhcp.gov.sl`), is the national surveying authority. Its mandate includes implementing a standardised national coordinate system and improving geodetic infrastructure; however, no public documentation of a CORS installation or real-time GNSS service has been located on the ministry website or in any AFREF/regional geodetic publication.

## Context Notes

- **National authority:** Directorate of Surveys and Lands (DSL), Ministry of Lands, Housing and Country Planning — `molhcp.gov.sl`. Separate Directorate of GIS and Remote Sensing also exists under the same ministry.
- **AFREF participation:** Sierra Leone is within the AFREF geographic scope for West Africa. No Sierra Leone IGS or AFREF core station has been identified; Sierra Leone does not appear in the list of countries that have established at least one CORS contributing to the AFREF Operational Data Centre (as of the 2015/2024 AFREF station count covering ~65 stations across ~22 countries). No GNSS station with country code SL found in HartRAO or EarthScope/IGS archives.
- **No entries on rtk2go or Centipede:** Zero SL mountpoints in either public sourcetable.
- **No entry on ntrip-list.com:** Sierra Leone absent from ntrip-list.com Africa listing.
- **No commercial NTRIP providers found:** GEODNET, ONOCOY, PointOne, HxGN SmartNet — none list Sierra Leone coverage.
- **Regional context:** Neighbouring Guinea and Guinea-Bissau also have no confirmed public caster. The nearest potentially reachable commercial NTRIP infrastructure is in Senegal (SEN-CORS, still under construction as of 2026-05-06) or Côte d'Ivoire (unconfirmed). No cross-border coverage applicable.
- **Practical hobbyist guidance:** Deploy a local GNSS base station for single-base RTK; use Galileo HAS / PPP for sub-metre work without connectivity.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope / IGS RINEX archive** — no Sierra Leone station identified; nearest qualifying stations are in Ghana or Senegal | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |
| **AFREF / RCMRD data centre** — AFREF raw GNSS archive; Sierra Leone not confirmed as contributor | https://www.rcmrd.org/ | Unknown |

## Negative Findings

- AFREF station count lists (~22 contributing countries as of 2024): Sierra Leone not included
- HartRAO GNSS archive: no SL station
- IGS network: no station with country code SL
- rtk2go monitor: zero SL mountpoints
- Centipede: zero SL nodes
- ntrip-list.com/africa: no Sierra Leone entry
- GEODNET, ONOCOY, PointOne: no Sierra Leone coverage
- molhcp.gov.sl: no GNSS service page or CORS/NTRIP documentation found

## Sources Consulted
- Directorate of Surveys and Lands (DSL): https://molhcp.gov.sl/directorate-of-surveys-and-lands/
- Directorate of GIS and Remote Sensing: https://molhcp.gov.sl/directorate-of-gis-and-remote-sensing/
- AFREF workshop 2024 (RCMRD): https://ric2024.rcmrd.org/afref
- AFREF station map / country list (GIM International): https://www.gim-international.com/content/article/development-between-2000-and-2015
- AFREF background (UN-SPIDER): https://un-spider.org/space-application/space-application-matrix/african-geodetic-reference-frame-afref
- UNGGIM Africa Regional Working Group report (2025): https://ggim.un.org/UNGGCE/documents/20250313%20UNGGIM%20Africa%20report.pdf
- ntrip-list.com Africa: https://ntrip-list.com/africa/
- rtk2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
