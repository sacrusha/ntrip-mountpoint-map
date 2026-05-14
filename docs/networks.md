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
**date_added**: 2026-05-13
**country**:   global (France-centric); ~40 country/territory codes in sourcetable
**operator**:  Centipede-RTK association (non-profit, formed Aug 2024); historically INRAE
**host:port**: `crtk.net:2101` (canonical since 2025-03-18); old `caster.centipede.fr:2101` resolves but redirect not guaranteed indefinitely
**type**:      single-base
**access**:    free, no registration (username = `centipede` or `c`; password same; or anonymous);
               1 device per IP address
**pipeline-access**: open
**stations**:  1,205 STR records (sourcetable 2026-05-13). Top territories by node count:
               France 709 (`FRA`), Hungary 217 (`HUN`), **United Kingdom ~45 (`ENG` —
               covers all of GB + Northern Ireland; *not* just England)**, Switzerland 30
               (`CHZ` — *not* Czech; Czech Republic uses `CZE` separately, 3 nodes),
               Netherlands 26 (`NLD`), Norway 21 (`NOR`; Svalbard separate as `SJM`),
               Canada 19 (`CAN`), Finland mainland 18 (`FIN`; Åland separate as `ALA`),
               **Denmark ~18 (`DAN` 10 + `DNK` 8 — both codes in parallel)**,
               Belgium 17 (`BEL`), **Serbia ~14 (`SER` 11 + `SRB` 3 in parallel)**,
               **Romania 9 (`ROM` 7 + `ROU` 2 in parallel)**, Czech Republic 3 (`CZE`).
**source**:    centipede-rtk.org; map.centipede-rtk.org
**caster_software**: Millipede (open-source, BSD-3, by Pierre Beyssac); ~50× capacity vs legacy
**last_researched_date**: 2026-05-13

Volunteer network initiated by INRAE (2019); now operated by non-profit
Centipede-RTK association. Migrated from `caster.centipede.fr` to
`crtk.net` on 2025-03-18 22:17 Paris time. `NEAR` mountpoint auto-routes
rover to the nearest base (RTCM3 MSM7); `NEAR4` is the lower-bandwidth
MSM4 variant for older receivers. Single federation endpoint; no separate
country-specific instances. Since June 2023, ~30 RENAG (Réseau National
GNSS Permanent) scientific stations are re-distributed through Centipede,
strengthening southeastern France coverage.

**Country-code legend caveat**: Centipede's sourcetable field-9 country
column does not consistently follow ISO 3166-1 alpha-3. `CHZ`, `ENG`,
`DAN`, `ROM`, and `SER` are non-ISO; `DAN`/`DNK`, `ROM`/`ROU`, and
`SER`/`SRB` are used in parallel and must be summed when counting per
country. See `docs/ntrip_research/_centipede_country_codes.md` for the
authoritative legend; per-country research files cite it.

---

## frednet — FReDNet (IT — Friuli-Venezia Giulia + adjacent Veneto/Lombardia)

**status**:    free
**date_added**: 2026-05-13
**host:port**: `158.110.30.81:2110`
**type**:      physical-coord-vrs
**access**:    free; account via operator portal; "public, private and scientific users"
**pipeline-access**: registration
**registration**: https://frednet.crs.ogs.it/en/servizio-rtk/
**stations**:  22 RTK-active (24 listed; LODI and UDIN have RTK off). Codes: ACOM, AFAL, CANV, CODR, FUSE, GRDO, JOAN, LOGA, MDEA, MGBU, MPRA, NOVE, PAZO, PMNT, SUSE, TOLS, TRIE, UDI1, UDI2, VALS, VARM, ZOUF.
**vrs**:       yes (`OGS_VRS`, `OGS_NEA` nearest-station, `OGS_FKP` network solution, single-station, DGPS)
**source**:    frednet.crs.ogs.it
**operator**:  OGS — Istituto Nazionale di Oceanografia e di Geofisica Sperimentale (CRS Udine)
**last_researched_date**: 2026-05-13

OGS-CRS crustal-deformation network operating since 2002; node in EPOS /
GLASS and the PNRR MEET project. Coverage is FVG plus adjacent Veneto
(CANV, SUSE, NOVE, MGBU, AFAL) and one Lombardy outlier (LODI). Station
spacing ~30–50 km — built for geodynamic monitoring of the Adria
microplate, not RTK density. RTK streams GPS+GLONASS RTCM 3.x; note
non-standard port 2110. ETRF2000(2008.0) reference frame. The caster also
cross-relays a subset of Re.M.FVG/Marussi physical stations under
`RAFVG_*` codes. Contact gnss@ogs.it.

Not currently in the `fetch_stations.py` SOURCES — `data/frednet.sourcetable`
is the Marussi caster output (see `rem_fvg` block below), not this network.
A separate SOURCES entry for FReDNet is optional: cross-relay means a
Marussi-anchored ingest already surfaces OGS coverage geometrically.

---

## rem_fvg — Re.M.FVG "A. Marussi" (IT — Friuli-Venezia Giulia + SI/AT border via relays)

**status**:    free
**date_added**: 2026-05-13
**host:port**: `gnsscaster.regione.fvg.it:8080`
**type**:      physical-coord-vrs
**access**:    sourcetable open; stream requires free registration form on Re.M.FVG portal
**pipeline-access**: registration
**registration**: https://rem.regione.fvg.it/rem-fvg/servizi/correzioni-differenziali
**stations**:  14 own physical (Ampezzo, Barcis, Bevazzana, Cervignano, Codroipo, Gorizia, MoggioUdinese, Paularo, Pordenone, Sappada, Tarvisio, Trieste, Udine) + 3 Slovenian SIGNAL relays (Bovec, Idrija, Koper). Sourcetable also cross-relays 11 `OGS_*` mounts from FReDNet.
**vrs**:       yes (VRS_RTCM23/31/32 quad-constellation GPS+GLO+GAL+BDS, MAC, IMAC, plus DGPS)
**source**:    rem.regione.fvg.it; regione.fvg.it
**operator**:  Regione Autonoma Friuli-Venezia Giulia
**last_researched_date**: 2026-05-13

Regional FVG positioning service operated by the Regione. Founded 1999,
opened to private users 2005, VRS since 2007, GPS+GLO+GAL since 2012/2019.
2024–2025 receiver refresh added BEIDOU plus two new stations (Sappada,
Paularo); Slovenian SIGNAL stations integrated at the border. Leica GNSS
Spider 7.11. ETRS89 / ETRF2000(2008.0). Free for everyone after a one-form
registration, no professional or residency gate. Cross-relays a subset of
FReDNet stations under `OGS_*` codes — geometric FVG coverage is the union
of the two networks.

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
**date_added**: 2026-05-13
**country**:   AU — Australia
**operator**:  Geoscience Australia
**host:port**: `ntrip.data.gnss.ga.gov.au:443` (TLS, primary); `:2101` plain TCP fallback
**type**:      single-base
**access**:    free; register at gnss.ga.gov.au/registration; CC BY 4.0
**pipeline-access**: registration
**registration**: https://gnss.ga.gov.au/registration
**stations**:  914 (sourcetable 2026-05-06)
**vrs**:       no
**signals**:   RTCM 3.3 MSM; GPS+GLO+GAL+BDS+QZS on most stations
**licence**:   CC BY 4.0
**pipeline-flags**: `solution_filter=False` (~42 IGS/international partner stations
                    re-streamed by AUSCORS are tagged solution=1 in the sourcetable
                    despite being physical receivers with fixed coordinates, e.g.
                    KIRU00SWE0 in Sweden, ENAO00PRT0 in the Azores)
**last_researched_date**: 2026-05-12

Geoscience Australia's national NTRIP service. Port 443 (TLS / NTRIP v2.0)
is the primary endpoint; port 2101 (plain NTRIP v1.0) remains live as a
fallback for older clients lacking TLS support. Mountpoint convention
`<STA4>00AUS0` (e.g. `ALIC00AUS0` Alice Springs, `SYDN00AUS0` Sydney).
Coverage is nationwide including WA interior, NT, and QLD outback; sparse
in the interior, dense (~100+ stations) along populated coasts. Old host
`auscors.ga.gov.au` dead since Jul 2022. Attribute "© Commonwealth of
Australia (Geoscience Australia)".

State/territory VRS networks are paid via commercial resellers and do not
expose a hobbyist tier: NSW CORSnet-NSW (Spatial NSW), VIC Vicmap Position
/ GPSnet (VAR-only since Jan 2019), WA Landgate CORS (2024-25 ~3% fee
increase), SA CORS (DHUD) — some free single-base via AUSCORS, paid VRS
via commercial — and QLD/TAS/NT/ACT through HxGN SmartNet Aus, Topnet,
AllDayRTK, Positioned RTK. AUSCORS is the practical zero-cost path for
hobbyists.

Volunteer supplement: 24 AUS-coded rtk2go bases + 3 Centipede nodes (CADA
in QLD, FARM48 NSW/VIC border, plus one more) per `stations_by_country.py
AUS` 2026-05-12.

---

## positionz — PositioNZ-RT (NZ)

**status**:    free
**date_added**: 2026-05-06
**host:port**: `positionz-rt.linz.govt.nz:2101`
**type**:      single-base
**access**:    free; LINZ account required; register via linz.govt.nz; CC BY 4.0 NZ
**pipeline-access**: registration
**stations**:  37 (CORS throughout NZ mainland, Chatham Islands, and Antarctica/Scott Base)
**source**:    linz.govt.nz; geonet.org.nz (stream management)
**operator**:  LINZ — Land Information New Zealand (Toitū Te Whenua)
**licence**:   CC BY 4.0 NZ

Single-base only (no VRS); raw 1 Hz RTCM 3.1 observations; recommended use within
15 km of connected station. Streaming latency reduced ~50–90% after BKG NtripCaster
software deployment. Attribute "Source: Land Information New Zealand".

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
**date_added**: 2026-05-13
**country**:   BR — Brazil
**operator**:  IBGE — Instituto Brasileiro de Geografia e Estatística
**host:port**: `gps-ntrip.ibge.gov.br:2101` (alt IP `170.84.40.52:2101`)
**type**:      single-base
**access**:    free; gov.br signup; 5-station limit per user; 1,000 concurrent max
**pipeline-access**: registration
**registration**: https://www.gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip
**stations**:  ~150 (149 STR in sourcetable 2026-05-12); 5 stations inaugurated
               Dec 2024 (Governador Valadares MG, Maceió AL, Januária MG, Pinhais PR,
               Nova Friburgo RJ); IBGE planned 2 more in 2025 (Lins/SP, Rosana/SP)
**reference_frame**: SIRGAS2000 (ITRF-compatible)
**last_researched_date**: 2026-05-12

National caster from IBGE; coverage spans all 26 states + DF, densest in
south/south-east (SP, MG, RJ, PR, RS); sparse in Amazon basin and
north-eastern interior. ~19 BR-coded rtk2go bases concentrate in SP metro
and southern states; small Centipede footprint.

Commercial alternatives include **geoRTK** (launched 1 Sep 2025; R$10/day,
R$79/wk, R$219/mo, R$2,099/yr; 30-day free trial; claims largest BR
RTK/PPK network with 500-station goal by 2026), **GeoPlus** (PPP-RTK +
NTRIP, contact-only), **RoverConnect / CPE Tecnologia** (single-base,
weekly prepaid), **RTKdata** (USD 40/mo, intl), and **TopNET Live**
(subscription, BR-specific nodes unconfirmed). All rely partly on RBMC-IP
stations re-streamed or augmented; independent verification of Amazon
coverage is not possible remotely. State geodetic offices (SP IGC, BA DGC,
MG, RJ) contribute stations to RBMC-IP rather than running independent
casters.

---

## ramsac — RAMSAC-NTRIP (AR)

**status**:    free
**date_added**: 2026-05-13
**country**:   AR — Argentina
**operator**:  IGN — Instituto Geográfico Nacional (Argentina)
**host:port**: `ntrip.ign.gob.ar:2101`
**type**:      single-base
**access**:    free; register via ign.gob.ar portal; 8-hr session cap, re-authentication required
**pipeline-access**: registration
**registration**: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro
**stations**:  ~203 (sourcetable 2026-05-12); modernisation programme expanded from 154 to ~204
**reference_frame**: POSGAR 07 (SIRGAS / ITRF compatible)
**last_researched_date**: 2026-05-12

Established 2010 by IGN with contributions from national/provincial cadastral
offices, universities, and private operators; originally ~69 stations.
Coverage spans all 23 provinces plus CABA, densest in Buenos Aires, Córdoba,
Santa Fe, Mendoza. Patagonia (La Pampa, Chubut, Santa Cruz, Tierra del
Fuego) remains sparse due to connectivity constraints; IGN has announced
plans to add stations as cellular/satellite links improve. Single-base only
(no VRS); hobbyist clients must select the nearest mountpoint manually.

Volunteer supplement: 6 AR-coded rtk2go bases (CASISA, LACU-COR-ARGENTINA,
MPBSAS001, PGDB-Arrias, PGDB-Luque, PRNAMEI) — mostly Córdoba province plus
1 Buenos Aires metro and 1 Entre Ríos. Zero AR-coded Centipede nodes.
Commercial alternatives (RTKArg, Trimble RTX, HxGN SmartNet+, TopNET Live)
require vendor-direct contact; no published AR-specific pricing.

---

## regna_rou — REGNA-ROU (UY)

**status**:    free
**host:port**: `rtk.igm.gub.uy:2101`
**type**:      physical-coord-vrs
**access**:    free; web registration at rtk.igm.gub.uy/SBC/Account/Register
**pipeline-access**: registration
**stations**:  ~35 unique physical (live sourcetable 2026-05-13: 96 STR rows after format-variant dedup)
**vrs**:       yes (15 zone VRS A–Z + `RTCM3-VRS` + `RTCM3-iMAX`)
**source**:    igm.gub.uy
**operator**:  IGM — Instituto Geográfico Militar (Uruguay)
**last_researched_date**: 2026-05-13

Uruguay IGM (Instituto Geográfico Militar). "El Servicio no tiene costo."
SIRGAS-ROU reference frame (ITRF-compatible). 1,000+ registered users as of 2025.
Expanded Dec 2025 with 8 new SinoGNSS M300 Pro CORS stations (multi-constellation
GPS+GLO+GAL+BDS via `UY**_MSM4` MSM4 mountpoints — Tacuarembó, Rivera, Artigas,
Durazno, Flores interior densification); older stations still RTCM 3 GPS+GLO only.
Leica GNSS Spider 7.11.1.109 caster. 1–2 cm horizontal with dual-frequency receiver.
Spanish-language portal is the main access friction for non-Spanish speakers; no
documented case of foreign-resident registration being rejected. Cross-border RAMSAC
(AR) stations near Colón/Concordia/Monte Caseros provide partial fallback at
sub-50 km baselines.

---

## regme_ec — REGME-IP (EC)

**status**:    free
**date_added**: 2026-05-01
**last_researched_date**: 2026-05-12
**country**:   EC — Ecuador
**type**:      single-base
**host:port**: `ntrip.igm.gob.ec:2101`
**access**:    free with registration; no stated residency restriction; service
               described as extending to "national and international" users
**registration**: https://www.geoportaligm.gob.ec/ntrip/public/register
**stations**:  26 physical CORS (live sourcetable 2026-05-12; nationwide
               coverage — Alausi, Ambato, Babahoyo, Chaco, Cotopaxi, Cuenca,
               El Carmen, Esmeraldas, ESPE, Francisco de Orellana, Guayaquil,
               Lago Agrio, Loja, Macas, Machala, Naranjal, Pajan, Pimampiro,
               Piñas, Portoviejo, Posorja, Quevedo, Quito, Riobamba, Santa
               Elena, Santa Isabel)
**operator**:  IGM — Instituto Geográfico Militar del Ecuador (`igm.gob.ec`)

REGME-IP (Red GNSS Ecuatoriana de Posicionamiento en tiempo real protocol IP) is
Ecuador's national free NTRIP RTK correction service, operated by IGM (the army's
mapping institute). Single unified national domain `ntrip.igm.gob.ec` introduced
February 2024; main server at IGM Quito with backup at ESPOCH Riobamba; 365 days/year
with technical support Mon–Fri 07:30–16:30. Stated as "totalmente libre y gratuito".
Live sourcetable 2026-05-12 carries 26 single-station mountpoints (each formatted
`<Town>-<CODE>-IGM`); no VRS/MAC/FKP rows — nearest-station model only, rovers
must pick the closest mount manually. RTCM 3 multi-GNSS (GPS+GLO+GAL+BDS+QZS+SBAS).
Caster SNIP simpleNTRIP_Caster [wPRO] R3.19.00. Zero ECU mountpoints on rtk2go
or Centipede.

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
**date_added**: 2026-05-08
**host:port**: Network 1 (GNSS Data Center): `www.gnssdata.or.kr:2101`
               Network 2 (NGII VRS/FKP): `vrs3.ngii.go.kr:2101`; FKP: `fkp.ngii.go.kr:2201`
**type**:      single-base
**access**:    Network 1: free; email registration at gnssdata.or.kr; NTRIP password =
               literal `gnss` (NOT the portal login password); no Korean national ID
               required; SOURCETABLE 200 OK 2026-05-08, 546 STR rows, 167 unique
               physical stations. Network 2 (NGII VRS): Korean government
               PASS/mobile-identity verification required — practical barrier for
               non-residents.
**pipeline-access**: registration
**stations**:  167 physical stations (Network 1 sourcetable, 8 contributing agencies:
               KORREF/NGII 94 rows, Single Base 433 rows, SMG/Seoul 10 rows;
               pipeline parser yields 493 distinct mountpoints after format-variant
               de-dup)
**source**:    gnssdata.or.kr (Network 1); ngii.go.kr (Network 2)
**operator**:  GNSS Data Center (federation of 8 Korean agencies — NGII, KASI, SMG,
               KMA, etc., Network 1); NGII — National Geographic Information
               Institute, Ministry of Land (Network 2)

Pipeline source (`cors_korea`) fetches Network 1 (`www.gnssdata.or.kr:2101`). Network 1
is the public hobbyist endpoint: email registration only, shared NTRIP password `gnss`.
Network 2 is the NGII direct VRS/FKP service requiring Korean government ID.
Seoul City supplementary network at `gnss.eseoul.go.kr` (separate registration,
same Korean-ID gate).

**Republication posture (2026-05-08)**: keep listing. The Korean-ID/PASS gate
applies to the real-time correction stream, not to station-coordinate metadata.
The same physical stations exposed in our ingested sourcetable are also
republished openly: flagship NGII stations SUWN and DAEJ are IGS members with
full site logs and coordinates at `network.igs.org/SUWN00KOR` and
`network.igs.org/DAEJ00KOR` (HTTP 200 verified 2026-05-08). The Network 1
sourcetable itself is anonymously fetchable from `www.gnssdata.or.kr:2101` (no
auth required to list mountpoints + base coordinates) — only the correction
stream is gated. Republishing mountpoint names and coarse station coordinates
does not exceed what NGII contributes openly to IGS. The existing
`pipeline-access: registration` flag and popup note already make the
foreigner-registration barrier visible to the user; that is the correct level
of disclosure. Cross-reference: SiReNT (`sirent`) is the project's precedent
for *not* republishing — but that operator (SLA, Singapore) gates the entire
service behind a paid subscription with no anonymous sourcetable, hence
country-marker-only treatment. NGII is a different shape: free service, gate is
on stream auth not on metadata.

---

## In-pipeline — physical-coord VRS

Sourcetable exposes real antenna locations; rover connects via VRS mountpoints.
Map shows physical station pins.

---

## ergnss — ERGNSS (ES)

**status**:    free
**date_added**: 2026-05-13
**country**:   ES — Spain (mainland + Balearics + Canaries via SPTR sub-service)
**operator**:  IGN España — Instituto Geográfico Nacional
**host:port**: `ergnss-ip.ign.es:2101` (data-only caster, mainland + Balearics; IP 193.144.251.13);
               `ergnss-tr.ign.es:2101` (network solutions VRS/MAC/FKP, IP 192.148.213.42);
               `ergnss-tr.ign.es:2102` (single-station)
**type**:      physical-coord-vrs
**access**:    free; register at ergnss.ign.es/gnuserportal/ (immediate); CC-compatible;
               max 10 simultaneous connections per account; ~12,000 registered users as of Jan 2024 (~60% agricultural sector)
**pipeline-access**: registration
**registration**: http://ergnss.ign.es/gnuserportal/
**stations**:  272 total (IGN permanent + 13 regional autonomous community networks + Puertos
               del Estado tide gauges; latest expansion adds PNAV, ARAJ, HOND per Jun 2025
               transportes.gob.es presentation); 17 processing subnets
**vrs**:       yes — VRS3M, MAC3M, FKP3M, CERCANA3M (RTCM 3.2 MSM); legacy VRS3, MAC3, FKP3, CERCANA3
**signals**:   GPS+GLO+GAL+BDS
**licence**:   Attribution required per Orden FOM/2807/2015
**last_researched_date**: 2026-05-12

National free service operated by IGN España. Canary Islands served by SPTR
sub-system at `ergnss-tr.ign.es`; recommended mountpoint `CERCANA3M`
(nearest-station mode, RTCM 3.2 MSM4, automatic failover) — VRS network-RTK
solutions less reliable over archipelago geometry. REGCAN95 coordinate
update for all Canaries stations: 2024-02-01. Sourcetable retrieved live
from `ergnss-tr.ign.es:2101` 2026-05-12: 8 STR rows (CERCANA3, CERCANA3M,
FKP3, FKP3M, MAC3, MAC3M, VRS3, VRS3M; `Server: NTRIP GNSMART_Caster 2.0/1.0`).
**Pipeline note**: the SPTR `:2101` sourcetable is VRS-only (all mounts at
0.00/0.00); physical Canary Islands stations come via the data-only caster
`ergnss-ip.ign.es:2101` (id: `ergnss`). The `ergnss_sptr` SOURCES entry is
therefore `type: vrs-only` and yields 0 physical pins; the VRS ring is driven
by the `ergnss` country marker.

Regional autonomous-community networks integrated into ERGNSS (single
IGN registration covers all): ARAGEA (Aragón), ERVA (Valencia), ITACYL
(Castilla y León), RAP (Andalucía), REGAM (Murcia), REP (Extremadura), RGAC
(Cantabria), RGAN (Navarra), RGAPA (Asturias — open access, no auth), RGE
(Basque Country), RGM (Madrid), RIOJA (La Rioja), XGAIB (Balearics), Puertos
del Estado. **CATNET** (Catalonia, ICGC) is separate — own caster
`catnet-ip.icgc.cat:2101` with own registration; sourcetable retrieved 2026-05-12
(VRS3M MSM + ~25 single-station legacy RTCM 2 mountpoints).

---

## satref — SatRef (HK)

**status**:    free
**date_added**: 2026-05-13
**country**:   HK — Hong Kong SAR
**last_researched_date**: 2026-05-12
**host:port**: `ntrip.geodetic.gov.hk:2101`
**type**:      single-base
**access**:    free; application by email/form to Survey and Mapping Office (geodetic.gov.hk);
               no professional licence required; no residency restriction
**pipeline-access**: registration
**stations**:  19 (16 reference + 3 integrity monitoring; TCHK under maintenance since Aug 2025)
**source**:    geodetic.gov.hk (Lands Department, Survey & Mapping Office)
**operator**:  Lands Department, Survey and Mapping Office (SMO), HKSAR Government
**licence**:   Open data (commercial and non-commercial reuse permitted)

Launched Jun 2007. 18 single-base RTCM 3.2 MSM5 streams (GPS+GLO+GAL+BDS+QZSS) in
the public sourcetable (21 STR rows total, including 3 NMEA Integrity Monitoring streams);
station mounts named `HKxx_32` / `T430_32`. VRS/Network RTK is a separate credentialed
product not exposed in the public sourcetable. Confirmed alive 2026-05-12 (SOURCETABLE
200 OK, 21 STR rows). Domain migrated to `ntrip.geodetic.gov.hk` from 1 June 2023;
old `www.geodetic.gov.hk` NTRIP endpoint decommissioned. Accounts inactive 12+ months
are terminated. Raw TCP (NTRIP 1.0) fallback required in fetcher.

---

## mosref — MoSRef (MO)

**status**:    free
**host:port**: `mosref.dscc.gov.mo:2101`
**type**:      physical-coord-vrs
**access**:    free; register at mosref.dscc.gov.mo; no professional credentials required;
               no Macao residency required
**pipeline-access**: registration
**stations**:  4 (FOMO — Macao Peninsula 2002; COAL — Coloane 2006; UMAC — Hengqin Island 2016;
               TAGR — Taipa Grande 2023); 4 HK partner stations extend VRS coverage
**operator**:  DSCC — Direcção dos Serviços de Cartografia e Cadastro (Cartography and Cadastre
               Bureau), Government of the Macao SAR
**source**:    dscc.gov.mo; mosref.dscc.gov.mo
**signals**:   GPS + GLONASS + BeiDou (BDS added 2021); recording interval 10 s; RINEX v3.02

**date_added**: 2026-05-06

MoSRef (Macao Satellite Positioning Reference Station Service) provides free NTRIP RTK
(single-base and VRS / Network RTK), RINEX download (up to 3 months), and coordinate
auto-computation. NTRIP introduced November 2012; BDS support added 2021. The four Macao
stations are backed by Leica GR50 receivers; four HK partner stations (HKLT, HKSL, HKMW,
HKNP) are included via a data-sharing agreement (since 2013), extending VRS coverage across
the Pearl River Delta. Portal: mosref.dscc.gov.mo. DSCC states: "DSCC provides … the
all-weather NTRIP RTK service to public for free of charge." Registration via online form;
no supporting documents required. Standard NTRIP v1/v2 clients compatible.

**missing**: confirm sourcetable response and mountpoint list from `mosref.dscc.gov.mo:2101`;
verify whether sandbox IP range is blocked (government caster may restrict non-Macao IPs).

---

## inacors — InaCORS (ID)

**status**:    free
**date_added**: 2026-05-13
**country**:   ID — Indonesia
**last_researched_date**: 2026-05-12
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
**date_added**: 2026-05-13
**country**:   CO — Colombia
**operator**:  IGAC — Instituto Geográfico Agustín Codazzi (Centro de Control Geodésico Nacional)
**host:port**: `sbc.igac.gov.co:2102` — 143 single-base `<CODE>_RTCM3` mountpoints,
               **137 unique exact lat/lon pairs** (canonical dedup; six coord-collisions
               where one site exposes 2–3 mountpoints).
               `sbc.igac.gov.co:2101` — 20 VRS/network mounts (MSM_VIRS, MSM_IMAX, MSM_NEAR,
               legacy RTCM3/RTCM2/CMR variants, regional cells LLANOS_RTCM3 /
               SUR_OESTE_RTCM3 / NOROESTE_RTCM3).
**type**:      physical-coord-vrs
**access**:    free; register at redgeodesica-sbc.igac.gov.co/sbc; Law 1955/2019 (PND Art. 281)
               mandates public access; Resolución IGAC 1771 de 2024 officialized the portal
**pipeline-access**: registration
**registration**: https://redgeodesica-sbc.igac.gov.co/sbc/Account/Register
**stations**:  143 STR / 137 unique exact lat/lon pairs on port 2102. Sourcetable
               byte-identical 2026-05-07 → 2026-05-13 (Content-Length 15621): no station
               additions or removals in that window. IGAC declares ~260 CORS in total
               (IGAC + SGC); the gap to 137 reflects post-processing-only stations and
               SGC GeoRED stations not piped into the RTK service.
**signals**:   GPS+GLO+GAL+BDS on MSM; GPS+GLO on most legacy RTCM3; GPS-only on RTCM2/DGPS
**licence**:   Law 1955/2019 (public access mandated)
**last_researched_date**: 2026-05-13

National Geodetic Control Centre launched Apr 2024 at SIRGAS conference;
26 stations added 2024 via Leica GR50/AR20 equipment; 39 added 2022–2024
(Cuatro Conceptos contract). Caster software Leica GNSS Spider 7.11.0.96.
Unusual in the region in being free + national + VRS together (other free
national casters in Latin America surveyed by this project — RAMSAC AR,
RBMC-IP BR, REGME-IP EC, IGN-CR — are single-base). ~67% of municipalities
covered as of 2023. Port 2101 exposes VRS/network mounts only (NEAR, iMAX,
VIRS) — zero physical pins after filtering. Physical-station mounts on
port 2102 are mislabelled `nmea=1` (Leica Spider default);
`nmea_filter=False` is set in the pipeline.

**Station-count reconciliation**: prior research recorded 124 (2026-05-07)
and 127 (2026-05-12) unique coords on port 2102; the 2026-05-13 canonical
recount returns 137. The sourcetable is byte-identical across all three
dates — the 124/127/137 drift is a **deduplication-method artefact**
(coordinate-rounding granularity), not real network growth. Canonical
method: `awk -F';' '/^STR/ {print $10","$11}' | sort -u | wc -l`.

Independent SGC GeoRED network (105+ stations) is post-processing only.
Zero CO rtk2go / Centipede.

---

## spslux — SPSLux (LU)

**status**:    free
**date_added**: 2026-05-06
**host:port**: `stream.spslux.lu:5005`
**type**:      physical-coord-vrs
**access**:    free; register at spslux.lu/SBC/Account/Register (subscribe "SPSLUX (N)RTK")
**pipeline-access**: registration
**stations**:  13 (some on international territory managed by partner networks)
**source**:    act.public.lu (ACT — Administration du Cadastre et de la Topographie)
**operator**:  ACT — Administration du Cadastre et de la Topographie

Port 5005, not 2101. IP 185.106.24.68. Luxembourg open-data policy — all services
free of charge. iMAX and VRS correction types; GPS, GLONASS, Galileo, BeiDou.
Accuracy ~2–3 cm horizontal, ~3–5 cm vertical. ETRS89/ITRF reference frame.

---

## icecors — IceCORS (IS)

**status**:    free
**date_added**: 2026-05-13
**country**:   IS — Iceland
**last_researched_date**: 2026-05-12
**host:port**: `178.19.53.126:2101`
**type**:      physical-coord-vrs
**access**:    free; registration required — contact `icecors@natt.is`
**pipeline-access**: registration
**stations**:  33 (~70–100 km spacing nationwide); 4 physical mounts exposed in sourcetable
               (AUSV, GEVK, SENG, VOGC — all Reykjanes peninsula); remaining 29 reachable
               via nearest-station selector (RTCM30/RTCM30_MSM) or VRS3/VRS3_MSM
**source**:    natt.is/is/landmaelingar/jardstodvakerfi; ggn01.lmi.is (registration portal still on LMÍ subdomain)
**operator**:  Náttúrufræðistofnun Íslands (Natural Science Institute of Iceland);
               geodetic functions transferred from LMÍ ~2024–2025

