# Cape Verde [CV] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: NO active public NTRIP RTK caster. One IGS scientific reference station (CPVG, Espargos, Sal) exists for post-processing only; no real-time RTK service for hobbyist use

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Most Recent Project Announcement

No formal project announcement for a Cape Verdean national NTRIP/RTK caster was found in any development-bank (World Bank, AfDB), UN, or geospatial trade press source as of 2026-05-12.

The volcano monitoring effort run by the Observatório Vulcanológico de Cabo Verde (OVCV) — joint INMG / Universidade de Cabo Verde / ITER (Tenerife) — operates a GPS-based ground-deformation network on Fogo island for geophysical research; outputs are scientific, not a public NTRIP RTK service.

## Context Notes

- **National geodetic authority**: Instituto Nacional de Gestão do Território (INGT), `ingt.gov.cv`, is responsible for cartography, cadastre and geodesia in Cape Verde, and runs the national SDI (`idecv.gov.cv`). INGT does **not** publish an NTRIP caster, sourcetable, or correction-service product as of 2026-05-12.
- **IGS reference station CPVG (Espargos, Sal Island)**: A single IGS continuously-operating GNSS reference station — site name CAP-VERT, four-character ID **CPVG**, DOMES 39601M001 — is hosted by **Instituto Nacional de Meteorologia e Geofisica (INMG)** on the roof of a building in Espargos, Sal Island. It is part of CNES/IGN France's **REGINA** network (Receiver GNSS Network for IGS and Navigation). CPVG provides daily/hourly RINEX for post-processing through CDDIS and IGN-IGS archives; it does **not** serve real-time RTCM corrections via public NTRIP, and a single station ~750 km offshore from the rest of the archipelago is not usable for RTK over the other islands.
- **Island geography**: Cape Verde consists of 10 islands spread over ~580 km of ocean; a meaningful national RTK network would require at minimum one CORS per island. No such infrastructure has been documented.
- **AFREF**: Cape Verde has not been identified in published AFREF operational station lists as contributing a real-time NTRIP stream.
- **EarthScope / SIRGAS**: Not in the SIRGAS network (Americas-focused). EarthScope/GAGE has no Cape Verde stations.
- **Volunteer networks (rtk2go, Centipede)**: Zero Cape Verde-coded stations in the project's 2026-05 archives. Cross-checked against `data/rtk2go.sourcetable` and `data/centipede.sourcetable`.
- **Global commercial networks**: GEODNET, ONOCOY, PointOne — no Cape Verde coverage confirmed.
- **Practical workaround for hobbyists**: Deploy a local base station for single-base RTK on whichever island is the work site, or use satellite-based PPP (Galileo HAS, Trimble RTX).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS CDDIS — CPVG station archive** | https://cddis.nasa.gov/archive/gnss/data/ | Free (NASA Earthdata account required) |
| **IGN-IGS / REGINA archive** | https://igs.ign.fr/ | Free |
| **SONEL** — CPVG height time-series and metadata | https://www.sonel.org/spip.php?page=gps&idStation=3597 | Free |

## Sources Consulted
- INGT (Instituto Nacional de Gestão do Território): https://ingt.gov.cv/ (no NTRIP/RTK section as of 2026-05-12)
- IDE-CV (national SDI): https://idecv.gov.cv/ (cadastral / mapping portal — no RTK service)
- INMG geofísica page: https://www.inmg.gov.cv/index.php/servicos/geofisica
- SONEL CPVG record (Cape Verde GPS station): https://www.sonel.org/spip.php?page=gps&idStation=3597
- IGS station log archive (CPVG): https://files.igs.org/pub/station/oldlog/cpvg_20230309.log
- IGS network list: https://network.igs.org/
- ArduSimple country selector — no Cape Verde page found
- RTK2go monitor (monitor.use-snip.com) — no Cape Verde streams
- NTRIP-list.com — no Cape Verde entry
- AFREF station documentation — no Cape Verde entry confirmed
- GIM International — "Developing a Fully Fledged CORS Map for Africa"
- GitHub mvarga1989 GNSS CORS RTK networks list — no Cape Verde entry
- General searches in Portuguese (Cabo Verde geodesia GNSS CORS RTK 2024 / 2025)
- `data/rtk2go.sourcetable` and `data/centipede.sourcetable` — zero CPV-coded streams
