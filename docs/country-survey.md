# Free RTK NTRIP — country-by-country survey

_How is RTK positioning solved (or not) in each country? Who runs it, is it
free, what are the gaps, and what does a hobbyist or small shop actually get?_

_Technical detail (endpoints, credentials, pipeline status) lives in
`docs/networks.md`. Network references use the pattern `→ networks.md: \`id\``
at the end of the relevant bullet — preserving this exact form lets you audit
coverage with `grep "networks.md:" docs/country-survey.md`._

_Volunteer station counts (rtk2go / Centipede) are drawn from live
`data/stations.json` as of 2026-04-19 and will drift over time._

_Last updated: 2026-04-22._

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

### MT — Malta

- **Free government RTK**: none confirmed. The Malta Environment and Planning
  Authority (MEPA, now MCESD/PA) and the Land Registry do not operate a public
  NTRIP caster. No national CORS network with public NTRIP has been identified
  through Alberding directory or EUREF listings.
- **Volunteer**: rtk2go 1 base — `EneGIS` at Naxxar (35.92°N, 14.44°E), RTCM
  3.2 MSM, carrier L1+L2, country code `MLT`. Single station covering the
  Maltese archipelago; baseline to Gozo ~25 km (marginal RTK range). No
  Centipede nodes detected in Malta bounding box.
- **Gap**: one rtk2go volunteer base is the only free RTK option for the entire
  archipelago (Malta + Gozo + Comino, ~316 km²). Coverage is practical for
  Malta island; Gozo is at the edge of a single-base baseline. No government
  network, no VRS. Nearest government NTRIP is ERGNSS (ES, ~1,700 km) or APOS
  (AT, ~1,400 km) — both useless at that range.
- **Closest paid alternative**: commercial surveying networks in Italy
  (NetGEO/TopNET ~€360/yr) offer no Malta coverage. GEODNET EU node density
  for Malta is unknown; worth checking if a node exists on the island.

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
- **Gap**: endpoint not discoverable without registration; register via geoportal.lt/web/litpos-en.

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

- **Government systems (not NTRIP)**:
  - СДКМ / SDCM (Система Дифференциальной Коррекции и Мониторинга): Russia's SBAS; L-band
    satellite corrections (~20 cm sub-metre); requires SBAS-capable receiver, no internet.
    Out of scope. → networks.md: `sdcm`
  - ФАГС / ВГС (Фундаментальная астрономо-геодезическая сеть / Высокоточная геодезическая
    сеть — Fundamental and High-Accuracy Geodetic Networks): government reference frame
    maintained by Росреестр; research/government use only, no public NTRIP delivery.
- **Free government RTK**: none. No federal authority provides a free public NTRIP stream.
- **Commercial RTK** (all paid; all over the $200/yr cutoff at current ₽/USD rates):
  - **EFT-CORS** (EFT GROUP, `ntrip.eft-cors.ru:2102`): Russia's largest CORS aggregator;
    hundreds of stations growing nationally; GPS+GLONASS+BDS+GAL; ports 2102 (all stations),
    2103 (nearest), 2104 (sCMRx); day/month/annual plans; RINEX post-processing free;
    3-day RTK trial. Updated tariffs from Sep 2025. → networks.md: `eft_cors`
  - **RTKNet** (`ntrip.rtknet.ru`, ports 6030–6041 by federal district): 300+ stations since
    2013; 30,000 ₽/yr annual (~$333/yr), 4,000 ₽/mo; 3-day free trial. → networks.md: `rtknet`
  - **HIVE** (Geosystems Aero, `hive.geosystems.aero`): pay-per-use — daily RTK +
    hourly RINEX; station owners contribute stations and receive revenue share. → networks.md: `hive_cors`
  - **ГЕОСПАЙДЕР** (НПП «ГЕОМАТИК», North-West Russia, `geospider.ru`, 49 stations): regional
    paid network centred on St. Petersburg; monthly/quarterly/annual subscriptions.
    → networks.md: `geospider`
  - **SmartNet** (Hexagon/Leica): international commercial VRS; Russia availability
    uncertain post-2022 sanctions.
