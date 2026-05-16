# US West & Southwest — NTRIP RTK Caster Research

**Date researched:** 2026-05-15

**States covered:** Texas (TX), Oklahoma (OK), Arkansas (AR), Louisiana (LA), New Mexico (NM), Arizona (AZ), Colorado (CO), Utah (UT), Nevada (NV), Wyoming (WY), Montana (MT), Idaho (ID), California (CA), Oregon (OR), Washington (WA), Hawaii (HI)

## Status: MIXED — free public casters: AR (ARDOT), AZ (AZCORS), CO (Mesa County RTVRN), OR (ORGN); paid subscription casters: LA (C4Gnet), UT/NV-Reno (TURN GPS), MT (MTSRN), WA (WSRN); TX restricted to DOT employees; OK, NM, ID, HI, WY have no state caster; CA (CRTN) has a one-time fee model; EarthScope NOTA + NPS CORS provide free single-base fallback region-wide

---

## Per-State Summary Table

| State | Free public caster | Network | host:port | VRS | Hobbyist | Probe result (2026-05-15) |
|---|---|---|---|---|---|---|
| TX | No (DOT-restricted) | TxDOT RTN | `txrtn.txdot.gov` (port not public) | Yes | No — employees/contractors only | Portal HTTPS 200; NTRIP port not published |
| OK | No | — | — | — | — | No state caster found |
| AR | Yes (free) | ARDOT RTN | `gps.ardot.gov:2101` | Yes | Likely yes | `SOURCETABLE 200 OK` — 8 STR |
| LA | Paid | C4Gnet (LSU C4G) | `c4gnet.xyz:9000` | Yes | Unclear | `SOURCETABLE 200 OK` — 32 STR |
| NM | No | — | — | — | — | No state caster confirmed; ARTGN status undocumented |
| AZ | Yes (free) | AZCORS | `azcors.azwater.gov` (port via SBC) | Yes | Yes | Portal behind Cloudflare; site active (PDF probe 403 anti-bot) |
| CO | Yes (free) | Mesa County RTVRN | `rtvrn.mesacounty.us:2101` | Yes | Likely yes | `SOURCETABLE 200 OK` — 6 STR |
| UT | Paid | TURN GPS | `165.239.144.5:2101` | Yes | Yes (Utah ID required, no residency) | Connection timeout (account-gated firewall) |
| NV | Paid | Nevada GPS Network (via TURN) | `168.179.231.11:2102` | Yes | Yes (TURN bundle) | Connection timeout (account-gated firewall) |
| NV | Paid (LV metro) | LVVWD GPS Network | host n/p, port `9899` | No (single-base) | Unclear | Application-gated; pricing not public |
| WY | No | — | — | — | — | No state caster; TURN GPS partial edge coverage |
| MT | Paid | MTSRN | `mtsrn.org:2101` | Yes | Unclear | `SOURCETABLE 200 OK` — 340 STR |
| ID | No | — | — | — | — | No state caster; TURN GPS edge coverage |
| CA | Fee (one-time) | CRTN (SOPAC/UCSD) | `132.239.152.4:2102–2105` | No | Likely yes | `SOURCETABLE 200 OK` on all four ports — 148/164/230/128 = 670 STR total (NorCal Z1-2 / Z3-4 / SoCal Z5 / Z6) |
| OR | Yes (free) | ORGN (ODOT) | `orgn.odot.state.or.us:9881` | Yes | Likely yes | `SOURCETABLE 200 OK` — 6 STR |
| WA | Paid | WSRN | `wsrn.org:2011` (NAD83-2011) + `wsrn.org:2022` (NATRF2022) | Yes | Unclear | `SOURCETABLE 200 OK` on 2011 (495 STR) and 2022 (0 STR, CAS-only) |
| HI | No | — | — | — | — | No state caster found |

**Regional baselines (all states):**

- **EarthScope NOTA** — `ntrip.earthscope.org:2101` — free non-commercial, single-base streams only. Densest coverage in seismically active western Cordillera (PBO heritage). 2026-05-15 probe: `SOURCETABLE 200 OK`, 1,095 STR entries globally.
- **NPS CORS** — `rtk.nps.gov:2101` — free; credentials only via gnss_posnav@nps.gov (manual provisioning). Many Western parks: Yosemite, Yellowstone, Grand Canyon, Glacier, Olympic, Crater Lake, Death Valley, Joshua Tree, Hawaii Volcanoes, Haleakalā. Some sites flagged offline as of 2026-05-02 (HALE, HAVO). See `US-NPS_NationalParkService.md`.

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
| **last_confirmed_alive** | `SOURCETABLE 200 OK` on 2026-05-15 (curl probe; 1,095 STR entries globally) |
| **datum_epoch** | Per-station; mix of IGS14/ITRF2014 and NAD83(2011) products; see EarthScope station metadata |
| **notes** | NOTA has dense coverage in western seismically active regions (Pacific Coast, Basin and Range, Rocky Mountains). Station spacing is variable — compact along active fault zones (CA, OR, WA, NV, UT), sparse in plains states (OK, TX panhandle, WY interior). Adequate for PPK/static; may be marginal for real-time RTK where baseline >30 km. Old hostname `rtgpsout.earthscope.org` retired July 2025. |

---

## NPS CORS — Federal Baseline (Western parks)

| Field | Value |
|---|---|
| **Network** | National Park Service CORS network |
| **Operator** | U.S. Department of the Interior, National Park Service (NPS) |
| **host:port** | `rtk.nps.gov:2101` (current; portal at ntrip.nps.gov) |
| **tariff** | Free — federal government service at no cost |
| **account provisioning** | Manual — contact gnss_posnav@nps.gov; no self-service |
| **hobbyist_eligibility** | Unclear — manual approval at NPS staff discretion |
| **VRS** | No — single-base RTK; RTCM MSM4 |
| **last_confirmed_alive** | 2026-05-02 (per `US-NPS_NationalParkService.md`) |
| **datum_epoch** | NAD83(2011)/2010.00 — transitioning to MYCS3 (applied 2026-02-13) per US-NPS file. Citation: see `docs/ntrip_research/US-NPS_NationalParkService.md`. |
| **Western coverage** | Yosemite, Yellowstone, Grand Canyon, Glacier, Olympic, Crater Lake, Death Valley, Joshua Tree, Hawaii Volcanoes, Haleakalā, Bryce Canyon, Zion, Sequoia, and others. Pacific stations: Hawaii Volcanoes (HAVO — flagged offline 2026-05-02), Haleakalā (HALE — flagged offline). |

---

## TX — Texas: TxDOT RTN (Restricted Access)

| Field | Value |
|---|---|
| **Network name** | TxDOT Real Time Network (TxDOT RTN) |
| **Operator** | Texas Department of Transportation (TxDOT) — Information Systems Division |
| **landing_url** | https://txrtn.txdot.gov/ |
| **access_url** | https://txrtn.txdot.gov/ (employees/contractors only) |
| **host:port** | `txrtn.txdot.gov` — port not publicly documented; NTRIP endpoint is not disclosed |
| **tariff** | No charge — access is restricted, not sold |
| **VRS** | Yes — network VRS; 256 CORS stations statewide |
| **num_stations** | 256 (stated, one per Texas county) |
| **hobbyist_eligibility** | No — restricted to TxDOT employees and TxDOT contractors/consultants on TxDOT-funded projects |
| **legal_residency_required** | N/A (restricted network) |
| **last_confirmed_alive** | `txrtn.txdot.gov` HTTPS 200 — 2026-05-15; sensor map at txrtn.txdot.gov/Map/SensorMap.aspx |
| **datum_epoch** | NAD83(2011)/2010.00 — Texas State Plane (per TxDOT survey datum policy); citation: omitted (no public TxDOT RTN datum doc accessible to non-staff). |

