# US Midwest — NTRIP RTK Caster Research
**Date researched:** 2026-05-07

**States covered:** Ohio (OH), Indiana (IN), Michigan (MI), Wisconsin (WI), Minnesota (MN), Iowa (IA), Illinois (IL), Missouri (MO), North Dakota (ND), South Dakota (SD), Nebraska (NE), Kansas (KS)

## Status: MIXED — seven states have a free public state-operated caster (OH, IN, MI, WI, MN, IA, MO); Illinois CORS network is under construction (no live NTRIP as of 2026-05-07); ND, SD, NE, KS have no public state caster; EarthScope NOTA provides sparse single-base fallback region-wide

---

## Regional Baseline: EarthScope NOTA

| Field | Value |
|---|---|
| **Network** | Network of the Americas (NOTA) — EarthScope Consortium (formerly UNAVCO) |
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3 raw streams) |
| **tariff** | Free for non-commercial, scientific, educational, or humanitarian use (annual licence renewal, self-service); USD 1,000/seat/yr commercial |
| **VRS** | No — single-base streams only |
| **hobbyist_eligibility** | Yes — non-commercial licence explicitly available |
| **legal_residency_required** | No |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe) |
| **MW station notes** | NOTA has stations in ND, SD, KS, and scattered across the region at geodetic spacing (~200–400 km); too sparse for reliable real-time RTK in most scenarios; useful for PPK/static post-processing. Not a substitute for any of the state VRS networks below. |

---

## Per-State Summary Table

| State | Network | Operator | host:port | Tariff | VRS | Hobbyist | Probe result 2026-05-07 |
|---|---|---|---|---|---|---|---|
| OH | ODOT RTN | ODOT | `156.63.133.115:2101` (IP; DNS ortn.dot.state.oh.us — no longer resolves) | Free | Yes | Unclear (likely yes) | IP 156.63.133.115:2101 timeout from external (account-gated firewall likely); portal + ODOT sign-up form confirmed active |
| IN | InCORS | INDOT | not published; provided after User Agreement accepted; IP 108.59.49.226; Leica SBC port scheme | Free | Yes (iMAX/MAX) | Unclear (UA required; no professional licence field) | incors.in.gov HTTP redirect live; NTRIP port timeout from external |
| MI | MDOT CORS / MSRN | MDOT | `mdotcors.michigan.gov` Leica SBC; free ports 10010–10011 (GNSS RTCM3); IP 148.149.0.87 (historical) | Free | Yes (network NS-IMAX-MSM4) | Unclear (SBC account; no stated professional requirement) | mdotcors.michigan.gov:2101 timeout/Cloudflare; NTRIP ports blocked from external; portal confirmed active via mdotcors.michigan.gov/sbc |
| WI | WISCORS | WisDOT | `wiscors.dot.wi.gov:2101` (IP 165.189.65.133) | Free | Yes | Unclear (registration required; no professional licence stated) | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe) |
| MN | MnCORS | MnDOT | `mncors.dot.state.mn.us:9000` (IP 151.111.142.75); port 9000 (non-standard Trimble Pivot) | Free | Yes (VRS-only) | Unclear (registration required; no professional licence stated) | Port 9000 + port 2101 both timed out from external (likely account-gated or IP-filtered); mncors.dot.state.mn.us DNS resolves; portal login page confirmed accessible |
| IA | IaRTN | Iowa DOT | `165.206.203.10:10000` (IP + non-standard port; Leica SBC; iartnsbc.iowadot.gov web portal) | Free | Yes (iMAX network) | Unclear (registration required; no professional licence stated) | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe of IP:10000) |
| IL | IDOT CORS | IDOT | No public NTRIP endpoint — network under construction (Nov 2024 kickoff; ~70 sites planned) | Free (when complete) | Unknown | Unknown | N/A — no live caster as of 2026-05-07 |
| MO | MoDOT RTN | MoDOT | `gpsweb3.modot.mo.gov:2101` (= `rtk3.modot.mo.gov:2101`; IP 168.166.125.30) | Free | Yes | Unclear (notarised User Agreement required) | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe) |
| ND | None | — | — | — | — | — | No public state caster found |
| SD | None | — | — | — | — | — | No public state caster found |
| NE | None | — | — | — | — | — | No public state caster found |
| KS | None | — | — | — | — | — | No public state caster found |

