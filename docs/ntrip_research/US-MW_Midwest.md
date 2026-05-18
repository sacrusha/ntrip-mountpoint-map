# US Midwest [US-MW] — NTRIP RTK Caster Research

**States:** OH, IN, MI, WI, MN, IA, IL, MO, ND, SD, NE, KS

## Status (region)

7/12 states run free public state caster (OH, IN, MI, WI, MN, IA, MO). IL caster under construction since Nov 2024 — no live NTRIP. ND, SD, NE, KS = no public state caster. EarthScope NOTA = sparse single-base fallback (geodetic spacing, not real-time RTK substitute). NSRS modernisation (NATRF2022 / NAPGD2022) FGCS vote scheduled Feb 2026 (Federal Register 2024-10-09); NGS-led CORS rollout mid-late 2026, state DOTs expected to publish parallel mountpoints during transition.

## Per-state summary

| State | Network | Operator | host:port | Tariff | VRS | Hobbyist | Live probe |
|---|---|---|---|---|---|---|---|
| OH | ODOT RTN | ODOT | `156.63.133.115:2101` (DNS `ortn.dot.state.oh.us`) | Free | Yes | ? | Pipeline OK 2026-05-06; external blocked (IP allowlist) |
| IN | InCORS | INDOT | not published; IP `108.59.49.226`; Leica SBC ports 7071-7073/9000/10000 post-UA | Free | Yes (iMAX/MAX) | ? | Portal HTTP 302; NTRIP firewalled (account-gated) |
| MI | MDOT CORS / MSRN | MDOT | `mdotcors.michigan.gov`; Leica SBC; free GNSS RTCM3 ports 10010/10011 | Free | Yes (NS-IMAX-MSM4) | ? | Portal HTTP 200; NTRIP firewalled (account-gated) |
| WI | WISCORS | WisDOT | `wiscors.dot.wi.gov:2101` (165.189.65.133) | Free | Yes (Trimble Pivot VRS) | ? | `SOURCETABLE 200 OK` 9 STR |
| MN | MnCORS | MnDOT | `mncors.dot.state.mn.us:9000` (151.111.142.75; non-std Trimble Pivot port) | Free | Yes (VRS-only) | ? | Pipeline OK 2026-05-06; external TCP blocked |
| IA | IaRTN | Iowa DOT | `165.206.203.10:10000` (Leica SBC); web `iartnsbc.iowadot.gov` | Free | Yes (iMAX) | ? | `SOURCETABLE 200 OK` 9 STR |
| IL | IDOT CORS | IDOT | none — network under construction (kickoff Nov 2024) | TBD free | ? | ? | N/A |
| MO | MoDOT RTN | MoDOT | `gpsweb3.modot.mo.gov:2101` (alias `rtk3.modot.mo.gov`; 168.166.125.30) | Free | Yes | ? (notarised UA) | `SOURCETABLE 200 OK` 8 STR |
| ND | — | — | — | — | — | — | NOTA only |
| SD | — | — | — | — | — | — | NOTA only |
| NE | — | — | — | — | — | — | NEBRS = post-processing only; NDOT internal-only |
| KS | — | — | — | — | — | — | NOTA only |

Hobbyist `?` = no explicit eligibility statement; no professional-licence field; no user-type restriction. Treat as permissive-but-unconfirmed.

## Regional baselines: federal

**EarthScope NOTA** — see `US-NOTA_NetworkOfTheAmericas.md`. MW coverage sparse single-base (~200–400 km spacing) all 12 states; geodetic-grade, not real-time RTK substitute. Per-state lookup `py scripts/stations_by_country.py US --source earthscope`.

**NPS CORS** — see `US-NPS_NationalParkService.md` (`rtk.nps.gov:2101`, manual provisioning, free, single-base). MW stations include Indiana Dunes, Voyageurs, Theodore Roosevelt etc. Per-radius `py scripts/stations_by_radius.py <lat> <lon> <km>`.

## OH — Ohio: ODOT RTN

