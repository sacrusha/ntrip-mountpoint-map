# Free RTK NTRIP — country-by-country survey

_How is RTK positioning solved (or not) in each country? Who runs it, is it
free, what are the gaps, and what does a hobbyist or small shop actually get?_

_Technical detail (endpoints, credentials, pipeline status) lives in
`docs/networks.md`. Network references use the pattern `→ networks.md: \`id\``
at the end of the relevant bullet — preserving this exact form lets you audit
coverage with `grep "networks.md:" docs/country-survey.md`._

_Volunteer station counts (rtk2go / Centipede) are drawn from live
`data/stations.json` as of 2026-04-19 and will drift over time._

_Last updated: 2026-04-20._

---

## Europe — Western

### AT — Austria

- **Free* government RTK**: APOS (BEV, `aposrtk.bev.gv.at:2101`, 37 stations, VRS) —
  free for agriculture/forestry via eAMA credentials (farm client number + PIN from
  Agrarmarkt Austria); professional/hobbyist use paid via bev.gv.at portal. In pipeline
  as `conditions` access (Free* in UI). → networks.md: `apos`
- **Volunteer**: rtk2go ~14 AT bases, Centipede ~1 AT node.
- **Gap**: hobbyists without agricultural credentials must pay via BEV portal;
  volunteers (rtk2go) are the only unconditionally free option.

### BE — Belgium

- **Free government RTK**:
  - FLEPOS (Flanders, `flepos.vlaanderen.be:2101`, 45 stations VRS) — free for
    all uses; currently timing out in CI. → networks.md: `flepos`
  - WALCORS (Wallonia, `gnss.wallonie.be:2101`, 23 stations VRS) — free for
    positioning; paid for machine-control/auto-guidance. → networks.md: `walcors`
  - GPSBru/AGN (Brussels NGI, `agn.ngi.be`, 1 station) — free, registration;
    useful only within ~30 km of Brussels. Low priority. → networks.md: `gpsbru`
- **Volunteer**: rtk2go ~24 NL+BE volunteer bases (mixed), Centipede ~25 BE/NL nodes.
- **Gap**: FLEPOS and WALCORS are VRS-only (0 physical pins on map); NRTK polygons deferred.

### CH — Switzerland

- **Free government RTK**: none. swipos (swisstopo) CHF 1,500/yr;
  *Geoinformationsgesetz* SR 510.62 classifies RTK as a value-added service.
- **Volunteer**: rtk2go ~20 CH bases, Centipede ~27 CH nodes (country code `CHZ`).
  Concentrated on the Swiss plateau and Jura; partial free coverage for hobbyists
  willing to accept volunteer uptime.
- **Paid only**: swipos ~CHF 1,500/yr ≈ $1,650 — over cutoff.

### DE — Germany

- **Free government RTK**: SAPOS (16 Bundesländer, ~270 stations, VRS). Most
  states free. Bayern €20/yr flat rate for non-agricultural use. Sachsen endpoint
  recently confirmed. All require per-state web registration. → networks.md: `sapos_*`
  SAPOS GEPOS (BKG federal) broadcasts SSR/PPP-RTK in SSRZ format — not standard
  RTCM; requires SSR-capable receiver. Out of scope.
- **Volunteer**: rtk2go ~14 DE bases, Centipede ~3 DE nodes — negligible alongside SAPOS.
- **Gap**: some states report single-coord VRS (0 physical pins); NRTK polygons deferred.
  BY €20/yr surcharge for non-agricultural users is a minor friction point.

### FR — France

- **Free government RTK**: none (commercial only: Teria/Hexagon, Orphéon/Trimble).
- **Volunteer**: Centipede ~719 volunteer bases in mainland France (densest free RTK
  coverage in France); rtk2go ~7 FR bases (negligible alongside Centipede).
- **Gap**: none in practice for mainland France — Centipede effectively provides
  national coverage.

### GB — United Kingdom

- **Free government RTK**: none. OS Net licensed to commercial resellers (SmartNet/Leica,
  TopNET/Trimble) under OS licence model since 2005.
