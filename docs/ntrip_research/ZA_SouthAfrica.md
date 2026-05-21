# South Africa [ZA] — NTRIP RTK Caster Research

## Status
ACTIVE — TrigNet (CD:NGI, free). FIG 2026 paper (Parker, NGI) confirms "over 70" CORS + 3 NRTK/VRS clusters + TrigNet 2030 modernisation strategy.

## Caster: TrigNet (CD:NGI)

| Field | Value |
|---|---|
| landing_url | https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network (operator-owned, states R 0.00 policy) |
| access_url | http://www.trignet.co.za/ (portal home; registration at `/RegisterAccount.aspx`) |
| host:port | `trignet.co.za:2101` — SOURCETABLE 200 OK 2026-05-16, server `NTRIP Trimble Ntrip Caster 5.2`, Content-Length 11783 |
| tariff | **R 0.00 (free)** — all NGI products/services free per public mandate; no VAT on zero-price gov service; USD equivalent $0.00. Perennial policy, re-confirmed 2026-05-16. Source: landing_url. |
| num_stations | **~70 physical CORS** (FIG 2026 paper: "over 70 operational CORS stations" as of Oct 2025). Sourcetable carries 77 STR rows = 73 single-base `*-SB` rows (a few stations expose 2 streams: `Plbb-SB` + `Plbb-SB_GPSGLOonly`; `Tdou-SB` + `TDOU-SB_GPSGLOonly`; `Pret-SB` + `PRET_JAXA`; `Ctwn-SB` + `CTWN_JAXA`) + 3 Network RTK aliases (`RTKNetWCape`, `RTKNetGauteng`, `RTKNetKZN`) + 1 countrywide DGPS alias (`DGPS-RSA`). Pipeline filter retains 73 SB rows (drops the 3 RTKNet + DGPS-RSA as solution=1 routing aliases). |
| vrs | yes — Network RTK clusters published as `RTKNetWCape`, `RTKNetGauteng`, `RTKNetKZN` (RTCM 3.1, 1004/1012/1005/1007/1033, GPS+GLONASS, nmea=1 i.e. rover GGA required). Single-base `*-SB` mounts elsewhere; DGPS via `DGPS-RSA` countrywide. |
| hobbyist_eligibility | yes — no surveying-licence requirement; open self-service registration; community forum posts confirm individual/developer signups |
| legal_residency_required | ? — no published residency restriction; no confirmed non-resident registration |
| last_confirmed_alive | 2026-05-21 — `http://www.trignet.co.za/` ECONNREFUSED from sandbox (2nd day; 2026-05-16 sandbox TCP probe succeeded with 77 STR, Trimble Caster 5.2). FIG 2026 paper (NGI-authored, May 2026) independently states "over 70 operational CORS stations" as of Oct 2025. Project cache `data/trignet.sourcetable` + `stations_by_country.py ZAF` confirm 73 active stations. |
| datum_epoch | **ITRF2005 @ epoch 2010.02** — operator-owned: NGI page states "co-ordinates of TrigNet stations ... are based on ITRF 2005 (epoch 2010.02)" at https://ngi.dalrrd.gov.za/index.php/technical-information/geodesy-and-gps/world-geodetic-system-1984-wgs84-and-the-international-terrestrial-reference-frame-itrf. |

### Datum tension (user-actionable)

- TrigNet active GNSS frame = **ITRF2005 @ 2010.02**.
- ZA national passive control + legacy basemaps = **Hartebeesthoek94** (ITRF91 @ 1994.0, official since 1999-01-01).
- Cross-frame transform needed if working from legacy ZA maps / cadastre vs TrigNet stream output. NGI publishes transformation params at https://ngi.dalrrd.gov.za/index.php/technical-information/geodesy-and-gps/datum-s-and-coordinate-systems.

### TrigNet details

