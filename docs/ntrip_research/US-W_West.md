# US West & Southwest [US-W] — NTRIP RTK Caster Research

**States:** TX, OK, AR, LA, NM, AZ, CO, UT, NV, WY, MT, ID, CA, OR, WA, HI

## Status (region)

Free public: AR (ARDOT), AZ (AZCORS), CO (Mesa County RTVRN), OR (ORGN). Paid: LA (C4Gnet entry USD 495/yr), UT/NV-Reno (TURN GPS USD 600/yr bundled), MT (MTSRN USD 1,500/yr), WA (WSRN USD 1,900/yr). TX restricted DOT-only. OK, NM, ID, HI, WY have no state caster. CA (CRTN) one-time USD 100 fee (under hobbyist threshold). EarthScope NOTA + NPS CORS = free single-base fallback region-wide.

## Per-state summary

| State | Free public caster | Network | host:port | VRS | Hobbyist | Probe |
|---|---|---|---|---|---|---|
| TX | No (DOT-restricted) | TxDOT RTN | `txrtn.txdot.gov` (port not public) | Yes | No — employees/contractors only | Portal HTTPS 200; NTRIP not published |
| OK | No | — | — | — | — | No state caster |
| AR | Yes (free) | ARDOT RTN | `gps.ardot.gov:2101` | Yes | Likely yes | OK 8 STR |
| LA | Paid | C4Gnet (LSU C4G) | `c4gnet.xyz:9000` | Yes | Unclear | OK 32 STR |
| NM | No | — | — | — | — | No state caster; ARTGN status undocumented post-2010 |
| AZ | Yes (free) | AZCORS | `azcors.azwater.gov` (SBC; port post-registration) | Yes | Yes (explicit) | Portal Cloudflare-gated |
| CO | Yes (free) | Mesa County RTVRN | `rtvrn.mesacounty.us:2101` | Yes | Likely yes | OK 6 STR |
| UT | Paid | TURN GPS | `165.239.144.5:2101` | Yes | Yes (Utah ID required, no residency) | TCP timeout (account-gated) |
| NV (north) | Paid | Nevada GPS Network (via TURN) | `168.179.231.11:2102` (HARN), `165.239.144.7:2101` (2011) | Yes | Yes (TURN bundle) | TCP timeout |
| NV (LV) | Paid (LV metro) | LVVWD GPS Network | host n/p, port `9899` | No (single-base) | Unclear | Application-gated |
| WY | No | — | — | — | — | No state caster; TURN GPS partial edge |
| MT | Paid | MTSRN | `mtsrn.org:2101` | Yes | Unclear | OK 340 STR |
| ID | No | — | — | — | — | No state caster; TURN GPS edge |
| CA | Fee USD 100 one-time | CRTN (SOPAC/UCSD) | `132.239.152.4:2102–2105` | No | Likely yes | OK 677 STR total |
| OR | Yes (free) | ORGN (ODOT) | `orgn.odot.state.or.us:9881` | Yes | Likely yes | OK 6 STR |
| WA | Paid | WSRN | `wsrn.org:2011` (NAD83-2011) + `wsrn.org:2022` (NATRF2022) | Yes | Unclear-leaning-no | OK 492 STR (2011) + 0 STR (2022, CAS-only) |
| HI | No | — | — | — | — | No state caster |

## Regional baselines

**EarthScope NOTA** — see `US-NOTA_NetworkOfTheAmericas.md`. West is NOTA's densest US region (PBO heritage in WA/OR/CA/NV/UT/AZ/MT/WY/ID/CO/NM); ~600+ stations in Cordillera. Per-state lookup `py scripts/stations_by_country.py US --source earthscope`.

**NPS CORS** — see `US-NPS_NationalParkService.md` (`rtk.nps.gov:2101`, manual provisioning, free, single-base, 142 STR 2026-05-18). Western parks: Yosemite, Yellowstone, Grand Canyon, Glacier, Olympic, Crater Lake, Death Valley, Joshua Tree, Bryce, Zion, Sequoia; Pacific: Hawaii Volcanoes (HAVO), Haleakalā (HALE). AZ AZCORS aggregates 15 EarthScope+NPS sites into its 71-station total; CA CRTN integrates NPS via NOTA pipeline; HI's only Pacific CORS density = NPS HAVO/HALE + NOTA volcanic stations.

## TX — TxDOT RTN (restricted access)

| Field | Value |
|---|---|
| Network | TxDOT Real Time Network |
| Operator | TxDOT Information Systems Division |
| landing_url | https://txrtn.txdot.gov/ |
| access_url | https://txrtn.txdot.gov/ (employees/contractors only) |
| host:port | `txrtn.txdot.gov` — port not publicly documented; NTRIP endpoint not disclosed |
| tariff | No charge — access restricted, not sold |
| vrs | Yes — network VRS |
| num_stations | 256 (one per TX county) |
| hobbyist_eligibility | No — restricted to TxDOT employees + contractors/consultants on TxDOT-funded projects |
| legal_residency_required | N/A (restricted) |
| last_confirmed_alive | Portal HTTPS 200 2026-05-18; sensor map at txrtn.txdot.gov/Map/SensorMap.aspx |
| datum_epoch | omitted — no operator-declared datum doc publicly accessible (TxDOT RTN portal is employees/contractors only). Prior value "NAD83(2011)/2010.00" was educated inference from generic Texas State Plane / NGS practice, not a TxDOT-declared frame for this caster; per primer [datum-epoch] (no operator declaration → omit), removed |

One of largest state CORS networks in country (256 stations, all 254 counties) but not opened to public. No public registration. Practical fallback: EarthScope NOTA (sparse), commercial (RTKdata, Point One, SmartNet).

## OK — no public state caster

ODOT does not operate public CORS RTK. Multiple sources (E38, Point One, GPS World) confirm "no public service".

Commercial: SmartNet Oklahoma (Leica; OKC + Tulsa), RTKdata (USD 40/mo, claimed statewide), Point One Polaris. EarthScope NOTA sparse in western OK. Nearest dense free RTN: ARDOT (`gps.ardot.gov:2101`) reachable from eastern OK within ~50 km of AR border.

## AR — ARDOT RTN

