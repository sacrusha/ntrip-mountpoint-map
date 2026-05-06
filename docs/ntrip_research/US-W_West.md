# US West & Southwest — NTRIP RTK Caster Research
**Date researched:** 2026-05-07

**States covered:** Texas (TX), Oklahoma (OK), Arkansas (AR), Louisiana (LA), New Mexico (NM), Arizona (AZ), Colorado (CO), Utah (UT), Nevada (NV), Wyoming (WY), Montana (MT), Idaho (ID), California (CA), Oregon (OR), Washington (WA), Hawaii (HI)

## Status: MIXED — free public casters: AR (ARDOT), AZ (AZCORS), CO (Mesa County RTVRN), OR (ORGN); paid subscription casters: LA (C4Gnet), UT/NV (TURN GPS), MT (MTSRN), WA (WSRN); TX restricted to DOT employees; OK, NM, ID, HI have no state caster; CA (CRTN) has a one-time fee model; EarthScope NOTA provides sparse single-base fallback region-wide

---

## Per-State Summary Table

| State | Free public caster | Network | host:port | VRS | Hobbyist | Probe result |
|---|---|---|---|---|---|---|
| TX | No (DOT-restricted) | TxDOT RTN | `txrtn.txdot.gov` (port not public) | Yes | No — employees/contractors only | Portal HTTP 200; NTRIP port not published |
| OK | No | — | — | — | — | No state caster found |
| AR | Yes (free) | ARDOT RTN | `gps.ardot.gov:2101` | Yes | Likely yes | SOURCETABLE 200 OK — 2026-05-07 |
| LA | Paid | C4Gnet (LSU C4G) | `c4gnet.xyz:9000` | Yes | Unclear | DNS resolves; service confirmed operational |
| NM | No | — | — | — | — | No state caster found |
| AZ | Yes (free) | AZCORS | `azcors.azwater.gov` (port via SBC) | Yes | Yes | DNS resolves; Leica SBC portal active — 2026-05-07 |
| CO | Yes (free) | Mesa County RTVRN | `rtvrn.mesacounty.us:2101` | Yes | Likely yes | SOURCETABLE 200 OK — 2026-05-07 |
| UT | Paid | TURN GPS | `165.239.144.5:2101` | Yes | Unclear | Timeout from external IP (account-gated) |
| NV | Paid | Nevada GPS Network (via TURN) | `168.179.231.11:2102` | Yes | Unclear | Shared TURN GPS subscription |
| WY | No | — | — | — | — | No state caster; TURN GPS partial edge coverage |
| MT | Paid | MTSRN | `mtsrn.org:2101` | Yes | Unclear | SOURCETABLE 200 OK — 2026-05-07 |
| ID | No | — | — | — | — | No state caster; TURN GPS edge coverage |
| CA | Fee (one-time) | CRTN (SOPAC/UCSD) | `132.239.152.4:2102–2105` | No | Unclear | SOURCETABLE 200 OK on 2102 and 2104 — 2026-05-07 |
| OR | Yes (free) | ORGN (ODOT) | `orgn.odot.state.or.us:9881` | Yes | Likely yes | SOURCETABLE 200 OK — 2026-05-07 |
| WA | Paid | WSRN | `wsrn.org:2011` / `wsrn.org:2022` | Yes | Unclear | SOURCETABLE 200 OK on both ports — 2026-05-07 |
| HI | No | — | — | — | — | No state caster found |

**Regional baseline (all states):** EarthScope NOTA — `ntrip.earthscope.org:2101` — free non-commercial, single-base streams only.

---

## EarthScope NOTA — Regional Baseline (all states)

| Field | Value |
|---|---|
| **Network** | Network of the Americas (NOTA) — EarthScope Consortium (formerly UNAVCO) |
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); also ports 2105 (BINEX), 2108 (position solutions) |
| **tariff** | Free (noncommercial license, annual self-service renewal); USD 1,000/seat/yr commercial |
| **VRS** | No — individual physical station streams only |
| **hobbyist_eligibility** | Yes — noncommercial license explicitly available; self-service at earthscope.org/user/licenses |
| **legal_residency_required** | No — global open access |
| **last_confirmed_alive** | SOURCETABLE 200 OK confirmed by the Northeast and Southeast research probes 2026-05-07; stable infrastructure |
| **notes** | NOTA has dense coverage in western seismically active regions (Pacific Coast, Basin and Range, Rocky Mountains). Station spacing is variable — compact along active fault zones (CA, OR, WA, NV, UT), sparse in plains states (OK, TX panhandle, WY interior). Adequate for PPK/static; may be marginal for real-time RTK. Old hostname `rtgpsout.earthscope.org` retired July 2025. |