- **Volunteer**: rtk2go ~61 GB bases, Centipede ~43 GB nodes (country code `ENG`).
  Largest volunteer cluster in the British Isles; uneven coverage — densest in
  England, sparse in Wales/Scotland/Northern Ireland.
- **Paid only**: SmartNet, TopNET, etc.

### IE — Ireland

- **Free government RTK**: none. OSi routes users to Trimble VRS Now (commercial).
- **Volunteer**: rtk2go ~12 IE bases, Centipede ~9 IE nodes. Sparse; growing.
- **Gap**: no free coordinated coverage; volunteer quality varies widely.

### LU — Luxembourg

- **Free government RTK**: SPSLux (ACT, `stream.spslux.lu:5005`, VRS) — Luxembourg
  open-data policy, all services free. → networks.md: `spslux`
- **Volunteer**: negligible.

### NL — Netherlands

- **Free government RTK**: none. Market fully privatised since ~2000 (06-GPS/Trimble).
- **Volunteer**: rtk2go ~24 NL bases, Centipede ~25 NL nodes. Together provide real
  but uneven volunteer coverage — functional for many hobbyist use cases.
- **Paid only**: commercial VRS services.

---

## Europe — Southern

### CY — Cyprus

- **Free government RTK**: DLS network is internal use only; not public NTRIP.
- **Note**: rtk2go spoofing exclusion for IL/Lebanon/Jordan/Sinai reaches southern
  Cyprus intermittently (GNSS spoofing from that region affects southern Cyprus).
- **Volunteer**: minimal.

### ES — Spain

- **Free government RTK**: ERGNSS (IGN, `ergnss-ip.ign.es:2101`, ~120 stations, VRS)
  — free, immediate web signup; CC-compatible, attribute IGN. → networks.md: `ergnss`
  RAP (Andalucía) supplements in the south; separate signup.
- **Volunteer**: rtk2go ~8 ES bases, Centipede ~1 ES node.
- **Gap**: good national coverage via ERGNSS.

### GR — Greece

- **Free government RTK**: none. HEPOS €160/3 months or ~€480/yr unlimited;
  URANUS commercial (TopNET Live/Topcon).
- **Volunteer**: rtk2go ~2 GR bases, Centipede ~2 GR nodes.
- **Paid affordable**: HEPOS ~€480/yr ≈ $525 (over $200/yr cutoff; not surfaced).
  Note: HEPOS also offers €160 for 3 months — arguably seasonal affordable.

### HR — Croatia

- **Free government RTK**: CROPOS (DGU, `gnss.cropos.hr:2101`, 35 stations, VRS)
  — free since Apr 2022 (Narodne novine 39/2022). → networks.md: `cropos`
- **Volunteer**: rtk2go ~4 HR bases, Centipede ~5 HR nodes.
- **Gap**: CROPOS VRS only (0 physical pins on map); NRTK polygon deferred.

### IT — Italy

- **Free government RTK**: no national free public caster. Strongly regional.
  - **FReDNet** (OGS/FVG, `gnsscaster.regione.fvg.it:8080`, ~39 stations) — Friuli-Venezia
    Giulia + border SI/AT. Free email registration. In pipeline. → networks.md: `frednet`
  - **SPIN3 GNSS** (CSI Piemonte, `spingnss.it:2101`, ~39 stations) — Piemonte + Lombardia +
    Valle d'Aosta. Free registration. Candidate. → networks.md: `spin3`
  - **GPS-UMBRIA** (Regione Umbria, `gpsumbria.regione.umbria.it:2101`, 12 stations) — Free
    registration. Candidate. → networks.md: `gpsumbria`
  - **Abruzzo + Lazio** (`gnss-rtk.regione.abruzzo.it:2101`, ~29 stations) — Single endpoint
    since Dec 2022. Free registration. Candidate. → networks.md: `gnss_abruzzo_lazio`
  - **SIT Puglia** (`gps.sit.puglia.it:2101`, 12 stations) — Free registration. Candidate.
    → networks.md: `sit_puglia`
  - **Campania** (`gps-sit.regione.campania.it:2101`, ~18 stations) — SPID identity required
    for new users; legacy credentials may work on old endpoint. Conditions access. Candidate.
    → networks.md: `gnss_campania`
  - **TPOS** (Provincia Autonoma di Trento, 11 stations) — Free; endpoint withheld until
    post-registration. Deferred. → networks.md: `tpos`
  - **STPOS** (Provincia Autonoma di Bolzano, 10 stations) — Free; endpoint withheld. Deferred.
    → networks.md: `stpos`
  - **Rete GNSS Veneto** (CISAS-Unipd, ~20 stations) — Free on request; endpoint not public.
    Deferred. → networks.md: `gnss_veneto`
  - **Rete GNSS Liguria** (Regione Liguria, 10 stations) — Free; endpoint not public. Deferred.
    → networks.md: `gnss_liguria`
  - **Sicili@net** (INGV Catania, ~80 stations) — Sicily + S. Calabria; free registration;
    endpoint not public. Deferred. → networks.md: `sicilianet`
  - **Molise** (Regione Molise, ~4 stations) — NTRIP delivery unconfirmed. Deferred.
    → networks.md: `molise_gnss`
  - **Emilia-Romagna** — public service discontinued; now commercial via NetGEO/TopNET.
    Rejected. → networks.md: `gps_emiliaromagna`
  - Regions **not yet confirmed**: Sardinia, Toscana, Basilicata. Calabria partially via
    Sicili@net (INGV Catania).
