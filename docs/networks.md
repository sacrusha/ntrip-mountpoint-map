<!-- Process / rules: networks.proc.md (pipeline: pipeline.md) -->
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
**pipeline-flags**: `nmea_filter=False` (all physical stations wrongly tagged NMEA=1);
                    `solution_filter=True` (default — catches 16 NEAR-xxx/NEAR_xxx VRS
                    streams which are correctly tagged solution=1 by the caster)

Community volunteer aggregator operated by SNIP / use-snip.com. Regional filtered
views on `:2103` (PL) and `:2104` (JP) are the same server — not separate SOURCES
entries. Parser infers `carrier = 2` when carrier field is blank and format starts
with `RTCM 3` (required to retain ~98% of rtk2go entries). The 16 NEAR-xxx/NEAR_xxx
mountpoints (e.g. `NEAR-AUT`, `NEAR_DEU`) are regional nearest-station VRS streams;
the caster correctly marks them `solution=1` so the default solution filter excludes
them even with `nmea_filter` off.

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
**pipeline-flags**: `nmea_filter=False`; `solution_filter=False` (caster incorrectly
                    tags physical stations with both NMEA=1 and solution=1)

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
**pipeline-flags**: `solution_filter=False` (~42 IGS/international partner stations
                    re-streamed by AUSCORS are tagged solution=1 in the sourcetable
                    despite being physical receivers with fixed coordinates, e.g.
                    KIRU00SWE0 in Sweden, ENAO00PRT0 in the Azores)

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

## ugrf — UGRF CORS (UG)

**status**:    free
**host:port**: `ugrf.mlhud.go.ug:2101`
**type**:      physical-coord-vrs
**access**:    free; register at ugrf.mlhud.go.ug/SBC (Leica Spider Business Centre)
**pipeline-access**: registration
**stations**:  78 (40 government + 38 private)
**source**:    ugrf.mlhud.go.ug (Surveys and Mapping Department, MLHUD)
**operator**:  MLHUD — Ministry of Lands, Housing and Urban Development

Sourcetable publicly accessible without credentials; streaming requires individual
registration. Single-base mountpoints: ENTB (Entebbe), GULU, SRTI, MBRA, Nearest
(auto-select). Network-RTK mountpoints: I-Max, VRS. System: Leica GNSS Spider.
Endpoint confirmed 2026-05-02.

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
**type**:      physical-vrs
**access**:    free; register by emailing icecors@natt.is with company name, contact
               name and email address; credentials returned by email
**pipeline-access**: registration
**stations**:  33 (70–100 km spacing nationwide)
**source**:    natt.is (LMÍ — Landmælingar Íslands)
**operator**:  LMÍ — Landmælingar Íslands (National Land Survey of Iceland)

33 physical GNSS stations covering Iceland at 70–100 km intervals. Caster at
`178.19.53.126:2101` (GNSMART software). Offers both single-base (RTCM30,
not recommended beyond 20 km from nearest station) and network correction
(VRS30, FKP30). All corrections reference ISN2016.

The sourcetable exposes only 4 individually-addressable physical mounts
(AUSV, GEVK, SENG, VOGC — all near Reykjavik), plus RTCM30/RTCM30_MSM
nearest-station selectors at (0,0) and VRS3/VRS3_MSM network mounts at (0,0).
The remaining 29 stations are reached exclusively via the RTCM30 selector or
VRS mountpoints, not as individual entries. Displaying the 4 visible stations
would misrepresent the 33-station network as a Reykjavik-only fragment, so the
pipeline holds at 0 until the full sourcetable is available.

**Caster misconfiguration**: GNSMART tags all mountpoints `NMEA=1` including the
4 physical single-base entries (which have unique coordinates and `solution=0`).
`nmea_filter=False` would be needed once display of partial data is acceptable.

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

**status**:    paid
**host:port**: `aposrtk.bev.gv.at:2101`
**type**:      physical-coord-vrs
**access**:    paid via bev.gv.at portal; free for agriculture/forestry users
               via eAMA credentials (farm client number + PIN, Agrarmarkt Austria)
**yearly_cost**: €200/mo RTK (~$220/mo); no annual plan
**registration**: https://www.bev.gv.at
**stations**:  37
**source**:    bev.gv.at (BEV — Bundesamt für Eich- und Vermessungswesen)
**operator**:  BEV — Bundesamt für Eich- und Vermessungswesen

**date_added**: 2026-04-30

Austria's national VRS network operated by BEV. Sourcetable is publicly readable;
RTCM stream authentication requires valid credentials. Hobbyists register and pay
via the BEV portal. No annual plan is offered; pricing is per-second, per-day, or
per-month: RTK (centimetre accuracy) €0.0015/sec, €20/day, €200/month; DGPS
(decimetre accuracy) €0.00015/sec, €2/day, €20/month. One-time setup fee €50.
Agriculture/forestry users get free access via eAMA credentials. 37 physical
reference stations with distinct coordinates are exposed in the sourcetable; these
show on the map as regular pins. SAPOS Bavaria (DE) and FReDNet (IT) provide
partial coverage across the AT border.

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
in CI — likely location-based firewall (BKG/RTCM caster list independently confirms
`flepos.vlaanderen.be:2101` is correct). Coverage requires NRTK polygon (deferred).

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

Intermittent outages documented. Currently timing out in CI. The SPW portal
uses `gnss.wallonie.be`; NTRIP host:port not published — given to registered
users only.

**investigate**: endpoint `gnss.wallonie.be:2101` unconfirmed; obtain
credentials via registration to verify.

---

## latpos — LatPos (LV)

**status**:    free
**host:port**: `latpos.lgia.gov.lv:2101`
**type**:      single-coord-vrs
**access**:    free since 2018; SBC portal signup at latpos.lgia.gov.lv/SBC
**pipeline-access**: registration
**stations**:  0 (27 LV + 5 EE + 4 LT border stations declared; single-coord)
**source**:    latpos.lgia.gov.lv (LGIA)
**operator**:  LGIA — Latvijas Ģeotelpiskās informācijas aģentūra

Domain `lgia.gov.lv` is live; SBC portal at `latpos.lgia.gov.lv` active but
registration-gated. Port changed from 5001 (Alberding directory, now timing out)
to 2101 (standard; NTRIP host:port given only post-registration).

**investigate**: confirm port 2101 resolves at `latpos.lgia.gov.lv` from a
Baltic-region IP; if still timing out, try 5001 again or contact LGIA.

---

## estpos — ESTPOS (EE)

**status**:    free
**host:port**: `gnss-rtk.maaruum.ee:2101`
**type**:      single-coord-vrs
**access**:    free until 31 Aug 2026 (director-general directive); portal account + service agreement
**pipeline-access**: conditions
**stations**:  0 (40 declared; VRS, iMAX, nearest-base; MSM5 available)
**source**:    www.maaruum.ee (Maa- ja Ruumiamet / Land and Spatial Authority)
**operator**:  Maa- ja Ruumiamet (Land and Spatial Authority)

Maa-amet rebranded as Maa- ja Ruumiamet and migrated to `maaruum.ee` (2025/26);
all `maaamet.ee` URLs redirect to the new domain. Old endpoint
`gnss-rtk.maaamet.ee:8083` no longer resolves. New NTRIP caster hostname and
port are unconfirmed — `gnss-rtk.maaruum.ee:2101` is the best current guess
(domain pattern preserved; port normalised to 2101). Pipeline updated to try
this address; verify from an Estonian IP. Service expiry Aug 2026 — review
before then.

**investigate**: confirm `gnss-rtk.maaruum.ee:2101` (or `estpos.maaruum.ee:2101`)
from an Estonian IP; check www.maaruum.ee/en/geodesy/gnss/estpos for current
endpoint docs and whether a service agreement is now required before the
sourcetable is served.

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
out in CI. Coverage requires NRTK polygon (deferred). `geoportal.sa` was
unreachable from an external session (browser-level failure, not HTTP error).

**investigate**: verify `ksacors.geoportal.sa:2101` from a Saudi/GCC IP;
cannot be confirmed or ruled out from outside the region.

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

Free networks with a confirmed host:port that have been added to
`fetch_stations.py` SOURCES but have not yet completed a successful cron fetch.
The next GitHub Actions run is the live verifier — type and counts may need
tuning once a sourcetable is observed.

---

## gpsbru — GPSBru / AGN (BE — Brussels)

**status**:    free
**host:port**: `agn.ngi.be` (port unconfirmed)
**type**:      single-base
**access**:    free; register at agn.ngi.be
**stations**:  1 (Uccle observatory)
**source**:    agn.ngi.be (NGI — National Geographic Institute)

Single station; useful only within ~30 km of Brussels. Low priority.

**missing**: confirm NTRIP port (standard 2101? try ncat/telnet agn.ngi.be 2101).

---

## thailand_dol — Thailand DOL LandGNSS (TH)

**status**:    free
**date_added**: 2026-05-04
**host:port**: `122.155.131.34:2101` (Central zone; full zone–port table at
               dol-rtknetwork.com/files/manual/1(PortNumber).pdf — 404 as of
               2026-05-04; other-zone ports not publicly accessible)
**type**:      unknown (sourcetable not yet observed; only mountpoint name in
               public docs is `VRS_RTCM32`)
**access**:    free with registration; Thai national ID (13-digit) required —
               foreign users cannot self-register via the standard form
**pipeline-access**: conditions
**registration**: https://dol-rtknetwork.com/index.php/register_gnss_beta
**stations**:  ~115–220 CORS (academic sources, 63 provinces)
**source**:    dol-rtknetwork.com (Department of Lands / กรมที่ดิน, Ministry of Interior)

Thai-language portal. Caster IP updated from `110.78.0.54` to `122.155.131.34`
(confirmed in DOL manuals); Central zone on port 2101. Added to SOURCES with a
best-guess `physical-vrs` type (national-CORS pattern); the next cron run is the
authoritative verifier and the type may need tuning then. Full zone–port PDF
currently 404; other-zone ports not publicly accessible. Possible future
credit/fee system indicated by a DOL procurement document (March 2026) but no
paid tier active as of 2026-05-04.

**investigate**: confirm sourcetable structure from the next cron run; obtain
full zone–port mapping for all regions.

---

## Deferred — free, endpoint not yet obtainable

---

## renep — ReNEP (PT)

**status**:    free
**host:port**: 193.137.94.71:2101 (physical single-base, RTCM3 GPS+GLONASS)
**type**:      physical-coord-vrs
**access**:    free; register at renep.dgterritorio.gov.pt
**stations**:  47
**source**:    dgterritorio.gov.pt (DGT — Direção-Geral do Território)
**pipeline-flags**: `nmea_filter=False` (39 of 47 physical stations on port 2101
                    wrongly tagged NMEA=1; VRS/network mounts live on separate ports
                    2106/2108 and do not appear in the port 2101 sourcetable, so the
                    override is safe)

IP confirmed live 2026-04-30. ETRS89 datum (mainland), ITRF93 (autonomous
regions). Stations and RINEX publicly visible. Port structure:

- **:2101** — 47 physical single-base stations, RTCM3 (GPS+GLONASS) → in pipeline
- **:2102** — same 47 stations, RTCM3 MSM5 (GPS+GLONASS+Galileo+BeiDou) → not ingested (duplicate)
- **:2106** — 3 VRS nearest-station mounts (NSRT23, NSRT, NSR5) → not ingested
- **:2108** — 2 network-correction mounts (ACRT, ACR5) → not ingested

**investigate**: confirm whether a hostname resolves to 193.137.94.71 (e.g.
ntrip.renep.dgterritorio.gov.pt) so the pipeline URL can use DNS rather than
a bare IP.

---

## litpos — LitPOS (LT)

**status**:    candidate
**host:port**: Primary: `193.219.10.2:2101` (VilniusTech Geodesy Institute, Vilnius;
               alt port 2111 noted by some users); Secondary: `195.182.72.152:2101`
               (GIS-Centras / VšĮ Statybos sektoriaus vystymo agentūra); both servers
               provide identical streams — no DNS hostnames published for either IP
**type**:      vrs-only
**access**:    free; register at geoportal.lt/web/litpos-paslauga/registracija
**stations**:  35
**operator**:  Nacionalinė žemės tarnyba (NZT — National Land Service under the Ministry
               of Agriculture); operated by GIS-Centras / VšĮ Statybos sektoriaus
               vystymo agentūra
**source**:    geoportal.lt (LitPOS service page and usage rules §3 — "visi LitPOS duomenys
               yra vieši ir teikiami nemokamai"); zinynas.geonovus.lt (IP/port, confirmed
               2026-04-30); curl 193.219.10.2:2101 → SOURCETABLE 200 OK, Trimble Ntrip
               Caster 5.2, Content-Length: 1677 (confirmed 2026-04-30)

EUPOS member network. Supports RTCM 2.3, RTCM 3.0, CMR, CMR+, CMRx, DGPS.
Example mountpoint: VRS_CMRx. Users can monitor live sessions at
geoportal.lt/app/litpos. Cross-border data sharing with LatPos (Latvia) and
ASG-EUPOS (Poland) is documented in the usage rules. Natural and legal persons
are eligible (§6 of usage rules); no professional surveying licence required.
No residency restriction found in the usage rules; non-Lithuanian registration
not confirmed but also not excluded.

---

## zakpos — ZAKPOS (UA)

**status**:    paid
**date_added**: 2026-04-30
**host:port**: `195.16.76.194:2102` (primary RTK, RTCM 3.1/3.2; per-second billing);
               also `:2131` (multi-constellation GPS+GLO+GAL+BDS), `:2100` (agri/drone),
               `:2999` (RTCM 3.1, Baltic 1977 vertical), `:3000` (RTCM 3.4, GPS+GLO+GAL+BDS+QZSS),
               `:3130` (individual bases, Baltic 1977), `:3131` (RTCM 3.4, EVRS);
               site: zakpos.zakgeo.com.ua; account: www.ua-pos.net or 195.16.76.195
**type**:      physical-coord-vrs (VRS zone mountpoints: VRSx_WEST/CENTR/EAST/SOUTH;
               SK63 zones 1–6; MSK_05; USK2000_4; UTM_35; MUKA_32 city base)
**access**:    paid subscription; account registration at www.ua-pos.net
**registration**: https://www.ua-pos.net
**yearly_cost**: 15,000 UAH/yr (~$366/yr) (wartime reduced tariff, April 2025);
               also: 2.43 UAH/min RTK, 1.08 UAH/min post-processing, 225 UAH/day,
               675 UAH/week, 1,600 UAH/month, 4,300 UAH/3 months, 8,000 UAH/6 months;
               pre-April 2025 rate was ~€400/yr / 0.06 €/min
**stations**:  unknown (mountpoints are VRS zone / coordinate-based; physical station count not confirmed)
**operator**:  ДП "Закарпатгеодезцентр" (State Enterprise "Zakarpathia Geodesy Centre")
**source**:    zakpos.zakgeo.com.ua (confirmed live, copyright © 2026)

Nationwide commercial GNSS positioning service, launched 2009 by ДП "Закарпатгеодезцентр".
Hub caster at Mukachevo (Zakarpattia Oblast). Part of UA-EUPOS. Accessed by bare IP only;
no DNS hostname.

Operational status (April 2025): active with wartime caveats. Service suspended 25 Feb 2022
under martial law; tariffs reduced and service resumed April 2025. Network pauses
automatically during active air-raid alerts. Mukachevo hub (far west) has been far less
affected by direct attacks than eastern regions.

Two EUREF-IP stations tied to Mukachevo stream via euref-ip.net:2101: MUK200UKR0 (Mukachevo,
NULP) and SULP00UKR0 (Lviv, IGS) — free reference, not NTRIP corrections.

**missing**: physical station count.

---

## ua_system_net — UA-System.NET (UA)