---

## TX — Texas: TxDOT RTN (Restricted Access)

| Field | Value |
|---|---|
| **Network name** | TxDOT Real Time Network (TxDOT RTN) |
| **Operator** | Texas Department of Transportation (TxDOT) — Information Systems Division |
| **host:port** | `txrtn.txdot.gov` — port not publicly documented; portal HTTP 200; NTRIP endpoint is not disclosed to the public |
| **tariff** | No charge — access is restricted, not sold |
| **VRS** | Yes — network VRS; 256 CORS stations statewide |
| **hobbyist_eligibility** | No — access is explicitly restricted to TxDOT employees and TxDOT contractors/consultants on TxDOT-funded projects |
| **legal_residency_required** | N/A (restricted network) |
| **last_confirmed_alive** | txrtn.txdot.gov portal HTTP 200 — 2026-05-07; sensor map accessible at txrtn.txdot.gov/Map/SensorMap.aspx |

### Context Notes

- TxDOT built one of the largest state-run CORS networks in the country (256 stations across all 254 counties) but has not opened it to public use. Multiple community sources (RPLS forum, Emlid community) confirm public access is not available.
- No registration pathway exists for non-TxDOT users.
- Practical fallback: EarthScope NOTA (free, sparse), commercial networks (RTKdata, Point One, SmartNet).
- GPS World's 2024 state-by-state public RTK list does not list Texas as having a public service.

---

## OK — Oklahoma: No Public State Caster

No state DOT or university RTK NTRIP caster found for Oklahoma as of 2026-05-07. ODOT (Oklahoma Department of Transportation) does not appear to operate a public CORS RTK network. Multiple sources (E38 Survey Solutions, Point One Nav) confirm "no public service" for Oklahoma.

**Gap:** Commercial options are the primary recourse: SmartNet Oklahoma (Leica; covers Oklahoma City and Tulsa markets), RTKdata (USD 40/mo, statewide coverage claimed), Point One Polaris. EarthScope NOTA provides sparse single-base fallback.

---

## AR — Arkansas: ARDOT RTN

| Field | Value |
|---|---|
| **Network name** | Arkansas Continuously Operating Reference Station Network / ARDOT Real Time Network (ARDOT RTN) |
| **Operator** | Arkansas Department of Transportation (ARDOT) — Surveys Division; Trimble Pivot platform |
| **host:port** | `gps.ardot.gov:2101` (IP 199.48.3.12) |
| **tariff** | Free |
| **VRS** | Yes — Trimble Pivot VRS; mountpoints include `ARDOT_RTX_CMRp`, `ARDOT_RTX_CMRx` (network solutions); `MS_CMRp`, `MS_CMRx` (nearest single base) |
| **hobbyist_eligibility** | Likely yes — registration is self-service via portal; no professional license field identified; ARDOT does not explicitly restrict hobbyist access |
| **legal_residency_required** | Unclear — no stated residency requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe of gps.ardot.gov:2101) |

### Context Notes

- ARDOT and its partners maintain GNSS CORS stations aligned with the NGS National Spatial Reference System.
- Registration: gps.ardot.gov (Trimble Pivot portal; login page at gps.ardot.gov/Login.aspx).
- Sensor map: gps.ardot.gov/Map/SensorMap.aspx
- Configuration guide for Trimble receivers: gps.ardot.gov/Configuring%20Trimble%20Receiver%20on%20ARDOT%20RTN.pdf
- **PAGIS (Pulaski Area GIS)** — supplementary single-base station in North Little Rock / Little Rock / Pulaski County AR; free; requires signed user agreement; NTRIP address provided post-registration; contact pagis.org 501.377.1264. Single station, not a VRS network; recommended within ~300 km / 185 miles.

---

## LA — Louisiana: C4Gnet (LSU Center for GeoInformatics)

