# Jamaica [JM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior: 2026-05-17)

## Status

Two distinct NTRIP-relevant layers in Jamaica:

1. **NLA VRS network** (Trimble Pivot platform) — **live portal located at `http://vrs.nla.gov.jm/`** (Trimble Pivot Web). The portal is reachable from the public Internet and exposes Login + Register account pages; no public host:port for the NTRIP caster is published, no tariff is published, and the registration policy is not stated on the public pages. Per the 2012 mycoordinates.org cadastral-surveying article, the network was originally configured as 13 CORS in JAD2001, with "no indication of user fees to be charged by the National Land Agency of Jamaica to the users of the VRS". Operational status of the underlying Pivot platform in 2025-2026 is not independently verified — only the Trimble Pivot Web frontend is confirmed reachable.
2. **EarthScope NOTA (former COCONet)** scientific streams from CN10 (Morant Cay), CN11 (Pedro Cay / San Pedro Cay), CN12 (Kingston / UWI Mona). All on `ntrip.earthscope.org:2101`; raw RTCM 3.3 single-base, not VRS.

| Field | Value |
|---|---|
| National caster | NLA VRS (Trimble Pivot Web) — portal reachable; NTRIP host:port not published; access policy unknown |
| Scientific streams in JM territory | Yes — EarthScope NOTA `CN11`, `CN12` (CN10 historically) |
| hobbyist_eligibility | EarthScope: yes (noncommercial NULA). NLA VRS: unclear |
| legal_residency_required | EarthScope: no. NLA VRS: unclear |
| last_confirmed_alive | 2026-05-21 — EarthScope `ntrip.earthscope.org:2101` `SOURCETABLE 200 OK` (curl); EarthScope GNSS real-time page HTTP 200; pipeline `py scripts/stations_by_country.py JAM` returns CN11 + CN12. NLA Trimble Pivot Web at `http://vrs.nla.gov.jm/` reachable per WebFetch; Login + Register account paths present. |

## NLA VRS Network (Trimble Pivot, `vrs.nla.gov.jm`)

| Field | Value |
|---|---|
| operator | National Land Agency (NLA), Ministry of Local Government and Rural Development |
| landing_url | https://www.nla.gov.jm/content/surveys-and-mapping (NLA Surveys & Mapping — no GNSS-service sub-page on this URL) |
| access_url | http://vrs.nla.gov.jm/ (Trimble Pivot Web; `RegisterAccount.aspx` + `Login.aspx` present) |
| host:port | not published. Pivot Web frontend confirmed reachable; underlying NTRIP caster port not advertised. |
| num_stations | 13 CORS originally configured (mycoordinates.org 2012). Live count in the Pivot Sensor Map could not be retrieved (page rendered "0 sensors" via WebFetch — Pivot maps are JS-driven and not server-rendered; this does NOT confirm zero stations). No NLA annual report or subsequent Jamaica Survey Department publication has been located that updates this figure; the 13-station count is the most recent published figure but is now 14 years old. |
| vrs | Configured as VRS at deployment (Trimble Pivot, 2008-2012 build per mycoordinates.org). Whether the VRS service is currently active and serving rovers in 2026 is not independently confirmed — only the Pivot Web frontend (Login + Register pages) has been verified reachable. |
| tariff | not published on `vrs.nla.gov.jm` Login/Register pages; no current NLA fee schedule located. mycoordinates.org 2012 article stated "no indication of user fees to be charged by the National Land Agency of Jamaica" — but that is a 2012 source, not an operator declaration today. |
| hobbyist_eligibility | unclear — registration page is reached via `/TrimblePivotWeb/RegisterAccount.aspx`; sandbox observed transient maintenance page when fetched on 2026-05-21, so signup policy could not be read from the form. |
| legal_residency_required | unclear |
| datum_epoch | JAD2001 (mycoordinates.org 2012 source: "the system is configured to function in the JAD2001 datum"). Not currently confirmed by an NLA operator-side declaration; per [datum-epoch] citation rule, retain in History note, omit from operator-citable field. |

History: the network was commissioned under a 2008 contract awarded by the Ministry of Agriculture (Jamaica) to Spatial Innovision Ltd. (Trimble Caribbean business partner), built on Cable & Wireless Frame Relay / MPLS plus Cable & Wireless and Digicel GSM/GPRS. Source: https://www.spatialvision.com/ministry-of-agriculture-jamaica-signs-major-contract-with-spatial-innovision-to-deliver-the-national-gps-infrastructure/

## EarthScope NOTA — COCONet stations in JM territory