| Field | Value |
|---|---|
| Network | Ohio Real Time Network (ex-ODOT VRS) |
| Operator | ODOT Engineering & Surveying; Trimble Pivot |
| landing_url | https://geodesy.noaa.gov/CORS/cors_faqs.shtml — NGS CORS state-provider FAQ (lists OH state RTK provider). Most-official third-party fallback; operator-owned landing absent — `transportation.ohio.gov/working/engineering/cadd-mapping/survey/cors-rtn` HTTP 404 2026-05-18 (entire `/working/engineering/` tree gone in ODOT site reorg, no operator-side successor surfaced); operator subdomain `ortn.dot.state.oh.us/TrimblePivotWeb/` is bare Trimble Pivot Login (excluded by landing_url spec; IP-allowlist gated externally) |
| access_url | https://ortn.dot.state.oh.us/TrimblePivotWeb/Login.aspx (Trimble Pivot Web; account-gated) |
| host:port | `156.63.133.115:2101` (DNS `ortn.dot.state.oh.us`) |
| tariff | Free |
| vrs | VRS-only. Mountpoints: `ODOT_G_R_E_C_RTX_RTCM3` (non-Trimble, GPS+GLO+GAL+BDS+L5), `ODOT_G_R_E_C_RTX_CMRx` (Trimble). Full-constellation rollout per 2021-02-02 ohiosurveyor.org notice |
| num_stations | 61 GNSS incl. cross-border data-share (Amerisurv 2020). No newer operator enumeration; sensor map account-gated |
| hobbyist_eligibility | ? — access-request form, no professional-licence field |
| legal_residency_required | ? |
| last_confirmed_alive | 2026-05-06 — pipeline `SOURCETABLE 200 OK`. External probes blocked (IP allowlist) |
| datum_epoch | omitted — operator portal (Trimble Pivot Login) account-gated; ODOT transportation.ohio.gov `/working/engineering/cadd-mapping/survey/cors-rtn` landing page HTTP 404 2026-05-18 (entire `/working/engineering/` tree removed in site reorg); no citable datum declaration located; ODOT Survey Manual / ODOT geodetics index not exhaustively searched for an ODOT-internal datum spec |

Contact: `cors@dot.state.oh.us`. Reseller (training/support): Laser Instruments / Precision Laser & Instrument.

## IN — Indiana: InCORS

| Field | Value |
|---|---|
| Network | Indiana Continuously Operating Reference System |
| Operator | INDOT, Land & Aerial Survey Office; Leica SBC |
| landing_url | https://incors.in.gov/ |
| access_url | https://incors.in.gov/useragreement.pdf (signed UA returned to `incors@indot.in.gov`) |
| host:port | not published; IP `108.59.49.226`; SBC ports 9000, 7071-7073, 10000 emailed after activation — port list carried from prior research, no operator-public citation located on incors.in.gov; non-standard Leica SBC range 7071-7073 unusual, treat as best-available pointer until operator email confirms |
| tariff | Free — "any user recognizing the value of such a service at no charge" |
| vrs | Yes — iMAX + MAX. Recommended `RTCM3_MAX` (GPS+GLO); MSM4 full-constellation available. 4-constellation network-wide since 2024-06-18 station upgrade |
| num_stations | 45 INDOT + 15 cross-state (MI/OH/KY) = 60 in solution |
| hobbyist_eligibility | ? — "any user" language; no professional-licence field; mailed UA |
| legal_residency_required | ? |
| last_confirmed_alive | 2026-05-18 — `incors.in.gov` socket connection closed unexpectedly (HTTPS unreachable from sandbox; was HTTP 302 on 2026-05-07; transient or new outage). NTRIP ports account-gated regardless. Pipeline (NTRIP) status independent of portal availability |
| datum_epoch | omitted — operator portal landing + linked Station Updates page + user agreement PDF checked, no citable datum declaration found; INDOT Land & Aerial Survey Office page / Indiana Geographic Information Council resources not exhaustively searched for an INDOT-internal datum spec |

Credentials emailed after manual activation. Station updates: https://incors.in.gov/Station%20Updates.html. Public RINEX FTP: https://ftp.incors.in.gov/

