# Free RTK NTRIP — country-by-country survey

_Purpose: ground truth for pipeline additions and the map's gap messaging._
_Organised by region. Each entry records: network name · endpoint · free/paid
status and basis · registration path · user-facing note for the map UI · open
questions. Entries with confirmed free endpoints are candidates for the
`SOURCES` list in `scripts/fetch_stations.py`._

_Last updated: 2026-04-20. Supersedes `.tmp/country-coverage.md`._

_Volunteer station counts (rtk2go / Centipede) are drawn from the live
`data/stations.json` as of 2026-04-19 and will drift over time as bases go
on/off-line. Use them as order-of-magnitude guidance, not precise figures._

---

## Europe — Western

### DE — Germany
- **SAPOS GEPOS** (BKG federal): `bkg1.positioning-service.net:2101` (alt: `caster.gepos.sapos.de:2101`) — no registration, CC-BY 4.0, free. PPP-RTK/SSR corrections via SSRZ format (not standard OSR RTCM); requires SSR-capable receiver or Geo++ SSR2OBS converter software (freely available). Continuous from Apr 2026 (was in optimization phase 2025–Mar 2026). Also broadcast via DAB+ radio.
- **SAPOS HEPS/EPS** (per-Bundesland): ~270 stations, VRS. Most Länder free. RP confirmed free (LVermGeo). ST confirmed free (LVermGeo). BY: free for agriculture via Landwirtschaftskammer; ~€20/yr for general/hobbyist use — **not fully free**. SN (Sachsen) endpoint unconfirmed, omitted from pipeline. All require per-Länder web registration. **Already in pipeline** (13 state casters; see `SOURCES` prefix `sapos_`).
- **Centipede**: ~3 volunteer DE nodes — negligible for a country already well-served by SAPOS.

### AT — Austria
- **APOS** (BEV): `aposrtk.bev.gv.at:2101`, 37 stations, VRS. Free for agriculture/forestry since Feb 2021 (requires eAMA credentials — farm client number + PIN from Agrarmarkt Austria). Professional/hobbyist use paid (BEV portal subscription). User-facing: "Paid VRS available (free only for ag/forestry sector via eAMA)."
- **rtk2go**: ~14 volunteer AT bases.
- **Centipede**: ~1 volunteer AT node.

### CH — Switzerland
- **swipos** (swisstopo): CHF 1,500/yr. *Geoinformationsgesetz* SR 510.62 classifies RTK as a value-added service; no free tier. User-facing: "Paid VRS available (swipos ~CHF 1,500/yr)."
- **rtk2go**: ~20 volunteer CH bases.
- **Centipede**: ~27 volunteer CH nodes (appearing as country code `CHZ` in the sourcetable; coordinates confirm they are across the Swiss plateau and Jura). Together with rtk2go, these provide partial free coverage for hobbyists willing to live without guaranteed uptime.

### FR — France
- **Centipede**: `crtk.net:2101` — free, no registration, ~719 volunteer bases in mainland France (as of Apr 2026 sourcetable), densest coverage in France. **Already in pipeline.**
- **rtk2go**: ~7 volunteer FR bases — minimal alongside Centipede.
- Commercial VRS: Teria (Hexagon), Orphéon (Trimble) — paid.

### BE — Belgium
- **FLEPOS** (Flanders): `flepos.vlaanderen.be:2101` (old `ntrip.flepos.be` dead 2026-04), 45 stations, VRS. Free for all uses (surveying and machine control), web self-signup at flepos.vlaanderen.be. In pipeline (endpoint currently timing out in CI — under investigation).
- **WALCORS** (Wallonia): `gnss.wallonie.be:2101`, 23 stations, VRS. Free for "positioning" uses (survey, GIS, drones). Paid for machine-control/auto-guidance since Jan 2013 (commercial resellers buy raw stream; not a hobbyist restriction in practice). Registration at gnss.wallonie.be (gnss@spw.wallonie.be). Candidate for pipeline.
- **GPSBru/AGN** (Brussels NGI): `agn.ngi.be` — endpoint confirmed at ngi.be; single station (Uccle observatory); NTRIP access via AGN portal. Operational as of mid-2024 (status page at agn.ngi.be). Free, registration via NGI. Low priority (single base; useful only within ~30 km of Brussels).