- **Post-2022 sanctions**: Western GNSS correction services (Trimble VRS Now, Leica SmartNet)
  suspended or restricted in Russia. Domestic services (EFT-CORS, RTKNet, HIVE) have
  expanded. GNSS receiver imports complicated by component sanctions; parallel-import
  workarounds exist.
- **Volunteer**: negligible. rtk2go ~1 RU-tagged station (a MIRAI overseas station
  miscoded); Centipede negligible. Russian hobbyists typically deploy a local base station
  using SNIP Lite or open-source NTRIP casters.
- **Gap**: no free RTK for hobbyists. Cheapest commercial option for occasional use is an
  EFT-CORS day pass; annual plans (~30,000 ₽/yr, ~$333/yr at current rates) exceed the
  project's $200/yr threshold. Hobbyists needing centimetre accuracy typically set up a
  local base.

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
  - Nova Scotia NSACS: 40-station government CORS; real-time NRTK only via paid
    commercial providers (Can-Net, SmartNet, Brandtnet). → networks.md: `nsacs`
  - Ontario, Alberta, Saskatchewan, Manitoba: no provincial CORS; no confirmed public NTRIP.
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

- **Free government RTK**: REGPMOC (IGN/MoD, `190.12.71.75:2101`) — requires MoD-issued licence (professional/commercial only). Not accessible for hobbyists. → networks.md: `regpmoc`

### UY — Uruguay

- **Free government RTK**: REGNA-ROU (IGM — Instituto Geográfico Militar,
  `rtk.igm.gub.uy:2101`, ~26 stations, single-base + VRS) — confirmed free
  ("El Servicio no tiene costo"); web registration at
  `rtk.igm.gub.uy/SBC/Account/Register`. VRS capable (1–2 cm horizontal
  with dual-frequency equipment). Network expanded Dec 2025 with 8 additional
  multiconstellation CORS; 1,000+ registered users. Reference frame
  SIRGAS-ROU (ITRF-compatible). → networks.md: `regna_rou` (candidate)
- **Volunteer**: rtk2go ~2 bases near the Argentinian border (border-area
  RAMSAC stations); no dedicated UY volunteer streams confirmed. Centipede —
  negligible.
- **Gap**: REGNA-ROU provides free national coverage; main friction is a
  registration step and Spanish-language portal. Candidate for pipeline
  ingestion once sourcetable accessibility is verified.

### VE — Venezuela

- **Free government RTK**: REMOS (IGVSB — Instituto Geográfico de Venezuela
  Simón Bolívar). 29 permanent stations installed nationally, 27 with NTRIP
  capability; Maracaibo (MARA) became the first to transmit corrections via
  NTRIP experimentally from Oct 2008. NTRIP caster endpoint **not publicly
  confirmed**: igvsb.gob.ve lists geodetic services but no public-facing
  host:port or registration portal has been found. The REMOS NTRIP service
  appears to have been limited in practice (only MARA streaming, with plans
  for the remainder — status of those plans is unclear post-2018). IGVSB is
  under the Ministry of Environment; economic and infrastructure constraints
  have historically slowed deployment.
- **Volunteer**: rtk2go — 0 confirmed mainland VE bases (3 rtk2go bases
  visible at coordinates 12°N, 68–69°W are on Curaçao/Aruba — Netherlands
  Antilles, not Venezuelan territory). Negligible Centipede presence.
- **Gap**: no confirmed free public NTRIP caster for mainland Venezuela.
  IGVSB/REMOS infrastructure exists on paper (29 stations, NTRIP-capable)
  but the caster endpoint is not publicly discoverable, and operational
  continuity is uncertain given Venezuela's infrastructure situation.
  GEODNET's South America server (`sa.geodnet.com:2101`, paid $40/month)
  is the nearest practical paid fallback. → networks.md: `remos_ven` (deferred)

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

