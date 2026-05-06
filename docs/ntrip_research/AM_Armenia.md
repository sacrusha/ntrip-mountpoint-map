# Armenia [AM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (unconfirmed) |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no confirmed service |
| **legal_residency_required** | null — no confirmed service |
| **last_confirmed_alive** | null — no caster confirmed alive |

## Most Recent Project Announcement

No formal announcement of a national NTRIP/RTK caster for Armenia was found in geospatial trade press, development-bank documents, or government portals as of 2026-05-06. Armenia's State Cadastre Committee (e-cadastre.am) and National Spatial Data Infrastructure (NSDI) program are active but have not publicly announced real-time GNSS correction streaming.

- Armenian Cadastre Committee: https://www.e-cadastre.am/en
- ADB project 54388-001 supporting Armenia NSDI: https://www.adb.org/projects/54388-001/main

## Context Notes

- **Cadastre Committee NSDI:** Armenia launched maparmenia.am (July 2022), a national geoportal with cadastral, orthophoto, and hydrographic layers. The committee has modernised its geodetic network, but no public NTRIP stream has been announced.
- **EuroGeographics / EU cooperation:** The National Agency of Cadastre has cooperated with European mapping agencies on NSDI implementation, but real-time RTK corrections are not part of documented outputs.
- **IGS / EPN stations:** At least one IGS station (ARTU — Artashat) exists in Armenia and feeds the global post-processing network; it is not known to serve an NTRIP stream for local hobbyist use.
- **Regional context:** Neighbouring Azerbaijan operates AzPOS (37 CORS); Georgia operates GEO-CORS (26 CORS). Armenia sits between two active national networks but has no equivalent publicly documented.
- **ArduSimple country selector:** Armenia is not listed as having a national RTK network.
- **Global commercial networks (GEODNET, ONOCOY):** No Armenia coverage confirmed.
- Practical workaround: Deploy a local base station for single-base RTK, or use satellite-based PPP (Trimble RTX, Fugro StarFix, Galileo HAS).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope / GAGE GNSS Archive** — ARTU station (Artashat, Armenia); IGS continuous RINEX data | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); commercial fee applies |

## Sources Consulted
- e-cadastre.am / cadastre.am (Armenian Cadastre Committee)
- EuroGeographics member profile — https://eurogeographics.org/news/implementing-the-national-spatial-data-infrastructure-in-armenia/
- ADB project 54388-001 (https://www.adb.org/projects/54388-001/main)
- UNOOSA NSDI presentation (https://ggim.un.org/2unwgic/documents/Vahagn_Muradyan_Lusine_Yeghiyan.pdf)
- ArduSimple country selector (https://www.ardusimple.com/rtk-correction-services-in-your-country/)
- RTK2GO monitor (monitor.use-snip.com) — no Armenia mount points visible
- NTRIP-list.com — no Armenia entries found
- IGS network resources (https://igs.org/network-resources/)
- GitHub mvarga1989 GNSS CORS list (https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks)