**status**:    paid
**date_added**: 2026-04-30
**host:port**: `gnss.org.ua:2101` (general, no coordinate system); also `:2100` (individual bases),
               `:2111–:2115` (SK63 zones 1–5 auto), `:2102/:2113` (SK63 zone 3),
               `:2222` (drone/UAV); MSK local-system zone ports (20001–20005+) via rtk.gnss.org.ua
**type**:      physical-coord-vrs (VRS; mountpoints: nearest, automax, vrs, i-max)
**access**:    paid subscription; Leica Spider Business Center login at gnss.org.ua
**registration**: https://gnss.org.ua
**yearly_cost**: 21,120–23,670 UAH/yr (~$515–577/yr) full national;
               regional packs (West/Karpaty/South/East): 13,000–13,500 UAH/yr (~$317–329/yr);
               also: 6.6 UAH/min (TIMER pack), 1,470 UAH/week, 3,630 UAH/month,
               8,190 UAH/3 months, 12,600 UAH/6 months; drone RTK: 15,510 UAH/yr (~$378/yr)
**stations**:  200+
**operator**:  Системи Солюшнс (Swiss-Ukrainian joint venture); brand: UA-System.NET
**source**:    systemnet.com.ua, gnss.org.ua (confirmed active, April 2025)

Largest commercial CORS network in Ukraine. Nationwide coverage with 200+ stations on Leica
Spider VRS platform. Wartime discount packages available for eastern and southern oblasts.
Drone/UAV mode via port 2222; MSK local coordinate system ports via rtk.gnss.org.ua.
Website and portal confirmed active as of April 2025.

---

## rtkhub — RTK HUB (UA)

**status**:    paid
**date_added**: 2026-04-30
**host:port**: not publicly listed; disclosed to registered users only
**type**:      physical-coord-vrs (services: Network RTK, nearest, single-base, DGPS, RINEX download)
**access**:    paid subscription; registration at rtkhub.com
**registration**: https://rtkhub.com
**yearly_cost**: 10,500 UAH/yr (~$256/yr) (from 01 Jan 2025; reduced from 15,000 UAH/yr);
               also: 2.50 UAH/min, 210 UAH/day, 600 UAH/week, 1,800 UAH/month,
               4,650 UAH/3 months, 6,300 UAH/6 months
**stations**:  unknown
**operator**:  TNT-TPI (formerly TNT-TPI GNSS Network); offices in Kyiv and Dnipro
**source**:    rtkhub.com, net.tnt-tpi.com (monitoring portal)

Nationwide commercial RTK network, rebranded from TNT-TPI GNSS Network to RTK HUB. Monitoring
portal at net.tnt-tpi.com. Host:port withheld — disclosed after registration. Most affordable
of the three major Ukrainian commercial networks.

**missing**: confirm host:port for documentation.

---

## ngcnet — NGCNET (UA)

**status**:    rejected
**date_added**: 2026-04-30

Listed in FIG pub74 global CORS directory as a Ukrainian network (ngcnet.com.ua). Domain has
no DNS record as of April 2026; likely defunct or absorbed into another network. No viable
endpoint.

---

## tpos — TPOS (IT — Trentino)

**status**:    free
**date_added**: 2026-04-30
**host:port**: `tpos.provincia.tn.it:2101` (SBC portal domain; mountpoints provided after login)
**type**:      physical-coord-vrs (VRS, MAX, NRT mountpoints)
**access**:    registration; free; self-service Leica Spider Business Center portal; no professional licence required
**registration**: https://www.tpos.provincia.tn.it
**stations**:  11
**operator**:  Servizio Catasto, Provincia Autonoma di Trento
**source**:    tpos.provincia.tn.it (PAT — Provincia Autonoma di Trento)

Trentino Positioning Service. 11 physical reference stations. Self-service SBC registration;
no professional licence required. RTK corrections, VRS/MAX/NRT mountpoints, and RINEX
archive (up to 1 year). Host:port confirmed via provincial institutional pages 2026-04-30.

---

## stpos — STPOS (IT — South Tyrol / Alto Adige)

**status**:    free
**date_added**: 2026-04-30
**host:port**: `www.stpos.it:2101` (SBC portal domain; mountpoints provided after documentation review)
**type**:      physical-coord-vrs
**access**:    registration; free; Leica Spider Business Center portal; requires ID scan + declaration
               of intended use to activate RTK access; RINEX available immediately after registration;
               no professional licence restriction
**registration**: https://www.stpos.it
**stations**:  10
**operator**:  Ufficio Catasto / Amt für Kataster, Provincia Autonoma di Bolzano / Autonome Provinz Bozen
**source**:    stpos.it (PAB — Provincia Autonoma di Bolzano)

South Tyrol Positioning Service. 10 physical reference stations. Bilingual (German/Italian).
Additional documentation step (ID + intended-use declaration) is light — no professional
credential required; RINEX archive available without it. Host:port confirmed via official
Bolzano cadastral pages 2026-04-30.

---

## gnss_veneto — Rete GNSS Veneto (IT — Veneto)

**status**:    free
**date_added**: 2026-04-30
**host:port**: `147.162.229.53:2101` (confirmed in site FAQ, question 4)
**type**:      physical-coord-vrs (MAX3, IMAX, NRT mountpoints)
**access**:    registration; free; email retegpsveneto@gmail.com with name, address, intended use;
               credentials assigned manually; open to any user ("liberamente accessibile previa registrazione")
**registration**: https://retegnssveneto.cisas.unipd.it
**stations**:  ~20
**operator**:  CISAS (Centro Interdipartimentale di Studi e Attività Spaziali), Università di Padova,
               on behalf of Regione del Veneto
**source**:    retegnssveneto.cisas.unipd.it (CISAS — Università degli Studi di Padova)

Veneto regional GNSS network. Site FAQ explicitly states observations are freely accessible
after registration. Mountpoints: MAX3 (RTCM 3.0 network solution), IMAX (RTCM 2.3 network
solution), NRT (nearest single-base). Credentials assigned by email; no automated portal.
Host:port confirmed from site FAQ 2026-04-30.

---

## gnss_liguria — Rete GNSS Liguria (IT — Liguria)

**status**:    free
**date_added**: 2026-04-30
**host:port**: `81.23.86.70:2101` (confirmed on Geoportal "Correzioni in Tempo Reale" page)
**type**:      physical-coord-vrs
**access**:    registration; free; online form via Liguria Geoportal; open to all users
               ("tutti gli utenti interessati al rilievo"); no professional credential required
**registration**: https://geoportal.regione.liguria.it/servizi/rete-gnss-liguria
**stations**:  10 (7 regional + 3 shared with SPIN3 GNSS)
**operator**:  Regione Liguria, Settore Informatica
**source**:    geoportal.regione.liguria.it (Regione Liguria)

Liguria regional GNSS network. Software upgraded 2021. 7 Liguria-owned stations plus 3
contributed from SPIN3 GNSS (Piemonte/Lombardia border). Host:port confirmed on Geoportal
"Correzioni in Tempo Reale" page 2026-04-30.

---

## sicilianet — Sicili@net (IT — Sicily + S. Calabria)

**status**:    free
**date_added**: 2026-04-30
**host:port**: `193.206.223.39:2101`
**type**:      physical-coord-vrs (MAX/IMAX, VRS, FKP, RTCM 3.0; single-base and network solutions)
**access**:    registration; free; email to request credentials via ct.ingv.it; explicitly open
               to all interested users ("in modo totalmente gratuito e a tutti gli utenti interessati")
**registration**: https://www.ct.ingv.it/index.php/risorse-e-servizi/sicil-net
**stations**:  ~80
**operator**:  INGV Osservatorio Etneo, Sezione di Catania (ct.ingv.it)
**source**:    ct.ingv.it (INGV — Istituto Nazionale di Geofisica e Vulcanologia, Catania)

Seismic monitoring network covering Sicily and southern Calabria. INGV Catania page
explicitly states corrections provided "in modo totalmente gratuito e a tutti gli utenti
interessati." Mountpoints: MAX/IMAX (Leica), VRS (Trimble), FKP (Geo++), RTCM 3.0.
Host:port confirmed on INGV Catania service page 2026-04-30.

---

## molise_gnss — Rete GNSS Molise (IT — Molise)

**status**:    rejected
**date_added**: 2026-04-30

Regione Molise does not operate a regional GNSS/NTRIP network. No NTRIP caster, no RTK
service, no permanent GNSS correction infrastructure found. Confirmed 2026-04-30
(site:regione.molise.it returns no results for GNSS/RTK/NTRIP; independent sources
explicitly state "Il Molise non ha una rete GNSS pubblica"). Users in Molise rely on
the adjacent Abruzzo+Lazio network (`gnss-rtk.regione.abruzzo.it:2101`) or national
commercial services.

---

## sarnet — SARNET (IT — Sardinia)

**status**:    paid
**date_added**: 2026-04-30
**country**:   IT — Sardinia
**host:port**: not confirmed (previously cited www.sarnet.it:2101 / 94.32.107.44:2101 are likely wrong)
**type**:      physical-coord-vrs (VRS, single-base, DGPS, RINEX archive)
**access**:    paid subscription; register via geodesia.biz/iscrizione-sarnet; no professional licence restriction stated
**registration**: https://www.geodesia.biz/iscrizione-sarnet
**yearly_cost**: €250/yr ex-IVA (~$293/yr); IVA 22% applies (→ ~€305/yr gross, ~$357/yr);
               confirmed via multiple current public procurement documents referencing SARNET subscriptions
**stations**:  ~14
**operator**:  SARNET s.r.l. (private consortium, geodesia.biz)
**source**:    geodesia.biz (SARNET s.r.l.)

Sardinia regional GNSS network. ~14 permanent stations covering Sardinia. Services: RTK
single-base, SARNET VRS (RTCM 3.0), DGPS, RINEX archive. No professional licence restriction
stated; hobbyists not explicitly excluded. Zero rtk2go or Centipede stations on the island —
SARNET is the only documented correction source for Sardinia.

**missing**: confirmed NTRIP caster host:port — contact via geodesia.biz/iscrizione-sarnet.

---

## acorn — ACORN (US-AK)

**status**:    free
**host:port**: `www.acorn-gnss.net:2101`
**type**:      physical-coord-vrs
**access**:    free; self-service registration at acorn-gnss.net (no professional licence field)
**pipeline-access**: registration
**stations**:  39 physical reference stations
**source**:    acorn-gnss.net (Alaska DNR — Division of Mining, Land & Water, Survey Section)
**operator**:  Alaska DNR, in partnership with DOTPF, NPS, and EarthScope

Trimble Pivot Web. Caster serves both VRS network-RTK and a nearest-station single-base
stream. Mountpoints (per 2025 DGGS workshop): MS_RTCM3 (connects to nearest station),
VRS_SouthCentral_RTCM3, VRS_Interior_RTCM3, VRS_SouthEast_RTCM3; NorthWest and
NortonSound (experimental) regions also documented. Anonymous sourcetable exposes only
VRS and MS_RTCM3 mountpoints; individual station streams visible after login. Raw
single-base streams from named physical stations also accessible via the NPS caster at
`rtk.nps.gov:2101`. Registration is self-service; the "Organisation" field on the login
page is present but its requirement is not clarified in public documentation. Endpoint
confirmed 2026-05-02.

---

## nps_cors — NPS CORS (US + territories)

**status**:    free
**host:port**: `rtk.nps.gov:2101`
**type**:      single-base
**access**:    conditions — credentials provisioned by emailing gnss_posnav@nps.gov; restriction scope unclear
**pipeline-access**: conditions
**stations**:  142 listed; ~128 active as of 2026-05-02 (DESO, GAA2, GAA3, HALE, HAVO, PAAL, SAJU offline)
**source**:    ntrip.nps.gov (portal) / rtk.nps.gov (NTRIP caster), National Park Service
**operator**:  National Park Service (NPS)

RTCM MSM4, 1-second streams. 142 stations spanning CONUS, Alaska, Pacific (Hawaii,
American Samoa), Marianas; includes ACORN physical stations in Alaska. Portal at
ntrip.nps.gov; NTRIP caster endpoint is rtk.nps.gov:2101. Datum: NAD 1983 (2011)
2010.0, transitioning to MYCS3 (positions updated February 2026). Accounts provisioned
manually by NPS staff via gnss_posnav@nps.gov; no public eligibility policy — described
internally as supporting NPS mapping and survey projects, but access has been extended to
ACORN partners and external contractors. Not in pipeline (credentials required;
sourcetable not publicly accessible). Confirmed alive 2026-05-02.

---

## remos_ven — REMOS (VE)

**status**:    free
**host:port**: not publicly confirmed
**type**:      unknown
**access**:    intended free (IGVSB government service)
**stations**:  ~8 listed on current IGVSB website (`igvsb.gob.ve/servicio/15`,
               2026-04-30); 27 NTRIP-capable out of 29 permanent as of 2012
               SIRGAS bulletins
**source**:    igvsb.gob.ve (IGVSB — Instituto Geográfico de Venezuela Simón Bolívar);
               SIRGAS Bol15/16/17 (~2010–2012, NTRIP setup documentation)

Maracaibo (MARA) was the first REMOS station to stream NTRIP corrections experimentally
(Oct 2008); plans to bring remaining stations online were unclear post-2018. No public
host:port or registration portal confirmed. SIRGAS bulletins (Bol15–Bol17) documented
installation of NTRIP server capability at 27 of 29 stations by ~2012 and referenced a
primary caster in a Venezuelan government datacenter plus a planned mirror, but neither
hostname was ever published. The BKG/RTCM-NTRIP global broadcaster registry (last updated
2024-01-30) contains no Venezuela/IGVSB entry. The igvsb.gob.ve website was reachable on
2026-04-30 and the REMOS service page (`/servicio/15`) confirmed 8 current stations at
Puerto Ayacucho, Barinas, Caracas, Coro, Barquisimeto, Maturín, and Maracaibo; no
NTRIP caster link or registration portal appeared anywhere on the site. Working hypothesis:
the caster was set up for internal/institutional use and was never made publicly accessible,
and continuity may have been affected by Venezuela's infrastructure situation post-2018.

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
**yearly_cost**: €160/quarter (~$170) or €480/yr (~$520), unlimited flat rate; per-minute
               plan also available (€90 one-time registration + undisclosed per-minute
               charge) — all prices ex-VAT; quarterly flat rate is under the $200 cutoff
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

## skpos — SKPOS (SK)

**status**:    paid-affordable
**date_added**: 2026-04-29
**country**:   SK
**type**:      VRS (network solution)
**host:port**: `skpos.gku.sk:2101` (legacy IP active until 2026-06-30 per
               2026-04-23 news on skpos.gku.sk)
**access**:    Free for public-sector bodies and municipalities under Act 145/1995;
               all other users (commercial, hobbyist) paid via the SKPOS online
               shop. Registration form (`skpos.gku.sk/register/`) explicitly
               offers **"Fyzická osoba bez živnostenského listu"** (natural person
               without trade/business licence) as an account type — open to
               private individuals with no professional registration. Country
               list covers virtually every UN member state; no Slovak residency
               restriction stated.
**registration**: `skpos.gku.sk/register/`
**yearly_cost**: 2026 schedule (EUR; VAT status not labelled on the public pages
               — GKÚ Bratislava is a state institution, so charges are
               historically treated as fees net of VAT for B2B invoicing, but
               the page does not state this explicitly), confirmed 2026-04-30
               on `skpos.gku.sk/en/o-skpos.php`:
                 SKPOS_cm/RTK (1 device, 1 yr): **€70 (~$79)**, includes 50 h RINEX
                 SKPOS_cm/RTK (1 device, 1 mo): €25 (~$28)
                 SKPOS_cm/RTK dual receiver (2× SIM, 1 yr): €140 (~$158)
                 SKPOS_dm/DGNSS (1 device, 1 yr): €25 (~$28), incl. 50 h RINEX
                 SKPOS_mm post-processing per hour: €3.00 base + €0.07/hr
                 SKPOS_mm post-processing 1000 h/yr bulk: €70 (~$79)
               Prices reflect a Dec 2022 revision (operating-cost adjustment);
               the obsolete pre-2022 cenník PDF (č.j. 2-124/2014) no longer
               applies. **At €70/yr SKPOS is one of the cheapest national-scale
               network-RTK services in the EU and the cheapest hobbyist on-ramp
               in the Visegrád region.**
