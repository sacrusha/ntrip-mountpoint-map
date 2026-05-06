# Kazakhstan [KZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: PARTIAL — private CORS providers exist; no confirmed government national RTK network with public NTRIP

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — private commercial CORS providers confirmed; national government NTRIP not confirmed |
| **host:port** | GeoComm: geocomm.kz (port not publicly confirmed); others unknown |
| **tariff** | Unknown — commercial; contact providers |
| **hobbyist_eligibility** | Unclear — commercial providers likely require a business contract |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | GeoComm site live as of research date (geocomm.kz) |

## Most Recent Project Announcement

A 2012 Government Decree of Kazakhstan (RK №721, May 31 2012) referenced RTK correction provision from the National Space Agency of Kazakhstan (KazCosmos, later reorganized into KazSat / Kazcosmos structures). No subsequent public announcement of an operational national NTRIP caster has been found.

GeoComm LLP (geocomm.kz, Almaty) operates a private network of CORS base stations across Kazakhstan and provides RTK corrections via GPRS/internet, requiring a GNSS receiver and internet modem. They are the most prominently documented commercial NTRIP provider found.

## Context Notes

- **No national public NTRIP**: ArduSimple's Kazakhstan page explicitly notes Kazakhstan has no established National RTK Network. Free global correction services (with sparse base-station density) are the stated alternative.
- **GeoComm CORS network**: GeoComm LLP advertises base stations across Kazakhstan at geocomm.kz/bazovye-stanczii/. They provide RTK corrections to subscribers; pricing and the specific NTRIP endpoint are not published on the public website.
- **Government decree**: Decree RK №721 (2012) authorized the National Space Agency to provide RTK corrections — but no resulting public NTRIP caster endpoint has been documented in any subsequent source.
- **KazSat / national agency**: Kazakhstan's space and geodetic activities have undergone multiple agency reorganizations; the current operational geodetic authority is Kazkosmos / the Committee on Land Management (under the Ministry of Agriculture). No public NTRIP stream from the government has been found.
- **Searches in Kazakh/Russian**: Searches for "Казахстан ГНСС НТРИП сеть" and "геодезия Казахстан реальное время" returned GeoComm as the dominant commercial provider; no government NTRIP caster URL surfaced.
- **Global commercial networks**: GEODNET, ONOCOY — sparse or unconfirmed Kazakhstan coverage.
- **Practical workaround**: Contact GeoComm (geocomm.kz) for commercial RTK subscription, deploy a local base station, or use satellite PPP (Galileo HAS, Trimble RTX).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — IGS stations in Kazakhstan (e.g., ARTI, ARTU, KIT3) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |
| **BKG NTRIP** — IGS real-time streams including Central Asian stations | https://igs.bkg.bund.de/ntrip/ | Free (account required) |

## Sources Consulted
- ArduSimple — RTK correction services and NTRIP Casters in Kazakhstan
- geocomm.kz — Базовые станции page
- southinstrument.kz — RTKNet reference (Kazakhstan market)
- GitHub mvarga1989 GNSS CORS RTK networks list
- Russian-language survey forums and trade press (gis2000.ru, vestnik-glonass.ru)
- RTK2go monitor — no Kazakhstan NTRIP streams confirmed
- NTRIP-list.com — no Kazakhstan entry confirmed
