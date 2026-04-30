# Free RTK NTRIP networks — technical record

_Authoritative reference for every network investigated, whether in pipeline or not._
_Read before touching `scripts/fetch_stations.py` or `index.html`._

## Role of this file

This is the **refined operator catalogue for our use**: networks discovered
via `docs/country-survey.md` and `docs/global-survey.md` are pulled in here,
verified, and curated into per-network blocks with endpoints, access terms,
pricing, and pipeline status. Think of it as the working bench between two
ends:

- The country/global surveys feed candidates in (broad, completeness-focused).
- This file refines them into structured records we can act on.
- `data/country_markers.json` then translates the subset that warrants a
  map marker into user-facing copy.

It is internal/developer-facing — acronyms and audit phrasing are fine here
because the audience is us, not hobbyists. The files are not mirrors of one
another: a country can have a paragraph in the survey without a block here
(if there is no operator worth cataloguing), and a block here can exist
without a marker (if it is regional-only or not substantial enough). The
content narrows at each step.

_Last updated: 2026-04-22._

---

## Format

Each entry uses these fields. Omit fields that don't apply (e.g. `host:port` for
candidates whose endpoint is withheld).

```
## <id> — <Name> (<COUNTRY>)

**status**:    free | paid-affordable | paid | restricted | weird | candidate | rejected
**host:port**: `host:port`
**type**:      single-base | physical-coord-vrs | single-coord-vrs
**access**:    free / registration / paid [brief terms]
**stations**:  N (approximate)
**source**:    url [, url …]

[Notes: gotchas, drop rationale — 1–5 lines.]

**investigate**: what to verify before the next pipeline change (CI-failing entries)
**missing**:    what a new session must find before this can be ingested (deferred entries)
```

**Popup notes (`SOURCE_AUTH.openNote` in `index.html`)** are derived from the
`**access**:` field here. When access is `conditions`, the restricting condition
must survive into the note — do not flatten to "Free registration required".
Conditions that must be preserved verbatim: paid tiers for certain use cases
(walcors), national identity requirements (gnss_campania: SPID), non-commercial
licence (earthscope), access deadlines (estpos), per-user limits (rbmc_ip).

Status glossary (describes the network's nature, not whether it's ingested —
ingestion is derivable from `SOURCES` in `scripts/fetch_stations.py` and from
`data/stations.json`):
- **free** — no fee to use. Includes both networks already wired into the
  pipeline and free networks whose host:port is still missing or only
  disclosable after registration. The entry text says which.
- **paid-affordable** — paid, under the project's ~$200/yr cutoff; surfaced
  in the UI as a hobbyist-reachable fallback.
- **paid** — paid, over the cutoff.
- **restricted** — exists but unobtainable for the target user (vetted
  partners only, sector-limited, no published rate).
- **weird** — something unusual that overrides the access question:
  non-standard NTRIP, active jamming/spoofing, infrastructure too sparse
  for RTK to work, war-disrupted with unknown status. The entry's notes
  carry the warning.
- **candidate** — free, endpoint known, ready to ingest but not yet wired
  into `fetch_stations.py`. Workflow state, not a network property.
- **rejected** — investigated and explicitly excluded from the catalogue;
  reason documented. Not a network property either; a meta-status that
  records what we ruled out.

---

## In-pipeline — single-base

Physical stations with distinct coordinates shown on map.

---

## rtk2go — RTK2GO (global)

**status**:    free
**host:port**: `rtk2go.com:2101`
**type**:      single-base
**access**:    free, no registration (username = any email, password = `none`)
**pipeline-access**: open
**stations**:  ~863
**source**:    rtk2go.com; use-snip.com
**operator**:  SNIP / use-snip.com

Community volunteer aggregator operated by SNIP / use-snip.com. `NEAR` mountpoint
requires rover NMEA GGA. Regional filtered views on `:2103` (PL) and `:2104` (JP)
are the same server — not separate SOURCES entries. Parser infers `carrier = 2`
when carrier field is blank and format starts with `RTCM 3` (required to retain
~98% of rtk2go entries).

---

## centipede — CentipedeRTK (global, France-centric)

**status**:    free
**host:port**: `crtk.net:2101`
**type**:      single-base
**access**:    free, no registration (username = `centipede`, password = `centipede`)
**pipeline-access**: open
**stations**:  ~1203
**source**:    centipede-rtk.org
**operator**:  Centipede-RTK association (non-profit)

Volunteer network initiated by INRAE (2019); now operated by non-profit
Centipede-RTK association (formed Aug 2024). Open-source Millipede caster stack
(BSD-3). Migrated from `caster.centipede.fr` to `crtk.net` on 2025-03-18.
`NEAR` mountpoint requires rover GGA; `NEAR4` for older equipment. 30+ countries
through one federation endpoint; no separate country-specific instances found.

---

## frednet — FReDNet (IT + border AT/SI)

**status**:    free
**host:port**: `gnsscaster.regione.fvg.it:8080`
**type**:      physical-coord-vrs
**access**:    sourcetable open; stream requires free email registration
**pipeline-access**: registration
**stations**:  ~39
**source**:    frednet.crs.ogs.it; gnsscaster.regione.fvg.it
**operator**:  OGS — Istituto Nazionale di Oceanografia e Geofisica Sperimentale

Operated by OGS (Istituto Nazionale di Oceanografia e Geofisica Sperimentale).
Crustal-deformation network for Friuli-Venezia Giulia; coverage extends into
Slovenia and W Austria. Register via frednet.crs.ogs.it.

---

## geortk — GeoRTK (JP)

**status**:    free
**host:port**: `geortk.jp:2101`
**type**:      single-base
**access**:    free, no registration; free indefinitely (1-yr advance notice if changed)
**pipeline-access**: open
**stations**:  ~41
**source**:    geortk.jp (Geosense Co., Ltd.)
**operator**:  Geosense Co., Ltd.

Japan volunteer caster. ~66 STR lines total; ~25 report 0/0 (offline bases) and
are dropped by coordinate filter. Sourcetable has shrunk over time.

---

## auscors — AUSCORS (AU)

**status**:    free
**host:port**: `ntrip.data.gnss.ga.gov.au:2101`
**type**:      single-base
**access**:    free; register at gnss.ga.gov.au/registration; CC BY 4.0
**pipeline-access**: registration
**stations**:  ~813
**source**:    gnss.ga.gov.au; auscors.ga.gov.au (dead since Jul 2022)
**operator**:  Geoscience Australia
**licence**:   CC BY 4.0

Operated by Geoscience Australia. Old host `auscors.ga.gov.au` dead since Jul 2022.
TLS also available on port 443. Attribute "© Commonwealth of Australia (Geoscience Australia)".

---

## positionz — PositioNZ-RT (NZ)

**status**:    free
**host:port**: `positionz-rt.linz.govt.nz:2101`
**type**:      single-base
**access**:    free; LINZ account required; register via linz.govt.nz; CC BY 4.0 NZ
**pipeline-access**: registration
**stations**:  ~62
**source**:    linz.govt.nz; toitutewhenua.govt.nz
**operator**:  LINZ — Land Information New Zealand
**licence**:   CC BY 4.0 NZ

NZ mainland + Chatham Islands + Antarctica. Streaming latency reduced ~90% in
Dec 2023 upgrade. Attribute "Source: Land Information New Zealand".

---

## trignet — TrigNet (ZA)

**status**:    free
**host:port**: `trignet.co.za:2101`
**type**:      single-base
**access**:    free; register at trignet.co.za
**pipeline-access**: registration
**stations**:  ~72
**source**:    trignet.co.za (NGI / National Geospatial Information, DALRRD)
**operator**:  NGI — National Geospatial Information (DALRRD)
**licence**:   Public mandate — all NGI products free of charge

All NGI products and services free of charge. No explicit CC licence; public mandate.
Single-base RTK (~5 cm) within 30–40 km; Network RTK (~3 cm) in Gauteng,
Western Cape, KwaZulu-Natal clusters only.

---

## rbmc_ip — RBMC-IP (BR)

**status**:    free
**host:port**: `gps-ntrip.ibge.gov.br:2101`
**type**:      single-base
**access**:    free; gov.br signup; 5-station limit per user; 1,000 concurrent max
**pipeline-access**: registration
**stations**:  ~140
**source**:    ibge.gov.br; gps-ntrip.ibge.gov.br
**operator**:  IBGE — Instituto Brasileiro de Geografia e Estatística

Alt IP: `170.84.40.52:2101`. 150 stations as of Dec 2024 (IBGE added 5 in Dec 2024).

---

## ramsac — RAMSAC-NTRIP (AR)

**status**:    free
**host:port**: `ntrip.ign.gob.ar:2101`
**type**:      single-base
**access**:    free; register via ign.gob.ar portal; 8-hr session cap
**pipeline-access**: registration
**stations**:  ~203
**source**:    ign.gob.ar
**operator**:  IGN — Instituto Geográfico Nacional (Argentina)

POSGAR 07 reference frame.

---

## regna_rou — REGNA-ROU (UY)

**status**:    free
**host:port**: `rtk.igm.gub.uy:2101`
**type**:      single-base + VRS
**access**:    free; web registration at rtk.igm.gub.uy/SBC/Account/Register
**pipeline-access**: registration
**stations**:  ~26
**source**:    igm.gub.uy
**operator**:  IGM — Instituto Geográfico Militar (Uruguay)

Uruguay IGM (Instituto Geográfico Militar). "El Servicio no tiene costo."
SIRGAS-ROU reference frame (ITRF-compatible). 1,000+ registered users as of 2025.
Expanded Dec 2025 with 8 new SinoGNSS M300 Pro CORS stations.
1–2 cm horizontal with dual-frequency receiver.

---

## earthscope — EarthScope NOTA (Americas)

**status**:    free
**host:port**: `ntrip.earthscope.org:2101`
**type**:      single-base
**access**:    free non-commercial (annual NULA renewal); commercial use per-seat licensed
**pipeline-access**: conditions
**stations**:  ~1096
**source**:    earthscope.org/data/gnss-realtime/
**operator**:  EarthScope Consortium
**licence**:   NULA (non-commercial; annual renewal)

Americas-wide. Also `:2105` (BINEX), `:2108` (PPP solutions). RTCM 3.3 MSM.
Legacy UNAVCO platform retired 2025-07-29; all users must use ntrip.earthscope.org.
Hobbyist and small-shop use confirmed in scope. Metadata/station-list display
permitted per NULA.

---

## mirai — MIRAI / Go!GNSS (JP + overseas partners)

**status**:    free
**host:port**: `ntrip.go.gnss.go.jp:2101`
**type**:      single-base
**access**:    free incl. commercial + automated ("peaceful purposes"); separate NtripCaster auth form
**pipeline-access**: registration
**stations**:  ~325
**source**:    go.gnss.go.jp (Cabinet Office SPAC)
**operator**:  Cabinet Office SPAC (go.gnss.go.jp)

Register at go.gnss.go.jp plus a separate NtripCaster authorization application.
Accounts expire after 365 days inactivity. Raw observations only (rover computes
RTK baseline). L1C/B support for QZSS QZS-6 added Jun 2025.

---

## cors_korea — CORS-KOREA (KR)

**status**:    free
**host:port**: `www.gnssdata.or.kr:2101`
**type**:      physical-coord-vrs
**access**:    free; sourcetable public without auth; stream registration may require Korean national ID
**pipeline-access**: conditions
**stations**:  ~498
**source**:    gnssdata.or.kr (NGII)
**operator**:  NGII — National Geographic Information Institute

VRS + FKP. ~90–100 physical stations at ~40 km spacing. Korean-language portal;
international access may be impractical if national ID is required.

---

## In-pipeline — physical-coord VRS

Sourcetable exposes real antenna locations; rover connects via VRS mountpoints.
Map shows physical station pins.

---

## ergnss — ERGNSS (ES)

**status**:    free
**host:port**: `ergnss-ip.ign.es:2101`
**type**:      physical-coord-vrs
**access**:    free; register at ergnss.ign.es/gnuserportal/ (immediate); CC-compatible
**pipeline-access**: registration
**stations**:  ~128
**source**:    ergnss.ign.es (IGN — Instituto Geográfico Nacional)
**operator**:  IGN — Instituto Geográfico Nacional
**licence**:   Attribution required per Orden FOM/2807/2015

~120 physical stations. GPS+GLO+GAL+BDS. Attribution to IGN required per
Orden FOM/2807/2015. RAP (Andalucía) supplements in the south; separate signup.

---

## satref — SatRef (HK)

**status**:    free
**host:port**: `ntrip.geodetic.gov.hk:2101`
**type**:      physical-coord-vrs
**access**:    free; register via geodetic.gov.hk or DATA.GOV.HK open-data path
**pipeline-access**: registration
**stations**:  ~22
**source**:    geodetic.gov.hk (Lands Department, Survey & Mapping Office)
**operator**:  Lands Department, Survey and Mapping Office (SMO)
**licence**:   Open data (commercial and non-commercial reuse permitted)

19 physical stations (16 reference + 3 integrity monitoring). Mountpoint `VRS32G`
(GPS+GLO+GAL+BDS). Open data policy (commercial and non-commercial reuse permitted).
Migrated to `ntrip.geodetic.gov.hk` Jun 2023; old `www.geodetic.gov.hk` domain
for NTRIP decommissioned. Accounts inactive 12+ months are terminated.
Raw TCP (NTRIP 1.0) fallback required in fetcher — responds `SOURCETABLE 200 OK`,
not HTTP.

---

## inacors — InaCORS (ID)

**status**:    free
**host:port**: `nrtk.big.go.id:2001`
**type**:      physical-coord-vrs
**access**:    free; register at nrtk.big.go.id; Law No. 4/2011 mandates free public service
**pipeline-access**: registration
**stations**:  ~4
**source**:    big.go.id (BIG — Badan Informasi Geospasial)
**operator**:  BIG — Badan Informasi Geospasial
**licence**:   Law No. 4/2011 (public access mandated)

Port 2001, not 2101. 200+ stations declared; only ~4 unique coords appear in
sourcetable — likely partial data exposure. 16,800+ registered users as of last report.

---

## igac — IGAC MAGNA-ECO (CO)

**status**:    free
**host:port**: `sbc.igac.gov.co:2101`
**type**:      physical-coord-vrs
**access**:    free; register at redgeodesica-sbc.igac.gov.co/sbc; Law 1955/2019 mandates public access
**pipeline-access**: registration
**stations**:  ~17
**source**:    igac.gov.co; redgeodesica-sbc.igac.gov.co
**operator**:  IGAC — Instituto Geográfico Agustín Codazzi
**licence**:   Law 1955/2019 (public access mandated)

233 stations declared; 17 unique coords in sourcetable. VRS also on `:2102`.
National Geodetic Control Centre launched Apr 2024 (Resolution 1771/2024).
First confirmed free VRS/NRTK in Latin America.

---

## spslux — SPSLux (LU)

**status**:    free
**host:port**: `stream.spslux.lu:5005`
**type**:      physical-coord-vrs
**access**:    free; register at spslux.lu/SBC/Account/Register (subscribe "SPSLUX (N)RTK")
**pipeline-access**: registration
**stations**:  ~17
**source**:    spslux.lu (ACT — Administration du Cadastre et de la Topographie)
**operator**:  ACT — Administration du Cadastre et de la Topographie

Port 5005, not 2101. IP 185.106.24.68. Luxembourg open-data policy — all services
free of charge.

---

## icecors — IceCORS (IS)

**status**:    free
**host:port**: `178.19.53.126:2101`
**type**:      physical-coord-vrs
**access**:    free ("data is free of charge" — natt.is); register at natt.is/is/landmaelingar/jardstodvakerfi
**pipeline-access**: registration
**stations**:  ~20 (populates on fetch; recently added to pipeline)
**source**:    natt.is (LMÍ — Landmælingar Íslands)
**operator**:  LMÍ — Landmælingar Íslands

GNCASTER software (same as SAPOS). Offers VRS (VRS30, FKP30) and single-base
(RTCM30). Stream credentials provided after registration at natt.is.

---

## SAPOS — Germany (DE, 16 Bundesländer)

**status**:    free (all 16 states)
**type**:      physical-coord-vrs (some states); single-coord-vrs (others — 0 map stations)
**access**:    sourcetable public; streams require per-Länder web registration
**registration**: https://www.sapos.de  (central portal links to each state's signup)
**source**:    sapos.de; zentrale-stelle-sapos.de

Federal-state RTK network. Each Bundesland operates its own NTRIP caster with
independent registration. Most states free for all uses. Bayern charges €20/yr
flat rate for non-agricultural use (free for agriculture) — under the $200/yr
cutoff. States whose sourcetables report a single coordinate for all virtual
mountpoints yield 0 map stations (single-coord VRS); coverage for those requires
NRTK polygons (deferred). Raw TCP (NTRIP 1.0) fallback required in fetcher —
SAPOS casters do not speak standard HTTP.

| id | state | host:port | map type | notes |
|---|---|---|---|---|
| `sapos_SH_HH` | Schleswig-Holstein + Hamburg | `sapos.geonord.de:2101` | single-coord VRS | 0 stations |
| `sapos_NI` | Niedersachsen + Bremen | `sapos-ni-ntrip.de:2101` | single-coord VRS | 0 stations |
| `sapos_NW` | Nordrhein-Westfalen | `sapos-nw-ntrip.de:2101` | single-coord VRS | 0 stations |
| `sapos_HE` | Hessen | `sapos-he-ntrip.de:2101` | physical-coord VRS | ~4 stations (3 unique coords) |
| `sapos_RP` | Rheinland-Pfalz | `sapos-ntrip.rlp.de:2101` | physical-coord VRS | ~17 stations (5 unique coords); confirmed free (LVermGeo) |
| `sapos_BW` | Baden-Württemberg | `sapos-bw-ntrip.de:2101` | single-coord VRS | 0 stations |
| `sapos_BY` | Bayern | `sapos-by-ntrip.de:2101` | single-coord VRS | €20/yr non-agri flat rate; free for agriculture |
| `sapos_SN` | Sachsen (GeoSN) | `ntrip.sachsen.de:2101` | populates on fetch | endpoint confirmed 2026-04; first successful CI fetch will populate count |
| `sapos_SL` | Saarland | `sapos-sl-ntrip.de:2101` | physical-coord VRS | ~14 stations (9 unique coords) |
| `sapos_BE` | Berlin | `sapos-be-ntrip.de:2101` | single-coord VRS | 52.48, 13.3 |
| `sapos_BB` | Brandenburg | `sapos-bb-ntrip.de:2101` | single-coord VRS | 52.23, 13.05 |
| `sapos_MV` | Mecklenburg-Vorpommern | `sapos-mv-ntrip.de:2101` | single-coord VRS | 0 stations |
| `sapos_LSA` | Sachsen-Anhalt | `sapos-lsa-ntrip.de:2101` | single-coord VRS | 0 stations |
| `sapos_TH` | Thüringen | `sapos-th-ntrip.de:2101` | single-coord VRS | 51.01, 11.03 |

Note: SAPOS GEPOS (BKG federal, `bkg1.positioning-service.net:2101`) broadcasts
SSR/PPP-RTK corrections in SSRZ format — not standard OSR RTCM; requires
SSR-capable receiver or Geo++ SSR2OBS converter. Out of scope for this pipeline.

---

## apos — APOS (AT)

**status**:    free
**host:port**: `aposrtk.bev.gv.at:2101`
**type**:      physical-coord-vrs
**access**:    conditions — free for agriculture/forestry via eAMA credentials
**pipeline-access**: conditions
               (farm client number + PIN from Agrarmarkt Austria);
               professional/hobbyist use paid via bev.gv.at portal
**yearly_cost**: pricing via bev.gv.at for professional/hobbyist use;
               eAMA free for agriculture/forestry
**stations**:  37
**source**:    bev.gv.at (BEV — Bundesamt für Eich- und Vermessungswesen)
**operator**:  BEV — Bundesamt für Eich- und Vermessungswesen

Austria's national VRS network (Free* in UI). Sourcetable is publicly readable;
RTCM stream authentication requires valid credentials. Hobbyists without farm
credentials register and pay via the BEV portal. 37 physical reference stations
with distinct coordinates are exposed in the sourcetable; these show on the map
as regular pins. SAPOS Bavaria (DE) and FReDNet (IT) provide partial coverage
across the AT border.

---

### Italy — regional networks

---

## spin3 — SPIN3 GNSS (IT — Piemonte, Lombardia, Valle d'Aosta)

**status**:    free
**host:port**: `spingnss.it:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via spingnss.it (CSI Piemonte public portal)
**pipeline-access**: registration
**stations**:  ~39
**source**:    spingnss.it (CSI Piemonte on behalf of Regione Piemonte, Lombardia, VdA)
**operator**:  CSI Piemonte

Inter-regional public network covering Piemonte, Lombardia, and Valle d'Aosta.
Operated by CSI Piemonte. Provides single-base RTCM 3.x streams and VRS.
Free public access with simple registration; no annual fee documented.

---

## gpsumbria — GPS-UMBRIA (IT — Umbria)

**status**:    free
**host:port**: `gpsumbria.regione.umbria.it:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via gpsumbria.regione.umbria.it
**pipeline-access**: registration
**stations**:  12
**source**:    gpsumbria.regione.umbria.it (Regione Umbria)
**operator**:  Regione Umbria

Regional GNSS network for Umbria. Free public service with 12 physical reference stations.

---

## gnss_abruzzo_lazio — Rete GNSS Abruzzo + Lazio (IT — Abruzzo + Lazio)

**status**:    free
**host:port**: `gnss-rtk.regione.abruzzo.it:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via Abruzzo regional geoportal
**pipeline-access**: registration
**stations**:  ~29
**source**:    gnss-rtk.regione.abruzzo.it (Regione Abruzzo / Regione Lazio)
**operator**:  Regione Abruzzo / Regione Lazio

Since December 2022, Regione Lazio's stations were integrated into the Abruzzo
caster. A single endpoint serves both regions' physical reference stations.

---

## sit_puglia — SIT Puglia GNSS (IT — Puglia)

**status**:    free
**host:port**: `gps.sit.puglia.it:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via sit.puglia.it (Sistema Informativo Territoriale)
**pipeline-access**: registration
**stations**:  12
**source**:    gps.sit.puglia.it (Regione Puglia)
**operator**:  Regione Puglia (SIT)

Puglia regional GNSS network. 12 physical reference stations. Free registration.

---

## gnss_campania — Rete GNSS Campania (IT — Campania)

**status**:    free
**host:port**: `gps-sit.regione.campania.it:2101`
**type**:      physical-coord-vrs
**access**:    conditions; new users require SPID (Italian national digital identity)
**pipeline-access**: conditions
               via the campania.it GNSS portal; legacy credentials publicly documented
               in Italian surveying forums may still work on the old endpoint
**stations**:  ~18
**source**:    regione.campania.it GNSS section (Regione Campania)
**operator**:  Regione Campania

Campania regional GNSS network. Access upgraded to SPID-authenticated portal;
legacy endpoint may accept old credentials. Free for SPID holders.

---

### US state DOT — physical-coord

---

## wiscors — WISCORS (US-WI)

**status**:    free
**host:port**: `wiscors.dot.wi.gov:2101`
**type**:      physical-coord-vrs (single-base + VRS)
**access**:    registration; free via wiscors.dot.wi.gov (Wisconsin DOT)
**pipeline-access**: registration
**stations**:  ~180
**source**:    wiscors.dot.wi.gov (Wisconsin Department of Transportation)
**operator**:  Wisconsin DOT

Wisconsin CORS Network operated by WisDOT. Offers both single-base streams
and VRS corrections. Many WI stations also appear in EarthScope NOTA —
verify overlap before ingesting to avoid duplicate pins.

---

## fprn — FPRN (US-FL)

**status**:    free
**host:port**: `ntrip.myfloridagps.com:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via myfloridagps.com (Florida DOT)
**pipeline-access**: registration
**stations**:  ~120
**source**:    myfloridagps.com (Florida Department of Transportation)
**operator**:  Florida DOT (FDOT)

Florida Permanent Reference Network operated by FDOT. Single-base and VRS
corrections. Some overlap with EarthScope NOTA expected.

---

## ardot_rtn — ARDOT RTN (US-AR)

**status**:    free
**host:port**: `gps.ardot.gov:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via ardot.gov (Arkansas DOT)
**pipeline-access**: registration
**stations**:  ~50
**source**:    ardot.gov (Arkansas Department of Transportation)
**operator**:  Arkansas DOT

Arkansas real-time network. Free after registration.

---

## macors — MaCORS (US-MA)

**status**:    free
**host:port**: `macorsrtk.massdot.state.ma.us:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via massdot.state.ma.us (MassDOT)
**pipeline-access**: registration
**stations**:  22
**source**:    massdot.state.ma.us (Massachusetts Department of Transportation)
**operator**:  Massachusetts DOT (MassDOT)

Massachusetts CORS network. 22 stations; free registration.

---

## vector — VECTOR VT (US-VT)

**status**:    free
**host:port**: `20.185.11.35:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via vcgi.vermont.gov (Vermont Center for Geographic Information)
**pipeline-access**: registration
**stations**:  ~15
**source**:    vcgi.vermont.gov (Vermont Center for Geographic Information)
**operator**:  Vermont Center for Geographic Information (VCGI)

Vermont CORS network operated by VCGI. Bare IP address; no hostname. Free registration.

---

## azcors — AzCORS (US-AZ)

**status**:    free
**host:port**: `azcors.azwater.gov:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via azwater.gov (Arizona Dept. of Water Resources)
**pipeline-access**: registration
**stations**:  51
**source**:    azwater.gov (Arizona Department of Water Resources)
**operator**:  Arizona Dept. of Water Resources (ADWR)

Arizona CORS Network operated by ADWR. 51 stations; free registration. Moderate
overlap with EarthScope NOTA expected.

---

## gcgc_rtn — GCGC RTN (US-MS)

**status**:    free
**host:port**: `rtn.usm.edu:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via usm.edu GCGC portal
**pipeline-access**: registration
**stations**:  ~35
**source**:    rtn.usm.edu (Gulf Coast Geodetic Consortium / University of Southern Mississippi)
**operator**:  Gulf Coast Geodetic Consortium / University of Southern Mississippi

Gulf Coast Geodetic Consortium real-time network via University of Southern Mississippi.
Covers Mississippi and adjacent Gulf Coast states. Free registration.

---

