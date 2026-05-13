# Nepal [NP] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh; prior pass 2026-05-06)

## Status: NO national public NTRIP caster — EarthScope/NOTA streams one Nepal CORS (KUGE) over its global caster as the only real-time path

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (domestic)** | No — no Nepali agency operates a publicly documented NTRIP endpoint |
| **EarthScope (NOTA) real-time stream** | Yes — single station `KUGE_RTCM3P3` (~27.62°N, 85.54°E, near Kathmandu) reachable via the EarthScope caster `ntrip.earthscope.org:2101` after NULA registration (legacy `rtgpsout.unavco.org:2101` retired 2025-07-29) |
| **host:port (domestic)** | null |
| **tariff (domestic)** | null |
| **tariff (EarthScope)** | Free for non-commercial use after NULA acceptance; USD 1,000/seat/yr commercial |
| **hobbyist_eligibility** | EarthScope: yes (non-commercial); no domestic service to evaluate |
| **legal_residency_required** | EarthScope: no — open globally with NULA |
| **last_confirmed_alive** | KUGE_RTCM3P3 listed in `data/stations.json` (earthscope source, ingested via the local fetch pipeline); no Nepal-hosted caster confirmed at any date |

## Most Recent Project Announcement

- **2019 (ongoing):** Nepal's Survey Department (Geodetic Survey Division) announced plans to establish 50+ CORS stations covering the entire country, with an initial 2 stations at Nagarkot. As of 2024 no public NTRIP endpoint has been published.
- **2016:** UN/Nepal Workshop on GNSS Applications (hosted by the Survey Department, Kathmandu, December 2016) included RTK and RTKLIB demonstrations; no NTRIP service was launched at that time.
- **UNAVCO/GAGE:** 11 existing scientific CORS (JMLA, NPGJ, JMSM, BESI, CHLM, NAST, SYBC, SNDL, RMJT, BRNZ) plus 5 newer stations operated by UNAVCO and Department of Mines and Geology — geodetic/scientific purpose, not an RTK corrections service for public use.
- Survey Department official site: https://survey.gov.np/

## Context Notes

- Nepal's Survey Department (Geodetic Survey Division) maintains 2 operational CORS stations at Nagarkot plus one at the Minbhawan head office (under construction in recent reporting), with ambition for 50+ stations covering the country. No public NTRIP endpoint has been advertised.
- UNAVCO/EarthScope (now NOTA / GAGE) operates ~16 scientific GNSS CORS in Nepal for seismic and geodynamic monitoring. Most are archival/post-processing only. **One station (KUGE) is publicly streamed via the EarthScope NTRIP caster in RTCM 3 MSM5 format** (mountpoint `KUGE_RTCM3P3`); requires a NOTA user account (NULA). This is the only realistically reachable real-time stream for hobbyists in Nepal as of 2026-05-12.
- NMGISC (National Mapping and Geospatial Information System Centre) and the Survey Department have both expressed intent to build a national CORS/NTRIP network, but no operational service has been publicly announced.
- Nepal lies in a high-seismicity zone; post-2015 Gorkha earthquake geodetic infrastructure has been rebuilt with international support (UNAVCO, IGS), but the focus has been scientific monitoring rather than survey-grade real-time corrections.
- Commercial global networks (GEODNET, ONOCOY, PointOne, Centipede): no Nepal coverage confirmed.
- rtk2go (per `scripts/stations_by_country.py NPL` 2026-05-12): no Nepal mountpoints.
- Practical workaround for hobbyists in Nepal: connect to `KUGE_RTCM3P3` via the EarthScope caster (baseline ≤ ~30 km from Kathmandu / Bhaktapur for cm-grade fix); for sites away from KUGE, deploy a local base station or fall back to satellite PPP (Trimble RTX, Galileo HAS, NRCAN PPP).

## Real-Time + Post-Processing Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope/NOTA real-time stream** — `ntrip.earthscope.org:2101` mountpoint `KUGE_RTCM3P3` (Kathmandu area, RTCM 3 MSM5) | https://www.earthscope.org/data/gnss-data/real-time/ | Free non-commercial after NULA |
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
- RTK2go monitor (no Nepal stations observed; confirmed via `scripts/stations_by_country.py NPL` 2026-05-12)
- Local pipeline check `scripts/stations_by_country.py NPL` (2026-05-12) — earthscope source returns 1 station (KUGE_RTCM3P3 at 27.62°N, 85.54°E)
