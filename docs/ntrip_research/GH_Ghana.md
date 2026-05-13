# Ghana [GH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry)

## Status: CORS network deployed (Aug 2025 nationwide launch); NTRIP caster endpoint NOT publicly disclosed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — physical network operational; no public host:port found |
| **Network name** | Ghana National CORS Network (SMD / Lands Commission) |
| **Operator** | Survey and Mapping Division (SMD), Lands Commission (`lc.gov.gh`), in PPP with GMX Systems Ghana Limited and Geo-Tech Systems Ltd |
| **host:port** | Not publicly published — no caster endpoint found in any directory or sourcetable as of 2026-05-12 |
| **tariff** | Not publicly listed; access expected through licensed-surveyor channel |
| **hobbyist_eligibility** | Unclear — network promoted for cadastral and hydrospatial surveys; no published hobbyist policy |
| **legal_residency_required** | Unclear — no published terms of service found |
| **last_confirmed_alive** | `https://www.lc.gov.gh/` HTTP 200 confirmed 2026-05-12; no GH mountpoint in any public NTRIP sourcetable (rtk2go / Centipede / EarthScope local stations.json 2026-05-12) |
| **Operator contact (technical partner)** | GMX Systems Ghana — `info@gmxsys.com`, +233 24 2133760 / +233 50 8988316; CORS page: https://www.gmxgh.com/index.php/cors-network/ (lists the network but publishes no host/port/tariff) |

## Operator

**Survey and Mapping Division (SMD) — Lands Commission**
P.O. Box MB 237, Accra, Ghana
Phone: 0302 429 760 / 0302 429 762 / 050 557 8100
Email: info@lc.gov.gh
Website: https://www.lc.gov.gh/

**GMX Systems Ghana Limited** — technical partner (subsidiary of GMX Systems Ltd., Israel)
**Geo-Tech Systems Ltd., Ghana** — PPP partner; provides field integration

## Timeline

| Date | Event |
|------|-------|
| Pre-2020 | SMD deploys 4 pilot CORS in Greater Accra, Ashanti, Western, and Brong-Ahafo regions; supports static (≤100 km) and RTK (≤20 km) survey |
| 2021 | Geo-Tech Systems / GMX Systems enter public-private partnership with Ghana Water Company and Lands Commission for a nationwide 85-station CORS network — described as the most extensive CORS network in West Africa at the time |
| Aug 19, 2025 | Lands Commission officially unveils the CORS network; nationwide observation exercise launched to tie 60+ newly established stations into the national geodetic framework (Ghana Grid Coordinate System). Plan to expand to 100 stations by end of 2025 |
| Aug 19, 2025 | Lands Commission simultaneously launches "digital geospatial data system" (DGDS) — a broader platform for 24/7 geospatial data access including CORS-derived corrections |

## Network Details

- **Stations:** ~60 physical CORS deployed nationwide as of Aug 2025; target 100 stations
- **Zoning:** Three geographic sectors — southern, middle belt, and upper
- **Claimed precision:** Centimetre-level accuracy for RTK fieldwork
- **Purpose stated:** Cadastral surveys, hydrospatial surveys, and other geospatial applications
- **Caster software / host:port:** Not published; GMX Systems supplies CORS hardware and likely NTRIP back-end software; no public sourcetable or registration portal found
- **WGIC case study:** Ghana network cited as an "exemplar geospatial PPP" in the World Geospatial Industry Council's Africa Geospatial PPPs report

## Negative Findings

- RTK2GO / Centipede / EarthScope: Zero GH mountpoints in any public sourcetable (verified via local `data/stations.json` 2026-05-12)
- NTRIP-list.com Africa: Ghana not listed
- ArduSimple country directory: Ghana not listed with a free or commercial NTRIP service
- mvarga1989 GNSS CORS list (GitHub): No Ghana NTRIP endpoint
- GMX Ghana CORS page (https://www.gmxgh.com/index.php/cors-network/, 2026-05-12) advertises the network but publishes no host, port, mountpoint, tariff or registration URL — access still gated to direct contact
- No public caster address found in any indexed source, academic paper, or news article as of 2026-05-12

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **SMD / Lands Commission** — RINEX data availability not confirmed; contact SMD directly | https://www.lc.gov.gh/ | Unknown |
| **IGS / EarthScope** — NSAS (Accra) station archive for post-processing | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |
| **GSSTI (Ghana Space Science and Technology Institute)** — hosts AFREF archive station in Accra; RINEX access via IGS network | https://www.gssti.gov.gh/ | Free non-commercial |

## Sources Consulted
- GPS World — Ghana nationwide CORS exercise: https://www.gpsworld.com/ghana-launches-nationwide-cors-network-exercise/
- Ghana News Agency — DGDS launch Aug 2025: https://gna.org.gh/2025/08/lands-commission-launches-digital-geospatial-data-system/
- Ghana Business News — DGDS launch: https://www.ghanabusinessnews.com/2025/08/20/lands-commission-launches-digital-geospatial-data-system/
- MyJoyOnline — Lands Commission / LiSAG / GMX launch: https://www.myjoyonline.com/lands-commission-lisag-and-gmx-launch-nationwide-gps-cors-network-observation/
- WGIC — Nationwide CORS Network Ghana PPP: https://wgicouncil.org/nationwide-cors-network-ghana-an-exemplar-geospatial-ppp/
- Graphic Online — CORS deployment: https://www.graphic.com.gh/news/general-news/ghana-news-lands-commission-deploys-effective-continuous-operating-reference-system.html
- Springer — CORS usage Greater Accra Region: https://link.springer.com/article/10.1007/s41651-020-00061-8
- SMD page on lc.gov.gh: https://www.lc.gov.gh/about-us/organizational-structure/survey-mapping-division-smd/
- mycoordinates.org — GNSS software for Ghana SMD: https://mycoordinates.org/development-of-gnss-software-for-ghana-survey-and-mapping-division/
- RTK2GO monitor (monitor.use-snip.com) — no GH mountpoints visible
- NTRIP-list.com/africa — Ghana not listed
- GMX Systems Ghana CORS network page: https://www.gmxgh.com/index.php/cors-network/ (2026-05-12, fetched via WebFetch — no caster credentials disclosed)
- Coordinates magazine — Ghana DGDS launch: https://mycoordinates.org/ghana-launches-digital-geospatial-data-system/
- curl probe of `https://www.lc.gov.gh/` 2026-05-12 — HTTP 200 OK
