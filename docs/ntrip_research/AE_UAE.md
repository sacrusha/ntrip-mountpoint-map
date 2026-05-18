# UAE [AE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (originally 2026-05-06; refactored 2026-05-12, 2026-05-15, 2026-05-17)

## Status: PARTIAL — DVRS (Dubai) and AD-GRS (Abu Dhabi) exist as government NRTK networks but are restricted to licensed surveyors / professional applicants; no hobbyist tier confirmed on either. One free hobbyist-accessible single-base mountpoint exists on rtk2go in Sharjah (MARAKEB). Two IGS reference stations (DUBI00ARE, ADH100ARE) are rebroadcast on IGS-IP — single-base, scientific use only.

---

## 1. DVRS — Dubai Virtual Reference System

| Field | Value |
|---|---|
| **landing_url** | https://www.dm.gov.ae/survey-department/dubai-virtual-reference-station/ |
| **access_url** | https://geodubai.dm.gov.ae/sites/buildingsmart/en/Pages/Registration.aspx (GeoDubai BIM/portal registration; DVRS subscription routed via `survey.dm.gov.ae/Admin/Dashboard/CheckFormExist?ApiServiceid=3706` linked from the landing page) |
| **operator** | Dubai Municipality, Survey Department |
| **host:port** | Not publicly disclosed. `geodubai.dm.gov.ae:2101` is the historically cited NTRIP endpoint in older third-party documentation; not verifiable from this sandbox (no outbound :2101 reachability). Operator does not publish the caster hostname. |
| **tariff** | Not publicly listed on operator landing as of 2026-05-17 (source: https://www.dm.gov.ae/survey-department/dubai-virtual-reference-station/). Subscription application is gated through the DM survey portal; price discovery requires a logged-in application. Currency unknown (AED expected). VAT status not stated. |
| **num_stations** | "More than 18" quad-constellation (GPS+GLO+GAL+BDS) reference stations across Dubai Emirate, verbatim from dm.gov.ae landing page (re-fetched 2026-05-17). |
| **vrs** | yes (VRS with NMEA GGA upload; RTCM streamed back). |
| **hobbyist_eligibility** | no — application restricted to surveying, construction, GIS, and government contractors per geospatialworld.net interview and operator portal flow. |
| **legal_residency_required** | unclear — no explicit residency clause; practical access requires UAE professional licensing / DM portal account, which is effectively residency-bound. |
| **last_confirmed_alive** | 2026-05-17 — `dm.gov.ae/survey-department/dubai-virtual-reference-station/` WebFetch 200 with content. `geodubai.dm.gov.ae/en/Pages/default.aspx` not re-probed this round. NTRIP port 2101 not probed from sandbox. |
| **datum_epoch** | WGS84 / ITRS — declared on operator geodesy page; epoch **not stated** on the operator page. Source: https://www.dm.gov.ae/survey-department/geodesy/ (re-fetched 2026-05-17). |

**Notes:**
- Designed 2001, tested 2002, service launched 2003 per FIG Cairo paper (Establishment & Testing of DVRS, mirrored on geospatialworld.net) — first NRTK network in the Middle East (5 Leica stations + Geo++ GNSMART originally; since expanded to 18+ quad-constellation stations). Third-party (non-operator) source notes ITRF2000 anchor epoch 2000.0 — not citable per operator-declaration rule, kept here as context only: https://geospatialworld.net/article/establishment-testing-of-dubai-virtual-reference-system-dvrs-national-gps-rtk-network/
- Local grid: Dubai Local Transverse Mercator (DLTM, central meridian 55°20′E, false easting 500 km) on WGS84 ellipsoid — EPSG:3997.
- Precise gravimetric geoid model exists for orthometric heights.
- The dm.gov.ae landing page now links DVRS subscription via `survey.dm.gov.ae/.../CheckFormExist?ApiServiceid=3706`, suggesting the portal has been unified under the DM Survey Application platform rather than legacy GeoDubai SharePoint pages. Earlier prior-research speculation that "the service may have been restructured" is confirmed: it's the same agency, new front-door.

---

## 2. AD-GRS — Abu Dhabi GNSS Reference Stations Network (Abu Dhabi Spatial Reference System)

| Field | Value |
|---|---|
| **landing_url** | https://geosmart.dmt.gov.ae/LSDCompany/PDFs/Survey%20Standards/Abu%20Dhabi%20Spatial%20Reference%20System.pdf (DMT GeoSMART survey-standards PDF; no dedicated landing page found) |
| **access_url** | https://www.tamm.abudhabi/en/life-events/business/housing-construction/construction/RequesttoJointheSurveyStationsNetworkSystem (TAMM service "Request to Join the Survey Stations Network System" — cited as the AD-GRS registration path by ardusimple.com, re-confirmed 2026-05-17) |
| **operator** | Department of Municipalities and Transport (DMT), Abu Dhabi (in partnership with Fugro for the 2017–2019 build-out) |
| **host:port** | Not publicly disclosed. No public sourcetable URL surfaced; operator does not publish the caster hostname. |
| **tariff** | Not publicly listed as of 2026-05-17 (source: https://www.tamm.abudhabi/en/life-events/business/housing-construction/construction/RequesttoJointheSurveyStationsNetworkSystem — service "Request to Join the Survey Stations Network System"). TAMM application gating; price discovery requires submitting the service request. Currency unknown (AED expected). VAT status not stated. |
| **num_stations** | 32 CORS across Abu Dhabi Emirate (recomputed 2019 by Fugro); plus 53 supplementary geodetic control pillars. Source: Fugro technical paper. |
| **vrs** | ? — system described as network-RTK GRS providing centimeter-level corrections; VRS vs MAC/FKP not explicitly stated in public docs. |
| **hobbyist_eligibility** | no — application is a government service "Request to Join the Survey Stations Network System" oriented at construction/housing professionals. |
| **legal_residency_required** | unclear — TAMM is the Abu Dhabi resident/business services portal; account creation typically requires a UAE Pass / Emirates ID, which is effectively residency-bound. |
| **last_confirmed_alive** | 2026-05-17 — Fugro technical-paper page re-fetched, 200 OK, confirms 32 CORS / ITRF2014@2019.0 / ITRF2000@2000.0. `tamm.abudhabi/...` still SPA-rendered (empty body via WebFetch), cited live by ardusimple.com (2026-05-17). No external NTRIP probe possible from sandbox. |
| **datum_epoch** | Abu Dhabi SRS — WGS84 / ITRF2000 at epoch 2000.0 (original 2008 establishment); recomputed in ITRF2014 at epoch 2019.0 by Fugro 2017–2019. Vertical: Ras Ghumays national vertical datum. Source: https://www.fugro.com/expertise/technical-papers/enhanced-geodetic-network-geoid-model-municipalities-abu-dhabi-emirate-fugro |

**Notes:**
- AD-GRS replaced the legacy Nahrwan 1967 datum as the official Abu Dhabi geodetic reference.
- The two CORS most commonly cited in academic literature are ADCN (Abu Dhabi city, coastal) and MDZN (Madinat Zayed, inland) — confirmed in a 2025 ISPRS Annals paper on UAE GNSS error variations.
- This entry is missing from prior project research (networks.md has no AD-GRS row; country_markers.json only has DVRS). PIPELINE NOTE downstream.

---

## 3. MARAKEB — rtk2go single-base (Sharjah)

| Field | Value |
|---|---|
| **landing_url** | http://rtk2go.com/ |
| **access_url** | http://new.rtk2go.com/ (rtk2go reservation/usage — free community caster; mountpoint discoverable via the public sourcetable) |
| **operator** | rtk2go community caster (Subcarrier Systems Corp / SNIP); base station operator anonymous (mountpoint name suggests Marakeb Technologies LLC, a UAE unmanned-systems company, but no confirmed link). |
| **host:port** | `rtk2go.com:2101` (mountpoint `MARAKEB`) — present in `data/rtk2go.sourcetable`; re-verified 2026-05-17 via `scripts/stations_by_country.py ARE` |
| **tariff** | free (community); rtk2go requires a valid email address as user/pw on the mountpoint per rtk2go.com terms. |
| **num_stations** | 1 (single base). |
| **vrs** | no — single-base RTCM 3.2 stream (messages 1005, 1033, 1074, 1084, 1094, 1124 → GPS+GLO+GAL+BDS MSM4 + station info). |
| **hobbyist_eligibility** | yes — rtk2go is open to anyone with a valid email; no professional credentials required. |
| **legal_residency_required** | no. |
| **last_confirmed_alive** | 2026-05-17 — present in current rtk2go sourcetable. Coverage radius ~20–50 km from 25.32 N, 55.45 E (Sharjah, ~22 km NE of Dubai centre). |
| **datum_epoch** | base operator does not publish a datum; rtk2go streams the operator's local frame. Treat as unknown — likely WGS84 current epoch but uncited. Omitted per spec. |

---

## 4. Other Emirates / Federal — Negative Findings

- **Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah, Fujairah:** no emirate-level public NTRIP caster found. Surveying firms cited as operating across these emirates rely on DVRS (Dubai) or AD-GRS (Abu Dhabi) reach or private base stations.
- **UAE federal:** no UAE-federal NTRIP network found; each emirate manages its own geodetic infrastructure.
- **rtk2go (other than MARAKEB):** 1 station total in ARE (`scripts/stations_by_country.py ARE`, 2026-05-17).
- **Centipede:** zero AE nodes (2026-05-17, same script).
- **EarthScope (NOTA):** zero AE stations (no ARE territory tag).
- **GEODNET:** coverage map (`rtk.geodnet.com/coverage/`) renders client-side; sandbox WebFetch returns headers only. No UAE GEODNET station cited in any web result. UAE coverage **unknown — not verified this pass** (GEODNET not in local pipeline sources; client-side coverage map not extractable from sandbox).
- **IGS-IP:** 2 ARE stations rebroadcast on `products.igs-ip.net:2101` and present in `data/igs_ip.sourcetable` (2026-05-17): `DUBI00ARE0` (Dubai, 25.0023 N 55.4668 E, TRIMBLE NETR9, GPS+GLO+GAL+BDS real-time, co-located on Dubai Municipality premises — same site as DVRS core) and `ADH100ARE0` (Abu Dhabi area, 24.38 N 54.52 E, 16 km from city centre). IGS-IP registration required (`register.rtcm-ntrip.org`); IGS data-use policy = research/non-commercial. Single-base streams, not VRS/NRTK. The 2024 announcement of American University of Sharjah as "first UAE IGS station" referred to AUS site joining IGS observation network; DUBI and ADH1 have been IGS members earlier (DUBI listed in IGS network for years).

---

## 5. Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **DVRS / GeoDubai** RINEX | https://geodubai.dm.gov.ae/ (when reachable; sandbox got ECONNREFUSED on 2026-05-15, not re-probed 2026-05-17) | Requires DM portal account |
| **AD-GRS** RINEX | https://geosmart.dmt.gov.ae/ + TAMM application | Application-gated |
| **IGS / EarthScope** | https://network.igs.org/ , https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## 6. Global Free Fallback

- **Galileo HAS** (~20–40 cm convergence, no connectivity required, globally available including UAE).

---

## URL Probe Results (from this sandbox, 2026-05-17)

| URL | Result |
|---|---|
| https://www.dm.gov.ae/survey-department/dubai-virtual-reference-station/ | WebFetch 200 — "more than 18 GNSS stations cover whole of Dubai"; GPS+GLO+GAL+BDS; NTRIP wireless; sub-cm 24/7; subscription link present |
| https://www.fugro.com/expertise/technical-papers/enhanced-geodetic-network-geoid-model-municipalities-abu-dhabi-emirate-fugro | WebFetch 200 — confirms 32 CORS, recomputed both ITRF2014@2019.0 and ITRF2000@2000.0 |
| https://network.igs.org/DUBI00ARE | WebFetch 200 — TRIMBLE NETR9, last RINEX 2026-05-06 |
| https://network.igs.org/ADH100ARE | (not probed; presence verified via local sourcetable) |
| https://www.dm.gov.ae/survey-department/geodesy/ | WebFetch 200 OK; WGS84/ITRS declaration confirmed |
| https://geodubai.dm.gov.ae/en/Pages/default.aspx | ECONNREFUSED from sandbox; URL returned by Google Search index — likely user-side reachable, sandbox-blocked egress |
| https://www.tamm.abudhabi/.../RequesttoJointheSurveyStationsNetworkSystem | WebFetch returned empty body (SPA / JS-rendered) — URL cited live by ardusimple.com same date |
| https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-uae-united-arab-emirates/ | 200 OK; primary source for AD-GRS / TAMM cross-reference |
| https://www.fugro.com/expertise/technical-papers/enhanced-geodetic-network-geoid-model-municipalities-abu-dhabi-emirate-fugro | 200 OK; primary source for AD-GRS 32-CORS, ITRF2014@2019.0 |
| http://rtk2go.com/ (port 2101 sourcetable) | Not probed from sandbox; MARAKEB presence re-verified 2026-05-17 via `scripts/stations_by_country.py ARE` |
| https://rtk.geodnet.com/coverage/ | Page rendered client-side; UAE coverage not extractable from server HTML |
| `geodubai.dm.gov.ae:2101` | Not probed from sandbox |

---

## Sources Consulted
- Dubai Municipality DVRS page: https://www.dm.gov.ae/survey-department/dubai-virtual-reference-station/
- Dubai Municipality Geodesy page (datum declaration): https://www.dm.gov.ae/survey-department/geodesy/
- GeoDubai portal: https://geodubai.dm.gov.ae/en/Pages/default.aspx
- DM Survey Application portal: https://survey.dm.gov.ae/admin/dashboard/formnav
- Geospatial World — "Establishment & Testing of DVRS" (ITRF epoch 2000): https://geospatialworld.net/article/establishment-testing-of-dubai-virtual-reference-system-dvrs-national-gps-rtk-network/
- Geospatial World interview — "Dubai's Reference Station, Middle East's First": https://geospatialworld.net/prime/interviews/dubai-reference-station-middle-east-first/
- DMT Abu Dhabi — Abu Dhabi Spatial Reference System (PDF): https://geosmart.dmt.gov.ae/LSDCompany/PDFs/Survey%20Standards/Abu%20Dhabi%20Spatial%20Reference%20System.pdf
- Fugro technical paper (AD-GRS 32-CORS, ITRF2014@2019.0, Ras Ghumays vertical): https://www.fugro.com/expertise/technical-papers/enhanced-geodetic-network-geoid-model-municipalities-abu-dhabi-emirate-fugro
- TAMM service — Request to Join the Survey Stations Network System: https://www.tamm.abudhabi/en/life-events/business/housing-construction/construction/RequesttoJointheSurveyStationsNetworkSystem
- ISPRS Annals 2025 — UAE GNSS error assessment (ADCN, MDZN): https://isprs-annals.copernicus.org/articles/X-G-2025/87/2025/isprs-annals-X-G-2025-87-2025.pdf
- American University of Sharjah — first UAE IGS station: https://www.aus.edu/media/news/first-gnss-station-with-igs-service-to-be-installed-in-the-uae
- ArduSimple UAE NTRIP page (AD-GRS + DVRS cross-reference): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-uae-united-arab-emirates/
- EPSG:3997 — WGS 84 / Dubai Local TM: https://epsg.io/3997
- rtk2go community caster: http://rtk2go.com/
- Local project data: `data/rtk2go.sourcetable` (MARAKEB, Sharjah), `data/igs_ip.sourcetable` (DUBI00ARE0, ADH100ARE0), `data/stations.json` (refreshed 2026-05-17 via `scripts/stations_by_country.py ARE`)
