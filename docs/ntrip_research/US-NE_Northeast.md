# US Northeast [US-NE] — NTRIP RTK Caster Research

**States:** ME, NH, VT, MA, RI, CT, NY, NJ, PA, DE, MD, DC

## Status (region)

Five free state networks (ME, VT, MA, CT, NY). NH/RI/NJ/PA/DE/MD/DC have no free public state caster. EarthScope NOTA provides sparse single-base fallback region-wide.

## Per-state summary

| State | Free public caster | Network | host:port | VRS | Hobbyist | Probe |
|---|---|---|---|---|---|---|
| ME | Yes | MaineDOT RTN | `medotrtn.maine.gov:2101` | Yes | Likely yes | OK 8 STR |
| NH | No | — | — | — | — | No state caster |
| VT | Yes | VECTOR | `vector.vermont.gov:2101` | Yes | Yes (explicit) | OK 36 STR |
| MA | Yes | MaCORS | `macorsrtk.massdot.state.ma.us:2101` | Yes (iMAX) | Yes | Timeout external (firewall); DNS resolves |
| RI | No | — | — | — | — | ACORN + MaCORS edge coverage |
| CT | Yes | ACORN | `acorn.uconn.edu:2101` | Yes | Yes (explicit) | OK 47 STR |
| NY | Yes | NYSNet | `rtn.dot.ny.gov:8080` (NTRIP); `cors.dot.ny.gov:443` portal | Yes (iMAX/MAC + `net_msm_vrs`) | Likely yes | OK 18 STR |
| NJ | No | — | — | — | — | No state caster |
| PA | No | — | — | — | — | No state caster |
| DE | No | — | — | — | — | No state caster |
| MD | No | — | — | — | — | No state caster (`mdotcors.org` → Michigan, not Maryland) |
| DC | No | — | — | — | — | No state caster |

## Regional baseline: EarthScope NOTA

See `US-NOTA_NetworkOfTheAmericas.md` for operator-scope detail. NE sub-coverage sparse — only 2 stations inside strict NE bbox (`P776_RTCM3P3` central NH, `P817_RTCM3P3` central PA). Cross-border stations just outside bbox reachable for stations near NE border; query `py scripts/stations_by_radius.py <lat> <lon> 100 --source earthscope`. Geodetic spacing — best as PPK fallback, not real-time RTK in NE.

## ME — MaineDOT Real-Time Network

| Field | Value |
|---|---|
| Network | Maine Real-Time Network (MaineDOT RTN) |
| Operator | MaineDOT Bureau of Project Development, Survey Section |
| Software | Trimble Pivot (migrated from legacy system; cutover 2025-10-01) |
| landing_url | https://medotrtn.maine.gov/ — operator Trimble Pivot portal; service description + signup |
| access_url | Skip — landing portal serves both purposes (state DOT pattern); support `rtnsupport.medot@maine.gov` |
| host:port | `medotrtn.maine.gov:2101` (52.165.92.197) |
| tariff | Free |
| vrs | Yes (VRS) — confirmed by live ST 2026-05-18 |
| num_stations | unknown — sourcetable contains only routing aliases (4 `VRS_*` + 4 `SingleStation_Nearest_*`); operator pages do not enumerate. Per primer [stations-vs-mps], ST count ≠ CORS count. Escalation: `rtnsupport.medot@maine.gov` |
| hobbyist_eligibility | Unclear — self-service registration (own Org/Username/Password); no professional-licence field; no explicit restriction |
| legal_residency_required | Unclear — no stated requirement |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (8 STR; Trimble Caster 5.3) |
| datum_epoch | NAD83(2011) Epoch 2010.00 — MaineDOT operator datasheet: https://www.maine.gov/mdot/surveyinfo/docs/NAD832011Epoch2010Datasheets.pdf |

MaineDOT replaced legacy CORS system (mdotcors.maine.gov, ECONNREFUSED since pre-cutover) with Trimble Pivot at medotrtn.maine.gov in 2025. Pre-cutover users had to re-register.

## NH — no public state caster

No state DOT or university RTK network. NHDOT operates CORS contributing to NOAA NCN for static post-processing only. Multiple sources (GPS World Dec 2024, E38, Point One) confirm "no public service".