33 physical GNSS stations covering Iceland at 70–100 km intervals. Caster at
`178.19.53.126:2101` (Geo++ GNSMART software). VRS3 and VRS3_MSM network-solution
mountpoints available; nearest-station selectors RTCM30/RTCM30_MSM; 4 individual
physical mounts (Reykjanes cluster). ISN2016 (ITRF2014 epoch 2016.0).

GNSMART tags all mountpoints `NMEA=1` including the 4 single-base entries
(which have unique coordinates and `solution=0`). `nmea_filter=False` would be
needed to expose the 4 physical pins; pipeline currently holds at 0.
Confirmed alive 2026-05-12 (SOURCETABLE 200 OK, 12 STR rows; caster + ggn01.lmi.is
portal both alive). The natt.is service page (natt.is/is/maelingar/thjonustur/icecors)
returned 404 on 2026-05-12 — page removed during institutional consolidation; the
updated info page is natt.is/is/landmaelingar/jardstodvakerfi.

**Alternative free path for the IGS station REYK00ISL0 (Reykjavik)**:
also streamed real-time via the EUREF-IP federation on all three
broadcasters (BKG `euref-ip.net:2101`, ROB `www.euref-ip.be:2101`,
ASI `euref-ip.asi.it:2101`) under the same mountpoint name. Useful when
the IceCORS registration is gated or pipeline filtering hides the local
Reykjanes mounts. See `euref_ip`.

---

## almgg_mn — CORS Network / MonPOS (MN)

**status**:    free
**date_added**: 2026-04-29
**last_researched_date**: 2026-05-12
**country**:   MN — Mongolia
**type**:      physical-coord-vrs (Trimble NetR8/NetR9 hardware; `MGL_network`
               VRS mountpoint plus physical single-base mounts;
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

Initial 6-station CORS infrastructure delivered in December 2010 by ILS (International
Land Systems) under the Millennium Challenge Corporation Property Rights Project, with
Trimble NetR8 receivers. Used initially for cadastral surveys and GCPs covering ~75,000
property plots. Network has since grown to 40+ stations countrywide. A government
announcement at `monpos.gazar.gov.mn/monpos/3/` (retrieved 2026-04-30) confirms the VRS
mountpoint `MGL_network` at `rtk.gazar.gov.mn` with shared public credentials. Accuracy:
≤35 km baseline, ±(2 cm + 1 ppm), RTCM 3.x. Station map on monpos.gazar.gov.mn shows
mixed online/offline status. Web portal uses an outdated/self-signed TLS cert
(re-verified 2026-05-12) — sandbox WebFetch returned cert errors though the caster
itself is live in the pipeline. Mongolia is ~1.56 million km²; average inter-station
distance ~200 km — RTK practical only in the Ulaanbaatar–Darkhan–Erdenet corridor.
In pipeline as `almgg_mn` since 2026-04-30 (credentials `rover`/`262461`).
Zero MN mountpoints on rtk2go or Centipede.

---

## SAPOS — Germany (DE, 16 Bundesländer)

**status**:    free (14 of 16 states; BY €20/yr non-agri flat rate; RP €120/yr/credential)
**date_added**: 2026-05-13
**country**:   DE — Germany (16 Bundesländer)
**type**:      physical-coord-vrs (some states); single-coord-vrs (others — 0 map stations)
**access**:    sourcetable public; streams require per-Länder web registration
**registration**: https://www.sapos.de  (central portal links to each state's signup)
**operator**:  AdV (Arbeitsgemeinschaft der Vermessungsverwaltungen der Länder); 16 Bundesland operators
**source**:    sapos.de; zentrale-stelle-sapos.de
**last_researched_date**: 2026-05-12

Federal-state RTK network (~270 stations). Each Bundesland operates its own NTRIP caster
with independent registration. 14 of 16 states free. Bayern €20/yr non-agri flat rate (free
for agriculture) — under $200/yr cutoff. Rheinland-Pfalz paid at €120/yr/credential
(HEPS/GPPS) + one-time €100 setup fee — most restrictive state. BW: data free, one-time
€150 admin fee. ST free since 01.07.2023; MV free since 01.01.2024 (one-time €100 admin
fee). SH: €0.10/min HEPS + free Open Data tier (sapos.geonord-od.de:2101, user=gast/pass=gast).
AdV-GR 4.0 (June 2024) replaced per-minute billing with flat-rate models nationwide.
States whose sourcetables report a single coordinate for all virtual mountpoints yield
0 map stations (single-coord VRS); coverage for those requires NRTK polygons (deferred).
Raw TCP (NTRIP 1.0) fallback required in fetcher — SAPOS casters do not speak standard HTTP.
rtk2go ~31 DE volunteer bases — negligible alongside SAPOS but useful for testing.

| id | state | host:port | map type | notes |
|---|---|---|---|---|
| `sapos_SH_HH` | Schleswig-Holstein + Hamburg | `sapos.geonord.de:2101` | single-coord VRS | 0 stations |
| `sapos_NI` | Niedersachsen + Bremen | `sapos-ni-ntrip.de:2101` | single-coord VRS | 0 stations |
| `sapos_NW` | Nordrhein-Westfalen | `sapos-nw-ntrip.de:2101` | single-coord VRS | 0 stations |
| `sapos_HE` | Hessen | `sapos-he-ntrip.de:2101` | physical-coord VRS | ~4 stations (3 unique coords) |
| _Rheinland-Pfalz_ | _RP_ | _`sapos-ntrip.rlp.de:2101`_ | _not ingested_ | paid €120/yr/credential (HEPS/GPPS) + €100 one-time setup, most restrictive state — surfaced as a paid-affordable country marker in `data/country_markers.json`, not in the pipeline |
| `sapos_BW` | Baden-Württemberg | `sapos-bw-ntrip.de:2101` | single-coord VRS | 0 stations |
| `sapos_BY` | Bayern | `sapos-by-ntrip.de:2101` | single-coord VRS | €20/yr non-agri flat rate; free for agriculture |
| `sapos_SN` | Sachsen (GeoSN) | `www.ntrip.sachsen.de:2101` | populates on fetch | `www.` prefix required (DE_Germany research 2026-05-07); was DNS-failing without it |
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
**date_added**: 2026-05-13
**country**:   AT — Austria
**operator**:  BEV — Bundesamt für Eich- und Vermessungswesen
**host:port**: `aposrtk.bev.gv.at:2101`
**type**:      physical-coord-vrs
**access**:    paid via bev.gv.at portal; free eAMA tier for agriculture/forestry users
               (Austrian Betriebsnummer / LFBIS-Nr.)
**yearly_cost**: €200/mo RTK (~$220/mo); no annual plan — per-second, per-day, per-month only
**yearly_cost_normalized**: 1120
**registration**: https://www.bev.gv.at
**stations**:  37 physical AT stations in sourcetable; BEV brochure cites 75 including
               cross-border partner stations (SAPOS Bavaria, FReDNet, swipos AGNES)
**vrs**:       yes (nationwide VRS, no baseline-distance degradation)
**last_researched_date**: 2026-05-12

Austria's national VRS network operated by BEV. Sourcetable is publicly
readable; RTCM stream authentication requires valid credentials. Standard
tier pricing: RTK €0.0015/sec, €20/day, €200/month; DGPS €0.00015/sec,
€2/day, €20/month; one-time €50 setup fee; €50,000/yr for APOS RAW (full
raw-station access). A fixed IPv4 must be registered per device — dynamic
IPs not accepted for the paid tier.

**eAMA free tier** (since 1 Feb 2021): free APOS RTK for agricultural /
forestry businesses, contract operators, machinery rings, and publicly
funded agri-research institutions. Registration via the eAMA portal
(services.ama.at) with Betriebsnummer + PIN; BEV credentials issued within
~48 business hours. Stated subsidy equivalence ~€400/yr per enrolled
operation.

Mountpoints: APOS_VRS (legacy RTCM 2.3), APOS_VRS3 (RTCM 3.1), APOS_VRS32_MSM
(RTCM 3.2 MSM GPS+GLO+GAL), APOS_VRS32_MSM_3D (3D interpolation), APOS_DGPS,
plus APOS_NET3 / APOS_Extended / APOS_Extended_plus (2025: RTCM 3.2 MSM4 +
BeiDou). 15 AUT-coded rtk2go bases + 1 Centipede node (BOKU) supplement
coverage, mostly eastern Austria; western Alps weaker. Liechtenstein has no
independent caster and depends on APOS (via eAMA) or Swiss swipos.

---

### Italy — regional networks

---

## spin3 — SPIN3 GNSS (IT — Piemonte, Lombardia, Valle d'Aosta)

**status**:    free
**host:port**: `158.102.7.10:2101` (bare IP; spingnss.it hostname times out; IP confirmed SOURCETABLE 200 OK 2026-05-07)
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
**stations**:  13 (7 regional + 6 university; GPS+GLONASS+Galileo+BeiDou; ~40 km spacing)
**source**:    gpsumbria.regione.umbria.it (Regione Umbria)
**operator**:  Regione Umbria

Regional GNSS network for Umbria. Free public service with 13 physical reference stations (7 regional + 6 university).

---

## gnss_abruzzo_lazio — Rete GNSS Abruzzo + Lazio (IT — Abruzzo + Lazio)

**status**:    free
**host:port**: `gnss-rtk.regione.abruzzo.it:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via gnssnet.regione.abruzzo.it/accesso.php
**pipeline-access**: registration
**registration**: https://gnssnet.regione.abruzzo.it/accesso.php
**stations**:  ~29
**source**:    gnss-rtk.regione.abruzzo.it (Regione Abruzzo / Regione Lazio)
**operator**:  Regione Abruzzo / Regione Lazio

Since December 2022, Regione Lazio's stations were integrated into the Abruzzo
caster (16 Abruzzo + 13 Lazio stations). Bare IP alias: `93.57.92.145:2101`.
Endpoint times out from CI — service confirmed operational (connectivity contract
renewed March 2025).

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
**date_added**: 2026-05-06
**host:port**: `gps.sit.regione.campania.it:2101`
**type**:      physical-coord-vrs
**access**:    open; public shared credentials: username `Campania`, password `GNSS` for
               30-second VRS (`1_VRS30`); 1-second RTK requires SPID (Italian national
               digital identity)
**pipeline-access**: open (public credentials)
**stations**:  multiple stations covering Campania provinces
**source**:    regione.campania.it GNSS section (Regione Campania)
**operator**:  Regione Campania — SIT (Sistema Informativo Territoriale)

Campania regional GNSS network. Public credentials (`Campania`/`GNSS`) provide
30-sec VRS without registration. 1-sec RTK requires SPID. Leica Spider caster.

---

### US state DOT — physical-coord

---

## wiscors — WISCORS (US-WI)

**status**:    free
**host:port**: `wiscors.dot.wi.gov:2101` (IP 165.189.65.133)
**type**:      physical-coord-vrs (single-base + VRS)
**access**:    registration; free via wiscors.dot.wi.gov (Wisconsin DOT)
**pipeline-access**: registration
**stations**:  115+ permanent statewide
**source**:    wiscors.dot.wi.gov (Wisconsin Department of Transportation)
**operator**:  Wisconsin DOT
**last_researched_date**: 2026-05-13

Wisconsin CORS Network operated by WisDOT (Trimble Pivot). Offers both single-base
streams and VRS corrections. Recommended mountpoint `RTCM32` (RTCM3 GPS+GLO+GAL);
`CMRxGNSS` added 2024 for Trimble receivers adds full multi-constellation including
BeiDou. Many WI stations also appear in EarthScope NOTA — verify overlap before
ingesting to avoid duplicate pins.

---

## fprn — FPRN (US-FL)

**status**:    free
**host:port**: `www.myfloridagps.com:10000` (IP 48.223.232.215; SOURCETABLE 200 OK 2026-05-13; 101 STR)
**type**:      physical-coord-vrs
**access**:    registration; free via myfloridagps.com (Florida DOT)
**pipeline-access**: registration
**stations**:  ~100 (live 2026-05-13: 101 STR rows including network solutions and single-base streams)
**vrs**:       yes (VRS, iMAX, MAX, FKP; `RTCM3_VRS` mountpoint in user guides)
**source**:    myfloridagps.com (Florida Department of Transportation, Geospatial office)
**operator**:  Florida DOT (FDOT)
**last_researched_date**: 2026-05-13

Florida Permanent Reference Network operated by FDOT on Leica GNSS Spider 7.11.1.109.
Non-standard port 10000 (NAD83 Network Solutions); 11000-series for TCP/IP. "Currently
there are no plans to charge users for any FPRN services or products." Open to anyone
with an NTRIP-ready GNSS receiver and internet access; no Florida residency requirement;
account activates within 24-48 hours. One account per rover. Formats: RTCM 2.3, RTCM
3.1, CMR+, RTCM 3.3 MSM4. Legacy IP `40.121.5.206` deprecated. Widely regarded as the
model state public RTK service. Some overlap with EarthScope NOTA expected.

---

## ardot_rtn — ARDOT RTN (US-AR)

**status**:    free
**host:port**: `gps.ardot.gov:2101` (IP 199.48.3.12; SOURCETABLE 200 OK 2026-05-13, 8 STR)
**type**:      physical-coord-vrs
**access**:    registration; free via ardot.gov (Arkansas DOT)
**pipeline-access**: registration
**stations**:  ~50
**source**:    ardot.gov (Arkansas Department of Transportation)
**operator**:  Arkansas DOT
**last_researched_date**: 2026-05-13

Arkansas real-time network on Trimble Pivot. Free after registration via the
gps.ardot.gov portal. Sensor map at gps.ardot.gov/Map/SensorMap.aspx. Mountpoints
include `ARDOT_RTX_CMRp/CMRx` (network solutions) and `MS_CMRp/CMRx` (nearest single
base). PAGIS (Pulaski Area GIS) supplementary single-base station serves Little Rock /
Pulaski County with a separate signed-agreement registration at pagis.org.

---

## macors — MaCORS (US-MA)

**status**:    free
**host:port**: `macorsrtk.massdot.state.ma.us:2101` (IP 193.8.43.161)
**type**:      physical-coord-vrs
**access**:    registration; free via massdot.state.ma.us (MassDOT)
**pipeline-access**: registration
**stations**:  22 (GNSS base stations, ~50 km spacing; Mass.gov current listing)
**vrs**:       yes (Leica iMAX; recommended `RTCM3MSM_IMAX` for full-constellation GPS+GLO+GAL+BDS)
**source**:    massdot.state.ma.us (Massachusetts Department of Transportation)
**operator**:  Massachusetts DOT (MassDOT)
**last_researched_date**: 2026-05-13

Massachusetts CORS network on Leica SpiderNet (SBC). 22 stations; free registration
("MassDOT does not currently charge a fee for network access"). Formats: RTCM 2.3,
RTCM 3.1/3.2 MSM4, CMR, CMR+. Coverage extends into RI, southern NH, eastern CT.
Port 2101 times out from external probes (re-verified 2026-05-13) — firewalled or
IP-allowlisted; users report successful connections from within the US once the
account is active.

---

## vector — VECTOR VT (US-VT)

**status**:    free
**host:port**: `vector.vermont.gov:2101` (IP 20.185.11.35)
**type**:      physical-coord-vrs
**access**:    registration; free via vector.vermont.gov (VTrans Geodetic Survey)
**pipeline-access**: registration
**stations**:  18 physical reference stations (live 2026-05-13: 36 STR rows = physical + single-base + VRS variants)
**vrs**:       yes (RTCM 3.1 and CMR+ single-base and network streams)
**source**:    vtrans.vermont.gov/highway/geodetic (Vermont Agency of Transportation)
**operator**:  Vermont Agency of Transportation (VTrans), Geodetic Survey
**last_researched_date**: 2026-05-13

Vermont Enhanced CORS and Transmission Of Real-time corrections, operated by VTrans
on a Trimble Pivot platform. Explicit hobbyist eligibility — "a free service utilized
by State and Federal Agencies, Surveyors, GIS users, Engineers, Scientists, and the
public at large". 18 stations statewide; all except VJSC and VTWR accredited with
NOAA NCN. Equipment upgrades from NetR9 to current-generation receivers completed
in 2025. SOURCETABLE 200 OK confirmed 2026-05-13 (36 STR entries). Previously listed
with bare IP `20.185.11.35`; canonical hostname `vector.vermont.gov` resolves to the
same IP.

---

## azcors — AzCORS (US-AZ)

**status**:    free
**host:port**: `azcors.azwater.gov:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via azwater.gov (Arizona Dept. of Water Resources)
**pipeline-access**: registration
**stations**:  52 (37 ADWR-managed + 15 EarthScope/NPS CORS sites; per ADWR March 2025 update reflected in AZCORS_InformationAndMountpoints20260406.pdf)
**source**:    azwater.gov (Arizona Department of Water Resources)
**operator**:  Arizona Dept. of Water Resources (ADWR)
**last_researched_date**: 2026-05-13

Arizona CORS Network operated by ADWR. 52 total sites (37 ADWR + 15 EarthScope/NPS);
ADWR consolidated and decommissioned several sites during the 2024–2025 modernisation,
superseding the earlier 71-site figure. Free registration at azcors.azwater.gov/sbc.
Moderate overlap with EarthScope NOTA expected. Port 2101 is the Leica SBC default;
external probes timeout (Cloudflare CDN in front of the portal) — actual port confirmed
post-registration only.

---

## gcgc_rtn — GCGC RTN (US-MS)

**status**:    free
**host:port**: `rtn.usm.edu:2101`
**type**:      physical-coord-vrs
**access**:    registration; free via usm.edu Gulf Coast Geospatial Center portal
**pipeline-access**: registration
**stations**:  ~52 CORS (Mississippi-focused; 14 STR live 2026-05-13)
**vrs**:       unclear (Trimble Pivot platform supports VRS; specific VRS mountpoints not confirmed in public docs)
**source**:    rtn.usm.edu (Gulf Coast Geospatial Center / University of Southern Mississippi)
**operator**:  Gulf Coast Geospatial Center (GCGC), University of Southern Mississippi
**last_researched_date**: 2026-05-13

Gulf Coast Geospatial Center Real Time Network operated by USM. 52 CORS stations
covering Mississippi; network established 2005 under the NOAA/NGS national initiative.
"Use of the network is free of charge"; open registration at rtn.usm.edu/RegisterAccount.aspx;
no professional licence requirement. Reference Data Shop produces virtual RINEX files.
Coverage is Mississippi-focused; does not meaningfully extend into Georgia or other
adjacent states. SOURCETABLE 200 OK re-confirmed 2026-05-13 (14 STR entries).

---

## alcors — AlCORS (US-AL)

**status**:    free
**host:port**: `aldotcors.dot.state.al.us:10099` (IP 205.172.52.26; 158 STR physical single-base);
               `:10011` (IP 205.172.52.26; 10 STR network mountpoints — `RTCMIMAX`, `AutoMAX`, `CMR+IMAX`, `LeicaMAX`)
**type**:      physical-coord-vrs
**access**:    registration; free via aldotcors.dot.state.al.us (Alabama DOT)
**pipeline-access**: registration
**stations**:  ~158 physical single-base on `:10099` (live 2026-05-13); 10 network solution mounts on `:10011`
**vrs**:       unclear (network mounts include `LeicaMAX`/`RTCMIMAX` — implies network RTK; VRS not explicitly confirmed)
**source**:    aldotcors.dot.state.al.us (Alabama Department of Transportation)
**operator**:  Alabama DOT (ALDOT) — Leica SpiderNet
**last_researched_date**: 2026-05-13

Alabama CORS network on Leica Spider Business Center (SBC). ALDOT transitioned from
legacy TCP to Leica SBC web portal circa 2022; old TCP connections no longer supported.
Standard NTRIP port 2101 firewalled. Only `205.172.52.26` is externally reachable
(`205.172.52.25` blocks all ports). Both `:10011` (network solutions: `RTCMIMAX`,
`AutoMAX`, `CMR+IMAX`, `LeicaMAX`, etc.) and `:10099` (158 physical single-base RTCM 3
GPS+GLO mountpoints) returned SOURCETABLE 200 OK on 2026-05-13. Free of charge per
multiple community sources; registration form requires a Company field but hobbyists
have successfully registered.

---

## orgn — ORGN (US-OR)

**status**:    free
**host:port**: `orgn.odot.state.or.us:9881` (IP 167.131.109.57; SOURCETABLE 200 OK 2026-05-13, 6 STR)
**type**:      physical-coord-vrs
**access**:    registration; free via oregon.gov/odot/orgn (Oregon DOT)
**pipeline-access**: registration
**stations**:  ~100
**source**:    oregon.gov (Oregon Department of Transportation)
**operator**:  Oregon DOT (ODOT)
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Oregon Real-Time GNSS Network. Leica GNSS Spider. Non-standard port 9881 (network
solutions); single-base solutions also offered on 167.131.0.205:9879 per ODOT PDFs.
Accounts issued via the rover request form at oregon.gov/odot/orgn/pages/rover-requests.aspx;
ODOT states it may "charge reasonable subscription fees for rover accounts" in future,
but partner accounts remain free permanently. Significant overlap with EarthScope NOTA
expected.

---

## msrn — MSRN (US-MI)

**status**:    free
**host:port**: `mdotcors.michigan.gov:10010` (free RTCM3 MSM4 port; 10011 = CMRx; per MSRN Port Scheme docs)
**type**:      physical-coord-vrs
**access**:    registration; free via michigan.gov (Michigan DOT)
**pipeline-access**: registration
**stations**:  ~95 CORS statewide
**source**:    michigan.gov (Michigan Department of Transportation)
**operator**:  Michigan DOT (MDOT)
**last_researched_date**: 2026-05-13

Michigan Spatial Reference Network operated by MDOT (Leica Spider Business Center).
Free NTRIP ports 10010 (RTCM3 MSM4) and 10011 (CMRx) per MSRN Port Scheme documentation;
port 10700 was incorrect. Account creation at `mdotcors.michigan.gov/sbc/Account/Register`;
recommended mountpoint `NS-IMAX-MSM4` (network-mode, full constellation). Rover must
upload GGA at least every 30 seconds. Significant overlap with EarthScope NOTA expected.

---

## nysnet — NYSNet (US-NY)

**status**:    free
**host:port**: `rtn.dot.ny.gov:8080` (NTRIP; IP 161.11.223.1 — port 2101 firewalled);
               `cors.dot.ny.gov` (SBC portal; IP 161.11.223.14)
**type**:      physical-coord-vrs
**access**:    registration; free via cors.dot.ny.gov (NYSDOT — credentials emailed after activation)
**pipeline-access**: registration
**stations**:  ~150 (live sourcetable 2026-05-13: 18 STR rows covering MAX/iMAX/MSM/CMR variants on shared physical infrastructure)
**vrs**:       yes (`net_msm_vrs` RTCM 3 MSM GPS+GLO+GAL+BDS; iMAX `net_msm_imax`, `GG_MSM_IMAX`; `near_msm` nearest-site)
**source**:    dot.ny.gov (New York State Department of Transportation, Engineering Division + NYC partners)
**operator**:  New York State DOT (NYSDOT)
**last_researched_date**: 2026-05-13

New York Spatial Reference Network operated by NYSDOT on Leica SpiderNet (GNSS Spider
7.10.1.168). "NYSDOT does not charge users a fee for access to the real-time network."
Recommended multi-constellation mountpoints for non-Leica rovers (Emlid, Ardusimple,
DJI RTK): `near_msm`, `net_msm_vrs`, `net_msm_imax`. Legacy mountpoints (`NetCell_MAX_RTCMv3`,
`NetCell_iMAX_*`) are GPS-only or GPS+GLO. Datum NAD83(2011) epoch 2010.0 MYCS2. NTRIP
service confirmed via curl on `rtn.dot.ny.gov:8080` (2026-05-13, 18 STR) — standard port
2101 timed out from external IP. 2024 NYSAPLS conference indicated planned full station
rebuilds and possible densification by 10+ CORS. Significant overlap with EarthScope NOTA
expected.

---

## incors — InCORS (US-IN)

**status**:    free
**host:port**: `incors.in.gov:10000` (IP 108.59.49.226; Leica SBC scheme)
**type**:      physical-coord-vrs
**access**:    conditions; signed User Agreement required (free); via incors.in.gov (INDOT)
**pipeline-access**: conditions
**stations**:  60 in solution (45 INDOT + 15 cross-state from MI, OH, KY)
**source**:    incors.in.gov (Indiana Department of Transportation)
**operator**:  Indiana DOT (INDOT)
**last_researched_date**: 2026-05-13

Indiana CORS Network operated by INDOT on a Leica Spider Business Center platform. Host
and port provided after the User Agreement (incors.in.gov/useragreement.pdf) is signed
and returned to incors@indot.in.gov; port 10000 is best-guess from Leica SBC defaults.
Connection refused from external IPs is expected — firewalled to registered accounts.
All four constellations (GPS+GLO+GAL+BDS) supported network-wide following the
2024-06-18 station upgrade; recommended mountpoint `RTCM3_MAX` (GPS+GLO), MSM4
full-constellation also available. FTP RINEX archive at `ftp.incors.in.gov`.

---

## iartn — IARTN (US-IA)

**status**:    free
**host:port**: `165.206.203.10:10000` (primary; bare IP, no DNS hostname currently);
               `iartnsbc.iowadot.gov:2101` (legacy, dead 2026-05-07)
**type**:      physical-coord-vrs
**access**:    registration; free via iowadot.gov (Iowa DOT)
**pipeline-access**: registration
**stations**:  83 IaRTN reference stations + 21 cross-state contributors (10 MnDOT, 4 WisDOT, 7 MoDOT)
**source**:    iowadot.gov (Iowa Department of Transportation);
               e38surveysolutions.com/blogs/news/emlid-reach-rx-or-rs2-and-dji-rtk-connection-to-iowa-ntrip-iartn (Emlid/DJI client setup walkthrough; mountpoint `MSM_IMAX` is the recommended full-constellation RTCM3 stream)
**operator**:  Iowa DOT
**last_researched_date**: 2026-05-13

Iowa Real-Time Network operated by Iowa DOT (Leica SBC). 83 physical stations placed at
Iowa DOT maintenance facilities; supplemented along borders by 10 MnDOT, 4 WisDOT, and
7 MoDOT cross-state stations included in the network solution. Free self-service
registration at `iartnsbc.iowadot.gov/sbc/Account/Register`; credentials emailed within
2 business days. Recommended mountpoint `MSM_IMAX` (RTCM3 MSM4, full constellation).
Legacy hostname `iartnsbc.iowadot.gov:2101` returns blank response (2026-05-07);
bare IP `165.206.203.10:10000` is the working endpoint. SOURCETABLE is open; individual
station streams require credentials. NATRF2022 migration planned mid-to-late 2026 with
parallel mountpoints during the NAD83(2011) → NATRF2022 transition.

---

## ct_acorn — ACORN (US-CT)

**status**:    free
**host:port**: `acorn.uconn.edu:2101` (IPs 137.99.150.112, 137.99.150.56)
**type**:      physical-coord-vrs
**access**:    registration; free via acorn.uconn.edu (CTDOT + UConn)
**pipeline-access**: registration
**stations**:  13 (9 in CT, 1 in RI, 2 in southern MA, 1 Long Island NY)
**vrs**:       yes (primary `VRS3_RTX` multi-constellation; `VRSX_RTX` for Trimble)
**source**:    acorn.uconn.edu (Connecticut DOT + UConn Department of Natural Resources)
**operator**:  CTDOT + University of Connecticut (UConn DNRE)
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Advanced Continuously Operating Reference Network for Connecticut. Trimble Pivot platform.
13 sensors covering CT, RI, southern MA, and Long Island NY. GPS + GLONASS + Galileo +
BeiDou (Galileo and BeiDou added mid-2025). Explicitly "free and available to the public";
no professional licence required. Useful fallback for Rhode Island users (no RI state
caster). SOURCETABLE 200 OK re-confirmed 2026-05-13 (48 STR entries).

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
**date_added**: 2026-05-13
**country**:   BE — Belgium (Flanders region)
**operator**:  Agentschap Informatie Vlaanderen / Agentschap Digitaal Vlaanderen
**host:port**: `flepos.vlaanderen.be:2101` (migrated to IP 3.64.78.173 on 2024-06-17)
**type**:      single-coord-vrs
**access**:    free for all uses; web self-signup at flepos.vlaanderen.be
**pipeline-access**: registration
**registration**: https://flepos.vlaanderen.be/Login.aspx
**stations**:  0 (45 declared; single-coord Flanders centroid)
**vrs**:       yes
**key_mountpoint**: FLEPOSVRS32GREC (RTCM 3.2; GPS+GLO+GAL+BDS)
**last_researched_date**: 2026-05-12

Old endpoint `ntrip.flepos.be` is NXDOMAIN as of 2026-04. SOURCETABLE 200 OK
confirmed 2026-05-06 from a Belgian probe; sometimes times out from external
IPs due to location-based firewalling. Subscription categories include
Survey, Agriculture, Machine guidance, Maritime, Education, Test. Admin
account creates per-device subscriptions; support.flepos@vlaanderen.be.

---

## walcors — WALCORS (BE — Wallonia)

**status**:    free
**date_added**: 2026-05-13
**country**:   BE — Belgium (Wallonia region)
**operator**:  SPW — Service Public de Wallonie (DGO3 — Agriculture, Ressources naturelles, Environnement)
**host:port**: `gnss.wallonie.be:8081` (IP 157.164.253.36)
**type**:      single-coord-vrs
**access**:    free for positioning; paid for machine-control / auto-guidance via commercial resellers
**pipeline-access**: registration
**registration**: https://gnss.wallonie.be (FR/DE)
**stations**:  0 (22 Wallonia + 13 cross-border LU/NL/FR/DE declared; single-coord VRS)
**vrs**:       yes
**mountpoints**: VRS32GREC (VRS), IMAX32GREC (Leica iMAX), NEAR32GREC (nearest physical)
**last_researched_date**: 2026-05-12

Port 8081 confirmed 2026-05-06. Three VRS product types span all major
constellations. Geographic software polygon restricts corrections to within
Belgium territory. Three user categories on the registration form: SURVEY,
GIS, GUIDAGE. 5 MB/hr data volume per user. Contact gnss@spw.wallonie.be /
+32 81 71 59 22.

Belgium-wide volunteer redundancy: 17 BEL-coded Centipede nodes (incl. `AHOA`,
`BIST`, `COCO`, `CRA1`, `LEMA`, `STAVE`, mostly Wallonia and the
Brussels–Antwerp corridor) plus 2 rtk2go bases (`ROOS1` central, `Stuer`
Antwerp). Useful when government caster registration is pending.

---

## latpos — LatPos (LV)

**status**:    free
**date_added**: 2026-05-06
**host:port**: `latpos.lgia.gov.lv:5001`
**type**:      single-coord-vrs
**access**:    free since 2018; SBC portal signup at latpos.lgia.gov.lv/SBC
**pipeline-access**: registration
**stations**:  0 (27 LV + 5 EE + 4 LT border stations declared; single-coord)
**source**:    latpos.lgia.gov.lv (LGIA)
**operator**:  LGIA — Latvijas Ģeotelpiskās informācijas aģentūra

Domain `lgia.gov.lv` is live; SBC portal at `latpos.lgia.gov.lv` active.
Port 5001 confirmed responding SOURCETABLE 200 OK on 2026-05-06. This is the
canonical port per Alberding directory and the research confirms it is live.
Non-standard port 5001 may be blocked by some egress firewalls (CI timeout
observed previously). Network accuracy ~2 cm horizontal.

---

## litpos — LitPOS (LT)

**status**:    free
**date_added**: 2026-05-07
**host:port**: Primary: `193.219.10.2:2101`; Secondary: `195.182.72.152:2101`
**type**:      vrs-only
**access**:    free; register at geoportal.lt/web/litpos-en/registration
**pipeline-access**: registration
**stations**:  35 LT + 3 PL (ASG-EUPOS) + 6 LV (LatPos) via EUPOS cooperation
**operator**:  VšĮ Statybos sektoriaus vystymo agentūra (SSVA); GIS-Centras technical operator
**source**:    geoportal.lt

EUPOS member. VRS-only sourcetable (all mounts at 54,23 / solution=1; 0 physical pins).
RTCM 2.3/3.1/3.2 (MSM5 GPS+GLO+GAL+BDS), CMR+, CMRx, DGPS. Confirmed alive 2026-05-07
(both IPs SOURCETABLE 200 OK, Trimble Pivot Platform, 12 STR rows).

---

## estpos — ESTPOS (EE)

**status**:    free
**date_added**: 2026-05-13
**country**:   EE — Estonia
**operator**:  Maa- ja Ruumiamet (Estonian Land and Spatial Development Board; formerly Maaamet)
**host:port**: `gnss-rtk.maaamet.ee:8083` (IP 213.184.51.72) — both maaamet.ee and
               maaruum.ee domains active during 2025/26 rebrand transition. NTRIP
               port TCP-timed-out from this sandbox 2026-05-12 — likely geo/IP filter.
**type**:      single-coord-vrs (40 CORS feeding VRS, iMAX, nearest-station)
**access**:    free until **31 Aug 2026** (director-general directive); portal account
               + service agreement; previously had Estonia-only IP restriction (current
               status with expanded network unclear — verify before relying)
**pipeline-access**: conditions
**registration**: https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html
**stations**:  40 CORS as of June 2025; rebuilt 2024–2025 with EU NextGenerationEU funding
**vrs**:       yes — iMAX, VRS, nearest-station; mountpoints `DGNSS_iMAX/VRS/Nearest`,
               `RTCM2_*`, `RTCM3_*`, `MSM5_*`
**signals**:   GPS+GLO+GAL+BDS; part of EUREF EPN; EST97/ETRS89
**last_researched_date**: 2026-05-12

Free until 31 August 2026 per Estonian Land and Spatial Development Board
director-general directive; post-August tariff not yet announced. Land Board
rebranded to Maa- ja Ruumiamet; ESTPOS user manual reissued 2026-03-12. Both
old (maaamet.ee) and new (maaruum.ee) domains active simultaneously.

**investigate**: confirm endpoint reachability from an Estonian IP; monitor
maaruum.ee/announcements for the post-2026-08-31 tariff decision.

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

**Republication posture (2026-05-07)**: keep listing. KSA-CORS is `vrs-only` —
the sourcetable exposes single-coordinate VRS mountpoints, not physical
antenna positions, and `data/stations.json` confirms 0 republished stations
(VRS filter drops them). There is no per-station coordinate metadata to weigh.
On policy: GASGI/GEOSA is a Saudi government agency and Saudi data policy is
"Open by Default" with non-discriminatory access (data.gov.sa, Open Data
Commons Attribution v1.0); no clause prohibiting station-metadata republication
was found. Operator policy pages (geosa.gov.sa, geoportal.sa, gasgi.gov.sa)
returned HTTP 503 from this sandbox and could not be read directly.

**investigate**: verify `ksacors.geoportal.sa:2101` from a Saudi/GCC IP;
cannot be confirmed or ruled out from outside the region. Re-check operator
policy page (gasgi.gov.sa FAQ + Getting-Started PDF) once it is reachable.

---

## cropos — CROPOS (HR)

**status**:    free
**date_added**: 2026-05-13
**country**:   HR — Croatia
**last_researched_date**: 2026-05-12
**host:port**: `gnss.cropos.hr:2101` (alt IP `195.29.198.194:2101`)
**type**:      vrs-only
**access**:    free since Apr 2022 (Narodne novine 39/2022); email/web registration at cropos.hr;
               one-time 40 EUR registration fee per Regulation NN 56/2023 / NN 106/25
**pipeline-access**: registration
**stations**:  0 (35+ declared including 2025 expansion; sourcetable reports 0/0 for all
               mountpoints — Trimble Pivot VRS convention)
**source**:    cropos.hr (DGU)
**operator**:  DGU — Državna geodetska uprava

15 VRS-only streams (all `CROPOS_VRS_*`; 0/0 coordinates per Trimble Pivot convention).
Caster IP changed Nov 2023 (old: 195.29.118.122 → new: 195.29.198.194). DPS (~0.3–0.5 m)
and VPPS (≤2 cm) free; GPPS post-processing 0.06 EUR/min (paid). One-time 40 EUR
registration fee per NN 56/2023 is the only remaining charge for VPPS users. Confirmed
alive 2026-05-12 (SOURCETABLE 200 OK, Trimble Ntrip Caster 5.2, 15 STR rows).

---

### US state DOT — VRS-only

---

## kycors — KyCORS (US-KY)

**status**:    free
**host:port**: `kycors.ky.gov:2101`
**type**:      single-coord-vrs
**access**:    registration; free via kycors.ky.gov (Kentucky Transportation Cabinet)
**pipeline-access**: registration
**stations**:  VRS only (6 STR rows live 2026-05-13)
**vrs**:       yes (recommended `RTX_RTCM3_2` — RTCM3 multi-constellation)
**source**:    kycors.ky.gov (Kentucky Transportation Cabinet)
**operator**:  Kentucky Transportation Cabinet (KYTC) — Trimble Pivot
**last_researched_date**: 2026-05-13

Kentucky Real Time Reference Network. VRS-only sourcetable; no physical-coordinate
mountpoints. Registration at kycors.ky.gov/RegisterAccount.aspx is manual (admin
approval; portal warns "DO NOT click REGISTER button more than once"); contact
KYCORS_Admin@ky.gov before registering if unsure. SOURCETABLE 200 OK re-confirmed
2026-05-13.

---

## mncors — MnCORS (US-MN)

**status**:    free
**host:port**: `mncors.dot.state.mn.us:9000` (IP 151.111.142.75; non-standard Trimble Pivot port)
**type**:      single-coord-vrs
**access**:    registration; free via mndot.gov (Minnesota DOT)
**pipeline-access**: registration
**stations**:  VRS only (underlying ~140 physical stations)
**source**:    mndot.gov (Minnesota Department of Transportation)
**operator**:  Minnesota DOT (MnDOT)
**last_researched_date**: 2026-05-13

Minnesota CORS Network operated by MnDOT (Trimble Pivot). Non-standard port 9000.
VRS-only sourcetable; physical stations not individually listed. Mountpoints include
`RTCM_32_NAD83(2011)` (RTCM3, multi-constellation); formats RTCM 2.3 / 3.1 / 3.4, CMR+,
CMRx. Accounts deactivate after one year of inactivity (≥1 second of use retains
active status). Four northern stations added to network solution in early 2026 (Stony
River, Tofte, Seagull Lake Access, Gunflint Midtrail) — northern wilderness / Boundary
Waters now covered. Significant overlap with EarthScope NOTA expected.

---

## odot_rtn — ODOT RTN (US-OH)

**status**:    free
**host:port**: `156.63.133.115:2101` (DNS `ortn.dot.state.oh.us`; HTTPS portal account-gated)
**type**:      single-coord-vrs
**access**:    registration; free via transportation.ohio.gov (Ohio DOT)
**pipeline-access**: registration
**stations**:  VRS only
**source**:    transportation.ohio.gov (Ohio Department of Transportation)
**operator**:  Ohio DOT
**last_researched_date**: 2026-05-13

Ohio Real-Time Network (Trimble Pivot). VRS-only sourcetable; mountpoints
`ODOT_G_R_E_C_RTX_RTCM3` (multi-constellation GPS+GLO+GAL+BDS+L5) and
`ODOT_G_R_E_C_RTX_CMRx` (Trimble) added after a 2024 receiver/software upgrade — the
network was previously GPS+GLO only. Free registration via the ODOT survey/CORS landing
page; no professional licence field identified. Trimble Pivot Web login at
`ortn.dot.state.oh.us/TrimblePivotWeb/Login.aspx`.

---

## modot_rtn — MoDOT RTN (US-MO)

**status**:    free
**host:port**: `rtk3.modot.mo.gov:2101` (= `gpsweb3.modot.mo.gov:2101`; IP 168.166.125.30)
**type**:      single-coord-vrs
**access**:    conditions; requires signed and notarized MoDOT CORS access agreement;
**pipeline-access**: conditions
               free once approved — contact via modot.mo.gov
**stations**:  VRS only (underlying 78 NetR5 CORS, max 70 km spacing)
**source**:    modot.mo.gov (Missouri Department of Transportation)
**operator**:  Missouri DOT
**last_researched_date**: 2026-05-13

Missouri DOT Real-Time Network (Trimble Pivot). VRS-only sourcetable; mountpoints:
`VRS_RTCM31` (GPS+GLO, recommended), `VRS_CMRplus`, `VRS_CMRx`, `VRS_RTCM21`,
`VRS_RTCM23`, `RTCM3Net_Autocell`. A multi-constellation `RTX_CMRx` mountpoint was
added in 2024 for Trimble receivers. Underlying network is 78 CORS stations (NetR5
receivers with Zephyr Geodetic II antennas) covering all 114 Missouri counties.
Requires notarized access agreement
(`gpsweb3.modot.mo.gov/MODOT_RTK_GPS_USER_AGREEMENT.pdf`) submitted to MoDOT before
credentials are issued; FAQ suggests registering under an organisation name to survive
personnel changes, but individuals can sign as their own entity.

---

## wvrtn — WVRTN (US-WV)

**status**:    free
**host:port**: `wvrtn.cors.us:2101` (alt IP `34.228.171.115:2101`; caster IP `206.212.1.199:2101` per WVDOT docs)
**type**:      single-coord-vrs
**access**:    registration; free via wvrtn.cors.us (WV Dept. of Transportation — IT Division, Highway Data Services Unit)
**pipeline-access**: registration
**stations**:  VRS only (underlying ~34 CORS upgraded to Trimble Alloy receivers in 2024; 7 STR rows live 2026-05-13)
**vrs**:       yes (recommended `rtxRTCM3_4_MSM` / `rtxCMRx` multi-constellation; older `rtxRTCM3_2` was renamed)
**source**:    transportation.wv.gov (WV Department of Transportation)
**operator**:  WVDOT — Information Technology Division, Highway Data Services Unit
**last_researched_date**: 2026-05-13

West Virginia Real Time Network. VRS-only sourcetable. Free registration at
wvrtn.cors.us/RegisterAccount.aspx; organisation field required but no professional
licence stated. Live 2026-05-13 mountpoints: `vrsRTCM3_1`, `vrsCMRx`, `vrsCMRplus`,
`vrsRTCM3_2`, `rtxCMRx` (multi-constellation), `rtxRTCM3_4_MSM` (multi-constellation),
plus a `NATRF2022_Test` preview of the 2026 NSRS datum modernisation. Backup hostname
`cors.us` resolves to same IP.

---

## mainedot — MaineDOT RTN (US-ME)

**status**:    free
**host:port**: `medotrtn.maine.gov:2101` (IP 52.165.92.197)
**type**:      vrs-only
**access**:    registration; free via medotrtn.maine.gov (MaineDOT Survey Section)
**pipeline-access**: registration
**stations**:  VRS only (8 STR rows live 2026-05-13)
**vrs**:       yes
**source**:    maine.gov/dot (Maine Department of Transportation, Bureau of Project Development)
**operator**:  Maine DOT
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Maine Real-Time Network. Migrated from legacy host `mdotcors.maine.gov` (now ECONNREFUSED)
to `medotrtn.maine.gov:2101` via Trimble Pivot on 2025-10-01; existing users were
required to re-register after the cutover. Mountpoints: `VRS_CMR`, `VRS_RTCM`,
`VRS_RTCM_23`. SOURCETABLE 200 OK re-confirmed 2026-05-13 (8 STR entries).

---

## mesa_rtvrn — Mesa County RTVRN (US-CO)

**status**:    free
**host:port**: `rtvrn.mesacounty.us:2101` (IP 35.131.54.14; SOURCETABLE 200 OK 2026-05-13, 6 STR)
**type**:      vrs-only
**access**:    registration; free via rtvrn.mesacounty.us
**pipeline-access**: registration
**stations**:  33 (17 NGS CORS + 16 county/partner stations) underlying VRS
**source**:    mesacounty.us/departments-and-services/public-works/gps-survey
**operator**:  Mesa County Public Works (Western Colorado)
**last_researched_date**: 2026-05-13

VRS-only network covering western Colorado. Mountpoints are all VRS_* (CMR,
CMRx, RTCMv3, RTX variants) — no single-base mountpoints exposed. Free
sign-up at rtvrn.mesacounty.us; same credentials used for NTRIP. Trimble
PIVOT backend; NAD83(2011). The 33-station network extends useful coverage
across western Colorado and into adjacent Utah and Wyoming; underlying 17 NGS CORS
likely overlap with EarthScope NOTA in northern Mesa County, but VRS streams have
no fixed coordinate so no duplicate pins on the map.

---

## Candidate — confirmed free, not yet ingested

Free networks with a confirmed host:port that have been added to
`fetch_stations.py` SOURCES but have not yet completed a successful cron fetch.
The next GitHub Actions run is the live verifier — type and counts may need
tuning once a sourcetable is observed.

---

## gpsbru — GPSBru / AGN (BE — Brussels)

**status**:    free
**date_added**: 2026-05-13
**country**:   BE — Belgium (Brussels Capital Region)
**operator**:  NGI / IGN — Nationaal Geografisch Instituut / Institut Géographique National
**host:port**: via AGN portal at agn.ngi.be (host/port issued after login request)
**type**:      single-base (UKKE — Uccle/Ukkel NGI campus, one physical station)
**access**:    free; login request via agn.ngi.be
**registration**: https://agn.ngi.be
**stations**:  1 (UKKE)
**vrs**:       no
**mountpoints**: UKKE_GNSS_3.0 (RTCM 3.0, GPS+GLONASS); RTCM 2.1/2.3 variants (GPS only)
**last_researched_date**: 2026-05-12

Single-base RTK usable within ~20 km of Ukkel; DGPS usable throughout
Belgium. RTCM 3.0 stream is dual-constellation (GPS+GLO) for improved urban
sky coverage.

**missing**: confirm public NTRIP port — host:port is issued only after AGN
login request.

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

**Republication posture (2026-05-07)**: keep listing. As of 2026-05-07 the
caster has never returned a parseable sourcetable from CI — `data/stations.json`
shows 0 republished stations and status:error — so no DOL station-coordinate
metadata is currently being surfaced. The Thai-national-ID gate is on stream
*registration*, not on coordinate metadata: DOL's CORS layout (114 stations,
63 provinces) is published in peer-reviewed literature (e.g. *Unification of
GNSS CORS coordinates in Thailand*, ResearchGate 355298294; *Performance of
Network-Based RTK GNSS for Cadastral Survey in Thailand*, IJG). dol-rtknetwork.com
returned HTTP 503 from this sandbox, so the operator's own ToS page could not
be read; no public clause prohibiting redistribution of station coordinates has
been located. If a future cron run does begin returning physical mountpoints,
revisit this note rather than assuming default-keep.