| Field | Value |
|---|---|
| Network | Arkansas Continuously Operating Reference Station Network / ARDOT RTN |
| Operator | ARDOT Surveys Division; Trimble Pivot |
| landing_url | http://gps.ardot.gov/ |
| access_url | http://gps.ardot.gov/Login.aspx (self-service Trimble Pivot) |
| host:port | `gps.ardot.gov:2101` (199.48.3.12) |
| tariff | Free |
| vrs | Yes — Trimble Pivot VRS; `ARDOT_RTX_CMRp/CMRx/RTCM31/RTCM34` (network solutions) + `MS_CMRp/CMRx/RTCM31/RTCM34` (Nearest Single Base) |
| num_stations | Unknown — physical CORS count not publicly enumerated; ARDOT cites "GNSS CORS stations aligned with NGS NSRS" without count. Mountpoints: 8 STR (multi-format variants over fewer physical bases — 4 NSB + 4 VRS combinations) |
| hobbyist_eligibility | Likely yes — self-service portal; no professional licence; no published restriction |
| legal_residency_required | Unclear — no stated requirement |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (8 STR; Trimble Caster 5.2) |
| datum_epoch | NAD83(2011)/2010.00 — stated on ARDOT Control Surveys page (aligned with NGS NSRS). Citation: https://ardot.gov/divisions/surveys/control-surveys/ (live via browser UA per 2026-05-18 re-probe; HTTP 200) |

Sensor map: http://gps.ardot.gov/Map/SensorMap.aspx. Trimble config guide: http://gps.ardot.gov/Configuring%20Trimble%20Receiver%20on%20ARDOT%20RTN.pdf.

**PAGIS (Pulaski Area GIS)** — supplementary single-base in North Little Rock / Little Rock / Pulaski County AR; free; signed UA; NTRIP address post-registration; pagis.org 501.377.1264. Single station, not VRS network; usable within ~300 km / 185 mi.

## LA — C4Gnet (LSU Center for GeoInformatics)

| Field | Value |
|---|---|
| Network | C4Gnet — Louisiana Statewide Real Time Network |
| Operator | LSU Center for GeoInformatics (C4G) |
| Software | Trimble Pivot (NTRIP Trimble Caster 5.2) |
| landing_url | https://c4gnet.xyz/ |
| access_url | https://store.c4g.lsu.edu/ (paid) |
| host:port | `c4gnet.xyz:9000` |
| tariff | Paid — 10-hr RTK USD 495/yr; 50-hr RTK USD 1,995/yr; 1-yr unlimited RTK (NTRIP only) USD 3,500; Full RTN membership USD 5,000/yr; GIS DGPS unlimited USD 995/yr; AG GNSS unlimited USD 1,500/yr; RINEX 1-sec data USD 1,500/yr. Source: store.c4g.lsu.edu fetched 2026-05-18 |
| vrs | Yes — VRS and Nearest Single Base (NSB) mountpoints (RTCM 3.2-MSM, CMR+, CMRx); RTCM3 banner GPS+GLO+GAL+BDS. PPP mountpoints present but out of scope per primer [scope] |
| num_stations | Unknown — physical CORS inventory not publicly enumerated; mountpoints 32 STR (mix VRS/NSB/PPP across formats + reference frames; only VRS+NSB in scope) |
| hobbyist_eligibility | Unclear — no explicit restriction; entry USD 495/yr above hobbyist USD 200/yr threshold |
| legal_residency_required | Unclear |
| last_confirmed_alive | 2026-05-18 — `c4gnet.xyz:9000` `SOURCETABLE 200 OK` (32 STR; Trimble Caster 5.2) |
| datum_epoch | NAD83(2011) Epoch 2010.00 (primary, mountpoint suffix `..._NAD83`) — operator landing (c4gnet.xyz fetched 2026-05-18): "Current NGS Reference Frame is NAD 83 (2011) Epoch 2010.00 for the conterminous U.S." For ITRF product: **operator landing page text still names "IGS08 epoch 2005.00"** as the ITRF reference, but live sourcetable (2026-05-18) advertises *both* **ITRF2014** mountpoints (`PPP_GNSS_CMRx_ITRF2014`, `PPP_GNSS_RTCM3_2_ITRF2014`) *and* **ITRF2020** mountpoints (`PPP_GREC_CMRx_ITRF2020`, `PPP_GREC_RTCM3_4_ITRF2020`) — neither matches the IGS08 named on the landing. Landing page stale vs broadcast on ITRF; PPP product carries dual ITRF realisations side-by-side. Confirm via `rosbor1@lsu.edu` or `vdubinin@lsu.edu` before survey-grade ITRF use. Geoid: GEOID18. Citations: https://c4gnet.xyz/, http://c4gnet.xyz/NTRIP_Mountpoints.aspx, live ST `c4gnet.xyz:9000` 2026-05-18 |

Network established 2007. Mountpoint naming: `TYPE_SATS_FORMAT_REFERENCEFRAME` (e.g. `GLN_RTCM3_2`, `PPP_GNSS_CMRp_NAD83`). Free RINEX subscription separate; contact `rosbor1@lsu.edu` or `vdubinin@lsu.edu`.

## NM — no confirmed public state caster

No state-operated RTK NTRIP caster confirmed operational for NM 2026-05-18. NMDOT does not operate public CORS RTK. GPS World, E38, Point One do not list NM as having public service.

**Historic ARTGN (Albuquerque Real-Time GNSS Network):** Launched 2007 by City of Albuquerque as paid subscription ~USD 200/mo (Dec 2010 American Surveyor article); served AGRS ~800-monument framework. Post-2013 operational status undocumented online — no press releases, municipal updates, or operator page surfaced. City of Albuquerque AGRS page (cabq.gov/municipaldevelopment/.../albuquerque-geodetic-reference-system) makes no current ARTGN reference. ARTGN connection guide (Yumpu mirror, 2013) is latest accessible doc. To confirm operational status contact City Surveyor 505-768-3614 / Construction Services Division — phone contact not attempted in this research; operational status remains undocumented.

Commercial: RTKdata (USD 40/mo, claims statewide NM), Point One Polaris, RTK Premium. EarthScope NOTA stations in NM (moderate density along Rio Grande Rift); useful for PPK + possibly single-base RTK near TUCUMCARI, PIETOWN, WHITE SANDS. Cross-border within ~50 km: AZCORS (free) reachable from western NM.

## AZ — AZCORS