### NL — Netherlands
- No public free NTRIP. Market fully privatised since ~2000 (06-GPS/Trimble). User-facing: "Paid VRS available."
- **Centipede**: ~25 volunteer NL nodes. **rtk2go**: ~24 volunteer NL bases. Together they provide real but uneven volunteer coverage — not a substitute for a coordinated VRS, but functional for many hobbyist use cases.

### LU — Luxembourg
- **SPSLux** (ACT — Administration du Cadastre et de la Topographie): `stream.spslux.lu:5005` (**port 5005, not 2101**; IP 185.106.24.68), VRS. Luxembourg open-data policy — all services free of charge. Free self-signup at spslux.lu/SBC/Account/Register; then subscribe to "SPSLUX (N)RTK" package in the SBC shop. Candidate for pipeline.

### IE — Ireland
- No public free NTRIP. OSi routes users to Trimble VRS Now (commercial).
- **Centipede**: ~9 volunteer IE nodes. **rtk2go**: ~12 volunteer IE bases. Sparse but growing community coverage — baseline quality varies widely.

### GB — United Kingdom
- No public free NTRIP. OS Net raw data licensed to commercial resellers (SmartNet/Leica, TopNET/Trimble) under OS licence model since 2005. User-facing: "Paid VRS available (SmartNet, TopNET, etc.)."
- **Centipede**: ~43 volunteer GB nodes (appearing as country code `ENG` in the sourcetable). **rtk2go**: ~61 volunteer GB bases. Combined, these are the largest volunteer RTK cluster in the British Isles — distributed unevenly across England, with sparser coverage in Wales/Scotland/Northern Ireland. Not a substitute for a national VRS, but genuinely useful in well-served areas.

---

## Europe — Southern

### ES — Spain
- **ERGNSS** (IGN): `ergnss-ip.ign.es:2101`, ~120 stations, VRS. Free, web self-signup (ergnss.ign.es/gnuserportal/), immediate. CC-compatible (Orden FOM/2807/2015); attribution to IGN required. GPS+GLO+GAL+BDS. Server confirmed operational (SNIP monitor shows up as of Mar 2026). Candidate for pipeline.
- **RAP** (Andalucia, Junta): supplements ERGNSS in the south; separate signup (rap@juntadeandalucia.es).
- **rtk2go**: ~8 volunteer ES bases. **Centipede**: ~1 volunteer ES node.

### PT — Portugal
- **ReNEP** (DGT — Direção-Geral do Território): 47 stations, VRS + single-base. Free, portal signup at renep.dgterritorio.gov.pt (renep@dgterritorio.pt). Host:port **withheld until post-registration** — stations and RINEX publicly visible; NTRIP credentials provided after account approval. ETRS89 datum (mainland), ITRF93 (autonomous regions). Candidate for pipeline (requires registration first to get host).

### IT — Italy
- No national free public caster. Regional networks vary per region.
- **FReDNet** (OGS, Friuli-Venezia Giulia): `gnsscaster.regione.fvg.it:8080`, 16 stations, VRS. Sourcetable publicly readable; stream requires email registration (rete.gnss.marussi@regione.fvg.it, free). **Already in pipeline** (sourcetable fetch confirmed working, 39 STR lines including VRS virtual mountpoints).
- **rtk2go**: ~12 volunteer IT bases. **Centipede**: ~3 volunteer IT nodes.

### HR — Croatia
- **CROPOS** (DGU): `gnss.cropos.hr:2101`, 35 stations, VRS. **Free since Apr 2022** (Narodne novine 39/2022 — DPS and VPPS no longer charged). Email/web registration dgu@dgu.hr. DPS (~0.3–0.5 m) and VPPS (~2 cm) free; GPPS post-processing paid. Note: NTRIP caster IP changed Nov 2023 (old: 195.29.118.122 → new: 195.29.198.194); DNS hostname `gnss.cropos.hr` should resolve correctly but verify if pipeline has connectivity issues. Candidate for pipeline.

### SI — Slovenia
- **SIGNAL** (GURS): **PAID €829.44/yr** (€622.08 early discount). No free tier. DROP.
- **rtk2go**: ~4 volunteer SI bases. **Centipede**: ~5 volunteer SI nodes.

