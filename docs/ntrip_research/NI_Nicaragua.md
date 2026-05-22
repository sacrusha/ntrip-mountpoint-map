# Nicaragua [NI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (3 NIC streams confirmed in local pipeline: 2 EarthScope NOTA + 1 IGS-IP rebroadcast of MANA. MANA STR row directly captured from BKG IGS-IP sourcetable today)

## Status: No domestic public NTRIP caster — INETER CORS is RINEX-only. EarthScope NOTA exposes two NIC real-time NTRIP streams (CNG2, JAPO) usable with an EarthScope NULA seat. The IGS station MANA (Managua, INETER campus) is also rebroadcast on BKG's IGS-IP caster (free, BKG account registration).

| Field | Value |
|---|---|
| Domestic NTRIP RTK caster | No |
| Foreign-operated NTRIP mountpoints physically in NI | 3 — EarthScope NOTA: `CNG2_RTCM3P3` (12.50°N -86.70°W, Chinandega area), `JAPO_RTCM3P3` (11.53°N -85.68°W, Juigalpa/Cocibolca corridor). BKG IGS-IP: `MANA00NIC0` (12.15°N -86.25°W, INETER campus Managua) |
| Government CORS network | Yes — INETER (Dirección General de Geodesia y Cartografía); RINEX post-processing only |

## Service A — EarthScope NOTA (CNG2 + JAPO)

| Field | Value |
|---|---|
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://data.earthscope.org/ (NULA acceptance + seat assignment) |
| host:port | `ntrip.earthscope.org:2101` (TCP) / `:443` (TLS); legacy `rtgpsout.unavco.org:2101` retired 2025-07-29 |
| Mountpoints | `CNG2_RTCM3P3` (Trimble NETR9, RTCM 3.3 MSM7, GPS+GLO+BDS+GAL+SBAS+QZS); `JAPO_RTCM3P3` (same hw+format). Both single-base, nmea=0 |
| num_stations | 2 NIC-tagged streams per `py scripts/stations_by_country.py NIC` 2026-05-22 |
| vrs | No — single-base raw RTCM 3 |
| tariff | Non-commercial: Free (NULA acceptance); Commercial: USD 1,000/seat/yr (5-seat min, 2-week 5-seat trial). EarthScope is US 501(c)(3) — no VAT |
| hobbyist_eligibility | Yes (non-commercial via NULA) |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-22 — present in `data/earthscope.sourcetable` cache; EarthScope NOTA realtime page reachable |
| datum_epoch | **ITRF2014, NOTA epoch 2026-03-30** — declared at https://www.earthscope.org/data/gnss-realtime/ ("For NOTA stations, the epoch date is 2026-03-30") |

CNG2 covers Chinandega/León (~64 km from Managua). JAPO covers the central Cocibolca/Río San Juan corridor. Managua city centre (12.13°N -86.25°W) sits between them; CNG2 is the closer base, but MANA (below) sits on top of Managua and is the practical pick for the capital.

## Service B — BKG IGS-IP (MANA Managua rebroadcast)

| Field | Value |
|---|---|
| landing_url | https://igs.bkg.bund.de/ntrip/ |
| access_url | https://igs.bkg.bund.de/ntrip/register (free BKG account) |
| host:port | `www.igs-ip.net:2101` |
| Mountpoint | `MANA00NIC0` — RTCM 3.1, messages 1004(1)/1005(30)/1007(30)/1012(1)/1019/1020/1029/1033(30), GPS+GLO, receiver SEPT POLARX5, auth Basic. Source: `rtgpsout.earthscope.org:2101/MANA_RTCM3` (BKG rebroadcasts the EarthScope feed) |
| num_stations | 1 (MANA Managua, INETER campus) |
| vrs | No — single-base 1 Hz raw RTCM 3.1 |
| tariff | Free (BKG NTRIP registration) |
| hobbyist_eligibility | Yes |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-22 — direct sourcetable curl returns STR row for MANA00NIC0 (`STR;MANA00NIC0;Managua;RTCM 3.1;...`) |
| datum_epoch | omitted — BKG IGS-IP does not publish per-mountpoint datum; primer rule: do not infer from caster identity. IGS station metadata at https://network.igs.org/MANA00NIC lists receiver/antenna only |

