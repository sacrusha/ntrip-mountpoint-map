# Free RTK NTRIP — country-by-country survey

_Purpose: ground truth for pipeline additions and the map's gap messaging._
_Organised by region. Each entry records: network name · endpoint · free/paid
status and basis · registration path · user-facing note for the map UI · open
questions. Entries with confirmed free endpoints are candidates for the
`SOURCES` list in `scripts/fetch_stations.py`._

_Last updated: 2026-04-20. Supersedes `.tmp/country-coverage.md`._

---

## Europe — Western

### DE — Germany
- **SAPOS GEPOS** (BKG federal): `bkg1.positioning-service.net:2101` (alt: `caster.gepos.sapos.de:2101`) — no registration, CC-BY 4.0, free. PPP-RTK/SSR corrections via SSRZ format (not standard OSR RTCM); requires SSR-capable receiver or Geo++ SSR2OBS converter software (freely available). Continuous from Apr 2026 (was in optimization phase 2025–Mar 2026). Also broadcast via DAB+ radio.
- **SAPOS HEPS/EPS** (per-Bundesland): ~270 stations, VRS. **All 16 Länder now free** — RP confirmed free (LVermGeo), ST confirmed free (LVermGeo), and BY agricultural-use free via Landwirtschaftskammer. Per-state casters (e.g. `sapos-bw-ntrip.de:2101`, `sapos-th-ntrip.de:2101`); all require per-Länder web registration. **Already in pipeline** (13 state casters; see `SOURCES` prefix `sapos_`).
- **Centipede**: a handful of volunteer DE nodes.

### AT — Austria
- **APOS** (BEV): `aposrtk.bev.gv.at:2101`, 37 stations, VRS. Free for agriculture/forestry since Feb 2021 (requires eAMA credentials — farm client number + PIN from Agrarmarkt Austria). Professional/hobbyist use paid (BEV portal subscription). User-facing: "Paid VRS available (free only for ag/forestry sector via eAMA)."
- Centipede: minimal AT nodes.

### CH — Switzerland
- **swipos** (swisstopo): CHF 1,500/yr. *Geoinformationsgesetz* SR 510.62 classifies RTK as a value-added service; no free tier. User-facing: "Paid VRS available (swipos ~CHF 1,500/yr)."

### FR — France
- **Centipede**: `crtk.net:2101` — free, no registration, 625+ volunteer bases, densest coverage in France. **Already in pipeline.**
- Commercial VRS: Teria (Hexagon), Orphéon (Trimble) — paid.

### BE — Belgium
- **FLEPOS** (Flanders): `ntrip.flepos.be:2101`, 45 stations, VRS. Free for all uses (surveying and machine control), web self-signup at flepos.vlaanderen.be. Candidate for pipeline.
- **WALCORS** (Wallonia): `gnss.wallonie.be:2101`, 23 stations, VRS. Free for "positioning" uses (survey, GIS, drones). Paid for machine-control/auto-guidance since Jan 2013 (commercial resellers buy raw stream; not a hobbyist restriction in practice). Registration at gnss.wallonie.be (gnss@spw.wallonie.be). Candidate for pipeline.
- **GPSBru/AGN** (Brussels NGI): `agn.ngi.be` — endpoint confirmed at ngi.be; single station (Uccle observatory); NTRIP access via AGN portal. Operational as of mid-2024 (status page at agn.ngi.be). Free, registration via NGI. Low priority (single base; useful only within ~30 km of Brussels).

### NL — Netherlands
- No public free NTRIP. Market fully privatised since ~2000 (06-GPS/Trimble). User-facing: "Paid VRS available."

### LU — Luxembourg
- **SPSLux** (ACT — Administration du Cadastre et de la Topographie): `stream.spslux.lu:5005` (**port 5005, not 2101**; IP 185.106.24.68), VRS. Luxembourg open-data policy — all services free of charge. Free self-signup at spslux.lu/SBC/Account/Register; then subscribe to "SPSLUX (N)RTK" package in the SBC shop. Candidate for pipeline.

