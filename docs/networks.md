# Free RTK NTRIP networks — research refinement

_Produced by Sonnet research agent, 2026-04-19. Starting reference for
future ingestion work — see `scripts/fetch_stations.py` `SOURCES` for
the casters currently fetched. Confidence notes and "drop" rationale are
preserved so a later session doesn't re-investigate already-settled
classifications._

## Confidence

**High:** RTK2GO, CentipedeRTK, ASG-EUPOS, FLEPOS, WALCORS, SAPOS, CROPOS,
FReDNet (IT), IBGE RBMC-IP, AUSCORS. Also confirmed paid (drop): SIGNAL SI,
SKPOS SK (both public-sector-only), CZEPOS CZ, ROMPOS RO, HEPOS GR, SWEPOS,
swipos CH, TUSAGA-Aktif TR.

**Moderate:** ReNEP PT (free+reg confirmed, caster host not in English docs),
PositioNZ NZ (same), URANUS GR/CY (may have migrated to commercial TopNet Live),
GeoDAF/ASI IT (actually EUREF raw, borderline out of scope).

**Low:** GPSBru BE Brussels (endpoint undocumented).

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
| `centipede` | CentipedeRTK | `crtk.net:2101` | Username: `centipede` · Password: `centipede` · Mountpoint: `NEAR` auto-selects nearest | ~860 bases; dense in France; migrated from caster.centipede.fr 2025-03-18 |
| `frednet` | FReDNet (OGS) | `gnsscaster.regione.fvg.it:8080` | Sourcetable open (no auth). Stream: email `rete.gnss.marussi@regione.fvg.it` for free credentials | 16 stations, NE Italy + Slovenia/Austria border; VRS |
| `geortk` | GeoRTK (Geosense) | `geortk.jp:2101` | No authentication required | ~200 stations with valid coords; Japan only; RTCM 3.x MSM; free indefinitely |

### rtk2go — technical notes
- Runs **SNIP Pro** (use-snip.com). SNIP is paid software for self-hosters; rtk2go absorbs that cost, so users get it free.
- **NEAR** is a SNIP Pro feature (not available in SNIP Lite). The client connects to the mountpoint named `NEAR` and sends a NMEA `$GGA` sentence; the caster routes to the closest active base. Most rover setups send GGA automatically; some cheap NTRIP clients require it to be enabled manually.
- SNIP Pro allows up to 5 NEAR streams per instance; rtk2go has several regional NEAR variants (e.g. `NEAR_RTCM3` etc.) — check the live sourcetable for current names.
- Source: use-snip.com/near-mount-points/, use-snip.com/rtk2go/

### Centipede — technical notes
- **NEAR** pseudo-mountpoint is Centipede's own implementation (not SNIP). Routes to the nearest Centipede node based on connected rover GGA position.
- Migrated from `caster.centipede.fr:2101` → `crtk.net:2101` on 2025-03-18. Old host is dead.
- Source: forum.geocommuns.fr migration announcement

## Registration required — pipeline candidates