### GR — Greece
- **HEPOS** (HEPOS S.A.): ~€480/yr for 1-year unlimited RTK; also €160 for 3 months or per-minute pricing. No free tier. User-facing: "Paid VRS available (HEPOS ~€480/yr)."
- **URANUS**: commercial TopNET Live (Topcon). DROP.
- **rtk2go**: ~2 volunteer GR bases. **Centipede**: ~2 volunteer GR nodes.

### CY — Cyprus
- DLS network: internal use only, not public NTRIP.
- Note: rtk2go's active spoofing exclusion for IL/Lebanon/Jordan/Sinai also affects Cyprus intermittently (spoofing radius reaches southern Cyprus).

---

## Europe — Northern

### SE — Sweden
- **SWEPOS** (Lantmäteriet): RTK tier paid (subscription). DGNSS tier (`dgnss-swepos.lm.se:2101`) is free, requires account (free registration), RTCM 2.3 — **~0.2 m horizontal accuracy, sub-metre only, out of scope**. User-facing: "Paid VRS available (SWEPOS Network RTK); free DGNSS at ~0.2 m not sufficient for this map."
- **rtk2go**: ~29 volunteer SE bases. **Centipede**: ~1 volunteer SE node. Volunteer coverage exists but is thin relative to Sweden's large area; most bases appear concentrated in the south.

### NO — Norway
- **CPOS/ETPOS** (Kartverket): NOK 8,000+/yr. No free RTK tier. User-facing: "Paid VRS available."
- **rtk2go**: ~25 volunteer NO bases. **Centipede**: ~21 volunteer NO nodes. Together ~46 volunteer bases — reasonable coverage in populated areas (Oslofjord, Vestlandet); sparse north of ~63°N.

### DK — Denmark
- **GPSnet** (privatised ~2000): no public free caster. Market fully private (Leica/Hexagon). User-facing: "Paid VRS available."
- **rtk2go**: ~16 volunteer DK bases. **Centipede**: ~9 DNK + 9 DAN nodes (both country codes resolve to Denmark geographically). Together ~34 volunteer bases — reasonable hobbyist coverage particularly in Jutland and the major islands.

### FI — Finland
- **FINPOS** (NLS / Maanmittauslaitos): RTK service (`finpos.nls.fi:2101`) granted only for research/testing; applicants must justify need, access is 3 months renewable with feedback. No general public tier. DGNSS free (open data, best ~0.5 m accuracy) but sub-metre. User-facing: "No public free RTK; research applications only."
- **rtk2go**: **~111 volunteer FI bases** — the largest national concentration on rtk2go after the USA. Combined with ~14 Centipede FI nodes this gives de facto near-national free RTK coverage in Finland, almost entirely through volunteer infrastructure. Many stations use standard `FIN_<locality>` naming. Station quality ranges from survey-grade to DIY; uptime is not guaranteed.

### IS — Iceland
- **IceCORS** (LMÍ — Landmælingar Íslands, National Land Survey of Iceland): `moe.lmi.is:2101` (IP 178.19.53.126:2101), ~20+ stations, VRS/single-base. Registration required (lmi.is/is/maelingar/thjonustur/icecors); operated by Geo++ GNNET software. Free status unconfirmed — likely charged as a professional service given sparse population / cost recovery model. **Verify cost before including; low priority.**

### EE — Estonia
- **ESTPOS** (Maa-amet / Land and Spatial Development Board): `gnss-rtk.maaamet.ee:8083`, 40 stations, VRS. **Free until 31 August 2026** per director-general directive. Portal account + service agreement required (geoportaal.maaamet.ee). VRS, iMAX, nearest-base; MSM5 available. Candidate for pipeline (note expiry; review before Aug 2026).

### LV — Latvia
- **LatPos** (LGIA): `latpos.lgia.gov.lv:5001` (**port 5001, not 2101** — confirmed per Alberding caster directory), 27 LV + 5 EE + 4 LT border stations, VRS. Free since 2018. SBC portal signup (latpos.lgia.gov.lv/SBC). In pipeline (CI times out — likely egress firewall on non-standard port).

### LT — Lithuania
- **LitPOS** (GIS-Centras, Geoportal.lt): 35 stations, VRS + DGPS. Services: RTK (~2 cm), DGPS (~0.3–0.5 m), GPPS post-processing. RTCM 2.1/2.3/3.1/3.2, CMR, CMR+, CMRx formats available. NTRIP endpoint not publicly listed without registration. **Free status confirmed uncertain** — registration at geoportal.lt/geoportal/web/litpos-en; pricing not displayed publicly. Contact LitPOS@geoportal.lt to confirm free status before ingesting.