**investigate**: confirm sourcetable structure from the next cron run; obtain
full zone–port mapping for all regions; re-check dol-rtknetwork.com ToS once
reachable from CI.

---

## Deferred — free, endpoint not yet obtainable

---

## slrb_bh — SLRB PRN (BH)

**status**:    free
**date_added**: 2026-05-13
**country**:   BH — Bahrain
**operator**:  Survey & Land Registration Bureau (SLRB), Kingdom of Bahrain
**type**:      VRS (likely; network-RTK per SLRB description; not explicitly stated in public material)
**host:port**: issued in credentials email after application (not publicly advertised)
**access**:    free of charge as of 2026-05-12; application by email to PRN@slrb.gov.bh
               with completed GPS Network Application Form; credentials issued in 1–2
               working days; one device per credential
**registration**: https://www.slrb.gov.bh/en/permanent-reference-networkprn
**stations**:  not disclosed (Bahrain ~765 km² — a single well-sited station covers
               the entire kingdom within typical 30 km RTK baseline)
**last_researched_date**: 2026-05-12

The Permanent Reference Network provides the geodetic basis for all
surveying operations in Bahrain. Available 24/7 to the whole kingdom; SLRB
notes "this service may incur charges in the future" but is currently free.
Application accepts both Individual and Agent applicant types; no
licensed-surveyor requirement stated. Specific NTRIP host:port, mountpoint
names, RTCM versions, VRS type, and supported constellations are not
published — issued only in the credentials email.

Prior pipeline classification (pre-2026-05-12) recorded PRN as
access-restricted with no public registration path; that was incorrect.
SLRB publishes a clear self-service registration path and explicit free
status. Zero BH mountpoints on rtk2go, Centipede, or EarthScope.

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
**yearly_cost_normalized**: 366
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
**yearly_cost**: 19,000 UAH/yr (~$460/yr) geodesy annual (VAT incl.; list ~19,900 UAH/yr);
               agro variant: 19,200 UAH/yr; shorter terms (1/3/6 mo) available.
               Observed 2026-05-07 via reseller gpsgeometer.com
**yearly_cost_normalized**: 460
**stations**:  200+
**operator**:  Системи Солюшнс (Swiss-Ukrainian joint venture); brand: UA-System.NET
**source**:    systemnet.com.ua, gnss.org.ua; reseller gpsgeometer.com (observed 2026-05-07)

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
**yearly_cost_normalized**: 256
**stations**:  unknown
**operator**:  TNT-TPI (formerly TNT-TPI GNSS Network); offices in Kyiv and Dnipro
**source**:    rtkhub.com, net.tnt-tpi.com (monitoring portal)

Nationwide commercial RTK network, rebranded from TNT-TPI GNSS Network to RTK HUB. Monitoring
portal at net.tnt-tpi.com. Host:port withheld — disclosed after registration. Most affordable
of the three major Ukrainian commercial networks.

**missing**: confirm host:port for documentation.

---

## kyivstar_rtk — Kyivstar mAgri.RTK (UA)

**status**:    paid
**date_added**: 2026-05-06
**country**:   UA
**host:port**: `rtk.kyivstar.ua:2101` (Trimble Ntrip Caster 5.2; confirmed 2026-05-06)
**type**:      physical-coord-vrs (VRS + Nearest; Trimble Pivot Platform)
**access**:    paid; requires active Kyivstar business contract subscription; individual
               subscriptions available; Starlink variant (mAgri.RTK 365 StarLink)
               for areas with unstable mobile connectivity
**registration**: `https://kyivstar.ua/business/products/geodesiya`
**yearly_cost**: 17,700 UAH/yr (~$430/yr) GEO 365; monthly 5,550 UAH (~$135/mo);
               7-day 1,800 UAH; daily 450 UAH; 7-day trial UAH 2