**Regional baseline (all 12 states):** EarthScope NOTA — `ntrip.earthscope.org:2101` — free non-commercial, single-base streams only.

---

## OH — Ohio: ODOT RTN

| Field | Value |
|---|---|
| **Network name** | Ohio Real Time Network (ODOT RTN; previously ODOT VRS / ODOT CORS) |
| **Operator** | Ohio Department of Transportation (ODOT) — Engineering & Surveying; Trimble Pivot platform |
| **host:port** | IP `156.63.133.115:2101`; DNS `ortn.dot.state.oh.us` no longer resolves from external probe (2026-05-07); registration delivers confirmed credentials including current address |
| **tariff** | Free |
| **VRS** | Yes — VRS-only; mountpoints: `ODOT_G_R_E_C_RTX_RTCM3` (non-Trimble; multi-constellation GPS+GLO+GAL+BDS+L5) and `ODOT_G_R_E_C_RTX_CMRx` (Trimble) |
| **hobbyist_eligibility** | Unclear — registration via online access-request form at odot.formstack.com/forms/odot_cors_vrs_login; no professional licence field identified; "access request" framing is neutral |
| **legal_residency_required** | Unclear — no stated requirement |
| **last_confirmed_alive** | Portal (odot.formstack.com sign-up) active 2026-05-07; IP:2101 timeout from external (consistent with account-gated firewall; not indicative of service outage) |

### Context Notes

- Full multi-constellation (GPS, GLONASS, Galileo, BeiDou, L5) support added in 2024 following receiver and software upgrades. The network was previously GPS+GLONASS only.
- Contact: cors@dot.state.oh.us / Ohio Real-Time Network Administrator.
- Registration portal: https://odot.formstack.com/forms/odot_cors_vrs_login
- Legacy DNS ortn.dot.state.oh.us stopped resolving from external (2026-05-07 probe); credentials provided at registration include current active host address.

---

## IN — Indiana: InCORS

| Field | Value |
|---|---|
| **Network name** | Indiana Continuously Operating Reference System (InCORS) |
| **Operator** | Indiana Department of Transportation (INDOT) — Land & Aerial Survey Office; Leica Spider Business Center (SBC) platform |
| **host:port** | Not publicly documented; IP `108.59.49.226`; Leica SBC uses non-standard port scheme (historically ports 9000, 7071–7073, 10000); host and port provided to user after User Agreement is accepted |
| **tariff** | Free — "The Indiana Department of Transportation is providing access to the InCORS Network to any user recognizing the value of such a service at no charge" |
| **VRS** | Yes — iMAX and MAX network solutions; recommended mountpoint `RTCM3_MAX` (GPS+GLONASS); MSM4 full-constellation also available |
| **hobbyist_eligibility** | Unclear — User Agreement must be signed and returned by mail, fax, or email to incors@indot.in.gov; no professional licence field in the public agreement form; no stated restriction on individual users; "any user" language in policy suggests broad access |
| **legal_residency_required** | Unclear — no stated requirement |
| **last_confirmed_alive** | incors.in.gov HTTP 302/redirect to HTTPS confirmed 2026-05-07; NTRIP port timeout from external (expected — Leica SBC firewalled to registered accounts) |
| **station count** | 45 INDOT stations + 15 shared from neighbouring state networks (MI, OH, KY) = 60 total in solution |

### Context Notes

- User Agreement form: https://incors.in.gov/useragreement.pdf — sign, return by email to incors@indot.in.gov or mail to 120 South Shortridge Rd, Indianapolis IN 46219-6705.
- Activation is manual; credentials emailed after processing.
- Station map: https://incors.in.gov/map.html
- FTP RINEX archive (post-processing): https://ftp.incors.in.gov/

---

## MI — Michigan: MDOT CORS / MSRN