**stations**:  ~26 SK permanent reference stations; VRS only (SKPOS_cm service)
**notes**:     Three service tiers: SKPOS_dm (decimetre, code), SKPOS_cm
               (centimetre, RTK/VRS), SKPOS_mm (post-processing). rtk2go ~2 SVK
               bases, Centipede ~2 SVK nodes as volunteer alternative.
**source**:    skpos.gku.sk/en/o-skpos.php; skpos.gku.sk/register/

---

## tencent_rtk — Tencent RTK (CN)

**status**:    paid
**host:port**: `cors.tencent.com` (ports 8001–8005, CGCS2000 on 8003; unconfirmed from
               current public sources — endpoint provisioned post-account, not in a
               public sourcetable)
**type**:      single-coord-vrs
**access**:    paid; enterprise B2B inquiry model as of 2026-04-30 — lbs.qq.com/rtk directs
               to "商务" (business inquiry) with no self-service purchase flow; Tencent
               account (WeChat/QQ, Chinese phone number typical) required; commercial use
               effectively requires a Chinese business licence
**yearly_cost**: ¥998/yr at 2022 free-beta launch (~$138/yr); current pricing not publicly
                 listed — enterprise inquiry only; ¥998 figure is community-reported, not
                 confirmed from a primary source price page
**stations**:  2,800+ virtual network stations; 33 provinces; 100% major urban road coverage
**source**:    lbs.qq.com/rtk (Tencent Location Service); dfcfw.com industry report,
               Sep 2022 (free-beta launch); xueqiu.com investor thread, 2025
**operator**:  Tencent Location Service (lbs.qq.com)

Launched 22 August 2022 as free public beta (免费公测) covering all 33 mainland provinces;
2 cm horizontal / 5 cm vertical accuracy; 5-constellation/16-frequency NTRIP. Access model
as of 2026-04-30 is enterprise B2B: the lbs.qq.com/rtk product page shows only a business
inquiry contact ("商务"), with no self-service pricing or purchase flow. A dedicated
RTK authentication SDK (RTK鉴权SDK) at lbs.qq.com/mobile/rtkLog suggests access is
provisioned per-account via app-developer integration rather than direct NTRIP subscription.
Individual developer accounts exist within the Tencent ecosystem but have not been confirmed
to grant RTK access specifically. The ¥998/yr figure (originally ~$138/yr) circulated in
community discussion at the 2022 beta launch; no primary source price page has been confirmed.
Service confirmed live as of 2026-04-30 via Google SERP index. Non-Chinese hobbyists have
no confirmed path; Chinese business licence likely required for commercial use.

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

**Free alternative for Nicosia area**: the IGS NICO station (Nicosia, Higher
Technical Institute) is broadcast by Geoscience Australia's AUSCORS caster
(`ntrip.data.gnss.ga.gov.au:2101`) as `NICO00CYP0`, RTCM 3.2 GPS+GLO
dual-freq, ITRF2020 current epoch. Free, no registration — see `auscors`.
Single base, useful L1+L2 baseline ~30 km, so practical coverage is greater
Nicosia and central Cyprus only. CYPOS remains the only path to island-wide
network RTK.

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

**status**:    weird
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

No free hobbyist path exists via OS Net, and no published OS Net tier sits
under the project's ~$200/yr affordability cutoff. Topcon TopNet Live's 7-day
Unlimited at £100 ex VAT is the shortest available paid block but annualises
to ~£5,200/yr if used weekly — a one-off pass, not an affordable subscription.
Volunteer bases on rtk2go/Centipede remain the only free option.

---

## osi_gnss — OSi Active GNSS Network (IE)

**status**:    weird
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

## soi_cors — SoI CORS (IN)

**status**:    paid
**date_added**: 2026-05-04
**country**:   IN — India
**host:port**: `103.205.244.106:2101` (Region 1 — UP, Uttarakhand, Haryana, Punjab,
               HP, NCR, MP, Rajasthan); `103.206.29.4:2105` (Region 2 — Maharashtra,
               Karnataka, southwards). Authoritative portal: `cors.surveyofindia.gov.in`.
**type**:      physical-coord-vrs
**access**:    free for Central/State Government and government academic/research; paid
               for PSU and private users. Online registration with Aadhaar or PAN ID
               required — no documented path for foreign nationals (Aadhaar/PAN are
               domestic IDs). Promotional free private-individual window
               1 Nov 2025–31 Jan 2026 expired.
**yearly_cost**: ₹70,800/yr (RTK12, incl. 18% GST, ~$745/yr); RTK1 ₹5,900/mo (~$62);
                 RTK3 ₹17,700 (~$186); RTK6 ₹35,400 (~$373). DGNSS1 ₹2,360/mo (~$25);
                 online RINEX ₹150/GB + GST. All prices observed 2026-05-04 on
                 cors.surveyofindia.gov.in/subscription-charges; over $200/yr cutoff.
**registration**: `https://cors.surveyofindia.gov.in`
**stations**:  1,105+ across India; an additional 70 Andhra Pradesh stations are being
               integrated into SoI CORS following the 13 Oct 2025 MoU between SoI and
               the AP Survey, Settlements & Land Records Department.
**source**:    cors.surveyofindia.gov.in (Survey of India)
**operator**:  Survey of India (Department of Science & Technology)

Aadhaar/PAN gating means the network is effectively Indian-residents-only. Tamil Nadu's
separate 70-station departmental network has not been merged into SoI as of 2026-05-04
(see `tn_cors`); Kerala's MoU dates to 18 Jan 2021 but no public caster has been
commissioned. Worth revisiting if foreign-resident registration becomes possible or if
TN/KL follow AP into the national network.

---

## tn_cors — Tamil Nadu State CORS (IN — Tamil Nadu)

**status**:    restricted
**date_added**: 2026-05-04
**country**:   IN — Tamil Nadu
**host:port**: not publicly listed
**type**:      unknown
**access**:    closed government infrastructure; access limited to Tamil Nadu Department
               of Survey and Settlement field staff for cadastral resurvey. No public
               NTRIP service, registration portal, or tariff exists.
**stations**:  70 (rooftops of state government establishments)
**source**:    tnlandsurvey.tn.gov.in (Commissionerate of Survey and Settlement);
               surveyofindia.gov.in/documents/tenders/document-11484-tnp-tender.pdf
**operator**:  Tamil Nadu Department of Survey and Settlement