### PL — Poland
- **ASG-EUPOS** (GUGiK): `system.asgeupos.pl:2101` (also :8080/:8082/:8083/:8086 for VRS variants), 130+ stations. **Free since Oct 2022** (all services, including RTK and DGNSS). Web self-signup at system.asgeupos.pl, admin approval 1–2 working days. GPS+GLO+GAL+BDS. VRS (NAWGIS/KODGIS/FKP/MAC). Candidate for pipeline.
- **rtk2go**: ~51 volunteer PL bases — third-largest national cluster on rtk2go. Well-distributed across the country.

---

## Europe — Eastern / Balkans

### RO — Romania
- **ROMPOS**: credit-based paid system. No open-data GNSS mandate. User-facing: "Paid VRS available (ROMPOS)."
- **Centipede**: ~7 ROM + 2 ROU volunteer nodes (both codes resolve to Romania). **rtk2go**: ~6 volunteer RO bases. Modest volunteer coverage concentrated near major cities.

### HU — Hungary
- **GNSSnet.hu**: likely paid.
- **Centipede**: **~223 volunteer HU nodes** — Hungary is the single largest non-France country in the Centipede sourcetable. Combined with ~5 rtk2go HU bases, this gives near-national free RTK coverage. Most Centipede HU stations are in the Great Hungarian Plain and northern Hungary; coverage in the mountainous north-east is thinner.

### CZ — Czech Republic
- **CZEPOS**: free for education/government; commercial use paid (ČÚZK Decree 31/1995). Not a general hobbyist path.
- **Centipede**: ~3 volunteer CZ nodes. **rtk2go**: ~4 volunteer CZ bases.

### SK — Slovakia
- **SKPOS**: free for public sector/municipalities; commercial use paid. Not a general hobbyist path.
- **rtk2go**: ~2 volunteer SK bases.

### BG — Bulgaria
- No government network. Commercial only.
- **rtk2go**: ~6 volunteer BG bases. **Centipede**: ~1 volunteer BG node.

### RS — Serbia
- **AGROS** (RGZ): paid; no English pricing page.
- **Centipede**: ~11 SER + 3 SRB nodes (both country codes resolve to Serbia/Vojvodina geographically). **rtk2go**: ~28 volunteer RS bases. Together ~42 volunteer bases — one of the denser volunteer clusters in the Western Balkans.

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
- **rtk2go**: ~3 volunteer UA bases; status uncertain given the conflict.

### BY — Belarus
- No public endpoint; state-controlled; international isolation.

### RU — Russia
- **SDCM**: SBAS/L-band satellite only, not NTRIP. No public caster.

---

## Europe — Territories and dependencies

_Entries here cover non-sovereign territories that appear in caster sourcetables
with distinct country codes. Most coverage comes from Centipede volunteer nodes._

### SJ — Svalbard (Norway)
- **Centipede**: 1 volunteer node (`NYAWIPEV`, lat ~78.9°N — likely at Ny-Ålesund research station). Single base; useful only within ~30–40 km. RTK is feasible in summer field conditions but very remote.

### GL — Greenland (Denmark)
- **rtk2go**: 1 volunteer base near Kangerlussuaq (Søndre Strømfjord, ~67°N). Isolated; coverage is effectively zero for most of Greenland.

### AX — Åland Islands (Finland)
- **Centipede**: ~2 volunteer nodes (country code `ALA` in sourcetable). Small archipelago between Finland and Sweden; partial coverage.

### French overseas territories

The Centipede network has volunteer nodes in several French overseas territories, served via the main `crtk.net:2101` caster:

| Territory | Code in sourcetable | Stations | Notes |
|---|---|---|---|
| Réunion (RE) | `REU` | ~4 Centipede | Indian Ocean island; partial coverage |
| Martinique (MQ) | `MTQ` | ~1 Centipede | Lesser Antilles; single base |
| New Caledonia (NC) | `NCL` | ~2 Centipede | Pacific territory; sparse |
| French Polynesia (PF) | `PYF` | ~2 Centipede | Pacific archipelago; sparse |