## alcors — AlCORS (US-AL)

**status**:    free
**host:port**: `aldotcors.dot.state.al.us:10011`
**type**:      physical-coord-vrs
**access**:    registration; free via dot.state.al.us (Alabama DOT)
**pipeline-access**: registration
**stations**:  ~50
**source**:    dot.state.al.us (Alabama Department of Transportation)
**operator**:  Alabama DOT (ALDOT)

Alabama CORS network operated by ALDOT. Non-standard port 10011 (Leica GNSS Spider
default). Free registration.

---

## orgn — ORGN (US-OR)

**status**:    free
**host:port**: `167.131.0.205:9879`
**type**:      physical-coord-vrs
**access**:    registration; free via oregon.gov (Oregon DOT)
**pipeline-access**: registration
**stations**:  ~100
**source**:    oregon.gov (Oregon Department of Transportation)
**operator**:  Oregon DOT (ODOT)

Oregon GPS Network operated by ODOT. Bare IP address; non-standard port 9879
(Leica). Significant overlap with EarthScope NOTA expected.

---

## msrn — MSRN (US-MI)

**status**:    free
**host:port**: `mdotcors.michigan.gov:10700`
**type**:      physical-coord-vrs
**access**:    registration; free via michigan.gov (Michigan DOT)
**pipeline-access**: registration
**stations**:  ~120
**source**:    michigan.gov (Michigan Department of Transportation)
**operator**:  Michigan DOT (MDOT)

Michigan Spatial Reference Network operated by MDOT. Non-standard port 10700
(Leica GNSS Spider). Significant overlap with EarthScope NOTA expected.

---

## nysnet — NYSNet (US-NY)

**status**:    free
**host:port**: `cors.dot.ny.gov:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via dot.ny.gov (New York State DOT)
**pipeline-access**: registration
**stations**:  ~150
**source**:    dot.ny.gov (New York State Department of Transportation)
**operator**:  New York State DOT (NYSDOT)

New York State GPS Network operated by NYSDOT. Significant overlap with
EarthScope NOTA expected.

---

## incors — InCORS (US-IN)

**status**:    free
**host:port**: `incors.in.gov:10000`
**type**:      physical-coord-vrs
**access**:    registration; free via incors.in.gov (Indiana Dept. of Administration)
**pipeline-access**: registration
**stations**:  ~70
**source**:    incors.in.gov (Indiana Department of Administration)
**operator**:  Indiana Dept. of Administration

Indiana CORS Network. Non-standard port 10000. Free registration.

---

## iartn — IARTN (US-IA)

**status**:    free
**host:port**: `iartnsbc.iowadot.gov:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via iowadot.gov (Iowa DOT)
**pipeline-access**: registration
**stations**:  83
**source**:    iowadot.gov (Iowa Department of Transportation)
**operator**:  Iowa DOT

Iowa Real-Time Network operated by Iowa DOT. 83 physical stations. Free registration.

---

## In-pipeline — VRS-only

Networks in pipeline that yield 0 map stations: sourcetable exposes only virtual
or single-coordinate mountpoints (VRS filter drops them), or the caster is
unreachable and no cached sourcetable exists. Stations remain in JSON from last
successful fetch once a cache exists.

---

## asg_eupos — ASG-EUPOS (PL)

**status**:    free
**host:port**: `system.asgeupos.pl:2101`
**type**:      single-coord-vrs
**access**:    free since Oct 2022; web signup; admin approval 1–2 working days
**pipeline-access**: registration
**stations**:  0 (130+ declared; single coord 52.0, 21.0 Warsaw)
**source**:    system.asgeupos.pl (GUGiK)
**operator**:  GUGiK — Główny Urząd Geodezji i Kartografii

Also ports :8080/:8082/:8083/:8086 for VRS variants. GPS+GLO+GAL+BDS.
VRS (NAWGIS/KODGIS/FKP/MAC). Coverage requires NRTK polygon (deferred).

---

## flepos — FLEPOS (BE — Flanders)

**status**:    free
**host:port**: `flepos.vlaanderen.be:2101`
**type**:      single-coord-vrs
**access**:    free for all uses; web self-signup at flepos.vlaanderen.be
**pipeline-access**: registration
**stations**:  0 (45 declared; single-coord Flanders centroid)
**source**:    flepos.vlaanderen.be
**operator**:  Agentschap Digitaal Vlaanderen

Old endpoint `ntrip.flepos.be` is NXDOMAIN as of 2026-04. Currently timing out
in CI. Coverage requires NRTK polygon (deferred).

**investigate**: connect from a European IP — could be location-based firewall rather
than egress block; also verify `flepos.vlaanderen.be:2101` still resolves correctly.

---

## walcors — WALCORS (BE — Wallonia)

**status**:    free
**host:port**: `gnss.wallonie.be:2101`
**type**:      single-coord-vrs
**access**:    free for positioning; paid for machine-control/auto-guidance (commercial resellers)
**pipeline-access**: registration
**stations**:  0 (23 declared; single-coord VRS; intermittently unreachable)
**source**:    gnss.wallonie.be (SPW)
**operator**:  SPW — Service Public de Wallonie

Intermittent outages documented. Currently timing out in CI.

**investigate**: check gnss.wallonie.be status page;
distinguish persistent outage from intermittent — if dead >4 weeks, drop from pipeline.

---

## latpos — LatPos (LV)

**status**:    free
**host:port**: `latpos.lgia.gov.lv:5001`
**type**:      single-coord-vrs
**access**:    free since 2018; SBC portal signup at latpos.lgia.gov.lv/SBC
**pipeline-access**: registration
**stations**:  0 (27 LV + 5 EE + 4 LT border stations declared; single-coord)
**source**:    latpos.lgia.gov.lv (LGIA)
**operator**:  LGIA — Latvijas Ģeotelpiskās informācijas aģentūra

Port 5001, not 2101 (confirmed per Alberding caster directory). Currently timing
out in CI.

**investigate**: re-verify port 5001 at latpos.lgia.gov.lv directly (try telnet/ncat
from a Baltic-region IP); also check LGIA website for endpoint changes.

---

## estpos — ESTPOS (EE)

**status**:    free
**host:port**: `gnss-rtk.maaamet.ee:8083`
**type**:      single-coord-vrs
**access**:    free until 31 Aug 2026 (director-general directive); portal account + service agreement
**pipeline-access**: conditions
**stations**:  0 (40 declared; VRS, iMAX, nearest-base; MSM5 available)
**source**:    geoportaal.maaamet.ee (Maa-amet / Land and Spatial Development Board)
**operator**:  Maa-amet (Land and Spatial Development Board)

Port 8083. Currently timing out in CI. Service expiry Aug 2026 — review before then.

**investigate**: verify `gnss-rtk.maaamet.ee:8083` from an Estonian IP; check
geoportaal.maaamet.ee for credential requirement (may now need service agreement
before sourcetable is served). Re-confirm free status before Aug 2026 or drop.

---

## ksa_cors — KSA-CORS (SA)

**status**:    free
**host:port**: `ksacors.geoportal.sa:2101`
**type**:      single-coord-vrs
**access**:    free; register via ksacors.geoportal.sa
**pipeline-access**: conditions
**stations**:  0 (209 declared; single-coord; GPS+GLO+GAL+BDS)
**source**:    ksacors.geoportal.sa (GASGI/GEOSA)
**operator**:  GASGI / GEOSA

Old endpoint `KSACORS.gcs.gov.sa` is NXDOMAIN as of 2026-04. Currently timing
out in CI. Coverage requires NRTK polygon (deferred).

**investigate**: verify `ksacors.geoportal.sa:2101` resolves and is reachable; try
connecting from a GCC-region IP; check geoportal.sa for updated endpoint or
registration requirement changes.

---

## cropos — CROPOS (HR)

**status**:    free
**host:port**: `gnss.cropos.hr:2101`
**type**:      single-coord-vrs
**access**:    free since Apr 2022 (Narodne novine 39/2022); email/web registration at cropos.hr
**pipeline-access**: registration
**stations**:  0 (35 declared; sourcetable reports 0/0 for all mountpoints)
**source**:    cropos.hr (DGU)
**operator**:  DGU — Državna geodetska uprava

Caster IP changed Nov 2023 (old: 195.29.118.122 → new: 195.29.198.194); DNS
hostname should resolve correctly. DPS (~0.3–0.5 m) and VPPS (~2 cm) free;
GPPS post-processing paid. Coverage requires NRTK polygon (deferred).

---

### US state DOT — VRS-only

---

## kycors — KyCORS (US-KY)

**status**:    free
**host:port**: `kycors.ky.gov:2101`
**type**:      single-coord-vrs
**access**:    registration; free via kycors.ky.gov (Kentucky Transportation Cabinet)
**pipeline-access**: registration
**stations**:  VRS only
**source**:    kycors.ky.gov (Kentucky Transportation Cabinet)
**operator**:  Kentucky Transportation Cabinet

Kentucky CORS Network. VRS-only service; no physical-coordinate mountpoints.
Register at kycors.ky.gov.

---

## mncors — MnCORS (US-MN)

**status**:    free
**host:port**: `mncors.dot.state.mn.us:9000`
**type**:      single-coord-vrs
**access**:    registration; free via mndot.gov (Minnesota DOT)
**pipeline-access**: registration
**stations**:  VRS only (underlying ~125 physical stations)
**source**:    mndot.gov (Minnesota Department of Transportation)
**operator**:  Minnesota DOT (MnDOT)

Minnesota CORS Network operated by MnDOT. Non-standard port 9000. VRS-only
sourcetable; physical stations not individually listed. Significant overlap
with EarthScope NOTA expected.

---

## odot_rtn — ODOT RTN (US-OH)

**status**:    free
**host:port**: `156.63.133.115:2101`
**type**:      single-coord-vrs
**access**:    registration; free via transportation.ohio.gov (Ohio DOT)
**pipeline-access**: registration
**stations**:  VRS only
**source**:    transportation.ohio.gov (Ohio Department of Transportation)
**operator**:  Ohio DOT

Ohio DOT real-time network. Bare IP address; VRS-only sourcetable. Free registration.

---

## modot_rtn — MoDOT RTN (US-MO)

**status**:    free
**host:port**: `rtk3.modot.mo.gov:2101`
**type**:      single-coord-vrs
**access**:    conditions; requires signed and notarized MoDOT CORS access agreement;
**pipeline-access**: conditions
               free once approved — contact via modot.mo.gov
**stations**:  VRS only
**source**:    modot.mo.gov (Missouri Department of Transportation)
**operator**:  Missouri DOT

Missouri DOT CORS network. VRS-only. Requires notarized access agreement
submitted to MoDOT before credentials are issued.

---

## wvrtn — WVRTN (US-WV)

**status**:    free
**host:port**: `wvrtn.cors.us:2101`
**type**:      single-coord-vrs
**access**:    registration; free via wvrtn.cors.us (WV Division of Highways)
**pipeline-access**: registration
**stations**:  VRS only
**source**:    transportation.wv.gov (West Virginia Division of Highways)
**operator**:  WV Division of Highways

West Virginia Real-Time Network. VRS-only sourcetable. Free registration.

---

## mainedot — MaineDOT CORS (US-ME)

**status**:    free
**host:port**: `mdotcors.maine.gov:2101`
**type**:      single-coord-vrs
**access**:    registration; free via maine.gov/mdot (Maine DOT)
**pipeline-access**: registration
**stations**:  VRS only (transitioning from single-base)
**source**:    maine.gov/mdot (Maine Department of Transportation)
**operator**:  Maine DOT

Maine DOT CORS network. Currently transitioning; sourcetable may show only VRS
streams until physical-coordinate mountpoints are published.

---

## mesa_rtvrn — Mesa County RTVRN (US-CO)

**status**:    free
**host:port**: `rtvrn.mesacounty.us:2101`
**type**:      single-coord-vrs
**access**:    registration; free via rtvrn.mesacounty.us
**pipeline-access**: registration
**stations**:  33 (17 NGS CORS + 16 county/partner stations) underlying VRS
**source**:    mesacounty.us/departments-and-services/public-works/gps-survey
**operator**:  Mesa County Public Works (Western Colorado)

VRS-only network covering western Colorado. Mountpoints are all VRS_* (CMR,
CMRx, RTCMv3, RTX variants) — no single-base mountpoints exposed. Free
sign-up at rtvrn.mesacounty.us; same credentials used for NTRIP. Trimble
PIVOT backend. Underlying 17 NGS CORS likely overlap with EarthScope NOTA
in northern Mesa County, but VRS streams have no fixed coordinate so no
duplicate pins on the map.

---

## Candidate — confirmed free, not yet ingested

Only one network (GPSBru) remains unconfirmed; all ingested networks have been moved to the appropriate in-pipeline sections.

---

## gpsbru — GPSBru / AGN (BE — Brussels)

**status**:    candidate
**host:port**: `agn.ngi.be` (port unconfirmed)
**type**:      single-base
**access**:    free; register at agn.ngi.be
**stations**:  1 (Uccle observatory)
**source**:    agn.ngi.be (NGI — National Geographic Institute)

Single station; useful only within ~30 km of Brussels. Low priority.

**missing**: confirm NTRIP port (standard 2101? try ncat/telnet agn.ngi.be 2101).

---

## Deferred — free, endpoint not yet obtainable

---

## renep — ReNEP (PT)

**status**:    free
**host:port**: withheld until post-registration
**type**:      physical-coord-vrs
**access**:    free; register at renep.dgterritorio.gov.pt
**stations**:  47
**source**:    dgterritorio.gov.pt (DGT — Direção-Geral do Território)

Host:port disclosed only after account approval. ETRS89 datum (mainland),
ITRF93 (autonomous regions). Stations and RINEX publicly visible.

**missing**: caster host:port — register at renep.dgterritorio.gov.pt to obtain;
or check Alberding directory / EUREF caster list for a public mirror.

---

## litpos — LitPOS (LT)

**status**:    free
**host:port**: not publicly listed
**type**:      physical-coord-vrs
**access**:    free (publicly-funded EUPOS member); register at geoportal.lt/web/litpos-en
**stations**:  35
**source**:    geoportal.lt (GIS-Centras)

RTCM 2.1/2.3/3.1/3.2, CMR, CMR+, CMRx. NTRIP host:port not publicly listed —
find via ArduSimple or Alberding caster directory before ingesting.

**missing**: caster host:port — search Alberding EUPOS directory (eupos.org),
ArduSimple country list, or contact via geoportal.lt/web/litpos-en.

---

## thailand_dol — Thailand DOL LandGNSS (TH)

**status**:    free
**host:port**: `110.78.0.54` with zone-based variable ports (port table at
               dol-rtknetwork.com/index.php/npage/view/9; PDF at
               dol-rtknetwork.com/uploads/files/manual/1(Port%20Number).pdf)
**type**:      VRS (network RTK)
**access**:    free with registration; register at
               dol-rtknetwork.com/index.php/register_gnss_beta
**stations**:  ~114–222 CORS (2019–2023 academic sources; 63 provinces covered)
**source**:    dol-rtknetwork.com (Department of Lands / กรมที่ดิน, Ministry of Interior)

Thai-language portal and manual. Caster IP `110.78.0.54` confirmed via public
aggregators; zone-based port scheme (multiple ports by geographic region) requires
downloading the port-number PDF or completing the beta registration to obtain the
full table. No single universal port confirmed for NTRIP sourcetable fetch.
Direct contact with Dept of Lands via dol.go.th recommended before pipeline ingestion.

**investigate**: confirm a single queryable sourcetable port or obtain the full
zone-port mapping from the Thai-language PDF at the URL above.

---

## zakpos — ZAKPOS (UA)

**status**:    weird
**host:port**: not currently accessible
**type**:      physical-coord-vrs
**access**:    was free; registration at zakhid.net.ua
**stations**:  ~50 (pre-conflict)
**source**:    zakhid.net.ua (Western Ukraine positioning service)

Ukrainian regional positioning service, disrupted since the Russian full-scale
invasion (Feb 2022). Operational status and endpoint availability unknown.
Do not add to pipeline until the service is confirmed operational.

**missing**: confirm service is operational and endpoint is reachable post-conflict.

---

## tpos — TPOS (IT — Trentino)

**status**:    free
**host:port**: withheld until post-registration
**type**:      physical-coord-vrs
**access**:    registration; free via tpos.provincia.tn.it (Provincia Autonoma di Trento)
**stations**:  11
**source**:    tpos.provincia.tn.it (PAT — Provincia Autonoma di Trento)

Trentino Positioning Service operated by the Autonomous Province of Trento. 11 physical
reference stations. Credentials disclosed only after account approval.

**missing**: caster host:port — register at tpos.provincia.tn.it; contact info at
https://www.provincia.tn.it/en/Services/TPOS-Trentino-POsitioning-Service

---

## stpos — STPOS (IT — South Tyrol / Alto Adige)

**status**:    free
**host:port**: withheld until post-registration
**type**:      physical-coord-vrs
**access**:    registration; free via stpos.it (Provincia Autonoma di Bolzano)
**stations**:  10
**source**:    stpos.it (Autonome Provinz Bozen / Provincia Autonoma di Bolzano)

South Tyrol Positioning Service operated by the Autonomous Province of Bolzano.
Bilingual (German/Italian). 10 physical reference stations.

**missing**: caster host:port — register at stpos.it; contact info at
https://www.provincia.bz.it/costruire-abitare/catasto-librofondiario/catasto/stpos-reti-appoggio-geodetico.asp

---

## gnss_veneto — Rete GNSS Veneto (IT — Veneto)

**status**:    free
**host:port**: not publicly listed
**type**:      physical-coord-vrs
**access**:    registration; apply via retegnssveneto.cisas.unipd.it
**stations**:  ~20
**source**:    retegnssveneto.cisas.unipd.it (CISAS — Università degli Studi di Padova)

Veneto regional GNSS network operated by CISAS (Centro Interdipartimentale di Studi e
Attività Spaziali), University of Padua. Credentials provided on request.

**missing**: caster host:port — contact via http://retegnssveneto.cisas.unipd.it/

---

## gnss_liguria — Rete GNSS Liguria (IT — Liguria)

**status**:    free
**host:port**: not publicly listed
**type**:      physical-coord-vrs
**access**:    registration; register via Liguria geoportal
**stations**:  10
**source**:    geoportal.regione.liguria.it (Regione Liguria)

Liguria regional GNSS network. 10 reference stations. Credentials via regional geoportal.

**missing**: caster host:port — contact via
https://geoportal.regione.liguria.it/servizi/rete-gnss-liguria.html

---

## sicilianet — Sicili@net (IT — Sicily + S. Calabria)

**status**:    free
**host:port**: not publicly listed
**type**:      physical-coord-vrs
**access**:    registration; apply via INGV Catania portal
**stations**:  ~80
**source**:    ct.ingv.it (INGV — Istituto Nazionale di Geofisica e Vulcanologia, Catania)

INGV Catania seismic monitoring network covering Sicily and southern Calabria. ~80 stations.
RTK service available to registered users; primarily a geophysical research network but open
to external applicants.

**missing**: caster host:port — contact via https://www.ct.ingv.it/index.php/risorse-e-servizi/sicil-net

---

## molise_gnss — Rete GNSS Molise (IT — Molise)

**status**:    free
**host:port**: not confirmed
**type**:      unknown
**access**:    unknown; likely registration-based
**stations**:  ~4
**source**:    regione.molise.it (Regione Molise)

Small regional GNSS network. NTRIP delivery unconfirmed; only ~4 reference stations
documented. Lowest-priority Italian regional network.

**missing**: confirm NTRIP delivery and endpoint — contact via regione.molise.it

---

## acorn — ACORN (US-AK)

**status**:    free
**host:port**: not confirmed
**type**:      physical-coord-vrs
**access**:    intended to be free; operated by Alaska DOT/PF
**stations**:  unknown
**source**:    dot.alaska.gov (Alaska Department of Transportation and Public Facilities)

Alaska CORS network. Free-intended service but NTRIP endpoint not confirmed from
public sources.

**missing**: confirm NTRIP host:port — search DOT/PF CORS documentation or Alberding directory.

---

## remos_ven — REMOS (VE)

**status**:    free
**host:port**: not publicly confirmed
**type**:      unknown
**access**:    intended free (IGVSB government service)
**stations**:  27 (NTRIP-capable, out of 29 permanent)
**source**:    igvsb.gob.ve (IGVSB — Instituto Geográfico de Venezuela Simón Bolívar)

Maracaibo (MARA) was the first REMOS station to stream NTRIP corrections experimentally
(Oct 2008); plans to bring remaining stations online were unclear post-2018. No public
host:port or registration portal confirmed. Operational continuity uncertain given
Venezuela's infrastructure constraints.

**missing**: confirm whether a public NTRIP caster is operational — check igvsb.gob.ve
or contact IGVSB; do not add to pipeline without a confirmed reachable endpoint.

---

## geocuba_gnss — GEOCUBA National GNSS Service (CU)

**status**:    restricted
**country**:   CU — Cuba
**type**:      single-base
**host:port**: not publicly listed
**access**:    restricted — appears limited to government and commercial survey clients;
               no self-service registration portal found
**yearly_cost**: n/a (no confirmed public service)
**stations**:  13 permanent stations (installed 2014–2019)
**operator**:  GEOCUBA (Grupo Empresarial GEOCUBA, under MINFAR —
               Ministerio de las Fuerzas Armadas Revolucionarias)
               `geocuba.cu`

**date_added**: 2026-04-29