Operational since at least 2017 per state Policy Notes ("DGPS-RTK based survey ... of
millimeter accuracy" for departmental resurvey). Not absorbed into SoI CORS as of
2026-05-04 — unlike Andhra Pradesh, which signed an integration MoU with SoI on
13 Oct 2025 (see `soi_cors`). rtk2go ~2 Tamil Nadu volunteer bases are unaffiliated.

---

## tusaga — TUSAGA-Aktif / CORS-TR (TR)

**status**:    paid
**date_added**: 2026-04-29
**host:port**: `212.156.70.42:2101` (also reachable as `tusaga-aktif.gov.tr:2101`;
               legacy port 55600)
**access**:    paid; one-time per-device registration fee, then RTK subscription
               purchased per period. Tariff set annually by BHİKPK
               (Inter-Ministerial Commission for Mapping Affairs). Online
               registration requires a TC Kimlik No (Turkish national ID), so
               foreign nationals without Turkish residency cannot self-register —
               must contact the agency directly. Universities and vocational
               schools may apply for free educational-area access via official
               letter to TKGM Harita Dairesi Başkanlığı; public bodies and
               universities also receive a 75% discount on 1-sec RINEX.
**yearly_cost**: 2026 schedule (gross, KDV/VAT included), confirmed 2026-04-30 on
               tusaga-aktif.gov.tr homepage:
                 Cihaz Abonelik (per-device registration, one-time): ₺550 (~$17)
                 RTK 1 mo: ₺1,000 (~$30) · 2 mo ₺2,000 · 3 mo ₺3,000 · 4 mo ₺4,000
                 RTK 5 mo: ₺5,000 · 6 mo ₺6,000 (~$182) · 1 yr ₺8,135 (~$247)
                 DGPS 1 mo: ₺405 (~$12) · 1 yr ₺2,985 (~$91)
                 RINEX 30-sec: free · RINEX 1-sec: ₺4/session (~$0.12)
               Approx ~32.9 TRY/USD. The annual RTK tier (~$247) is just above
               the $200/yr hobbyist cutoff; the 6-month block at ~$182 is the
               cheapest period that fits inside the cutoff. Shorter monthly
               blocks exist (₺1,000/mo, ~$30) but annualise to ~$360, so they
               are one-off passes, not sustained subscriptions.
**stations**:  ~158 physical single-base GNSS stations (Turkey + Northern Cyprus);
               146 was earlier count, 12 border/Marmara stations added 2018
**source**:    tusaga-aktif.gov.tr; tkgm.gov.tr; harita.gov.tr

---

## vngeonet — VNGEONET (VN)

**status**:    paid
**host:port**: `vngeonet.vn:2101` (VRS) — IP `14.238.1.125`; `:2102` (iMAX); `:2103`
               (single-base)
**type**:      physical-coord-vrs (VRS + iMAX + single-base mountpoints)
**access**:    Paid since Sep 2024 per Circular 47/2024/TT-BTC; register at
               gddt.vngeonet.vn. "Organizations and individuals" (tổ chức và cá
               nhân) explicitly eligible per the instructions page; passport
               accepted alongside Vietnamese Citizen ID for individual registration,
               so **foreign nationals can register**. RTK account is case-sensitive.
**yearly_cost**: Confirmed 2026-04-30 on gddt.vngeonet.vn homepage service cards
               (VAT status not explicitly stated on the public page; Circular
               47/2024/TT-BTC of the Ministry of Finance is the authoritative
               legal source, building on Circular 03/2020/TT-BTNMT):
                 RTK 1 mo, nationwide, per rover: 750,000 VNĐ (~$29.5)
                 RTK 6 mo: 4,280,000 VNĐ (~$168)
                 RTK 12 mo: 6,750,000 VNĐ (~$266)
                 RTK 12 mo in zones with >80 km station spacing: **0 VNĐ (free)**
               Approx ~25,420 VND/USD. The free zone-based tier covers parts of
               the network where station density is sparse — useful free option
               for hobbyists outside the densely covered river deltas.
**stations**:  65
**source**:    vngeonet.vn; gddt.vngeonet.vn (National Centre for Satellite
               Positioning Station Management / Trung tâm Quản lý trạm định vị
               vệ tinh quốc gia, Bộ TN&MT)

Three-port caster: port 2101 VRS network solution, port 2102 iMAX network
solution, port 2103 single-base.

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
               Annual flat rate ~€375 / ~$415 at ~400 HUF/EUR — over the $200/yr cutoff.
               The per-minute RTK rate (~€1.20/hr) is the only tier that fits inside
               the cutoff, and only for occasional use up to roughly 150 hours/year;
               the 30-day local-radius pass (~€38) is a single-project block, not a
               sustained subscription. Outside the 50 km radius the local flat rate
               falls back to per-minute billing without separate notice.
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
**host:port**: `pagenet.namria.gov.ph` — port not on public-facing pages (issued
               post-subscription per the RTK Connection Guide); standard NTRIP
               port 2101 inferred. Contact: `pagenet@namria.gov.ph`,
               tel +63 2 8884-2849.
**access**:    Paid under Executive Order 471 (regulatory charges, no VAT applies).
               Open to individuals via online form; payment by LandBank deposit
               slip available outside Metro Manila. No surveying-licence
               requirement per FAQ. Nationality/residency not explicitly
               restricted, but the bank-deposit payment route is a practical
               barrier for foreign hobbyists — confirm with NAMRIA.
**yearly_cost**: Full schedule at pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx,
               confirmed 2026-04-30 (PHP, no VAT; ~56.5 PHP/USD):
                 One-time registration (per client, all services): PHP 1,000 (~$18)
                 Real-time RTK per hour, per rover: **PHP 100/hr (~$1.77/hr)**
                 RTK Unlimited 1 day (+PHP 500 per extra rover): PHP 1,000 (~$18)
                 RTK Unlimited 5 days: PHP 3,500 (~$62)
                 RTK Unlimited 15 days: PHP 7,500 (~$133)
                 RTK Unlimited 1 month: PHP 12,000 (~$212)
                 RINEX 1–20 sec: PHP 50/MB · RINEX 30–60 sec: free with subscription
                 Coordinate Computation: free
               The per-hour rate (~$1.77/hr) is the only tier that fits inside
               the ~$200/yr cutoff, and only for occasional use up to ~90
               hours/year. The 1-day pass (~$18) covers a single session;
               longer blocks rise quickly (1 month ~$212 is just over the
               cutoff). No annual flat rate is published.
**stations**:  52
**operator**:  NAMRIA — National Mapping and Resource Information Authority
**source**:    namria.gov.ph; pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx

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
**date_added**: 2026-04-30
**country**:   BG
**type**:      VRS (network RTK)
**host:port**: `gnss.geonet.bg:2101` (IP `95.43.249.1:2101`); confirmed on
               geonet.bg/help.html 2026-04-30
**access**:    paid contract with operator. No explicit hobbyist exclusion;
               no explicit hobbyist tier either. Open to private individuals.
**yearly_cost**: €600/yr (~$660/yr) for RTK12 annual unlimited plan (excl. VAT).
               Other unlimited plans: RTK1 €105/mo, RTK3 €250/3 mo, RTK6 €395/6 mo.
               GeoNet 150 (occasional-use): €15/mo base + €0.10/min GEO-RTK and
               €0.10/min PPData beyond 150 included minutes; 24-month minimum
               contract. Per-minute PPData standalone: €0.10/min. Multi-account
               discounts 5% (2 accounts), 7% (3 accounts); 4+ negotiated.
               All prices exclude Bulgarian VAT (ДДС).
               Source: Solitech AD tariff sheet dated 01.04.2026.
**stations**:  certified per Instruction РД-02-20-25/2011 by АГКК (Agency for
               Geodesy, Cartography and Cadastre); Certificate of Conformity
               No. 013/2020 renewed to 2026 (per 2024-07-01 news)
**source**:    geonet.bg; geonet.bg/help.html; geonet.bg/abonamenti.html
**operator**:  Зенит-Гео ЕООД (Zenit-Geo Ltd) — commercial private operator;
               distribution via Солитех АД (Solitech AD), official Trimble
               reseller for Bulgaria

GEO-RTK is GeoNet Bulgaria's commercial network RTK / VRS service. Provides
absolute position accuracy within ~2 cm. No free hobbyist tier. GCSES (the
state Geodesy, Cartography and Cadastre Agency) operates government reference
stations but provides no public NTRIP caster.

**investigate**: pull the April 2026 tariff PDF and record BGN/EUR per tier;
clarify whether private individuals (no business registration) can sign a
contract with Solitech.

---

## montepos — MONTEPOS (ME)

**status**:    paid
**date_added**: 2026-04-29
**country**:   ME
**type**:      VRS-capable (9 CORS locations)
**host:port**: not on the public-facing page; disclosed post-registration.
               Application form (`Zahtjev za MontePos`, 2024-04-11 PDF) and
               tariff PDF (`MontePos- tehnički detalji`, 2024-04-11) downloadable
               from `wapi.gov.me`; contact Goran Popović, dipl. inž. geod.,
               Načelnik odsjeka za geodetske radove i državnu granicu,
               tel +382 67 641 119.
**access**:    Paid subscription. Periods confirmed on gov.me/clanak/montepos:
               **24 h, 48 h, 1 month, 3 months, 6 months, 1 year, 2 years**.
               Application form submitted to Uprava za nekretnine; payment to
               giro account 832-1081-58 with "Montepos - RTK" in the
               purpose-of-payment field.
**yearly_cost**: EUR figures not on the public page; tariff PDF
               `MontePos- tehnički detalji` (382 KB, 2024-04-11) on `wapi.gov.me`;
               no professional licence requirement mentioned. Montenegro uses
               EUR as de facto currency.
**stations**:  9 permanent CORS stations
**source**:    gov.me/clanak/montepos (Uprava za nekretnine — Real Estate
               Administration)

Montenegro's national CORS/VRS network. Subscription required for all tiers;
no free access. Application materials are publicly downloadable on `wapi.gov.me`
but actual EUR figures need to be pulled from the tariff PDF.

**investigate**: retrieve the EUR tariff per period from the 2024-04-11 PDF on
wapi.gov.me; obtain the post-registration NTRIP host:port via
`uznmontepos@gmail.com` or +382 67 641 119.

---

## srpos_ba — SRPOS (BA — Republika Srpska)

**status**:    paid
**date_added**: 2026-04-30
**country**:   BA
**type**:      VRS + iMAX + MAX + FKP + nearest-station single base
**host:port**: `srpos.rgurs.org:2101` (web portal `http://srpos.rgurs.org/sbc`);
               legacy `81.93.74.247:8080` also documented in user-access guide
**access**:    Paid. Tariff schedule established by Decision in Sl. glasnik RS
               85/2011; current rates apply post-2013 (a 20% reduction was in
               force only until 1 Jan 2013). No professional surveying licence
               required — registration form imposes no licensing condition.
               Foreign nationals not explicitly excluded but the RS giro account
               payment route practically favours in-entity users.
**yearly_cost**: Confirmed 2026-04-30 from
               `rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf`
               (BAM, pegged 1.95583 to 1 EUR; ~$0.578/BAM. VAT treatment not
               explicitly stated on the document — government tariff schedule):
                 RTK: 0.20 KM/min · 10 h 30 KM (~€15, ~$17) · 20 h 50 KM (~$29) ·
                   50 h 150 KM (~$87) · 1 mo 250 KM (~€128, ~$145) ·
                   6 mo 750 KM (~$433) · 1 yr 1,000 KM (~€511, ~$578)
                 DGPS: 0.15 KM/min · 10 h 20 KM (~$12) · 1 mo 200 KM (~$116) ·
                   1 yr 1,000 KM (~$578)
                 Post-processing RTK <30 s/hr: 22 KM/hr; DGPS ≥30 s/hr: 13 KM/hr
                 RINEX RTK 28 KM/hr; DGPS 17 KM/hr; combined 33 KM/hr
                 Coordinate transformation (web, per point) 13 KM
               Short pre-paid blocks (10 h ~$17, 20 h ~$29) translate to roughly
               $1.45–1.70/hr — the only rate in the schedule that fits inside
               the ~$200/yr cutoff, and only for occasional use; per-minute
               (0.20 KM/min ≈ $7/hr), the 1-month tier (~$145), and the annual
               (~$578) are all above the cutoff.
**mountpoints**: MAX-AUTO (RTCM 3.1, GPS+GLO), iMAX-AUTO (3.1), VRS-AUTO (3.1),
               FKP-AUTO (RTCM 2.3 msg 18/19, GPS only), NEAREST (3.1, single
               base), iMAX-AUTO-2.3 (RTCM 2.3)
**stations**:  ~17 (RS portion of the 34-station BiHPOS network)
**source**:    rgurs.org/stranica/srpos; rgurs.org/en/stranica/srpos;
               rgurs.org/uploads/pages/SRPOS_Korisnicki_pristup.pdf;
               rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf
**operator**:  RGURS / RUGIPP — Republička uprava za geodetske i imovinsko-pravne
               poslove, Republika Srpska. Admin Spomenko Mitrović,
               tel +387 55 220-890 / +387 55 202-643. Launched 27 Sep 2011.

The Republika Srpska sub-network of the EU-funded BiHPOS project. Streams MAX,
iMAX, VRS, FKP, and a nearest-station single-base mountpoint. Sister network
FBiHPOS (Federation of BiH) is documented separately.

---

## fbihpos_ba — FBiHPOS (BA — Federation of BiH)

**status**:    paid
**date_added**: 2026-04-30
**country**:   BA
**type**:      VRS + iMAX + MAX + nearest-station single base; combined H+V
               correction stream
**host:port**: `fbihpos.katastar.ba:8080` — note port 8080, not the
               conventional NTRIP 2101. The third-party-cited `fbihpos.fgu.com.ba`
               appears to be an older or alternative hostname; the current
               authoritative access guide (FGU 2024) specifies the
               `katastar.ba` host.
**access**:    Paid. Registration form (FGU 2022) explicitly has a "FIZIČKA
               LICA" (natural persons) section with no surveying-company,
               professional-licence, or trade-registration requirement; fields
               are name, surname, address, city, email, phone, username.
               Foreign-applicant eligibility not explicitly stated — contact
               FBiHPOS directly to confirm.
**yearly_cost**: Tariff per FBiH Government Decision V. broj 605/2022
               (14.04.2022), confirmed 2026-04-30 (BAM, pegged 1.95583 to 1 EUR;
               ~$0.578/BAM; gross — these are statutory fees, no separate VAT
               line, paid to Jedinstveni račun trezora FBiH 1020500000106698,
               vrsta prihoda 722516):
                 4.1.1 One-time user registration: 100 KM (~$58)
                 4.2.1 RTK-VPSP 7 days:  150 KM (~$87)
                 4.2.2 RTK-VPSP 1 mo:    250 KM (~$145)
                 4.2.3 RTK-VPSP 2 mo:    350 KM (~$203)
                 4.2.4 RTK-VPSP 3 mo:    450 KM (~$261)
                 4.2.5 RTK-VPSP 4 mo:    550 KM (~$319)
                 4.2.6 RTK-VPSP 5 mo:    650 KM (~$377)
                 4.2.7 RTK-VPSP 6 mo:    750 KM (~$435)
                 4.2.8 RTK-VPSP 12 mo:  1,000 KM (~$580)
                 4.4.6 All FBiHPOS services 12 mo: 1,400 KM (~$812)
                 4.4.7 Post-processing only 12 mo: 700 KM (~$406)
               Multi-rover discounts: -10% on the 2nd rover, -20% on the 3rd,
               capped at -50%. The 1-month and 7-day blocks are short-period
               passes; all RTK tiers (including the 1-month at $145, 2-month at
               $203 and the annual at $580) annualise above the project's
               ~$200/yr cutoff for sustained use.
**mountpoints**: MAX-AUTO, iMAX-3G, VRS-AUTO, VRS-3G, NEAREST, FBiH_H+V
**stations**:  ~17 (FBiH portion of the 34-station BiHPOS network)
**source**:    fgu.com.ba/bs/servisi.html;
               fgu.com.ba/files/Novosti/2024/PDF/FBiHPOS - novo/Pristup FBiHPOS servisima.pdf;
               fgu.com.ba/files/Novosti/2022/PDF/tarife/b/TARIFA NAKNADA ZA VRSENJE USLUGA IZ OBLASTI PREMJERA I KATASTRA.pdf
**operator**:  FGU — Federalna uprava za geodetske i imovinsko-pravne poslove,
               Federacija BiH (`fgu.com.ba` — note `.com.ba`, not `.gov.ba`).
               Caster runs on a separate cadastre subdomain (`fbihpos.katastar.ba`).
               Contact `fbihpos@fgu.com.ba`, tel +387 33 586 065.

The FBiH sub-network of the BiHPOS project, sister to SRPOS. Six published RTK
mountpoints span MAX, iMAX, VRS network solutions plus a NEAREST single-base
and a combined-component FBiH_H+V stream. Tariff parallels the SRPOS schedule
in scale (1-month ~$145 vs SRPOS ~$145; annual ~$580 vs SRPOS ~$578) but with
a higher one-time registration (100 KM vs 0).

---

## kopos — KOPOS / Kosovo Positioning System (XK)

**status**:    paid
**date_added**: 2026-04-30
**country**:   XK
**type**:      VRS (8 CORS stations + computation centre in Pristina; Leica GNSS Spider)
**host:port**: `kopos.rks-gov.net:2101` (Spider Business Center login portal; NTRIP mountpoints and credentials provided inside portal post-login)
**access**:    paid; annual subscription + one-time registration fee; register at akk.rks-gov.net; no surveying-licence requirement found
**yearly_cost**: €400/yr (~$468); plus €20 one-time registration fee
**stations**:  8 permanent CORS; RTK horizontal ±2 cm, vertical ±4 cm
**operator**:  Agjencia Kadastrale e Kosovës (Kosovo Cadastral Agency / AKK)
**source**:    akk.rks-gov.net

Kosovo's national GNSS reference network, operated by the Kosovo Cadastral Agency (AKK)
as an EUPOS-aligned CORS network. AKK 04/24 tariff schedule confirmed via the 2025 Annual
Report (issued 2026-03-25); pricing unchanged since early 2024. Portal alive 2026-04-30.
The SBC registration form requests rover brand, serial number, and address; no surveying
licence number required. No free hobbyist tier.

---

## sstp_by — ССТП РБ / Belgeodesiya CORS (BY)

**status**:    restricted
**date_added**: 2026-04-30
**country**:   BY — Belarus
**type**:      network RTK (VRS; mountpoints: BelarusVRS, NEAR, BelarusVRS(MSM5), NEAR(MSM5) on port 8080; Precision Agriculture port 8081)
**host:port**: `sstp.geo.by:8080` (IP fallback: `93.125.21.51:8080`)
**access**:    paid; signed public contract (Публичный договор) with РУП «Белгеодезия»;
               available to individuals (физическое лицо) and organisations (юридическое лицо);
               restricted to residents of the Republic of Belarus (tariff "для резидентов РБ");
               no self-service portal
**yearly_cost**: 150.78 BYN/month (~$53/month; ~$641/yr annualised) — "Точная навигация" fixed plan;
               metered: 0.24 BYN/min RTK (~$0.085/min) under "Общий" plan; no annual RTK flat rate.
               Agriculture flat-rate (Точное земледелие): 6,000 BYN/yr (~$2,124/yr) per board device.
               Tariff effective 01.05.2023 (geo.by/images/tariffs.pdf); stated "без НДС" (excl. 20% VAT).
**stations**:  ~98 continuously operating reference stations (national coverage)
**operator**:  РУП «Белгеодезия» (Belgeodesiya state enterprise),
               under Государственный комитет по имуществу Республики Беларусь
               (State Committee for Property — Госкомимущество)
**registration**: https://geo.by/services/sstp

Belarus national CORS network (Спутниковая система точного позиционирования — ССТП РБ).
Provides RTK and DGPS differential corrections plus RINEX post-processing files
(RINEX 1-hr file: 3.63 BYN, ~$1.29). Since March 2020 Belgeodesiya feeds data to two
EPN analytical centres, but the RTK correction service is entirely separate and not
accessible outside Belarus.

Access is restricted to residents of the Republic of Belarus who sign a public contract;
both individuals and organisations may sign. No self-service portal; host:port and
credentials issued per-contract. Confirmed alive 2026-04-30 (tariff PDF and RTK manual
both served from geo.by).

Hardware supply: EU, UK, and US sanctions applied to Belarus since 2020–2022 suspend
exports of surveying and precision-GNSS equipment (Topcon, Trimble, Leica all announced
suspension). Replacement rover hardware is materially harder to source than in
unsanctioned neighbouring states, compounding the barriers to hobbyist RTK use.

---

## scrtn — SCRTN (US-SC)

**status**:    paid
**date_added**: 2026-04-30
**type**:      VRS (Trimble Pivot NW platform)
**host:port**: `scrtn.sc.gov:2101`
**access**:    paid; subscribe at scrtn.sc.gov; no professional-licence requirement; any subscriber may obtain a login
**yearly_cost**: $600/yr per login (annual renewal same rate)
**operator**:  SC Revenue and Fiscal Affairs Office / SC Department of Transportation
**source**:    scrtn.sc.gov

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
**registration**: https://hlcmgroup.com/contact/ (hlcmgroup.com/vrs-faqs/ returned 404 as of 2026-04-30)
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
**date_added**: 2026-04-30
**type**:      VRS (Trimble-based)
**host:port**: not publicly listed (GeoBC website reorganisation; portal URLs returning 404 as of 2026-04-30)
**access**:    paid; contact GeoBC (gov.bc.ca/geobc or 1-800-663-7867); no self-service portal currently accessible
**yearly_cost**: CAD 1,650/yr (~$1,212); statutory fee per Land Act, B.C. Reg. 55/98, confirmed to 2026-04-21
**operator**:  GeoBC / Province of British Columbia
**source**:    gov.bc.ca/geobc (Province of British Columbia)

British Columbia real-time network. No free tier. No Canadian province offers free
public NTRIP — confirmed across all ten provinces and three territories. The statutory
fee of CAD 1,650/yr is confirmed in the Land Act Subscription Fee Regulation (B.C. Reg.
55/98); BC PST (7%) may apply. NTRIP portal URL not currently accessible from public
sources following a gov.bc.ca website reorganisation.

---

## nsacs — Nova Scotia NSACS (CA-NS)

**status**:    paid
**date_added**: 2026-04-30
**access**:    RINEX post-processing free via NRCan; real-time NRTK via paid commercial
               resellers only: HxGN SmartNet NA (`smartnetna.com`, CAD $3,327.96/yr Atlantic;
               CAD $6,084/yr national), Can-Net (`gps.can-net.ca`, pricing not public),
               Brandtnet (`rtk.brandt.ca`, pricing behind account login)
**yearly_cost**: CAD 3,328/yr (~$2,429/yr) — HxGN SmartNet Atlantic (NB, NL, NS, PE) plan;
               Can-Net and Brandtnet pricing not publicly listed; national SmartNet: CAD 6,084/yr (~$4,441/yr).
               GST/HST status not stated on SmartNet product page — treat as unknown; confirm at checkout.
**stations**:  40
**source**:    novascotia.ca (Nova Scotia Spatial Services)

Nova Scotia Active Control System — 40 permanently installed government GNSS receivers
forming the NSCRS (Nova Scotia Coordinate Referencing System). Province owns the
stations; three commercial providers access the ACS data under data-licensing agreements
and sell real-time NRTK subscriptions. No free real-time tier; no direct provincial
NTRIP caster. SmartNet pricing confirmed 2026-04-30 at smartnetna.com/store_product_selector.cfm.

---

## dvrs — DVRS (AE)

**status**:    restricted
**date_added**: 2026-04-30
**access**:    restricted; professional application only (licensed engineering/surveying firms);
               no individual or hobbyist registration path at any price
**yearly_cost**: not publicly listed (professional application required)
**stations**:  18+
**source**:    dm.gov.ae (Dubai Municipality)

Dubai Virtual Reference System. 18+ 4-constellation reference stations covering Dubai
Emirate. Access by formal professional application only — no hobbyist path.

Portal status (2026-04-30): geodubai.dm.gov.ae returning errors; dm.gov.ae/survey-department
DVRS sub-pages returning 404. Service may have been restructured or migrated to a DM
e-services login. Main dm.gov.ae site is live.

---

## regpmoc — REGPMOC (PE)

**status**:    paid
**date_added**: 2026-04-30
**host:port**: `190.12.71.75:2101`
**type**:      single-base
**access**:    paid; application + payment to IGN required; credentials issued by email;
               no self-service portal; not explicitly restricted to licensed surveyors per
               IGN's "Políticas de Uso del Servicio NTRIP" policy document
**yearly_cost**: no official PEN tariff found (TUPA pages at gob.pe returning 404);
               reseller indication: ~$85/month (~$1,020/yr) at one Peruvian integrator —
               not an official IGN rate
**stations**:  ~65 single-base
**operator**:  IGN — Instituto Geográfico Nacional del Perú (under Ministry of Defence)
**source**:    ign.gob.pe (IGN — Instituto Geográfico Nacional)

Red Geodésica Permanente de Monitoreo Continuo. ~65 single-base stations nationally.
RTCM 3.2 and CMR+ formats; NTRIP v2.0; max 100 simultaneous users/station. Access is
by application to IGN + payment; credentials issued by email. IGN policy document does
not explicitly restrict to licensed surveying organisations. Official fee schedule (TUPA)
currently returning 404 on gob.pe.

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

**status**:    rejected
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

Rejected — military-operated geodetic directorate; no public NTRIP service.

---

## ges_syria — General Establishment for Survey (SY)

**status**:    rejected
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

Rejected — military-operated; no public NTRIP service; conflict-disrupted infrastructure.

---

## otc_gnss — OTC GNSS (TN)

**status**:    paid
**date_added**: 2026-04-30
**country**:   TN
**type**:      single-base (physical coordinates)
**host:port**: not publicly listed (disclosed after subscription)
**access**:    paid subscription; register at otc.nat.tn/geodesy/gnss/subscription; no explicit eligibility restriction found
**yearly_cost**: 6,000 TND/yr (~$2,070/yr); prices H.T. (excl. VAT); confirmed 2026-04-30
**stations**:  23 (physical; Saharan region not covered)
**source**:    otc.nat.tn (OTC — Office de la Topographie et de la Cartographie)
**operator**:  OTC (Ministère de l'Équipement et de l'Habitat, Tunisia)

Full published tier table — all H.T., excl. VAT (source: otc.nat.tn/geodesy/gnss/subscription;
at 1 TND ≈ $0.345, observed 2026-04-30):
60 TND/day (~$21), 480 TND/15 days (~$166), 840 TND/month (~$290), 2,400 TND/3 months
(~$828), 3,600 TND/6 months (~$1,242), 4,800 TND/9 months (~$1,656), 6,000 TND/yr (~$2,070).

Office de la Topographie et de la Cartographie national GNSS network. 3 stations
installed 2005 (Tunis, Monastir, Sfax); expanded to 23 with 20 additional stations
distributed across non-Saharan Tunisia in 2010; fully operational since 2011. Each
station is equipped with a weather sensor (temperature, pressure, humidity). Network
referenced to WGS84–ITRF 2000 (NTT — Nouveau Système Tunisien de Triangulation).
RTK corrections delivered via NTRIP subscription; NTRIP host:port disclosed post-subscription.
No free tier. No explicit eligibility restriction on subscription page.

---

## rjgc_cors — RJGC CORS (JO)

**status**:    restricted
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

Restricted — no public self-service registration; real-time RTK access limited to licensed users.

---

## pak_rehber — Pak-Rehber (PK)

**status**:    restricted
**date_added**: 2026-04-30
**type**:      VRS (network RTK; RTCM 3.x MSM4/MSM7; ~4–5 ms latency)
**coverage**:  Karachi metropolitan area only (city + ~20 km outskirts); not nationwide Pakistan
**access**:    restricted; "only authorised users can use" (per official brochure);
               authorisation process not publicly documented
**yearly_cost**: not publicly listed
**stations**:  unknown (Karachi metro only)
**operator**:  SUPARCO Business Solutions (Pvt.) Ltd. (commercial arm of SUPARCO — Space
               and Upper Atmosphere Research Commission)
**source**:    suparco.biz (SUPARCO Business Solutions)

NRTK service operated by SUPARCO Business Solutions using Topcon GNSS software. Covers
Karachi metropolitan area and ~20 km outskirts only. The official brochure
(suparco.biz/wp-content/uploads/2025/03/pak-rehber.pdf, confirmed live 2026-04-30)
explicitly states "Only authorized users can use the Pak-Rehber precise positioning
service." No public host:port, sourcetable, or hobbyist registration path found.
Pak-SBAS (sub-metre L-band satellite corrections) is a separate SUPARCO service,
out of scope.

---

## slcorsnet — SLCORSnet (LK)

**status**:    paid
**country**:   LK — Sri Lanka
**type**:      physical-coord-vrs (VRS / FKP / MAC)
**host:port**: `222.165.190.67:2101`
**access**:    paid subscription — 1-day (2,000 LKR), 7-day (10,000 LKR), 30-day
               (30,000 LKR), and annual (360,000 LKR) tiers; prices stated as
               "including all taxes". Registration open to individuals; no
               surveying-company licence requirement stated publicly. Payment by
               bank transfer to Peoples Bank (Narahenpita).
**yearly_cost**: 360,000 LKR/yr (~$1,127/yr)
**registration**: https://slcorsnet.survey.gov.lk
**stations**:  unknown (Phase 1: Western Province and surroundings; island-wide rollout ongoing)

**date_added**: 2026-04-30

Sri Lanka Continuously Operating Reference Station Network, operated by the Survey
Department of Sri Lanka (Surveyor General's Office, Colombo). Established end of 2016.
Physical GNSS reference stations transmit raw data to a Control Centre for network
processing; real-time RTCM corrections delivered via VRS, FKP, or MAC. Post-processing
RINEX and autonomous GNSS post-processing (SSRPOST / GNWEB) also available. Payment
by bank transfer to Peoples Bank (Narahenpita); bank-transfer-only payment may
complicate non-resident registration in practice. Host:port `222.165.190.67:2101`
confirmed live 2026-04-30 from public "How to Use" page. Pricing confirmed publicly
at slcorsnet.survey.gov.lk/how-to-use/pricing/ (no login required) on 2026-04-30 audit.
Not added to pipeline — paid service at ~$1,127/yr.

---

## corsnet_lk — CORSnet (LK)

**status**:    paid
**country**:   LK — Sri Lanka
**type**:      physical-coord-vrs (VRS)
**host:port**: not publicly listed (provided to subscribers post-registration)
**access**:    paid commercial subscription; self-service registration open to
               individuals (register → confirm email → request connection → pay →
               activate); pricing confirmed publicly at corsnet.lk/services
**yearly_cost**: 345,000 LKR/yr (~$1,080/yr)
**registration**: https://corsnet.lk/user/register/
**stations**:  ~15+ (island-wide coverage claimed)

**date_added**: 2026-04-30

Sri Lanka's first and largest private RTK network, established 2014. Originally
implemented by Suleco (Pvt) Ltd; now operated by CORSnet (Pvt) Ltd. Provides
centimetre-level RTK corrections island-wide via NTRIP/TCP. Sectors served include
surveying, construction, GIS, drone operations, and agricultural machinery. Accuracy
quoted as 2.5 mm + 0.5 ppm (static) and 15 mm + 1 ppm (RTK). Plans range from
2,500 LKR/day to 1,000,000 LKR for 5 years; VAT inclusion not explicitly stated on
the public pricing page. Hobbyist eligibility confirmed: registration open to any
individual with a network-ready GNSS receiver. Host:port provided post-registration;
pricing confirmed publicly 2026-04-30 at corsnet.lk/services.
Not added to pipeline — paid service at ~$1,080/yr, and caster address not public.

---

## kazgeodesy — НЦГПИ / KazGeoDesy (KZ)

**status**:    paid-affordable
**country**:   KZ — Kazakhstan
**type**:      physical-coord-vrs (network RTK)
**host:port**: **investigate**: likely `rtk.qgeo.kz:2101` (unconfirmed; not publicly disclosed)
**access**:    paid subscription; self-service portal at rtk.qgeo.kz; registration
               requires Kazakh ИИН (individual) or БИН (business) — de-facto
               residency requirement; foreign users cannot complete self-service
**yearly_cost**: 65,000 ₸/yr (~$141/yr)
**registration**: https://rtk.qgeo.kz
**stations**:  120+ (concentrated around Almaty, Astana, and northern corridor)

**date_added**: 2026-04-30

РГП «Национальный центр геодезии и пространственной информации» (НЦГПИ); colloquially
still "Казгеодезия / KazGeoDesy". Current legal entity is НЦГПИ under the Committee
of Geodesy and Cartography, Ministry of Digital Development, Innovations and Aerospace
Industry (qazgeodesy.kz). RTK service delivered via rtk.qgeo.kz; tariffs confirmed
publicly at rtk.qgeo.kz/tarifs (no login required 2026-04-30): 65,000 ₸/yr annual,
or 7,000 ₸/month. Each subscription covers up to 5 reference stations and 5
simultaneous rover connections. Additional periods (7-day trial, 2-year, 3-year,
5-year, Unlimited) present in portal but prices not shown publicly on this visit.
VAT inclusion unclear — 12% Kazakh VAT may apply. The legacy kazgeodeziya.kz domain
returns a hosting-expired error; active domain is qazgeodesy.kz / rtk.qgeo.kz.
Country is ~2.7 million km²; baselines will be long outside urban centres.
Not added to pipeline — paid service; caster address unconfirmed.

---

## almgc_tj — State Committee for Land Management and Geodesy (TJ)

**status**:    rejected
**country**:   TJ
**access**:    no public NTRIP endpoint found; agency website unreachable
**source**:    zamin.tj (State Committee for Land Management and Geodesy)
**host:port**: not found

**date_added**: 2026-04-30

The State Committee for Land Management and Geodesy (Государственный комитет
по земельному управлению и геодезии) operates GNSS equipment for cadastral
and land-reform work across Tajikistan, supported by the "Fazo" Institute.
A national geodetic GNSS network was established partly through the World
Bank Land Registration and Cadastre System project (~2005–2012). No public
NTRIP caster or open self-service CORS endpoint has been identified.
The almgc.tj domain returned browser error pages on 2026-04-30; no cached
or archived version returned any GNSS or NTRIP content. No evidence that
a real-time NTRIP/RTK service has ever been publicly operated by this agency.
CAIAG (Central Asian Institute for Applied Geosciences) maintains one
permanent GNSS station in the Pamir region as part of its 30-station
Central Asia seismic monitoring network; this is a research facility and
does not provide an RTK correction service.
Rejected — no public endpoint found; agency website unreachable.

---

## kyrpos — KyrPos GNSS Network (KG)

**status**:    paid
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

Paid — over $200/yr threshold; not viable for most hobbyists. No free public
NTRIP endpoint in Kyrgyzstan.

---

## tm_cors — Turkmenistan National CORS Network (TM)

**status**:    rejected
**country**:   TM
**type**:      single-base (physical CORS)
**access**:    government-internal; no public endpoint found
**operator**:  Land Resources Service of Turkmenistan (Turkmengeodezija,
               Ashgabat), supported by FAO
**host:port**: not found
**stations**:  65 (built 2022–2025 per FAO project documentation)

**date_added**: 2026-04-30

A 65-station CORS network was built under a 2022–2025 FAO-supported project
(Technical Assistance to Support the Establishment of Digital Land Cadastre
in Turkmenistan). The network underpins national cadastral surveying and
land administration. Checked on 2026-04-30: no entry in BKG/IGS, mvarga1989,
ArduSimple, SNIP, or rtk2go monitors; no .gov.tm or .com.tm domain references
CORS, NTRIP, or port 2101. A 2024 article on turkmenistan.gov.tm reports
ongoing GNSS equipment training, confirming the infrastructure exists but is
not yet publishing a public service. No operator website, email, or phone for
Turkmengeodezija was discoverable.
Rejected — no public endpoint; government-internal infrastructure only.

---

## azpos — AzPOS (AZ)

**status**:    restricted
**country**:   AZ
**type**:      physical-coord-vrs (Leica GNSS Spider)
**access**:    bilateral service agreement required; no self-service registration;
               "legal entities and individuals" may apply per operator contact
               page, but process is conducted entirely in Azerbaijani; no
               published tariff
**host:port**: `azpos.az:2101` (authentication-gated; no public sourcetable to
               unauthenticated queries; confirmed provisionally 2026-04-30 via
               SNIP checker — blank response, consistent with IP-whitelisting or
               authenticated NTRIP)
**operator**:  State Service on Property Issues under the Ministry of Economy
               (Əmlak Məsələləri Dövlət Xidməti); SBC portal:
               http://www.azpos.az/sbc/ (Leica Spider Business Center)
**registration**: https://emlak.gov.az/az/news/view/4856-Əlaqə (contact page)
**stations**:  45 (37 original + 8 restored in Karabakh 2024: Fuzuli, Jebrail,
               Zangilan, Kəlbəcər ×2, Ağdam, Şuşa, Laçın)
**signals**:   GPS, GLONASS, Galileo, BeiDou
**nmea_filter**: n/a (not in pipeline)

**date_added**: 2026-04-30

AzPOS (Azerbaijan Positioning Observation System) is the national CORS network
operated by the State Service on Property Issues under the Ministry of Economy
of Azerbaijan. Originally 37 stations at ~30–40 km spacing across mainland
Azerbaijan; 8 stations were restored in the Karabakh region in 2024 following
the September 2023 restoration of full territorial control. Receivers validated
with Leica GS18; backend is Leica GNSS Spider (VRS capable). The SBC login
portal at azpos.az/sbc/ shows an RTK product with Subscription Period,
Consumption Limit, and Working Area fields — all values hidden pre-login.
No published tariff found on any public page (ArduSimple lists AzPOS as "paid
national service" with no price). Access requires bilateral agreement; pricing
and final host:port confirmed only after contracting.
Restricted — no published tariff; contract-only access.

---

## armpos — ARMPOS (AM)

**status**:    restricted
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

Restricted — access limited to licensed surveyors and government cadastre users; no public NTRIP endpoint.
**missing**: public NTRIP host:port and access conditions — contact Cadastre
Committee via cadastre.am.

---

## geocors_ge — GeoCors (GE)

**status**:    restricted
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

Restricted — paid subscription; pricing and access terms not publicly documented; no hobbyist registration path.
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

## eft_cors — EFT-CORS / СДГС CORS (RU)

**status**:    paid
**type**:      physical-coord-vrs
**host:port**: `ntrip.eftgroup.ru:2101` (primary); `:2102` all stations; `:2103` nearest;
               `:2104` sCMRx format; port 70+region-code for regional subsets (e.g., 7040 = Kaluga Oblast).
               Note: the legacy domain `eftcors.ru` has an SSL error; use `eftgroup.ru` infrastructure.
**access**:    paid; day/month/6-month/annual plans; 3-day free RTK trial; RINEX 1 Hz/30 s free
**yearly_cost**: ₽50,400/yr (~$593/yr); RTK+ enhanced: ₽60,480/yr (~$711/yr); EFT-hardware discount: ₽30,240/yr (~$356/yr). All prices 5% VAT included. Observed 2026-05-02.
**registration**: `https://bp.eft-cors.ru/register`
**stations**:  hundreds, growing; GPS+GLONASS+BDS+GAL
**source**:    eft-cors.ru (EFT GROUP, Moscow)
**operator**:  EFT GROUP

Russia's largest CORS aggregator. Operated by EFT GROUP (геодезическое оборудование). Stations
added by partners across all federal districts. No free public RTK tier; RINEX basic (1 Hz, 30 s
intervals) is free for post-processing; extended RINEX (higher-rate) is paid. Registration
requires only name + email; individual sign-up supported. Credentials provided after subscribing.

---

## rtknet — RTKNet (RU)

**status**:    paid
**type**:      single-base
**host:port**: `94.250.250.43:2101` (primary IP); `cors.rtknet.ru:2101` (hostname alias);
               regional ports: 6030 Central, 6031 North-West, 6033 Volga, 6034 Ural,
               6038 North Caucasus, 6040 South, 6041 Siberia/Far East (RTCM32-MSM streams).
               Port 2101 for own mobile base.
**access**:    paid; 3-day free trial (new customers or via geodetika.ru support); register at rtknet.ru
**yearly_cost**: ₽30,000/yr (~$353/yr at ~85 ₽/USD). VAT inclusion not stated on pricing page — confirm with operator. Observed 2026-05-02.
**registration**: `https://rtknet.ru`
**stations**:  300+ across Russia; RTCM 3.0 and RTCM 3.2-MSM4; 1 Hz
**source**:    rtknet.ru (ООО «ГЕОДЕТИКА» / Geodetika)
**operator**:  ООО «ГЕОДЕТИКА» (Geodetika)

Growing since 2013; covers all federal districts. Individual registration via self-service
cabinet (rtknet.ru/cabinet/auth/); public offer contract (договор-оферта), no B2B requirement.
Some equipment resellers include 1-year RTKNet access with GNSS receiver purchases.

---

## hive_cors — HIVE (RU)

**status**:    paid
**type**:      single-base
**host:port**: `hive.geosystems.aero:2101` (confirmed 2026-05-02 via forum.geosystems.aero/t/nastrojki-ntrip/1233)
**access**:    pay-per-use — RTK charged daily (until 23:59 MSK); first ~5 min (~100 KB) free per station;
               RINEX charged hourly; station owners get free NTRIP caster software + storage + 50% revenue share
**yearly_cost**: variable (pay-per-use; per-station daily prices only visible on map after login — not publicly listed)
**registration**: `https://hive.geosystems.aero`
**stations**:  742 in 79 Russian regions (independently owned; aggregation platform, not a CORS network)
**source**:    hive.geosystems.aero (Индустриальные геодезические системы / Geosystems.aero, Omsk)
**operator**:  Индустриальные геодезические системы (Geosystems.aero)

Aggregation model — not a traditional CORS network: independent reference station owners connect
their stations to HIVE; users pay per-station per-day for RTK (single-baseline, no VRS computation
layer). Per-station daily prices are set by the station owner and only visible after login on the
map card. Accepts VISA/MC and Russian e-wallets. 742 stations across 79 regions as of 2026-05-02.

---

## geospider — ГЕОСПАЙДЕР (RU — North-West)

**status**:    paid
**type**:      physical-coord-vrs
**host:port**: `geo-spider.net:2101` (confirmed via multiple third-party setup guides and official PDFs hosted at geospider.ru/instructions; confirm via geospider.ru if needed)
**access**:    paid; day/week/fortnight/month/quarter/annual subscriptions; register via geospider.ru
**yearly_cost**: ₽44,100/yr (~$519/yr, 30% annual discount applied). All prices 5% VAT included. Observed 2026-05-02.
**registration**: `https://geospider.ru`
**stations**:  200+ (St. Petersburg, Moscow, Leningrad, Novgorod, Pskov, Tver, Vologda oblasts and expanding)
**source**:    geospider.ru (ООО «НПП «ГЕОМАТИК», St. Petersburg)
**operator**:  ООО «НПП «ГЕОМАТИК»

Regional-to-expanding network for North-West and Central Russia. RTK in local MSK coordinate
system (network RTK / VRS to MSK). RINEX also available (separate subscription). Individual
sign-up supported; no company registration required. Coverage expanding beyond original North-West
footprint as of 2026.

---

## Rejected — explicitly excluded

---

## geodaf — GeoDAF / ASI (IT)

**status**:    rejected
**host:port**: `geodaf.mt.asi.it` (EUREF mirror)
**reason**:    raw GNSS observations only (EUREF raw); no RTK or VRS streams;
               suitable for post-processing only — borderline out of scope

---

## agrs_nl — AGRS.NL / Kadaster (NL)

**status**:    free
**date_added**: 2026-05-01
**country**:   NL — Netherlands
**type**:      single-base (~30 mainland stations; BES islands catalogued separately under `bq_cors`)
**host:port**: `ntrip.kadaster.nl:2101` (plain TCP) / `ntrip.kadaster.nl:443` (TLS)
**access**:    free, anonymous; email as username suggested for outage notifications but optional
**registration**: https://nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams
**operator**:  NSGI / Kadaster Nederland (`nsgi.nl`)

NSGI's Active Geodetic Reference System for the Netherlands (AGRS.NL). Free,
anonymous access. Legal basis: Kadasterwet BWBR0037196 art. 19 lid 4. ~30 mainland
stations, RTCM 3.2 MSM. The same caster also hosts BES island stations (7 streams),
catalogued under `bq_cors`.
TU Delft mirror: `gnss1.tudelft.nl:2101` — subset of stations, no TLS.
**Volunteer**: none. Zero NL-mainland candidate stations separate from AGRS.NL.

---

## netpos — NETPOS / Kadaster (NL)

**status**:    paid
**date_added**: 2026-05-01
**country**:   NL — Netherlands
**type**:      single-base raw reference streams (not VRS)
**host:port**: `ntrip.cloud.kadaster.nl:443` (TLS only; NTRIP auth B;Y required)
**access**:    paid; username + password issued on activation; eHerkenning portal for
               NL legal entities; foreign users apply via contact form at nsgi.nl
**registration**: https://nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams
**yearly_cost**: €475/station/yr excl. BTW (~$520/yr) for 1–2 stations; volume to €95/station/yr for 10+ (2026 tariff)
**operator**:  NSGI / Kadaster Nederland (`nsgi.nl`)

NETPOS delivers raw reference station streams from the same ~30 AGRS.NL
physically-positioned base stations, as an authenticated paid service.
Priced per station per year (2026, excl. BTW): 1–2 stations €475/station,
3–4 €380, 5–6 €285, 7–9 €190, 10+ €95. VAT-exempt. Not a VRS / network-RTK
service — streams are single-base raw observations for users who compute their
own corrections.

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

**status**:    weird
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

**status**:    restricted
**reason**:    restricted to TXDOT employees and contractors only; no public or hobbyist registration

---

## calrtns — CalRTNS / Caltrans CORS (US-CA)

**status**:    restricted
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

**status**:    weird
**reason**:    public regional service discontinued; stations now commercially operated
               via NetGEO/TopNET Live (netgeo.it); not free

---

## ergand — ERGAND Geodetic Network (AD)

**status**:    weird
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

Post-processing only; no public NTRIP service found. Surfaced as a `weird`
country marker so target users in Andorra know what's locally available.

---

## li_cors — Liechtenstein Geodata / ATG (LI)

**status**:    weird
**country**:   LI — Liechtenstein
**type**:      no independent CORS programme
**host:port**: not applicable
**access**:    no public NTRIP caster
**notes**:     The Amt für Tiefbau und Geoinformation (ATG, llv.li) manages national
               geodata infrastructure but operates no CORS network or NTRIP caster.
               Liechtenstein surveyors rely on swipos (swisstopo, CHF 1,500/yr ≈ $1,650)
               which covers the entire principality via AGNES stations 5–10 km across the
               Swiss border. No free public RTK endpoint exists for the territory.

No CORS programme or public NTRIP service found. Surfaced as a `weird`
country marker so target users in Liechtenstein know what's locally available.

---

## sm_cors — San Marino Geodetic Reference (SM)

**status**:    weird
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

Post-processing only; no public NTRIP service found. Surfaced as a `weird`
country marker so target users in San Marino know what's locally available.

---

## qc_mern — Réseau GNSS du Québec / MERN (CA-QC)

**status**:    weird
**reason**:    per-station direct TCP streams (not NTRIP aggregated); incompatible with
               standard NTRIP pipeline; no NTRIP caster endpoint published

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

**status**:    weird
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

SIRGAS Bol21 (2016) states "El IGM se está incorporando a esta iniciativa" (IGM Bolivia
is joining this initiative) — referring to the commercial GeoBolivia SRL RED-GEO network,
not IGM operating its own public caster. Academic fieldwork (UMSA university thesis) cites
using "CORS GEO1 perteneciente a la empresa Geo Bolivia S.R.L." as the reference station,
confirming practitioners use the commercial network rather than an IGM service directly.
`igm.gob.bo` was unreachable on 2026-04-30 (the entry's `igmbolivia.gob.bo` may be a
different active domain — verify). No confirmed public NTRIP endpoint for IGM Bolivia;
pricing, if any service exists, has not been found.

**missing**: confirm whether igmbolivia.gob.bo has a public NTRIP caster host:port or
             whether MARGEN-ROC NTRIP is exclusively RINEX/post-processing.

---

## redgeo_bo — RED-GEO CORS NTRIP (BO)

**status**:    paid
**country**:   BO — Bolivia
**type**:      single-base
**host:port**: caster port 6060; full hostname not publicly confirmed — credentials
               (host, port, username, password) issued by phone only
**access**:    paid; phone registration required; no online self-service portal
**yearly_cost**: not publicly listed (contact GeoBolivia SRL via Facebook or phone)
**registration**: geoboliviasrl.info (GeoBolivia SRL website — unreachable 2026-04-30;
                  Facebook page "GeoBolivia SRL - Geomática" active)
**stations**:  ~7 stations: La Paz (GEO 1), Cochabamba (GEO 2), Oruro (GEO 3),
               Sacaba (GEO 4), Tarija (GEO 5), Santa Cruz (GEO 6), Yacuiba (Tarija dept.)
**source**:    geoboliviasrl.info (when reachable); SIRGAS Bol21 (2016); UMSA thesis;
               facebook.com/GeoBoliviaSRL (active, posts within days of 2026-04-30)

**date_added**: 2026-04-29

RED-GEO is a private commercial CORS NTRIP network operated by GeoBolivia SRL. The network
is described as regulated under Bolivia's Ley 2997 del Topógrafo and administered in
coordination with COTOBOL (Colegio de Topógrafos de Bolivia). The caster supports
GPS + GLONASS + Galileo + BeiDou on port 6060. Station coordinates are tied to Class A
and B points of the government MARGEN framework. Access requires phoning GeoBolivia SRL
to receive credentials; no hostname or pricing is published on the website or in any indexed
source. A Facebook post (within weeks of 2026-04-30) offered one year of RED-GEO access
free as a hardware bundle bonus, confirming the service is active. General subscription
pricing in BOB is not publicly available. geoboliviasrl.info was unreachable on 2026-04-30.

**missing**: confirm full caster hostname and subscription pricing in Bs/yr once
             geoboliviasrl.info is accessible or via Facebook contact.

---

## ign_gt_cors — IGN Guatemala Red CORS (GT)

**status**:    weird
**country**:   GT — Guatemala
**type**:      single-base
**host:port**: none — post-processing RINEX download service only; no NTRIP caster
**access**:    free RINEX data downloadable from ign.gob.gt; no real-time corrections
**registration**: ign.gob.gt (Instituto Geográfico Nacional — Guatemala)
**stations**:  ~17 stations distributed nationally

**date_added**: 2026-04-30

Guatemala's Instituto Geográfico Nacional (IGN) operates a Red CORS (Continuously Operating
Reference Stations) of approximately 17 stations distributed across the national territory.
The network was established with technical and financial support from RIC (Registro de
Información Catastral) to enable rapid cadastral surveys tied to the national reference
system. RINEX 2.11 data is available for download from the IGN website. The IGN and RIC
public portals list only a post-processing RINEX data product ("datos CORS"); no separately
priced or free live NTRIP/RTK streaming subscription is publicly documented. ArduSimple
(2026) does not list Guatemala as having a national RTK network accessible to hobbyists.
Free RINEX archive only; no real-time NTRIP service offered. Surfaced as a `weird`
country marker so target users in Guatemala know free post-processing data exists.

## ip_cors_hn — IP CORS Honduras / IGN Honduras (HN)

**status**:    weird
**country**:   HN — Honduras
**type**:      single-base
**host:port**: none — post-processing RINEX download service only; no NTRIP caster
**access**:    free RINEX data downloadable at cors.ip.gob.hn; no real-time corrections
**registration**: https://cors.ip.gob.hn
**stations**:  5 (Tegucigalpa/TEG, San Pedro Sula/ICF1, Juticalpa/JUT1,
               Siguatepeque/UNCF, La Ceiba/CEIB)

**date_added**: 2026-04-30

The Dirección General de Cartografía y Geografía (DGCG), sub-directorate of the
Instituto de la Propiedad (IP), operates Honduras's national CORS network. Its portal
(cors.ip.gob.hn) provides free RINEX file downloads for 5 stations covering major
urban centres. No NTRIP caster endpoint, no real-time RTK service, and no subscription
tariff exist or have been announced publicly. The "IGN Honduras" brand (ign.hn) is the
same institution — the former IGN was reorganised into the DGCG/IP; ign.hn is an
auxiliary web presence for the same network. Honduras is absent from ArduSimple and
rtcm-ntrip.org caster directories. A 2024 public comment on the IP's Facebook page
explicitly called for activation of a live CORS/NTRIP service, confirming it had not
yet occurred at that date.
Free RINEX archive only; no real-time NTRIP service exists. Surfaced as a `weird`
country marker so target users in Honduras know free post-processing data exists.

## ign_hn_cors — IGN Honduras CORS (HN)

**status**:    rejected
**country**:   HN — Honduras

**date_added**: 2026-04-30

IGN Honduras is not a separate entity from the IP/DGCG — see `ip_cors_hn`. The IGN
brand is maintained at ign.hn as an auxiliary web presence; the CORS network described
there is the same 5-station network documented under `ip_cors_hn`. No separate NTRIP
service or caster endpoint exists under the IGN brand.
Rejected — same institution as `ip_cors_hn`; post-processing only.

## ineter_cors — INETER CORS (NI)

**status**:    weird
**country**:   NI — Nicaragua
**type**:      single-base
**host:port**: none — post-processing RINEX download service only; no NTRIP caster
**access**:    free RINEX data accessible via consultacf.ineter.gob.ni; no real-time corrections
**registration**: consultacf.ineter.gob.ni (INETER — Catastro Físico)
**stations**:  unknown

**date_added**: 2026-04-30

INETER (Instituto Nicaragüense de Estudios Territoriales), through its Dirección General
de Geodesia y Cartografía, maintains a network of satellite observation CORS stations as
part of its SIRGAS contributions and the national spatial data infrastructure (IDE). The
Catastro Físico portal (consultacf.ineter.gob.ni/Servicio/ConsultaDatosCORS) provides
RINEX data access for post-processing. No public NTRIP caster endpoint or live streaming
subscription has been found. The INETER and SINAPRED public portals list only a
post-processing RINEX product ("datos CORS"); no real-time RTK service is publicly
documented. Nicaragua's Ortega-Murillo government is subject to targeted OFAC sanctions
(individuals/entities), but the sanctions do not specifically restrict civil GNSS
infrastructure access; the absence of a public NTRIP endpoint is a capacity/policy issue.
Free RINEX archive only; no real-time NTRIP service offered. Surfaced as a `weird`
country marker so target users in Nicaragua know free post-processing data exists.

## cnr_sv_cors — CNR/IGCN CORS (SV)

**status**:    weird
**country**:   SV — El Salvador
**type**:      single-base
**host:port**: none — post-processing RINEX download service only; no NTRIP caster
**access**:    free RINEX data accessible via e.cnr.gob.sv; no real-time corrections
**registration**: e.cnr.gob.sv (Centro Nacional de Registros — IGCN online services)
**stations**:  ≥3 confirmed active CORS: SNJE, SSIA, VMIG; SSIA also in IGS global network

**date_added**: 2026-04-30

The Instituto Geográfico y del Catastro Nacional (IGCN) within El Salvador's Centro
Nacional de Registros (CNR) has operated active CORS stations since at least 2007.
Known stations include SNJE, SSIA (San Salvador, also part of the IGS global network),
and VMIG, with the network densified across multiple departments. RINEX data is available
via the eCNR online services portal. The CNR and IGCN public portals list only a
post-processing RINEX product ("datos CORS"); no separately priced or free live NTRIP/RTK
streaming subscription is publicly documented. The commercial operator Survey3G provides
the only known real-time NTRIP service in El Salvador.
Free RINEX archive only; no real-time NTRIP service offered. Surfaced as a `weird`
country marker so target users in El Salvador know free post-processing data exists.

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

**status**:    free
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

**status**:    weird
**country**:   PG — Papua New Guinea
**type**:      single-base (scientific reference stations; no RTK density)
**host:port**: not publicly listed
**access**:    no public NTRIP caster confirmed
**stations**:  ~6: IGS stations LAE1 (Unitech, Lae) and PNGM/WAIG (DLPP, Port Moresby);
               plus ~4 APREF stations under the PNG2020 datum programme (FIG 2025)
**operator**:  DLPP (Department of Lands and Physical Planning) for WAIG/PNGM;
               PNG University of Technology (Unitech) for LAE1
**source**:    dlpp.gov.pg (403 on 2026-04-30); Stanaway, Nidkombu et al., FIG Working
               Week 2025 paper (confirmed sparse network, FAIR NTRIP access planned);
               quickclose.com.au/Waig_installation.pdf; aspng.org

**date_added**: 2026-04-29

Both IGS stations contribute raw GNSS observations to Geoscience Australia's Asia-Pacific
Reference Frame (APREF) network. WAIG (IGS code PNGM), installed at Eda Tano Haus,
Waigani Drive, Port Moresby, underpins the PNG2020 geodetic datum; LAE1 at Unitech has
been part of the IGS tracking network since 2002. The FIG 2025 paper (Stanaway, Nidkombu
et al.) confirms the PNG2020 programme intends to offer RTCM3/NTRIP access under a
UN-GGIM FAIR open-access principle, but as of April 2025 the network is sparse and the
portal is not yet public. dlpp.gov.pg returned HTTP 403 on 2026-04-30. The MRA PNG
(`mra.gov.pg`) ran a demonstration NTRIP test at a Unitech GNSS workshop but no public
endpoint was published. Station spacing makes baselines far exceed the practical ~30 km
RTK range for all but Lae and Port Moresby.

The AUSCORS broadcaster (`ntrip.data.gnss.ga.gov.au:2101`) streams APREF-contributing
stations across the Pacific, but PNG-area streams are reference-grade archive feeds,
not a substitute for a local RTK CORS network. Hobbyists must deploy a local base
station. Secondary contact: ASPNG (`aspng.org`), maintained by Quickclose.

## fiji_dlss_cors — Fiji CORS (FJ)

**status**:    weird
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

**date_added**: 2026-05-01

No government RTK correction service found. The Lands and Survey Division holds geodetic
responsibility but no NTRIP caster host:port or registration portal has been identified.
COCONet / EarthScope NOTA includes at least one station in Antigua for geophysics monitoring.
The legacy UNAVCO NTRIP platform was retired 2025-07-29; EarthScope NOTA continues at
`ntrip.earthscope.org:2101`, but whether any Caribbean / AG station is present in the
new caster's sourcetable has not been confirmed.
Zero AG mountpoints on rtk2go or Centipede.

**missing**: check `ntrip.earthscope.org:2101` sourcetable for AG-coded stations;
confirm whether Antigua COCONet station was migrated to the EarthScope caster.

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

## almgg_mn — CORS Network / MonPOS (MN)

**status**:    free
**country**:   MN — Mongolia
**type**:      physical-coord-vrs (Trimble NetR8/NetR9 hardware; MGL_network is VRS;
               caster: SubCarrier Systems SNIP R3.14.00, curl-confirmed 2026-04-30)
**host:port**: `rtk.gazar.gov.mn:2101` (primary; curl-confirmed 2026-04-30);
               alternate IP `66.181.168.80:2101`
**access**:    free; shared public credentials posted on the government announcement
               page (`monpos.gazar.gov.mn/monpos/3/`): username `rover`,
               password `262461`; individual accounts also available via
               `geodesy.gov.mn` (citizen / legal entity login)
**registration**: https://monpos.gazar.gov.mn (MonPOS portal);
                  https://geodesy.gov.mn (individual account registration —
                  ГЗЗУНС portal; "Иргэн" = citizen and "Хуулийн этгээд" =
                  legal entity options; Mongolian DAN QR login may be required
                  for full portal access)
**stations**:  40+ (Trimble NetR8/NetR9 with choke-ring and Zephyr Geodetic
               antennas; Ulaanbaatar, Darkhan, Erdenet + nationwide)
**operator**:  General Office of Land Relations, Geodesy and Cartography
               (Газар зохион байгуулалт, геодези, зураг зүйн ерөнхий газар,
               `gazar.gov.mn`); formerly ALACGaC / ALMGG
**source**:    monpos.gazar.gov.mn/monpos/3/ (public announcement with credentials,
               confirmed 2026-04-30)
**pipeline-flags**: `solution_filter=False` (6 physical stations wrongly tagged
                    solution=1 by the caster)

**date_added**: 2026-04-29

Initial 6-station CORS infrastructure delivered in December 2010 by ILS (International
Land Systems) under the Millennium Challenge Corporation Property Rights Project, with
Trimble NetR8 receivers. Used initially for cadastral surveys and GCPs covering ~75,000
property plots. Network has since grown to 40+ stations countrywide. A government
announcement at `monpos.gazar.gov.mn/monpos/3/` (retrieved 2026-04-30) confirms the VRS
mountpoint `MGL_network` at `rtk.gazar.gov.mn` with shared public credentials. Accuracy:
≤35 km baseline, ±(2 cm + 1 ppm), RTCM 3.x. Station map on monpos.gazar.gov.mn shows
mixed online/offline status. Mongolia is ~1.56 million km²; average inter-station
distance ~200 km — RTK practical only in the Ulaanbaatar–Darkhan–Erdenet corridor.
Added to pipeline 2026-04-30 (`almgg_mn` in SOURCES, credentials `rover`/`262461`).
Zero MN mountpoints on rtk2go or Centipede.

## survey_bn — Survey Department Brunei (BN)

**status**:    weird
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

**status**:    free
**country**:   BF — Burkina Faso
**type**:      single-base (physical CORS stations)
**host:port**: `www.bfcors.net:2101` (inferred from Trimble Pivot Web architecture;
               not directly curl-confirmed — TCP connection not verifiable via browser)
**access**:    free with registration; administrator-issued credentials
**registration**: https://www.bfcors.net/RegisterAccount.aspx (self-service form;
                  admin emails credentials on approval; no professional licence field
                  in registration form, though IGB communications target surveyors)
