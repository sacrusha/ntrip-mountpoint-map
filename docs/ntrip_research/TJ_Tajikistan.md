# Tajikistan [TJ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (refresh of 2026-05-06 entry)

## Status: NO active public NTRIP caster confirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — none confirmed |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no caster confirmed alive |

## Most Recent Project Announcement

No formal project announcement for a Tajikistani national NTRIP/RTK caster was found in any development-bank, UN, or geospatial trade press source as of 2026-05-06.

An academic paper referenced from neighboring-country GNSS literature notes that GNSS permanent networks exist in Kyrgyzstan, Tajikistan, and Uzbekistan in a scientific monitoring context. However, this refers to geodynamics and plate-motion research stations, not to RTK corrections delivery.

## Context Notes

- **No documented CORS RTK network**: Searches in Russian ("Таджикистан ГНСС НТРИП сеть", "геодезия Таджикистан реальное время CORS") and English found no Tajikistani CORS network or NTRIP caster with an operational endpoint.
- **Scientific GNSS stations**: The Central Asian Geodynamics network and affiliated projects (USGS, NASA, UNAVCO) have installed permanent GNSS receivers in Tajikistan for tectonic monitoring — these are research stations, not RTK correction sources.
- **Geodetic authority**: The State Committee for Land Management and Geodesy of Tajikistan is the relevant authority. No NTRIP service was found from that body.
- **GeoComm Kazakhstan**: GeoComm (geocomm.kz), which operates commercial CORS in Kazakhstan, does not appear to extend coverage into Tajikistan based on available information.
- **Global commercial networks**: GEODNET, ONOCOY — no confirmed Tajikistan coverage.
- **Neighboring coverage**: Kazakhstan (partial commercial CORS), Kyrgyzstan (KyrPOS, 18 stations), and Uzbekistan (developing national CORS) are more developed. Tajikistan's difficult mountainous terrain would make a CORS network expensive to build.
- **Practical workaround**: Deploy a local base station for single-base RTK, or use satellite PPP (Galileo HAS, Trimble RTX).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — geodynamics-network stations in Tajikistan region | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |

## Sources Consulted
- Searches in Russian and English (no Tajikistani NTRIP/CORS found 2026-05-06 or 2026-05-13)
- Tajikistan UNFCCC Fourth National Communication: https://unfccc.int/sites/default/files/resource/4NC_TJK_eng_0.pdf — no GNSS/CORS infrastructure mentioned
- ResearchGate — "GNSS Permanent Networks in Kyrgyzstan" (regional context mentioning Tajikistan)
- GeoComm Kazakhstan (geocomm.kz) — no Tajikistan coverage listed
- E3S Conferences 2024 — Central Asian geodetic papers (Uzbekistan and Kazakhstan focus)
- RTK2go monitor — no Tajikistan NTRIP streams 2026-05-13
- ArduSimple country selector — no Tajikistan page (URL returns 404 2026-05-13)
- GitHub mvarga1989 GNSS CORS RTK networks list — no Tajikistan entry confirmed
