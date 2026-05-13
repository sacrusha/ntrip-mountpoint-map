# US Northeast — NTRIP RTK Caster Research
**Date researched:** 2026-05-07 (re-verified 2026-05-13: ACORN/UConn, VECTOR, MaineDOT RTN, KeyNetGPS all SOURCETABLE 200 OK; NYSNet's `rtn.dot.ny.gov:8080` confirmed alive — SOURCETABLE 200 OK with 18 STR entries including the public `net_msm_vrs`, `net_msm_imax`, and `near_msm` mountpoints — superseding the 2026-05-07 timeout result; standard NTRIP port 2101 on NYSNet remains firewalled; MaCORS remains unreachable from external probes; MaCORS station count corrected to 22 base stations)

**States covered:** Maine (ME), New Hampshire (NH), Vermont (VT), Massachusetts (MA), Rhode Island (RI), Connecticut (CT), New York (NY), New Jersey (NJ), Pennsylvania (PA), Delaware (DE), Maryland (MD), Washington DC (DC)

## Status: MIXED — five free state networks (ME, VT, MA, CT, NY); NH/RI/NJ/PA/DE/MD/DC have no free public state caster; EarthScope NOTA provides sparse single-base fallback region-wide

---

## Per-State Summary Table

| State | Free public caster | Network | host:port | VRS | Hobbyist | Probe result |
|---|---|---|---|---|---|---|
| ME | Yes (free) | MaineDOT RTN | `medotrtn.maine.gov:2101` | Yes | Likely yes | SOURCETABLE 200 OK — 2026-05-13 |
| NH | No | — | — | — | — | No state caster found |
| VT | Yes (free) | VECTOR | `vector.vermont.gov:2101` | Yes | Yes (no restriction stated) | SOURCETABLE 200 OK — 2026-05-13 (36 STR entries) |
| MA | Yes (free) | MaCORS | `macorsrtk.massdot.state.ma.us:2101` | Yes (iMAX) | Yes (no restriction stated) | Timeout from external IP (firewall); DNS resolves; state confirmed operational |
| RI | No | — | — | — | — | No state caster; MaCORS edge coverage |
| CT | Yes (free) | ACORN | `acorn.uconn.edu:2101` | Yes | Yes (public registration) | SOURCETABLE 200 OK — 2026-05-13 (48 STR entries) |
| NY | Yes (free) | NYSNet | `rtn.dot.ny.gov:8080` (NTRIP); `cors.dot.ny.gov:443` (portal) | Yes (iMAX/MAC + `net_msm_vrs`) | Likely yes | NTRIP port 8080: SOURCETABLE 200 OK — 2026-05-13 (18 STR); port 2101: timeout from external IP |
| NJ | No | — | — | — | — | No state caster found |
| PA | No | — | — | — | — | No state caster found |
| DE | No | — | — | — | — | No state caster found |
| MD | No | — | — | — | — | No state caster found |
| DC | No | — | — | — | — | No state caster found |

---

## EarthScope NOTA — Regional Baseline (all states)

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); also ports 2105 (BINEX), 2108 (position solutions) |
| **tariff** | Free (noncommercial license, annual renewal, no fee) · Commercial: USD 1,000/seat/yr |
| **VRS** | No — single-base physical station streams only |
| **hobbyist_eligibility** | Yes — noncommercial license explicitly allows individual use with no revenue from derived products |
| **legal_residency_required** | No — global open access |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` confirmed 2026-05-13 (curl probe; 1,080 STR entries globally) |
| **NE station count** | 2 stations within strict NE bbox (38–48°N, 66–82°W): `P776_RTCM3P3` (43.54°N, −71.38°W — central NH) and `P817_RTCM3P3` (40.15°N, −78.51°W — central PA). Station spacing ~200–400 km in this region — adequate for PPK/static, baseline distance may degrade real-time RTK |
| **format** | RTCM 3.3 (MSM4/5 full constellation: GPS+GLO+BDS+GAL+SBAS+QZS) |
| **registration** | EarthScope account required; self-service at earthscope.org/data/gnss-realtime/; noncommercial license accepted online; free trial: 2 weeks / 5 seats (one-time) |

**Context:** NOTA is a geodetic science network, not a surveying infrastructure network. NE station spacing is too wide for reliable real-time RTK in most scenarios; it is best used for PPK post-processing or as a fallback where no state network exists. New service launched 2024-05-01.

---

## ME — Maine: MaineDOT Real-Time Network

| Field | Value |
|---|---|
| **Network name** | Maine Real-Time Network (MaineDOT RTN) |
| **Operator** | Maine Department of Transportation (MaineDOT), Bureau of Project Development, Survey Section |
| **Software** | Trimble Pivot (migrated from legacy system; migration cutover October 1, 2025) |
| **host:port** | `medotrtn.maine.gov:2101` (IP 52.165.92.197) |
| **tariff** | Free |
| **VRS** | Yes — mountpoints: `VRS_CMR`, `VRS_RTCM`, `VRS_RTCM_23` |
| **hobbyist_eligibility** | Unclear — registration is self-service (select own Organization/Username/Password); no professional license field identified; no explicit restriction; contact rtnsupport.medot@maine.gov to confirm |
| **legal_residency_required** | Unclear — no stated requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-13 (curl probe of medotrtn.maine.gov:2101; 8 STR entries) |

**Context:** MaineDOT replaced the previous CORS system (mdotcors.maine.gov, which became unresponsive) with a Trimble Pivot-based system at medotrtn.maine.gov in 2025. Existing users were required to re-register after October 1, 2025 cutover. The legacy host mdotcors.maine.gov returns ECONNREFUSED as of 2026-05-07. Support: rtnsupport.medot@maine.gov.

---

## NH — New Hampshire: No Public State Caster

No state DOT or university RTK network found for New Hampshire as of 2026-05-07. NHDOT maintains CORS stations contributing to NOAA NCN for static post-processing only. Multiple sources (GPS World Dec 2024, E38 Survey Solutions, Point One Nav) confirm "no public service" in NH.

**Gap:** EarthScope NOTA has one station in NH (P776, central NH) as a single-base fallback. Commercial options: KeyNetGPS (vrs.keynetgps.com:2101, paid — see Multi-State section below) covers NH as part of its Northeast VRS network.

---

## VT — Vermont: VECTOR

| Field | Value |
|---|---|
| **Network name** | VECTOR — Vermont Enhanced CORS and Transmission Of Real-time Corrections |
| **Operator** | Vermont Agency of Transportation (VTrans), Geodetic Survey unit; CORS stations accredited with NOAA NCN |
| **Software** | Trimble Pivot |
| **host:port** | `vector.vermont.gov:2101` (IP 20.185.11.35) |
| **tariff** | Free |
| **VRS** | Yes — RTCM 3.1 and CMR+ single-base and network streams |
| **hobbyist_eligibility** | Yes — explicitly "a free service utilized by State and Federal Agencies, Surveyors, GIS users, Engineers, Scientists, and the public at large"; no professional license required |
| **legal_residency_required** | No — no stated restriction |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-13 (curl probe; 36 STR entries) |
| **station count** | 18 reference stations statewide (live sourcetable on 2026-05-13 declares 36 STR mountpoints — physical, single-base, and VRS combinations); all except VJSC and VTWR accredited with NOAA NCN |

**Context:** Registration is self-service at vector.vermont.gov (email link: vtrans.vermont.gov/highway/geodetic). Equipment upgrades from NetR9 to current-generation receivers were completed in 2025.

---

## MA — Massachusetts: MaCORS

| Field | Value |
|---|---|
| **Network name** | MaCORS — Massachusetts Continuously Operating Reference Station Network |
| **Operator** | MassDOT (Massachusetts Department of Transportation) |
| **Software** | Leica SpiderNet (Spider Business Center) |
| **host:port** | `macorsrtk.massdot.state.ma.us:2101` (IP 193.8.43.161) |
| **tariff** | Free — "MassDOT does not currently charge a fee for network access" |
| **VRS** | Yes — iMAX network mount points (multi-base network correction); recommended mountpoint: `RTCM3MSM_IMAX` (full constellation GPS+GLO+BDS+GAL) |
| **hobbyist_eligibility** | Yes — "MassDOT is now granting public access"; no professional license field in registration; no stated restriction |
| **legal_residency_required** | No — no stated restriction |
| **last_confirmed_alive** | DNS resolves to 193.8.43.161; port 2101 times out from external IP (firewall or IP allowlist likely required) — confirmed again 2026-05-13; MassDOT portal (macors.massdot.state.ma.us) HTTP 200 as of 2026-05-07. Service confirmed operational by multiple user reports and current Mass.gov MaCORS page |
| **station count** | 22 GNSS base stations approximately 50 km apart (current Mass.gov 2026 listing). Older sources reference 18 stations; the 22-station count is the current figure. |
| **formats** | RTCM 2.3, RTCM 3.1, CMR, CMR+, RTCM 3.2 MSM4 |
| **coverage** | Massachusetts + edge coverage into Rhode Island, southern NH, and CT |

**Context:** Registration at macors.massdot.state.ma.us. Port 2101 blocked from external IPs in CI probes; this is consistent with the Leica SpiderNet SBC requiring a registered account session. Users report successful connections from within the US. MaCORS also provides Rhode Island partial coverage (see RI section).

---

## RI — Rhode Island: No Dedicated State Caster

Rhode Island has no state-operated RTK NTRIP caster. The state relies on MaCORS (Massachusetts) for edge VRS coverage via the ACORN (Connecticut) and MaCORS station on Rhode Island (ACORN has one sensor in Providence area; MaCORS southernmost stations reach into RI).

**Gap:** Coverage is technically possible near Providence via ACORN (CT) and MaCORS (MA) but is not a designated RI service, and baseline distances may be marginal (~50–80 km from nearest reference stations). Commercial fallback: KeyNetGPS (see multi-state section).

---

## CT — Connecticut: ACORN

| Field | Value |
|---|---|
| **Network name** | ACORN — Advanced Continuously Operating Reference Network |
| **Operator** | Connecticut Department of Transportation (CTDOT) + University of Connecticut (UConn) Department of Natural Resources and the Environment (DNRE) |
| **Software** | Trimble Pivot |
| **host:port** | `acorn.uconn.edu:2101` (IPs: 137.99.150.112, 137.99.150.56) |
| **tariff** | Free — "ACORN is free and available to the public" |
| **VRS** | Yes — primary mountpoint: `VRS3_RTX` (multi-constellation); Trimble equipment: `VRSX_RTX` |
| **hobbyist_eligibility** | Yes — explicitly "free and available to the public"; registration at acorn.uconn.edu; no professional license required |
| **legal_residency_required** | No |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-13 (curl probe; 48 STR entries) |
| **station count** | 13 sensors total: 9 in Connecticut, 1 in Rhode Island (Providence), 2 in southern Massachusetts, 1 on Long Island NY |
| **constellations** | GPS, GLONASS, Galileo (EU), BeiDou (CN) — Galileo and BeiDou added as of mid-2025 |

**Context:** Sustained state budget funding established after extensive testing and validation. CTDOT operates the reference receivers; UConn NRE operates the servers. Useful for RI, southern MA, and Long Island NY users near CT stations.

---

## NY — New York: NYSNet

| Field | Value |
|---|---|
| **Network name** | NYSNet — New York Spatial Reference Network (CORS + RTN) |
| **Operator** | New York State Department of Transportation (NYSDOT), Engineering Division + NYC partners |
| **Software** | Leica SpiderNet (`GNSS Spider 7.10.1.168/1.0` per 2026-05-13 sourcetable header) |
| **host:port (RTN)** | `rtn.dot.ny.gov:8080` — confirmed SOURCETABLE 200 OK on 2026-05-13 (curl probe). Full port/mountpoint list at cors.dot.ny.gov/SBC → RTN Ports/Mount Points. Port 2101 timed out from external IP (firewalled). |
| **host:port (SBC portal)** | `cors.dot.ny.gov` (HTTP 200 portal; NTRIP on :2101 timed out from external IP, consistent with account-gated access) |
| **tariff** | Free — "NYSDOT does not charge users a fee for access to the real-time network" |
| **VRS** | Yes — `net_msm_vrs` (RTCM 3 MSM, GPS+GLO+GAL+BDS, network VRS) is in the live sourcetable. Also iMAX (`net_msm_imax`, `GG_MSM_IMAX`, etc.) for Leica MAC users, and `near_msm` (nearest site, MSM full constellation). Full mountpoint list on 2026-05-13 includes: `NetCell_MAX_RTCMv3`, `NetCell_iMAX_RTCMv3`, `NearSite_GIS_RTCM12`, `NearSite_CMR+`, `NetCell_iMAX_CMRP`, `NetCell_iMAX_CMR`, `NearSite_CMR`, `NearSite_RTCMv3`, `GG_RTCM3_MAX`, `GG_RTCM3_IMAX`, `GG_CMRP_IMAX`, `GG_MSM_IMAX`, `near_msm`, `GG_RTCM3_MAX_1017`, `net_msm_imax`, `test`, `net_msm_vrs`, `NYAB_GIS_RTCM12`. |
| **hobbyist_eligibility** | Likely yes — registration is open (email + self-service); no professional license field identified in public FAQ; no explicit restriction stated |
| **legal_residency_required** | Unclear — no stated restriction |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-13 (curl probe of `rtn.dot.ny.gov:8080`; 18 STR entries returned). DNS resolves (161.11.223.1 for rtn.dot.ny.gov; 161.11.223.14 for cors.dot.ny.gov); portal HTTP 200. NYSDOT social account (@nysnet) active. 2024 NYSAPLS conference presentation confirms ongoing operations and planned densification. |
| **constellations** | GPS, GLONASS, Galileo, BeiDou (live sourcetable advertises `GPS+GLO+GAL+BDS` on the MSM mountpoints; legacy mountpoints `NetCell_MAX_RTCMv3`, `NetCell_iMAX_*` are GPS-only or GPS+GLO) |
| **datum** | NAD83(2011) epoch 2010.0 MYCS2 |

**Context:** Free registration at cors.dot.ny.gov; credentials emailed after activation. 2024 conference update (NYSAPLS Jan 2024) indicated planned full station rebuilds (cabling, receivers, choke-ring antennas) and possible densification by 10+ CORS. Network RTK products require NRE or professional use — no explicit restriction against hobbyists found. 2026-05-13 sourcetable confirms `near_msm`, `net_msm_vrs`, and `net_msm_imax` are the recommended multi-constellation mountpoints for non-Leica rovers (Emlid, Ardusimple, DJI RTK).

---

## NJ — New Jersey: No Public State Caster

No state DOT or university RTK network found for New Jersey as of 2026-05-07. Multiple sources confirm "RTK Premium covers the entire state" as the primary option, implying no free public infrastructure. No NJDOT, Rutgers, or Princeton CORS caster found.

**Gap:** NJ falls between NYSNet (NY, which may have some coverage in northern NJ near NYC) and EarthScope NOTA (no NJ station). Commercial options: KeyNetGPS (covers NJ) and AlphaRTK (covers NJ area — see multi-state section).

---

## PA — Pennsylvania: No Public State Caster

No active PennDOT-operated CORS RTK NTRIP caster found as of 2026-05-07. A 2011 PennDOT/NGS presentation (Harpster) described PACS (Pennsylvania CORS System) and VRS plans, but no live public endpoint has been confirmed. Multiple 2024 sources list PA as having no public RTK service. Penn State (PSU) maintains some CORS for research but no public RTK caster.

**Gap:** Commercial options: KeyNetGPS (vrs.keynetgps.com:2101, covers PA — SOURCETABLE 200 OK confirmed 2026-05-07; paid subscription) and AlphaRTK (covers PA; USD 195/mo; see multi-state section). EarthScope NOTA has one PA station (P817, Altoona area) for single-base/PPK use.

---

## DE — Delaware: No Public State Caster

No state-operated RTK NTRIP caster found for Delaware as of 2026-05-07. DelDOT does not appear to operate a public CORS network. Multiple sources confirm no public service for Delaware.

**Gap:** Commercial options: KeyNetGPS (covers DE), AlphaRTK (covers DE). State is small enough that nearby NJ, MD, and PA commercial networks provide viable baseline distances.

---

## MD — Maryland: No Public State Caster

No free public state-operated RTK NTRIP caster found for Maryland as of 2026-05-07. MDOT SHA (State Highway Administration) maintains geodetic control monuments and HARN points for static post-processing but does not operate a public real-time RTK caster. Multiple 2024 sources list MD as having "no public service" (GPS World) or covered only by RTK Premium (commercial). Note: mdotcors.org resolves to ECONNREFUSED — this is Michigan DOT CORS (MDOT CORS = Michigan), not Maryland.

**Contact:** MDOT SHA Survey Division: Erik Donald, 410-545-8976, edonald@mdot.maryland.gov.

**Gap:** Commercial options: KeyNetGPS (covers MD/DC), AlphaRTK (covers MD/DC; USD 195/mo). EarthScope NOTA has no station in MD.

---

## DC — Washington DC: No Public Caster

Washington DC has no dedicated public RTK NTRIP caster. DC is covered by the same commercial networks serving MD and VA (KeyNetGPS, AlphaRTK). EarthScope NOTA has no DC station. NGS operates CORS stations in the DC area contributing to NOAA NCN for static post-processing only.

---

## Multi-State Commercial Networks

### KeyNetGPS (Keystone Precision Solutions / Keypre)

| Field | Value |
|---|---|
| **Coverage** | VA, DC, MD, DE, PA, NJ, NY, CT, RI, MA, VT, NH, ME (entire Northeast) |
| **host:port** | `vrs.keynetgps.com:2101` (IP 209.255.196.164) |
| **tariff** | Not publicly listed; contact via keypre.com or resellers (Laser Industries 412-510-3089, Duncan-Parnell 833-916-0557) |
| **VRS** | Yes — Trimble VRS3Net software; mountpoints `VRS_CMRp`, `VRS_CMRx`, `SingleBase_CMRp`, `SingleBase_RTCM3` (6 STR entries live 2026-05-13) |
| **hobbyist_eligibility** | Unclear — no explicit restriction; subscriber agreement required |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-13 (curl probe; 6 STR entries) |

Primary paid option for PA, NJ, DE, NH, RI, and parts of NY/MD/DC without free coverage.

### AlphaRTK

| Field | Value |
|---|---|
| **Coverage** | DE, MD, NJ, PA, DC |
| **host:port** | Not published publicly; contact info@alphartk.com |
| **tariff** | USD 195/1 month · USD 995/6 months · USD 1,595/24 months (observed 2026-05-07, alphartk.com); free 1-week trial available |
| **VRS** | Unknown |
| **hobbyist_eligibility** | Unclear — professional orientation but no stated restriction; trial available |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | alphartk.com HTTP 200 as of 2026-05-07 |

---

## Post-Processing Fallback

| Service | Coverage | Cost |
|---|---|---|
| **NOAA NCN CORS** — static RINEX download (multiple stations per NE state) | All NE states | Free; no account required for data download |
| **EarthScope NOTA RINEX archive** | 2 NE stations (P776 NH, P817 PA) | Free noncommercial; account required |

---

## Sources Consulted

- NYSNet FAQ: https://cors.dot.ny.gov/FAQ.htm (observed 2026-05-07)
- NYSNet welcome: https://cors.dot.ny.gov/NYSNet%20welcome_0.htm
- NYSAPLS 2024 conference handout (CORS/RTN update): https://cdn.ymaws.com/www.nysapls.org/resource/resmgr/2024_conference/course_handouts/2024_nysapls_nysdot_cors-rtn.pdf
- MaCORS portal: https://macors.massdot.state.ma.us/ (observed 2026-05-07)
- MaCORS Mass.gov page: https://www.mass.gov/how-to/the-massachusetts-continuously-operating-reference-station-network-macors
- MALSCE MaCORS announcement: https://www.malsce.org/news/massdots-gps-network-now-available-for-use/
- Maine DOT Survey page: https://www.maine.gov/dot/doing-business/permitting-policy/survey-and-right-of-way-information
- Maine RTN portal: https://medotrtn.maine.gov/ (SOURCETABLE 200 OK confirmed 2026-05-07)
- Vermont VECTOR portal: https://vector.vermont.gov/ (SOURCETABLE 200 OK confirmed 2026-05-07)
- VTrans VECTOR real-time page: https://vtrans.vermont.gov/highway/geodetic/cors/real-time
- ACORN welcome: http://acorn.uconn.edu/ (SOURCETABLE 200 OK confirmed 2026-05-07)
- ACORN / UConn Today article: https://today.uconn.edu/2022/05/acorn-helps-connecticut-use-gps-faster-and-more-accurately/
- CT Surveyors ACORN article: https://ctsurveyors.org/acorn-real-time-positioning-for-connecticut/
- EarthScope GNSS Realtime: https://www.earthscope.org/data/gnss-realtime/ (observed 2026-05-07)
- EarthScope NOTA licensing announcement: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- EarthScope SOURCETABLE probe: ntrip.earthscope.org:2101 — SOURCETABLE 200 OK confirmed 2026-05-07; NE stations filtered by lat/lon
- E38 Survey Solutions state-by-state NTRIP: https://e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state
- E38 MaCORS Emlid guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-massachusetts-ntrip-macors
- E38 NYSNet Emlid guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-new-york-ntrip-nysnet
- ArduSimple USA NTRIP: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- KeyNetGPS portal: https://vrs.keynetgps.com/ (SOURCETABLE 200 OK confirmed 2026-05-07)
- KeyNetGPS product (Duncan-Parnell): https://www.duncan-parnell.com/itemdetail/W-KEYNETGPS
- Keypre about KeyNetGPS: https://www.keypre.com/keynetgps/about-keynet-gps/
- AlphaRTK: https://www.alphartk.com/ (observed 2026-05-07)
- MDOT SHA geodetic: https://roads.maryland.gov/mdotsha/pages/Index.aspx?PageId=61
- Maine Technical MaCORS server migration: https://www.mainetechnical.com/macors-new-server-location
- GPS World public RTK list: https://www.gpsworld.com/finally-a-list-of-public-rtk-base-stations-in-the-u-s/
- NTRIP-list North America: https://ntrip-list.com/north-america/
- Point One Nav NH: https://pointonenav.com/states/new-hampshire/
- Point One Nav PA: https://pointonenav.com/states/pennsylvania/
- PointMan public VRS list: https://pointman.com/list-of-public-vrs-correction-services-that-will-work-with-pointman/
- curl probes performed 2026-05-07 and re-verified 2026-05-13: medotrtn.maine.gov:2101 (OK, 8 STR), vector.vermont.gov:2101 (OK, 36 STR), acorn.uconn.edu:2101 (OK, 48 STR), ntrip.earthscope.org:2101 (OK, 1080 STR), vrs.keynetgps.com:2101 (OK, 6 STR), rtn.dot.ny.gov:8080 (OK, 18 STR — new confirmation 2026-05-13; supersedes earlier "timeout" entry for NYSNet which only reflected port 2101), macorsrtk.massdot.state.ma.us:2101 (timeout/firewall), rtn.dot.ny.gov:2101 (timeout), cors.dot.ny.gov:2101 (timeout)