**stations**:  ~13 physical: 9 original (2011 MCA-BF funding) + 4 capital-region (2018)
**operator**:  IGB — Institut Géographique du Burkina (`igb.bf`), Ouagadougou
**source**:    bfcors.net (Trimble Pivot Web portal, confirmed live 2026-04-30 —
               Sensor Map showed 13 station markers); igb.bf/presentation-du-reseau-gnss-cors/

**date_added**: 2026-04-29

Nine permanent GNSS stations established in 2011 under a contract between MCA-BF
(Millennium Challenge Account Burkina Faso) and Trimble Europe BV (~700 million FCFA
contract signed May 2010); IGB assumed technical management in September 2012. Station
locations: Gampela, Manga, Fada, Diapaga, Dori, Ouahigouya, Dédougou, Bobo, Gaoua.
Four additional capital-region stations added in 2018 (Ouagadougou-IGB, Koubri,
Dapélogo, Tanguen-Dassouri). Registration is free at `bfcors.net`; the administrator
emails credentials. Two coups in 2022 and membership in the Alliance of Sahel States
(AES) from January 2025 have reduced bilateral technical cooperation with France/West,
but the IGB service has continued operating; bfcors.net was live on 2026-04-30 with 13
stations visible on the Sensor Map. No BF mountpoints on rtk2go or Centipede.