## MI — Michigan: MDOT CORS / MSRN

| Field | Value |
|---|---|
| Network | Michigan Statewide Reference Network (MSRN) under MDOT CORS |
| Operator | MDOT; Leica SBC |
| landing_url | https://mdotcors.michigan.gov/sbc |
| access_url | https://mdotcors.michigan.gov/sbc/Account/Register |
| host:port | `mdotcors.michigan.gov`; free GNSS RTCM3 on ports 10010 (MSM4), 10011 (CMRx); legacy GPS/GNSS ports 10000-10006; IP `148.149.0.87` |
| tariff | Free — documented MSRN Port Scheme: free access all RTK + RINEX streams |
| vrs | Yes — iMAX-equivalent network solution; recommended `NS-IMAX-MSM4` |
| num_stations | ~95 statewide |
| hobbyist_eligibility | ? — historical user mix ~60% survey / 29% ag / 11% GIS; no stated restriction |
| legal_residency_required | ? |
| last_confirmed_alive | 2026-05-07 — portal HTTP 200; NTRIP ports firewalled to registered accounts (expected) |
| datum_epoch | omitted — operator Leica SBC portal returns HTTP 403 to scripted probes 2026-05-18 (anti-bot); landing page reachable but no datum text observed in cached fetches; no separate MDOT geodetics FAQ page located. Flag as operator-FAQ-not-located |

GGA every 30s required. Alt domain `mdotcors.org` redirects to Michigan portal (148.149.27.70). Not Maryland (frequent confusion in third-party listings).

## WI — Wisconsin: WISCORS

| Field | Value |
|---|---|
| Network | Wisconsin Continuously Operating Reference Station Network |
| Operator | WisDOT; Trimble Pivot |
| landing_url | https://wisconsindot.gov/Pages/doing-bus/eng-consultants/cnslt-rsrces/tools/wiscors/default.aspx — WisDOT page; HTTP 200 2026-05-18. Earlier-cited `/Pages/doing-business/...` slug is 404 (WisDOT path uses `doing-bus`, not `doing-business`) |
| access_url | https://wiscorsweb.dot.wi.gov/TrimblePivotWeb/RegisterAccount.aspx |
| host:port | `wiscors.dot.wi.gov:2101` (165.189.65.133; was 130.47.252.87 pre-2016) |
| tariff | Free |
| vrs | VRS-only. Recommended `RTCM32` (GPS+GLO+GAL). `CMRxGNSS` added 2024 for Trimble (full multi-constellation incl. BeiDou; Seiler Geospatial 2024) |
| num_stations | 115+ statewide |
| hobbyist_eligibility | ? — self-service registration; credentials emailed; no professional-licence field |
| legal_residency_required | ? |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (9 STR; Trimble Caster 5.3) |
| datum_epoch | NAD83(2011) Epoch 2010.00 — WISCORS FAQ explicit (Q "What is the current Horizontal Reference Frame and Adjustment associated with WISCORS?"): "As of March 2013, the WISCORS Network base station coordinates are closely aligned with the North American Datum of 1983 (2011) epoch 2010.00. NAD83(2011)". Citation: https://wiscorsweb.dot.wi.gov/TrimblePivotWeb/documents/wiscors-faq.pdf (rev. 2023-02-27) |

Contact: `wiscors@dot.wi.gov`. FAQ PDF: https://wiscorsweb.dot.wi.gov/TrimblePivotWeb/documents/wiscors-faq.pdf

## MN — Minnesota: MnCORS