- **Commercial paid**: NetGEO/TopNET (~€360/yr, national), PegasoNow/Hexagon.
  → networks.md: `netgeo`, `pegasonow`
- **Volunteer**: rtk2go ~12 IT bases, Centipede ~3 IT nodes.
- **Gap**: central Italy (Toscana, Basilicata) has no confirmed free NTRIP. Northern Italy
  well covered by SPIN3 + FReDNet once candidates are ingested. Southern Italy improving
  (Puglia, Campania, Sicily via Sicili@net deferred).

### PT — Portugal

- **Free government RTK**: ReNEP (DGT, 47 stations, VRS + single-base) — free,
  portal signup at renep.dgterritorio.gov.pt; host:port withheld until post-registration.
  → networks.md: `renep` (deferred)
- **Volunteer**: rtk2go ~2 PT bases, Centipede negligible.
- **Gap**: ReNEP requires registration to discover endpoint; blocked for now.

### SI — Slovenia

- **Free government RTK**: none. SIGNAL (GURS) €829.44/yr. → networks.md: `signal`
- **Volunteer**: rtk2go ~4 SI bases, Centipede ~5 SI nodes.

---

## Europe — Northern

### DK — Denmark

- **Free government RTK**: none. GPSnet privatised ~2000; market fully private (Leica/Hexagon).
- **Volunteer**: rtk2go ~16 DK bases, Centipede ~9 DNK + ~9 DAN nodes (both codes
  resolve to Denmark). Together ~34 bases; reasonable coverage in Jutland and major islands.
- **Paid only**: commercial VRS.

### EE — Estonia

- **Free government RTK**: ESTPOS (Maa-amet, `gnss-rtk.maaamet.ee:8083`, 40 stations,
  VRS) — free until 31 Aug 2026 per director-general directive. → networks.md: `estpos`
- **Volunteer**: negligible.
- **Gap**: service expiry Aug 2026; currently timing out in CI (suspected egress firewall).

### FI — Finland

- **Free government RTK**: FINPOS (NLS) RTK granted only for research with written
  justification; 3-month renewable. DGNSS free but sub-metre — out of scope.
- **Volunteer**: rtk2go ~111 FI bases (largest national cluster on rtk2go after USA),
  Centipede ~14 FI nodes. De facto near-national free RTK through volunteer
  infrastructure; uptime not guaranteed.
- **Gap**: no public free government RTK for hobbyists; volunteer coverage is unusually dense.

### IS — Iceland

- **Free government RTK**: IceCORS (LMÍ, `178.19.53.126:2101`, VRS + single-base)
  — confirmed free ("data is free of charge" — natt.is). → networks.md: `icecors`
- **Volunteer**: negligible.

### LT — Lithuania

- **Free government RTK**: LitPOS (GIS-Centras, 35 stations, VRS + DGPS) — free
  status confirmed (publicly-funded EUPOS member); NTRIP host:port not publicly listed.
  → networks.md: `litpos` (deferred)