**missing**: confirm `www.bfcors.net:2101` by curl or by completing registration;
             confirm whether professional vetting applies during account approval.

---

## ign_bj — IGN Bénin Permanent GNSS Station Network (BJ)

**status**:    free
**country**:   BJ — Benin
**type**:      single-base (physical CORS stations)
**host:port**: not publicly listed (disclosed after registration via IGN Bénin / CatIS)
**access**:    free with registration; accessible via Benin Cadastral Information System
**registration**: https://service-public.bj (service PS01085 — "Fichier des stations permanentes GNSS")
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
A 2021 procurement notice on `ign.bj` referenced "modernisation du réseau CORS-GNSS
vers la solution RTK (NTRIP)", confirming RTK/NTRIP delivery was in scope at that time.
CatIS (`catistest.xroad.bj`) lists "Stations CORS GNSS Permanentes / Institut Géographique
National" as a registered system and `ign.bj` homepage is responsive (confirmed 2026-05-01);
no public caster hostname found in any directory or sourcetable.

**missing**: confirm NTRIP host:port by completing CatIS / IGN Bénin registration;
confirm station count and whether any stations have been added since MCA-Bénin period.

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

## dgigc_tg — IGNTOGO / Togo National CORS Network (TG)

**status**:    free
**country**:   TG — Togo
**type**:      single-base (physical CORS stations, exact count unconfirmed)
**host:port**: not publicly listed; `igntogo.tg` unreachable as of 2026-05-01 —
               contact IGNTOGO via `urbanisme.gouv.tg`