Thirteen GNSS CORS stations distributed across Cuba's provinces, installed between
2014 and 2019 using non-US hardware (acquired outside US embargo restrictions). A
unified GNSS data server feeds these stations and an NTRIP service was confirmed as
operational in a 2024 conference paper ("Servicio NTRIP GNSS en Cuba: perspectivas y
retos", Informática Habana 2024). The server is described as published within
GEOCUBA's Geospatial Information Centre and intended for "prioritised sectors of the
national economy" — terrestrial, maritime, and aerial precision positioning. No
public host:port, credential portal, or non-governmental access procedure has been
published. Access from outside Cuba would additionally face Cuba's state-controlled
internet infrastructure (ETECSA monopoly) and US OFAC licensing considerations for
any US-origin software or payment processing. Zero CUB mountpoints on rtk2go or
Centipede.

**missing**: confirm whether a public or semi-public NTRIP endpoint exists — contact
GEOCUBA via `geocuba.cu` or the Revista Cubana de Geomática editorial contacts
(`geomatica.geocuba.cu`); do not add to pipeline without a confirmed reachable
endpoint and access model.

---

## Paid — affordable (under $200/yr cutoff)

Surface in UI as paid alternatives for users in areas with no free coverage.

---

## geodnet_usa — GEODNET USA

**status**:    paid
**host:port**: `rtk.geodnet.com:2101`
**type**:      single-base
**access**:    paid
**yearly_cost**: $40/month (~$480/yr; $160 for a 4-month seasonal block)
**operator**:  HYFIX.AI (geodnet.com)
**source**:    geodnet.com (HYFIX.AI)

Sourcetable publicly readable. Removed from free-source pipeline 2026-04-20.

---

## geodnet_eu — GEODNET Europe

**status**:    paid
**host:port**: `eu.geodnet.com:2101`
**type**:      single-base
**access**:    paid
**yearly_cost**: $40/month
**operator**:  HYFIX.AI (geodnet.com)
**source**:    geodnet.com (HYFIX.AI)

---

## geodnet_aus — GEODNET Australia

**status**:    paid
**host:port**: `aus.geodnet.com:2101`
**type**:      single-base
**access**:    paid
**yearly_cost**: $40/month
**operator**:  HYFIX.AI (geodnet.com)
**source**:    geodnet.com (HYFIX.AI)

---

## geodnet_sa — GEODNET South America

**status**:    paid
**host:port**: `sa.geodnet.com:2101`
**type**:      single-base
**access**:    paid
**yearly_cost**: $40/month
**operator**:  HYFIX.AI (geodnet.com)
**source**:    geodnet.com (HYFIX.AI)

---

## hepos — HEPOS (GR)

**status**:    paid-affordable
**host:port**: `uranus.gr:2101`
**access**:    paid
**yearly_cost**: €160 per 3-month block (~$170); ~€480/yr unlimited (~$520) — 3-month
               option is under the $200 cutoff for seasonal hobbyist use
**stations**:  unknown
**source**:    ktimatologio.gr (HEPOS S.A.)
**operator**:  HEPOS S.A. / Ktimatologio

---

## rompos — ROMPOS (RO)

**status**:    paid-affordable
**date_added**: 2026-04-29
**country**:   RO
**type**:      VRS (network RTK)
**host:port**: `rtk.rompos.ro:2101` (also `93.113.10.123:2101`); port 2105 also listed
**access**:    paid; ANCPI account required; self-service registration at epay.ancpi.ro;
               rover managed via app.rompos.ro
**registration**: `app.rompos.ro` (account creation at `epay.ancpi.ro`)
**yearly_cost**: ~€169/yr (~$183) — under $200/yr cutoff; monthly subscription also
               available; pricing set by ANCPI Order No. 16/2019
**stations**:  80+ permanent CORS stations (VRS output)
**source**:    rompos.ro; ancpi.ro
**operator**:  ANCPI — Agenția Națională de Cadastru și Publicitate Imobiliară

---

## tencent_rtk — Tencent RTK (CN)

**status**:    paid-affordable
**host:port**: `cors.tencent.com` (ports 8001–8005, CGCS2000 on 8003)
**type**:      single-coord-vrs
**access**:    paid; Tencent account (WeChat/QQ) required; no professional surveying licence needed
**yearly_cost**: ~¥998/yr (~$138/yr) at 2022 launch pricing; current 2025/2026 pricing unconfirmed
**stations**:  2,800+ virtual network stations; 33 provinces; 100% major urban road coverage
**source**:    lbs.qq.com/rtk (Tencent Location Service)
**operator**:  Tencent Location Service (lbs.qq.com)

Launched 2022 as free public beta; moved to paid at ~¥998/yr. No surveying licence required —
open to individuals. Requires a Tencent account (Chinese phone number typical for WeChat/QQ).
If current pricing matches 2022 launch, this is the sole sub-$200/yr commercial option in China.
Service status as of 2025/2026 not confirmed; verify at lbs.qq.com/rtk before recommending.

**investigate**: confirm current pricing and service availability at lbs.qq.com/rtk; verify
whether a non-Chinese Tencent account can be used to register.

---

## Paid — over cutoff or structurally restricted

Brief entries only.

---

## signal — SIGNAL (SI)

**status**:    paid
**host:port**: host:port not publicly listed (provided post-registration via gu-signal.si)
**type**:      VRS (network RTK)
**access**:    paid; registration at gu-signal.si
**yearly_cost**: €829.44/yr (~$905); €622.08 early-discount (~$680)
**stations**:  16 permanent CORS stations
**source**:    gu-signal.si
**operator**:  GURS — Geodetska uprava Republike Slovenije (Surveying and Mapping Authority)

---

## cypos — CYPOS (CY)

**status**:    paid
**country**:   CY
**type**:      VRS + iMAX + FKP + MAC
**host:port**: host:port not publicly listed (provided post-registration)
**access**:    paid subscription; register at portal.dls.moi.gov.cy
**registration**: `portal.dls.moi.gov.cy/en/application_forms/engrafi-cypos/`
**yearly_cost**: not publicly listed (rechecked 2026-04-30: no rate schedule on
               dls.moi.gov.cy or portal.dls.moi.gov.cy; ArduSimple's Cyprus NTRIP
               guide describes CYPOS only as "paid national service" with no
               figures). Tariff disclosed only after registration. DLS Portal
               itself confirmed alive 2026-04-30 (a 28-Apr-2026 maintenance
               notice was posted). No public phone/email for CYPOS specifically;
               general DLS contact via dls.moi.gov.cy.
**stations**:  7 permanent GNSS stations (free areas of the Republic)
**source**:    portal.dls.moi.gov.cy; helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf;
               ardusimple.com/rtk-correction-services-and-ntrip-casters-in-cyprus/
**operator**:  DLS — Department of Lands and Surveys, Ministry of Interior

CYPOS (Cyprus Positioning System) operational since 2010. Provides VRS, iMAX,
FKP, and MAC network RTK products. Available only in the government-controlled
areas (south / free areas); the northern third under the administration of
the Turkish Republic of Northern Cyprus is not covered.

---

## swepos — SWEPOS Network RTK (SE)

**status**:    paid
**access**:    paid; free DGNSS tier sub-metre only (out of scope)
**yearly_cost**: ~9,000 SEK/yr (~$850)
**source**:    lantmateriet.se

---

## cpos — CPOS/ETPOS (NO)

**status**:    paid
**access**:    paid
**yearly_cost**: NOK 8,000+/yr (~$740)
**source**:    kartverket.no

---

## swipos — swipos (CH)

**status**:    paid
**access**:    paid; *Geoinformationsgesetz* SR 510.62 classifies RTK as value-added service
**yearly_cost**: CHF 1,500/yr (~$1,650)
**source**:    swisstopo.admin.ch

---

## os_net — OS Net (GB)

**status**:    paid
**date_added**: 2026-04-29
**country**:   GB
**type**:      physical single-base / network RTK (VRS via resellers)
**host:port**: host:port not publicly listed; access only through licensed
               commercial resellers (HxGN SmartNet/Hexagon, TopNET Live/Trimble,
               AXIO-NET, Premium Positioning, SoilEssentials, Swift Navigation,
               Topcon)
**access**:    paid; OS Net raw streams licensed to seven commercial partners
               since 2005 under the OS licence model; Ordnance Survey does not
               offer a direct public NTRIP endpoint
**yearly_cost**: Reseller-dependent. Confirmed published tariffs (2026-04-30):
               • Leica HxGN SmartNet via SCCS Survey (`sccssurvey.co.uk/leica-smartnet.html`):
                 NRTK Unlimited £2,160/yr ex VAT (~$2,873), 2 yr £3,190 (~$4,243),
                 3 yr £4,480 (~$5,958); NRTK Limited 480 hrs/yr £1,300 (~$1,729);
                 DGNSS Unlimited £815/yr (~$1,084), DGNSS Limited 40 hrs/mo £490
                 (~$652). Free SmartRINEX post-processing included. UK VAT 20%.
               • Topcon TopNet Live via Drone Pilot Academy
                 (`dronepilotacademy.co.uk/product/topnet-live-vrs-license/`),
                 ex VAT: Unlimited 12 mo £1,700 (~$2,261), Limited 600 hrs/12 mo
                 £1,000 (~$1,330), Unlimited 6 mo £1,000, Unlimited 30 days £300
                 (~$399), **Unlimited 7 days £100 (~$133)**, plus tiny annual
                 hour-bucket packs from £100/5 hrs to £250/11 hrs. Optional
                 EE/roaming SIM add-ons £150–200/yr. Marketed to drone pilots
                 and hobbyists; no professional licence required.
               • Trimble VRS Now via Korec (`korecgroup.com/product/trimble-vrs-now/`)
                 listed as £POA; market estimates put it in the £600–£2,600/yr
                 band. Hitechniques (IE reseller, `hitechniques.ie`) lists a
                 1-yr / 600-hr Trimble VRS Now subscription at €590 (~$640) for
                 Ireland coverage — likely the closest published proxy.
               • AXIO-NET (FarmRTK), SoilEssentials (EssentialsNet), Premium
                 Positioning (RTK Premium), Point One (Polaris): no published
                 retail tariff confirmed in this pass.
**stations**:  ~110 physical CORS stations across Great Britain
**operator**:  Ordnance Survey (`ordnancesurvey.co.uk`)
**source**:    ordnancesurvey.co.uk/geodesy-positioning/os-net;
               sccssurvey.co.uk/leica-smartnet.html;
               dronepilotacademy.co.uk/product/topnet-live-vrs-license/;
               korecgroup.com/product/trimble-vrs-now/

No free hobbyist path exists via OS Net. The cheapest hobbyist on-ramp is
Topcon TopNet Live's 7-day Unlimited at £100 ex VAT — viable for a single
weekend project. Annual subscriptions are over the $200/yr cutoff regardless
of reseller. Volunteer bases on rtk2go/Centipede remain the only free option.

---

## osi_gnss — OSi Active GNSS Network (IE)

**status**:    restricted
**date_added**: 2026-04-29
**country**:   IE
**type**:      physical single-base (RINEX archive free; real-time via commercial VRS)
**host:port**: host:port not publicly listed for real-time; RINEX files
               downloadable free at `gnss.osi.ie`
**access**:    RINEX post-processing files: free, no registration required.
               Real-time NTRIP corrections: commercial only (Trimble VRS Now /
               HxGN SmartNet); OSi does not operate a public real-time caster.
**yearly_cost**: OSi's own service is free RINEX post-processing only — no
               real-time tariff exists to price. The closest published Irish
               real-time tariff (2026-04-30) is Trimble VRS Now via Hitechniques
               (`hitechniques.ie`) at €590/yr (~$640) for a 1-year, 600-hour
               subscription covering Ireland. HxGN SmartNet (Leica) also has IE
               coverage via UK partners (see `os_net` entry for SCCS tariffs).
               Reconfirmed via tailte.ie/services/geodetic/ — portal is
               migrating from gnss.osi.ie to gnss.tailte.ie in May 2026.
**stations**:  ~24 active GNSS reference stations (Republic of Ireland + OSNI
               collaboration for Northern Ireland)
**operator**:  OSi — Ordnance Survey Ireland, now Tailte Éireann
               (`tailte.ie/services/geodetic/`); migrating from `osi.ie`. OSNI —
               Ordnance Survey of Northern Ireland (`nidirect.gov.uk/osni`).
**source**:    tailte.ie/services/geodetic/; gnss.osi.ie (→ gnss.tailte.ie May 2026);
               hitechniques.ie

OSi's active GNSS network supports geodetic infrastructure and free RINEX
download but does not expose a public NTRIP stream for real-time RTK.
Hobbyists needing real-time corrections must use Trimble VRS Now (Hitechniques,
€590/yr / 600 h), HxGN SmartNet, or rely on volunteer bases (rtk2go ~12 IE,
Centipede ~9 IE).

---

## sirent — SiReNT (SG)

**status**:    paid
**date_added**: 2026-04-29
**country**:   SG
**type**:      VRS (network solution — RTK, DGNSS, PP On-Demand)
**host:port**: `203.127.20.71:2101`
**access**:    paid; 3-day trial (one per calendar month) with CorpPass or SingPass
               login — SingPass requires Singapore residency (NRIC/FIN); CorpPass
               requires a registered Singapore entity. Non-resident hobbyists have
               no viable access path without a Singapore corporate presence.
**registration**: `app.sla.gov.sg/sirent`
**yearly_cost**: SGD $107/month per receiver (~SGD $1,284/yr, ~$960/yr); volume
               tiers for 10–88 accounts at SGD $64.20 and SGD $32.10/month
**stations**:  ~8 physical reference stations covering the city-state
**source**:    sla.gov.sg/regulatory/property-boundaries/survey-reference-system

---

## soi_cors — SoI-CORS (IN)

**status**:    paid
**date_added**: 2026-04-29
**country**:   IN — India
**host:port**: `cors.surveyofindia.gov.in` (port not publicly listed)
**type**:      single-base + VRS
**access**:    paid; free only for Central/State Government and academic institutions
**yearly_cost**: ₹5,032/month (₹60,384/yr, ~$720/yr) for private users; over $200/yr cutoff
**stations**:  1,105+
**source**:    surveyofindia.gov.in

Promotional free 3-month window (Nov 2025–Jan 2026) expired. Worth revisiting if policy changes.

---

## tusaga — TUSAGA-Aktif / CORS-TR (TR)

**status**:    paid
**date_added**: 2026-04-29
**host:port**: `212.156.70.42:2101` (also port 55600)
**access**:    paid; one-off registration fee + annual RTK subscription. Fee set
               annually by BHİKPK (Inter-Ministerial Commission for Mapping Affairs);
               exact TRY amount not on public website. Universities and vocational
               schools may apply for free educational-area access via official letter
               to TKGM Harita Dairesi Başkanlığı.
**yearly_cost**: not publicly listed (contact tusaga-aktif.gov.tr, tel. 444 46 77);
               over $200/yr cutoff inferred
**stations**:  ~158 physical single-base GNSS stations (Turkey + Northern Cyprus);
               146 was earlier count, 12 border/Marmara stations added 2018
**source**:    tusaga-aktif.gov.tr; tkgm.gov.tr; harita.gov.tr

---

## vngeonet — VNGEONET (VN)

**status**:    paid
**host:port**: `vngeonet.vn:2101` (VRS); `:2102` (iMAX); `:2103` (single-base)
**type**:      physical-coord-vrs (VRS + iMAX + single-base mountpoints)
**access**:    fees since Sep 2024 per Circular 47/2024/TT-BTC; pricing not public;
               register at gddt.vngeonet.vn
**yearly_cost**: not publicly listed (fees per Circular 47/2024/TT-BTC since Sep 2024)
**stations**:  65
**source**:    vngeonet.vn (National Centre for Satellite Positioning Station Management /
               Trung tâm Quản lý trạm định vị vệ tinh quốc gia, Bộ TN&MT)

Was free until Aug 2024. Three-port caster: port 2101 VRS network solution, port 2102
iMAX network solution, port 2103 single-base. RTK account (case-sensitive) required;
create via gddt.vngeonet.vn.

---

## gnssnet_hu — GNSSnet.hu (HU)

**status**:    paid
**date_added**: 2026-04-29
**country**:   HU
**type**:      VRS (network RTK), single-base RTK, and DGNSS
**host:port**: `ntrip.gnssnet.hu:2101`
**access**:    paid; web registration at gnssnet.hu; one-time per-company connection fee
**registration**: `gnssnet.hu`
**yearly_cost**: All figures net of ÁFA (Hungarian VAT, 27%).
               One-time registration: 12,000 HUF (~€30) per company, regardless of service mix.
               Per-minute (default if no flat-rate subscription is active):
                 RTK 8 HUF/min, Network RTK 12 HUF/min, DGNSS 3 HUF/min
                 (RTK ≈ 480 HUF/hr ≈ €1.20/hr; Network RTK ≈ 720 HUF/hr ≈ €1.80/hr).
               Flat rates apply to RTK and Network RTK at the same price (DGNSS in parentheses):
                 30 days, within 50 km of a fixed coordinate: 15,000 HUF (DGNSS 6,000)
                 30 days, usable within a 365-day window:     36,000 HUF (DGNSS 12,000)
                 90 days, usable within a 365-day window:     72,000 HUF (DGNSS 24,000)
                 150 days, usable within a 365-day window:   108,000 HUF (DGNSS 36,000)
                 365-day continuous access:                  150,000 HUF (DGNSS 54,000)
               Annual flat rate ~€375 / ~$415 at ~400 HUF/EUR — over the $200/yr cutoff,
               but the 30-day local-radius (~€38) and per-minute tariffs are realistic
               hobbyist on-ramps for project work. Outside the 50 km radius the local
               flat rate falls back to per-minute billing without separate notice.
               Multi-subscription discount: −10% on the 2nd simultaneous flat-rate
               subscription of the same type/duration, −20% on the 3rd onwards (applied
               only to the second-and-further line items, not the first).
               Prices reflect Feb 2023 reduction; current schedule confirmed against
               `gnssnet.hu/pdf/gnss_valosideju_szolg_arak.pdf` (2026-04-30).
**source**:    gnssnet.hu; lechnerkozpont.hu/oldal/gnss;
               gnssnet.hu/pdf/gnss_valosideju_szolg_arak.pdf
**operator**:  Lechner Nonprofit Kft. (Lechner Tudásközpont / Lechner Knowledge Centre)

---

## egnss_tw — e-GNSS (TW)

**status**:    paid
**country**:   TW
**type**:      VRS (VBS-RTK network solution)
**host:port**: 210.241.63.193:81
**access**:    pay-per-use; web membership registration at egnss.nlsc.gov.tw/content.aspx?i=20150625102221503
**yearly_cost**: membership permit TWD 2,000/5-year period (~$60); VBS-RTK service TWD 300/receiver/day (~$9/day); annual-account contracts available for regular users; DGNSS service TWD 100/receiver/day
**stations**:  78 physical base stations (VBS virtual output)
**source**:    egnss.nlsc.gov.tw (NLSC/MoI — 國土測繪中心)

---

## myrtk — MyRTKnet (MY)

**status**:    paid
**date_added**: 2026-04-29
**country**:   MY
**type**:      VRS / single-base / network DGPS (multiple correction types: VRS,
               MAC, iMAX, SB Peninsular, SB Sabah & Sarawak, RINEX)
**host:port**: `pxy.myrtknet.gov.my:2101` (VRS/MAC/iMAX/DGPS),
               `:2102` (SB Sabah & Sarawak), `:2103` (SB Peninsular)
**access**:    paid; registration mandatory; cost-recovery basis under Survey Act;
               private-sector users pay both a one-time registration fee and an
               annual subscription fee; government departments pay reduced registration
**registration**: `myrtknet.jupem.gov.my`
**yearly_cost**: RM 1,000 one-time registration (private sector; RM 500 for
               government); RM 3,000/yr real-time subscription (~$855/yr at
               current rates). Over $200/yr hobbyist cutoff.
**stations**:  ~78 physical reference stations (Peninsular + Sabah + Sarawak)
**source**:    jupem.gov.my; myrtknet.jupem.gov.my

---

## pagenet — PAGeNet (PH)

**status**:    paid
**access**:    PHP 1,000 one-time + ongoing subscription (EO 471); 52 stations
**yearly_cost**: PHP 1,000 one-time (~$17) + subscription (ongoing amount not publicly listed)
**source**:    namria.gov.ph

---

## czepos — CZEPOS (CZ)

**status**:    paid
**date_added**: 2026-04-29
**country**:   CZ
**type**:      VRS (network solution)
**host:port**: czepos.cuzk.gov.cz:2101 (RTK3 MSM, RTCM 3.2); port 2111 (legacy Leica Spider proxy)
**access**:    free for public authorities, schools, universities, and students; all
               other users (commercial, hobbyist) charged under ČÚZK Decree 31/1995 Sb.
               as amended by 156/2023 Sb.: 10,000 CZK/yr (~€400) per receiver, or
               1,000 CZK/month. Registration at czepos.cuzk.gov.cz.
**yearly_cost**: 10,000 CZK/yr (~€400) per receiver (commercial); over €200/yr hobbyist cutoff
**stations**:  ~30 CZ permanent stations + 27 foreign-network stations; VRS only
**notes**:     Three service tiers: DGPS, RTK (single-base), VRS3 (network solution).
               Not a general hobbyist path. Centipede has ~3 CZ nodes, rtk2go ~4 CZ bases
               as volunteer alternative.

---

## skpos — SKPOS (SK)

**status**:    paid
**date_added**: 2026-04-29
**country**:   SK
**type**:      VRS (network solution)
**host:port**: skpos.gku.sk:2101 (IP fallback: 193.93.74.56)
**access**:    free for public-sector bodies and municipalities; all other users
               (commercial, hobbyist) paid via SKPOS online shop at
               skposonlineobchod.gku.sk. Pricing not publicly listed without login;
               GKÚ raised rates in December 2022. Slovakia uses EUR.
               Registration at skpos.gku.sk/register/.
**yearly_cost**: not publicly listed (requires login to online shop); over €200/yr cutoff inferred
**stations**:  ~26 SK permanent reference stations; VRS only (SKPOS_cm service)
**notes**:     Three service tiers: SKPOS_dm (decimetre, code), SKPOS_cm (centimetre, RTK/VRS),
               SKPOS_mm (post-processing). Not a general hobbyist path. rtk2go ~2 SVK bases,
               Centipede ~2 SVK nodes as volunteer alternative.

---

## agros — AGROS (RS)

**status**:    paid
**date_added**: 2026-04-29
**country**:   RS
**type**:      VRS (Trimble VRS Now backbone)
**host:port**: agros.rgz.gov.rs:2101
**access**:    paid; registration via rgz.gov.rs (Serbian portal)
**yearly_cost**: 8,688 RSD/yr (~€74/yr) RTK flat-rate; 5,379 RSD/yr (~€46/yr) DGPS flat-rate; hourly/monthly packages available
**stations**:  ~30 permanent CORS
**source**:    rgz.gov.rs (Republički geodetski zavod — RGZ)

Serbia's national CORS network. RTK flat-rate is paid-affordable (~€74/yr, under $200/yr cutoff).
Pricing confirmed from official Uredba (regulation) published by RGZ; Serbian portal only.

---

## geonet_bg — GeoNet Bulgaria GEO-RTK (BG)

**status**:    paid
**date_added**: 2026-04-29
**country**:   BG
**type**:      VRS (network RTK)
**host:port**: not publicly listed (contact via geonet.bg)
**access**:    paid; pricing not published on website
**yearly_cost**: not publicly listed (contact geonet.bg)
**source**:    geonet.bg
**operator**:  GeoNet Bulgaria (private company)

GEO-RTK is GeoNet Bulgaria's commercial network RTK / VRS service. Provides absolute
position accuracy within ~2 cm. No free hobbyist tier; pricing requires direct contact
with the operator. GCSES (the state Geodesy, Cartography and Cadastre Agency) operates
government reference stations but provides no public NTRIP caster.

---

## montepos — MONTEPOS (ME)

**status**:    paid
**date_added**: 2026-04-29
**country**:   ME
**type**:      VRS-capable (9 CORS locations)
**host:port**: not publicly listed (contact Uprava za nekretnine, Podgorica)
**access**:    paid subscription tiers: 24 h, 48 h, 1 month, 3 months, 6 months, 1 year, 2 years
**yearly_cost**: not published on official page (contact gov.me/clanak/montepos); Montenegro uses EUR
**stations**:  ~9 permanent CORS stations
**source**:    gov.me (Uprava za nekretnine — Real Estate Administration)

Montenegro's national CORS/VRS network. Subscription required for all tiers; no free access.
Registration and pricing via gov.me/clanak/montepos or direct contact with the agency.

---

## bihos — BiHPOS (BA)

**status**:    paid
**date_added**: 2026-04-29
**country**:   BA
**type**:      VRS-capable; dual-entity administration
**host:port**: not publicly listed; FBiHPOS: contact fgu.com.ba; SRPOS: contact rgurs.org/srpos
**access**:    paid; two independent geodetic authorities: FGU (FBiH) and RGURS (Republika Srpska)
**yearly_cost**: not published on public website; flexible periods (yearly, monthly, other) per RGURS documentation
**stations**:  34 (17 FBiHPOS + 17 SRPOS); EU-funded; operational since 2011
**source**:    fgu.com.ba (Federal Geodetic Administration) + rgurs.org (Republic Authority for Geodetic and Property Affairs, Republika Srpska)

Bosnia and Herzegovina's GNSS reference station network, implemented as part of the EU BiHPOS project.
Split between two entities with separate control centres and subscription processes.
FBiHPOS covers the Federation of BiH; SRPOS covers Republika Srpska; the two control centres
exchange data across entity boundaries.

---

## kopos — KOPOS / Kosovo Positioning System (XK)

**status**:    paid
**date_added**: 2026-04-29
**country**:   XK
**type**:      VRS (8 CORS stations + computation centre in Pristina)
**host:port**: not publicly listed (contact AKK via akk.rks-gov.net)
**access**:    paid; registration via akk.rks-gov.net
**yearly_cost**: not publicly listed on website (contact Kosovo Cadastral Agency)
**stations**:  8 permanent CORS; RTK horizontal ±2 cm, vertical ±4 cm
**source**:    akk.rks-gov.net (Agjencia Kadastrale e Kosovës — Kosovo Cadastral Agency)

Kosovo's national GNSS reference network. Established by the Kosovo Cadastral Agency
(AKK) as an EUPOS-aligned CORS network. Paid subscription required; no free hobbyist
tier confirmed. Pricing not published on public web pages — contact AKK directly.
No free public NTRIP endpoint confirmed.

---

## sstp_by — ССТП РБ / Belgeodesiya CORS (BY)

**status**:    restricted
**date_added**: 2026-04-29
**country**:   BY — Belarus
**type**:      network RTK (VRS-capable; 98 CORS)
**host:port**: not publicly listed (contact geo.by)
**access**:    paid; signed contract required with РУП «Белгеодезия»;
               no self-service registration portal; organisations only
**yearly_cost**: not published on public website; tariffs coordinated with
               Госкомимущество (State Committee for Property); periodic options
               include 1, 3, 6, and 12-month subscriptions (geo.by/services/sstp)
**stations**:  ~98 continuously operating reference stations (national coverage)
**operator**:  РУП «Белгеодезия» (Belgeodesiya state enterprise),
               under Государственный комитет по имуществу Республики Беларусь
               (State Committee for Property — Госкомимущество)
**registration**: https://geo.by/services/sstp/predostavlenie-informatsii-sstp

Belarus national CORS network (Спутниковая система точного позиционирования — ССТП РБ).
Provides RTK and DGPS differential corrections plus RINEX post-processing files.
Since March 2020 Belgeodesiya feeds data to two EPN analytical centres, making
selected stations nominally IGS-adjacent, but the RTK correction service is
entirely separate and not publicly accessible.

Access is restricted to organisations holding a current contract. No hobbyist or
individual self-signup path exists. Host:port is not disclosed on the public website;
connection credentials are issued per-contract.

Hardware supply: EU, UK, and US sanctions applied to Belarus since 2020–2022 suspend
exports of surveying and precision-GNSS equipment (Topcon, Trimble, Leica all announced
suspension). Replacement rover hardware is materially harder to source than in
unsanctioned neighbouring states, compounding the barriers to hobbyist RTK use.

**missing**: confirm current host:port and annual tariff level (BYN) from geo.by
tariff documentation or industry contact.

---

## scrtn — SCRTN (US-SC)

**status**:    paid
**access**:    paid subscription; pricing via scdot.org
**yearly_cost**: not publicly listed (contact SCDOT)
**source**:    scdot.org (South Carolina Department of Transportation)

---

## ncrtn — NCRTN (US-NC)

**status**:    paid
**access**:    paid; subscription via ncems.org
**yearly_cost**: ~$500/yr
**source**:    ncems.org (North Carolina Emergency Management / NCDOT)

---

## tdot_rtn — TDOT RTN (US-TN)

**status**:    paid
**access**:    paid; subscription via tn.gov/tdot
**yearly_cost**: ~$450/yr
**source**:    tn.gov/tdot (Tennessee Department of Transportation)

---

## turn_gps — TURN GPS (US-UT)

**status**:    paid
**access**:    paid; subscription via turngps.org
**yearly_cost**: ~$600/yr
**source**:    turngps.org (State of Utah)

---

## mtsrn — MTSRN (US-MT)

**status**:    paid
**access**:    paid; subscription via mdt.mt.gov
**yearly_cost**: ~$1,500/yr
**source**:    mdt.mt.gov (Montana Department of Transportation)

---

## wsrn — WSRN (US-WA)

**status**:    paid
**access**:    paid; subscription via wsdot.wa.gov
**yearly_cost**: ~$1,900/yr
**source**:    wsdot.wa.gov (Washington State Department of Transportation)

WSRN is operated by WSDOT with PANGA/CWU contributing antennae, communications,
and data archiving for Puget Sound stations. Multiple correction formats per
station (RTCM 3.1, RTCM 3.2 MSM, CMR+). Free tier not publicly documented.

---

## crtn — CRTN / California Real Time Network (US-CA)

**status**:    paid-affordable
**host:port**: `132.239.152.4:2102` (NorCal zones 1–2), `:2103` (NorCal zones 3–4),
               `:2104` (SoCal zone 5), `:2105` (SoCal zone 6)
**type**:      single-base
**access**:    paid; one-time $100 processing fee; universities and schools exempt
**yearly_cost**: $100 one-time (under the $200 cutoff) — not annual
**stations**:  ~250 across California (clearinghouse, see below)
**source**:    sopac-csrc.ucsd.edu/index.php/crtn (Scripps Orbit and Permanent Array
               Center, UC San Diego)
**operator**:  CSRC EC / SOPAC at UCSD

Clearinghouse for real-time GNSS data from multiple California networks: SOPAC
(SCIGN), UC Berkeley/USGS Menlo Park (BARD), USGS Pasadena (SCIGN),
Caltrans (CVSRN), Orange County Public Works (OCRTN), and EarthScope NOTA
stations. RTCM 3.0, 1 Hz, latency <1 s. Registration via the CRTN Registration
form (linked from the SOPAC page); credentials issued in 7+ days. The $100
processing fee is one-time and falls below the project's $200/yr affordability
cutoff — surfaced in UI as a paid-affordable info marker rather than an
in-pipeline entry. Significant station overlap with `earthscope` (already in
pipeline, free with annual NULA non-commercial agreement) — same physical
antennae are reachable through either caster.

---

## bard — BARD / Bay Area Regional Deformation network (US-CA)

**status**:    free
**host:port**: no independent caster — streams disseminated via `crtn`
**type**:      single-base (physical stations)
**access**:    via SOPAC CRTN (paid-affordable, one-time $100) or EarthScope NOTA
               (free, in-pipeline, annual NULA)
**stations**:  ~40 continuously operating GNSS receivers in Northern California
**source**:    seismo.berkeley.edu/bard (UC Berkeley Seismological Laboratory) /
               ncedc.org (NCEDC archive)
**operator**:  UC Berkeley BSL + USGS Menlo Park, supported by USGS and Cal OES

BARD is a 40-station crustal-deformation network around the San Francisco Bay
and Northern California. It is a research/monitoring array, not a standalone
public NTRIP service: real-time RTCM streams are exposed via SOPAC CRTN
(see `crtn`), and 24-hour RINEX archives via NCEDC. Many BARD stations are
also archived in EarthScope NOTA, so the same physical antennae can be reached
through the in-pipeline `earthscope` source. Listed for documentation; no
separate pipeline entry. Country-marker route is `crtn` (info) plus the
existing `earthscope` pins — duplicate pins at shared coordinates are
expected and tolerated by the renderer.

---

## panga — PANGA / Pacific Northwest Geodetic Array (US-WA, OR, ID)

**status**:    free
**host:port**: no independent public caster
**type**:      single-base (physical stations)
**access**:    via EarthScope NOTA (free, in-pipeline, annual NULA) or WSRN
               (paid, ~$1,900/yr) for the Washington subset
**stations**:  ~220 PANGA-operated CWU sites + ~700 NOTA stations processed
               at the CWU Geodesy Laboratory
**source**:    panga.org / geodesy.cwu.edu (Central Washington University
               Geodesy Laboratory)
**operator**:  CWU Geodesy Lab; UNAVCO/EarthScope for NOTA-operated sites

PANGA is a research array spanning the Pacific Northwest and the wider Cascadia
subduction zone. Real-time data are telemetered to CWU and processed in-house
(JPL RTG, Trimble RTKNet) for hazard monitoring; CWU does not operate a public
hobbyist NTRIP caster. Hobbyists in WA / OR / ID reach the same physical
stations through `earthscope` (in-pipeline, free) or — for Washington — through
`wsrn` (paid). Listed for documentation; no separate pipeline entry. Same
duplicate-pin caveat as BARD.

---

## prsn_cors — Puerto Rico Seismic Network CORS (PR)

**status**:    free
**country**:   PR — Puerto Rico (US territory)
**type**:      single-base (physical CORS)
**host:port**: not publicly listed
**access**:    research/academic registration via UPRM; free for qualifying users;
               hobbyist self-service registration not confirmed
**registration**: `prsn.uprm.edu/English/research/geodesy/NTRIP_info.php`
**stations**:  18–24 permanent GNSS stations (Puerto Rico, adjacent islands, USVI)
**operator**:  Puerto Rico Seismic Network (PRSN), University of Puerto Rico Mayagüez
               (UPRM)
**yearly_cost**: n/a (academic/research service; pricing not publicly stated)

**date_added**: 2026-04-29

The PRSN is one of the densest CORS networks in the world relative to territory size.
Its GNSS infrastructure spans Puerto Rico, nearby smaller islands, and extends into
the US and British Virgin Islands (~18–24 stations as of 2016 literature; exact current
count not confirmed). The PRSN website documents an NTRIP service for real-time
corrections (RTCM streams), but the caster host:port is not advertised on open-access
pages — the service appears oriented toward academic and government users who register
with UPRM. The NSF and NOAA partially funded the network. EarthScope NOTA (`earthscope`)
independently streams several PRVI-region stations (COCONet / NOTA overlap). Hobbyists
who cannot obtain PRSN credentials fall back to EarthScope NOTA.

**missing**: confirm current host:port and whether hobbyist registration is available
via `prsn.uprm.edu`; verify current station count and whether any mountpoints appear
on rtk2go or in EarthScope sourcetable.

---

## vrs_pr — VRS Systems PR (PR)

**status**:    paid
**country**:   PR — Puerto Rico (US territory)
**type**:      VRS (virtual reference station)
**host:port**: not publicly listed
**access**:    paid subscription (commercial service); contact HLCM Group
**registration**: `hlcmgroup.com/vrs.php`
**stations**:  8 physical GNSS receivers providing island-wide VRS coverage
**operator**:  HLCM Group, Inc. (Bayamón, Puerto Rico)
**yearly_cost**: not publicly listed (contact HLCM Group, tel. 787-398-8852)

**date_added**: 2026-04-29

VRS Systems PR is the only commercial VRS network in Puerto Rico. HLCM Group owns and
operates all eight antenna sites and internet access points, enabling it to guarantee
service continuity. The network was upgraded in July 2022 to support Galileo and BeiDou
(four-constellation: GPS + GLONASS + Galileo + BeiDou) using Trimble Pivot Platform
GNSS Real-Time Network software. The service is marketed at surveying, mapping/GIS,
construction, and agriculture professionals. Pricing is not disclosed on the public
website; out of scope for the map (paid, no free tier) but documented for completeness.

---

## bc_rtn — BC RTN (CA-BC)

**status**:    paid
**access**:    paid regional subscription; contact GeoBC via gov.bc.ca/geobc
**yearly_cost**: not publicly listed
**source**:    gov.bc.ca/geobc (Province of British Columbia)

British Columbia real-time network. No free tier. No Canadian province offers free
public NTRIP — confirmed across all ten provinces and three territories.

---

## nsacs — Nova Scotia NSACS (CA-NS)

**status**:    paid
**access**:    RINEX post-processing free via NRCan; real-time NRTK via paid commercial
**yearly_cost**: not publicly listed (varies by commercial reseller: Can-Net, HxGN SmartNet, Brandtnet)
               providers only: Can-Net/Cansel (`gps.can-net.ca:2300`), HxGN SmartNet
               NA, Brandtnet (`rtk.brandt.ca`)
**stations**:  40
**source**:    novascotia.ca (Nova Scotia Spatial Services)

Nova Scotia Active Control System — 40 permanently installed government GNSS receivers
forming the NSCRS (Nova Scotia Coordinate Referencing System). Province owns the
stations; three commercial providers access the ACS data under data-licensing agreements
and sell real-time NRTK subscriptions. No free real-time tier; no direct provincial
NTRIP caster.

---

## dvrs — DVRS (AE)

**status**:    paid
**access**:    restricted; professional application via dm.gov.ae (Dubai Municipality)
**yearly_cost**: not publicly listed (professional application required)
**stations**:  18+
**source**:    dm.gov.ae (Dubai Municipality)

Dubai Virtual Reference System. 18+ 4-constellation reference stations covering Dubai
Emirate. Access is by formal professional application only (licensed engineering/surveying
firms) — no individual or hobbyist registration path.

---

## regpmoc — REGPMOC (PE)

**status**:    paid
**host:port**: `190.12.71.75:2101`
**type**:      physical-coord-vrs
**access**:    restricted; MoD-issued licence required (professional/commercial only)
**yearly_cost**: not publicly listed (MoD-issued licence required)
**stations**:  unknown
**source**:    ign.gob.pe (IGN — Instituto Geográfico Nacional, under Ministry of Defence)

Red Geodésica Permanente de Monitoreo Continuo. Government CORS network operated by
Peru's IGN under the Ministry of Defence. Host:port is publicly known (190.12.71.75:2101)
but stream access requires an official licence — no general hobbyist path.

---

## igrs — IGRS (IQ)

**status**:    weird
**access**:    restricted; no public NTRIP caster identified
**yearly_cost**: N/A (no public NTRIP caster)
**stations**:  7
**source**:    Not publicly listed (Iraq Geodetic Reference System)

Only 7 reference stations at 500–800 km inter-station spacing — far too sparse for
RTK (baseline ≫ 100 km). No public NTRIP caster found. Documented for completeness;
not a usable RTK resource for hobbyists.

---

## dag_lb — Directorate of Geographic Affairs (LB)

**status**:    free
**date_added**: 2026-04-29
**country**:   LB
**type**:      unknown
**host:port**: not publicly listed
**access**:    no confirmed public NTRIP
**registration**: lebarmy.gov.lb (military directorate; no hobbyist portal)
**yearly_cost**: N/A
**stations**:  unknown
**operator**:  Directorate of Geographic Affairs (مديرية الشؤون الجغرافية), Lebanese Armed Forces

Lebanon's sole national geodetic authority. Established by law on 6 February 1962
under the Ministry of National Defence; responsibilities include triangulation,
elevation measurement, aerial photography, and official mapping. No public NTRIP
caster, open sourcetable, or hobbyist registration portal has been found in any NTRIP
directory, academic publication, or government source.

The country's post-2019 financial collapse (GDP roughly halved by 2024, banking
system insolvent) makes hardware imports and ongoing operational fees prohibitive.
The 2023–2024 Israel-Hezbollah war caused approximately US$11 billion in infrastructure
damage. Pervasive military GNSS spoofing active since October 2023 across
Israel/Lebanon/Jordan/Sinai renders RTK corrections unreliable across southern Lebanon
and the Bekaa Valley regardless of correction source.

