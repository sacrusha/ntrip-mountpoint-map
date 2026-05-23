# UAE [AE] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

Two emirate-level government NRTK networks — DVRS (Dubai Municipality, 18
GNSS stations) and AD-GRS (DMT Abu Dhabi, 32 CORS). Both are gated behind
emirate-portal applications oriented at survey / construction / GIS
professionals; neither publishes a host:port, neither publishes a price
list. No tariff and no clear hobbyist tier on either; both effectively
require an emirate-pass account (UAE Pass / DM portal account) so
function as paid+restricted for an outside hobbyist.

One free single-base on rtk2go in Sharjah (`MARAKEB`) covers a ~20-50 km
radius around 25.32, 55.45 — the only zero-friction free RTK path for an
AE hobbyist. Two IGS-IP rebroadcasts (DUBI00ARE0, ADH100ARE0) are
research-only (single-base, IGS data policy).

No emirate-level network in Sharjah / Ajman / Umm Al Quwain / Ras Al
Khaimah / Fujairah; no UAE-federal NTRIP service.

## Casters

### DVRS — Dubai Virtual Reference Station (Dubai Municipality)

- operator: Dubai Municipality, Survey Department
- landing_url: https://www.dm.gov.ae/survey-department/dubai-virtual-reference-station/
- access_url: https://survey.dm.gov.ae/Admin/Dashboard/CheckFormExist?ApiServiceid=3706
  (DM survey portal — DVRS subscription request, linked from the landing page;
  the older GeoDubai SharePoint portal at https://geodubai.dm.gov.ae/ has been
  unified under this DM Survey Application platform)
- access_type: paid — operator landing describes a subscription model;
  ArduSimple categorises DVRS as "paid regional service"; no pricing
  published on the landing page (tariff not published — checked:
  dm.gov.ae landing 2026-05-23 via WebFetch; ArduSimple UAE page
  2026-05-23 via WebFetch; geospatialworld.net Dubai-reference interview
  2026-05-23)
- coverage: Emirate of Dubai (~4,114 km²); operator describes "whole of
  Dubai" with sub-cm 24/7 accuracy
- num_stations: 18 (operator-declared; verbatim 2026-05-23 from dm.gov.ae:
  *"more than 18 GNSS stations covering the whole of Dubai"*)
- hobbyist_eligibility: no — DVRS subscription is gated through
  survey.dm.gov.ae, which routes applications to surveying, construction,
  GIS and government users; a DM portal account is required, which
  practically requires UAE Pass / Emirates ID
- residency_required: ? — DM portal access is not formally residency-locked
  but in practice requires UAE Pass / Emirates ID, which is residency-
  bound (checked: dm.gov.ae 2026-05-23 WebFetch — registration requires
  DM portal account; geospatialworld 2026-05-23 — describes professional
  subscriber base)