EarthScope NOTA has one NH station (P776 central NH) as single-base fallback. Commercial: KeyNetGPS (paid, see multi-state section).

## VT — VECTOR

| Field | Value |
|---|---|
| Network | VECTOR — Vermont Enhanced CORS and Transmission Of Real-time Corrections |
| Operator | VTrans Geodetic Survey unit; CORS sites NOAA NCN-accredited |
| Software | Trimble Pivot |
| landing_url | https://vtrans.vermont.gov/highway/geodetic/cors/real-time — VTrans Geodetic page; service description, datum, account-request workflow |
| access_url | https://vector.vermont.gov/ — operator Trimble Pivot portal; self-service registration + sourcetable host |
| host:port | `vector.vermont.gov:2101` (20.185.11.35) |
| tariff | Free |
| vrs | Yes (VRS) + single-base streams. Solution types per live ST 2026-05-18: 2 VRS mountpoints (`VRS_RTCM3`, `VRS_CMRp`; solution flag 1) + 16 per-station single-base mountpoints in both RTCM 3.1 and CMRx (solution flag 0). No MAC/FKP/iMAX |
| formats | RTCM 3.1 (GPS+GLO), CMR+ (GPS+GLO), CMRx (GPS+GLO+GAL+BDS). No RTCM 3.2/3.3 MSM streams advertised; full-constellation only via CMRx (Trimble proprietary) — non-Trimble multi-const users have no advertised mountpoint |
| hobbyist_eligibility | Yes — VTrans explicit: "free service utilized by State and Federal Agencies, Surveyors, GIS users, Engineers, Scientists, and the public at large" |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (36 STR; Trimble Caster 5.3) |
| station_count | 18 reference stations statewide; live ST 34-36 STR (single-base + VRS combos across RTCM3/CMR+/CMRx); all except VJSC and VTWR NOAA NCN-accredited |
| datum_epoch | NAD83(2011) Epoch 2010.00 — VTrans declaration: "the Vermont CORS are referenced to NAD 83(2011) epoch 2010.00" via vtrans.vermont.gov / outside.vermont.gov VTrans-hosted document |

NetR9 → current-generation receiver upgrades completed 2025.

## MA — MaCORS

| Field | Value |
|---|---|
| Network | MaCORS — Massachusetts Continuously Operating Reference Station Network |
| Operator | MassDOT |
| Software | Leica SpiderNet (Spider Business Center) |
| landing_url | https://www.mass.gov/how-to/the-massachusetts-continuously-operating-reference-station-network-macors — Mass.gov service description |
| access_url | https://macors.massdot.state.ma.us/ — Leica SBC portal; registration + account management |
| host:port | `macorsrtk.massdot.state.ma.us:2101` (193.8.43.161) |
| tariff | Free — "MassDOT does not currently charge a fee for network access" |
| vrs | Yes — iMAX network mountpoints (multi-base correction); recommended `RTCM3MSM_IMAX` (GPS+GLO+BDS+GAL) |
| hobbyist_eligibility | Yes — "MassDOT is now granting public access"; no professional-licence field; no stated restriction |
| legal_residency_required | No |
| last_confirmed_alive | DNS resolves (`macorsrtk.massdot.state.ma.us` → `rtk.madot.net` → 193.8.43.161); port 2101 times out external (firewall / IP allowlist). Mass.gov portal HTTP 200. Service confirmed operational by user reports |
| station_count | 22 GNSS base stations ~50 km apart (current Mass.gov 2026 listing). Older sources reference 18 |
| formats | RTCM 2.3, RTCM 3.1, CMR, CMR+, RTCM 3.2 MSM4 |
| coverage | Massachusetts + edge into RI, southern NH, CT |
| datum_epoch | omitted — no citable operator declaration. Mass.gov MaCORS landing fetched 2026-05-18 returns HTTP 403 to scripted probe (anti-bot); prior cached fetches contained no frame/epoch text. Leica SBC portal account-gated. Third-party `MaCORS_FAQs_Rev2.pdf` mirror at ashgps.com states NAD83(2011) ep 2010.00 (**pointer carried forward from prior research; mirror PDF not re-fetched in this session — re-verify before citing**). Not citable on MassDOT-controlled domain |

