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
- **SAPOS GEPOS** (BKG federal): `bkg1.positioning-service.net:2101` — no registration, CC-BY 4.0. PPP-RTK/SSR corrections (not standard RTK RTCM); requires SSR-capable receiver. Permanent from Apr 2026.
- **SAPOS HEPS/EPS** (per-Bundesland): ~270 stations, VRS. **12/16 Länder free** (BW, BE, BB, HB, HH, HE, MV, NI, NRW, SL, SN, TH); **paid**: BY (~€20/yr), RP (price TBC); **mixed**: ST. Per-state casters (e.g. `sapos-bw-ntrip.de:2101`, `sapos-th-ntrip.de:2101`); all require per-Länder web registration. **Already in pipeline** (13 state casters; see `SOURCES` prefix `sapos_`).
- **Centipede**: a handful of volunteer DE nodes.

### AT — Austria
- **APOS** (BEV): `aposrtk.bev.gv.at:2101`, 37 stations, VRS. Free **only for agriculture/forestry** (eAMA credentials). Professional/hobbyist use paid. User-facing: "Paid VRS available (free only for ag/forestry sector)."
- Centipede: minimal AT nodes.

### CH — Switzerland
- **swipos** (swisstopo): CHF 1,500/yr. *Geoinformationsgesetz* SR 510.62 classifies RTK as a value-added service; no free tier. User-facing: "Paid VRS available (swipos ~CHF 1,500/yr)."

### FR — France
- **Centipede**: `crtk.net:2101` — free, no registration, 625+ volunteer bases, densest coverage in France. **Already in pipeline.**
- Commercial VRS: Teria (Hexagon), Orphéon (Trimble) — paid.

### BE — Belgium
- **FLEPOS** (Flanders): `ntrip.flepos.be:2101`, 45 stations, VRS. Free, web self-signup at flepos.vlaanderen.be. Candidate for pipeline.
- **WALCORS** (Wallonia): `gnss.wallonie.be:2101`, 23 stations, VRS. Free for survey/GIS; paid for precision ag/auto-guidance since Jan 2013. Candidate for pipeline.
- **GPSBru/AGN** (Brussels): likely `ntrip.ngi.be:2101` (unconfirmed). Single station (Uccle); operational status uncertain. Low priority.

### NL — Netherlands
- No public free NTRIP. Market fully privatised since ~2000 (06-GPS/Trimble). User-facing: "Paid VRS available."

### LU — Luxembourg
- **SPSLux** (ACT): `stream.spslux.lu:5005` (**port 5005, not 2101**), VRS. Luxembourg open-data policy. SBC portal free signup. Candidate for pipeline.

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
- **ReNEP** (DGT): 47 stations, VRS. Free, portal signup at renep.dgterritorio.gov.pt. Host:port **withheld until post-registration** — stations publicly listed; host provided after approval.

### IT — Italy
- No national free public caster. Regional networks vary per region.
- **FReDNet** (OGS, Friuli-Venezia Giulia): `gnsscaster.regione.fvg.it:8080`, 16 stations, VRS. Sourcetable publicly readable; stream requires email registration (rete.gnss.marussi@regione.fvg.it, free). **Already in pipeline** (sourcetable fetch confirmed working, 39 STR lines).

### HR — Croatia
- **CROPOS** (DGU): `gnss.cropos.hr:2101`, 35 stations, VRS. **Free since Apr 2022** (Narodne novine 39/2022). Email/web registration dgu@dgu.hr. DPS (~0.3–0.5 m) and VPPS (~2 cm) free; GPPS post-processing paid. Candidate for pipeline.

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
- **SWEPOS** (Lantmäteriet): RTK tier ~SEK 15,000/yr. DGNSS tier (`dgnss-swepos.lm.se:2101`) is free but RTCM 2.3 sub-metre only — **out of scope**. User-facing: "Paid VRS available (SWEPOS ~SEK 15,000/yr)."

### NO — Norway
- **CPOS/ETPOS** (Kartverket): NOK 8,000+/yr. No free RTK tier. User-facing: "Paid VRS available."

### DK — Denmark
- **GPSnet** (privatised ~2000): no public free caster. Market fully private (Leica/Hexagon). User-facing: "Paid VRS available."

### FI — Finland
- **FINPOS** (NLS): free for 3-month research applications only; no general public tier. DGNSS free but sub-metre. User-facing: "No public free RTK; research applications only."

### IS — Iceland
- **IceCORS** (NLSI): reportedly free; NTRIP endpoint unconfirmed. Low priority — sparse population. Verify before including.

### EE — Estonia
- **ESTPOS** (Maa-amet): `gnss-rtk.maaamet.ee:8083`, 40 stations, VRS. **Free until 31 August 2026.** Portal account + service agreement required (geoportaal.maaamet.ee). VRS, iMAX, nearest-base; MSM5 available. Candidate for pipeline (note expiry).

### LV — Latvia
- **LatPos** (LGIA): `latpos.lgia.gov.lv:2101`, 27 LV + 5 EE + 4 LT border stations, VRS. **Free since 2018.** SBC portal signup (latpos.lgia.gov.lv/SBC). Candidate for pipeline.

### LT — Lithuania
- **LitPOS** (Geoportal.lt): 35 stations, VRS likely. **Free status unconfirmed** — pricing not publicly displayed. Likely free given EUPOS/government mandate. Contact LitPOS@geoportal.lt before ingesting.