- datum_epoch: WGS84 / ITRS — declared on the Dubai Municipality Geodesy
  page (https://www.dm.gov.ae/survey-department/geodesy/, WebFetch 200
  2026-05-23: *"realization of … WGS84 … and the international
  Terrestrial Reference System ITRS … via the connection of 4 selected
  main sites of the Dubai national GPS network to the closest IGS
  Permanents tracking sites"*). Epoch not stated on the operator page.
  Local grid is EPSG:3997 (WGS 84 / Dubai Local TM, central meridian
  55°20′E, false easting 500 km); orthometric heights use a precise
  gravimetric geoid model.

Notes: Designed 2001, tested 2002, launched 2003 — first NRTK in the
Middle East. Originally 5 Leica + Geo++ GNSMART, since expanded to 18+
quad-constellation (GPS+GLO+GAL+BDS). Caster host is not disclosed
publicly; `geodubai.dm.gov.ae:2101` (213.42.55.155) and
`survey.dm.gov.ae:2101` (213.42.54.19) probed 2026-05-23 — both TCP
timed out (DM caster either gated to the customer-facing host issued
post-subscription, or restricted from non-AE source addresses).

### AD-GRS — Abu Dhabi GNSS Reference Stations Network

- operator: Department of Municipalities and Transport (DMT), Abu Dhabi
  (2017–2019 expansion delivered in partnership with Fugro)
- landing_url: https://geosmart.dmt.gov.ae/LSDCompany/PDFs/Survey%20Standards/Abu%20Dhabi%20Spatial%20Reference%20System.pdf
  (DMT GeoSMART survey-standards PDF; no dedicated landing page found)
- access_url: https://www.tamm.abudhabi/en/life-events/business/housing-construction/construction/RequesttoJointheSurveyStationsNetworkSystem
  (TAMM "Request to Join the Survey Stations Network System" — the AD-GRS
  registration path per ArduSimple; SPA-rendered, empty WebFetch body
  2026-05-23, but cited live by ArduSimple same date)
- access_type: paid — ArduSimple categorises AD-GRS as a paid regional
  service; TAMM service flow routes applications to construction /
  housing professionals (tariff not published — checked: TAMM service
  page 2026-05-23 WebFetch (SPA empty body); ArduSimple UAE 2026-05-23;
  Fugro technical paper 2026-05-23)
- coverage: Emirate of Abu Dhabi (~67,340 km²); ADCN (Abu Dhabi city,
  coastal) and MDZN (Madinat Zayed, inland) are the most-cited stations
  in academic work
- num_stations: 32 (Fugro technical paper, recomputed 2017–2019; plus
  53 supplementary geodetic control pillars). An earlier 2008
  configuration had 20 CORS — superseded.
- hobbyist_eligibility: no — TAMM service is "Request to Join the
  Survey Stations Network System" gated to construction/housing
  professionals; UAE Pass / Emirates ID required
- residency_required: ? — TAMM requires UAE Pass which is residency-
  bound in practice; no explicit nationality rule found on the service
  page (checked: TAMM service URL 2026-05-23 WebFetch; ArduSimple UAE
  2026-05-23; ResearchGate Georeferencing Abu Dhabi 2026-05-23 via
  WebSearch)
- datum_epoch: ITRF2014 at epoch 2019.0 — Fugro technical paper
  (https://www.fugro.com/expertise/technical-papers/enhanced-geodetic-network-geoid-model-municipalities-abu-dhabi-emirate-fugro,
  WebFetch 200 2026-05-23): *"Abu Dhabi GPS Reference Stations network,
  consisting of 32 CORS, was recomputed in both ITRF2014 at Epoch 2019.0
  and historical ITRF2000 at Epoch 2000.0"*. Vertical datum: Ras Ghumays.

### MARAKEB — rtk2go single-base (Sharjah)

- operator: rtk2go community caster (Subcarrier Systems Corp / SNIP);
  base station operator anonymous, name suggests Marakeb Technologies LLC
  (UAE unmanned-systems company), no operator-confirmed link
- See `RTK2GO.md` for credentials / etiquette / known-unreliable warning
- access_type: free, no registration (rtk2go convention: any email as
  username, password `none`)
- coverage: ~20–50 km radius around 25.32, 55.45 (Sharjah, ~22 km NE
  of Dubai centre); useful for hobbyist work across Dubai-Sharjah-Ajman
  metro
- num_stations: 1 (single base)
- hobbyist_eligibility: yes
- residency_required: no
- sourcetable: `rtk2go.com:2101`, mountpoint `MARAKEB` — present in
  `data/rtk2go.sourcetable` 2026-05-23. RTCM 3.2 stream
  (1005, 1033, 1074, 1084, 1094, 1114, 1124 → GPS+GLO+GAL+QZSS+BDS MSM4
  + station info).
- vrs: no
- stations_source: rtk2go monitor https://monitor.use-snip.com/
- datum_epoch: omitted — base operator does not declare a datum; rtk2go
  does not transmit a transformation message

### IGS-IP — DUBI00ARE0, ADH100ARE0

- operator: IGS / EarthScope / BKG rebroadcast (covered in `IGS.md` and
  `Earthscope.md`)
- DUBI00ARE0 — Dubai (25.00, 55.47), TRIMBLE NETR9, RTCM 3.2 + MSM3
  (msgs 1073/1083/1093/1123 per `data/igs_ip.sourcetable` 2026-05-23),
  GPS+GLO+GAL+BDS, hosted on the Dubai Municipality premises (same site
  as DVRS core); rebroadcast by IGS NRIAG
- ADH100ARE0 — Abu Dhabi area (24.38, 54.52), SEPT POLARX5, RTCM 3.2 +
  MSM4, GPS+GLO+GAL+BDS, rebroadcast via Fugro contribution
- access_type: restricted — IGS registration at register.rtcm-ntrip.org;
  IGS data policy = research / non-commercial
- These are single-base streams, not VRS / NRTK. Useful for Dubai-city or
  Abu Dhabi-city RTK only, and for post-processing.

## Disqualified / not applicable

- **Centipede** — 0 AE nodes 2026-05-23 (`py scripts/stations_by_country.py ARE`).
- **EarthScope NOTA** — Americas-only.
- **GEODNET, onocoy, PointOne, HxGN SmartNet, Trimble VRS Now** — no
  UAE coverage advertised on public coverage maps 2026-05-23.
- **Other emirates (Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah,
  Fujairah)** — no emirate-level public NTRIP caster found; surveying
  firms operating there use DVRS or AD-GRS reach or private bases.
- **UAE federal** — no UAE-federal NTRIP network; each emirate manages
  its own geodetic infrastructure.

## Post-Processing (RINEX) fallback

| Service | URL | Notes |
|---|---|---|
| DVRS / GeoDubai RINEX | https://geodubai.dm.gov.ae/ | Requires DM portal account |
| AD-GRS RINEX | https://geosmart.dmt.gov.ae/ + TAMM application | Application-gated |
| IGS / EarthScope | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted

- Dubai Municipality DVRS page (WebFetch 200 2026-05-23):
  https://www.dm.gov.ae/survey-department/dubai-virtual-reference-station/
- Dubai Municipality Geodesy / datum declaration (WebFetch 200 2026-05-23):
  https://www.dm.gov.ae/survey-department/geodesy/
- DM Survey Application portal (subscription router):
  https://survey.dm.gov.ae/Admin/Dashboard/CheckFormExist?ApiServiceid=3706
- GeoDubai portal (legacy front-end):
  https://geodubai.dm.gov.ae/en/Pages/default.aspx
- Geospatial World — Establishment & Testing of DVRS (FIG Cairo paper
  mirror): https://geospatialworld.net/article/establishment-testing-of-dubai-virtual-reference-system-dvrs-national-gps-rtk-network/
- Geospatial World — Dubai's Reference Station interview:
  https://geospatialworld.net/prime/interviews/dubai-reference-station-middle-east-first/
- FIG Cairo paper — Establishment of DVRS:
  https://www.fig.net/resources/proceedings/fig_proceedings/cairo/papers/ts_03/ts03_04_marzooqi_etal.pdf
- DMT Abu Dhabi Spatial Reference System PDF (GeoSMART survey-standards):
  https://geosmart.dmt.gov.ae/LSDCompany/PDFs/Survey%20Standards/Abu%20Dhabi%20Spatial%20Reference%20System.pdf
- Fugro technical paper (32 CORS, ITRF2014@2019.0, Ras Ghumays vertical;
  WebFetch 200 2026-05-23):
  https://www.fugro.com/expertise/technical-papers/enhanced-geodetic-network-geoid-model-municipalities-abu-dhabi-emirate-fugro
- TAMM service — Request to Join the Survey Stations Network System
  (SPA-rendered, empty WebFetch body; URL live per ArduSimple):
  https://www.tamm.abudhabi/en/life-events/business/housing-construction/construction/RequesttoJointheSurveyStationsNetworkSystem
- ResearchGate — Georeferencing System for Abu Dhabi Spatial Data (2008
  vs 2019 vintage of the network): https://www.researchgate.net/publication/331608656_Georeferencing_System_for_Abu_Dhabi_Spatial_Data
- ISPRS Annals 2025 — UAE GNSS error variations (ADCN, MDZN):
  https://isprs-annals.copernicus.org/articles/X-G-2025/87/2025/isprs-annals-X-G-2025-87-2025.pdf
- American University of Sharjah — first UAE IGS station (AUS site
  joining IGS observation network):
  https://www.aus.edu/media/news/first-gnss-station-with-igs-service-to-be-installed-in-the-uae
- ArduSimple UAE NTRIP (WebFetch 200 2026-05-23):
  https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-uae-united-arab-emirates/
- EPSG:3997 — WGS 84 / Dubai Local TM: https://epsg.io/3997
- Direct TCP probes 2026-05-23:
  - `geodubai.dm.gov.ae:2101` (213.42.55.155) → timed out
  - `survey.dm.gov.ae:2101` (213.42.54.19) → timed out
- Local data 2026-05-23: `py scripts/stations_by_country.py ARE` →
  igs_ip:2 (DUBI00ARE0, ADH100ARE0), rtk2go:1 (MARAKEB)
