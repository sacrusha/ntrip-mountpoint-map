# Nepal [NP] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster (CORS infrastructure in development)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — no publicly documented NTRIP endpoint found |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no public caster confirmed at any date |

## Most Recent Project Announcement

- **2019 (ongoing):** Nepal's Survey Department (Geodetic Survey Division) announced plans to establish 50+ CORS stations covering the entire country, with an initial 2 stations at Nagarkot. As of 2024 no public NTRIP endpoint has been published.
- **2016:** UN/Nepal Workshop on GNSS Applications (hosted by the Survey Department, Kathmandu, December 2016) included RTK and RTKLIB demonstrations; no NTRIP service was launched at that time.
- **UNAVCO/GAGE:** 11 existing scientific CORS (JMLA, NPGJ, JMSM, BESI, CHLM, NAST, SYBC, SNDL, RMJT, BRNZ) plus 5 newer stations operated by UNAVCO and Department of Mines and Geology — geodetic/scientific purpose, not an RTK corrections service for public use.
- Survey Department official site: https://survey.gov.np/

## Context Notes

- Nepal's Survey Department (Geodetic Survey Division) maintains 2 operational CORS stations at Nagarkot, with more under construction as of the most recently available information.
- UNAVCO/EarthScope operates ~16 scientific GNSS CORS in Nepal for seismic and geodynamic monitoring — data is archival / post-processing only; no public NTRIP RTK stream is offered from these stations.
- NMGISC (National Mapping and Geospatial Information System Centre) and the Survey Department have both expressed intent to build a national CORS/NTRIP network, but no operational service has been publicly announced.
- Nepal lies in a high-seismicity zone; post-2015 Gorkha earthquake geodetic infrastructure has been rebuilt with international support (UNAVCO, IGS), but the focus has been scientific monitoring rather than survey-grade real-time corrections.
- Commercial global networks (GEODNET, ONOCOY, PointOne, Centipede): no Nepal coverage confirmed.
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS, NRCAN PPP). UNAVCO archival RINEX is free for post-processing.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope/GAGE GNSS Archive** — archival RINEX from Nepal scientific CORS (NAST, SYBC, CHLM, etc.) | https://www.unavco.org/data/gps-gnss/ | Free non-commercial (account + NULA); $1,000/seat/yr commercial |
| **IGS data** — KATM station (Kathmandu, IGS) | https://igs.org/ | Free |

## Sources Consulted
- mycoordinates.org — UN/Nepal Workshop on Applications of GNSS (2016): https://mycoordinates.org/united-nationsnepal-workshop-on-the-applications-of-gnss/
- NepJOL — "GNSS Practice in Survey Department": https://www.nepjol.info/index.php/NJG/article/view/23009
- FIG — "The Fundamental Role of GNSS in Modern Surveying": https://www.fig.net/resources/proceedings/fig_proceedings/nepal/papers/ts03b/TS03B_upadhyaya_gyawali_et_al_12890.pdf
- MDPI Remote Sensing — Advancements of Geodetic Activities in Nepal (2022): https://www.mdpi.com/2072-4292/14/7/1586
- Geospatial World — Surveying Mount Everest using GNSS and CORS: https://geospatialworld.net/article/surveying-mount-everest-using-gnss-and-cors/
- UNAVCO/EarthScope real-time data: https://www.unavco.org/data/gps-gnss/real-time/real-time.html
- ArduSimple country RTK list (Nepal not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2go monitor (no Nepal stations observed)