| Field | Value |
|---|---|
| **Network name** | C4Gnet — Louisiana Statewide Real Time Network |
| **Operator** | LSU Center for GeoInformatics (C4G), Louisiana State University |
| **Software** | Leica GNSS Spider |
| **host:port** | `c4gnet.xyz:9000` |
| **tariff** | Paid — 1-year unlimited RTK (NTRIP only): USD 3,500; 50-hour RTK: USD 1,995/yr; 10-hour RTK: USD 495/yr; GIS DGPS unlimited: USD 995/yr; Full RTN membership: USD 5,000/yr. Source: store.c4g.lsu.edu, observed 2026-05-07 |
| **VRS** | Yes — VRS, PPP, and Nearest Single Base (NSB) products |
| **hobbyist_eligibility** | Unclear — no explicit restriction; professional surveying context implied; entry-level 10-hour tier at USD 495/yr is accessible |
| **legal_residency_required** | Unclear — no stated residency requirement; LSU-operated, US-accessible |
| **last_confirmed_alive** | c4gnet.xyz website HTTP 200 — 2026-05-07; mountpoints page at c4gnet.xyz/NTRIP_Mountpoints.aspx documents VRS, PPP, and NSB solutions |

### Context Notes

- Network established 2007, the year Louisiana launched its statewide CORS infrastructure.
- Mountpoint naming convention: `TYPE_SATS_FORMAT_REFERENCEFRAME` (e.g., `VRS_GREC_RTCM3_2_NAD83` for full constellation VRS in RTCM 3.2).
- Constellations: GREC (GPS + GLONASS + Galileo + BeiDou).
- Reference frame: NAD83 (2011) and ITRF2014 products available.
- Subscriptions purchased at store.c4g.lsu.edu.
- Free post-processing (RINEX download) is available separately — annual free subscription; contact rosbor1@lsu.edu or vdubinin@lsu.edu.

---

## NM — New Mexico: No Public State Caster

No state-operated RTK NTRIP caster found for New Mexico as of 2026-05-07. NMDOT does not appear to operate a public CORS RTK network. Multiple sources (GPS World, E38 Survey Solutions, Point One Nav) do not list New Mexico as having a public service.

**Gap:** Commercial options: RTKdata (USD 40/mo, claims statewide NM coverage), Point One Polaris, RTK Premium. EarthScope NOTA has stations in NM (instrument density is moderate along the Rio Grande Rift); useful for PPK. No university RTK network identified.

---

## AZ — Arizona: AZCORS

| Field | Value |
|---|---|
| **Network name** | Arizona CORS Network (AZCORS) |
| **Operator** | Arizona Department of Water Resources (ADWR) — Leica Spider Business Center (SBC) platform |
| **host:port** | `azcors.azwater.gov` — NTRIP caster port is assigned post-registration via Leica SBC portal; standard SBC port 2101 is not directly confirmed by external probe (site is behind Cloudflare CDN); SBC portal at azcors.azwater.gov/sbc |
| **tariff** | Free — "free access to all Real Time and RINEX Data Products in the AZCORS network" (ADWR, observed 2026-05-07) |
| **VRS** | Yes — Leica SBC supports iMAX/MAX network solutions; mountpoint list distributed post-registration |
| **hobbyist_eligibility** | Yes — registration is open to any user at azcors.azwater.gov/sbc/Account/Register; no professional license required |
| **legal_residency_required** | No — no stated residency requirement |
| **last_confirmed_alive** | azcors.azwater.gov/sbc portal HTTP 200 — 2026-05-07; ADWR AZCORS page active with April 2026 update (AZCORS_InformationAndMountpoints20260406.pdf available on azwater.gov) |
| **station count** | 56 ADWR-managed + 15 EarthScope/NPS CORS sites = 71 total CORS sites in network as of 2026-04-06 |

### Context Notes

- ADWR operates two virtual servers for network redundancy.
- Information and mountpoints document updated April 6, 2026: azwater.gov/sites/default/files/2026-04/AZCORS_InformationAndMountpoints20260406.pdf
- Also listed on Arizona geospatial hub: azgeo-data-hub-agic.hub.arcgis.com/pages/azcors
- AZCORS incorporates EarthScope and National Park Service stations, giving broad statewide coverage including remote desert and canyon country.
- Commercial alternative: AZGPS (azgps.net) — paid VRS network also covering AZ.

---

## CO — Colorado: Mesa County RTVRN

