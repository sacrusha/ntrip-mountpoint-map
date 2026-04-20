# Free RTK NTRIP networks — authoritative record

_Every network investigated, whether in pipeline or not. Updated 2026-04-20._
_Read this before touching `scripts/fetch_stations.py` or `index.html`._

---

## Confidence

**High:** RTK2GO, CentipedeRTK, ASG-EUPOS, FLEPOS, WALCORS, SAPOS (most Länder
free; BY €20/yr flat rate for non-agricultural, free for agriculture — under
$200/yr cutoff; SN confirmed endpoint `ntrip.sachsen.de:2101`; RP confirmed
free), CROPOS, FReDNet (IT), IBGE RBMC-IP, AUSCORS, PositioNZ NZ, MIRAI JP
(commercial + automated use confirmed), IceCORS IS (confirmed free — natt.is),
ERGNSS ES, SatRef HK, InaCORS ID, TrigNet ZA, RAMSAC AR, EarthScope NOTA US,
CORS-KOREA KR (free; sourcetable public; stream registration may require Korean
national ID). Also confirmed paid: SIGNAL SI, SKPOS SK, CZEPOS CZ, SWEPOS RTK SE,
swipos CH, TUSAGA-Aktif TR, VNGEONET VN (fees since Sep 2024),
HEPOS GR €160/yr, ROMPOS RO €169/yr (both under $200/yr cutoff — affordable).

**Moderate:** ReNEP PT (free+reg confirmed; host withheld until post-registration),
GeoDAF/ASI IT (EUREF raw, borderline out of scope), Thailand DOL LandGNSS TH
(confirmed free; host:port not yet found), LitPOS LT (confirmed free EUPOS member;
host:port not publicly listed).

---

## Drops from the starting list

| Network | Reason |
|---|---|
| NETPOS / Kadaster (NL) | Restricted to Kadaster/Rijkswaterstaat internal use. |
| EUREF-IP / IGS-IP | Raw GNSS observations only; explicitly unsuitable for real-time kinematic positioning. |
| FINPOS RTK (FI) | RTK granted only for research with written justification. DGNSS free but sub-metre — out of scope. |
| APN (IL) | Pervasive military GNSS spoofing active continuously since Oct 2023 across Israel/Lebanon/Jordan/Sinai/Cyprus. RTK unreliable regardless of NTRIP access. |
| RTKdata.online | Server unreachable since launch; 0 stations collected; no independent data (Kansi Solutions, same parent as paid rtkdata.com). |

---

## VRS — how it affects the map

VRS (Virtual Reference Station) networks generate corrections relative to a
virtual point near the rover. In sourcetables they appear in two ways:

**Physical-coord VRS** — sourcetable reports real antenna locations for each
physical base station. Rover connects using a VRS mountpoint; corrections are
network-derived but the map can show where the physical infrastructure is.
These networks pass the pipeline and appear on the map.

**Single-coord VRS** — sourcetable reports the same lat/lon for every virtual
mountpoint (typically a country centroid or a rounded city centre). The pipeline
drops these: all stations share one coordinate, triggering the VRS filter.
Result: 0 stations on map. Coverage for these networks requires NRTK polygons
(deferred feature).

**Zero-coord VRS** — sourcetable reports 0/0 for all mountpoints (no location
data exposed at all). Dropped by the coordinate filter. Same result: 0 stations.

---

## In pipeline — single-base (show on map)

Physical stations with distinct coordinates. Station count from live data.

| id | name | host:port | stations | notes |
|---|---|---|---|---|
| `rtk2go` | RTK2GO | `rtk2go.com:2101` | ~863 | Volunteer; username=any email, pass=`none`; `NEAR` requires GGA; `:2103` PL, `:2104` JP regional filtered views |
| `centipede` | CentipedeRTK | `crtk.net:2101` | ~1203 | Volunteer; user=`centipede`, pass=`centipede`; `NEAR` requires GGA; `NEAR4` for older equipment; migrated from caster.centipede.fr 2025-03-18 |
| `frednet` | FReDNet (OGS) | `gnsscaster.regione.fvg.it:8080` | ~39 | NE Italy + Slovenia/Austria border; sourcetable open; stream: email rete.gnss.marussi@regione.fvg.it |
| `geortk` | GeoRTK (Geosense) | `geortk.jp:2101` | ~41 | Japan only; no auth; ~25 of 66 STR lines report 0/0 (offline bases) and are dropped; free indefinitely |
| `auscors` | AUSCORS | `ntrip.data.gnss.ga.gov.au:2101` | ~813 | AU; single-base; CC BY 4.0; register gnss.ga.gov.au/registration; TLS also on :443 |
| `positionz` | PositioNZ-RT | `positionz-rt.linz.govt.nz:2101` | ~62 | NZ mainland + Chatham Is + Antarctica; single-base RTCM; CC BY 4.0 NZ; LINZ account + positionz@linz.govt.nz |
| `trignet` | TrigNet | `trignet.co.za:2101` | ~72 | ZA; register trignet.co.za |
| `rbmc_ip` | RBMC-IP (IBGE) | `gps-ntrip.ibge.gov.br:2101` | ~140 | BR; single-base; gov.br signup; 5-station limit per user |
| `ramsac` | RAMSAC-NTRIP | `ntrip.ign.gob.ar:2101` | ~203 | AR; single-base; 8-hr session cap; ntrip@ign.gob.ar or ign.gob.ar portal |
| `earthscope` | EarthScope NOTA | `ntrip.earthscope.org:2101` | ~1096 | Americas; RTCM 3.3 MSM; non-commercial annual NULA; earthscope.org/data/gnss-realtime/; UNAVCO retired 2025-07-29 |
| `mirai` | MIRAI (Go!GNSS) | `ntrip.go.gnss.go.jp:2101` | ~325 | JP + overseas partners; free incl. commercial + automated ("peaceful purposes"); go.gnss.go.jp + NtripCaster form; accounts expire after 365 days inactivity |
| `cors_korea` | CORS-KOREA | `www.gnssdata.or.kr:2101` | ~498 | KR; VRS+FKP; sourcetable public without auth; stream registration may require Korean national ID |