| Field | Value |
|---|---|
| **Network name** | Michigan Department of Transportation CORS / Michigan Statewide Reference Network (MDOT CORS / MSRN) |
| **Operator** | Michigan Department of Transportation (MDOT) — Leica Spider Business Center (SBC) platform |
| **host:port** | `mdotcors.michigan.gov` (Leica SBC web portal); IP `148.149.0.87` (MSRN NTRIP effective 2021-04-15); free GNSS RTCM3 RTK datastreams on ports 10010–10011; standard NTRIP port 2101 not confirmed available from external; `mdotcors.michigan.gov:2101` resolves via Cloudflare (104.18.35.27 / 172.64.152.229) but timed out from external (2026-05-07) |
| **tariff** | Free — "FREE access to all RTK datastreams and RINEX data streams for ports 10010–10011 on the MSRN Port Scheme" (MSRN Port Scheme documentation); also free access on legacy GPS/GNSS ports 10000–10006 |
| **VRS** | Yes — network-mode (iMAX equivalent); recommended mountpoint `NS-IMAX-MSM4` (RTCM3 MSM4 full constellation) |
| **hobbyist_eligibility** | Unclear — account registration at mdotcors.michigan.gov/sbc/Account/Register; Leica SBC registration form; no professional licence requirement found; user distribution historically ~60% survey, 29% agriculture, 11% GIS — no stated access restriction by user type |
| **legal_residency_required** | Unclear — no stated requirement |
| **last_confirmed_alive** | mdotcors.michigan.gov/sbc HTTP portal confirmed active 2026-05-07; NTRIP ports blocked from external probe (consistent with account-gated firewall) |
| **station count** | ~95 CORS stations statewide (MSRN) |

### Context Notes

- The MSRN Port Scheme (MSRN Port Scheme20210501.xlsx, published at mdotcors.michigan.gov) documents the full port-to-format mapping. Key free ports: 10010 (GNSS RTCM3 MSM4) and 10011 (GNSS CMRx).
- Access: account creation at mdotcors.michigan.gov → subscribe to MSM4 tier → retrieve NTRIP credentials from Account Details > User Profile.
- GGA position message must be sent to the server at least every 30 seconds (NTRIP requirement).
- The SBC domain mdotcors.org redirects to the Michigan-specific portal (not Michigan DOT CORS; note: mdotcors.org was previously Maryland-focused but Michigan MDOT holds this domain — confirmed by DNS resolving to 148.149.27.70).

---

## WI — Wisconsin: WISCORS

| Field | Value |
|---|---|
| **Network name** | Wisconsin Continuously Operating Reference Station Network (WISCORS) |
| **Operator** | Wisconsin Department of Transportation (WisDOT) — Trimble Pivot platform |
| **host:port** | `wiscors.dot.wi.gov:2101` (IP 165.189.65.133; previously 130.47.252.87, changed 2016) |
| **tariff** | Free |
| **VRS** | Yes — VRS-only; recommended mountpoint `RTCM32` (RTCM3, GPS+GLONASS+Galileo) |
| **hobbyist_eligibility** | Unclear — self-service registration at wiscorsweb.dot.wi.gov; username and password emailed after registration; no professional licence field identified |
| **legal_residency_required** | Unclear — no stated requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe of wiscors.dot.wi.gov:2101) |
| **station count** | 115+ permanent GNSS reference stations statewide |

### Context Notes

- Registration: https://wiscorsweb.dot.wi.gov/TrimblePivotWeb/RegisterAccount.aspx
- WISCORS FAQ (2023): wiscorsweb.dot.wi.gov/TrimblePivotWeb/documents/wiscors-faq.pdf
- Sensor map: https://wiscorsweb.dot.wi.gov/TrimblePivotWeb/Map/SensorMap.aspx
- Contact: wiscors@dot.wi.gov
- DNS alias is stable; users connecting via `wiscors.dot.wi.gov` (not IP) are automatically redirected if IP changes.

---

## MN — Minnesota: MnCORS

| Field | Value |
|---|---|
| **Network name** | Minnesota Continuously Operating Reference Station Network (MnCORS) |
| **Operator** | Minnesota Department of Transportation (MnDOT) — Trimble Pivot platform; cooperative with other state agencies, counties, cities, private partners |
| **host:port** | `mncors.dot.state.mn.us:9000` (IP 151.111.142.75; non-standard Trimble Pivot port); port 9000 and port 2101 both timed out from external probe — consistent with account-gated firewall |
| **tariff** | Free — "no subscription fee" (MnCORS FAQ) |
| **VRS** | Yes — VRS-only; mountpoints include `RTCM_32_NAD83(2011)` (RTCM3, multi-constellation); formats: RTCM 2.3, RTCM 3.1, RTCM 3.4, CMR+, CMRx |
| **hobbyist_eligibility** | Unclear — self-service registration at mncors.dot.state.mn.us; no professional licence requirement stated; accounts deactivated after 1 year of inactivity (≥1 second of use per year retains active status) |
| **legal_residency_required** | Unclear — no stated requirement |
| **last_confirmed_alive** | mncors.dot.state.mn.us DNS resolves to 151.111.142.75; MnDOT CORS page confirms ongoing service; 4 new northern stations added to network solutions in early 2026 (Stony River, Tofte, Seagull Lake Access, Gunflint Midtrail) |
| **station count** | 140+ reference stations statewide (including recent northern additions) |

