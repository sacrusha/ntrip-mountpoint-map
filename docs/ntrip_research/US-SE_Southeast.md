# US Southeast — NTRIP RTK Caster Research
**States covered:** Virginia (VA), West Virginia (WV), North Carolina (NC), South Carolina (SC), Georgia (GA), Florida (FL), Alabama (AL), Mississippi (MS), Tennessee (TN), Kentucky (KY)
**Date researched:** 2026-05-07

## Status: MIXED — most states have an active public or state-operated caster; Virginia has no state caster; Georgia has no free public caster

---

## Regional Baseline: EarthScope NOTA

| Field | Value |
|---|---|
| **Network** | Network of the Americas (NOTA) — EarthScope Consortium (formerly UNAVCO) |
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3 raw streams) |
| **tariff** | Free for non-commercial, scientific, educational, or humanitarian use (annual licence renewal); USD 1,000/seat/yr commercial |
| **VRS** | No — single-base streams only (individual station mountpoints) |
| **hobbyist_eligibility** | Yes — non-commercial licence explicitly available; self-service at earthscope.org/user/licenses |
| **legal_residency_required** | No |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` returned on 2026-05-07 (curl probe) |
| **notes** | Old hostname `rtgpsout.earthscope.org` retired July 2025; new platform live April 2025. Provides sparse but geodetic-quality single-base streams in all 10 Southeast states. Not a substitute for a state VRS network but useful as a fallback where state networks are absent or inaccessible. |

---

## Virginia (VA)

**No state-operated public NTRIP RTK caster exists.**

VDOT attempted to build a statewide RTK network but abandoned the effort after litigation from Leica and Topcon, whose commercial subscription networks (e.g., SmartNet) were already operating in the state. As of 2026-05-07 no VDOT or other Virginia state-agency caster has been identified.

| Field | Value |
|---|---|
| **Active public caster** | No — no state or public-agency caster found |
| **host:port** | N/A |
| **tariff** | N/A |
| **VRS** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A |
| **Alternatives** | EarthScope NOTA (single-base, free non-commercial); KEYNET (commercial, covers MD + parts of VA); Leica SmartNet / Topcon TopNET (commercial, paid) |

### Context Notes

- VDOT Survey Manual (Chapter 5, last updated 2023) acknowledges the use of commercial RTK/VRS networks for contractor work but does not reference any VDOT-hosted caster. Contact: GeoSpatial-info@VDOT.virginia.gov.
- No VDOT or Virginia state-agency NTRIP endpoint was found in ntrip-list.com, the WVRTN cross-border listings, or RPLS forum discussions specific to VA.

---

## West Virginia (WV) — WVRTN

| Field | Value |
|---|---|
| **Network name** | West Virginia Real Time Network (WVRTN) |
| **Operator** | WV Dept. of Transportation — Information Technology Division, Highway Data Services Unit |
| **host:port** | `wvrtn.cors.us:2101` (also reachable at `34.228.171.115:2101`; caster port confirmed `206.212.1.199:2101` per WVDOT documentation) |
| **tariff** | Free |
| **VRS** | Yes — VRS-only; recommended mountpoint `rtxRTCM3_2` (RTCM3, multi-constellation); older GPS+GLONASS-only mountpoints also present |
| **hobbyist_eligibility** | Unclear — registration requires an organisation field; no professional licence stated as required; likely yes for any user with a valid email |
| **legal_residency_required** | Unclear — no stated residency requirement; registration open at wvrtn.cors.us/RegisterAccount.aspx |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` returned on 2026-05-07 (curl probe of `wvrtn.cors.us:2101`) |

### Context Notes

- 34 CORS stations; 2024 GeoCon presentation confirmed recent upgrade to Trimble Alloy receivers (multi-constellation expansion).
- For registration issues or support: WVRTNHelpDesk@wv.gov
- Backup / legacy hostname: `cors.us` (resolves to same IP as of 2026-05-07).

---

## North Carolina (NC) — NC RTN

