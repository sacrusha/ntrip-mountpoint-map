# Tanzania [TZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-13 entry; no operational change — still NO active public NTRIP caster)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster confirmed |

## Most Recent Project Announcements

- **2019-04-30**: World Bank blog — technology demonstration workshop for 30+ licensed surveyors hosted by Tanzania's Surveys and Mapping Division (SMD) in Dodoma. Survey-grade accuracy demonstrated; no CORS/NTRIP infrastructure announced.
  URL: https://blogs.worldbank.org/en/sustainablecities/how-can-we-help-surveyors-tanzania-understand-promise-new-technology

- **AFREF commitment (pre-2006)**: Tanzania committed to at least one CORS station as part of AFREF. Whether a physical station was installed and whether it streams real-time NTRIP remains unconfirmed — AFREF data centre (afrefdata.org) was unreachable at research date.

- **RCMRD CORS portal** (corsdata.rcmrd.org): Tanzania is an RCMRD member state; portal is Leica Spider Business Center login-gated. Whether Tanzania has a station connected and whether real-time NTRIP is dispensed cannot be confirmed from public-facing data. RCMRD itself has a single GNSS CORS at its Nairobi HQ; Tanzania-territory coverage from this would be too long-baseline to be practical for RTK.
  Contact: rcmrd@rcmrd.org / +254 723 786161

- **Ardhi University (ARU), Dar es Salaam — internal CORS station**: ARU's Department of Geospatial Sciences and Technology lists a "CORS station" among its high-tech research equipment (alongside total stations, robotic total stations, MESA satellite receiving station, automatic tide gauge). Source: aru.ac.tz/pages/department-of-geospatial-sciences-and-technology (observed 2026-05-13). No public NTRIP endpoint, station name, or sourcetable advertised; appears academic-teaching / post-processing only, not a public real-time NTRIP caster. No academic publication located documenting a TZ-hosted public NTRIP service.
- **Datum/epoch declaration:** omitted -- no citable operator declaration (no active caster; East View Geospatial country profile mentions "TAREF 11, WGS84 / EGM 96" but is not an operator source under primer rule).

## Nearest Confirmed RTK Streams
- **Rwanda**: EarthScope BYAH/KMBR/NYBA/RUBO (institutional account required)
- **Kenya**: Muya CORS (commercial, 25+ stations)
- Local-data probe via `py scripts/stations_by_radius.py -6.16 35.74 500` (Dodoma centre, 500 km radius): **zero** rtk2go / Centipede / EarthScope hits per 2026-05-13 run — confirms no usable public real-time NTRIP coverage within reach of any populated Tanzanian centre. Re-run on data refresh to verify persistence.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **RCMRD CORS data portal** — Tanzania is an RCMRD member state; RINEX may be accessible if a station is connected; login-gated | https://corsdata.rcmrd.org/sbc | Unknown — contact rcmrd@rcmrd.org |
| **IGS/CDDIS** — no Tanzania station confirmed; nearest: MAL200KEN (Malindi, Kenya) | https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html | Free (NASA Earthdata account required) |

## ArduSimple Page
ArduSimple Tanzania page (ardusimple.com/rtk-correction-services-and-ntrip-casters-in-tanzania/), re-checked 2026-05-13 (no change observed 2026-05-17), explicitly states Tanzania is not among countries with a national RTK network. Lists only RTK2GO (community, no QA), IGS, EarthScope as free options; RTK Premium Network (54€/mo) and Galileo HAS as paid/alt; suggests independent base station deployment as primary path.

## Sources Consulted
- RTK2GO live sourcetable (no TZ-coded stations 2026-05-13)
- EarthScope ntrip.earthscope.org:2101 — no TZ stations 2026-05-13
- IGS Network CSV bounding-box filter — only MAL200KEN (Malindi, Kenya) returned
- RTCM-NTRIP registry — no TZ casters
- BKG IGS NTRIP sourcetable — no TZ
- Centipede crtk.net:2101 sourcetable — no TZ-coded mountpoints 2026-05-13
- Local data probe `py scripts/stations_by_radius.py -6.16 35.74 500` — zero hits within 500 km of Dodoma 2026-05-13
- RCMRD corsdata.rcmrd.org (login-gated)
- Ardhi University Geospatial Sciences and Technology department: https://www.aru.ac.tz/pages/department-of-geospatial-sciences-and-technology (CORS station equipment listed; not public NTRIP)
- ArduSimple Tanzania page (2026-05-13)
- corsstations.com, ntrip-list.com/africa/
- World Bank SMD Tanzania blog (2019)
- GIM International CORS Africa map
- East View Geospatial Tanzania country profile: https://geospatial.com/country_profiles/tanzania/ — confirms Tanzanian reference frame epoch (TAREF 11, WGS84 / EGM 96); no public NTRIP caster mentioned
