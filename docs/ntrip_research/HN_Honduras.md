# Honduras [HN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (`cors.ip.gob.hn` HTTP 200 again; portal HTML last-modified 2022-05-26 — stable but no policy/endpoint change since then. 4 EarthScope HND-tagged real-time NTRIP streams confirmed in local pipeline 2026-05-22 via direct sourcetable inspection of `data/earthscope.sourcetable`)

## Status: PARTIAL — no Honduras-operated public NTRIP caster, but 4 EarthScope NOTA real-time RTK streams exist on HND soil (free non-commercial via NULA). Government IP/DGCG CORS is post-processing RINEX only (FTP).

| Field | Value |
|---|---|
| Active NTRIP RTK caster (HN-operated) | No |
| Active NTRIP RTK mountpoint physically in HN | Yes — 4 HND-tagged EarthScope NOTA streams on `ntrip.earthscope.org:2101`: `CN18_RTCM3P3` (17.41 N -83.94, Swan Islands/Bay Islands area), `CN21_RTCM3P3` (13.40 N -87.43, Gulf of Fonseca south), `ROA0_RTCM3P3` (16.32 N -86.53, Roatán north coast), `TEG2_RTCM3P3` (14.09 N -87.21, Tegucigalpa). All carry STR records with carrier=2, nmea=0, solution=0 — full real-time RTCM 3.3 MSM7, accessible under NULA seat |
| Operator (government CORS) | Instituto de la Propiedad (IP) · Dirección General de Cartografía y Geografía (DGCG); also marketed as "IGN Honduras" (ign.hn) — same institution |
| landing_url — IP/DGCG CORS | `https://cors.ip.gob.hn/` (operator-owned portal — self-signed cert, TLS verification fails on common Windows stacks; HTTP works) |
| access_url — IP/DGCG CORS | Skip — landing_url already conveys the FTP archive workflow; no separate registration page |
| host:port | None published. RINEX archive only via `ftp://ceiba.ip.gob.hn` (the portal instructs users to enable FTP in Chrome `chrome://flags/#enable-ftp` or Edge `edge://flags/#enable-ftp` before clicking "Descargar Archivos") |
| Service type | RINEX post-processing via FTP archive; no real-time NTRIP product |
| num_stations | Unverified — operator portal HTML carries no per-station metadata. Prior research lists 5 (Tegucigalpa, San Pedro Sula, Juticalpa, Siguatepeque, La Ceiba) but this is not directly confirmable from cors.ip.gob.hn pages reachable 2026-05-22 |
| vrs | n/a — no caster |
| tariff | Free RINEX via FTP (no account evidenced in current portal HTML; FTP openly reachable per portal instructions). No NTRIP tariff (no NTRIP product) |
| hobbyist_eligibility | n/a — no real-time service |
| legal_residency_required | n/a |
| last_confirmed_alive | 2026-05-22 — `http://cors.ip.gob.hn/` HTTP 200 (Microsoft-IIS/10.0, Content-Length 35,349; Last-Modified 2022-05-26 — portal HTML unchanged in ~4 years, suggesting stable but stagnant operation) |
| datum_epoch | omitted — no citable declaration. Honduras adopted WGS 84 at legislative level (cartographic conventions ~2000) but neither cors.ip.gob.hn nor any IP/DGCG page declares the frame+epoch of the CORS coordinates. Legislative reference ≠ operator-portal frame declaration per primer |

## Service B — EarthScope NOTA (free real-time, 4 HND streams)