---

## In pipeline — physical-coord VRS (show on map)

Sourcetable reports real antenna locations; rover connects via VRS mountpoints.

| id | name | host:port | stations | notes |
|---|---|---|---|---|
| `ergnss` | ERGNSS (IGN) | `ergnss-ip.ign.es:2101` | ~128 | ES; ~120 stations; register ergnss.ign.es/gnuserportal/ — immediate; CC-compatible, attribute IGN |
| `satref` | SatRef HK | `ntrip.geodetic.gov.hk:2101` | ~22 | HK; 19 physical stations; mountpoint VRS32G; register geodetic.gov.hk |
| `inacors` | InaCORS | `nrtk.big.go.id:2001` | ~4 | ID; **port 2001**; 200+ stations declared; only 4 unique coords in sourcetable — likely partial data; register nrtk.big.go.id |
| `igac` | IGAC MAGNA-ECO | `sbc.igac.gov.co:2101` | ~17 | CO; 233 stations declared; law-mandated free (Law 1955/2019); Spider SBC at redgeodesica-sbc.igac.gov.co/sbc |
| `spslux` | SPSLux | `stream.spslux.lu:5005` | ~17 | LU; **port 5005**; register spslux.lu/sbc/; open data |
| `sapos_HE` | SAPOS Hessen | `sapos-he-ntrip.de:2101` | ~4 | DE; 3 unique coords; free; sapos.de |
| `sapos_RP` | SAPOS Rheinland-Pfalz | `sapos-ntrip.rlp.de:2101` | ~17 | DE; 5 unique coords; confirmed free; sapos.de |
| `sapos_SL` | SAPOS Saarland | `sapos-sl-ntrip.de:2101` | ~14 | DE; 9 unique coords; free; sapos.de |
| `icecors` | IceCORS | `178.19.53.126:2101` | TBD | IS; GNCASTER; VRS30/FKP30 + single-base RTCM30; free; register natt.is/is/landmaelingar/jardstodvakerfi |

---

## In pipeline — single-coord VRS (0 stations, not mappable)

All mountpoints in sourcetable share one coordinate — VRS filter drops them all.
Coverage requires NRTK polygons (deferred). These networks exist and work for
rovers; they just cannot be shown as individual station pins.

| id | name | host:port | declared stations | single coord |
|---|---|---|---|---|
| `asg_eupos` | ASG-EUPOS | `system.asgeupos.pl:2101` | 130+ | 52.0, 21.0 (Warsaw) |
| `flepos` | FLEPOS | `flepos.vlaanderen.be:2101` | 45 | single point (Flanders centroid) |
| `latpos` | LatPos | `latpos.lgia.gov.lv:5001` | 27 | single point; **port 5001** |
| `ksa_cors` | KSA-CORS | `ksacors.geoportal.sa:2101` | 209 | single point; register ksacors.geoportal.sa |
| `sapos_BE` | SAPOS Berlin | `sapos-be-ntrip.de:2101` | — | 52.48, 13.3 |
| `sapos_BB` | SAPOS Brandenburg | `sapos-bb-ntrip.de:2101` | — | 52.23, 13.05 |
| `sapos_BW` | SAPOS Baden-Württemberg | `sapos-bw-ntrip.de:2101` | — | 49.0, 8.4 |
| `sapos_BY` | SAPOS Bayern | `sapos-by-ntrip.de:2101` | — | 49.0, 11.5; €20/yr non-agri flat rate |
| `sapos_SH_HH` | SAPOS Schleswig-Holstein+Hamburg | `sapos.geonord.de:2101` | — | 54.18, 9.82 |
| `sapos_NI` | SAPOS Niedersachsen+Bremen | `sapos-ni-ntrip.de:2101` | — | 52.41, 9.8 |
| `sapos_NW` | SAPOS Nordrhein-Westfalen | `sapos-nw-ntrip.de:2101` | — | single point |
| `sapos_MV` | SAPOS Mecklenburg-Vorpommern | `sapos-mv-ntrip.de:2101` | — | single point |
| `sapos_LSA` | SAPOS Sachsen-Anhalt | `sapos-lsa-ntrip.de:2101` | — | single point |
| `sapos_TH` | SAPOS Thüringen | `sapos-th-ntrip.de:2101` | — | 51.01, 11.03 |