Coverage in each territory is thin (1–4 nodes over large areas), but where a base exists within 30–50 km the corrections are usable.

---

## Americas — North

### US — United States
- **EarthScope NOTA**: `ntrip.earthscope.org:2101` (RTCM 3.3), also `:2105` (BINEX), `:2108` (PPP solutions). ~1000+ stations, single-base raw RTCM 3.3 MSM. Free for non-commercial use (annual NULA renewal; unlimited seats). Commercial use licensed per-seat. Legacy UNAVCO platform fully retired 2025-07-29; all users must use ntrip.earthscope.org. Americas-wide; station spacing ~30–50 km in many states. Candidate for pipeline (non-commercial TOS; metadata/station-list display permitted per NULA).
- **State DOT networks** (representative free ones): NYSNet (NY), MDOT CORS/MSRN (MI), MnCORS (MN), WISCORS (WI, 115+ stations), ORGN (OR). Many more exist; EarthScope fills gaps.
- **Restricted state networks**: TxDOT RTN (employees/contractors only), CaltransRTN (vetted partners only), WSRN WA (~$1,900/yr).
- **rtk2go**: **~142 volunteer US bases** — the largest single-country cluster on rtk2go. Dense in the upper Midwest, Pacific Northwest, and mid-Atlantic; sparse across the Great Plains and interior South.
- **Centipede**: ~3 volunteer US nodes.
- No federal free NTRIP: NOAA/NGS real-time service shut Apr 2013 (budget sequestration). Not revived.

### CA — Canada
- No national or provincial free NTRIP. NRCan is post-processing only (CACS/CSRS RINEX). Vast geography, low rural density. User-facing: "No public free NTRIP; commercial VRS available."
- **rtk2go**: ~56 volunteer CA bases. **Centipede**: ~13 volunteer CA nodes. Combined ~69 volunteer bases — concentrated heavily in British Columbia, Ontario, and southern Quebec. Coverage outside urban corridors is very thin relative to the country's area.

---

## Americas — Latin

### BR — Brazil
- **RBMC-IP** (IBGE): `170.84.40.52:2101` (alt: `gps-ntrip.ibge.gov.br:2101`), 150 stations as of Dec 2024 (IBGE inaugurated 5 new stations Dec 2024; 2 more planned 2025), single-base RTCM 3.2 MSM. Free, gov.br signup. 5-station limit per user; 1,000 concurrent max. Candidate for pipeline.
- **rtk2go**: ~17 volunteer BR bases, concentrated in São Paulo and southern states.

### AR — Argentina
- **RAMSAC-NTRIP** (IGN): `ntrip.ign.gob.ar:2101`, ~69 stations, single-base. Free, email ntrip@ign.gob.ar or portal. 8-hour session cap per connection. POSGAR 07 reference frame. Candidate for pipeline.
- **rtk2go**: ~6 volunteer AR bases, mostly around Buenos Aires and Córdoba.

### CO — Colombia
- **IGAC MAGNA-ECO**: `sbc.igac.gov.co:2101` (VRS/network) / `:2102` (single-base), 233 stations (IGAC + SGC + others), VRS capable. Registration at redgeodesica-sbc.igac.gov.co/sbc (Spider Business Center); free after account approval. Law 1955/2019 mandates public access. National Geodetic Control Centre launched Apr 2024 (Resolution 1771/2024 established portal). First confirmed free VRS/NRTK in Latin America. Candidate for pipeline.

### MX — Mexico
- **RGNA** (INEGI): RINEX post-processing only; no streaming NTRIP caster. User-facing: "No free public RTK."
- **rtk2go**: ~2 volunteer MX bases.

### CL — Chile
- **RGN/SIRGAS-CHILE** (IGM): RINEX downloads only; no streaming caster. User-facing: "No free public RTK."
- **rtk2go**: ~1 volunteer CL base.

### PY — Paraguay / EC — Ecuador / CR — Costa Rica
- **rtk2go**: ~3 volunteer bases each (PRY, ECU, CRI). No known national free NTRIP caster in any of these countries.

### PE — Peru
- **REGPMOC** (IGN/MoD): caster at `190.12.71.75:2101` requires MoD-issued licence (professional/commercial only). Not accessible for hobbyists.

### CU — Cuba
- **GEOCUBA**: 13 stations; no public endpoint; state enterprise; connectivity constraints.

