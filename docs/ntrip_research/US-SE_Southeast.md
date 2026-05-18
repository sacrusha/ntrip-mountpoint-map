# US Southeast [US-SE] — NTRIP RTK Caster Research

**States:** VA, WV, NC, SC, GA, FL, AL, MS, TN, KY

## Status (region)

8/10 states have active state-operated caster (5 free, 3 paid). VA and GA have no public state caster.

## Per-state summary

| State | Network | Operator | host:port | Tariff | VRS | Hobbyist | Live 2026-05-18 | Datum citable |
|---|---|---|---|---|---|---|---|---|
| VA | None | — | — | — | — | — | N/A | N/A |
| WV | WVRTN | WVDOT | `wvrtn.cors.us:2101` | Free | Yes | Unclear (likely yes) | OK 7 STR | No |
| NC | NC RTN | NC Geodetic Survey | `rtn.nc.gov:2101` | Paid USD 500 one-time | Yes | Unclear | Portal HTTP 200; NTRIP firewalled | No |
| SC | SCRTN | SC Geodetic Survey | `scrtn.sc.gov:2101` | Paid USD 1,200 first | Yes | Unclear | OK 14 STR | No |
| GA | None | — | — | — | — | — | N/A | N/A |
| FL | FPRN | FDOT | `48.223.232.215:10000` | Free | Yes | Yes (explicit) | OK 101 STR | Yes — NAD83(2011) 2010.0 / NATRF2022 2020.0 / WGS84(G2296) / ITRF2020 |
| AL | AlCORS | ALDOT | `205.172.52.26:10011` & `:10099` | Free | Yes (Leica iMAX) | Unclear (likely yes) | OK 10 + 158 STR | No |
| MS | GCGC RTN | USM | `rtn.usm.edu:2101` | Free | Yes | Yes (explicit) | OK 14 STR | No |
| TN | TDOT GNSS RTN | TDOT | Not public (via portal.tndot.net) | Paid USD 450/yr | Yes | Unclear | Portal HTTP 302; NTRIP firewalled | No |
| KY | KyCORS | KYTC | `kycors.ky.gov:2101` | Free | Yes | Unclear (likely yes) | OK 6 STR | No |

## Regional baselines

**EarthScope NOTA**: see `US-NOTA_NetworkOfTheAmericas.md`. SE coverage sparse geodetic single-base in all 10 SE states; fills gaps where state absent (VA, GA) or restricted/paid (NC, SC, TN). Per-radius query `py scripts/stations_by_radius.py <lat> <lon> <km>`.

**NPS CORS**: see `US-NPS_NationalParkService.md` (endpoint `rtk.nps.gov:2101`, free, manual provisioning, single-base). SE/Caribbean stations: FL `DESO_RTCM3` (De Soto NM — RTCM 3.4), PR `SAJU_RTCM3` (San Juan NHS). FL FPRN provides dense free statewide coverage subsuming DESO single-base for most users.

## VA — no state-operated public caster

VDOT reportedly attempted statewide RTK network and abandoned after litigation from Leica/Topcon (commercial SmartNet etc. already operating) — sourced from RPLS forum thread, not independently confirmed by VDOT press release or court filing. **No further verification attempted in this session** (VDOT press-release archive, eVA procurement records, Virginia court-records databases not searched) — litigation claim status remains unresolved; treat as community lore until corroborated. As of 2026-05-18 no VDOT or other VA state-agency caster identified.

| Field | Value |
|---|---|
| Active public caster | No |
| Alternatives | EarthScope NOTA (single-base, free non-commercial); KeyNetGPS (commercial, covers parts of VA); Leica SmartNet / Topcon TopNET (commercial) |

VDOT Survey Manual (Chapter 5, last updated 2023) acknowledges commercial RTK/VRS use but references no VDOT-hosted caster. Contact: `GeoSpatial-info@VDOT.virginia.gov`.

## WV — WVRTN