- **Volunteer**: negligible.
- **Gap**: endpoint not discoverable without registration; contact LitPOS@geoportal.lt.

### LV — Latvia

- **Free government RTK**: LatPos (LGIA, `latpos.lgia.gov.lv:5001`, 27 LV + border
  stations, VRS) — free since 2018. Port 5001. → networks.md: `latpos`
- **Volunteer**: negligible.
- **Gap**: currently timing out in CI (suspected egress firewall on non-standard port).

### NO — Norway

- **Free government RTK**: none. CPOS/ETPOS (Kartverket) NOK 8,000+/yr.
- **Volunteer**: rtk2go ~25 NO bases, Centipede ~21 NO nodes. Together ~46 bases;
  reasonable in populated areas (Oslofjord, Vestlandet); sparse north of ~63°N.
- **Paid only**: CPOS/ETPOS.

### PL — Poland

- **Free government RTK**: ASG-EUPOS (GUGiK, `system.asgeupos.pl:2101`, 130+
  stations, VRS) — free since Oct 2022; admin approval 1–2 working days.
  → networks.md: `asg_eupos`
- **Volunteer**: rtk2go ~51 PL bases (third-largest national cluster on rtk2go).
- **Gap**: ASG-EUPOS is VRS (0 physical pins); NRTK polygon deferred. rtk2go offers
  real physical pins as a complement.

### SE — Sweden

- **Free government RTK**: none for RTK. SWEPOS DGNSS (`dgnss-swepos.lm.se:2101`)
  free with account (free registration); RTCM 2.3; ~0.2 m horizontal — sub-metre, out of scope.
- **Volunteer**: rtk2go ~29 SE bases, Centipede ~1 SE node. Thin relative to
  Sweden's large area; mostly in the south.
- **Paid only**: SWEPOS Network RTK subscription.

---

## Europe — Eastern / Balkans

### AL — Albania / XK — Kosovo / MD — Moldova

- **Free government RTK**: no confirmed public NTRIP endpoint in any of these three.
- **Volunteer**: negligible.

### BA — Bosnia and Herzegovina

- **Free government RTK**: BiHPOS — dual-entity administrative split; paid; limited resources.
  → networks.md: `bihos`
- **Volunteer**: negligible.

### BG — Bulgaria

- **Free government RTK**: no government network; commercial only.
- **Volunteer**: rtk2go ~6 BG bases, Centipede ~1 BG node.

### BY — Belarus

- **Free government RTK**: no public endpoint; state-controlled; international isolation.
- **Volunteer**: negligible.

### CZ — Czech Republic

- **Free government RTK**: CZEPOS — free for education/government; commercial use paid (ČÚZK Decree 31/1995). Not a general hobbyist path.
- **Volunteer**: Centipede ~3 CZ nodes, rtk2go ~4 CZ bases.

### HU — Hungary

- **Free government RTK**: GNSSnet.hu — likely paid; pricing not public.
- **Volunteer**: Centipede ~223 HU nodes (single largest non-France country in
  Centipede sourcetable), rtk2go ~5 HU bases. Near-national free RTK coverage
  through volunteers; densest in the Great Hungarian Plain and northern Hungary.

### ME — Montenegro

- **Free government RTK**: MONTEPOS — paid subscription tiers. → networks.md: `montepos`
- **Volunteer**: negligible.

### MK — North Macedonia

- **Free government RTK**: no confirmed national network name or NTRIP endpoint.
- **Volunteer**: negligible.

### RO — Romania

- **Free government RTK**: ROMPOS — paid credit-based; no open-data GNSS mandate.
- **Volunteer**: Centipede ~7 ROM + ~2 ROU nodes, rtk2go ~6 RO bases. Modest
  coverage concentrated near major cities.
- **Paid affordable**: ROMPOS ~€169/yr ≈ $183 — under $200/yr cutoff; mention in UI.

### RS — Serbia

- **Free government RTK**: AGROS (RGZ) — paid; no English pricing page. → networks.md: `agros`
- **Volunteer**: Centipede ~11 SER + ~3 SRB nodes, rtk2go ~28 RS bases. Together
  ~42 bases — one of the denser volunteer clusters in the Western Balkans.

