# Free RTK NTRIP networks — technical record

_Authoritative reference for every network investigated, whether in pipeline or not._
_Read before touching `scripts/fetch_stations.py` or `index.html`._
_Networks are identified via `docs/country-survey.md` and `docs/global-survey.md`;_
_detail, endpoints, and pipeline status live here._

_Last updated: 2026-04-20._

---

## Format

Each entry uses these fields. Omit fields that don't apply (e.g. `host:port` for
candidates whose endpoint is withheld).

```
## <id> — <Name> (<COUNTRY>)

**status**:    in-pipeline | candidate | deferred | paid-affordable | paid | rejected
**host:port**: `host:port`
**type**:      single-base | physical-coord-vrs | single-coord-vrs
**access**:    free / registration / paid [brief terms]
**stations**:  N (approximate)
**source**:    url [, url …]

[Notes: gotchas, drop rationale — 1–5 lines.]

**investigate**: what to verify before the next pipeline change (CI-failing entries)
**missing**:    what a new session must find before this can be ingested (deferred entries)
```

Status glossary:
- **in-pipeline** — present in `SOURCES` in `scripts/fetch_stations.py`
- **candidate** — confirmed free, endpoint known, not yet ingested
- **deferred** — free but endpoint missing or requires live registration to obtain
- **paid-affordable** — paid, under the project's $200/yr cutoff; surfaced in UI as fallback
- **paid** — paid, over cutoff, or structurally restricted
- **rejected** — investigated and explicitly excluded; reason documented

---

## In-pipeline — single-base

Physical stations with distinct coordinates shown on map.

---

## rtk2go — RTK2GO (global)

**status**:    in-pipeline
**host:port**: `rtk2go.com:2101`
**type**:      single-base
**access**:    free, no registration (username = any email, password = `none`)
**stations**:  ~863
**source**:    rtk2go.com; use-snip.com

Community volunteer aggregator operated by SNIP / use-snip.com. `NEAR` mountpoint
requires rover NMEA GGA. Regional filtered views on `:2103` (PL) and `:2104` (JP)
are the same server — not separate SOURCES entries. Parser infers `carrier = 2`
when carrier field is blank and format starts with `RTCM 3` (required to retain
~98% of rtk2go entries).

---

## centipede — CentipedeRTK (global, France-centric)

**status**:    in-pipeline
**host:port**: `crtk.net:2101`
**type**:      single-base
**access**:    free, no registration (username = `centipede`, password = `centipede`)
**stations**:  ~1203
**source**:    centipede-rtk.org

Volunteer network initiated by INRAE (2019); now operated by non-profit
Centipede-RTK association (formed Aug 2024). Open-source Millipede caster stack
(BSD-3). Migrated from `caster.centipede.fr` to `crtk.net` on 2025-03-18.
`NEAR` mountpoint requires rover GGA; `NEAR4` for older equipment. 30+ countries
through one federation endpoint; no separate country-specific instances found.

---

## frednet — FReDNet (IT + border AT/SI)

**status**:    in-pipeline
**host:port**: `gnsscaster.regione.fvg.it:8080`
**type**:      physical-coord-vrs
**access**:    sourcetable open; stream requires free email registration
**stations**:  ~39
**source**:    frednet.crs.ogs.it; gnsscaster.regione.fvg.it

Operated by OGS (Istituto Nazionale di Oceanografia e Geofisica Sperimentale).
Crustal-deformation network for Friuli-Venezia Giulia; coverage extends into
Slovenia and W Austria. Register by emailing rete.gnss.marussi@regione.fvg.it.

---

## geortk — GeoRTK (JP)

**status**:    in-pipeline
**host:port**: `geortk.jp:2101`
**type**:      single-base
**access**:    free, no registration; free indefinitely (1-yr advance notice if changed)
**stations**:  ~41
**source**:    geortk.jp (Geosense Co., Ltd.)