| Field | Value |
|---|---|
| Network | Minnesota Continuously Operating Reference Station Network |
| Operator | MnDOT; Trimble Pivot. Cooperative w/ counties/cities/private partners |
| landing_url | https://www.dot.state.mn.us/surveying/cors/index.html |
| access_url | https://mncors.dot.state.mn.us/ (Register link in portal) |
| host:port | `mncors.dot.state.mn.us:9000` (151.111.142.75; non-std Trimble Pivot port) |
| tariff | Free — "No" subscription fee (MnCORS FAQ) |
| vrs | VRS-only. Example `RTCM_32_NAD83(2011)`. Also CMR+/CMRx + legacy RTCM 2.3/3.1 |
| num_stations | "Over 140 known positions" total in cooperative broadcast (MnDOT landing 2026-05-18 verbatim: "receivers at over 140 known positions"). Of those, 55 are NGS-certified MnCORS-owned sites (MnCORS FAQ: "55 of which are a part of the MnCORS network"); remainder = partner contributions (counties, cities, private). 4 northern additions (Stony River, Tofte, Seagull Lake Access, Gunflint Midtrail) early 2026 (Feb 2025 MnDOT bulletin) |
| hobbyist_eligibility | ? — self-service registration; "subscription remains active as long as you use it at least a few seconds a year" |
| legal_residency_required | ? |
| last_confirmed_alive | 2026-05-06 — pipeline `SOURCETABLE 200 OK`; external TCP blocked (IP allowlist) |
| datum_epoch | NAD83(2011) Epoch 2010.00 — MnCORS FAQ explicit: "NAD83(2011) (Epoch 2010.00)" as primary adjustment (NAD83(1996) alternatives also available). Citation: https://www.dot.state.mn.us/surveying/cors/mncors_faq.html |

Contact: `CORSVRS.DOT@state.mn.us`. 2026 northern densification covers Boundary Waters corridor.

## IA — Iowa: IaRTN

| Field | Value |
|---|---|
| Network | Iowa Real-Time Network |
| Operator | Iowa DOT; Leica SBC |
| landing_url | https://iowadot.gov/consultants-contractors/design/iowa-real-time-network |
| access_url | https://iartnsbc.iowadot.gov/sbc/Account/Register |
| host:port | `165.206.203.10:10000` (Leica SBC). Web portal `iartnsbc.iowadot.gov` (HTTPS account-gated) |
| tariff | Free — "no current plans to charge users to access the network" |
| vrs | Yes — iMAX. Recommended `MSM_IMAX` (RTCM3 MSM4 full constellation) |
| num_stations | 83 IaRTN + cross-state (10 MnDOT, 4 WisDOT, 7 MoDOT). Iowa DOT PDF station-list HTTP 403 from sandbox; values from earlier research |
| hobbyist_eligibility | ? — self-service registration; activation within 2 business days; no professional-licence field |
| legal_residency_required | ? |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (9 STR; GNSS Spider 7.11.1.109) |
| datum_epoch | omitted — no citable declaration on operator portal. 2025-12-02 Iowa DOT announcement (403 from sandbox) commits to NATRF2022 transition mid-late 2026 with parallel legacy/NATRF2022 mountpoints during cutover — operator-declared *plan*, not active frame |

Reference station list: https://iowadot.gov/media/1387/download?inline=. NATRF2022 announcement: https://iowadot.gov/announcement/2025-12-02/new-reference-frame-2026.

## IL — Illinois: IDOT CORS (under construction)

No public NTRIP caster as of 2026-05-18. IDOT kickoff Nov 2024; first 3 monuments (Litchfield, Petersburg, Jacksonville) installed Aug 2024. Target ~70 sites statewide. Framed as "the first free public network of its kind in Illinois". No NTRIP endpoint, sourcetable, registration portal, or launch date published.

**Most recent announcement:** 2024-11-07 IDOT blog "CORS network installation kicks off" — https://idot.illinois.gov/about-idot/stay-connected/idot-blog/cors-network-installation-kicks-off.html. MeriTalk State & Local mirror: https://www.meritalkslg.com/articles/illinois-kicks-off-cors-network-installation/

**Funding:** USD 6.25M total (USD 4.5M Federal ADCMS grant 2023 + state match). Monument: stainless-steel rod tripod drilled 12 ft, domed antenna.