### Context Notes

- Registration: at mncors.dot.state.mn.us → "MnCORS Data Access and User Management Website" → Register.
- Contact: CORSVRS.DOT@state.mn.us
- Network covers all of Minnesota including northern wilderness areas (Boundary Waters region); recent 2026 densification in northeastern MN.
- The non-standard port 9000 is typical of Trimble Pivot deployments and confirmed by multiple community sources.

---

## IA — Iowa: IaRTN

| Field | Value |
|---|---|
| **Network name** | Iowa Real-Time Network (IaRTN) |
| **Operator** | Iowa Department of Transportation (Iowa DOT) — Leica Spider Business Center (SBC) platform |
| **host:port** | IP `165.206.203.10:10000` (non-standard Leica SBC port; SOURCETABLE 200 OK confirmed 2026-05-07); web portal `iartnsbc.iowadot.gov` (port 2101 and port 80/443 timeout/403 from external — account-gated) |
| **tariff** | Free — "There are no current plans for the Iowa DOT to charge users to access the network, whether from the public or private sector" |
| **VRS** | Yes — iMAX network solution; recommended mountpoint `MSM_IMAX` (RTCM3 MSM4, full constellation) |
| **hobbyist_eligibility** | Unclear — online registration at iartnsbc.iowadot.gov/sbc/Account/Register; account activated within 2 working days after registration; no professional licence requirement found |
| **legal_residency_required** | Unclear — no stated requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe of 165.206.203.10:10000) |
| **station count** | 83 CORS stations placed at Iowa DOT maintenance facilities statewide |

### Context Notes

- Registration: https://iartnsbc.iowadot.gov/sbc/Account/Register — email, username, password self-service; credentials emailed within 2 business days.
- USDA NRCS Trimble configuration document confirms IP 165.206.203.10, port 10000, mountpoint `MSM_IMAX`.
- RINEX archive (post-processing): available through IaRTN portal post-login.
- Contact Iowa DOT Geodetics for access questions.

---

## IL — Illinois: No Active Public Caster (Network Under Construction)

**No public NTRIP RTK caster is operating as of 2026-05-07.**

IDOT launched a CORS network installation project in November 2024, funded by a $4.5 million federal Advanced Digital Construction Management Systems grant plus matching state funds (total $6.25 million). The eventual network will comprise approximately 70 sites statewide. IDOT has explicitly described it as "the first free public network of its kind in Illinois." No NTRIP endpoint, registration portal, or launch date has been published as of 2026-05-07.

### Most Recent Project Announcement

**IDOT CORS Network Installation Kickoff — November 2024:** Initial site installations in Litchfield, Petersburg, and Jacksonville. Once all ~70 statewide sites are installed, IDOT plans to operate a free public GNSS/RTK correction service. No NTRIP host or timeline confirmed.

Source: https://idot.illinois.gov/about-idot/stay-connected/idot-blog/cors-network-installation-kicks-off.html (observed 2026-05-07)

### Commercial Alternatives in Illinois

| Network | host:port | Tariff | VRS | Notes |
|---|---|---|---|---|
| **ReIL-NET** (Kara Company) | `caster.reil-net.com` ports 12050–12051 (network); 12054–12055 (SPS) | USD 200/month (observed 2026-05-07) | Yes — `VRS-RTCM3-MSM5` | 55+ base stations, Chicagoland and Central IL; Leica Spider |
| **Illinois Clearinghouse listed** | — | Various | — | MyWay RTK (agricultural); Trimble VRS Now (USA-wide, paid) |

Contact ReIL-NET: 708-482-8888 / karaco.com/pages/reil-net-rtk-network

---

## MO — Missouri: MoDOT RTN