| Field | Value |
|---|---|
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://data.earthscope.org/ (EarthScope account + NULA acceptance + seat assignment) |
| host:port | `ntrip.earthscope.org:2101` (TCP) / `:443` (TLS); legacy `rtgpsout.unavco.org:2101` retired 2025-07-29 |
| Mountpoints | `CN18_RTCM3P3` (Septentrio POLARX5), `CN21_RTCM3P3` (POLARX5), `ROA0_RTCM3P3` (POLARX5), `TEG2_RTCM3P3` (Trimble NETR9). All RTCM 3.3 with MSM7 (1077/1087/1097/1107/1117) + 1005/1007/1013/1029/1033, GPS+GLO+BDS+GAL+SBAS+QZS |
| num_stations | 4 HND-tagged streams (confirmed in `data/earthscope.sourcetable` 2026-05-22) |
| vrs | No — single-base raw RTCM 3.3 |
| tariff | Non-commercial: Free (NULA acceptance); Commercial: USD 1,000/seat/yr (5-seat min, 2-week 5-seat trial). EarthScope is US 501(c)(3) — no VAT |
| hobbyist_eligibility | Yes (non-commercial via NULA) |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-22 — STR rows present in `data/earthscope.sourcetable`; EarthScope NOTA realtime page reachable |
| datum_epoch | **ITRF2014, NOTA epoch 2026-03-30** — declared at https://www.earthscope.org/data/gnss-realtime/ ("For NOTA stations, the epoch date is 2026-03-30") |

**Coverage notes**: TEG2 sits in the capital Tegucigalpa — the primary practical pick for central HN. CN21 covers the southern Pacific coast (Gulf of Fonseca). ROA0 sits on Roatán in the Bay Islands and CN18 is on the Swan Islands ~310 km offshore — both geographically isolated from mainland users, useful only locally. Together with EarthScope NOTA's neighbouring streams in SV (SSIA) and NIC (CNG2/JAPO), this gives the Central American hobbyist a coherent free real-time RTK belt.

## Volunteer & Open Coverage

| Source | Status |
|---|---|
| rtk2go | 0 HN stations 2026-05-22 |
| Centipede | 0 HN nodes 2026-05-22 |
| Commercial NTRIP | No NTRIP-list.com / ArduSimple / Point One / GEODNET / RTKdata operator publishes HN coverage |

## Most Recent Project Announcement

No announcement of a planned Honduras-operated NTRIP / real-time RTK service. The IP/DGCG network has operated as a post-processing RINEX service since its establishment. No SIRGAS-RT stream operated by HN; the 4 EarthScope NOTA stations on HN soil are the only free real-time RTK feed.

**Regional context**: El Salvador (Survey3G commercial + SSIA scientific), Costa Rica (IGN-CR free national caster), Nicaragua (EarthScope NOTA + IGS-IP rebroadcast), Honduras (EarthScope NOTA on HND soil) and Panama (EarthScope NOTA + MIRAI rebroadcast) all have some form of real-time RTK access. Guatemala alone remains without any real-time path in 2026-05.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| IP/DGCG CORS — RINEX archive | https://cors.ip.gob.hn/ → `ftp://ceiba.ip.gob.hn` | Free; FTP must be enabled in browser flags |
| EarthScope NOTA RINEX (CN18, CN21, ROA0, TEG2) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |
| SIRGAS-CON RINEX | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |

## Sources

- IP/DGCG CORS portal: https://cors.ip.gob.hn/ (HTTP 200 2026-05-22, Last-Modified 2022-05-26)
- Instituto de la Propiedad: https://www.ip.gob.hn/
- IP Cartography services: https://www.ip.gob.hn/direcciones/cartografia-geografia/tramites-cartografia-y-geografia
- IP Cartography FAQ: https://www.ip.gob.hn/preguntas_frecuente_catastro
- EarthScope NOTA realtime (datum ITRF2014 / NOTA epoch 2026-03-30): https://www.earthscope.org/data/gnss-realtime/
- EarthScope licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- NTRIP-list.com North America: https://ntrip-list.com/north-america/
- ArduSimple country directory: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- Local pipeline `py scripts/stations_by_country.py HND` 2026-05-22: 4 earthscope realtime streams (CN18, CN21, ROA0, TEG2), 0 rtk2go, 0 Centipede