### PL — Poland
- **ASG-EUPOS** (GUGiK): `system.asgeupos.pl:2101` (also :8080/:8082/:8083/:8086 for VRS variants), 130+ stations. **Free since Oct 2022.** Web self-signup, admin approval 1–2 working days. GPS+GLO+GAL+BDS. VRS (NAWGIS/KODGIS/FKP/MAC). Candidate for pipeline.

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
- **EarthScope NOTA**: `ntrip.earthscope.org:2101`, ~1000+ stations, single-base raw RTCM 3.x. Free for non-commercial use (annual license renewal). Americas-wide; station spacing ~30–50 km in many states. Legacy UNAVCO platform retired 2025-07-29. Candidate for pipeline (non-commercial TOS; metadata/station-list display permitted per NULA).
- **State DOT networks** (representative free ones): NYSNet (NY), MDOT CORS/MSRN (MI), MnCORS (MN), WISCORS (WI, 115+ stations), ORGN (OR). Many more exist; EarthScope fills gaps.
- **Restricted state networks**: TxDOT RTN (employees/contractors only), CaltransRTN (vetted partners only), WSRN WA (~$1,900/yr).
- No federal free NTRIP: NOAA/NGS real-time service shut Apr 2013 (budget sequestration). Not revived.

### CA — Canada
- No national or provincial free NTRIP. NRCan is post-processing only (CACS/CSRS RINEX). Vast geography, low rural density. Some Centipede volunteer nodes exist. User-facing: "No public free NTRIP; commercial VRS available."

---

## Americas — Latin

### BR — Brazil
- **RBMC-IP** (IBGE): `170.84.40.52:2101` (alt: `gps-ntrip.ibge.gov.br:2101`), 150 stations, single-base RTCM 3.2 MSM. Free, gov.br signup. 5-station limit per user; 1,000 concurrent max. Candidate for pipeline.

### AR — Argentina
- **RAMSAC-NTRIP** (IGN): `ntrip.ign.gob.ar:2101`, ~69 stations, single-base. Free, email ntrip@ign.gob.ar or portal. 8-hour session cap per connection. POSGAR 07 reference frame. Candidate for pipeline.

### CO — Colombia
- **IGAC MAGNA-ECO**: `sbc.igac.gov.co:2101` (VRS) / `:2102` (single-base), 233 stations (120 IGAC + 105 SGC + others), VRS capable. Free, email/web signup (sbc.igac.gov.co). Law 1955/2019 mandates public access. First confirmed free VRS/NRTK in Latin America. Candidate for pipeline.

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
- **AUSCORS** (Geoscience Australia): `ntrip.data.gnss.ga.gov.au:2101` (also port 443 TLS), 700+ stations, single-base RTCM 3.x. Free, web signup (gnss.ga.gov.au/registration). **CC BY 4.0** — attribute "© Commonwealth of Australia (Geoscience Australia)". Old host `auscors.ga.gov.au` dead since Jul 2022. Candidate for pipeline.
- State VRS (CORSnet-NSW, GPSnet VIC, etc.): cost-recovery, paid.

### NZ — New Zealand
- **PositioNZ-RT** (LINZ): `positionz-rt.linz.govt.nz:2101`, 100+ stations, single-base. Free, LINZ account + email positionz@linz.govt.nz. **CC BY 4.0 NZ** — attribute "Source: Land Information New Zealand". NZ mainland + offshore islands. Candidate for pipeline.

---

## Asia Pacific — East Asia

### JP — Japan
- **GEONET** (GSI): post-processing RINEX only; no public NTRIP.
- **MIRAI** (Cabinet Office SPAC): `ntrip.go.gnss.go.jp:2101`, ~300+ stations including overseas partners, single-base raw RTCM 3 observations. Free with registration + separate authorization form. Accounts deleted after 365 days inactivity. Raw observations only (rover computes RTK baseline) — adequate for <50 cm use. Candidate for pipeline.
- **QZSS CLAS**: satellite-delivered (L6 band), not NTRIP; free, cm-level, no internet. Out of scope for this map.
- **GeoRTK** (Geosense): `geortk.jp:2101`, free, no registration. **Already in pipeline** (~200 stations with valid coords).
- Commercial: SoftBank ichimill ¥5–8k/month; Docomo GNSS.

### KR — South Korea
- **CORS-KOREA** (NGII): `www.gnssdata.or.kr:2101`, public password `gnss`, ~90 stations at ~40 km spacing, VRS + FKP. Free, registration via ngii.go.kr (Korean-only portal). Login mandatory since ~2023. Candidate for pipeline.

### CN — China
- **Qianxun** (千寻知寸, Alibaba+Norinco JV): ~¥3,600–3,800/yr. No free tier. Surveying and Mapping Law 2017 restricts CORS; provincial networks for licensed surveyors only. User-facing: "Paid VRS available; no free public access."

### TW — Taiwan
- **e-GNSS** (NLSC/MoI): pay-per-use + paper form registration (mail/fax). Cost-recovery. DROP.

### HK — Hong Kong
- **SatRef** (Lands Dept): `ntrip.geodetic.gov.hk:2101`, mountpoint `VRS32G`, 19 stations, VRS. Free, email geodetic@landsd.gov.hk. 4-constellation. Open data policy. Migrated to current domain Jun 2023. Accounts inactive 12+ months terminated. Candidate for pipeline.

### SG — Singapore
- **SiReNT** (SLA): SGD $107/month. 3-day trial requires SingPass (residents only). DROP.

---

## Asia Pacific — South & SE Asia

### IN — India
- **SoI-CORS** (Survey of India): 1,105+ stations. Free for government/academic use; ₹5,032/month for private users. Promotional free window Nov 2025–Jan 2026 expired. Worth revisiting if policy changes.

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
