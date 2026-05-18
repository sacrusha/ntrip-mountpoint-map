# Trinidad and Tobago [TT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-13 entry)

## Status: TTAGN listed by ministry; gpscors.gov.tt DNS now resolves again from sandbox 2026-05-17 (NXDOMAIN of 2026-05-13 was transient); NTRIP port still not externally probed; EarthScope COCONet CN57 remains usable nearby alternative

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes per ministry listing (government-operated; 24/365 CORS; registration required) — but unreachable externally |
| **Operator** | Surveys and Mapping Division, Ministry of Agriculture, Land and Fisheries |
| **Network name** | Trinidad and Tobago Active Geodetic Network (TTAGN) |
| **landing_url** | `https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/` — operator (Surveys and Mapping Division) Online Web Services page; lists TTAGN as an active service and gives the access URL. Most descriptive operator-owned page reachable from sandbox. |
| **access_url** | `http://www.gpscors.gov.tt/gpscorstt` — ministry-listed access URL for TTAGN portal (registration / credential issuance path). DNS resolution intermittent (NXDOMAIN 2026-05-13, resolved 2026-05-17); contact `surmaptt@gmail.com` if portal unreachable. |
| **host:port — TTAGN** | not published; ministry-listed access URL is `http://www.gpscors.gov.tt/gpscorstt`. DNS for `gpscors.gov.tt` failed to resolve from sandbox 2026-05-13 (NXDOMAIN); same lookup on 2026-05-17 succeeded (`nslookup gpscors.gov.tt` returned A record). Earlier NXDOMAIN was therefore transient. NTRIP port reachability not yet retested. |
| **num_stations** | ? — current count not stated on operator pages reachable from sandbox. The 2013 academic design paper records an original 5-station deployment in 2007; no expansion or contraction announcement found through 2026-05-17. Confirm with `surmaptt@gmail.com` for current figure. |
| **tariff** | not published publicly; contact Surveys and Mapping Division |
| **hobbyist_eligibility** | Unclear — TTAGN primarily serves professional land surveyors and engineers; hobbyist access policy not documented |
| **legal_residency_required** | Unclear — government network; no explicit residency requirement stated |
| **last_confirmed_alive** | agriculture.gov.tt Online Web Services page HTTP 200 confirmed 2026-05-17 (TTAGN still listed as an active service); `gpscors.gov.tt` DNS resolved 2026-05-17 (transient NXDOMAIN of 2026-05-13 cleared). NTRIP port 2101 not yet re-probed in same session — service status remains **listed-active / NTRIP-port-unverified**. |
| **datum_epoch** | omitted -- no citable operator declaration on agriculture.gov.tt online-web-services page; 2013 academic design paper referenced ITRF but operator portal silent. |

## Most Recent Project Announcement

TTAGN was established as the Caribbean's first Active GPS Reference Network, originally comprising five stations, built with support from Fujitsu and Trimble Navigation. The network provides 24/365 GPS corrections. The Surveys and Mapping Division's Online Web Services page at agriculture.gov.tt lists TTAGN as an active service offering GPS corrections, with the access URL given as http://www.gpscors.gov.tt/gpscorstt. No new announcement or expansion news was found as of 2026-05-06.

## Context Notes