### IE — Ireland
- No public free NTRIP. OSi routes users to Trimble VRS Now (commercial). Some Centipede volunteer nodes exist.

### GB — United Kingdom
- No public free NTRIP. OS Net raw data licensed to commercial resellers (SmartNet/Leica, TopNET/Trimble) under OS licence model since 2005. Some Centipede volunteer nodes exist. User-facing: "Paid VRS available (SmartNet, TopNET, etc.)."

---

## Europe — Southern

### ES — Spain
- **ERGNSS** (IGN): `ergnss-ip.ign.es:2101`, ~120 stations, VRS. Free, web self-signup (ergnss.ign.es/gnuserportal/), immediate. CC-compatible (Orden FOM/2807/2015); attribution to IGN required. GPS+GLO+GAL+BDS. Candidate for pipeline.
- **RAP** (Andalucia, Junta): supplements ERGNSS in the south; separate signup (rap@juntadeandalucia.es).

### PT — Portugal
- **ReNEP** (DGT — Direção-Geral do Território): 47 stations, VRS + single-base. Free, portal signup at renep.dgterritorio.gov.pt (renep@dgterritorio.pt). Host:port **withheld until post-registration** — stations and RINEX publicly visible; NTRIP credentials provided after account approval. ETRS89 datum (mainland), ITRF93 (autonomous regions). Candidate for pipeline (requires registration first to get host).

### IT — Italy
- No national free public caster. Regional networks vary per region.
- **FReDNet** (OGS, Friuli-Venezia Giulia): `gnsscaster.regione.fvg.it:8080`, 16 stations, VRS. Sourcetable publicly readable; stream requires email registration (rete.gnss.marussi@regione.fvg.it, free). **Already in pipeline** (sourcetable fetch confirmed working, 39 STR lines).

### HR — Croatia
- **CROPOS** (DGU): `gnss.cropos.hr:2101`, 35 stations, VRS. **Free since Apr 2022** (Narodne novine 39/2022 — DPS and VPPS no longer charged). Email/web registration dgu@dgu.hr. DPS (~0.3–0.5 m) and VPPS (~2 cm) free; GPPS post-processing paid. Note: NTRIP caster IP changed Nov 2023 (old: 195.29.118.122 → new: 195.29.198.194); DNS hostname `gnss.cropos.hr` should resolve correctly but verify if pipeline has connectivity issues. Candidate for pipeline.

### SI — Slovenia
- **SIGNAL** (GURS): **PAID €829.44/yr** (€622.08 early discount). No free tier. DROP.

### GR — Greece
- **HEPOS** (HEPOS S.A.): €480/yr. No free tier. User-facing: "Paid VRS available (HEPOS ~€480/yr)."
- **URANUS**: commercial TopNET Live (Topcon). DROP.

### CY — Cyprus
- DLS network: internal use only, not public NTRIP.

---

## Europe — Northern

### SE — Sweden
- **SWEPOS** (Lantmäteriet): RTK tier paid (subscription). DGNSS tier (`dgnss-swepos.lm.se:2101`) is free, requires account (free registration), RTCM 2.3 — **~0.2 m horizontal accuracy, sub-metre only, out of scope**. User-facing: "Paid VRS available (SWEPOS Network RTK); free DGNSS at ~0.2 m not sufficient for this map."

### NO — Norway
- **CPOS/ETPOS** (Kartverket): NOK 8,000+/yr. No free RTK tier. User-facing: "Paid VRS available."

### DK — Denmark
- **GPSnet** (privatised ~2000): no public free caster. Market fully private (Leica/Hexagon). User-facing: "Paid VRS available."

### FI — Finland
- **FINPOS** (NLS): free for 3-month research applications only; no general public tier. DGNSS free but sub-metre. User-facing: "No public free RTK; research applications only."

### IS — Iceland
- **IceCORS** (LMÍ — Landmælingar Íslands, National Land Survey of Iceland): `moe.lmi.is:2101` (IP 178.19.53.126:2101), ~20+ stations, VRS/single-base. Registration required (lmi.is/is/maelingar/thjonustur/icecors); operated by Geo++ GNNET software. Free status unconfirmed — likely charged as a professional service given sparse population / cost recovery model. **Verify cost before including; low priority.**