| Field | Value |
|---|---|
| **Network name** | North Carolina GNSS CORS and Real-Time Network (NC RTN) |
| **Operator** | NC Geodetic Survey (NCGS) — a division of the NC Dept. of Environment and Natural Resources |
| **host:port** | `rtn.nc.gov:2101` — DNS resolves (`207.4.106.112`) but port 2101 timed out from external probe on 2026-05-07; web portal (port 443) active |
| **tariff** | Paid — first RTK login: USD 500 one-time fee; second login: included with first; subsequent logins: USD 250 each. CORS data download (static RINEX): free. Payment by cheque. |
| **VRS** | Yes — Trimble Pivot VRS network |
| **hobbyist_eligibility** | Unclear — registration requires an organisation; no professional licence explicitly required in public documentation; hobbyist access not prohibited but USD 500 entry cost is a practical barrier |
| **legal_residency_required** | Unclear — not stated in public materials |
| **last_confirmed_alive** | Portal at rtn.nc.gov returned HTTP 200 on 2026-05-07; NTRIP port 2101 timed out (may be restricted to credentialled connections / IP filtering) |

### Context Notes

- Fees are one-time (perpetual login credentials), not annual — making NC RTN comparatively cost-effective for frequent users once the upfront fee is paid.
- Invoicing occurs in the first week of the month following account creation.
- Station map: rtn.nc.gov/Map/SensorMap.aspx

---

## South Carolina (SC) — SCRTN

| Field | Value |
|---|---|
| **Network name** | South Carolina Real Time Network (SCRTN) |
| **Operator** | SC Revenue and Fiscal Affairs Office — SC Geodetic Survey |
| **host:port** | `scrtn.sc.gov:2101` — `SOURCETABLE 200 OK` returned on 2026-05-07 (curl probe) |
| **tariff** | Paid — first subscription: USD 1,200; additional subscriptions by same subscriber: USD 600 each. Payment due at time of application; no refunds. (Source: SCGS RTN Subscriber Agreement, rev. 04/2023) |
| **VRS** | Yes — Trimble Pivot VRS; 43 GNSS receivers in SC plus 2 receivers in GA and 10 in NC |
| **hobbyist_eligibility** | Unclear — subscriber agreement implies professional/business context; no explicit exclusion of individuals but USD 1,200 entry cost and formal agreement deter casual use |
| **legal_residency_required** | Unclear — no stated residency requirement found |
| **last_confirmed_alive** | 2026-05-07 (curl probe of scrtn.sc.gov:2101 — SOURCETABLE 200 OK) |

### Context Notes

- Satellite constellations: GPS, GLONASS, Galileo, BeiDou.
- Stated accuracy: ~2 cm horizontal, ~4 cm vertical.
- Registration: sc.accessgov.com/rfa/Forms/Page/rfa/scrtn/ (not through scrtn.sc.gov directly).

---

## Georgia (GA)

**No free public state-operated NTRIP RTK caster exists.**

GDOT does not operate a public CORS RTK network. The only identified network with Georgia coverage is the commercial eGPS Solutions RTN (Norcross, GA).

| Field | Value |
|---|---|
| **Active public caster** | No — no state or university free-public caster found |
| **host:port** | N/A (state); eGPS contact: info@egps.net / 770-695-3361 |
| **tariff — eGPS** | Plan A (dual network): USD 2,475/yr; Plan B (VRS only): USD 1,650/yr; Plan C (Flex): USD 50/day capped USD 400/mo; Plan D (Agriculture): USD 1,000/yr (source: egps.net/netservices.html, observed 2026-05-07) |
| **VRS — eGPS** | Yes — GEO++ and eGPS VRS network products |
| **hobbyist_eligibility — eGPS** | Unclear — no hobbyist tier listed; minimum Plan C at USD 50/day |
| **legal_residency_required** | N/A (state); unclear (eGPS) |
| **last_confirmed_alive** | eGPS website HTTP 200 on 2026-05-07; no NTRIP port probe possible (host not published) |

### Context Notes

- GDOT explicitly prohibits RTK from being used to establish project control values, which may explain the absence of a state-funded public RTK network.
- EarthScope NOTA provides sparse single-base streams in Georgia (free non-commercial).
- The GCGC RTN (rtn.usm.edu), operated by the University of Southern Mississippi, is a Mississippi network; its coverage does not extend meaningfully into Georgia.

---

## Florida (FL) — FPRN