**access**:    professional use; registration via IGNTOGO; access terms not
               published on public website
**registration**: https://urbanisme.gouv.tg (Ministry of Town Planning and Urban
                  Development website)
**stations**:  unconfirmed count; deployment began 2017; 614 geodetic benchmarks
               nationwide as of 2025; CORS stations at key reference points
**operator**:  IGNTOGO (formerly DGIGC — Direction Générale de l'Information
               Géographique et de la Cartographie, renamed February 2026);
               Ministry of Town Planning and Urban Development (`urbanisme.gouv.tg`)
**yearly_cost**: unknown (no public tariff)

**date_added**: 2026-05-01

A national CORS network was deployed from 2017 under DGIGC, renamed IGNTOGO in
February 2026. A March 2026 interministerial communiqué mandated systematic
attachment of all topographic, cadastral, urbanism, and infrastructure work to the
National Geodetic Network, with a three-month compliance window. As of 2026, Togo
has 614 geodetic benchmarks (1st, 2nd, and 3rd order) including 11 first-order
benchmarks. `igntogo.tg` is unreachable (connection refused, confirmed 2026-05-01);
`urbanisme.gouv.tg` remains reachable but contains no CORS/NTRIP portal. No public
NTRIP caster host:port found in any directory, sourcetable, or registration portal.
Zero TG mountpoints on rtk2go or Centipede.

**missing**: confirm NTRIP host:port by contacting IGNTOGO via `urbanisme.gouv.tg`;
confirm exact CORS station count and access model; check whether any stations
have been shared to rtk2go or Centipede; confirm whether a new IGNTOGO web portal
replaces `igntogo.tg`.

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

**status**:    rejected
**country**:   GL — Greenland (Danish autonomous territory)
**type**:      single-base (geodetic reference network; RINEX/PPK only)
**host:port**: n/a — no NTRIP caster; RINEX files via Dataforsyningen
**access**:    RINEX 2/3 freely available via `dataforsyningen.dk`; no RTK/NTRIP
               stream identified in any aggregator as of 2026-05-01
**registration**: https://dataforsyningen.dk (Dataforsyningen — Danish national
                  geodata portal); UNAVCO/EarthScope archive also accessible
**stations**:  ~60 continuous GNSS stations across Greenland
**operator**:  KDS/Klimadatastyrelsen (Danish Agency for Climate Data, formerly SDFi)
               + DTU Space; Asiaq (Greenland Survey) contributes territorial operations

**date_added**: 2026-05-01

GNET (go-gnet.org) is a geodetic monitoring network spanning Greenland, maintained
primarily for ice-sheet dynamics research, sea-level and glacial isostatic rebound
studies, and geodetic reference-frame maintenance. RINEX 2/3 observation files are
distributed via Dataforsyningen (`dataforsyningen.dk`); go-gnet.org and asiaq.gl
confirmed alive 2026-05-01. Asiaq (`asiaq.gl`) lists Survey and Construction services
but publishes no GNSS correction product. No public NTRIP streaming caster found in
any aggregator (ntrip-list.com/europe, rtk2go, EarthScope NOTA sourcetable) as of
2026-05-01. Zero GRL stations in rtk2go, Centipede, or EarthScope NOTA streaming
sourcetables. Rejected: RINEX/PPK only.

**missing**: confirm whether KDS, DTU Space, or Asiaq is planning a public NTRIP
             streaming service for Greenland.

## umhvorvisstovan_fo — Umhvørvisstovan GNSS Network (FO)

**status**:    restricted
**country**:   FO — Faroe Islands (Danish autonomous territory)
**type**:      single-base (4 confirmed physical GNSS reference stations)
**host:port**: not publicly listed; access requires direct contact with Umhvørvisstovan
**access**:    professional/commercial clients (surveying firms, construction companies);
               no self-service portal or published endpoint; hobbyist eligibility unclear
**registration**: https://us.fo/kort/geodesi (agency contact; no self-service signup)
**stations**:  4 physical: Klaksvík, Vestmanna, Trongisvágur, Argir (confirmed 2026-05-01)
**operator**:  Umhvørvisstovan — The Faroese Environment Agency (`us.fo`,
               formerly `umhvorvisstovan.fo`)

**date_added**: 2026-05-01

Umhvørvisstovan holds responsibility for surveying, mapping, and geodesy of the Faroe
Islands (land and sea). The agency's geodesy page (`us.fo/kort/geodesi`, confirmed
2026-05-01) explicitly advertises centimetre-level RTK access via 4 permanent GNSS
reference stations for surveying firms and construction companies. No caster hostname,
port, sourcetable URL, or tariff is published; access is entirely via direct contact.
One EPN station (ARGI00FRO, Argir, Tórshavn) was part of the EUREF Permanent GNSS
Network; RINEX 2 data submission ceased February 2021. Danish GPSnet explicitly
excludes the Faroe Islands. Zero FRO mountpoints on rtk2go or Centipede. A Geospatial
Centre at Fróðskaparsetur Føroya (Setur, the University of the Faroe Islands) was
launched in partnership with Landsverk and Umhvørvisstovan to develop geodesy and
surveying capacity.

**missing**: confirm caster host:port and whether a tariff is published; clarify
whether non-commercial / hobbyist access is available via us.fo/kort/geodesi.

## gibr_gi — BIGF/IGS Reference Station Gibraltar (GI)

**status**:    weird
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

**status**:    weird
**country**:   CW — Curaçao
**type**:      unknown (no public caster endpoint identified)
**host:port**: not publicly listed
**access**:    unknown — no public self-service registration portal found
**registration**: https://www.kadaster.cw/contact
**yearly_cost**: n/a (no public service)
**stations**:  unknown; NSGI can establish GNSS infrastructure at local government request
**operator**:  Stichting Kadaster en Openbare Registers Curaçao (`kadaster.cw`);
               geodetic support available from NSGI (`nsgi.nl`) on request

**date_added**: 2026-05-01

No public RTK correction service or NTRIP caster found for Curaçao. Kadaster Curaçao
(`kadaster.cw`, confirmed alive 2026-05-01) has no GNSS or NTRIP section. Neither
`ntrip.kadaster.nl:2101` nor `ntrip.cloud.kadaster.nl:443` carries any CUW-coded
mountpoint (sourcetable verified 2026-05-01); NSGI FAQ states geodetic enquiries for
Curaçao must go to local authorities. EarthScope COCONet station CN40_RTCM3P3
(12.18°N, −68.96°W) streams via `ntrip.earthscope.org:2101` under NULA (free
non-commercial) — the practical free option for the island. Three rtk2go volunteer
bases near Willemstad (CWM_JAJO, MPA_JAJO, UTE_JAJO) supplement EarthScope coverage.

**missing**: confirm with Kadaster Curaçao whether any public NTRIP caster or RTK
correction service exists or is planned.

## aw_cors — Aruba Geodetic / DLV CORS (AW)

**status**:    weird
**country**:   AW — Aruba
**type**:      unknown (no public caster endpoint identified)
**host:port**: not publicly listed
**access**:    unknown — no public self-service registration portal found
**registration**: https://www.gobierno.aw/en/dienst-landmeetkunde-en-vastgoedregistratie-dlv
**yearly_cost**: n/a (no public service)
**stations**:  unknown
**operator**:  Dienst Landmeetkunde en Vastgoedregistratie (DLV), Government of Aruba
               (`gobierno.aw`)

**date_added**: 2026-05-01