| Field | Value |
|---|---|
| Network | Arizona CORS Network (AZCORS) — implements AZHMP (Arizona Height Modernization Program) |
| Operator | Arizona Dept of Water Resources (ADWR) — Leica SBC |
| landing_url | https://www.azwater.gov/hydrology/azcors |
| access_url | https://azcors.azwater.gov/sbc/Account/Register (self-service) |
| host:port | `azcors.azwater.gov:2101` (Leica SBC default) — external probe gated by Cloudflare CDN; NTRIP TCP socket reachable only post-provisioning. Pipeline `azcors` source = error/timeout state (data/source_health.json); anonymous probe firewalled; caster documented active per April 2026 ADWR materials |
| tariff | Free — ADWR explicit: "free access to all Real Time and RINEX Data Products in the AZCORS network". Open-data policy |
| vrs | Yes — Leica SBC supports iMAX/MAX network solutions; full mountpoint list post-registration |
| num_stations | "71 total: 56 ADWR-managed + 15 ingested from EarthScope + NPS" — figure attributed to ADWR landing page in prior research, **not re-verifiable from sandbox 2026-05-18 (azwater.gov returns HTTP 403 to scripted probes; PDF AZCORS_InformationAndMountpoints20260406.pdf also 403)**. Whether the 71/56/15 breakdown originates from the (reachable in browser) landing text or from the (unreachable) PDF is unclear from current research state — flag as unverified pending in-browser re-check |
| hobbyist_eligibility | Yes — open registration; no professional licence required; "AZCORS is open to any users with an open-data policy" |
| legal_residency_required | No — no stated requirement |
| last_confirmed_alive | ADWR AZCORS landing active (Cloudflare challenge for scripted GETs; HTTP 200 in browser; last update banner 2026/04/14). ArduSimple US RTK list also lists AZCORS as free public |
| datum_epoch | omitted — citation chain unverified from sandbox 2026-05-18: AZCORS_InformationAndMountpoints20260406.pdf returns HTTP 403 (anti-bot, no UA-swap or wayback bypass); ADWR landing https://www.azwater.gov/hydrology/azcors also HTTP 403. Prior value "NAD83(2011)/2010.00" carried from earlier research without a re-validated operator citation; per primer [datum-epoch] (declared only, not inferred, no operator declaration → omit), value omitted until operator page can be confirmed in-browser. Pointer: PDF filename pattern suggests datum content but is not a fetchable citation |

ADWR operates two virtual servers for redundancy. Information + mountpoints PDF (2026-04-06): https://www.azwater.gov/sites/default/files/2026-04/AZCORS_InformationAndMountpoints20260406.pdf. Also: https://azgeo-data-hub-agic.hub.arcgis.com/pages/azcors. AZCORS incorporates EarthScope + NPS stations for broad statewide coverage incl. remote desert / canyon country. AZHMP (Arizona Height Modernization Program) is the umbrella program; AZCORS is its CORS implementation (listed separately on NGS state-provider FAQ as "Arizona Height Mod Program (AZHMP)" but operationally identical).

Commercial alternative: AZGPS (azgps.net) — paid VRS network covering AZ + southern CA; founded Nov 2004, ~100+ sites; pricing not publicly listed.

## CO — Mesa County RTVRN

| Field | Value |
|---|---|
| Network | Real-Time Virtual Reference Network (RTVRN) |
| Operator | Mesa County CO — Public Works Department, GPS Survey |
| Software | Trimble Pivot (NTRIP Trimble Caster 5.3) |
| landing_url | https://www.mesacounty.us/departments-and-services/public-works/gps-survey/real-time-virtual-reference-network-rtvrn |
| access_url | https://rtvrn.mesacounty.us/RegisterAccount.aspx (self-service) |
| host:port | `rtvrn.mesacounty.us:2101` (35.131.54.14) |
| tariff | Free — "a free service to the public" |
| vrs | Yes — 6 VRS mountpoints: `VRS_CMR`, `VRS_CMRx`, `VRS_RTCMv3`, `VRS_CMR_RTX`, `VRS_CMRx_RTX`, `VRS_RTCMv3_RTX`. RTX_* variants = GPS+GLO+GAL+BDS; legacy = GPS+GLO (operator PDF, 2025-05) |
| num_stations | 6 STR (all VRS variants); 33 base stations contribute, 17 of those are NGS CORS (per "RTVRN Login Instructions and NTRIP Mountpoints" PDF, 2025-05) |
| hobbyist_eligibility | Likely yes — public service; no stated restriction; serves "surveying, construction, agriculture, mapping, and science industries" |
| legal_residency_required | No — no stated restriction |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (6 STR; Trimble Caster 5.3) |
| datum_epoch | NAD83(2011); epoch omitted — same "RTVRN Login Instructions and NTRIP Mountpoints" PDF (2025-05) was read for station count + datum but contains no epoch declaration (PDF re-extracted via pdftotext 2026-05-18: mountpoint table + format notes only, no epoch text). RTVRN portal also silent on epoch. Datum citation: https://www.mesacounty.us/sites/default/files/2025-05/RTVRN%20Login%20Instructions%20and%20NTRIP%20Mountpoints.pdf |

Login format: `organization/username` (e.g. `ABC surveying/ABC1`). Coverage centred Western CO (Grand Junction / Mesa County); 33-station network reaches western CO and edges into adjacent UT and WY — extent of UT/WY overlap not enumerated by operator; likely 10-30 km cross-border (single-base RTK threshold) rather than full state-wide coverage. Only confirmed free public VRS network in CO; CDOT does not operate public RTK caster.

## UT — TURN GPS

| Field | Value |
|---|---|
| Network | Utah Reference Network (TURN GPS) |
| Operator | Utah Geospatial Resource Center (UGRC); Trimble Pivot VRS |
| landing_url | https://gis.utah.gov/products/turn/ |
| access_url | https://turngps-billpay.ugrc.utah.gov/ (subscription via Utah ID) |
| host:port | `165.239.144.5:2101` (NAD83/2011); alt `165.239.144.7:2101` |
| tariff | Paid — USD 600/yr per login; bundles TURN Utah + Nevada GPS access (gis.utah.gov/documentation/turn/connecting/: "Each subscription costs $600 for one year") |
| vrs | Yes — Trimble Pivot VRS; recommended `GNSS-VRS-NAD83-RTCM32` (GPS+GLO+GAL+BDS); also `VRS-NAD83` variants CMRp/CMRx/RTCM31/RTCM32; nearest-base `MS-` prefixed |
| num_stations | "Over 100 permanently located GPS receivers" (operator); statewide UT + portions southern ID, western WY, southern NV |
| hobbyist_eligibility | Yes — subscription requires Utah ID; no professional licence required |
| legal_residency_required | No — Utah ID = state digital identity, not residency; non-residents can register |
| last_confirmed_alive | TCP timeout external 2026-05-18 (consistent with account-gated firewall); turngps.utah.gov HTTPS 200 |
| datum_epoch | NAD83(2011)(EPOCH 2010.0000) — operator explicit on connecting page: "NAD83(2011)(EPOCH:2010.0000.)". Citation: https://gis.utah.gov/documentation/turn/connecting/ |

