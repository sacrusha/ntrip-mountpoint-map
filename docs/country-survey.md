<!-- Process / rules: country-survey.proc.md (pipeline: pipeline.md) -->
# Free RTK NTRIP — country-by-country survey

_How is RTK positioning solved (or not) in each country? Who runs it, is it
free, what are the gaps, and what does a hobbyist or small shop actually get?_

## Role of this file

This survey is the **completeness picture**: the place to see which
countries have been investigated, what was found, and where the gaps still
are. Its purpose is to make under-coverage visible — a missing heading is
itself a signal — and to capture the per-country reasoning that drives
everything downstream.

It is **not** a refined catalogue of operators (that is `docs/networks.md`,
which curates the surveyed findings into per-network blocks for our use), and
it is **not** end-user copy (that is `data/country_markers.json`, which
translates the conclusions into short user-facing notes for the map). The
three files don't have to mirror each other; each has a distinct role and
audience. Think of the flow as: survey → networks → markers, with each step
narrowing and re-styling for its audience.

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

**date_added**: 2026-05-06

- **Paid government RTK**: APOS (BEV, `aposrtk.bev.gv.at:2101`, 37 stations, VRS) —
  paid for hobbyists via bev.gv.at portal. No annual plan; billing is per-second,
  per-day, or per-month. RTK (centimetre accuracy): €200/month or €20/day (~$220/mo
  or ~$22/day). DGPS (decimetre accuracy): €20/month or €2/day. One-time setup fee
  €50. Free only for agriculture/forestry users with Austrian farm credentials (eAMA).
  → networks.md: `apos`
- **Volunteer**: rtk2go ~13 AT bases, Centipede ~1 AT node.
- **Gap**: no free hobbyist RTK; the only unconditionally free option is volunteer
  stations on rtk2go. Agricultural users get APOS free via eAMA.

### BE — Belgium

**date_added**: 2026-05-06

- **Free government RTK**:
  - FLEPOS (Flanders, `flepos.vlaanderen.be:2101`, 45 stations VRS) — free for
    all uses; currently timing out in CI. → networks.md: `flepos`
  - WALCORS (Wallonia, `gnss.wallonie.be:8081`, 23 stations VRS) — free for
    positioning; paid for machine-control/auto-guidance. Port 8081 confirmed
    2026-05-06 (port 2101 firewall-blocked). → networks.md: `walcors`
  - GPSBru/AGN (Brussels NGI, `agn.ngi.be`, 1 station) — free, registration;
    useful only within ~30 km of Brussels. Low priority. → networks.md: `gpsbru`
- **Volunteer**: rtk2go ~3 BE bases, ~21 NL bases (mixed geography); Centipede ~17 BE nodes, ~26 NL nodes.
- **Gap**: FLEPOS and WALCORS are VRS-only (0 physical pins on map); NRTK polygons deferred.

### CH — Switzerland

**date_added**: 2026-04-29

- **Free government RTK**: none. swipos (swisstopo) CHF 1,500/yr;
  *Geoinformationsgesetz* SR 510.62 classifies RTK as a value-added service.
  → networks.md: `swipos`
- **Volunteer**: rtk2go ~20 CH bases, Centipede ~27 CH nodes (country code `CHZ`).
  Concentrated on the Swiss plateau and Jura; partial free coverage for hobbyists
  willing to accept volunteer uptime.
- **Paid only**: swipos ~CHF 1,500/yr ≈ $1,650 — expensive for a hobbyist.
- **Gap**: no free coordinated RTK; volunteer bases on the Swiss plateau give
  partial hobbyist coverage but with no uptime guarantee.

### LI — Liechtenstein

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Amt für Tiefbau und Geoinformation
  (ATG, llv.li) manages national geodata infrastructure but operates no public NTRIP
  caster. Liechtenstein has no independent GPS reference station programme (CORS); private surveyors use swipos
  (swisstopo, CHF 1,500/yr), which geometrically covers the entire principality via
  Swiss AGNES stations 5–10 km away. → networks.md: `li_cors`
- **Volunteer**: none. Zero LI stations on rtk2go or Centipede (bounding-box check
  confirmed). Swiss volunteer bases near St. Gallen/Rhine valley may provide incidental
  coverage.
- **Paid only**: swipos ~CHF 1,500/yr ≈ $1,650 — expensive for a hobbyist; only practical RTK
  service for the territory.

### DE — Germany

**date_added**: 2026-04-28

- **Free government RTK**: SAPOS (16 Bundesländer, ~270 stations, VRS). Most
  states free. Bayern €20/yr flat rate for non-agricultural use. Sachsen endpoint
  recently confirmed. All require per-state web registration. → networks.md: `sapos_*`
  SAPOS GEPOS (BKG federal) broadcasts SSR/PPP-RTK in SSRZ format — not standard
  RTCM; requires SSR-capable receiver. Out of scope.
- **Volunteer**: rtk2go ~14 DE bases, Centipede ~3 DE nodes — negligible alongside SAPOS.
- **Gap**: some states report single-coord VRS (0 physical pins); NRTK polygons deferred.
  BY €20/yr surcharge for non-agricultural users is a minor friction point.

### FR — France

**date_added**: 2026-04-28

- **Free government RTK**: none (commercial only: Teria/Hexagon, Orphéon/Trimble).
- **Volunteer**: Centipede ~719 volunteer bases in mainland France (densest free RTK
  coverage in France); rtk2go ~7 FR bases (negligible alongside Centipede).
- **Gap**: none in practice for mainland France — Centipede effectively provides
  national coverage.

### GB — United Kingdom

**date_added**: 2026-04-29

- **Free government RTK**: none. OS Net (Ordnance Survey, ~110 stations) is
  licensed exclusively to commercial resellers (HxGN SmartNet/Hexagon,
  TopNET/Trimble, AXIO-NET, SoilEssentials, Premium Positioning, Point One,
  Topcon) under the OS licence model since 2005; no public NTRIP endpoint.
  → networks.md: `os_net`
- **Volunteer**: rtk2go ~61 GB bases, Centipede ~43 GB nodes (country code `ENG`).
  Largest volunteer cluster in the British Isles; uneven coverage — densest in
  England, sparse in Wales/Scotland/Northern Ireland.
- **Paid (annual)**: confirmed published tariffs (2026-04-30, ex 20% UK VAT):
  Leica HxGN SmartNet via SCCS Survey £2,160/yr unlimited NRTK (£1,300/yr
  for 480 hrs limited); Topcon TopNet Live via Drone Pilot Academy £1,700/yr
  unlimited; Trimble VRS Now via Korec is "Price On Application".
- **Paid (shortest blocks)**: Topcon TopNet Live publishes short paid blocks —
  £100 for 7 days unlimited (~$133), £300 for 30 days unlimited (~$399), and
  hour-bucket annual passes from £100/5 hrs to £250/11 hrs. These cover one-off
  project sessions but they are not cheap on a recurring basis (£100/wk = ~£5,200
  if used every week of the year; £100/5 hrs = £20/hr).
- **Gap**: no free coordinated coverage and no inexpensive recurring OS Net
  subscription; volunteer bases are the only free option and coverage thins
  sharply outside English population centres.

### IE — Ireland

**date_added**: 2026-04-29

- **Free government RTK**: none. OSi (now Tailte Éireann) operates a ~24-station
  active GNSS network but provides only free RINEX post-processing — no
  real-time NTRIP caster. Portal migrating from `gnss.osi.ie` to
  `gnss.tailte.ie` in May 2026. → networks.md: `osi_gnss`
- **Paid real-time**: closest published Irish tariff (2026-04-30) is Trimble
  VRS Now via Hitechniques (`hitechniques.ie`) at €590/yr (~$640) for 600
  hours of usage covering Ireland; HxGN SmartNet has IE coverage via UK
  partners (see GB entry).
- **Volunteer**: rtk2go ~12 IE bases, Centipede ~9 IE nodes. Sparse; growing.
- **Gap**: no free coordinated coverage and no short-term commercial pass at
  Topcon TopNet Live's price point — IE real-time RTK requires either a €590
  annual commitment or volunteer base coverage of variable quality.

### LU — Luxembourg

**date_added**: 2026-04-29

- **Free government RTK**: SPSLux (ACT, `stream.spslux.lu:5005`, VRS) — Luxembourg
  open-data policy, all services free. → networks.md: `spslux`
- **Volunteer**: negligible.

### NL — Netherlands

**date_added**: 2026-05-01

- **Free government RTK**: AGRS.NL — NSGI / Kadaster Nederland (`ntrip.kadaster.nl:2101`
  plain TCP, `ntrip.kadaster.nl:443` TLS) — free, anonymous. ~30 mainland stations,
  RTCM 3.2 MSM. Same caster hosts BES island stations (catalogued under BQ). Legal
  basis: Kadasterwet BWBR0037196 art. 19 lid 4. TU Delft mirror: `gnss1.tudelft.nl:2101`
  (station subset, no TLS). → networks.md: `agrs_nl`
- **Paid per-station raw streams**: NETPOS — same ~30 physical stations as AGRS.NL but
  authenticated paid feed at `ntrip.cloud.kadaster.nl:443` (TLS, B;Y auth). Priced per
  station per year (2026, excl. BTW): €475 (1–5 stations), €380 (6–10), €285 (11–15),
  €190 (16–20), €95 (21+). Not VRS — delivers single-base raw observations for users
  computing their own corrections. NL legal entities via eHerkenning portal; foreign
  users via contact form. → networks.md: `netpos`
- **Commercial** (paid, expensive for a hobbyist): 06-GPS (Trimble NL, VRS, ~250
  stations) — €1,500/yr excl. VAT (~€1,815 incl., ~$2,000/yr); not surfaced.
  → networks.md: `06gps`
- **Volunteer**: rtk2go ~24 NL bases, Centipede ~25 NL nodes. Together provide real
  but uneven coverage — functional for many hobbyist use cases.
- **Gap**: AGRS.NL free tier not yet in the pipeline — hobbyists currently rely on
  volunteer infrastructure; ingesting AGRS.NL would substantially improve official-frame
  coverage.

---

## Europe — Southern

### CY — Cyprus

**date_added**: 2026-04-29

- **Government RTK (paid)**: CYPOS (Department of Lands and Surveys / DLS, Ministry
  of Interior, 7 stations, VRS + iMAX + FKP + MAC) — paid subscription; register
  via the DLS Portal (`portal.dls.moi.gov.cy`); host:port and tariff disclosed
  only post-registration (rechecked 2026-04-30, no public figures). → networks.md: `cypos`
- **Free single-base via AUSCORS**: Geoscience Australia's AUSCORS broadcaster
  (`ntrip.data.gnss.ga.gov.au:2101`) carries the IGS NICO station (Nicosia,
  35.14°N 33.40°E, RTCM 3.2, GPS+GLO dual-freq) — free, no registration. Single
  base, ITRF2020 current epoch, ~30 km useful L1+L2 baseline, so practical
  coverage is greater Nicosia and central Cyprus. ITRF→WGS84 is essentially
  identity for cm-level work; a Cyprus LTM grid transformation is only needed
  for ties into legacy cadastral data. Already visible on this map under
  `auscors`. → networks.md: `auscors`
- **Note**: GNSS spoofing originating from the IL/Lebanon/Sinai region intermittently
  affects southern Cyprus — rovers may lose fix near the coast facing east.
- **Volunteer**: rtk2go ~1 CY base, Centipede ~0 CY nodes. Minimal coverage.
- **Gap**: no Cyprus-government free NTRIP; AUSCORS NICO is the only free
  national-frame option but covers only the Nicosia area. CYPOS is the only
  paid option for island-wide network RTK.