| Field | Value |
|---|---|
| **Network name** | Real-Time Virtual Reference Network (RTVRN) |
| **Operator** | Mesa County, Colorado — Public Works Department, GPS Survey |
| **Software** | Trimble Pivot |
| **host:port** | `rtvrn.mesacounty.us:2101` (IP 35.131.54.14) |
| **tariff** | Free — "a free service to the public" (Mesa County, observed 2026-05-07) |
| **VRS** | Yes — six VRS mountpoints: `VRS_CMR`, `VRS_CMRx`, `VRS_RTCMv3`, `VRS_CMR_RTX`, `VRS_CMRx_RTX`, `VRS_RTCMv3_RTX` |
| **hobbyist_eligibility** | Likely yes — public service with no stated restrictions; serves "surveying, construction, agriculture, mapping, and science industries" |
| **legal_residency_required** | No — no stated restriction |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe of rtvrn.mesacounty.us:2101) |
| **station count** | 33 base stations; 17 are NGS CORS stations |
| **datum** | NAD83 (2011) |

### Context Notes

- Registration at rtvrn.mesacounty.us (account subscription required; self-service).
- Coverage is centered on western Colorado (Grand Junction / Mesa County area) but 33-station network provides useful coverage across western Colorado and into adjacent Utah and Wyoming.
- This is the only confirmed free public VRS network in Colorado; CDOT does not operate a public RTK caster.
- Contact: Mesa County Public Works, GPS Survey section.

---

## UT — Utah: TURN GPS

| Field | Value |
|---|---|
| **Network name** | Utah Reference Network (TURN GPS) |
| **Operator** | Utah Geospatial Resource Center (UGRC) — State of Utah; Trimble Pivot VRS platform |
| **host:port** | `165.239.144.5:2101` (NAD83/2011); also `165.239.144.7:2101` (NAD83/2011 alternate) |
| **tariff** | Paid — USD 600/year per login (includes access to both TURN and Nevada GPS networks); payment via turngps-billpay.ugrc.utah.gov |
| **VRS** | Yes — Trimble Pivot VRS; recommended mountpoint: `GNSS-VRS-NAD83-RTCM32` (full GNSS multi-constellation); also `VRS-NAD83` variants in CMRp, CMRx, RTCM31, RTCM32 |
| **hobbyist_eligibility** | Unclear — subscription requires Utah ID account; no professional license stated as required; subscription open to any individual |
| **legal_residency_required** | Unclear — Utah ID required for subscription billing; no explicit residency restriction stated |
| **last_confirmed_alive** | 165.239.144.5:2101 — connection timeout from external IP (consistent with account-gated access); turngps.utah.gov portal HTTP 200 — 2026-05-07 |
| **station count** | Statewide coverage across Utah; extends into southern Idaho, western Wyoming, and southern Nevada |

### Context Notes

- TURN GPS is a state-managed paid service, not a commercial vendor.
- Registration: turngps.utah.gov → create Utah ID → subscribe at turngps-billpay.ugrc.utah.gov.
- Constellations: GPS + GLONASS (primary); additional constellation support via Trimble Pivot.
- TURN GPS also administers the Nevada GPS Network (see NV section below).

---

## NV — Nevada: Nevada GPS Network (via TURN GPS)

| Field | Value |
|---|---|
| **Network name** | Nevada GPS Network (formerly Washoe County GPS Network / NNCRN) |
| **Operator** | Utah Geospatial Resource Center (UGRC) — administered jointly; historically Washoe County, NV |
| **host:port** | `168.179.231.11:2102` (NAD83/HARN legacy); `165.239.144.7:2101` (NAD83/2011) |
| **tariff** | Paid — USD 600/year (bundled with TURN GPS Utah subscription; same account covers both networks) |
| **VRS** | Yes — Trimble Pivot VRS (same platform as TURN GPS) |
| **hobbyist_eligibility** | Unclear — same conditions as TURN GPS |
| **legal_residency_required** | Unclear — same conditions as TURN GPS |
| **last_confirmed_alive** | nevadagps.utah.gov portal active (ECONNREFUSED from external TCP probe — firewall consistent with account-gated access); Sensor Map at nevadagps.utah.gov/Map/SensorMap.aspx confirmed |
| **coverage** | Reno area (northern Nevada); coverage is not statewide — southern Nevada and Las Vegas metro are not covered by this network |

### Context Notes

- The Nevada GPS Network was originally the Washoe County GPS Network (Reno area); it was transferred to Utah UGRC management.
- Subscribers to TURN GPS automatically gain Nevada network access.
- Las Vegas area is served by the Las Vegas Valley Water District (LVVWD) Leica network — contact via LVVWD Engineering Survey Division (702-258-7163); not a free public service.
- EarthScope NOTA has stations in Nevada (Basin and Range region, high station density compared to many western states).