---

## In pipeline — zero-coord VRS (0 stations, not mappable)

Sourcetable reports 0/0 for all mountpoints. Dropped by coordinate filter.

| id | name | host:port | notes |
|---|---|---|---|
| `cropos` | CROPOS | `gnss.cropos.hr:2101` | HR; 35 stations; free since Apr 2022; register dgu@dgu.hr or cropos.hr |

---

## In pipeline — connectivity failures (0 stations)

Fetch times out; no cached sourcetable to fall back to.

| id | name | host:port | notes |
|---|---|---|---|
| `walcors` | WALCORS | `gnss.wallonie.be:2101` | BE Wallonia; 23 stations VRS; free for positioning; intermittently unreachable |
| `estpos` | ESTPOS | `gnss-rtk.maaamet.ee:8083` | EE; 40 stations VRS; free until Aug 2026; port 8083; times out from GitHub Actions |

---

## In pipeline — new / under test

| id | name | host:port | notes |
|---|---|---|---|
| `sapos_SN` | SAPOS Sachsen (GeoSN) | `ntrip.sachsen.de:2101` | DE; newly confirmed endpoint; station count TBD |
| `geodnet_usa` | GEODNET USA | `rtk.geodnet.com:2101` | Paid ($40/mo); testing whether sourcetable is public without auth |
| `geodnet_eu` | GEODNET Europe | `eu.geodnet.com:2101` | Paid; testing sourcetable accessibility |
| `geodnet_aus` | GEODNET Australia | `aus.geodnet.com:2101` | Paid; testing sourcetable accessibility |
| `geodnet_sa` | GEODNET S. America | `sa.geodnet.com:2101` | Paid; testing sourcetable accessibility |

---

## Candidates — not yet in pipeline

| name | host:port | notes |
|---|---|---|
| Thailand DOL LandGNSS | unknown | TH; confirmed free government service; register dol-rtknetwork.com; host:port not yet found |
| LitPOS | unknown | LT; confirmed free (EUPOS member); register geoportal.lt/web/litpos-en; host:port not publicly listed |
| ReNEP (DGT) | sent post-registration | PT; 47 stations; register renep.dgterritorio.gov.pt; host withheld until approved |
| GPSBru / AGN | `agn.ngi.be` | BE; single station (Brussels/Uccle); ~30 km radius only; register agn.ngi.be |

---

## Paid / drop

**Affordable (under $200/yr cutoff — mention in UI as paid alternatives):**
HEPOS GR `uranus.gr:2101` €160/yr ≈ $174 · ROMPOS RO €169/yr ≈ $183

**Over $200/yr cutoff:**
SIGNAL SI €200/yr ≈ $215 (also €0.12/min pay-per-use) ·
SWEPOS RTK SE ~9,000 SEK/yr ≈ $850 (free DGNSS tier sub-metre only) ·
swipos CH CHF 1,500/yr ≈ $1,650 ·
CPOS NO NOK 8,000/yr ≈ $740 ·
SiReNT SG SGD 107/mo ≈ $950/yr ·
SoI-CORS IN ₹5,000/mo (free only for government/academic) ·
GNSSnet.hu HU (commercial; pricing not public) ·
TUSAGA-Aktif TR `212.156.70.42:2101` 146 stations (pricing not public) ·
VNGEONET VN (fees since Sep 2024 per Circular 47/2024/TT-BTC; pricing not public) ·
e-GNSS TW · MyRTKnet MY · PAGeNet PH (pricing not public)

**Structural drop (access restricted regardless of price):**
SKPOS SK (public-sector only) ·
CZEPOS CZ (ČÚZK Decree 31/1995) ·
NETPOS/Kadaster NL (Kadaster/Rijkswaterstaat internal use only)

---

## Sources

rtk2go.com · centipede-rtk.org · asgeupos.pl · flepos.vlaanderen.be · gnss.wallonie.be ·
gim-international.com (FLEPOS 3.0) · renep.dgterritorio.gov.pt · frednet.crs.ogs.it ·
geodaf.mt.asi.it · uranus.gr · zentrale-stelle-sapos.de · cropos.hr · earthscope.org ·
ibge.gov.br · auscors.ga.gov.au · linz.govt.nz · skpos.gku.sk · gu-signal.si ·
czepos.cuzk.gov.cz · maanmittauslaitos.fi · rompos.ro · github.com/mvarga1989 ·
ardusimple.com · natt.is · dol-rtknetwork.com · geoportal.lt · sachsen.de (GeoSN) ·
geodnet.com · gnssdata.or.kr