Japan volunteer caster. ~66 STR lines total; ~25 report 0/0 (offline bases) and
are dropped by coordinate filter. Sourcetable has shrunk over time.

---

## auscors — AUSCORS (AU)

**status**:    in-pipeline
**host:port**: `ntrip.data.gnss.ga.gov.au:2101`
**type**:      single-base
**access**:    free; register at gnss.ga.gov.au/registration; CC BY 4.0
**stations**:  ~813
**source**:    gnss.ga.gov.au; auscors.ga.gov.au (dead since Jul 2022)

Operated by Geoscience Australia. Old host `auscors.ga.gov.au` dead since Jul 2022.
TLS also available on port 443. Attribute "© Commonwealth of Australia (Geoscience Australia)".

---

## positionz — PositioNZ-RT (NZ)

**status**:    in-pipeline
**host:port**: `positionz-rt.linz.govt.nz:2101`
**type**:      single-base
**access**:    free; LINZ account + email positionz@linz.govt.nz; CC BY 4.0 NZ
**stations**:  ~62
**source**:    linz.govt.nz; toitutewhenua.govt.nz

NZ mainland + Chatham Islands + Antarctica. Streaming latency reduced ~90% in
Dec 2023 upgrade. Attribute "Source: Land Information New Zealand".

---

## trignet — TrigNet (ZA)

**status**:    in-pipeline
**host:port**: `trignet.co.za:2101`
**type**:      single-base
**access**:    free; register at trignet.co.za
**stations**:  ~72
**source**:    trignet.co.za (NGI / National Geospatial Information, DALRRD)

All NGI products and services free of charge. No explicit CC licence; public mandate.
Single-base RTK (~5 cm) within 30–40 km; Network RTK (~3 cm) in Gauteng,
Western Cape, KwaZulu-Natal clusters only.

---

## rbmc_ip — RBMC-IP (BR)

**status**:    in-pipeline
**host:port**: `gps-ntrip.ibge.gov.br:2101`
**type**:      single-base
**access**:    free; gov.br signup; 5-station limit per user; 1,000 concurrent max
**stations**:  ~140
**source**:    ibge.gov.br; gps-ntrip.ibge.gov.br

Alt IP: `170.84.40.52:2101`. 150 stations as of Dec 2024 (IBGE added 5 in Dec 2024).

---

## ramsac — RAMSAC-NTRIP (AR)

**status**:    in-pipeline
**host:port**: `ntrip.ign.gob.ar:2101`
**type**:      single-base
**access**:    free; email ntrip@ign.gob.ar or ign.gob.ar portal; 8-hr session cap
**stations**:  ~203
**source**:    ign.gob.ar

POSGAR 07 reference frame.

---

## earthscope — EarthScope NOTA (Americas)

**status**:    in-pipeline
**host:port**: `ntrip.earthscope.org:2101`
**type**:      single-base
**access**:    free non-commercial (annual NULA renewal); commercial use per-seat licensed
**stations**:  ~1096
**source**:    earthscope.org/data/gnss-realtime/

Americas-wide. Also `:2105` (BINEX), `:2108` (PPP solutions). RTCM 3.3 MSM.
Legacy UNAVCO platform retired 2025-07-29; all users must use ntrip.earthscope.org.
Hobbyist and small-shop use confirmed in scope. Metadata/station-list display
permitted per NULA.

---

## mirai — MIRAI / Go!GNSS (JP + overseas partners)

**status**:    in-pipeline
**host:port**: `ntrip.go.gnss.go.jp:2101`
**type**:      single-base
**access**:    free incl. commercial + automated ("peaceful purposes"); separate NtripCaster auth form
**stations**:  ~325
**source**:    go.gnss.go.jp (Cabinet Office SPAC)

Register at go.gnss.go.jp plus a separate NtripCaster authorization application.
Accounts expire after 365 days inactivity. Raw observations only (rover computes
RTK baseline). L1C/B support for QZSS QZS-6 added Jun 2025.

---