State-managed paid service, not commercial vendor. Registration: turngps.utah.gov → create Utah ID → subscribe at turngps-billpay.ugrc.utah.gov. Constellations: GPS+GLO+GAL+BDS via RTCM3.2.

## NV — multiple operators

### Nevada GPS Network (UGRC; Reno / northern NV)

| Field | Value |
|---|---|
| Network | Nevada GPS Network (formerly Washoe County GPS / NNCRN) |
| Operator | UGRC — administered jointly; historically Washoe County NV |
| landing_url | https://nevadagps.utah.gov/ — operator Nevada GPS portal (Reno area; UGRC-managed). Prior cite `https://gis.utah.gov/gps/ngps/` HTTP 301 → `https://gis.utah.gov/products/turn/` (TURN-only page covering "Utah and portions of Idaho, Wyoming, and southern Nevada" — does not address the Reno-area Nevada GPS Network) 2026-05-18; ngps slug no longer routes to a Nevada-specific page |
| access_url | https://nevadagps.utah.gov/ (subscription via TURN bundle; same Utah ID) |
| host:port | `168.179.231.11:2102` (NAD83/HARN legacy); `165.239.144.7:2101` (NAD83/2011) |
| tariff | Paid — USD 600/yr bundled with TURN GPS UT; same Utah ID |
| vrs | Yes — Trimble Pivot (shared with TURN) |
| num_stations | Reno / Washoe County area; not statewide — southern NV and Las Vegas not covered |
| hobbyist_eligibility | Yes — same as TURN |
| legal_residency_required | No — same as TURN |
| last_confirmed_alive | nevadagps.utah.gov HTTPS timeout external 2026-05-18; gis.utah.gov/gps/ngps/ HTTP 301 → gis.utah.gov/products/turn/ (TURN-only landing, no NV-specific content); 168.179.231.11:2102 TCP timeout |
| datum_epoch | NAD83(2011)/2010.0000 on `165.239.144.7:2101`; legacy NAD83/HARN (NAD83/94 HARN) on `168.179.231.11:2102`. Citation: https://gis.utah.gov/documentation/turn/connecting/ |

### LVVWD GPS Base Station Network (Las Vegas Valley)

| Field | Value |
|---|---|
| Network | Las Vegas Valley Water District GPS/GNSS Base Station Network |
| Operator | LVVWD (cooperating with NDOT, City of Las Vegas, Clark County Water Reclamation, Lincoln County NV) |
| landing_url | https://www.lvvwd.com/engineering-resources/survey-right-of-way/ |
| access_url | https://www.lvvwd.com/apps/base-station-network-access/ (application form; credentials issued by District Surveyor 702-258-7163) |
| host:port | Host not publicly listed; **port 9899**. Mountpoint names match site names (e.g. `nvbm`). RTK link via NTRIP or TCP/IP |
| tariff | Not publicly listed — credentials issued on application |
| vrs | No — single-base mountpoints |
| num_stations | 19 sites total; 8 are NOAA/NGS CORS (operator page 2026-05-18) |
| hobbyist_eligibility | Unclear — application form collects entity/use info; no published policy |
| legal_residency_required | Unclear |
| last_confirmed_alive | 2026-05-18 — application form + survey resources pages HTTPS 200 |
| datum_epoch | omitted — not published; presumed NAD83(2011) per typical western state practice but no citable operator statement |
| data_archive | Static 5-second epoch RINEX in 1-hr zipped files (GMT) |

Nevada GPS Network originally Washoe County GPS Network (Reno); transferred to UGRC management. TURN subscribers automatically gain Nevada (Reno) network access. LVVWD covers LV Valley with station network distinct from UGRC; access application-based; pricing undisclosed publicly. EarthScope NOTA has stations in NV (Basin and Range, high density compared to many western states) — free fallback.

## WY — no public state caster

No state-operated RTK NTRIP caster. WYDOT does not operate public CORS RTK. PLSW references CORS resources but operates no NTRIP caster. Wyoming Geodetic Coordination Committee lists resources but no operational caster.

TURN GPS (UT) partial paid edge coverage in southern WY near UT border. EarthScope NOTA (PBO stations) sparse single-base. Commercial: RTKdata USD 40/mo, Point One Polaris, RTK Premium. Cross-border within ~50 km: Mesa County RTVRN (CO, free) reachable in extreme south-central WY; MTSRN (paid) reachable in northern WY near MT border.

## MT — MTSRN

| Field | Value |
|---|---|
| Network | Montana State Reference Network |
| Operator | Montana State Library (MSL) with partners MDT (Montana DOT), tribal nations, counties, educational institutions; Trimble Pivot VRS |
| landing_url | https://msl.mt.gov/mtsrn/ |
| access_url | https://www.mtsrn.org/RegisterAccount.aspx (subscription via PayZang) |
| host:port | `mtsrn.org:2101` (3.23.213.134) |
| tariff | Paid — USD 1,500 per login per year (rate effective 2024-07-01; rates reviewed each biennium, announced January odd-years, effective July 1). 2027-biennium MTSRN Revised Glidepath (March 2026) on legmt.gov; no 2026-07-01 rate change publicised |
| vrs | Yes — VRS corrections across five geographic subnets: NEMT (Northeast MT), NCMT (Northcentral MT), NWMT (Northwest MT), SWMT (Southwest MT), SCMT (Southcentral MT) |
| num_stations | 120 stations statewide (MTSRN FAQ: "About 120 stations"). Mountpoint sourcetable: 340 STR (per-station × per-format across 5 subnets) 2026-05-18 |
| hobbyist_eligibility | Unclear — Trimble Pivot registration; no professional licence explicitly required; USD 1,500/yr well above hobbyist threshold; no published hobbyist tier |
| legal_residency_required | No — no stated restriction; contact `mtsrn@mt.gov` |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (340 STR; Trimble Caster 5.2) |
| datum_epoch | NAD83(2011) Epoch 2010.0 — MTSRN FAQ explicit: "2011 realization of North American Datum of 1983 or NAD 83(2011), epoch 2010.0". Citation: https://msl.mt.gov/mtsrn/faq |