| Field | Value |
|---|---|
| **Network name** | Missouri Department of Transportation Real-Time Network (MoDOT RTN) |
| **Operator** | Missouri Department of Transportation (MoDOT) — Trimble Pivot platform |
| **host:port** | `gpsweb3.modot.mo.gov:2101` (= `rtk3.modot.mo.gov:2101`; IP 168.166.125.30) |
| **tariff** | Free — "No, it is a free network" (MoDOT RTN FAQ) |
| **VRS** | Yes — VRS-only; mountpoints: `VRS_RTCM31` (RTCM 3.1, GPS+GLONASS — recommended for most equipment), `VRS_CMRplus`, `VRS_CRMx`, `VRS_RTCM21`, `VRS_RTCM23`, `RTCM3Net_Autocell` |
| **hobbyist_eligibility** | Unclear — User Agreement must be downloaded, signed, notarised, and submitted to MoDOT; agreement language refers to "company owner or officer" in FAQ guidance, but no professional licence requirement was found; individual users can sign as their own entity |
| **legal_residency_required** | Unclear — no stated requirement |
| **last_confirmed_alive** | `SOURCETABLE 200 OK` — 2026-05-07 (curl probe of gpsweb3.modot.mo.gov:2101 and rtk3.modot.mo.gov:2101) |
| **station count** | 78 GNSS CORS stations (NetR5 receivers with Zephyr Geodetic II antennas); max spacing 70 km; NGS CORS specifications |
| **constellations** | GPS + GLONASS (VRS_RTCM31 and CMR products); full-constellation support status unclear |

### Context Notes

- User Agreement: https://gpsweb3.modot.mo.gov/MODOT_RTK_GPS_USER_AGREEMENT.pdf — download, sign, notarise, return to MoDOT. MoDOT then grants access and emails credentials.
- MoDOT FAQ advises registering under a company/organisation name to avoid access loss from personnel changes; this does not explicitly prohibit individual registrations.
- Portal: https://gpsweb3.modot.mo.gov/
- Contact: GPS Utility Mapping System office via modot.org/gps-utility-mapping-system
- Covers all 114 Missouri counties including Kansas City and St. Louis metro areas.

---

## ND — North Dakota: No Public State Caster

No state DOT, university (UND, NDSU), or other public agency NTRIP RTK caster has been identified for North Dakota as of 2026-05-07. Multiple authoritative sources (GPS World Dec 2024 public RTK list, E38 Survey Solutions state-by-state guide, Point One Navigation state comparison) confirm "no public service" for ND.

**Gap:** EarthScope NOTA has stations in ND at geodetic spacing (too sparse for real-time RTK in most scenarios). Commercial alternatives: Trimble VRS Now (global, paid) and Midstates VRS (acquired by Trimble in 2020) previously covered ND and eastern SD — now integrated into Trimble Positioning Services / VRS Now. Pricing: agricultural tier ~USD 750/yr; survey/construction tier ~USD 1,650/yr (source: Agweek article on Midstates VRS acquisition, 2020).

---

## SD — South Dakota: No Public State Caster

No South Dakota DOT (SDDOT), South Dakota State University (SDSU), or other public agency NTRIP RTK caster has been identified for South Dakota as of 2026-05-07. GPS World (Dec 2024), E38 Survey Solutions, and Point One Navigation all confirm "no public service" for SD.

**Gap:** EarthScope NOTA has stations in SD. Commercial alternatives: Trimble VRS Now / Midstates VRS (formerly covered eastern SD with several hundred users; now under Trimble Positioning Services). TrueNav Tech (Sioux Falls, SD) provides physical (non-VRS) single-base NTRIP for SD, MN, IA, NE — pricing not published; contact jon@truenav.tech / 605-366-1322.

---

## NE — Nebraska: No Public State Caster

No Nebraska Department of Transportation (NDOT) or other public agency NTRIP RTK caster is available as of 2026-05-07. NDOT owns approximately 40 fixed GPS reference stations used internally but these are not networked as a public NTRIP service. GPS World (Dec 2024) lists NE as "no public service." Nebraska agriculture stakeholders have identified the absence of a public network as a significant gap, as farmers pay USD 1,000–1,500/tractor/yr for commercial subscriptions.

**Most Recent Announcement:** Nebraska RTK CORS modernisation initiative documented in an AGRAsoft white paper (agrasoft.net/info/nebraska-rtk-cors-modernization) — describes the problem and advocates for a public network, but no funded project or timeline exists as of 2026-05-07.