## cors_korea — CORS-KOREA (KR)

**status**:    in-pipeline
**host:port**: `www.gnssdata.or.kr:2101`
**type**:      physical-coord-vrs
**access**:    free; sourcetable public without auth; stream registration may require Korean national ID
**stations**:  ~498
**source**:    gnssdata.or.kr (NGII)

VRS + FKP. ~90–100 physical stations at ~40 km spacing. Korean-language portal;
international access may be impractical if national ID is required.

---

## In-pipeline — physical-coord VRS

Sourcetable exposes real antenna locations; rover connects via VRS mountpoints.
Map shows physical station pins.

---

## ergnss — ERGNSS (ES)

**status**:    in-pipeline
**host:port**: `ergnss-ip.ign.es:2101`
**type**:      physical-coord-vrs
**access**:    free; register at ergnss.ign.es/gnuserportal/ (immediate); CC-compatible
**stations**:  ~128
**source**:    ergnss.ign.es (IGN — Instituto Geográfico Nacional)

~120 physical stations. GPS+GLO+GAL+BDS. Attribution to IGN required per
Orden FOM/2807/2015. RAP (Andalucía) supplements in the south; separate signup.

---

## satref — SatRef (HK)

**status**:    in-pipeline
**host:port**: `ntrip.geodetic.gov.hk:2101`
**type**:      physical-coord-vrs
**access**:    free; email geodetic@landsd.gov.hk or DATA.GOV.HK open-data path
**stations**:  ~22
**source**:    geodetic.gov.hk (Lands Department, Survey & Mapping Office)

19 physical stations (16 reference + 3 integrity monitoring). Mountpoint `VRS32G`
(GPS+GLO+GAL+BDS). Open data policy (commercial and non-commercial reuse permitted).
Migrated to `ntrip.geodetic.gov.hk` Jun 2023; old `www.geodetic.gov.hk` domain
for NTRIP decommissioned. Accounts inactive 12+ months are terminated.
Raw TCP (NTRIP 1.0) fallback required in fetcher — responds `SOURCETABLE 200 OK`,
not HTTP.

---

## inacors — InaCORS (ID)

**status**:    in-pipeline
**host:port**: `nrtk.big.go.id:2001`
**type**:      physical-coord-vrs
**access**:    free; register at nrtk.big.go.id; Law No. 4/2011 mandates free public service
**stations**:  ~4
**source**:    big.go.id (BIG — Badan Informasi Geospasial)

Port 2001, not 2101. 200+ stations declared; only ~4 unique coords appear in
sourcetable — likely partial data exposure. 16,800+ registered users as of last report.

---

## igac — IGAC MAGNA-ECO (CO)

**status**:    in-pipeline
**host:port**: `sbc.igac.gov.co:2101`
**type**:      physical-coord-vrs
**access**:    free; register at redgeodesica-sbc.igac.gov.co/sbc; Law 1955/2019 mandates public access
**stations**:  ~17
**source**:    igac.gov.co; redgeodesica-sbc.igac.gov.co

233 stations declared; 17 unique coords in sourcetable. VRS also on `:2102`.
National Geodetic Control Centre launched Apr 2024 (Resolution 1771/2024).
First confirmed free VRS/NRTK in Latin America.

---

## spslux — SPSLux (LU)

**status**:    in-pipeline
**host:port**: `stream.spslux.lu:5005`
**type**:      physical-coord-vrs
**access**:    free; register at spslux.lu/SBC/Account/Register (subscribe "SPSLUX (N)RTK")
**stations**:  ~17
**source**:    spslux.lu (ACT — Administration du Cadastre et de la Topographie)

Port 5005, not 2101. IP 185.106.24.68. Luxembourg open-data policy — all services
free of charge.

---

## icecors — IceCORS (IS)