### Context Notes

- TxDOT operates one of the largest state-run CORS networks in the country (256 stations across all 254 counties) but has not opened it to public use. RPLS forum and Emlid community threads confirm public access is unavailable.
- No registration pathway exists for non-TxDOT users.
- Practical fallback: EarthScope NOTA (free, sparse), commercial networks (RTKdata, Point One, SmartNet).
- GPS World's December 2024 state-by-state public RTK list does not list Texas as having a public service.

---

## OK — Oklahoma: No Public State Caster

No state DOT or university RTK NTRIP caster found for Oklahoma as of 2026-05-15. ODOT (Oklahoma Department of Transportation) does not operate a public CORS RTK network. Multiple sources (E38 Survey Solutions, Point One Nav, GPS World) confirm "no public service" for Oklahoma.

**Gap:** Commercial options are the primary recourse: SmartNet Oklahoma (Leica; covers Oklahoma City and Tulsa markets), RTKdata (USD 40/mo, statewide coverage claimed), Point One Polaris. EarthScope NOTA provides sparse single-base fallback in western OK; nearest dense free RTN coverage is ARDOT (gps.ardot.gov:2101) reachable from eastern OK within ~50 km of the AR border.

---

## AR — Arkansas: ARDOT RTN

| Field | Value |
|---|---|
| **Network name** | Arkansas Continuously Operating Reference Station Network / ARDOT Real Time Network (ARDOT RTN) |
| **Operator** | Arkansas Department of Transportation (ARDOT) — Surveys Division; Trimble Pivot platform |
| **landing_url** | http://gps.ardot.gov/ |
| **access_url** | http://gps.ardot.gov/Login.aspx (self-service Trimble Pivot account registration) |
| **host:port** | `gps.ardot.gov:2101` (IP 199.48.3.12) |
| **tariff** | Free |
| **VRS** | Yes — Trimble Pivot VRS; mountpoints include `ARDOT_RTX_CMRp/CMRx/RTCM31/RTCM34` (network solutions) and `MS_CMRp/CMRx/RTCM31/RTCM34` (Nearest Single Base, NSB) |
| **num_stations** | Mountpoints: 8 STR (4 NSB + 4 VRS format variants); underlying base-station count not publicly enumerated on the portal — ARDOT lists "GNSS CORS stations aligned with the NGS National Spatial Reference System" without count. |
| **hobbyist_eligibility** | Likely yes — self-service portal registration; no professional license field; no published hobbyist restriction |
| **legal_residency_required** | Unclear — no stated residency requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-15 (curl probe of `gps.ardot.gov:2101`; 8 STR entries) |
| **datum_epoch** | NAD83(2011)/2010.00 (aligned with NGS NSRS; stated on ARDOT Control Surveys page); citation: https://ardot.gov/divisions/surveys/control-surveys/ |

### Context Notes

- ARDOT and partners maintain GNSS CORS stations aligned with the NGS NSRS.
- Registration at gps.ardot.gov (Trimble Pivot portal; login page at gps.ardot.gov/Login.aspx).
- Sensor map: http://gps.ardot.gov/Map/SensorMap.aspx
- Configuration guide for Trimble receivers: http://gps.ardot.gov/Configuring%20Trimble%20Receiver%20on%20ARDOT%20RTN.pdf (HTTP 200 confirmed 2026-05-15)
- **PAGIS (Pulaski Area GIS)** — supplementary single-base station in North Little Rock / Little Rock / Pulaski County AR; free; requires signed user agreement; NTRIP address provided post-registration; contact pagis.org 501.377.1264. Single station, not a VRS network; usable within ~300 km / 185 miles.

---

## LA — Louisiana: C4Gnet (LSU Center for GeoInformatics)

| Field | Value |
|---|---|
| **Network name** | C4Gnet — Louisiana Statewide Real Time Network |
| **Operator** | LSU Center for GeoInformatics (C4G), Louisiana State University |
| **Software** | Trimble Pivot (caster banner: "NTRIP Trimble Ntrip Caster 5.2") |
| **landing_url** | https://c4gnet.xyz/ |
| **access_url** | https://store.c4g.lsu.edu/ (paid subscription) |
| **host:port** | `c4gnet.xyz:9000` |
| **tariff** | Paid — 10-hour RTK: USD 495/yr; 50-hour RTK: USD 1,995/yr; 1-year unlimited RTK (NTRIP only): USD 3,500; Full RTN membership: USD 5,000/yr; GIS DGPS unlimited: USD 995/yr. Source: store.c4g.lsu.edu, observed 2026-05-15 |
| **VRS** | Yes — VRS, PPP, and Nearest Single Base (NSB) mountpoints (RTCM 3.2-MSM, CMR+, CMRx); RTCM3 banner shows GPS+GLO+GAL+BDS |
| **num_stations** | Mountpoints: 32 STR (mix of VRS, PPP, NSB variants across formats and reference frames); underlying base-station inventory not enumerated on portal |
| **hobbyist_eligibility** | Unclear — no explicit restriction; entry-level 10-hour tier at USD 495/yr is the lowest barrier but still above the project's USD 200/yr hobbyist cutoff |
| **legal_residency_required** | Unclear — no stated residency requirement; LSU-operated, US-accessible |
| **last_confirmed_alive** | `c4gnet.xyz:9000` `SOURCETABLE 200 OK` on 2026-05-15 (curl probe; 32 STR entries) |
| **datum_epoch** | NAD83(2011) and ITRF2014 products both available; mountpoint name suffix indicates reference frame (e.g. `..._NAD83`); citation: http://c4gnet.xyz/NTRIP_Mountpoints.aspx |

### Context Notes

- Network established 2007 with Louisiana statewide CORS infrastructure.
- Mountpoint naming: `TYPE_SATS_FORMAT_REFERENCEFRAME` (e.g., `GLN_RTCM3_2` = full constellation VRS in RTCM 3.2; `PPP_GNSS_CMRp_NAD83` = PPP NSB in CMR+ on NAD83).
- Subscriptions purchased at store.c4g.lsu.edu.
- Free post-processing (RINEX download) available separately — annual free subscription; contact rosbor1@lsu.edu or vdubinin@lsu.edu.

---

## NM — New Mexico: No Confirmed Public State Caster

No state-operated RTK NTRIP caster confirmed operational for New Mexico as of 2026-05-15. NMDOT does not operate a public CORS RTK network. Multiple sources (GPS World, E38 Survey Solutions, Point One Nav) do not list NM as having a public service.

**Historic ARTGN (Albuquerque Real-Time GNSS Network):** Launched 2007 by the City of Albuquerque as a paid subscription service (~USD 200/month per the December 2010 American Surveyor article); served the Albuquerque Geodetic Reference System (AGRS) ~800-monument framework. Current operational status undocumented online — no post-2013 press releases or municipal updates found. The City of Albuquerque AGRS page (cabq.gov/municipaldevelopment/…/albuquerque-geodetic-reference-system, HTTP 200 on 2026-05-15) makes no current ARTGN reference. Contact City Surveyor Loren Risenhoover at 505-768-3614 to confirm current status.