**yearly_cost_normalized**: 430
**stations**:  97 physical base stations (Trimble equipment; nationwide monitoring 24/7)
**operator**:  Kyivstar (Veon Group — Ukraine's largest mobile operator)
**source**:    kyivstar.ua/business/products/geodesiya (observed 2026-05-06)

Sourcetable confirmed 2026-05-06: 14+ mountpoints including VRS (RTCM3Net), VRS_old
(RTCM 3.1), Nearest_MSM5, Nearest_MSM7, Nearest (RTCM 3.4 MSM4), UCS2000 zone mounts,
MSK local coordinate system mounts (MSK_80, MSK_05, MSK_07, MSK_12, MSK_14, MSK_18,
MSK_21). GPS+GLO+GAL+BDS+QZS. Uses xFill Premium for signal continuity during outages.
All networks pause during air-raid alerts in affected oblasts. Coverage in occupied and
front-line territories severely degraded.

---

## ngcnet — NGCNET (UA)

**status**:    other
**date_added**: 2026-04-30

Listed in FIG pub74 global CORS directory as a Ukrainian network (ngcnet.com.ua). Domain has
no DNS A record (DoH lookup 2026-05-07 returns SOA-only for the `com.ua.` parent zone);
defunct or absorbed into another network. No viable endpoint.

---

## tpos — TPOS (IT — Trentino)

**status**:    free
**date_added**: 2026-04-30
**host:port**: `194.105.50.232:2101` (bare IP; confirmed SOURCETABLE 200 OK 2026-05-07; tpos.provincia.tn.it is the SBC portal domain, does not resolve as NTRIP caster)
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
**date_added**: 2026-05-06
**host:port**: `62.101.0.40:2109` (SOURCETABLE 200 OK on port 2109, 2026-05-07; port 2101
               on same IP refused; domain: `www.stpos.it`)
**type**:      physical-coord-vrs
**access**:    registration; free; Leica Spider Business Center portal; requires ID scan + declaration
               of intended use to activate RTK access; RINEX available immediately after registration;
               no professional licence restriction
**registration**: https://www.stpos.it
**stations**:  10
**operator**:  Ufficio Catasto / Amt für Kataster, Provincia Autonoma di Bolzano / Autonome Provinz Bozen
**source**:    stpos.it (PAB — Provincia Autonoma di Bolzano)

South Tyrol Positioning Service. 10 physical reference stations (Bozen, Bruneck, Corvara,
Feldthurns, Helm-M.Elmo, Latsch, Mals, Merano2000, Prettau, Vipiteno). Bilingual (German/Italian).
Note non-standard port 2109. Additional documentation step (ID + intended-use declaration) is
light — no professional credential required; RINEX archive available without it.

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

**status**:    other
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
**yearly_cost_normalized**: 293
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
**type**:      vrs-only (anonymous sourcetable)
**access**:    free; self-service registration at acorn-gnss.net (no professional licence field)
**pipeline-access**: registration
**stations**:  39 physical reference stations underlying 4 regional VRS solutions + 1 experimental
**source**:    acorn-gnss.net (Alaska DNR — Division of Mining, Land & Water, Survey Section)
**operator**:  Alaska DNR, in partnership with DOTPF, NPS, and EarthScope
**last_researched_date**: 2026-05-13

Trimble Pivot Web (NTRIP Trimble Ntrip Caster 5.2). Caster serves both VRS network-RTK
and a nearest-station single-base stream. Live sourcetable (2026-05-13) lists 8 STR
mountpoints: `MS_RTCM3` (connects to nearest station), `VRS_SouthCentral_RTCM3` (+CMRx),
`VRS_Interior_RTCM3`, `VRS_SouthEast_RTCM3` (+CMRx), `VRS_NorthWest_RTCM3`, and
`VRS_NortonSound_RTCM3_EXPERIMENTAL` (Seward Peninsula / Norton Sound). All eight
mountpoints declare GPS+GLO+GAL+BDS — upgrade from the older GPS+GLO-only configuration.
Anonymous sourcetable exposes only VRS and MS_RTCM3 mountpoints; individual physical
station streams visible only after login. Raw single-base streams from named physical
stations also accessible via the NPS caster at `rtk.nps.gov:2101`. Registration is
self-service; the "Organisation" field on the login page is present but its requirement
is not clarified in public documentation.

---

## nps_cors — NPS CORS (US + territories)

**status**:    free
**host:port**: `rtk.nps.gov:2101`
**type**:      single-base
**access**:    conditions — credentials provisioned by emailing gnss_posnav@nps.gov; restriction scope unclear
**pipeline-access**: conditions
**stations**:  141 active mountpoints (live sourcetable 2026-05-13; the seven stations previously offline — DESO, GAA2, GAA3, HALE, HAVO, PAAL, SAJU — are all back)
**source**:    ntrip.nps.gov (portal) / rtk.nps.gov (NTRIP caster), National Park Service
**operator**:  National Park Service (NPS)
**last_researched_date**: 2026-05-13

RTCM 3.2 (most stations) / RTCM 3.4 (newest), 1-second single-base streams; declared
message set `1004(1),1005/1007(5),PBS(10)`. 141 active mountpoints spanning CONUS,
Alaska, Pacific (Hawaii, American Samoa), Marianas; includes ACORN physical stations in
Alaska. Constellations: GPS+GLO+GAL+BDS network-wide per live sourcetable — upgrade from
the earlier MSM4 GPS-only configuration documented in 2022. Portal at ntrip.nps.gov;
NTRIP caster endpoint is rtk.nps.gov:2101. Datum: NAD 1983 (2011) 2010.0; MYCS3 (NGS
Multi-Year CORS Solution 3, ITRF2020 epoch 2020.00) applied 2026-02-13 using August 2025
data. Accounts provisioned manually by NPS staff via gnss_posnav@nps.gov; no public
eligibility policy — described internally as supporting NPS mapping and survey projects,
but access has been extended to ACORN partners and external contractors. Not in
pipeline (credentials required; sourcetable not publicly accessible).

---

## remos_ven — REMOS (VE)

**status**:    free
**host:port**: not publicly confirmed
**type**:      unknown
**access**:    intended free (IGVSB government service; Stonex Venezuela advertises
               free NTRIP for RTK equipment users via IGVSB)
**stations**:  ~8 listed on IGVSB website; 27 NTRIP-capable out of 29 permanent as
               of 2012 SIRGAS bulletins
**source**:    igvsb.gob.ve (IGVSB — Instituto Geográfico de Venezuela Simón Bolívar);
               SIRGAS Bol15/16/17; SIRGAS Americas Facebook (December 2025)
**date_added**: 2026-05-06
**last_researched_date**: 2026-05-13

Maracaibo (MARA) was the first REMOS station to stream NTRIP corrections experimentally
(Oct 2008). No public host:port or registration portal confirmed. SIRGAS bulletins
(Bol15–Bol17) documented NTRIP server capability at 27 of 29 stations by ~2012 but
never published a hostname. December 2025: IGVSB reported progress integrating CORS
stations into the SIRGAS-RT real-time caster (SIRGAS Americas Facebook post); the
narrative is unchanged at 2026-05-13. The BKG/RTCM-NTRIP global broadcaster registry
(last updated 2024-01-30) contains no Venezuela/IGVSB entry. `igvsb.gob.ve` returned
HTTP 200 on 2026-05-13 but no NTRIP caster link or registration portal is published.
GPS jamming was reported around Venezuelan territory September–December 2025 (FAA
advisory MAIQUETIA FIR, November 2025–February 2026). Infrastructure degradation
post-2018 documented in January 2026 Geo Week News article.

---

## acnovo_ve — Acnovo NTRIP (VE)

**status**:    other
**date_added**: 2026-05-06
**country**:   VE — Venezuela
**type**:      single-base
**host:port**: not publicly listed; credentials (host, port, username, password) delivered
               post-registration via acnovo.net
**access**:    paid; ~USD 20 per subscription period (billing cycle unclear — possibly
               monthly or per-session; promotional coupon codes advertised); register at
               acnovo.net / cursos.acnovo.net
**stations**:  unconfirmed count; website claims 24/7 nationwide base stations
**source**:    acnovo.net (confirmed live, last modified 2025-07-01; HTTP 200 re-confirmed
               2026-05-13); cursos.acnovo.net
**operator**:  Acnovo (private commercial; also brands as acnovo.com)
**last_researched_date**: 2026-05-13

Acnovo is a private commercial NTRIP correction provider in Venezuela, operating a grid
of base stations with RTCM 3.x output compatible with RTK receivers and drones. No public
sourcetable URL confirmed; credentials are disclosed only after subscription. Billing cycle
is not clearly stated — the training portal (cursos.acnovo.net) lists "SERVICIO GNSS NTRIP
EXPRESS" at USD 20 with a promotional coupon (code `NTRIPEXPRESS`) that may reduce the
cost to zero (validity unclear). Effective yearly cost therefore unconfirmed.
`other` status: real commercial NTRIP service in a country with no confirmed free option;
annual cost cannot be established from public sources, so the structured fields can't
carry the story.

---

## geocuba_gnss — GEOCUBA National GNSS Service (CU)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   CU — Cuba
**last_researched_date**: 2026-05-12
**type**:      single-base
**host:port**: not publicly listed
**access**:    restricted — appears limited to government and commercial survey clients;
               no self-service registration portal found
**yearly_cost**: n/a (no confirmed public service)
**stations**:  13 permanent stations (installed 2014–2019)
**operator**:  GEOCUBA (Grupo Empresarial GEOCUBA, under MINFAR —
               Ministerio de las Fuerzas Armadas Revolucionarias)
               `geocuba.cu`

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
**yearly_cost_normalized**: 480
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
**yearly_cost_normalized**: 480
**operator**:  HYFIX.AI (geodnet.com)
**source**:    geodnet.com (HYFIX.AI)

---

## geodnet_aus — GEODNET Australia

**status**:    paid
**host:port**: `aus.geodnet.com:2101`
**type**:      single-base
**access**:    paid
**yearly_cost**: $40/month
**yearly_cost_normalized**: 480
**operator**:  HYFIX.AI (geodnet.com)
**source**:    geodnet.com (HYFIX.AI)

---

## geodnet_sa — GEODNET South America

**status**:    paid
**host:port**: `sa.geodnet.com:2101`
**type**:      single-base
**access**:    paid
**yearly_cost**: $40/month
**yearly_cost_normalized**: 480
**operator**:  HYFIX.AI (geodnet.com)
**source**:    geodnet.com (HYFIX.AI)

---

## hepos — HEPOS (GR)

**status**:    paid
**date_added**: 2026-05-13
**country**:   GR — Greece
**last_researched_date**: 2026-05-12
**host:port**: `ntrip.hepos.gr:2101`
**type**:      vrs-only
**access**:    paid; individual online registration accepted; no professional licence required;
               pay-as-you-go (€90 + VAT per bundle) or flat-rate subscription
**registration**: hepos.gr
**yearly_cost**: €480/yr (~$520) ex-VAT flat-rate (unlimited); quarterly: €160 (~$170) ex-VAT
**yearly_cost_normalized**: 520
**stations**:  98 permanent reference stations covering mainland Greece and islands
**source**:    hepos.gr (KTIMATOLOGIO S.A. / Hellenic Cadastre)
**operator**:  KTIMATOLOGIO S.A. (Hellenic Cadastre)

Launched 2008; progressively upgraded to full GNSS (GPS, GLONASS, Galileo, BeiDou).
Reference system HTRS07 (Greek realization of ETRS89). Quarterly flat rate (€160)
is under the $200/yr cutoff. Online credit-card payment; no licensing check documented.

---

## uranus_gr — URANUS / TopNET Live Greece (GR)

**status**:    paid
**date_added**: 2026-05-13
**country**:   GR — Greece
**last_researched_date**: 2026-05-12
**host:port**: credentials issued after registration (uranus.gr)
**type**:      vrs-only
**access**:    paid; 3-day free trial; pricing not publicly listed; contact uranus@treecomp.gr
**yearly_cost**: not published
**stations**:  117 reference stations covering Greece and Cyprus
**operator**:  Tree Company Corporation A.E.B.E. (Treecomp) — Topcon distributor

Private commercial VRS network; distinct from HEPOS. GPS, GLONASS, Galileo, BeiDou;
advertised 99% coverage of Greece. Confirmed alive 2026-05-06 (uranus.gr HTTP 200).

---

## rompos — ROMPOS (RO)

**status**:    paid
**date_added**: 2026-05-06
**country**:   RO
**type**:      physical-coord-vrs (VRS; mountpoints include RO_VRS_3.1)
**host:port**: `rtk.rompos.ro:2101` (also `93.113.10.123:2101`); port 2105 for
               single-base product
**access**:    paid; ANCPI account required; self-service registration at epay.ancpi.ro;
               rover managed via app.rompos.ro
**registration**: `https://app.rompos.ro` (account creation at `https://epay.ancpi.ro`)
**yearly_cost**: 1,000 RON/yr (~€200/yr, VAT included); monthly: 100 RON/month (~€20/month);
               pricing set by ANCPI Order No. 16/2019 (in force since 2019-02-04)
**yearly_cost_normalized**: 220
**stations**:  86 permanent CORS stations (ETRS89); GPS+GLONASS+Galileo
**source**:    rompos.ro; ancpi.ro (ANCPI — Agenția Națională de Cadastru și Publicitate Imobiliară)
**operator**:  ANCPI — Agenția Națională de Cadastru și Publicitate Imobiliară

Caster confirmed live 2026-05-06 (SOURCETABLE 200 OK). Accuracy ±3 cm stated.
Payment via epay.ancpi.ro (card) or bank transfer (IBAN RO57TREZ701501503X017556);
activation within 1 business day. At ~€200/yr this is just at the hobbyist cutoff —
affordable for most EU-adjacent users.

Volunteer fallback: 9 Centipede nodes split across **both** the non-ISO
`ROM` code (7 nodes) and ISO `ROU` (2 nodes — `ROMS1`, `ROMS2`); both
codes are used in parallel and must be summed for the per-country total.
6 rtk2go ROU-coded bases supplement modestly. See
`docs/ntrip_research/_centipede_country_codes.md`.

---

## skpos — SKPOS (SK)

**status**:    paid
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
**yearly_cost_normalized**: 79
**stations**:  ~26 SK permanent reference stations; VRS only (SKPOS_cm service)
**notes**:     Three service tiers: SKPOS_dm (decimetre, code), SKPOS_cm
               (centimetre, RTK/VRS), SKPOS_mm (post-processing). rtk2go ~2 SVK
               bases, Centipede ~2 SVK nodes as volunteer alternative.
**source**:    skpos.gku.sk/en/o-skpos.php; skpos.gku.sk/register/

---

## tencent_rtk — Tencent RTK (CN)

**status**:    paid
**date_added**: 2026-05-13
**country**:   CN — China (mainland)
**operator**:  Tencent Location Service (lbs.qq.com)
**host:port**: `cors.tencent.com:8001` — SOURCETABLE 200 OK 2026-05-12 (`Server: TECNETCORS/1.0`,
               resolves 183.47.109.226 / 121.14.23.32, 7 mountpoints). Higher ports (`:8002`–`:8005`)
               historically advertised for different reference frames / epochs but not re-probed.
**type**:      single-coord-vrs
**mountpoints**: `RTCM32_GRC`, `RTCM32_GNSS`, `RTCM32_GNSS2`, `RTCM32_GRECJ`, `RTCM32_S1`,
               `RTCM32_C`, `RTCM32_GRECJ2` (all RTCM3X; constellation combinations G=GPS, R=GLO,
               E=GAL, C=BDS, J=QZS)
**access**:    paid; B2B/enterprise positioning as of 2026 — self-service hobbyist purchase
               deprecated from public lbs.qq.com/rtk. Survey-reseller channels still sell
               short-duration accounts. Tencent account (WeChat/QQ, Chinese phone number),
               real-name verification required.
**yearly_cost**: 2022 retail tariff (still widely reproduced by survey resellers, no primary
               post-2024 page confirmed): ¥7.88/1d · ¥18.88/3d · ¥38.88/7d · ¥128.88/30d ·
               ¥998.88/365d (~$140/yr). Current self-service pricing not confirmed.
**yearly_cost_normalized**: 140
**stations**:  2,800+ virtual network stations; 33 mainland provinces; claimed 2 cm horizontal /
               5 cm vertical, 99.99% availability
**last_researched_date**: 2026-05-12

Launched 22 August 2022 as free public beta. Access has retreated to enterprise
positioning while resellers continue to sell short-duration accounts. Foreign
hobbyist path is blocked (Tencent ID / WeChat / Chinese phone number / business
licence gate).

---

## Paid — over cutoff or structurally restricted

Brief entries only.

---

## sx_cors — Kadaster Sint Maarten CORS (SX)

**status**:    paid
**country**:   SX — Sint Maarten (Dutch part)
**date_added**: 2026-05-07
**type**:      unknown
**host:port**: not publicly listed (issued on subscription)
**access**:    paid; contact kadaster.sx
**registration**: https://kadaster.sx/services/
**yearly_cost**: XCG 3,600/yr (~USD 2,022/yr) per receiver; XCG 360/month option
**yearly_cost_normalized**: 2022
**stations**:  unknown (island is 34 km²; single station likely)
**operator**:  Stichting Kadaster- en Hypotheekwezen Sint Maarten

Paid CORS service confirmed on kadaster.sx/services (2026-05-07). No public sourcetable;
host:port issued on subscription. Targets professional surveyors. Nearest free option:
EarthScope CN59 on Anguilla (~20 km, NULA free non-commercial).

---

## orpheon — Orphéon (FR)

**status**:    paid
**date_added**: 2026-05-13
**country**:   FR — France
**last_researched_date**: 2026-05-12
**host:port**: `ntrip.reseau-orpheon.fr`; port 8500 (topography), port 7500 (agriculture)
**type**:      physical-coord-vrs
**access**:    paid; annual or multi-year subscriptions; hourly packages available;
               no professional licence required; international users may subscribe online
**yearly_cost**: €756–3,456 TTC/yr (VAT inclusive) depending on coverage area
               (departmental / regional / national) and service type (topography/agriculture);
               5% discount at 36 months, 10% at 60 months; well above $200/yr cutoff
**yearly_cost_normalized**: 824
**stations**:  ~215–220 permanent Full GNSS stations across mainland France and French
               West Indies; ~60 km average inter-station spacing
**operator**:  Géodata Diffusion SAS (part of Hexagon Group)
**source**:    reseau-orpheon.fr

VRS and i-Max (individualised MAX) mountpoints. GPS, GLONASS, Galileo, BeiDou.
Also offers pay-per-hour packages for occasional users via shop.reseau-orpheon.fr.

---

## teria — Teria (FR)

**status**:    paid
**date_added**: 2026-05-13
**country**:   FR — France
**last_researched_date**: 2026-05-12
**host:port**: `teriartk.eu:2101`
**type**:      physical-coord-vrs
**access**:    paid; annual and short-period subscriptions; no professional licence required;
               sold via resellers (i3map, Tech4Maps, D3E Geospatial, Sttl-Topographie)
**yearly_cost**: from €895 HT/yr (excl. 20% French VAT) — national unlimited RTK;
               well above $200/yr cutoff
**yearly_cost_normalized**: 976
**stations**:  ~187 GPS/GNSS permanent stations covering metropolitan France
**operator**:  Exagone SAS, on behalf of Ordre des Géomètres-Experts (OGE)
**source**:    reseau-teria.com

VRS, i-Max, MAC, FKP, PRS variants in RTCM 2.3/3.0/3.1/3.2 (MSM4/MSM5). Also offers
TERIAsat (L-band) and TERIArinex (post-processing) variants. Confirmed alive 2026-05-07
(SOURCETABLE 200 OK, Geo++ GNSMART 2.0 caster, 30+ mountpoints).

---

## grafcan_repcan — GRAFCAN REPCAN (ES-Canarias)

**status**:    paid
**date_added**: 2026-05-13
**country**:   ES — Spain (Canary Islands sub-region)
**last_researched_date**: 2026-05-12
**type**:      physical-coord-vrs (RTCM 3.2 MSM5; CMR+/RTCM 2.3 on SNMG and TIAS)
**host:port**: `195.53.241.146:2101` (also `gnss.grafcan.es`)
**access**:    paid; annual fee per device/receiver — price not publicly listed;
               purchase via tiendavirtual.grafcan.es (Tienda Virtual → Varios)
               Free for public administrations with active SITCAN contract.
               IGIC (7% — Canary Islands VAT rate) applies.
**yearly_cost**: not publicly listed (purchase via tiendavirtual.grafcan.es)
**registration**: https://pre-web.grafcan.es/servicios/red-estaciones-gnss/alta-gnss/
**stations**:  20 (AGUI, ALDE, ALJR, ANTI, ARGU, FRON, GRAF, HRIA, LIVA, MAZO,
               MORJ, OLIV, SNMG, STEI, STTE, TERR, TIAS, TRLJ, VHMO, YAIZ)
**operator**:  Cartografía de Canarias S.A. (GRAFCAN)
**source**:    grafcan.es/servicios/red-estaciones-gnss/

Regional paid network for the Canary Islands. Recommended mountpoint: `CERCANA3M`
(nearest station, automatic failover) or `GRAF3M` — network-RTK solutions are
less reliable over archipelago geometry; nearest-single-station mode is the
operator recommendation. Free RINEX archive for all 20 stations at
`gnss.grafcan.es` (no account required). Hardware updated January 2024;
REGCAN95 coordinate update applied 2024-02-01. Hobbyists should use the free
IGN SPTR service (`ergnss-tr.ign.es:2101`) as first option.

---

## signal — SIGNAL (SI)

**status**:    paid
**date_added**: 2026-05-06
**country**:   SI
**host:port**: `178.172.26.131:8080` (Trimble Ntrip Caster 5.2; confirmed 2026-05-06)
**type**:      physical-coord-vrs (VRS, MAC/MAX, individual station streams)
**access**:    paid; registration requires signed contract posted to Geodetski inštitut
               Slovenije; public bodies and students free with documentation
**registration**: `https://gu-signal.si/postopek-registracije/`
**yearly_cost**: €829.44/yr (~$905/yr) excl. VAT; €622.08 early-discount (~$680/yr);
               pay-per-use €0.12/connected minute excl. VAT
**yearly_cost_normalized**: 905
**stations**:  16 Slovenian CORS + cross-border (AT, HR, IT, HU adjacents accessible)
**source**:    gu-signal.si (GURS — Geodetska uprava Republike Slovenije)
**operator**:  GURS — Geodetska uprava Republike Slovenije (Surveying and Mapping Authority)

Sourcetable confirmed at 178.172.26.131:8080 (2026-05-06). VRS mountpoints: VRSSLO(2_3),
VRSSLO(3_1), VRSMSM5, VRSCMRx, VRSCMRp. MAC: MacSLO. Also individual station
streams. GPS+GLO (RTCM 2.3/3.1); GPS+GLO+GAL+BDS (CMRx, MSM5). Annual Slovenian VAT 22%
additional. Registration requires postal mail of signed contract — allow ~2 business days.

---

## cypos — CYPOS (CY)

**status**:    paid
**date_added**: 2026-05-13
**country**:   CY — Cyprus (government-controlled south)
**operator**:  DLS — Department of Lands and Surveys, Ministry of Interior (`dls.moi.gov.cy`)
**type**:      VRS + iMAX + FKP + MAC (Leica GNSS Spider; SBC on internal IP `213.7.195.11`)
**host:port**: runtime caster host:port issued only after subscription activation; not advertised externally
**access**:    paid subscription; profile-validation at a Citizen Service Centre (Cypriot ID or
               residence-permit-backed civil registration) — practical residency gate
**registration**: `portal.dls.moi.gov.cy/en/application_forms/engrafi-cypos/`
**yearly_cost**: **€238.00/yr per receiver** (12-month tier) or €142.80/6 months — confirmed
               from official `helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf` Figure 4
               (2026-05-12); 2nd/3rd-receiver bundles same per-receiver rate. VAT inclusivity
               not annotated (Cyprus standard 19%); auto-renewal not enabled. Activation
               within 2 working days after payment.
**yearly_cost_normalized**: 260
**stations**:  7 permanent GNSS stations (Nicosia, Limassol, Larnaca, Paphos, Paralimni, Polis,
               Evrychou) on the south coast and central plateau; in continuous 24/7/365 operation since 2010
**reference_frame**: ETRS89 / CGRS93 (Cyprus Geodetic Reference System 1993)
**last_researched_date**: 2026-05-12

CYPOS (Cyprus Positioning System) operational since 2010. North-Cyprus
areas (Turkish Republic of Northern Cyprus administration) are not covered.
Open to physical and legal persons per CYPOSNetwork.pdf, but the Citizen
Service Centre profile-validation step is the practical residency barrier
for foreign hobbyists. Service is incompatible with GPS mobile phones —
requires RTCM-capable surveying / RTK-grade GNSS receiver.

**Free alternative for Nicosia area**: the IGS NICO station (Nicosia,
Higher Technical Institute) streams real-time on multiple casters — via
Geoscience Australia's AUSCORS (`ntrip.data.gnss.ga.gov.au:2101`, single
GA account; see `auscors`) **and** via all three EUREF-IP federated
broadcasters (BKG `euref-ip.net:2101`, ROB `www.euref-ip.be:2101`, ASI
`euref-ip.asi.it:2101`, per-broadcaster registration; see `euref_ip`).
Both paths carry the same `NICO00CYP0` mountpoint, RTCM 3.2 GPS+GLO
dual-freq, ITRF2020 current epoch — free, no commercial split. Single
base, useful L1+L2 baseline ~30 km from the Nicosia campus. CYPOS remains
the only path to island-wide network RTK.

---

## swepos — SWEPOS Network RTK (SE)

**status**:    paid
**date_added**: 2026-05-06
**country**:   SE
**type**:      vrs-only
**host:port**: `nrtk-swepos.lm.se:80` (also port 8500); DGNSS tier: `dgnss-swepos.lm.se:2101`
**access**:    paid; free DGNSS tier sub-metre only (out of scope for cm-grade RTK)
**registration**: `https://www.lantmateriet.se/en/geodata/our-products/product-list/swepos-network-rtk/`
**yearly_cost**: 12,000 SEK/yr (~$1,050/yr) for 1–3 subscriptions; 90-day block 5,000 SEK; 1,000-min pot 5,000 SEK (valid 12 months)
**yearly_cost_normalized**: 1050
**stations**:  ~480 reference stations nationwide (SWEREF 99 / ETRS89)
**source**:    lantmateriet.se (Lantmäteriet — Swedish National Land Survey)
**operator**:  Lantmäteriet — Swedish National Land Survey

Confirmed 12,000 SEK/yr from official Lantmäteriet subscription page 2026-05-06. Earlier
entries referencing ~9,000 SEK were stale. 10-day free trial for new customers. Nordic
add-on: Finland +7,000 SEK/yr, Norway (CPOS) +5,000 SEK/yr. IoT/M2M SIM option for
annual subscribers. RTCM 3.4 MSM4 (GPS+GLONASS+Galileo+BeiDou) via MSM_GNSS mountpoint.

---

## cpos — CPOS/ETPOS (NO)

**status**:    paid
**date_added**: 2026-05-06
**country**:   NO
**host:port**: `159.162.103.14:2101`
**type**:      vrs-only
**access**:    paid; 1-month free trial for new customers; no professional licence required;
               ETPOS post-processing included with all subscriptions
**registration**: kartverket.no
**yearly_cost**: NOK 11,000/yr (~$1,020) Standard (surveying); NOK 5,000/yr (~$460) Landbruk
               (agriculture); NOK 8,000/yr Fast (fixed installation) — all ex-VAT; agriculture
               tier is lowest recurring commitment
**yearly_cost_normalized**: 460
**stations**:  280+ permanent geodetic stations; ~5,000 active users
**source**:    kartverket.no (Kartverket — Norwegian Mapping Authority)

---

## gpsnet_dk — GPSnet.dk (DK)

**status**:    paid
**date_added**: 2026-05-13
**country**:   DK — Denmark
**last_researched_date**: 2026-05-12
**type**:      vrs-only (Trimble VRS technology)
**host:port**: not published; SIM-card-based delivery model (contact geoteam.dk)
**access**:    paid; short-term logins (1 week / 1 month / 3 months) and annual surveying,
               agriculture, construction, drone tiers available
**yearly_cost**: not publicly listed (price shown after login/quote)
**registration**: https://www.geoteam.dk/produkter/gpsnetdk
**operator**:  Geoteam A/S, Ballerup (registered 2008; approved by Klimadatastyrelsen)
**source**:    geoteam.dk

Denmark's primary cadastral VRS network. Contributes 13–15 state stations from
Klimadatastyrelsen. Registered and approved by Klimadatastyrelsen for cadastral use.
Not added to pipeline: no published host:port and paid service.

Volunteer fallback for DK hobbyists: 17 rtk2go DNK bases + **18 Centipede
nodes** split across two parallel Centipede codes — 8 `DNK` + 10 `DAN`
(both mean Denmark; the non-ISO `DAN` code is used in parallel with ISO
`DNK` and earlier research counted only the latter). All cluster in
Jutland; near-zero Centipede coverage in Sjælland. See
`docs/ntrip_research/_centipede_country_codes.md`.

---

## rtkconnect_dk — RTKconnect (DK)

**status**:    paid
**date_added**: 2026-05-13
**country**:   DK — Denmark
**last_researched_date**: 2026-05-12
**type**:      vrs-only (FKP + VRS; RTCM3, L1/L2/L5, MSM7; GPS+GLO+GAL+BDS)
**host:port**: not published; provided after subscription (contact rtkconnect.dk)
**access**:    paid; single-login per subscription, unlimited devices; no professional
               licence required
**yearly_cost**: 6,599 DKK/yr (~$840/yr)
**yearly_cost_normalized**: 840
**registration**: https://rtkconnect.dk/products/rtk-netvaerk
**operator**:  RTKconnect ApS, Holstebro (registered 2024)
**source**:    rtkconnect.dk

Newest Danish commercial VRS network (est. 2024). 111 stations including 13 from
Klimadatastyrelsen; avg baseline 10 km; Class A typical (<1 cm horizontal, <2 cm vertical).
100% uptime reported (last 365 days). Over $200/yr hobbyist cutoff. Not added to pipeline:
paid service and no published host:port.

---

## swipos — swipos (CH)

**status**:    paid
**date_added**: 2026-05-13
**country**:   CH — Switzerland
**operator**:  swisstopo — Federal Office of Topography (Bundesamt für Landestopografie)
**host:port**: `www.swipos.ch:2101` (plain TCP) · `www.swipos.ch:2102` (TLS / NTRIP-2 SSL — recommended; credential-gated)
**type**:      vrs-only (VRS computed from 31 AGNES permanent stations + neighbouring country stations)
**access**:    paid; *Geoinformationsgesetz* SR 510.62 classifies RTK as value-added service;
               individuals and foreign users may subscribe; no professional licence required
**yearly_cost**: CHF 1,500/yr (~$1,650) first licence; CHF 600/yr 2nd–3rd; CHF 200/yr each additional;
               pay-per-use CHF 0.50/min; swipos-INFRA CHF 310/mo/station for raw access. All fees net of 8.1% VAT.
**yearly_cost_normalized**: 1650
**registration**: https://shop.swipos.ch
**signals**:   GPS+GLO+GAL+BDS; **RTCM 3.4 MSM4** rolled in 2026 (mountpoints `MSM_GISGEO_LV95LN02`,
               `MSM_GISGEO_LV95LHN95`); legacy RTCM 3.1 GPS+GLO via `VRS_GISGEO_*` mountpoints
**last_researched_date**: 2026-05-12

Switzerland's national VRS RTK service; 31 AGNES stations backbone. SOURCETABLE
200 OK confirmed via curl on 2026-05-12 (`Server: NTRIP Trimble Ntrip Caster 5.2`);
4 mountpoints. swisstopo's docs now recommend MSM4 + secure NTRIP over port 2102.
swipos-NAV (sub-metre DGNSS) remains free but is out of project scope. Data volume
~3 MB/hour for RTCM 3 + NTRIP per swisstopo documentation. Liechtenstein has no
independent caster and falls back on swipos or APOS.

Volunteer fallback: 20 CHE-coded rtk2go bases + 30 CHZ Centipede nodes
(2026-05-13) covering the Plateau and Jura corridor (Bern, Lausanne,
Yverdon, Basel/Solothurn, Zürich, Eastern Switzerland) — meaningful free
alternative to swipos for hobbyists in those zones. Centipede uses the
non-ISO code `CHZ` for Switzerland; Czech Republic stations are under
`CZE` separately (see `docs/ntrip_research/_centipede_country_codes.md`).
Wayback snapshots of the legacy `caster.centipede.fr:2101` sourcetable
show steady community build-out — 7 CHZ stations in 2023-01, 10 in
2024-01, 18 in 2025-01, 30 in 2026-05 — i.e. a real ~4× growth over three
years, not a sudden recent appearance as the 2026-05-06 research had
mistakenly recorded.

---

## os_net — OS Net (GB)

**status**:    other
**date_added**: 2026-05-13
**country**:   GB — Great Britain
**last_researched_date**: 2026-05-12
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
under the project's ~$200/yr affordability cutoff. Topcon TopNet Live's
7-day Unlimited at £100 ex VAT is the shortest available paid block but
annualises to ~£5,200/yr if used weekly — a one-off pass, not an affordable
subscription.

Volunteer fallback: 60 GBR-coded rtk2go bases + 45 Centipede nodes
(sourcetable 2026-05-13). **Centipede uses the non-ISO code `ENG` for the
entire United Kingdom — England *and* Scotland *and* Wales *and* Northern
Ireland** (coordinate spot-checks confirm Scottish, Welsh, and NI stations
all under `ENG`; see `docs/ntrip_research/_centipede_country_codes.md`).
Northern Ireland in particular relies on Centipede `ENG` nodes since OS
Net itself does not cover NI; NI users have no other free national source.

---

## osi_gnss — OSi Active GNSS Network (IE)

**status**:    other
**date_added**: 2026-05-13
**country**:   IE — Ireland
**operator**:  Tailte Éireann (formerly Ordnance Survey Ireland; consolidation complete);
               OSNI (`nidirect.gov.uk/osni`) for Northern Ireland
**type**:      physical single-base (RINEX archive free; real-time wholesaled to commercial resellers)
**host:port**: not publicly listed for real-time; RINEX free via `gnss.tailte.ie`
**access**:    RINEX post-processing files free (account required); real-time NTRIP via
               commercial Trimble VRS Now / HxGN SmartNet / TopNET Live only — Tailte Éireann
               does not operate a public real-time caster
**yearly_cost**: closest published IE real-time tariff is **Trimble VRS Now via Hitechniques**
               (`hitechniques.ie`, live 2026-05-13): €980/yr/100h excl. VAT (~€1,205 incl. 23% VAT);
               **€1,390/yr/600h excl. VAT** (~€1,710 incl. VAT). Pricing has been **flat since at
               least 2020** per Wayback Machine snapshots (600h = €1,390 in 2020-01 / 2023-01 /
               2024-01 / 2025-01 / 2026-05; 100h = €980 in 2023-01 / 2026-05). The
               previously-noted €590/yr/600h figure was a research error (wrong product or
               reseller), **not** a real price increase. HxGN SmartNet IE coverage via UK
               partners. The administrative migration `gnss.osi.ie` → `gnss.tailte.ie` is
               complete (legacy URL serves redirect notice 2026-05-12).
**stations**:  ~24 active GNSS reference stations (RoI + OSNI collaboration)
**source**:    tailte.ie/services/geodetic/; hitechniques.ie
**last_researched_date**: 2026-05-12

Tailte Éireann's active GNSS network supports geodetic infrastructure and
free RINEX download but does not expose a public NTRIP stream. Volunteer
backstops: rtk2go (10 IE bases) and Centipede (8 IE bases — east-coast cluster).

---

## sirent — SiReNT (SG)

**status**:    paid
**date_added**: 2026-05-06
**country**:   SG
**type**:      physical-coord-vrs (VRS; Trimble Pivot Platform 4.7)
**host:port**: `199.184.151.36:2101` (confirmed 2026-05-06; older published IP:
               `203.127.20.71:2101`)
**access**:    paid; 3-day trial (one per calendar month) with SingPass or CorpPass
               login — SingPass requires Singapore NRIC/FIN (foreign residents may
               apply for Singpass Foreign User Account via SFA); CorpPass requires a
               Singapore-registered entity. Non-resident visitors have no viable
               access path.
**registration**: `https://app.sla.gov.sg/sirent`
**yearly_cost**: S$107/month (~S$1,284/yr, ~$960/yr); S$64.20/month (10–50 accounts);
               S$32.10/month (51+ accounts); one-time S$32.10 admin fee
**yearly_cost_normalized**: 970
**stations**:  5 physical reference stations (SNTU @ Nanyang Technological University,
               SKEP @ Keppel Club, SLOY @ Loyang, SSEK @ Senoko, SNYP @ Nanyang Polytechnic).
               Earlier docs cited 8 codes (SLYG, SNPT, SNUS, SNYU, SRPT) extracted from a
               sourcetable read; those codes appear to be densification / structural-monitoring
               mountpoints, not the canonical 5-station service network confirmed by SLA
               documentation and Wikipedia.
**source**:    app.sla.gov.sg/sirent (SLA — Singapore Land Authority); Wikipedia (SiReNT)
**operator**:  SLA — Singapore Land Authority

---

## mbcrtk — MBC RTK / B-RTK (KR)

**status**:    restricted
**date_added**: 2026-05-08
**country**:   KR
**type**:      physical-coord-vrs (B-RTK platform; NTRIP + DMB + ATSC 3.0 distribution)
**host:port**: not publicly listed; correction stream gated behind hardware purchase
**access**:    restricted; no public consumer NTRIP signup. Access bundled with custom
               B-RTK receiver hardware (SMC-3000 / MRD-1000 / MRP-2000 / TDR-3000 /
               MGI-2000 product family) sold to fleet, automotive, and OEM integrators.
               No published end-user pricing; sales gate is "Technical Information
               Service Team", +82 2-789-1646 (homepage 2026-05-08). No self-serve path
               for hobbyists at any price.