**status**:    in-pipeline
**host:port**: `178.19.53.126:2101`
**type**:      physical-coord-vrs
**access**:    free ("data is free of charge" — natt.is); register at natt.is/is/landmaelingar/jardstodvakerfi
**stations**:  ~20 (populates on fetch; recently added to pipeline)
**source**:    natt.is (LMÍ — Landmælingar Íslands)

GNCASTER software (same as SAPOS). Offers VRS (VRS30, FKP30) and single-base
(RTCM30). Stream credentials via icecors@natt.is.

---

## SAPOS — Germany (DE, 16 Bundesländer)

**status**:    in-pipeline (all 16 states)
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

**status**:    in-pipeline
**host:port**: `aposrtk.bev.gv.at:2101`
**type**:      physical-coord-vrs
**access**:    conditions — free for agriculture/forestry via eAMA credentials
               (farm client number + PIN from Agrarmarkt Austria);
               professional/hobbyist use paid via bev.gv.at portal
**yearly_cost**: pricing via bev.gv.at for professional/hobbyist use;
               eAMA free for agriculture/forestry
**stations**:  37
**source**:    bev.gv.at (BEV — Bundesamt für Eich- und Vermessungswesen)

Austria's national VRS network (Free* in UI). Sourcetable is publicly readable;
RTCM stream authentication requires valid credentials. Hobbyists without farm
credentials register and pay via the BEV portal. 37 physical reference stations
with distinct coordinates are exposed in the sourcetable; these show on the map
as regular pins. SAPOS Bavaria (DE) and FReDNet (IT) provide partial coverage
across the AT border.

---

## In-pipeline — single-coord VRS / connectivity failures

Networks in pipeline that yield 0 map stations: either all sourcetable entries
share one coordinate (VRS filter drops them), or the caster is unreachable and
no cached sourcetable exists. Stations remain in JSON from last successful fetch
once a cache exists.

---

## asg_eupos — ASG-EUPOS (PL)

**status**:    in-pipeline
**host:port**: `system.asgeupos.pl:2101`
**type**:      single-coord-vrs
**access**:    free since Oct 2022; web signup; admin approval 1–2 working days
**stations**:  0 (130+ declared; single coord 52.0, 21.0 Warsaw)
**source**:    system.asgeupos.pl (GUGiK)

Also ports :8080/:8082/:8083/:8086 for VRS variants. GPS+GLO+GAL+BDS.
VRS (NAWGIS/KODGIS/FKP/MAC). Coverage requires NRTK polygon (deferred).

---

## flepos — FLEPOS (BE — Flanders)

**status**:    in-pipeline
**host:port**: `flepos.vlaanderen.be:2101`
**type**:      single-coord-vrs
**access**:    free for all uses; web self-signup at flepos.vlaanderen.be
**stations**:  0 (45 declared; single-coord Flanders centroid)
**source**:    flepos.vlaanderen.be

Old endpoint `ntrip.flepos.be` is NXDOMAIN as of 2026-04. Currently timing out
in CI. Coverage requires NRTK polygon (deferred).

**investigate**: connect from a European IP — could be location-based firewall rather
than egress block; also verify `flepos.vlaanderen.be:2101` still resolves correctly.

---

## walcors — WALCORS (BE — Wallonia)

**status**:    in-pipeline
**host:port**: `gnss.wallonie.be:2101`
**type**:      single-coord-vrs
**access**:    free for positioning; paid for machine-control/auto-guidance (commercial resellers)
**stations**:  0 (23 declared; single-coord VRS; intermittently unreachable)
**source**:    gnss.wallonie.be (gnss@spw.wallonie.be, SPW)

Intermittent outages documented. Currently timing out in CI.

**investigate**: check gnss.wallonie.be status page or contact gnss@spw.wallonie.be;
distinguish persistent outage from intermittent — if dead >4 weeks, drop from pipeline.

---

## latpos — LatPos (LV)

**status**:    in-pipeline
**host:port**: `latpos.lgia.gov.lv:5001`
**type**:      single-coord-vrs
**access**:    free since 2018; SBC portal signup at latpos.lgia.gov.lv/SBC
**stations**:  0 (27 LV + 5 EE + 4 LT border stations declared; single-coord)
**source**:    latpos.lgia.gov.lv (LGIA)