**Gap:** Commercial options: RTKdata (USD 40/mo, claims statewide NM coverage), Point One Polaris, RTK Premium. EarthScope NOTA has stations in NM (moderate density along the Rio Grande Rift); useful for PPK and possibly single-base RTK near population centers (TUCUMCARI, PIETOWN, WHITE SANDS region). Cross-border alternatives within ~50 km of state line: ARDOT (eastern AR, far from NM); AZCORS (free) reachable from western NM near the AZ border.

---

## AZ — Arizona: AZCORS

| Field | Value |
|---|---|
| **Network name** | Arizona CORS Network (AZCORS) |
| **Operator** | Arizona Department of Water Resources (ADWR) — Leica Spider Business Center (SBC) platform |
| **landing_url** | https://www.azwater.gov/hydrology/azcors |
| **access_url** | https://azcors.azwater.gov/sbc/Account/Register (self-service registration) |
| **host:port** | `azcors.azwater.gov:2101` (Leica SBC default); external probe is gated by Cloudflare CDN — the NTRIP caster TCP socket is reachable only after account provisioning. Stations.json health: `azcors` source is in error/timeout state (data/source_health.json, 2026-05-15) — the pipeline's anonymous probe is firewalled; the caster itself is documented active per April 2026 ADWR materials. |
| **tariff** | Free — "free access to all Real Time and RINEX Data Products in the AZCORS network" (ADWR, observed 2026-05-15) |
| **VRS** | Yes — Leica SBC supports iMAX/MAX network solutions; full mountpoint list distributed post-registration |
| **num_stations** | 71 total CORS sites: 56 ADWR-managed + 15 ingested from EarthScope and National Park Service. Source: azwater.gov/hydrology/azcors landing page, last updated 2026/04/14 per page metadata. The AZCORS_InformationAndMountpoints20260406.pdf hosted on azwater.gov returns HTTP 403 (anti-bot) to scripted probes but is referenced from the public page. |
| **hobbyist_eligibility** | Yes — open registration at azcors.azwater.gov/sbc/Account/Register; no professional license required |
| **legal_residency_required** | No — no stated residency requirement |
| **last_confirmed_alive** | ADWR AZCORS landing page active (Cloudflare challenge for scripted GETs; HTTP 200 in browser, last update banner 2026/04/14); ArduSimple US RTK list (observed 2026-05-15) lists AZCORS as a free public NTRIP service |
| **datum_epoch** | NAD83(2011)/2010.00 — confirmed in AZCORS mountpoint document and consistent with NGS NSRS; citation: https://www.azwater.gov/hydrology/azcors (page references AZCORS_InformationAndMountpoints20260406.pdf) |

### Context Notes

- ADWR operates two virtual servers for network redundancy.
- Information and mountpoints document updated April 6, 2026: https://www.azwater.gov/sites/default/files/2026-04/AZCORS_InformationAndMountpoints20260406.pdf (PDF probe HTTP 403 — anti-bot; page itself accessible in browser).
- Also listed on Arizona geospatial hub: https://azgeo-data-hub-agic.hub.arcgis.com/pages/azcors (HTTP 200 on 2026-05-15).
- AZCORS incorporates EarthScope and NPS stations, giving broad statewide coverage including remote desert and canyon country.
- Commercial alternative: AZGPS (azgps.net) — paid VRS network covering AZ and southern CA; founded Nov 2004, ~100+ sites; subscription pricing not publicly listed.

---

## CO — Colorado: Mesa County RTVRN

| Field | Value |
|---|---|
| **Network name** | Real-Time Virtual Reference Network (RTVRN) |
| **Operator** | Mesa County, Colorado — Public Works Department, GPS Survey |
| **Software** | Trimble Pivot (caster banner: "NTRIP Trimble Ntrip Caster 5.3") |
| **landing_url** | https://www.mesacounty.us/departments-and-services/public-works/gps-survey/real-time-virtual-reference-network-rtvrn |
| **access_url** | https://rtvrn.mesacounty.us/RegisterAccount.aspx (self-service registration) |
| **host:port** | `rtvrn.mesacounty.us:2101` (IP 35.131.54.14) |
| **tariff** | Free — "a free service to the public" (Mesa County, observed 2026-05-15) |
| **VRS** | Yes — six VRS mountpoints: `VRS_CMR`, `VRS_CMRx`, `VRS_RTCMv3`, `VRS_CMR_RTX`, `VRS_CMRx_RTX`, `VRS_RTCMv3_RTX` |
| **num_stations** | Mountpoints: 6 STR (all VRS variants); per Mesa County: 33 base stations contribute, of which 17 are NGS CORS stations |
| **hobbyist_eligibility** | Likely yes — public service with no stated restrictions; serves "surveying, construction, agriculture, mapping, and science industries" |
| **legal_residency_required** | No — no stated restriction |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-15 (curl probe of `rtvrn.mesacounty.us:2101`; 6 STR entries) |
| **datum_epoch** | NAD83(2011); epoch not explicitly published, presumed 2010.00 per NGS NSRS alignment; citation: https://www.mesacounty.us/sites/default/files/2025-05/RTVRN%20Login%20Instructions%20and%20NTRIP%20Mountpoints.pdf |

### Context Notes

- Registration at rtvrn.mesacounty.us (account subscription required; self-service).
- Coverage centred on Western Colorado (Grand Junction / Mesa County) but the 33-station network reaches across western CO and edges into adjacent UT and WY.
- Only confirmed free public VRS network in Colorado; CDOT does not operate a public RTK caster.
- Contact: Mesa County Public Works, GPS Survey section.

---

## UT — Utah: TURN GPS

| Field | Value |
|---|---|
| **Network name** | Utah Reference Network (TURN GPS) |
| **Operator** | Utah Geospatial Resource Center (UGRC) — State of Utah; Trimble Pivot VRS platform |
| **landing_url** | https://gis.utah.gov/products/turn/ |
| **access_url** | https://turngps-billpay.ugrc.utah.gov/ (subscription via Utah ID) |
| **host:port** | `165.239.144.5:2101` (NAD83/2011); also `165.239.144.7:2101` (NAD83/2011 alternate) |
| **tariff** | Paid — USD 600/year per login (currently bundles TURN Utah + Nevada GPS access; UGRC has indicated this may split per-region in future) |
| **VRS** | Yes — Trimble Pivot VRS; recommended mountpoint `GNSS-VRS-NAD83-RTCM32` (full multi-constellation: GPS+GLO+GAL+BDS); also `VRS-NAD83` variants in CMRp, CMRx, RTCM31, RTCM32; nearest-base `MS-` prefixed mountpoints |
| **num_stations** | 100+ stations; statewide UT plus portions of southern Idaho, western Wyoming, and southern Nevada |
| **hobbyist_eligibility** | Yes — subscription requires a Utah ID account; no professional license required |
| **legal_residency_required** | No — Utah ID is a state digital identity, not residency; non-residents can register |
| **last_confirmed_alive** | `165.239.144.5:2101` connection timeout from external IP on 2026-05-15 (consistent with account-gated firewall); turngps.utah.gov portal HTTPS 200 |
| **datum_epoch** | NAD83(2011)/2010.0000; citation: https://gis.utah.gov/documentation/turn/connecting/ |

### Context Notes