### RU — Russia

- **Free government RTK**: SDCM — SBAS/L-band satellite only, not NTRIP. No public caster.
- **Volunteer**: negligible.

### SK — Slovakia

- **Free government RTK**: SKPOS — free for public sector/municipalities; commercial use paid. Not a general hobbyist path.
- **Volunteer**: rtk2go ~2 SK bases.

### UA — Ukraine

- **Free government RTK**: ZAKPOS — disrupted since Feb 2022 (Russian invasion). Status unknown;
  deferred until service is confirmed operational post-conflict. → networks.md: `zakpos`
- **Volunteer**: rtk2go ~3 UA bases; status uncertain given the conflict.

---

## Europe — Territories and dependencies

### AX — Åland Islands (FI)

- **Volunteer**: Centipede ~2 AX nodes (country code `ALA`). Small archipelago between Finland and Sweden; partial coverage.

### French overseas territories

Centipede volunteer nodes in several French overseas territories, served via `crtk.net`:

| Territory | Code | Stations | Notes |
|---|---|---|---|
| Réunion (RE) | `REU` | ~4 Centipede | Indian Ocean island; partial coverage |
| Martinique (MQ) | `MTQ` | ~1 Centipede | Lesser Antilles; single base |
| New Caledonia (NC) | `NCL` | ~2 Centipede | Pacific territory; sparse |
| French Polynesia (PF) | `PYF` | ~2 Centipede | Pacific archipelago; sparse |

### GL — Greenland (DK)

- **Volunteer**: rtk2go 1 base near Kangerlussuaq (~67°N). Coverage effectively zero for most of Greenland.

### SJ — Svalbard (NO)

- **Volunteer**: Centipede 1 node (`NYAWIPEV`, ~78.9°N — likely Ny-Ålesund research station). Useful only within ~30–40 km.

---

## Americas — North

### CA — Canada

- **Free government RTK**: none confirmed in any province.
  - NRCan: post-processing only (CACS/CSRS RINEX archive; NRCAN-PPP web tool). No streaming NTRIP.
  - Quebec MERN: per-station direct TCP streams; not NTRIP-aggregated — pipeline-incompatible.
    → networks.md: `qc_mern` (rejected)
  - BC RTN: paid regional service via GeoBC. → networks.md: `bc_rtn`
  - Ontario, Alberta, Saskatchewan, Manitoba: no confirmed free public NTRIP.
- **Volunteer**: rtk2go ~56 CA bases, Centipede ~13 CA nodes. Concentrated heavily
  in BC, Ontario, and southern Quebec; very thin elsewhere.
- **Gap**: no free national or provincial NTRIP in Canada. Volunteer networks are
  the only free path for hobbyists.

### US — United States