Port 2101 firewalled to registered accounts (Leica SBC standard).

## RI — no dedicated state caster

Relies on neighbour networks: ACORN (CT) places `URIL` station in Kingston RI (41.49°N -71.53°W) served as `URIL3`/`URILP`/`URILX` + inside ACORN VRS hull; MaCORS (MA) southernmost stations reach northern RI.

Commercial fallback: KeyNetGPS (see multi-state section).

## CT — ACORN

| Field | Value |
|---|---|
| Network | ACORN — Advanced Continuously Operating Reference Network |
| Operator | CTDOT + UConn Dept. of Natural Resources and the Environment (DNRE) |
| Software | Trimble Pivot |
| landing_url | http://acorn.uconn.edu/ — UConn-hosted ACORN portal home |
| access_url | https://portal.ct.gov/dot/-/media/dot/aec/const_inspection/acorn_faq.pdf — CTDOT-hosted ACORN FAQ (rev 2025-10-06); covers fee, eligibility, datum, station roster, admin contact |
| host:port | `acorn.uconn.edu:2101` (round-robin: 137.99.150.112, 137.99.150.56) |
| tariff | Free — "ACORN is currently free and open to the public" (operator FAQ) |
| vrs | Yes — primary `VRS3_RTX` (multi-const); Trimble `VRSX_RTX` |
| hobbyist_eligibility | Yes — explicit "free and open to the public". Self-service registration. Account does not expire; subscriptions auto-renew annually. Default policy disallows simultaneous logins from one account (RTK-pair logins by admin request) |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (47 STR; Trimble Caster 5.2) |
| station_count | 13 physical sensors: 9 CT (CTBK Brookfield, CTDA Darien, CTEG East Granby, CTGR Groton, CTGU Guilford, CTMA Mansfield, CTNE Newington, CTPN Putnam, CTWI Winchester); 1 RI (URIL Kingston, URI campus); 2 southern MA (MASB Sturbridge, MASH Sheffield); 1 Long Island NY (NYRH Riverhead) |
| constellations | GPS+GLO+GAL+BDS — Galileo + BeiDou added July 2025. Multi-const requires `VRS3_RTX` (Trimble: `VRSX_RTX`). Mountpoints ending in `P` = CMR+ = GPS+GLO only |
| datum_epoch | NAD83(2011) Epoch 2010.0 — ACORN FAQ (CTDOT-hosted): "ACORN's Default Reference Frame: NAD 83 (2011) ... NAD 83 (2011) Position (Epoch 2010.0)". Per-station ITRF velocity table in same document. Citation: https://portal.ct.gov/dot/-/media/dot/aec/const_inspection/acorn_faq.pdf |

Sustained state budget funding. CTDOT operates reference receivers; UConn NRE operates servers. Useful for RI (URIL hull-internal), southern MA, Long Island NY users near CT stations. Admin contact: `kevin.franklin@uconn.edu`.

**Long Island NY — ACORN vs NYSNet:** eastern LI sits inside ACORN hull via NYRH (Riverhead); also within NYSNet's NY coverage. Neither operator publishes formal guidance on choice. Practical pointer: ACORN free, single-LI station = baseline degrades fast west of Riverhead, uses NAD83(2011) ep 2010.0; NYSNet free, denser across NY, uses NAD83(2011) ep 2010 MYCS2 (the MYCS2 height model is the only frame-level difference). Western-LI user near NYC geometrically closer to NYSNet stations; eastern-LI near Riverhead has either available. Confirm with operator before deployment.

## NY — NYSNet