---

## Asia Pacific — Oceania

### AU — Australia
- **AUSCORS** (Geoscience Australia): `ntrip.data.gnss.ga.gov.au:2101` (also port 443 TLS), 700+ stations (5,500+ registered users as of 2024), single-base RTCM 3.x. Free, web signup (gnss.ga.gov.au/stream then register). **CC BY 4.0** — attribute "© Commonwealth of Australia (Geoscience Australia) [year]". Old host `auscors.ga.gov.au` dead since Jul 2022. Candidate for pipeline.
- **rtk2go**: ~27 volunteer AU bases. **Centipede**: ~3 volunteer AU nodes. Volunteer coverage is thin relative to Australia's size but supplements AUSCORS in densely populated south-eastern areas.
- State VRS (CORSnet-NSW, GPSnet VIC, etc.): cost-recovery, paid.

### NZ — New Zealand
- **PositioNZ-RT** (LINZ / Toitū Te Whenua): `positionz-rt.linz.govt.nz:2101`, 37 CORS stations (NZ mainland + Chatham Islands + Antarctica), single-base RTCM. Free, LINZ account required (linz.govt.nz); email positionz@linz.govt.nz for credentials. **CC BY 4.0 NZ** — attribute "Source: Land Information New Zealand". Streaming latency reduced ~90% (Dec 2023 upgrade). Service is 24/7 with best-efforts uptime. Candidate for pipeline.
- **rtk2go**: ~11 volunteer NZ bases, concentrated in the North Island and upper South Island.

---

## Asia Pacific — East Asia

### JP — Japan
- **GEONET** (GSI): post-processing RINEX only; no public NTRIP.
- **MIRAI** (Cabinet Office SPAC / Go!GNSS): `ntrip.go.gnss.go.jp:2101`, ~300+ stations including overseas partners, single-base raw RTCM 3 observations. Free for scientific, educational, and **commercial** use (all peaceful purposes). Registration at go.gnss.go.jp + separate NtripCaster authorization application. Accounts deleted after 365 days inactivity. Raw observations only (rover computes RTK baseline). TOS permits automated fetching — data shared openly for all users. L1C/B support for QZSS QZS-6 added Jun 2025. Candidate for pipeline.
- **QZSS CLAS**: satellite-delivered (L6 band), not NTRIP; free, cm-level, no internet. Out of scope for this map.
- **GeoRTK** (Geosense): `geortk.jp:2101`, free, no registration. **Already in pipeline** (~200 stations with valid coords; ~338 STR lines total, ~130–140 active at any time).
- **rtk2go**: ~24 volunteer JP bases, supplementing GeoRTK.
- Commercial: SoftBank ichimill ¥5–8k/month; Docomo GNSS.

### KR — South Korea
- **CORS-KOREA** (NGII): `www.gnssdata.or.kr:2101`, ~90–100 stations at ~40 km spacing, VRS + FKP. Free (NGII provides network RTK free of charge). Login uses registered email as NTRIP username. Registration via gnssdata.or.kr (Korean-language portal; Korean national ID may be required — verify if international access is practical). Candidate for pipeline.
- **rtk2go**: ~3 volunteer KR bases.

### CN — China
- **Qianxun** (千寻知寸, Alibaba+Norinco JV): ~¥3,600–3,800/yr. No free tier. Surveying and Mapping Law 2017 restricts CORS; provincial networks for licensed surveyors only. User-facing: "Paid VRS available; no free public access."

### TW — Taiwan
- **e-GNSS** (NLSC/MoI): pay-per-use + paper form registration (mail/fax). Cost-recovery. DROP.
- **rtk2go**: ~3 volunteer TW bases.

### HK — Hong Kong
- **SatRef** (Lands Department / Survey & Mapping Office): `ntrip.geodetic.gov.hk:2101`, mountpoints including `VRS32G` (GPS+GLONASS+Galileo+BeiDou VRS). 19 CORS (16 reference + 3 integrity monitoring). Free, email geodetic@landsd.gov.hk for account, or via DATA.GOV.HK open-data path. 4-constellation. Open data policy (commercial and non-commercial reuse permitted). Migrated to `ntrip.geodetic.gov.hk` Jun 2023 (old `www.geodetic.gov.hk` domain for NTRIP decommissioned). Accounts inactive 12+ months terminated. Candidate for pipeline.