---

## WY — Wyoming: No Public State Caster

No state-operated RTK NTRIP caster found for Wyoming as of 2026-05-07. WYDOT does not operate a public CORS RTK network. The Professional Land Surveyors of Wyoming (PLSW) references CORS resources but does not operate an NTRIP caster.

**Gap:** TURN GPS (Utah) provides partial edge coverage in southern Wyoming near the Utah border. EarthScope NOTA (Plate Boundary Observatory stations) provides sparse single-base streams. Commercial options: RTKdata (USD 40/mo), Point One Polaris. No free public VRS network exists for Wyoming.

---

## MT — Montana: MTSRN

| Field | Value |
|---|---|
| **Network name** | Montana State Reference Network (MTSRN) |
| **Operator** | Montana State Library (MSL), with partners including MDT (Montana Department of Transportation), tribal nations, counties, educational institutions; Trimble Pivot VRS platform |
| **host:port** | `mtsrn.org:2101` (IP 3.23.213.134) |
| **tariff** | Paid — USD 1,500 per login per year (rate effective July 1, 2024; rates reviewed each biennium). Payment via PayZang portal. |
| **VRS** | Yes — VRS corrections broadcast across five geographic subnets: Northeast MT (NEMT), Northcentral MT (NCMT), Northwest MT (NWMT), Southwest MT (SWMT), Southcentral MT (SCMT) |
| **hobbyist_eligibility** | Unclear — subscription requires registration via Trimble Pivot site; no professional license explicitly required; USD 1,500/yr is a significant barrier for occasional hobbyist use |
| **legal_residency_required** | Unclear — no stated restriction; contact mtsrn@mt.gov |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe of mtsrn.org:2101) |
| **station count** | 50+ GNSS reference stations statewide |

### Context Notes

- MTSRN launched March 2022; commercial subscription service launched shortly after.
- Registration: mtsrn.org/RegisterAccount.aspx → PayZang payment → confirmation email from MTSRN Coordinator Kazi Arifuzzaman (mtsrn@mt.gov / 406-444-0240).
- Static RINEX data is free to the public; real-time NTRIP requires subscription.
- Partners (tribal nations, counties, etc.) receive access at no cost in exchange for station hosting contributions.

---

## ID — Idaho: No Public State Caster

No state-operated RTK NTRIP caster found for Idaho as of 2026-05-07. ITD (Idaho Transportation Department) installed CORS stations circa 2005–2006 for internal use but does not appear to operate a public RTK NTRIP service. Idaho Surveying & Land Information Center (ISU GIS Center) documented plans for a Real-Time Network for Idaho but no operational public endpoint was found.

**Gap:** TURN GPS (Utah) extends partial coverage into southern Idaho. EarthScope NOTA provides sparse single-base streams (Plate Boundary Observatory stations in Idaho). Commercial options: RTKdata (USD 40/mo), Point One Polaris.

---

## CA — California: CRTN (California Real-Time Network)

| Field | Value |
|---|---|
| **Network name** | California Real-Time Network (CRTN) |
| **Operator** | Scripps Orbit and Permanent Array Center / California Spatial Reference Center (SOPAC/CSRC), UC San Diego — clearinghouse aggregating: EarthScope NOTA, UC Berkeley/USGS BARD, USGS Pasadena SCIGN, Caltrans CVSRN, Orange County OCRTN, SOPAC SCIGN |
| **host:port** | `132.239.152.4:2102` (NorCal Zones 1–2) · `132.239.152.4:2103` (NorCal Zones 3–4) · `132.239.152.4:2104` (SoCal Zone 5) · `132.239.152.4:2105` (SoCal Zone 6) |
| **tariff** | One-time USD 100 registration/processing fee (universities and schools exempt); no annual charge. One free NTRIP account per user; additional accounts: USD 1,000/yr per additional account (contributing members). Source: sopac-csrc.ucsd.edu, observed 2026-05-07 |
| **VRS** | No — individual physical base station streams only (RTCM 3.0 per station); not a VRS network |
| **hobbyist_eligibility** | Unclear — no explicit professional restriction; USD 100 fee is accessible; registration via SurveyMonkey form; account approval takes at least 7 days |
| **legal_residency_required** | No — no stated residency requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 on both 132.239.152.4:2102 (NorCal) and 132.239.152.4:2104 (SoCal) (curl probes) |
| **format** | RTCM 3.0 (standard); RTCM 3.1 also available by modifying mountpoint name to `XXXX_RTCM3P1` (announced October 2025) |
| **contact** | Maria Turingan, mrturingan@ucsd.edu |

