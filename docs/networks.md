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

## Keep / add

| id | name | country | type | access | ntrip_host:port | signup_url | notes |
|---|---|---|---|---|---|---|---|
| `rtk2go` | RTK2GO | global | single-base | free | `rtk2go.com:2101` |  | ~800 volunteer bases; rovers connect with any email + password `none`. |
| `centipede` | CentipedeRTK | FR (+30) | single-base | free | `caster.centipede.fr:2101` |  | ~860 bases; dense in metro FR; NEAR pseudo-mountpoint selects nearest. |
| `asg-eupos` | ASG-EUPOS | PL | nrtk | registration | `system.asgeupos.pl:2101`; `:8080`/`:8086` for VRS | https://system.asgeupos.pl/ | Free since Oct 2022; VRS/MAC via NAWGIS/KODGIS; admin approval required. |
| `flepos` | FLEPOS 3.0 | BE (Flanders) | nrtk | registration | `flepos.vlaanderen.be:2101` | https://flepos.vlaanderen.be/ | Free; VRS mountpoints `FLEPOSVRS31GR`, `FLEPOSVRS32GREC`; 45 stations. |
| `walcors` | WALCORS | BE (Wallonia) | nrtk | category | `gnss.wallonie.be:2101` | https://gnss.wallonie.be/walcors/acces-au-reseau.html | Free for guidance/ag; surveyors submit written form; 23 stations; all BE since 2017. |
| `gpsbru` | GPSBru / AGN | BE (Brussels) | single-base | registration | _unconfirmed_ | https://agn.ngi.be/ | Free-with-reg likely; caster host not in public English docs — verify. |
| `renep` | ReNEP (DGT) | PT | single-base | registration | _not public_ | https://renep.dgterritorio.gov.pt/node/add/registo | Caster host sent after approval; contact renep@dgterritorio.pt. |
| `frednet` | FReDNet (OGS) | IT (FVG/Veneto) | nrtk | free | `gnsscaster.regione.fvg.it:8080` |  | No registration; 16-station network; VRS + single-base; north-east IT only. |
| `geodaf-asi` | GeoDAF / ASI EUREF | IT | single-base | registration | `euref-ip.asi.it:2101` | http://geodaf.mt.asi.it/gps_caster_access.php | Raw EUREF observations, not computed RTK; 5-connection cap — borderline, probably drop. |
| `uranus` | URANUS | GR / CY | nrtk | registration | _unconfirmed_ | https://www.uranus.gr/ | May have merged into commercial TopNet Live — verify before including. |
| `sapos` | SAPOS | DE | nrtk | registration | `sapos-ntrip.de:2101` (central ZSS) | https://zentrale-stelle-sapos.de/en/fees-registration/ | Free in most Länder (NRW, HH, SH, BE, TH, BW; BY ag only); some still charge; Galileo+BeiDou since Mar 2024. |
| `cropos` | CROPOS | HR | nrtk | registration | `gnss.cropos.hr:2101` (likely) | https://gnss.cropos.hr/ | Free since Apr 2022 (NN 39/2022); DPS + VPPS VRS ~2 cm; verify current reg fee. |
| `earthscope` | EarthScope NOTA | global (US) | single-base | registration | `ntrip.earthscope.org:2101` | https://www.earthscope.org/data/gnss-realtime/ | Raw RTCM 3.3 + BINEX, not computed corrections; free for non-commercial; ~1000 stations Americas. Borderline. |
| `ibge-rbmc` | RBMC-IP (IBGE) | BR | single-base | registration | `170.84.40.52:2101` | https://www.gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip | Free; 150 CORS; RTCM 3.2 MSM; single-base only. |
| `auscors` | AUSCORS (Geoscience AU) | AU | single-base | registration | `ntrip.data.gnss.ga.gov.au:2101` | https://gnss.ga.gov.au/registration | Free; single-base + SSR/PPP; TLS required; AU-wide. |
| `positionz` | PositioNZ-RT (LINZ) | NZ | single-base | registration | _unconfirmed_ | https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-real-time-service | Free with LINZ account; recommend ≤15 km baseline; contact positionz@linz.govt.nz. |

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