- **Legal framework**: 测量法 (Surveying and Mapping Law of the PRC, 2002, revised 2017),
  Articles 27–29 require institutional surveying credentials (测绘资质) to operate or access
  CORS networks. All government and provincial CORS are closed to unlicensed individuals.
- **Government networks (licensed professionals only)**:
  - 全国卫星导航定位基准站 (National CORS, Ministry of Natural Resources / NASG): 2,700+
    stations; feeds the 北斗地基增强系统 (BeiDou Ground-Based Augmentation System / BGAS);
    no public NTRIP endpoint. → networks.md: `bgas_china`
  - 省级CORS网 (Provincial CORS — all 34 provinces/municipalities): first established by
    深圳SZCORS (Shenzhen, 2003); every province now has its own network; registration
    requires organisational credentials + surveying licence; some provinces free for
    licensed organisations, others charge (e.g., Sichuan ¥8,000/yr). Not hobbyist-accessible.
- **Commercial RTK** (no professional licence required; open to individuals):
  - **千寻知寸 Qianxun** (Alibaba + Norinco JV, `rtk.ntrip.qxwz.com:8003`): 2,700+
    stations, 33 provinces; ¥3,600–3,800/yr (~$500–528/yr) — over $200/yr cutoff;
    individuals register directly. Most widely used commercial CORS in China.
    → networks.md: `qianxun`
  - **中国移动CORS China Mobile CORS** (CMCC, 4,400+ stations, nationwide): ~¥3,600/yr
    (~$500/yr); NTRIP access via data plan; open to individuals. Same price bracket as
    Qianxun. → networks.md: `cmcc_cors`
  - **腾讯位置服务RTK Tencent RTK** (`cors.tencent.com`): launched 2022 as free beta; moved
    to paid at ~¥998/yr (~$138/yr); 2,800+ virtual network stations; 33 provinces; requires
    Tencent account (WeChat/QQ). If still offered at that price it is the only sub-$200/yr
    option in China, but current status (2025/2026) is unconfirmed. → networks.md: `tencent_rtk`
- **Volunteer**: negligible. rtk2go ~1 CHN-tagged volunteer station; Centipede negligible.
  Chinese hobbyists (drone pilots, precision-agriculture DIY, autonomous-vehicle developers)
  typically pay Qianxun at full price or deploy a local base using SinoGNSS / ComNav /
  Unicore Communications receivers.
- **Gap**: 测量法 closes all government CORS to unlicensed users. The lowest confirmed
  commercial price is Tencent RTK at ~¥998/yr (~$138/yr), but its 2025/2026 operational
  status is unconfirmed and requires a Chinese platform account. Qianxun/CMCC at ~$500/yr
  are the reliable options.

### HK — Hong Kong

- **Free government RTK**: SatRef (Lands Dept / SMO, `ntrip.geodetic.gov.hk:2101`,
  19 stations, VRS, 4-constellation, open data) — free, register via geodetic.gov.hk.
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

### MO — Macao SAR (China)

- **Free government RTK**: none confirmed with a public NTRIP endpoint. The
  Cartography and Cadastre Bureau (DSCC / Direcção dos Serviços de Cartografia
  e Cadastro) operates reference stations but does not publish a public NTRIP
  caster. No Macao entry found in Alberding directory, EUREF listings, or any
  cached sourcetable.
- **Adjacent network — SatRef (HK)**: Hong Kong SatRef
  (`ntrip.geodetic.gov.hk:2101`, free with email registration) has three
  stations within practical range of Macao:
  - `HKCL_32`: 22.30°N, 113.91°E — ~40 km from Macao peninsula
  - `HKNP_32`: 22.25°N, 113.89°E — ~37 km from Macao peninsula
  - `HKSL_32`: 22.37°N, 113.93°E — ~45 km from Macao peninsula

  These baselines (37–45 km) are at the edge of reliable single-base RTK
  (~30–40 km practical limit for cm-level accuracy). VRS mountpoint `VRS32G`
  covers all of Hong Kong and potentially reaches Macao; whether SatRef's
  NRTK VRS engine extends virtual reference points to Macao coordinates is
  not confirmed — depends on server-side polygon extent. → networks.md: `satref`