| Field | Value |
|---|---|
| Network | West Virginia Real Time Network |
| Operator | WVDOT IT Division, Highway Data Services Unit |
| landing_url | https://wvrtn.cors.us/ — operator portal |
| access_url | Skip — landing portal is sole operator-owned access page; community guides (E38, laserinst.com WVDOH VRS) describe workflow but third-party |
| host:port | `wvrtn.cors.us:2101` (also `34.228.171.115:2101`; caster-side `206.212.1.199:2101` per WVDOT docs) |
| num_stations | 32 CORS, 17 on NSRS (WVRTN portal text 2026-05-18: "32 Continuously Operating Reference Stations(CORS) with 17 of these sites on the National Spatial Reference Frame (NSRS)"; prior file recorded 34/14 from older 2024 GeoCon presentation, superseded). Live ST 7 mountpoints — all VRS/network-solution/test streams, not per-station |
| tariff | Free |
| vrs | VRS-only; recommended `rtxRTCM3_4_MSM` (RTCM 3.4 MSM, GPS+GLO+GAL+BDS). Older `vrsRTCM3_*` GPS+GLO-only also present |
| hobbyist_eligibility | Unclear — registration requires Organization field; no professional licence stated; likely yes for any user with valid email |
| legal_residency_required | Unclear — no stated requirement |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (7 STR: `vrsRTCM3_1`, `vrsCMRx`, `vrsCMRplus`, `vrsRTCM3_2`, `rtxCMRx`, `rtxRTCM3_4_MSM`, `NATRF2022_Test`; Trimble Caster 5.2 / PIVOT 4.3.2) |
| datum_epoch | NAD 83(2011) — portal explicit: "Current coordinate system is NAD 83(2011)". NATRF2022 plan: "When details are provided on NATRF 2022, the WVRTN will provide details regarding how it will be implemented" (`NATRF2022_Test` mountpoint already live; Trimble beta). Citation: https://wvrtn.cors.us/ |

Recent Trimble Alloy receiver upgrades. Support: `WVRTNHelpDesk@wv.gov`. Backup hostname: `cors.us` (same IP).

## NC — NC RTN

| Field | Value |
|---|---|
| Network | North Carolina GNSS CORS and Real-Time Network (NC RTN) |
| Operator | NC Geodetic Survey (NCGS), division of NC DENR |
| landing_url | https://rtn.nc.gov/ — operator portal welcome |
| access_url | https://ncgs.state.nc.us/pages/CORS-and-GNSS.htm — NCGS overview (ECONNREFUSED from sandbox 2026-05-18) |
| host:port | `rtn.nc.gov:2101` (DNS `207.4.106.112`); port 2101 timed out external; web portal :443 active |
| num_stations | unknown — operator does not enumerate physical CORS count on portal. SCRTN Subscriber Agreement references "10 NC stations" used by SC network but partial cross-border, not NC RTN total |
| tariff | Paid — first RTK login: USD 500 one-time; second login: included with first; subsequent logins: USD 250 each. CORS static RINEX: free. Payment by cheque. Source: rtn.nc.gov sign-up form |
| vrs | Yes — Trimble Pivot VRS |
| hobbyist_eligibility | Unclear — registration requires Organization; no professional licence; USD 500 entry cost = practical barrier |
| legal_residency_required | Unclear |
| last_confirmed_alive | Portal HTTP 200; NTRIP port 2101 IP-filtered external |
| datum_epoch | omitted — no citable operator declaration (welcome silent; NCGS page ECONNREFUSED) |

Fees are one-time (perpetual credentials), not annual — cost-effective for frequent users once paid. Invoicing first week of month after account creation. Station map: rtn.nc.gov/Map/SensorMap.aspx.

## SC — SCRTN

