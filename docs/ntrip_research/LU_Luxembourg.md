# Luxembourg [LU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (station list research added; prior: 2026-05-17)

## Status: YES — free government NTRIP caster (SPSLux) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (SPSLux — free) |
| **landing_url — SPSLux** | `https://act.public.lu/fr/gps-reseaux/spslux1.html` — operator-owned (Administration du Cadastre et de la Topographie / ACT) SPSLux service overview page (FR). Describes the network, free policy, accuracy. |
| **access_url — SPSLux** | `https://act.public.lu/fr/gps-reseaux/spslux1/1spsluxaccess.html` — operator-owned access page describing the cadastre-portal subscription workflow. `https://www.spslux.lu/SBC/Account/Register` is the bare SBC registration form, not a service description page. |
| **host:port — SPSLux** | `stream.spslux.lu:5005` (IP: 185.106.24.68) |
| **VRS** | Yes — iMAX and VRS network correction types offered; both provide equivalent cm-level accuracy. 18 mountpoints exposed (VRS_G/GR/GRE/GREC, IMAX_G/GR/GRE/GREC variants in RTCM 3 / CMR / MSM5, plus NEAREST_* single-base and DGNSS_IMAX_RTCM2 / DGPS_IMAX_RTCM2) |
| **tariff** | Free — all SPSLux real-time and post-processing services are provided at no cost in line with Luxembourg's open-data policy |
| **hobbyist_eligibility** | yes — no professional licensing requirement stated; open registration |
| **legal_residency_required** | unclear — not explicitly required; open-data policy implies broad access; no restriction stated in public documentation |
| **last_confirmed_alive** | 2026-05-12 — `curl --http0.9 http://stream.spslux.lu:5005/` returned `SOURCETABLE 200 OK` (Server: `GNSS Spider 7.10.1.168/1.0`, Content-Length 1957). Sourcetable lists VRS_G(R)(E)(C)_RTCM3 / MSM5, IMAX_G(R)(E)(C)_RTCM3 / MSM5, NEAREST_G(R)(E)(C)_RTCM3 / MSM5, plus DGNSS streams; all rows tagged country `L` and `SPSLux`. 2026-05-17 sandbox re-probe HTTP 000 (egress blocked); operator datum + access URLs reachable via search snippet |
| **datum_epoch** | **ETRS89 (ETRF2000 @ 2020.82)** + ITRS. Operator: `https://act.public.lu/fr/gps-reseaux/spslux1/spsluxgeodeticdatum.html` |

## Context Notes

- **SPSLux** (Satellite Positioning System Luxembourg): National GNSS positioning network operated by the Administration du Cadastre et de la Topographie (ACT), Geodetic Department. Provides Network RTK (iMAX and VRS correction types) and DGNSS corrections in real time.
- **Infrastructure**: 13 continuously operating reference stations (some on international territory managed by partner networks: 3 SAPOS Germany, 2 WALCORS Belgium, 1 ORPHEON France, 1 SAT-INFO France; 6 Luxembourg-owned). Station names partially known from a 2011 document: Beyren, Machtum, Tarchamps among LU stations. Provides horizontal accuracy of ~2–3 cm and vertical ~3–5 cm under good conditions.
- **Physical station coordinates**: A coordinate list PDF (ITRS + ETRS89 + LUREF coords, ~491 KB) and location map PDF are published at `https://act.public.lu/fr/gps-reseaux/spslux1/spslux_sites_coord.html` — page returned HTTP 403 from this sandbox (2026-05-21); confirmed reachable and referenced in multiple search results. Direct PDF link on that page for download.
- **Correction types / mountpoints**: iMAX (network corrections optimised for Leica equipment) and VRS (standard; compatible with all major receiver brands); DGNSS stream also available. Full mountpoint list downloadable from the ACT portal. Signals from GPS, GLONASS, Galileo, BeiDou processed.
- **Access**: Registration required via the ACT cadastre portal shop on first login (subscribe to "SPSLUX (N)RTK" package — zero cost). Mobile data (GSM/4G) required for real-time access.
- **Reference system / datum_epoch**: SPSLux station coordinates managed in **ETRS89 (ETRF2000 @ 2020.82)** + ITRS; national LUREF realised through SPSLux. Source (operator): `https://act.public.lu/fr/gps-reseaux/spslux1/spsluxgeodeticdatum.html`. Datum re-computed by Uni.lu / ACT in 2014, 2019, 2020 tracking ITRF2008/2014/2020 + ETRF2008/2014/2020 evolution.
- **Operator contact**: spslux@act.etat.lu

## Cross-Border Coverage (Centipede in adjacent FR/BE/DE)

While SPSLux is the natural choice inside Luxembourg, the Centipede-RTK network is dense in the neighbouring French and Belgian regions and covers the whole of LU territory with overlapping baselines:
- 21 Centipede stations within 100 km of Luxembourg City as of 2026-05-12 (`py scripts/stations_by_radius.py 49.6 6.1 100`)
- Closest cross-border: `GEGE` (49.455, 6.192, FRA, 17.4 km), `KUBA` (49.657, 5.866, BEL, 18.0 km), `EMC3` (49.407, 5.745, FRA, 33.4 km)
- Centipede is fully free and open (caster.centipede.fr:2101); useful as a backup or for users who prefer the volunteer-network ethos over an account at ACT
- rtk2go: 0 LU entries; AUS/BEL/FRA bases nearby

## Post-Processing (RINEX) Fallback

RINEX data available via the same ACT portal at no cost after registration. FTP access to archived observation files.

## Sources Consulted

- SPSLux station coordinates page (PDF linked, 403 from sandbox): https://act.public.lu/fr/gps-reseaux/spslux1/spslux_sites_coord.html (confirmed reachable per search results 2026-05-21; PDF ~491 KB contains ITRS + ETRS89 + LUREF coords for all 13 network stations)
- SPSLux service overview: https://act.public.lu/fr/gps-reseaux/spslux1.html
- SPSLux geodetic datum (operator-declared ETRS89 ETRF2000 @ 2020.82): https://act.public.lu/fr/gps-reseaux/spslux1/spsluxgeodeticdatum.html
- Uni.lu SPSLux-LUREF coordinate-monitoring project (2014/2019/2020 ITRF/ETRF transitions): https://www.uni.lu/fstm-en/research-projects/spslux-luref/
- SPSLux NTRIP/Caster page: https://act.public.lu/fr/gps-reseaux/spslux1/ntripcasterclient.html
- SPSLux access page: https://act.public.lu/fr/gps-reseaux/spslux1/1spsluxaccess.html
- SPSLux mountpoints page: https://act.public.lu/fr/gps-reseaux/spslux1/spsluxmountpoints.html
- ArduSimple Luxembourg RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-luxembourg/
- Live caster probe (2026-05-12): `curl --http0.9 http://stream.spslux.lu:5005/` → SOURCETABLE 200 OK; 18 STR rows; Server `GNSS Spider 7.10.1.168/1.0`
- Local pipeline check (2026-05-12): `py scripts/stations_by_radius.py 49.6 6.1 100` → 21 Centipede stations within 100 km (all FRA/BEL); no native LU pins in rtk2go/centipede/earthscope