- **Free government RTK**: EarthScope NOTA (`ntrip.earthscope.org:2101`, ~1,000+
  stations, single-base, non-commercial NULA) — Americas-wide, dense in western USA.
  → networks.md: `earthscope`

  State DOT/CORS networks with confirmed endpoints (all free registration unless noted):

  | Network    | State | Host:Port                             | Type           | Stations |
  |------------|-------|---------------------------------------|----------------|----------|
  | WISCORS    | WI    | `wiscors.dot.wi.gov:2101`             | physical + VRS | ~180     |
  | FPRN       | FL    | `ntrip.myfloridagps.com:2101`         | physical + VRS | ~120     |
  | ARDOT RTN  | AR    | `gps.ardot.gov:2101`                  | physical + VRS | ~50      |
  | MaCORS     | MA    | `macorsrtk.massdot.state.ma.us:2101`  | physical + VRS | 22       |
  | VECTOR     | VT    | `20.185.11.35:2101` (bare IP)         | physical + VRS | ~15      |
  | AzCORS     | AZ    | `azcors.azwater.gov:2101`             | physical + VRS | 51       |
  | GCGC RTN   | MS    | `rtn.usm.edu:2101`                    | physical + VRS | ~35      |
  | AlCORS     | AL    | `aldotcors.dot.state.al.us:10011`     | physical + VRS | ~50      |
  | KyCORS     | KY    | `kycors.ky.gov:2101`                  | VRS only       | —        |
  | MnCORS     | MN    | `mncors.dot.state.mn.us:9000`         | VRS only       | —        |
  | ORGN       | OR    | `167.131.0.205:9879` (bare IP)        | physical + VRS | ~100     |
  | MSRN       | MI    | `mdotcors.michigan.gov:10700`         | physical + VRS | ~120     |
  | NYSNet     | NY    | `cors.dot.ny.gov:2101`                | physical + VRS | ~150     |
  | InCORS     | IN    | `incors.in.gov:10000`                 | physical + VRS | ~70      |
  | IARTN      | IA    | `iartnsbc.iowadot.gov:2101`           | physical + VRS | 83       |
  | ODOT RTN   | OH    | `156.63.133.115:2101` (bare IP)       | VRS only       | —        |
  | MoDOT RTN  | MO    | `rtk3.modot.mo.gov:2101`              | VRS only       | —        |
  | WVRTN      | WV    | `wvrtn.cors.us:2101`                  | VRS only       | —        |
  | MaineDOT   | ME    | `mdotcors.maine.gov:2101`             | VRS only       | —        |

  Note: MnCORS, ORGN, MSRN, NYSNet, AzCORS have significant EarthScope NOTA overlap —
  expect duplicate physical pins until deduplication is added. VRS-only entries (KyCORS,
  MnCORS, ODOT, MoDOT, WVRTN, MaineDOT) produce no physical pins; shown as VRS stopgap circles.

  MoDOT requires notarized access agreement (conditions access). → networks.md: `modot_rtn`
  ACORN (AK) — endpoint unconfirmed, deferred. → networks.md: `acorn`

  Paid/restricted states: SCRTN (SC, price not listed), NCRTN (NC ~$500/yr), TDOT (TN ~$450/yr),
  TURN GPS (UT ~$600/yr), MTSRN (MT ~$1,500/yr), WSRN (WA ~$1,900/yr), TxDOT (employees-only),
  Caltrans (vetted agency partners only). → networks.md: `scrtn`, `ncrtn`, `tdot_rtn`,
  `turn_gps`, `mtsrn`, `wsrn`, `txrtn`, `calrtns`

  No federal free NTRIP: NOAA/NGS real-time service shut Apr 2013 (budget sequestration).
- **Volunteer**: rtk2go ~142 US bases (largest single-country cluster on rtk2go);
  dense in upper Midwest, Pacific Northwest, mid-Atlantic. Centipede ~3 US nodes.
- **Gap**: Great Plains and interior South have sparse coverage despite state networks.

---

## Americas — Latin

### AR — Argentina

- **Free government RTK**: RAMSAC-NTRIP (IGN, `ntrip.ign.gob.ar:2101`, ~69 stations,
  single-base) — free, 8-hr session cap. → networks.md: `ramsac`
- **Volunteer**: rtk2go ~6 AR bases, mostly Buenos Aires and Córdoba.

### BR — Brazil

- **Free government RTK**: RBMC-IP (IBGE, `gps-ntrip.ibge.gov.br:2101`, 150 stations,
  single-base) — free, gov.br signup, 5-station limit per user. → networks.md: `rbmc_ip`
- **Volunteer**: rtk2go ~17 BR bases, concentrated in São Paulo and southern states.

### CL — Chile

- **Free government RTK**: RGN/SIRGAS-CHILE (IGM) — RINEX downloads only; no streaming caster.
- **Volunteer**: rtk2go ~1 CL base.

### CO — Colombia

- **Free government RTK**: IGAC MAGNA-ECO (IGAC, `sbc.igac.gov.co:2101`, 233 stations,
  VRS) — free, Law 1955/2019 mandates public access. → networks.md: `igac`
- **Volunteer**: negligible.

### CR — Costa Rica / EC — Ecuador / PY — Paraguay

- **Volunteer**: rtk2go ~3 bases each (CRI, ECU, PRY). No known national free NTRIP caster.

### CU — Cuba

- **Free government RTK**: GEOCUBA — 13 stations; no public endpoint; state enterprise; connectivity constraints.

### MX — Mexico

- **Free government RTK**: RGNA (INEGI) — RINEX post-processing only; no streaming NTRIP caster.
- **Volunteer**: rtk2go ~2 MX bases.

