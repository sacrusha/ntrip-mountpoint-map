# Trinidad and Tobago [TT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: National caster (TTAGN) listed by ministry; portal externally unreachable; one EarthScope NOTA station nearby as free fallback

| Field | Value |
|---|---|
| National NTRIP RTK caster | TTAGN — listed as active service by Ministry of Agriculture; portal externally unreachable (HTTP ECONNREFUSED 2026-05-22) |
| Operator | Surveys and Mapping Division, Ministry of Agriculture, Land and Fisheries |
| Network name | Trinidad and Tobago Active Geodetic Network (TTAGN) |
| landing_url | https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ (Surveys and Mapping Division operator page; lists TTAGN as an active service) |
| access_url | http://www.gpscors.gov.tt/gpscorstt (ministry-listed access URL — portal HTTP ECONNREFUSED 2026-05-22; DNS resolved 2026-05-17 + 2026-05-22 → consistent with ministry-internal-network access or sustained service outage). Contact `surmaptt@gmail.com` if portal unreachable. |
| host:port | not published; access URL is `http://www.gpscors.gov.tt/gpscorstt`. Service-routability for non-TT IPs unverified |
| num_stations | ? — 2013 academic paper documents a 5-station tender/design (2007); whether all five were built, are operational as of 2026, or have been expanded/reduced is not publicly verifiable. Operator pages do not enumerate stations. Confirm with `surmaptt@gmail.com` for current figure. |
| tariff | not published on any operator page (`agriculture.gov.tt` Online Web Services page lists TTAGN without pricing, 2026-05-22); contact Surveys and Mapping Division (`surmaptt@gmail.com`). Source: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ |
| vrs | ? — not stated on operator pages |
| hobbyist_eligibility | ? — service oriented to licensed land surveyors and engineers (Surveys and Mapping Division also acts as Land Survey Board registrar); hobbyist access policy not documented |
| legal_residency_required | ? — government network; no explicit residency rule stated |
| last_confirmed_alive | agriculture.gov.tt Online Web Services page HTTP 200 confirmed 2026-05-22 (TTAGN still listed as active service alongside CMIS/`surveys.gov.tt` and public map). DNS `gpscors.gov.tt` resolves (nslookup A record 2026-05-22); HTTP port responds ECONNREFUSED 2026-05-22. Service status: **listed-active / publicly-unreachable**. |
| datum_epoch | omitted — no citable operator declaration on agriculture.gov.tt; 2013 academic design paper referenced ITRF but operator portal silent |

## TTAGN background

Established as the Caribbean's first Active GPS Reference Network — original deployment 5 reference stations (2007) with Fujitsu and Trimble Navigation support. Designed for 24/365 GPS correction delivery via cellular, MSK radio beacon (planned 2007 follow-on), and internet. Per the 2013 academic paper, baseline-comparison accuracy to international reference frames was sub-cm. The Surveys and Mapping Division's contact: 118 Frederick Street, Port of Spain; +1 868-627-9201 ext. 237; `surmaptt@gmail.com`.

Portal-status timeline:
- 2026-05-06: `gpscors.gov.tt/GPSCORSTT/default.aspx` → ECONNREFUSED
- 2026-05-13: DNS for `gpscors.gov.tt` → NXDOMAIN (transient resolver issue)
- 2026-05-17: DNS resolves again
- 2026-05-22: DNS resolves (nslookup A record), HTTP ECONNREFUSED → portal not publicly reachable; ministry-only network access plausible. Ministry page still lists the URL as the access path.

CMIS (Cadastre Management Information System) at `surveys.gov.tt` and the public map at `surveys.gov.tt/publicmap` are listed alongside TTAGN on the Online Web Services page — unrelated to NTRIP/RTK.

## EarthScope NOTA free stream in TT territory

**EarthScope NOTA CN57_RTCM3P3** (10.84 N / 60.94 W, **Toco area, NE tip of Trinidad** — tagged TTO in `data/earthscope.sourcetable` line 146; location confirmed via EarthScope/COCONet station info). Reachable via `ntrip.earthscope.org:2101`. Free non-commercial under NULA, $1,000/seat/yr commercial, ITRF2014 / NOTA epoch 2026-03-30. Probed baselines 2026-05-22: ~66 km to Port of Spain, ~39 km to southern Tobago (Scarborough area), ~36 km to northern Grenada tip. All well outside cm-grade single-base range (~20–30 km dual-frequency), but the closest free public RTK source for NE Trinidad / southern Tobago coastal work. EarthScope NOTA detailed in its dedicated research file.

Confirmed 2026-05-22 via `py scripts/stations_by_radius.py 10.50 -61.30 250` → 2 EarthScope hits (CN57 + CN46 Carriacou GRD); zero non-EarthScope sources.

## Volunteer / commercial overlay (2026-05-22)

Zero TT mountpoints on rtk2go, Centipede, GEODNET, ONOCOY per local pipeline + WebSearch. Galileo HAS (~40 cm broadcast SSR) covers TT but is out-of-scope per project primer.

## Sources
- Surveys and Mapping Division — Online Web Services: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/online-web-services/ (WebFetch 2026-05-22 → HTTP 200; TTAGN listed with access URL `http://www.gpscors.gov.tt/gpscorstt`; no host:port / station list / tariff on page)
- Surveys and Mapping Division contact: https://agriculture.gov.tt/divisions-units/divisions/surveys-and-mapping/
- TTAGN portal: http://www.gpscors.gov.tt/gpscorstt — WebFetch 2026-05-22 → ECONNREFUSED; nslookup gpscors.gov.tt 2026-05-22 → A record returned
- Academia.edu — "A new geodetic infrastructure for Trinidad and Tobago" (2013, 5-station design): https://www.academia.edu/5286063/A_new_geodetic_infrastructure_for_Trinidad_and_Tobago
- EarthScope GNSS realtime (CN57 fallback): https://www.earthscope.org/data/gnss-realtime/ (ITRF2014, NOTA epoch 2026-03-30)
- Local pipeline 2026-05-22: `data/earthscope.sourcetable` line 146 (CN57 TTO); `stations_by_country.py TTO` returns CN57; `stations_by_radius.py 10.50 -61.30 250` → 2 EarthScope hits, zero others