| Field | Value |
|---|---|
| **Network name** | Florida Permanent Reference Network (FPRN) |
| **Operator** | Florida Dept. of Transportation (FDOT) — Geospatial office |
| **host:port** | `www.myfloridagps.com` / IP `40.121.5.206`; NTRIP port scheme via myfloridagps.com/links/2025products.pdf (port 10000 series for network RTK; port scheme not directly confirmed by probe — port 10000 timed out from this network on 2026-05-07) |
| **tariff** | Free — FDOT states "currently there are no plans to charge users for any FPRN services or products" (FAQ 2025) |
| **VRS** | Yes — VRS, iMAX, MAX, FKP; VRS mountpoint `RTCM3_VRS` confirmed in user guides; formats: RTCM 2.3, RTCM 3.1, CMR+, RTCM 3.3 MSM4 |
| **hobbyist_eligibility** | Yes — "Anyone with a NTRIP ready GPS/GNSS Receiver" and internet access; no equipment brand restrictions |
| **legal_residency_required** | No — registration at myfloridagps.com/sbc; no Florida residency requirement stated |
| **last_confirmed_alive** | Website (myfloridagps.com) active 2026-05-07; FPRN FAQ updated 2025; IP port 10000 timed out from external probe (likely IP-restricted; service confirmed active by user community reports) |

### Context Notes

- ~100 dual-frequency GNSS receivers statewide; one account required per rover.
- Registration: myfloridagps.com/sbc/Account/Register; account activation within 24–48 hours.
- FPRN is widely regarded as a model state public RTK service — no fees, no professional requirement, broad constellation support.
- Station map: myfloridagps.com/DMap/

---

## Alabama (AL) — ALDOT CORS (AlCORS)

| Field | Value |
|---|---|
| **Network name** | Alabama Department of Transportation CORS Network (ALDOT CORS / AlCORS) |
| **Operator** | Alabama Dept. of Transportation (ALDOT) — Leica SpiderNet platform |
| **host:port** | `aldotcors.dot.state.al.us` / IP `205.172.52.25`; primary NTRIP port is **not** 2101 (timed out); secondary IP `205.172.52.26:10099` returned `SOURCETABLE 200 OK` on 2026-05-07; reported user ports: 10011, 10099 (Leica SpiderNet non-standard ports) |
| **tariff** | Free — confirmed free of charge in multiple surveying community sources (rpls.com, Emlid community) |
| **VRS** | Unclear — user reports reference `LeicaMAX` mountpoint (network solution type) which implies network RTK; VRS specifically not confirmed |
| **hobbyist_eligibility** | Unclear — registration form requires Company field (Leica SBC platform); no professional licence stated as required; hobbyists have successfully registered per community reports |
| **legal_residency_required** | Unclear — no stated residency requirement |
| **last_confirmed_alive** | `205.172.52.26:10099` — `SOURCETABLE 200 OK` on 2026-05-07; web portal aldotcors.dot.state.al.us returns HTTP 200 |

### Context Notes

- ALDOT transitioned from a legacy TCP-based interface to a Leica Spider Business Center (SBC) web portal circa 2022 ("NEW ALDOT NTRIP SETTINGS" YouTube guide, August 2022). Old TCP connections no longer supported.
- Registration: aldotcors.dot.state.al.us/SBC/Account/Register
- Portal management: aldotcors.dot.state.al.us/SBC/Account/Index
- Reported working mountpoint: `LeicaMAX`; also `ALGR_RTCM3`.
- The non-standard port (`10099`) is typical of Leica SpiderNet deployments; standard NTRIP port 2101 is firewalled.

---

## Mississippi (MS) — GCGC RTN

| Field | Value |
|---|---|
| **Network name** | Gulf Coast Geospatial Center Real Time Network (GCGC RTN) |
| **Operator** | University of Southern Mississippi — Gulf Coast Geospatial Center (GCGC) |
| **host:port** | `rtn.usm.edu:2101` — `SOURCETABLE 200 OK` returned on 2026-05-07 (curl probe) |
| **tariff** | Free — "Use of the network is free of charge" (USM GCGC website) |
| **VRS** | Unclear — Trimble Pivot platform supports VRS; specific VRS mountpoints not confirmed in public documentation; the Reference Data Shop does produce virtual RINEX files |
| **hobbyist_eligibility** | Yes — open registration at rtn.usm.edu/RegisterAccount.aspx; no professional licence requirement stated |
| **legal_residency_required** | No — registration open to anyone |
| **last_confirmed_alive** | 2026-05-07 (curl probe of rtn.usm.edu:2101 — SOURCETABLE 200 OK) |

### Context Notes