| id | name | host:port | how to register | notes |
|---|---|---|---|---|
| `asg-eupos` | ASG-EUPOS | `system.asgeupos.pl:2101` (`:8080`/`:8086` for VRS) | Web self-signup at system.asgeupos.pl — admin approval 1–2 working days | Free since Oct 2022; VRS/MAC; 130+ stations; PL |
| `flepos` | FLEPOS | `ntrip.flepos.be:2101` | Web self-signup at flepos.vlaanderen.be | 45 stations; VRS; BE Flanders |
| `walcors` | WALCORS | `gnss.wallonie.be:2101` | Email/web form at gnss.wallonie.be/walcors/inscription.html | 23 stations; VRS; free for survey/GIS; paid for ag auto-guidance; BE Wallonia |
| `ergnss` | ERGNSS (IGN) | `ergnss-ip.ign.es:2101` | Web self-signup at ergnss.ign.es/gnuserportal/ — immediate | ~120 stations; VRS; ES; CC-compatible, attribute IGN |
| `sapos` | SAPOS HEPS/EPS | per-Länder (central: `sapos-ntrip.de:2101`) | Per-state web forms at sapos.de | ~270 stations; VRS; 12/16 Länder free (BY ~€20/yr, RP paid); DE |
| `cropos` | CROPOS | `gnss.cropos.hr:2101` | Email dgu@dgu.hr or web form | 35 stations; VRS; free since Apr 2022; HR |
| `estpos` | ESTPOS | `gnss-rtk.maaamet.ee:8083` | Portal at geoportaal.maaamet.ee | 40 stations; VRS; free until Aug 2026; EE |
| `latpos` | LatPos | `latpos.lgia.gov.lv:2101` | SBC portal at latpos.lgia.gov.lv/SBC | 27 LV + border stations; VRS; free since 2018; LV |
| `spslux` | SPSLux | `stream.spslux.lu:5005` | SBC portal at spslux.lu/sbc/ | **Port 5005** (not 2101); full country VRS; LU open data |
| `trignet` | TrigNet | `trignet.co.za:2101` | Register at trignet.co.za | 55+ stations; VRS in 3 clusters + single-base; ZA |
| `ibge-rbmc` | RBMC-IP (IBGE) | `170.84.40.52:2101` | gov.br signup at gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip | 150 stations; single-base; BR |
| `ramsac` | RAMSAC-NTRIP | `ntrip.ign.gob.ar:2101` | Email ntrip@ign.gob.ar or portal ign.gob.ar | ~69 stations; single-base; 8-hr session cap; AR |
| `igac` | IGAC MAGNA-ECO | `sbc.igac.gov.co:2101` (VRS) / `:2102` (single) | Email/web at sbc.igac.gov.co | 233 stations; VRS; CO — first confirmed free VRS in LATAM |
| `ksa-cors` | KSA-CORS | `KSACORS.gcs.gov.sa:2101` | Email signed form to info@geosa.gov.sa | 209 stations; VRS; SA |
| `inacors` | InaCORS | `nrtk.big.go.id:2001` | Self-register at nrtk.big.go.id | **Port 2001**; 200+ stations; VRS; ID |
| `cors-korea` | CORS-KOREA | `www.gnssdata.or.kr:2101` | Register at ngii.go.kr (Korean-language portal) · Password: `gnss` (public) | ~90 stations; VRS+FKP; KR |
| `satref` | SatRef HK | `ntrip.geodetic.gov.hk:2101` | Email geodetic@landsd.gov.hk | 19 stations; VRS; mountpoint `VRS32G`; HK |
| `auscors` | AUSCORS | `ntrip.data.gnss.ga.gov.au:2101` | Web signup at gnss.ga.gov.au/registration | 700+ stations; single-base; TLS also on :443; CC BY 4.0; AU |
| `positionz` | PositioNZ-RT | `positionz-rt.linz.govt.nz:2101` | LINZ account + email positionz@linz.govt.nz | 100+ stations; single-base; CC BY 4.0 NZ; NZ |
| `earthscope` | EarthScope NOTA | `ntrip.earthscope.org:2101` | Annual non-commercial license at earthscope.org/data/gnss-realtime/ | ~1000 stations; raw RTCM 3.x obs; Americas; non-commercial only |
| `renep` | ReNEP (DGT) | host sent post-registration | Register at renep.dgterritorio.gov.pt/node/add/registo | 47 stations; host withheld until approved; PT |
| `gpsbru` | GPSBru / AGN | _unconfirmed_ (likely `ntrip.ngi.be:2101`) | Register at agn.ngi.be | Single station (Brussels/Uccle); operational status uncertain; BE |

## Paid / drop

SIGNAL (SI, €829/yr), SKPOS (SK, public-sector only), CZEPOS (CZ, ČÚZK Decree 31/1995),
ROMPOS (RO), HEPOS (GR, €160/3mo), SWEPOS (SE, ~12 000 SEK/yr), swipos (CH, CHF 1500/yr),
TUSAGA-Aktif (TR, education only), GNSSnet.hu (HU, appears commercial).

## Sources

rtk2go.com · centipede-rtk.org · asgeupos.pl · flepos.vlaanderen.be · gnss.wallonie.be ·
gim-international.com (FLEPOS 3.0) · renep.dgterritorio.gov.pt · frednet.crs.ogs.it ·
geodaf.mt.asi.it · uranus.gr · zentrale-stelle-sapos.de · cropos.hr · earthscope.org ·
ibge.gov.br · auscors.ga.gov.au · linz.govt.nz · skpos.gku.sk · gu-signal.si ·
czepos.cuzk.gov.cz · maanmittauslaitos.fi · rompos.ro · github.com/mvarga1989 · ardusimple.com