### AD — Andorra

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. ERGAND (Govern d'Andorra geodetic agency)
  operates 2 EPN reference stations (PCAR at Pic de Carroi, RULL) and provides
  post-processing services and a national geoid model, but no public NTRIP caster has
  been identified. → networks.md: `ergand`
- **Volunteer**: none. Zero AD stations on rtk2go or Centipede (bounding-box check
  confirmed). ERGNSS (ES) and Centipede (FR) border stations are the practical
  free-correction option for work near the Spanish or French frontiers.

### ES — Spain

**date_added**: 2026-04-28

- **Free government RTK**: ERGNSS (IGN, `ergnss-ip.ign.es:2101`, ~120 stations, VRS)
  — free, immediate web signup; CC-compatible, attribute IGN. → networks.md: `ergnss`
  RAP (Andalucía) supplements in the south; separate signup.
  Canary Islands use a separate ERGNSS sub-service (SPTR) — see ES-Canarias below.
- **Volunteer**: rtk2go ~8 ES bases, Centipede ~1 ES node.
- **Gap**: good national coverage via ERGNSS; Canary Islands best served by SPTR
  (`ergnss-tr.ign.es:2101`), not the mainland endpoint.

### ES-Canarias — Canary Islands (ES)

**date_added**: 2026-05-06

- **Free government RTK**: IGN España SPTR (`ergnss-tr.ign.es:2101` network solutions,
  `:2102` single-station) — same IGN free registration and CC licence as mainland
  ERGNSS; ~15–16 stations across all seven islands. Recommended mountpoint:
  `CERCANA3M` (auto-routes to nearest station, RTCM 3.2 MSM4, automatic failover).
  VRS network-RTK less reliable over archipelago geometry — nearest-station mode is
  the IGN-recommended approach. → networks.md: `ergnss`
- **Regional paid**: GRAFCAN REPCAN (`195.53.241.146:2101`, also `gnss.grafcan.es`)
  — Cartografía de Canarias S.A.; 20 stations; annual fee per device, price not
  publicly listed (purchase via tiendavirtual.grafcan.es). Free for public
  administrations with active SITCAN contract; IGIC (7%) applies. Recommended
  mountpoint: `CERCANA3M` or `GRAF3M`. Free RINEX archive at `gnss.grafcan.es`
  (no account required). → networks.md: `grafcan_repcan`
- **Volunteer**: none. Zero Canary Islands stations on rtk2go or Centipede.
- **Gap**: IGN SPTR is the free recommended option; GRAFCAN REPCAN is the paid
  regional alternative with broader station redundancy. Neither HxGN SmartNet nor
  Centipede has confirmed Canary Islands coverage.

### GR — Greece

**date_added**: 2026-04-29

- **Free government RTK**: none. HEPOS (HEPOS S.A. / Ktimatologio, `uranus.gr:2101`,
  VRS) — flat-rate plans €160/quarter (~$170) or €480/yr (~$525), unlimited; per-minute
  plan also available (€90 one-time registration + undisclosed per-minute charge); all
  prices ex-VAT. Quarterly flat rate affordable for seasonal hobbyist use.
  → networks.md: `hepos`
- **Volunteer**: rtk2go ~2 GR bases, Centipede ~2 GR nodes.
- **Paid affordable**: HEPOS — €160/quarter (~$170) or €480/yr (~$525) unlimited flat
  rate; pay-per-minute option also available (€90 registration, per-minute rate not
  published); quarterly flat rate affordable for seasonal hobbyist use.
- **Gap**: no free government RTK; HEPOS quarterly block is the lowest-cost
  entry; volunteer coverage very thin.

### HR — Croatia

**date_added**: 2026-04-28

- **Free government RTK**: CROPOS (DGU, `gnss.cropos.hr:2101`, 35 stations, VRS)
  — free since Apr 2022 (Narodne novine 39/2022). → networks.md: `cropos`
- **Volunteer**: rtk2go ~4 HR bases, Centipede ~5 HR nodes.
- **Gap**: CROPOS VRS only (0 physical pins on map); NRTK polygon deferred.

### MT — Malta

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed. The Malta Environment and Planning
  Authority (MEPA, now MCESD/PA) and the Land Registry do not operate a public
  NTRIP caster. No national fixed reference station network (CORS) with public NTRIP has been identified
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
  (NetGEO/TopNET ~€360/yr) do not cover Malta. GEODNET has no confirmed node
  on Malta or Gozo (no hexagon visible on coverage map as of 2026-05-06).

### IT — Italy

**date_added**: 2026-04-30

- **Free government RTK**: no national free public caster. Strongly regional.
  - **FReDNet** (OGS/FVG, `gnsscaster.regione.fvg.it:8080`, ~39 stations) — Friuli-Venezia
    Giulia + border SI/AT. Free email registration. In pipeline. → networks.md: `frednet`
  - **SPIN3 GNSS** (CSI Piemonte, `spingnss.it:2101`, ~39 stations) — Piemonte + Lombardia +
    Valle d'Aosta. Free registration. In pipeline. → networks.md: `spin3`
  - **GPS-UMBRIA** (Regione Umbria, `gpsumbria.regione.umbria.it:2101`, 12 stations) — Free
    registration. In pipeline. → networks.md: `gpsumbria`
  - **Abruzzo + Lazio** (`gnss-rtk.regione.abruzzo.it:2101`, ~29 stations) — Single endpoint
    since Dec 2022. Free registration. In pipeline. → networks.md: `gnss_abruzzo_lazio`
  - **SIT Puglia** (`gps.sit.puglia.it:2101`, 12 stations) — Free registration. In pipeline.
    → networks.md: `sit_puglia`
  - **Campania** (`gps-sit.regione.campania.it:2101`, ~18 stations) — SPID identity required
    for new users; legacy credentials may work on old endpoint. Conditions access. In pipeline.
    → networks.md: `gnss_campania`
  - **TPOS** (Provincia Autonoma di Trento, `tpos.provincia.tn.it:2101`, 11 stations) — Free;
    self-service SBC portal; no professional licence required; VRS/MAX/NRT mountpoints + RINEX
    archive. In pipeline. → networks.md: `tpos`
  - **STPOS** (Provincia Autonoma di Bolzano, `www.stpos.it:2101`, 10 stations) — Free; SBC
    portal; ID scan + intended-use declaration required to activate RTK (RINEX immediate); no
    professional restriction. In pipeline. → networks.md: `stpos`
  - **Rete GNSS Veneto** (CISAS-Unipd, `147.162.229.53:2101`, ~20 stations) — Free; email
    registration; MAX3/IMAX/NRT mountpoints; open to any user. In pipeline. → networks.md: `gnss_veneto`
  - **Rete GNSS Liguria** (Regione Liguria, `81.23.86.70:2101`, 10 stations) — Free; online
    registration; open to all; 7 regional + 3 SPIN3 stations. In pipeline. → networks.md: `gnss_liguria`
  - **Sicili@net** (INGV Catania, `193.206.223.39:2101`, ~80 stations) — Sicily + S. Calabria;
    free to all; email registration; MAX/IMAX/VRS/FKP mountpoints. In pipeline. → networks.md: `sicilianet`
  - **Emilia-Romagna** — public service discontinued; now commercial via NetGEO/TopNET.
    Rejected. → networks.md: `gps_emiliaromagna`
  - **Molise** — Regione Molise does not operate a GNSS network. Rejected. → networks.md: `molise_gnss`
  - Regions **not yet confirmed**: Toscana, Basilicata. Calabria partially via Sicili@net.
- **Commercial paid**: NetGEO/TopNET (~€360/yr, national), PegasoNow/Hexagon.
  SARNET (Sardinia, ~14 stations, ~€250/yr ex-IVA (~$293/yr); only correction source on
  the island; no rtk2go or Centipede stations in Sardinia).
  → networks.md: `netgeo`, `pegasonow`, `sarnet`
- **Volunteer**: rtk2go ~12 IT bases, Centipede ~3 IT nodes.
- **Gap**: central Italy (Toscana, Basilicata) has no confirmed free NTRIP. Five previously
  deferred networks (TPOS, STPOS, Veneto, Liguria, Sicili@net) now have confirmed caster
  addresses and are candidates for pipeline ingestion.

### SM — San Marino

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Ufficio Tecnico del Catasto e Cartografia
  (gov.sm) maintains a single permanent GNSS reference station (RSMC) and distributes
  post-processing data but operates no public NTRIP caster. San Marino is fully enclosed
  by Italy; Emilia-Romagna's public network was discontinued (now commercial), and the
  adjacent Marche region has no confirmed public caster. → networks.md: `sm_cors`
- **Volunteer**: none. Zero SM stations on rtk2go or Centipede (bounding-box check
  confirmed).
- **Paid only**: NetGEO/TopNET (~€360/yr ≈ $390, national Italy) covers San Marino
  as part of its Italian footprint; expensive for a hobbyist (~$390/yr). → networks.md: `netgeo`

### PT — Portugal

**date_added**: 2026-04-29

- **Free government RTK**: ReNEP (DGT, 47 stations, VRS + single-base) — free,
  portal signup at renep.dgterritorio.gov.pt; caster at 193.137.94.71, port 2101
  (physical RTCM3), port 2102 (MSM5), port 2106 (nearest-station VRS), port 2108
  (network corrections). → networks.md: `renep` (in pipeline as of 2026-04-30)
- **Volunteer**: rtk2go ~2 PT bases, Centipede negligible.

### SI — Slovenia

**date_added**: 2026-04-29

- **Free government RTK**: none. SIGNAL (GURS — Surveying and Mapping Authority,
  `gu-signal.si`, 16 stations, VRS) — €829.44/yr (~$905); early-discount €622.08/yr
  (~$680). → networks.md: `signal`
- **Volunteer**: rtk2go ~4 SI bases, Centipede ~5 SI nodes.
- **Gap**: no free government NTRIP; volunteer bases provide ad-hoc coverage; SIGNAL
  is the only nationwide option but at a professional subscription price.

---

## Europe — Northern

### DK — Denmark

**date_added**: 2026-04-29

- **Free government RTK**: none. GPSnet was privatised ~2000; the successor commercial
  network is operated under Leica/Hexagon. SDFi (Styrelsen for Dataforsyning og Infrastruktur)
  holds geodetic authority but offers no public NTRIP service.
- **Volunteer**: rtk2go ~17 DNK bases, Centipede ~8 DNK nodes. Together ~25 bases;
  reasonable coverage in Jutland and major islands.
- **Paid only**: commercial VRS (Leica/Hexagon).
- **Gap**: no free government RTK; volunteer rtk2go/Centipede bases are the practical
  free option, with gaps in Bornholm and remote island areas.

### FO — Faroe Islands (DK)

**date_added**: 2026-05-01

- **Government RTK (restricted, no public endpoint)**: Umhvørvisstovan — the Faroese
  Environment Agency (`us.fo`, formerly `umhvorvisstovan.fo`) operates 4 permanent GNSS
  reference stations (Klaksvík, Vestmanna, Trongisvágur, Argir) and explicitly advertises
  centimetre-level RTK access for surveying firms and construction companies
  (`us.fo/kort/geodesi`, confirmed 2026-05-01). No caster hostname, port, sourcetable URL,
  or tariff is published; access requires contacting the agency directly. Hobbyist
  eligibility unclear — page language implies professional/commercial clients. Danish
  GPSnet does not extend to the Faroe Islands. → networks.md: `umhvorvisstovan_fo`
- **Volunteer**: none. Zero FRO stations on rtk2go or Centipede.
- **Gap**: RTK service confirmed but entirely gated behind direct contact with
  Umhvørvisstovan; no published endpoint or pricing. Hobbyists must deploy a local base
  or use PPP unless they can arrange direct institutional access.

### EE — Estonia

**date_added**: 2026-04-28

- **Free government RTK**: ESTPOS (Maa-amet, `gnss-rtk.maaamet.ee:8083`, 40 stations,
  VRS) — free until 31 Aug 2026 per director-general directive. → networks.md: `estpos`
- **Volunteer**: negligible.
- **Gap**: service expiry Aug 2026; currently timing out in CI (suspected egress firewall).

### FI — Finland

**date_added**: 2026-04-29

- **Free government RTK**: FINPOS (Maanmittauslaitos / NLS, `finpos.nls.fi:2101`)
  RTK granted only for research and testing with written justification; 3-month
  renewable; no production use. DGNSS free but sub-metre — out of scope.
  → networks.md: `finpos`
- **Volunteer**: rtk2go ~112 FI bases (largest national cluster on rtk2go after
  USA), Centipede ~18 FI nodes. De facto near-national free RTK through volunteer
  infrastructure; uptime not guaranteed.
- **Gap**: no public free government RTK for hobbyists; volunteer coverage is
  unusually dense and the practical free option.

### IS — Iceland

**date_added**: 2026-04-28

- **Free government RTK**: IceCORS (LMÍ, `178.19.53.126:2101`, VRS + single-base)
  — confirmed free ("data is free of charge" — natt.is). → networks.md: `icecors`
- **Volunteer**: negligible. ~2 AUSCORS reference stations (HOFN, REYK) appear in the
  pipeline but are geodetic infrastructure, not hobbyist correction services.
- **Gap**: IceCORS physical stations all carry nmea=1 (physical-coord-vrs) so the pipeline
  yields 0 map pins; a VRS circle is the current map representation. Registration at
  natt.is required to obtain stream credentials.

### LT — Lithuania

**date_added**: 2026-04-30

- **Free government RTK**: LitPOS (NZT / GIS-Centras, 35 stations, VRS) — free;
  endpoint confirmed 2026-04-30 (`193.219.10.2:2101` primary, `195.182.72.152:2101`
  secondary; both tested live). Register at geoportal.lt/web/litpos-paslauga/registracija.
  Added to pipeline. → networks.md: `litpos`
- **Volunteer**: negligible.
- **Gap**: none — LitPOS provides national VRS coverage, free with registration.

### LV — Latvia

**date_added**: 2026-04-28

- **Free government RTK**: LatPos (LGIA, `latpos.lgia.gov.lv:5001`, 27 LV + border
  stations, VRS) — free since 2018. Port 5001. → networks.md: `latpos`
- **Volunteer**: negligible.
- **Gap**: currently timing out in CI (suspected egress firewall on non-standard port).

### NO — Norway

**date_added**: 2026-04-29

- **Free government RTK**: none. CPOS/ETPOS (Kartverket, `cpos.kartverket.no:2101`,
  ~130 stations, VRS) — NOK 8,000+/yr (~$740/yr); expensive for a hobbyist.
  → networks.md: `cpos`
- **Volunteer**: rtk2go ~25 NO bases, Centipede ~21 NO nodes. Together ~46 bases;
  reasonable in populated areas (Oslofjord, Vestlandet); sparse north of ~63°N.
- **Paid only**: CPOS/ETPOS NOK 8,000+/yr (~$740/yr).
- **Gap**: no free government RTK; hobbyists rely on volunteer bases (good coverage
  south of ~63°N, sparse further north).

### PL — Poland

**date_added**: 2026-04-28

- **Free government RTK**: ASG-EUPOS (GUGiK, `system.asgeupos.pl:2101`, 130+
  stations, VRS) — free since Oct 2022; admin approval 1–2 working days.
  → networks.md: `asg_eupos`
- **Volunteer**: rtk2go ~51 PL bases (third-largest national cluster on rtk2go).
- **Gap**: ASG-EUPOS is VRS (0 physical pins); NRTK polygon deferred. rtk2go offers
  real physical pins as a complement.

### SE — Sweden

**date_added**: 2026-04-29

- **Free government RTK**: none for RTK. SWEPOS (Lantmäteriet, `dgnss-swepos.lm.se:2101`
  for DGNSS tier, VRS) — DGNSS tier free with account (free registration); RTCM 2.3;
  ~0.2 m horizontal — sub-metre, out of scope. Network RTK subscription ~9,000 SEK/yr
  (~$850/yr); expensive for a hobbyist. → networks.md: `swepos`
- **Volunteer**: rtk2go ~29 SE bases, Centipede ~1 SE node. Thin relative to
  Sweden's large area; mostly in the south.
- **Paid only**: SWEPOS Network RTK ~9,000 SEK/yr (~$850/yr).
- **Gap**: no free cm-accuracy NTRIP; volunteer bases cover southern Sweden adequately
  but thin out north of ~60°N.

---

## Europe — Eastern / Balkans

### AL — Albania

**date_added**: 2026-05-06

- **Free government RTK**: none with a public endpoint. ALBCORS (ASIG — Autoriteti
  Shtetëror për Informacionin Gjeohapësinor, state geodetic authority) operates 27
  CORS stations (21 ground-mounted + 6 roof-type, incorporating the former ALBPOS
  system) with a control centre in Tirana; aligned to ETRS89. Access is
  application-based (form at `krgjsh.asig.gov.al`; contact info.albcors@asig.gov.al);
  NTRIP host:port not publicly listed. 2023 EUREF Gothenburg symposium confirmed
  operational status. → networks.md: `albcors`
- **Commercial**: SATNET LIVE (Land&Co / Topcon Albania distributor, `landcoal.com`)
  — application via landcoal.com or SATNET app; 3 free days for new registrations;
  1 year free with Land&Co GNSS equipment purchase; ongoing pricing not published.
- **Volunteer**: none. Zero AL stations on rtk2go or Centipede.
- **Gap**: no free public NTRIP. Apply to ALBCORS via krgjsh.asig.gov.al or try
  SATNET LIVE via landcoal.com.

### XK — Kosovo

**date_added**: 2026-04-30

- **Free government RTK**: none. KOPOS / Kosovo Positioning System (Agjencia Kadastrale e Kosovës /
  Kosovo Cadastral Agency, `kopos.rks-gov.net:2101`, 8 permanent CORS, VRS, Leica GNSS Spider platform)
  — paid; €400/yr (~$468) annual subscription plus €20 one-time registration fee; no surveying-licence
  requirement found on the SBC registration form. NTRIP mountpoints and credentials provided inside the
  Spider Business Center portal after account creation. → networks.md: `kopos`
- **Volunteer**: none. Zero XK stations on rtk2go or Centipede.
- **Gap**: no free government RTK; KOPOS is the sole national network at ~$468/yr — expensive for a hobbyist.

### MD — Moldova

**date_added**: 2026-05-06

- **Government RTK (paid, open)**: MOLDPOS (Moldova Positioning System, S.E. INGEOCAD
  under the Agency for Geodesy, Cartography and Cadastre — AGCC, `agcc.gov.md`);
  caster IP `185.108.183.29:8080` (Leica Spider; non-standard port); SBC portal
  `moldpos.ingeocad.md`; VRS / MAX / MSM mountpoints; GPS+GLONASS+Galileo.
  Paid service since AGCC Order No. 04 of 06.01.2012; MDL tariff schedule not
  published online — contact via `ingeocad.md`. Free test
  zones (FreeZone mountpoints: FZUTM, FZUASM, FZMA, FZINGEOCAD, FZCDEIC;
  credentials `moldpos` / `moldpos`) allow trial without subscription. INGEOCAD
  explicitly states "MOLDPOS is an open network; any GPS receiver owner can join."
  No surveying licence required; no explicit residency restriction. Network
  launched 2011 (~10 stations); 2025 modernisation adds 5 more Leica Spider
  licences. Moldova is EU candidate (2022); ETRS89-aligned. → networks.md: `moldpos`
- **Volunteer**: none. Zero MDA stations on rtk2go or Centipede.
- **Gap**: no free national RTK, but FreeZone test mounts are a genuine free
  option for the handful of fixed test locations. Outside those, the paid
  subscription (MDL tariff via INGEOCAD) is required.

### BA — Bosnia and Herzegovina

**date_added**: 2026-04-29

- **Government RTK (paid, RS half — SRPOS)**: SRPOS (RGURS — Republička uprava
  za geodetske i imovinsko-pravne poslove, Republika Srpska, `srpos.rgurs.org:2101`
  or legacy `81.93.74.247:8080`, ~17 stations, MAX + iMAX + VRS + FKP +
  nearest-station). 2026 tariff confirmed 2026-04-30 (BAM, pegged 1.95583 to
  1 EUR): RTK 0.20 KM/min · 10 h **30 KM (~€15, ~$17)** · 20 h 50 KM (~$29) ·
  1 mo 250 KM (~€128, ~$145) · 1 yr 1,000 KM (~€511, ~$578); DGPS 1 mo 200 KM
  (~$116). Short pre-paid blocks (10/20 hours, ~$17 / ~$29) are the cheapest
  entry; per-minute (~$7/hr) and longer tiers rise quickly. Open to natural
  persons (no licence requirement); RS giro-account payment route.
  → networks.md: `srpos_ba`
- **Government RTK (paid, FBiH half — FBiHPOS)**: FBiHPOS (FGU — Federalna
  uprava za geodetske i imovinsko-pravne poslove, Federacija BiH,
  `fbihpos.katastar.ba:8080` — note port 8080, not 2101, ~17 stations,
  MAX + iMAX + VRS + NEAREST + combined H+V mountpoints). Tariff per FBiH
  Government Decision V. broj 605/2022 (BAM, gross): 100 KM (~$58) one-time
  registration; RTK-VPSP 7 days 150 KM (~$87), 1 mo 250 KM (~$145), 6 mo
  750 KM (~$435), 12 mo 1,000 KM (~$580); a "all services" 12-mo at 1,400 KM
  and post-processing-only 12-mo at 700 KM also exist. Multi-rover discounts
  -10% / -20% / cap -50%. Open to natural persons (the registration form has
  a dedicated "FIZIČKA LICA" section with no licence requirement). The 7-day
  and 1-month passes are the cheap short-period options; longer commitments
  scale up to 1,000 KM (~$580) for an annual subscription. Contact
  `fbihpos@fgu.com.ba`, +387 33 586 065. → networks.md: `fbihpos_ba`
- **Volunteer**: negligible. ~1 BIH base on rtk2go, zero on Centipede.
- **Gap**: no free RTK on either entity-level network. SRPOS short pre-paid
  hourly blocks (~$17 for 10 hours, ~$29 for 20 hours) are the cheap entry in
  Republika Srpska; FBiHPOS has no comparable hourly tier and its shortest
  block is a 7-day pass at 150 KM (~$87). Volunteer bases are the only free
  option.

### BG — Bulgaria

**date_added**: 2026-04-29

- **Free government RTK**: none. АГКК / GCSES (Агенция по геодезия, картография и
  кадастър — Geodesy, Cartography and Cadastre Agency) operates reference stations but
  no public NTRIP caster has been identified.
- **Commercial**: GeoNet Bulgaria GEO-RTK (Зенит-Гео ЕООД / Zenit-Geo Ltd,
  distributed by Солитех АД / Solitech AD, `gnss.geonet.bg:2101`, VRS).
  Certified by АГКК under Instruction РД-02-20-25/2011 (Cert. No. 013/2020,
  renewed to 2026). Pricing confirmed from Solitech AD tariff sheet dated
  01.04.2026: RTK12 annual unlimited €600/yr (~$660/yr) excl. VAT; shorter
  plans from €105/mo. GeoNet 150 occasional-use plan: €15/mo base + €0.10/min
  beyond 150 included minutes (24-month minimum). No explicit exclusion of
  private individuals. → networks.md: `geonet_bg`
- **Volunteer**: rtk2go ~7 BGR bases, Centipede ~1 BGR node. Thin coverage concentrated
  near Sofia and the main urban corridor.
- **Gap**: no free government RTK and no public hobbyist path; volunteer bases near Sofia
  are the only free option.

### BY — Belarus

**date_added**: 2026-04-30

- **Context**: EU Regulation 765/2006 (Belarus sanctions, extended and deepened via
  successive packages through 2024) mirrors the Russia-track on dual-use and advanced
  technology goods. Topcon, Trimble, and Leica suspended GNSS product exports to Belarus
  in 2022 in line with US, EU, and UK controls. Western precision-GNSS hardware is no
  longer legally importable, making replacement rover equipment materially harder to
  obtain than in unsanctioned neighbouring countries. Belarus also participates in the
  Russia–Belarus Union State, so GNSS policy broadly tracks Russian practice: state
  monopoly operator, no self-service public access.

- **Free government RTK**: none. ССТП РБ (Satellite System of Precise Positioning of
  the Republic of Belarus), operated by РУП «Белгеодезия» (state enterprise Belgeodesiya,
  under the State Committee for Property — Госкомимущество), covers ~98 continuously
  operating reference stations across Belarus with 1–2 cm RTK accuracy. Caster at
  `sstp.geo.by:8080` (IP fallback `93.125.21.51:8080`). Access requires signing a public
  contract (Публичный договор) with Belgeodesiya; available to individuals (физическое
  лицо) and organisations, but restricted to residents of the Republic of Belarus (tariff
  titled "для резидентов Республики Беларусь"). Billing is metered (0.24 BYN/min RTK,
  ~$0.085/min, "Общий" plan) or a fixed monthly plan ("Точная навигация", 150.78 BYN/month,
  ~$53/month, ~$641/yr if renewed monthly); no annual RTK flat rate published. No
  self-service portal. → networks.md: `sstp_by`

- **Volunteer**: none. Zero BY stations on rtk2go or Centipede.

- **Gap**: no free hobbyist access to ССТП РБ; the residency requirement and
  contract-only sign-up make it inaccessible to non-Belarusian users. Sanctions-
  constrained hardware supply compounds the barrier for those who could qualify.

### CZ — Czech Republic

**date_added**: 2026-04-29

- **Free government RTK**: CZEPOS (Zeměměřický úřad / ČÚZK, `czepos.cuzk.gov.cz:2101`,
  ~30 stations + 27 foreign-network stations, VRS) — free for public authorities,
  schools, and students; commercial/hobbyist use charged under Decree 31/1995 Sb.
  (as amended by 156/2023 Sb.): 10,000 CZK/yr (~€400) per receiver, or 1,000 CZK/month.
  Registration at `czepos.cuzk.gov.cz`. Expensive for a hobbyist.
  → networks.md: `czepos`
- **Volunteer**: rtk2go ~4 CZE bases, Centipede ~3 CZE nodes.
- **Gap**: no free hobbyist path; volunteer density is too thin for national coverage;
  the only affordable option is a self-operated base or a Centipede node.

### HU — Hungary

**date_added**: 2026-04-29

- **Government RTK (paid)**: GNSSnet.hu (Lechner Nonprofit Kft. / Lechner Tudásközpont,
  `ntrip.gnssnet.hu:2101`, VRS network solution + single-base RTK + DGNSS). Tariff
  (net of 27% ÁFA, Feb 2023 schedule, reconfirmed 2026-04-30): 12,000 HUF (~€30)
  one-time registration per company; 365-day flat rate 150,000 HUF (~€375) for RTK
  or Network RTK (54,000 HUF for DGNSS); shorter flat blocks at 30/90/150 days
  (36,000 / 72,000 / 108,000 HUF); a 30-day local-radius option within 50 km of one
  fixed coordinate at 15,000 HUF (~€38); per-minute fallback at 8 HUF/min RTK,
  12 HUF/min Network RTK, 3 HUF/min DGNSS. Expensive at the annual rate; the
  per-minute RTK rate (~€1.20/hr) is cheap for occasional use; the 30-day
  local-radius pass (~€38) covers a single project within 50 km of one
  point. Registration at `gnssnet.hu`.
  → networks.md: `gnssnet_hu`
- **Volunteer**: Centipede ~223 HUN nodes (single largest non-France country in the
  Centipede sourcetable), rtk2go ~6 HUN bases. Near-national free RTK coverage
  through volunteers; densest in the Great Hungarian Plain and northern Hungary.
- **Gap**: no free government RTK. The Centipede volunteer network provides practical
  free coverage for most of the country without registration; GNSSnet.hu is the
  paid alternative, with a 30-day 50 km flat (~€38) or per-minute (~€1.20/hr RTK)
  tariff that makes a single-project sign-up feasible for hobbyists.

### ME — Montenegro

**date_added**: 2026-04-29

- **Government RTK (paid)**: MONTEPOS (Uprava za nekretnine / Real Estate
  Administration, `gov.me/clanak/montepos`) — 9 CORS stations, VRS-capable.
  Subscription periods confirmed 2026-04-30: 24 h, 48 h, 1 month, 3 months,
  6 months, 1 year, 2 years. Application form (`Zahtjev za MontePos`) and
  tariff PDF (`MontePos- tehnički detalji`, both 2024-04-11 PDFs on
  `wapi.gov.me`); EUR figures not yet retrieved. Host:port not on the public
  page — disclosed post-registration. Payment to giro account 832-1081-58
  with "Montepos - RTK" purpose. Admin contact Goran Popović, tel
  +382 67 641 119. No professional licence required. Montenegro uses EUR.
  → networks.md: `montepos`
- **Volunteer**: none. Zero MNE stations on rtk2go or Centipede.
- **Gap**: no free RTK; paid MONTEPOS is the only option, and pricing is only
  visible after pulling the tariff PDF or contacting the admin directly.

### MK — North Macedonia

**date_added**: 2026-05-06

- **Government RTK (paid, open)**: MAKPOS (Macedonian Positioning System, Agency for
  Real Estate Cadastre — AREC, `katastar.gov.mk`); caster `makpos.katastar.gov.mk:9001`
  (Leica GNSS Spider RT Proxi Server + NTRIP caster; independently confirmed on Alberding
  GmbH worldwide caster map); SBC portal `makpos.katastar.gov.mk/sbc/`. 14 reference
  base stations at 50–70 km spacing across ~25,700 km². Services: DGPS (0.3–0.5 m,
  RTCM 2.x), RTK (2–4 cm, RTCM 2.x/3.x), precise positioning (<1 cm, RINEX). Galileo
  support added April 2020. Tariff: MKD schedule not publicly posted; one source indicates
  free of charge for compatible GNSS devices on 3G/GPRS — unconfirmed if still current;
  contact AREC Sector for Geodetic Works to confirm. No surveying licence requirement
  found. Register at `makpos.katastar.gov.mk/sbc/Account/Register`. → networks.md: `makpos`
- **Volunteer**: negligible. Zero MKD stations on rtk2go or Centipede.

### RO — Romania

**date_added**: 2026-04-29

- **Free government RTK**: ROMPOS (ANCPI — Agenția Națională de Cadastru și Publicitate
  Imobiliară, `rtk.rompos.ro:2101`, VRS, ~80+ permanent fixed reference stations (CORS)) — paid
  credit-based; ~€169/yr (~$183) — modest annual fee, affordable for a hobbyist. Registration via
  `app.rompos.ro` (ANCPI account required; self-service at `epay.ancpi.ro`).
  → networks.md: `rompos`
- **Volunteer**: Centipede ~10 ROM/ROU nodes, rtk2go ~7 ROU bases. Modest coverage
  concentrated near major cities.
- **Gap**: no free RTK; ROMPOS is paid-affordable at ~€169/yr and is the practical
  option for hobbyists needing national-scale coverage.

### RS — Serbia

**date_added**: 2026-04-29

- **Free government RTK**: AGROS (Republički geodetski zavod — RGZ, `agros.rgz.gov.rs`)
  — paid; ~30 permanent fixed reference stations (CORS); VRS (Trimble VRS Now backbone). RTK flat-rate
  subscription: 1,125 RSD/month (~€10/month) or 8,688 RSD/year (~€74/yr at ~117 RSD/EUR);
  DGPS flat-rate: 703 RSD/month or 5,379 RSD/year (~€46/yr). Per-minute and hourly
  packages also available. Registration via rgz.gov.rs (Serbian portal).
  → networks.md: `agros`
- **Volunteer**: Centipede ~20 SER + ~3 SRB nodes, rtk2go ~35 SRB/SER bases — one of
  the denser volunteer clusters in the Western Balkans, concentrated in Vojvodina.
- **Gap**: AGROS RTK is paid-affordable (~€74/yr, well within hobbyist reach);
  volunteer coverage is good in Vojvodina but sparse in southern Serbia.

### RU — Russia

**date_added**: 2026-05-02

- **Government systems (not NTRIP)**:
  - СДКМ / SDCM (Система Дифференциальной Коррекции и Мониторинга): Russia's SBAS; L-band
    satellite corrections (~20 cm sub-metre); requires SBAS-capable receiver, no internet.
    Out of scope. → networks.md: `sdcm`
  - ФАГС / ВГС (Фундаментальная астрономо-геодезическая сеть / Высокоточная геодезическая
    сеть — Fundamental and High-Accuracy Geodetic Networks): government reference frame
    maintained by Росреестр; research/government use only, no public NTRIP delivery.
- **Free government RTK**: none. No federal authority provides a free public NTRIP stream.
- **Commercial RTK** (all paid; all expensive for a hobbyist at current ₽/USD rates):
  - **EFT-CORS** (EFT GROUP, `ntrip.eftgroup.ru:2101`): Russia's largest CORS aggregator;
    hundreds of stations growing nationally; GPS+GLONASS+BDS+GAL; ports 2101 primary,
    2102 (all stations), 2103 (nearest), 2104 (sCMRx); day/month/annual plans; RINEX
    basic post-processing free; 3-day RTK trial; individual registration with name + email
    only. Annual 50,400 ₽/yr (~$593/yr); day pass 420 ₽ (~$5). 5% VAT included.
    → networks.md: `eft_cors`
  - **RTKNet** (`cors.rtknet.ru:2101` / `94.250.250.43:2101`, regional ports 6030–6041):
    300+ stations since 2013; 30,000 ₽/yr annual (~$353/yr at ~85 ₽/USD), 4,000 ₽/mo
    (~$47/mo); 3-day free trial; public offer contract, individual sign-up.
    → networks.md: `rtknet`
  - **HIVE** (Геосистемс Аэро, `hive.geosystems.aero:2101`): aggregation platform with
    742 stations across 79 regions; pay-per-station per-day (single-baseline RTK, no VRS);
    hourly RINEX; station owners contribute and receive revenue share. Per-station prices
    only visible on map after login. → networks.md: `hive_cors`
  - **ГЕОСПАЙДЕР** (НПП «ГЕОМАТИК», `geo-spider.net:2101`): 200+ stations across North-West
    and Central Russia; RTK in MSK local coordinate system (network RTK/VRS); annual plan
    44,100 ₽/yr (~$519/yr, 30% discount); day pass 315–525 ₽; 5% VAT included.
    Coverage expanding. → networks.md: `geospider`
  - **SmartNet** (Hexagon/Leica): international commercial VRS; Russia availability
    uncertain post-2022 sanctions.
- **Post-2022 sanctions**: Western GNSS correction services (Trimble VRS Now, Leica SmartNet)
  suspended or restricted in Russia. Domestic services (EFT-CORS, RTKNet, HIVE) have
  expanded. GNSS receiver imports complicated by component sanctions; parallel-import
  workarounds exist.
- **Volunteer**: negligible. rtk2go ~1 RU-tagged station (a MIRAI overseas station
  miscoded); Centipede negligible. Russian hobbyists typically deploy a local base station
  using SNIP Lite or open-source NTRIP casters.
- **Gap**: no free RTK for hobbyists. Cheapest occasional-use option is a day pass (315–420 ₽,
  ~$4–5); cheapest annual plan is RTKNet at 30,000 ₽/yr (~$353/yr). All annual plans are
  expensive relative to median hobbyist budgets. Hobbyists needing centimetre accuracy
  typically set up a local base instead.

### SK — Slovakia

**date_added**: 2026-04-29

- **Government RTK (paid-affordable, hobbyist-eligible)**: SKPOS (GKÚ
  Bratislava / Geodetický a kartografický ústav, `skpos.gku.sk:2101`, ~26
  stations, VRS). 2026 schedule confirmed 2026-04-30: SKPOS_cm/RTK
  **€70/yr (~$79)** or €25/mo (~$28) per device; dual-receiver €140/yr;
  SKPOS_dm/DGNSS €25/yr; SKPOS_mm post-processing €0.07/hr or €70 for
  1000 h/yr. Free for Slovak public-sector bodies and municipalities under
  Act 145/1995. Registration form (`skpos.gku.sk/register/`) explicitly accepts
  "Fyzická osoba bez živnostenského listu" (private individual without trade
  licence) and lists almost all UN member states — open internationally.
  **One of the cheapest national-scale network-RTK services in the EU and
  the cheapest hobbyist on-ramp in the Visegrád region.** → networks.md: `skpos`
- **Volunteer**: rtk2go ~2 SVK bases, Centipede ~2 SVK nodes.
- **Gap**: none for hobbyists at €70/yr; SKPOS is the recommended path.

### UA — Ukraine

**date_added**: 2026-04-30

- **Context**: No government-run national RTK caster exists. UA-EUPOS was conceived as
  Ukraine's contribution to the pan-European EUPOS standard (same framework as Poland's
  ASG-EUPOS, Slovakia's SKPOS) but never became a unified public service — in practice the
  ecosystem is dominated by competing commercial operators. ZAKPOS is the original
  UA-EUPOS-branded member; UA-System.NET is the largest. All networks pause or reduce
  capacity during air-raid alerts; coverage in Kharkiv, Zaporizhzhia, Donetsk, Kherson, and
  Luhansk oblasts is severely degraded or absent due to infrastructure damage and occupation.

- **Free government RTK**: none. The State Permanent GNSS Network (СКНЗУ, Держгеокадастр)
  operates reference stations for geodetic control and post-processing but provides no public
  NTRIP caster. GeoTerrace (Lviv Polytechnic, geoterrace.lpnu.ua) is RINEX / post-processing
  only — no real-time RTK service.

- **Commercial** (all paid; all over $200/yr):
  - **UA-System.NET** (Системи Солюшнс, `gnss.org.ua:2101`, 200+ stations, nationwide, VRS)
    — 21,120–23,670 UAH/yr (~$515–577/yr) full national; regional packs (West/Karpaty/
    South/East) ~13,000–13,500 UAH/yr (~$317–329/yr); wartime discount packages for eastern
    and southern oblasts; Leica Spider VRS platform. → networks.md: `ua_system_net`
  - **ZAKPOS** (ДП "Закарпатгеодезцентр", `195.16.76.194:2102`, nationwide, VRS zone-based)
    — 15,000 UAH/yr (~$366/yr) wartime reduced tariff (April 2025); hub at Mukachevo
    (Zakarpattia, far west); pauses during air-raid alerts; service resumed after martial-law
    suspension (Feb 2022–April 2025). → networks.md: `zakpos`
  - **RTK HUB** (TNT-TPI, `rtkhub.com`, nationwide; host:port not published) — 10,500
    UAH/yr (~$256/yr) from Jan 2025; endpoint disclosed post-registration.
    → networks.md: `rtkhub`
  - **NGCNET** (NGC Ltd) — DNS not resolving April 2026; likely defunct. → networks.md: `ngcnet`

- **Volunteer**: rtk2go ~3 UA bases; status uncertain. Zero Centipede nodes in Ukraine.

- **Gap**: No free RTK anywhere in Ukraine. UA-System.NET is the largest and most modern
  (200+ stations, Leica VRS, warzone discount plans); RTK HUB is the most affordable
  (~$256/yr) but does not publish its endpoint. Active front-line jamming and spoofing
  further degrade signal quality in conflict zones. A self-operated base station is the
  only reliable option in areas of active conflict.

---

## Europe — Territories and dependencies

### AX — Åland Islands (FI)

**date_added**: 2026-05-06

- **Volunteer**: Centipede ~2 AX nodes (country code `ALA`). Small archipelago between Finland and Sweden; partial coverage.
- **FINPOS (Finland NLS)**: Nominally covers Åland territory, but its real-time RTK service is restricted to research and testing use only — 3-month term grants, requires written justification. Free DGNSS (sub-metre) and RINEX raw data services are open to registered users. Not a hobbyist RTK option; see → FI entry and networks.md: `finpos`.
- **Gap**: The two Centipede nodes are the only no-restriction centimetre-level RTK option in Åland. SWEPOS (Sweden, `swepos.lantmateriet.se:2101`) covers the nearest Swedish mainland (~200 km from Åland) but requires a paid subscription and coverage geometry is marginal at that distance.

### French overseas territories

**date_added**: 2026-04-29

Centipede volunteer nodes in several French overseas territories, served via `crtk.net`.
TERIA (Ordre des Géomètres-Experts / Hexagon) covers the Antilles-Guyane zone at the
same subscription price as mainland France (from €895 HT/yr, ~$970/yr — expensive for a hobbyist). IGN RGP maintains permanent GNSS reference stations in Guyane,
Guadeloupe, and Mayotte; real-time streaming is restricted and requires a formal request
to CNES — not a walk-up public NTRIP service.

| Territory | Code | Stations | Notes |
|---|---|---|---|
| Réunion (RE) | `REU` | ~4 Centipede | Indian Ocean island; partial coverage |
| Martinique (MQ) | `MTQ` | ~1 Centipede | Lesser Antilles; single base |
| New Caledonia (NC) | `NCL` | ~2 Centipede | Pacific territory; sparse |
| French Polynesia (PF) | `PYF` | ~2 Centipede | Pacific archipelago; sparse |
| French Guiana (GF) | `GUF` | 0 Centipede, 0 rtk2go | Mainland South America; Kourou ESA spaceport has scientific GNSS instrumentation (not public NTRIP); TERIA paid coverage |
| Guadeloupe (GP) | `GLP` | 0 Centipede, 0 rtk2go | Lesser Antilles; TERIA paid coverage |
| Mayotte (YT) | `MYT` | 0 Centipede, 0 rtk2go | Indian Ocean; IGN RGP reference frame (RGM23); TERIA coverage unconfirmed for YT |

### UK Crown dependencies and overseas territories

**date_added**: 2026-04-29

OS Net (Ordnance Survey GB) covers Great Britain only and does not extend to
any Crown dependency or overseas territory. SmartNet/TopNET licensed resellers
similarly have no published coverage for these jurisdictions.

| Territory | Code | Volunteer | Notes |
|---|---|---|---|
| Gibraltar (GI) | `GIB` | 0 rtk2go, 0 Centipede | British Overseas Territory on the southern Spanish coast. No confirmed public NTRIP. ERGNSS (ES) stations at Ceuta (~28 km) and Tarifa (~16 km) are the practical free-correction option — both within L1+L2 RTK baseline. GIB operates a BIGF/IGS tide-gauge reference station (GIBR) for post-processing only. → networks.md: `gibr_gi` |
| Jersey (JE) | `JEY` | 1 Centipede (`JE12`, registered as `ENG`) | Bailiwick of Jersey. No confirmed government NTRIP. One Centipede volunteer base on the island provides partial coverage. |
| Guernsey (GG) | `GGY` | 0 rtk2go, 0 Centipede | Bailiwick of Guernsey. No confirmed government NTRIP; no volunteer stations found. Nearest rtk2go/Centipede bases are on the French coast or Jersey. |
| Isle of Man (IM) | `IMN` | 0 rtk2go, 0 Centipede | Crown dependency. No confirmed government NTRIP; no volunteer stations found. Nearest bases are in northern England or Northern Ireland (~60–80 km). |

### GL — Greenland (DK)

**date_added**: 2026-05-01

- **Free government RINEX (PPK only)**: GNET — Greenland GNSS Network (`go-gnet.org`),
  ~60 continuous GNSS stations, operated jointly by KDS/Klimadatastyrelsen (Danish Agency
  for Climate Data, formerly SDFi) and DTU Space. RINEX 2/3 observation files distributed
  via Dataforsyningen (`dataforsyningen.dk`) for post-processing; no real-time NTRIP
  stream advertised in any aggregator as of 2026-05-01. Asiaq (Greenland Survey,
  `asiaq.gl`) lists Survey and Construction services but publishes no GNSS correction
  product. → networks.md: `gnet_gl`
- **Volunteer**: none. Zero GRL stations on rtk2go, Centipede, or EarthScope NOTA.
- **Gap**: no public RTK correction service of any kind for Greenland. GNet RINEX archives
  are freely available for PPK via Dataforsyningen; hobbyists needing real-time corrections
  must deploy a local base or use PPP.

### SJ — Svalbard (NO)

**date_added**: 2026-05-06

- **Free government RTK**: none for Svalbard. CPOS (Kartverket, `159.162.103.14:2101`)
  explicitly covers **mainland Norway only** — Svalbard and Jan Mayen excluded;
  no Svalbard stations feed the CPOS VRS solution. Kartverket's geodetic
  observatory at Ny-Ålesund (Brandal facility, opened 2018; VLBI + permanent
  GNSS) provides raw RTCM 3.2 MSM5 data under commercial data agreements to
  licensed operators — not a public NTRIP caster.
- **Free single-base via EarthScope**: IGS stations NYA1 and NYAL at Ny-Ålesund
  stream 1 Hz real-time observations via `ntrip.earthscope.org:2101` (free with
  EarthScope account, non-commercial). Single-base coverage; useful within ~30–40 km
  of Ny-Ålesund for RTK if a nearby base is configured.
- **Volunteer**: Centipede 1 node (`NYAWIPEV`, ~78.9°N, Ny-Ålesund — AWIPEV
  Franco-German Arctic research station). Useful within ~20–40 km (Kongsfjorden
  area). Longyearbyen (~120 km SE) is outside reliable RTK range.
- **Gap**: no free RTK for Longyearbyen and most of Svalbard. Hobbyists must
  deploy a local base or use PPP (Galileo HAS, ~40 cm).

---

## Americas — North

### CA — Canada

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed in any province.
  - NRCan: post-processing only (CACS/CSRS RINEX archive; NRCAN-PPP web tool). No streaming NTRIP.
  - Quebec MERN: per-station direct TCP streams; not NTRIP-aggregated — pipeline-incompatible.
    → networks.md: `qc_mern` (rejected)
  - BC RTN: paid regional service via GeoBC, CAD 1,650/yr (~$1,212). → networks.md: `bc_rtn`
  - Nova Scotia NSACS: 40-station government fixed reference station network (CORS); real-time NRTK only via paid
    commercial providers (HxGN SmartNet, Can-Net, Brandtnet); SmartNet Atlantic plan (NB, NL, NS, PE) at CAD
    $3,328/yr (~$2,429/yr); Can-Net and Brandtnet pricing not publicly listed. → networks.md: `nsacs`
  - Ontario, Alberta, Saskatchewan, Manitoba: no provincial CORS; no confirmed public NTRIP.
- **Volunteer**: rtk2go ~65 CA bases, Centipede ~19 CA nodes. Concentrated heavily
  in BC, Ontario, and southern Quebec; very thin elsewhere.
- **Gap**: no free national or provincial NTRIP in Canada. Volunteer networks are
  the only free path for hobbyists.

### US — United States

**date_added**: 2026-05-02

- **Free government RTK**: EarthScope NOTA (`ntrip.earthscope.org:2101`, ~1,000+
  stations, single-base, non-commercial NULA) — Americas-wide, dense in western USA.
  → networks.md: `earthscope`

  Physical-coordinate state DOT networks (free registration unless noted; all listed
  in `docs/networks.md`): WISCORS (WI), FPRN (FL), ARDOT RTN (AR), MaCORS (MA),
  VECTOR (VT), AzCORS (AZ), GCGC RTN (MS), AlCORS (AL), ORGN (OR), MSRN (MI),
  NYSNet (NY), InCORS (IN), IARTN (IA) — physical stations.
  VRS-only: KyCORS (KY), MnCORS (MN), ODOT RTN (OH), MoDOT RTN (MO, notarized
  agreement required), WVRTN (WV), MaineDOT (ME), Mesa County RTVRN (CO, county-level,
  ~33 underlying stations across western Colorado).
  → networks.md: `wiscors`, `fprn`, `ardot_rtn`, `macors`, `vector`, `azcors`,
  `gcgc_rtn`, `alcors`, `orgn`, `msrn`, `nysnet`, `incors`, `iartn`, `kycors`,
  `mncors`, `odot_rtn`, `modot_rtn`, `wvrtn`, `mainedot`, `mesa_rtvrn`

  Note: MnCORS, ORGN, MSRN, NYSNet, AzCORS have significant EarthScope NOTA overlap —
  expect duplicate physical pins until deduplication is added. VRS-only entries (KyCORS,
  MnCORS, ODOT RTN, MoDOT RTN, WVRTN, MaineDOT, Mesa County RTVRN) produce no physical
  pins; shown as VRS stopgap circles.

  MoDOT requires notarized access agreement (conditions access). → networks.md: `modot_rtn`
  ACORN (AK) — `www.acorn-gnss.net:2101`, Trimble Pivot Web, operated by Alaska DNR +
  DOTPF/NPS/EarthScope. Caster serves both a nearest-station single-base stream
  (MS_RTCM3) and VRS network-RTK (SouthCentral, SouthEast, Interior; NorthWest and
  NortonSound experimental). Anonymous sourcetable exposes VRS and MS_RTCM3 mountpoints;
  individual station streams require login. Free; self-service registration at
  acorn-gnss.net (no professional licence field required). In pipeline (2026-05-02).
  → networks.md: `acorn`

  NPS CORS (national) — `rtk.nps.gov:2101`, 142 stations across US and territories
  (~128 active 2026-05-02), RTCM MSM4, single-base. Operated by National Park Service;
  includes ACORN physical stations in Alaska. Portal: ntrip.nps.gov; NTRIP caster:
  rtk.nps.gov:2101. Datum transitioning to MYCS3 (positions updated February 2026).
  Credentials via gnss_posnav@nps.gov; no public eligibility policy. Not in pipeline
  (credentials required). → networks.md: `nps_cors`

  Research / dual-access arrays (no independent free hobbyist caster — listed for
  documentation, with the same physical antennae reachable through other in-pipeline
  sources): BARD (~40 stations, SF Bay / Northern California, UC Berkeley + USGS)
  reaches NTRIP via SOPAC CRTN or EarthScope NOTA; PANGA (~220 CWU sites + ~700 NOTA
  stations processed at CWU, Pacific Northwest / Cascadia) reaches NTRIP via EarthScope
  NOTA or — for Washington only — paid WSRN. → networks.md: `bard`, `panga`

  Paid/restricted states: CRTN (CA, $100 one-time fee, paid-affordable; clearinghouse for
  SOPAC SCIGN, BARD, USGS Pasadena SCIGN, Caltrans CVSRN, Orange County OCRTN, and
  EarthScope NOTA in California; universities/schools exempt from fee), SCRTN (SC, $600/yr per login), NCRTN (NC ~$500/yr), TDOT (TN ~$450/yr), TURN GPS (UT ~$600/yr), MTSRN
  (MT ~$1,500/yr), WSRN (WA ~$1,900/yr; PANGA/CWU contributes Puget Sound antennae),
  TxDOT (employees-only), Caltrans (vetted agency partners only). → networks.md: `crtn`,
  `scrtn`, `ncrtn`, `tdot_rtn`, `turn_gps`, `mtsrn`, `wsrn`, `txrtn`, `calrtns`

  No federal free NTRIP: NOAA/NGS real-time service shut Apr 2013 (budget sequestration).
- **Volunteer**: rtk2go ~142 US bases (largest single-country cluster on rtk2go);
  dense in upper Midwest, Pacific Northwest, mid-Atlantic. Centipede ~3 US nodes.
- **Gap**: Great Plains and interior South have sparse coverage despite state networks.

### PR — Puerto Rico (US territory)

**date_added**: 2026-04-29

- **Free government RTK**: EarthScope NOTA (`ntrip.earthscope.org:2101`, single-base,
  non-commercial NULA) — several NOTA/COCONet stations in the PRVI region stream
  real-time corrections; the same non-commercial registration used for the continental
  US applies. → networks.md: `earthscope`

  PRSN CORS (`prsn.uprm.edu`) — 18–24 permanent GNSS stations operated by the
  Puerto Rico Seismic Network (University of Puerto Rico Mayagüez); the PRSN pages
  describe an NTRIP service for real-time corrections. Access is research/academic
  oriented and requires registration via UPRM; host:port not publicly listed on the
  open web. → networks.md: `prsn_cors`

  NOAA NCN maintains several CORS stations in PR (e.g. PRJC, PRGY, P780, PRMI, N240)
  — post-processing only via UFCORS/CLASS; no real-time NTRIP stream since the 2013
  shutdown.

- **Commercial**: VRS Systems PR (HLCM Group, `hlcmgroup.com`) — 8-receiver island-wide
  VRS network, four-constellation (GPS + GLONASS + Galileo + BeiDou), upgraded 2022;
  pricing not publicly listed (contact HLCM Group). → networks.md: `vrs_pr`

- **Volunteer**: rtk2go — 0 confirmed PR mountpoints in current sourcetable. Centipede
  — negligible.
- **Gap**: EarthScope NOTA gives hobbyists free single-base corrections; PRSN's academic
  NTRIP caster likely requires institutional registration. VRS Systems PR is the only
  island-wide NRTK option but is commercial with undisclosed pricing.

### VI — US Virgin Islands (US territory)

**date_added**: 2026-04-29

- **Free government RTK**: none territory-operated. EarthScope NOTA (`ntrip.earthscope.org:2101`,
  non-commercial NULA) includes COCONet/NOTA stations in the PRVI region that cover the
  Virgin Islands; the same registration as continental US applies.
  → networks.md: `earthscope`
- **Volunteer**: none. Zero VI mountpoints on rtk2go or Centipede.

---

## Americas — Latin

### BO — Bolivia

**date_added**: 2026-04-30

- **Free government RTK**: none confirmed. IGM Bolivia (Instituto Geográfico Militar,
  `igmbolivia.gob.bo`) operates MARGEN-ROC (Red de Operaciones Continuas) and the CEPAG
  processing centre for SIRGAS contributions. IGM advertises raw RINEX and an NTRIP
  correction service, but no public endpoint or registration portal has been found.
  `igm.gob.bo` was unreachable on 2026-04-30 (`igmbolivia.gob.bo` may differ — unverified).
  Crucially, SIRGAS Bol21 (2016) states IGM was "joining" the commercial GeoBolivia SRL
  initiative rather than operating its own public caster; fieldwork literature confirms
  practitioners use the commercial GeoBolivia GEO1 station rather than an IGM service.
  → networks.md: `margen_bolivia`
- **Commercial**: RED-GEO CORS NTRIP (GeoBolivia SRL, Ley 2997 del Topógrafo / COTOBOL)
  — ~7 stations covering La Paz, Cochabamba, Oruro, Sacaba, Tarija, Santa Cruz, and
  Yacuiba; caster port 6060. Credentials issued by phone only — no self-service portal
  or published hostname. Pricing not listed publicly; Facebook page active as of
  2026-04-30 (website geoboliviasrl.info unreachable same date). → networks.md: `redgeo_bo`
- **Commercial**: GEOEQUIPOS SRL Red CORS (`geoequipossrl.com/red-cors/`) — a second private
  commercial network; mobile-payment friendly via QR codes in Bolivianos (≤500 Bs per
  transaction). Host:port and pricing not publicly documented; contact via website.
- **Volunteer**: rtk2go — 0 confirmed BO bases. Centipede — negligible.
- **Gap**: no free public NTRIP for hobbyists. The government MARGEN-ROC service appears
  to delegate RTK corrections to GeoBolivia SRL commercially. RED-GEO is phone-subscription
  only with unpublished pricing. GEOEQUIPOS offers a second commercial option with QR-code
  mobile payments.

### AR — Argentina

**date_added**: 2026-04-29

- **Free government RTK**: RAMSAC-NTRIP (IGN, `ntrip.ign.gob.ar:2101`, ~206 stations,
  single-base) — free, 8-hr session cap, web registration at ign.gob.ar. → networks.md: `ramsac`
- **Volunteer**: rtk2go ~7 AR bases, mostly Buenos Aires and Córdoba.
- **Gap**: RAMSAC provides solid national single-base coverage; the 8-hour session cap requires periodic re-authentication but does not block hobbyist use.

### BR — Brazil

**date_added**: 2026-05-06

- **Free government RTK**: RBMC-IP (IBGE, `gps-ntrip.ibge.gov.br:2101`, ~150 stations,
  single-base) — free, gov.br signup, 5-station limit per user, 1,000 concurrent max.
  Five new stations inaugurated December 2024 (Governador Valadares, Maceió, Januária,
  Pinhais, Nova Friburgo). → networks.md: `rbmc_ip`
- **Commercial**: geoRTK (geortk.com.br, launched September 2025) — claims largest RTK/PPK
  network in Brazil, targeting 500 stations; BRL 10/day or BRL 79/week plans with 30-day
  free trial. GeoPlus (geoplusbrasil.com) and RTKdata (rtkdata.com/br/, USD 40/month) also
  operate commercial networks with national coverage claims.
- **Volunteer**: rtk2go ~17 BR bases, concentrated in São Paulo and southern states.
- **Gap**: RBMC-IP coverage is sparse in the Amazon basin and north-east interior; the 5-simultaneous-mountpoint cap is not a practical barrier for hobbyists but the gov.br account requirement adds a registration step.

### BZ — Belize

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed. The Surveys and Mapping Section (Ministry of Natural Resources, `naturalresources.gov.bz`) is responsible for horizontal and vertical control networks and supervises cadastral surveys; no fixed reference station network (CORS) or public NTRIP caster endpoint found. Belize's national spatial data infrastructure (BNSDI, `portal.bnsdi.gov.bz`) provides map data access but does not include a real-time GNSS correction service.
- **Volunteer**: none. Zero BZ stations on rtk2go or Centipede.
- **Gap**: no domestic RTK service. Cross-border reach from Mexico (INEGI CORS,
  `ntrip.inegi.org.mx:2101`, free with registration) may cover the Corozal and Orange Walk
  districts in northern Belize, and Guatemala's IGN CORS (`rtk.igntopo.gob.gt:2101`) may
  extend into western Belize (Cayo District) — both unconfirmed for actual usable baselines
  at those distances.

### CL — Chile

**date_added**: 2026-05-01

- **Free government RTK**: RGN/SIRGAS-CHILE (IGM — Instituto Geográfico Militar, `igm.cl`,
  `sirgaschile.cl`, ~180+ fixed reference stations (CORS), single-base) — RINEX files and
  coordinate certificates downloadable free via `sirgaschile.cl`. IGM announced a real-time
  NTRIP service in 2025 (procedure: `youtube.com/watch?v=4yuH1W05eII`); however,
  `ntrip.igm.cl:2101` returns connection refused and IGM's NTRIP sub-pages return HTTP 500
  as of 2026-05-01. ArduSimple (2025) describes the network as CORS/PPK only — whether the
  announced real-time service is operational is unconfirmed. → networks.md: `sirgas_chile`
- **Commercial** (paid; pricing not publicly listed):
  - **Geocom GNSS Network** (`geocom.cl/pages/red-gnss`): commercial CORS covering major
    population centres; NTRIP subscription; pricing not on public pages (6-month demo reportedly
    available on request). → networks.md: `geocom_gnss_cl`
  - **KollNET** (`kollnerlabrana.cl/kollnet.html`): prepaid packages (7-day / 15-day / 30-day /
    annual); pricing not publicly listed. → networks.md: `kollnet_cl`
- **Volunteer**: rtk2go ~1 CL base (Iquique, Tarapacá region). No EarthScope CHL-coded stations.
- **Gap**: no confirmed free public NTRIP caster endpoint as of 2026-05-01. SIRGAS-CHILE has
  180+ CORS and RINEX is freely downloadable; real-time RTK streaming may exist but no working
  public endpoint has been verified. Chile's long north–south geography means a hobbyist
  caster would need dense station coverage — the infrastructure exists but hobbyist access
  is not yet self-service confirmed.

### CO — Colombia

**date_added**: 2026-04-29

- **Free government RTK**: IGAC MAGNA-ECO (IGAC, `sbc.igac.gov.co:2101`, 233 declared stations,
  physical-coord-vrs, 17 unique physical coordinates in sourcetable) — free, register at
  redgeodesica-sbc.igac.gov.co/sbc; Law 1955/2019 mandates public access. → networks.md: `igac`
- **Volunteer**: negligible. Two COL-coded stations appear via EarthScope NOTA.
- **Gap**: MAGNA-ECO is the first confirmed free VRS/NRTK in Latin America; the sourcetable reports only 17 distinct physical coordinates, so hobbyists outside the populated Andean corridor may find coverage thin.

### GT — Guatemala

**date_added**: 2026-04-30

- **Free government RTK**: IGN Guatemala (Instituto Geográfico Nacional, `ign.gob.gt`) operates a fixed reference station network (CORS) of ~17 stations distributed nationally, established with technical and financial support from RIC (Registro de Información Catastral). RINEX 2.11 data is available for download. The IGN and RIC public portals list only a post-processing RINEX product; no live NTRIP/RTK streaming service is publicly documented. → networks.md: `ign_gt_cors`
- **Volunteer**: rtk2go — 0 confirmed GT bases. Centipede — negligible.
- **Gap**: no real-time RTK for hobbyists; government CORS is post-processing only. No commercial NTRIP provider lists Guatemala coverage.

### HN — Honduras

**date_added**: 2026-04-30

- **Free government RTK**: none. The IP/DGCG (Dirección General de Cartografía y
  Geografía, sub-directorate of the Instituto de la Propiedad) operates a 5-station
  CORS network (Tegucigalpa, San Pedro Sula, Juticalpa, Siguatepeque, La Ceiba)
  accessible at cors.ip.gob.hn — the portal is a post-processing RINEX download
  service only; no NTRIP caster host:port or real-time RTK subscription exists.
  The "IGN Honduras" brand at ign.hn is the same institution (DGCG), not a separate
  agency. → networks.md: `ip_cors_hn`
- **Volunteer**: none. Zero HN stations on rtk2go or Centipede.
- **Gap**: no real-time RTK for hobbyists, free or paid. The 5-station CORS network
  provides post-processing RINEX downloads only. No commercial NTRIP provider lists
  Honduras coverage.

### NI — Nicaragua

**date_added**: 2026-04-30

- **Free government RTK**: INETER CORS (Instituto Nicaragüense de Estudios Territoriales, Dirección General de Geodesia y Cartografía, `consultacf.ineter.gob.ni`): CORS infrastructure exists with RINEX data downloadable via the Catastro Físico portal; the INETER and SINAPRED portals list only a post-processing RINEX product; no real-time NTRIP streaming service is publicly documented. → networks.md: `ineter_cors`
- **Volunteer**: none. Zero NI stations on rtk2go or Centipede.
- **Gap**: no real-time RTK for hobbyists; government CORS is post-processing only. No commercial NTRIP provider lists Nicaragua coverage.

### PA — Panama

**date_added**: 2026-04-29

- **Free government RTK**: IGNTG CORS (Instituto Geográfico Nacional "Tommy Guardia", `ignpanama.anati.gob.pa`, ~19 stations, single-base) — fixed reference station network (CORS) under ANATI (Autoridad Nacional de Administración de Tierras). Seven stations are part of SIRGAS-CON and have internet connectivity with remote monitoring; the remaining stations are national densification points. A 2025 modernisation project is restoring eight previously inoperative stations. Real-time NTRIP access terms are not publicly documented — no self-service registration portal or public host:port found; access appears to require direct contact with IGNTG. → networks.md: `igntg_cors_pa`
- **Commercial**: Topored (`panama.casadeltopografo.com/topored`) — 28 stations across Panama and Colombia, operated by Casa del Topógrafo (control centre in Bogotá). Emits differential corrections via NTRIP; RINEX download also offered. Pricing not publicly listed (contact via website). → networks.md: `topored_pa`
- **Volunteer**: none. Zero PA stations on rtk2go or Centipede.
- **Gap**: no confirmed free public NTRIP for hobbyists; IGNTG's 19-station CORS is the government framework but the caster endpoint and credentials are not publicly listed. Commercial Topored is the only known real-time NTRIP option but at undisclosed subscription cost.

### SV — El Salvador

**date_added**: 2026-05-06

- **Free government RTK**: CNR/IGCN (Centro Nacional de Registros — Instituto Geográfico y del Catastro Nacional, `cnr.gob.sv`) operates active fixed reference stations (CORS) including SNJE, SSIA, and VMIG; RINEX data available via eCNR online services. The CNR portal lists only a post-processing RINEX product; no live NTRIP/RTK streaming service is publicly documented. → networks.md: `cnr_sv_cors`
- **Commercial**: Survey3G (`survey3g.com`) — pioneer commercial NTRIP service in El Salvador; 6 stations (San Miguel, Perkin, La Unión, San Salvador-UES, Santa Ana, Cojute); GPS+GLONASS+BDS+GAL, L1/L2/L5; credentials supplied by email after payment. Published pricing (survey3g.com/servicios-de-ntrip/, confirmed 2026-05-06): USD 45/mo · USD 135/3 mo · USD 450/12 mo — above the $200/yr hobbyist cutoff. → networks.md: `survey3g_sv`
- **Volunteer**: none. Zero SV stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists; government CORS is post-processing only; Survey3G costs ~$450/yr for annual access.

### CR — Costa Rica

**date_added**: 2026-04-29

- **Free government RTK**: IGN-CR CORS (Instituto Geográfico Nacional — Registro Nacional,
  `igncaster.snitcr.go.cr`, 14 stations, single-base) — free with web registration at
  `snitcr.go.cr` (SNIT — Sistema Nacional de Información Territorial). After creating a SNIT
  account, navigate to Herramientas → Herramientas GNSS and accept terms; access to the caster
  requires a twice-daily validation cycle (00:00 / 12:00 local time). Station data also used for
  RINEX download and online post-processing. → networks.md: `ign_cr_cors`
- **Volunteer**: rtk2go ~4 CRI bases (Huacas, Alajuela, San José / OVSI area, San Isidro).
  EarthScope NOTA provides 2 CRI-coded stations (QSEC, VRAI — free, in-pipeline).
- **Gap**: the 14-station IGN-CR CORS covers the central valley and main regions well; the
  twice-daily validation delay is a minor operational friction. Free to register; no fees.

### EC — Ecuador

**date_added**: 2026-05-01

- **Free government RTK**: REGME-IP — Red GNSS Militar Ecuatoriana de Posicionamiento
  en Tiempo Real (IGM — Instituto Geográfico Militar del Ecuador,
  `ntrip.igm.gob.ec:2101`, single-base) — free with registration at
  `https://www.geoportaligm.gob.ec/ntrip/`; stated as "totalmente libre y gratuito".
  Confirmed active 2026-05-01; SIRGAS bulletin (2022) names the endpoint explicitly.
  → networks.md: `regme_ec`
- **Volunteer**: rtk2go ~3 ECU bases.
- **Gap**: REGME-IP is the confirmed free national caster; online registration with no
  stated residency restriction.

### PY — Paraguay

**date_added**: 2026-04-28

- **Free government RTK**: none confirmed. No national NTRIP caster identified.
- **Volunteer**: rtk2go ~3 PRY bases.
- **Gap**: no confirmed free public NTRIP for Paraguay; hobbyists must deploy a local
  base station.

### CU — Cuba

**date_added**: 2026-04-29

- **Context**: Cuba's RTK landscape is shaped by two overlapping constraints: the US embargo restricts import and payment pathways for US-origin GNSS hardware (Trimble, Leica, Javad all fall under OFAC licensing requirements), and Cuba's national internet infrastructure — operated exclusively by ETECSA, the state telecoms monopoly — is expensive, intermittent, and gated behind dual-currency pricing that makes sustained data connections difficult for individuals. GEOCUBA (Grupo Empresarial GEOCUBA), the state geodetics and cartography enterprise under the Ministry of the Revolutionary Armed Forces (MINFAR), has deployed a national GNSS fixed reference station network (CORS) using non-US hardware (primarily Chinese and Eastern European receivers) acquired outside embargo restrictions. A 2024 conference paper ("Servicio NTRIP GNSS en Cuba: perspectivas y retos", Informática Habana 2024) confirmed that a national NTRIP service has been established internally — but its public accessibility is uncertain.

- **Free government RTK**: GEOCUBA national GNSS service (GEOCUBA, `geocuba.cu`, 13 permanent stations installed 2014–2019, single-base) — no publicly listed host:port or self-service registration portal; the caster is described as published within GEOCUBA's Geospatial Information Centre and targeted at "prioritised sectors of the national economy." No evidence of hobbyist or general-public access. Connectivity from outside Cuba to any internal server would face both internet infrastructure constraints and potential embargo-licensing friction for payment or software. → networks.md: `geocuba_gnss`

- **Volunteer**: none. Zero CUB stations on rtk2go or Centipede.

- **Gap**: no confirmed free public NTRIP endpoint accessible to hobbyists inside or outside Cuba. The 13-station GEOCUBA network exists operationally but appears to serve government and commercial survey clients only. Non-US GNSS hardware (u-blox, Unicore, Septentrio) is importable under general licence; the practical barrier is internet access and institutional gatekeeping rather than an absolute legal prohibition. Hobbyists outside Cuba cannot rely on a Cuban caster; hobbyists inside Cuba have no confirmed path to a self-service connection.

### HT — Haiti

**date_added**: 2026-04-29

- **Context**: Criminal gangs (the "Viv Ansanm" coalition) control approximately 90 % of Port-au-Prince and its metropolitan area as of early 2026. Haiti has had no elected president or legislature since the assassination of President Moïse in July 2021. Infrastructure disruption, hardware-import collapse, and the loss of effective government authority make any near-term expansion of geodetic services structurally impossible.

- **Free government RTK**: CNIGS (Centre National de l'Information Géo-Spatiale, `cnigs.ht`) — as of 2018 one NTRIP fixed reference station (CORS) in Port-au-Prince was operational, installed with post-earthquake reconstruction aid. CNIGS had plans for a broader national CORS system; status of expansion and current operability of that single station is unconfirmed given the 2024–2026 security collapse. No public host:port found; CNIGS's website and office in Tabarre (northern Port-au-Prince) have an uncertain operational status. → networks.md: `cnigs_ht`

- **Volunteer**: none. Zero HT stations confirmed on rtk2go or Centipede.

- **Gap**: no confirmed free public NTRIP for hobbyists. The single CNIGS CORS station (if still operating) is inaccessible without direct contact with CNIGS staff. Hardware import, physical site access, and institutional continuity are all at risk under current conditions. Do not rely on any Haitian CORS for field work without on-the-ground verification.

### DO — Dominican Republic

**date_added**: 2026-04-29

- **Free government RTK**: REGNA-RD (IGN-JJHM — Instituto Geográfico Nacional "José Joaquín
  Hungría Morell", `ntrip.ign.gob.do`, port not publicly listed, ~11+ single-base fixed reference stations (CORS),
  growing) — free with web registration at `ntrip.ign.gob.do`. Credentials and connection
  instructions issued after form submission. Network is actively expanding: two stations added
  in Moca and Puerto Plata in late 2024; 11 northern-region stations certified mid-2024;
  further installations planned along the Haiti border zone with the Ministry of Defence.
  SIRGAS-compatible reference frame. → networks.md: `regna_rd`

- **Commercial** (paid; pricing not on public website):
  - **FUNDCORSRD** (`fundcorsrd.com`): ~30 stations; foundation-operated; NTRIP subscription;
    pricing not publicly listed (contact via website). → networks.md: `fundcorsrd`
  - **CORS-RD / Geomatica** (`geomatica.com.do`): Trimble-based commercial network;
    registration + monthly fee per rover; pricing not listed publicly. → networks.md: `cors_rd_geo`
  - **CODIA-CORS-MET** (`codia.org.do`): Professional association (engineers/architects/
    surveyors) members only; NTRIP subscription; pricing not listed publicly. → networks.md: `codia_cors`

- **Volunteer**: none confirmed. Zero DO stations on rtk2go or Centipede.

- **Gap**: REGNA-RD is free and open after a straightforward web registration; the main
  friction is that the host:port is not shown until after login, and the network is still
  sparse — coverage is strongest in the north (Santiago / Puerto Plata corridor) with the
  south and border zone still being filled. Commercial alternatives (FUNDCORSRD, CORS-RD,
  CODIA) offer denser coverage for professionals but at undisclosed subscription costs.

### BB — Barbados

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Lands and Surveys Department (Ministry of Housing,
  Lands and Maintenance) holds geodetic responsibility; no public NTRIP caster or registration
  portal found. A decommissioned NOAA CORS station (BDOS) was removed from service in 2013.
- **Volunteer**: none. Zero BB stations on rtk2go or Centipede.

### BS — Bahamas

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Department of Lands and Surveys (Ministry of
  Works) is the geodetic authority; no public NTRIP caster or registration portal found.
  Two EarthScope COCONet stations (CN13, San Salvador Island; CN14, Great Inagua) stream
  real-time data via `ntrip.earthscope.org:2101` (NULA, free non-commercial) — geophysics
  monitoring sites only, not positioned for population-area RTK. → networks.md: `earthscope`
- **Volunteer**: none. Zero BS stations on rtk2go or Centipede.

### JM — Jamaica

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed. The National Land Agency (NLA, `nla.gov.jm`) is
  the geodetic and surveys authority; no public NTRIP caster or registration portal found.
  A mid-2000s VRS network built by Spatial Innovision for NLA is unconfirmed as currently
  active with any public endpoint. Three EarthScope NOTA/COCONet stations in Jamaican
  waters stream via `ntrip.earthscope.org:2101` (NULA, free non-commercial): CN10 (Morant
  Cay, ~130 km SE of Kingston), CN11 (Pedro Cay, ~130 km S of Kingston) — both remote
  offshore cays, not practical for mainland RTK — and CN12 (Kingston, UWI Mona campus
  Physics Dept roof), the only station useful for hobbyist RTK on the main island.
  → networks.md: `earthscope`
- **Volunteer**: none. Zero JM stations on rtk2go or Centipede.

### TT — Trinidad and Tobago

**date_added**: 2026-04-29

- **Free government RTK**: TTAGN (Trinidad and Tobago Active Geodetic Network; Surveys and
  Mapping Division, Ministry of Agriculture, Land and Fisheries, `gpscors.gov.tt`, ~5 stations,
  single-base) — access model not publicly documented; host:port and registration procedure
  not listed on the public website. EarthScope COCONet station CN57 (~10.84°N, −60.94°W,
  Trinidad) streams via `ntrip.earthscope.org:2101` (NULA, free non-commercial) —
  single geophysics station only. → networks.md: `ttagn`, `earthscope`
- **Volunteer**: none. Zero TT stations on rtk2go or Centipede.
- **Gap**: TTAGN exists and appears operational, but whether hobbyists can register and
  connect is unclear from public sources; contact Surveys and Mapping Division at
  `agriculture.gov.tt` for access details.

### AG — Antigua and Barbuda

**date_added**: 2026-05-06

- **Free government RTK**: none national. The Lands and Survey Division is the geodetic
  authority; no public NTRIP caster or registration portal found.
- **EarthScope NOTA** (`ntrip.earthscope.org:2101`) — free noncommercial (annual NULA);
  includes COCONet stations CN00 (Codrington, Barbuda) and CN01 (Bethesda, Antigua main
  island), plus a site on uninhabited Redonda Island. CN01 is the practical option for
  most of Antigua: single-base, good within ~20–30 km. Legacy UNAVCO platform retired
  2025-07-29; all streams now at earthscope.org. → networks.md: `earthscope`
- **Volunteer**: none. Zero AG stations on rtk2go or Centipede.

### KN — Saint Kitts and Nevis

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Lands and Surveys Unit (`gov.kn`) holds
  geodetic responsibility; no public NTRIP caster or registration portal found.
  COCONet lists a seismic-monitoring cGPS station on Saint Kitts (Soufrière Hills
  monitoring network), but no real-time NTRIP stream is publicly advertised.
- **Volunteer**: none. Zero KN stations on rtk2go or Centipede.

### LC — Saint Lucia

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed. The Survey and Mapping Section (Ministry of
  Physical Development, Housing and Urban Renewal) is the geodetic authority; no public
  NTRIP caster or registration portal found. UNAVCO installed two COCONet/NOTA cGPS
  sites (CN04 and CN47, both on the roof of the NEMO building near Castries) in 2014;
  these stream as real-time NTRIP via `ntrip.earthscope.org:2101` (free non-commercial,
  NULA account required). Both are co-located at the same NEMO site, so geographic
  coverage is limited to northern Saint Lucia; baseline to Vieux Fort / Soufrière in the
  south is ~30–40 km, at the edge of reliable cm-accuracy range. → networks.md: `earthscope`
- **Volunteer**: none. Zero LC stations on rtk2go or Centipede.

### VC — Saint Vincent and the Grenadines

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Lands and Surveys Department
  (`transport.gov.vc`) is the geodetic authority. A World Bank–funded Caribbean
  Digital Transformation Project (2020–2025) funded geodetic network modernisation
  and datum modernisation work; as of early 2025 the project was completing a
  digital mapping exercise, but no public NTRIP caster or host:port has been
  announced.
- **Volunteer**: none. Zero VC stations on rtk2go or Centipede.

### GD — Grenada

**date_added**: 2026-05-06

- **Free government RTK**: none. No national CORS or NTRIP caster identified.
- **EarthScope COCONet**: CN46 (Mount Pleasant, Carriacou — a Grenada dependency
  ~35 km north of the main island) streams via `ntrip.earthscope.org:2101` —
  free non-commercial under EarthScope NULA (account required); RTCM 3.3 MSM7
  1 Hz single-base. Practical caveat: CN46 is 35–75 km from Grenada's main island,
  outside reliable cm-precision single-base RTK range (~20–30 km); users on the
  main island likely need a local base. → networks.md: `earthscope`
- **Volunteer**: none. Zero GRD stations on rtk2go or Centipede.
- **Gap**: no national NTRIP service; EarthScope CN46 (Carriacou) is the only
  free real-time stream in Grenada territory but is too distant for main-island
  RTK. Deploy a local base for work on Grenada island.

### KY — Cayman Islands (UK Overseas Territory)

**date_added**: 2026-04-29

- **Free government RTK**: none free. The Lands and Survey Department (`caymanlandinfo.ky`)
  operates four fixed GPS reference stations (CORS) — GCFS and GCEA (Grand Cayman), CBMD (Cayman Brac), LCSB (Little
  Cayman) — under the PAIP (Positional Accuracy Improvement Programme). RINEX data are
  available free for post-processing. Real-time RTK corrections are available as a paid
  subscription; pricing is not listed publicly (contact the Chief Surveyor via
  `caymanlandinfo.ky`). No public NTRIP caster or host:port discovered. → networks.md:
  `ky_cors`
- **Volunteer**: none. Zero KY stations on rtk2go or Centipede. No EarthScope COCONet
  station in Cayman waters.

### TC — Turks and Caicos Islands (UK Overseas Territory)

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Survey and Mapping Department (Lands
  Division, Attorney General's Chambers, `gov.tc/landsurvey`) maintains the national
  geodetic network and cadastre; no public NTRIP caster, host:port, or registration
  portal found.
- **Volunteer**: none. Zero TC stations on rtk2go or Centipede. No EarthScope COCONet
  station in TCI waters found in local data.

### VG — British Virgin Islands (UK Overseas Territory)

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Land and Survey Department
  (`bvi.gov.vg/departments/land-and-survey-department`) maintains the National Geodetic
  Framework; no public NTRIP caster or host:port found.
- **EarthScope NOTA**: one COCONet station, CN03_RTCM3P3 (18.49°N, −64.40°W, Tortola
  area, dual-frequency, country code VGB), streams via `ntrip.earthscope.org:2101`
  under the free non-commercial NULA licence — the only free real-time GNSS correction
  reachable in BVI territory. → networks.md: `earthscope`
- **Volunteer**: none. Zero VG stations on rtk2go or Centipede.
- **Gap**: a single EarthScope station (CN03) is live and free; hobbyists can connect
  under NULA. Government RTK corrections are not publicly accessible.

---

## Dutch Caribbean

### CW — Curaçao

**date_added**: 2026-05-01

- **Free government RTK**: none confirmed. Stichting Kadaster en Openbare Registers Curaçao
  (`kadaster.cw`, confirmed alive 2026-05-01) has no GNSS or NTRIP section. Neither the
  NSGI/Kadaster Netherlands caster (`ntrip.kadaster.nl:2101`) nor the TLS caster
  (`ntrip.cloud.kadaster.nl:443`) carries any CUW-coded mountpoint (sourcetable verified
  2026-05-01); NSGI FAQ confirms geodetic enquiries for Curaçao must go to local
  authorities. → networks.md: `cw_cors`
- **EarthScope NOTA**: one COCONet station, CN40_RTCM3P3 (12.18°N, −68.96°W, near
  Willemstad, dual-frequency, country code CUW), streams via `ntrip.earthscope.org:2101`
  under the free non-commercial NULA licence. → networks.md: `earthscope`
- **Volunteer**: rtk2go ~3 CW bases (CWM_JAJO_RTK_RTCM3_X, MPA_JAJO_RTK_RTCM3_X,
  UTE_JAJO_RTK_RTCM3_X — all near Willemstad). Centipede — none.
- **Gap**: EarthScope CN40 and three rtk2go volunteer bases provide de-facto free
  correction coverage around Willemstad; no government NTRIP service exists.

### AW — Aruba

**date_added**: 2026-05-01

- **Free government RTK**: none confirmed. Dienst Landmeetkunde en Vastgoedregistratie
  (DLV) is the geodetic authority; `dlv.aw` yields no live result (2026-05-01); `gov.aw`
  contains only civil aviation GNSS references. NSGI FAQ confirms DLV falls outside
  NSGI's mandate. → networks.md: `aw_cors`
- **EarthScope NOTA**: one COCONet station, CN19_RTCM3P3 (12.61°N, −70.05°W, northern
  Aruba, dual-frequency, country code ABW), installed 2013, streams via
  `ntrip.earthscope.org:2101` under the free non-commercial NULA licence.
  → networks.md: `earthscope`
- **Volunteer**: rtk2go ~1 AW base (PINOST1, Santa Cruz, 12.50°N, −69.98°W).
  Centipede — none.
- **Gap**: EarthScope CN19 and one rtk2go volunteer base provide limited free coverage;
  no government NTRIP service exists.

### BQ — Bonaire, Sint Eustatius, Saba (Dutch special municipalities)

**date_added**: 2026-05-06

- **Free government RTK**: AGRS.BES — Kadaster Nederland / NSGI (`ntrip.kadaster.nl:2101`
  unencrypted, `ntrip.kadaster.nl:443` TLS) — free, anonymous, confirmed active
  2026-05-06. Seven BES-coded streams across three islands: Bonaire (BON200BES0 RTCM 3.3
  MSM, BONK00BES0 RTCM 3.3 MSM), Saba (SABY00BES0 RTCM 3.3 MSM, SABY0 RTCM 3.1 legacy,
  SABY00BES1 raw SBF), Sint Eustatius (SEUS00BES0 RTCM 3.3 MSM, SEUS0 RTCM 3.1 legacy).
  Single-base streams; not VRS. NSGI pricing page explicitly lists BES stations as free
  (€0); no username or password required. → networks.md: `bq_cors`
- **Volunteer**: none on rtk2go or Centipede.
- **Gap**: single-base streams only — each island has its own dedicated reference
  station(s). Bonaire: BON200BES0 or BONK00BES0; Saba: SABY00BES0; Sint Eustatius: SEUS00BES0.

### SX — Sint Maarten (Dutch part)

**date_added**: 2026-05-01

- **Free government RTK**: none confirmed. Stichting Kadaster- en Hypotheekwezen Sint
  Maarten (`kadaster.sx`) became GIS-capable in 2025 but operates no public NTRIP
  caster; NSGI sourcetable carries no SXM-coded mountpoints (verified 2026-05-01).
  An early-2026 MOU between VROMI / Kadaster Sint Maarten and Kadaster Netherlands
  confirms institutional cooperation — not an operational NTRIP service. → networks.md:
  `sx_cors`
- **Volunteer**: none. Zero SX stations on rtk2go or Centipede. The nearest EarthScope
  COCONet station is CN59_RTCM3P3 (18.21°N, −63.05°W, country code AIA — on Anguilla,
  ~20 km north of Sint Maarten), which streams via `ntrip.earthscope.org:2101` under the
  free NULA licence and is reachable from SXM territory. → networks.md: `earthscope`
- **Gap**: no SXM-coded public NTRIP exists; EarthScope CN59 on neighbouring Anguilla
  is the closest free option (~20 km baseline, dual-frequency).

---

### MX — Mexico

**date_added**: 2026-05-01

- **Free government RTK**: RGNA — Red Geodésica Nacional Activa (INEGI — Instituto Nacional de
  Estadística y Geografía, ~36 stations, single-base) — RINEX files at 15-second intervals,
  freely downloadable via SFTP at `geodesia.inegi.org.mx`. INEGI's current documentation
  (confirmed 2026-05-01) states no real-time NTRIP/RTK streaming is offered — post-processing
  only. A 2013 SIRGAS bulletin discussed NTRIP aspirations; these were not implemented.
  → networks.md: `rgna_mx`
- **Commercial** (paid; pricing not on public websites — contact required):
  - **Red CORS México** (DTM Topografía, `dtmtopografia.com/cors-mexico/`): largest commercial
    network by national coverage, 85+ cities; monthly and annual memberships; pricing not listed
    on public pages. → networks.md: `red_cors_mx`
  - **GeoCORS / Survey+** (`en.surveyplusmx.com`): 55+ stations nationally; 15-day demo
    available; pricing not listed publicly. → networks.md: `geocors_mx`
  - **Hi-Target Red CORS** (resellers such as `puntovisado.com`): ~MX$2,414/month per licence;
    resold through GNSS equipment dealers. → networks.md: `hitarget_cors_mx`
- **Volunteer**: rtk2go ~3 MX bases (Tamaulipas, Querétaro, Baja California).
  EarthScope NOTA provides ~18 MEX-coded single-base stations (free, in-pipeline) concentrated
  in Baja California and southern Mexico.
- **Gap**: no free RTK/NTRIP endpoint in Mexico. RGNA is confirmed RINEX/PPK-only.
  EarthScope NOTA is the only confirmed free in-pipeline option, covering mainly the
  northern border zone (~18 MEX-coded stations).

### PE — Peru

**date_added**: 2026-05-06

- **Free government RTK**: REGPMOC — Red Geodésica Permanente de Monitoreo Continuo (IGN — Instituto
  Geográfico Nacional del Perú, under Ministry of Defence, `190.12.71.75:2101`, 70 registered ERP
  stations / 35+ active as of late 2024; MQ04 Moquegua added March 2026)
  — paid; application + payment to IGN required; credentials issued by email; no self-service portal. IGN's
  own "Políticas de Uso del Servicio NTRIP" policy document does not explicitly restrict to licensed surveyors
  or commercial organisations. No official PEN tariff publicly available (TUPA pages returning 404); reseller
  indication: ~$85/month (~$1,020/yr) at one Peruvian integrator (unverified, not an official IGN rate). RTCM
  3.2 and CMR+; NTRIP v2.0. → networks.md: `regpmoc`

- **Volunteer**: rtk2go ~1 PE base (LIMA1\_RTCM3, Lima, RTCM 3.2, active). Zero PE nodes on Centipede.

- **Gap**: REGPMOC gives excellent national single-base coverage but requires direct engagement with IGN
  and payment (no online self-service). The single Lima rtk2go base is the only confirmed free option;
  hobbyists outside Lima have no free correction source.

### UY — Uruguay

**date_added**: 2026-04-28

- **Free government RTK**: REGNA-ROU (IGM — Instituto Geográfico Militar,
  `rtk.igm.gub.uy:2101`, ~26 stations, single-base + VRS) — confirmed free
  ("El Servicio no tiene costo"); web registration at
  `rtk.igm.gub.uy/SBC/Account/Register`. VRS capable (1–2 cm horizontal
  with dual-frequency equipment). Network expanded Dec 2025 with 8 additional
  multiconstellation fixed reference stations (CORS); 1,000+ registered users. Reference frame
  SIRGAS-ROU (ITRF-compatible). → networks.md: `regna_rou`
- **Volunteer**: rtk2go ~2 bases near the Argentinian border (border-area
  RAMSAC stations); no dedicated UY volunteer streams confirmed. Centipede —
  negligible.
- **Gap**: REGNA-ROU provides free national coverage; main friction is a
  registration step and Spanish-language portal. In pipeline as `regna_rou`.

### GY — Guyana

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. GL&SC (Guyana Lands and Surveys
  Commission, `glsc.gov.gy`) operates an 8-station fixed reference station network (CORS) (Eclipse Falls,
  Supenaam, Georgetown, New Amsterdam, Olive Creek, Lethem, Linden, and one
  additional site) established 2018–2019 under a G$93 million contract with
  Ordnance Survey International; network is connected to SIRGAS. No public
  NTRIP caster host:port or self-service registration portal has been published;
  access appears to be for professional/government use only. → networks.md:
  `glsc_cors`
- **Volunteer**: none. Zero GY stations on rtk2go or Centipede.
- **Gap**: no free or hobbyist-accessible NTRIP confirmed; the CORS infrastructure
  exists (8 stations nationally) but no public caster endpoint is listed.

### SR — Suriname

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed. MI-GLIS (land registry/cadastral authority)
  has no documented GNSS correction service. Suriname has at least one GNSS monument
  processed by IBGE's SIRGAS-CON analysis centre (post-processing RINEX only; not a
  real-time NTRIP stream). Brazil's RBMC-IP northernmost stations are ~700–900 km
  from Paramaribo — too distant for single-base RTK.
- **Volunteer**: none. Zero SR stations on rtk2go or Centipede.
- **Gap**: no NTRIP caster of any kind — government, commercial, or community.
  Deploy a local base station for RTK; use Galileo HAS / PPP for sub-metre work.

### VE — Venezuela

**date_added**: 2026-05-06

- **Free government RTK**: REMOS (IGVSB — Instituto Geográfico de Venezuela
  Simón Bolívar, `igvsb.gob.ve`). 29 permanent stations installed nationally, 27 with
  NTRIP capability per 2012 SIRGAS bulletins; as of December 2025, IGVSB reported
  progress integrating CORS stations into the SIRGAS-RT real-time caster. No public
  caster host:port or registration portal has been found; the caster appears to operate
  for institutional use only. Free service advertised via Stonex Venezuela for RTK
  equipment users. → networks.md: `remos_ven` (deferred)
- **Commercial**: Acnovo / acnovo.net — private CORS network operating across Venezuela;
  24/7 base stations, RTCM 3.x; ~USD 20 per subscription period (exact billing cycle
  unclear); credentials delivered post-registration. → networks.md: (no block yet)
- **Volunteer**: rtk2go — 0 confirmed mainland VE bases (3 rtk2go bases
  visible at ~12°N, 68–69°W are on Curaçao/Aruba, not Venezuelan territory).
  Negligible Centipede presence.
- **Gap**: no confirmed free public NTRIP caster for mainland Venezuela.
  Acnovo.net is the most accessible commercial option (~$20/period). GPS jamming
  was reported around Venezuelan territory September–December 2025 (FAA advisory
  covering MAIQUETIA FIR, November 2025–February 2026); local single-base RTK
  is less affected than satellite-derived PPP.

---

## Asia Pacific — Oceania

### AU — Australia

**date_added**: 2026-05-06

- **Free government RTK**: AUSCORS (Geoscience Australia, `ntrip.data.gnss.ga.gov.au:2101`
  or TLS on port 443, 914 stations, single-base, CC BY 4.0) — free, web signup at
  gnss.ga.gov.au/registration. Mountpoints follow `<STA4>00AUS0` convention; RTCM 3.3 MSM.
  → networks.md: `auscors`
- **Commercial**: State VRS networks (CORSnet-NSW, GPSnet VIC, SARNRIP SA, CORS-Q QLD, etc.)
  are cost-recovery and paid — pricing varies by state but generally expensive for a hobbyist;
  contact each state land agency directly. Commercial nationwide VRS also via HxGN SmartNet Aus,
  Positioned RTK, and AllDayRTK.
- **Volunteer**: rtk2go ~26 AU bases, Centipede ~3 AU nodes. Thin relative to Australia's size;
  supplements AUSCORS in densely populated south-eastern areas.
- **Gap**: AUSCORS single-base coverage is solid continent-wide; state VRS networks offer
  network solutions but are paid — hobbyists should use AUSCORS directly.

### NZ — New Zealand

**date_added**: 2026-04-29

- **Free government RTK**: PositioNZ-RT (LINZ, `positionz-rt.linz.govt.nz:2101`,
  ~62 fixed reference stations (CORS), single-base, CC BY 4.0 NZ) — free, LINZ account required;
  register at linz.govt.nz. → networks.md: `positionz`
- **Volunteer**: rtk2go ~11 NZ bases, concentrated in the North Island and upper South Island.
- **Gap**: PositioNZ-RT covers the mainland and Chatham Islands with good single-base density;
  no practical gap for hobbyists — registration is the only friction.

### FJ — Fiji

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Department of Lands and Survey
  (Ministry of Lands and Mineral Resources, `lands.gov.fj`) established a
  fixed reference station network (CORS) of ~10 stations: two long-running stations in Suva and Lautoka
  plus eight new sites (Labasa, Nabouwalu, Taveuni, Kadavu, Koro Island,
  Lakeba, Ono-i-Lau, Rotuma) commissioned via the Fiji Geodetic Datum Project
  (2019–2022, SPC-supported) to achieve <50 km inter-station spacing. No
  public NTRIP caster host:port or registration portal has been published;
  SPC's September 2022 milestone announcement noted that access regulations
  were still being developed. One Fiji site (LAUT) contributes to AUSCORS
  and the APREF archive. → networks.md: `fiji_dlss_cors`
- **Volunteer**: none. Zero FJ stations on rtk2go or Centipede.
- **Gap**: CORS infrastructure now in place nationally but no public NTRIP
  endpoint has been announced; deploy a local base or await policy finalisation
  from the Ministry of Lands.

### PG — Papua New Guinea

**date_added**: 2026-04-30

- **Free government RTK**: none confirmed. DLPP (Department of Lands and Physical
  Planning) operates WAIG/PNGM CORS in Port Moresby and supports the PNG2020 geodetic
  datum; PNG University of Technology (Unitech) hosts IGS station LAE1 in Lae. Both
  are scientific reference stations contributing to Geoscience Australia's APREF
  network; `dlpp.gov.pg` returned HTTP 403 on 2026-04-30. A FIG 2025 paper (Stanaway,
  Nidkombu et al.) confirms ~6-station PNG2020 programme network and intent to offer
  RTCM3/NTRIP under a UN-GGIM FAIR open-access principle, but the portal was not yet
  public as of April 2025. The MRA PNG ran a demonstration NTRIP test at a Unitech
  workshop but published no public endpoint. → networks.md: `png_dlpp_cors`
- **Volunteer**: none. Zero PG stations on rtk2go or Centipede.
- **Gap**: no hobbyist-accessible RTK correction service exists in PNG. AUSCORS
  streams APREF stations (`ntrip.data.gnss.ga.gov.au:2101`) but coverage over PNG is
  reference-grade with baselines far exceeding practical RTK range. Hobbyists must
  deploy a local base. Contact ASPNG (`aspng.org`) for updates on PNG2020 NTRIP portal.

---

## Asia Pacific — East Asia

### CN — China

**date_added**: 2026-04-30

- **Legal framework**: 测量法 (Surveying and Mapping Law of the PRC, 2002, revised 2017),
  Articles 27–29 require institutional surveying credentials (测绘资质) to operate or access
  fixed reference station networks (CORS). All government and provincial CORS are closed to unlicensed individuals.
- **Government networks (licensed professionals only)**:
  - 全国卫星导航定位基准站 (National CORS, Ministry of Natural Resources / NASG): 2,700+
    stations; feeds the 北斗地基增强系统 (BeiDou Ground-Based Augmentation System / BGAS);
    no public NTRIP endpoint. → networks.md: `bgas_china`
  - 省级CORS网 (Provincial CORS — all 34 provinces/municipalities): first established by
    深圳SZCORS (Shenzhen, 2003); every province now has its own network; registration
    requires organisational credentials + surveying licence; some provinces free for
    licensed organisations, others charge (e.g., Sichuan ¥8,000/yr). Not hobbyist-accessible.
    → networks.md: `chinese_provincial_cors`
- **Commercial RTK** (no professional licence required; open to individuals):
  - **千寻知寸 Qianxun** (Alibaba + Norinco JV, `rtk.ntrip.qxwz.com:8003`): 2,700+
    stations, 33 provinces; ¥3,600–3,800/yr (~$500–528/yr) — expensive for a hobbyist;
    individuals register directly. Most widely used commercial CORS in China.
    → networks.md: `qianxun`
  - **中国移动CORS China Mobile CORS** (CMCC, 4,400+ stations, nationwide): ~¥3,600/yr
    (~$500/yr); NTRIP access via data plan; open to individuals. Same price bracket as
    Qianxun. → networks.md: `cmcc_cors`
  - **腾讯位置服务RTK Tencent RTK** (`cors.tencent.com`, unconfirmed from current public
    sources): launched August 2022 as free public beta; 2,800+ virtual network stations;
    33 provinces; 2 cm horizontal accuracy. As of 2026-04-30 the product page
    (lbs.qq.com/rtk) shows enterprise business-inquiry contact only — no self-service
    pricing or purchase flow. A ¥998/yr figure circulated in community discussion at the
    2022 beta launch but has not been confirmed from a primary source price page; current
    pricing is unknown. Access via an SDK integration model suggests enterprise
    developer / B2B positioning, not individual subscription. Chinese phone number and
    likely business licence required for commercial use. → networks.md: `tencent_rtk`
- **Volunteer**: negligible. rtk2go ~1 CHN-tagged volunteer station; Centipede negligible.
  Chinese hobbyists (drone pilots, precision-agriculture DIY, autonomous-vehicle developers)
  typically pay Qianxun at full price or deploy a local base using SinoGNSS / ComNav /
  Unicore Communications receivers.
- **Gap**: 测量法 closes all government CORS to unlicensed users. Qianxun and CMCC at
  ~¥3,600/yr (~$500/yr) are the only commercial options with confirmed individual
  registration. Tencent RTK is live but has moved to an enterprise inquiry model with
  no published hobbyist pricing; it cannot currently be recommended as an accessible
  option. Non-Chinese hobbyists have no confirmed path.

### HK — Hong Kong

**date_added**: 2026-04-29

- **Free government RTK**: SatRef (Lands Dept / SMO, `ntrip.geodetic.gov.hk:2101`,
  19 physical stations + VRS mountpoint `VRS32G`, physical-coord-vrs, 4-constellation,
  open data) — free, register via geodetic.gov.hk. → networks.md: `satref`
- **Volunteer**: negligible. ~0 rtk2go HK bases; city-state geography.
- **Gap**: well-covered; SatRef VRS gives network-level accuracy across all of Hong
  Kong with a single email-registration account. No practical gap for hobbyists.

### JP — Japan

**date_added**: 2026-04-28

- **Free government RTK**: GEONET (GSI) — post-processing RINEX only; no public NTRIP.
  MIRAI / Go!GNSS (Cabinet Office SPAC, `ntrip.go.gnss.go.jp:2101`, ~300+ stations,
  free incl. commercial + automated) — raw observations. → networks.md: `mirai`
  QZSS CLAS — satellite-delivered (L6 band), not NTRIP; free, cm-level, no internet. Out of scope.
- **Volunteer**: GeoRTK (Geosense, `geortk.jp:2101`, ~41 stations, no auth, free).
  → networks.md: `geortk`; rtk2go ~24 JP bases.
- **Gap**: well-covered between MIRAI and GeoRTK. Commercial: SoftBank ichimill ¥5–8k/month.

### KR — South Korea

**date_added**: 2026-04-28

- **Free government RTK**: CORS-KOREA (NGII, `www.gnssdata.or.kr:2101`, ~90–100 stations,
  VRS + FKP) — free; sourcetable public; stream registration may require Korean national ID.
  → networks.md: `cors_korea`
- **Volunteer**: rtk2go ~3 KR bases.
- **Gap**: Korean-language portal only; international hobbyists may be blocked by national ID requirement.

### MO — Macao SAR (China)

**date_added**: 2026-05-06

- **Free government RTK**: MoSRef — Macao Satellite Positioning Reference
  Station Service (DSCC / Direcção dos Serviços de Cartografia e Cadastro,
  `mosref.dscc.gov.mo:2101`, 4 stations + 4 HK partner stations, VRS) — free;
  online registration at `mosref.dscc.gov.mo`; no professional credentials
  required; no Macao residency required. Services include single-base RTK,
  Network RTK (VRS), RINEX download (up to 3 months), and coordinate
  auto-computation. BeiDou support added 2021; NTRIP introduced 2012.
  → networks.md: `mosref`
- **Stations**: FOMO (Peninsula, 2002), COAL (Coloane, 2006), UMAC (Hengqin
  Island / UM campus, 2016), TAGR (Taipa Grande, relocated 2023). Four Hong
  Kong partner stations (HKLT, HKSL, HKMW, HKNP) extend VRS coverage across
  the Pearl River Delta.
- **Volunteer**: none. Zero rtk2go or Centipede stations in the Macao bounding
  box (~30 km² territory).
- **Gap**: well-covered; MoSRef VRS gives network-level accuracy across all of
  Macao with a free account. No practical gap for hobbyists.

### MN — Mongolia

**date_added**: 2026-04-30

- **Free government RTK**: confirmed — MonPOS / GAZAR CORS (General Office of Land
  Relations, Geodesy and Cartography, `gazar.gov.mn`), 40+ stations (Trimble
  NetR8/NetR9, built since 2011 with MCC funding). A public government announcement
  at `monpos.gazar.gov.mn/monpos/3/` (2026-04-30) confirms VRS mountpoint
  `MGL_network` at `rtk.gazar.gov.mn:2101` (alt IP `66.181.168.80:2101`) with shared
  open credentials (username `rover`, password `262461`); port 2101 is inferred, not
  stated explicitly. Individual registration available via `geodesy.gov.mn` (citizen
  or legal entity). No fee found. In pipeline as `almgg_mn` (2026-04-30). → networks.md: `almgg_mn`
- **Volunteer**: none. Zero MN stations on rtk2go or Centipede.
- **Gap**: coverage is very sparse — ~200 km average baselines nationally; RTK
  practical only in the Ulaanbaatar–Darkhan–Erdenet corridor. Hobbyists outside
  that corridor must deploy a local base station.

### SG — Singapore

**date_added**: 2026-04-29

- **Free government RTK**: none. SiReNT (Singapore Land Authority, `203.127.20.71:2101`,
  VRS network solution) — paid; SGD $107/month per receiver (~SGD $1,284/yr, ~$960/yr).
  3-day trial available (one per month) with CorpPass or SingPass login — SingPass requires
  Singapore residency (NRIC/FIN); CorpPass requires a registered Singapore entity. Non-resident
  hobbyists have no viable access path without a Singapore corporate presence. Registration at
  `app.sla.gov.sg/sirent`. → networks.md: `sirent`
- **Volunteer**: negligible (city-state). Zero SG stations on rtk2go or Centipede.
- **Gap**: SiReNT is well-engineered for a city-state (~8 reference stations) but priced and
  credentialled for professional surveyors; foreign hobbyists are effectively excluded.

### TW — Taiwan

**date_added**: 2026-04-29

- **Free government RTK**: none. e-GNSS (NLSC/Ministry of Interior, `210.241.63.193:81`, 78 stations, VBS-RTK) — paid pay-per-use; membership permit TWD 2,000/5 years (~$60), then TWD 300/receiver/day (~$9/day) for VBS-RTK. Registration via web form at `egnss.nlsc.gov.tw`. Annual-account contracts available for regular users. → networks.md: `egnss_tw`
- **Volunteer**: rtk2go ~3 TWN bases. Zero Centipede nodes.
- **Gap**: no free public RTK in Taiwan; hobbyists pay day-rate or deploy a local base and share via rtk2go.

---

## Asia Pacific — South & SE Asia

### AF — Afghanistan

**date_added**: 2026-04-28

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

**date_added**: 2026-04-29

- **Free government RTK**: SOB VRS (Survey of Bangladesh, `202.53.170.98:8011`,
  6 stations backing a VRS network) — registration required via `data.sob.gov.bd`;
  pricing not publicly listed (payment via Rocket/bKash/SureCash mobile banking).
  Stations at Dhaka, Chittagong, Rajshahi, Khulna, Maulavibazar, Rangpur, operating
  since December 2011; baselines 100–200 km across 147,570 km², inadequate for
  reliable L1+L2 RTK except near station locations. SOB lists a "GNSS fixed reference station network (CORS)
  expansion" project but expanded station count not yet confirmed.
  → networks.md: `sob_bd`
- **Volunteer**: none. Zero BD stations on rtk2go or Centipede.
- **Gap**: no practical free RTK for hobbyists; the 6-station VRS covers registration
  and pricing hurdles but its 100–200 km baselines make cm-accuracy unreliable across
  most of the country — a local base station is the only reliable workaround.

### BT — Bhutan

**date_added**: 2026-04-29

- **Free government RTK**: MiraNet / DrukNet CORS (National Land Commission —
  DoSAM, `miranet.nlcs.gov.bt`, `ntrip.druknet.net`, 13 stations, single-base)
  — paid subscription Nu 10,000/yr (~$110/yr); free for educational and
  research use with supporting documentation. Subscription requests and
  credentials managed via `miranet.nlcs.gov.bt/pre-registration/form`.
  Government agencies and Dzongkhags pay the same lump-sum rate. Network
  established 2014 (6 stations); expanded to 13 stations. Supports both
  RTK streaming and re-processed static RINEX download (daily/hourly).
  → networks.md: `miranet_bt`
- **Volunteer**: none. Zero BT stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists; nominal-fee subscription
  (~$110/yr — modest annual fee) is the practical path. Educational and
  research users qualify for free access.

### ID — Indonesia

**date_added**: 2026-04-29

- **Free government RTK**: InaCORS (BIG — Badan Informasi Geospasial, `nrtk.big.go.id:2001`,
  200+ stations declared, physical-coord-vrs) — free, registration at nrtk.big.go.id;
  public access mandated by Law No. 4/2011. Non-standard port 2001. → networks.md: `inacors`
- **Volunteer**: rtk2go ~8 ID bases (Java/Bali).
- **Gap**: InaCORS is free and legally mandated but only ~4 unique station coordinates appear
  in the sourcetable — coverage outside Java/Bali is sparse; volunteer bases fill parts of
  the gap on the most-populated islands.

### IN — India

**date_added**: 2026-05-04

- **Government RTK (paid, residency-gated)**: SoI CORS (Survey of India,
  `103.205.244.106:2101` Region 1 — UP, Uttarakhand, Haryana, Punjab, HP, NCR,
  MP, Rajasthan; `103.206.29.4:2105` Region 2 — Maharashtra, Karnataka,
  southwards; portal `cors.surveyofindia.gov.in`; 1,105+ physical stations
  with VRS overlays). Free for Central/State Government and government
  academic/research; PSU and private users pay RTK1 ₹5,900/mo (incl. 18% GST,
  ~$62/mo) up to RTK12 ₹70,800/yr (~$745/yr); DGNSS1 ₹2,360/mo (~$25/mo);
  online RINEX post-processing ₹150/GB + GST. Registration requires Aadhaar
  or PAN ID, so foreign nationals have no documented sign-up path even at
  the paid tier. Promotional free private-individual window
  (1 Nov 2025–31 Jan 2026) expired; post-promotion private rate is the paid
  RTK1 plan above. → networks.md: `soi_cors`
- **State networks**:
  - **Andhra Pradesh** — 70-station SSLR network signed an MoU with SoI on
    13 Oct 2025 to integrate into the national SoI CORS; no standalone AP
    NTRIP endpoint confirmed post-MoU. Coverage will surface under SoI CORS
    once integration completes; no separate access path.
  - **Tamil Nadu** — Department of Survey and Settlement operates 70 stations
    on rooftops of state government buildings; closed cadastral resurvey
    infrastructure for departmental staff only. No public NTRIP caster, no
    tariff, no MoU with SoI as of 2026-05-04. → networks.md: `tn_cors`
  - **Kerala** — Survey & Land Records Department signed an MoU with SoI on
    18 Jan 2021 for a VRS/NTRIP/NavIC-capable network; CORS hardware is in
    use by departmental surveyors for the Ente Bhoomi digital resurvey, but
    no public endpoint or tariff has been published. Pre-commissioning for
    external users.
- **ISRO / NavIC**: NavIC is India's regional GNSS satellite constellation,
  not a CORS or NTRIP RTK correction service; ISRO operates no NTRIP caster.
  Constellation currently degraded (NVS-02 failed orbit-raising Jan 2025;
  NVS-03/04/05 planned by Sep 2027) — out of scope here either way.
- **Commercial**: GEODNET (`rtk.geodnet.com`) carries volunteer-contributed
  India base stations sold via the GEODNET token-credit model; HYFIX
  (`hyfix.in`) is the local reseller. Trimble VRS Now and Hexagon HxGN
  SmartNet have no confirmed production NRTK coverage in India, despite
  Trimble equipment being sold widely in country. RTKdata (`rtkdata.com`)
  resells global NTRIP including India coverage from $40/mo with a 30-day
  trial.
- **Volunteer**: rtk2go ~2 IND bases (Tamil Nadu). No Centipede IND nodes.
- **Gap**: no free public RTK for hobbyists. SoI CORS is restricted to
  government/academia for free use, and the only private-user path is a paid
  subscription (~$745/yr) gated behind Aadhaar/PAN — effectively
  Indian-residents-only. State CORS networks (AP integrating into SoI; TN
  closed; Kerala pre-commissioning) add no third-party access. Foreign
  hobbyists have no documented free or paid NTRIP path into India; the
  practical fallback is a self-deployed local base.

### LK — Sri Lanka

**date_added**: 2026-04-30

- **Government RTK**: SLCORSnet (Survey Department of Sri Lanka,
  `222.165.190.67:2101`, VRS / FKP / MAC) — paid subscription; users must
  register at slcorsnet.survey.gov.lk and purchase a licence. Pricing
  confirmed publicly (no login required): 360,000 LKR/yr (~$1,127/yr);
  shorter tiers available (30,000 LKR/month, 10,000 LKR/week, 2,000 LKR/day).
  Prices stated as "including all taxes". Registration open to individuals;
  no surveying-company licence requirement stated publicly. Payment by bank
  transfer to Peoples Bank (Narahenpita); bank-transfer-only may complicate
  non-resident registration in practice. Network established 2016; Phase 1
  covers Western Province and surroundings; island-wide rollout ongoing.
  Endpoint confirmed live 2026-04-30. → networks.md: `slcorsnet`
- **Commercial**: CORSnet (CORSnet Pvt Ltd, corsnet.lk, island-wide, ~15+
  stations, VRS) — paid commercial service; pricing confirmed publicly at
  corsnet.lk/services: 345,000 LKR/yr (~$1,080/yr); shorter plans from
  2,500 LKR/day. Self-service registration open to individuals (register →
  confirm email → request connection → pay → activate). Host:port provided
  post-registration only. Established 2014; first private island-wide RTK
  network in Sri Lanka. → networks.md: `corsnet_lk`
- **Volunteer**: none. Zero LK stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists; both available networks are
  paid and expensive (~$1,100/yr). SLCORSnet endpoint confirmed live;
  CORSnet host:port disclosed post-registration only.

### MM — Myanmar

**date_added**: 2026-04-28

- **Free government RTK**: none confirmed for public access. Survey Department
  (`surveydepartment.gov.mm`) has established a fixed reference station network concept (CORS) with a
  Yangon CORS Data Center, but no public NTRIP host:port, open sourcetable,
  or registration portal has been found. The February 2021 military coup and
  subsequent civil conflict have severely degraded civilian infrastructure and
  internet access; geospatial data is treated as sensitive under military
  governance.
- **Volunteer**: none. Zero MM stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists. Survey Department CORS may exist
  internally but is not publicly accessible. No commercial NTRIP provider
  lists Myanmar coverage.

### BN — Brunei Darussalam

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Department of Survey and Mapping
  (`survey.gov.bn`) operates a national geospatial infrastructure including GNSS
  reference stations used for cadastral control; the Geoportal Ukur
  (`geoportal.survey.gov.bn`) provides map access but no public NTRIP caster
  host:port or open sourcetable has been found. No Brunei entry appears in the
  Alberding caster list or any known sourcetable archive. Brunei's small territory
  (~5,765 km²) would need only one or two stations for full RTK coverage, but no
  public streaming endpoint has been documented.
- **Volunteer**: none. Zero BN stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists. Malaysia's MyRTKnet (`myrtknet.gov.my`)
  covers Sabah and Sarawak on Borneo (~150 km from Brunei's border); its paid
  subscription is the nearest practical option, but access model and cross-border
  validity require direct confirmation with JUPEM.

### MY — Malaysia

**date_added**: 2026-04-29

- **Free government RTK**: none. MyRTKnet (JUPEM, `pxy.myrtknet.gov.my:2101` for VRS/MAC/iMAX/DGPS;
  `:2102` SB Sabah & Sarawak; `:2103` SB Peninsular, ~78 stations, VRS network solution) —
  paid; RM 1,000 one-time registration + RM 3,000/yr real-time subscription (~$855/yr at current
  rates) — expensive for a hobbyist. Mandated under the Survey Act as cost-recovery. Registration
  at `myrtknet.jupem.gov.my`. → networks.md: `myrtk`
- **Volunteer**: one MYS base on rtk2go (Malacca). Zero Centipede nodes.
- **Gap**: no free RTK in Malaysia. Hobbyists face cost-recovery pricing; the sole practical
  alternative is deploying a local base or relying on the single Malacca volunteer base on rtk2go.

### NP — Nepal

**date_added**: 2026-04-28

- **Free government RTK**: none confirmed for public/hobbyist access. Survey
  Department (Geodetic Survey Division, `dos.gov.np`) is building a fixed reference station network (CORS)
  (~4 stations established, mandate to expand to 27–50 at ~70–80 km
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

**date_added**: 2026-04-28

- **Government RTK (paid)**: PAGeNet (NAMRIA, 52 stations, `pagenet.namria.gov.ph`,
  port issued post-subscription — standard 2101 inferred). Tariff confirmed
  2026-04-30 at `pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx` (PHP, no VAT —
  regulatory charges under EO 471): PHP 1,000 (~$18) one-time registration; RTK
  per-hour PHP 100/hr (~$1.77/hr); RTK Unlimited 1 day PHP 1,000 (~$18), 5 days
  PHP 3,500, 15 days PHP 7,500, 1 month PHP 12,000 (~$212); 30/60-sec RINEX free
  with subscription. The per-hour rate (~$1.77/hr) is cheap for occasional
  use; the 1-day pass (~$18) covers a single session; the 1-month tier
  (~$212) is the longest published block — there is no annual flat rate.
  Open to individuals; non-Metro Manila clients pay by LandBank deposit slip,
  which is a practical barrier for foreign
  hobbyists. → networks.md: `pagenet`
- **Volunteer**: negligible.

### PK — Pakistan

**date_added**: 2026-04-30

- **Free government RTK**: none confirmed for hobbyists. Pak-Rehber, operated by
  SUPARCO Business Solutions (Pvt.) Ltd. (commercial arm of SUPARCO), is an NRTK
  service covering the Karachi metropolitan area only (not nationwide). The official
  brochure explicitly states "Only authorized users can use the Pak-Rehber precise
  positioning service" — authorisation process not publicly documented; no host:port,
  open registration portal, or sourcetable found publicly. SUPARCO is also deploying
  Pak-SBAS (L-band SBAS, sub-metre accuracy, satellite-delivered) — out of scope.
  → networks.md: `pak_rehber`
- **Volunteer**: none. Zero PK stations on rtk2go or Centipede.
- **Gap**: no free public RTK for hobbyists. Pak-Rehber is restricted to authorised
  users and covers Karachi only; hobbyists elsewhere in Pakistan (881,000 km²) have
  no confirmed correction source and would need to deploy a local base station.

### KH — Cambodia

**date_added**: 2026-05-06

- **Free government RTK**: Khmer GEONET (GDCG / General Department of Cadastre and
  Geography, MLMUPC) — 5 fixed reference stations (CORS) (Phnom Penh, Kandal, Kampong Speu, Siem Reap,
  Stung Treng), built with JICA technical cooperation (Aug 2021–Dec 2024); free-trial
  period extended to 2026-07-01 (khmergeonet.xyz, observed 2026-05-06); post-trial pricing
  not publicly listed (contact via khmergeonet.xyz). NTRIP host:port not publicly
  documented; Trimble Pivot software visible at `167.179.14.66:8080` but not a public
  NTRIP caster endpoint. → networks.md: `khmer_geonet` (candidate)
- **Volunteer**: none. Zero KH stations on rtk2go or Centipede.
- **Gap**: Khmer GEONET is the only identified CORS infrastructure; free trial runs to
  July 2026; post-trial pricing unconfirmed. Sparse coverage (5 stations across
  ~181,000 km²) limits RTK to areas within ~50 km of each station.

### LA — Laos

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. National Geographic Department (NGD) operates
  a geodetic reference network (Lao National Datum 1997); IGN FI (France) supplied and
  installed a fixed reference station system (CORS) for real-time positioning; ComNav delivered the first CORS
  station in 2013 (Vientiane). No public NTRIP host:port, open sourcetable, or
  registration portal found. UniqTeK (private Lao company, uniqteklao.com) operates a
  commercial CORS/RTK service — access model and pricing not publicly listed.
- **Volunteer**: none. Zero LA stations on rtk2go or Centipede.
- **Gap**: geodetic CORS infrastructure exists but no public NTRIP delivery has been found.
  Direct contact with NGD or UniqTeK is required.

### TH — Thailand

**date_added**: 2026-05-04

- **Free government RTK**: LandGNSS (Dept of Lands / กรมที่ดิน, `122.155.131.34`,
  zone-based ports, ~115–220 CORS reference stations, VRS corrections via
  `VRS_RTCM32`, free with registration) — Central zone confirmed on port 2101;
  full zone–port PDF (dol-rtknetwork.com/files/manual/1(PortNumber).pdf) currently
  404; register at dol-rtknetwork.com/index.php/register_gnss_beta; Thai-language
  portal; registration requires a Thai national ID — foreign users cannot
  self-register.
  → networks.md: `thailand_dol`
- **Volunteer**: rtk2go ~3 TH bases; sparse.
- **Gap**: full zone–port mapping unavailable (PDF link 404 as of 2026-05-04);
  foreign hobbyists effectively excluded by the Thai national ID registration
  requirement.

### VN — Vietnam

**date_added**: 2026-04-29

- **Government RTK (paid, foreigner-eligible)**: VNGEONET (National Centre for
  Satellite Positioning Station Management, `vngeonet.vn:2101` / `:2102` / `:2103`,
  IP `14.238.1.125`, 65 stations, VRS + iMAX + single-base). Paid since Sep 2024
  per Circular 47/2024/TT-BTC. 2026 schedule confirmed 2026-04-30: 750,000 VNĐ/mo
  (~$29.5), 4,280,000 VNĐ/6 mo (~$168), 6,750,000 VNĐ/yr (~$266); registration
  accepts passport scans alongside Citizen ID, so foreign nationals can register.
  **Free 12-month tier in zones with >80 km station spacing** — useful for
  hobbyists outside the densely covered river deltas. → networks.md: `vngeonet`
- **Volunteer**: negligible. Zero VN stations on rtk2go or Centipede.
- **Gap**: dense-coverage zones cost ~$30/month minimum; the free zone-spacing
  tier covers only the sparsest parts of the network.

---

## Middle East & Africa

### AE — UAE

**date_added**: 2026-05-06

- **Free government RTK**: DVRS (Dubai Municipality, 18+ stations, 4-constellation, VRS)
  — professional application only; no public hobbyist path. The DM survey sub-pages were
  returning 404 in late April 2026 but geodubai.dm.gov.ae was confirmed reachable again
  by 2026-05-06; NTRIP port 2101 status unconfirmed externally. → networks.md: `dvrs`
- **Volunteer**: negligible. Zero AE stations on rtk2go or Centipede.

### AO — Angola

**date_added**: 2026-05-06

- **Free government RTK**: none. IGCA (Instituto Geográfico e Cadastral de Angola)
  operates REPANGOL — 18 permanent CORS stations installed 2010, aligned to ITRF2008,
  maintained by TeroMovigo (last confirmed 2020). REPANGOL is a geodetic reference
  frame; no public NTRIP endpoint has ever been documented. REPANGOL's website
  (repangol.net) was offline (connection refused) as of 2026-05-06. Decreto
  Presidencial n.º 115/21 (2021) mandates IGCA to manage and expand REPANGOL but
  includes no RTK service announcement.
- **Volunteer**: none. Zero AO stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. REPANGOL infrastructure exists but is
  post-processing / geodetic-reference only with no public NTRIP delivery.

### BF — Burkina Faso

**date_added**: 2026-04-30

- **Context**: Two coups in 2022 (January and September) brought Captain Ibrahim
  Traoré to power; Burkina Faso left ECOWAS in January 2025 as a founding member
  of the Alliance of Sahel States (AES) alongside Mali and Niger. French forces
  completed withdrawal by early 2023; Wagner Group / Africa Corps has operated
  alongside Burkinabè forces since late 2023. Active jihadist insurgency (Jama'at
  Nusrat al-Islam wal-Muslimin and IS-Sahel affiliates) affects roughly 40–60% of
  national territory as of April 2026. The UK updated export licences in January
  2024 removing Burkina Faso as a permissible destination for certain controlled
  goods; no US/EU OFAC sanctions are currently in force. No change to GNSS policy
  has been announced by the transitional government, but the IGB (Institut
  Géographique du Burkina) operates under reduced bilateral technical-cooperation
  partnerships now that French/Western links are curtailed.

- **Free government RTK**: BF-CORS (IGB — Institut Géographique du Burkina,
  `igb.bf`, ~13 physical single-base stations) — free with registration.
  Nine stations established 2011 with MCA-BF (Millennium Challenge Account)
  funding (Gampela, Manga, Fada, Diapaga, Dori, Ouahigouya, Dédougou, Bobo,
  Gaoua); four capital-region stations added 2018 (Ouagadougou-IGB, Koubri,
  Dapélogo, Tanguen-Dassouri). Registration at `www.bfcors.net/RegisterAccount.aspx`;
  administrator emails credentials on approval. `bfcors.net` confirmed live
  2026-04-30 (Trimble Pivot Web portal, 13 stations on Sensor Map). Caster
  inferred at `www.bfcors.net:2101` (Trimble Pivot Web standard port; not
  curl-confirmed). → networks.md: `bfcors`

- **Volunteer**: none confirmed. Zero BF stations on rtk2go; no BF nodes on
  Centipede.

- **Gap**: BF-CORS is the confirmed free service; registration via `bfcors.net`
  is the immediate next step. Conflict and reduced bilateral cooperation create
  some uncertainty about long-term operational continuity, but the IGB technical
  service has remained running through the political transitions to date.

### BJ — Benin

**date_added**: 2026-04-29

- **Free government RTK**: IGN Bénin permanent GNSS station network (`ign.bj`) —
  seven physical single-base fixed reference stations (CORS) (Cotonou, Abomey, Savalou, Parakou,
  Natitingou, Nikki, Kandi) built with MCA-Bénin funding, each with a ~100 km
  coverage radius. Accessible via the Benin Cadastral Information System (CatIS).
  A government service registration path exists (`service-public.bj` lists
  "Fichier des stations permanentes GNSS"); NTRIP host:port not publicly listed
  on the web — disclosed after registration. → networks.md: `ign_bj`

- **Volunteer**: negligible. Zero BJ stations on rtk2go; no confirmed BJ nodes
  on Centipede.

- **Gap**: seven stations across ~115,000 km² gives ~130 km average spacing —
  adequate for L1+L2 RTK only in the south where stations are denser; northern
  coverage (Nikki, Kandi) may have gaps. Registration via IGN Bénin or
  `service-public.bj` is the access path.

### BH — Bahrain

**date_added**: 2026-04-28

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  The Survey and Land Registration Bureau (SLRB) manages geodetic
  infrastructure (Bahrain Geodetic Datum 2000 / BGD2000) and a small
  number of fixed reference stations (CORS); access restricted to licensed surveyors.
  Bahrain's entire territory is ~765 km² — a single station would
  theoretically cover it, but no public caster has been identified.
- **Volunteer**: none. Zero BH stations on rtk2go or Centipede.
- **Gap**: no free NTRIP path. KSA-CORS VRS may spill ~50 km into
  Bahrain from nearby Dammam/Al-Ahsa stations, but that service is
  Saudi-licensed. → networks.md: `ksa_cors`

### BW — Botswana

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  The Department of Surveys and Mapping (DSM, Ministry of Lands and Water
  Affairs, `gov.bw`) has built a national fixed reference station network (CORS) of ~55 stations
  (project commenced 2011, ~10 stations added per year). The network supports
  cadastral surveying and geodetic control; DSM documents describe GNSS RTK
  use from CORS as accepted practice. No public NTRIP caster host:port has been
  identified; access appears to require direct engagement with DSM.
  → networks.md: `dsm_bw`
- **Volunteer**: none. Zero BW stations on rtk2go or Centipede.
- **Gap**: no free public NTRIP for hobbyists. A 55-station CORS network
  at a country area of ~582,000 km² yields ~30–40 km average station spacing —
  adequate for L1+L2 RTK if the endpoint were publicly accessible.

### CD — DR Congo

**date_added**: 2026-04-28

- **Free government RTK**: none. Institut Géographique du Congo (IGC)
  formally responsible for geodesy; limited AFREF contributions. No
  public fixed reference station (CORS) caster found; connectivity and power constraints make
  continuous RTK streaming very unlikely near-term.
- **Volunteer**: none. Zero CD stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in DR Congo.

### CI — Côte d'Ivoire

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed publicly accessible. **RECI** (Réseau
  CORS Ivoirien), operated by BNETD-CIGN (Bureau National d'Études Techniques et
  de Développement — Centre d'Information Géographique National), comprises 5
  permanent GNSS stations plus 1 IGS-affiliated station; confirmed operational as
  of a September 2025 francophone surveyors congress presentation (Abidjan, FGF).
  No public NTRIP host:port or registration portal has been published; access appears
  institutional. Côte d'Ivoire is confirmed in the AFREF 2024 list of countries with
  at least one operational CORS installation. → networks.md: `reci_ci` (deferred)
- **Volunteer**: Centipede ~1 node (country code `CIV`). Zero rtk2go bases.
- **Gap**: RECI exists and is operational but not publicly accessible; volunteer
  Centipede node is the only free RTK option. Contact BNETD-CIGN for institutional access.

### CM — Cameroon

**date_added**: 2026-04-28

- **Free government RTK**: none. Institut National de Cartographie (INC)
  manages geodetic infrastructure; no public fixed reference station (CORS) caster found. AFREF
  contributions are raw archives, not streaming RTK.
- **Volunteer**: none. Zero CM stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Cameroon.

### CV — Cape Verde / Cabo Verde

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. INGT (Instituto Nacional de Gestão
  do Território, `ingt.gov.cv`) is the national authority for geodesy,
  cartography, and the Spatial Data Infrastructure of Cape Verde (IDE-CV);
  geodesy is a stated core mandate. No public NTRIP caster or RTK streaming
  endpoint has been identified for the archipelago. → networks.md: `ingt_cv`
- **Volunteer**: none. Zero CV stations on rtk2go or Centipede.

### CF — Central African Republic

**date_added**: 2026-04-29

- **Context**: The CAR has experienced near-continuous civil conflict since
  2012; the CPC (Coalition of Armed Groups) controls large rural areas while
  government authority is limited mainly to Bangui and a few secondary towns.
  French forces (Operation Sangaris) withdrew in 2016; Russia's Wagner Group
  (now Africa Corps) has been embedded with national forces since 2018 and
  operates gold and diamond concessions nationwide. No US/EU OFAC sanctions
  target the CAR state, but the conflict environment severely disrupts
  civilian infrastructure investment including geodetic networks.

- **Free government RTK**: none confirmed. ICASEES (Institut Centrafricain des
  Statistiques et des Études Économiques et Sociales, `icasees.org`) handles
  statistics; mapping and geodesy fall nominally under the Ministry of Town
  Planning and Housing (IGN-equivalent functions), but no national fixed reference station network (CORS)
  or public NTRIP caster has been identified. No CAR station appears in the IGS
  Network or AFREF Operational Data Centre. → networks.md: `igntc_cf`

- **Volunteer**: none. Zero CF stations on rtk2go or Centipede.

- **Gap**: no free RTK for hobbyists anywhere in the CAR. Ongoing conflict,
  severely limited power and connectivity infrastructure, and the absence of
  any identified geodetic CORS programme make a public NTRIP endpoint very
  unlikely in the near term; deploy a local base station.

### CG — Republic of the Congo (Brazzaville)

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed. CERGEC (Centre de Recherche
  Géographique et de Production Cartographique), operating under the Ministry
  of Scientific Research, is the national mapping and geodesy authority; IGN FI
  (France) has provided geomatics partnership support. In June 2024 IGN FI
  regional director Aude Areste announced in Brazzaville that IGN FI would accompany
  CERGEC in implementing geomatics projects (scope: GIS, digitisation, satellite
  location systems — no specific CORS deployment committed). No public fixed reference station (CORS)
  caster or NTRIP endpoint has been identified.
- **Volunteer**: none. Zero CG stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network or NTRIP
  caster anywhere in the Republic of the Congo.

### DJ — Djibouti

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. No national fixed reference station programme (CORS) or public
  NTRIP caster found. Djibouti's small territory (~23,000 km²) and limited
  surveying-authority capacity have not yielded any discoverable streaming RTK
  infrastructure.
- **Volunteer**: none. Zero DJ stations on rtk2go or Centipede.

### DZ — Algeria

**date_added**: 2026-05-06

- **Free government RTK**: none. Two distinct national GNSS networks exist; neither
  publishes a hobbyist-accessible NTRIP endpoint:
  - **AL-CORS-Net** (also known as **SAAP** — Système Algérien d'Aide au Positionnement)
    — 189-station Network-RTK / VRS service on a Geo++ GNSMART backend, operated by
    INCT (Institut National de Cartographie et de Télédétection), a body subordinate to
    the Ministry of National Defence. Six anchor/reference stations: Algiers (DZAL), Oran
    (DZOR), Constantine (DZCO), Ouargla (OGLA), Béchar (BECH), Tindouf (TIND).
    Published performance ~1.3 cm horizontal, ~2.2 cm vertical (1σ), ~97% VRS
    availability; an academic study confirmed live VRS sessions Oct 2021 – Jan 2022.
    No public registration portal, tariff, or NTRIP host:port has been advertised.
    → networks.md: `alcorsnet_dz`
  - **REGAT** (Réseau Géodésique de l'ATlas) — ~53-station seismotectonic monitoring
    network operated by **CRAAG** (Centre de Recherche en Astronomie, Astrophysique et
    Géophysique). Raw RINEX archive for crustal-deformation research; no real-time
    NTRIP/RTK service.
- **Volunteer**: none. Zero DZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists anywhere in Algeria. AL-CORS-Net is structurally
  unlikely to open a hobbyist path without a separate civilian mandate; REGAT is
  research infrastructure, not a correction service.

### GA — Gabon

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Agence Nationale de l'Urbanisme,
  des Travaux Topographiques et du Cadastre (ANUTTC) and the Direction Générale
  des Travaux Topographiques et du Cadastre manage geodetic and cadastral
  infrastructure; no public fixed reference station (CORS) caster or NTRIP endpoint has been found. IGN FI
  (France) has historically assisted with Gabonese geodetic projects.
- **Volunteer**: none. Zero GA stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network or NTRIP
  caster anywhere in Gabon.

### ML — Mali

**date_added**: 2026-04-29

- **Context**: Two coups (August 2020, May 2021) brought the military junta led by Assimi Goïta to power;
  Mali was suspended from ECOWAS and left ECOWAS/AES in January 2025 as founding member of the
  Alliance of Sahel States (AES) alongside Niger and Burkina Faso. Wagner Group (now Africa Corps)
  replaced French forces from late 2021; France completed military withdrawal by 2023. Active
  insurgencies across the north and centre of the country in April 2026 create severe infrastructure
  and import-logistics constraints. No public GNSS policy change has been announced under the junta.

- **Free government RTK**: none confirmed. Institut Géographique du Mali (IGM, `igm-mali.ml`)
  is the national mapping and geodesy authority; no public NTRIP caster or fixed reference station (CORS) endpoint
  discovered. IGM contributions to AFREF are raw-archive RINEX, not streaming RTK.
  → networks.md: `igm_mali`

- **Volunteer**: none. Zero ML stations on rtk2go or Centipede.

- **Gap**: no free RTK for hobbyists. Active conflict, power-grid instability, and restricted
  hardware imports (receiver duty/customs friction) make sustained streaming RTK unlikely near-term.

### TD — Chad

**date_added**: 2026-05-05

- **Context**: President Idriss Déby Itno died April 2021; his son Mahamat Idriss Déby led a
  Transitional Military Council until a managed constitutional referendum (2023) and presidential
  election (May 2024) returned him as elected president. Chad ended its 60-year defence agreement
  with France in November 2024; the last French base at N'Djamena was handed over January 2025.
  No Western sanctions apply to Chad, but the political realignment and loss of French logistical
  support reduce the bilateral geodetic-infrastructure pipeline that had underpinned recent GNSS
  survey projects.

- **Free government RTK**: none. IGN FI installed 75 geodetic monuments plus 50 orientation
  pillars and computed a geoid model for N'Djamena and surroundings under the RGT20 project
  (Réseau Géodésique du Tchad 2020; first pillar inaugurated March 2020, project completed
  February 2021), delivered to the Ministry of Land Planning, Housing and Urbanism (MATDHU).
  RGT20 is passive survey control (physical pillars + Circé software), not a streaming caster.
  No NTRIP caster host:port has been found; Chad is absent from rtk2go, corsstations.com, the
  GitHub community CORS list, SmartNet, GEODNET, and other directories checked.
  → networks.md: `chad_cors`

- **Volunteer**: none. Zero TD stations on rtk2go or Centipede.

- **Gap**: no free RTK for hobbyists. Chad has no CORS network of any kind — government,
  commercial, or community; the RGT20 deliverable is passive geodetic control, not real-time RTK.

### EG — Egypt

**date_added**: 2026-04-29

- **Free government RTK**: none. ESA CORS (Egyptian Survey Authority, `esa.gov.eg`,
  ~40 stations, single-base physical) — established January 2012, adjusted to ITRF2008
  and later ITRF2014, covering Cairo and the Nile Delta. No public NTRIP caster or
  self-service registration has been found; the network is used for government land
  administration, infrastructure projects, and subsidence/tectonic research.
  ESA also operates NACN (New Agricultural Cadastral Network, 1997), tied to the
  zero-order HARN, but again with no streaming RTK endpoint.
  → networks.md: `esa_cors_eg`
- **Volunteer**: none. Zero EG stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists anywhere in Egypt. ESA CORS covers the Nile Valley
  corridor but has never been opened as a public NTRIP service; no commercial RTK
  provider with a public endpoint has been identified.

### ET — Ethiopia

**date_added**: 2026-05-06

- **Free government RTK**: nascent. ETCORS (SSGI, `ssgi.gov.et`) — ~10 stations
  launched December 2024 in Addis Ababa and six regional cities (Bonga, Semera,
  Jigjiga, Debre Berhan, Jimma, plus Sheger/surrounds); aims for 30 stations
  within 2 years, 200 for national coverage. Intended as free public service
  ("for Ethiopia and neighboring countries") but NTRIP host:port not yet publicly
  discoverable. Deferred.
- **Volunteer**: none. Zero ET stations on rtk2go or Centipede.
- **Gap**: no confirmed public NTRIP for hobbyists. Even once the endpoint is
  published, only ~10 stations serve Ethiopia's 1.1 million km²; coverage will be
  extremely sparse outside the capital and the handful of instrumented cities for
  the foreseeable future.

### GH — Ghana

**date_added**: 2026-05-06

- **Free government RTK**: none publicly accessible. **Ghana National CORS
  Network** — Survey and Mapping Division (SMD), Lands Commission (`lc.gov.gh`),
  in PPP with GMX Systems Ghana Ltd and Geo-Tech Systems Ltd — officially unveiled
  August 19 2025 with ~60 physical stations nationwide; target 100 stations by end
  of 2025. Simultaneously launched a "digital geospatial data system" (DGDS) for
  24/7 geospatial data access. No public NTRIP host:port or registration portal has
  been published; access appears to be via licensed-surveyor channel. GSSTI (Accra)
  hosts an IGS/AFREF reference site with a free non-commercial RINEX archive.
  → networks.md: `ghana_cors`
- **Volunteer**: none. Zero GH stations on rtk2go or Centipede.
- **Gap**: CORS infrastructure now deployed nationally but no hobbyist-accessible
  NTRIP endpoint has been published. Contact SMD/Lands Commission (`info@lc.gov.gh`)
  for access enquiries.

### GM — Gambia

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Department of Lands and Surveys
  (Ministry of Lands and Regional Government) is the national geodetic authority;
  no public fixed reference station (CORS) caster or NTRIP endpoint has been found.
- **Volunteer**: none. Zero GM stations on rtk2go or Centipede.

### GN — Guinea (Conakry)

**date_added**: 2026-04-29

- **Context**: A military coup on 5 September 2021 ousted President Alpha Condé;
  Colonel Mamadi Doumbouya leads the transitional government (CNRD). ECOWAS
  suspended Guinea and imposed financial sanctions (lifted after transition
  roadmap commitments); no US/EU OFAC sanctions target the Guinean state. The
  political situation has not directly disrupted existing geodetic infrastructure,
  but reduced bilateral technical-cooperation with France (IGN FI, AFD) since the
  coup limits the pipeline for new GNSS modernisation projects.

- **Free government RTK**: none confirmed. The INC (Institut National
  Cartographique, under the Ministry of Town Planning) is the national geodesy
  and mapping authority. No public NTRIP caster or RTK streaming endpoint has
  been found; INC has not published a fixed reference station network (CORS) or caster host:port. AFREF
  contributions from Guinea are raw-archive RINEX at most. → networks.md: `inc_gn`

- **Volunteer**: none. Zero GN stations on rtk2go or Centipede.

- **Gap**: no free RTK for hobbyists. The transitional government context and
  curtailed bilateral cooperation make near-term CORS modernisation unlikely;
  deploy a local base station.

### GW — Guinea-Bissau

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The DGCF (Direcção-Geral de
  Cartografia e Fotogrametria) under the Ministry of Urban Planning and
  Construction is the principal mapping authority; no public fixed reference station network (CORS),
  NTRIP caster, or RTK streaming endpoint has been identified. LNEG (Portugal)
  produced the national geological map (1:400 000, 2014) in partnership with
  Guinea-Bissau's Directorate of Geology and Mines, suggesting geodetic
  infrastructure collaboration exists at raw-archive level only. No GW station
  appears in the IGS Network or AFREF Operational Data Centre. → networks.md: `dgcf_gw`

- **Volunteer**: none. Zero GW stations on rtk2go or Centipede.

### IL — Israel

**date_added**: 2026-04-29

- **Free government RTK**: APN (Survey of Israel, `mapigps.co.il`) — likely free for
  licensed surveyors. **Rejected from pipeline**: pervasive military GNSS spoofing
  active continuously since Oct 2023 across Israel/Lebanon/Jordan/Sinai/Cyprus (~50,000
  flights affected in 2024). RTK unreliable regardless of NTRIP access. → networks.md: `apn`
- **Volunteer**: negligible.
- **Gap**: APN may nominally exist but RTK fix quality is fundamentally unreliable due to ongoing military spoofing; no practical free option for hobbyists.

### PS — Palestinian Territories (West Bank + Gaza)

**date_added**: 2026-04-29

- **Context**: No Palestinian public NTRIP caster exists. The Palestinian Authority
  administers Areas A and B in the West Bank; Area C (~60 % of the West Bank's land
  area, including most open terrain where field surveys occur) remains under Israeli
  civil and military administration, restricting where Palestinian surveyors can deploy
  equipment without coordination. Surveying and construction in Area C requires Israeli
  Civil Administration permits that are rarely granted. Gaza's infrastructure was
  catastrophically disrupted by the 2023–2026 war, and GNSS hardware classified as
  dual-use under Israel's import regime requires case-by-case approval to enter the
  strip — a process that frequently stalls or is denied. Even in the West Bank, the
  ongoing spoofing environment (military GPS jamming/spoofing active since October 2023
  across Israel, Lebanon, Jordan, Sinai, and Cyprus) degrades RTK fix reliability
  regardless of correction source. Taken together, these factors — fragmented
  administration, a hostile electromagnetic environment, and hardware-import barriers
  in Gaza — mean that centimetre-level RTK is practically unavailable to Palestinian
  hobbyists and small shops for the foreseeable future.

- **Free government RTK**: none. No Palestinian fixed reference station network (CORS) or public NTRIP caster
  has been established. The Palestinian Authority continues to rely on the
  Palestine 1923 triangulation network for cadastral work; academic papers from Birzeit
  and An-Najah universities confirm that 3D GNSS reference frame modernisation is
  ongoing research rather than an operational infrastructure. No host:port has been
  found in any NTRIP directory, sourcetable, or public document. → networks.md: `pa_cors`

- **Israeli APN (note)**: Israel's Survey of Israel VRS (`mapigps.co.il`) physically
  covers parts of the West Bank through its base-station geometry, but access is
  restricted to licensed Israeli surveyors; Palestinian surveyors have no recognised
  path to registration. APN is separately rejected from pipeline due to spoofing.
  → networks.md: `apn`

- **Volunteer**: none. Zero PS stations on rtk2go or Centipede.

- **Gap**: no free or paid public RTK correction service is accessible to Palestinian
  hobbyists. Local base deployment is the only viable option in the West Bank (Area
  A/B), and is effectively impossible in Gaza under current conditions. PPP
  (e.g., Galileo HAS, ~40 cm) is the only realistic positioning fallback.

### JO — Jordan

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Royal Jordanian Geographic Centre
  (RJGC, `rjgc.gov.jo`) maintains geodetic reference stations and operates fixed reference station (CORS)
  infrastructure for cadastral and defence use; no public NTRIP caster or
  self-service registration portal has been found. → networks.md: `rjgc_cors`
- **Research single-base**: ACOR (American Center of Research, Amman) operates
  one GNSS NTRIP base station at its Tla' Ali campus for archaeological field
  projects (`acorjordan.org/ntrip-network/`); access by request, not a public
  service. Useful only within ~30–40 km of Amman.
- **Note**: pervasive military GNSS spoofing active continuously since Oct 2023
  across Israel/Lebanon/Jordan/Sinai/Cyprus renders RTK corrections unreliable
  across much of Jordan regardless of NTRIP source.
- **Volunteer**: none. Zero JO stations on rtk2go or Centipede.
- **Gap**: no free public NTRIP for hobbyists. Spoofing environment makes
  RTK challenging regardless of correction source.

### LB — Lebanon

**date_added**: 2026-04-29

- **Context**: Lebanon's post-2019 financial collapse (GDP roughly halved by 2024,
  banking system insolvent, triple-digit inflation through 2023) makes GNSS hardware
  imports and any ongoing fee a prohibitive barrier. The 2023–2024 Israel-Hezbollah
  war caused ~US$11 billion in infrastructure damage; reconstruction needs dwarf the
  resources available for geospatial modernisation. Government dysfunction has stalled
  any fixed reference station programme (CORS): the Directorate of Geographic Affairs (مديرية الشؤون الجغرافية,
  `lebarmy.gov.lb`) is a military directorate established 1962 for triangulation and
  aerial survey — no public NTRIP caster or self-service CORS programme has been
  announced. Pervasive military GNSS spoofing active since October 2023 across
  Israel/Lebanon/Jordan/Sinai/Cyprus renders RTK corrections unreliable across
  southern Lebanon and the Bekaa Valley regardless of correction source.

- **Free government RTK**: none. The Directorate of Geographic Affairs handles all
  national geodetic and topographic work but operates no confirmed public NTRIP caster
  or hobbyist registration portal. No host:port has been found in any NTRIP directory,
  published sourcetable, or academic reference. → networks.md: `dag_lb`

- **Volunteer**: none. Zero LB stations on rtk2go or Centipede.

- **Gap**: no free RTK for hobbyists anywhere in Lebanon. Economic collapse,
  ongoing reconstruction, and an active spoofing environment make a public CORS
  programme unlikely in the near term. Hobbyists must deploy a local base or use PPP.

### IQ — Iraq

**date_added**: 2026-04-29

- **Context**: Iraq's geodetic infrastructure was built under US military coordination
  post-2003 and handed to the State Commission on Survey under the Ministry of Water
  Resources. The Kurdistan Region (KRG) maintains a degree of administrative
  separation, including its own GIS office under the Kurdistan Region Statistics
  Office (KRSO), but no independent fixed reference station (CORS) caster has been identified for the KRG.
  US sanctions targeting Iran-aligned militias and dual-use hardware exports complicate
  procurement of survey-grade GNSS receivers for some actors, though oil-sector
  operators (the dominant precision-surveying clientele) typically obtain equipment
  through international partners. RTK spoofing in cross-border areas (Iranian border
  environs) has been documented; the June 2025 Israeli–Iranian conflict extended
  spoofing/jamming effects across southern Iraq.

- **Free government RTK**: IGRS — Iraqi Geospatial Reference System (State Commission
  on Survey / Ministry of Water Resources), 7 physical CORS at 500–800 km spacing
  (Baghdad, Basrah, Talil, Balad, Qayyarah, Al Asad + Zaxo); far too wide for RTK
  (baseline ≫ 100 km). No public NTRIP caster found; CORS data archived to IGS for
  post-processing only. → networks.md: `igrs`

- **Volunteer**: none. Zero IQ stations on rtk2go or Centipede.

- **Gap**: no usable free RTK anywhere in Iraq, including the Kurdistan Region. Station
  density is insufficient for network RTK. Hobbyists must deploy a local base or use
  PPP; oil-sector operators use private VRS infrastructure not publicly accessible.

### IR — Iran

**date_added**: 2026-05-04

- **Context**: Iran sits under comprehensive US and EU sanctions (OFAC Iran sanctions
  programme, EU Council Regulation 359/2011 and successors) that make procurement of
  Western survey-grade GNSS hardware — Trimble, Topcon, Leica, and most OEM chipsets
  — effectively impossible through normal import channels. Domestic software
  development (University of Tehran fixed reference station (CORS) processing platform, tested on the National
  Iranian South Oil Company network) is a direct response to this dependency. Iran
  operates its own GPS jamming and spoofing infrastructure, used continuously near
  sensitive military and government sites in Tehran and other cities; the June 2025
  Israeli–Iranian conflict ("12 Day War") caused a documented surge in jamming and
  spoofing across the Strait of Hormuz, Persian Gulf, and Tehran metropolitan area,
  disrupting ride-hailing apps, delivery platforms, and consumer mapping services for
  months afterwards. The internet infrastructure is heavily filtered (national intranet
  policy), and the Iranian-domain NTRIP casters listed below appear to restrict
  external access at the IP/firewall level — direct sourcetable queries from outside
  Iran time out, so endpoint details rely on Iranian practitioner documentation.

- **Government NTRIP RTK**:
  - Hoda Pro (سامانه ملی هدی پرو, `hodapro.ncc.gov.ir:2101`) — RTK / Network-RTK
    service from the National Cartographic Center, riding on the IPGN station
    infrastructure. Paid subscription via `eshop.ncc.gov.ir` (rates not publicly
    listed; the subscription portal is unreachable from outside Iran). Sign-up
    requires Iranian national ID and Iranian banking. The legacy `hoda.ncc.gov.ir`
    caster is DGPS-only and out of project scope. → networks.md: `hodapro_ir`
  - SHAMIM (سامانه شمیم, شبکه موقعیت‌یابی یکپارچه مالکیت‌ها; `178.252.173.15:2101`,
    SHAMIM Plus at `178.252.173.75:2101`) — 144-station VRS/NRTK network on a Geo++
    GNSMART backend, operated by the Organisation for Registration of Deeds and
    Properties for the national cadastre programme. No subscription fee, but
    registration is documented only for cadastre-licensed surveyors with an Iranian
    national ID, Iranian mobile, and a registered GNSS receiver serial. No documented
    path for unaffiliated hobbyists. → networks.md: `shamim_ir`

- **Other government networks**:
  - IPGN — Iranian Permanent GPS Network for Geodynamics (`ipgn.ncc.gov.ir`,
    National Cartographic Center), ~127 physical CORS built post-2003 Bam earthquake
    for tectonic monitoring, velocity, and strain-field estimation; raw RINEX archived
    to IGS for post-processing. IPGN itself does not run a public NTRIP RTK caster —
    NCC's real-time arm is Hoda Pro above. → networks.md: `ipgn`
  - SEMT (سمت) — a third Iranian RTK correction service named alongside SHAMIM and
    Hoda Pro in practitioner material; operator, endpoint, and access terms not yet
    investigated. **investigate**

- **Volunteer**: none. Zero IR stations on rtk2go or Centipede.

- **Gap**: no documented free or affordable hobbyist path. Hoda Pro is paid and
  payment-gated to Iranian banking; SHAMIM is no-fee but cadastre-licensed-only;
  foreign hobbyists or residents have no registration path on either. Western
  hardware embargoes and persistent GPS jamming/spoofing make on-the-ground RTK
  unreliable regardless of correction availability. Practical fallback is PPP
  or a self-deployed local base with domestically-procurable hardware.

### SY — Syria

**date_added**: 2026-04-29

- **Context**: Syria's geodetic infrastructure was severely disrupted by 13 years of civil
  war (2011–2024). The Assad regime fell in December 2024 and a transitional government was
  formed in March 2025. US sanctions were largely lifted by OFAC General Licence 25
  (May 2025) and a further Executive Order (June 2025); EU and UK sanctions were eased in
  parallel, though some export restrictions on dual-use equipment remain. Pre-war, a handful
  of research-grade GNSS stations existed (Damascus, Aleppo universities; Syrian Geological
  Survey), but no public NTRIP caster was ever deployed. Reconstruction of basic geospatial
  infrastructure has not yet reached real-time GNSS streaming. Military GNSS spoofing active
  in the wider region (Israel/Lebanon/Sinai since Oct 2023) reaches into southern and western
  Syria, further complicating practical RTK use even if corrections were available.

- **Free government RTK**: none. The General Establishment for Survey (المؤسسة العامة
  للمساحة, the national mapping authority) has no confirmed public NTRIP caster or
  self-service registration portal. No host:port has been found in any directory, sourcetable,
  or academic reference. → networks.md: `ges_syria`

- **Volunteer**: none. Zero SY stations on rtk2go or Centipede.

- **Gap**: no free RTK for hobbyists. Reconstruction of geodetic infrastructure is a
  long-term post-conflict priority; a public NTRIP caster is unlikely before the national
  reference frame and basic fixed reference station (CORS) deployment are re-established. Revisit once international
  geodetic cooperation with the transitional government is confirmed (e.g. EUREF or IGS
  station affiliation).

### KE — Kenya

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed with a public NTRIP endpoint. Survey
  of Kenya (SoK, `survey.go.ke`) operates national geodetic control (~20 Tier-3
  CORS for the KENREF geodetic reference frame); no public NTRIP caster or RTK
  streaming host:port has been found. RCMRD (`rcmrd.org`) hosts geodetic research
  infrastructure but no public RTK stream. → networks.md: `sok_ke`
- **Commercial**: Muya CORS (`muya-cors.com`), operated by Measurement Systems
  Ltd (25+ stations, single-base + network RTK, GPS/GLONASS/BeiDou/Galileo) —
  self-serve signup; flexible tiers (hourly/daily/monthly); pricing not publicly
  listed (contact via `muya-cors.com`). Confirmed in active field use Feb 2025
  (Orbital Africa case study, Kitisuru, Nairobi). → networks.md: `muya_cors_ke`
- **Announced**: Kenya Power 15-station CORS network announced Apr 2025 (targeting
  "professionals engaged in precise land and engineering surveys" under IESR);
  undergoing gazettement submission; no live NTRIP stream confirmed.
- **Volunteer**: rtk2go 1 base (Kenya). No Centipede nodes.
- **Gap**: no free government or volunteer RTK coverage at national scale.
  Hobbyists must use Muya CORS (pricing on inquiry) or deploy a local base.

### LR — Liberia

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Liberia Land Authority (LLA,
  `lla.gov.lr`) is the national land administration body; no public fixed reference station (CORS) caster
  or NTRIP endpoint has been found.
- **Volunteer**: none. Zero LR stations on rtk2go or Centipede.

### LS — Lesotho

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Department of Lands, Surveys and
  Physical Planning (Ministry of Local Government, Chieftainship, Home Affairs
  and Police) is the national geodetic authority; no public fixed reference station (CORS) caster or NTRIP
  endpoint has been found.
- **Volunteer**: none. Zero LS stations on rtk2go or Centipede.
- **Gap**: no free RTK within Lesotho, but the country is entirely enclaved
  by South Africa. TrigNet (`trignet.co.za:2101`, free) has stations ringing
  Lesotho — Bloemfontein, Bethlehem, and the eastern Highlands corridor — at
  roughly 100–200 km spacing. Stations within ~30–40 km of the Maseru and
  north-eastern border zones may provide usable single-base RTK baselines for
  hobbyists already inside South Africa. TrigNet is not a Lesotho service and
  cross-border coverage is incidental. → networks.md: `trignet`

### KW — Kuwait

**date_added**: 2026-04-28

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  PACI and Kuwait Municipality operate GNSS reference stations for
  cadastral/infrastructure use (Kuwait Geodetic Network / KGN); streams
  issued only to licensed surveying firms under municipal contract —
  no public caster host:port identified.
- **Volunteer**: none. Zero KW stations on rtk2go or Centipede.
- **Gap**: no free NTRIP path. Kuwait is small (~17,800 km²) and flat;
  a modest fixed reference station network (CORS) would suffice for national RTK if opened, but
  no open-access mandate exists.

### LY — Libya

**date_added**: 2026-04-29

- **Context**: Libya has had no unified functioning government since 2014.
  Two rival administrations — the GNU (Tripoli, UN-recognised) and the GNS
  backed by the House of Representatives and Haftar's LNA (Benghazi/East) —
  each control separate civil institutions. UN Security Council sanctions and
  asset-freeze frameworks remain active (UNSCR 1970 and successor resolutions).
  Hardware imports (surveying equipment, GNSS receivers) require navigating
  dual-administration customs and sanctions compliance, making sustained
  national fixed reference station (CORS) infrastructure deployment effectively impossible under current
  conditions.

- **Free government RTK**: none. The Libyan Survey Authority (الهيئة العامة
  للمساحة, al-Hay'a al-ʿĀmma lil-Masāḥa) is the nominal national mapping
  body but no public NTRIP caster or RTK streaming endpoint has been
  identified from either Tripoli- or Benghazi-administered institutions.
  Libya participates in NAFREF (North Africa Reference Frame, part of AFREF)
  in principle; no AFREF-contributing permanent station with a public NTRIP
  stream is known to be operational. No network named LIBPOS or similar
  appears in any public CORS registry. host:port not publicly listed.
  → networks.md: `libpos_ly`

- **Volunteer**: none. Zero LY stations on rtk2go or Centipede.

- **Gap**: no free RTK for hobbyists anywhere in Libya. Both conflict and
  the structural absence of a functioning central geodetic administration
  make near-term change unlikely; deploy a local base station. The situation
  mirrors Sudan (SD) — do not wait for a public endpoint.

### MA — Morocco

**date_added**: 2026-05-06

- **Government RTK (registration required)**: ANCFCC (Agence Nationale de la
  Conservation Foncière, du Cadastre et de la Cartographie, `ancfcc.gov.ma`)
  operates a 60-station permanent GNSS network with nodes at Laayoune and Dakhla
  in the MA-administered southern provinces. The ANCFCC page
  (ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/) explicitly describes
  real-time RTK and RTK-Network corrections delivered via internet (NTRIP protocol);
  host:port not published — registration at ancfcc.gov.ma required; tariff not
  public. Licensed professional access; hobbyist eligibility unclear.
  → networks.md: `ancfcc`
- **Commercial**: itri (SAMTOP, `itri-gnss.ma`), Morocco's first private permanent
  GNSS network (launched 2020) — 231 stations nationwide; single-base RTK, network
  RTK, and VRS modes; GPS+GLONASS+Galileo+BeiDou. Registration at
  `secure.itri-gnss.ma/admin/auth/register`; professional subscription, pricing
  not public. → networks.md: `itri_ma`
- **Volunteer**: rtk2go ~2 bases (MAR).
- **Gap**: no free coordinated RTK coverage. Both ANCFCC and itri require
  registration and professional subscriptions. Single volunteer base(s) only.
- **Western Sahara (EH)**: the MA-administered territory (≈80% of Western
  Sahara, including Laayoune and Dakhla) falls within the ANCFCC network's
  nominal coverage — physical stations are confirmed in both cities. The SADR /
  Polisario-controlled "Free Zone" (eastern desert, ≈20%) has no known geodetic
  infrastructure, no public NTRIP caster, and no MINURSO geodetic programme.
  Zero EH stations appear on rtk2go or Centipede. No separate EH entry is
  warranted given the disputed status and absence of independent coverage.

### MR — Mauritania

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The DATU (Direction des Affaires
  Topographiques et de l'Urbanisme, under the Ministry of Housing and Urbanism)
  is the nominal authority for geodesy and cadastre in Mauritania; no public
  NTRIP caster or RTK streaming endpoint has been found. Mauritania's territory
  is ~1,031,000 km², mostly Saharan desert — extremely sparse infrastructure
  makes a nationwide fixed reference station network (CORS) a very long-term prospect. AFREF contributions
  from Mauritania, if any, are raw-archive RINEX only. → networks.md: `datu_mr`

- **Volunteer**: none. Zero MR stations on rtk2go or Centipede.

- **Gap**: no free RTK for hobbyists. Geography and infrastructure constraints
  are the primary barrier; no CORS programme has been identified. Deploy a local
  base station.

### MG — Madagascar

**date_added**: 2026-05-05

- **Free government RTK**: none. FTM (Foiben-Taosarintanin'i Madagasikara —
  Institut Géographique et Hydrographique, `ftm.mg`) is the national mapping
  authority responsible for geodesy and is mandated to maintain the national
  geodetic and levelling network compatible with AFREF/ITRF. One IGS station
  exists (ABPO00MDG, Ambohimpanompo near Antananarivo; Septentrio PolaRx5,
  installed 2007), operated locally by the University of Antananarivo
  Institute of Geophysics with data archived to UNAVCO/EarthScope and IGS;
  this is a raw-observation archive station, not an RTK streaming caster.
  No public NTRIP caster or RTK streaming endpoint from FTM has been found,
  and Madagascar is absent from SmartNet, Polaris, GEODNET, and onocoy
  directories. → networks.md: `ftm_mg`
- **Volunteer**: none. Zero MG stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists in Madagascar. The IGS archive station
  provides RINEX data for scientific use only; hobbyist RTK requires
  deploying a local base.

### MU — Mauritius

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed with a public NTRIP endpoint. The
  Survey Division of the Ministry of Housing and Land Use Planning is the
  national mapping and geodesy authority. A 2016 RCMRD-facilitated feasibility
  workshop examined establishing a fixed reference station network (CORS); no operational public caster
  has been confirmed since. → networks.md: `survey_mu`
- **Volunteer**: none. Zero MU stations on rtk2go or Centipede.

### MW — Malawi

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  The Department of Surveys (Ministry of Lands, `lands.gov.mw`) operates a
  Geodetic and Topographic Survey Section and established at least one AFREF fixed reference station (CORS)
  at Lilongwe (Capitol Hill) contributing RINEX archives to UNAVCO; no
  public NTRIP caster or RTK streaming host:port has been found.
- **Volunteer**: none. Zero MW stations on rtk2go or Centipede.

### MZ — Mozambique

**date_added**: 2026-04-29

- **Free government RTK**: none. CENACARTA (Centro Nacional de Cartografia e
  Teledetecção, `cenacarta.gov.mz`, under Ministry of Agriculture) operates
  ~8 fixed reference stations (CORS) (CHMO, MPTB, QLMN, NACL, LCNG, XXAI, MTND, SOFL) listed
  in the Corsmap/AFREF continental dataset; no public NTRIP caster or RTK
  streaming host:port has been found. DINAGECA (Direcção Nacional de
  Geografia e Cadastro, under Ministry of Land and Environment) handles
  cadastral geodesy; no independent NTRIP caster confirmed.
  → networks.md: `cenacarta_mz`
- **Volunteer**: none. Zero MZ stations on rtk2go or Centipede. Four TrigNet ZA
  stations near the Limpopo border (Nspt, Pbwa, Sprt, Tdou) are in pipeline via
  TrigNet and provide incidental single-base RTK coverage in southern Mozambique
  (Gaza/Maputo provinces) — not a Mozambique service. → networks.md: `trignet`
- **Gap**: no free RTK within Mozambique proper. Hobbyists in the southernmost
  provinces (Gaza, Maputo) may reach TrigNet stations across the South Africa
  border at up to ~100–150 km; all other regions must deploy a local base.

### NA — Namibia

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  The Surveyor General's Department (SGDN, Ministry of Agriculture, Water
  and Land Reform) is responsible for geodetic control and the national
  geodetic reference network; it uses GNSS survey methods for first-order
  control and urban-scale densification. One IGS research station operates
  in Windhoek (WIND00NAM, HartRAO data centre) for scientific archiving —
  not an RTK streaming caster. No public NTRIP caster host:port has been
  found in any directory, sourcetable, or academic reference.
  → networks.md: `sgdn_na`
- **Volunteer**: none. Zero NA stations on rtk2go or Centipede.
- **Gap**: no free public NTRIP for hobbyists. Namibia's ~824,000 km²
  and sparse population make full national fixed reference station (CORS) coverage a long-term
  infrastructure project; hobbyists must deploy a local base.

### NE — Niger

**date_added**: 2026-04-28

- **Free government RTK**: none. Institut Géographique National du
  Niger (IGNN) is responsible for geodesy; sparse IGS-affiliated
  research stations only — no public NTRIP delivery. Saharan geography
  and infrastructure constraints make a sustained physical RTK network
  very difficult.
- **Volunteer**: none. Zero NE stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public fixed reference station network (CORS)
  or NTRIP caster anywhere in Niger.

### NG — Nigeria

**date_added**: 2026-05-01

- **Free government RTK**: none with a working public caster. NIGNET (Office of the Surveyor
  General of the Federation — OSGoF, 15 stations at 500–1,000 km spacing) was designed for
  geodetic reference frame maintenance (AFREF), not RTK corrections; inter-station spacing is
  far too wide for reliable network RTK. A research prototype NTRIP caster was implemented on
  the network (with PayPal payment integration); `gnssnigeria.com`, the apparent subscriber
  portal, is unreachable as of 2026-05-01 — no stable public endpoint confirmed.
  → networks.md: `nignet`
- **Volunteer**: negligible. Zero NG stations on rtk2go or Centipede.
- **Gap**: no free public RTK in Nigeria. Fixed reference station (CORS) infrastructure exists but serves geodetic
  purposes at unsuitable spacing; hobbyists must deploy a local base station.

### OM — Oman

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  OmanCORSnet (47 stations, Leica GNSS Spider / Spider Business Center),
  operated by NSGIA — National Survey and Geospatial Information Authority
  (successor to NSA, under Ministry of Defence); portal at
  `omancorsnet.gov.om`; NTRIP host:port issued post-registration only.
  Datum: ONGD17 (Oman National Geodetic Datum 2017, ITRF2014 epoch 2017.0).
  No hobbyist or open-registration tier documented; service targets licensed
  surveyors and government users. IGS station MUSK (Muscat) streams raw GNSS
  observations via EarthScope/IGS-IP — not an RTK service. → networks.md: `omancorsnet`
- **Volunteer**: none. Zero OM stations on rtk2go or Centipede.
- **Gap**: no free NTRIP path for hobbyists. OmanCORSnet's 47 stations cover
  Oman's ~309,500 km² at professional-tier access only; no public endpoint or
  individual registration path has been documented.

### QA — Qatar

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed with a public NTRIP endpoint.
  QCORS — Qatar Continuously Operating Reference Stations (9 stations,
  established 2009–2010, ±2 cm horizontal accuracy) — operated by CGIS
  (Centre for GIS, Ministry of Municipality); portal at `gisqatar.org.qa`;
  NTRIP host:port issued post-subscription only. No public self-registration
  page or hobbyist tier identified; service described as for "government and
  private survey and mapping communities." Datum: QNSRS / QND95.
  → networks.md: `qcors`
- **Volunteer**: none. Zero QA stations on rtk2go or Centipede.
- **Gap**: no free NTRIP path for hobbyists. Qatar's small territory
  (~11,600 km²) makes QCORS sufficient for national coverage but access is
  subscription-gated with no confirmed individual tier.

### SA — Saudi Arabia

**date_added**: 2026-04-28

- **Free government RTK**: KSA-CORS (GASGI/GEOSA, `ksacors.geoportal.sa:2101`, 209
  stations, VRS) — free, register via ksacors.geoportal.sa. → networks.md: `ksa_cors`
- **Volunteer**: negligible.
- **Gap**: KSA-CORS VRS (0 physical pins); currently timing out in CI; NRTK polygon deferred.

### SD — Sudan

**date_added**: 2026-04-28

- **Free government RTK**: none. Sudan Survey Authority (SSA) planned a GNSS fixed reference station network (CORS)
  as part of AFREF participation (55 station sites identified) but no
  operational public caster has been found. Ongoing armed conflict (April 2023–)
  severely disrupts civil infrastructure; status unknown.
- **Volunteer**: none. Zero SD stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. Do not pursue until conflict ends and
  infrastructure is confirmed operational.

### SL — Sierra Leone

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Directorate of Surveys and Lands
  (Ministry of Lands, Housing and Country Planning, `molhcp.gov.sl`) aims to
  implement a standardised national coordinate system and improve geodetic
  infrastructure; no public fixed reference station (CORS) caster or NTRIP endpoint has been found.
- **Volunteer**: none. Zero SL stations on rtk2go or Centipede.

### SN — Senegal

**date_added**: 2026-05-06

- **Government RTK (paid, tariff not public)**: SENCORS (ANAT — Agence Nationale
  de l'Aménagement du Territoire / DTGC, `caster.geodesie.sn:2101`, Leica Spider
  Business Center). Network built 2022–2024 via World Bank PROCASEF (16 CORS
  stations) plus 5 JICA stations integrated 2025; total ~21 stations nationwide.
  Portal at `geodesie.sn`. Caster went offline January 2026 (disk failure) and was
  restored March 16, 2026. Subscription plan described as 90-day flat-rate; pricing
  not publicly disclosed without account login — contact ANAT (`anat.sn`).
  Registration form requires username/name/email/company; no stated residency
  restriction. → networks.md: `sen_cors`
- **Volunteer**: rtk2go ~1 SN base; Centipede ~2 SN nodes.
- **Gap**: SENCORS is operational since March 2026 but tariff is not publicly
  listed; Centipede nodes remain the only confirmed free option.

### SZ — Eswatini (formerly Swaziland)

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Surveyor General's Department
  (Ministry of Natural Resources, `gov.sz`) maintains the national survey control
  and trigonometric network; no public fixed reference station (CORS) caster or NTRIP endpoint has been
  found.
- **Volunteer**: none. Zero SZ stations on rtk2go or Centipede.

### TG — Togo

**date_added**: 2026-05-01

- **Free government RTK**: Togo CORS (IGNTOGO — formerly DGIGC, Direction
  Générale de l'Information Géographique et de la Cartographie, renamed
  February 2026; Ministry of Town Planning and Urban Development,
  `urbanisme.gouv.tg`) — 614 geodetic benchmarks and a fixed reference
  station network (CORS) of continuously operating stations deployed since
  2017. A March 2026 interministerial communiqué mandates that all
  topographic, cadastral, urbanism, and infrastructure work be attached to
  the National Geodetic Network (réseau géodésique national); a three-month
  compliance period was granted. NTRIP host:port not publicly listed;
  `igntogo.tg` unreachable as of 2026-05-01 — access via IGNTOGO /
  `urbanisme.gouv.tg`. → networks.md: `dgigc_tg`

- **Volunteer**: none. Zero TG stations on rtk2go or Centipede.

- **Gap**: CORS network confirmed operational (March 2026 communiqué) and
  official reference for all professional work as of 2026; NTRIP endpoint
  not publicly discoverable — contact IGNTOGO via `urbanisme.gouv.tg` for
  credentials.

### TR — Turkey

**date_added**: 2026-04-29

- **Government RTK (paid, residency-gated)**: TUSAGA-Aktif / CORS-TR (TKGM —
  General Directorate of Land Registry and Cadastre, jointly with HGM — General
  Directorate of Mapping, `212.156.70.42:2101`, ~158 physical GNSS stations,
  single-base). 2026 schedule (KDV included, confirmed 2026-04-30): one-off
  device registration ₺550 (~$17); RTK 1 mo ₺1,000 (~$30), 6 mo ₺6,000 (~$182),
  1 yr ₺8,135 (~$247); DGPS 1 yr ₺2,985 (~$91); 30-sec RINEX free, 1-sec
  ₺4/session. Online registration requires a TC Kimlik No (Turkish national
  ID) — foreign nationals without Turkish residency cannot self-register.
  Universities and vocational schools may apply for free educational-area RTK
  access via TKGM. → networks.md: `tusaga`
- **Volunteer**: rtk2go ~3 TR bases; Centipede — none. Zero TUR nodes confirmed.
- **Gap**: no free public NTRIP. The annual RTK tier costs ~$247 and the
  6-month block ~$182, so picking one or the other depends on whether half a
  year of fieldwork is enough. Foreign visitors without a Turkish national ID
  must contact the agency directly or deploy a local base.

## Caucasus

### AZ — Azerbaijan

**date_added**: 2026-04-30

- **Free government RTK**: none. AzPOS — Azerbaijan Positioning Observation System
  (State Service on Property Issues / Əmlak Məsələləri Dövlət Xidməti,
  `emlak.gov.az`) — 45 physical fixed reference stations (CORS) at 30–40 km
  spacing (GPS + GLONASS + Galileo + BeiDou); original 37 stations plus 8
  restored in Karabakh region in 2024 (Fuzuli, Jebrail, Zangilan, Kəlbəcər ×2,
  Ağdam, Şuşa, Laçın). Backend is Leica GNSS Spider (VRS capable). Caster
  provisionally at `azpos.az:2101` (authentication-gated; no public sourcetable
  to unauthenticated queries). Access requires a signed bilateral service
  agreement; "legal entities and individuals" may apply per the operator's
  contact page, but there is no self-service web registration and the process is
  conducted entirely in Azerbaijani. No published tariff.
  → networks.md: `azpos`
- **Volunteer**: none. Zero AZ stations on rtk2go or Centipede.
- **Gap**: no free or self-service RTK for hobbyists. AzPOS is accessible in
  principle to individuals but requires a bilateral contract with a government
  office in Baku — effectively restricted for most visitors. Deploy a local base
  station for centimetre-level work.

### AM — Armenia

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed publicly accessible. ARMPOS —
  Armenian Continuously Operating Reference Station network (State Committee
  for Real Property Cadastre / Անշարժ Գույքի Կադաստրի Պետական Կոմիտե,
  `cadastre.am`), 12 physical single-base stations covering the full territory,
  commissioned by Leica Geosystems in 2013 with Norwegian Mapping Authority
  funding. Capable of real-time NTRIP RTK and RINEX post-processing; uses
  coordinate reference system ARMREF02. Access restricted to licensed surveyors
  and government cadastre users — no open self-service registration found. Host:port
  not publicly listed. → networks.md: `armpos`
- **Volunteer**: none. Zero AM stations on rtk2go or Centipede.
- **Gap**: no free public NTRIP. 12 stations across ~30,000 km² is adequate
  spacing (~50 km apart) for L1+L2 RTK if access were open; hobbyists must
  deploy a local base.

### GE — Georgia

**date_added**: 2026-05-06

- **Free government RTK**: GeoCors (National Agency of Public Registry / NAPR,
  Ministry of Justice, `geocors.napr.gov.ge:2101`) — 26 physical single-base fixed reference stations (CORS)
  established since 2011 (7 Class A forming the national geodetic frame +
  expanded Class B coverage); Leica Spider Business Center platform.
  Self-service web registration available at `geocors.napr.gov.ge/SBC/Account/Register`.
  Access is paid — pricing not listed on the public website (contact NAPR; service
  is intended for licensed surveyors and cadastre users). → networks.md: `geocors_ge`
- **Volunteer**: none. Zero GE stations on rtk2go or Centipede.
- **Gap**: paid government NTRIP with no hobbyist tier identified; pricing not
  publicly discoverable. The 2024–2025 Georgian political crisis does not appear
  to have disrupted the GeoCors technical service. Deploy a local base for
  hobbyist use.

### TN — Tunisia

**date_added**: 2026-05-06

- **Free government RTK**: none. OTC (Office de la Topographie et du Cadastre,
  `otc.nat.tn`) operates 23 permanent GNSS stations nationwide (3 installed 2005; 20
  added 2010; fully operational since 2011; Saharan region excluded). Network linked
  to ITRF2000/WGS84. RTK corrections via paid NTRIP subscription; host:port not
  publicly listed (disclosed on subscription). → networks.md: `otc_gnss`
- **Volunteer**: none. Zero TN stations confirmed on rtk2go or Centipede.
- **Paid only**: OTC GNSS — 6,000 TND/yr annual subscription; shorter durations from
  60 TND/day to 3,600 TND/6 months; VAT status not stated on the public subscription
  page; subscribe at otc.nat.tn/geodesy/gnss/subscription. No explicit eligibility
  restriction. Coverage gap: stations do not extend into the Saharan south (roughly
  south of Gafsa/Tozeur latitude).

### TZ — Tanzania

**date_added**: 2026-04-29

- **Free government RTK**: none. Survey and Mapping Division / Tanzania National
  Geo-innovation Centre (TNGC, `tngc.lands.go.tz`, under Ministry of Lands,
  Housing and Human Settlements) operates national geodetic control and
  capacity-building in geospatial technologies; no public NTRIP caster or RTK
  streaming host:port has been found. AFREF/IGS contributions are raw-observation
  archives, not RTK streaming. → networks.md: `tngc_tz`
- **Volunteer**: none. Zero TZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists anywhere in Tanzania; deploy a local base.

### UG — Uganda

**date_added**: 2026-05-02

- **Free government RTK**: UGRF CORS (Ministry of Lands, Housing & Urban
  Development) — 78 stations (40 government + 38 private), VRS and single-base.
  Free with registration; endpoint `ugrf.mlhud.go.ug:2101`, sourcetable publicly
  accessible (curl-confirmed 2026-05-02). Single-base mountpoints: ENTB, GULU,
  SRTI, MBRA, Nearest (auto-select). Network-RTK mountpoints: I-Max, VRS.
  Register at `ugrf.mlhud.go.ug/SBC` (Leica Spider Business Centre portal).
  Now in pipeline.
- **Volunteer**: 1 AUSCORS station (MBAR00UGA0, Mbarara) via EarthScope/AUSCORS;
  raw observations under non-commercial NULA — functional for RTK within range.
- **Commercial**: EagleCORS (`eaglecors.com`) — separate commercial service, out of scope.

### BI — Burundi

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed with a public NTRIP endpoint. IGEBU
  (Institut Géographique du Burundi, `igebu.bi`) is the national mapping agency
  responsible for geodesy, cartography, and hydro-meteorology. IGEBU received
  GNSS equipment and coordinate-transformation training under a JICA-supported
  project (technology transfer completed 2010). No public fixed reference station network (CORS) or NTRIP
  caster endpoint has been found; no BI station appears in the AFREF Operational
  Data Centre. National datum is still Arc 1960 (Clarke 1880 ellipsoid) — the geodetic
  reference frame has not been modernised to a GNSS-based system. → networks.md: `igebu_bi`
- **Volunteer**: none. Zero BI stations on rtk2go or Centipede.
- **Gap**: no free RTK available in Burundi. An RCMRD AFREF capacity-building workshop
  (August 2024) included Burundi but announced no operational caster. Hobbyists must
  deploy a local base or accept GNSS autonomous accuracy.

### RW — Rwanda

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed with a public NTRIP endpoint. The
  Rwanda Geodetic Network (RGN) is a network of ~10 fixed reference stations (CORS) managed by RLMUA
  (Rwanda Land Management and Use Authority, `lands.rw`). RLMUA states that RGN
  "analyses and distributes data free of charge", but the available public
  documentation describes post-processed RINEX distribution only; no NTRIP
  caster host:port has been found in any public directory or sourcetable.
  → networks.md: `rgn_rw`
- **Volunteer**: none. Zero RW stations on rtk2go or Centipede.
- **Gap**: no real-time free RTK for hobbyists despite an operational CORS
  network. If RLMUA adds an NTRIP streaming endpoint it could qualify as a
  free in-pipeline source; revisit once a host:port is publicly listed on
  `lands.rw`.

### YE — Yemen

**date_added**: 2026-04-28

- **Free government RTK**: none. General Survey Authority (GAS) operated a small
  fixed reference station network (CORS) pre-conflict; civil war since 2015 has severely disrupted all
  public infrastructure. No functioning public NTRIP caster is known.
- **Volunteer**: rtk2go 1 base — `s9123A22404` at Sanaa (15.29°N, 44.24°E),
  RTCM 3.2, GPS + BDS dual-frequency. Single independent hobbyist installation;
  connectivity and uptime unreliable given ongoing conflict.
- **Gap**: effectively no RTK coverage for hobbyists. The single rtk2go station
  provides a ~50–70 km useful radius under good conditions but cannot be relied
  upon. Note for map completeness only; recommending RTK activity in Yemen is
  not appropriate given the conflict context.

### ZA — South Africa

**date_added**: 2026-04-29

- **Free government RTK**: TrigNet (NGI/DALRRD, `trignet.co.za:2101`, ~72 stations,
  single-base + Network RTK in Gauteng / Western Cape / KwaZulu-Natal clusters) —
  all NGI products free; web registration at trignet.co.za. → networks.md: `trignet`
- **Volunteer**: rtk2go ~1 ZA base, Centipede ~1 ZA node.
- **Gap**: TrigNet provides free nationwide single-base RTK (~5 cm within 30–40 km);
  Network RTK (~3 cm) only in the three metro clusters; rural areas rely on
  single-base geometry.

### ZM — Zambia

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. The Zambia Survey Department (Ministry of
  Lands and Natural Resources) participates in AFREF/SAFREF continental reference
  framework; fixed reference stations (CORS) contribute raw-observation RINEX archives to the IGS
  regional data centre at HartRAO — no public NTRIP streaming endpoint found.
- **Volunteer**: none. Zero ZM stations on rtk2go or Centipede.

### ZW — Zimbabwe

**date_added**: 2026-04-29

- **Free government RTK**: none free confirmed. ZINGSA (Zimbabwe National Geospatial
  and Space Agency, `zingsa.ac.zw`) operates a national fixed reference station network (CORS) covering the
  country, used for surveying, precision agriculture, and ionospheric monitoring.
  The Surveyor General's Office also administers CORS services under the Land Survey
  Act; S.I. 47 of 2023 prescribes fees for CORS access, indicating a paid model.
  Host:port not publicly listed; access appears to require contact with ZINGSA or the
  Surveyor General's Office. → networks.md: `zingsa_cors`
- **Volunteer**: none. Zero ZW stations on rtk2go or Centipede.
- **Gap**: no free public NTRIP for hobbyists. US Zimbabwe sanctions programme
  terminated March 2024; no sanctions barrier to hardware import. Paid CORS access
  only, with pricing not on public website.

---

## Central Asia

### KZ — Kazakhstan

**date_added**: 2026-04-30

- **Free government RTK**: none. The national RTK service is operated by
  НЦГПИ (National Centre of Geodesy and Spatial Information, qazgeodesy.kz),
  formerly branded KazGeoDesy / Казгеодезия, under the Committee of Geodesy
  and Cartography. A self-service portal at rtk.qgeo.kz offers paid
  subscriptions to individuals and organisations: 65,000 ₸/yr (~$141/yr)
  annual, or 7,000 ₸/month. Each subscription covers up to 5 reference
  stations and 5 simultaneous rover connections. Registration requires a
  Kazakh individual or business identifier (ИИН or БИН), which is a
  de-facto residency requirement — foreign users cannot complete self-service
  registration. Host:port not publicly disclosed; likely rtk.qgeo.kz:2101
  (unconfirmed). Portal confirmed live 2026-04-30.
  → networks.md: `kazgeodesy`
- **Volunteer**: negligible. Zero KZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. НЦГПИ is paid-affordable for Kazakh
  residents (~$141/yr) but de-facto unavailable to foreign users without a
  Kazakh ИИН. Country is ~2.7 million km²; even with a subscription,
  baselines will be long outside Almaty, Astana, and the northern corridor.

### UZ — Uzbekistan

**date_added**: 2026-05-06

- **Free government RTK**: none confirmed publicly accessible.
  UzGeodezKadastr (State Committee for Land Resources, Geodesy, Cartography and State
  Cadastre, `uzgeodezkadastr.uz`) operates 30–50 permanent GNSS reference stations
  concentrated in Tashkent, the Fergana Valley, and major provincial centres (50-station
  plan described in 2016–2017 literature; 2024 academic paper confirms the network is
  operational for state/professional use). No public NTRIP endpoint, registration portal,
  or published tariff. Access restricted to licensed surveyors and state agencies; no
  open-data mandate analogous to Indonesia's Law No. 4/2011.
- **Volunteer**: negligible. Zero UZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. Central Asian pattern is uniformly closed-access;
  deploy a local base station.

### TJ — Tajikistan

**date_added**: 2026-04-30

- **Free government RTK**: none confirmed. The State Committee for Land
  Management and Geodesy (zamin.tj) and the "Fazo" Institute operate GNSS
  equipment for cadastral and land-reform work, but no public NTRIP caster
  or open fixed reference station (CORS) endpoint has been found. The
  agency's almgc.tj domain was unreachable on 2026-04-30; no archived or
  cached version returned any GNSS or NTRIP content. CAIAG's Central Asia
  seismic network includes one TJ station (Pamir region) but this is
  research-only, not an RTK service. → networks.md: `almgc_tj`
- **Volunteer**: none. Zero TJ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists; no paid commercial alternative
  identified. Landlocked mountainous country with sparse geodetic
  infrastructure; hobbyists should deploy a local base station.

### KG — Kyrgyzstan

**date_added**: 2026-05-06

- **Free government RTK**: none free. KyrPOS (State Agency for Land Resources,
  Cadastre, Geodesy and Cartography — ГАЗРКГК, gosreg.gov.kg), operated as a
  paid subscription service: 170 KGS/day · 3,180 KGS/month per receiver (~$37/mo
  at May 2026 rates), minimum one month; contract-based sign-up (email
  `gosreg.gov.kg` with signed contract + GNSS receiver serial, then bank
  payment). Host:port published on gosreg.gov.kg/ky/?page_id=3029:
  `cors.gosreg.gov.kg:8085` (non-standard port; port unreachable externally, likely
  geo-filtered or credential-gated). 18 CORS stations in 5 zones: Chui/Bishkek area
  (6), Fergana Valley/Osh (8), Naryn (1), Issyk-Kul (3).
  → networks.md: `kyrpos`
- **Volunteer**: none. Zero KG stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. KyrPOS is paid; CAIAG (German-funded research
  institute in Bishkek) operates permanent GNSS stations including a Bishkek IGS/ESA
  site but these are research-only with no RTK correction service. Hobbyists should
  deploy a local base station.

### TM — Turkmenistan

**date_added**: 2026-04-30

- **Free government RTK**: none. No national NTRIP/RTK-CORS network has been
  found in any public registry (BKG/IGS, mvarga1989 CORS list, ArduSimple,
  SNIP, rtk2go monitor) or on any .gov.tm / .com.tm domain. The national
  mapping agency is Turkmengeodezija (Turkmen Map Production Enterprise,
  Ashgabat). FAO supported the Land Resources Service in building a 65-station
  fixed reference station (CORS) infrastructure (2022–2025), and a 2024 article
  on turkmenistan.gov.tm confirms GNSS training is ongoing — indicating the
  network exists for internal use but is not publishing a public NTRIP service.
  No operator website, email, or phone for Turkmengeodezija was discoverable as
  of 2026-04-30. → networks.md: `tm_cors`
- **Volunteer**: none. Zero TM stations on rtk2go or Centipede.
- **Gap**: no free or commercial RTK accessible to hobbyists. Turkmenistan has
  one of the most restricted information environments in Central Asia; the CORS
  network exists but operates as closed government infrastructure. Hobbyists
  should deploy a local base station.
