# Brunei [BN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (planned RTK augmentation; no public endpoint) |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster confirmed alive |

## Most Recent Project Announcement

**Survey Department Zero Order GNSS Network (8 stations, established ~2009)** — A 2011 UNOOSA/UN-GNSS presentation by Brunei's Survey Department described 8 CORS stations (KBEL, LABI, MURA, LAMU, LIAN, TEMB, TUTO, UKUR) supporting the GDBD2009 datum and providing "24-hour RTK data to GNSS/GPS users in Brunei Darussalam." A 2017 SEASC presentation additionally referenced a planned "Positioning Augmentation Center." No NTRIP host:port or public access portal has ever been published externally. As of 2026-05-06, the Survey Department website (survey.gov.bn) and Geoportal Ukur list no RTK subscription or data download service.

Source: UNOOSA UN-GNSS/18 presentation (2011) — https://www.unoosa.org/documents/pdf/psa/activities/2011/un-gnss/18.pdf (note: 404 as of 2026-05-06; content sourced via mycoordinates.org summary)

## Context Notes

- **Survey Department (Jabatan Ukur)**: operates the Geoportal Ukur mapping platform (https://geoportal.survey.gov.bn/); the Geoportal shows a web map only — no RTK, CORS, or RINEX download links visible. Department homepage now at https://survey.gov.bn/ (previous mod.gov.bn URL returns 404).
- **CORS Zero Order Network**: 8 stations — KBEL, LABI, MURA, LAMU, LIAN, TEMB, TUTO, UKUR — established for the GDBD2009 datum. Described as providing 24h RTK data in a 2011 government presentation, but no public NTRIP endpoint or data portal has been published externally.
- **No public NTRIP endpoint** has been confirmed online.
- **Malaysia's MyRTKnet** covers up to the Malaysia-Brunei border but does not include Brunei territory in its coverage map.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede-RTK): no Brunei coverage confirmed.
- Practical workaround for hobbyists: deploy a local base station for single-base RTK, or use satellite-based PPP services (Trimble RTX, u-blox PointPerfect where available).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / IGS** — no Brunei stations confirmed in IGS or APREF networks; nearest stations are in Malaysia. No Brunei RINEX publicly available via standard archives as of 2026-05-06. | https://www.earthscope.org/data/gnss-data/ | N/A |

## Sources Consulted
- Brunei Survey Department (current URL): https://survey.gov.bn/
- Geoportal Ukur: https://geoportal.survey.gov.bn/
- mycoordinates.org — GDBD2009 datum realization and 8 CORS station IDs (KBEL, LABI, MURA, LAMU, LIAN, TEMB, TUTO, UKUR): https://mycoordinates.org/the-realization-of-geocentric-datum-for-brunei-darussalam-2009/
- Hydro International — Brunei Survey Department profile: https://www.hydro-international.com/content/company/survey-department-brunei
- NTRIP-list.com Asia: https://ntrip-list.com/
- GEODNET coverage map: https://geodnet.com/
- MyRTKnet (Malaysia) coverage map: https://www.geodesi.gov.my/myrtknet
