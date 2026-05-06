# Belize [BZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no public NTRIP RTK caster operating; no CORS network found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster endpoint identified |

## Most Recent Project Announcement

No public announcement of a planned NTRIP or CORS program found as of 2026-05-06. The Surveys and Mapping Section (Ministry of Natural Resources, `naturalresources.gov.bz`) maintains horizontal and vertical control networks and supervises cadastral surveys, but no fixed reference station network (CORS) or public NTRIP caster endpoint has been published. The Belize National Spatial Data Infrastructure portal (`portal.bnsdi.gov.bz`) provides map data access but does not include real-time GNSS corrections.

## Context Notes

- **Surveys and Mapping Section** (Ministry of Natural Resources, `naturalresources.gov.bz/index.php/surveys-and-mappings-section/`): Responsible for all aspects of mapping including horizontal and vertical control; Principal Surveyor Kevin Gutierrez heads the section. No CORS or NTRIP infrastructure is mentioned on the website or in any indexed technical publication.
- **BNSDI** (`portal.bnsdi.gov.bz`): Belize National Spatial Data Infrastructure portal is operational (HTTP 200) but provides only static map data and cadastral layers — no real-time GNSS correction service.
- **rtk2go / Centipede**: Zero BZ-coded stations in either sourcetable as of 2026-05-06. No volunteer base stations operating from Belize.
- **Border proximity**: Nearest free public NTRIP stations are in Mexico (INEGI CORS, `ntrip.inegi.org.mx:2101`) and Guatemala (IGN-Guatemala, `rtk.igntopo.gob.gt:2101`). Cross-border single-base use may be feasible for northern and western Belize (Corozal, Orange Walk, Cayo Districts) if baselines remain under ~50 km, but this is unverified for actual coverage reach.
- **EarthScope NOTA**: No Belize-territory NOTA stations in the EarthScope sourcetable.
- **IGS / AFREF**: No IGS core or AFREF-affiliated station in Belize.
- **Gap assessment**: Belize is a small country (~23,000 km²) with a population of ~400,000; the geodetic surveying community is small. There is no evidence of a near-term CORS program. The most practical free-correction option for northern/western Belize is border-reach from Mexican or Guatemalan casters, which is unconfirmed for actual usable baselines.

## Post-Processing (RINEX) Fallback

No national RINEX archive identified. EarthScope NOTA and IGS archives contain no Belize-specific stations.

## Sources Consulted
- Surveys and Mapping Section, Ministry of Natural Resources: https://naturalresources.gov.bz/index.php/surveys-and-mappings-section/
- BNSDI portal: https://portal.bnsdi.gov.bz/
- rtk2go sourcetable — zero BZ stations confirmed 2026-05-06
- Centipede sourcetable — zero BZ stations confirmed 2026-05-06
- ArduSimple RTK correction services by country: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- EarthScope NOTA sourcetable: https://ntrip.earthscope.org:2101 (no BZ stations)