| Field | Value |
|---|---|
| Network | South Carolina Real Time Network |
| Operator | SC Revenue and Fiscal Affairs Office — SC Geodetic Survey |
| landing_url | https://scrtn.sc.gov/ — operator portal welcome |
| access_url | https://rfa.sc.gov/programs-services/geodetic/rtnstatus — RFA SCRTN status / service page (ECONNREFUSED from sandbox 2026-05-18). Registration form `sc.accessgov.com/rfa/Forms/Page/rfa/scrtn/` |
| host:port | `scrtn.sc.gov:2101` — `SOURCETABLE 200 OK` 2026-05-18 |
| num_stations | 43 SC + 2 GA + 10 NC = 55 contributing (per scrtn.sc.gov portal) |
| tariff | Paid — first subscription USD 1,200; additional subscriptions same subscriber USD 600 each. Payment at application; no refunds. Source: SCGS RTN Subscriber Agreement, rev. 04/2023 (ECONNREFUSED from sandbox; cached value) |
| vrs | Yes — Trimble Pivot VRS (`VRS_RTCM31`, `VRS_RTCM32`, `RTX_RTCM32` GPS+GLO+GAL+BDS+QZS, `VRS_CMRx`) |
| hobbyist_eligibility | Unclear — subscriber agreement implies professional/business; no explicit individual exclusion but USD 1,200 entry + formal agreement deter casual use |
| legal_residency_required | Unclear |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (14 STR; Trimble Caster 5.2) |
| datum_epoch | omitted — no citable operator declaration located on scrtn.sc.gov or rfa.sc.gov (sandbox 2026-05-18 reachability gated). Speculation about operator (Mat Wellslager) discussing NATRF2022 in community channels removed — no specific RPLS thread / NSPS webinar / SC Society of Professional Land Surveyors newsletter URL has been verified |

Stated accuracy ~2 cm horiz / ~4 cm vert. Registration: sc.accessgov.com/rfa/Forms/Page/rfa/scrtn/.

## GA — no free public state caster

GDOT does not operate a public CORS RTK network. GDOT Policy 4465-8 ("Guidelines for Performing Network RTK GPS Surveys") explicitly: "GPS Reference Network and/or RTK of any kind will not be allowed to establish project control values on Department projects" — RTK permitted for photogrammetric/secondary activities only after confinement onto existing project control. Consistent with GDOT not operating public caster.

| Field | Value |
|---|---|
| Active public caster | No |
| Commercial fallback (eGPS, paid) | Plan A (dual network) USD 2,475/yr; Plan B (VRS only) USD 1,650/yr; Plan C (Flex) USD 50/day cap USD 400/mo; Plan D (Agriculture) USD 1,000/yr (egps.net/netservices.html 2026-05-07) |
| eGPS VRS | Yes — GEO++ + eGPS products |
| eGPS hobbyist | No free tier; minimum Plan C USD 50/day; falls under "restricted/paid" per primer [licensing] |

EarthScope NOTA provides sparse single-base in GA. GCGC RTN (USM, MS) coverage does not extend meaningfully into GA.

## FL — FPRN

| Field | Value |
|---|---|
| Network | Florida Permanent Reference Network (FPRN) |
| Operator | FDOT Geospatial office |
| landing_url | https://www.fdot.gov/geospatial/fprn.shtm |
| access_url | https://www.myfloridagps.com/ — Leica SBC portal |
| host:port | `48.223.232.215:10000` (NAD83-broadcast Network Solutions); 11000-series ports for TCP/IP; legacy IP `40.121.5.206` deprecated |
| tariff | Free — FAQ explicit: "Currently there are no plans to charge users for any FPRN services or products" |
| vrs | Yes — VRS, iMAX, MAX, FKP; mountpoint `RTCM3_VRS`; formats RTCM 2.3 / RTCM 3.1 / CMR+ / RTCM 3.3 MSM4 |
| hobbyist_eligibility | Yes — FAQ explicit: "Anyone with an NTRIP ready GPS/GNSS Receiver. Access to the Internet is required" |
| legal_residency_required | No — registration at myfloridagps.com/sbc; no FL residency stated |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (101 STR; GNSS Spider 7.11.1.109); myfloridagps.com HTTPS 200 |
| datum_epoch | **CITABLE** — operator FAQ (myfloridagps.com/faq/fprnfaq2025.html, fetched 2026-05-18) declares: **NAD83(2011) Epoch 2010.0000**, **NATRF2022 Epoch 2020.0000**, **WGS84(G2296)**, **ITRF2020** (updated quarterly). Port 10000 = NAD83-aligned Network Solutions; other ports serve additional frames |
| num_stations | "Array of 100 or more continuously operating, dual-frequency geodetic GNSS receivers" (FAQ) |

