# Nicaragua [NI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: No domestic public NTRIP caster — INETER CORS is RINEX-only. However, EarthScope (NOTA) operates two NIC-tagged real-time NTRIP streams that are usable inside Nicaragua with an EarthScope NULA seat.

| Field | Value |
|---|---|
| **Domestic public NTRIP RTK caster** | No |
| **Foreign-operated NTRIP streams covering NI** | Yes — EarthScope NOTA: `CNG2_RTCM3P3` (12.50 N, -86.70 — near Chinandega), `JAPO_RTCM3P3` (11.53 N, -85.68 — near Juigalpa/San Carlos area). Both RTCM 3.3, GPS+GLO+BDS+GAL+SBAS+QZS, TRIMBLE NETR9, single-base. Auth required (Y), no NMEA, fee flagged `SEAT_REQUIRED` |
| **Domestic government CORS network** | Yes — INETER CORS (Dirección General de Geodesia y Cartografía); RINEX post-processing only |
| **INETER access portal** | https://consultacf.ineter.gob.ni (Catastro Físico) — RINEX downloads on request |
| **EarthScope sourcetable** | `gnss.earthscope.org:2101` (RTCM 3 streams listed for NIC, MEX, HND, CRI, etc.) |
| **EarthScope access policy** | Free non-commercial via NULA (No-cost User License Agreement) + a seat assignment; commercial use USD 1,000 / seat / year |
| **hobbyist_eligibility — EarthScope** | Yes — NULA covers personal, hobbyist, educational, non-commercial use. Seat allocation requires registration with EarthScope/UNAVCO |
| **legal_residency_required** | No — EarthScope NULA is open globally |
| **last_confirmed_alive** | `consultacf.ineter.gob.ni` reachable 2026-05-12 (search index returns HTTP 200). EarthScope NIC streams present in local `data/earthscope.sourcetable` (last fetch see source_health.json) |

## EarthScope NOTA — the practical real-time option in Nicaragua

Two NIC stations are streamed live via EarthScope's NTRIP caster as of 2026-05-12:

| Mountpoint | Lat | Lon | Receiver | Format | Constellations |
|---|---|---|---|---|---|
| `CNG2_RTCM3P3` | 12.50 | -86.70 | Trimble NETR9 | RTCM 3.3 (MSM7) | GPS GLO BDS GAL SBAS QZS |
| `JAPO_RTCM3P3` | 11.53 | -85.68 | Trimble NETR9 | RTCM 3.3 (MSM7) | GPS GLO BDS GAL SBAS QZS |

These are single-base streams — operate effectively within ~30–50 km of each station for full RTK. CNG2 covers the Chinandega / León area (≈64 km from Managua). JAPO covers the central Cocibolca / Río San Juan corridor. Managua city centre (12.13 N, -86.25 W) sits between them; CNG2 is the closer base.

To use: register a free EarthScope account → submit/accept NULA → request a seat → use issued credentials against `gnss.earthscope.org:2101`. See https://www.earthscope.org/data/gnss-data/.

## INETER Government CORS Network — RINEX only

**Instituto Nicaragüense de Estudios Territoriales (INETER)**, via the **Dirección General de Geodesia y Cartografía**, maintains Nicaragua's geodetic infrastructure.

| Field | Value |
|---|---|
| **Portal** | `consultacf.ineter.gob.ni` (Catastro Físico) |
| **Geodesy page** | `ineter.gob.ni/geodesiaycartografia.html` |
| **Service type** | RINEX data download for post-processing; no documented real-time NTRIP product |
| **host:port** | None published |
| **Access** | RINEX via the Catastro Físico portal |

INETER's mandate covers the National Coordinate System (Sistema Nacional de Coordenadas) and the national Infraestructura de Datos Espaciales (IDE). The IDE portal `mapserveride.ineter.gob.ni/IDE-BCN/` provides cartographic services but no NTRIP caster, mountpoint list, or self-service real-time registration page has been found on any INETER property.

INETER's seismic monitoring network (`webserver2.ineter.gob.ni`) uses GPS-disciplined timing for seismology — those are not positioning CORS.

## Volunteer & Open Coverage

| Source | Status |
|---|---|
| **rtk2go** | 0 NI stations as of 2026-05-12; 3 nearby CRI rtk2go stations (DGEOB1, DoleVNC, OVSI) all ≥200 km away — not useful for Nicaraguan RTK |
| **Centipede** | 0 NI nodes |
| **GEODNET / ONOCOY / PointOne** | No NI coverage on public-facing product pages |
| **Commercial NTRIP resellers** | Not listed for NI on NTRIP-list.com, ArduSimple country directory, Point One, GEODNET, RTKdata |

## Most Recent Project Announcement

No announcement of a planned Nicaragua public NTRIP caster found as of 2026-05-12. INETER's geodetic pages continue to describe post-processing workflows only. No SIRGAS real-time stream listed for NI.

**Regional context**: El Salvador (commercial Survey3G), Costa Rica (IGN-CR free national caster) have national NTRIP services in the same Central American corridor. Honduras, like Nicaragua, remains RINEX-only at the national level. EarthScope NOTA's regional Trimble NETR9 streams are the practical free real-time option across Honduras / Nicaragua / Costa Rica / El Salvador / Panama for non-commercial users.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **INETER Catastro Físico** — GNSS/RINEX download | https://consultacf.ineter.gob.ni/ | Free (request/account basis) |
| **INETER IDE/BCN** — national cartographic base viewer | https://mapserveride.ineter.gob.ni/IDE-BCN/ | Free |
| **EarthScope** — NIC RINEX archive (CNG2, JAPO, etc.) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA + seat) |

## Sources Consulted
- INETER Geodesia y Cartografía: https://www.ineter.gob.ni/geodesiaycartografia.html
- INETER Catastro Físico portal: https://consultacf.ineter.gob.ni/
- INETER main site: https://www.ineter.gob.ni/
- INETER IDE Base Cartográfica Nacional: https://mapserveride.ineter.gob.ni/IDE-BCN/
- EarthScope GNSS Data Services: https://www.earthscope.org/data/gnss-data/
- NTRIP-list.com North America: https://ntrip-list.com/north-america/
- ArduSimple country directory: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- Local data: `py scripts/stations_by_country.py NIC` — 0 rtk2go, 0 Centipede, 2 EarthScope (CNG2_RTCM3P3, JAPO_RTCM3P3) (2026-05-12)
- Local file: data/earthscope.sourcetable lines 150 (CNG2), 239 (JAPO) (snapshot 2026-05-12)
