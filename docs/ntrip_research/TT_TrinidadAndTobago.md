# Trinidad and Tobago [TT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (refresh of 2026-05-06 entry)

## Status: TTAGN listed by ministry but external reachability is degraded; gpscors.gov.tt DNS no longer resolves from sandbox; CN57 EarthScope station offers a usable nearby alternative

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes per ministry listing (government-operated; 24/365 CORS; registration required) — but unreachable externally |
| **Operator** | Surveys and Mapping Division, Ministry of Agriculture, Land and Fisheries |
| **Network name** | Trinidad and Tobago Active Geodetic Network (TTAGN) |
| **host:port — TTAGN** | not published; ministry-listed access URL is `http://www.gpscors.gov.tt/gpscorstt` — DNS for `gpscors.gov.tt` failed to resolve from sandbox on 2026-05-13 (NXDOMAIN-equivalent: "Could not resolve host"). Whether the domain is offline globally or only blocked from non-TT resolvers is unclear. |
| **tariff** | not published publicly; contact Surveys and Mapping Division |
| **hobbyist_eligibility** | Unclear — TTAGN primarily serves professional land surveyors and engineers; hobbyist access policy not documented |
| **legal_residency_required** | Unclear — government network; no explicit residency requirement stated |
| **last_confirmed_alive** | agriculture.gov.tt Online Web Services page HTTP 200 confirmed 2026-05-13 (TTAGN still listed as an active service); `gpscors.gov.tt:2101` DNS resolution FAILED 2026-05-13 (unable to confirm caster alive). Ministry portal continues to advertise the service so it may simply be ministry-network-only. |

## Most Recent Project Announcement

TTAGN was established as the Caribbean's first Active GPS Reference Network, originally comprising five stations, built with support from Fujitsu and Trimble Navigation. The network provides 24/365 GPS corrections. The Surveys and Mapping Division's Online Web Services page at agriculture.gov.tt lists TTAGN as an active service offering GPS corrections, with the access URL given as http://www.gpscors.gov.tt/gpscorstt. No new announcement or expansion news was found as of 2026-05-06.

## Context Notes

- **TTAGN**: A 24/365 CORS network covering both Trinidad and Tobago islands. Original deployment: 5 reference stations (2007, per 2013 academic paper). Current station count not confirmed in any source found during this research; the government's Online Web Services page does not list individual stations. No expansion announcement found.
- **Portal status:** gpscors.gov.tt/GPSCORSTT/default.aspx returned ECONNREFUSED on 2026-05-06; on 2026-05-13 DNS resolution for `gpscors.gov.tt` itself failed entirely from sandbox ("Could not resolve host: gpscors.gov.tt"). The agriculture.gov.tt ministry page still references `http://www.gpscors.gov.tt/gpscorstt` (curl on agriculture.gov.tt confirmed 2026-05-13, TTAGN listed alongside CMIS at surveys.gov.tt and the CMIS public map at surveys.gov.tt/publicmap). It is not clear whether the NTRIP caster is publicly routable for any IP; ministry-only network access is plausible.
- **CMIS (Cadastre Management Information System) / surveys.gov.tt**: Listed alongside TTAGN as an Online Web Service. Public map at https://www.surveys.gov.tt/publicmap. Run by Surveys and Mapping Division but unrelated to NTRIP/RTK.
- **curl probe of `gpscors.gov.tt:2101`**: DNS FAILED on 2026-05-13. From the sandbox, neither IPv4 lookup nor connection completes.
- **Nearest viable RTK alternative within ~50 km**: `py scripts/stations_by_radius.py 10.5 -61.3 200` returns **CN57_RTCM3P3** (EarthScope, 10.84°N -60.94°W, ~55 km off Tobago's east coast) — this is the only confirmed externally-reachable NTRIP mountpoint serving Trinidad and Tobago territory. EarthScope COCONet station; account + NULA required.
- **Surveys and Mapping Division** contact: 118 Frederick Street, Port of Spain; phone 868-627-9201 ext. 237; email surmaptt@gmail.com.
- **Spatial Dimension** (UK GIS firm) supported the division's Cadastre Management Information System (CMIS / Landfolio); not related to NTRIP caster operations.
- The Surveys and Mapping Division also operates as the Land Survey Board registrar — suggesting NTRIP access may be limited to licensed land surveyors.
- **RTK2go / Centipede-RTK**: No Trinidad and Tobago base stations confirmed in public sourcetables on 2026-05-13.
- **EarthScope (NOTA)**: One Trinidad-region COCONet station available — **CN57_RTCM3P3** (10.84°N, -60.94°W, off the east coast between Trinidad and Tobago) — confirmed in local data 2026-05-13 with `[TTO]` country code. Free for non-commercial use with NULA.
- **Global commercial fallbacks:** Galileo HAS (~40 cm, no internet); GEODNET and Onocoy — no confirmed TT coverage in public station maps.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **TTAGN RINEX data** — available via Surveys and Mapping Division | https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ | Unknown — contact surmaptt@gmail.com |
| **NOAA NGS CORS** (any shared TT stations in NCN) | https://geodesy.noaa.gov/CORS/ | Free |

## Sources Consulted
- Surveys and Mapping Division — Online Web Services: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ — HTTP 200 confirmed 2026-05-13; TTAGN, CMIS (surveys.gov.tt), and CMIS public map (surveys.gov.tt/publicmap) all listed; gpscors.gov.tt/gpscorstt referenced as access URL
- Surveys and Mapping Division — contact page: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/ — address, phone, email confirmed 2026-05-06
- TTAGN portal: http://www.gpscors.gov.tt/GPSCORSTT/default.aspx — ECONNREFUSED 2026-05-06; DNS resolution FAILED 2026-05-13 (NXDOMAIN-equivalent from sandbox; portal may be ministry-network-internal)
- curl probe of `gpscors.gov.tt:2101` — DNS resolution failed 2026-05-13
- Local data probe via `py scripts/stations_by_radius.py 10.5 -61.3 200` — EarthScope CN57_RTCM3P3 confirmed 55 km from query point with [TTO] code 2026-05-13
- Spatial Dimension project page: https://www.spatialdimension.com/projects/trinidad-and-tobago-survey-and-mapping-division/ — CMIS/Landfolio only; no NTRIP detail
- Survey Trinidad and Tobago Ltd: https://www.surveytt.com/ — private surveying firm; no TTAGN/NTRIP detail
- Academia.edu — "A new geodetic infrastructure for Trinidad and Tobago" (2013; original 5-station TTAGN design): https://www.academia.edu/5286063/A_new_geodetic_infrastructure_for_Trinidad_and_Tobago
- RTK2go monitor (monitor.use-snip.com) — no TT stations 2026-05-13
- ArduSimple country search — no TT-specific page found