### Context Notes

- CRTN is a data clearinghouse, not a network RTK processor. It does not compute VRS corrections; users must select a nearby physical base station and maintain acceptable baseline distance (~20–30 km for RTK).
- Zone selection is geographic — use the nearest zone's port for best performance.
- The BARD (Bay Area Regional Deformation) component at UC Berkeley provides real-time streams for the San Francisco Bay Area.
- Caltrans CVSRN (Central Valley Spatial Reference Network) stations are included.
- Registration: SurveyMonkey form linked from sopac-csrc.ucsd.edu/index.php/crtn-connecting/

---

## OR — Oregon: ORGN

| Field | Value |
|---|---|
| **Network name** | Oregon Real-Time GNSS Network (ORGN) |
| **Operator** | Oregon Department of Transportation (ODOT) — Geometronics Unit; Leica GNSS Spider software |
| **host:port** | `orgn.odot.state.or.us:9881` (IP 167.131.109.57; confirmed SOURCETABLE 200 OK 2026-05-07) |
| **tariff** | Free — "All rover users will be issued a rover account at no direct charge" (ODOT, beta phase; future subscription fees noted as possible for non-partner users) |
| **VRS** | Yes — network (i-MAX/MAX) multi-base correctors; also single-base correctors for users outside primary network boundary |
| **hobbyist_eligibility** | Likely yes — stated "all users" receive accounts at no charge; no professional license field identified in account request; contact ORGN@odot.oregon.gov to confirm |
| **legal_residency_required** | No — no stated restriction |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe of 167.131.109.57:9881; hostname orgn.odot.state.or.us resolves to this IP) |
| **format** | RTCM 3.x (non-proprietary); also Trimble CMR+ for Trimble equipment users |

### Context Notes

- Accounts issued as NTRIP username and password via the ORGN rover account request form at oregon.gov/odot/orgn/pages/account-requests.aspx.
- ODOT states it may "charge reasonable subscription fees for rover accounts" in future; partner accounts remain free permanently.
- ORGN uses non-standard port 9881 (Leica Spider default), not 2101. Port 2101 timed out; port 9881 confirmed active.
- Contact: ORGN@odot.oregon.gov; ODOT Geometronics Unit, 800 Airport Road SE, Salem, OR 97301.

---

## WA — Washington: WSRN

| Field | Value |
|---|---|
| **Network name** | Washington State Reference Network (WSRN) |
| **Operator** | Multi-agency public/private cooperative; operated through Trimble Pivot platform; administered from wsrn3.org |
| **host:port** | `wsrn.org:2011` (NAD83-2011 datum) · `wsrn.org:2022` (NATRF2022 new datum); legacy port 8080 is being retired |
| **tariff** | Paid — Non-partner subscription: USD 1,900/yr per login; 5 logins: USD 5,700/yr; 10 logins: USD 10,000/yr; 20 logins: USD 15,000/yr. Partner agencies (government, NGS cooperators) receive free access. Source: WSRN FAQ (wsrn3.org, observed 2026-05-07) |
| **VRS** | Yes — Trimble Pivot network corrections; mountpoints listed at wsrn3.org/MountpointNaming.aspx |
| **hobbyist_eligibility** | Unclear — registration at wsrn3.org/RegisterAccount.aspx; no professional license explicitly required; USD 1,900/yr is a practical barrier for hobbyist use |
| **legal_residency_required** | Unclear — no stated residency requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 on both wsrn.org:2011 and wsrn.org:2022 (curl probes) |
| **datum transition** | WSRN is actively transitioning to NATRF2022; port 2022 delivers NATRF2022; port 2011 delivers legacy NAD83(2011). Port 8080 will be retired. |

### Context Notes

- WSRN is a long-running cooperative involving WSDOT and multiple public/private partners.
- Partner agencies (state, federal, local government) receive free access; non-partners pay USD 1,900/yr.
- The City of Bellingham documents WSRN as available via cob.org/services/maps/monuments/wsrn.
- PANGA (Pacific Northwest Geodetic Array, operated by Central Washington University) operates 220+ GNSS stations in the PNW for geodetic science; real-time GNSS processing is done internally (JPL RTG + Trimble RTKNet); no confirmed public NTRIP caster endpoint found for PANGA as of 2026-05-07.

