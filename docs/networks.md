# Free RTK NTRIP networks — research refinement

_Produced by Sonnet research agent, 2026-04-19. Starting reference for
future ingestion work — see `scripts/fetch_stations.py` `SOURCES` for
the casters currently fetched. Confidence notes and "drop" rationale are
preserved so a later session doesn't re-investigate already-settled
classifications._

## Confidence

**High:** RTK2GO, CentipedeRTK, ASG-EUPOS, FLEPOS, WALCORS, SAPOS (most
Länder free; BY free for agriculture only, ~€20/yr for general use; RP
confirmed free), CROPOS, FReDNet (IT), IBGE RBMC-IP, AUSCORS, PositioNZ NZ,
MIRAI JP (commercial + automated use confirmed). Also confirmed paid (drop):
SIGNAL SI, SKPOS SK (both public-sector-only), CZEPOS CZ, ROMPOS RO, HEPOS GR,
SWEPOS RTK, swipos CH, TUSAGA-Aktif TR, VNGEONET VN (fees since Sep 2024).

**Moderate:** ReNEP PT (free+reg confirmed; host withheld until post-registration),
CORS-KOREA KR (free confirmed; sourcetable public without auth; stream registration
portal Korean-only, national ID likely required — international utility limited),
GeoDAF/ASI IT (EUREF raw, borderline out of scope).

**Low:** IceCORS IS — resolved: confirmed free ("data is free of charge" — natt.is), endpoint `178.19.53.126:2101` (GNCASTER), VRS + single-base, registration via natt.is/is/landmaelingar/jardstodvakerfi.

## Drops from the starting list

| Network | Reason |
|---|---|
| NETPOS / Kadaster (NL) | Restricted to Kadaster/Rijkswaterstaat internal use. |
| EUREF-IP | Raw GNSS observations only; operators say "unsuitable for real-time kinematic positioning". |
| FINPOS RTK (FI) | RTK granted only for research with written justification. DGNSS is free but sub-metre — out of scope here. |

## In pipeline

| id | name | host:port | credentials | notes |
|---|---|---|---|---|
| `rtk2go` | RTK2GO | `rtk2go.com:2101` | Username: any email · Password: `none` · Mountpoint: `NEAR` auto-selects nearest (client must send NMEA GGA) | ~800 volunteer bases globally |
| `centipede` | CentipedeRTK | `crtk.net:2101` | Username: `centipede` (or `c`) · Password: `centipede` (or `c`) · Mountpoint: `NEAR` (requires NMEA GGA); use `NEAR4` on older equipment (John Deere etc.) | ~860 bases; dense in France; migrated from caster.centipede.fr 2025-03-18 |
| `frednet` | FReDNet (OGS) | `gnsscaster.regione.fvg.it:8080` | Sourcetable open (no auth). Stream: email `rete.gnss.marussi@regione.fvg.it` for free credentials | 16 stations, NE Italy + Slovenia/Austria border; VRS |
| `geortk` | GeoRTK (Geosense) | `geortk.jp:2101` | No authentication required | ~200 stations with valid coords; Japan only; RTCM 3.x MSM; free indefinitely |

### rtk2go — technical notes
- Runs **SNIP Pro** (use-snip.com). SNIP is paid software for self-hosters; rtk2go absorbs that cost, so users get it free.
- **NEAR** is a SNIP Pro feature (not available in SNIP Lite). The client connects to the mountpoint named `NEAR` and sends a NMEA `$GGA` sentence; the caster routes to the closest active base. Most rover setups send GGA automatically; some cheap NTRIP clients require it to be enabled manually.
- SNIP Pro allows up to 5 NEAR streams per instance; rtk2go has several regional NEAR variants (e.g. `NEAR_RTCM3` etc.) — check the live sourcetable for current names.
- Source: use-snip.com/near-mount-points/, use-snip.com/rtk2go/

### Centipede — technical notes
- Login accepts `c` or `centipede`; password likewise. Both work.
- **NEAR** requires client to send NMEA GGA (same as rtk2go). On older/proprietary equipment (John Deere, some legacy displays) use `NEAR4` instead.
- Migrated from `caster.centipede.fr:2101` → `crtk.net:2101` on 2025-03-18. Old host is dead.
- Source: centipede-rtk.org/the-centipede-rtk-network (official connection credentials page)