MTSRN launched March 2022. Registration: mtsrn.org/RegisterAccount.aspx → PayZang → confirmation from MTSRN Coordinator Kazi Arifuzzaman (`mtsrn@mt.gov` / 406-444-0240). Static RINEX free. Partners (tribal nations, counties) free in exchange for hosting; educational separate agreements. 2027-biennium glidepath: https://archive.legmt.gov/content/Publications/fiscal/2027-Biennium/Committees/Section-E/MSL-MT-State-Reference-Network-Update-March2026.pdf.

## ID — no public state caster

No state-operated RTK NTRIP caster. ITD installed CORS ~2005-06 (Pocatello, Idaho Falls, Rexburg, Driggs) for internal use, not public. ISU GIS Center documented Real-Time Network for Idaho (giscenter.isu.edu/research/Techpg/GC/rtn.htm); cooperative ISU + Frontier Precision + Monsen + UGRC project established southeastern ID VRS — stations now feed into TURN GPS UT footprint.

2024 Idaho Geospatial Office Geodetic Control TWG (gis.idaho.gov/geodetic-control-twg) lists "real-time correction network" as ongoing focus with NGS; no separate ID public caster announced.

TURN GPS (UT) extends paid coverage (USD 600/yr) into southern ID. EarthScope NOTA sparse (PBO). Cross-border within ~50 km: ORGN (free) eastern OR near ID border; MTSRN (paid) northern ID near MT border.

## CA — CRTN

| Field | Value |
|---|---|
| Network | California Real-Time Network |
| Operator | SOPAC / California Spatial Reference Center (CSRC), UC San Diego — clearinghouse aggregating: EarthScope NOTA, UC Berkeley/USGS BARD, USGS Pasadena SCIGN, Caltrans CVSRN, Orange County OCRTN, SOPAC SCIGN |
| landing_url | http://sopac-csrc.ucsd.edu/index.php/crtn/ |
| access_url | http://sopac-csrc.ucsd.edu/index.php/crtn-connecting/ (SurveyMonkey form; account approval ≥ 7 days) |
| host:port | `132.239.152.4:2102` (NorCal Z1-2) · `:2103` (NorCal Z3-4) · `:2104` (SoCal Z5) · `:2105` (SoCal Z6) |
| tariff | One-time USD 100 processing fee (universities + schools exempt); no annual charge. Operator explicit: "$100 processing fee, exempt for universities and schools". Additional accounts USD 1,000/yr (contributing-member tier). Consortium-member tier USD 20,000/yr for simultaneous access to any 20 sites |
| vrs | No — individual physical base-station streams only; not network-RTK processor |
| num_stations | Mountpoint counts 2026-05-18 (line-count minus header/end): ~148 (`:2102`) + ~171 (`:2103`) + ~235 (`:2104`) + ~131 (`:2105`) = **~685 STR**. Per-port flutter day-to-day. Underlying station count: 431 GNSS-capable stations / 707 historical reference frame (CRTN portal). Recent additions: DWR 1500/ARBC/CWD1/ORLD (2026-02-21); Q102/Q122/Q164 + CTSRN PGRV/PDLR/AZYA (2025-12-06) |
| hobbyist_eligibility | Likely yes — USD 100 one-time fee under project's USD 200/yr cutoff; no explicit professional restriction; SurveyMonkey form |
| legal_residency_required | No — no stated requirement |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` on all four ports (server "NTRIP Sopac Caster/1.0"); 677 STR total |
| datum_epoch | **CSRS Epoch 2025.00 (NAD83(2011))** since 2025-08-11 migration. **CSRS here = California Spatial Reference System, NOT Canadian Spatial Reference System NAD83(CSRS)** — name collision; California operator uses "CSRS" / "CSRN" terminology in their own framework. Operator verbatim (connecting page 2026-05-18): "CRTN base stations broadcast CSRS Epoch 2025.00 (NAD83) positions." Explainer (csrn-epoch-2025-00 2026-05-18): formally **"CSRN Epoch 2025.00 NAD83(2011)"** — "realized by the geodetic coordinates and uncertainties of the CSRN on the date of 2025.00." Operator: "rigorously aligned to the current definition of the National Spatial Reference System (NSRS) through a set of coordinate transformations from ITRF2020." Historical streams previously NAD83(2011)/2010.00. Citations: http://sopac-csrc.ucsd.edu/index.php/crtn-connecting/, https://sopac-csrc.ucsd.edu/index.php/csrn-epoch-2025-00/ |
| format | RTCM 3.1 / 3.3 — varies by mountpoint (legacy BARD: RTCM 3.1; NOTA-integration: RTCM 3.3) |
| contact | Maria Turingan, `mrturingan@ucsd.edu` |

Data clearinghouse, not network RTK processor — no VRS computed. Users select nearby physical base; baseline ~20-30 km for RTK. Zone selection geographic. BARD (Bay Area Regional Deformation, UC Berkeley) real-time streams for SF Bay. Caltrans CVSRN (Central Valley) stations included in CRTN; Caltrans standalone CVSRN restricted to vetted partners. SDCRTN (San Diego County, ~13 stations); free for County employees + approved partners; non-county via CRTN. OCRTN (Orange County) mirrored to CRTN.

## OR — ORGN

| Field | Value |
|---|---|
| Network | Oregon Real-Time GNSS Network |
| Operator | ODOT Geometronics Unit; Leica GNSS Spider |
| landing_url | https://www.oregon.gov/odot/orgn/pages/products-services.aspx |
| access_url | https://www.oregon.gov/odot/orgn/pages/rover-requests.aspx |
| host:port | `orgn.odot.state.or.us:9881` (network; IP 167.131.109.57). Single-base on `167.131.0.205:9879` per ODOT Trimble Access PDFs |
| tariff | Free — "All rover users will be issued a rover account at no direct charge". ODOT reserves potential future fees for non-partner users; partner accounts remain permanently free |
| vrs | Yes — network (i-MAX/MAX) multi-base; also single-base for users outside primary network boundary |
| num_stations | ~150 physical stations; ~90% multi-constellation (GPS+GLO+GAL — **NO BDS in operator quote**); ~70 km spacing (ODOT about page re-fetched 2026-05-18: "Approximately 90% of the 150 stations now collect data from three constellations GPS, GLONASS, and Galileo"). 6 STR mountpoints (`Nearest_Single_RTCM3`, `MAX_RTCM3`, `IMAX_CMR_AG`, `IMAX_CMR+`, +2 variants). **BDS absence: ODOT about page is the only operator-cited constellation statement available; whether BDS is excluded by network policy or the quote pre-dates the BDS-receiver fleet rollout is not clarified by ODOT. Constellation list may be understated for current hardware — confirm via `ORGN@odot.oregon.gov` before relying on BDS** |
| hobbyist_eligibility | Likely yes — "all users" receive accounts at no charge; no professional licence field; contact `ORGN@odot.oregon.gov` to confirm |
| legal_residency_required | No — no stated restriction |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (6 STR; GNSS Spider 7.9.0.386) |
| datum_epoch | NAD83(2011) Epoch 2010.00 — ODOT explicit: "NAD 83(2011) epoch 2010.00". Citation: https://www.oregon.gov/odot/orgn/pages/about-us.aspx |
| format | RTCM 3.x; also Trimble CMR+ for Trimble users |

Accounts issued via rover request form. Non-std Leica Spider ports (9879 single-base, 9881 network), not 2101. Contact: `ORGN@odot.oregon.gov`; 1-888-275-6368.

## WA — WSRN

| Field | Value |
|---|---|
| Network | Washington State Reference Network |
| Operator | Multi-agency public/private (WSDOT-led with PANGA/CWU contributing antennae, comms, data archiving for Puget Sound); Trimble Pivot; administered from wsrn3.org |
| landing_url | http://www.wsrn.org/about.aspx (ECONNREFUSED from sandbox 2026-05-18; portal accessible per user) |
| access_url | http://wsrn3.org/RegisterAccount.aspx (subscription or partner application) |
| host:port | `wsrn.org:2011` (NAD83-2011 / Epoch 2010.00, MYCS3 height model) · `wsrn.org:2022` (NATRF2022, sourcetable empty pending mountpoint provisioning). Legacy port 8080 retiring |
| tariff | Paid — non-partner USD 1,900/yr per login; tiered bundles (5 logins USD 5,700, 10 USD 10,000, 20 USD 15,000, 40 USD 20,000). **Derivation chain (explicit):** operator pricing page `http://www.wsrn.org/about.aspx` reachable via plain HTTP (HTTP 200 2026-05-18; ECONNREFUSED via HTTPS — WebFetch auto-upgrades to HTTPS and fails); pricing text not extracted in sandbox because tooling promotes HTTPS. Fallback citation: March 2024 City of Cheney WSRN subscriber agreement V24.1 (third-party municipal contract publishing the WSRN rate card). Earlier confirmation: 2015 Caltrans PI memo + 2016 RPLS forum (rates unchanged 2015–2024). Partner agencies (government, NGS cooperators) free. 90-day test accounts one-time per individual/firm. Well above USD 200/yr hobbyist threshold |
| vrs | Yes — Trimble Pivot network corrections; per-station per-format (RTCM 3.1 GPS+GLO; RTCM 3.2-MSM GPS+GLO+GAL+BDS+QZS; legacy CMR+); mountpoints at wsrn3.org/MountpointNaming.aspx |
| num_stations | 492 STR on port 2011 (per-station × per-format) 2026-05-18; 0 STR on port 2022 (CAS line only — NATRF2022 caster online, mountpoint provisioning pending). PANGA contributes 220+ GNSS stations to PNW geodetic backbone; WSRN-overlapping subset reflected in mountpoint counts |
| hobbyist_eligibility | Unclear-leaning-no — no published hobbyist tier; positioned for surveyors/engineering firms; USD 1,900/yr practical barrier |
| legal_residency_required | Unclear |
| last_confirmed_alive | 2026-05-18 — `wsrn.org:2011` `SOURCETABLE 200 OK` (492 STR; Trimble Caster 5.1); `wsrn.org:2022` `SOURCETABLE 200 OK` (CAS line only, 0 STR — NATRF2022 caster live but mountpoint catalogue pending; `CAS;192.168.248.36;2022;ROVERS_2022;WSRN;…`) |
| datum_epoch | NAD83-2011 / Epoch 2010.00 with MYCS3 height model on port 2011 (WSRN sourcetable station metadata); NATRF2022 on port 2022 (active provisioning, catalogue not populated). Citation: http://www.wsrn3.org/NewREADME.aspx ("the current reference framework is NAD83-2011 Epoch 2010.00"); WSRN Datum Plan PDF: http://www.wsrn.org/WSRN_Datum_Plan.pdf |