### EE — Estonia
- **ESTPOS** (Maa-amet / Land and Spatial Development Board): `gnss-rtk.maaamet.ee:8083`, 40 stations, VRS. **Free until 31 August 2026** per director-general directive. Portal account + service agreement required (geoportaal.maaamet.ee). VRS, iMAX, nearest-base; MSM5 available. Candidate for pipeline (note expiry; review before Aug 2026).

### LV — Latvia
- **LatPos** (LGIA): `latpos.lgia.gov.lv:2101`, 27 LV + 5 EE + 4 LT border stations, VRS. **Free since 2018.** SBC portal signup (latpos.lgia.gov.lv/SBC). Candidate for pipeline.

### LT — Lithuania
- **LitPOS** (GIS-Centras, Geoportal.lt): 35 stations, VRS + DGPS. Services: RTK (~2 cm), DGPS (~0.3–0.5 m), GPPS post-processing. RTCM 2.1/2.3/3.1/3.2, CMR, CMR+, CMRx formats available. NTRIP endpoint not publicly listed without registration. **Free status confirmed uncertain** — registration at geoportal.lt/geoportal/web/litpos-en; pricing not displayed publicly. Contact LitPOS@geoportal.lt to confirm free status before ingesting.

### PL — Poland
- **ASG-EUPOS** (GUGiK): `system.asgeupos.pl:2101` (also :8080/:8082/:8083/:8086 for VRS variants), 130+ stations. **Free since Oct 2022** (all services, including RTK and DGNSS). Web self-signup at system.asgeupos.pl, admin approval 1–2 working days. GPS+GLO+GAL+BDS. VRS (NAWGIS/KODGIS/FKP/MAC). Candidate for pipeline.

---

## Europe — Eastern / Balkans

### RO — Romania
- **ROMPOS**: credit-based paid system. No open-data GNSS mandate. User-facing: "Paid VRS available (ROMPOS)."

### HU — Hungary
- **GNSSnet.hu**: likely paid.
- **Centipede**: 130+ community nodes — near-national coverage. Users effectively have free service via Centipede.

### CZ — Czech Republic
- **CZEPOS**: free for education/government; commercial use paid (ČÚZK Decree 31/1995). Not a general hobbyist path.

### SK — Slovakia
- **SKPOS**: free for public sector/municipalities; commercial use paid. Not a general hobbyist path.

### BG — Bulgaria
- No government network. Commercial only.

### RS — Serbia
- **AGROS** (RGZ): paid; no English pricing page. Some Centipede volunteer nodes exist.

### HR — see Europe — Southern.

### BA — Bosnia and Herzegovina
- **BiHPOS**: dual-entity administrative split; likely paid; limited resources.

### ME — Montenegro
- **MONTEPOS**: paid subscription tiers.

### MK — North Macedonia
- No confirmed national network name or NTRIP endpoint.

### AL — Albania / XK — Kosovo / MD — Moldova
- No confirmed public NTRIP endpoint in any of these three.

### UA — Ukraine
- **ZAKPOS**: disrupted since Feb 2022 (Russian invasion). Status unknown.

### BY — Belarus
- No public endpoint; state-controlled; international isolation.

### RU — Russia
- **SDCM**: SBAS/L-band satellite only, not NTRIP. No public caster.

---

## Americas — North

### US — United States
- **EarthScope NOTA**: `ntrip.earthscope.org:2101` (RTCM 3.3), also `:2105` (BINEX), `:2108` (PPP solutions). ~1000+ stations, single-base raw RTCM 3.3 MSM. Free for non-commercial use (annual NULA renewal; unlimited seats). Commercial use licensed per-seat. Legacy UNAVCO platform fully retired 2025-07-29; all users must use ntrip.earthscope.org. Americas-wide; station spacing ~30–50 km in many states. Candidate for pipeline (non-commercial TOS; metadata/station-list display permitted per NULA).
- **State DOT networks** (representative free ones): NYSNet (NY), MDOT CORS/MSRN (MI), MnCORS (MN), WISCORS (WI, 115+ stations), ORGN (OR). Many more exist; EarthScope fills gaps.
- **Restricted state networks**: TxDOT RTN (employees/contractors only), CaltransRTN (vetted partners only), WSRN WA (~$1,900/yr).
- No federal free NTRIP: NOAA/NGS real-time service shut Apr 2013 (budget sequestration). Not revived.