| Field | Value |
|---|---|
| Network | NYSNet — New York Spatial Reference Network (CORS + RTN) |
| Operator | NYSDOT Engineering Division + NYC partners |
| Software | Leica SpiderNet (`GNSS Spider 7.10.1.168/1.0`) |
| landing_url | https://cors.dot.ny.gov/NYSNet%20welcome_0.htm — operator NYSDOT welcome page |
| access_url | https://cors.dot.ny.gov/FAQ.htm — operator FAQ; fee policy, datum/epoch, registration, routes to SBC portal at `cors.dot.ny.gov/SBC` |
| host:port (RTN) | `rtn.dot.ny.gov:8080` — `SOURCETABLE 200 OK`. Full port/mountpoint list at cors.dot.ny.gov/SBC → RTN Ports/Mount Points. Port 2101 timed out external (firewalled) |
| host:port (SBC portal) | `cors.dot.ny.gov` (HTTP 200; NTRIP :2101 timed out external, consistent with account-gated access) |
| tariff | Free — operator FAQ: "No. NYSDOT does not charge users a fee for access to the real-time network" |
| vrs | Yes — `net_msm_vrs` (RTCM 3 MSM, GPS+GLO+GAL+BDS, network VRS). Also iMAX (`net_msm_imax`, `GG_MSM_IMAX`) for Leica MAC users. `near_msm` (nearest-site MSM full constellation). 18 STR live 2026-05-18 incl. `NetCell_MAX_RTCMv3`, `NetCell_iMAX_RTCMv3`, `NearSite_GIS_RTCM12`, `NearSite_CMR+`, `NetCell_iMAX_CMRP`, `NetCell_iMAX_CMR`, `NearSite_CMR`, `NearSite_RTCMv3`, `GG_RTCM3_MAX`, `GG_RTCM3_IMAX`, `GG_CMRP_IMAX`, `GG_MSM_IMAX`, `near_msm`, `GG_RTCM3_MAX_1017`, `net_msm_imax`, `test`, `net_msm_vrs`, `NYAB_GIS_RTCM12` |
| hobbyist_eligibility | Likely yes — registration open (email + self-service); no professional-licence field in public FAQ; no explicit restriction; operator FAQ contains no eligibility constraint |
| legal_residency_required | Unclear |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (18 STR; GNSS Spider 7.10.1.168/1.0) |
| constellations | GPS+GLO+GAL+BDS on MSM mountpoints (`near_msm`, `net_msm_imax`, `net_msm_vrs`); legacy `NetCell_MAX_RTCMv3`, `NetCell_iMAX_*` are GPS-only or GPS+GLO |
| datum_epoch | NAD83(2011) Epoch 2010 MYCS2 — operator FAQ (re-verified 2026-05-18): "NAD83 (2011) EPOCH 2010 MYCS2". Citation: https://cors.dot.ny.gov/FAQ.htm. **MYCS2→MYCS3 transition unresolved**: NGS released MYCS3 in 2024–2025 (Oct 2022 IGS20 alignment per geodesy.noaa.gov/CORS/news/mycs3/mycs3.shtml; modelled coordinates "currently being generated" per June 2025 update); NYSNet FAQ as of 2026-05-18 still names MYCS2 with no migration notice. Sister network ACORN (CT) cites NAD83(2011) Epoch 2010.0 without MYCS qualifier; NPS slide deck names NAD83(2011) 2010.0 without MYCS qualifier. NYSNet treatment of MYCS3 = pointer / unresolved |

Free registration at cors.dot.ny.gov; credentials emailed. 2024 NYSAPLS conference handout: planned full station rebuilds (cabling, receivers, choke-ring antennas) + possible densification by 10+ CORS.

## NJ — no public state caster

No NJDOT/Rutgers/Princeton RTK NTRIP caster (re-confirmed 2026-05-18). RTK Premium covers entire state (commercial, paid). Historical small NJIT CORS array not maintained as public real-time service.

NJ falls between NYSNet (NY; partial coverage in northern NJ near NYC) and EarthScope NOTA (no NJ station). Commercial: KeyNetGPS, AlphaRTK.

## PA — no public state caster

No active PennDOT-operated CORS RTK NTRIP caster (re-confirmed 2026-05-18 via E38, Point One, GPS World). 2011 PennDOT/NGS presentation (Harpster) described PACS (Pennsylvania CORS System) + VRS plans; no live public endpoint confirmed since. **Post-2011 PennDOT geodetic / PSLS (Pennsylvania Society of Land Surveyors) sources not exhaustively searched in this session — PACS revival/cancellation status remains unresolved.** Penn State CORS for research only. PennDOT's `request-access-to-transportation-related-data-feeds` covers traffic/ITS, not RTK corrections.