Long-running cooperative (WSDOT, Seattle Public Utilities, multiple partners). Partner agencies free; non-partners pay. 90-day test accounts once per individual/firm. City of Bellingham documents WSRN at cob.org/services/maps/monuments/wsrn. PANGA (Pacific Northwest Geodetic Array, CWU) operates 220+ GNSS for geodetic science; real-time GNSS processing internal (JPL RTG + Trimble RTKNet); no public PANGA-direct NTRIP endpoint. Hobbyists in WA reach same physical PANGA stations via free EarthScope NOTA (in-pipeline) or WSRN-overlapping subset via WSRN paid.

## HI — no public state caster

HDOT does not operate public CORS RTK. GPS World Dec 2024 lists HI as "no public service". E38 Survey Solutions absent. Pacific GPS Facility at UH SOEST/HIGP (soest.hawaii.edu/pgf/) processes real-time GPS for research (constraining KOK1, KOKB, MKEA to ITRF2000), no public NTRIP caster. Kīlauea GPS network = HVO/USGS + UH + Stanford research collaboration, not public.

EarthScope NOTA: handful of GNSS in HI (volcanic monitoring Big Island + Maui — KOKB, MKEA, MAUI, HILO area), limited spacing, islands geographically isolated. NPS CORS: Pacific stations HAVO (Hawaii Volcanoes) + HALE (Haleakalā), both present in 2026-05-18 NPS sourcetable.

Topcon announced Topnet Live expansion to include HI in October 2024 (commercial paid). Commercial alternatives: Topnet Live (Topcon), Point One Polaris. No free VRS network identified.

## Multi-state commercial networks (reference)

