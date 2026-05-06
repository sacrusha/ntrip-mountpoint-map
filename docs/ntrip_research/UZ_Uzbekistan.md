# Uzbekistan [UZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no publicly accessible NTRIP caster confirmed; state CORS exists but access is restricted

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (state network exists; not open to public) |
| **host:port** | not publicly documented |
| **tariff** | not published |
| **hobbyist_eligibility** | No — access restricted to licensed surveyors and state agencies |
| **legal_residency_required** | unclear (moot; no open registration path exists) |
| **last_confirmed_alive** | n/a — no public endpoint found; UzGeodezKadastr websites reachable but no NTRIP registration portal discovered as of 2026-05-06 |

## Most Recent Project / Literature Reference

**GNSS network expansion planning (2016–2017 literature)** — Academic literature (ScienceDirect / Journal of Applied Geodesy) describes a plan for Uzbekistan's national GNSS datum modernisation and CORS network buildout: 50 reference stations planned, split between Type-A stations (~300–400 km spacing, geodetic reference) and Type-B stations (~50–80 km spacing, RTK service). The paper by Ergashev et al. describes the network architecture but does not record an operational NTRIP endpoint or a public access policy.

Source: "The review and development of a modern GNSS network and datum in Uzbekistan" — https://www.sciencedirect.com/science/article/pii/S1674984717300526

A 2024 E3S Conferences paper ("Analysis of the quality of measurements of permanent base stations in Uzbekistan") references active permanent base stations and discusses measurement quality, confirming the network is operational for state/professional use, but again provides no public endpoint.

Source: https://www.e3s-conferences.org/articles/e3sconf/pdf/2024/28/e3sconf_icape2024_02020.pdf

## Context Notes

- **UzGeodezKadastr** (State Committee for Land Resources, Geodesy, Cartography and State Cadastre) is the responsible authority. Official website: uzgeodezkadastr.uz. The site is reachable but contains no NTRIP registration portal, no published host:port, and no public subscription information.
- **State CORS network**: literature confirms 30–50 permanent GNSS reference stations across the country's territory, concentrated in Tashkent, the Fergana Valley, and major provincial centres. The network serves geodetic reference frame maintenance and cadastral survey work for licensed professionals and state entities.
- **No open-data mandate**: Uzbekistan has no legislation analogous to Indonesia's Law No. 4/2011 mandating free public access to GNSS correction services. Post-Soviet Central Asian geodetic agencies typically treat CORS data as an internal professional resource.
- **Volunteer coverage**: zero UZ mountpoints on rtk2go; zero nodes on Centipede. NTRIP-list.com does not list a UZ entry.
- **Commercial alternatives**: no international commercial NTRIP provider (GEODNET, PointOne, RTKdata, HxGN SmartNet, Trimble VRS Now) has confirmed Uzbekistan coverage as of 2026-05-06.
- **Regional context**: neighbouring Kazakhstan (KazGeodesy CORS network) and Kyrgyzstan (KNAG GeoNet) also operate state-only CORS networks. Tajikistan similarly has no public endpoint. The Central Asian pattern is uniformly closed-access.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / UNAVCO IGS stations** — one UZ IGS station (TASH, Tashkent) archives RINEX daily | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **EUREF Permanent Network (EPN)** — TASH listed as EPN supplementary site | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- UzGeodezKadastr official site: https://uzgeodezkadastr.uz/
- "The review and development of a modern GNSS network and datum in Uzbekistan": https://www.sciencedirect.com/science/article/pii/S1674984717300526
- "Creation of a State GNSS Network as a Basic Component of the National GIS of Uzbekistan" (ResearchGate): https://www.researchgate.net/publication/313101095_CREATION_A_STATE_GNSS_NETWORK_AS_A_BASIC_COMPONENT_OF_THE_NATIONAL_GEOGRAPHIC_INFORMATION_SYSTEM_OF_UZBEKISTAN
- "Analysis of the quality of measurements of permanent base stations in Uzbekistan" (E3S Conferences 2024): https://www.e3s-conferences.org/articles/e3sconf/pdf/2024/28/e3sconf_icape2024_02020.pdf
- NTRIP-list.com Asia: https://ntrip-list.com/asia/
- rtk2go sourcetable — zero UZ entries confirmed 2026-05-06
- country-survey.md UZ stub (2026-04-28)