- **Volunteer**: none. Zero rtk2go or Centipede stations in the Macao bounding
  box (~32 km² peninsula/island cluster).
- **Gap**: no local free RTK. The most practical path is SatRef (HK) VRS —
  free, requires email registration, and the VRS virtual reference is
  compute-generated at the rover's reported position, so it may extend to
  Macao coordinates if the server polygon covers it. Mainland China's Qianxun
  and provincial CORS networks are restricted to licensed surveyors under
  Surveying and Mapping Law 2017 — not a hobbyist path. GEODNET has nodes in
  the Pearl River Delta; the $40/month tier (~$160 for 4-month season) is
  under the $200/yr cutoff.

### SG — Singapore

- **Free government RTK**: SiReNT (SLA) SGD $107/month; 3-day trial requires SingPass (residents only).
- **Volunteer**: negligible (city-state).

### TW — Taiwan

- **Free government RTK**: e-GNSS (NLSC/MoI) — pay-per-use + paper form registration. Paid.
- **Volunteer**: rtk2go ~3 TW bases.

---

## Asia Pacific — South & SE Asia

### AF — Afghanistan

- **Free government RTK**: none. AGCHO (Afghan Geodesy and Cartography Head
  Office) operated two stations decommissioned by 2010–2011. The Taliban
  takeover (August 2021) and subsequent withdrawal of international
  development assistance make further infrastructure development highly
  unlikely. No public NTRIP endpoint has ever been discovered.
- **Volunteer**: none. Zero AF stations on rtk2go or Centipede.
- **Gap**: no RTK infrastructure accessible to hobbyists. Security environment,
  internet infrastructure gaps, and collapse of international geodetic
  cooperation since 2021 make a public NTRIP caster implausible near-term.

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

### MM — Myanmar

- **Free government RTK**: none confirmed for public access. Survey Department
  (`surveydepartment.gov.mm`) has established a CORS network concept with a
  Yangon CORS Data Center, but no public NTRIP host:port, open sourcetable,
  or registration portal has been found. The February 2021 military coup and
  subsequent civil conflict have severely degraded civilian infrastructure and
  internet access; geospatial data is treated as sensitive under military
  governance.
- **Volunteer**: none. Zero MM stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists. Survey Department CORS may exist
  internally but is not publicly accessible. No commercial NTRIP provider
  lists Myanmar coverage.

### MY — Malaysia

- **Free government RTK**: MyRTKnet (JUPEM, 78 stations) — paid; Survey Act cost-recovery.
- **Volunteer**: negligible.

### NP — Nepal

- **Free government RTK**: none confirmed for public/hobbyist access. Survey
  Department (Geodetic Survey Division, `dos.gov.np`) is building a CORS
  network (~4 stations established, mandate to expand to 27–50 at ~70–80 km
  inter-station spacing). No public NTRIP caster or open registration portal
  found; network serves geodetic reference frame maintenance, not real-time
  public streaming. EarthScope NOTA hosts ~11+ research CORS in Nepal (operated
  with Dept of Mines and Geology; research-use orientation, sparse coverage).
- **Volunteer**: none. Zero NP stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists. Survey Department CORS rollout
  is ongoing but endpoint is internal; research stations are sparse and require
  account approval. Nepal's terrain and limited internet outside urban centres
  further constrain practical NTRIP use.

### PH — Philippines

- **Free government RTK**: PAGeNet (NAMRIA, 52 stations) — PHP 1,000 one-time + ongoing (EO 471). Paid.
- **Volunteer**: negligible.

### PK — Pakistan

- **Free government RTK**: none confirmed for hobbyists. SUPARCO (Space and
  Upper Atmosphere Research Commission) operates Pak-Rehber, an NRTK service
  delivering cm-level corrections to "authorized users"; no public-facing
  NTRIP host:port, open registration portal, or sourcetable has been found.
  Access appears to require direct contact with SUPARCO. SUPARCO is also
  deploying Pak-SBAS (L-band SBAS) for sub-metre accuracy — satellite-delivered,
  out of scope. → networks.md: `pak_rehber`