Account activation 24-48h. Only SE caster with clearly operator-declared datum/epoch as of 2026-05-18. FPRN widely regarded as model state public RTK: no fees, no professional requirement, broad constellation, multi-frame output.

## AL — AlCORS

| Field | Value |
|---|---|
| Network | Alabama DOT CORS Network (ALDOT CORS / AlCORS) |
| Operator | ALDOT — Leica SpiderNet |
| landing_url | https://aldotcors.dot.state.al.us/ — Leica SBC portal welcome |
| access_url | Skip — landing portal serves both purposes (routes to `/SBC/Account/Register`) |
| host:port | `aldotcors.dot.state.al.us` resolves to `205.172.52.25` and `205.172.52.26`; only `:26` reachable externally on ports 10011 (network solutions) + 10099 (single-base). Std NTRIP port 2101 firewalled on both IPs |
| num_stations | 158 physical single-base streams on `205.172.52.26:10099` (live ST 2026-05-18; 1 stream per CORS — RTCM 3 GPS+GLO). Port `:10011` carries 10-mountpoint network-solution layer (LeicaMAX/iMAX/NEAR/MSM4 variants), not per-station |
| tariff | Free — confirmed by surveying community sources (rpls.com, Emlid community) |
| vrs | Yes — `:10011` advertises Leica `LeicaMAX` / `LeicaIMAX` / `IMAX_MSM4` (iMAX) and `NEAR_MSM4`. iMAX = Leica NRTK product functionally equivalent to VRS. Canonical `_VRS` mountpoint name not published; NRTK capability operator-advertised |
| hobbyist_eligibility | Unclear — registration form requires Company field (Leica SBC standard); no professional licence; hobbyists have successfully registered per community |
| legal_residency_required | Unclear |
| last_confirmed_alive | 2026-05-18 — `205.172.52.26:10011` OK 10 STR (`RTCMIMAX`, `AutoMAX`, `CMR+IMAX`, `LeicaMAX`, `LeicaIMAX`, `CMR+NEAR`, `Near_Leica_GG`, `Near_RTCMv3_GG`, `NEAR_MSM4`, `IMAX_MSM4` — last two added 2025, GPS+GLO+GAL+BDS) and `:10099` OK 158 STR (single-base, RTCM 3 GPS+GLO); GNSS Spider 7.8.0.9445 |
| datum_epoch | omitted — no citable operator declaration (welcome silent; no separate ALDOT geodetics page found) |

ALDOT transitioned from legacy TCP to Leica SBC web portal ~2022 (YouTube "NEW ALDOT NTRIP SETTINGS" Aug 2022). Reported working mountpoint: `LeicaMAX`; also `ALGR_RTCM3`. Non-std port `:10099` typical for Leica SpiderNet.

## MS — GCGC RTN

| Field | Value |
|---|---|
| Network | Gulf Coast Geospatial Center Real Time Network |
| Operator | USM — Gulf Coast Geospatial Center (GCGC) |
| landing_url | https://www.usm.edu/gulf-coast-geospatial-center/real_time_network.php — USM operator overview |
| access_url | http://rtn.usm.edu/ — operator portal |
| host:port | `rtn.usm.edu:2101` — `SOURCETABLE 200 OK` 2026-05-18 |
| num_stations | "52 CORS across MS" attributed to USM operator page in prior research (USM landing not re-fetched in this session — station-count age unclear; treat as best-available estimate until next refresh). Network established 2005 under NOAA/NGS national initiative |
| tariff | Free — USM operator page explicit: "Use of the network is free of charge" |
| vrs | Yes — live ST: `RTCM31_VRS`, `RTCM23_VRS`, `CMRX_VRS`, `CMRPLUS_VRS`, plus VRS_GNSS_* and VRS_GPGL_* (GPS+GLO+GAL+BDS on GNSS variants); `SB_*` and `NSB_*` single-base |
| hobbyist_eligibility | Yes — open registration; no professional licence requirement stated |
| legal_residency_required | No — registration open to anyone |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (14 STR; Trimble Caster 5.2) |
| datum_epoch | omitted — USM page describes service in general terms; ST mountpoint names contain `_NAD83` suffix but a string in a mountpoint name is not an operator-published datum declaration |