### PE — Peru

- **Free government RTK**: REGPMOC (IGN/MoD, `190.12.71.75:2101`) — requires MoD-issued licence (professional/commercial only). Not accessible for hobbyists.

---

## Asia Pacific — Oceania

### AU — Australia

- **Free government RTK**: AUSCORS (Geoscience Australia, `ntrip.data.gnss.ga.gov.au:2101`,
  700+ stations, 5,500+ registered users as of 2024, single-base, CC BY 4.0) — free, web signup.
  → networks.md: `auscors`; State VRS networks (CORSnet-NSW, GPSnet VIC, etc.) are cost-recovery, paid.
- **Volunteer**: rtk2go ~27 AU bases, Centipede ~3 AU nodes. Thin relative to
  Australia's size; supplements AUSCORS in densely populated south-eastern areas.

### NZ — New Zealand

- **Free government RTK**: PositioNZ-RT (LINZ, `positionz-rt.linz.govt.nz:2101`,
  37 CORS stations, single-base, CC BY 4.0 NZ) — free, LINZ account required.
  → networks.md: `positionz`
- **Volunteer**: rtk2go ~11 NZ bases, concentrated in the North Island and upper South Island.

---

## Asia Pacific — East Asia

### CN — China

- **Free government RTK**: none. Qianxun (千寻知寸, Alibaba+Norinco JV) ~¥3,600–3,800/yr.
  Surveying and Mapping Law 2017 restricts CORS; provincial networks for licensed
  surveyors only.
- **Volunteer**: negligible.

### HK — Hong Kong

- **Free government RTK**: SatRef (Lands Dept / SMO, `ntrip.geodetic.gov.hk:2101`,
  19 stations, VRS, 4-constellation, open data) — free, email geodetic@landsd.gov.hk.
  → networks.md: `satref`
- **Volunteer**: negligible (city-state).

### JP — Japan

- **Free government RTK**: GEONET (GSI) — post-processing RINEX only; no public NTRIP.
  MIRAI / Go!GNSS (Cabinet Office SPAC, `ntrip.go.gnss.go.jp:2101`, ~300+ stations,
  free incl. commercial + automated) — raw observations. → networks.md: `mirai`
  QZSS CLAS — satellite-delivered (L6 band), not NTRIP; free, cm-level, no internet. Out of scope.
- **Volunteer**: GeoRTK (Geosense, `geortk.jp:2101`, ~41 stations, no auth, free).
  → networks.md: `geortk`; rtk2go ~24 JP bases.
- **Gap**: well-covered between MIRAI and GeoRTK. Commercial: SoftBank ichimill ¥5–8k/month.

### KR — South Korea

- **Free government RTK**: CORS-KOREA (NGII, `www.gnssdata.or.kr:2101`, ~90–100 stations,
  VRS + FKP) — free; sourcetable public; stream registration may require Korean national ID.
  → networks.md: `cors_korea`
- **Volunteer**: rtk2go ~3 KR bases.
- **Gap**: Korean-language portal only; international hobbyists may be blocked by national ID requirement.

### SG — Singapore

- **Free government RTK**: SiReNT (SLA) SGD $107/month; 3-day trial requires SingPass (residents only).
- **Volunteer**: negligible (city-state).

### TW — Taiwan

- **Free government RTK**: e-GNSS (NLSC/MoI) — pay-per-use + paper form registration. Paid.
- **Volunteer**: rtk2go ~3 TW bases.

---

## Asia Pacific — South & SE Asia

### BD — Bangladesh

- **Free government RTK**: SOB VRS — only 6 stations covering 147,000 km²; baselines
  100–200 km, inadequate for RTK.

### ID — Indonesia

- **Free government RTK**: InaCORS (BIG, `nrtk.big.go.id:2001`, 200+ stations, VRS)
  — free, Law No. 4/2011 mandate. Port 2001. → networks.md: `inacors`
- **Volunteer**: rtk2go ~8 ID bases (Java/Bali).

### IN — India

- **Free government RTK**: SoI-CORS (`cors.surveyofindia.gov.in`, 1,105+ stations)
  — free only for Central/State Government and academic institutions; private users
  ₹5,032/month. Promotional free 3-month window (Nov 2025–Jan 2026) expired.
  Worth revisiting if policy changes.