- **Volunteer**: none. Zero PK stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists. Pak-Rehber is restricted to
  authorized users; endpoint and registration path are not publicly documented.
  Pakistan's large area (881,000 km²) and varied terrain mean hobbyists must
  deploy a local base station or contact SUPARCO directly.

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
  — professional application only (dm.gov.ae); no public hobbyist path. → networks.md: `dvrs`
- **Volunteer**: negligible.

### AO — Angola

- **Free government RTK**: none. Instituto Geográfico e Cadastral de
  Angola (IGCA) is rebuilding post-conflict geodetic infrastructure;
  AFREF reference sites exist but are internal/research-only — no
  public NTRIP delivery.
- **Volunteer**: none. Zero AO stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Angola.

### BH — Bahrain

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  The Survey and Land Registration Bureau (SLRB) manages geodetic
  infrastructure (Bahrain Geodetic Datum 2000 / BGD2000) and a small
  number of CORS; access restricted to licensed surveyors.
  Bahrain's entire territory is ~765 km² — a single station would
  theoretically cover it, but no public caster has been identified.
- **Volunteer**: none. Zero BH stations on rtk2go or Centipede.
- **Gap**: no free NTRIP path. KSA-CORS VRS may spill ~50 km into
  Bahrain from nearby Dammam/Al-Ahsa stations, but that service is
  Saudi-licensed. → networks.md: `ksa_cors`

### CD — DR Congo

- **Free government RTK**: none. Institut Géographique du Congo (IGC)
  formally responsible for geodesy; limited AFREF contributions. No
  public CORS caster found; connectivity and power constraints make
  continuous RTK streaming very unlikely near-term.
- **Volunteer**: none. Zero CD stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in DR Congo.

### CI — Côte d'Ivoire

- **Volunteer**: Centipede ~2 CI nodes (country code `CIV`). No national NTRIP caster.

### CM — Cameroon

- **Free government RTK**: none. Institut National de Cartographie (INC)
  manages geodetic infrastructure; no public CORS caster found. AFREF
  contributions are raw archives, not streaming RTK.
- **Volunteer**: none. Zero CM stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Cameroon.

### DZ — Algeria

- **Free government RTK**: AL-CORS-Net / REGAT (INCT) — under Ministry of National Defence; security-sensitive. No public caster.
- **Volunteer**: negligible.

### EG — Egypt

- **Free government RTK**: ESA CORS + NACN (~40 stations) — internal use only; Nile Delta + Cairo corridor.
- **Volunteer**: negligible.

### ET — Ethiopia

- **Free government RTK**: nascent. ETCORS (SSGI, `ssgi.gov.et`) — ~10 stations
  launched December 2025 in Addis Ababa and six regional cities; aims for 30
  stations within 2 years, 200 for national coverage. Intended as free public
  service ("for Ethiopia and neighboring countries") but NTRIP host:port not
  yet publicly discoverable. Deferred.
- **Volunteer**: none. Zero ET stations on rtk2go or Centipede.
- **Gap**: no confirmed public NTRIP for hobbyists as of April 2026. Even once
  the endpoint is published, only ~10 stations serve Ethiopia's 1.1 million km²;
  coverage will be extremely sparse outside the capital and the handful of
  instrumented cities for the foreseeable future.

### GH — Ghana

- **Free government RTK**: none. Survey and Mapping Division (Lands
  Commission) and GSSTI operate a handful of IGS/AFREF reference sites
  (Accra); raw-observation archives only — no NTRIP streaming.
- **Volunteer**: none. Zero GH stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Ghana.

### IL — Israel

- **Free government RTK**: APN (Survey of Israel, `mapigps.co.il`) — likely free for
  licensed surveyors. **Rejected from pipeline**: pervasive military GNSS spoofing
  active continuously since Oct 2023 across Israel/Lebanon/Jordan/Sinai/Cyprus (~50,000
  flights affected in 2024). RTK unreliable regardless of NTRIP access. → networks.md: `apn`