---

## HI — Hawaii: No Public State Caster

No state-operated RTK NTRIP caster found for Hawaii as of 2026-05-07. HDOT does not appear to operate a public CORS RTK network. Hawaii is not listed in GPS World's public RTK state list or E38 Survey Solutions' state-by-state guide.

**Gap:** EarthScope NOTA has GNSS stations in Hawaii (geologically important volcanic monitoring sites on Big Island and Maui), though station spacing is limited and islands are geographically isolated. Topcon announced expansion of Topnet Live service to include Hawaii in October 2024 — a commercial paid option. Commercial alternatives: Topnet Live (Topcon), Point One Polaris. No free VRS network identified.

---

## Multi-State Commercial Networks (reference)

| Network | Coverage | host:port | Tariff | VRS |
|---|---|---|---|---|
| **RTKdata** | All 50 states | Contact rtkdata.com | USD 40/mo; 30-day free trial | Unknown |
| **Point One Polaris** | All 50 states | Contact pointonenav.com | USD 50/mo | Yes |
| **SmartNet (Leica/Hexagon)** | OK, TX, WA, others | Contact smartnetna.com | Paid (not disclosed publicly) | Yes |
| **Topnet Live (Topcon)** | TX, WA, HI, others | Contact topconpositioning.com | Paid | Yes |
| **RTK Premium** | Most western states (gaps) | Contact rtkpremium.com | Paid | Yes |

---

## Post-Processing Fallback

| Service | Coverage | Cost |
|---|---|---|
| **NOAA NCN CORS** — static RINEX download | All western states | Free; no account required |
| **EarthScope NOTA RINEX archive** | All western states (variable density) | Free noncommercial; account required |
| **CRTN RINEX (SOPAC/CSRC)** | California | Free; same account as NTRIP access |
| **SOPAC/BARD** — UC Berkeley Bay Area | California Bay Area | Free |

---

## Sources Consulted