### CA — Canada
- No national or provincial free NTRIP. NRCan is post-processing only (CACS/CSRS RINEX). Vast geography, low rural density. Some Centipede volunteer nodes exist. User-facing: "No public free NTRIP; commercial VRS available."

---

## Americas — Latin

### BR — Brazil
- **RBMC-IP** (IBGE): `170.84.40.52:2101` (alt: `gps-ntrip.ibge.gov.br:2101`), 150 stations as of Dec 2024 (IBGE inaugurated 5 new stations Dec 2024; 2 more planned 2025), single-base RTCM 3.2 MSM. Free, gov.br signup. 5-station limit per user; 1,000 concurrent max. Candidate for pipeline.

### AR — Argentina
- **RAMSAC-NTRIP** (IGN): `ntrip.ign.gob.ar:2101`, ~69 stations, single-base. Free, email ntrip@ign.gob.ar or portal. 8-hour session cap per connection. POSGAR 07 reference frame. Candidate for pipeline.

### CO — Colombia
- **IGAC MAGNA-ECO**: `sbc.igac.gov.co:2101` (VRS/network) / `:2102` (single-base), 233 stations (IGAC + SGC + others), VRS capable. Registration at redgeodesica-sbc.igac.gov.co/sbc (Spider Business Center); free after account approval. Law 1955/2019 mandates public access. National Geodetic Control Centre launched Apr 2024 (Resolution 1771/2024 established portal). First confirmed free VRS/NRTK in Latin America. Candidate for pipeline.

### MX — Mexico
- **RGNA** (INEGI): RINEX post-processing only; no streaming NTRIP caster. User-facing: "No free public RTK."

### CL — Chile
- **RGN/SIRGAS-CHILE** (IGM): RINEX downloads only; no streaming caster. User-facing: "No free public RTK."

### PE — Peru
- **REGPMOC** (IGN/MoD): caster at `190.12.71.75:2101` requires MoD-issued licence (professional/commercial only). Not accessible for hobbyists.

### CU — Cuba
- **GEOCUBA**: 13 stations; no public endpoint; state enterprise; connectivity constraints.

---

## Asia Pacific — Oceania

### AU — Australia
- **AUSCORS** (Geoscience Australia): `ntrip.data.gnss.ga.gov.au:2101` (also port 443 TLS), 700+ stations (5,500+ registered users as of 2024), single-base RTCM 3.x. Free, web signup (gnss.ga.gov.au/stream then register). **CC BY 4.0** — attribute "© Commonwealth of Australia (Geoscience Australia) [year]". Old host `auscors.ga.gov.au` dead since Jul 2022. Candidate for pipeline.
- State VRS (CORSnet-NSW, GPSnet VIC, etc.): cost-recovery, paid.

### NZ — New Zealand
- **PositioNZ-RT** (LINZ / Toitū Te Whenua): `positionz-rt.linz.govt.nz:2101`, 37 CORS stations (NZ mainland + Chatham Islands + Antarctica), single-base RTCM. Free, LINZ account required (linz.govt.nz); email positionz@linz.govt.nz for credentials. **CC BY 4.0 NZ** — attribute "Source: Land Information New Zealand". Streaming latency reduced ~90% (Dec 2023 upgrade). Service is 24/7 with best-efforts uptime. Candidate for pipeline.

---

## Asia Pacific — East Asia