Port 5001, not 2101 (confirmed per Alberding caster directory). Currently timing
out in CI.

**investigate**: re-verify port 5001 at latpos.lgia.gov.lv directly (try telnet/ncat
from a Baltic-region IP); also check LGIA website for endpoint changes.

---

## estpos — ESTPOS (EE)

**status**:    in-pipeline
**host:port**: `gnss-rtk.maaamet.ee:8083`
**type**:      single-coord-vrs
**access**:    free until 31 Aug 2026 (director-general directive); portal account + service agreement
**stations**:  0 (40 declared; VRS, iMAX, nearest-base; MSM5 available)
**source**:    geoportaal.maaamet.ee (Maa-amet / Land and Spatial Development Board)

Port 8083. Currently timing out in CI. Service expiry Aug 2026 — review before then.

**investigate**: verify `gnss-rtk.maaamet.ee:8083` from an Estonian IP; check
geoportaal.maaamet.ee for credential requirement (may now need service agreement
before sourcetable is served). Re-confirm free status before Aug 2026 or drop.

---

## ksa_cors — KSA-CORS (SA)

**status**:    in-pipeline
**host:port**: `ksacors.geoportal.sa:2101`
**type**:      single-coord-vrs
**access**:    free; registration: sign form + email info@geosa.gov.sa
**stations**:  0 (209 declared; single-coord; GPS+GLO+GAL+BDS)
**source**:    ksacors.geoportal.sa (GASGI/GEOSA)

Old endpoint `KSACORS.gcs.gov.sa` is NXDOMAIN as of 2026-04. Currently timing
out in CI. Coverage requires NRTK polygon (deferred).

**investigate**: verify `ksacors.geoportal.sa:2101` resolves and is reachable; try
connecting from a GCC-region IP; check geoportal.sa for updated endpoint or
registration requirement changes.

---

## cropos — CROPOS (HR)

**status**:    in-pipeline
**host:port**: `gnss.cropos.hr:2101`
**type**:      single-coord-vrs
**access**:    free since Apr 2022 (Narodne novine 39/2022); email/web registration at cropos.hr
**stations**:  0 (35 declared; sourcetable reports 0/0 for all mountpoints)
**source**:    cropos.hr (DGU)

Caster IP changed Nov 2023 (old: 195.29.118.122 → new: 195.29.198.194); DNS
hostname should resolve correctly. DPS (~0.3–0.5 m) and VPPS (~2 cm) free;
GPPS post-processing paid. Coverage requires NRTK polygon (deferred).

---

## In-pipeline — new / under test

---

## geodnet_usa — GEODNET USA

**status**:    in-pipeline (testing sourcetable accessibility)
**host:port**: `rtk.geodnet.com:2101`
**type**:      single-base
**access**:    paid ($40/month after 30-day trial)
**stations**:  TBD
**source**:    geodnet.com (HYFIX.AI)

Testing whether sourcetable is publicly readable without auth per NTRIP spec.
If stations returned, display as paid-service layer. $40/mo × 4 months = $160
< $200/yr cutoff for seasonal use.

---

## geodnet_eu — GEODNET Europe

**status**:    in-pipeline (testing sourcetable accessibility)
**host:port**: `eu.geodnet.com:2101`
**type**:      single-base
**access**:    paid ($40/month)
**stations**:  TBD
**source**:    geodnet.com (HYFIX.AI)

---

## geodnet_aus — GEODNET Australia

**status**:    in-pipeline (testing sourcetable accessibility)
**host:port**: `aus.geodnet.com:2101`
**type**:      single-base
**access**:    paid ($40/month)
**stations**:  TBD
**source**:    geodnet.com (HYFIX.AI)

---

## geodnet_sa — GEODNET South America