- ODOT ORGN product page: https://www.oregon.gov/odot/orgn/pages/products-services.aspx (observed 2026-05-07)
- ODOT ORGN rover accounts: https://www.oregon.gov/odot/orgn/pages/account-requests.aspx
- ODOT ORGN about page: https://www.oregon.gov/odot/orgn/pages/about-us.aspx
- AZCORS / ADWR page: https://www.azwater.gov/hydrology/azcors (observed 2026-05-07)
- AZCORS mountpoints doc (April 2026): https://www.azwater.gov/sites/default/files/2026-04/AZCORS_InformationAndMountpoints20260406.pdf
- AZCORS SBC login: https://azcors.azwater.gov/sbc/Account
- AZCORS new station article (March 2025): https://www.azwater.gov/news/articles/2025-03-19
- AZGeo AZCORS hub: https://azgeo-data-hub-agic.hub.arcgis.com/pages/azcors
- ARDOT RTN portal: http://gps.ardot.gov/ (SOURCETABLE 200 OK confirmed 2026-05-07)
- ARDOT RTN sensor map: http://gps.ardot.gov/Map/SensorMap.aspx
- ARDOT GPS Control / Arkansas GIS Office: https://gis.arkansas.gov/product/ardot-gps-control/
- ARDOT Control Surveys page: https://ardot.gov/divisions/surveys/control-surveys/
- PAGIS GPS Reference Station: https://www.pagis.org/index.php/data-resources/gps-reference-station-access/
- TxDOT RTN portal: https://txrtn.txdot.gov/ (HTTP 200 confirmed 2026-05-07)
- TxDOT GPS page: https://www.txdot.gov/data-maps/global-positioning-system-gps.html
- C4Gnet.XYZ portal: https://c4gnet.xyz/ (observed 2026-05-07)
- C4Gnet NTRIP mountpoints: http://c4gnet.xyz/NTRIP_Mountpoints.aspx
- LSU C4G store — 1-year unlimited RTK: https://store.c4g.lsu.edu/products/1-year-unlimited-rtk-rover-ntrip-only-account (USD 3,500 observed 2026-05-07)
- LSU C4G store — full RTN: https://store.c4g.lsu.edu/index.php?product_id=62&route=product%2Fproduct
- Mesa County RTVRN: https://www.mesacounty.us/departments-and-services/public-works/gps-survey/real-time-virtual-reference-network-rtvrn (observed 2026-05-07)
- Mesa County GPS Survey: https://www.mesacounty.us/departments-and-services/public-works/gps-survey
- TURN GPS UGRC: https://gis.utah.gov/products/turn/ (observed 2026-05-07)
- TURN GPS connecting guide: https://gis.utah.gov/documentation/turn/connecting/
- TURN GPS bill pay: https://turngps-billpay.ugrc.utah.gov
- Nevada GPS Network (UGRC): https://gis.utah.gov/gps/ngps/
- Nevada GPS Network (Reno portal): https://nevadagps.utah.gov/
- MTSRN main: https://msl.mt.gov/mtsrn/ (observed 2026-05-07)
- MTSRN subscribe: https://msl.mt.gov/mtsrn/subscribe
- MTSRN FAQ: https://msl.mt.gov/mtsrn/faq
- MTSRN how it works: https://msl.mt.gov/mtsrn/howitworks
- MTSRN subscription launch announcement: https://content.govdelivery.com/accounts/MTLIBRARY/bulletins/393bfda
- MTSRN Pivot portal: https://www.mtsrn.org/ (SOURCETABLE 200 OK on :2101 confirmed 2026-05-07)
- CRTN (SOPAC/CSRC): http://sopac-csrc.ucsd.edu/index.php/crtn/ (observed 2026-05-07)
- CRTN connecting guide: http://sopac-csrc.ucsd.edu/index.php/crtn-connecting/
- WSRN about: http://www.wsrn.org/about.aspx
- WSRN new visitor info: http://www.wsrn3.org/NewREADME.aspx
- WSRN join/register: http://wsrn3.org/RegisterAccount.aspx
- WSRN datum plan: http://www.wsrn.org/WSRN_Datum_Plan.pdf
- WSRN Update (CSRC presentation May 2025): https://sopac-csrc.ucsd.edu/wp-content/uploads/2025/07/WSRN-Update-CSRC-051525.pdf
- WSRN Mountpoint naming: http://www.wsrn3.org/MountpointNaming.aspx
- City of Bellingham WSRN page: https://cob.org/services/maps/monuments/wsrn
- PANGA (CWU geodesy): https://www.geodesy.org/realtime/
- MTSRN biennium rate announcement (Sept 2024): https://archive.legmt.gov/content/Publications/fiscal/2025-Biennium/Section-E/Interim/MSL-MT-State-Reference-Network-Update-Sept2024.pdf
- EarthScope GNSS Realtime: https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA: https://www.earthscope.org/nota/
- E38 Survey Solutions — RTK by state: https://e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state (observed 2026-05-07)
- ArduSimple — US RTK casters: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/ (observed 2026-05-07)
- NTRIP-list North America: https://ntrip-list.com/north-america/ (observed 2026-05-07)
- GPS World public RTK list: https://www.gpsworld.com/finally-a-list-of-public-rtk-base-stations-in-the-u-s/
- Point One Nav — state pages for AZ, TX, OK, NM, WY, ID, HI: https://pointonenav.com/states/[state]/
- Topcon Topnet Live Hawaii expansion (Oct 2024): https://www.topconpositioning.com/us/en/articles/topcon-announces-significant-expansion-of-topnet-live-coverage-across-western-usa-and-hawaii
- curl probes performed 2026-05-07:
  - gps.ardot.gov:2101 — SOURCETABLE 200 OK
  - rtvrn.mesacounty.us:2101 — SOURCETABLE 200 OK
  - mtsrn.org:2101 — SOURCETABLE 200 OK
  - wsrn.org:2011 — SOURCETABLE 200 OK
  - wsrn.org:2022 — SOURCETABLE 200 OK
  - 132.239.152.4:2102 — SOURCETABLE 200 OK (CRTN NorCal)
  - 132.239.152.4:2104 — SOURCETABLE 200 OK (CRTN SoCal)
  - orgn.odot.state.or.us:9881 (167.131.109.57:9881) — SOURCETABLE 200 OK
  - txrtn.txdot.gov — HTTP 200 portal; NTRIP port not public
  - azcors.azwater.gov:2101 — timeout (Cloudflare CDN; backend port scheme via Leica SBC provided post-registration)
  - 165.239.144.5:2101 (TURN GPS) — timeout (account-gated firewall)
  - c4gnet.xyz:9000 — DNS resolves; portal HTTP 200