Serves: surveying, engineering, transportation, precision ag, emergency management, scientific research. Contact: `debra.armstead@usm.edu` / 228.276.1733. Coverage MS-focused; does not extend into GA.

## TN — TDOT GNSS RTN

| Field | Value |
|---|---|
| Network | TDOT GNSS Reference Network |
| Operator | TDOT Geodetics Division; Leica-based platform (migrated Feb 2025) |
| landing_url | https://www.tn.gov/tdot/engineering-division/geodetics/gnss-reference-network.html |
| access_url | https://portal.tndot.net/ — operator subscription/account portal; `purchase_license.cfm` has fee schedule + T&C link |
| host:port | Not publicly documented; provided post-payment via portal.tndot.net; port 2101 timed out external (account-gated) |
| num_stations | unknown — TDOT pages do not enumerate physical CORS; FY25 T&C PDF silent on count. Pre-migration legacy Trimble "~50 stations" is a third-party estimate from prior research (no specific URL retained); not operator-confirmed for post-Feb-2025 Leica system |
| tariff | Paid — USD 450 per 12-month term (FY25 T&C: USD 150 processing + USD 300 access (12 × USD 25/mo); portal.tndot.net/FY_25_GNSS_TC_FINAL.pdf, pdftotext 2026-05-17). FY26-specific T&C PDF not located on TDOT landing 2026-05-18; landing directs new users to `portal.tndot.net/purchase_license.cfm` |
| vrs | Yes — Leica network platform provides VRS + network solutions |
| hobbyist_eligibility | Unclear — formal T&C; USD 450/yr moderate barrier; no professional licence explicitly required |
| legal_residency_required | Unclear — TN portal but no residency clause confirmed |
| last_confirmed_alive | portal.tndot.net HTTP 302 (redirect to login) 2026-05-18; subscription purchase page active |
| datum_epoch | omitted — no citable operator declaration |

TDOT replaced legacy Trimble CORS with Leica system; migration complete 2025-02-01. Pre-existing Trimble credentials invalid after that. New users: create portal account → accept T&C → pay → receive credentials. Status: status.tndot.net.

## KY — KyCORS

| Field | Value |
|---|---|
| Network | Kentucky Real Time Reference Network (KyCORS) |
| Operator | KYTC; Trimble Pivot |
| landing_url | https://kycors.ky.gov/ — operator portal welcome |
| access_url | Skip — landing covers manual-approval workflow; routes pre-registration queries to `KYCORS_Admin@ky.gov` |
| host:port | `kycors.ky.gov:2101` — `SOURCETABLE 200 OK` 2026-05-18 (Trimble Caster 4.1) |
| num_stations | unknown — welcome does not enumerate; live ST advertises 6 mountpoints (all VRS / network-solution variants). ArcGIS metadata (`1ada443a5bc6432091d15ac8cf2ec5a0`) describes network but no verified station total |
| tariff | Free |
| vrs | VRS-only; recommended `RTX_RTCM3-2` (RTCM 3.2, GPS+GLO+GAL+BDS+QZS); legacy `VRS_RTCM3` GPS+GLO only. All mountpoints note "User ID Required" in field 18 |
| hobbyist_eligibility | Unclear — registration at `/RegisterAccount.aspx`; manual admin approval; no professional licence explicitly required. ("hobbyist use reported in community guides" claim retracted — no specific community guide URL retained in prior research; inference removed) |
| legal_residency_required | Unclear — admin approval = staff discretion |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (6 STR; NET line "KY Transportation Cabinet") |
| datum_epoch | omitted — no citable operator declaration |

Manual registration process — portal warns "DO NOT click REGISTER button more than once" and notes system "is often slow to respond". Contact `KYCORS_Admin@ky.gov` before registering if uncertain. Multiple rovers: indicate number needed in reply to confirmation email.

## Sources