**status**:    in-pipeline (testing sourcetable accessibility)
**host:port**: `sa.geodnet.com:2101`
**type**:      single-base
**access**:    paid ($40/month)
**stations**:  TBD
**source**:    geodnet.com (HYFIX.AI)

---

## Candidates — confirmed free, not yet ingested

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

## wiscors — WISCORS (US-WI)

**status**:    candidate
**host:port**: `wi-cors.wisc.edu:2101` (to verify)
**type**:      physical-coord-vrs (single-base + VRS)
**access**:    free; registration at wi-cors.wisc.edu
**stations**:  ~180
**source**:    wi-cors.wisc.edu (University of Wisconsin–Madison Survey Science)

Wisconsin CORS Network operated by UW-Madison. Offers both single-base streams
and VRS corrections. Note: many WI stations also appear in EarthScope NOTA —
verify overlap before ingesting to avoid duplicate pins. Physical stations should
show distinct coordinates.

**missing**: verify `wi-cors.wisc.edu:2101` returns an NTRIP sourcetable and confirm
station overlap with EarthScope NOTA.

---

## Deferred — free, endpoint not yet obtainable

---

## renep — ReNEP (PT)

**status**:    deferred
**host:port**: withheld until post-registration
**type**:      physical-coord-vrs
**access**:    free; register at renep.dgterritorio.gov.pt (renep@dgterritorio.pt)
**stations**:  47
**source**:    dgterritorio.gov.pt (DGT — Direção-Geral do Território)

Host:port disclosed only after account approval. ETRS89 datum (mainland),
ITRF93 (autonomous regions). Stations and RINEX publicly visible.

**missing**: caster host:port — register at renep.dgterritorio.gov.pt to obtain;
or check Alberding directory / EUREF caster list for a public mirror.

---

## litpos — LitPOS (LT)

**status**:    deferred
**host:port**: not publicly listed
**type**:      physical-coord-vrs
**access**:    free (publicly-funded EUPOS member); register at geoportal.lt/web/litpos-en
**stations**:  35
**source**:    geoportal.lt (GIS-Centras)

RTCM 2.1/2.3/3.1/3.2, CMR, CMR+, CMRx. NTRIP host:port not publicly listed —
find via ArduSimple or Alberding caster directory before ingesting.
Contact LitPOS@geoportal.lt to confirm.

**missing**: caster host:port — search Alberding EUPOS directory (eupos.org),
ArduSimple country list, or email LitPOS@geoportal.lt.

---

## thailand_dol — Thailand DOL LandGNSS (TH)

**status**:    deferred
**host:port**: not publicly found
**type**:      unknown
**access**:    confirmed free government service; register at dol-rtknetwork.com
**stations**:  unknown
**source**:    dol-rtknetwork.com (Department of Lands, Ministry of Interior)

Thai-language portal and manual. Connection details documented in Thai-language
manual at dol-rtknetwork.com. Host:port not found in public aggregators.
Direct contact with Dept of Lands required before ingesting.

**missing**: caster host:port and station count — download Thai manual from
dol-rtknetwork.com or contact rtk@dol.go.th.

---

## mncors — MnCORS (US-MN)

**status**:    deferred
**host:port**: not confirmed
**type**:      physical-coord-vrs (single-base + Network RTK)
**access**:    free; registration at mndot.gov
**stations**:  ~125
**source**:    mndot.gov (Minnesota Department of Transportation)

Minnesota CORS Network operated by MnDOT. Note: significant overlap expected
with EarthScope NOTA — verify before ingesting.

**missing**: confirm NTRIP host:port (search MNDOT CORS manual or Alberding
caster list); verify EarthScope overlap.

---

## orgn — ORGN (US-OR)

**status**:    deferred
**host:port**: not confirmed
**type**:      single-base
**access**:    free; registration at oregon.gov
**stations**:  ~100
**source**:    oregon.gov (Oregon Department of Transportation)