- TURN GPS is a state-managed paid service, not a commercial vendor.
- Registration: turngps.utah.gov → create Utah ID → subscribe at turngps-billpay.ugrc.utah.gov.
- Constellations: GPS + GLONASS + Galileo + BeiDou via RTCM3.2.
- TURN GPS also administers the Nevada GPS Network (Reno area) — see NV section.

---

## NV — Nevada: Multiple Operators

### Nevada GPS Network (UGRC; Reno / northern NV)

| Field | Value |
|---|---|
| **Network name** | Nevada GPS Network (formerly Washoe County GPS Network / NNCRN) |
| **Operator** | Utah Geospatial Resource Center (UGRC) — administered jointly; historically Washoe County, NV |
| **landing_url** | https://gis.utah.gov/gps/ngps/ |
| **access_url** | https://nevadagps.utah.gov/ (subscription via TURN bundle) |
| **host:port** | `168.179.231.11:2102` (NAD83/HARN legacy); `165.239.144.7:2101` (NAD83/2011) |
| **tariff** | Paid — USD 600/year (bundled with TURN GPS Utah subscription; same Utah ID covers both networks) |
| **VRS** | Yes — Trimble Pivot VRS (shared platform with TURN GPS) |
| **num_stations** | Coverage in Reno / Washoe County area; not statewide — southern NV and Las Vegas metro are not covered by this network |
| **hobbyist_eligibility** | Yes — same conditions as TURN GPS |
| **legal_residency_required** | No — same conditions as TURN GPS |
| **last_confirmed_alive** | `gis.utah.gov/gps/ngps/` HTTPS 200 on 2026-05-15; `nevadagps.utah.gov` HTTPS timeout from external IP (firewall consistent with account-gated access); `168.179.231.11:2102` TCP probe timed out |
| **datum_epoch** | NAD83(2011)/2010.00 on `165.239.144.7:2101`; legacy NAD83(HARN) on `168.179.231.11:2102`; citation: https://gis.utah.gov/gps/ngps/ |

### LVVWD GPS Base Station Network (Las Vegas Valley)

| Field | Value |
|---|---|
| **Network name** | Las Vegas Valley Water District GPS/GNSS Base Station Network |
| **Operator** | Las Vegas Valley Water District (cooperating with Nevada DOT, City of Las Vegas, Clark County Water Reclamation District, Lincoln County NV) |
| **landing_url** | https://www.lvvwd.com/engineering-resources/survey-right-of-way/ |
| **access_url** | https://www.lvvwd.com/apps/base-station-network-access/ (application form; credentials issued by District Surveyor 702-258-7163) |
| **host:port** | Host not publicly listed; **port 9899**. Mountpoint names match site names (e.g. `nvbm`). RTK link via NTRIP or TCP/IP. Source: lvvwd.com/engineering-resources/survey-right-of-way/, observed 2026-05-15 |
| **tariff** | Not publicly listed — credentials issued on application |
| **VRS** | No — single-base mountpoints |
| **num_stations** | Not publicly enumerated; multiple LV-area sites listed in member-cooperative description |
| **hobbyist_eligibility** | Unclear — application form collects entity/use info; no published policy on hobbyist eligibility |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | 2026-05-15 — application form and survey resources pages HTTPS 200 |
| **datum_epoch** | Unclear — not published on portal; presumed NAD83(2011) per typical Western state practice; citation: omitted (no public LVVWD datum statement) |
| **data archive** | Static 5-second epoch RINEX in 1-hour zipped files; downloadable via gps-data-share interface |

### Context Notes

- Nevada GPS Network was originally the Washoe County GPS Network (Reno); transferred to UGRC management.
- TURN GPS subscribers automatically gain Nevada (Reno) network access.
- LVVWD covers the Las Vegas Valley with a station network distinct from UGRC; access is application-based, pricing not disclosed publicly.
- EarthScope NOTA has stations in NV (Basin and Range region, high station density compared to many western states) — free fallback.

---

## WY — Wyoming: No Public State Caster

No state-operated RTK NTRIP caster found for Wyoming as of 2026-05-15. WYDOT does not operate a public CORS RTK network. The Professional Land Surveyors of Wyoming (PLSW) references CORS resources but does not operate an NTRIP caster. The Wyoming Geodetic Coordination Committee (geodetic.geospatialhub.org) lists resources but no operational caster.

**Gap:** TURN GPS (UT) provides partial paid edge coverage in southern Wyoming near the Utah border. EarthScope NOTA (Plate Boundary Observatory stations) provides sparse single-base streams. Commercial options: RTKdata (USD 40/mo), Point One Polaris, RTK Premium. No free public VRS network exists for Wyoming. Cross-border alternatives within ~50 km: Mesa County RTVRN (CO, free) reachable in extreme south-central WY; MTSRN (paid) reachable in northern WY near the MT border.

---

## MT — Montana: MTSRN

| Field | Value |
|---|---|
| **Network name** | Montana State Reference Network (MTSRN) |
| **Operator** | Montana State Library (MSL), with partners including MDT (Montana DOT), tribal nations, counties, and educational institutions; Trimble Pivot VRS platform |
| **landing_url** | https://msl.mt.gov/mtsrn/ |
| **access_url** | https://www.mtsrn.org/RegisterAccount.aspx (subscription via PayZang portal) |
| **host:port** | `mtsrn.org:2101` (IP 3.23.213.134) |
| **tariff** | Paid — USD 1,500 per login per year (rate effective July 1, 2024; rates reviewed each biennium and announced January of odd-numbered years, taking effect July 1). The 2027-biennium "MTSRN Revised Glidepath (March 2026)" document is published on legmt.gov but no 2026-07-01 rate change has been publicised at the time of this review. |
| **VRS** | Yes — VRS corrections broadcast across five geographic subnets: Northeast MT (NEMT), Northcentral MT (NCMT), Northwest MT (NWMT), Southwest MT (SWMT), Southcentral MT (SCMT) |
| **num_stations** | 50+ GNSS reference stations statewide. Mountpoint sourcetable: 340 STR rows (per-station × per-format combinations across the five subnets) on 2026-05-15. |
| **hobbyist_eligibility** | Unclear — registration via Trimble Pivot site; no professional license explicitly required; USD 1,500/yr is well above the project's USD 200/yr hobbyist cutoff; no published hobbyist tier |
| **legal_residency_required** | No — no stated restriction; contact mtsrn@mt.gov |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-15 (curl probe of `mtsrn.org:2101`; 340 STR entries) |
| **datum_epoch** | NAD83(2011)/2010.00 (per MTSRN documentation aligned with NGS NSRS); citation: https://msl.mt.gov/mtsrn/howitworks |

### Context Notes

- MTSRN launched March 2022; commercial subscription service launched shortly after.
- Registration: mtsrn.org/RegisterAccount.aspx → PayZang payment → confirmation email from MTSRN Coordinator Kazi Arifuzzaman (mtsrn@mt.gov / 406-444-0240).
- Static RINEX data is free to the public; real-time NTRIP requires subscription.
- Partners (tribal nations, counties, etc.) receive access at no cost in exchange for station hosting contributions; educational users have separate agreements.
- 2027-biennium update PDF: https://archive.legmt.gov/content/Publications/fiscal/2027-Biennium/Committees/Section-E/MSL-MT-State-Reference-Network-Update-March2026.pdf (HTTP 200 on 2026-05-15; binary text not auto-extracted, rate decision pending public announcement).

---

## ID — Idaho: No Public State Caster