**stations**:  140+ base stations nationwide (operator's own claim, 2026-05-08)
**source**:    rtk.mbc.co.kr/eng (HTTPS 200 verified 2026-05-08)
**operator**:  MBC — Munhwa Broadcasting Corporation (terrestrial broadcaster)

National Korean broadcast+telecommunication-integrated RTK service operating since
~2017; partnership with US BitPath announced 2024-05-29 to extend the same B-RTK
platform across US ATSC 3.0 broadcasters. Supports GPS+GLONASS+BDS+Galileo+QZSS,
RTCM 3.4. Hobbyist-relevant only as context; the free hobbyist path in KR is
`cors_korea` (Network 1, GNSS Data Center). Marker tier: `restricted`.

---

## soi_cors — SoI CORS (IN)

**status**:    paid
**date_added**: 2026-05-13
**country**:   IN — India
**last_researched_date**: 2026-05-12
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
**yearly_cost_normalized**: 745
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
**date_added**: 2026-05-13
**country**:   IN — Tamil Nadu
**last_researched_date**: 2026-05-12
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
**yearly_cost_normalized**: 247
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
**yearly_cost_normalized**: 266
**stations**:  65 (24 Geodetic CORS + 41 NRTK CORS); commissioning completed 2019
**source**:    vngeonet.vn; gddt.vngeonet.vn (National Centre for Satellite
               Positioning Station Management / Trung tâm Quản lý trạm định vị
               vệ tinh quốc gia). Operator string in sourcetable: `DoSM` (Department
               of Survey, Mapping and Geographic Information / Cục Đo đạc, Bản đồ
               và Thông tin địa lý). Parent ministry: MONRE until late 2025; from
               2026 the merged Ministry of Agriculture and Environment
**last_researched_date**: 2026-05-12

Three-port caster: port 2101 VRS network solution, port 2102 iMAX network
solution, port 2103 single-base. Sourcetable probe `vngeonet.vn:2101` 2026-05-12
returned SOURCETABLE 200 OK with 20 VRS mountpoints (all `VRS.*M3`/`M6` Leica
Spider products, GPS+GLO+GAL+BDS+QZSS, NMEA-driven, listed at network reference
point 20.67°N 105.53°E); server header `GNSS Spider 7.7.1.9072/1.0`. Foreign-receiver
users should test `VRS.WGS84` first.

---

## gnssnet_hu — GNSSnet.hu (HU)

**status**:    paid
**date_added**: 2026-05-13
**country**:   HU — Hungary
**last_researched_date**: 2026-05-12
**type**:      vrs-only
**host:port**: `ntrip1.gnssnet.hu:2101` (primary, Budapest); `ntrip2.gnssnet.hu:2101`
               (backup, Penc/KGO) — two independently operating, identically configured servers
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
               `gnssnet.hu/pdf/gnss_valosideju_szolg_arak.pdf` (2026-05-07).
**yearly_cost_normalized**: 415
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
**yearly_cost_normalized**: 462
**stations**:  78 physical base stations (VBS virtual output)
**source**:    egnss.nlsc.gov.tw (NLSC/MoI — 國土測繪中心)

---

## myrtk — MyRTKnet (MY)

**status**:    paid
**date_added**: 2026-04-29
**last_researched_date**: 2026-05-12
**country**:   MY
**type**:      VRS / single-base / network DGPS (multiple correction types: VRS,
               MAC, iMAX, SB Peninsular, SB Sabah & Sarawak, RINEX)
**host:port**: `pxy.myrtknet.gov.my:2101` (VRS/MAC/iMAX/DGPS),
               `:2102` (SB Sabah & Sarawak), `:2103` (SB Peninsular)
**access**:    paid; registration mandatory; cost-recovery basis under Survey Act;
               private-sector users pay both a one-time registration fee and an
               annual subscription fee; government departments pay reduced registration
**registration**: `myrtknet.jupem.gov.my`
**yearly_cost**: RM 3,000/yr (~$670/yr at May 2026 rates) real-time subscription
               + RM 1,000 one-time registration (private sector; RM 500 for
               government). Over $200/yr hobbyist cutoff. SST status for
               JUPEM subscriptions not confirmed; prices as published.
**yearly_cost_normalized**: 745
**stations**:  ~78 physical reference stations (65 Peninsular + ~13 Sabah & Sarawak;
               30–150 km spacing, average >150 km in East Malaysia)
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
**yearly_cost_normalized**: 95
**stations**:  52
**operator**:  NAMRIA — National Mapping and Resource Information Authority
**source**:    namria.gov.ph; pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx

---

## czepos — CZEPOS (CZ)

**status**:    paid
**date_added**: 2026-05-13
**country**:   CZ — Czech Republic
**last_researched_date**: 2026-05-12
**type**:      VRS (network solution)
**host:port**: czepos.cuzk.gov.cz:2101 (RTK3 MSM, RTCM 3.2); port 2111 (legacy Leica Spider proxy)
**access**:    free for public authorities, schools, universities, and students; all
               other users (commercial, hobbyist) charged under ČÚZK Decree 31/1995 Sb.
               as amended by 383/2015 Sb.: ~80 CZK+VAT/hr or ~10,000 CZK/yr (~€400)
               flat-rate per receiver. Registration at czepos.cuzk.gov.cz.
**yearly_cost**: ~10,000 CZK/yr (~€400) per receiver (commercial); over €200/yr hobbyist cutoff
**yearly_cost_normalized**: 437
**stations**:  ~30 CZ permanent stations (recent additions: Opava 2026, Olomouc 2024) +
               27 foreign-network stations; VRS (MAX, iMAX, VirtualRS)
**notes**:     Three service tiers: DGPS (~20 CZK/hr), RTK single-base, VRS3 (network
               solution ~80 CZK/hr). Not a general hobbyist path. Private alternative:
               TopNET (GB-geodezie, topnet.gb-geodezie.cz:8006, ~75 CZK/hr), same price
               bracket. Centipede ~3 CZE nodes, rtk2go ~4 CZE bases as volunteer alternative.

---

## agros — AGROS (RS)

**status**:    paid
**date_added**: 2026-04-29
**country**:   RS
**type**:      VRS (Trimble VRS Now backbone)
**host:port**: agros.rgz.gov.rs:2101
**access**:    paid; registration via rgz.gov.rs (Serbian portal)
**yearly_cost**: 8,688 RSD/yr (~€74/yr) RTK flat-rate; 5,379 RSD/yr (~€46/yr) DGPS flat-rate; hourly/monthly packages available
**yearly_cost_normalized**: 81
**stations**:  ~30 permanent CORS
**source**:    rgz.gov.rs (Republički geodetski zavod — RGZ)

Serbia's national CORS network. RTK flat-rate is paid-affordable (~€74/yr, under $200/yr cutoff).
Pricing confirmed from official Uredba (regulation) published by RGZ; Serbian portal only.

---

## geonet_bg — GeoNet Bulgaria GEO-RTK (BG)

**status**:    paid
**date_added**: 2026-05-13
**country**:   BG — Bulgaria
**last_researched_date**: 2026-05-12
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
**yearly_cost_normalized**: 660
**stations**:  certified per Instruction РД-02-20-25/2011 by АГКК (Agency for
               Geodesy, Cartography and Cadastre); Certificate of Conformity
               No. 013/2020 renewed to 2026 (per 2024-07-01 news)
**source**:    geonet.bg; geonet.bg/help.html; geonet.bg/abonamenti.html
**operator**:  Зенит-Гео ЕООД (Zenit-Geo Ltd) — commercial private operator;
               distribution via Солитех АД (Solitech AD), official Trimble
               reseller for Bulgaria

GEO-RTK is GeoNet Bulgaria's commercial network RTK / VRS service. Provides
absolute position accuracy within ~2 cm. No free hobbyist tier. AGKK (the
state Geodesy, Cartography and Cadastre Agency) certifies GeoNet but
operates no competing free service. BULiPOS (`bulipos.eu`, operated by iPOS
Ltd. with the Institute of Water Problems / BAS and the Bulgarian Aerospace
Agency) is a research-oriented network — no public NTRIP RTK service or
self-service registration found.

Volunteer fallback: 6 BGR-coded rtk2go bases (`BG-BRESTOVO-ST`, `DR_TODOROV`,
`MESTY`, `Pernik` Sofia region, `Me4etoagro` central east, `RUSE_BG`) plus
2 Centipede nodes (`AGROEKIP` Varna area, `BGDD` central north) provide
partial single-base RTK coverage of central / northern / eastern Bulgaria,
no signup.

**investigate**: re-verify the 04.2026 Solitech tariff PDF (not accessible
from the 2026-05-12 research environment); clarify whether private
individuals without business registration can sign a contract with Solitech.

---

## moldpos — MOLDPOS (MD)

**status**:    paid
**date_added**: 2026-05-06
**country**:   MD
**type**:      physical-coord-vrs
**host:port**: `185.108.183.29:8080` (Leica Spider; non-standard port 8080)
**access**:    paid subscription; registration via SBC portal
               `moldpos.ingeocad.md/SBC/Account/Register`; free test zones
               available without subscription (mountpoints FZUTM, FZUASM, FZMA,
               FZINGEOCAD, FZCDEIC; credentials `moldpos` / `moldpos`)
**yearly_cost**: MDL tariff schedule not published online; contact via
                 `ingeocad.md` for current rates
**stations**:  10+ (launched with 10 in 2011; 5 additional Leica Spider licences
               procured 2025 for expansion)
**operator**:  S.E. INGEOCAD under Agency for Geodesy, Cartography and
               Cadastre (AGCC), `agcc.gov.md`
**registration**: http://moldpos.ingeocad.md/SBC/Account/Register

MOLDPOS — Moldova Positioning System. Paid since AGCC Order No. 04 of
06.01.2012. Caster runs Leica Spider Business Center v7.10.0.114; VRS / MAX /
MSM mountpoints; GPS+GLONASS+Galileo. INGEOCAD explicitly markets it as "an
open network; any GPS receiver owner can join" — no surveying licence required.
Free test zones (FreeZone mounts) allow trial without subscription at five fixed
locations across Moldova. Moldova is EU candidate (2022); ETRS89-aligned.
Contact via `ingeocad.md` (Chișinău, str. Pușkin 47).

---

## makpos — MAKPOS (MK)

**status**:    paid
**date_added**: 2026-05-06
**country**:   MK
**type**:      physical-coord-vrs
**host:port**: `makpos.katastar.gov.mk:9001` (confirmed on Alberding GmbH
               worldwide NTRIP caster map; Leica GNSS Spider RT Proxi Server)
**access**:    subscription via Spider Business Center; register at
               `makpos.katastar.gov.mk/sbc/Account/Register`. One source
               indicates free of charge for users with compatible GNSS devices
               on 3G/GPRS — unconfirmed if still current; contact AREC to confirm
**yearly_cost**: MKD schedule not publicly posted; contact AREC Sector for
                 Geodetic Works (`katastar.gov.mk/en/about-us/contact/`)
**stations**:  14 reference base stations at 50–70 km spacing (~25,700 km²)
**operator**:  Agency for Real Estate Cadastre (AREC), `katastar.gov.mk`
**registration**: https://makpos.katastar.gov.mk/sbc/Account/Register

MAKPOS — Macedonian Positioning System. Services: DGPS (0.3–0.5 m, RTCM 2.x),
RTK (2–4 cm, RTCM 2.x/3.x), precise positioning (<1 cm, RINEX). Galileo support
added April 2020. Portal: makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx. Caster
independently confirmed reachable on Alberding GmbH worldwide caster map (port 9001).
No professional licence requirement documented.

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
**date_added**: 2026-05-13
**country**:   BA — Bosnia and Herzegovina (Republika Srpska entity)
**last_researched_date**: 2026-05-12
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
**yearly_cost_normalized**: 578
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
FBiHPOS (Federation of BiH) is documented separately. Volunteer fallback: 1
rtk2go base `AGROORSOLIC` at 45.01°N 18.60°E in Posavina (northern Bosnia,
near Orašje); zero Centipede BA nodes. Within ~150–200 km of central Bosnia
the nearest free rtk2go cluster is on the Serbian side.

---

## fbihpos_ba — FBiHPOS (BA — Federation of BiH)

**status**:    paid
**date_added**: 2026-05-13
**country**:   BA — Bosnia and Herzegovina (Federation entity)
**last_researched_date**: 2026-05-12
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
**yearly_cost_normalized**: 597
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
**type**:      VRS (8 CORS stations + computation centre in Pristina; Leica GNSS Spider /
               Spider Business Center v7.8.1.438; RTCM 2.3 FKP + VRS; GPS+GLONASS+Galileo)
**host:port**: `kopos.rks-gov.net:2101` (IP 91.239.145.45; Spider Business Center login
               portal; NTRIP mountpoints and credentials provided inside portal
               post-login). TCP probes to port 2101 timed out from external IP
               2026-05-06 and 2026-05-12 — likely geo-firewalled outside Kosovo;
               credentials are issued via the SBC HTTPS portal which remains reachable
**access**:    paid; annual subscription + one-time registration fee; register at akk.rks-gov.net; no surveying-licence requirement found
**yearly_cost**: €400/yr (~$468); plus €20 one-time registration fee. Shorter durations
               available: €250/6 months, €60/month. RINEX post-processing tier €100/yr
               or €30/month. Kosovo standard VAT 18%; tariff document does not state
               whether prices include VAT — verify at AKK
**yearly_cost_normalized**: 475
**stations**:  8 permanent CORS; RTK horizontal ±2 cm, vertical ±4 cm
**operator**:  Agjencia Kadastrale e Kosovës (Kosovo Cadastral Agency / AKK)
**source**:    akk.rks-gov.net; Administrative Instruction QRK No. 04/2024 (tariff PDF)
**last_researched_date**: 2026-05-13

Kosovo's national GNSS reference network, operated by the Kosovo Cadastral Agency (AKK)
as an EUPOS-aligned CORS network. Network commissioned 2012–2013 under a 2011 World
Bank-funded ICB contract with Leica Geosystems; eight AR25 choke-ring antenna reference
stations distributed nationwide; control centre in Pristina. AKK 04/24 tariff schedule
confirmed via the 2025 Annual Report (issued 2026-03-25) and the source PDF; pricing
unchanged since early 2024. SBC portal HTTPS alive 2026-05-13. The SBC registration
form requests rover brand, serial number, and address; no surveying licence number
required. No free hobbyist tier. Kosovo's non-UN-member status has historically
complicated EUREF/EPN participation; no confirmed EPN station.

---

## sstp_by — ССТП РБ / Belgeodesiya CORS (BY)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   BY — Belarus
**last_researched_date**: 2026-05-12
**type**:      physical-coord-vrs
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
credentials issued per-contract. Confirmed alive 2026-05-07 (sourcetable 200 OK, 47 STR,
tariff PDF and RTK manual served from geo.by). Port 8081 (previously referenced for Agro
plans) was unreachable 2026-05-07; all Agro-* mountpoints now on port 8080 — **verify
before removing the port 8081 reference from legacy docs**.

Hardware supply: EU, UK, and US sanctions applied to Belarus since 2020–2022 suspend
exports of surveying and precision-GNSS equipment (Topcon, Trimble, Leica all announced
suspension). Replacement rover hardware is materially harder to source than in
unsanctioned neighbouring states, compounding the barriers to hobbyist RTK use.

---

## scrtn — SCRTN (US-SC)

**status**:    paid
**date_added**: 2026-05-07
**type**:      vrs-only
**host:port**: `scrtn.sc.gov:2101`
**access**:    paid; subscribe at sc.accessgov.com/rfa; no professional-licence requirement
**yearly_cost**: $1,200 first login; $600 each additional (SCGS RTN Subscriber Agreement rev. 04/2023); no refunds; GPS+GLO+GAL+BDS
**yearly_cost_normalized**: 400
**operator**:  SC Revenue and Fiscal Affairs Office — SC Geodetic Survey
**source**:    scrtn.sc.gov
**last_researched_date**: 2026-05-13

43 GNSS receivers in SC plus 2 in GA and 10 in NC. SOURCETABLE 200 OK re-confirmed
2026-05-13 (14 STR entries). Stated accuracy ~2 cm horizontal / ~4 cm vertical.
Payment due at time of application; no refunds.

---

## ncrtn — NCRTN (US-NC)

**status**:    paid
**host:port**: `rtn.nc.gov:2101` (DNS 207.4.106.112)
**type**:      vrs-only
**access**:    paid; subscribe at rtn.nc.gov; no professional-licence requirement stated
**yearly_cost**: $500 one-time per login (perpetual credentials, not annual renewal); second login included with first; additional: $250 each
**yearly_cost_normalized**: 167
**operator**:  NC Geodetic Survey (NC Dept. of Environment and Natural Resources)
**source**:    rtn.nc.gov
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Trimble Pivot VRS network. Portal HTTP 200 re-confirmed 2026-05-13; NTRIP port 2101
IP-filtered (timed out from external probe). Static RINEX download is free. Payment
by cheque. Invoicing first week of month following account creation.

---

## tdot_rtn — TDOT RTN (US-TN)

**status**:    paid
**host:port**: not publicly listed; provided post-payment via portal.tndot.net
**type**:      vrs-only
**access**:    paid; subscribe at portal.tndot.net; no professional-licence requirement stated
**yearly_cost**: $450/yr (FY25 rate; payment by credit/debit via portal)
**yearly_cost_normalized**: 450
**operator**:  Tennessee Dept. of Transportation (TDOT) — Geodetics Division
**source**:    portal.tndot.net / tn.gov/tdot
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Migrated from Trimble-based to Leica-based platform 2025-02-01; pre-migration
credentials no longer valid. New users create account at portal.tndot.net → accept
T&C → pay → receive credentials. Status page: status.tndot.net. Portal HTTP 200
re-confirmed 2026-05-13.

---

## keynetgps — KeyNetGPS (US — Northeast multi-state)

**status**:    paid
**date_added**: 2026-05-13
**country**:   US — VA, DC, MD, DE, PA, NJ, NY, CT, RI, MA, VT, NH, ME
**host:port**: `vrs.keynetgps.com:2101` (IP 209.255.196.164; SOURCETABLE 200 OK 2026-05-13, 6 STR)
**type**:      vrs-only
**access**:    paid; pricing not publicly listed — contact via keypre.com or resellers
**yearly_cost**: not published
**vrs**:       yes (Trimble VRS3Net; mountpoints `VRS_CMRp`, `VRS_CMRx`, `SingleBase_CMRp`, `SingleBase_RTCM3`)
**stations**:  unknown (commercial — not disclosed)
**operator**:  Keystone Precision Solutions (Keypre)
**source**:    keypre.com/keynetgps
**last_researched_date**: 2026-05-13

Commercial subscription VRS network covering the entire US Northeast (VA through ME).
Practical paid option in NH, NJ, PA, DE, MD, DC, RI — states with no free public state
caster. Pricing not posted publicly; routed through Keypre or resellers (Laser Industries,
Duncan-Parnell). Subscriber agreement required; hobbyist eligibility not explicitly
stated. SOURCETABLE 200 OK confirmed 2026-05-13 (6 STR entries).

---

## alpha_rtk — AlphaRTK (US — Mid-Atlantic)

**status**:    paid
**date_added**: 2026-05-13
**country**:   US — DE, MD, NJ, PA, DC
**host:port**: not publicly listed; credentials issued post-subscription
**type**:      vrs-only (presumed; Trimble-based per reseller materials, unconfirmed)
**access**:    paid; 1-week free trial; subscribe via alphartk.com
**yearly_cost**: $195/month · $995/6 months · $1,595/24 months (alphartk.com, observed 2026-05-07; no annual plan)
**yearly_cost_normalized**: 798
**stations**:  unknown
**operator**:  AlphaRTK (commercial)
**source**:    alphartk.com
**last_researched_date**: 2026-05-13

Commercial paid network covering Delaware, Maryland, New Jersey, Pennsylvania, and
Washington DC. No annual plan; cheapest sustained-use is the 24-month rolling
subscription (~$798/yr equivalent). 1-week free trial available, useful for spot
jobs. Subscriber agreement required; hobbyist eligibility not explicitly stated.

---

## egps_ga — eGPS Solutions RTN (US-GA)

**status**:    paid
**date_added**: 2026-05-13
**country**:   US — Georgia (also some surrounding states)
**host:port**: not publicly listed; provided post-subscription
**type**:      vrs-only (GEO++ and eGPS VRS network products)
**access**:    paid; subscribe at egps.net
**yearly_cost**: $2,475/yr Plan A (dual network) · $1,650/yr Plan B (VRS only) · Plan C $50/day capped $400/mo · Plan D agriculture $1,000/yr (egps.net/netservices.html, 2026-05-07)
**yearly_cost_normalized**: 1650
**vrs**:       yes
**stations**:  unknown
**operator**:  eGPS Solutions (Norcross, GA)
**source**:    egps.net
**last_researched_date**: 2026-05-13

The only identified RTK network with Georgia coverage; GDOT does not operate a public
caster. No hobbyist tier — cheapest sustained option is Plan B at $1,650/yr. Plan C
"Flex" ($50/day, capped $400/mo) is the most practical for occasional use. EarthScope
NOTA provides sparse free single-base streams in Georgia as a non-commercial fallback.

---

## turn_gps — TURN GPS (US-UT + NV)

**status**:    paid
**host:port**: `165.239.144.5:2101` (NAD83/2011); `165.239.144.7:2101` (alternate / NV — account-gated; external probes time out)
**type**:      vrs-only
**access**:    paid; subscribe at turngps.utah.gov; Utah ID account required (digital identity, not residency)
**yearly_cost**: $600/yr per login (currently covers both Utah TURN GPS and Nevada GPS Network; UGRC has indicated this may split per-region in future)
**yearly_cost_normalized**: 600
**operator**:  Utah Geospatial Resource Center (UGRC), State of Utah
**source**:    gis.utah.gov/products/turn/
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Trimble Pivot VRS, 100+ stations across UT plus southern ID, western WY, and southern
NV edge coverage. Full GNSS via RTCM32 (`GNSS-VRS-NAD83-RTCM32`: GPS+GLONASS+Galileo+BeiDou).
One subscription covers UT and the Nevada GPS Network (formerly Washoe County / NNCRN,
now UGRC-administered; northern Nevada / Reno area only — Las Vegas metro is covered
instead by the application-gated LVVWD network).

---

## mtsrn — MTSRN (US-MT)

**status**:    paid
**host:port**: `mtsrn.org:2101` (SOURCETABLE 200 OK 2026-05-13, 336 STR — per-station × per-format combinations across the five subnets)
**type**:      vrs-only
**access**:    paid; subscribe at mtsrn.org; no professional-licence requirement stated
**yearly_cost**: $1,500/yr per login (rate effective July 2024; PayZang portal)
**yearly_cost_normalized**: 1500
**operator**:  Montana State Library (MSL), with MDT, tribal nations, counties, universities
**source**:    msl.mt.gov/mtsrn
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Launched March 2022; five geographic VRS subnets (NE, NC, NW, SW, SC Montana). 50+
CORS stations. Partner agencies receive access in exchange for station hosting.
Static RINEX free to public. Rates are reviewed each biennium and announced January
of odd-numbered years (next review due January 2027 for July 2027 effective date).

---

## wsrn — WSRN (US-WA)

**status**:    paid
**host:port**: `wsrn.org:2011` (NAD83/2011, 486 STR); `wsrn.org:2022` (NATRF2022 — caster live but mountpoints not yet provisioned as of 2026-05-13)
**type**:      vrs-only
**access**:    paid; subscribe at wsrn3.org; no professional-licence requirement stated
**yearly_cost**: $1,900/yr non-partner (5 logins $5,700; 10 logins $10,000; 20 logins $15,000); partner agencies (govt, NGS cooperators) receive free access
**yearly_cost_normalized**: 1900
**operator**:  Multi-agency cooperative (WSDOT + public/private partners), Trimble Pivot
**source**:    wsrn3.org
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Actively transitioning to NATRF2022 — port 2022 delivers NATRF2022; port 2011 delivers
legacy NAD83(2011); port 8080 being retired. PANGA/CWU contributes Puget Sound antennae.
SOURCETABLE 200 OK re-confirmed 2026-05-13 — port 2011 returns 486 STR rows; port 2022
returns only the CAS line (0 STR, mountpoint provisioning expected through 2H2026
alongside the NSRS modernisation roll-out).

---

## c4gnet — C4Gnet / Louisiana RTN (US-LA)

**status**:    paid
**host:port**: `c4gnet.xyz:9000` (SOURCETABLE 200 OK 2026-05-13, 32 STR)
**type**:      physical-coord-vrs
**access**:    paid; subscribe at store.c4g.lsu.edu; no professional-licence requirement
**yearly_cost**: $495/yr (10-hr RTK tier); $1,995/yr (50-hr); $3,500/yr (unlimited RTK); $5,000/yr (full RTN membership)
**yearly_cost_normalized**: 495
**operator**:  LSU Center for GeoInformatics (C4G), Louisiana State University
**source**:    c4gnet.xyz
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13

Louisiana statewide real-time network established 2007. Leica GNSS Spider platform.
Full GREC constellation (GPS+GLONASS+Galileo+BeiDou). VRS, PPP, and Nearest Single
Base (NSB) products; NAD83(2011) and ITRF2014 frames available. Free RINEX post-
processing subscription available separately. No free hobbyist tier; entry-level
10-hour RTK tier at $495/yr.

---

## crtn — CRTN / California Real Time Network (US-CA)

**status**:    paid
**host:port**: `132.239.152.4:2102` (NorCal zones 1–2), `:2103` (NorCal zones 3–4),
               `:2104` (SoCal zone 5), `:2105` (SoCal zone 6) — SOURCETABLE 200 OK on
               :2102 and :2104 re-confirmed 2026-05-13
**type**:      single-base
**access**:    paid; one-time $100 processing fee; universities and schools exempt
**yearly_cost**: $100 one-time (under the $200 cutoff) — not annual
**yearly_cost_normalized**: 33
**stations**:  ~250 across California (clearinghouse, see below)
**source**:    sopac-csrc.ucsd.edu/index.php/crtn (Scripps Orbit and Permanent Array
               Center, UC San Diego)
**operator**:  CSRC EC / SOPAC at UCSD
**last_researched_date**: 2026-05-13

Clearinghouse for real-time GNSS data from multiple California networks: SOPAC
(SCIGN), UC Berkeley/USGS Menlo Park (BARD), USGS Pasadena (SCIGN),
Caltrans (CVSRN), Orange County Public Works (OCRTN), and EarthScope NOTA
stations. RTCM 3.0, 1 Hz, latency <1 s; RTCM 3.1 available via `XXXX_RTCM3P1`
mountpoint suffix (announced October 2025). Registration via the CRTN Registration
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
**date_added**: 2026-05-13
**country**:   CA-BC — British Columbia, Canada
**last_researched_date**: 2026-05-12
**type**:      VRS (Trimble-based)
**host:port**: not publicly listed (GeoBC website reorganisation; portal URLs returning 404 as of 2026-04-30)
**access**:    paid; contact GeoBC (gov.bc.ca/geobc or 1-800-663-7867); no self-service portal currently accessible
**yearly_cost**: CAD 1,650/yr (~$1,212); statutory fee per Land Act, B.C. Reg. 55/98, confirmed to 2026-04-21
**yearly_cost_normalized**: 1212
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
**date_added**: 2026-05-13
**country**:   CA-NS — Nova Scotia, Canada
**last_researched_date**: 2026-05-12
**access**:    RINEX post-processing free via NRCan; real-time NRTK via paid commercial
               resellers only: HxGN SmartNet NA (`smartnetna.com`, CAD $3,327.96/yr Atlantic;
               CAD $6,084/yr national), Can-Net (`gps.can-net.ca`, pricing not public),
               Brandtnet (`rtk.brandt.ca`, pricing behind account login)
**yearly_cost**: CAD 3,328/yr (~$2,429/yr) — HxGN SmartNet Atlantic (NB, NL, NS, PE) plan;
               Can-Net and Brandtnet pricing not publicly listed; national SmartNet: CAD 6,084/yr (~$4,441/yr).
               GST/HST status not stated on SmartNet product page — treat as unknown; confirm at checkout.
**yearly_cost_normalized**: 2429
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
**date_added**: 2026-05-13
**country**:   AE — UAE (Dubai Emirate only)
**operator**:  Dubai Municipality, Survey Department
**type**:      VRS (network-RTK with NMEA GGA upload)
**host:port**: `geodubai.dm.gov.ae:2101` (historical; external NTRIP port not confirmed 2026-05-12)
**access**:    restricted; professional application via DM portal (surveying / construction / GIS / government contractors); no individual or hobbyist registration path
**registration**: https://geodubai.dm.gov.ae/sites/buildingsmart/en/Pages/Registration.aspx
**vrs**:       yes
**stations**:  18+ quad-constellation (GPS+GLO+GAL+BDS) reference stations across Dubai Emirate
**last_researched_date**: 2026-05-12

Dubai Virtual Reference System — first NRTK network in the Middle East
(commissioned March 2002, originally 5 Leica stations + Geo++ GNSMART;
expanded to 18+ quad-constellation stations). Aligned to the Dubai Local
Coordinate System. Corrections are RTCM streamed back on NMEA GGA upload.
Credentials are issued after DM portal application; known users are RTA,
DEWA, military departments, and licensed construction/infrastructure firms.

Portal status (2026-05-12): the `dm.gov.ae/survey-department/dubai-virtual-reference-station/`
sub-page returns errors / 404; the `geodubai.dm.gov.ae` portal pages remain
reachable. NTRIP port 2101 on the historical hostname has not been confirmed
from an external IP — the service may have migrated to unified DM e-services
infrastructure while keeping the GeoDubai portal as the application front-end.

No separate Abu Dhabi, Sharjah, or UAE-federal NTRIP caster has been
publicly documented; ADCC appears in academic NetworkRTK literature but
without a public endpoint. Zero AE mountpoints on rtk2go, Centipede, or
EarthScope.

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

**status**:    other
**date_added**: 2026-05-13
**country**:   IQ — Iraq
**last_researched_date**: 2026-05-12
**access**:    restricted; no public NTRIP caster identified
**yearly_cost**: N/A (no public NTRIP caster)
**stations**:  7
**source**:    Not publicly listed (Iraq Geodetic Reference System)

Only 7 reference stations at 500–800 km inter-station spacing — far too sparse for
RTK (baseline ≫ 100 km). No public NTRIP caster found. Documented for completeness;
not a usable RTK resource for hobbyists.

---

## dag_lb — Directorate of Geographic Affairs (LB)

**status**:    other
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

**status**:    other
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

## gas_ye — General Survey Authority (YE)

**status**:    other
**date_added**: 2026-05-13
**country**:   YE — Yemen
**type**:      unknown
**host:port**: not publicly listed
**access**:    no confirmed public NTRIP
**yearly_cost**: N/A
**stations**:  unknown; pre-conflict CORS stations operated by GAS; current status not
               verifiable
**source**:    not publicly listed (General Survey Authority / هيئة المساحة العامة; website
               unreachable 2026-05-13)
**operator**:  General Survey Authority (GAS), Yemen
**last_researched_date**: 2026-05-13

Yemen's national geodetic authority. No public NTRIP caster, open sourcetable, or
hobbyist registration portal has been found in any directory, sourcetable, or academic
reference. The country has been in active civil conflict since 2015 between Houthi
forces (Sanaa and the north-west) and the internationally recognised government (Aden);
hostilities have severely disrupted all public infrastructure including geodetic and
mapping services. The GAS website was unreachable in all searches conducted 2026-05-06
and 2026-05-13. The historic IGS site ADEN (Aden) has not appeared in current IGS
operational lists. Zero YE stations on rtk2go, Centipede, or EarthScope; `stations_by_radius.py
15.36 44.19 200` (Sanaa) returns zero results 2026-05-13. No commercial RTK provider
(GEODNET, PointOne, etc.) lists Yemen coverage. Galileo HAS (~40 cm, no internet) is
theoretically usable but of limited practical value in a conflict zone with restricted
import of GNSS equipment.

Surfaced as `other` so YE users land on a marker that explains why no service is
reachable rather than a silent gap. Do not pursue until a confirmed public NTRIP
endpoint appears in a directory or official Yemeni government announcement.

---

## otc_gnss — OTC GNSS (TN)

**status**:    paid
**date_added**: 2026-04-30
**country**:   TN
**type**:      single-base (physical coordinates)
**host:port**: not publicly listed (disclosed after subscription)
**access**:    paid subscription; register at otc.nat.tn/geodesy/gnss/subscription; no explicit eligibility restriction found
**yearly_cost**: 6,000 TND/yr (~$2,070/yr); VAT status not stated on the public subscription page; confirmed 2026-05-06
**yearly_cost_normalized**: 2070
**stations**:  23 (physical; Saharan south not covered — roughly south of Gafsa/Tozeur latitude)
**source**:    otc.nat.tn (OTC — Office de la Topographie et du Cadastre)
**operator**:  OTC (Ministère de l'Équipement et de l'Habitat, Tunisia)

Full published tier table (source: otc.nat.tn/geodesy/gnss/subscription; VAT applicability
not stated; at 1 TND ≈ $0.345, observed 2026-05-06):
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

## omancorsnet — OmanCORSnet (OM)

**status**:    restricted
**date_added**: 2026-05-06
**country**:   OM
**type**:      physical-coord-vrs (Leica GNSS Spider / Spider Business Center)
**host:port**: not publicly disclosed; issued post-registration via Spider Business Center
**access**:    restricted; registration at `omancorsnet.gov.om/SBC/Account/Index`;
               no confirmed hobbyist or individual tier; targets licensed surveying
               professionals and government users
**yearly_cost**: not publicly listed
**stations**:  47 physical CORS distributed nationwide (installed 2016 by NSA)
**operator**:  NSGIA — National Survey and Geospatial Information Authority
               (successor to NSA — National Survey Authority; under Ministry of Defence)
               Geoportal: `nsaomangeoportal.gov.om`
**source**:    nsaomangeoportal.gov.om/en/oman-corsnet; omancorsnet.gov.om
**signals**:   multi-constellation GNSS (exact mix not publicly confirmed)
**datum**:     ONGD17 — Oman National Geodetic Datum 2017 (ITRF2014, epoch 2017.0)

Forty-seven CORS installed by the National Survey Authority in 2016. Software platform
is Leica GNSS Spider (Spider Business Center), consistent with VRS capability. Datum
is ONGD17, replacing ONGD14; national geoid is OMANGEOID. The SBC login portal is
reachable from external IPs but NTRIP caster port is not publicly documented. No
confirmed individual/hobbyist registration tier; access appears gated to licensed
surveyors and government contractors. IGS station MUSK (Muscat) is a separate
EarthScope-archived observation stream, not an RTK service.

Restricted — no public host:port; no hobbyist registration path confirmed.
**missing**: confirm host:port and whether non-professional registration is possible;
contact NSGIA via nsaomangeoportal.gov.om.

---

## qcors — QCORS (QA)

**status**:    restricted
**date_added**: 2026-05-06
**country**:   QA
**type**:      unknown (9-station network with TCP/IP data centre; VRS likely)
**host:port**: not publicly disclosed; issued post-subscription via CGIS
**access**:    restricted; application to CGIS required; no public self-service registration;
               serves "government and private survey and mapping communities"
**yearly_cost**: not publicly listed
**stations**:  9 (connected via TCP/IP; ±2 cm horizontal, ±10 cm vertical claimed)
**operator**:  CGIS — Centre for GIS, Ministry of Municipality (State of Qatar)
               Portal: `gisqatar.org.qa`; GeoPortal: `geoportal.gisqatar.org.qa`
**source**:    gisqatar.org.qa/en (CGIS Services page)
**datum**:     QNSRS / QND95 (Qatar National Datum 1995)

QCORS (Qatar Continuously Operating Reference Stations) was installed 2009 and
commenced operations 2010 under the Centre for GIS, Ministry of Municipality.
Nine stations connected via TCP/IP to a central data centre; described as providing
"economical advantages against conventional GNSS surveying where two GPS units are
necessary." No public self-registration or hobbyist tier documented. CGIS also
operates a GeoPortal (geoportal.gisqatar.org.qa/qmape/) for GIS web mapping;
the CORS service is separate and gated. No publicly known NTRIP host:port.

Restricted — application-based; host:port not publicly disclosed; no individual tier.
**missing**: confirm host:port, tariff, and whether non-professional registration is
feasible; contact CGIS at `cgisinfo@gisqatar.org.qa` or +974 4426 6284.

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
**yearly_cost_normalized**: 1127
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
**yearly_cost_normalized**: 1080
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

**status**:    paid
**country**:   KZ — Kazakhstan
**type**:      physical-coord-vrs (network RTK)
**host:port**: **investigate**: likely `rtk.qgeo.kz:2101` (unconfirmed; not publicly disclosed)
**access**:    paid subscription; self-service portal at rtk.qgeo.kz; registration
               requires Kazakh ИИН (individual) or БИН (business) — de-facto
               residency requirement; foreign users cannot complete self-service
**yearly_cost**: 65,000 ₸/yr (~$141/yr)
**yearly_cost_normalized**: 141
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

**status**:    other
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

## kyrpos — KyrPOS GNSS Network (KG)

**status**:    paid
**country**:   KG
**type**:      single-base / VRS (unclear from public documentation)
**access**:    paid; contract-based sign-up via `gosreg.gov.kg/ky/?page_id=3029`;
               submit signed contract (GNSS receiver make/model/serial + period)
               then bank payment; credentials issued post-payment
**yearly_cost**: 3,180 KGS/month (~$37/mo at May 2026 rates) per receiver;
                 170 KGS/day also offered; minimum 1 month
**yearly_cost_normalized**: 444
**operator**:  State Agency for Land Resources, Cadastre, Geodesy and
               Cartography of the Kyrgyz Republic (ГАЗРКГК — Государственное
               агентство земельных ресурсов, кадастра, геодезии и
               картографии)
**registration**: gosreg.gov.kg/ky/?page_id=3029 — official KyrPOS connection
                  page with 9-step sign-up and contract template download
**host:port**: `cors.gosreg.gov.kg:8085` (non-standard port; confirmed on
               gosreg.gov.kg/ky/?page_id=3029, 2026-05-06; unreachable from
               external IP — likely geo-filtered or credential-gated)
**stations**:  18 (Chui/Bishkek 6, Fergana Valley/Osh 8, Naryn 1, Issyk-Kul 3)

**date_added**: 2026-05-06

KyrPOS is the national GNSS correction network operated by the Kyrgyz
cadastral and geodesy agency (ГАЗРКГК). Subscribers pay per month per
receiver; the minimum period is one month. Endpoint `cors.gosreg.gov.kg:8085`
is published on the official service page. Over the $200/yr threshold at monthly
billing (~$37/mo × 12 = ~$444/yr) — not viable for most hobbyists.

CAIAG (Central Asian Institute for Applied Geosciences, German-funded,
Bishkek) operates a monitoring network of 30+ GNSS stations including the
Bishkek IGS site (BIK0 / BIS2, joint with ESA/ESOC since 2016) and an
IGS tracking station at the Pamir High Mountain Observatory. These are
research facilities and do not provide an RTK correction service.

Paid — over $200/yr threshold; not viable for most hobbyists. No free public
NTRIP endpoint in Kyrgyzstan.

---

## tm_cors — Turkmenistan National CORS Network (TM)

**status**:    other
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

## uzpos — UZPOS (UZ)

**status**:    other
**country**:   UZ — Uzbekistan
**type**:      physical (CORS network; RTK service architecture per 2016–2017 literature)
**access**:    government-internal / licensed-surveyors-only; no public NTRIP endpoint
               or registration portal published
**operator**:  State Committee for Land Resources, Geodesy, Cartography and State
               Cadastre (UzGeodezKadastr); control centre in Tashkent
**registration**: https://uzgeodezkadastr.uz (HTTP 200 2026-05-13; no NTRIP portal)
**host:port**: not publicly documented
**stations**:  30–50 planned (Type-A geodetic + Type-B RTK, per Ergashev et al.
               2016–2017); active stations confirmed by 2024 quality-analysis paper
               (continuous data flow from Samarkand to Tashkent control centre)
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-13

Uzbekistan's national CORS infrastructure (UZPOS) is operated as a closed archival
service for licensed professionals and state agencies — no open NTRIP registration
path exists. Cross-checked 2026-05-13: zero UZ mountpoints on rtk2go, Centipede,
or EarthScope; project pipeline radius probe at (41.3°N, 69.3°E) returns zero
stations within 800 km of Tashkent. No commercial international caster (GEODNET,
Point One, RTKdata, SmartNet, Trimble VRS Now) advertises Uzbekistan coverage.
Hobbyists must deploy a private base station for RTK work. RINEX post-processing
is available via the IGS station TASH (EarthScope/UNAVCO; also an EPN supplementary
site). Central Asian pattern is uniformly closed-access (cf. `kazgeodesy` paid-but-
ИИН-gated, `kyrpos` paid contract-based, `tm_cors` government-internal,
`almgc_tj` no endpoint).

---

## azpos — AzPOS (AZ)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   AZ — Azerbaijan
**operator**:  State Service on Property Issues under the Ministry of Economy
               (Əmlak Məsələləri Dövlət Xidməti); operator entity "Kadastr və
               Yer Quruluşu Layihə Tədqiqat Mərkəz"
**type**:      physical-coord-vrs (Leica GNSS Spider backend)
**host:port**: `azpos.az:2101` (provisional; authentication-gated, no sourcetable
               response to unauthenticated queries — consistent with IP-whitelisting
               or authenticated NTRIP). Actual delivered hostname/port issued per subscriber.
**access**:    bilateral service agreement required; no self-service registration;
               "legal entities and individuals" may apply; process conducted in Azerbaijani
**registration**: https://www.emlak.gov.az/en/page/view/96; contact: azpos@emlak.gov.az
**stations**:  45 (37 original 2014 commissioning + 8 restored in Karabakh 2024:
               Fuzuli, Jebrail, Zangilan, Kəlbəcər ×2, Ağdam, Şuşa, Laçın)
**signals**:   GPS + GLONASS (2014 baseline); Galileo + BeiDou per recent project documentation
**last_researched_date**: 2026-05-12

AzPOS (Azerbaijan Positioning Observation System) is the national CORS
network operated by the State Service on Property Issues under the Ministry
of Economy. Originally 37 stations at 30–40 km spacing across mainland
Azerbaijan (usable RTK radius ~20 km/station, communication range up to
70 km); 8 stations were added in the Karabakh region in 2024 following the
September 2023 restoration of territorial control. Control centre supports
up to 100 parallel RTK users (2014 spec). The SBC login portal at
`azpos.az/sbc/` shows an RTK product with Subscription Period, Consumption
Limit, and Working Area fields — all values hidden pre-login. No published
tariff; ArduSimple lists AzPOS as "paid national service" without price.
The contract-based access model with a Baku office in practice favours
local residents or agents.

Volunteer: 1 rtk2go base — `WHTCTY` at 40.38°N 49.89°E in greater Baku
(country code `AZE`); useful within ~20 km. Zero AZ-coded Centipede or
EarthScope stations.

Restricted — no published tariff; contract-only access.

---

## albcors — ALBCORS (AL)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   AL — Albania
**operator**:  ASIG — Autoriteti Shtetëror për Informacionin Gjeohapësinor
               (State Authority for Geospatial Information), Tirana
**type**:      single-base (physical CORS)
**host:port**: not publicly listed (issued after application via krgjsh.asig.gov.al)
**access**:    application-required via the ASIG portal; no public self-service registration
**registration**: https://krgjsh.asig.gov.al/?page_id=1218&lang=en
**stations**:  27 (21 ground-mounted concrete blocks + 6 roof-type, incorporating
               the former ALBPOS system)
**signals**:   multi-constellation; aligned to ETRS89
**last_researched_date**: 2026-05-12

ALBCORS replaced the ALBPOS system (found non-compliant with national CORS
standards in 2015) and was confirmed operational at the 2023 EUREF Symposium
in Gothenburg. The 27-station network covers Albania (~29,000 km²) with a
control centre at ASIG premises in Tirana. Albania is an EU candidate
country; ETRS89 alignment supports future EU-compatible surveying. Access
requires submitting an application form via krgjsh.asig.gov.al (KRGJSH =
Kontrolli i Rrjetit Gjeodezik dhe Shërbimeve Hartografike); host:port is not
publicly disclosed.

Commercial alternative: **SATNET LIVE** (Land&Co — Topcon Albania
distributor, landcoal.com), accessed via the SATNET mobile app — 3 free
trial days for new registrations, free for 1 year with Land&Co GPS
equipment purchase; ongoing rate is not published.

**missing**: confirm NTRIP host:port, tariff, and whether non-professional
access is feasible — apply via krgjsh.asig.gov.al.

---

## armpos — ARMPOS (AM)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   AM — Armenia
**operator**:  State Committee for Real Property Cadastre of the Republic of
               Armenia (Անշարժ Գույքի Կադաստրի Պետական Կոմիտե / Cadastre Committee)
**type**:      single-base (physical CORS)
**host:port**: not publicly listed (application via cadastre.am)
**access**:    restricted; intended for licensed surveyors and government cadastre users; no open self-service registration
**registration**: https://www.cadastre.am/en
**stations**:  12 single-base stations, ~50 km spacing across ~30,000 km²
**signals**:   GPS + GLONASS (original Leica L1+L2; multi-constellation upgrade status not publicly documented)
**reference_frame**: ARMREF02
**last_researched_date**: 2026-05-12

ARMPOS (Armenian CORS) was commissioned in 2013 by the State Committee for
Real Property Cadastre with Norwegian government funding (NOK 9.8 million,
~$1.6 million at 2013 rates) and supervision by the Norwegian Mapping
Authority (Statens kartverk). Twelve reference stations cover the full
territory of Armenia, including the central plateau (Yerevan, Gyumri,
Vanadzor) and the southern Syunik / Kapan highlands. The State Committee is
the sole owner; the network supports real-time NTRIP RTK (metre, sub-metre,
centimetre) and post-processing (centimetre / sub-centimetre).

No public NTRIP host:port has been published in any directory (rtk2go,
ntrip-list.com, IGS, mvarga1989 list, ArduSimple). The Cadastre Committee
operates the e-cadastre.am and cadastre.am portals but does not surface RTK
as a user-facing service. Regional context: paid/restricted networks bracket
Armenia — AzPOS (AZ) to the east and GeoCors (GE) to the north; the South
Caucasus has no free open-registration RTK network. IGS station ARTU
(Artashat) is available for post-processing via EarthScope.

**missing**: public NTRIP host:port and access conditions — contact Cadastre
Committee via cadastre.am.

---

## geocors_ge — GeoCors (GE)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   GE — Georgia
**last_researched_date**: 2026-05-12
**type**:      single-base (physical CORS)
**access**:    paid; registration required (Leica Spider Business Center)
**host:port**: `geocors.napr.gov.ge:2101` (standard SBC port; pricing not public)
**operator**:  National Agency of Public Registry (NAPR), Ministry of Justice
               of Georgia (საჯარო რეესტრის ეროვნული სააგენტო)
**registration**: geocors.napr.gov.ge/SBC/Account/Register
**yearly_cost**: not publicly listed (paid subscription; contact NAPR)
**stations**:  26 physical single-base CORS — 7 Class A (national geodetic frame)
               + expanded Class B (regional densification)
**signals**:   GPS, GLONASS (Leica Spider platform)
**nmea_filter**: n/a (not in pipeline)

GeoCors is Georgia's national CORS network, established since 2011 under the
National Agency of Public Registry (NAPR), a legal-entity public-law body
under the Ministry of Justice. The 26-station network includes 7 Class A
stations forming the unified national spatial grid and expanded Class B stations
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
**yearly_cost_normalized**: 390
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
**yearly_cost_normalized**: 593
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
**yearly_cost_normalized**: 353
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
**yearly_cost_normalized**: 519
**registration**: `https://geospider.ru`
**stations**:  200+ (St. Petersburg, Moscow, Leningrad, Novgorod, Pskov, Tver, Vologda oblasts and expanding)
**source**:    geospider.ru (ООО «НПП «ГЕОМАТИК», St. Petersburg)
**operator**:  ООО «НПП «ГЕОМАТИК»

Regional-to-expanding network for North-West and Central Russia. RTK in local MSK coordinate
system (network RTK / VRS to MSK). RINEX also available (separate subscription). Individual
sign-up supported; no company registration required. Coverage expanding beyond original North-West
footprint as of 2026.

---

## Other — user-relevant but doesn't fit free/paid/restricted/RINEX

---

## geodaf — GeoDAF / ASI (IT)

**status**:    other
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
**yearly_cost**: €475/station/yr excl. BTW (~$538/yr) for 1–5 stations; volume to €95/station/yr for 21+ (2026 tariff, Tarievenregeling Kadaster BWBR0037196/2026-01-01)
**yearly_cost_normalized**: 538
**operator**:  NSGI / Kadaster Nederland (`nsgi.nl`)

NETPOS delivers raw reference station streams from the same ~30 AGRS.NL
physically-positioned base stations, as an authenticated paid service.
Priced per station per year (2026, excl. BTW): 1–5 stations €475/station,
6–10 €380, 11–15 €285, 16–20 €190, 21+ €95. VAT-exempt. Not a VRS / network-RTK
service — streams are single-base raw observations for users who compute their
own corrections.

---

## 06gps — 06-GPS (NL)

**status**:    other
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

## euref_ip — EUREF-IP / EPN broadcasters (federation)

**status**:    free
**date_added**: 2026-05-13
**country**:   global (federation; EPN stations across Europe + cross-border)
**operator**:  EUREF federation — BKG (Germany), ROB (Belgium), ASI (Italy)
**type**:      single-base (raw 1 Hz RTCM 3.x observations from EPN reference stations; no VRS/MAC/FKP)
**host:port**: `euref-ip.net:2101` (BKG, primary; TLS on `:443`); mirrors at
               `www.euref-ip.be:2101` (ROB; TLS `:2102`) and `euref-ip.asi.it:2101` (ASI)
**access**:    free with **per-broadcaster registration** (no SSO across the three);
               no residency / no professional gating
**registration**: BKG `http://register.rtcm-ntrip.org/cgi-bin/registration.cgi`
                  (also covers IGS-IP and products.igs-ip.net);
                  ROB `https://www.euref-ip.be/user-registration/user-registration-main-page.php`
**stations**:  ~229 unique EPN stations across the federation (BKG 218 STR, ROB 214 STR,
               ASI 201 STR; high overlap). Mountpoint convention: IGS 9-char + monument
               number, e.g. `PCAR00AND0` (Andorra), `REYK00ISL0` (Iceland),
               `NICO00CYP0` (Cyprus), `NABG00NOR0` (Ny-Ålesund, Svalbard)
**vrs**:       no
**signals**:   RTCM 3.3 / 3.2 / 3.1 (BKG skews 3.3, ROB skews 3.2);
               most streams GPS+GLO+GAL+BDS, some add QZS/SBAS/IRS
**last_researched_date**: 2026-05-13

ROB registration page disclaims kinematic suitability ("raw GNSS data streams are
unsuitable for operational real-time kinematic positioning"); BKG and ASI make no
equivalent statement. NMEA=0 across the federation (no GGA upload required); all
streams require Basic auth except a handful (DELF00NLD0 on BKG; 7 open streams on
ROB). Three streams flagged `fee:Y` are Austrian APOS/BEV upstreams (PFA300AUT0,
SBG200AUT0, TRF200AUT0) and may not stream to anonymous EUREF-IP accounts without
separate APOS authorisation.

---

## igs_ip — IGS-IP (federation)

**status**:    free
**date_added**: 2026-05-13
**country**:   global (IGS network)
**operator**:  BKG (caster operations)
**type**:      single-base (raw 1 Hz RTCM 3.x observations from global IGS stations; no VRS)
**host:port**: `www.igs-ip.net:2101`
**access**:    free with BKG account (same registration form as EUREF-IP)
**registration**: http://register.rtcm-ntrip.org/cgi-bin/registration.cgi
**vrs**:       no
**last_researched_date**: 2026-05-13

Global counterpart to EUREF-IP, carrying IGS-network reference stations
worldwide. Single-base RTK applies under the same constraints as EUREF-IP
(short baselines, multi-band rovers preferred). For Europe the EUREF-IP
broadcasters are the more comprehensive source; outside Europe IGS-IP is
the relevant federation entry.

Sister caster `products.igs-ip.net:2101` (BKG, same account) carries
**IGS-RTS SSR corrections** for PPP rather than RTCM observation streams —
out of scope for this project's standard-RTK pipeline; documented for
completeness.

---

## finpos — FINPOS RTK (FI)

**status**:    other
**reason**:    RTK access granted only for research with written justification (3-month
               renewable); no general public tier; DGNSS free but sub-metre only

---

## apn — APN (IL)

**status**:    other
**reason**:    pervasive military GNSS spoofing active continuously since Oct 2023
               across Israel/Lebanon/Jordan/Sinai/Cyprus (~50,000 flights affected in 2024);
               RTK unreliable regardless of NTRIP access

---

## pa_cors — Palestinian Authority CORS (PS)

**status**:    other
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

**status**:    other
**reason**:    server unreachable since launch; 0 stations ever collected; operated by
               Kansi Solutions GmbH (same parent as paid rtkdata.com); no independent
               data — aggregates rtk2go/Centipede visually

---

## idot_cors — IDOT CORS (US-IL)

**status**:    other
**country**:   US-IL
**date_added**: 2026-05-07
**last_researched_date**: 2026-05-13
**reason**:    announced/under construction; no live NTRIP endpoint as of 2026-05-13.
               IDOT launched network installation in November 2024 with $4.5M federal
               (ADCMS grant) + matching state funds ($6.25M total); ~70 sites statewide
               planned. IDOT described it as "the first free public network of its kind
               in Illinois." No host:port or launch timeline published. Commercial
               interim option: ReIL-NET (Kara Company, 55+ stations, Chicagoland +
               Central IL, $200/month; karaco.com/pages/reil-net-rtk-network).

---

## txrtn — TXDOT CORS (US-TX)

**status**:    restricted
**country**:   US — Texas
**host:port**: `txrtn.txdot.gov` (portal HTTP 200 2026-05-13; NTRIP port not published)
**operator**:  Texas Department of Transportation (TxDOT) — Information Systems Division
**stations**:  256 CORS statewide (all 254 counties)
**reason**:    access explicitly restricted to TxDOT employees and contractors/consultants
               on TxDOT-funded projects; no public registration pathway. Sensor map visible
               at txrtn.txdot.gov/Map/SensorMap.aspx. One of the largest state CORS networks
               in the country but never opened to public use.
**last_researched_date**: 2026-05-13

---

## calrtns — CalRTNS / Caltrans CORS (US-CA)

**status**:    restricted
**reason**:    access restricted to vetted state/county agency partners; no general public
               or hobbyist registration available

---

## sdcm — СДКМ / SDCM (RU)

**status**:    other
**reason**:    satellite-based augmentation system (SBAS), not NTRIP; L-band broadcast
               corrections (~20 cm sub-metre accuracy); requires SBAS-capable receiver,
               no internet connection used; out of scope for this project

---

## bgas_china — 北斗地基增强系统 BeiDou GBAS (CN)

**status**:    other
**reason**:    access restricted to licensed surveying organisations under 测量法
               (Surveying and Mapping Law of the PRC, Articles 27–29); no public
               NTRIP endpoint for unlicensed individuals; hobbyist registration path
               does not exist

---

## chinese_provincial_cors — Chinese Provincial CORS (CN)

**status**:    other
**reason**:    access restricted by law to licensed surveying organisations under
               测量法 (Surveying and Mapping Law of the PRC, 2017); hobbyist /
               individual use is not legally permitted — not a cost or
               registration barrier

All 31 provincial/municipal CORS networks are operated by natural-resources
or land-resources bureaux and feed into the national BGAS. Individual
registration is not available; credentials require institutional affiliation
with a licensed surveying body. Same legal barrier as `bgas_china`.

**Republication posture (2026-05-07, verified)**: drop confirmed. Not in
`scripts/fetch_stations.py` SOURCES and must not be added. The 测量法 gate is
not just a registration barrier — Articles 27–29 make unlicensed acquisition
or republication of CORS network data legally restricted, distinct from the
KR / TH / SA cases where the gate is on stream auth only.

---

## gps_emiliaromagna — Rete GPS Emilia-Romagna (IT)

**status**:    other
**reason**:    public regional service discontinued; stations now commercially operated
               via NetGEO/TopNET Live (netgeo.it); not free

---

## ergand — ERGAND Geodetic Network (AD)

**status**:    other
**date_added**: 2026-05-13
**country**:   AD — Andorra
**operator**:  ERGAND (Govern d'Andorra) — Cartografia / IDE Andorra
**type**:      single-base (EPN reference station, distributed via EUREF-IP federation)
**host:port**: PCAR00AND0 streamed real-time on all three EUREF-IP broadcasters
               (live 2026-05-13): BKG `euref-ip.net:2101` (TLS `:443`),
               ROB `www.euref-ip.be:2101` (TLS `:2102`), ASI `euref-ip.asi.it:2101`.
               Upstream Leica GR50 receiver also directly reachable at
               `185.194.59.113:2101`. No Andorran national caster.
**access**:    free with per-broadcaster EUREF-IP registration (no SSO across the three);
               no Andorran public NTRIP service
**registration**: BKG `http://register.rtcm-ntrip.org/cgi-bin/registration.cgi` or
                  ROB `https://www.euref-ip.be/user-registration/user-registration-main-page.php`
**stations**:  2 EPN members operated by ERGAND — **PCAR00AND0** at Pic de Carroi (~2520 m,
               ~5 km from Andorra la Vella; baselines stay <30 km across the country) and
               **RULL** which is **RINEX-only** (not exposed on any EUREF-IP broadcaster as of
               2026-05-13 despite being an EPN member)
**last_researched_date**: 2026-05-13

PCAR00AND0 is a raw 1 Hz single-base RTCM 3.x stream — not VRS, but with
PCAR ~5 km from Andorra la Vella the entire country fits inside reliable
RTK baselines from a single station. ERGAND also publishes post-processing
data and the AND08 / GEOAND01 national geoid (Leica/Topcon/Trimble
formats); no independent Andorran NTRIP caster has been announced.

Practical VRS alternative: ERGNSS (ES) at `ergnss-ip.ign.es:2101` and the
multi-constellation SPTR sub-service `ergnss-tr.ign.es:2102`, free with
registration; Catalan border stations are within VRS range of Andorra.
Centipede-RTK has sparse coverage in Ariège / Pyrénées-Orientales (France)
that is marginal at the northern border. See `euref_ip` for federation-wide
details.

---

## li_cors — Liechtenstein Geodata / ATG (LI)

**status**:    other
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

**status**:    other
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

**status**:    other
**reason**:    per-station direct TCP streams (not NTRIP aggregated); incompatible with
               standard NTRIP pipeline; no NTRIP caster endpoint published

---

## qianxun — 千寻知寸 Qianxun (CN)

**status**:    paid
**date_added**: 2026-05-13
**country**:   CN — China (mainland)
**operator**:  Qianxun Sensing Network Co., Ltd. (千寻位置网络) — Alibaba + Norinco / SASAC JV
**host:port**: `rtk.ntrip.qxwz.com:8001` (ITRF2008) · `:8002` (WGS84) · `:8003` (CGCS2000) —
               all three SOURCETABLE 200 OK 2026-05-12 (`Server: POP_GW_Ntrip_1.0`, IP 39.107.207.235)
**type**:      VRS (nationwide; computed from 2,700+ reference stations)
**mountpoints**: `AUTO` (RTCM3X full GNSS auto-pick), `RTCM30_GG` (RTCM3X legacy GPS+GLO 1004/1012),
               `RTCM23_GPS` (RTCM2X legacy GPS-only), `RTCM32_GGB` (RTCM3X MSM7 GPS+GLO+BDS)
**access**:    paid; individuals register at qxwz.com or mall.qxwz.com using Chinese mobile
               number; pay via Alipay/WeChat Pay; **real-name (实名认证) verification with
               mainland ID required — no practical foreign-hobbyist path**
**yearly_cost**: CNY 400/month or **CNY 3,600/year** for individual single-day-single-network
               survey use (Leicado reseller, confirmed 2026-05-12); commonly quoted CNY 3,600–3,800/yr;
               5-hour free trials via the Qianxun trial portal. Enterprise SSR/PPP-RTK CNY 8,000–12,000/yr.
**yearly_cost_normalized**: 500
**stations**:  2,700+ base stations; 33 mainland provinces; GPS+GLO+GAL+BDS (+QZS higher tiers)
**last_researched_date**: 2026-05-12

China's dominant commercial CORS network and default for surveyors, drone
industry, and autonomous-vehicle developers. Brands: FindCM (cm-level RTK),
FindMSM/FindAR (sub-metre SSR), FindFAST/FastFind (PPP-RTK / SSR PPP).

---

## cmcc_cors — 中国移动CORS China Mobile CORS (CN)

**status**:    paid
**date_added**: 2026-05-13
**country**:   CN — China (mainland)
**operator**:  China Mobile Communications Corporation (中国移动) — branded "OnePoint 高精度定位" / "中移智能"
**type**:      VRS (NTRIP CMCC interaction mode); host:port provisioned per account on activation
**access**:    paid; individual registration via China Mobile data account; **Chinese mobile
               number + real-name verification required — no practical foreign-hobbyist path**;
               daily/monthly/annual tiers
**yearly_cost**: ~¥3,600/yr (~$500/yr) — over $200/yr cutoff; bundling-friendly for IoT devices on China Mobile data plans
**yearly_cost_normalized**: 500
**stations**:  4,400+ nationwide (CMCC investment ~CNY 336M; densest Chinese commercial network by station count)
**last_researched_date**: 2026-05-12

China Mobile's high-precision positioning service. CMCC's stronger angle is
bundling: account paired with a CMCC SIM/data plan for IoT (drones,
agricultural autosteer, shared-bike fleets, autonomous logistics, port
automation).

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
**stations**:  none operational; RGT20 delivered 75 geodetic monuments + 50 orientation
               pillars (passive control, not CORS)
**source**:    ignfi.fr (IGN FI, Paris — implementing partner for RGT20 project)
**operator**:  Ministry of Land Planning, Housing and Urbanism (MATDHU); responsible
               national authority for the RGT20 deliverable

**date_added**: 2026-05-05

IGN FI installed 75 geodetic monuments plus 50 orientation pillars and computed a geoid
model for N'Djamena and surroundings under the RGT20 project (Spatial Data Infrastructure
for N'Djamena and environs; first pillar inaugurated March 2020, project completed February
2021). That infrastructure is passive survey control (Circé software + pillar coordinates),
not a streaming NTRIP caster. Chad is absent from rtk2go, corsstations.com, the GitHub
community CORS list, SmartNet, GEODNET, and every other directory checked. France ended
all defence and geodetic bilateral programme ties with Chad in January 2025.

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
**stations**:  one IGS contributing station (ABPO00MDG, Ambohimpanompo near Antananarivo;
               Septentrio PolaRx5, installed 2007) operated locally by the University of
               Antananarivo Institute of Geophysics, archived to UNAVCO/EarthScope and IGS
               — RINEX archive only, not an RTK caster

**date_added**: 2026-05-05

FTM (Foiben-Taosarintanin'i Madagasikara) is the national mapping and hydrographic agency,
mandated by law to maintain the geodetic reference network and align it with AFREF/ITRF.
FTM's stated activities include GPS densification of the national geodetic network and
definition of a new reference system compatible with international standards. No public
NTRIP caster endpoint, RTK streaming service, or registration portal has been found on
ftm.mg or in AFREF/IGS documentation as of 2026. ABPO00MDG is a passive scientific archive
asset; Madagascar is absent from SmartNet, Polaris, GEODNET, and onocoy directories, and
shows zero mountpoints on rtk2go or Centipede.

**missing**: confirm whether FTM has launched any NTRIP caster since 2023; check AFREF
ODC and igs.org for any additional MG station IDs beyond ABPO00MDG.

---

## cnigs_ht — CNIGS CORS (HT)

**status**:    other
**date_added**: 2026-05-13
**country**:   HT — Haiti
**last_researched_date**: 2026-05-12
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
**date_added**: 2026-05-13
**country**:   DO — Dominican Republic
**operator**:  IGN-JJHM — Instituto Geográfico Nacional "José Joaquín Hungría Morell"
**type**:      single-base (physical CORS; no VRS confirmed)
**host:port**: `ntrip.ign.gob.do` (NTRIP port behind Cloudflare WAF — direct TCP probe
               to 2101 timed out 2026-05-12; portal reachable, port disclosed after registration)
**access**:    free with registration; credentials issued after form submission
**registration**: https://ntrip.ign.gob.do/
**stations**:  2 original (Moca, Puerto Plata) + November 2025 expansion announcement
               (size/locations not yet enumerated publicly; mid-2024 had certified 11+ in
               northern region; 5 additional certified by August 2025)
**last_researched_date**: 2026-05-12

REGNA-RD (Red Geodésica Nacional Activa — República Dominicana) is the
official national geodetic network. SIRGAS-compatible reference frame. The
service is free; a web registration form issues credentials. Port not
published on the public website; raw NTRIP TCP appears to sit behind a
Cloudflare WAF that blocks unauthorised access from outside Cloudflare-allowed
paths. Additional installations planned along the Haiti border zone in
partnership with the Ministry of Defence.

**investigate**: confirm total station count and current host:port once
registered; verify whether any VRS/network solution (MAC/iMAX) is offered.

---

## fundcorsrd — FUNDCORSRD (DO)

**status**:    other
**date_added**: 2026-04-29
**last_researched_date**: 2026-05-12
**country**:   DO — Dominican Republic
**type**:      single-base (physical CORS; paired RTCM 3.0 legacy GPS+GLO and
               RTCM 3.2/3.3 MSM multi-GNSS streams per station)
**host:port**: `190.166.228.161:2103` (sourcetable curl-confirmed 2026-05-12;
               11 308 bytes, 74 STR rows = 37 stations × 2 formats; SNIP [wPRO]
               R3.19.00 of 2025-12-19)
**access**:    credentials issued on direct request via fundcorsrd.com contact form;
               terms not posted publicly
**registration**: fundcorsrd.com
**stations**:  37 (live sourcetable 2026-05-12 — nationwide; e.g. BARA La Romana,
               FCAC Azua, FCBN Bani, FCBO Bonao, FCSC Santiago)

Fundación para el Establecimiento de la Red de Estaciones Permanentes de la República
Dominicana (FUNDCORSRD) is a non-profit foundation, founded in 2016 by Dominican
surveyors, operating 37 physical CORS stations nationwide. Each station serves
both a legacy RTCM 3.0 GPS+GLO stream and an RTCM 3.2/3.3 MSM multi-GNSS
(GPS+GLO+GAL+BDS, often MSM7) stream. Self-described as serving "society in general,"
with 838+ registered users as of 2025; 2025 press coverage confirmed a strategic
agreement with IGN to contribute to the Dominican Republic's Satellite Geodetic
System. Inaugurated new Santo Domingo office in 2025. Sourcetable is anonymously
readable but rover credentials are issued only after a direct request through
the foundation's contact form — pricing, eligibility, and ongoing terms are
not disclosed on the public site, so a hobbyist cannot tell ahead of contact
whether they qualify or what (if anything) they would be charged.

---

## cors_rd_geo — CORS-RD / Geomatica (DO)

**status**:    paid
**date_added**: 2026-05-13
**country**:   DO — Dominican Republic
**last_researched_date**: 2026-05-12
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
**date_added**: 2026-05-13
**country**:   DO — Dominican Republic
**last_researched_date**: 2026-05-12
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
**date_added**: 2026-05-13
**country**:   BO — Bolivia
**operator**:  IGM Bolivia — Instituto Geográfico Militar; CEPAG (Centro de
               Procesamiento y Análisis de Datos GNSS) processing centre
**type**:      single-base (42 continuous reference stations per 2026 research)
**host:port**: not publicly listed; access procedure documented in YouTube walkthrough
               (`youtube.com/watch?v=4yuH1W05eII`)
**access**:    paid; annual fee + formal written request; no self-service registration
**yearly_cost**: not publicly listed (contact CEPAG — igmbolivia.gob.bo)
**registration**: igmbolivia.gob.bo (IGM Bolivia website)
**stations**:  42 continuous reference stations; MARGEN-ROC contributes to SIRGAS-CON via CEPAG
**last_researched_date**: 2026-05-12

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
**date_added**: 2026-05-13
**country**:   BO — Bolivia
**operator**:  GeoBolivia SRL (commercial); governed by COTOBOL (Colegio de
               Topógrafos de Bolivia) under Ley 2997 del Topógrafo
**type**:      single-base; GPS+GLO+GAL+BDS
**host:port**: caster port 6060; full hostname not publicly confirmed —
               credentials issued post-subscription
**access**:    paid; professional-surveyor governance under Ley 2997 implies
               hobbyist sign-up may be restricted in practice
**yearly_cost**: not publicly listed (contact GeoBolivia SRL via Facebook or phone)
**registration**: geoboliviasrl.info (Wix-hosted; HTTP 200 on 2026-05-12, technical
                  specs not exposed); Facebook "GeoBolivia SRL - Geomática" active
**stations**:  ~7 stations: La Paz (GEO 1), Cochabamba (GEO 2), Oruro (GEO 3),
               Sacaba (GEO 4), Tarija (GEO 5), Santa Cruz (GEO 6), Yacuiba (Tarija dept.)
**last_researched_date**: 2026-05-12

A 2026-05-12 page fetch shows the site live but no public pricing or
hostname. Station coordinates are tied to Class A/B points of the
government MARGEN framework. A Facebook post offered one year of RED-GEO
access free as a hardware-bundle bonus, confirming the service is active.

A third commercial Bolivian network, **GEOEQUIPOS SRL Red CORS**
(`geoequipossrl.com/red-cors/`), appears in research (2026-05-12) — mobile
QR-code payments in Bolivianos (≤500 Bs/transaction), contact: +591
78866188, info@geoequipossrl.com, Calle Pinilla 2588 La Paz. Host/port and
pricing remain behind contact gate; no separate block yet.

**missing**: confirm full caster hostname and subscription pricing in
Bs/yr once geoboliviasrl.info technical specs are exposed.

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

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
**country**:   GT — Guatemala
**type**:      single-base
**host:port**: none — post-processing RINEX download service only; no NTRIP caster
**access**:    free RINEX data downloadable from ign.gob.gt; no real-time corrections
**registration**: ign.gob.gt (Instituto Geográfico Nacional — Guatemala)
**stations**:  16 confirmed (live IGN geoportal 2026-05-12; programmatic target 17)

Guatemala's Instituto Geográfico Nacional (IGN) operates a Red CORS (Continuously Operating
Reference Stations) of 16 stations confirmed in the live IGN geoportal map as of 2026-05-12
(elena, huehue, mita, tikal, morales, taxisco, chisec, chicaman, tinta, barillas, coate,
cotzu, sayaxche, naranjo, poptun, gualan).
The network was established with technical and financial support from RIC (Registro de
Información Catastral) to enable rapid cadastral surveys tied to the national reference
system. RINEX 2.11 data is available for download from the IGN website. The IGN and RIC
public portals list only a post-processing RINEX data product ("datos CORS"); no separately
priced or free live NTRIP/RTK streaming subscription is publicly documented. ArduSimple
(2026) does not list Guatemala as having a national RTK network accessible to hobbyists.
Free RINEX archive only; no real-time NTRIP service offered. Surfaced as a `weird`
country marker so target users in Guatemala know free post-processing data exists.

## ip_cors_hn — IP CORS Honduras / IGN Honduras (HN)

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
**country**:   HN — Honduras
**type**:      single-base
**host:port**: none — post-processing RINEX download service only; no NTRIP caster
**access**:    free RINEX data downloadable at cors.ip.gob.hn; no real-time corrections
**registration**: https://cors.ip.gob.hn
**stations**:  5 (Tegucigalpa/TEG, San Pedro Sula/ICF1, Juticalpa/JUT1,
               Siguatepeque/UNCF, La Ceiba/CEIB)

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

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
**country**:   HN — Honduras

IGN Honduras is not a separate entity from the IP/DGCG — see `ip_cors_hn`. The IGN
brand is maintained at ign.hn as an auxiliary web presence; the CORS network described
there is the same 5-station network documented under `ip_cors_hn`. No separate NTRIP
service or caster endpoint exists under the IGN brand.
Rejected — same institution as `ip_cors_hn`; post-processing only.

## ineter_cors — INETER CORS (NI)

**status**:    other
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

**status**:    other
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

**status**:    other
**country**:   SV — El Salvador
**type**:      single-base
**host:port**: not publicly listed (credentials supplied by email after payment)
**access**:    paid — monthly/quarterly/annual subscription; pricing published at
               survey3g.com/servicios-de-ntrip/ (confirmed 2026-05-06)
**yearly_cost**: $450/yr
**registration**: survey3g.com
**stations**:  6 stations: San Miguel, Perkin, La Unión, San Salvador-UES (research/edu),
               Santa Ana, Cojute; ~50 km radius each; ~90% national coverage

**date_added**: 2026-05-06

Survey3G is the principal commercial NTRIP provider in El Salvador, offering RTK
correction streams from six stations covering the national territory. Constellations:
GPS, GLONASS, BeiDou, Galileo; frequencies L1/L2/L5. The network operates 24/7;
credentials (IP, port, username, password) are unique per subscription period and
supplied by email 32–48 hours before the start date. Published tiers: USD 15/7 days ·
USD 30/15 days · USD 45/month · USD 135/3 months · USD 450/12 months. Annual cost of
$450/yr exceeds the $200/yr hobbyist cutoff — rejected for pipeline.

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

**status**:    other
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
**access**:    free trial extended to 2026-07-01 (khmergeonet.xyz, observed 2026-05-06);
               post-trial pricing not publicly listed — contact via khmergeonet.xyz
**yearly_cost**: not publicly listed (contact GDCG)
**registration**: khmergeonet.xyz
**stations**:  5 (Phnom Penh, Kandal, Kampong Speu, Siem Reap, Stung Treng)
**operator**:  General Department of Cadastre and Geography (GDCG), Ministry of
               Land Management, Urban Planning and Construction (MLMUPC)

**date_added**: 2026-05-06

Cambodia's national CORS and precise positioning service, built under JICA technical
cooperation (August 2021 – December 2024). The 5 CORS provide single-base corrections
for registered GNSS users in pilot coverage areas. Service branded Khmer GEONET
(khmergeonet.xyz). Free trial extended to 2026-07-01; subscription pricing after
that date is not on the public website.

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

**status**:    other
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

**status**:    other
**date_added**: 2026-05-13
**country**:   FJ — Fiji
**last_researched_date**: 2026-05-12
**type**:      single-base (no public NTRIP confirmed; CORS physically established)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found; access policy under development (as of 2022)
**registration**: no self-service portal identified
**stations**:  ~10 (2 legacy: Suva, Lautoka; 8 new: Labasa, Nabouwalu, Taveuni,
               Kadavu, Koro Island, Lakeba, Ono-i-Lau, Rotuma)
**operator**:  Department of Lands and Survey (Ministry of Lands and Mineral
               Resources, `lands.gov.fj`)
**yearly_cost**: n/a (no confirmed public service)

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

## repangol — REPANGOL (AO)

**status**:    other
**date_added**: 2026-05-13
**country**:   AO — Angola
**operator**:  IGCA — Instituto Geográfico e Cadastral de Angola
**type**:      physical CORS network; no public NTRIP caster
**host:port**: not publicly listed; `repangol.net` returned ECONNREFUSED 2026-05-06 (DNS resolves, TCP refused)
**access**:    no public NTRIP service documented; access path via IGCA only
**registration**: contact IGCA via `igca.gov.ao` (the `repangol.net` portal is offline)
**stations**:  18 permanent CORS installed 2010 (IGCA mandate per Decreto Presidencial n.º 115/21); maintenance completed 2020 by TeroMovigo
**reference_frame**: ITRF2008
**last_researched_date**: 2026-05-12

Angola's national geodetic CORS network, designed for the reference frame
and post-processing support. No public real-time RTK / NTRIP service is
documented; IGCA's website is reachable but lists no NTRIP service, and
the network's own `repangol.net` site has been offline. Zero AO mountpoints
on rtk2go, Centipede, or EarthScope. No commercial RTK provider lists
Angola coverage. Surfaced as `other` so AO users land on a marker that
explains national infrastructure exists but isn't publicly accessible.

---

## dsm_bw — Department of Surveys and Mapping CORS (BW)

**status**:    other
**date_added**: 2026-05-13
**country**:   BW — Botswana
**operator**:  Department of Surveys and Mapping (DSM), Ministry of Lands and
               Water Affairs, Gaborone (`gov.bw`)
**type**:      physical CORS network; no confirmed public NTRIP caster
**host:port**: not publicly listed
**access**:    no public NTRIP caster found; access requires direct engagement with DSM
**registration**: no public portal identified
**stations**:  ~55 physical CORS (project commenced 2011, ~10 stations/yr); average
               spacing ~30–40 km across ~582,000 km². 2017 academic snapshot showed
               only 28 of installed stations operating correctly — reliability has
               historically been a concern
**reference_frame**: BNGRS02 (Botswana National Geodetic Reference System 2002);
               legacy BTRS / Cape Datum / Modified Clarke 1880 also in use
**last_researched_date**: 2026-05-12

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

**status**:    other
**date_added**: 2026-05-13
**country**:   CV — Cape Verde
**operator**:  INGT — Instituto Nacional de Gestão do Território (`ingt.gov.cv`),
               under the Ministry of Infrastructure, Land Use Planning and
               Housing (MIOTH)
**type**:      unknown (no confirmed public NTRIP caster); single IGS post-processing
               station CPVG (REGINA, Espargos/Sal Island) — not RTK
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no public portal identified
**stations**:  CPVG (Sal Island) IGS reference station only — REGINA network (CNES/IGN France)
**last_researched_date**: 2026-05-12

INGT is the Cape Verde state entity responsible for Territory Ordering, Urban
Planning, Property Registry, Geodesy, Cartography, and the national Spatial
Data Infrastructure (IDE-CV, `idecv-ingt.opendata.arcgis.com`). Geodesy is a
stated core mandate. No public NTRIP caster host:port has been found in any
directory, sourcetable, or academic reference for the archipelago. Zero CV
mountpoints on rtk2go or Centipede.

## ag_cors — Antigua and Barbuda GNSS / COCONet (AG)

**status**:    free
**date_added**: 2026-05-13
**country**:   AG — Antigua and Barbuda
**operator**:  Lands and Survey Division (Ministry of Lands, Housing and Agriculture);
               EarthScope NOTA stations operated by the EarthScope Consortium (former UNAVCO/COCONet)
**type**:      single-base (EarthScope NOTA streams; no AG-national caster)
**host:port**: `ntrip.earthscope.org:2101` (RTCM 3.3); ports 2105 (BINEX), 2108 (PPP)
**access**:    free non-commercial via EarthScope; account + annual NULA acceptance required
**registration**: https://www.earthscope.org/data/gnss-realtime/
**stations**:  3 EarthScope NOTA — CN01 (Bethesda, Antigua main), BGGY (Codrington, Barbuda),
               RDON (Redonda Island). No AG-national caster.
**last_researched_date**: 2026-05-12

No AG-national RTK service exists; the Lands and Survey Division
(`lands.gov.ag`, Landfolio portal) holds geodetic responsibility but
operates no NTRIP caster. Real-time corrections in AG territory come
exclusively from EarthScope NOTA (former COCONet/UNAVCO; legacy
`rtgpsout.unavco.org` retired 2025-07-29):

- **CN01_RTCM3P3** (Trimble NetR9, 17.05 -61.76) — Bethesda, Antigua main
  island; original COCONet site; primary single-base for Antigua positioning
  (<20–30 km reliable range).
- **BGGY_RTCM3P3** (Trimble NetR9, 17.05 -61.86) — Codrington area,
  Barbuda; current EarthScope code (legacy CN00 superseded).
- **RDON_RTCM3P3** (Septentrio PolaRx5, 16.93 -62.35) — Redonda Island,
  uninhabited dependency; expansion-phase install; too distant for
  cm-accuracy from the main islands but useful for any work on Redonda.

Streams are raw 1 Hz multi-constellation RTCM 3.3 MSM7 single-base (not
VRS). Five additional EarthScope stations on Montserrat (CN62, TRNT, RCHY,
AIRS, OLVN) lie 50–60 km from Redonda/Antigua and can serve as alternates
when CN01/BGGY are unavailable, with degraded fix probability at that
baseline. Tariff (NULA v. 2025-05-30): free non-commercial; $1,000/seat/yr
commercial (min 5 seats). Zero AG mountpoints on rtk2go or Centipede.

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
**type**:      single-base (EarthScope NOTA streams in neighbouring islands; no VC-national caster)
**host:port**: `ntrip.earthscope.org:2101` (nearest free streams; no VC-territory station)
**access**:    free non-commercial via EarthScope; account + annual NULA acceptance required
**registration**: https://www.earthscope.org/data/gnss-realtime/
**stations**:  no station in VC territory; nearest EarthScope NOTA streams are CN47
               (Saint Lucia, ~58 km north of Kingstown) and CN46 (Carriacou/Grenada,
               ~88 km south). Geodetic modernisation work underway (Caribbean Digital
               Transformation Project, World Bank, 2020–2026)
**operator**:  Lands and Surveys Department (`transport.gov.vc`); EarthScope NOTA
               stations operated by the EarthScope Consortium (former UNAVCO/COCONet)
**date_added**: 2026-04-29
**last_researched_date**: 2026-05-13

No COCONet/EarthScope station sits in VC territory. The nearest free streams are
EarthScope NOTA single-base mountpoints in neighbouring countries: `CN47_RTCM3P3`
on Saint Lucia (13.71°N, −60.94°W, ~58 km north of Kingstown) and `CN46_RTCM3P3`
on Carriacou, Grenada (12.49°N, −61.43°W, ~88 km south). CN47 is at the comfortable
edge of single-base RTK practicality for dual-frequency multi-constellation receivers;
CN46 is degraded but workable for decimetre work in the southern Grenadines. Hobbyists
needing cm-grade fixes on Saint Vincent itself should deploy a local base.

The World Bank–funded Caribbean Digital Transformation Project (US$28 million,
2020–2026) includes a geodetic reference network modernisation component for SVG:
datum update from BWI 1945 Grid to ITRF, equipment procurement (handover Feb 2024),
and a digital mapping exercise completed Dec 2024 – Jan 2025 with This is PLACE
using a fixed-wing VTOL drone. No CORS / NTRIP follow-on has been announced. Zero
VC mountpoints on rtk2go or Centipede.

**missing**: re-check whether the CARDTP geodetic modernisation resulted in a
public CORS NTRIP endpoint; contact Lands and Surveys Department via
`transport.gov.vc` for any planned public caster.

## vg_cors — British Virgin Islands GNSS / COCONet (VG)

**status**:    free
**date_added**: 2026-05-13
**country**:   VG — British Virgin Islands (UK Overseas Territory)
**operator**:  Land and Survey Department (`bvi.gov.vg`); EarthScope NOTA station
               operated by the EarthScope Consortium (former UNAVCO/COCONet)
**type**:      single-base (EarthScope NOTA stream; no VG-national caster)
**host:port**: `ntrip.earthscope.org:2101` (RTCM 3.3); ports 2105 (BINEX), 2108 (PPP)
**access**:    free non-commercial via EarthScope; account + annual NULA acceptance required
**registration**: https://www.earthscope.org/data/gnss-realtime/
**stations**:  1 EarthScope NOTA — `CN03_RTCM3P3` (Tortola, 18.49°N, −64.40°W;
               Septentrio POLARX5; raw 1 Hz multi-constellation RTCM 3.3 MSM7)
**last_researched_date**: 2026-05-12

No VG-national RTK service exists. The Land and Survey Department holds geodetic
responsibility but operates no NTRIP caster. As a UK Overseas Territory the BVI is
outside Ordnance Survey's OS Net coverage and no FCDO geospatial aid programme has
funded an NTRIP service. Real-time corrections in BVI territory come exclusively
from EarthScope NOTA (former COCONet/UNAVCO; legacy `rtgpsout.unavco.org` retired
2025-07-29):

- **CN03_RTCM3P3** (Septentrio POLARX5, 18.49 -64.40) — Tortola, the main BVI
  island; single-base reference (NOT VRS). Reliable RTK within ~20–30 km of the
  antenna covers most of Tortola and Virgin Gorda. Anegada (~60 km north) is at the
  outer limit; STVI on St. Thomas (USVI, ~30 km west) is a useful second reference.

Sourcetable probe `ntrip.earthscope.org:2101` returned SOURCETABLE 200 OK 2026-05-12
with CN03 listed under country code `VGB`. Tariff (NULA v. 2025-05-30): free
non-commercial; USD $1,000/seat/yr commercial (min 5 seats). Zero VG mountpoints on
rtk2go or Centipede.

## vi_cors — US Virgin Islands GNSS / COCONet (VI)

**status**:    free
**date_added**: 2026-05-13
**country**:   VI — US Virgin Islands (US territory)
**operator**:  US territory; no VI-territorial NTRIP caster. EarthScope NOTA station
               operated by the EarthScope Consortium (former UNAVCO/COCONet); NOAA
               NCN CORS provides RINEX only
**type**:      single-base (EarthScope NOTA stream; no VRS engine)
**host:port**: `ntrip.earthscope.org:2101` (RTCM 3.3); ports 2105 (BINEX), 2108 (PPP)
**access**:    free non-commercial via EarthScope; account + annual NULA acceptance required
**registration**: https://www.earthscope.org/data/gnss-realtime/
**stations**:  1 EarthScope NOTA streaming in VI territory — `STVI_RTCM3P3` (St. Thomas,
               18.34°N, −64.97°W; Trimble NETR9; tagged country code `USA` in the
               EarthScope sourcetable). NOAA NCN lists four USVI stations (STVI and
               VITH on St. Thomas; CRO1 and VIKH on St. Croix) for RINEX download only
**last_researched_date**: 2026-05-12

No VI-territorial RTK service exists. Real-time corrections come from EarthScope NOTA
single-base streams:

- **STVI_RTCM3P3** (Trimble NETR9, 18.34 -64.97) — St. Thomas (~5 km SW of Charlotte
  Amalie); part of the legacy Puerto Rico GPS Network (PRGPS) sub-network. Useful for
  short-baseline RTK within ~30–50 km — covers St. Thomas, St. John, and the BVI side
  via CN03 as a second reference (~30 km NE). St. Croix (50–80 km south) is outside
  reliable single-base RTK range from STVI.

The Puerto Rico Seismic Network (PRSN/UPRM) operates ~18 GNSS stations covering
PR + USVI + BVI; its NTRIP endpoint is restricted to academic/government users and
the public NTRIP info page returned ECONNREFUSED 2026-05-06 — see `prsn_cors` block.
EarthScope sourcetable probe `ntrip.earthscope.org:2101` returned SOURCETABLE 200 OK
2026-05-12 with STVI present. Tariff (NULA v. 2025-05-30): free non-commercial;
USD $1,000/seat/yr commercial (min 5 seats). Zero VI mountpoints on rtk2go or
Centipede; no commercial RTK network (Trimble VRS Now, Hexagon SmartNet, GEODNET)
confirmed to cover USVI.

## glsc_cors — Guyana CORS (GY)

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
**country**:   GY — Guyana
**type**:      single-base (professional/government access; no public NTRIP confirmed)
**host:port**: not publicly listed
**access**:    no public NTRIP caster found
**registration**: no self-service portal identified
**stations**:  8 (Eclipse Falls, Supenaam, Georgetown, New Amsterdam, Olive Creek,
               Lethem, Linden + 1 additional site)
**operator**:  GL&SC (Guyana Lands and Surveys Commission, `glsc.gov.gy`)
**yearly_cost**: n/a (no confirmed public service)

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
**date_added**: 2026-05-13
**country**:   BD — Bangladesh
**operator**:  Survey of Bangladesh (SoB), Ministry of Defence
               (`sob.gov.bd`); data portal `data.sob.gov.bd`
**type**:      VRS (6 physical CORS backing a VRS network)
**host:port**: `202.53.170.98:8011` (current per SoB Geodetic Service page);
               legacy `202.40.181.3:8021` recorded by ArduSimple
**access**:    registration required; pricing not listed on public website —
               consult `data.sob.gov.bd` or contact SOB directly
**registration**: `data.sob.gov.bd/signup-user.php`
**yearly_cost**: not publicly listed (payment via Rocket/bKash/SureCash mobile
               banking per SOB data-service model — a Bangladeshi phone number /
               bank account is needed to actually transact)
**stations**:  6 physical CORS at Dhaka, Chittagong, Rajshahi, Khulna,
               Maulavibazar, Rangpur — operating since 19 December 2011;
               VRS software on server generates virtual corrections; ~73-station
               expansion programme listed on sob.gov.bd, ground-truth status not confirmed
**last_researched_date**: 2026-05-12

Bangladesh's national GNSS CORS network was established in December 2011
with six permanent stations spanning ~147,570 km². A VRS software layer on
the SoB data-centre server generates RTK corrections from the 6 CORS plus
surrounding IGS reference stations and supports post-processing RINEX. The
caster IP is publicly documented but requires a registered account for
NTRIP access. With only 6 underlying stations across the country,
inter-station baselines run 100–200 km — outside the 30–50 km envelope
needed for reliable L1+L2 RTK; corrections degrade significantly away from
station locations.

Volunteer fallback: 1 Centipede node `BENGLA4` near Chittagong (22.27°N
91.81°E, country code `BGD`), single base via `caster.centipede.fr:2101`,
useful within ~20–30 km. Zero rtk2go BD bases.

**investigate**: confirm completion status of the ~73-station expansion
programme; verify whether a newer host:port or pricing schedule is now
publicly available.

## miranet_bt — MiraNet / DrukNet CORS (BT)

**status**:    paid
**date_added**: 2026-05-13
**country**:   BT — Bhutan
**operator**:  National Land Commission Secretariat (NLCS), Royal Government of Bhutan;
               caster software MIRACaster operated by MIRASpaco (Portugal); web: `web.nlcs.gov.bt`
**type**:      single-base (13 physical CORS stations); IP `103.252.84.100`
**host:port**: `ntrip.druknet.net:2101` (portal: `miranet.nlcs.gov.bt`)
**access**:    paid subscription tiers — Basic (1 user) Nu 10,000/yr, Standard (2 users)
               Nu 17,500/yr, Premium (3 users) Nu 22,500/yr; government agencies flat
               Nu 10,000/yr unlimited; education/research free with supporting document
**registration**: `miranet.nlcs.gov.bt/pre-registration/form`
**yearly_cost**: Nu 10,000/yr (~$110/yr) Basic; up to Nu 22,500/yr Premium
**yearly_cost_normalized**: 110
**stations**:  13 single-base stations (2024 NSDI metadata); network established 2014
               with 6 stations (THIM, BUMT, KANG, PHUN, GELE, DEOT); added DTNG, WNGD,
               DGPL (2020), HAAC, LHUN, SPGT (2022), SIPS, ZHEM (2023); DEOT and GELE
               flagged for decommissioning
**vertical_datum**: DrukGeoid 2015
**last_researched_date**: 2026-05-12

Bhutan's national CORS network was established in 2014 with 6 Trimble receivers
and expanded to 13 stations. Managed via Trimble-based CORS management software
branded as MiraNet (DrukNet). The portal at `miranet.nlcs.gov.bt` provides both
real-time RTK NTRIP streaming and re-processed static RINEX data (daily and
hourly). NLCS levies a nominal fee to cover infrastructure, remote support
contracts, and recurrent internet/power costs. Educational and research users
receive free access upon submitting an official supporting document. Subscription
credentials (username/password) are issued after payment or approval.
Vertical datum: DrukGeoid 2015.

## survey_bn — Survey Department Brunei (BN)

**status**:    other
**date_added**: 2026-05-13
**country**:   BN — Brunei Darussalam
**operator**:  Department of Survey and Mapping (Jabatan Ukur), Ministry of Development,
               Brunei Darussalam (`survey.gov.bn`)
**type**:      Zero Order GNSS Network (8 stations, established ~2009); no public NTRIP caster
**host:port**: not publicly listed
**access**:    no open NTRIP service found
**registration**: no self-service portal identified; contact `survey.gov.bn`
**stations**:  8 documented in 2011 UN-GNSS presentation (KBEL, LABI, MURA, LAMU,
               LIAN, TEMB, TUTO, UKUR) supporting GDBD2009 datum; 2017 SEASC
               referenced a planned "Positioning Augmentation Center"
**last_researched_date**: 2026-05-12

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

**status**:    other
**date_added**: 2026-05-13
**country**:   BF — Burkina Faso
**operator**:  IGB — Institut Géographique du Burkina (`igb.bf`), Ouagadougou
**type**:      single-base (physical CORS stations); RTK NTRIP not publicly confirmed
**host:port**: not publicly confirmed (`www.bfcors.net:2101` inferred from Trimble
               Pivot Web architecture but not directly verifiable; no public RTK
               NTRIP tariff or endpoint published)
**access**:    contact IGB; post-processing RINEX is the explicitly documented use
               case in IGB materials — no NTRIP real-time caster service announced
**registration**: contact IGB via `igb.bf`
**stations**:  ~13 physical: 9 original (2011 MCA-BF funding) + 4 capital-region (2018)
**last_researched_date**: 2026-05-12

Nine permanent GNSS stations established in 2011 under a contract between
MCA-BF (Millennium Challenge Account Burkina Faso) and Trimble Europe BV
(~700 million FCFA contract signed May 2010); IGB assumed technical
management September 2012. Station locations: Gampela, Manga, Fada,
Diapaga, Dori, Ouahigouya, Dédougou, Bobo-Dioulasso, Gaoua. Four additional
capital-region stations added 2018 (Ouagadougou-IGB, Koubri, Dapélogo,
Tanguen-Dassouri). Raw data from station BF01 (Ouagadougou) used in 2024
academic ionospheric VTEC publications.

Security situation since the 2022 military coup and membership of the
Alliance of Sahel States (AES, January 2025) has reduced bilateral technical
cooperation with France/West; ongoing jihadist insurgency affects ~40–60%
of national territory as of April 2026. Station operational continuity is
uncertain. Zero BF mountpoints on rtk2go, Centipede, or EarthScope; no
stations within 200 km of Ouagadougou on any tracked free source.

**missing**: confirm whether IGB exposes a public NTRIP RTK caster (vs
post-processing-only RINEX access).

---

## reci_ci — RECI (CI)

**status**:    other
**date_added**: 2026-05-13
**country**:   CI — Côte d'Ivoire
**operator**:  BNETD-CIGN — Bureau National d'Études Techniques et de Développement /
               Centre d'Information Géographique National
**type**:      physical CORS network; RTK NTRIP mode enabled 2022; no public host:port
**host:port**: not publicly listed
**access**:    no public NTRIP service; access via institutional channel (BNETD-CIGN, government survey agencies)
**registration**: contact BNETD-CIGN via `cntig.net`
**stations**:  5 permanent CORS (RECI — Réseau CORS Ivoirien) + 1 IGS station; passive
               monumentation tiers RGIR (43 markers), RGIO (716 markers), and RGID densification
**last_researched_date**: 2026-05-12

Côte d'Ivoire's national CORS network, deployed and modernised by Toposat
in support of BNETD-CIGN's geodetic infrastructure programme. RECI was
upgraded to RTK NTRIP mode in 2022 (confirmed in 2025 academic literature
on land-rights surveying and the September 2025 FGF congress
"Le Réseau Géodésique de la Côte d'Ivoire", BALE / CIGN). No public NTRIP
caster URL, port, or registration portal has been published — access
opaque, institutional channel only. Centipede CIV count was ~2 in earlier
fetches and dropped to 0 on 2026-05-12 (transient or off-line). Static
network coords are open via ArcGIS Africa GeoPortal.

---

## ign_bj — IGN Bénin Permanent GNSS Station Network (BJ)

**status**:    free
**date_added**: 2026-05-13
**country**:   BJ — Benin
**operator**:  IGN Bénin — Institut Géographique National du Bénin (`ign.bj`),
               under the Ministry of Land Affairs
**type**:      single-base (physical CORS stations); 2022 upgrade enabled RTK NTRIP mode
**host:port**: not publicly listed (disclosed after registration via IGN Bénin / CatIS)
**access**:    free with registration; accessible via Benin Cadastral Information System;
               hobbyist eligibility not confirmed (upgrade purpose is land-rights / cadastral)
**registration**: https://service-public.bj (service PS01085 — "Fichier des stations permanentes GNSS")
                  or direct contact with IGN Bénin (`ign.bj`)
**stations**:  7 physical: Cotonou, Abomey, Savalou, Parakou, Natitingou, Nikki, Kandi
**last_researched_date**: 2026-05-12

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

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
**country**:   GN — Guinea (Conakry)
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    unknown — no public caster or registration portal discovered
**stations**:  unknown
**operator**:  INC — Institut National Cartographique, under the Ministry of
               Town Planning, Guinea (Conakry)
**yearly_cost**: unknown

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

## datu_mr — DGTC Mauritania Geodetic Network (MR)

**status**:    other
**date_added**: 2026-04-29
**last_researched_date**: 2026-05-12
**country**:   MR — Mauritania
**type**:      unknown (no confirmed public NTRIP caster)
**host:port**: not publicly listed
**access**:    no public caster or registration portal discovered
**stations**:  unknown
**operator**:  Direction de la Géodésie, Topographie et de la Cartographie
               (DGTC, sometimes referenced as GDGTA), Nouakchott, Mauritania.
               (Block id `datu_mr` retained for stability; "DATU" in the id
               reflects an earlier, incorrect operator-name reading.)
**reason**:    no Mauritanian national NTRIP/RTK caster found in Arabic, French,
               or English sources, in AFREF station lists, or in the BKG sourcetable
               as of 2026-05-12; survey practice on the ground relies on satellite
               PPP (Trimble RTX, Fugro StarFix) or shipping a base to site.

The national geodetic/mapping authority (DGTC) has no publicly documented GNSS
correction service. Mauritania's territory is ~1,031,000 km², predominantly
Saharan desert with extremely sparse road and power infrastructure outside the
Atlantic coastal strip; a national CORS network is a very long-term infrastructure
prospect. AFREF contributions from Mauritania, if any, are raw-archive RINEX only.
A 2018 Spectra Geospatial case study documented that a power-transmission survey
in Mauritania used Trimble RTX satellite PPP precisely because no ground-based
NTRIP caster was available. No US/EU sanctions apply. Zero MR mountpoints on
rtk2go or Centipede; nearest free alternatives are in Morocco (ANCFCC, paid)
and Senegal (SENCORS, undisclosed tariff).

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

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
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

No public CORS network or NTRIP caster has been found for the Central African
Republic. The country has experienced near-continuous armed conflict since 2012;
government authority outside Bangui is extremely limited. Wagner/Africa Corps
presence since 2018 and ongoing CPC insurgency severely constrain civilian
infrastructure investment. No CAR station appears in the IGS Network or AFREF
Operational Data Centre. Zero CF mountpoints on rtk2go or Centipede.

---

## dgcf_gw — DGCF Guinea-Bissau (GW)

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
**country**:   GW — Guinea-Bissau
**type**:      unknown
**host:port**: not publicly listed
**access**:    unknown
**registration**: no public portal found
**stations**:  unknown; no GW station identified in IGS Network or AFREF ODC
**operator**:  DGCF — Direcção-Geral de Cartografia e Fotogrametria, Ministry
               of Urban Planning and Construction
**yearly_cost**: n/a

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

**status**:    other
**date_added**: 2026-05-13
**country**:   BI — Burundi
**operator**:  IGEBU — Institut Géographique du Burundi (`igebu.bi`); under
               the Ministry of Water, Environment, Land Management and Urban
               Planning
**type**:      unknown
**host:port**: not publicly listed
**access**:    unknown
**registration**: no public portal found
**stations**:  unknown; no BI station identified in IGS Network or AFREF ODC
**last_researched_date**: 2026-05-12

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

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
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
**date_added**: 2026-05-13
**country**:   FO — Faroe Islands (Danish autonomous territory)
**last_researched_date**: 2026-05-12
**type**:      single-base (4 confirmed physical GNSS reference stations)
**host:port**: not publicly listed; access requires direct contact with Umhvørvisstovan
**access**:    professional/commercial clients (surveying firms, construction companies);
               no self-service portal or published endpoint; hobbyist eligibility unclear
**registration**: https://us.fo/kort/geodesi (agency contact; no self-service signup)
**stations**:  4 physical: Klaksvík, Vestmanna, Trongisvágur, Argir (confirmed 2026-05-01)
**operator**:  Umhvørvisstovan — The Faroese Environment Agency (`us.fo`,
               formerly `umhvorvisstovan.fo`)

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

**status**:    other
**date_added**: 2026-05-13
**country**:   GI — Gibraltar (British Overseas Territory)
**operator**:  BIGF (British Isles GPS Facility, NERC / BGS)
**type**:      single-base (scientific tide-gauge monitoring station; RINEX archive only)
**host:port**: not publicly listed (RINEX data via BIGF archive at bigf.ac.uk).
               **GIBR is NOT exposed on any EUREF-IP broadcaster** (verified absent from
               BKG, ROB, and ASI sourcetables 2026-05-13).
**access**:    restricted — archive data only; no real-time NTRIP stream
**registration**: https://www.bigf.ac.uk/request_data/form.html
**stations**:  1 (GIBR — at the Gibraltar tide gauge; IGS TIGA sea-level project)
**yearly_cost**: n/a (archive data free on request; no subscription)
**last_researched_date**: 2026-05-13

The Gibraltar GNSS station is part of the BIGF network operated by NERC /
British Geological Survey, co-located with the tide gauge. RINEX is
available on request from BIGF; HM Government of Gibraltar's GeoPortal
(geoportal.gov.gi) publishes no NTRIP or RTK correction service.

Hobbyists working in Gibraltar can use **ERGNSS (ES)** free of charge:
Tarifa (`TAR00`/`TAR20`) is ~16 km away and Ceuta (`CEU10`) ~28 km — both
within useful L1+L2 RTK baseline. See `ergnss`.

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

**status**:    other
**date_added**: 2026-05-13
**country**:   CW — Curaçao
**last_researched_date**: 2026-05-12
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

## aw_cors — Aruba Geodetic / DLV CORS (AW)

**status**:    other
**date_added**: 2026-05-13
**country**:   AW — Aruba
**operator**:  Department for Infrastructure Management and Planning (DIP, `gobierno.aw`)
               — survey/land registration mandate; legacy Dienst Landmeetkunde en
               Vastgoedregistratie (DLV) referenced on older portal paths
**type**:      EarthScope NOTA + rtk2go volunteer (no Aruban national caster)
**host:port**: EarthScope: `ntrip.earthscope.org:2101`; rtk2go: `rtk2go.com:2101`
**access**:    free non-commercial (EarthScope NULA) or open volunteer (rtk2go)
**registration**: EarthScope account at https://www.earthscope.org/data/gnss-realtime/; rtk2go: none
**stations**:  2 free streams cover the island — **CN19_RTCM3P3** (EarthScope NOTA, NW
               coast near California Lighthouse, 12.61°N -70.05°W, installed by UNAVCO
               June 2013) and **PINOST1** (rtk2go volunteer, Santa Cruz, 12.50°N
               -69.98°W). ~16 km apart; either alone covers Aruba within typical
               <20 km RTK baseline.
**last_researched_date**: 2026-05-12

No Aruba national RTK service. Aruba is an autonomous constituent country of
the Kingdom of the Netherlands and is **not** covered by Kadaster/NSGI
AGRS.BES — which serves only the BES special municipalities (Bonaire, Sint
Eustatius, Saba). DIP holds survey/land-registration mandate; `gob.aw` and
`gobierno.aw` contain no NTRIP or RTK correction content.

CN19 is part of EarthScope's Network of the Americas (NOTA, ex-COCONet);
installed cooperatively with the Meteorological Department of Aruba. RTCM 3.3
single-base stream; check `monitor.use-snip.com` for live PINOST1 status.
Nearest cross-border free streams (AGRS.BES on Bonaire) are ~130 km east,
well beyond usable RTK baseline. Practical fallbacks if both streams are
down: local base/rover pair, Galileo HAS (~40 cm), or commercial PPP.

## bahamas_lands_cors — Bahamas Lands & Surveys CORS (BS)

**status**:    other
**date_added**: 2026-05-13
**country**:   BS — The Bahamas
**operator**:  Department of Lands and Surveys, Bahamas Government
               (deployment by Spatial Dimension in partnership with Trimble Inc., ~2020)
**type**:      physical CORS network (Trimble Pivot Platform); no public NTRIP caster
**host:port**: not publicly listed
**access**:    no public NTRIP service; access likely gated to licensed Bahamian
               surveyors via institutional procedure (Department of Lands and Surveys)
**registration**: contact Department of Lands and Surveys via `bahamas.gov.bs`
               (HTTP 403 from automated fetch 2026-05-12)
**stations**:  23 Trimble CORS + 3 tide-gauge stations deployed ~2020 under the
               Landfolio cadastral-modernisation programme
**last_researched_date**: 2026-05-12

National Bahamian CORS infrastructure deployed for the Department of Lands
and Surveys by Spatial Dimension in partnership with Trimble (~2020),
alongside Landfolio cadastral software and Bahamian field-surveying kits.
Spread of 23 stations across ~700 km W–E / ~1200 km N–S is sufficient for
VRS over populated islands if operated as such, but the public NTRIP
endpoint is not advertised. Earth­Scope NOTA stations **CN13** (San
Salvador Island) and **CN14** (Great Inagua) are the only confirmed public
RTK streams in BS territory, both ~460–525 km SE of Nassau — too distant
for single-base RTK from the main population centre. NOAA NGS lists an
**AUTEC** station on Andros operated by the US Navy, but that is a US
federal installation, not a Bahamian national service.

---

## bq_cors — BES Islands Geodetic / Kadaster NL (BQ)

**status**:    free
**date_added**: 2026-05-13
**country**:   BQ — Bonaire, Sint Eustatius, Saba (Dutch special municipalities)
**last_researched_date**: 2026-05-12
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
but optional. Both casters confirmed live via sourcetable fetch (2026-05-06). Modern
`00BES0`-format mountpoints use RTCM 3.3 MSM; legacy 3.1 mountpoints (SABY0, SEUS0)
maintained for backward compatibility.
Single-station raw reference streams — not a VRS/network-RTK service. Kadaster's
NETPOS network-RTK service (Netherlands mainland only) does not extend to BES.
Zero BES-coded rtk2go or Centipede stations.

## alcorsnet_dz — AL-CORS-Net / SAAP (DZ)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   DZ — Algeria
**last_researched_date**: 2026-05-12
**type**:      vrs-only (Geo++ GNSMART Network-RTK)
**host:port**: not publicly listed
**access**:    restricted — operated under the Ministry of National Defence (INCT);
               no self-service registration or public NTRIP endpoint published
**registration**: https://www.inct.mdn.dz/
**yearly_cost**: n/a (no public commercial service)
**stations**:  189 permanent GNSS stations; 6 anchor/reference stations —
               Algiers (DZAL), Oran (DZOR), Constantine (DZCO), Ouargla (OGLA),
               Béchar (BECH), Tindouf (TIND)
**operator**:  Institut National de Cartographie et de Télédétection (INCT),
               Ministry of National Defence (`inct.mdn.dz`)

**date_added**: 2026-05-06

AL-CORS-Net (also known as SAAP — Système Algérien d'Aide au Positionnement) is a
189-station Network-RTK service on a Geo++ GNSMART backend. Published performance is
~1.3 cm horizontal, ~2.2 cm vertical (1σ) with ~97% VRS availability, and an academic
study confirmed live VRS sessions between October 2021 and January 2022. INCT sits
under the Ministry of National Defence; the INCT website returns SSL warnings and
surfaces no end-user signup path, and no public registration portal, tariff, or NTRIP
host:port has been advertised. A hobbyist path is structurally unlikely without a
separate civilian mandate.

REGAT (Réseau Géodésique de l'ATlas) — ~53 stations across the Algerian Atlas — is a
**separate** seismotectonic monitoring network operated by **CRAAG** (Centre de
Recherche en Astronomie, Astrophysique et Géophysique). RINEX archive for crustal-
deformation research; no real-time RTK service.

**missing**: confirm whether INCT has published any AL-CORS-Net host:port since 2024,
and whether REGAT RINEX data are accessible via UNAVCO/EarthScope or a national portal.

## esa_cors_eg — Egyptian Survey Authority CORS (EG)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   EG — Egypt
**last_researched_date**: 2026-05-12
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

**status**:    other
**date_added**: 2026-05-13
**country**:   IR — Iran
**last_researched_date**: 2026-05-12
**type**:      single-base
**host:port**: n/a — post-processing only; no public NTRIP caster
**access**:    raw RINEX archived to IGS for scientific post-processing
**registration**: `ipgn.ncc.gov.ir/en/accounts/signup/`
**yearly_cost**: n/a
**stations**:  ~127 physical CORS (phase 1 2004–2006, 106 stations; phase 2 completed
               2013 to 127 stations in ITRF2014)
**operator**:  National Cartographic Center of Iran (سازمان نقشه‌برداری کشور / NCC),
               `ncc.gov.ir`

Iranian Permanent GPS Network for Geodynamics, established post-2003 Bam earthquake
for tectonic monitoring, velocity and strain-field estimation. Base network covers
Zagros Mountains, Central Iran, Alborz, East Iran, Makran, Loot, and Kopeh-Dagh, plus
three local sub-networks. RINEX archived to IGS for scientific post-processing.

NCC's real-time correction arm is a separate paid product, **Hoda Pro**
(`hodapro.ncc.gov.ir`) — see `hodapro_ir`. The IPGN itself does not operate a public
NTRIP RTK caster of its own; the sign-up portal at `ipgn.ncc.gov.ir` is reachable
externally but is the geodynamics-data account, not an RTK gateway.

**missing**: confirmation that RINEX downloads work without an IGS-class research
affiliation; confirmation of what the IPGN sign-up portal issues to non-research
applicants.

---

## hodapro_ir — Hoda Pro (IR)

**status**:    other
**date_added**: 2026-05-13
**country**:   IR — Iran
**last_researched_date**: 2026-05-12
**type**:      physical-coord-vrs
**host:port**: `hodapro.ncc.gov.ir:2101`
**access**:    paid subscription via `eshop.ncc.gov.ir`; sign-up requires Iranian
               national ID and Iranian banking; e-shop firewall-blocked from outside
               Iran
**registration**: `eshop.ncc.gov.ir`
**yearly_cost**: not publicly listed
**stations**:  ~127 (shares the IPGN station network — see `ipgn`)
**operator**:  National Cartographic Center of Iran (سازمان نقشه‌برداری کشور / NCC),
               `ncc.gov.ir`

Hoda Pro (سامانه ملی هدی پرو) is the RTK / Network-RTK arm of NCC's national
positioning programme, riding on the IPGN station network. Distinct product from
the legacy DGPS-only HODA service (`hoda.ncc.gov.ir`, out of project scope) and
from the IPGN geodynamics caster (`ipgn`, post-processing only).

Classified `weird` rather than `paid` because the e-shop and rate card are
firewall-blocked from outside Iran, so neither a verifiable `yearly_cost` nor
confirmation that unaffiliated Iranian individuals can register is obtainable.
Foreign hobbyists or residents have no documented sign-up path; the network is
nonetheless surfaced because Iranian target users searching for "هدی پرو" should
land on a marker that explains what NCC actually sells.

**missing**: actual subscription rates; whether registration is open to Iranian
individuals without a licensed-surveyor credential.

---

## shamim_ir — SHAMIM (IR)

**status**:    restricted
**date_added**: 2026-05-13
**country**:   IR — Iran
**last_researched_date**: 2026-05-12
**type**:      physical-coord-vrs
**host:port**: `178.252.173.15:2101` (SHAMIM); `178.252.173.75:2101` (SHAMIM Plus)
**access**:    cadastre-licensed surveyors only — registration requires Iranian
               national ID (کد ملی), Iranian mobile for OTP, and a specific GNSS
               receiver's serial number bound to the account; no documented path
               for unaffiliated users
**registration**: `shamim.ssaa.ir`
**yearly_cost**: n/a (no fee, but cadastre-programme gated)
**stations**:  144 physical permanent GNSS stations nationwide (installed 2016–2017)
**operator**:  Organisation for Registration of Deeds and Properties
               (سازمان ثبت اسناد و املاک کشور, `ssaa.ir`)

SHAMIM (شمیم — شبکه موقعیت‌یابی یکپارچه مالکیت‌ها, Integrated Unified Property
Management Network) is Iran's national cadastral CORS network. Geo++ GNSMART backend
serving Nearest, VRS, FKP, MAX, and IMAX modes; the original SHAMIM caster and the
expanded SHAMIM Plus tier run on neighbouring IPs. Built to accelerate the national
cadastre programme.

Restricted rather than free at the marker level: although there is no subscription
fee, registration is documented only for users with a cadastre-programme professional
connection (licensed cadastral surveyors, SSAA-outsourced operators), with each
account bound to an approved receiver. No mechanism is described for an unaffiliated
hobbyist — Iranian or otherwise — to obtain credentials. Endpoints firewalled outside
Iran; not in the ingestion pipeline.

---

## rgna_mx — Red Geodésica Nacional Activa (MX)

**status**:    other
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
**yearly_cost_normalized**: 1450
**stations**:  not published separately (resold network)
**operator**:  Hi-Target (hardware vendor); resold via Mexican GNSS dealers

Hi-Target CORS licences are sold monthly through Mexican GNSS equipment resellers.
The monthly price (~MX$2,414) corresponds to roughly $120/month or ~$1,450/yr — above the
$200/yr paid-affordable cutoff. Not added to pipeline: paid service.

---

## sirgas_chile — RGN/SIRGAS-CHILE (CL)

**status**:    other
**date_added**: 2026-05-13
**country**:   CL — Chile
**last_researched_date**: 2026-05-12
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
**date_added**: 2026-05-13
**country**:   CL — Chile
**operator**:  Geocom S.A. — Chilean Trimble distributor (`geocom.cl`)
**type**:      physical single-base / VRS
**host:port**: `ntrip.geocom.cl:2101` (SOURCETABLE 200 OK 2026-05-12; `Server: Pycaster Ntrip Version 1`;
               one public mountpoint `TEST_RTCM`, production mountpoints credential-gated)
**access**:    paid subscription; 6-month demo reportedly available on request; pricing not
               on public website; ventas@geocom.cl / +562 2480 3600. A free "GEOCASTER"
               service for GEOCOM-equipment owners is also announced (hobbyist access outside
               their equipment ecosystem undocumented).
**registration**: `geocom.cl/pages/red-gnss`
**yearly_cost**: not publicly listed
**stations**:  not published; coverage spans Calama, Antofagasta, Los Andes, Santiago, Talca,
               Concepción, Los Ángeles, Temuco, Valdivia, Osorno, Puerto Montt (~23°S–41°S)
**last_researched_date**: 2026-05-12

Geocom's GNSS network provides RTK corrections for professional survey use
across Chile. Network calculated at epoch 2025.0 and linked to SIRGAS via
fiducial stations. Not added to pipeline: paid service.

---

## kollnet_cl — KollNET (CL)

**status**:    paid
**date_added**: 2026-05-13
**country**:   CL — Chile
**operator**:  Kollner Labraña & Cía. Ltda. (`kollnerlabrana.cl`)
**type**:      physical single-base / VRS (8 reference stations)
**host:port**: not publicly documented; provided after purchase. Caster port 2101 timed out
               from external IPs in 2026-05-06 and 2026-05-12 probes — consistent with
               purchase-gated access
**access**:    paid prepaid packages (brand-agnostic NTRIP receiver accepted; no annual contract required)
**registration**: `kollnerlabrana.cl/kollnet.html`
**yearly_cost**: tariff confirmed 2026-05-12 (CLP, +19% IVA): CLP 48,000 / 7 days · CLP 60,000 /
               15 days · CLP 85,000 / 30 days · CLP 180,000 / 3 mo · **CLP 450,000 / 12 mo**
               (~$470/yr at 2026-05-12 spot rate — over $200/yr cutoff)
**yearly_cost_normalized**: 470
**stations**:  8 (Santiago, Valparaíso, Los Andes, Santa Cruz, Talca, Chillán, Temuco, Frutillar);
               claimed precision 1–4 cm HRMS within ~100 km per station
**last_researched_date**: 2026-05-12

Commercial NTRIP CORS correction service operated by a Chilean surveying
equipment company. Brand-agnostic — any NTRIP-capable RTK receiver accepted.

---

## ign_cr_cors — IGN-CR CORS / SNIT NTRIP Caster (CR)

**status**:    free
**date_added**: 2026-05-13
**country**:   CR — Costa Rica
**operator**:  IGN-CR — Instituto Geográfico Nacional (within Registro Nacional, Ministerio de
               Justicia y Paz; SNIT — Sistema Nacional de Información Territorial)
**type**:      physical single-base (14 stations); no VRS computed stream
**host:port**: `igncaster.snitcr.go.cr:2101` — SOURCETABLE 200 OK confirmed via direct fetch
               2026-05-12 (`Server: NTRIP BKG Caster/2.0.44`; 14 STR + 1 CAS + 1 NET; reference
               point 9.92°N / -84.05°W Curridabat/San José)
**access**:    free-with-registration — SNIT account required; account credentials validated
               against caster at 12:00 midnight and 12:00 noon CR time (UTC−6); initial access
               may take up to 12 h after registration
**registration**: `snitcr.go.cr` (Herramientas → Herramientas GNSS → Caster → accept T&Cs)
**stations**:  14 physical (QUEP3 Quepos, LBRA3 Liberia, NYCO3 Nicoya, SAGE3 San-Isidro-PZ,
               NEIL3 Ciudad-Neilly, CIQE3 Ciudad-Quesada, PUNT3 Puntarenas, RIDC3 Curridabat,
               LIMN3 Limón, BRBR3 Bribri, CHLS3 Los-Chiles, LCRZ3 La-Cruz, CAPO3 Cariari,
               PJMZ3 Puerto-Jiménez); all RTCM 3.3 GPS+GLO+GAL+BDS, message types 1004 + 1008
               only (no MSM); Trimble TRM159900.00 SCIS; all streams tagged "Prueba" in misc
**reference_frame**: CR05 / CRTM05 (ITRF-aligned)
**last_researched_date**: 2026-05-12

Real-time NTRIP corrections and RINEX via the SNIT platform; caster
software BKG NtripCaster 2.0.44 (advertises as `Caster-Nacional-Costa-Rica`).
No VRS computed stream — per-physical-station only; for sites further than
~20 km from the nearest station, RTK fix quality degrades. Private commercial
**PX GNSS** (`pxgnss.com`) operates 13-station network with cm RTK; no public
host:port or pricing.

Volunteer alternatives: 3 CRI-coded rtk2go bases (`DGEOB1` Liberia/Guanacaste,
`DoleVNC`, `OVSI`) + 2 EarthScope stations (`QSEC_RTCM3P3`, `VRAI_RTCM3P3`)
useful as cross-check or backup if SNIT account validation is delayed.

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
**date_added**: 2026-05-06
**country**:   KE
**type**:      physical-coord-vrs
**host:port**: host:port disclosed post-registration (IP, port, username,
               password issued after signup at `muya-cors.com`)
**access**:    paid with registration; self-serve signup via muya-cors.com;
               Mpesa payment supported; contact via `muya-cors.com` for pricing
**yearly_cost**: not publicly listed; flexible tiers (hourly/daily/monthly);
                 pricing provided on inquiry
**stations**:  25+ base stations across Kenya (GPS/GLONASS/BeiDou/Galileo)
**operator**:  Measurement Systems Ltd, Nairobi
               operating as Muya CORS (`muya-cors.com`)
**source**:    muya-cors.com; orbital.co.ke (field use report, Feb 2025 Kitisuru)

Muya CORS provides RTK corrections and post-processing services via a
network of GNSS CORS. Credentials are issued post-registration. Pricing is
not publicly disclosed; flexible tiers (hourly/daily/monthly). Mpesa payment
and individual registration confirmed — no surveying licence requirement.
Operationally confirmed in active use Feb 2025 (Orbital Africa case study,
Kitisuru, Nairobi). Only confirmed commercial RTK NTRIP option for Kenya.

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

**status**:    restricted
**date_added**: 2026-05-06
**country**:   MA
**type**:      physical-coord-vrs
**host:port**: host:port not publicly listed; registration at ancfcc.gov.ma required
**access**:    restricted — licensed cadastral professional access only; no self-service
               registration path for hobbyists; contact ANCFCC via +212 6 60 10 27 01–06
**stations**:  60 permanent GNSS stations including nodes at Laayoune and Dakhla
**source**:    ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/
**operator**:  ANCFCC — Agence Nationale de la Conservation Foncière, du Cadastre et de la Cartographie

60-station national GNSS network connected to a central server in Rabat via private
network. Services confirmed (ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/,
observed 2026-05-06): (1) RINEX at 1/5/10/15/20/30/60 s; (2) online coordinate
computation; (3) real-time RTK and RTK-Network corrections via internet (NTRIP protocol
explicitly stated). Host:port not published; registration required; professional access only.

---

## itri_ma — itri permanent GNSS network (MA)

**status**:    restricted
**date_added**: 2026-05-06
**country**:   MA
**type**:      physical-coord-vrs
**host:port**: not publicly listed; credentials issued post-registration via
               secure.itri-gnss.ma/admin/auth/register
**access**:    professional subscription; pricing not public; contact via `itri-gnss.ma`
**stations**:  231 permanent GNSS stations (as of 2026-05-06)
**operator**:  SAMTOP / itri — itri-gnss.ma
**registration**: https://secure.itri-gnss.ma/admin/auth/register

Morocco's first private permanent GNSS network, designed by SAMTOP and launched 2020.
231 stations nationwide; GPS+GLONASS+Galileo+BeiDou. Correction modes: single-base RTK,
network RTK, VRS. RINEX post-processing also provided. Marketed "dédié aux professionnels";
hobbyist eligibility not confirmed. Caster port 2101 returned ECONNREFUSED from outside
Morocco 2026-05-06 — endpoint is private.

---

## sen_cors — SEN-CORS (SN)

**status**:    other
**date_added**: 2026-05-06
**country**:   SN
**type**:      physical-coord-vrs
**host:port**: `caster.geodesie.sn:2101`
**access**:    paid subscription — tariff not publicly listed without account login;
               registration at geodesie.sn requires username/name/email/company;
               no stated residency restriction; contact ANAT (`anat.sn`)
**stations**:  ~21 (16 PROCASEF/World Bank stations 2022–2024 + 5 JICA stations
               integrated 2025; coverage across Senegal)
**source**:    geodesie.sn; anat.sn; procasef.com; ignfi.fr
**operator**:  ANAT (Agence Nationale de l'Aménagement du Territoire) and
               DTGC (Direction des Travaux Géographiques et Cartographiques)

SENCORS (geodesie.sn) is Senegal's national GNSS correction network, built
2022–2024 via PROCASEF (World Bank funding) plus 5 JICA-backed stations integrated
2025. Backend is Leica Spider Business Center; delivers VRS/Network-RTK corrections.
Portal went live early 2025; suffered a disk failure January 2026 and was restored
March 16, 2026. As of May 2026 the network is operational. The subscription plan
is described as "90 jours — Forfaitaire — Illimitée" (90-day flat-rate unlimited);
pricing in XOF/USD is not visible without account login.
`weird` status: operational with a publicly documented host:port but undisclosed
tariff — cannot determine whether it falls within hobbyist cost range.

---

## ghana_cors — Ghana National CORS Network (GH)

**status**:    other
**date_added**: 2026-05-13
**country**:   GH — Ghana
**last_researched_date**: 2026-05-12
**type**:      unknown
**host:port**: not publicly listed
**access**:    no public NTRIP endpoint found; access appears to be via licensed-surveyor
               channel (PPP with GMX Systems Ghana Ltd and Geo-Tech Systems Ltd)
**yearly_cost**: not applicable (no public commercial tier found)
**stations**:  ~60 deployed nationwide as of Aug 2025; target 100 by end of 2025
**operator**:  Survey and Mapping Division (SMD), Lands Commission (`lc.gov.gh`),
               in PPP with GMX Systems Ghana Ltd and Geo-Tech Systems Ltd
**source**:    gpsworld.com (GPS World Aug 2025); gna.org.gh (Ghana News Agency Aug 2025);
               wgicouncil.org (WGIC Africa geospatial PPPs report); lc.gov.gh

Ghana National CORS Network officially unveiled August 19 2025 by the Lands Commission
and its PPP partners GMX Systems Ghana Ltd and Geo-Tech Systems Ltd. Nationwide
observation exercise launched to tie ~60 newly established stations into the Ghana Grid
Coordinate System. Target of 100 stations by end of 2025. Simultaneously launched a
"digital geospatial data system" (DGDS) for 24/7 geospatial data access. The network is
cited as the "most extensive CORS network in West Africa" in the WGIC Africa geospatial
PPPs report. No public NTRIP host:port or hobbyist registration portal has been found.

**missing**: confirm whether a public NTRIP endpoint or hobbyist-accessible subscription
             service is available; check lc.gov.gh for service announcements.

## etcors — ETCORS (ET)

**status**:    other
**date_added**: 2026-05-13
**last_researched_date**: 2026-05-12
**country**:   ET — Ethiopia
**type**:      unknown (no confirmed public NTRIP endpoint)
**host:port**: not publicly listed
**access**:    unknown — no public registration portal or caster host:port found
**registration**: https://ssgi.gov.et
**stations**:  10 (Addis Ababa, Bonga, Semera, Jigjiga, Debre Berhan, Jimma,
               plus 4 in Sheger and surrounding towns); planned expansion to
               20 in 2024/25 and ~200 long-term
**operator**:  SSGI — Space Science and Geospatial Institute (`ssgi.gov.et`);
               successor to the Ethiopian Mapping Agency / EGIA

Ethiopia's national CORS network (ETCORS) was inaugurated December 2024 by the
Space Science and Geospatial Institute. State media described centimetre-level
real-time accuracy. Director Abdisa Yilma stated intent to expand to 20 stations
within the 2024/25 fiscal year and ~200 long-term. No public NTRIP caster
host:port, registration portal, or tariff has been announced; access appears to
require direct contact with SSGI. The SSGI is the natural successor to the
Ethiopian Mapping Agency (EMA), later EGIA, merged into SSGI in 2022. Surfaced
as a `weird` country marker so hobbyists visiting Ethiopia know a nascent
correction service exists and can follow its rollout via ssgi.gov.et.

**missing**: confirm whether a public NTRIP endpoint or registration portal is
             available; check ssgi.gov.et or ethionsdi.gov.et for announcements.