| Network | Coverage | host:port | Tariff | VRS |
|---|---|---|---|---|
| RTKdata | All 50 states | rtkdata.com | USD 40/mo; 30-day free trial | Unknown |
| Point One Polaris | All 50 states | pointonenav.com | USD 50/mo | Yes |
| SmartNet (Leica/Hexagon) | OK, TX, WA, others | smartnetna.com | Paid (not disclosed) | Yes |
| Topnet Live (Topcon) | TX, WA, HI, others | topconpositioning.com | Paid | Yes |
| RTK Premium | Most western (gaps) | rtkpremium.com | Paid | Yes |
| AZGPS | AZ, So-CA | azgps.net | Paid (not disclosed) | Yes |

## Post-processing fallback

| Service | Coverage | Cost |
|---|---|---|
| NOAA NCN CORS — static RINEX | All western states | Free; no account |
| EarthScope NOTA RINEX | All western states (variable density) | Free non-commercial; account |
| CRTN RINEX (SOPAC/CSRC) | California | Free; same account as NTRIP |
| SOPAC/BARD | CA Bay Area | Free |
| MTSRN RINEX | Montana | Free (no subscription) |
| PGF (UH SOEST) | Hawaii | Research access |

## Key findings & gaps

- **Free public NTRIP RTK** in 4/16 states: AR, AZ, CO via Mesa County, OR. Plus CA at USD 100 one-time (under USD 200/yr threshold — affordable).
- **Paid state-level subscription** in 4 states: LA (C4G entry USD 495/yr), MT (USD 1,500/yr), UT/NV-Reno (USD 600/yr bundled), WA (USD 1,900/yr).
- **No state caster** in 6 states: OK, NM (ARTGN status unverified), WY, ID, HI; plus TX (DOT-restricted, not hobbyist-accessible).
- **Federal fallbacks** (EarthScope NOTA, NPS CORS) cover seismically active western Cordillera densely. Plains (eastern WY, eastern MT, western OK panhandle, western NE) sparse.
- **WSRN USD 1,900/yr** = most expensive western state network. LVVWD pricing undisclosed.
- **CRTN USD 100 one-time** = cheapest gateway to large station network (431 GNSS-capable stations / ~685 STR rows 2026-05-18) in West; under hobbyist threshold. Migrated to CSRS Epoch 2025.00 NAD83(2011) 2025-08-11 (transmitted via existing RTCM 3.3 streams).
- **Mesa County RTVRN** geographically narrow (Western CO) but free and maintained.
- **AZCORS** = 71 sites (56 ADWR + 15 EarthScope/NPS) per ADWR 2026-04-14 page — figure carried from prior research; 2026-05-18 sandbox cannot re-fetch ADWR landing/PDF (HTTP 403, no UA-swap or wayback bypass) to re-validate the 71/56/15 breakdown.
- **WSRN NATRF2022 port (2022)** = caster handshake live, empty mountpoint catalogue — provisioning expected through 2H2026 alongside NSRS modernisation rollout.
- **Volunteer/community casters** (rtk2go) in West cluster densely in PNW (WA, OR) — counted via `data/stations.json` per pipeline.
- **Open items requiring direct contact**: ARTGN (NM) operational status (505-768-3614); LVVWD (NV) pricing + hobbyist eligibility; AZCORS confirmed external NTRIP port (Cloudflare CDN obscures anonymous probe); MTSRN biennial rate review for 2026-07-01 (March 2026 glidepath published, no rate change announced).

## Sources