- 52 CORS stations covering Mississippi; network established 2005 under NOAA/NGS national initiative.
- Serves: surveying, engineering, transportation, precision agriculture, emergency management, scientific research.
- Contact: debra.armstead@usm.edu / 228.276.1733
- Coverage is Mississippi-focused; does not extend into Georgia or other adjacent states.

---

## Tennessee (TN) — TDOT GNSS Reference Network

| Field | Value |
|---|---|
| **Network name** | TDOT GNSS Reference Network |
| **Operator** | Tennessee Dept. of Transportation (TDOT) — Geodetics Division; Leica-based platform (migrated Feb 2025) |
| **host:port** | Not publicly documented; provided to subscribers post-payment via portal.tndot.net account management; `portal.tndot.net:2101` timed out on external probe 2026-05-07 |
| **tariff** | Paid — USD 450 per fiscal year (FY25 contract, source: portal.tndot.net/FY_25_GNSS_TC_FINAL.pdf); payment by credit/debit card via portal |
| **VRS** | Yes — confirmed (Leica network platform provides VRS and network solutions) |
| **hobbyist_eligibility** | Unclear — subscription terms and conditions require formal agreement; USD 450/yr fee is a moderate barrier; no professional licence explicitly required |
| **legal_residency_required** | Unclear — not stated in public materials; Tennessee state portal, but no residency clause confirmed |
| **last_confirmed_alive** | portal.tndot.net HTTP 200 on 2026-05-07; subscription purchase page active |

### Context Notes

- TDOT replaced its legacy Trimble-based CORS network with a Leica-based system; migration completed February 1, 2025. Pre-existing Trimble credentials no longer valid after that date.
- New users: create account at portal.tndot.net → accept T&C → pay → receive credentials.
- Status page: status.tndot.net
- Topcon received the original TDOT CORS contract; Leica received the subsequent contract per bidnetdirect.com listing.

---

## Kentucky (KY) — KyCORS

| Field | Value |
|---|---|
| **Network name** | Kentucky Real Time Reference Network (KyCORS) |
| **Operator** | Kentucky Transportation Cabinet (KYTC) — Trimble Pivot platform |
| **host:port** | `kycors.ky.gov:2101` — `SOURCETABLE 200 OK` returned on 2026-05-07 (curl probe) |
| **tariff** | Free |
| **VRS** | Yes — VRS-only; recommended mountpoint `RTX_RTCM3_2` (RTCM3, multi-constellation) |
| **hobbyist_eligibility** | Unclear — registration at kycors.ky.gov/RegisterAccount.aspx; form is not automated (manual admin approval); no professional licence explicitly required; hobbyist use reported in community guides |
| **legal_residency_required** | Unclear — no stated residency requirement; admin approval process may exercise discretion |
| **last_confirmed_alive** | 2026-05-07 (curl probe of kycors.ky.gov:2101 — SOURCETABLE 200 OK) |

### Context Notes

- Registration is a manual process — the site warns "DO NOT click REGISTER button more than once" and notes the system "is often slow to respond." Contact KYCORS_Admin@ky.gov before registering if uncertain.
- If access for multiple rovers is needed, indicate number needed in reply to confirmation email.
- ArcGIS metadata: arcgis.com item ID 1ada443a5bc6432091d15ac8cf2ec5a0

---

## Per-State Summary Table

| State | Network | Operator | host:port | Tariff | VRS | Hobbyist eligible | Caster alive 2026-05-07 |
|---|---|---|---|---|---|---|---|
| VA | None | — | — | — | — | — | N/A |
| WV | WVRTN | WVDOT | `wvrtn.cors.us:2101` | Free | Yes | Unclear (likely yes) | Yes (SOURCETABLE confirmed) |
| NC | NC RTN | NC Geodetic Survey | `rtn.nc.gov:2101` | USD 500 one-time | Yes | Unclear | Portal active; NTRIP port IP-filtered |
| SC | SCRTN | SC Geodetic Survey | `scrtn.sc.gov:2101` | USD 1,200 first; USD 600 add'l | Yes | Unclear | Yes (SOURCETABLE confirmed) |
| GA | None | — | — | — | — | — | N/A |
| FL | FPRN | FDOT | `www.myfloridagps.com` / IP `40.121.5.206` (non-std ports) | Free | Yes | Yes | Website active; port scheme via products PDF |
| AL | AlCORS | ALDOT | `aldotcors.dot.state.al.us` (port 10099) | Free | Unclear | Unclear (likely yes) | Yes (SOURCETABLE on 205.172.52.26:10099) |
| MS | GCGC RTN | Univ. Southern Mississippi | `rtn.usm.edu:2101` | Free | Unclear | Yes | Yes (SOURCETABLE confirmed) |
| TN | TDOT GNSS RTN | TDOT | Not public (via portal.tndot.net) | USD 450/yr | Yes | Unclear | Portal active |
| KY | KyCORS | KYTC | `kycors.ky.gov:2101` | Free | Yes | Unclear (likely yes) | Yes (SOURCETABLE confirmed) |