## Registration required — pipeline candidates

| id | name | host:port | how to register | notes |
|---|---|---|---|---|
| `asg-eupos` | ASG-EUPOS | `system.asgeupos.pl:2101` (`:8080`/`:8086` for VRS) | Web self-signup at system.asgeupos.pl — admin approval 1–2 working days | Free since Oct 2022; VRS/MAC; 130+ stations; PL |
| `flepos` | FLEPOS | `flepos.vlaanderen.be:2101` (was `ntrip.flepos.be` — dead 2026-04) | Web self-signup at flepos.vlaanderen.be | 45 stations; VRS; BE Flanders |
| `walcors` | WALCORS | `gnss.wallonie.be:2101` | Registration at gnss.wallonie.be (gnss@spw.wallonie.be) | 23 stations; VRS; free for positioning (survey, GIS, drones, hobbyist); "paid" restriction applies to commercial resellers of raw stream, not end-user positioning; BE Wallonia |
| `ergnss` | ERGNSS (IGN) | `ergnss-ip.ign.es:2101` | Web self-signup at ergnss.ign.es/gnuserportal/ — immediate | ~120 stations; VRS; ES; CC-compatible, attribute IGN |
| `sapos` | SAPOS HEPS/EPS | per-Länder (central: `sapos-ntrip.de:2101`) | Per-state web forms at sapos.de | ~270 stations; VRS; most Länder free; BY free for agriculture only (~€20/yr general); RP confirmed free; **already in pipeline** as 13 `sapos_*` casters; DE |
| `cropos` | CROPOS | `gnss.cropos.hr:2101` | Email dgu@dgu.hr or web form | 35 stations; VRS; free since Apr 2022 (Narodne novine 39/2022); **caster IP changed Nov 2023** (→ 195.29.198.194); hostname should resolve correctly; HR |
| `estpos` | ESTPOS | `gnss-rtk.maaamet.ee:8083` | Portal at geoportaal.maaamet.ee | 40 stations; VRS; free until Aug 2026; EE |
| `latpos` | LatPos | `latpos.lgia.gov.lv:5001` (port 5001, not 2101 — per Alberding caster directory) | SBC portal at latpos.lgia.gov.lv/SBC | 27 LV + border stations; VRS; free since 2018; LV |
| `spslux` | SPSLux | `stream.spslux.lu:5005` | SBC portal at spslux.lu/sbc/ | **Port 5005** (not 2101); full country VRS; LU open data |
| `trignet` | TrigNet | `trignet.co.za:2101` | Register at trignet.co.za | 55+ stations; VRS in 3 clusters + single-base; ZA |
| `ibge-rbmc` | RBMC-IP (IBGE) | `170.84.40.52:2101` | gov.br signup at gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip | 150 stations; single-base; BR |
| `ramsac` | RAMSAC-NTRIP | `ntrip.ign.gob.ar:2101` | Email ntrip@ign.gob.ar or portal ign.gob.ar | ~69 stations; single-base; 8-hr session cap; AR |
| `igac` | IGAC MAGNA-ECO | `sbc.igac.gov.co:2101` (VRS/network) / `:2102` (single-base) | Spider Business Center at redgeodesica-sbc.igac.gov.co/sbc; free after approval | 233 stations; VRS; first confirmed free VRS in LATAM; Law 1955/2019; CO |
| `ksa-cors` | KSA-CORS | `ksacors.geoportal.sa:2101` (migrated from dead `KSACORS.gcs.gov.sa` 2026-04) | Email signed form to info@geosa.gov.sa | 209 stations; VRS; SA |
| `inacors` | InaCORS | `nrtk.big.go.id:2001` | Self-register at nrtk.big.go.id | **Port 2001**; 200+ stations; VRS; ID |
| `cors-korea` | CORS-KOREA | `www.gnssdata.or.kr:2101` | Register at gnssdata.or.kr (Korean-language portal); login uses registered email as NTRIP username | ~90–100 stations; VRS+FKP; free; **Korean national ID may be required — verify international access before pipeline**; KR |
| `satref` | SatRef HK | `ntrip.geodetic.gov.hk:2101` | Email geodetic@landsd.gov.hk | 19 stations; VRS; mountpoint `VRS32G`; HK |
| `auscors` | AUSCORS | `ntrip.data.gnss.ga.gov.au:2101` | Web signup at gnss.ga.gov.au/registration | 700+ stations; single-base; TLS also on :443; CC BY 4.0; AU |
| `positionz` | PositioNZ-RT | `positionz-rt.linz.govt.nz:2101` | LINZ account + email positionz@linz.govt.nz | 37 CORS stations (NZ mainland + Chatham Is + Antarctica); single-base RTCM; CC BY 4.0 NZ; NZ |
| `earthscope` | EarthScope NOTA | `ntrip.earthscope.org:2101` (also `:2105` BINEX, `:2108` PPP) | Annual non-commercial NULA at earthscope.org/data/gnss-realtime/ | ~1000 stations; RTCM 3.3 MSM; Americas; non-commercial (commercial licensed per-seat); UNAVCO legacy platform fully retired 2025-07-29 |
| `mirai` | MIRAI (Go!GNSS) | `ntrip.go.gnss.go.jp:2101` | Registration at go.gnss.go.jp + NtripCaster authorization form | ~300+ stations incl. overseas partners; raw RTCM 3 obs; free incl. commercial + automated use ("peaceful purposes"); accounts expire after 365 days inactivity; JP |
| `renep` | ReNEP (DGT) | host sent post-registration | Register at renep.dgterritorio.gov.pt/node/add/registo | 47 stations; host withheld until approved; PT |
| `gpsbru` | GPSBru / AGN | `agn.ngi.be` | Register at agn.ngi.be | Single station (Brussels/Uccle); operational as of mid-2024; ~30 km radius only; BE |

