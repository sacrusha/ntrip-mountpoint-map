# Tajikistan [TJ] - NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: NO public NTRIP RTK caster confirmed. National geodetic GNSS network built ~2005-2012 under World Bank LRCSP supports cadastre / orthophoto work via the FAZO Institute but no real-time RTK corrections endpoint is published. RTK2go / Centipede / EarthScope / IGS-IP: zero TJ stations. Nearest cross-border CORS is KITG (Uzbekistan, ~175 km from Dushanbe) - post-processing only at that baseline.

## Why there is no public caster

- **Agency for Land Management, Geodesy and Cartography (ALMGC)** of Tajikistan is the relevant authority (per UNECE and GIM-International references; older Russian-language sources cite "State Committee for Land Management and Geodesy" - same entity, agency since reorganization). No public NTRIP service is advertised on any state portal. Russian-language searches ("Tajikistan GNSS NTRIP set", "geodesy Tajikistan real time CORS") returned no operational endpoint 2026-05-13 / 2026-05-23. Channels checked for the negative: ALMGC web presence 2026-05-23; FAZO Institute publications 2026-05-23; avrocom-geo.tj/projects 2026-05-23; monitor.use-snip.com 2026-05-23; ntrip-list.com 2026-05-23; mvarga1989 GNSS CORS list 2026-05-23.
- **FAZO Institute** (subordinate to ALMGC) produced ~2,500 digital orthophoto sheets at 1:5,000 (0.5 m pixel) using GNSS field surveys trained under the World Bank-funded Land Registration and Cadastre System Project (LRCSP, ~2005-2012). Those activities consumed GNSS but did not result in a public NTRIP caster - the geodetic network is operated as cadastre infrastructure, not a corrections service.
- **Avrocom-Geo** (private surveyor, avrocom-geo.tj) lists GNSS-RTK cadastral measuring as a service - this is a survey contractor using their own / borrowed bases, not a public caster.
- **Central Asian Geodynamics network** (GFZ + CAIAG cooperation since 2009) operates 1 permanent GNSS station on Tajikistan territory for tectonic monitoring (CAIAG GNSS page states "30 permanent stations ... Tajikistan (1)"; fetched 2026-05-23). Research station, post-processed; no real-time RTCM stream is advertised on caiag.kg or GFZ data publications.
- **GeoComm Kazakhstan** (geocomm.kz) does not extend coverage into Tajikistan based on available material.
- **GEODNET / ONOCOY / Skylark / PointOne** - no Tajikistan ground stations confirmed.
- **Local data 2026-05-23**: `scripts/stations_by_country.py TJK` returns no entries; `scripts/stations_by_radius.py 38.56 68.78 500` returns 2 stations - both KITG00UZB0 (Uzbekistan, 175 km from Dushanbe) on AUSCORS rebroadcast + IGS-IP. KITG is single-base, far outside RTK baseline range, post-processing only.

## Hobbyist path

1. **Cm-class** - none free; deploy a local base for single-baseline RTK.
2. **Sub-decimetre** - Galileo HAS (~20-40 cm horizontal after convergence, satellite-delivered, free).
3. **Post-processing only** - KITG (UZB), DUSH (TJK - IGS post-processed; no NTRIP), or other Central Asian IGS stations via EarthScope / CDDIS.

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| EarthScope GNSS data archive (regional Central Asia + DUSH) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA) |
| NASA CDDIS (IGS / MGEX archive) | https://cddis.nasa.gov/ | Free non-commercial (account) |

## Sources

- Avrocom-Geo (private surveyor, GNSS-RTK cadastral): https://avrocom-geo.tj/index.php/projects
- ResearchGate "Cadastral mapping in Tajikistan" + GIM International article (FAZO orthophoto, World Bank LRCSP context): https://www.gim-international.com/content/article/cadastral-mapping-in-tajikistan
- ISPRS XXXIX-B6/2012 "Transfer of Technology for Cadastral Mapping in Tajikistan": https://isprs-archives.copernicus.org/articles/XXXIX-B6/41/2012/isprsarchives-XXXIX-B6-41-2012.pdf
- World Bank Tajikistan Land Reg & Cadastre project: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/704991508334674315/tajikistan-land-regis-cadastre
- ResearchGate "GNSS Permanent Networks in Kyrgyzstan" (Central Asia regional context including Tajikistan)
- ArduSimple country selector - no Tajikistan page (URL returns 404)
- GitHub mvarga1989 GNSS CORS RTK networks list - no Tajikistan entry
- Local data 2026-05-23: `scripts/stations_by_country.py TJK` -> no stations; `scripts/stations_by_radius.py 38.56 68.78 500` -> KITG00UZB0 (175 km, Uzbekistan, post-processing only)
- WebSearch "Tajikistan GNSS CORS NTRIP network 2025 cadastre national geodesy" 2026-05-23 - no public service surfaced