### JP — Japan
- **GEONET** (GSI): post-processing RINEX only; no public NTRIP.
- **MIRAI** (Cabinet Office SPAC / Go!GNSS): `ntrip.go.gnss.go.jp:2101`, ~300+ stations including overseas partners, single-base raw RTCM 3 observations. Free for scientific, educational, and **commercial** use (all peaceful purposes). Registration at go.gnss.go.jp + separate NtripCaster authorization application. Accounts deleted after 365 days inactivity. Raw observations only (rover computes RTK baseline). TOS permits automated fetching — data shared openly for all users. L1C/B support for QZSS QZS-6 added Jun 2025. Candidate for pipeline.
- **QZSS CLAS**: satellite-delivered (L6 band), not NTRIP; free, cm-level, no internet. Out of scope for this map.
- **GeoRTK** (Geosense): `geortk.jp:2101`, free, no registration. **Already in pipeline** (~200 stations with valid coords).
- Commercial: SoftBank ichimill ¥5–8k/month; Docomo GNSS.

### KR — South Korea
- **CORS-KOREA** (NGII): `www.gnssdata.or.kr:2101`, ~90–100 stations at ~40 km spacing, VRS + FKP. Free (NGII provides network RTK free of charge). Login uses registered email as NTRIP username. Registration via gnssdata.or.kr (Korean-language portal; Korean national ID may be required — verify if international access is practical). Candidate for pipeline.

### CN — China
- **Qianxun** (千寻知寸, Alibaba+Norinco JV): ~¥3,600–3,800/yr. No free tier. Surveying and Mapping Law 2017 restricts CORS; provincial networks for licensed surveyors only. User-facing: "Paid VRS available; no free public access."

### TW — Taiwan
- **e-GNSS** (NLSC/MoI): pay-per-use + paper form registration (mail/fax). Cost-recovery. DROP.

### HK — Hong Kong
- **SatRef** (Lands Department / Survey & Mapping Office): `ntrip.geodetic.gov.hk:2101`, mountpoints including `VRS32G` (GPS+GLONASS+Galileo+BeiDou VRS). 19 CORS (16 reference + 3 integrity monitoring). Free, email geodetic@landsd.gov.hk for account, or via DATA.GOV.HK open-data path. 4-constellation. Open data policy (commercial and non-commercial reuse permitted). Migrated to `ntrip.geodetic.gov.hk` Jun 2023 (old `www.geodetic.gov.hk` domain for NTRIP decommissioned). Accounts inactive 12+ months terminated. Candidate for pipeline.

### SG — Singapore
- **SiReNT** (SLA): SGD $107/month. 3-day trial requires SingPass (residents only). DROP.

---

## Asia Pacific — South & SE Asia

### IN — India
- **SoI-CORS** (Survey of India): 1,105+ stations. NTRIP caster at `cors.surveyofindia.gov.in`. Free for Central/State Government and government academic institutions. Private users charged (₹5,032/month or similar cost-recovery rate). Promotional free 3-month window Nov 2025–Jan 2026 expired; no confirmed extension as of Apr 2026. Worth revisiting if policy changes (SoI social media channels for announcements).

### ID — Indonesia
- **InaCORS** (BIG): `nrtk.big.go.id:2001` (**port 2001, not 2101**), 200+ stations, VRS (MAX, i-MAX, VRS). Free, self-service registration (nrtk.big.go.id). Law No. 4/2011 mandates free public geospatial service. Candidate for pipeline.

### TH — Thailand
- **DOL LandGNSS** (Dept of Lands): 100–250 stations. Registration at dol-rtknetwork.com (Thai language only). Free vs paid **unconfirmed**; NTRIP host:port not publicly documented in English. **Direct contact with Dept of Lands required before including.**

### VN — Vietnam
- **VNGEONET**: 65 stations. Free until Aug 2024; Circular 47/2024/TT-BTC imposed fees Sep 2024. Out of scope.

### MY — Malaysia
- **MyRTKnet** (JUPEM): 78 stations. Paid subscription (Survey Act cost-recovery). No free tier.

### PH — Philippines
- **PAGeNet** (NAMRIA): 52 stations. PHP 1,000 one-time + ongoing subscription (EO 471). No free hobbyist access.

### BD — Bangladesh
- **SOB VRS**: only 6 stations covering 147,000 km² — baselines 100–200 km, inadequate for RTK. Access unclear.