Zero LB stations on rtk2go or Centipede as of 2026-04-29.

Deferred indefinitely. Do not pursue until a confirmed public NTRIP endpoint appears
in an NTRIP directory or official Lebanese government announcement.

---

## ges_syria — General Establishment for Survey (SY)

**status**:    free
**date_added**: 2026-04-29
**country**:   SY
**type**:      unknown
**host:port**: not publicly listed
**access**:    no confirmed public NTRIP
**yearly_cost**: N/A
**stations**:  unknown
**source**:    not publicly listed (General Establishment for Survey / المؤسسة العامة للمساحة)
**operator**:  General Establishment for Survey, Syrian Arab Republic

Syria's national mapping authority. No public NTRIP caster, open sourcetable, or
hobbyist registration portal has been found. Pre-war research GNSS stations existed
(Damascus, Aleppo universities; Syrian Geological Survey), but no public RTK streaming
service was ever deployed. The 2011–2024 civil war severely disrupted all geodetic
infrastructure. The Assad regime fell December 2024; a transitional government was
formed March 2025. US sanctions were largely lifted by OFAC General Licence 25 (May
2025) and Executive Order (June 2025); EU/UK sanctions eased in parallel, though some
export restrictions on dual-use equipment remain.

Deferred until geodetic reconstruction produces a confirmed public NTRIP endpoint — a
long-term outcome requiring re-establishment of the national reference frame and CORS
deployment. Do not pursue until EUREF, IGS, or direct government sources confirm an
operational caster.

---

## otc_gnss — OTC GNSS (TN)

**status**:    paid
**date_added**: 2026-04-29
**country**:   TN
**type**:      single-base (physical coordinates)
**host:port**: not publicly listed (disclosed after subscription)
**access**:    paid subscription; register at otc.nat.tn/geodesy/gnss/subscription
**yearly_cost**: not publicly listed (contact commercial department)
**stations**:  23 (physical; Saharan region not covered)
**source**:    otc.nat.tn (OTC — Office de la Topographie et de la Cartographie)
**operator**:  OTC (Ministère de l'Équipement et de l'Habitat, Tunisia)

Office de la Topographie et de la Cartographie national GNSS network. 3 stations
installed 2005 (Tunis, Monastir, Sfax); expanded to 23 with 20 additional stations
distributed across non-Saharan Tunisia in 2010; fully operational since 2011. Each
station is equipped with a weather sensor (temperature, pressure, humidity). Network
referenced to WGS84–ITRF 2000 (NTT — Nouveau Système Tunisien de Triangulation).
RTK corrections delivered via NTRIP subscription; NTRIP host:port not published
openly. No free tier. No hobbyist self-service registration path found.

---

## rjgc_cors — RJGC CORS (JO)

**status**:    free
**date_added**: 2026-04-29
**country**:   JO
**type**:      unknown
**host:port**: not publicly listed
**access**:    restricted; no public self-service registration found
**yearly_cost**: N/A (no confirmed public NTRIP)
**stations**:  unknown
**source**:    rjgc.gov.jo (RJGC — Royal Jordanian Geographic Centre)
**operator**:  Royal Jordanian Geographic Centre (RJGC)

RJGC maintains geodetic reference stations and CORS infrastructure for Jordan's
national spatial reference system and cadastral use. No public NTRIP caster,
open sourcetable, or hobbyist registration portal has been found. RJGC provides
geospatial data and maps to government and private sectors; real-time RTK access,
if available, appears restricted to licensed users. Deferred until a confirmed
public endpoint is found.

Note: ACOR (American Center of Research, Amman, acorjordan.org/ntrip-network/)
operates a single GNSS NTRIP base station at its Tla' Ali campus for
archaeological field research — contact-based access, not a public service,
useful only within ~30–40 km of central Amman.

Note on spoofing: pervasive military GNSS spoofing active continuously since
Oct 2023 across Israel/Lebanon/Jordan/Sinai/Cyprus makes RTK corrections
unreliable across much of Jordan regardless of NTRIP source availability.

---

## pak_rehber — Pak-Rehber (PK)

**status**:    paid
**access**:    restricted; authorized users only — contact suparco.gov.pk (SUPARCO)
**yearly_cost**: not publicly listed (authorized users only)
**stations**:  unknown
**source**:    suparco.gov.pk (SUPARCO — Space and Upper Atmosphere Research Commission)

Government NRTK service delivering cm-level corrections to "authorized users." No
public-facing NTRIP host:port, open registration portal, or sourcetable found.
Access requires direct contact with SUPARCO. Pak-SBAS (sub-metre satellite corrections,
L-band) is a separate out-of-scope service also under SUPARCO.

---

## slcorsnet — SLCORSnet (LK)

**status**:    paid
**country**:   LK — Sri Lanka
**type**:      physical-coord-vrs (VRS / FKP / MAC)
**host:port**: `222.165.190.67:2101`
**access**:    paid subscription — 1-day, 7-day, 30-day, and annual licence tiers;
               registration at slcorsnet.survey.gov.lk
**yearly_cost**: not publicly listed (requires portal login to view pricing)
**registration**: slcorsnet.survey.gov.lk
**stations**:  unknown (Phase 1: Western Province and surroundings; island-wide rollout ongoing)

**date_added**: 2026-04-29