**Gap:** Commercial alternatives: Midwest RTK Network (mwrtk.net — Trimble Pivot portal, Seiler Instrument Company territory; site responds via DNS but NTRIP port not publicly confirmed). TrueNav Tech covers NE. Trimble VRS Now (national, paid).

---

## KS — Kansas: No Public State Caster

No Kansas Department of Transportation (KDOT) or other public agency NTRIP RTK caster has been identified for Kansas as of 2026-05-07. KDOT does not list a CORS or RTK network on its GIS resources page. GPS World (Dec 2024), E38 Survey Solutions, and Point One Navigation all confirm "no public service" for KS.

**Gap:** EarthScope NOTA has stations in KS. Commercial alternatives: RTK Premium (statewide, partial); Trimble VRS Now (national paid). SmartNet North America has an Oklahoma portal (smartnetna.com) with possible southern Kansas edge coverage.

---

## Post-Processing Fallback

| Service | Coverage | Cost |
|---|---|---|
| **NOAA NCN CORS** — static RINEX download (multiple stations per state) | All 12 states | Free; no account required |
| **EarthScope NOTA RINEX archive** | Stations in ND, SD, KS and sparse Midwest | Free non-commercial; account required |
| **IaRTN RINEX** | Iowa | Free; post-login access |
| **MDOT CORS RINEX** (virtual RINEX / VRS RINEX) | Michigan | Free; account required |
| **InCORS FTP** (ftp.incors.in.gov) | Indiana | Free; publicly accessible |

---

## Sources Consulted