Effective single-base RTK reach within ~30 km of Managua centre — usable for the capital and immediate surroundings. RTCM 3.1 message set (no MSM) so older RTCM 3.0/3.1 rovers fine; MSM-only rovers must accept legacy 1004 GPS L1+L2.

## INETER government CORS — RINEX only

**Instituto Nicaragüense de Estudios Territoriales (INETER)**, via the Dirección General de Geodesia y Cartografía, maintains Nicaragua's national geodetic infrastructure.

| Field | Value |
|---|---|
| landing_url | https://www.ineter.gob.ni/geodesiaycartografia.html |
| access_url | https://consultacf.ineter.gob.ni/ (Catastro Físico portal) — CORS data request: https://consultacf.ineter.gob.ni/Servicio/ConsultaDatosCORS |
| Service | RINEX request for post-processing. Contact `soporteCatastro@ineter.gob.ni` / +505 2249-2763. No documented real-time NTRIP product |
| host:port | None published |
| num_stations | Not declared on indexed INETER pages |
| datum_epoch | omitted — no citable declaration on indexed `ineter.gob.ni` geodesy or catastro pages |
| last_confirmed_alive | 2026-05-22 — `consultacf.ineter.gob.ni` accessible per search results |

INETER's IDE portal (`mapserveride.ineter.gob.ni/IDE-BCN/`) provides cartographic services but no NTRIP caster or mountpoint catalogue. INETER's seismic-monitoring network (`webserver2.ineter.gob.ni`) uses GPS-disciplined timing — not positioning CORS.

## Volunteer & open coverage

| Source | Status |
|---|---|
| rtk2go | 0 NI stations 2026-05-22 |
| Centipede | 0 NI nodes 2026-05-22 |
| GEODNET / ONOCOY / PointOne | No NI coverage on public-facing product pages |
| Commercial NTRIP resellers | Not listed for NI on NTRIP-list.com, ArduSimple country directory, Point One, GEODNET, RTKdata |

## Most Recent Project Announcement

No announcement of a planned Nicaragua public NTRIP caster as of 2026-05-22. INETER geodetic pages continue to describe post-processing workflows only. No SIRGAS-RT stream listed for NI.

**Regional context**: El Salvador (Survey3G commercial) and Costa Rica (IGN-CR free national caster) have national NTRIP services. Honduras, Guatemala and Nicaragua remain RINEX-only at the national level. EarthScope NOTA's regional Trimble NETR9 streams are the practical free real-time option across HND/NIC/CRI/SLV/PAN for non-commercial users.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| INETER Catastro Físico (GNSS/RINEX request) | https://consultacf.ineter.gob.ni/ | Free (request basis) |
| INETER IDE/BCN (cartographic base viewer) | https://mapserveride.ineter.gob.ni/IDE-BCN/ | Free |
| EarthScope NIC RINEX archive (CNG2, JAPO, etc.) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |

## Sources

- INETER Geodesia y Cartografía: https://www.ineter.gob.ni/geodesiaycartografia.html
- INETER Catastro Físico portal: https://consultacf.ineter.gob.ni/
- INETER CORS data request: https://consultacf.ineter.gob.ni/Servicio/ConsultaDatosCORS
- INETER main site: https://www.ineter.gob.ni/
- INETER IDE Base Cartográfica Nacional: https://mapserveride.ineter.gob.ni/IDE-BCN/
- EarthScope NOTA realtime: https://www.earthscope.org/data/gnss-realtime/ (datum ITRF2014, NOTA epoch 2026-03-30)
- EarthScope licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- BKG IGS-IP sourcetable (curl 2026-05-22 captured MANA00NIC0 RTCM 3.1 STR): `www.igs-ip.net:2101`
- BKG NTRIP service / registration: https://igs.bkg.bund.de/ntrip/ · https://igs.bkg.bund.de/ntrip/register
- IGS station MANA: https://network.igs.org/MANA00NIC
- ArduSimple Nicaragua (no national RTK): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-nicaragua/
- Local pipeline `py scripts/stations_by_country.py NIC` 2026-05-22: 2 EarthScope (CNG2, JAPO) + 1 IGS-IP (MANA00NIC0) = 3 MPs; 0 rtk2go, 0 Centipede