Sri Lanka Continuously Operating Reference Station Network, operated by the Survey
Department of Sri Lanka (Surveyor General's Office, Colombo). Established end of 2016.
Physical GNSS reference stations transmit raw data to a Control Centre for network
processing; real-time RTCM corrections delivered via VRS, FKP, or MAC. Post-processing
RINEX and autonomous GNSS post-processing (SSRPOST / GNWEB) also available. Payments
via local or international debit/credit card to the Department of Survey's bank account.
Host:port `222.165.190.67:2101` identified from public "How to Use" documentation.
Not added to pipeline — paid service; pricing not confirmed under $200/yr cutoff.

---

## corsnet_lk — CORSnet (LK)

**status**:    rejected
**country**:   LK — Sri Lanka
**type**:      physical-coord-vrs (VRS)
**host:port**: not publicly listed (credentials supplied on registration)
**access**:    paid commercial subscription; pricing not publicly listed (contact via
               corsnet.lk/user/register/)
**yearly_cost**: not publicly listed
**registration**: corsnet.lk/user/register/
**stations**:  ~15+ (island-wide coverage claimed)

**date_added**: 2026-04-29

Sri Lanka's first and largest private RTK network, established 2014. Originally
implemented by Suleco (Pvt) Ltd; now operated by CORSnet (Pvt) Ltd. Provides
centimetre-level RTK corrections island-wide via NTRIP/TCP. Sectors served include
surveying, construction, GIS, drone operations, and agricultural machinery. Accuracy
quoted as 2.5 mm + 0.5 ppm (static) and 15 mm + 1 ppm (RTK). Pricing not published.
Rejected — paid commercial with no confirmed pricing under $200/yr cutoff.

---

## kazgeodesy — KazGeoDesy (KZ)

**status**:    paid
**access**:    restricted; institutional licence or commercial reseller contract required
**yearly_cost**: not publicly listed
**stations**:  120+
**source**:    Not publicly listed (Committee on Land Management, Republic of Kazakhstan)

120+ CORS stations concentrated around Almaty, Astana, and the northern corridor.
No open self-service registration — access through official institutional channels
or a commercial reseller. Country is ~2.7 million km²; baselines will be long
outside urban centres even with a subscription.

---

## almgc_tj — State Committee for Land Management and Geodesy (TJ)

**status**:    free
**country**:   TJ
**access**:    restricted; no public NTRIP endpoint found
**yearly_cost**: not publicly listed
**source**:    zamin.tj (State Committee for Land Management and Geodesy)
**host:port**: not publicly listed

**date_added**: 2026-04-29

The State Committee for Land Management and Geodesy (Государственный комитет
по земельному управлению и геодезии) operates GNSS equipment for cadastral
and land-reform work across Tajikistan, supported by the "Fazo" Institute.
A national geodetic GNSS network was established partly through the World
Bank Land Registration and Cadastre System project (~2005–2012). No public
NTRIP caster or open self-service CORS endpoint has been identified.
CAIAG (Central Asian Institute for Applied Geosciences) maintains one
permanent GNSS station in the Pamir region as part of its 30-station
Central Asia seismic monitoring network; this is a research facility and
does not provide an RTK correction service.
Rejected — no public endpoint. Deferred pending discovery of open endpoint.

---

## kyrpos — KyrPos GNSS Network (KG)

**status**:    free
**country**:   KG
**type**:      single-base / VRS (unclear from public documentation)
**access**:    paid; contract-based sign-up, no self-service portal
**yearly_cost**: 3,180 KGS/month (~$437/yr at ~87 KGS/USD, April 2026);
                 170 KGS/day rate also offered
**operator**:  State Agency for Land Resources, Cadastre, Geodesy and
               Cartography of the Kyrgyz Republic (ГАЗРКГК — Государственное
               агентство земельных ресурсов, кадастра, геодезии и
               картографии)
**registration**: gosreg.gov.kg/ru/forma-onlajn-podklyucheniya/ — download
                  contract form, complete with receiver details and connection
                  period, submit to agency; credentials issued after signing
**host:port**: not publicly listed (disclosed after contract registration)
**stations**:  unknown

**date_added**: 2026-04-29

KyrPos is the national GNSS correction network operated by the Kyrgyz
cadastral and geodesy agency (ГАЗРКГК). Subscribers pay per month per
receiver; the minimum period is one month. No host:port or mountpoint list
is visible on the public website. Over the $200/yr threshold — not viable
for most hobbyists.

CAIAG (Central Asian Institute for Applied Geosciences, German-funded,
Bishkek) operates a monitoring network of 30+ GNSS stations including the
Bishkek IGS site (BIK0 / BIS2, joint with ESA/ESOC since 2016) and an
IGS tracking station at the Pamir High Mountain Observatory. These are
research facilities and do not provide an RTK correction service.

Rejected (paid, over cutoff). Deferred — no free or affordable public
NTRIP endpoint in Kyrgyzstan.

---

## tm_cors — Turkmenistan National CORS Network (TM)

**status**:    free
**country**:   TM
**type**:      single-base (physical CORS)
**access**:    restricted; government-internal use only, no public endpoint found
**yearly_cost**: not publicly listed
**operator**:  Ministry of Agriculture and Land Resources Service of
               Turkmenistan, supported by FAO
**host:port**: not publicly listed
**stations**:  65 (acquired 2022–2025 per FAO project documentation)

**date_added**: 2026-04-29

A 65-station CORS network was built under a 2022–2025 FAO-supported project
(Technical Assistance to Support the Establishment of Digital Land Cadastre
in Turkmenistan). The network underpins national cadastral surveying and
land administration. No public NTRIP endpoint, registration portal, or
pricing has been found. Turkmenistan has one of the most restricted
information environments in Central Asia; all geodetic infrastructure is
treated as government-internal. No IGS stations in Turkmenistan.

Rejected — no public endpoint, no hobbyist path. Deferred pending any
change in government data-access policy.

---

## azpos — AzPOS (AZ)

**status**:    free
**country**:   AZ
**type**:      single-base (physical CORS)
**access**:    paid; contract required — no self-service registration
**host:port**: not publicly listed (disclosed after service agreement)
**operator**:  State Committee on Property Issues (Əmlak Məsələləri Dövlət
               Xidməti) / Design Research Centre for Cadastre & Land Management
               (Kadastr və Yer Quruluşu Layihə Tədqiqat Mərkəz)
**registration**: emlak.gov.az (apply via the operator; agreement-based)
**yearly_cost**: not publicly listed (contract-based commercial pricing)
**stations**:  ~45 physical CORS (37 original across AZ + 8 restored in
               Karabakh region 2024: Fuzuli, Jebrail, Zangilan, Kəlbəcər ×2,
               Ağdam, Şuşa, Laçın)
**signals**:   GPS, GLONASS, Galileo
**nmea_filter**: n/a (not in pipeline)

**date_added**: 2026-04-29

AzPOS (Azerbaijan Positioning Observation System) is the national CORS network
operated by the State Committee on Property Issues under the Ministry of Economy
of Azerbaijan. Originally established with 37 stations at ~30–40 km spacing
covering mainland Azerbaijan, 8 stations were restored in the formerly occupied
Karabakh region in 2024 following the September 2023 Azerbaijani military
operation that restored full territorial control. Station placement was
validated with Leica GS18 receivers. The network provides RTK and DGNSS
post-processing services for cadastral, mapping, and engineering applications.
Access requires a signed service agreement; pricing and host:port details are
disclosed only after contracting with the operator. No free or hobbyist tier
identified.

Rejected — paid/contract-only. No public NTRIP endpoint.
**missing**: pricing and host:port — contact operator via emlak.gov.az.

---

## armpos — ARMPOS (AM)

**status**:    free
**country**:   AM
**type**:      single-base (physical CORS)
**access**:    restricted; no public self-service registration found
**host:port**: not publicly listed
**operator**:  State Committee for Real Property Cadastre of the Republic of
               Armenia (Անշարժ Գույքի Կադաստրի Պետական Կոմիտե / Cadastre Committee)
**registration**: cadastre.am (for licensed surveyors and government agencies)
**yearly_cost**: not publicly listed
**stations**:  12 physical single-base stations (full national coverage)
**signals**:   GPS, GLONASS (Leica infrastructure)
**nmea_filter**: n/a (not in pipeline)

**date_added**: 2026-04-29

ARMPOS (Armenian CORS) was commissioned in 2013 by the State Committee for Real
Property Cadastre with Norwegian government funding (NOK 9.8 million) and
supervision by the Norwegian Mapping Authority (Statens kartverk). Twelve
permanently installed reference stations cover the full territory of Armenia;
the associated coordinate reference system is ARMREF02. The system is designed
for real-time NTRIP RTK (metre, sub-metre, centimetre) and post-processing
(centimetre/sub-centimetre). Access is limited to licensed surveyors and
government cadastre users; no open hobbyist registration or publicly listed
host:port found. The State Committee is the sole owner of the network.

Rejected — restricted access, no public NTRIP endpoint.
**missing**: public NTRIP host:port and access conditions — contact Cadastre
Committee via cadastre.am.

---

## geocors_ge — GeoCors (GE)

**status**:    free
**country**:   GE
**type**:      single-base (physical CORS)
**access**:    paid; registration required (Leica Spider Business Center)
**host:port**: `geocors.napr.gov.ge:2101` (standard SBC port; pricing not public)
**operator**:  National Agency of Public Registry (NAPR), Ministry of Justice
               of Georgia (საჯარო რეესტრის ეროვნული სააგენტო)
**registration**: geocors.napr.gov.ge/SBC/Account/Register
**yearly_cost**: not publicly listed (paid subscription; contact NAPR)
**stations**:  23 physical single-base CORS — 7 Class A (national geodetic frame)
               + 16 Class B (regional densification)
**signals**:   GPS, GLONASS (Leica Spider platform)
**nmea_filter**: n/a (not in pipeline)

**date_added**: 2026-04-29

GeoCors is Georgia's national CORS network, established since 2010 under the
National Agency of Public Registry (NAPR), a legal-entity public-law body
under the Ministry of Justice. The 23-station network is divided into 7 Class A
stations forming the unified national spatial grid and 16 Class B stations
providing denser regional coverage. The Leica Spider Business Center platform
handles subscription management; a Sign Up page exists at the SBC URL.
The service targets licensed surveyors and cadastral users. Pricing is not
listed on the public website; the intended NTRIP port is 2101 (standard SBC
default). The 2024–2025 Georgian political crisis (disputed parliamentary
election) has not been reported to affect the technical operation of GeoCors.

Rejected — paid/subscription, pricing and access terms not publicly documented.
**missing**: pricing, mountpoint list, and confirmed access conditions for
non-professional users.

---

## netgeo — NetGEO (IT — national)

**status**:    paid
**access**:    paid
**yearly_cost**: ~€360/yr (~$390)
**source**:    netgeo.it (TopNET Live)

Commercial RTK network covering Italy. Includes some publicly-funded reference stations
made available commercially after regional network restructuring (e.g. Emilia-Romagna).

---

## pegasonow — PegasoNow (IT — national)

**status**:    paid
**access**:    commercial subscription; pricing not publicly listed
**yearly_cost**: not publicly listed
**source**:    pegasonow.it (Hexagon / Leica Geosystems Italy)

Enterprise-focused commercial NRTK network covering Italy. Not free.

---

## Rejected — explicitly excluded

---

## geodaf — GeoDAF / ASI (IT)

**status**:    rejected
**host:port**: `geodaf.mt.asi.it` (EUREF mirror)
**reason**:    raw GNSS observations only (EUREF raw); no RTK or VRS streams;
               suitable for post-processing only — borderline out of scope

---

## netpos — NETPOS / Kadaster (NL)

**status**:    rejected
**reason**:    restricted to Kadaster/Rijkswaterstaat internal use only; not public NTRIP

---

## 06gps — 06-GPS (NL)

**status**:    rejected
**date_added**: 2026-04-29
**country**:   NL — Netherlands
**type**:      VRS
**host:port**: not publicly listed (proprietary Trimble VRS caster)
**access**:    paid — €1,500/yr excl. VAT (~€1,815 incl. 21 % BTW, ~$2,000/yr)
**registration**: 06-gps.nl/tarieven-aanmelding/ (subscription form; schools and
               municipalities have separate rate categories)
**yearly_cost**: €1,500/yr excl. VAT (~$2,000/yr)
**stations**:  ~250 (VRS, physical reference stations across NL)
**operator**:  06-GPS B.V. (Trimble distribution partner / independent NL operator)

Commercial VRS network operated since ~2000. The only nationwide RTK correction
service in the Netherlands; Kadaster's NETPOS is internal-use only. Over the
$200/yr cutoff — not surfaced on the map. Free 1-month trial available.

---

## euref_ip — EUREF-IP / EPN

**status**:    rejected
**reason**:    raw GNSS observations only; explicitly unsuitable for real-time kinematic
               positioning; useful for PPP post-processing only

---

## igs_ip — IGS-IP / products.igs-ip.net

**status**:    rejected
**reason**:    raw observations (igs-ip.net) and SSR corrections (products.igs-ip.net)
               — enables PPP, not RTK; requires PPP-capable receiver

---

## finpos — FINPOS RTK (FI)

**status**:    rejected
**reason**:    RTK access granted only for research with written justification (3-month
               renewable); no general public tier; DGNSS free but sub-metre only

---

## apn — APN (IL)

**status**:    weird
**reason**:    pervasive military GNSS spoofing active continuously since Oct 2023
               across Israel/Lebanon/Jordan/Sinai/Cyprus (~50,000 flights affected in 2024);
               RTK unreliable regardless of NTRIP access

---

## pa_cors — Palestinian Authority CORS (PS)

**status**:    rejected
**date_added**: 2026-04-29
**country**:   PS — Palestinian Territories (West Bank + Gaza)
**type**:      n/a
**host:port**: not publicly listed
**access**:    n/a — no public endpoint
**registration**: no registration portal found
**stations**:  0 (no operational RTK caster confirmed)
**operator**:  Palestinian Authority / Palestinian Land Authority

The Palestinian Authority has no confirmed public NTRIP caster. Cadastral and
engineering surveys continue to reference the Palestine 1923 triangulation network.
Academic research (Birzeit University, An-Najah National University) addresses
3D GNSS reference frame modernisation and datum transformation but does not describe
an operational public CORS service. Area C of the West Bank (Israeli civil/military
administration, ~60 % of West Bank land area) requires Israeli Civil Administration
permits for infrastructure deployment. Gaza hardware imports (GNSS receivers fall
under Israel's dual-use item regime) require case-by-case approval that frequently
stalls. Pervasive military GNSS spoofing active since October 2023 across
Israel/Lebanon/Jordan/Sinai/Cyprus further degrades RTK reliability.
Zero PS mountpoints on rtk2go or Centipede.

**missing**: confirm whether any Palestinian university or the Palestinian Land
Authority has established a real-time NTRIP endpoint; check whether the PA's
ongoing GNSS reference frame programme (`pcbs.gov.ps`) has progressed to a
public caster.

---

## rtkdata_online — RTKdata.online

**status**:    rejected
**reason**:    server unreachable since launch; 0 stations ever collected; operated by
               Kansi Solutions GmbH (same parent as paid rtkdata.com); no independent
               data — aggregates rtk2go/Centipede visually

---

## txrtn — TXDOT CORS (US-TX)

**status**:    rejected
**reason**:    restricted to TXDOT employees and contractors only; no public or hobbyist registration

---

## calrtns — CalRTNS / Caltrans CORS (US-CA)

**status**:    rejected
**reason**:    access restricted to vetted state/county agency partners; no general public
               or hobbyist registration available

---

## sdcm — СДКМ / SDCM (RU)

**status**:    rejected
**reason**:    satellite-based augmentation system (SBAS), not NTRIP; L-band broadcast
               corrections (~20 cm sub-metre accuracy); requires SBAS-capable receiver,
               no internet connection used; out of scope for this project

---

## bgas_china — 北斗地基增强系统 BeiDou GBAS (CN)

**status**:    rejected
**reason**:    access restricted to licensed surveying organisations under 测量法
               (Surveying and Mapping Law of the PRC, Articles 27–29); no public
               NTRIP endpoint for unlicensed individuals; hobbyist registration path
               does not exist

---

## chinese_provincial_cors — Chinese Provincial CORS (CN)

**status**:    rejected
**reason**:    access restricted by law to licensed surveying organisations under
               测量法 (Surveying and Mapping Law of the PRC, 2017); hobbyist /
               individual use is not legally permitted — not a cost or
               registration barrier

All 31 provincial/municipal CORS networks are operated by natural-resources
or land-resources bureaux and feed into the national BGAS. Individual
registration is not available; credentials require institutional affiliation
with a licensed surveying body. Same legal barrier as `bgas_china`.

---

## gps_emiliaromagna — Rete GPS Emilia-Romagna (IT)

**status**:    rejected
**reason**:    public regional service discontinued; stations now commercially operated
               via NetGEO/TopNET Live (netgeo.it); not free

---

## ergand — ERGAND Geodetic Network (AD)

**status**:    free
**country**:   AD — Andorra
**type**:      single-base (EPN reference stations)
**host:port**: not publicly listed
**access**:    post-processing data available; no public NTRIP caster identified
**registration**: cartografia.ad (IDE Andorra i Cartografia portal)
**stations**:  2 (PCAR at Pic de Carroi; RULL) — EPN/IGS members
**notes**:     ERGAND (Govern d'Andorra geodetic agency) operates two reference stations
               integrated into the EUREF Permanent Network and EPOS. Provides GEOAND01
               geoid in Leica/Topcon/Trimble formats and post-processing services.
               No independent public NTRIP caster found. Hobbyists near the Spanish or
               French border can use ERGNSS (ES) or Centipede (FR) corrections.

---

## li_cors — Liechtenstein Geodata / ATG (LI)

**status**:    free
**country**:   LI — Liechtenstein
**type**:      no independent CORS programme
**host:port**: not applicable
**access**:    no public NTRIP caster
**notes**:     The Amt für Tiefbau und Geoinformation (ATG, llv.li) manages national
               geodata infrastructure but operates no CORS network or NTRIP caster.
               Liechtenstein surveyors rely on swipos (swisstopo, CHF 1,500/yr ≈ $1,650)
               which covers the entire principality via AGNES stations 5–10 km across the
               Swiss border. No free public RTK endpoint exists for the territory.

---

## sm_cors — San Marino Geodetic Reference (SM)

**status**:    free
**country**:   SM — San Marino
**type**:      single-base (permanent reference station)
**host:port**: not publicly listed
**access**:    no public NTRIP caster identified
**registration**: gov.sm / Ufficio Tecnico del Catasto e Cartografia
**stations**:  1 (RSMC permanent station)
**notes**:     The Ufficio Tecnico del Catasto distributes raw GNSS data from the RSMC
               station for post-processing but operates no public NTRIP caster. San Marino
               is fully enclosed by Italy; Emilia-Romagna's public network was discontinued
               and the Marche region has no confirmed public caster. Commercial coverage via
               NetGEO/TopNET (~€360/yr, IT national). → networks.md: `netgeo`

---

## qc_mern — Réseau GNSS du Québec / MERN (CA-QC)

**status**:    weird
**reason**:    per-station direct TCP streams (not NTRIP aggregated); incompatible with
               standard NTRIP pipeline; no NTRIP caster endpoint published

---

## eft_cors — EFT-CORS / СДГС CORS (RU)

**status**:    paid
**host:port**: `ntrip.eft-cors.ru:2102` (all stations); `:2103` nearest; `:2104` sCMRx format;
               port 70+region-code for regional subsets (e.g., 7040 = Kaluga Oblast)
**access**:    paid; day/month/6-month/annual plans; 3-day free RTK trial; RINEX post-processing free
**yearly_cost**: not publicly listed (annual price); updated tariffs from Sep 2025
**stations**:  hundreds, growing; GPS+GLONASS+BDS+GAL
**source**:    eft-cors.ru (EFT GROUP, Moscow)
**operator**:  EFT GROUP

Russia's largest CORS aggregator. Operated by EFT GROUP (геодезическое оборудование). Stations
added by partners across all federal districts. No free public tier for RTK; RINEX archives
are free for post-processing (RINEX 2.11 and 3.02). Credentials provided after subscribing.

---

## rtknet — RTKNet (RU)

**status**:    paid
**host:port**: `ntrip.rtknet.ru`; ports by federal district: 6030 Central, 6031 North-West,
               6033 Volga, 6034 Ural, 6038 North Caucasus, 6040 South, 6041 Siberia/Far East;
               port 2101 for own mobile base
**access**:    paid; 3-day free trial; register at rtknet.ru
**yearly_cost**: 30,000 ₽/yr (~$333/yr at ~90 ₽/USD)
**stations**:  300+ across Russia; RTCM 3.0 and RTCM 3.2-MSM4; 1 Hz
**source**:    rtknet.ru
**operator**:  rtknet.ru

Growing since 2013; covers all federal districts. Some equipment resellers include 1-year
RTKNet access with GNSS receiver purchases.

---

## hive_cors — HIVE (RU)

**status**:    paid
**host:port**: `hive.geosystems.aero` (exact port not confirmed)
**access**:    pay-per-use — RTK charged daily, RINEX charged hourly; station owners
               get free NTRIP caster software + storage; owners receive 50% revenue share
**yearly_cost**: variable (pay-per-use)
**source**:    hive.geosystems.aero (Geosystems Aero, Russia)
**operator**:  Geosystems Aero

Aggregation model: independent reference station owners connect their stations to HIVE;
users pay per-day RTK access. Pricing and station geography viewable on the map.

---

## geospider — ГЕОСПАЙДЕР (RU — North-West)

**status**:    paid
**host:port**: not publicly listed; obtain via geospider.ru
**access**:    paid; monthly/quarterly/annual subscriptions; register via geospider.ru
**yearly_cost**: not publicly listed
**stations**:  49 (North-West Russia, centred on St. Petersburg)
**source**:    geospider.ru (НПП «ГЕОМАТИК», St. Petersburg)
**operator**:  НПП «ГЕОМАТИК»

Regional network for the North-West federal district. RTCM 3.1 in local coordinate systems.
Operated by НПП «ГЕОМАТИК». Coverage extends over Leningrad Oblast and adjacent regions.

---

## qianxun — 千寻知寸 Qianxun (CN)

**status**:    paid
**host:port**: `rtk.ntrip.qxwz.com:8003` (CGCS2000); alt IP `60.205.8.49:8003`
**access**:    paid; individuals register directly at qxwz.com; no surveying licence required
**yearly_cost**: ~¥3,600–3,800/yr (~$500–528/yr) — over $200/yr cutoff
**stations**:  2,700+ base stations; 33 provinces; GPS+GLONASS+BDS+GAL
**source**:    qxwz.com (千寻位置 Qianxun SI — Alibaba Group + Norinco JV)
**operator**:  Qianxun SI — Alibaba Group + Norinco JV

China's dominant commercial CORS network. Launched 2016; RTCM 3.x via NTRIP standard protocol.
Open to individuals without professional licence. Most RTK survey equipment in China
pre-configures Qianxun credentials. Coverage claimed as 100% of major highways and 95%+
population coverage.

---

## cmcc_cors — 中国移动CORS China Mobile CORS (CN)

**status**:    paid
**access**:    paid; individual registration via China Mobile data account; no surveying licence required; also available daily/monthly
**yearly_cost**: ~¥3,600/yr (~$500/yr) — over $200/yr cutoff
**stations**:  4,400+ nationwide
**source**:    China Mobile (中国移动); NTRIP via CMCC network
**operator**:  China Mobile (CMCC)

China Mobile's high-precision positioning service built on 4,400+ CORS base stations. NTRIP
connection uses the CMCC interactive mode. Pricing comparable to Qianxun. Coverage and
uptime depend on China Mobile cellular infrastructure.

---

## igm_mali — Institut Géographique du Mali CORS (ML)

**status**:    free
**host:port**: not publicly listed
**access**:    unknown — no public caster or registration portal discovered
**stations**:  unknown
**source**:    igm-mali.ml (Institut Géographique du Mali, Bamako)
**operator**:  Institut Géographique du Mali (IGM), Ministry of Equipment, Transport and Désenclavement

**date_added**: 2026-04-29

National geodesy and mapping authority. IGM contributions to AFREF are RINEX raw-archive only;
no streaming NTRIP caster found. Active conflict (April 2026 coordinated insurgent attacks) and
junta governance under the Alliance of Sahel States make near-term public CORS deployment unlikely.

**missing**: confirm whether IGM operates any NTRIP caster or has a candidate endpoint; check
AFREF data centre for ML station IDs.

---

## chad_cors — Chad National Geodetic Network (TD)

**status**:    free
**host:port**: not publicly listed
**access**:    unknown — no public caster or registration portal discovered
**stations**:  unknown
**source**:    ignfi.fr (IGN FI, Paris — implementing partner for RGT20 project)
**operator**:  Ministère des Infrastructures et Désenclavement du Tchad (responsible national authority)

**date_added**: 2026-04-29

IGN FI installed 74 geodetic pillars and computed a geoid model for N'Djamena and surroundings
under the RGT20 project (Spatial Data Infrastructure for N'Djamena, completed circa 2020).
That infrastructure is passive survey control (Circé software + pillar coordinates), not a
streaming NTRIP caster. No public endpoint found. France ended all defence and geodetic
bilateral programme ties with Chad in January 2025.

**missing**: confirm whether any Chadian authority (or IGN FI successor project) has published
an NTRIP caster endpoint; check AFREF data centre for TD station IDs.

---

## ftm_mg — FTM Réseau GNSS Permanent (MG)

**status**:    free
**country**:   MG — Madagascar
**type**:      single-base (unknown — no streaming NTRIP found)
**host:port**: not publicly listed
**access**:    unknown — no public caster or registration portal discovered
**registration**: ftm.mg (national mapping agency website)
**stations**:  unknown; one IGS archive station (ABPO00MDG, ~100 km south of Antananarivo)
               operated by UNAVCO/EarthScope — RINEX archive only, not an RTK caster

**date_added**: 2026-04-29

FTM (Foiben-Taosarintanin'i Madagasikara) is the national mapping and hydrographic agency,
mandated by law to maintain the geodetic reference network and align it with AFREF/ITRF.
FTM's stated activities include GPS densification of the national geodetic network and
definition of a new reference system compatible with international standards. No public
NTRIP caster endpoint, RTK streaming service, or registration portal has been found on
ftm.mg or in AFREF/IGS documentation as of 2026. The single IGS contributing station
(ABPO00MDG at Ambakoana, last RINEX data June 2023) is a passive archive asset, not
an RTK correction stream.

**missing**: confirm whether FTM has launched any NTRIP caster since 2023; check AFREF
ODC and igs.org for any additional MG station IDs beyond ABPO00MDG.

---

## cnigs_ht — CNIGS CORS (HT)

**status**:    free
**country**:   HT — Haiti
**type**:      single-base (one confirmed station in Port-au-Prince; expansion unconfirmed)
**host:port**: not publicly listed
**access**:    unknown — host:port not publicly discoverable; CNIGS contact required
**registration**: cnigs.ht (agency website — accessibility uncertain as of 2026)
**stations**:  1 confirmed operational (Port-au-Prince, 2018); broader national expansion
               planned but unconfirmed

**date_added**: 2026-04-29

CNIGS (Centre National de l'Information Géo-Spatiale), created by decree 27 March 2006 under
the Ministry of Planning and External Cooperation, received Ashtech GNSS equipment donations
post-2010 earthquake and installed one NTRIP CORS station in Port-au-Prince. As of 2018,
that station was delivering RTK corrections to the earthquake-affected region, and CNIGS
had publicised plans for a national CORS expansion. UNAVCO trained CNIGS engineers on COCONet
station maintenance (CN09, JME2) in 2016. No subsequent public endpoint or registration portal
has been found. As of 2026, gang coalitions ("Viv Ansanm") control approximately 90 % of
Port-au-Prince and its metropolitan area; the CNIGS Tabarre office's operational status is
unconfirmed; hardware import and institutional continuity are severely at risk. Station ABPO
(Jacmel area) operated via COCONet/EarthScope — RINEX archive, not RTK streaming.

**missing**: confirm current operational status of CNIGS CORS station; confirm whether any
host:port has been published since 2018; check EarthScope/COCONet inventory for HT station
IDs and their current uptime.

---

## regna_rd — REGNA-RD (DO)

**status**:    free
**country**:   DO — Dominican Republic
**type**:      single-base (physical CORS; no VRS confirmed)
**host:port**: ntrip.ign.gob.do (port not publicly listed; disclosed after registration)
**access**:    free with registration — form at ntrip.ign.gob.do; credentials issued after submission
**registration**: ntrip.ign.gob.do
**stations**:  ~11+ (northern region certified mid-2024; national expansion ongoing)

**date_added**: 2026-04-29

REGNA-RD (Red Geodésica Nacional Activa — República Dominicana) is operated by the
Instituto Geográfico Nacional "José Joaquín Hungría Morell" (IGN-JJHM), the official
national mapping and geodetic authority. As of 2024 the network reached at least 11
certified CORS in the northern region (Santiago de los Caballeros corridor, Moca,
Puerto Plata); five further stations were certified across other provinces by August 2025.
Additional installations are planned along the Haiti border zone in partnership with the
Ministry of Defence. SIRGAS-compatible reference frame. The service is free; a web
registration form issues credentials and connection instructions. Port is not published
on the public website.

**investigate**: confirm total station count and current host:port once registered;
verify whether any VRS/network solution (MAC/iMAX) is offered in addition to single-base
streams.

---

## fundcorsrd — FUNDCORSRD (DO)

**status**:    paid
**country**:   DO — Dominican Republic
**type**:      single-base (physical CORS)
**host:port**: not publicly listed
**access**:    paid subscription (pricing not on public website; contact via fundcorsrd.com)
**registration**: fundcorsrd.com
**yearly_cost**: not publicly listed
**stations**:  ~30

**date_added**: 2026-04-29

Fundación para el Establecimiento de la Red de Estaciones Permanentes de la República
Dominicana (FUNDCORSRD) is a private foundation operating ~30 CORS stations across the
national territory. Stations track GPS, GLONASS, BeiDou, and Galileo. Provides NTRIP
RTCM corrections for surveying professionals. Over 838 registered users as of 2025.
Inaugurated new Santo Domingo office (calle E No. 8, sector El Cacique, Distrito Nacional)
in 2025. Subscription pricing not listed on public website.

---

## cors_rd_geo — CORS-RD / Geomatica (DO)

**status**:    paid
**country**:   DO — Dominican Republic
**type**:      single-base (Trimble-based physical CORS)
**host:port**: not publicly listed
**access**:    paid — registration fee + monthly per-rover fee; pricing not listed publicly
**registration**: geomatica.com.do
**yearly_cost**: not publicly listed
**stations**:  not listed publicly

**date_added**: 2026-04-29

CORS-RD is a commercial CORS network operated by Geomedición, Instrumentos y Sistemas
(GIS / Geomatica), a Dominican geomatics equipment company established 1998. Trimble-based
infrastructure. Targets surveying professionals and engineers; uses NTRIP RTCM protocol.
Subscription requires registration fee plus a monthly per-rover charge. Pricing not found
on public website.

---

## codia_cors — CODIA-CORS-MET (DO)

**status**:    paid
**country**:   DO — Dominican Republic
**type**:      single-base (physical CORS)
**host:port**: not publicly listed
**access**:    members-only paid subscription — requires active CODIA membership (annual
               dues) plus a separate CORS subscription with credentials from the CODIA-CORS
               department; pricing not listed publicly
**registration**: codia.org.do
**yearly_cost**: not publicly listed
**stations**:  not listed publicly

**date_added**: 2026-04-29

CODIA-CORS-MET is a GNSS correction service offered by the Colegio Dominicano de
Ingenieros, Arquitectos y Agrimensores (CODIA), the professional licensing body for
engineers, architects, and surveyors in the Dominican Republic. Access requires an active
CODIA membership (with annual obligations current) and a separate CORS subscription.
Delivers real-time NTRIP RTCM corrections at centimetre level. Not accessible to hobbyists
without professional membership. Pricing not on public website.

---

## ttagn — TTAGN (TT)

**status**:    free
**country**:   TT — Trinidad and Tobago
**type**:      single-base (~5 physical CORS; no VRS confirmed)
**host:port**: not publicly listed (site `gpscors.gov.tt` exists; access model undocumented)
**access**:    unknown — registration procedure and host:port not published on public website;
               Surveys and Mapping Division contact required
**registration**: agriculture.gov.tt (Ministry of Agriculture, Land and Fisheries —
                  Surveys and Mapping Division)
**stations**:  ~5 (installed across Trinidad and Tobago c.2010s; current operational count
               unverified)
**operator**:  Surveys and Mapping Division, Ministry of Agriculture, Land and Fisheries
               (agriculture.gov.tt)

**date_added**: 2026-04-29

TTAGN (Trinidad and Tobago Active Geodetic Network) is a network of five GPS CORS
installed by the Surveys and Mapping Division to provide a national geodetic infrastructure
with 24/7 continuous operation. The system was designed to deliver differential GPS data
via cellular telephone service, radio beacon, and the internet. An official portal at
`gpscors.gov.tt` exists but access terms and NTRIP host:port details are not documented
on the public-facing pages. EarthScope COCONet station CN57 (~10.84°N, −60.94°W, Trinidad)
is streamed real-time via `ntrip.earthscope.org:2101` as part of NOTA (NULA, free
non-commercial) — one geophysics-monitoring station, not a substitute for a national RTK
service.

**missing**: confirm current NTRIP host:port; confirm whether registration is free for
hobbyists or restricted to licensed surveyors; verify station count and operational uptime.

---

## margen_bolivia — MARGEN-ROC NTRIP (BO)

**status**:    paid
**country**:   BO — Bolivia
**type**:      single-base
**host:port**: not publicly listed
**access**:    paid; prior request and payment required; no self-service registration portal found
**yearly_cost**: not publicly listed (contact CEPAG — igmbolivia.gob.bo)
**registration**: igmbolivia.gob.bo (IGM Bolivia website)
**stations**:  unknown; MARGEN-ROC has stations at Cochabamba, La Paz, Santa Cruz, and other
               cities; 53 GPS stations contribute to SIRGAS-CON via CEPAG

**date_added**: 2026-04-29

MARGEN (Marco de Referencia Geocéntrico Nacional) is Bolivia's national geodetic reference
framework, maintained by the Instituto Geográfico Militar (IGM). The Red de Operaciones
Continuas (MARGEN-ROC) is a set of continuously tracking GNSS stations that serve as
reference bases for differential surveys and contribute weekly solutions to the SIRGAS
network via the CEPAG (Centro de Procesamiento y Análisis de Datos GNSS) processing centre.
IGM advertises an NTRIP RTK correction service and sells raw/RINEX data from MARGEN-ROC
stations, but no free public endpoint or self-service registration portal has been found.
Access requires direct contact with CEPAG. ArduSimple (2026) lists Bolivia as having no
established national RTK network for hobbyists.

**missing**: confirm whether IGM Bolivia has published a public NTRIP caster host:port;
confirm current pricing (Bs/yr); check SIRGAS-CON station list for BO station IDs.

---

## redgeo_bo — RED-GEO CORS NTRIP (BO)

**status**:    paid
**country**:   BO — Bolivia
**type**:      single-base
**host:port**: caster port 6060; full host not publicly confirmed
**access**:    paid; username and password required; pricing not listed publicly
**yearly_cost**: not publicly listed (contact geoboliviasrl.info)
**registration**: geoboliviasrl.info (GeoBolivia SRL website)
**stations**:  ~6 stations: La Paz (GEO 1), Cochabamba (GEO 2), Oruro (GEO 3),
               Sacaba (GEO 4), Tarija (GEO 5), Santa Cruz (GEO 6)

**date_added**: 2026-04-29

RED-GEO is a private commercial CORS NTRIP network operated by GeoBolivia SRL. The network
is described as regulated under Bolivia's Ley 2997 del Topógrafo and administered in
coordination with COTOBOL (Colegio de Topógrafos de Bolivia). The caster supports
GPS + GLONASS + Galileo + BeiDou on port 6060. Station coordinates are tied to Class A
and B points of the government MARGEN framework. Access is described as free for
institutions with which GeoBolivia SRL has a data usage agreement; general subscription
pricing is not published on the website.

**missing**: confirm full caster hostname; confirm subscription pricing in Bs/yr;
confirm whether any access tier is free for individual hobbyists.

---

## ign_gt_cors — IGN Guatemala Red CORS (GT)

**status**:    free
**country**:   GT — Guatemala
**type**:      single-base
**host:port**: not publicly listed
**access**:    restricted — credentials (username, password, host:port) supplied by IGN on
               request; no self-service portal found
**yearly_cost**: unknown — no pricing information found publicly
**registration**: ign.gob.gt (Instituto Geográfico Nacional — Guatemala)
**stations**:  ~17 stations distributed nationally

**date_added**: 2026-04-29

Guatemala's Instituto Geográfico Nacional (IGN) operates a Red CORS (Continuously Operating
Reference Stations) of approximately 17 stations distributed across the national territory.
The network was established with technical and financial support from RIC (Registro de
Información Catastral) to enable rapid cadastral surveys tied to the national reference
system. RINEX 2.11 data is available for download from the IGN website. Real-time NTRIP
corrections are technically available (a caster exists with IP, port, username, and password)
but credentials must be obtained directly from IGN — no public self-service registration
or free-access announcement found. ArduSimple (2026) does not list Guatemala as having a
national RTK network accessible to hobbyists.

**missing**: confirm whether IGN Guatemala offers free or paid NTRIP access and on what terms;
obtain host:port from IGN directly; check whether RIC operates an independent caster.

## ip_cors_hn — IP CORS Honduras (HN)

**status**:    free
**country**:   HN — Honduras
**type**:      single-base
**host:port**: not publicly listed
**access**:    unknown — RINEX download confirmed at cors.ip.gob.hn; real-time NTRIP terms
               not documented; no self-service registration portal found
**yearly_cost**: unknown
**registration**: cors.ip.gob.hn (Instituto de la Propiedad)
**stations**:  unknown

**date_added**: 2026-04-29

The Instituto de la Propiedad (IP) operates a cadastral CORS network whose portal
(cors.ip.gob.hn) offers RINEX data downloads for post-processing. The portal describes
continuous measurement stations providing a geodetic reference framework. No public NTRIP
caster endpoint, host:port, or user registration flow has been found; real-time access
likely requires direct contact with IP.

**missing**: confirm whether IP CORS provides real-time NTRIP access; obtain host:port
and access terms from Instituto de la Propiedad directly.

## ign_hn_cors — IGN Honduras CORS (HN)

**status**:    free
**country**:   HN — Honduras
**type**:      single-base
**host:port**: not publicly listed
**access**:    unknown — CORS stations listed at ign.hn/estacionescors; NTRIP caster
               endpoint not published
**yearly_cost**: unknown
**registration**: ign.hn (Instituto Geográfico Nacional de Honduras)
**stations**:  unknown

**date_added**: 2026-04-29

The Instituto Geográfico Nacional (IGN) of Honduras maintains active GNSS reference
stations as part of the national geodetic reference framework (datum WGS-84 / ITRF14).
The CORS section of the IGN website (ign.hn/estacionescors) offers data downloads and
describes the stations as operating continuously 24/7. No public NTRIP caster host:port
or user registration page was found; real-time RTK correction delivery appears to require
direct contact with IGN.

**missing**: confirm whether IGN Honduras provides public real-time NTRIP access; obtain
host:port and registration process.

## ineter_cors — INETER CORS (NI)

**status**:    free
**country**:   NI — Nicaragua
**type**:      single-base
**host:port**: not publicly listed
**access**:    post-processing only confirmed; RINEX data available via
               consultacf.ineter.gob.ni; real-time NTRIP access not found
**yearly_cost**: unknown
**registration**: consultacf.ineter.gob.ni (INETER — Catastro Físico)
**stations**:  unknown

**date_added**: 2026-04-29

INETER (Instituto Nicaragüense de Estudios Territoriales), through its Dirección General
de Geodesia y Cartografía, maintains a network of satellite observation CORS stations as
part of its SIRGAS contributions and the national spatial data infrastructure (IDE). The
Catastro Físico portal (consultacf.ineter.gob.ni/Servicio/ConsultaDatosCORS) provides
RINEX data access for post-processing. No public NTRIP caster endpoint or real-time
streaming access has been found. Nicaragua's Ortega-Murillo government is subject to
targeted OFAC sanctions (individuals/entities), but the sanctions do not specifically
restrict civil GNSS infrastructure access; the absence of a public NTRIP endpoint appears
to be a capacity/policy issue rather than a sanctions barrier.

**missing**: confirm whether INETER operates a real-time NTRIP caster; obtain host:port
and access terms if available.

## cnr_sv_cors — CNR/IGCN CORS (SV)

**status**:    free
**country**:   SV — El Salvador
**type**:      single-base
**host:port**: not publicly listed
**access**:    post-processing RINEX only confirmed via eCNR (e.cnr.gob.sv); no free
               public real-time NTRIP endpoint found
**yearly_cost**: unknown
**registration**: e.cnr.gob.sv (Centro Nacional de Registros — IGCN online services)
**stations**:  ≥3 confirmed active CORS: SNJE, SSIA, VMIG; SSIA also in IGS global network

**date_added**: 2026-04-29

The Instituto Geográfico y del Catastro Nacional (IGCN) within El Salvador's Centro
Nacional de Registros (CNR) has operated active CORS stations since at least 2007.
Known stations include SNJE, SSIA (San Salvador, also part of the IGS global network),
and VMIG, with the network densified across multiple departments. RINEX data is available
via the eCNR online services portal. No public real-time NTRIP caster has been found;
all documented access is for post-processing.

**missing**: confirm whether CNR/IGCN provides real-time NTRIP access; obtain host:port
from CNR's Geodesia department if available.

## zingsa_cors — ZINGSA CORS Network (ZW)

**status**:    paid
**country**:   ZW — Zimbabwe
**type**:      single-base
**host:port**: not publicly listed
**access**:    paid — S.I. 47 of 2023 (Land Survey Act, Surveyor-General's Office
               Prescribed Fees Amendment Notice, 7 April 2023) establishes fees for
               CORS access; contact ZINGSA or the Surveyor General's Office for rates
**yearly_cost**: not publicly listed
**registration**: zingsa.ac.zw (Zimbabwe National Geospatial and Space Agency)
**stations**:  unknown — national coverage stated

**date_added**: 2026-04-29

ZINGSA (Zimbabwe National Geospatial and Space Agency), launched by President
Mnangagwa in 2021, operates a national CORS network used for high-precision
surveying, precision agriculture, geophysical research, and ionospheric
monitoring. The Surveyor General's Office (Ministry of Lands, Agriculture,
Fisheries, Water and Rural Development, agric.gov.zw) administers the same
infrastructure under the Land Survey Act. The 2023 statutory instrument
(S.I. 47 of 2023) confirms a paid-access model; no public free tier or NTRIP
caster host:port has been found. US Zimbabwe sanctions programme terminated
March 2024 (OFAC Executive Order revoked, transitional designations moved to
GLOMAG); no sanctions barrier to hardware import exists as of April 2026.
No public registration portal or host:port discoverable without direct contact.

**missing**: confirm whether a free or registration-only tier exists; obtain
host:port and fee schedule from ZINGSA (zingsa.ac.zw/geodesy) or the
Surveyor General's Office.

## survey3g_sv — Survey3G NTRIP (SV)

**status**:    rejected
**country**:   SV — El Salvador
**type**:      single-base
**host:port**: not publicly listed (credentials supplied with subscription)
**access**:    paid — monthly/quarterly/annual subscription; pricing updated every 6
               months and not listed on public web pages
**yearly_cost**: not publicly listed (contact survey3g.com)
**registration**: survey3g.com
**stations**:  4 stations: Oriente, San Salvador, Occidente, UES

**date_added**: 2026-04-29

Survey3G is the principal commercial NTRIP provider in El Salvador, offering RTK
correction streams from four stations covering the national territory. Constellations:
GPS, GLONASS, BeiDou, Galileo; frequencies L1/L2/L5. The network operates 24/7 and
offers flexible subscription tiers (monthly, quarterly, annual). Pricing is not
published on the website and is updated every 6 months; contact is required for rates.
Rejected for pipeline — paid and pricing not confirmed as under $200/yr cutoff.

---

## igntg_cors_pa — IGNTG CORS Network (PA)

**status**:    free
**country**:   PA — Panama
**type**:      single-base
**host:port**: not publicly listed
**access**:    no public NTRIP caster found; real-time access requires direct contact with IGNTG
**registration**: ignpanama.anati.gob.pa (Instituto Geográfico Nacional "Tommy Guardia")
**stations**:  ~19 national CORS; 7 are SIRGAS-CON internet-connected nodes (IGN1, AZUE,
               DAVI, DARI, PUAR, PMEC, CHEP); 8 additional stations being restored under
               the 2025 modernisation project
**operator**:  IGNTG / ANATI (Autoridad Nacional de Administración de Tierras)
**yearly_cost**: n/a (no confirmed public service)

**date_added**: 2026-04-29

IGNTG is Panama's national mapping agency (geodesy, cartography, geophysics) under ANATI.
The CORS network supports the national geodetic reference frame (ITRF-compatible), SIRGAS
contributions, and cadastral surveys. Seven stations have permanent internet connectivity
and are processed weekly by SIRGAS data processing centres. A 2025 modernisation project
is restoring eight previously inoperative stations. No public NTRIP caster host:port or
self-service registration portal has been found; access to real-time corrections appears
to require institutional contact with IGNTG (phone: +507 524-0434). The website lists
CORS station coordinates and monuments but not connection details.

**missing**: confirm whether IGNTG provides any public NTRIP streaming service; obtain
host:port if one exists. Check ignpanama.anati.gob.pa/index.php/cors for updates after
the 2025 modernisation completes.

---

## topored_pa — Topored CORS Network (PA)

**status**:    rejected
**country**:   PA — Panama
**type**:      single-base
**host:port**: not publicly listed (credentials supplied with subscription)
**access**:    paid subscription; emits differential corrections via NTRIP
**registration**: panama.casadeltopografo.com/topored (Casa del Topógrafo Panama)
**stations**:  ~28 stations across Panama and Colombia (national + cross-border coverage);
               control centre in Bogotá, Colombia
**operator**:  Casa del Topógrafo (Bogotá/Panama City); network branded "Topored"
**yearly_cost**: not publicly listed (contact via website)

**date_added**: 2026-04-29

Topored is Panama's largest commercial CORS network, operated by Casa del Topógrafo with
a control centre in Bogotá, Colombia. The 28-station network covers the Republic of Panama
and adjacent Colombian territory. Corrections are delivered via NTRIP; RINEX data download
is also available for registered users. Pricing is not published on the website. Rejected
for pipeline — paid service and no confirmed hobbyist-accessible free tier.

---

## khmer_geonet — Khmer GEONET (KH)

**status**:    candidate
**country**:   KH — Cambodia
**type**:      single-base (5 physical CORS)
**host:port**: not publicly listed; Trimble Pivot web interface visible at
               167.179.14.66:8080 but not a public NTRIP endpoint
**access**:    free trial (extended to June 2025); post-trial pricing not publicly
               listed — contact via khmergeonet.xyz
**yearly_cost**: not publicly listed (contact GDCG)
**registration**: khmergeonet.xyz
**stations**:  5 (Phnom Penh, Kandal, Kampong Speu, Siem Reap, Stung Treng)
**operator**:  General Department of Cadastre and Geography (GDCG), Ministry of
               Land Management, Urban Planning and Construction (MLMUPC)

**date_added**: 2026-04-29

Cambodia's national CORS and precise positioning service, built under JICA technical
cooperation (August 2021 – December 2024). The 5 CORS provide single-base corrections
for registered GNSS users in pilot coverage areas. Service branded Khmer GEONET
(khmergeonet.xyz). Free trial was extended a full year to 24 June 2025; subscription
pricing after that date is not on the public website.

NTRIP caster host:port not discoverable from public sources. Trimble Pivot software
is used for the data centre; the IP 167.179.14.66:8080 appears in a sensor-map URL
but is not a public NTRIP endpoint. Until the NTRIP details are confirmed and a
free-or-affordable tier is verified, this entry is candidate rather than pipeline.

**missing**: public NTRIP host:port and post-trial pricing — contact GDCG via
khmergeonet.xyz or MLMUPC (mlmupc.gov.kh) to confirm access terms.

---

## ngd_laos_cors — NGD / CORS Network (LA)

**status**:    free
**country**:   LA — Laos (Lao PDR)
**type**:      single-base (physical CORS)
**host:port**: not publicly listed
**access**:    unknown; no public registration portal found
**stations**:  unknown (at least 1 confirmed operational in Vientiane, 2013)
**operator**:  National Geographic Department (NGD), Ministry of Natural Resources
               and Environment

**date_added**: 2026-04-29

NGD holds the mandate for land surveying, mapping, and geodetic control under Prime
Minister Decree No. 73/PM (1995). National geodetic datum established 1997 (Lao
National Datum 1997, origin Vientiane Nongteng Astro Pillar). Two known CORS
infrastructure strands:

1. **IGN FI project**: French firm IGN FI supplied and installed a CORS system for
   real-time positioning in Laos (date not publicly specified; referenced in IGN FI
   portfolio at ignfi.fr). Station count and public access terms not confirmed.

2. **ComNav / first CORS station**: the first BeiDou-capable CORS station was
   commissioned in Vientiane on 25 November 2013 using ComNav M300 receiver, R300
   handheld, and CDC CORS software. Application scope: land surveying, mapping,
   forestry, and temporal monitoring.

No public NTRIP host:port, open sourcetable, or hobbyist registration portal has been
found for the government network. UniqTeK Company Limited (uniqteklao.com), a private
100% Lao-owned firm operating since 2014, runs a separate commercial CORS/RTK service
described as the largest RTK and CORS network in Lao PDR; access model and pricing are
not published on their website.

**missing**: public NTRIP caster host:port and access terms — contact NGD via
mlre.gov.la or UniqTeK via uniqteklao.com.

---

## png_dlpp_cors — DLPP / WAIG CORS + Unitech LAE1 (PG)

**status**:    free
**country**:   PG — Papua New Guinea
**type**:      single-base (scientific reference stations; no RTK density)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**stations**:  2 known (WAIG in Port Moresby operated by DLPP; LAE1 at PNG University
               of Technology, Lae, operated by Unitech Surveying & Land Studies dept)
**operator**:  DLPP (Department of Lands and Physical Planning) for WAIG;
               PNG University of Technology (Unitech) for LAE1
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

Both stations contribute raw GNSS observations to Geoscience Australia's Asia-Pacific
Reference Frame (APREF) network and are archived at the Geoscience Australia GNSS Data
Centre (data.gnss.ga.gov.au). WAIG, installed at Eda Tano Haus, Waigani Drive, Port
Moresby (see quickclose.com.au/Waig_installation.pdf), underpins the PNG2020 geodetic
datum; LAE1 at Unitech has been part of the IGS tracking network since 2002. Neither
station is exposed via a public NTRIP caster for RTK correction use, and station
spacing makes baseline distances far exceed the practical ~30 km L1+L2 RTK range.

The AUSCORS broadcaster (`ntrip.data.gnss.ga.gov.au:2101`) streams APREF-contributing
stations across the Pacific, but PNG-area streams are reference-grade archive feeds,
not a substitute for a local RTK CORS network. No independent government or volunteer
NTRIP caster for PNG has been found; hobbyists must deploy a local base station.

**missing**: public NTRIP endpoint — contact DLPP via dlpp.gov.pg or Geoscience
Australia GNSS operations via data.gnss.ga.gov.au for APREF stream availability.

## fiji_dlss_cors — Fiji CORS (FJ)

**status**:    free
**country**:   FJ — Fiji
**type**:      single-base (no public NTRIP confirmed; CORS physically established)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found; access policy under development (as of 2022)
**registration**: no self-service portal identified
**stations**:  ~10 (2 legacy: Suva, Lautoka; 8 new: Labasa, Nabouwalu, Taveuni,
               Kadavu, Koro Island, Lakeba, Ono-i-Lau, Rotuma)
**operator**:  Department of Lands and Survey (Ministry of Lands and Mineral
               Resources, `lands.gov.fj`)
**yearly_cost**: n/a (no confirmed public service)

**date_added**: 2026-04-29

The Fiji Geodetic Datum Project (2019–2022) was conducted in three phases by the
Department of Lands and Survey, the Fiji Hydrographic Service, the Fiji Navy, and
SPC (Pacific Community), occupying 193 geodetic control stations. Eight new CORS
sites were added to the two existing stations in Suva and Lautoka, achieving <50 km
spacing across Viti Levu, Vanua Levu, and the outer islands. Data compilation and
analysis was supported by SPC's Geodetic Survey team and Geoscience Australia
(COSPPac programme). The project was announced as a milestone by SPC in September
2022; at that time officials stated that "there is currently no regulation for
accessing data from the CORS stations" and that a policy framework was being
prepared. One Fiji station (LAUT, Lautoka) contributes to AUSCORS and the APREF
archive (`ntrip.data.gnss.ga.gov.au:2101`) as a reference-grade stream, not an RTK
correction service. No public NTRIP caster host:port has been announced.
Zero FJ mountpoints on rtk2go or Centipede.

**missing**: confirm whether a public NTRIP endpoint has been activated following
the 2022 milestone — contact the Department of Lands and Survey via `lands.gov.fj`
or check with SPC's geospatial division (`spc.int`) for any Pacific CORS access
programme.

## libpos_ly — Libyan Survey Authority CORS (LY)

**status**:    free
**country**:   LY — Libya
**type**:      unknown (no confirmed network)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  unknown; no operational CORS network confirmed
**operator**:  الهيئة العامة للمساحة (al-Hay'a al-ʿĀmma lil-Masāḥa —
               Libyan Survey Authority / General Authority for Survey),
               Tripoli — nominal; no public RTK delivery confirmed from
               either the GNU (Tripoli) or GNS/HoR (Benghazi) administrations
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

Libya participates nominally in NAFREF (North Africa Reference Frame, part of
AFREF), but no AFREF-contributing permanent GNSS station with a public NTRIP
stream has been identified as operational. No network using the name LIBPOS or
an equivalent appears in any public CORS registry (EUREF, IGS, AFREF, rtk2go,
Centipede). Zero LY mountpoints on any volunteer caster.

The absence is structural: since 2014 Libya has operated under two rival
administrations (GNU in Tripoli, GNS/HoR-LNA in Benghazi). UN Security Council
sanctions (UNSCR 1970 and successor resolutions) and asset-freeze frameworks
remain in force. No central authority exists to commission, fund, or maintain a
national CORS network. Hardware imports face dual-administration customs barriers
and sanctions compliance requirements. No survey of open-source or academic
literature revealed any operational public NTRIP endpoint.

**missing**: no confirmed public endpoint exists. Revisit only after a verified
unified administration and published CORS programme are confirmed. For context
on the governance situation see the GNU/HoR deadlock reporting at
securitycouncilreport.org.

## sgdn_na — Surveyor General's Department GNSS (NA)

**status**:    free
**country**:   NA — Namibia
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  unknown; national geodetic control network exists but no
               streaming RTK endpoint confirmed
**operator**:  Surveyor General's Department (SGDN), Ministry of Agriculture,
               Water and Land Reform, Windhoek
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

SGDN manages Namibia's national geodetic reference network and uses GNSS survey
methods for first-order control and urban densification. One IGS contributing
station operates in Windhoek (WIND00NAM, archived at HartRAO data centre) for
raw-observation archiving — not an RTK streaming caster. No public NTRIP caster
has been found in any directory, sourcetable, or academic reference. Zero NA
mountpoints on rtk2go or Centipede.

**missing**: confirm whether SGDN or a successor programme has launched a public
NTRIP caster; check HartRAO geodesy pages and AFREF documentation for any
Namibia-hosted streaming endpoint.

## dsm_bw — Department of Surveys and Mapping CORS (BW)

**status**:    free
**country**:   BW — Botswana
**type**:      unknown (physical CORS; no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found; access requires direct engagement
               with DSM
**registration**: no public portal identified
**stations**:  ~55 physical CORS (project commenced 2011, ~10 stations/yr);
               average spacing ~30–40 km across ~582,000 km²
**operator**:  Department of Surveys and Mapping (DSM), Ministry of Lands and
               Water Affairs, Gaborone (`gov.bw`)
**yearly_cost**: unknown (no public tariff found)

**date_added**: 2026-04-29

DSM has built a national CORS network of approximately 55 stations since 2011.
DSM technical documentation describes GNSS RTK from CORS as accepted practice
for cadastral surveying, with baselines up to 40 km permitted. No public NTRIP
caster host:port has been found in any directory, sourcetable, or academic
reference. Zero BW mountpoints on rtk2go or Centipede.

**missing**: confirm whether DSM provides a public NTRIP streaming endpoint;
check `gov.bw` land-management pages and contact DSM geodesy section for
host:port and access terms.

## survey_mu — Survey Division CORS Feasibility (MU)

**status**:    free
**country**:   MU — Mauritius
**type**:      unknown (feasibility stage; no confirmed operational caster)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  unknown; CORS network feasibility studied 2016, no confirmed
               operational deployment
**operator**:  Survey Division, Ministry of Housing and Land Use Planning,
               Ebène (`housing.govmu.org`)
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

The Survey Division is the national geodetic authority for Mauritius. A May
2016 workshop hosted at the Ministry in Ebène, facilitated by RCMRD (Regional
Centre for Mapping of Resources for Development), examined establishing a CORS
network; around 40 participants from government ministries and private sector
attended. No evidence of an operational public NTRIP caster has been found
since that workshop. Zero MU mountpoints on rtk2go or Centipede. No IGS
archive stations confirmed in Mauritius proper.

**missing**: confirm whether the Survey Division or a successor programme
has launched an operational CORS network with a public NTRIP endpoint; check
`housing.govmu.org` and RCMRD/AFREF documentation for any Mauritius-hosted
streaming endpoint.

---

## ingt_cv — INGT Geodetic Network (CV)

**status**:    free
**country**:   CV — Cape Verde
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  unknown
**operator**:  INGT — Instituto Nacional de Gestão do Território (`ingt.gov.cv`),
               under the Ministry of Infrastructure, Land Use Planning and
               Housing (MIOTH)
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

INGT is the Cape Verde state entity responsible for Territory Ordering, Urban
Planning, Property Registry, Geodesy, Cartography, and the national Spatial
Data Infrastructure (IDE-CV, `idecv-ingt.opendata.arcgis.com`). Geodesy is a
stated core mandate. No public NTRIP caster host:port has been found in any
directory, sourcetable, or academic reference for the archipelago. Zero CV
mountpoints on rtk2go or Centipede.

**missing**: confirm whether INGT operates or plans a public GNSS correction
streaming service; check `ingt.gov.cv/ingt/servicos/` and contact INGT
geodesy section for any host:port or pilot NTRIP endpoint.

## ag_cors — Antigua and Barbuda GNSS / COCONet (AG)

**status**:    free
**country**:   AG — Antigua and Barbuda
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  unknown; at least one COCONet station present (geophysics monitoring, RINEX archive)
**operator**:  Lands and Survey Division (Ministry of Lands, Housing and Agriculture);
               COCONet station operated by UNAVCO / EarthScope Consortium
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

No government RTK correction service found. The Lands and Survey Division holds geodetic
responsibility but no NTRIP caster host:port or registration portal has been identified.
COCONet / EarthScope NOTA includes at least one station in Antigua for geophysics monitoring;
real-time streaming via `ntrip.earthscope.org:2101` is not confirmed for this station.
Zero AG mountpoints on rtk2go or Centipede.

**missing**: verify whether any COCONet/NOTA station in Antigua streams via
`ntrip.earthscope.org:2101`; check EarthScope station inventory for AG stations.

## kn_cors — Saint Kitts and Nevis GNSS / COCONet (KN)

**status**:    free
**country**:   KN — Saint Kitts and Nevis
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  unknown; COCONet lists at least one seismic/geophysics cGPS station
**operator**:  Lands and Surveys Unit (`gov.kn`); COCONet station operated by
               UNAVCO / EarthScope Consortium (seismic monitoring)
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

No government RTK correction service found. The Lands and Surveys Unit is the geodetic
authority (`gov.kn/lands-and-surveys-unit/`) but no NTRIP caster has been announced.
A COCONet cGPS station exists for volcanic/seismic monitoring but no real-time NTRIP
endpoint is publicly advertised. Zero KN mountpoints on rtk2go or Centipede.

## lc_cors — Saint Lucia GNSS / COCONet (LC)

**status**:    free
**country**:   LC — Saint Lucia
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  2 COCONet cGPS sites (CN04, CN47) installed 2014; RINEX archive only
**operator**:  Survey and Mapping Section (Ministry of Physical Development, Housing
               and Urban Renewal); COCONet stations operated by UNAVCO / EarthScope
               Consortium
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

UNAVCO engineers installed two COCONet cGPS sites (CN04 and CN47) in Saint Lucia in
February–March 2014, in collaboration with the University of the West Indies and the
Ministry of Physical Development. These are geophysics monitoring stations with RINEX
archives; no public NTRIP streaming endpoint has been confirmed. The Survey and Mapping
Section holds geodetic responsibility but has not published an NTRIP caster host:port.
Zero LC mountpoints on rtk2go or Centipede.

## vc_cors — Saint Vincent and the Grenadines GNSS (VC)

**status**:    free
**country**:   VC — Saint Vincent and the Grenadines
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  unknown; geodetic modernisation work underway (Caribbean Digital
               Transformation Project, World Bank, 2020–2025)
**operator**:  Lands and Surveys Department (`transport.gov.vc`)
**yearly_cost**: n/a (no public service)

**date_added**: 2026-04-29

The World Bank–funded Caribbean Digital Transformation Project (US$28 million,
2020–2025) included a geodetic reference network modernisation component for
Saint Vincent and the Grenadines: datum update from BWI 1945 Grid to ITRF,
equipment procurement, and a digital mapping exercise (Dec 2024 – Jan 2025).
No public NTRIP caster host:port has been announced as of early 2025.
Zero VC mountpoints on rtk2go or Centipede.

**missing**: re-check whether the CARDTP geodetic modernisation resulted in a
public CORS NTRIP endpoint; contact Lands and Surveys Department via
`transport.gov.vc` for any planned public caster.

## glsc_cors — Guyana CORS (GY)

**status**:    free
**country**:   GY — Guyana
**type**:      single-base (professional/government access; no public NTRIP confirmed)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no self-service portal identified
**stations**:  8 (Eclipse Falls, Supenaam, Georgetown, New Amsterdam, Olive Creek,
               Lethem, Linden + 1 additional site)
**operator**:  GL&SC (Guyana Lands and Surveys Commission, `glsc.gov.gy`)
**yearly_cost**: n/a (no confirmed public service)

**date_added**: 2026-04-29

The 8-station CORS network was established 2018–2019 under a G$93 million contract
between GL&SC and Ordnance Survey International. Stations are distributed across
Guyana's 10 administrative regions and connected to SIRGAS. Ordnance Survey
supported installation of six new stations, restoration of the Network Operations
Centre, and staff training in network maintenance and expansion. The network was
recognised by the government as critical infrastructure for managing land demand
arising from Guyana's oil and gas revenues (production began 2019). No public NTRIP
caster host:port or self-service registration portal has been published; GL&SC's
website (`glsc.gov.gy/services/survey-services`) describes services for licensed
surveyors and engineers but does not list correction-stream credentials.
Zero GY mountpoints on rtk2go or Centipede.

**missing**: confirm whether a public NTRIP endpoint exists or is planned — contact
GL&SC via `glsc.gov.gy` or check procurement notices (e.g. invitation-to-bid for
CORS network software, 2023) for signs of an operational caster rollout.

## sob_bd — SOB VRS (BD)

**status**:    paid
**country**:   BD — Bangladesh
**type**:      VRS (6 physical CORS backing a VRS network)
**host:port**: `202.53.170.98:8011`
**access**:    registration required; pricing not listed on public website —
               consult `data.sob.gov.bd` or contact SOB directly
**registration**: `data.sob.gov.bd/signup-user.php`
**yearly_cost**: not publicly listed (payment via Rocket/bKash/SureCash mobile
               banking per SOB data-service model)
**stations**:  6 physical CORS at Dhaka, Chittagong, Rajshahi, Khulna,
               Maulavibazar, Rangpur — operating since 19 December 2011;
               VRS software on server generates virtual corrections
**operator**:  Survey of Bangladesh (SoB), Ministry of Defence
               (`sob.gov.bd`); data portal `data.sob.gov.bd`

**date_added**: 2026-04-29

Bangladesh's national GNSS CORS network was established in December 2011 with
six permanent stations spanning the country's 147,570 km². A VRS software
layer on the SOB data-centre server generates RTK correction streams and also
supports post-processing RINEX download. The caster IP `202.53.170.98:8011`
is publicly documented by SOB but requires a registered account for NTRIP
access. Payment for SOB data services is handled via Bangladeshi mobile banking
(Rocket, bKash, SureCash). With only 6 underlying stations across ~148,000 km²,
inter-station baselines run 100–200 km — outside the 30–50 km envelope needed
for reliable L1+L2 RTK; corrections will degrade significantly away from
station locations. No pricing is published on the public website.

**investigate**: confirm whether SOB has expanded beyond 6 stations as part of
the "GNSS CORS network expansion" project listed at
`sob.portal.gov.bd/pages/static-pages/6922dc2c933eb65569e0ec7c`, and whether
a newer host:port or pricing schedule is now publicly available.

## miranet_bt — MiraNet / DrukNet CORS (BT)

**status**:    paid-affordable
**country**:   BT — Bhutan
**type**:      single-base (13 physical CORS stations)
**host:port**: `ntrip.druknet.net:2101` (NTRIP; portal: `miranet.nlcs.gov.bt`)
**access**:    paid subscription; free for education/research with documentation
**registration**: `miranet.nlcs.gov.bt/pre-registration/form`
**yearly_cost**: Nu 10,000/yr (~$110/yr); government agencies same flat rate;
               education/research free
**stations**:  13 single-base stations; network established 2014 (6 stations),
               expanded to 13; covers Bhutan's ~38,394 km²
**operator**:  National Land Commission Secretariat — Department of Survey and
               Mapping (DoSAM), Royal Government of Bhutan; web: `web.nlcs.gov.bt`

**date_added**: 2026-04-29

Bhutan's national CORS network was established in 2014 with 6 Trimble receivers
and expanded to 13 stations. Managed via Trimble-based CORS management software
branded as MiraNet (DrukNet). The portal at `miranet.nlcs.gov.bt` provides both
real-time RTK NTRIP streaming and re-processed static RINEX data (daily and
hourly). NLCS levies a nominal fee to cover infrastructure, remote support
contracts, and recurrent internet/power costs. Educational and research users
receive free access upon submitting an official supporting document. Subscription
credentials (username/password) are issued after payment or approval.
Vertical datum: DrukGeoid 2015.

## almgg_mn — CORS Network (MN)

**status**:    restricted
**country**:   MN — Mongolia
**type**:      single-base (government cadastral use; no public NTRIP)
**host:port**: not publicly listed
**access**:    no open self-service path confirmed; restricted to licensed
               surveyors and government agencies
**registration**: no self-service portal identified; contact
               `gazar.gov.mn`
**yearly_cost**: n/a (no confirmed public service)
**stations**:  40+ (Trimble NetR8/NetR9 with choke-ring and Zephyr Geodetic
               antennas; cities: Ulaanbaatar, Darkhan, Erdenet + nationwide)
**operator**:  General Office of Land Relations, Geodesy and Cartography
               (Газар зохион байгуулалт, геодези, зураг зүйн ерөнхий газар,
               `gazar.gov.mn`); formerly ALACGaC / ALMGG

**date_added**: 2026-04-29

Initial 6-station CORS infrastructure was delivered in December 2010 by ILS
(International Land Systems) under the Millennium Challenge Corporation Property
Rights Project, with Trimble NetR8 receivers and R5 rover bundles supplied to
the Mongolian Agency for Land Affairs, Construction, Geodesy and Cartography.
Used initially for cadastral surveys and orthorectification GCPs covering ~75,000
property plots. Network has since grown to 40+ stations countrywide. No public
NTRIP caster host:port or registration portal has been found; access is restricted
to government and licensed surveying use. Mongolia is ~1.56 million km²; average
inter-station distance is ~200 km, making RTK practical only near the
Ulaanbaatar–Darkhan–Erdenet corridor. Zero MN mountpoints on rtk2go or Centipede.

**missing**: confirm whether a public NTRIP endpoint exists — check `gazar.gov.mn`
and the NSDI portal (`nsdi.gov.mn`) for credentials or procurement notices.

## survey_bn — Survey Department Brunei (BN)

**status**:    restricted
**country**:   BN — Brunei Darussalam
**type**:      unknown (no sourcetable discovered)
**host:port**: not publicly listed
**access**:    no open NTRIP service found
**registration**: no self-service portal identified; contact `survey.gov.bn`
**yearly_cost**: n/a (no confirmed public service)
**stations**:  unknown
**operator**:  Department of Survey and Mapping, Ministry of Development,
               Brunei Darussalam (`survey.gov.bn`)

**date_added**: 2026-04-29

The Department of Survey and Mapping operates a geodetic infrastructure and
Geoportal Ukur (`geoportal.survey.gov.bn`) for national mapping. GNSS CORS
stations are used internally for cadastral control; a 2011 UN-GNSS presentation
confirmed ISO 9001 certification and surveying operations. No public NTRIP caster
host:port, sourcetable, or self-service registration has been found. Brunei's
territory is ~5,765 km² (two enclaves in Sarawak/Borneo); one or two stations
would suffice for national RTK coverage. No BN mountpoints on rtk2go or Centipede.
Nearest practical option for hobbyists is Malaysia's MyRTKnet (Sarawak stations,
`myrtknet.gov.my`), though cross-border validity requires confirmation with JUPEM.

**missing**: confirm whether a public NTRIP endpoint or open registration exists —
check `survey.gov.bn` directly or contact the department for geodetic services.

---

## bfcors — BF-CORS GNSS Network (BF)

**status**:    candidate
**country**:   BF — Burkina Faso
**type**:      single-base (physical CORS stations)
**host:port**: not publicly listed (disclosed post-registration via `bfcors.net`)
**access**:    free with registration; administrator-issued credentials
**registration**: `www.bfcors.net` (self-service form; admin sends password)
**stations**:  ~13 physical: 9 original (2011 MCA-BF funding) + 4 capital-region (2018)
**operator**:  IGB — Institut Géographique du Burkina (`igb.bf`), Ouagadougou
**yearly_cost**: free

**date_added**: 2026-04-29

Nine permanent GNSS stations established in 2011 under a contract between MCA-BF
(Millennium Challenge Account Burkina Faso) and Trimble Europe BV; IGB assumed
technical management in September 2012. Station locations: Gampela, Manga, Fada,
Diapaga, Dori, Ouahigouya, Dédougou, Bobo, Gaoua. Four additional capital-region
stations added in 2018 with government funding (Ouagadougou-IGB, Koubri, Dapélogo,
Tanguen-Dassouri). Registration is free at `www.bfcors.net`; the administrator
emails credentials. Two coups in 2022 and membership in the Alliance of Sahel
States (AES) from January 2025 have reduced bilateral technical cooperation with
France/West, but the IGB service has continued operating through both transitions.
No BF mountpoints on rtk2go or Centipede.

**missing**: confirm current host:port by completing registration at `bfcors.net`;
verify operational status given post-coup bilateral changes.

---

## ign_bj — IGN Bénin Permanent GNSS Station Network (BJ)

**status**:    candidate
**country**:   BJ — Benin
**type**:      single-base (physical CORS stations)
**host:port**: not publicly listed (disclosed after registration via IGN Bénin / CatIS)
**access**:    free with registration; accessible via Benin Cadastral Information System
**registration**: `service-public.bj` (service PS01085 — "Fichier des stations permanentes GNSS")
                  or direct contact with IGN Bénin (`ign.bj`)
**stations**:  7 physical: Cotonou, Abomey, Savalou, Parakou, Natitingou, Nikki, Kandi
**operator**:  IGN Bénin — Institut Géographique National du Bénin (`ign.bj`),
               under the Ministry of Land Affairs
**yearly_cost**: free

**date_added**: 2026-04-29

Seven permanent GNSS stations built with MCA-Bénin (Millennium Challenge Account)
funding, each stated to have a ~100 km coverage radius. The network is accessible
via the Benin Cadastral Information System (CatIS, `catistest.xroad.bj`). A
government service registration path is listed at `service-public.bj` under
"Fichier des stations permanentes GNSS" (PS01085). Seven stations across ~115,000 km²
gives average spacing ~130 km — adequate for L1+L2 RTK in the south where stations
are denser; northern coverage may have gaps. Zero BJ mountpoints on rtk2go or Centipede.

**missing**: confirm current NTRIP host:port by completing CatIS / IGN Bénin
registration; confirm station count and whether any stations have been added since
MCA-Bénin period.

---

## inc_gn — INC Guinea CORS (GN)

**status**:    free
**country**:   GN — Guinea (Conakry)
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    unknown — no public caster or registration portal discovered
**stations**:  unknown
**operator**:  INC — Institut National Cartographique, under the Ministry of
               Town Planning, Guinea (Conakry)
**yearly_cost**: unknown

**date_added**: 2026-04-29

INC is the national cartography and geodesy authority in Guinea. No public NTRIP
caster endpoint, RTK streaming service, or registration portal has been found in
any NTRIP directory, sourcetable, or academic reference. AFREF contributions from
Guinea, if any, are raw-archive RINEX. The 2021 coup (Colonel Mamadi Doumbouya /
CNRD) suspended Guinea from ECOWAS and reduced French bilateral geodetic technical
cooperation (IGN FI, AFD programmes), curtailing the pipeline for CORS modernisation
projects. Zero GN mountpoints on rtk2go or Centipede.

**missing**: confirm whether INC operates any NTRIP caster or has a candidate
endpoint; check AFREF ODC for GN station IDs; revisit when bilateral geodetic
cooperation resumes.

---

## datu_mr — DATU Mauritania Geodetic Network (MR)

**status**:    free
**country**:   MR — Mauritania
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    unknown — no public caster or registration portal discovered
**stations**:  unknown
**operator**:  DATU — Direction des Affaires Topographiques et de l'Urbanisme,
               Ministry of Housing and Urbanism, Nouakchott, Mauritania
**yearly_cost**: unknown

**date_added**: 2026-04-29

DATU is the national authority responsible for geodesy and cadastre in Mauritania.
No public NTRIP caster endpoint, RTK streaming service, or self-service registration
has been found. Mauritania's territory is ~1,031,000 km², predominantly Saharan
desert with extremely sparse road and power infrastructure outside the Atlantic
coastal strip; a national CORS network is a very long-term infrastructure prospect.
AFREF contributions from Mauritania, if any, are raw-archive RINEX only. No US/EU
sanctions apply to Mauritania. Zero MR mountpoints on rtk2go or Centipede.

**missing**: confirm whether DATU or a successor agency has any NTRIP endpoint;
check AFREF ODC for MR station IDs; search Arabic-language Mauritanian government
portals for any announced CORS programme.

---

## dgigc_tg — Togo National CORS Network (TG)

**status**:    candidate
**country**:   TG — Togo
**type**:      single-base (physical CORS stations, exact count unconfirmed)
**host:port**: not publicly listed (contact DGIGC)
**access**:    professional use; registration via DGIGC; access terms not
               published on public website
**registration**: `urbanisme.gouv.tg` (Ministry of Town Planning and Urban
                  Development website)
**stations**:  unconfirmed count; deployment began 2017; 614 geodetic benchmarks
               nationwide as of 2025; CORS stations at key reference points
**operator**:  DGIGC — Direction Générale de l'Information Géographique et de la
               Cartographie, Ministry of Town Planning and Urban Development
               (`urbanisme.gouv.tg`)
**yearly_cost**: unknown (no public tariff)

**date_added**: 2026-04-29

A national CORS network was deployed from 2017 under DGIGC. A March 2026
interministerial communiqué mandated systematic attachment of all topographic,
cadastral, urbanism, and infrastructure work to the National Geodetic Network,
with a three-month compliance window. As of April 2026, Togo has 614 geodetic
benchmarks (1st, 2nd, and 3rd order) including 11 first-order benchmarks. No
public NTRIP caster host:port has been found in any directory, sourcetable, or
published registration portal. Zero TG mountpoints on rtk2go or Centipede.

**missing**: confirm NTRIP host:port by contacting DGIGC via `urbanisme.gouv.tg`;
confirm exact CORS station count and access model; check whether any stations
have been shared to rtk2go or Centipede.

---

## igntc_cf — CAR National Geodesy / Mapping Authority (CF)

**status**:    rejected
**country**:   CF — Central African Republic
**type**:      unknown
**host:port**: not publicly listed
**access**:    unknown
**registration**: no public portal found
**stations**:  unknown; no stations identified in IGS Network or AFREF ODC
**operator**:  Ministry of Town Planning and Housing (IGN-equivalent national
               mapping function); ICASEES (`icasees.org`) handles statistics
               only and does not operate geodetic infrastructure
**yearly_cost**: n/a

**date_added**: 2026-04-29

No public CORS network or NTRIP caster has been found for the Central African
Republic. The country has experienced near-continuous armed conflict since 2012;
government authority outside Bangui is extremely limited. Wagner/Africa Corps
presence since 2018 and ongoing CPC insurgency severely constrain civilian
infrastructure investment. No CAR station appears in the IGS Network or AFREF
Operational Data Centre. Zero CF mountpoints on rtk2go or Centipede.

**missing**: confirm whether any CAR government agency has deployed CORS or
filed a station with the AFREF ODC; search French-language Bangui government
portals for any announced geodesy programme.

---

## dgcf_gw — DGCF Guinea-Bissau (GW)

**status**:    rejected
**country**:   GW — Guinea-Bissau
**type**:      unknown
**host:port**: not publicly listed
**access**:    unknown
**registration**: no public portal found
**stations**:  unknown; no GW station identified in IGS Network or AFREF ODC
**operator**:  DGCF — Direcção-Geral de Cartografia e Fotogrametria, Ministry
               of Urban Planning and Construction
**yearly_cost**: n/a

**date_added**: 2026-04-29

No public CORS network or NTRIP caster has been found for Guinea-Bissau.
Portuguese geodetic partner LNEG produced the national geological map (2014)
in collaboration with the Directorate of Geology and Mines; geodetic work is
at raw-archive level only. No GW station appears in the IGS Network or the
AFREF Operational Data Centre. Zero GW mountpoints on rtk2go or Centipede.

**missing**: confirm whether DGCF or any other GW agency has deployed CORS or
shared stations with AFREF ODC; search Portuguese-language GW government
portals for any announced GNSS modernisation programme.

---

## igebu_bi — IGEBU (BI)

**status**:    rejected
**country**:   BI — Burundi
**type**:      unknown
**host:port**: not publicly listed
**access**:    unknown
**registration**: no public portal found
**stations**:  unknown; no BI station identified in IGS Network or AFREF ODC
**operator**:  IGEBU — Institut Géographique du Burundi (`igebu.bi`); under
               the Ministry of Water, Environment, Land Management and Urban
               Planning
**yearly_cost**: n/a

**date_added**: 2026-04-29

IGEBU is the national mapping and hydro-meteorological authority. A JICA-supported
technical cooperation project transferred GNSS equipment and coordinate-transformation
skills to IGEBU; technology transfer was completed and verified in October 2010. No
public CORS network or NTRIP caster has been found. No BI station appears in the IGS
Network or the AFREF Operational Data Centre. Zero BI mountpoints on rtk2go or
Centipede.

**missing**: confirm whether IGEBU or any other BI agency has deployed CORS since 2010;
check whether the 2024 National Technical Geomatics Committee (`sp-bcg.gov.bi`)
activities include any CORS deployment plan; search French-language Bujumbura
government portals for any announced RTK programme.

---

## rgn_rw — Rwanda Geodetic Network / RGN (RW)

**status**:    restricted
**country**:   RW — Rwanda
**type**:      single-base (physical CORS)
**host:port**: not publicly listed
**access**:    free (post-processed RINEX confirmed); real-time RTK/NTRIP access
               model not confirmed
**registration**: `lands.rw` (RLMUA portal)
**stations**:  ~10 CORS sites nationwide
**operator**:  RLMUA — Rwanda Land Management and Use Authority (`lands.rw`)
**yearly_cost**: n/a (post-processed data stated free of charge)

**date_added**: 2026-04-29

The Rwanda Geodetic Network (RGN) is a network of ~10 CORS owned, maintained, and
operated by RLMUA. RLMUA states that RGN "analyses and distributes the data free of
charge." Published documentation describes post-processed RINEX/coordinate data for
surveyors, GIS users, engineers, and the public. No NTRIP caster host:port has been
found in any public sourcetable, CORS directory, or RLMUA web page. Challenges noted
by RLMUA include high setup costs (only 10 sites established), power instabilities,
and insufficient user skills — consistent with post-processed-only distribution.
Zero RW mountpoints on rtk2go or Centipede.

**missing**: confirm whether RGN has an NTRIP real-time streaming endpoint by
contacting RLMUA via `lands.rw`; confirm whether the 10 CORS sites include any
mountpoints accessible via standard NTRIP client; check whether station count has
grown since the 2010s AFREF affiliation efforts.

---

## gnet_gl — GNet Greenland Geodetic Network (GL)

**status**:    restricted
**country**:   GL — Greenland (Danish autonomous territory)
**type**:      n/a (geodetic reference network; no streaming NTRIP caster)
**host:port**: not publicly listed
**access**:    restricted (RINEX data via EarthScope/UNAVCO archive; real-time stream
               not publicly advertised)
**registration**: https://www.unavco.org/data/gps-gnss/data-access-methods/
**stations**:  ~60 continuous GNSS stations across Greenland
**operator**:  DTU Space (Technical University of Denmark) + Asiaq (Greenland Survey)
               in collaboration with DMI, NGA, and UNAVCO
**yearly_cost**: n/a (archive data free; no NTRIP subscription model identified)

**date_added**: 2026-04-29

GNet is a geodetic monitoring network spanning Greenland, maintained primarily for
ice-sheet dynamics research, sea-level and glacial isostatic rebound studies, and
geodetic reference-frame maintenance. DTU Space leads science operations; Asiaq
(Greenland Survey, based in Nuuk) contributes Greenlandic territorial operations.
RINEX data are archived at UNAVCO / EarthScope GAGE Facility and are freely accessible
for post-processing. No public NTRIP streaming caster has been identified. SDFi
(Styrelsen for Dataforsyning og Infrastruktur), Denmark's national mapping authority,
holds geodetic responsibility for Greenland but does not operate a public Greenlandic
NTRIP service. Zero GRL stations confirmed in rtk2go, Centipede, or EarthScope
NOTA streaming sourcetables.

**missing**: confirm whether DTU Space, Asiaq, or SDFi has established or is
             planning a public NTRIP streaming service for Greenland; check whether
             any EarthScope NOTA stations in Greenland carry streaming access.

## umhvorvisstovan_fo

**status**:    rejected
**country**:   FO — Faroe Islands (Danish autonomous territory)
**type**:      n/a (no CORS network / NTRIP service identified)
**host:port**: not publicly listed
**access**:    n/a
**registration**: n/a
**stations**:  0 confirmed NTRIP mountpoints; one EPN permanent station (ARGI00FRO,
               Argir/Tórshavn) used for reference-frame maintenance only
**operator**:  Umhvørvisstovan — The Faroese Environment Agency (`umhvorvisstovan.fo`)
**yearly_cost**: n/a

**date_added**: 2026-04-29

Umhvørvisstovan holds responsibility for surveying, mapping, and geodesy of the
Faroe Islands (land and sea). The agency operates UAV-based mapping programmes and
publishes topographic data. One EPN station, ARGI00FRO (Argir, Tórshavn), is part
of the EUREF Permanent GNSS Network; RINEX 2 data submission ceased February 2021.
No public NTRIP caster, RTK correction service, or CORS network with streaming
endpoint has been found in any sourcetable, national directory, or agency web page.
Danish GPSnet explicitly excludes the Faroe Islands. Zero FRO mountpoints on
rtk2go or Centipede. A Geospatial Centre at Fróðskaparsetur Føroya (Setur, the
University of the Faroe Islands) was launched in partnership with Landsverk and
Umhvørvisstovan to develop geodesy and surveying capacity — this may lead to a
public CORS service in future.

**missing**: confirm whether Umhvørvisstovan or Landsverk has established or is
planning a public NTRIP service; check whether ARGI00FRO RINEX data resumed
post-2021 and whether any real-time stream is accessible.

## gibr_gi — BIGF/IGS Reference Station Gibraltar (GI)

**status**:    rejected
**country**:   GI — Gibraltar (British Overseas Territory)
**type**:      single-base (scientific tide-gauge monitoring station)
**host:port**: not publicly listed (RINEX data via BIGF archive at bigf.ac.uk)
**access**:    restricted (archive data; not a walk-up RTK correction service)
**registration**: https://www.bigf.ac.uk/request_data/form.html
**stations**:  1 (GIBR — at the Gibraltar tide gauge; IGS TIGA project)
**operator**:  BIGF (British Isles GPS Facility, NERC / BGS)
**yearly_cost**: n/a (archive data free on request; no subscription)

**date_added**: 2026-04-29

The Gibraltar GNSS station (GIBR) is part of the BIGF network operated by the
Natural Environment Research Council / British Geological Survey. It is co-located
with the tide gauge and contributes to the IGS TIGA sea-level project. RINEX
data is available on request from BIGF. No real-time NTRIP stream is offered;
HM Government of Gibraltar's GeoPortal (geoportal.gov.gi) provides no NTRIP
or RTK correction service. Hobbyists working in Gibraltar can use ERGNSS (ES)
free of charge: Tarifa (TAR00/TAR20) is ~16 km away and Ceuta (CEU10) ~28 km —
both within the useful L1+L2 RTK baseline.

## ky_cors — Cayman Islands CORS / PAIP (KY)

**status**:    paid
**country**:   KY — Cayman Islands (British Overseas Territory)
**type**:      single-base (4 CORS: GCFS, GCEA on Grand Cayman; CBMD on Cayman Brac; LCSB on Little Cayman)
**host:port**: not publicly listed
**access**:    paid (real-time RTK subscription; RINEX post-processing free)
**registration**: https://www.caymanlandinfo.ky/Services/Surveying/Geodetic-System
**yearly_cost**: not publicly listed (contact Chief Surveyor via caymanlandinfo.ky)
**stations**:  4 physical CORS (PAIP network; additional RTK infill stations installed for full island coverage)
**operator**:  Lands and Survey Department, Cayman Islands Government

**date_added**: 2026-04-29

The Positional Accuracy Improvement Programme (PAIP) established a modern GPS
control infrastructure across all three Cayman Islands under the CIGD11 geodetic
datum (epoch 2011-01-01). RINEX data are freely available; real-time RTK corrections
are offered as a subscription package but pricing and the NTRIP host:port are not
published — prospective users must contact the Chief Surveyor. No EarthScope COCONet
station exists in Cayman waters. Zero rtk2go or Centipede volunteer bases.

**missing**: confirm whether a public NTRIP caster or host:port is listed anywhere;
determine subscription pricing.

## cw_cors — Curaçao Geodetic / Kadaster CORS (CW)

**status**:    rejected
**country**:   CW — Curaçao
**type**:      unknown (no public caster endpoint identified)
**host:port**: not publicly listed
**access**:    unknown — no public self-service registration portal found
**registration**: https://www.kadaster.cw/contact
**yearly_cost**: n/a (no public service)
**stations**:  unknown; NSGI can establish GNSS infrastructure at local government request
**operator**:  Stichting Kadaster en Openbare Registers Curaçao (`kadaster.cw`);
               geodetic support available from NSGI (`nsgi.nl`) on request

**date_added**: 2026-04-29

No public RTK correction service or NTRIP caster found. Kadaster Curaçao maintains
the land registry and cadastre; NSGI (the Netherlands' national geodetic authority)
can provide geodetic infrastructure including GNSS reference station establishment
and inclusion in AGRS.NL on request from the Curaçao government. Whether a public
NTRIP caster has been established through that channel is not confirmed. EarthScope
COCONet station CN40_RTCM3P3 (12.18°N, −68.96°W) streams via
`ntrip.earthscope.org:2101` under NULA (free non-commercial) — the practical free
option for the island. Three rtk2go volunteer bases near Willemstad (CWM_JAJO,
MPA_JAJO, UTE_JAJO) supplement EarthScope coverage.

**missing**: verify with Kadaster Curaçao or NSGI whether any public NTRIP caster
or RTK correction service exists for Curaçao.

## aw_cors — Aruba Geodetic / DLV CORS (AW)

**status**:    rejected
**country**:   AW — Aruba
**type**:      unknown (no public caster endpoint identified)
**host:port**: not publicly listed
**access**:    unknown — no public self-service registration portal found
**registration**: https://www.gobierno.aw/en/dienst-landmeetkunde-en-vastgoedregistratie-dlv
**yearly_cost**: n/a (no public service)
**stations**:  unknown
**operator**:  Dienst Landmeetkunde en Vastgoedregistratie (DLV), Government of Aruba
               (`gobierno.aw`)

**date_added**: 2026-04-29

No public RTK correction service or NTRIP caster found. DLV is the geodetic and
survey authority for Aruba, responsible for coordinate systems and land registration.
NSGI can provide geodetic infrastructure on request. EarthScope COCONet station
CN19_RTCM3P3 (12.61°N, −70.05°W, installed 2013) streams via
`ntrip.earthscope.org:2101` under NULA (free non-commercial) — the practical free
option for the island. One rtk2go volunteer base (PINOST1, Santa Cruz) is also present.

**missing**: verify with DLV whether any public NTRIP caster or RTK correction
service exists for Aruba.

## bq_cors — BES Islands Geodetic / Kadaster NL (BQ)

**status**:    rejected
**country**:   BQ — Bonaire, Sint Eustatius, Saba (Dutch special municipalities)
**type**:      unknown (no public caster endpoint identified)
**host:port**: not publicly listed
**access**:    unknown — no public self-service registration portal found
**registration**: https://bes.kadaster.nl/
**yearly_cost**: n/a (no public service)
**stations**:  unknown; NSGI may include at least one GNSS reference station per
               island in AGRS.NL
**operator**:  Kadaster Nederland — BES (`bes.kadaster.nl`); geodetic support from
               NSGI (`nsgi.nl`), which publishes the BESTRANS transformation for
               BES coordinate systems

**date_added**: 2026-04-29

Bonaire, Sint Eustatius, and Saba are special municipalities of the Netherlands.
Kadaster Nederland took over cadastral and surveying functions for the BES islands
on 1 January 2021. NSGI maintains BESTRANS (the transformation between BES local
coordinate systems and ITRS) and can include permanent GNSS reference stations in
AGRS.NL. No public NTRIP caster or host:port has been found. The nearest EarthScope
COCONet station is CN40_RTCM3P3 on Curaçao (~80 km from Bonaire), reachable via
`ntrip.earthscope.org:2101` under NULA — marginal for L1-only hardware, usable with
dual-frequency. Zero BES-coded rtk2go or Centipede stations found.

**missing**: confirm with Kadaster BES or NSGI whether any AGRS.NL station on Bonaire,
Sint Eustatius, or Saba streams real-time corrections via NTRIP.

## sx_cors — Sint Maarten Geodetic / Kadaster SXM (SX)

**status**:    rejected
**country**:   SX — Sint Maarten (Dutch part)
**type**:      unknown (no public caster endpoint identified)
**host:port**: not publicly listed
**access**:    unknown — no public self-service registration portal found
**registration**: https://kadaster.sx/
**yearly_cost**: n/a (no public service)
**stations**:  unknown
**operator**:  Stichting Kadaster- en Hypotheekwezen Sint Maarten (`kadaster.sx`);
               spatial open data via Ministry of VROMI
               (`gis-vromi-sxm.opendata.arcgis.com`)

**date_added**: 2026-04-29

No public RTK correction service or NTRIP caster found. Kadaster Sint Maarten is a
private foundation established in 1999 that manages land registration and surveying;
it achieved GIS capability in 2025 (ArcGIS platform deployment). The Ministry of VROMI
operates an open spatial data portal. No NTRIP host:port or real-time correction
service has been announced. The nearest EarthScope COCONet station is CN59_RTCM3P3
(18.21°N, −63.05°W, country code AIA — physically on Anguilla, ~20 km north of Sint
Maarten), which streams via `ntrip.earthscope.org:2101` under NULA (free
non-commercial) and is usable from SXM territory at that baseline.

**missing**: verify with Kadaster Sint Maarten or VROMI whether any NTRIP caster
or RTK correction service exists on Sint Maarten.

## regat_dz — REGAT Permanent GPS Network (DZ)

**status**:    restricted
**country**:   DZ — Algeria
**type**:      physical single-base (53–56 continuously operating GPS stations)
**host:port**: not publicly listed
**access**:    restricted — operated under the Ministry of National Defence (INCT);
               no self-service registration or public NTRIP endpoint published
**registration**: https://www.inct.mdn.dz/
**yearly_cost**: n/a (no public commercial service)
**stations**:  53–56 physical stations across the Algerian Atlas and northern Tell
               (Algiers, Oran, Constantine, Ouargla, Béchar, Tindouf and ~47 others);
               planned expansion to ~150+ stations
**operator**:  Institut National de Cartographie et de Télédétection (INCT),
               Ministry of National Defence (`inct.mdn.dz`)

**date_added**: 2026-04-29

REGAT (Réseau Géodésique de l'ATlas) is a seismotectonic/geodetic monitoring network
operated by INCT under the Algerian Ministry of National Defence. The network spans the
Nubia-Eurasia plate boundary — the most seismically active segment of North Africa —
and is used for crustal deformation monitoring and seismic hazard assessment, not for
real-time RTK corrections to end users. Station data are collected in RINEX format for
post-processing in research contexts; no streaming NTRIP caster has been identified in
any public documentation. INCT also deployed an initial 6-station backbone (Algiers,
Oran, Constantine, Ouargla, Béchar, Tindouf) before 2018 with plans to reach 146
stations nationally, but no public NTRIP service has been announced. Because INCT is a
subordinate body of the Ministry of National Defence, a hobbyist NTRIP service is
structurally unlikely without a separate civilian mandate.

**missing**: confirm whether any civilian or commercial NTRIP caster exists in Algeria
(independent of INCT), and whether REGAT RINEX data are accessible via UNAVCO/EarthScope
or a national data portal.

## esa_cors_eg — Egyptian Survey Authority CORS (EG)

**status**:    restricted
**country**:   EG — Egypt
**type**:      physical single-base (~40 stations, CORS + NACN combined)
**host:port**: not publicly listed
**access**:    restricted — established for internal government/cadastral use and
               national infrastructure projects; no public self-service portal found
**registration**: https://www.esa.gov.eg/
**yearly_cost**: n/a (no public commercial service)
**stations**:  ~40 physical stations across Cairo, Nile Delta, and surrounding regions
               (CORS network established 2012, adjusted to ITRF2008/2014; NACN
               established 1997)
**operator**:  Egyptian Survey Authority (ESA / الهيئة المصرية العامة للمساحة),
               under the Ministry of Water Resources and Irrigation (`esa.gov.eg`)

**date_added**: 2026-04-29

ESA established the first Egyptian CORS network in January 2012 (adjusted to ITRF2008,
epoch 2011.8096) and has since updated it to ITRF2014. The network is concentrated in
the Cairo corridor and Nile Delta — Egypt's population and agricultural heartland. ESA
also operates NACN (New Agricultural Cadastral Network, 1997), which has been tied to
the HARN zero-order reference network. No streaming NTRIP caster or real-time RTK
correction service has been publicly announced; the CORS infrastructure appears to be
used for government land administration, infrastructure projects, and tectonic/subsidence
research rather than as a public positioning service. No pricing, registration URL, or
host:port for public access has been found in any open source.

**missing**: confirm whether ESA has opened any NTRIP endpoint, even on a paid or
institutional basis, and whether any commercial RTK service operates in Egypt.

---

## ipgn — Iranian Permanent GNSS Network (IR)

**status**:    restricted
**date_added**: 2026-04-29
**country**:   IR
**type**:      physical single-base (~127 stations)
**host:port**: not confirmed for real-time NTRIP streaming; portal `ipgn.ncc.gov.ir`
**access**:    registration at `ipgn.ncc.gov.ir/en/accounts/signup/` — web portal
               accessible internationally but real-time NTRIP streaming reachability
               from outside Iran not confirmed; internet filtering (national intranet)
               may block external connections
**registration**: `ipgn.ncc.gov.ir/en/accounts/signup/`
**yearly_cost**: not publicly listed
**stations**:  ~127 physical CORS (phase 1: 2004–2006, 106 stations; phase 2: completed
               2013, 127 stations in ITRF2014)
**operator**:  National Cartographic Center of Iran (سازمان نقشه‌برداری کشور / NCC),
               `ncc.gov.ir`

Iranian Permanent GNSS Network for Geodynamics: established post-2003 Bam earthquake
for tectonic monitoring, velocity and strain-field estimation. Base network covers
Zagros Mountains, Central Iran, Alborz, East Iran, Makran, Loot, and Kopeh-Dagh; three
local sub-networks. Data archived to IGS for scientific post-processing. Primarily a
geodynamics and reference-frame resource — real-time RTK correction delivery for
hobbyists is not the stated purpose. Reachable NTRIP streaming from outside Iran is
unconfirmed due to Iran's filtered internet infrastructure.

**missing**: confirm whether ipgn.ncc.gov.ir exposes a live NTRIP sourcetable accessible
from outside Iran, and what mountpoint credentials are issued to registered users.

---

## shamim_ir — SHAMIM (IR)

**status**:    restricted
**date_added**: 2026-04-29
**country**:   IR
**type**:      physical single-base (VRS / NRTK capable, 144 stations)
**host:port**: `178.252.171.15:2101`
**access**:    free-with-registration — Iranian national ID (کد ملی) required;
               inaccessible to foreign users; no foreign-resident registration path
**registration**: `shamim.ssaa.ir` (Organisation for Registration of Deeds and
                  Properties / سازمان ثبت اسناد و املاک کشور)
**yearly_cost**: free for non-commercial use (personal national-ID subscription)
**stations**:  144 physical permanent GNSS stations nationwide (installed 2016–2017)
**operator**:  Organisation for Registration of Deeds and Properties
               (سازمان ثبت اسناد و املاک کشور, `ssaa.ir`)

SHAMIM (شمیم — abbreviation for شبکه موقعیت‌یابی یکپارچه مالکیت‌ها, Integrated Unified
Property Management Network) is the national cadastral CORS network operated by Iran's
property registration authority. Supports Nearest, VRS, FKP, MAX, and IMAX virtual
reference modes; achieves 8 mm + 1 ppm accuracy in static mode. Designed to accelerate
the national cadastral survey programme.

Registration requires an Iranian national identification number, making the service
inaccessible to foreign hobbyists or researchers. NTRIP caster IP (`178.252.171.15:2101`)
is published in Persian-language surveying community documentation. Not added to pipeline:
national-ID gating makes it a restricted domestic service, not a publicly-accessible
free NTRIP endpoint.

---

## rgna_mx — Red Geodésica Nacional Activa (MX)

**status**:    free
**date_added**: 2026-04-29
**country**:   MX
**type**:      physical single-base (~36 stations)
**host:port**: not publicly listed (geodesia.inegi.org.mx portal references an NTRIP service;
               no host:port discovered from public sources)
**access**:    free-with-registration — access to real-time streaming appears to require direct
               contact with INEGI's geodesy department; RINEX downloads are fully self-service
**registration**: `inegi.org.mx/temas/geodesia_activa/` (contact for streaming access)
**yearly_cost**: free (RINEX); streaming terms not publicly documented
**stations**:  ~36 permanent GNSS stations distributed nationally (as of CALE2025 coordinate catalogue)
**operator**:  INEGI — Instituto Nacional de Estadística y Geografía (`inegi.org.mx`)

The RGNA is Mexico's national active geodetic reference network under INEGI. Stations record
GNSS data continuously, contributing to SIRGAS and IGS. RINEX files are freely downloadable
at `inegi.org.mx/app/geo2/rgna/`. INEGI technical documentation references a real-time NTRIP
service hosted at `geodesia.inegi.org.mx`, but no public self-service registration portal or
host:port has been found through open-source research. Not added to pipeline pending endpoint
confirmation.

**missing**: confirm whether geodesia.inegi.org.mx exposes a live NTRIP sourcetable accessible
to the public, and what credentials or registration pathway grants streaming access.

---

## red_cors_mx — Red CORS México (MX)

**status**:    paid
**date_added**: 2026-04-29
**country**:   MX
**type**:      physical single-base (85+ coverage cities nationwide)
**host:port**: not publicly listed
**access**:    paid — monthly and annual memberships; pricing not on public website (contact required)
**registration**: `dtmtopografia.com/cors-mexico/membresias/`
**yearly_cost**: not publicly listed
**stations**:  85+ cities with coverage (physical CORS count not published)
**operator**:  DTM Topografía (`dtmtopografia.com`)

Red CORS México® is described as the largest commercial CORS network in Mexico by national
coverage. Transmits RTK corrections via NTRIP; compatible with any brand GNSS RTK receiver.
Monthly and annual subscription tiers available. Not added to pipeline: paid service.

---

## geocors_mx — GeoCORS / Survey+ (MX)

**status**:    paid
**date_added**: 2026-04-29
**country**:   MX
**type**:      physical single-base (55+ stations)
**host:port**: not publicly listed
**access**:    paid — subscription; 15-day demo available; pricing not on public website
**registration**: `en.surveyplusmx.com`
**yearly_cost**: not publicly listed
**stations**:  55+ CORS stations nationally
**operator**:  Survey+ / CORS México (`surveyplusmx.com`)

GeoCORS (branded Survey+) is the second major commercial CORS NTRIP network in Mexico,
claiming the largest physical station count nationally. Offers a free 15-day demo for GNSS
devices. Not added to pipeline: paid service.

---

## hitarget_cors_mx — Hi-Target Red CORS Mexico (MX)

**status**:    paid
**date_added**: 2026-04-29
**country**:   MX
**type**:      physical single-base / VRS
**host:port**: not publicly listed
**access**:    paid — monthly licence; ~MX$2,414/month (~$120/yr annualised, under $200/yr cutoff)
**registration**: resellers (e.g. `puntovisado.com`)
**yearly_cost**: ~MX$2,414/month (reseller price); annual rate approximately MX$29,000 (~$1,450/yr)
**stations**:  not published separately (resold network)
**operator**:  Hi-Target (hardware vendor); resold via Mexican GNSS dealers

Hi-Target CORS licences are sold monthly through Mexican GNSS equipment resellers.
The monthly price (~MX$2,414) corresponds to roughly $120/month or ~$1,450/yr — above the
$200/yr paid-affordable cutoff. Not added to pipeline: paid service.

---

## sirgas_chile — RGN/SIRGAS-CHILE (CL)

**status**:    free
**date_added**: 2026-04-29
**country**:   CL
**type**:      physical single-base (180+ CORS stations)
**host:port**: not publicly listed (real-time NTRIP service announced 2025; no public
               host:port discoverable — procedure video at youtube.com/watch?v=4yuH1W05eII)
**access**:    RINEX free; real-time NTRIP access appears to require contact with IGM
               (`ventas@igm.cl` or geodesy department)
**registration**: `sirgaschile.cl` (coordinate certificates and RINEX); NTRIP streaming
                  registration not self-service
**yearly_cost**: RINEX free; streaming terms not publicly documented
**stations**:  180+ CORS stations; expanded by 28 new first-level stations announced 2025
**operator**:  IGM — Instituto Geográfico Militar de Chile (`igm.cl`, `sirgaschile.cl`)

SIRGAS-CHILE is Chile's national geodetic reference network under the army's IGM. Consists
entirely of CORS stations covering the national territory from Arica to Punta Arenas. In 2025
IGM launched a renovated sirgaschile.cl platform and announced real-time NTRIP streaming
services alongside the existing RINEX download and online post-processing (PPP) tools.
No public self-service registration portal or host:port for the NTRIP caster has been found
through open-source research. Not added to pipeline pending endpoint confirmation.

**missing**: confirm whether a public-facing NTRIP sourcetable is live at igm.cl or
sirgaschile.cl, and what registration pathway (if any) grants free hobbyist access.

---

## geocom_gnss_cl — Geocom GNSS Network (CL)

**status**:    paid
**date_added**: 2026-04-29
**country**:   CL
**type**:      physical single-base / VRS
**host:port**: not publicly listed
**access**:    paid — subscription; 6-month demo reportedly available on request; pricing not
               on public website
**registration**: `geocom.cl/pages/red-gnss`
**yearly_cost**: not publicly listed
**stations**:  not published (commercial network covering major population centres)
**operator**:  Geocom (`geocom.cl`)

Geocom's GNSS network provides RTK corrections for professional survey use across Chile.
Network calculated at epoch 2025.0 and linked to SIRGAS via fiducial stations. Not added
to pipeline: paid service.

---

## kollnet_cl — KollNET (CL)

**status**:    paid
**date_added**: 2026-04-29
**country**:   CL
**type**:      physical single-base / VRS
**host:port**: not publicly listed
**access**:    paid — prepaid packages (7-day / 15-day / 30-day / annual); pricing not publicly
               listed
**registration**: `kollnerlabrana.cl/kollnet.html`
**yearly_cost**: not publicly listed
**stations**:  not published
**operator**:  Kollner Labraña & Cía. Ltda. (`kollnerlabrana.cl`)

KollNET is a commercial NTRIP CORS correction service operated by a Chilean surveying
equipment company. Not added to pipeline: paid service.

---

## ign_cr_cors — IGN-CR CORS / SNIT NTRIP Caster (CR)

**status**:    candidate
**date_added**: 2026-04-29
**country**:   CR
**type**:      physical single-base (14 stations)
**host:port**: `igncaster.snitcr.go.cr:2101` (port inferred from standard NTRIP; not
               independently confirmed from sourcetable)
**access**:    free-with-registration — SNIT account required; after registration a twice-daily
               validation cycle (00:00 / 12:00 local) activates caster access
**registration**: `snitcr.go.cr` (create SNIT account → Herramientas → Herramientas GNSS →
                  accept terms)
**yearly_cost**: free
**stations**:  14 permanent GNSS stations; data also used for RINEX download and online
               post-processing; part of Red Geodésica Nacional de Referencia Horizontal (GNRH)
**operator**:  IGN — Instituto Geográfico Nacional (part of Registro Nacional, `snitcr.go.cr`)

The IGN-CR CORS network provides real-time NTRIP corrections and RINEX data via the SNIT
(Sistema Nacional de Información Territorial) platform. Corrections reference the CR-SIRGAS
geodetic framework. The caster hostname `igncaster.snitcr.go.cr` is referenced in multiple
secondary sources; port 2101 is inferred (standard NTRIP) but not confirmed from a live
sourcetable fetch. Not yet added to pipeline: host:port needs confirmation and access requires
SNIT account creation (free, web-based).

**investigate**: confirm live sourcetable at igncaster.snitcr.go.cr:2101 and that physical

---

## nignet — NIGNET (NG)

**status**:    restricted
**date_added**: 2026-04-29
**country**:   NG
**type**:      physical single-base (geodetic reference network)
**host:port**: host:port not publicly listed; a research NTRIP prototype with BKG
               Standard NTRIP Caster (Linux) and PayPal payment integration was
               documented in academic literature but no stable public endpoint
               confirmed as of 2026
**access**:    no public free access; the research prototype was described as
               paid (PayPal); operational real-time service not confirmed
**yearly_cost**: not publicly listed
**stations**:  9–16 physical CORS stations (sources vary; OSGoF literature states
               15–16; AFREF lists 9 operational); 500–1,000 km inter-station
               spacing — designed for geodetic reference frame (AFREF), not RTK
**operator**:  OSGoF — Office of the Surveyor General of the Federation
               (`osgof.gov.ng`)
**source**:    osgof.gov.ng; academic literature (ubibliorum.ubi.pt NTRIP prototype
               paper); gnssnigeria.com

NIGNET was established to maintain the Nigerian Geodetic Reference Frame and
contribute to AFREF. Inter-station distances of 500–1,000 km across Nigeria's
923,768 km² make reliable L1+L2 network RTK impractical — corrections would be
extrapolated well beyond the 50–70 km baseline limit. A research paper documented
implementation of an NTRIP caster on the network with a management system and
PayPal payment integration; this has not been confirmed as a stable, publicly
accessible service. No free hobbyist NTRIP path identified.

**missing**: confirm whether any endpoint at osgof.gov.ng or gnssnigeria.com
             has been made publicly available; check if commercial providers
             (e.g. CHCNAV RTK network cited as operating in Nigeria) have
             established a hobbyist-accessible caster.

## sok_ke — Survey of Kenya CORS / Geodetic Control (KE)

**status**:    restricted
**date_added**: 2026-04-29
**country**:   KE
**type**:      physical single-base (national geodetic control network)
**host:port**: host:port not publicly listed
**access**:    no public free access confirmed; SoK streams are issued to
               licensed surveyors under government contract — no hobbyist
               NTRIP path found
**yearly_cost**: not publicly listed
**stations**:  count not publicly confirmed; national geodetic control
               points distributed across Kenya
**operator**:  Survey of Kenya (SoK, `survey.go.ke`); RCMRD
               (Regional Centre for Mapping of Resources for Development,
               `rcmrd.org`) hosts geodetic research infrastructure but
               no confirmed independent public CORS stream
**source**:    survey.go.ke; scirp.org (accuracy assessment of private CORS
               vs. SoK control points, 2025); corsmap.com; ardusimple.com

No public NTRIP caster host:port for SoK has been found in any directory,
sourcetable, or academic source. Academic literature uses SoK geodetic
control points as a reference benchmark for private CORS accuracy tests —
confirming the network exists but is not publicly accessible for RTK
streaming. RCMRD geodetic infrastructure similarly has no confirmed public
NTRIP endpoint.

**missing**: confirm whether SoK or RCMRD have published an NTRIP caster
             endpoint for public or registered access; check survey.go.ke
             for any service portal.

## muya_cors_ke — Muya CORS (KE)

**status**:    paid
**date_added**: 2026-04-29
**country**:   KE
**type**:      physical single-base + network RTK
**host:port**: host:port disclosed post-registration (IP, port, username,
               password issued after signup at `muya-cors.com`)
**access**:    paid with registration; pricing not publicly listed on website
**yearly_cost**: not publicly listed (contact Measurement Systems Ltd)
**stations**:  ~25 base stations across Kenya (single-base and networked RTK)
**operator**:  Measurement Systems Ltd (`measurementsystems.org`),
               operating as Muya CORS (`muya-cors.com`)
**source**:    muya-cors.com; measurementsystems.org; ardusimple.com;
               georole.co.ke; orbital.co.ke (field use report, Sep 2024)

Muya CORS provides RTK corrections and post-processing services via a
network of GNSS CORS tracking GPS, GLONASS, BeiDou, and Galileo. Credentials
are issued post-registration. Pricing is not on the public website; described
as subscription-based in KSh. Used operationally in Nairobi (Kitisuru
topographic survey, Sep 2024). Over the $200/yr threshold — excluded from
pipeline. Only commercial RTK NTRIP option confirmed for Kenya.

**missing**: obtain current annual pricing in KSh and USD equivalent.

## tngc_tz — Tanzania National Geo-innovation Centre / Survey Division (TZ)

**status**:    restricted
**date_added**: 2026-04-29
**country**:   TZ
**type**:      physical single-base (national geodetic control)
**host:port**: host:port not publicly listed
**access**:    no public free access confirmed; TNGC focus is geodetic
               capacity-building and raw-observation archiving, not RTK
               streaming delivery
**yearly_cost**: not applicable (no NTRIP service confirmed)
**stations**:  AFREF-affiliated reference stations (raw-observation archives
               only); count not publicly confirmed as RTK-capable stream
**operator**:  Tanzania National Geo-innovation Centre (TNGC,
               `tngc.lands.go.tz`) / Survey and Mapping Division, Ministry
               of Lands, Housing and Human Settlements (MLHHSD)
**source**:    tngc.lands.go.tz; ardusimple.com/rtk-correction-services-and-ntrip-casters-in-tanzania;
               ntrip-list.com/africa

TNGC was established at the University of Dodoma with Korean government
support, primarily for GNSS capacity-building and geospatial training.
AFREF/IGS contributions from Tanzania are raw-observation archives — not
RTK streaming. No public NTRIP caster host:port has been found in any
directory or sourcetable. Tanzania is confirmed as not having a National RTK
Network by ArduSimple's Africa survey (2025).

**missing**: confirm whether TNGC or Survey Division have initiated any
             NTRIP streaming service; check tngc.lands.go.tz for updates.

## cenacarta_mz — CENACARTA CORS (MZ)

**status**:    restricted
**date_added**: 2026-04-29
**country**:   MZ
**type**:      physical single-base (geodetic reference / AFREF)
**host:port**: host:port not publicly listed
**access**:    no public free access confirmed; stations listed in Corsmap
               and AFREF datasets as raw-observation or static CORS only
**yearly_cost**: not applicable (no NTRIP service confirmed)
**stations**:  ~8 physical CORS stations: CHMO (Chimoio), MPTB (Maputo),
               QLMN (Quelimane), NACL (Nacala), LCNG (Lichinga), XXAI
               (Xai Xai), MTND (Tete), SOFL (Beira) — Corsmap dataset
**operator**:  CENACARTA — Centro Nacional de Cartografia e Teledetecção
               (`cenacarta.gov.mz`), Ministry of Agriculture; DINAGECA
               (Direcção Nacional de Geografia e Cadastro, Ministry of Land
               and Environment) for cadastral geodesy
**source**:    corsmap.com/location/mozambique; gim-international.com
               (CORS map Africa article); un-spider.org (CENACARTA profile);
               publico.pt (2006: first permanent GPS station established)

CENACARTA's ~8 CORS stations are documented in the Corsmap crowdsourced
Africa dataset and contribute to AFREF. No public NTRIP caster or RTK
streaming host:port has been found in any directory, sourcetable, or
academic reference. Corsmap notes direct contact was made with Mozambique
custodians — confirming CORS exist but no streaming NTRIP endpoint was
surfaced. DINAGECA handles cadastral geodesy separately; no independent
NTRIP caster confirmed for either agency.

**missing**: confirm whether CENACARTA or DINAGECA have stood up an NTRIP
             caster; check cenacarta.gov.mz and mozgis.gov.mz for service
             portals.
mountpoints (NMEA=0) are present; add to SOURCES once verified.

---

## ancfcc — Réseau GNSS Permanent ANCFCC (MA)

**status**:    free
**date_added**: 2026-04-29
**country**:   MA
**type**:      single-base
**host:port**: host:port not publicly listed
**access**:    restricted — licensed professional access only; no public NTRIP delivery identified
**stations**:  ~60 permanent GNSS stations including nodes at Laayoune and Dakhla
**source**:    ancfcc.gov.ma/ReseauGnss/
**operator**:  ANCFCC — Agence Nationale de la Conservation Foncière, du Cadastre et de la Cartographie

~60-station national GNSS network connected to a central server in Rabat via private
network. Provides RINEX archives and RTK/Network-RTK corrections. Access appears
restricted to licensed cadastral professionals; no public NTRIP caster endpoint has
been identified in any sourcetable, directory, or academic reference.

**missing**: confirm whether a public NTRIP endpoint exists or is planned; verify
             access terms at ancfcc.gov.ma.

---

## sen_cors — SEN-CORS (SN)

**status**:    free
**date_added**: 2026-04-29
**country**:   SN
**type**:      single-base (planned)
**host:port**: host:port not publicly listed
**access**:    not yet operational; no public NTRIP caster found
**stations**:  ~16 planned (PROCASEF/World Bank programme) + 5 additional (JICA, Dakar region)
**source**:    anat.sn; procasef.com; ignfi.fr (PROCASEF geodetic reference network)
**operator**:  ANAT (Agence Nationale de l'Aménagement du Territoire) and
               DTGC (Direction des Travaux Géographiques et Cartographiques)

SEN-CORS is the national permanent GNSS network under construction through the
PROCASEF land cadastre programme (World Bank funding) and a parallel JICA-backed
5-station deployment in Dakar. Physical installation and initial testing were
projected for late 2025/2026. No public NTRIP host:port has been published.

**missing**: confirm whether SEN-CORS has launched a public NTRIP caster;
             check anat.sn and procasef.com for service announcements.