No public RTK correction service or NTRIP caster found for Aruba. DLV (`dlv.aw`,
no live result as of 2026-05-01) is the geodetic and survey authority; `gov.aw`
contains only civil aviation GNSS references and no RTK correction content. NSGI
FAQ confirms DLV falls outside NSGI's mandate. EarthScope COCONet station
CN19_RTCM3P3 (12.61°N, −70.05°W, installed 2013) streams via
`ntrip.earthscope.org:2101` under NULA (free non-commercial) — the practical free
option for the island. One rtk2go volunteer base (PINOST1, Santa Cruz) is also present.

**missing**: confirm with DLV (Government of Aruba) whether any public NTRIP caster
or RTK correction service exists or is planned.

## bq_cors — BES Islands Geodetic / Kadaster NL (BQ)

**status**:    free
**date_added**: 2026-05-01
**country**:   BQ — Bonaire, Sint Eustatius, Saba (Dutch special municipalities)
**type**:      single-base (7 streams: 2 on Bonaire, 3 on Saba, 2 on Sint Eustatius)
**host:port**: `ntrip.kadaster.nl:2101` (unencrypted) / `ntrip.kadaster.nl:443` (TLS)
**access**:    free, anonymous; no username/password required
**registration**: https://nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams
**stations**:  Bonaire: BON200BES0 (Stonex SC2200, GPS+GLO+GAL+BDS),
               BONK00BES0 (Leica GR30, GPS+GLO+GAL+BDS);
               Saba: SABY00BES0 (Septentrio PolRX5E, GPS+GLO+GAL+BDS),
               SABY00BES1 (raw SBF), SABY0 (legacy RTCM 3.1, GPS+GLO);
               Sint Eustatius: SEUS00BES0 (Septentrio PolRX5, GPS+GLO+GAL+BDS),
               SEUS0 (legacy RTCM 3.1, GPS+GLO)
**operator**:  NSGI / Kadaster Nederland BES (`nsgi.nl`, `bes.kadaster.nl`)

NSGI pricing page (nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams,
confirmed 2026-05-01) explicitly lists "GNSS-stations op de BES-eilanden" as part of
the free tier (€0, no VAT). Access is fully anonymous — no username or password
required; using an email as username is suggested by NSGI for outage notifications
but optional. Both casters confirmed live via sourcetable fetch (2026-05-01). Streams
use RTCM 3.2 MSM; legacy RTCM 3.1 mountpoints also present (SABY0, SEUS0).
Single-station raw reference streams — not a VRS/network-RTK service. Kadaster's
NETPOS network-RTK service (Netherlands mainland only) does not extend to BES.
Zero BES-coded rtk2go or Centipede stations.

## sx_cors — Sint Maarten Geodetic / Kadaster SXM (SX)

**status**:    weird
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

**date_added**: 2026-05-01

No public RTK correction service or NTRIP caster found for Sint Maarten. NSGI's
sourcetable carries no SXM-coded mountpoints (verified 2026-05-01). Kadaster Sint
Maarten is a private foundation established in 1999 that manages land registration
and surveying; it achieved GIS capability in 2025 (ArcGIS platform deployment). An
early-2026 MOU between VROMI / Kadaster Sint Maarten and Kadaster Netherlands confirms
institutional cooperation — not an operational NTRIP service. The nearest EarthScope
COCONet station is CN59_RTCM3P3 (18.21°N, −63.05°W, country code AIA — physically on
Anguilla, ~20 km north of Sint Maarten), which streams via `ntrip.earthscope.org:2101`
under NULA (free non-commercial) and is usable from SXM territory at that baseline.

**missing**: confirm with Kadaster Sint Maarten or VROMI whether any NTRIP caster
or RTK correction service is planned; revisit as the Kadaster Netherlands cooperation
develops.

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

## ipgn — Iranian Permanent GPS Network for Geodynamics (IR)

**status**:    weird
**date_added**: 2026-05-04
**country**:   IR
**type**:      single-base (post-processing, no public NTRIP RTK)
**host:port**: n/a — no public NTRIP RTK caster operates under the IPGN name; NCC's
               real-time correction service is the separate Hoda Pro caster (see
               `hodapro_ir`)
**access**:    raw RINEX archived to IGS for scientific post-processing
**registration**: `ipgn.ncc.gov.ir/en/accounts/signup/` (account portal; reachable
                  externally but issues no public NTRIP RTK credentials)
**yearly_cost**: n/a (not an RTK service)
**stations**:  ~127 physical CORS (phase 1: 2004–2006, 106 stations; phase 2: completed
               2013, 127 stations in ITRF2014)
**operator**:  National Cartographic Center of Iran (سازمان نقشه‌برداری کشور / NCC),
               `ncc.gov.ir`

Iranian Permanent GPS Network for Geodynamics: established post-2003 Bam earthquake
for tectonic monitoring, velocity and strain-field estimation. Base network covers
Zagros Mountains, Central Iran, Alborz, East Iran, Makran, Loot, and Kopeh-Dagh; three
local sub-networks. Data archived to IGS for scientific post-processing.

The IPGN station infrastructure feeds NCC's real-time correction product, branded
**Hoda Pro** (`hodapro.ncc.gov.ir`) and sold as a paid subscription via
`eshop.ncc.gov.ir` — documented separately in `hodapro_ir`. The IPGN itself does not
operate a public NTRIP RTK caster of its own.

**missing**: confirmation that hobbyist-grade RINEX downloads from `ipgn.ncc.gov.ir`
work without an IGS-class research affiliation; confirmation of what (if anything)
the IPGN sign-up portal issues to non-research applicants.

---

## hodapro_ir — Hoda Pro (IR)

**status**:    weird
**date_added**: 2026-05-04
**country**:   IR
**type**:      physical-coord-vrs (RTK / Network-RTK; built on the IPGN station network)
**host:port**: `hodapro.ncc.gov.ir:2101` (domain indexed and named in NCC material;
               directly unreachable from outside Iran, sourcetable not externally
               verified)
**access**:    paid subscription, sold via `eshop.ncc.gov.ir`; sign-up requires
               Iranian national ID and Iranian banking; the e-shop is firewall-blocked
               from outside Iran
**registration**: `eshop.ncc.gov.ir` (NCC e-shop; login required)
**yearly_cost**: not publicly listed — subscription tiers from daily through annual
                 are documented in NCC announcement material, but specific rates are
                 not exposed on any externally reachable page
**stations**:  built on the IPGN station infrastructure (~127 CORS, see `ipgn`)
**operator**:  National Cartographic Center of Iran (سازمان نقشه‌برداری کشور / NCC),
               `ncc.gov.ir`

Hoda Pro (سامانه ملی هدی پرو) is the RTK / Network-RTK arm of NCC's national
positioning programme, sitting above the legacy DGPS-only HODA service
(`hoda.ncc.gov.ir`, out of project scope). Distinct product from the IPGN
geodynamics network (`ipgn`), which is post-processing only and shares the
underlying CORS sites.

Classified `weird` rather than `paid` because the subscription portal and rate card
are firewall-blocked from outside Iran, so we cannot supply a verifiable
`yearly_cost` figure and cannot confirm whether unaffiliated Iranian individuals
can complete registration. Foreign hobbyists or residents have no documented
sign-up path. Not in the ingestion pipeline.

**missing**: actual subscription rates; confirmation of whether registration is
open to Iranian individuals without a licensed-surveyor credential.

---

## shamim_ir — SHAMIM (IR)

**status**:    restricted
**date_added**: 2026-05-04
**country**:   IR
**type**:      physical-coord-vrs (Geo++ GNSMART backend; 144 stations)
**host:port**: SHAMIM `178.252.173.15:2101`; SHAMIM Plus `178.252.173.75:2101`
               (the two tiers are documented in Persian practitioner material;
               externally unreachable, sourcetable not directly verified)
**access**:    cadastre-licensed surveyors only — registration requires Iranian
               national ID (کد ملی), Iranian mobile number for OTP, and registration
               of a specific GNSS receiver's serial number against the user's account;
               no documented path for general hobbyists or non-cadastre users
**registration**: `shamim.ssaa.ir` (Organisation for Registration of Deeds and
                  Properties / سازمان ثبت اسناد و املاک کشور)
**yearly_cost**: free of charge for qualified users (cadastre programme funded);
                 not a fee gate
**stations**:  144 physical permanent GNSS stations nationwide (installed 2016–2017)
**operator**:  Organisation for Registration of Deeds and Properties
               (سازمان ثبت اسناد و املاک کشور, `ssaa.ir`)

SHAMIM (شمیم — abbreviation for شبکه موقعیت‌یابی یکپارچه مالکیت‌ها, Integrated Unified
Property Management Network) is the national cadastral CORS network operated by Iran's
property registration authority. Geo++ GNSMART backend; supports Nearest, VRS, FKP,
MAX, and IMAX virtual reference modes; the original SHAMIM caster and an expanded
SHAMIM Plus tier run on neighbouring IPs. Designed to accelerate the national cadastre
programme.

Restricted rather than free at the marker level: although there is no subscription
fee, registration is documented only for users with a professional cadastre-programme
connection (licensed cadastral surveyors, SSAA-outsourced operators), with each
account bound to an approved receiver's serial number. No mechanism is described
for an unaffiliated hobbyist — Iranian or otherwise — to obtain credentials.
Endpoints unreachable from outside Iran at the firewall level; not in the ingestion
pipeline.

---

## rgna_mx — Red Geodésica Nacional Activa (MX)

**status**:    weird
**date_added**: 2026-05-01
**country**:   MX
**type**:      physical single-base (~36 stations)
**host:port**: n/a — RINEX/post-processing only; no NTRIP caster
**access**:    RINEX files freely downloadable via SFTP at `geodesia.inegi.org.mx`
               (migration from FTP effective Oct 2024); no RTK/NTRIP streaming offered
**registration**: https://inegi.org.mx/temas/geodesia_activa/ (RINEX download)
**yearly_cost**: n/a
**stations**:  ~36 permanent GNSS stations distributed nationally (CALE2025 coordinate catalogue)
**operator**:  INEGI — Instituto Nacional de Estadística y Geografía (`inegi.org.mx`)

The RGNA is Mexico's national active geodetic reference network under INEGI, contributing
to SIRGAS and IGS. INEGI's current English-language documentation (confirmed 2026-05-01)
explicitly states no real-time RTK/NTRIP streaming is offered — data are RINEX files at
15-second intervals, available free without registration. A 2013 SIRGAS bulletin discussed
NTRIP aspirations; these were not implemented. Rejected: RINEX/PPK only.

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

**status**:    weird
**date_added**: 2026-05-01
**country**:   CL
**type**:      physical single-base (180+ CORS stations)
**host:port**: `ntrip.igm.cl:2101` — connection refused (2026-05-01); IGM NTRIP
               sub-pages returning HTTP 500; no working public endpoint confirmed
**access**:    RINEX free via `sirgaschile.cl`; real-time NTRIP unconfirmed —
               ArduSimple (2025) describes the network as CORS/PPK only; IGM
               announced NTRIP in 2025 (procedure: youtube.com/watch?v=4yuH1W05eII)
**registration**: `sirgaschile.cl` (coordinate certificates and RINEX); NTRIP streaming
                  registration not self-service
**yearly_cost**: RINEX free; streaming terms not publicly documented
**stations**:  180+ CORS stations; expanded by 28 new first-level stations announced 2025
**operator**:  IGM — Instituto Geográfico Militar de Chile (`igm.cl`, `sirgaschile.cl`)

SIRGAS-CHILE is Chile's national geodetic reference network under the army's IGM. Consists
entirely of CORS stations covering the national territory from Arica to Punta Arenas. In 2025
IGM launched a renovated sirgaschile.cl platform and announced real-time NTRIP streaming
services alongside the existing RINEX download and online post-processing (PPP) tools.
No public self-service registration portal or working host:port for the NTRIP caster has
been found. `ntrip.igm.cl:2101` returns connection refused and IGM's NTRIP sub-pages
return HTTP 500 (confirmed 2026-05-01). ArduSimple (2025) describes the network as
CORS/PPK only. Not added to pipeline pending endpoint confirmation.

**missing**: confirm whether the 2025-announced NTRIP service is operational; check
sirgaschile.cl and igm.cl for a working caster address and registration pathway.

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

**status**:    free
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
**date_added**: 2026-05-01
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
PayPal payment integration; `gnssnigeria.com`, the apparent subscriber portal, is
unreachable as of 2026-05-01 (connection errors on all paths). `osgof.gov.ng` lists
"Requests for RTK CORS correction" as a service line but no endpoint or rate is
published (homepage and services page load; most recent news Oct 2025). No free
hobbyist NTRIP path identified.

**missing**: confirm whether a stable endpoint has been established at osgof.gov.ng
             or a replacement portal; `gnssnigeria.com` unreachable as of 2026-05-01;
             check if commercial providers (e.g. CHCNAV RTK network cited as
             operating in Nigeria) have established a hobbyist-accessible caster.

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
NTRIP endpoint. survey.go.ke was unreachable (error page) on 2026-04-30;
no subdomain (cors.survey.go.ke, gnss.go.ke) appears in any indexed source.
KeRRA tender documents (2025–2026) reference SoK datum but cite no NTRIP
endpoint. Government CORS access, if any, appears to be via institutional
accounts only.

## muya_cors_ke — Muya CORS (KE)

**status**:    paid
**date_added**: 2026-04-29
**country**:   KE
**type**:      physical single-base + network RTK
**host:port**: host:port disclosed post-registration (IP, port, username,
               password issued after signup at `muya-cors.com`)
**access**:    paid with registration; self-serve signup via muya-cors.com;
               Mpesa payment supported
**yearly_cost**: KES 35,000/yr (~$271/yr)
**stations**:  ~27 base stations across Kenya (single-base and networked RTK)
**operator**:  Measurement Systems Ltd (`measurementsystems.org`),
               operating as Muya CORS (`muya-cors.com`)
**source**:    muya-cors.com; measurementsystems.org; ardusimple.com;
               georole.co.ke; orbital.co.ke (field use report, Sep 2024);
               instagram.com/measurementsystemsltd (price, 2026-04-30)

Muya CORS provides RTK corrections and post-processing services via a
network of GNSS CORS tracking GPS, GLONASS, BeiDou, and Galileo. Credentials
are issued post-registration. KES 35,000/yr (~$271 at 2026-04-30 rate) is
from a Measurement Systems Ltd promotional post (Instagram, 2026-04-30);
no primary price sheet confirmed. Mpesa payment and individual registration
confirmed — no surveying licence requirement found. Operationally active as
of January 2026 (social media) and Google Play app updated October 2025.
Over the $200/yr threshold — excluded from pipeline. Only commercial RTK
NTRIP option confirmed for Kenya.

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

**status**:    weird
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

---

## regme_ec — REGME-IP (EC)

**status**:    free
**date_added**: 2026-05-01
**country**:   EC — Ecuador
**type**:      single-base
**host:port**: `ntrip.igm.gob.ec:2101`
**access**:    free with registration; no stated residency restriction; open to all
**registration**: https://www.geoportaligm.gob.ec/ntrip/
**stations**:  not published (military geodetic network)
**operator**:  IGM — Instituto Geográfico Militar del Ecuador (`igm.gob.ec`)

REGME-IP (Red GNSS Militar Ecuatoriana de Posicionamiento en Tiempo Real) is Ecuador's
national free NTRIP RTK correction service, operated by the army's mapping institute.
Stated as "totalmente libre y gratuito" (entirely free). Registration required via the
geoportal; no residency restriction stated on the registration page. SIRGAS bulletin
(2022) explicitly names `ntrip.igm` listening on port 2101. Geoportal and visor
(`geoportaligm.gob.ec/ntrip/public/visor`) confirmed reachable 2026-05-01.
Zero ECU mountpoints currently on rtk2go; in-pipeline candidate.

**missing**: verify sourcetable contents and mountpoint names at `ntrip.igm.gob.ec:2101`;
confirm station count and geographic distribution.