**Commercial fallback in IL (paid, out of scope; context only):** ReIL-NET (`caster.reil-net.com` ports 12050-12055; Leica Spider; 55+ stations Chicagoland + Central IL; subscription price USD 200 (monthly or yearly billing) — Karaco product page verbatim "Regular price $200.00", https://karaco.com/pages/reil-net-rtk-network, fetched 2026-05-18; tariff/yr cadence ambiguous on page).

## MO — Missouri: MoDOT RTN

| Field | Value |
|---|---|
| Network | Missouri DOT Real-Time Network |
| Operator | MoDOT; Trimble Pivot |
| landing_url | https://gpsweb3.modot.mo.gov/ |
| access_url | https://gpsweb3.modot.mo.gov/MODOT_RTK_GPS_USER_AGREEMENT.pdf (signed + notarised, returned to MoDOT) |
| host:port | `gpsweb3.modot.mo.gov:2101` (alias `rtk3.modot.mo.gov`; 168.166.125.30) |
| tariff | Free — "No, it is a free network" (MoDOT FAQ) |
| vrs | VRS-only. Mountpoints: `VRS_RTCM31` (GPS+GLO; recommended), `VRS_CMRplus`, `VRS_CMRx`, `VRS_RTCM21`, `VRS_RTCM23`, `RTCM3NET_AUTOCELL`, `RTX_CMRx` (multi-const Trimble; added 2024 per Seiler Geospatial) |
| num_stations | 80+ GNSS stations (MoDOT FAQ). ≤70 km max spacing; covers all 114 MO counties (earlier 78-station figure superseded) |
| hobbyist_eligibility | ? — notarised UA required; FAQ recommends registering under org name (does not explicitly prohibit individuals) |
| legal_residency_required | ? |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (8 STR; Trimble Caster 5.3) |
| datum_epoch | NAD83(2011) Epoch 2010.00 — MoDOT FAQ explicit: "NAD83(2011) Epoch 2010.00 adjustment". Citation: https://gpsweb3.modot.mo.gov/faq.html |

Contact via modot.org/gps-utility-mapping-system.

## ND, SD, NE, KS — no public state caster

Confirmed (GPS World Dec 2024 lists explicitly "No public service"; E38 Survey Solutions; Point One state pages; 2026-05-18 re-search):

- **ND**: no state caster. NOTA stations at geodetic spacing.
- **SD**: no state caster. NOTA stations. TrueNav Tech (Sioux Falls) markets single-base NTRIP across SD/MN/IA/NE with self-service 30-day free trial; hobbyist-friendly via trial; pricing not published.
- **NE**: no state caster. NEBRS (UNL + NDOT) = post-processing RINEX only; account-required and free per UNL School of Natural Resources NEBRS page (covers data download policy + station list). NDOT runs ~40 internal-only stations. Public-network advocacy paper: agrasoft.net/info/nebraska-rtk-cors-modernization (Jan 2024, author Kevin Kenney). **Caveat: AGRAsoft is a commercial agriculture-software vendor; the page is policy advocacy, not a neutral source — treat the "$3M/yr potentially leaving the state in subscription fees" figure as advocacy framing, not audited data.**
- **KS**: no state caster. KDOT GIS Resources lists no CORS/RTK. SmartNet North America Oklahoma portal covers OK/KS/TX corridor (paid).

Commercial fallbacks (out of scope, context only): Trimble VRS Now / RTX, Midstates VRS (now Trimble Positioning Services), Midwest RTK Network (mwrtk.net), RTKdata.com.

## Regional 2026 datum migration (NATRF2022 / NAPGD2022)

NSRS modernisation: NAD83(2011) → NATRF2022; NAVD88 → NAPGD2022. FGCS approval vote scheduled Feb 2026 per NGS / Federal Register notice 2024-10-09 (https://www.federalregister.gov/documents/2024/10/09/2024-23347/...). NGS-led rollout across CORS networks mid-late 2026.

State DOT RTN behaviour during transition:
- **IA**: explicit operator announcement (2025-12-02) — parallel NAD83(2011) + NATRF2022 mountpoints during cutover.
- **MN, WI, MI, OH, MO, IN**: implicit — expected to follow NGS guidance with parallel mountpoints; no operator-side commitment text confirmed.

Re-read each network's announcement page before cutover; new mountpoints likely appear in 2H 2026 sourcetables.

## Post-processing fallback

NOAA NCN CORS RINEX (free, no account); EarthScope NOTA RINEX (free non-commercial; account); IaRTN RINEX (post-login); MDOT CORS virtual RINEX (account); InCORS FTP (https://ftp.incors.in.gov/, public).

## Sources

- WISCORS: https://wiscorsweb.dot.wi.gov/trimblepivotweb/ ; https://wisconsindot.gov/Pages/doing-bus/eng-consultants/cnslt-rsrces/tools/wiscors/default.aspx ; FAQ PDF wiscorsweb.dot.wi.gov/TrimblePivotWeb/documents/wiscors-faq.pdf ; www.seilergeo.com/wiscors-ip-address-and-url-change-2/
- InCORS: https://incors.in.gov/ ; https://incors.in.gov/useragreement.pdf ; https://incors.in.gov/Station%20Updates.html ; https://ftp.incors.in.gov/
- MDOT CORS: https://mdotcors.michigan.gov/sbc ; https://mdotcors.michigan.gov/sbc/Account/Register ; MSRN Port Scheme XLSX
- MnCORS: https://www.dot.state.mn.us/surveying/cors/index.html ; FAQ https://www.dot.state.mn.us/surveying/cors/mncors_faq.html ; https://mncors.dot.state.mn.us/ ; Feb 2025 MnDOT bulletin content.govdelivery.com/accounts/MNDOT/bulletins/3d3904c
- IaRTN: https://iowadot.gov/consultants-contractors/design/iowa-real-time-network ; portal https://iartnsbc.iowadot.gov/ ; reference station list https://iowadot.gov/media/1387/download?inline= ; NATRF2022 announcement https://iowadot.gov/announcement/2025-12-02/new-reference-frame-2026
- ODOT RTN: https://ortn.dot.state.oh.us/TrimblePivotWeb/Login.aspx (operator Trimble Pivot Web) ; prior `https://transportation.ohio.gov/working/engineering/cadd-mapping/survey/cors-rtn` is HTTP 404 2026-05-18 (site reorg, full `/working/engineering/` tree removed) ; multi-const 2021-02-02 announcement https://ohiosurveyor.org/aws/osps/pt/sd/news_article/350530/_PARENT/layout_details/false
- MoDOT RTN: https://gpsweb3.modot.mo.gov/ ; FAQ https://gpsweb3.modot.mo.gov/faq.html ; UA PDF https://gpsweb3.modot.mo.gov/MODOT_RTK_GPS_USER_AGREEMENT.pdf ; multi-const update www.seilergeo.com/update-to-wiscors-and-modot-rtk-networks/
- IDOT CORS: https://idot.illinois.gov/about-idot/stay-connected/idot-blog/cors-network-installation-kicks-off.html ; meritalkslg.com/articles/illinois-kicks-off-cors-network-installation/ ; clearinghouse.isgs.illinois.edu/webdocs/ilhmp/reference.html ; ReIL-NET karaco.com/pages/reil-net-rtk-network
- Regional refs: https://www.gpsworld.com/finally-a-list-of-public-rtk-base-stations-in-the-u-s/ ; e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state ; pointonenav.com/states/{north-dakota,south-dakota,nebraska,kansas,michigan}/ ; ntrip-list.com/north-america/ ; www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- NGS CORS FAQ (state RTK provider list): https://geodesy.noaa.gov/CORS/cors_faqs.shtml
- NSRS modernisation: Federal Register 2024-10-09 www.federalregister.gov/documents/2024/10/09/2024-23347/... ; NGS New Datums FAQ geodesy.noaa.gov/datums/newdatums/FAQNewDatums.shtml
- NE/SD/KS gap: agrasoft.net/info/nebraska-rtk-cors-modernization ; truenav.tech ; rtkdata.com/us/{nebraska,illinois} ; smartnetna.com/pr_sn_oklahoma.cfm ; agweek.com/business/midstates-vrs-launches-cellular-based-rtk
- EarthScope NOTA portal (ingested-global, do NOT probe per primer): https://www.earthscope.org/data/gnss-realtime/