- WISCORS portal: https://wiscorsweb.dot.wi.gov/trimblepivotweb/ (SOURCETABLE 200 OK confirmed 2026-05-07)
- WISCORS WisDOT page: https://wisconsindot.gov/Pages/doing-bus/eng-consultants/cnslt-rsrces/tools/wiscors/default.aspx
- WISCORS IP change notice (Seiler Geospatial): https://www.seilergeo.com/wiscors-ip-address-and-url-change-2/
- WISCORS station list: https://wisconsindot.gov/Pages/doing-bus/eng-consultants/cnslt-rsrces/tools/wiscors/stations.aspx
- WISCORS FAQ PDF (2023): https://wiscorsweb.dot.wi.gov/TrimblePivotWeb/documents/wiscors-faq.pdf
- InCORS main page: https://incors.in.gov/ (observed 2026-05-07)
- InCORS RTK page: https://incors.in.gov/rtk.aspx
- InCORS User Agreement: https://incors.in.gov/useragreement.pdf
- InCORS FTP: https://ftp.incors.in.gov/
- E38 Survey Solutions — InCORS guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-indiana-ntrip-incors
- MDOT CORS SBC portal: https://mdotcors.michigan.gov/sbc (observed 2026-05-07)
- MDOT CORS registration: https://mdotcors.michigan.gov/sbc/Account/Register
- MIDOT CORS UPDATE — Shawn Roy MSRN Administrator (presentation): https://slidetodoc.com/midot-cors-update-shawn-roy-midot-msrn-administrator/
- E38 Survey Solutions — MDOT CORS guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-michigan-ntrip-mdot-cors
- MnCORS main page: https://www.dot.state.mn.us/surveying/cors/index.html (observed 2026-05-07)
- MnCORS FAQ: https://www.dot.state.mn.us/surveying/cors/mncors_faq.html
- MnCORS portal: https://mncors.dot.state.mn.us/ (DNS resolves to 151.111.142.75)
- E38 Survey Solutions — MnCORS guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-minnesota-ntrip-mncors
- IaRTN Iowa DOT page: https://iowadot.gov/consultants-contractors/design/iowa-real-time-network
- IaRTN portal (SBC): https://iartnsbc.iowadot.gov/ (SOURCETABLE 200 OK on IP 165.206.203.10:10000 confirmed 2026-05-07)
- IaRTN FAQ: https://iowadot.gov/consultants-contractors/design/iowa-real-time-network/frequently-asked-questions
- USDA NRCS Trimble Access / IaRTN config guide: https://www.nrcs.usda.gov/sites/default/files/2022-11/Configure%20Trimble%20Access%20for%20Iowa%20RTN.pdf
- E38 Survey Solutions — IaRTN guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-iowa-ntrip-iartn
- ODOT RTN CORS page: https://dx-authoring.myohio.gov/wps/portal/gov/odot/working/engineering/cadd-mapping/survey/cors-rtn/ (observed 2026-05-07)
- ODOT VRS registration form: https://odot.formstack.com/forms/odot_cors_vrs_login
- Ohio Surveyor news — ODOT RTN multi-constellation: https://ohiosurveyor.org/aws/osps/pt/sd/news_article/350530/_PARENT/layout_details/false
- Laser Instruments ODOT VRS page: https://www.laserinst.com/odot-vrs/
- E38 Survey Solutions — ODOT VRS guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-connection-to-ohio-ntrip-odot-vrs
- MoDOT RTN FAQ: https://gpsweb3.modot.mo.gov/faq.html (observed 2026-05-07)
- MoDOT RTN portal: https://gpsweb3.modot.mo.gov/ (SOURCETABLE 200 OK on :2101 confirmed 2026-05-07)
- MoDOT User Agreement PDF: https://gpsweb3.modot.mo.gov/MODOT_RTK_GPS_USER_AGREEMENT.pdf
- MoDOT RTN completed announcement (American Surveyor): https://amerisurv.com/2010/02/23/missouri-dot-real-time-network-completed/
- MoDOT GPS Utility Mapping: https://www.modot.org/gps-utility-mapping-system
- RTKLIB issue #584 (MoDOT host/port): https://github.com/tomojitakasu/RTKLIB/issues/584
- Emlid Community — MoDOT VRS: https://community.emlid.com/t/missouri-dot-vrs/32478
- MoDOT Realtime Network Upgrade: https://www.modot.org/realtime-network-upgrade
- IDOT CORS kickoff blog post (Nov 2024): https://idot.illinois.gov/about-idot/stay-connected/idot-blog/cors-network-installation-kicks-off.html
- Illinois Clearinghouse — RTK networks: https://clearinghouse.isgs.illinois.edu/webdocs/ilhmp/reference.html
- ReIL-NET / Kara Company: https://www.karaco.com/pages/reil-net-rtk-network (observed 2026-05-07)
- E38 Survey Solutions — RTK access by state: https://e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state
- ArduSimple — US NTRIP casters: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- NTRIP-list.com North America: https://ntrip-list.com/north-america/ (observed 2026-05-07)
- GPS World public RTK list (Dec 2024): https://www.gpsworld.com/finally-a-list-of-public-rtk-base-stations-in-the-u-s/
- Point One Nav state pages: https://pointonenav.com/states/north-dakota/ · /south-dakota/ · /nebraska/ · /kansas/ · /michigan/ (observed 2026-05-07)
- AGRAsoft Nebraska RTK CORS: https://www.agrasoft.net/info/nebraska-rtk-cors-modernization
- TrueNav Tech: https://www.truenav.tech/ (observed 2026-05-07)
- Agweek — Midstates VRS / Trimble acquisition: https://www.agweek.com/business/midstates-vrs-launches-cellular-based-rtk
- Frontier Precision VRS services: https://frontierprecision.com/technical-services/value-added-services/vrs-services/
- EarthScope GNSS Realtime: https://www.earthscope.org/data/gnss-realtime/ (observed 2026-05-07)
- curl probes performed 2026-05-07:
  - `wiscors.dot.wi.gov:2101` — SOURCETABLE 200 OK
  - `gpsweb3.modot.mo.gov:2101` — SOURCETABLE 200 OK
  - `rtk3.modot.mo.gov:2101` — SOURCETABLE 200 OK
  - `165.206.203.10:10000` (IaRTN IP) — SOURCETABLE 200 OK
  - `ntrip.earthscope.org:2101` — SOURCETABLE 200 OK (connection established)
  - `incors.in.gov:80` — HTTP 302 redirect to HTTPS (server alive)
  - `incors.in.gov:2101` — timeout (account-gated)
  - `mncors.dot.state.mn.us:9000` — timeout (account-gated or IP-filtered)
  - `mncors.dot.state.mn.us:2101` — timeout
  - `mdotcors.michigan.gov:2101` / ports 10200–10700 — timeout (Cloudflare fronting)
  - `mdotcors.org:2101` — timeout
  - `156.63.133.115:2101` (Ohio ODOT IP) — timeout (account-gated)
  - `ortn.dot.state.oh.us` — DNS does not resolve from external (2026-05-07)
  - `iartnsbc.iowadot.gov:2101` — timeout
