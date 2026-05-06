# Trinidad and Tobago [TT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — government NTRIP caster (TTAGN) exists; portal reachable but NTRIP host:port not publicly documented

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government-operated; 24/365 CORS; registration required) |
| **Operator** | Surveys and Mapping Division, Ministry of Agriculture, Land and Fisheries |
| **Network name** | Trinidad and Tobago Active Geodetic Network (TTAGN) |
| **host:port — TTAGN** | not published; access portal at gpscors.gov.tt/gpscorstt; contact division for NTRIP credentials |
| **tariff** | not published publicly; contact Surveys and Mapping Division |
| **hobbyist_eligibility** | Unclear — TTAGN primarily serves professional land surveyors and engineers; hobbyist access policy not documented |
| **legal_residency_required** | Unclear — government network; no explicit residency requirement stated |
| **last_confirmed_alive** | agriculture.gov.tt Online Web Services page HTTP 200 confirmed 2026-05-06; gpscors.gov.tt/GPSCORSTT/default.aspx returned ECONNREFUSED on 2026-05-06 (portal may be firewall-restricted or moved) |

## Most Recent Project Announcement

TTAGN was established as the Caribbean's first Active GPS Reference Network, originally comprising five stations, built with support from Fujitsu and Trimble Navigation. The network provides 24/365 GPS corrections. The Surveys and Mapping Division's Online Web Services page at agriculture.gov.tt lists TTAGN as an active service offering GPS corrections, with the access URL given as http://www.gpscors.gov.tt/gpscorstt. No new announcement or expansion news was found as of 2026-05-06.

## Context Notes

- **TTAGN**: A 24/365 CORS network covering both Trinidad and Tobago islands. Original deployment: 5 reference stations (2007, per 2013 academic paper). Current station count not confirmed in any source found during this research; the government's Online Web Services page does not list individual stations. No expansion announcement found.
- **Portal status:** gpscors.gov.tt/GPSCORSTT/default.aspx returned ECONNREFUSED when fetched on 2026-05-06. The domain resolves but the port is either firewalled or the web portal has moved/is restricted. The agriculture.gov.tt ministry page lists the URL as http://www.gpscors.gov.tt/gpscorstt and confirms the service is offered. It is not clear whether the NTRIP caster itself (port 2101) is publicly routable; no external probe was successful.
- **curl probe of `gpscors.gov.tt:2101`**: not executable via shell tools in this session. WebFetch to gpscors.gov.tt returned ECONNREFUSED, indicating the web interface on the standard HTTP port is not openly reachable from outside T&T.
- **Surveys and Mapping Division** contact: 118 Frederick Street, Port of Spain; phone 868-627-9201 ext. 237; email surmaptt@gmail.com.
- **Spatial Dimension** (UK GIS firm) supported the division's Cadastre Management Information System (CMIS / Landfolio); not related to NTRIP caster operations.
- The Surveys and Mapping Division also operates as the Land Survey Board registrar — suggesting NTRIP access may be limited to licensed land surveyors.
- **RTK2go / Centipede-RTK**: No Trinidad and Tobago base stations confirmed in public sourcetables.
- **Global commercial fallbacks:** Galileo HAS (~40 cm, no internet); GEODNET and Onocoy — no confirmed TT coverage in public station maps.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **TTAGN RINEX data** — available via Surveys and Mapping Division | https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ | Unknown — contact surmaptt@gmail.com |
| **NOAA NGS CORS** (any shared TT stations in NCN) | https://geodesy.noaa.gov/CORS/ | Free |

## Sources Consulted
- Surveys and Mapping Division — Online Web Services: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ — HTTP 200, TTAGN listed, access URL gpscors.gov.tt/gpscorstt confirmed 2026-05-06
- Surveys and Mapping Division — contact page: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/ — address, phone, email confirmed 2026-05-06
- TTAGN portal: https://gpscors.gov.tt/GPSCORSTT/default.aspx — ECONNREFUSED 2026-05-06 (portal inaccessible from outside TT)
- curl probe of `gpscors.gov.tt:2101` — not executable: shell tools unavailable in this session
- Spatial Dimension project page: https://www.spatialdimension.com/projects/trinidad-and-tobago-survey-and-mapping-division/ — CMIS/Landfolio only; no NTRIP detail
- Survey Trinidad and Tobago Ltd: https://www.surveytt.com/ — private surveying firm; no TTAGN/NTRIP detail
- Academia.edu — "A new geodetic infrastructure for Trinidad and Tobago" (2013; original 5-station TTAGN design): https://www.academia.edu/5286063/A_new_geodetic_infrastructure_for_Trinidad_and_Tobago
- RTK2go monitor (monitor.use-snip.com) — no TT stations
- ArduSimple country search — no TT-specific page found