- **Volunteer**: negligible.

### IQ — Iraq

- **Free government RTK**: IGRS — only 7 stations at 500–800 km spacing; far too wide for RTK. No public caster. → networks.md: `igrs`
- **Volunteer**: negligible.

### IR — Iran

- **Free government RTK**: IPGN/SHIMIM (NCC) — inward-facing; US/EU sanctions; geospatial data treated as sensitive. No public endpoint.
- **Volunteer**: negligible.

### KE — Kenya

- **Volunteer**: rtk2go ~1 KE base. No known national RTK network with public access.

### KW — Kuwait

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  PACI and Kuwait Municipality operate GNSS reference stations for
  cadastral/infrastructure use (Kuwait Geodetic Network / KGN); streams
  issued only to licensed surveying firms under municipal contract —
  no public caster host:port identified.
- **Volunteer**: none. Zero KW stations on rtk2go or Centipede.
- **Gap**: no free NTRIP path. Kuwait is small (~17,800 km²) and flat;
  a modest CORS network would suffice for national RTK if opened, but
  no open-access mandate exists.

### MA — Morocco

- **Volunteer**: rtk2go ~1 MA base. No known national RTK network with public access.

### MZ — Mozambique

- **Free government RTK**: none. CENACARTA (national mapping authority) has CORS
  stations in the AFREF/Corsmap continental dataset but no public NTRIP caster
  or RTK streaming endpoint found.
- **Volunteer**: none. Zero MZ stations on rtk2go or Centipede. Four TrigNet ZA
  stations near the Limpopo border (Nspt, Pbwa, Sprt, Tdou) are in pipeline via
  TrigNet and provide incidental single-base RTK coverage in southern Mozambique
  (Gaza/Maputo provinces) — not a Mozambique service.
- **Gap**: no free RTK for hobbyists within Mozambique proper. Southernmost
  provinces may benefit from nearby TrigNet coverage.

### NE — Niger

- **Free government RTK**: none. Institut Géographique National du
  Niger (IGNN) is responsible for geodesy; sparse IGS-affiliated
  research stations only — no public NTRIP delivery. Saharan geography
  and infrastructure constraints make a sustained physical RTK network
  very difficult.
- **Volunteer**: none. Zero NE stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Niger.

### NG — Nigeria

- **Free government RTK**: NIGNET — 11–15 stations at 500–1,000 km spacing; far too wide for RTK. No public caster.
- **Volunteer**: negligible.

### OM — Oman

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  National Accurate Geodetic Survey Network (NAGSN), supporting ONGD14
  and geoid model OmG2016, is operationally managed by the National Survey
  Authority; streams issued to licensed surveying companies via formal
  application — no public caster URL identified for hobbyists. IGS station
  at Muscat (MUSK) broadcasts raw observations via EarthScope/IGS-IP, not
  RTK streams.
- **Volunteer**: none. Zero OM stations on rtk2go or Centipede.
- **Gap**: no free NTRIP path. Oman's ~309,500 km² and mountainous terrain
  (Al Hajar range) mean useful national coverage requires ~20–30 stations;
  NAGSN appears to exist at that scale but remains closed to public access.

### QA — Qatar

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  Ministry of Municipality manages CORS tied to the Qatar National Spatial
  Reference System (QNSRS / QND95); internal use by licensed surveyors and
  government contractors only — no public caster URL identified.
- **Volunteer**: none. Zero QA stations on rtk2go or Centipede.
- **Gap**: no free NTRIP path for hobbyists. Qatar is small (~11,600 km²);
  a single Doha reference station would theoretically cover the territory,
  but no such public stream exists.

### SA — Saudi Arabia

- **Free government RTK**: KSA-CORS (GASGI/GEOSA, `ksacors.geoportal.sa:2101`, 209
  stations, VRS) — free, register via ksacors.geoportal.sa. → networks.md: `ksa_cors`
- **Volunteer**: negligible.
- **Gap**: KSA-CORS VRS (0 physical pins); currently timing out in CI; NRTK polygon deferred.