No state-operated RTK NTRIP caster found for Idaho as of 2026-05-15. ITD (Idaho Transportation Department) installed CORS stations circa 2005–2006 (Pocatello, Idaho Falls, Rexburg, Driggs) for internal use but does not operate a public RTK NTRIP service. Idaho State University's GIS Center documented a Real-Time Network for Idaho (giscenter.isu.edu/research/Techpg/GC/rtn.htm); the cooperative ISU + Frontier Precision + Monsen + UGRC project established a southeastern Idaho VRS network (Pocatello/ISU + Jerome, Twin Falls, Blackfoot, Idaho Falls + planned Rupert, Aberdeen, Soda Springs) — the network's stations now feed into TURN GPS Utah's coverage footprint.

The 2024 Idaho Geospatial Office Geodetic Control TWG (gis.idaho.gov/geodetic-control-twg) lists "real-time correction network" as an ongoing focus area in cooperation with NGS for an Idaho spatial reference system update; no separate public Idaho caster has been announced.

**Gap:** TURN GPS (UT) extends paid coverage (USD 600/yr) into southern Idaho. EarthScope NOTA provides sparse single-base streams (PBO stations). Commercial options: RTKdata (USD 40/mo), Point One Polaris. Cross-border alternatives within ~50 km of state line: ORGN (free) in eastern OR near the ID border; MTSRN (paid) reachable from northern ID near the MT border.

---

## CA — California: CRTN (California Real-Time Network)

