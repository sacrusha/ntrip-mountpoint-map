# Madagascar [MG] — NTRIP RTK Caster Research
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

**IOGA4MET-EI expansion** (c. 2019–2020): Five permanent Trimble NetR9 GNSS stations deployed across Madagascar as part of the INTERREG-5 Indian Ocean "ReNovRisk Cyclones and Climate Change" project. These are research stations for tropospheric water-vapor sensing — they do NOT expose NTRIP mountpoints for RTK corrections.

Stations: DSUA (Antsiranana), MASM (Sainte-Marie), MATA (Toamasina), MAFD (Tôlanaro), NOSY (Nosy Be)

**Source URL:** https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2020.566105/full

**AFREF Workshop 2024** (August 12–15, 2024): Geodetic capacity-building across Africa including Madagascar participation; no NTRIP caster launch announced.
**Source URL:** https://ric2024.rcmrd.org/afref

## Context Notes

- **FTM** (Foiben-Taosarintanin'i Madagasikara, national mapping agency): No evidence of operating or planning a public NTRIP caster.
- **AFREF**: Madagascar reportedly has at least one CORS station contributing RINEX data for post-processing — not RTK.
- **ASECNA SBAS**: Covers Madagascar for aviation sub-meter accuracy — excluded (DGNSS/SBAS only).
- Global commercial networks (GEODNET, ONOCOY, Trimble RTX, Point One): No confirmed Madagascar coverage.
- Practical reality: Rover operators must use a local owned base station or post-process against AFREF/IGS RINEX archive.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS/CDDIS** (NASA) — global IGS archive; Madagascar AFREF station(s) if contributed | https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html | Free (NASA Earthdata account required) |
| **RGP** (French IGN) — archives IOGA4MET station data (DSUA, MASM, MATA, MAFD, NOSY) | https://rgp.ign.fr/ | Free |

## Sources Consulted
- RTK2GO sourcetable (rtk2go.com:2101)
- SNIP Monitor
- NTRIP-list Africa (ntrip-list.com/africa/)
- IGS Network (network.igs.org)
- GAGE/UNAVCO
- GEODNET, ONOCOY, Centipede-RTK, TrigNet, Point One Navigation
- UN-SPIDER AFREF Knowledge Portal
- GIM International CORS Africa map
- UN-GGIM Africa Activities Report 2025