**Regional baseline (all 10 states):** EarthScope NOTA — `ntrip.earthscope.org:2101` — free non-commercial, single-base streams only.

---

## Sources Consulted

- WVRTN portal: https://wvrtn.cors.us/
- WVRTN Laser Instruments page: https://www.laserinst.com/wvdohvrs
- E38 Survey Solutions — West Virginia NTRIP guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-west-virginia-ntrip-wvrtn
- West Virginia GeoCon 2024 session: https://julnet.swoogo.com/wvgeocon24/session/2152037/the-wvrtn-cors-network
- NC RTN portal: https://rtn.nc.gov/
- NC Geodetic Survey CORS page: https://ncgs.state.nc.us/pages/CORS-and-GNSS.htm
- SCRTN portal: https://scrtn.sc.gov/
- SC RTN status (RFA): https://rfa.sc.gov/programs-services/geodetic/rtnstatus
- SC RTN Subscriber Agreement (04/2023): https://rfa.sc.gov/sites/default/files/2023-04/SCGS%20RTN%20Subscriber%20Agreement%204_2023.pdf
- FPRN (FDOT): https://www.fdot.gov/Geospatial/fprn.shtm
- FPRN FAQ 2025: https://www.myfloridagps.com/faq/fprnfaq2025.html
- FPRN FAQ (FDOT mirror): https://www.fdot.gov/Geospatial/fprnfaq.shtm
- E38 Survey Solutions — Florida NTRIP guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-florida-ntrip-fprn
- SparkFun FDOT discussion: https://community.sparkfun.com/t/fdot-maybe-the-new-golden-standard-for-a-statewide-ntrip-caster/67255
- ALDOT CORS registration: https://aldotcors.dot.state.al.us/SBC/Account/Register
- ALDOT CORS Emlid Community discussion: https://community.emlid.com/t/alabama-cors-network/29310
- AlCORS RPLS forum: https://rpls.com/forums/gnss-geodesy/alabama-alcors/
- GCGC RTN (USM): https://www.usm.edu/gulf-coast-geospatial-center/real_time_network.php
- GCGC RTN portal: http://rtn.usm.edu/
- TDOT GNSS Reference Network: https://www.tn.gov/tdot/engineering-division/geodetics/gnss-reference-network.html
- TDOT GNSS Portal: https://portal.tndot.net/
- TDOT FY25 Terms & Conditions: https://portal.tndot.net/FY_25_GNSS_TC_FINAL.pdf
- TDOT GNSS Network Change FAQ: https://www.tn.gov/content/dam/tn/tdot/geodetics/TDOT%20GNSS%20Network%20Change%20FAQ.pdf
- KyCORS portal: https://kycors.ky.gov/
- KyCORS ArcGIS item: https://www.arcgis.com/home/item.html?id=1ada443a5bc6432091d15ac8cf2ec5a0
- E38 Survey Solutions — Kentucky NTRIP guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-kentucky-ntrip-kycors
- eGPS Solutions Georgia RTN: https://egps.net/netservices.html
- VDOT Survey Manual Chapter 5: https://www.vdot.virginia.gov/media/vdotvirginiagov/doing-business/technical-guidance-and-support/technical-guidance-documents/location-and-design/migrated/surveymanual/Chapter5_acc05112023_PM.pdf
- RPLS forums — VA/DC/MD RTK networks: https://rpls.com/forums/gnss-geodesy/rtk-networks-in-va-dc-md/
- EarthScope GNSS realtime data: https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA: https://www.earthscope.org/nota/
- E38 Survey Solutions — RTK access by state: https://e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state
- ArduSimple — US RTK casters: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- ArduSimple — Georgia RTK casters: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-georgia/
- NTRIP-list.com North America: https://ntrip-list.com/north-america/
- curl probes of all hostnames listed — 2026-05-07
