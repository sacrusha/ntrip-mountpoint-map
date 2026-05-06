# Cape Verde [CV] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

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

No formal project announcement for a Cape Verdean national NTRIP/RTK caster was found in any development-bank (World Bank, AfDB), UN, or geospatial trade press source as of 2026-05-06.

## Context Notes

- **No national CORS found**: Searches in Portuguese ("Cabo Verde geodesia GNSS RTK CORS") and English found no Cape Verdean CORS network, NTRIP caster, or national RTK correction service. The national geodetic/cartographic authority (Instituto Nacional de Gestão do Território — INGT, or predecessor INGT/IGC) has no publicly documented GNSS correction service.
- **Island geography**: Cape Verde consists of 10 islands spread over ~580 km of ocean; a meaningful national RTK network would require at minimum one CORS per island. No such infrastructure has been documented.
- **AFREF**: Cape Verde has not been identified in published AFREF operational station lists as contributing a real-time NTRIP stream.
- **IGS / EarthScope**: There are no confirmed Cape Verde GNSS stations in the IGS or EarthScope/GAGE archive based on available search results.
- **SIRGAS**: Not in the SIRGAS network (Americas-focused; Cape Verde is African).
- **Global commercial networks**: GEODNET, ONOCOY, PointOne — no Cape Verde coverage confirmed.
- **Practical workaround**: Deploy a local base station for single-base RTK on whichever island is the work site, or use satellite-based PPP (Galileo HAS, Trimble RTX).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — check for any Cape Verde area campaign stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |

## Sources Consulted
- ArduSimple country selector — no Cape Verde page found
- RTK2go monitor (monitor.use-snip.com) — no Cape Verde streams
- NTRIP-list.com — no Cape Verde entry
- AFREF station documentation — no Cape Verde entry confirmed
- UNAVCO/GAGE permanent station search — no Cape Verde results returned
- GIM International — "Developing a Fully Fledged CORS Map for Africa"
- GitHub mvarga1989 GNSS CORS RTK networks list — no Cape Verde entry
- General searches in Portuguese (Cabo Verde geodesia GNSS CORS RTK 2024)