Commercial: KeyNetGPS (covers PA, `vrs.keynetgps.com:2101` `SOURCETABLE 200 OK` 2026-05-18, paid); AlphaRTK (covers PA; USD 195/mo). EarthScope NOTA has one PA station (P817, Altoona area) for single-base/PPK.

## DE — no public state caster

DelDOT does not operate a public CORS network. Multiple sources confirm.

Commercial: KeyNetGPS (covers DE), AlphaRTK (covers DE). State small enough that nearby NJ/MD/PA commercial networks provide viable baseline.

## MD — no public state caster

MDOT SHA maintains geodetic control + HARN points for static post-processing only. No real-time RTK caster. Multiple 2024 sources list MD as "no public service" (GPS World) or covered only by RTK Premium (commercial). `mdotcors.org` (DNS 148.149.27.70) is the Michigan Spatial Reference Network (MDOT CORS-MSRN, Michigan DOT) — frequent confusion in third-party listings.

MDOT SHA Survey: Erik Donald, 410-545-8976, `edonald@mdot.maryland.gov`.

Commercial: KeyNetGPS (covers MD/DC), AlphaRTK (covers MD/DC; USD 195/mo).

## DC — no public caster

No dedicated DC RTK NTRIP. Covered by same commercial networks as MD/VA (KeyNetGPS, AlphaRTK). EarthScope NOTA has no DC station. NGS CORS in DC area contribute to NOAA NCN for static post-processing only.

## Multi-state commercial networks

### KeyNetGPS (Keystone Precision Solutions / Keypre)