## Paid / drop

**Affordable (under $200/yr cutoff):**
HEPOS (GR, €160/yr ≈ $174 — confirmed annual, not per-quarter),
ROMPOS (RO, ~€169/yr ≈ $183).

**Over cutoff:**
SIGNAL (SI, €200/yr ≈ $215 — pay-per-minute also available at €0.12/min; earlier €829/yr figure appears to be a higher tier or stale),
SWEPOS RTK (SE, ~9,000 SEK/yr ≈ $850; free DGNSS tier is sub-metre only),
swipos (CH, CHF 1,500/yr ≈ $1,650),
CPOS (NO, NOK 8,000/yr ≈ $740),
SiReNT (SG, SGD 107/mo ≈ $950/yr),
SoI-CORS (IN, ₹5,000/mo; paid for private users; free only for government/academic),
TUSAGA-Aktif (TR, `212.156.70.42:2101`, 146 stations; pricing not public),
GNSSnet.hu (HU, appears commercial; pricing not public),
VNGEONET (VN, fees since Sep 2024 per Circular 47/2024/TT-BTC; pricing not public),
e-GNSS (TW), MyRTKnet (MY), PAGeNet (PH) — pricing not public.

**Structural drop:**
SKPOS (SK, public-sector only), CZEPOS (CZ, ČÚZK Decree 31/1995),
NETPOS/Kadaster (NL, restricted to Kadaster/Rijkswaterstaat internal use).

**Drop — operational obstruction:** APN (IL, `mapigps.co.il`) — pervasive military GNSS spoofing
active continuously since Oct 2023 across Israel/Lebanon/Jordan/Sinai/Cyprus makes RTK unreliable
regardless of NTRIP access. Exclude from pipeline until spoofing ceases.

## Sources

rtk2go.com · centipede-rtk.org · asgeupos.pl · flepos.vlaanderen.be · gnss.wallonie.be ·
gim-international.com (FLEPOS 3.0) · renep.dgterritorio.gov.pt · frednet.crs.ogs.it ·
geodaf.mt.asi.it · uranus.gr · zentrale-stelle-sapos.de · cropos.hr · earthscope.org ·
ibge.gov.br · auscors.ga.gov.au · linz.govt.nz · skpos.gku.sk · gu-signal.si ·
czepos.cuzk.gov.cz · maanmittauslaitos.fi · rompos.ro · github.com/mvarga1989 · ardusimple.com