---

## Middle East & Africa

### SA — Saudi Arabia
- **KSA-CORS** (GASGI/GEOSA): `KSACORS.gcs.gov.sa:2101`, 209 stations, VRS. Free, download + email signed form to info@geosa.gov.sa (ksacors.gcs.gov.sa/RegisterAccount.aspx). GPS+GLO+GAL+BDS. Candidate for pipeline.

### IL — Israel
- **APN** (Survey of Israel): `mapigps.co.il`, likely free for licensed surveyors/researchers (email apn@mapi.gov.il). **Important caveat: intense military GNSS spoofing/jamming active across Israel + Lebanon/Jordan/Sinai/Cyprus since October 2023. RTK unreliable regardless of NTRIP access.** Map UI should flag this region.

### AE — UAE
- **DVRS** (Dubai Municipality): 18+ stations, VRS, 4-constellation. Professional application only (dm.gov.ae). No public hobbyist path.

### IR — Iran
- **IPGN/SHIMIM** (NCC): inward-facing governance; US/EU sanctions; geospatial data treated as sensitive. No public endpoint.

### IQ — Iraq
- **IGRS**: only 7 stations at 500–800 km spacing — far too wide for RTK. No public caster.

### EG — Egypt
- **ESA CORS + NACN** (~40 stations): internal use only; Nile Delta + Cairo corridor. No public access.

### DZ — Algeria
- **AL-CORS-Net / REGAT** (INCT): under Ministry of National Defence — security-sensitive. No public caster.

### NG — Nigeria
- **NIGNET**: 11–15 stations at 500–1,000 km spacing — far too wide for RTK. No public caster.

### ZA — South Africa
- **TrigNet** (NGI): `trignet.co.za:2101`, 55+ stations. Mixed: DGPS (~0.35 m) + single-base RTK + VRS clusters in Gauteng, Western Cape, KwaZulu-Natal only. Free, register at trignet.co.za. No explicit CC licence; public mandate. Candidate for pipeline.

---

## Open questions

1. **LitPOS (LT)**: contact LitPOS@geoportal.lt to confirm free status before ingesting.
2. **IceCORS (IS)**: confirm NTRIP host:port and free status (low priority).
3. **Thailand DOL LandGNSS**: contact Dept of Lands directly; host:port and free status unconfirmed.
4. **GPSBru/AGN (BE-Brussels)**: single station; confirm host and operational status if including.
5. **Registration credentials**: obtain for registration-required networks (ASG-EUPOS, FLEPOS, WALCORS, ERGNSS, AUSCORS, PositioNZ, CORS-KOREA, InaCORS, KSA-CORS, etc.) to store as GitHub Actions secrets and ingest.
6. **ESTPOS (EE) expiry**: service is free until Aug 2026; review before that date.
7. **MIRAI (JP) authorization flow**: confirm whether bot/automated fetch is permitted under the registration TOS.

## Pipeline status summary

| Status | Networks |
|---|---|
| **In pipeline** | rtk2go, Centipede, FReDNet (IT), GeoRTK (JP), SAPOS ×13 (DE) |
| **Candidate — no-registration** | SPSLux (LU) |
| **Candidate — registration required** | ASG-EUPOS (PL), FLEPOS (BE), WALCORS (BE), ERGNSS (ES), CROPOS (HR), ESTPOS (EE), LatPos (LV), AUSCORS (AU), PositioNZ-RT (NZ), RBMC-IP (BR), RAMSAC (AR), IGAC MAGNA-ECO (CO), TrigNet (ZA), KSA-CORS (SA), InaCORS (ID), CORS-KOREA (KR), SatRef (HK), EarthScope NOTA (US) |
| **Verify first** | LitPOS (LT), IceCORS (IS), Thailand DOL LandGNSS, GPSBru (BE) |
| **Paid / drop** | swipos (CH), SWEPOS (SE), CPOS (NO), SIGNAL (SI), HEPOS (GR), ROMPOS (RO), SiReNT (SG), e-GNSS (TW), MyRTKnet (MY), PAGeNet (PH) |