- ODOT ORGN products: https://www.oregon.gov/odot/orgn/pages/products-services.aspx
- ODOT ORGN rover accounts: https://www.oregon.gov/odot/orgn/pages/rover-requests.aspx
- ODOT ORGN about (datum citation): https://www.oregon.gov/odot/orgn/pages/about-us.aspx
- ODOT ORGN connection PDFs: https://www.oregon.gov/odot/ORGN/Documents/Network-Connection-TSC2-Trimble-Access.pdf, Single-Base-Solutions-TSC2-Trimble-Access.pdf
- AZCORS / ADWR: https://www.azwater.gov/hydrology/azcors
- AZCORS mountpoints PDF (April 2026): https://www.azwater.gov/sites/default/files/2026-04/AZCORS_InformationAndMountpoints20260406.pdf
- AZCORS SBC: https://azcors.azwater.gov/sbc/Account
- AZGeo AZCORS hub: https://azgeo-data-hub-agic.hub.arcgis.com/pages/azcors
- AZGPS (commercial): https://azgps.net
- ARDOT RTN portal: http://gps.ardot.gov/
- ARDOT RTN sensor map: http://gps.ardot.gov/Map/SensorMap.aspx
- ARDOT GPS Control / Arkansas GIS Office: https://gis.arkansas.gov/product/ardot-gps-control/
- ARDOT Control Surveys (datum citation): https://ardot.gov/divisions/surveys/control-surveys/
- ARDOT Trimble config PDF: http://gps.ardot.gov/Configuring%20Trimble%20Receiver%20on%20ARDOT%20RTN.pdf
- PAGIS GPS Reference: https://www.pagis.org/index.php/data-resources/gps-reference-station-access/
- TxDOT RTN portal: https://txrtn.txdot.gov/
- TxDOT GPS page: https://www.txdot.gov/data-maps/global-positioning-system-gps.html
- C4Gnet portal (datum citation): https://c4gnet.xyz/
- C4Gnet NTRIP mountpoints (datum citation): http://c4gnet.xyz/NTRIP_Mountpoints.aspx
- LSU C4G store (pricing citation): https://store.c4g.lsu.edu/
- LSU C4G store 1-yr unlimited: https://store.c4g.lsu.edu/products/1-year-unlimited-rtk-rover-ntrip-only-account
- LSU C4G store full RTN: https://store.c4g.lsu.edu/index.php?product_id=62&route=product%2Fproduct
- Mesa County RTVRN: https://www.mesacounty.us/departments-and-services/public-works/gps-survey/real-time-virtual-reference-network-rtvrn
- Mesa County RTVRN docs (mountpoints + datum citation): https://www.mesacounty.us/sites/default/files/2025-05/RTVRN%20Mountpoint%20Names.pdf, https://www.mesacounty.us/sites/default/files/2025-05/RTVRN%20Login%20Instructions%20and%20NTRIP%20Mountpoints.pdf
- Mesa County RTVRN portal: https://rtvrn.mesacounty.us/
- TURN GPS UGRC: https://gis.utah.gov/products/turn/
- TURN GPS connecting (datum + tariff citation): https://gis.utah.gov/documentation/turn/connecting/
- TURN GPS bill pay: https://turngps-billpay.ugrc.utah.gov
- TURN GPS portal: https://turngps.utah.gov/
- Nevada GPS Network (Reno area; operator portal): https://nevadagps.utah.gov/
- Nevada GPS Network legacy UGRC slug (HTTP 301 → gis.utah.gov/products/turn/ 2026-05-18, no longer Nevada-specific): https://gis.utah.gov/gps/ngps/
- Washoe County GPS Base Stations: https://washoecounty.gov/csd/engineering_capitalprojects/development_services/gps_base_stations/index.php
- LVVWD survey/right-of-way: https://www.lvvwd.com/engineering-resources/survey-right-of-way/
- LVVWD account request: https://www.lvvwd.com/apps/base-station-network-access/
- MTSRN main: https://msl.mt.gov/mtsrn/
- MTSRN subscribe: https://msl.mt.gov/mtsrn/subscribe
- MTSRN FAQ (datum + station count citation): https://msl.mt.gov/mtsrn/faq
- MTSRN how it works: https://msl.mt.gov/mtsrn/howitworks
- MTSRN launch announcement: https://content.govdelivery.com/accounts/MTLIBRARY/bulletins/393bfda
- MTSRN biennium rate update Sept 2024: https://archive.legmt.gov/content/Publications/fiscal/2025-Biennium/Section-E/Interim/MSL-MT-State-Reference-Network-Update-Sept2024.pdf
- MTSRN revised glidepath March 2026: https://archive.legmt.gov/content/Publications/fiscal/2027-Biennium/Committees/Section-E/MSL-MT-State-Reference-Network-Update-March2026.pdf
- MTSRN Pivot portal: https://www.mtsrn.org/
- CRTN SOPAC/CSRC: http://sopac-csrc.ucsd.edu/index.php/crtn/
- CRTN connecting (datum + fee citation): http://sopac-csrc.ucsd.edu/index.php/crtn-connecting/
- CRTN station list (epoch migration citation): https://sopac-csrc.ucsd.edu/index.php/crtn-stationlist/
- CRTN consortium: https://sopac-csrc.ucsd.edu/index.php/crtn-consortium/
- CRTN connecting PDF: http://sopac-csrc.ucsd.edu/wp-content/uploads/2019/11/Connecting_to_CRTN_Resource_11-14-19.pdf
- SDCRTN procedures: https://www.sandiegocounty.gov/content/dam/sdc/dpw/COUNTY_SURVEYOR/SDCRTN_procedures2.pdf
- Caltrans D6 RTN: https://dot.ca.gov/caltrans-near-me/district-6/district-6-programs/d6-land-surveys/d6-rtn-gps
- 2015 Caltrans PI memo: https://dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/preliminary-investigations/real-time-gps-networks-pi-a11y.pdf
- WSRN about: http://www.wsrn.org/about.aspx
- WSRN new visitor info (datum citation): http://www.wsrn3.org/NewREADME.aspx
- WSRN join/register: http://wsrn3.org/RegisterAccount.aspx
- WSRN datum plan: http://www.wsrn.org/WSRN_Datum_Plan.pdf
- WSRN CSRC presentation May 2025: https://sopac-csrc.ucsd.edu/wp-content/uploads/2025/07/WSRN-Update-CSRC-051525.pdf
- WSRN Mountpoint naming: http://www.wsrn3.org/MountpointNaming.aspx
- WSRN FAQ PDF: http://www.wsrn3.org/WSRN_FAQ.pdf
- City of Bellingham WSRN: https://cob.org/services/maps/monuments/wsrn
- PANGA (CWU): https://www.geodesy.org/, https://www.panga.org/
- ISU GIS Center RTN history: https://giscenter.isu.edu/research/Techpg/GC/rtn.htm
- Frontier Precision SE Idaho RTN: https://frontierprecision.com/news/real-time-gnss-network-southeast-idaho/
- Idaho Geospatial Office Geodetic Control TWG: https://gis.idaho.gov/geodetic-control-twg
- PLSW CORS: https://www.plsw.org/cors/
- Wyoming Geodetic Coordination: https://geodetic.geospatialhub.org/pages/resources
- ARTGN background (American Surveyor 2010): https://amerisurv.com/2010/12/05/real-time-gnss-network-in-new-mexico/
- City of Albuquerque AGRS: https://www.cabq.gov/municipaldevelopment/architects-engineers-contractors/construction-services/albuquerque-geodetic-reference-system
- ARTGN connection guide (2013 archived): https://www.yumpu.com/en/document/view/17923468/
- Pacific GPS Facility (UH SOEST): http://www.soest.hawaii.edu/pgf/
- Topcon Topnet Live HI expansion (Oct 2024): https://www.topconpositioning.com/us/en/articles/topcon-announces-significant-expansion-of-topnet-live-coverage-across-western-usa-and-hawaii
- EarthScope GNSS Realtime: https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA: https://www.earthscope.org/nota/
- E38 Survey Solutions RTK by state: https://e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state
- ArduSimple US RTK: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- NTRIP-list NA: https://ntrip-list.com/north-america/
- GPS World public RTK list: https://www.gpsworld.com/finally-a-list-of-public-rtk-base-stations-in-the-u-s/
- NGS CORS FAQ (state RTK provider list — confirms AR, AZ via AZHMP, OR, UT/NV, WA, MT, LA): https://geodesy.noaa.gov/CORS/cors_faqs.shtml
- USCG NDGPS decommissioning: https://www.federalregister.gov/documents/2018/03/21/2018-05684/discontinuance-of-the-nationwide-differential-global-positioning-system-ndgps
- Point One Nav state pages (AZ, TX, OK, NM, WY, ID, HI): https://pointonenav.com/states/[state]/
- Probes 2026-05-18 (curl `--http0.9 -A 'NTRIP/1.0'`): gps.ardot.gov:2101 OK 8 STR; rtvrn.mesacounty.us:2101 OK 6 STR; mtsrn.org:2101 OK 340 STR; wsrn.org:2011 OK 492 STR; wsrn.org:2022 OK 0 STR (CAS only); 132.239.152.4:2102/2103/2104/2105 OK 150+166+231+130 = 677 STR; orgn.odot.state.or.us:9881 OK 6 STR; c4gnet.xyz:9000 OK 32 STR; txrtn.txdot.gov HTTPS 200; azcors.azwater.gov HTTPS 403 (Cloudflare); 165.239.144.5:2101 TCP timeout (account-gated); 168.179.231.11:2102 TCP timeout