### SG — Singapore
- **SiReNT** (SLA): SGD $107/month. 3-day trial requires SingPass (residents only). DROP.

---

## Asia Pacific — South & SE Asia

### IN — India
- **SoI-CORS** (Survey of India): 1,105+ stations. NTRIP caster at `cors.surveyofindia.gov.in`. Free for Central/State Government and government academic institutions. Private users charged (₹5,032/month or similar cost-recovery rate). Promotional free 3-month window Nov 2025–Jan 2026 expired; no confirmed extension as of Apr 2026. Worth revisiting if policy changes (SoI social media channels for announcements).

### ID — Indonesia
- **InaCORS** (BIG — Badan Informasi Geospasial): `nrtk.big.go.id:2001` (**port 2001, not 2101**; IP 103.22.171.6), 200+ stations, VRS (MAX, i-MAX, VRS). Free, self-service registration at nrtk.big.go.id. Over 16,800 registered users as of last report. Law No. 4/2011 mandates free public geospatial service. Candidate for pipeline.
- **rtk2go**: ~8 volunteer ID bases (concentrated in Java/Bali).

### TH — Thailand
- **DOL LandGNSS** (Dept of Lands, Ministry of Interior): website dol-rtknetwork.com (Thai language). Network managed by Technology Mapping Division. NTRIP connection details documented in Thai-language manual at dol-rtknetwork.com/index.php/npage/manual. Free vs paid status **unconfirmed for public/hobbyist use**; registration page available (dol-rtknetwork.com/index.php/register_gnss_beta). **Direct contact with Dept of Lands required before including.**
- **rtk2go**: ~2 volunteer TH bases.

### VN — Vietnam
- **VNGEONET** (National Centre for Satellite Positioning Station Management): 65 CORS stations (24 geodetic + 41 NRTK, 50–80 km spacing). Free until Aug 2024; Circular 47/2024/TT-BTC (Ministry of Finance) imposed fees effective Sep 2024. Fees apply to all stations with average spacing ≤80 km. **Out of scope.**

### MY — Malaysia
- **MyRTKnet** (JUPEM): 78 stations. Paid subscription (Survey Act cost-recovery). No free tier.

### PH — Philippines
- **PAGeNet** (NAMRIA): 52 stations. PHP 1,000 one-time + ongoing subscription (EO 471). No free hobbyist access.

### BD — Bangladesh
- **SOB VRS**: only 6 stations covering 147,000 km² — baselines 100–200 km, inadequate for RTK. Access unclear.

---

## Middle East & Africa

### SA — Saudi Arabia
- **KSA-CORS** (GASGI/GEOSA): `ksacors.geoportal.sa:2101` (migrated from `KSACORS.gcs.gov.sa` which is dead/NXDOMAIN 2026-04), 209 active stations, VRS. Free, registration: sign form and email to info@geosa.gov.sa. GPS+GLO+GAL+BDS. In pipeline (CI times out — egress firewall).

### IL — Israel
- **APN** (Survey of Israel): `mapigps.co.il`, likely free for licensed surveyors/researchers (email apn@mapi.gov.il). **Critical caveat: pervasive military GNSS spoofing traced to Ein Shemer Airfield active continuously since October 2023, affecting Israel + Lebanon + Jordan + Sinai + Cyprus + southern Turkey. 50,000+ flights affected in 2024 alone. GPS signals show false locations (e.g. receiver "appears" to be in Beirut or Cairo). RTK is unreliable regardless of NTRIP access.** Map UI should flag this entire region. DROP from pipeline until spoofing ceases.

### AE — UAE
- **DVRS** (Dubai Municipality): 18+ stations, VRS, 4-constellation. Professional application only (dm.gov.ae). No public hobbyist path.

### TR — Turkey
- **TUSAGA-Aktif** (TKGM/HGM joint): `212.156.70.42:2101` (also port 55600), 146 stations, VRS/FKP/MAC. **Paid subscription required.** Membership + annual fee to General Directorate of Land Registry (TKGM). DROP for free pipeline.
- **rtk2go**: ~3 volunteer TR bases.

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
- **TrigNet** (NGI / National Geospatial Information, DALRRD): `trignet.co.za:2101`, 55+ stations. Products: DGPS (~0.35 m) countrywide; single-base RTK (~5 cm) within 30–40 km; Network RTK (~3 cm) in Gauteng, Western Cape, KwaZulu-Natal clusters only. **All NGI products and services free of charge.** Register at trignet.co.za for credentials. No explicit CC licence; public mandate. Candidate for pipeline.
- **rtk2go**: ~1 volunteer ZA base. **Centipede**: ~1 volunteer ZA node.