| Field | Value |
|---|---|
| Coverage | VA, DC, MD, DE, PA, NJ, NY, CT, RI, MA, VT, NH, ME (entire Northeast) |
| landing_url | https://www.keypre.com/keynetgps/about-keynet-gps/ |
| access_url | https://vrs.keynetgps.com/ — Trimble VRS3Net portal |
| host:port | `vrs.keynetgps.com:2101` (209.255.196.164) |
| tariff | 30-day USD 375 per subscription; annual USD 3,135 (net 30) or USD 3,300 (monthly increments of USD 275/mo, credit card on file). Source: KeyNetGPS Pricing PDF (www.keypre.com/getmedia/9461f194-…/KeyNetGPS-Pricing-and-Registration-Process-(1).pdf, fetched 2026-05-18) |
| vrs | Yes — Trimble VRS3Net; mountpoints `VRS_CMRp`, `VRS_CMRx`, `SingleBase_CMRp`, `SingleBase_RTCM3` (6 STR live 2026-05-18) |
| hobbyist_eligibility | Unclear — no explicit restriction; subscriber agreement required. Annual USD 3,135 well above hobbyist range |
| legal_residency_required | Unclear |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` (6 STR; Trimble Caster 5.1) |

Resellers: Laser Industries 412-510-3089; Duncan-Parnell 833-916-0557. Primary paid option for PA, NJ, DE, NH, RI, parts of NY/MD/DC without free coverage.

### AlphaRTK

| Field | Value |
|---|---|
| Coverage | DE, MD, NJ, PA, DC |
| landing_url | https://www.alphartk.com/ — describes coverage, hardware compat, contact `info@alphartk.com` |
| access_url | Skip — landing covers tariff, free-trial, signup contact (no separate portal) |
| host:port | Not published; contact `info@alphartk.com` |
| tariff | USD 195/1mo · USD 695/6mo · USD 995/12mo · USD 1,595/24mo (observed 2026-05-18, alphartk.com — down from prior file: 6mo was USD 995, 12mo was USD 1,595). Free 1-week trial |
| vrs | Unknown |
| hobbyist_eligibility | Unclear — professional orientation; trial available |
| legal_residency_required | Unclear |
| last_confirmed_alive | alphartk.com HTTP 200 2026-05-18. Website alive ≠ NTRIP caster alive; host:port unpublished; no public sourcetable probe possible. Treat as pointer, not confirmed live caster |

## Post-processing fallback

| Service | Coverage | Cost |
|---|---|---|
| NOAA NCN CORS — static RINEX | All NE states | Free; no account |
| EarthScope NOTA RINEX | 2 NE stations (P776 NH, P817 PA) | Free non-commercial; account required |

## Sources

- NYSNet FAQ: https://cors.dot.ny.gov/FAQ.htm
- NYSNet welcome: https://cors.dot.ny.gov/NYSNet%20welcome_0.htm
- NYSAPLS 2024 conf handout: https://cdn.ymaws.com/www.nysapls.org/resource/resmgr/2024_conference/course_handouts/2024_nysapls_nysdot_cors-rtn.pdf
- MaCORS portal: https://macors.massdot.state.ma.us/
- MaCORS Mass.gov: https://www.mass.gov/how-to/the-massachusetts-continuously-operating-reference-station-network-macors
- MALSCE MaCORS announcement: https://www.malsce.org/news/massdots-gps-network-now-available-for-use/
- Maine DOT Survey: https://www.maine.gov/dot/doing-business/permitting-policy/survey-and-right-of-way-information
- MaineDOT RTN portal: https://medotrtn.maine.gov/
- MaineDOT NAD83(2011) datasheets (datum citation): https://www.maine.gov/mdot/surveyinfo/docs/NAD832011Epoch2010Datasheets.pdf
- VTrans VECTOR real-time: https://vtrans.vermont.gov/highway/geodetic/cors/real-time
- VECTOR portal: https://vector.vermont.gov/
- ACORN welcome: http://acorn.uconn.edu/
- ACORN FAQ (operator, datum citation): https://portal.ct.gov/dot/-/media/dot/aec/const_inspection/acorn_faq.pdf
- CT Surveyors ACORN: https://ctsurveyors.org/acorn-real-time-positioning-for-connecticut/
- EarthScope GNSS Realtime: https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- E38 Survey Solutions state-by-state: https://e38surveysolutions.com/pages/ntrip-rtk-network-access-by-state
- E38 MaCORS Emlid guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-massachusetts-ntrip-macors
- E38 NYSNet Emlid guide: https://e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-new-york-ntrip-nysnet
- ArduSimple USA NTRIP: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- KeyNetGPS portal: https://vrs.keynetgps.com/
- KeyNetGPS pricing PDF: https://www.keypre.com/getmedia/9461f194-ea72-43a1-9b88-29dd50fe8f4e/KeyNetGPS-Pricing-and-Registration-Process-(1).pdf
- Keypre about: https://www.keypre.com/keynetgps/about-keynet-gps/
- AlphaRTK: https://www.alphartk.com/
- MDOT SHA geodetic: https://roads.maryland.gov/mdotsha/pages/Index.aspx?PageId=61
- GPS World public RTK list: https://www.gpsworld.com/finally-a-list-of-public-rtk-base-stations-in-the-u-s/
- NTRIP-list North America: https://ntrip-list.com/north-america/
- Point One Nav NH: https://pointonenav.com/states/new-hampshire/
- Point One Nav PA: https://pointonenav.com/states/pennsylvania/
- NGS CORS FAQ (state RTK provider list — confirms ME/MA/NY/VT free; lists NC, SC, TN paid; does not list ACORN-CT, RI, NH, NJ, PA, DE, MD, DC): https://geodesy.noaa.gov/CORS/cors_faqs.shtml
- Probes 2026-05-18 (curl `--http0.9 -A 'NTRIP/1.0'`): medotrtn.maine.gov:2101 OK 8 STR; vector.vermont.gov:2101 OK 36 STR; acorn.uconn.edu:2101 OK 47 STR; ntrip.earthscope.org:2101 OK ~1080 STR (ingested-global); vrs.keynetgps.com:2101 OK 6 STR; rtn.dot.ny.gov:8080 OK 18 STR; macorsrtk.massdot.state.ma.us:2101 timeout; rtn.dot.ny.gov:2101 timeout; cors.dot.ny.gov:2101 timeout; mdotcors.org (DNS 148.149.27.70, Michigan, not Maryland)
