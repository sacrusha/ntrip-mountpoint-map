# Ghana [GH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21

## Status

National CORS network deployed and partially operational under the Lands Commission / SMD with PPP partners GMX Systems Ghana and Geo-Tech Systems. 52 stations reported operational as of mid-2026 against a 100-station target. **No public NTRIP caster host:port has been disclosed** on any operator site, sourcetable, or press release. No volunteer / community NTRIP coverage either.

## Network — Ghana National CORS (Lands Commission / SMD)

| Field | Value |
|---|---|
| **landing_url** | https://www.lc.gov.gh/ (Lands Commission; SMD is a division — page exists, no CORS portal exposed) |
| **access_url** | https://www.gmxgh.com/index.php/cors-network/ — operator-adjacent CORS-Network page maintained by technical partner GMX Systems Ghana. Advertises the service, lists no host/port/mountpoint/tariff/registration form; only a "CONTACT US" button. Direct contact: info@gmxsys.com, +233 24 2133760 / +233 50 8988316. No self-service signup exists. |
| **host:port** | not publicly published — no caster endpoint found in any directory, operator page, or sourcetable as of 2026-05-21 |
| **num_stations** | 52 reported operational (Graphic Online + MyJoyOnline coverage of the Aug 2025 launch and subsequent Lands Commission communications, repeated in 2026 reporting); 100-station target (timeline slipped past end-2025); ~60 stations described as "newly established" at the Aug 19 2025 nationwide observation exercise; pre-2020 SMD pilot of 4 CORS (Greater Accra, Ashanti, Western, Brong-Ahafo) |
| **vrs** | ? — no operator documentation found |
| **tariff** | not publicly listed; expected through licensed-surveyor channel |
| **hobbyist_eligibility** | ? — network framed for cadastral and hydrospatial surveys; no published hobbyist policy |
| **legal_residency_required** | ? — no published terms of service |
| **last_confirmed_alive** | `https://www.lc.gov.gh/` HTTP 200 confirmed 2026-05-21 (no CORS section); 0 GH mountpoints in any public sourcetable (rtk2go / Centipede / EarthScope, local `data/stations.json` 2026-05-21) |
| **datum_epoch** | omitted — Ghana Grid Coordinate System referenced in launch press; no citable operator declaration of datum/epoch found on lc.gov.gh or gmxgh.com |

## Operator

**Survey and Mapping Division (SMD) — Lands Commission**, P.O. Box MB 237, Accra. Phone 0302 429 760 / 0302 429 762 / 050 557 8100. Email info@lc.gov.gh. https://www.lc.gov.gh/

**GMX Systems Ghana Limited** — technical partner; Israeli-Ghanaian joint venture launched April 2022, affiliated with the Israeli Etkes Group (Leica Geosystems representative in Israel); the parent Israeli GMX Systems Ltd. entered the Ghana CORS PPP with Geo-Tech Systems, Ghana Water Company and Lands Commission in 2021. Hosts the CORS network software on its virtual platform; CORS page https://www.gmxgh.com/index.php/cors-network/ advertises the service without publishing host, port, mountpoint, tariff or registration URL.

**Geo-Tech Systems Ltd., Ghana** — PPP partner, field integration.

**LiSAG** (Licensed Surveyors Association of Ghana) — co-launch partner of the August 2025 nationwide observation exercise.

## Timeline

| Date | Event |
|------|-------|
| Pre-2020 | SMD operates 4 pilot CORS in Greater Accra, Ashanti, Western, Brong-Ahafo; supports static (≤100 km) and RTK (≤20 km) |
| 2021 | Geo-Tech / GMX enter PPP with Ghana Water Company and Lands Commission for an 85-station nationwide network |
| 2025-08-19 | Lands Commission unveils CORS network; nationwide observation exercise launched to tie ~60 newly established stations into Ghana Grid Coordinate System. Target 100 stations by end-2025 |
| 2025-08-19 | Lands Commission also launches Digital Geospatial Data System (DGDS) — broader 24/7 geospatial-access platform that includes CORS-derived corrections |
| 2026-05-21 | Subsequent reporting cites 52 CORS operational; 100-station target reaffirmed but past end-2025 deadline. No public NTRIP host:port disclosed |

## Negative Findings

- rtk2go / Centipede / EarthScope: 0 GH mountpoints (verified 2026-05-22 via local `data/stations.json` snapshot — this only covers the casters wired into our pipeline; rtk2go sourcetable was also probed directly)
- GEODNET / ONOCOY / PointOne / Skylark: no GH coverage identified. These networks are not in `data/stations.json` (not wired into our pipeline); absence is inferred from each network's own coverage page (GEODNET map shows no GH pins; ONOCOY only lists their European core 2026-05-22), not from a sourcetable probe of each commercial caster
- NTRIP-list.com Africa: Ghana not listed
- ArduSimple country directory: Ghana not listed with a free or commercial NTRIP service
- mvarga1989 GNSS CORS list (GitHub): no Ghana NTRIP endpoint
- GMX Ghana CORS page: advertises network, publishes no host/port/tariff/registration URL (re-checked 2026-05-22)
- No 2026 press release surfaces a public caster address; News Ghana parliamentary CORS coverage 2026-05 does not disclose one

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| SMD / Lands Commission RINEX availability (not confirmed; contact SMD directly) | https://www.lc.gov.gh/ | unknown |
| IGS / EarthScope — Accra-area Nigerian/Ghanaian IGS holdings | https://www.earthscope.org/data/gnss-data/ | free non-commercial (account required) |
| GSSTI (Ghana Space Science and Technology Institute) — Accra AFREF archive station | https://www.gssti.gov.gh/ | free non-commercial |

## Sources

- Israel Trade Mission to Ghana — "New Israel-Ghanaian Venture, GMX Systems, launched" (April 2022, confirms joint-venture structure, not subsidiary): https://itrade.gov.il/ghana/2022/04/13/new-israel-ghanaian-venture-gmx-systems-launched-with-festive-opening/
- GPS World — Ghana nationwide CORS exercise: https://www.gpsworld.com/ghana-launches-nationwide-cors-network-exercise/
- Ghana News Agency — DGDS launch Aug 2025: https://gna.org.gh/2025/08/lands-commission-launches-digital-geospatial-data-system/
- Ghana Business News — DGDS launch: https://www.ghanabusinessnews.com/2025/08/20/lands-commission-launches-digital-geospatial-data-system/
- MyJoyOnline — Lands Commission / LiSAG / GMX launch: https://www.myjoyonline.com/lands-commission-lisag-and-gmx-launch-nationwide-gps-cors-network-observation/
- WGIC — Nationwide CORS Network Ghana PPP exemplar: https://wgicouncil.org/nationwide-cors-network-ghana-an-exemplar-geospatial-ppp/
- Graphic Online — CORS deployment: https://www.graphic.com.gh/news/general-news/ghana-news-lands-commission-deploys-effective-continuous-operating-reference-system.html
- Springer — CORS usage Greater Accra Region: https://link.springer.com/article/10.1007/s41651-020-00061-8
- SMD page: https://www.lc.gov.gh/about-us/organizational-structure/survey-mapping-division-smd/
- News Ghana — Parliament backs Lands Commission reform (2026-05): https://www.newsghana.com.gh/parliament-backs-lands-commission-reform-drive/
- Coordinates magazine — Ghana DGDS launch: https://mycoordinates.org/ghana-launches-digital-geospatial-data-system/
- GMX Systems Ghana CORS page: https://www.gmxgh.com/index.php/cors-network/
- Local: `py scripts/stations_by_country.py GHA` → no stations