- **TTAGN**: A 24/365 CORS network covering both Trinidad and Tobago islands. Original deployment: 5 reference stations (2007, per 2013 academic paper). Current station count not confirmed in any source found during this research; the government's Online Web Services page does not list individual stations. No expansion announcement found.
- **Portal status timeline:** gpscors.gov.tt/GPSCORSTT/default.aspx returned ECONNREFUSED 2026-05-06; DNS resolution for `gpscors.gov.tt` FAILED 2026-05-13 (NXDOMAIN from sandbox resolver); DNS resolution SUCCEEDED 2026-05-17 (A record returned). The 2026-05-13 NXDOMAIN appears to have been a transient resolver issue, not a domain takedown. The agriculture.gov.tt ministry page still references `http://www.gpscors.gov.tt/gpscorstt` (HTTP 200 confirmed 2026-05-17, TTAGN listed alongside CMIS at surveys.gov.tt and the CMIS public map at surveys.gov.tt/publicmap). NTRIP caster public-routability for non-TT IPs remains unverified — ministry-only network access still plausible.
- **CMIS (Cadastre Management Information System) / surveys.gov.tt**: Listed alongside TTAGN as an Online Web Service. Public map at https://www.surveys.gov.tt/publicmap. Run by Surveys and Mapping Division but unrelated to NTRIP/RTK.
- **DNS lookup of `gpscors.gov.tt`**: FAILED 2026-05-13 (transient); SUCCEEDED 2026-05-17. Port 2101 not yet re-probed in 2026-05-17 session.
- **Nearest viable RTK alternative within ~50 km**: EarthScope COCONet station **CN57_RTCM3P3** (10.84°N -60.94°W, ~55 km off Tobago's east coast) reachable via the ingested EarthScope NOTA caster — coverage tracked via local helper script (`py scripts/stations_by_radius.py 10.5 -61.3 200`, source filter `earthscope`). EarthScope NULA + non-commercial use applies; see docs/ntrip_research notes on EarthScope (researched separately, not duplicated here).
- **Surveys and Mapping Division** contact: 118 Frederick Street, Port of Spain; phone 868-627-9201 ext. 237; email surmaptt@gmail.com.
- **Spatial Dimension** (UK GIS firm) supported the division's Cadastre Management Information System (CMIS / Landfolio); not related to NTRIP caster operations.
- The Surveys and Mapping Division also operates as the Land Survey Board registrar — suggesting NTRIP access may be limited to licensed land surveyors.
- **RTK2go / Centipede-RTK**: No Trinidad and Tobago base stations in public sourcetables per 2026-05-13 ingest; not re-checked 2026-05-17.
- **EarthScope (NOTA)**: One Trinidad-region COCONet station available — **CN57_RTCM3P3** (10.84°N, -60.94°W, off the east coast between Trinidad and Tobago) — confirmed in local data 2026-05-13 with `[TTO]` country code. Free for non-commercial use with NULA. Full EarthScope NOTA detail lives outside this file (ingested-global; reference via helper scripts, not duplicated as caster entry).
- **Global commercial fallbacks:** Galileo HAS (~40 cm, no internet) — out of project scope per primer [scope] (SSR/PPP-tier), mentioned for completeness only; GEODNET and Onocoy — RTK-tier, no confirmed TT coverage in public station maps.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **TTAGN RINEX data** — available via Surveys and Mapping Division | https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ | Unknown — contact surmaptt@gmail.com |
| **NOAA NGS CORS** (any shared TT stations in NCN) | https://geodesy.noaa.gov/CORS/ | Free |

## Sources Consulted
- Surveys and Mapping Division — Online Web Services: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ — HTTP 200 confirmed 2026-05-17; TTAGN + CMIS (surveys.gov.tt) + CMIS public map (surveys.gov.tt/publicmap) all listed; gpscors.gov.tt/gpscorstt referenced as access URL
- Surveys and Mapping Division — contact page: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/ — address, phone, email confirmed 2026-05-06
- TTAGN portal: http://www.gpscors.gov.tt/GPSCORSTT/default.aspx — ECONNREFUSED 2026-05-06; DNS NXDOMAIN 2026-05-13 (transient); DNS resolved 2026-05-17 (transient NXDOMAIN cleared; portal HTTP not re-probed)
- nslookup `gpscors.gov.tt` 2026-05-17 — A record returned
- Local data probe `py scripts/stations_by_radius.py 10.5 -61.3 200` — EarthScope CN57_RTCM3P3 confirmed 55 km from query point with [TTO] code 2026-05-13
- Spatial Dimension project page: https://www.spatialdimension.com/projects/trinidad-and-tobago-survey-and-mapping-division/ — CMIS/Landfolio only; no NTRIP detail
- Survey Trinidad and Tobago Ltd: https://www.surveytt.com/ — private surveying firm; no TTAGN/NTRIP detail
- Academia.edu — "A new geodetic infrastructure for Trinidad and Tobago" (2013; original 5-station TTAGN design): https://www.academia.edu/5286063/A_new_geodetic_infrastructure_for_Trinidad_and_Tobago
- RTK2go monitor (monitor.use-snip.com) — no TT stations 2026-05-13
- ArduSimple country search — no TT-specific page found