### KE — Kenya
- **rtk2go**: ~1 volunteer KE base. No known national RTK network with public access.

### MA — Morocco
- **rtk2go**: ~1 volunteer MA base. No known national RTK network with public access.

### SN — Senegal
- **Centipede**: ~2 volunteer SN nodes. No national NTRIP caster.

### CI — Côte d'Ivoire
- **Centipede**: ~2 volunteer CI nodes (country code `CIV`). No national NTRIP caster.

---

## Open questions

1. **LitPOS (LT)**: Confirmed free (publicly-funded EUPOS member, registration at
   geoportal.lt/web/litpos-en). NTRIP host:port not publicly listed — find via
   public aggregators (ArduSimple, Alberding caster directory) before ingesting.

2. **IceCORS (IS)**: ✓ Confirmed free ("The data is free of charge" — natt.is).
   Endpoint `178.19.53.126:2101` (GNCASTER, same software as SAPOS). Sourcetable
   publicly accessible without auth. Offers VRS (VRS30, FKP30) and single-base
   (RTCM30). Stream credentials via email to icecors@natt.is. Added to pipeline.

3. **Thailand DOL LandGNSS**: ✓ Confirmed free government service. Registration at
   dol-rtknetwork.com. Move to pipeline candidate — find NTRIP host:port from
   public sources (ArduSimple list, user forums) before ingesting.

4. **CORS-KOREA (KR)**: Sourcetable publicly accessible without credentials (NTRIP
   spec). Stream registration portal is Korean-language only; Korean national ID
   likely required — limits practical utility for international users.

5. **ReNEP (PT) host:port**: Not disclosed pre-registration. Complete DGT
   registration at dgterritorio.gov.pt to obtain the NTRIP endpoint.

## Pipeline status summary

_As of 2026-04-20. "In pipeline" = present in `SOURCES` in `scripts/fetch_stations.py`._

| Status | Networks |
|---|---|
| **In pipeline** | rtk2go, Centipede, FReDNet (IT), GeoRTK (JP), SAPOS ×13 (DE) |
| **Candidate — no-registration** | SPSLux (LU), Thailand DOL LandGNSS (TH) |
| **Candidate — registration required** | ASG-EUPOS (PL), FLEPOS (BE), WALCORS (BE), ERGNSS (ES), CROPOS (HR), LatPos (LV), AUSCORS (AU), PositioNZ-RT (NZ), RBMC-IP (BR), RAMSAC (AR), IGAC MAGNA-ECO (CO), TrigNet (ZA), KSA-CORS (SA), InaCORS (ID), CORS-KOREA (KR), SatRef (HK), EarthScope NOTA (US, non-commercial NULA), MIRAI (JP), LitPOS (LT), IceCORS (IS) |
| **VRS — 0 stations** | ESTPOS (EE, VRS; also times out), CROPOS (HR, VRS) |
| **Verify first** | ReNEP (PT, host withheld pre-registration) |
| **Paid / drop** | swipos (CH), SWEPOS RTK (SE), CPOS (NO), SIGNAL (SI), HEPOS (GR), ROMPOS (RO), SiReNT (SG), e-GNSS (TW), MyRTKnet (MY), PAGeNet (PH), TUSAGA-Aktif (TR), VNGEONET (VN, fees since Sep 2024), SoI-CORS (IN, paid for private users), NETPOS/Kadaster (NL, restricted internal use) |
| **Out of scope (spoofing)** | APN (IL) — active GNSS spoofing makes RTK unreliable across Israel/Lebanon/Jordan/Sinai/Cyprus |
| **Out of scope (raw obs only)** | EUREF-IP, IGS-IP — no RTK streams; suitable for post-processing only |
| **Removed from pipeline** | RTKdata.online — server unreachable since launch; 0 stations ever collected; no independent data (Kansi Solutions GmbH, same parent as paid rtkdata.com) |