| Field | Value |
|---|---|
| **Network name** | California Real-Time Network (CRTN) |
| **Operator** | Scripps Orbit and Permanent Array Center / California Spatial Reference Center (SOPAC/CSRC), UC San Diego — clearinghouse aggregating: EarthScope NOTA, UC Berkeley/USGS BARD, USGS Pasadena SCIGN, Caltrans CVSRN, Orange County OCRTN, SOPAC SCIGN |
| **landing_url** | http://sopac-csrc.ucsd.edu/index.php/crtn/ |
| **access_url** | http://sopac-csrc.ucsd.edu/index.php/crtn-connecting/ (SurveyMonkey registration form; account approval ≥ 7 days) |
| **host:port** | `132.239.152.4:2102` (NorCal Zones 1–2) · `132.239.152.4:2103` (NorCal Zones 3–4) · `132.239.152.4:2104` (SoCal Zone 5) · `132.239.152.4:2105` (SoCal Zone 6) |
| **tariff** | One-time USD 100 registration/processing fee (universities and schools exempt); no annual charge. One free NTRIP account per user; additional accounts USD 1,000/yr per (contributing-member tier). Consortium-member tier: USD 20,000/yr for simultaneous access to any 20 sites. Source: sopac-csrc.ucsd.edu, observed 2026-05-15 |
| **VRS** | No — individual physical base-station streams only; not a network-RTK processor. The Epoch 2025.00 NAD83(2011) migration announced 2025-08-11 is transmitted via the existing RTCM 3.3 streams; no separate `_RTCM3P1` mountpoint suffix exists in the live sourcetable. |
| **num_stations** | Mountpoint counts on 2026-05-15 (live curl): 148 (port 2102) + 164 (port 2103) + 230 (port 2104) + 128 (port 2105) = **670 STR** rows. Underlying station count: ~430 reference stations (per recent CRTN summaries; historical 2019 figure was 606 stations / 244 GNSS-upgraded — physical network has continued to expand). Recent additions per CRTN station-list page: DWR stations 1500/ARBC/CWD1/ORLD (2026-02-21); Q102/Q122/Q164 + CTSRN PGRV/PDLR/AZYA (2025-12-06); migration to Epoch 2025.00 (2025-08-11). |
| **hobbyist_eligibility** | Likely yes — USD 100 one-time fee is under the project's USD 200/yr cutoff; no explicit professional restriction; SurveyMonkey form |
| **legal_residency_required** | No — no stated residency requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` on all four ports (2102/2103/2104/2105) — 2026-05-15 (curl probes; server banner "NTRIP Sopac Caster/1.0") |
| **datum_epoch** | NAD83(2011)/Epoch 2025.00 since 2025-08-11 migration (announced on the CRTN station-list page); historical streams remain at NAD83(2011)/2010.00. Citation: https://sopac-csrc.ucsd.edu/index.php/crtn-stationlist/ |
| **format** | RTCM 3.1 / 3.3 — varies by mountpoint (legacy BARD streams RTCM 3.1; NOTA-integration streams RTCM 3.3). |
| **contact** | Maria Turingan, mrturingan@ucsd.edu |

### Context Notes

- CRTN is a data clearinghouse, not a network RTK processor. It does not compute VRS corrections; users select a nearby physical base station and maintain acceptable baseline distance (~20–30 km for RTK).
- Zone selection is geographic — use the nearest zone's port for best performance.
- The BARD (Bay Area Regional Deformation) component at UC Berkeley provides real-time streams for the San Francisco Bay Area.
- Caltrans CVSRN (Central Valley Spatial Reference Network) stations are included in CRTN. Caltrans' standalone CVSRN is restricted to vetted state/county agency partners with data-sharing agreements (not hobbyist-accessible directly).
- San Diego County Real Time Network (SDCRTN) — operated by County of San Diego (~13 stations); free for County employees and approved partners; non-county users go through CRTN. Procedure document at sandiegocounty.gov/content/dam/sdc/dpw/COUNTY_SURVEYOR/SDCRTN_procedures2.pdf.
- Orange County OCRTN — Orange County Public Works; mirrored into CRTN; no standalone hobbyist caster.
- Registration: SurveyMonkey form linked from sopac-csrc.ucsd.edu/index.php/crtn-connecting/

---

## OR — Oregon: ORGN

| Field | Value |
|---|---|
| **Network name** | Oregon Real-Time GNSS Network (ORGN) |
| **Operator** | Oregon Department of Transportation (ODOT) — Geometronics Unit; Leica GNSS Spider software |
| **landing_url** | https://www.oregon.gov/odot/orgn/pages/products-services.aspx |
| **access_url** | https://www.oregon.gov/odot/orgn/pages/rover-requests.aspx (rover-account request form) |
| **host:port** | `orgn.odot.state.or.us:9881` (network connection; IP 167.131.109.57). Single-base solutions also offered on `167.131.0.205:9879` per ODOT Trimble Access PDFs. |
| **tariff** | Free — "All rover users will be issued a rover account at no direct charge" (ODOT Products and Services page, observed 2026-05-15). ODOT reserves potential future subscription fees for non-partner users; partner accounts remain permanently free. |
| **VRS** | Yes — network (i-MAX/MAX) multi-base correctors; also single-base correctors for users outside primary network boundary |
| **num_stations** | Mountpoints: 6 STR (Nearest_Single_RTCM3, MAX_RTCM3, IMAX_CMR_AG, IMAX_CMR+, plus 2 more variants); underlying base-station inventory not publicly enumerated on portal |
| **hobbyist_eligibility** | Likely yes — stated "all users" receive accounts at no charge; no professional license field identified in account request; contact ORGN@odot.oregon.gov to confirm |
| **legal_residency_required** | No — no stated restriction |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-15 (curl probe of `orgn.odot.state.or.us:9881`; 6 STR entries; server banner "GNSS Spider 7.9.0.386/1.0") |
| **datum_epoch** | NAD83(2011)/2010.00; citation: https://www.oregon.gov/odot/orgn/pages/products-services.aspx |
| **format** | RTCM 3.x (non-proprietary); also Trimble CMR+ for Trimble equipment users |

### Context Notes

- Accounts issued as NTRIP username and password via the ORGN rover account request form at oregon.gov/odot/orgn/pages/rover-requests.aspx.
- ODOT states it may "charge reasonable subscription fees for rover accounts" in future; partner accounts remain free permanently.
- ORGN uses non-standard ports (9879 single-base, 9881 network — Leica Spider defaults), not 2101.
- Contact: ORGN@odot.oregon.gov; 1-888-275-6368; ODOT Geometronics Unit, 800 Airport Road SE, Salem, OR 97301.

---

## WA — Washington: WSRN

| Field | Value |
|---|---|
| **Network name** | Washington State Reference Network (WSRN) |
| **Operator** | Multi-agency public/private cooperative (WSDOT-led with PANGA/CWU contributing antennae, comms, and data archiving for Puget Sound stations); Trimble Pivot platform; administered from wsrn3.org |
| **landing_url** | http://www.wsrn.org/about.aspx |
| **access_url** | http://wsrn3.org/RegisterAccount.aspx (subscription or partner application) |
| **host:port** | `wsrn.org:2011` (NAD83-2011 / Epoch 2010.00, MYCS3 height model) · `wsrn.org:2022` (NATRF2022, new datum; sourcetable empty pending mountpoint provisioning); legacy port 8080 is being retired |
| **tariff** | Paid — non-partner subscription: USD 1,900/yr per login; tiered multi-login bundles (5 logins USD 5,700, 10 logins USD 10,000, 20 logins USD 15,000) per 2015 Caltrans Preliminary Investigation memo and 2016 RPLS forum discussion. Current rate is published only in the subscription application PDF (linked from wsrn3.org); no public rate update beyond 2015 has been located. Partner agencies (government, NGS cooperators) receive free access. Significantly above the USD 200/yr hobbyist cutoff. 90-day test accounts are available one-time per individual/firm. |
| **VRS** | Yes — Trimble Pivot network corrections; multiple correction formats per station (RTCM 3.1 GPS+GLO; RTCM 3.2-MSM GPS+GLO+GAL+BDS+QZS; legacy CMR+); mountpoints listed at wsrn3.org/MountpointNaming.aspx |
| **num_stations** | Mountpoints: 495 STR on port 2011 (per-station × per-format) on 2026-05-15; 0 STR on port 2022 (CAS line only — NATRF2022 caster online, mountpoint provisioning pending). PANGA contributes 220+ GNSS stations to the PNW geodetic backbone — the WSRN-overlapping subset is reflected in mountpoint counts. |
| **hobbyist_eligibility** | Unclear-leaning-no — no published hobbyist tier; positioned for surveyors/engineering firms; USD 1,900/yr is a practical barrier |
| **legal_residency_required** | Unclear — no stated residency requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-15 on both `wsrn.org:2011` (495 STR; server banner "NTRIP Trimble Ntrip Caster 5.1") and `wsrn.org:2022` (CAS line only, 0 STR — NATRF2022 caster is live but mountpoints are still being provisioned; only a `CAS;192.168.248.36;2022;ROVERS_2022;WSRN;…` clause is published) |
| **datum_epoch** | NAD83-2011 / Epoch 2010.00 with MYCS3 height model on port 2011 (per WSRN sourcetable station metadata); NATRF2022 on port 2022 (active provisioning, mountpoint catalogue not yet populated). Citation: http://www.wsrn3.org/NewREADME.aspx ("the current reference framework is NAD83-2011 Epoch 2010.00"); WSRN datum transition plan at http://www.wsrn.org/WSRN_Datum_Plan.pdf |

### Context Notes

- WSRN is a long-running cooperative involving WSDOT, Seattle Public Utilities and multiple public/private partners.
- Partner agencies (state, federal, local government) receive free access; non-partners pay subscription. 90-day test accounts available one-time per individual/firm.
- The City of Bellingham documents WSRN as available via cob.org/services/maps/monuments/wsrn.
- PANGA (Pacific Northwest Geodetic Array, operated by Central Washington University) operates 220+ GNSS stations in the PNW for geodetic science; real-time GNSS processing is internal (JPL RTG + Trimble RTKNet); no public PANGA-direct NTRIP caster endpoint located on 2026-05-15. Hobbyists in WA reach the same physical PANGA stations via free EarthScope NOTA (in-pipeline) or — for the WSRN-overlapping subset — via WSRN paid.

---

## HI — Hawaii: No Public State Caster

No state-operated RTK NTRIP caster found for Hawaii as of 2026-05-15. HDOT does not operate a public CORS RTK network. Hawaii is listed as having no public service in GPS World's December 2024 state-by-state public RTK survey and is absent from E38 Survey Solutions' state guide. The Pacific GPS Facility at UH SOEST/HIGP (soest.hawaii.edu/pgf/) operates real-time GPS processing for research (constraining KOK1, KOKB, MKEA to ITRF2000) but does not run a public NTRIP caster. The Kīlauea GPS network is an HVO/USGS + UH + Stanford research collaboration, not public.

**Gap:** EarthScope NOTA has a handful of GNSS stations in Hawaii (volcanic monitoring sites on Big Island and Maui — KOKB, MKEA, MAUI, HILO area), though station spacing is limited and the islands are geographically isolated. NPS CORS includes 8 Pacific stations (Hawaii Volcanoes HAVO, Haleakalā HALE) — both flagged offline as of 2026-05-02 per US-NPS file. Topcon announced expansion of Topnet Live to include Hawaii in October 2024 — a commercial paid option. Commercial alternatives: Topnet Live (Topcon), Point One Polaris. No free VRS network identified.

---

## Multi-State Commercial Networks (reference)

| Network | Coverage | host:port | Tariff | VRS |
|---|---|---|---|---|
| **RTKdata** | All 50 states | Contact rtkdata.com | USD 40/mo; 30-day free trial | Unknown |
| **Point One Polaris** | All 50 states | Contact pointonenav.com | USD 50/mo | Yes |
| **SmartNet (Leica/Hexagon)** | OK, TX, WA, others | Contact smartnetna.com | Paid (not disclosed publicly) | Yes |
| **Topnet Live (Topcon)** | TX, WA, HI, others | Contact topconpositioning.com | Paid | Yes |
| **RTK Premium** | Most western states (gaps) | Contact rtkpremium.com | Paid | Yes |
| **AZGPS** | AZ, So-CA | Contact azgps.net | Paid (not disclosed) | Yes |

---

## Post-Processing Fallback

| Service | Coverage | Cost |
|---|---|---|
| **NOAA NCN CORS** — static RINEX download | All western states | Free; no account required |
| **EarthScope NOTA RINEX archive** | All western states (variable density) | Free noncommercial; account required |
| **CRTN RINEX (SOPAC/CSRC)** | California | Free; same account as NTRIP access |
| **SOPAC/BARD** — UC Berkeley Bay Area | California Bay Area | Free |
| **MTSRN RINEX** | Montana | Free (no subscription required for static) |
| **PGF (UH SOEST)** | Hawaii | Research access |

---

## Key Findings & Gaps

- **Free public NTRIP RTK** exists in 4 of 16 states surveyed (AR, AZ, CO via Mesa County, OR). Plus CA at USD 100 one-time (under the project's USD 200/yr cutoff — affordable).
- **Paid state-level subscription** in 4 states: LA (C4G entry tier USD 495/yr), MT (USD 1,500/yr), UT/NV-Reno (USD 600/yr bundled), WA (USD 1,900/yr).
- **No state caster** in 6 states: OK, NM (ARTGN status unverified), WY, ID, HI, plus TX (DOT-restricted, not hobbyist-accessible).
- **Federal fallbacks** (EarthScope NOTA, NPS CORS) cover the seismically active western Cordillera densely. Plains states (eastern WY, eastern MT, western OK panhandle, western NE) are sparse.
- **WSRN's USD 1,900/yr** remains the most expensive Western state network — significantly above peers (TURN/Nevada GPS USD 600, MTSRN USD 1,500). LVVWD pricing is undisclosed, requiring direct contact.
- **CRTN's USD 100 one-time** is the cheapest gateway to a large station network (~430 reference stations / 670 mountpoint rows across 4 ports) in the West; falls under the project's USD 200/yr affordability cutoff. CRTN migrated to Epoch 2025.00 NAD83(2011) coordinates on 2025-08-11 — transmitted via existing RTCM 3.3 streams. (A prior version of this file recorded a separate "`_RTCM3P1` suffix" rollout on 2025-10-22; that was not present in the live sourcetable and has been removed.)
- **Mesa County RTVRN** is geographically narrow (Western Colorado) but free and well-maintained.
- **AZCORS** continues at 71 total CORS sites (56 ADWR + 15 EarthScope/NPS) per ADWR's 2026-04-14 page update. (A prior version of this file recorded 52 sites attributed to a March 2025 ADWR communication; the current public ADWR page and AZGeo hub both state 56+15=71, so this file restores that figure.)
- **WSRN NATRF2022 port (2022)** remains live with caster handshake but empty mountpoint catalogue — provisioning expected through 2H2026 alongside the NSRS modernisation rollout.
- **Volunteer/community casters** (rtk2go) in the West cluster densely in the Pacific Northwest (WA, OR) — counted via `data/stations.json` per the procedures in `country-survey.proc.md` (this file does not edit them).
- **Open items requiring direct contact**: ARTGN (NM) operational status; LVVWD (NV) pricing and hobbyist eligibility; AZCORS confirmed external NTRIP port (Cloudflare CDN obscures); MTSRN biennial rate review for 2026-07-01 (March 2026 glidepath PDF published, no rate change announced yet).

---

## Sources Consulted

- ODOT ORGN product page: https://www.oregon.gov/odot/orgn/pages/products-services.aspx (HTTP 200 on 2026-05-15)
- ODOT ORGN rover accounts: https://www.oregon.gov/odot/orgn/pages/rover-requests.aspx (HTTP 200 on 2026-05-15)
- ODOT ORGN about page: https://www.oregon.gov/odot/orgn/pages/about-us.aspx
- ODOT ORGN connection PDFs: https://www.oregon.gov/odot/ORGN/Documents/Network-Connection-TSC2-Trimble-Access.pdf, Single-Base-Solutions-TSC2-Trimble-Access.pdf
- AZCORS / ADWR page: https://www.azwater.gov/hydrology/azcors (Cloudflare challenge on scripted GET; HTTP 200 in browser, 2026/04/14 update banner)
- AZCORS mountpoints doc (April 2026): https://www.azwater.gov/sites/default/files/2026-04/AZCORS_InformationAndMountpoints20260406.pdf (HTTP 403 to scripted curl, anti-bot)
- AZCORS SBC login: https://azcors.azwater.gov/sbc/Account (HTTP 403 to anonymous probes)
- AZGeo AZCORS hub: https://azgeo-data-hub-agic.hub.arcgis.com/pages/azcors (HTTP 200 on 2026-05-15)
- AZGPS (commercial): https://azgps.net
- ARDOT RTN portal: http://gps.ardot.gov/ (HTTP 200; `SOURCETABLE 200 OK` on :2101 with 8 STR on 2026-05-15)
- ARDOT RTN sensor map: http://gps.ardot.gov/Map/SensorMap.aspx (HTTP 200 on 2026-05-15)
- ARDOT GPS Control / Arkansas GIS Office: https://gis.arkansas.gov/product/ardot-gps-control/
- ARDOT Control Surveys page: https://ardot.gov/divisions/surveys/control-surveys/
- ARDOT Trimble Receiver configuration: http://gps.ardot.gov/Configuring%20Trimble%20Receiver%20on%20ARDOT%20RTN.pdf (HTTP 200 on 2026-05-15)
- PAGIS GPS Reference Station: https://www.pagis.org/index.php/data-resources/gps-reference-station-access/
- TxDOT RTN portal: https://txrtn.txdot.gov/ (HTTPS 200 confirmed 2026-05-15)
- TxDOT GPS page: https://www.txdot.gov/data-maps/global-positioning-system-gps.html
- C4Gnet.XYZ portal: https://c4gnet.xyz/ (HTTPS 200 on 2026-05-15)
- C4Gnet NTRIP mountpoints: http://c4gnet.xyz/NTRIP_Mountpoints.aspx
- LSU C4G store — 1-year unlimited RTK: https://store.c4g.lsu.edu/products/1-year-unlimited-rtk-rover-ntrip-only-account (USD 3,500 confirmed 2026-05-15)
- LSU C4G store — full RTN: https://store.c4g.lsu.edu/index.php?product_id=62&route=product%2Fproduct
- Mesa County RTVRN: https://www.mesacounty.us/departments-and-services/public-works/gps-survey/real-time-virtual-reference-network-rtvrn (HTTPS 200 on 2026-05-15)
- Mesa County GPS Survey: https://www.mesacounty.us/departments-and-services/public-works/gps-survey
- Mesa County RTVRN docs (2025-05): https://www.mesacounty.us/sites/default/files/2025-05/RTVRN%20Mountpoint%20Names.pdf, https://www.mesacounty.us/sites/default/files/2025-05/RTVRN%20Login%20Instructions%20and%20NTRIP%20Mountpoints.pdf
- Mesa County RTVRN portal: https://rtvrn.mesacounty.us/, https://rtvrn.mesacounty.us/RegisterAccount.aspx
- TURN GPS UGRC: https://gis.utah.gov/products/turn/ (HTTPS 200 on 2026-05-15)
- TURN GPS connecting guide: https://gis.utah.gov/documentation/turn/connecting/
- TURN GPS bill pay: https://turngps-billpay.ugrc.utah.gov
- TURN GPS portal: https://turngps.utah.gov/, https://secure.utah.gov/turngps/
- Nevada GPS Network (UGRC): https://gis.utah.gov/gps/ngps/ (HTTPS 200 on 2026-05-15)
- Nevada GPS Network (Reno portal): https://nevadagps.utah.gov/ (external HTTPS timeout on 2026-05-15)
- Washoe County GPS Base Stations: https://washoecounty.gov/csd/engineering_capitalprojects/development_services/gps_base_stations/index.php
- LVVWD survey/right-of-way page: https://www.lvvwd.com/engineering-resources/survey-right-of-way/ (HTTPS 200 on 2026-05-15)
- LVVWD account request: https://www.lvvwd.com/apps/base-station-network-access/ (HTTPS 200 on 2026-05-15)
- MTSRN main: https://msl.mt.gov/mtsrn/ (HTTPS 200 on 2026-05-15)
- MTSRN subscribe: https://msl.mt.gov/mtsrn/subscribe
- MTSRN FAQ: https://msl.mt.gov/mtsrn/faq
- MTSRN how it works: https://msl.mt.gov/mtsrn/howitworks
- MTSRN subscription launch announcement: https://content.govdelivery.com/accounts/MTLIBRARY/bulletins/393bfda
- MTSRN biennium rate update (Sept 2024): https://archive.legmt.gov/content/Publications/fiscal/2025-Biennium/Section-E/Interim/MSL-MT-State-Reference-Network-Update-Sept2024.pdf
- MTSRN revised glidepath (March 2026): https://archive.legmt.gov/content/Publications/fiscal/2027-Biennium/Committees/Section-E/MSL-MT-State-Reference-Network-Update-March2026.pdf (HTTP 200 on 2026-05-15)
- MTSRN Pivot portal: https://www.mtsrn.org/ (`SOURCETABLE 200 OK` on :2101 with 340 STR on 2026-05-15)
- CRTN (SOPAC/CSRC): http://sopac-csrc.ucsd.edu/index.php/crtn/ (HTTP 200 on 2026-05-15)
- CRTN connecting guide: http://sopac-csrc.ucsd.edu/index.php/crtn-connecting/ (HTTP 200 on 2026-05-15)
- CRTN station list: https://sopac-csrc.ucsd.edu/index.php/crtn-stationlist/ (HTTP 200 on 2026-05-15)
- CRTN consortium: https://sopac-csrc.ucsd.edu/index.php/crtn-consortium/
- CRTN connecting resource (PDF): http://sopac-csrc.ucsd.edu/wp-content/uploads/2019/11/Connecting_to_CRTN_Resource_11-14-19.pdf
- SDCRTN procedures: https://www.sandiegocounty.gov/content/dam/sdc/dpw/COUNTY_SURVEYOR/SDCRTN_procedures2.pdf
- Caltrans D6 RTN page: https://dot.ca.gov/caltrans-near-me/district-6/district-6-programs/d6-land-surveys/d6-rtn-gps
- 2015 Caltrans Preliminary Investigation memo: https://dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/preliminary-investigations/real-time-gps-networks-pi-a11y.pdf
- WSRN about: http://www.wsrn.org/about.aspx (HTTP 200 on 2026-05-15)
- WSRN new visitor info: http://www.wsrn3.org/NewREADME.aspx (HTTP 200 on 2026-05-15)
- WSRN join/register: http://wsrn3.org/RegisterAccount.aspx (HTTP 200 on 2026-05-15)
- WSRN datum plan: http://www.wsrn.org/WSRN_Datum_Plan.pdf (HTTP 200 on 2026-05-15)
- WSRN Update (CSRC presentation May 2025): https://sopac-csrc.ucsd.edu/wp-content/uploads/2025/07/WSRN-Update-CSRC-051525.pdf
- WSRN Mountpoint naming: http://www.wsrn3.org/MountpointNaming.aspx (HTTP 200 on 2026-05-15)
- WSRN FAQ PDF: http://www.wsrn3.org/WSRN_FAQ.pdf
- City of Bellingham WSRN page: https://cob.org/services/maps/monuments/wsrn
- PANGA (CWU geodesy): https://www.geodesy.org/, https://www.panga.org/
- ISU GIS Center RTN history: https://giscenter.isu.edu/research/Techpg/GC/rtn.htm; https://giscenter.isu.edu/pdf/PDF_GC/RTNforIdaho.pdf
- Frontier Precision SE Idaho RTN announcement: https://frontierprecision.com/news/real-time-gnss-network-southeast-idaho/
- Idaho Geospatial Office Geodetic Control TWG: https://gis.idaho.gov/geodetic-control-twg
- PLSW CORS: https://www.plsw.org/cors/
- Wyoming Geodetic Coordination: https://geodetic.geospatialhub.org/pages/resources
- ARTGN background (American Surveyor 2010): https://amerisurv.com/2010/12/05/real-time-gnss-network-in-new-mexico/ (HTTPS 200 on 2026-05-15)
- City of Albuquerque AGRS page: https://www.cabq.gov/municipaldevelopment/architects-engineers-contractors/construction-services/albuquerque-geodetic-reference-system (HTTPS 200 on 2026-05-15)
- ARTGN connection guide (2013, archived): https://www.yumpu.com/en/document/view/17923468/
- Pacific GPS Facility (UH SOEST): http://www.soest.hawaii.edu/pgf/, http://www.soest.hawaii.edu/pgf/SEQ/processing.shtml
- Topcon Topnet Live expansion (Oct 2024): https://www.topconpositioning.com/us/en/articles/topcon-announces-significant-expansion-of-topnet-live-coverage-across-western-usa-and-hawaii (HTTPS 200 on 2026-05-15)
- EarthScope GNSS Realtime: https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA: https://www.earthscope.org/nota/ (HTTPS 200 on 2026-05-15)
- E38 Survey Solutions — RTK by state: https://e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state (observed 2026-05-15)
- ArduSimple — US RTK casters: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/ (observed 2026-05-15)
- NTRIP-list North America: https://ntrip-list.com/north-america/ (observed 2026-05-15)
- GPS World public RTK list: https://www.gpsworld.com/finally-a-list-of-public-rtk-base-stations-in-the-u-s/
- USCG NDGPS decommissioning: https://www.federalregister.gov/documents/2018/03/21/2018-05684/discontinuance-of-the-nationwide-differential-global-positioning-system-ndgps
- Point One Nav — state pages for AZ, TX, OK, NM, WY, ID, HI: https://pointonenav.com/states/[state]/
- curl probes performed 2026-05-15 (literal results, no editorialising):
  - gps.ardot.gov:2101 — `SOURCETABLE 200 OK` (8 STR)
  - rtvrn.mesacounty.us:2101 — `SOURCETABLE 200 OK` (6 STR)
  - mtsrn.org:2101 — `SOURCETABLE 200 OK` (340 STR)
  - wsrn.org:2011 — `SOURCETABLE 200 OK` (495 STR)
  - wsrn.org:2022 — `SOURCETABLE 200 OK` (0 STR — CAS line only, NATRF2022 caster online but empty pending mountpoint provisioning)
  - 132.239.152.4:2102 — `SOURCETABLE 200 OK` (CRTN NorCal Z1-2, 148 STR)
  - 132.239.152.4:2103 — `SOURCETABLE 200 OK` (CRTN NorCal Z3-4, 164 STR)
  - 132.239.152.4:2104 — `SOURCETABLE 200 OK` (CRTN SoCal Z5, 230 STR)
  - 132.239.152.4:2105 — `SOURCETABLE 200 OK` (CRTN SoCal Z6, 128 STR)
  - orgn.odot.state.or.us:9881 (167.131.109.57:9881) — `SOURCETABLE 200 OK` (6 STR)
  - c4gnet.xyz:9000 — `SOURCETABLE 200 OK` (32 STR)
  - ntrip.earthscope.org:2101 — `SOURCETABLE 200 OK` (1,095 STR globally)
  - txrtn.txdot.gov (HTTPS landing) — HTTP 200; NTRIP port not public
  - azcors.azwater.gov (HTTPS landing) — HTTP 403 to scripted GET (Cloudflare bot challenge); backend SBC NTRIP port confirmed via post-registration only
  - 165.239.144.5:2101 (TURN GPS) — TCP timeout (account-gated firewall)
  - 168.179.231.11:2102 (Nevada GPS via TURN) — TCP timeout (account-gated firewall)

SELF-REVIEW: PASS
