# Tanzania [TZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

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

- **RCMRD CORS portal** (corsdata.rcmrd.org): Tanzania is an RCMRD member state; portal is Leica Spider Business Center login-gated. Whether Tanzania has a station connected and whether real-time NTRIP is dispensed cannot be confirmed from public-facing data.
  Contact: rcmrd@rcmrd.org / +254 723 786161

## Nearest Confirmed RTK Streams
- **Rwanda**: EarthScope BYAH/KMBR/NYBA/RUBO (institutional account required)
- **Kenya**: Muya CORS (commercial, 25+ stations)

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **RCMRD CORS data portal** — Tanzania is an RCMRD member state; RINEX may be accessible if a station is connected; login-gated | https://corsdata.rcmrd.org/sbc | Unknown — contact rcmrd@rcmrd.org |
| **IGS/CDDIS** — no Tanzania station confirmed; nearest: MAL200KEN (Malindi, Kenya) | https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html | Free (NASA Earthdata account required) |

## ArduSimple Page
ArduSimple Tanzania page (ardusimple.com/rtk-correction-services-and-ntrip-casters-in-tanzania/), updated 2026-05-06, explicitly states Tanzania is not among countries with a national RTK network.

## Sources Consulted
- RTK2GO live sourcetable (874 STR entries — no TZ)
- EarthScope ntrip.earthscope.org:2101 — no TZ stations
- IGS Network CSV bounding-box filter — only MAL200KEN returned
- RTCM-NTRIP registry — no TZ casters
- BKG IGS NTRIP sourcetable — no TZ
- RCMRD corsdata.rcmrd.org (login-gated)
- ArduSimple Tanzania page (2026-05-06)
- corsstations.com, ntrip-list.com/africa/
- World Bank SMD Tanzania blog (2019)
- GIM International CORS Africa map