Oregon GPS Network (ORGN) operated by ODOT. Primarily single-base streams.
Significant overlap with EarthScope expected.

**missing**: confirm NTRIP host:port.

---

## msrn — MSRN (US-MI)

**status**:    deferred
**host:port**: not confirmed
**type**:      physical-coord-vrs
**access**:    free; registration at michigan.gov
**stations**:  ~120
**source**:    michigan.gov (Michigan Department of Transportation)

Michigan Spatial Reference Network operated by MDOT. Significant overlap
with EarthScope expected.

**missing**: confirm NTRIP host:port.

---

## nysnet — NYSNet (US-NY)

**status**:    deferred
**host:port**: not confirmed
**type**:      physical-coord-vrs
**access**:    free; registration via Cornell/NRCC
**stations**:  ~150
**source**:    nrcc.cornell.edu (Northeast Regional Climate Center / Cornell)

New York State GPS Network. Provides RTCM 3.x and VRS corrections. Significant
overlap with EarthScope expected.

**missing**: confirm current NTRIP host:port; verify whether Cornell NRCC still
operates this or whether it has been transferred to NYS DOT.

---

## zakpos — ZAKPOS (UA)

**status**:    deferred
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

## Paid — affordable (under $200/yr cutoff)

Surface in UI as paid alternatives for users in areas with no free coverage.

---

## hepos — HEPOS (GR)

**status**:    paid-affordable
**host:port**: `uranus.gr:2101`
**access**:    paid; ~€160/3 months or ~€480/yr unlimited; also per-minute pricing
**yearly_cost**: €160 per 3-month block (~$170); ~€480/yr unlimited (~$520) — 3-month
               option is under the $200 cutoff for seasonal hobbyist use
**stations**:  unknown
**source**:    ktimatologio.gr (HEPOS S.A.)

---

## rompos — ROMPOS (RO)

**status**:    paid-affordable
**host:port**: unknown
**access**:    paid credit-based system; ~€169/yr
**yearly_cost**: ~€169/yr (~$183) — under $200 cutoff
**stations**:  unknown
**source**:    rompos.ro

---

## Paid — over cutoff or structurally restricted

Brief entries only.

---

## signal — SIGNAL (SI)

**status**:    paid
**access**:    €829.44/yr (€622.08 early discount)
**yearly_cost**: €829.44/yr (~$905); €622.08 early-discount (~$680)
**source**:    gu-signal.si

---

## swepos — SWEPOS Network RTK (SE)

**status**:    paid
**access**:    ~9,000 SEK/yr ≈ $850; free DGNSS tier sub-metre only (out of scope)
**yearly_cost**: ~9,000 SEK/yr (~$850)
**source**:    lantmateriet.se

---

## cpos — CPOS/ETPOS (NO)

**status**:    paid
**access**:    NOK 8,000+/yr ≈ $740
**yearly_cost**: NOK 8,000+/yr (~$740)
**source**:    kartverket.no

---

## swipos — swipos (CH)

**status**:    paid
**access**:    CHF 1,500/yr ≈ $1,650; *Geoinformationsgesetz* SR 510.62 classifies RTK as value-added service
**yearly_cost**: CHF 1,500/yr (~$1,650)
**source**:    swisstopo.admin.ch

---

## sirent — SiReNT (SG)

**status**:    paid
**access**:    SGD $107/month ≈ $950/yr; 3-day trial requires SingPass (residents only)
**yearly_cost**: SGD $107/month (~SGD $1,284/yr, ~$960/yr)
**source**:    sla.gov.sg

---

## soi_cors — SoI-CORS (IN)

**status**:    paid
**access**:    free only for Central/State Government and academic institutions;
               private users ₹5,032/month ≈ $240/yr × ongoing
**yearly_cost**: ₹5,032/month (~$720/yr) for private users
**source**:    surveyofindia.gov.in

Promotional free 3-month window (Nov 2025–Jan 2026) expired. Worth revisiting if policy changes.

---

## tusaga — TUSAGA-Aktif (TR)