| Station | Location | In live sourcetable 2026-05-21 |
|---|---|---|
| CN10 | Morant Cay (~130 km SE of Kingston) | No — historically installed under COCONet and maintained by UNAVCO through at least 2013; absent from EarthScope pipeline snapshot 2026-05-21. No public EarthScope announcement of decommissioning has been located; treat real-time status as offline pending operator confirmation. |
| CN11 | Pedro Cay / San Pedro Cay (~130 km S of Kingston), 17.02, -77.78 | Yes (`CN11_RTCM3P3`) |
| CN12 | Kingston — UWI Mona campus, Physics Dept roof, 18.00, -76.75 | Yes (`CN12_RTCM3P3`) |

CN10 and CN11 are isolated cays 80+ miles offshore and outside practical single-base RTK range from any populated area on the main island. **CN12 in Kingston is the only EarthScope station relevant to hobbyist RTK on Jamaica.**

| Field | Value |
|---|---|
| host:port | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP). Confirmed live 2026-05-21 via curl (SOURCETABLE 200 OK). |
| num_stations (JM territory) | 2 in live snapshot (CN11 + CN12); 3 historically (incl. CN10) |
| vrs | No — single-base raw RTCM 3.3 MSM7 |
| Stream type | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 |
| Tariff — noncommercial | Free (USD $0.00) — account + annual NULA acceptance required. Source: https://www.earthscope.org/data/gnss-realtime/ |
| Tariff — commercial | USD $1,000 per seat per year (EarthScope 501(c)(3); no VAT). Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| datum_epoch | ITRF2014, epoch 2026-03-30 (operator declaration: https://www.earthscope.org/data/gnss-realtime/) |

Legacy platform: old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

## Volunteer / Global Coverage (2026-05-21)

- `py scripts/stations_by_country.py JAM` — 2 EarthScope stations (CN11, CN12). Zero rtk2go, igs_ip, centipede JAM nodes.
- GEODNET / ONOCOY: no Jamaica stations on public coverage maps.

## Other NLA-Associated GNSS Infrastructure (Post-Processing Only)

A separate 13-station scientific CORS network operated by the NLA in collaboration with UW-Madison (Prof. Chuck DeMets) for plate-motion research exists; data are post-processed, not streamed via NTRIP. Page: http://www.geology.wisc.edu/~chuck/Jamaica/ (HTTP 200 2026-05-21 — personal academic page, reachable.)

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| EarthScope GNSS Data Archive — COCONet CN11, CN12 (live) + CN10 (archival RINEX, real-time status uncertain) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); USD 1,000/seat/yr commercial |
| NLA / UW-Madison 13-station scientific CORS | http://www.geology.wisc.edu/~chuck/Jamaica/ | Free (research/scientific use) |

## Sources

- NLA VRS Trimble Pivot Web (confirmed live 2026-05-21): http://vrs.nla.gov.jm/ ; Sensor map: http://vrs.nla.gov.jm/TrimblePivotWeb/Map/SensorMap.aspx ; Login: http://vrs.nla.gov.jm/TrimblePivotWeb/Login.aspx ; Register: http://vrs.nla.gov.jm/TrimblePivotWeb/RegisterAccount.aspx
- NLA Surveys & Mapping page: https://www.nla.gov.jm/content/surveys-and-mapping
- Spatial Innovision Ltd. project pages: https://www.spatialvision.com/projects/ and https://www.spatialvision.com/ministry-of-agriculture-jamaica-signs-major-contract-with-spatial-innovision-to-deliver-the-national-gps-infrastructure/ (2008 contract)
- mycoordinates.org (2012-08), "The Jamaica VRS and Cadastral Surveying": https://mycoordinates.org/the-jamaica-vrs-and-cadastral-surveying/ — 13 CORS, JAD2001, "no indication of user fees"
- JAD2001 reference: https://epsg.io/3448 and https://www.jamaicancaves.org/jad2001.htm
- EarthScope GNSS real-time data: https://www.earthscope.org/data/gnss-realtime/ (HTTP 200, 2026-05-21; ITRF2014 + epoch 2026-03-30 declared in FAQ)
- EarthScope commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- EarthScope NULA PDF: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf
- EarthScope NTRIP sourcetable: `ntrip.earthscope.org:2101` (curl 2026-05-21, SOURCETABLE 200 OK)
- UNAVCO Jamaica upgrade: https://www.unavco.org/news/unavco-upgrades-coconet-cgps-sites-in-jamaica/
- UWI Earthquake Unit: https://www.mona.uwi.edu/earthquake/
- UW-Madison Jamaica GPS network: http://www.geology.wisc.edu/~chuck/Jamaica/
- `py scripts/stations_by_country.py JAM` (2026-05-21) → CN11 + CN12