- **Volunteer**: negligible.

### MY — Malaysia

- **Free government RTK**: MyRTKnet (JUPEM, 78 stations) — paid; Survey Act cost-recovery.
- **Volunteer**: negligible.

### PH — Philippines

- **Free government RTK**: PAGeNet (NAMRIA, 52 stations) — PHP 1,000 one-time + ongoing (EO 471). Paid.
- **Volunteer**: negligible.

### TH — Thailand

- **Free government RTK**: DOL LandGNSS (Dept of Lands) — confirmed free government
  service; NTRIP host:port not yet found; Thai-language manual at
  dol-rtknetwork.com/index.php/npage/manual. → networks.md: `thailand_dol` (deferred)
- **Volunteer**: rtk2go ~2 TH bases.

### VN — Vietnam

- **Free government RTK**: VNGEONET (65 stations) — was free until Aug 2024; fees
  since Sep 2024 per Circular 47/2024/TT-BTC. Paid; out of scope.
- **Volunteer**: negligible.

---

## Middle East & Africa

### AE — UAE

- **Free government RTK**: DVRS (Dubai Municipality, 18+ stations, 4-constellation, VRS)
  — professional application only (dm.gov.ae); no public hobbyist path.
- **Volunteer**: negligible.

### DZ — Algeria

- **Free government RTK**: AL-CORS-Net / REGAT (INCT) — under Ministry of National Defence; security-sensitive. No public caster.
- **Volunteer**: negligible.

### CI — Côte d'Ivoire

- **Volunteer**: Centipede ~2 CI nodes (country code `CIV`). No national NTRIP caster.

### EG — Egypt

- **Free government RTK**: ESA CORS + NACN (~40 stations) — internal use only; Nile Delta + Cairo corridor.
- **Volunteer**: negligible.

### IL — Israel

- **Free government RTK**: APN (Survey of Israel, `mapigps.co.il`) — likely free for
  licensed surveyors. **Rejected from pipeline**: pervasive military GNSS spoofing
  active continuously since Oct 2023 across Israel/Lebanon/Jordan/Sinai/Cyprus (~50,000
  flights affected in 2024). RTK unreliable regardless of NTRIP access.
- **Volunteer**: negligible.

### IQ — Iraq

- **Free government RTK**: IGRS — only 7 stations at 500–800 km spacing; far too wide for RTK. No public caster.
- **Volunteer**: negligible.

### IR — Iran

- **Free government RTK**: IPGN/SHIMIM (NCC) — inward-facing; US/EU sanctions; geospatial data treated as sensitive. No public endpoint.
- **Volunteer**: negligible.

### KE — Kenya

- **Volunteer**: rtk2go ~1 KE base. No known national RTK network with public access.

### MA — Morocco

- **Volunteer**: rtk2go ~1 MA base. No known national RTK network with public access.

### NG — Nigeria

- **Free government RTK**: NIGNET — 11–15 stations at 500–1,000 km spacing; far too wide for RTK. No public caster.
- **Volunteer**: negligible.

### SA — Saudi Arabia

- **Free government RTK**: KSA-CORS (GASGI/GEOSA, `ksacors.geoportal.sa:2101`, 209
  stations, VRS) — free, registration via info@geosa.gov.sa. → networks.md: `ksa_cors`
- **Volunteer**: negligible.
- **Gap**: KSA-CORS VRS (0 physical pins); currently timing out in CI; NRTK polygon deferred.

### SN — Senegal

- **Volunteer**: Centipede ~2 SN nodes. No national NTRIP caster.

### TR — Turkey

- **Free government RTK**: none. TUSAGA-Aktif (TKGM/HGM) — paid membership + annual fee.
- **Volunteer**: rtk2go ~3 TR bases.

### ZA — South Africa

- **Free government RTK**: TrigNet (NGI/DALRRD, `trignet.co.za:2101`, 55+ stations,
  single-base + Network RTK in major clusters) — all products free. → networks.md: `trignet`
- **Volunteer**: rtk2go ~1 ZA base, Centipede ~1 ZA node.