**status**:    paid
**host:port**: `212.156.70.42:2101` (also port 55600)
**access**:    paid; membership + annual fee to TKGM/HGM
**yearly_cost**: annual fee (amount not publicly listed); contact TKGM/harita.gov.tr
**stations**:  146
**source**:    tkgm.gov.tr; harita.gov.tr

---

## vngeonet — VNGEONET (VN)

**status**:    paid
**access**:    fees since Sep 2024 per Circular 47/2024/TT-BTC; pricing not public
**yearly_cost**: not publicly listed (fees per Circular 47/2024/TT-BTC since Sep 2024)
**stations**:  65
**source**:    vngeonet.vn (National Centre for Satellite Positioning Station Management)

Was free until Aug 2024.

---

## gnssnet_hu — GNSSnet.hu (HU)

**status**:    paid
**access**:    commercial; pricing not public
**yearly_cost**: not publicly listed
**source**:    gnssnet.hu

---

## egnss_tw — e-GNSS (TW)

**status**:    paid
**access**:    pay-per-use + paper form registration (mail/fax)
**yearly_cost**: pay-per-use (pricing not publicly listed)
**source**:    nlsc.gov.tw (NLSC/MoI)

---

## myrtk — MyRTKnet (MY)

**status**:    paid
**access**:    paid subscription (Survey Act cost-recovery); 78 stations
**yearly_cost**: not publicly listed
**source**:    jupem.gov.my

---

## pagenet — PAGeNet (PH)

**status**:    paid
**access**:    PHP 1,000 one-time + ongoing subscription (EO 471); 52 stations
**yearly_cost**: PHP 1,000 one-time (~$17) + subscription (ongoing amount not publicly listed)
**source**:    namria.gov.ph

---

## czepos — CZEPOS (CZ)

**status**:    paid
**access**:    free for education/government; commercial use paid (ČÚZK Decree 31/1995)
**yearly_cost**: not publicly listed for commercial use
**source**:    czepos.cuzk.gov.cz

Not a general hobbyist path.

---

## skpos — SKPOS (SK)

**status**:    paid
**access**:    free for public sector/municipalities; commercial use paid
**yearly_cost**: not publicly listed for commercial use
**source**:    skpos.gku.sk

Not a general hobbyist path.

---

## agros — AGROS (RS)

**status**:    paid
**access**:    paid; no English pricing page; contact rgz.gov.rs
**yearly_cost**: not publicly listed (contact RGZ/Republicka geodetska uprava)
**stations**:  ~30
**source**:    rgz.gov.rs (Republički geodetski zavod)

Serbia's national positioning network. Subscription required; no public free tier.

---

## montepos — MONTEPOS (ME)

**status**:    paid
**access**:    paid subscription tiers; contact upco.gov.me
**yearly_cost**: not publicly listed
**stations**:  ~20
**source**:    upco.gov.me (Uprava za nekretnine)

Montenegro's national CORS network. Paid service.

---

## bihos — BiHPOS (BA)

**status**:    paid
**access**:    paid; dual-entity administration (FBiH + RS) complicates access; limited resources
**yearly_cost**: not publicly listed
**stations**:  ~25 (estimate)
**source**:    fgu.com.ba / rgurs.rs (dual entity)

Bosnia and Herzegovina's CORS network, split between the Federation of BiH and
Republika Srpska geodetic authorities. Operational status uncertain.

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

**status**:    rejected
**reason**:    pervasive military GNSS spoofing active continuously since Oct 2023
               across Israel/Lebanon/Jordan/Sinai/Cyprus (~50,000 flights affected in 2024);
               RTK unreliable regardless of NTRIP access

---

## rtkdata_online — RTKdata.online

**status**:    rejected
**reason**:    server unreachable since launch; 0 stations ever collected; operated by
               Kansi Solutions GmbH (same parent as paid rtkdata.com); no independent
               data — aggregates rtk2go/Centipede visually