- WVRTN portal: https://wvrtn.cors.us/
- WVRTN laserinst.com WVDOH VRS: https://www.laserinst.com/wvdohvrs
- E38 Survey Solutions — WV Emlid guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-west-virginia-ntrip-wvrtn
- NC RTN portal: https://rtn.nc.gov/
- NCGS CORS page: https://ncgs.state.nc.us/pages/CORS-and-GNSS.htm
- SCRTN portal: https://scrtn.sc.gov/
- SC RTN status (RFA): https://rfa.sc.gov/programs-services/geodetic/rtnstatus
- SC RTN Subscriber Agreement (04/2023): https://rfa.sc.gov/sites/default/files/2023-04/SCGS%20RTN%20Subscriber%20Agreement%204_2023.pdf
- FPRN (FDOT landing): https://www.fdot.gov/geospatial/fprn.shtm
- FPRN FAQ 2025 (datum + tariff + eligibility citation): https://www.myfloridagps.com/faq/fprnfaq2025.html
- FPRN FAQ (FDOT mirror, older NAD83-only): https://www.fdot.gov/Geospatial/fprnfaq.shtm
- E38 FL Emlid guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-florida-ntrip-fprn
- SparkFun FDOT discussion: https://community.sparkfun.com/t/fdot-maybe-the-new-golden-standard-for-a-statewide-ntrip-caster/67255
- AlCORS registration: https://aldotcors.dot.state.al.us/SBC/Account/Register
- AlCORS Emlid Community: https://community.emlid.com/t/alabama-cors-network/29310
- AlCORS RPLS forum: https://rpls.com/forums/gnss-geodesy/alabama-alcors/
- GCGC RTN USM operator (tariff citation): https://www.usm.edu/gulf-coast-geospatial-center/real_time_network.php
- GCGC RTN portal: http://rtn.usm.edu/
- TDOT GNSS Reference Network: https://www.tn.gov/tdot/engineering-division/geodetics/gnss-reference-network.html
- TDOT portal: https://portal.tndot.net/
- TDOT FY25 T&C: https://portal.tndot.net/FY_25_GNSS_TC_FINAL.pdf
- TDOT GNSS Network Change FAQ: https://www.tn.gov/content/dam/tn/tdot/geodetics/TDOT%20GNSS%20Network%20Change%20FAQ.pdf
- KyCORS portal: https://kycors.ky.gov/
- KyCORS ArcGIS item: https://www.arcgis.com/home/item.html?id=1ada443a5bc6432091d15ac8cf2ec5a0
- E38 KY Emlid guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-kentucky-ntrip-kycors
- eGPS GA: https://egps.net/netservices.html
- VDOT Survey Manual Ch5: https://www.vdot.virginia.gov/media/vdotvirginiagov/doing-business/technical-guidance-and-support/technical-guidance-documents/location-and-design/migrated/surveymanual/Chapter5_acc05112023_PM.pdf
- RPLS VA/DC/MD: https://rpls.com/forums/gnss-geodesy/rtk-networks-in-va-dc-md/
- EarthScope GNSS realtime: https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA: https://www.earthscope.org/nota/
- E38 state guide: https://e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state
- ArduSimple US RTK: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- ArduSimple GA: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-georgia/
- NTRIP-list NA: https://ntrip-list.com/north-america/
- NGS CORS FAQ (state RTK provider list — confirms AL, FL, KY, NC, SC, TN as state-listed; WV/MS listed): https://geodesy.noaa.gov/CORS/cors_faqs.shtml
- Probes 2026-05-18 (curl `--http0.9 -A 'NTRIP/1.0'`): wvrtn.cors.us:2101 OK 7 STR; scrtn.sc.gov:2101 OK 14 STR; rtn.usm.edu:2101 OK 14 STR; kycors.ky.gov:2101 OK 6 STR; 48.223.232.215:10000 OK 101 STR (FPRN); 205.172.52.26:10011 OK 10 STR + :10099 OK 158 STR (AlCORS); rtn.nc.gov:2101 timeout (portal HTTP 200); portal.tndot.net HTTP 302