### SD — Sudan

- **Free government RTK**: none. Sudan Survey Authority (SSA) planned a GNSS CORS
  network as part of AFREF participation (55 station sites identified) but no
  operational public caster has been found. Ongoing armed conflict (April 2023–)
  severely disrupts civil infrastructure; status unknown.
- **Volunteer**: none. Zero SD stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. Do not pursue until conflict ends and
  infrastructure is confirmed operational.

### SN — Senegal

- **Volunteer**: Centipede ~2 SN nodes. No national NTRIP caster.

### TR — Turkey

- **Free government RTK**: none. TUSAGA-Aktif (TKGM/HGM) — paid membership + annual fee.
- **Volunteer**: rtk2go ~3 TR bases.

### TZ — Tanzania

- **Free government RTK**: none. Survey and Mapping Division / TNGC
  (`tngc.lands.go.tz`) operate national geodetic control; no public NTRIP caster
  found. AFREF/IGS contributions are raw-observation archives, not RTK streaming.
- **Volunteer**: none. Zero TZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists anywhere in Tanzania.

### UG — Uganda

- **Free government RTK**: UGRF CORS (Ministry of Lands, Housing & Urban
  Development, `ugrf.mlhud.go.ug`, 40 government + 38 private stations, VRS +
  single-base) — stated free as of 2024 ("absolutely free of charge"); web
  registration via Spider Business Center (`ugrf.go.ug/SBC`); host:port
  disclosed post-registration. Single-base mountpoints: ENTB, GULU, SRTI, MBRA.
  Deferred (endpoint withheld until post-registration).
- **Volunteer**: 1 AUSCORS station (MBAR00UGA0, Mbarara) via EarthScope/AUSCORS;
  raw observations under non-commercial NULA — functional for RTK within range.
- **Gap**: UGRF is the only confirmed free government NTRIP in East Africa but
  is not yet in pipeline (endpoint not publicly findable). EagleCORS
  (`eaglecors.com`) is a separate commercial service — out of scope.

### YE — Yemen

- **Free government RTK**: none. General Survey Authority (GAS) operated a small
  CORS network pre-conflict; civil war since 2015 has severely disrupted all
  public infrastructure. No functioning public NTRIP caster is known.
- **Volunteer**: rtk2go 1 base — `s9123A22404` at Sanaa (15.29°N, 44.24°E),
  RTCM 3.2, GPS + BDS dual-frequency. Single independent hobbyist installation;
  connectivity and uptime unreliable given ongoing conflict.
- **Gap**: effectively no RTK coverage for hobbyists. The single rtk2go station
  provides a ~50–70 km useful radius under good conditions but cannot be relied
  upon. Note for map completeness only; recommending RTK activity in Yemen is
  not appropriate given the conflict context.

### ZA — South Africa

- **Free government RTK**: TrigNet (NGI/DALRRD, `trignet.co.za:2101`, 55+ stations,
  single-base + Network RTK in major clusters) — all products free. → networks.md: `trignet`
- **Volunteer**: rtk2go ~1 ZA base, Centipede ~1 ZA node.

---

## Central Asia

### KZ — Kazakhstan

- **Free government RTK**: none confirmed publicly accessible.
  KazGeoDesy (Committee on Land Management) operates a CORS network of 120+
  stations; access requires an institutional licence or commercial reseller
  contract — no open self-service path found. → networks.md: `kazgeodesy`
- **Volunteer**: negligible. Zero KZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. Country is ~2.7 million km² with
  most stations concentrated around Almaty, Astana, and the northern corridor;
  even a public caster would yield long baselines outside urban centres.

### UZ — Uzbekistan

- **Free government RTK**: none confirmed publicly accessible.
  UzGeodezKadastr operates national CORS stations (referenced in GNSS/seismic
  literature); no public NTRIP endpoint found. Access restricted to licensed
  surveyors and state agencies.
- **Volunteer**: negligible. Zero UZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. Coverage demand concentrated in
  Tashkent and the Fergana Valley; no open-data geodesy policy identified.