- **Mandate:** Section 3A, Land Survey Act 8 of 1997 (per FIG 2026 paper).
- **TrigNet 2030 strategy:** NGI modernisation roadmap toward "resilient, user-centric, interoperable CORS infrastructure integrated with regional and global geodetic frameworks" (FIG 2026 paper). No published tariff change; free-policy reiterated.
- **Operator:** Chief Directorate: National Geo-spatial Information (CD:NGI), Dept. of Agriculture, Land Reform and Rural Development (DALRRD).
- **Auth:** Basic (username + password, Base64) post-registration.
- **Caster software:** Trimble Ntrip Caster 5.2 (front-end); back-end Trimble Pivot Platform per STR records.
- **Protocol:** NTRIP v1/v2; needs real NTRIP client (RTKLIB, Lefebure, u-blox) — plain HTTP libraries fail.
- **Service tiers:**

| Tier | Accuracy | Coverage |
|---|---|---|
| DGPS | ~0.35 m | countrywide (`DGPS-RSA`) |
| Single-base RTK | ~0.05 m | within 30–40 km of each `*-SB` station |
| Network RTK (VRS) | ~0.03 m | Gauteng (`RTKNetGauteng`), Western Cape (`RTKNetWCape`), KwaZulu-Natal (`RTKNetKZN`) clusters only |

## Volunteer / Global Supplements (informational; ingested-globals)

- **rtk2go:** 1 ZAF — `LouwNPP` (Paulpietersburg, KZN/MP border, -27.34/30.90), RTCM 3.3 MSM.
- **Centipede:** 1 ZAF — `PIER` (-32.43/25.74, Eastern Cape near Pearston), u-blox ZED-F9P, RTCM3 GPS+GLO+GAL+BDS.
- **IGS-IP (BKG):** 8 ZAF stations (CTWN, HARB, HRAG×2, HRAO, RBAY, SUT1, SUTM) — single-base raw 1 Hz.
- `stations_by_country.py ZAF` 2026-05-21: 73 trignet, 1 rtk2go, 1 centipede, 8 igs_ip, 2 mirai, 1 auscors = 86 total source-records.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| TrigNet RINEX (daily/hourly all stations) | http://www.trignet.co.za/ | free (R 0.00; same NGI public mandate) |

## Negative Findings

- HxGN SmartNet ZA: coverage map endpoint returns 403; no ZA-specific signup, host:port, or tariff found 2026-05-16 → skipped per spec (no operator info page + no semi-official third-party page with usable detail).
- Trimble VRS Now: no ZA coverage confirmed.
- Topcon Topnet Live: no ZA coverage confirmed.
- No commercial private NTRIP network with published ZAR tariff + endpoint beyond TrigNet.

## Sources
- TrigNet operator landing: https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network
- TrigNet datum citation (operator-owned): https://ngi.dalrrd.gov.za/index.php/technical-information/geodesy-and-gps/world-geodetic-system-1984-wgs84-and-the-international-terrestrial-reference-frame-itrf
- NGI datums + coordinate systems page (incl. Hartebeesthoek94 / ITRF transforms): https://ngi.dalrrd.gov.za/index.php/technical-information/geodesy-and-gps/datum-s-and-coordinate-systems
- TrigNet portal: http://www.trignet.co.za/
- FIG 2026 paper (Parker, NGI) "Status and Future of TrigNet" — https://fig.net/resources/proceedings/fig_proceedings/fig2026/papers/ts01h/TS01H_parker_14083_abs.pdf (FIG Congress 2026, Cape Town, states "over 70 operational CORS" Oct 2025, 3 NRTK/VRS clusters, TrigNet 2030, ITRF alignment)
- Wonnacott, "The Implementation of the Hartebeesthoek94 Co-ordinate System in South Africa" — https://www.fig.net/organisation/comm/5/library/reports/wonnacott.pdf (Hartebeesthoek94 = ITRF91 @ 1994.0)
- ardusimple ZA: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-south-africa/
- b4x.com NTRIP forum thread (live TrigNet connections, Nov 2024): https://www.b4x.com/android/forum/threads/ntrip-mount-points.163904/
- ntrip-list.com Africa: https://ntrip-list.com/africa/
