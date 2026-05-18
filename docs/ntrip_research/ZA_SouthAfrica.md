# South Africa [ZA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verification of 2026-05-16 baseline) | USD/ZAR ref: 1 USD ≈ 16.589 ZAR (2026-05-06)

## Status: ACTIVE — TrigNet (CD:NGI, free). FIG 2026 paper (Parker, NGI) confirms "over 70" CORS + 3 NRTK/VRS clusters + TrigNet 2030 modernisation strategy.

> 2026-05-17 caveat: TCP probe `trignet.co.za:2101` timed out from sandbox (DNS resolves 196.15.132.2; HTTP 80 portal 200). 2026-05-16 probe successful with 77 STR; treat sandbox-side blockage as transient. FIG abstract independently states "over 70 operational CORS" as of Oct 2025.

---

## Caster 1: TrigNet (CD:NGI) — CONFIRMED ACTIVE

| Field | Value |
|---|---|
| landing_url | https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network (operator-owned, states R 0.00 policy) |
| access_url | http://www.trignet.co.za/ (portal home; registration at `/RegisterAccount.aspx`) |
| host:port | `trignet.co.za:2101` — SOURCETABLE 200 OK 2026-05-16, server `NTRIP Trimble Ntrip Caster 5.2`, Content-Length 11783 |
| tariff | **R 0.00 (free)** — all NGI products/services free per public mandate; no VAT on zero-price gov service; USD equivalent $0.00. Perennial policy, re-confirmed 2026-05-16. Source: landing_url. |
| num_stations | **77** STR entries in sourcetable 2026-05-16 (down from 83 on 2026-05-12). Mix: ~70 single-base `*-SB` mounts (e.g. `Pret-SB` -25.73/28.28, `Ctwn-SB` -33.95/18.46) + 3 Network RTK clusters (`RTKNetWCape`, `RTKNetGauteng`, `RTKNetKZN` equivalents) + a few legacy/DGPS mounts. Per-station country tag: ZAF for all. |
| vrs | yes — Network RTK clusters in Gauteng, Western Cape, KwaZulu-Natal; single-base RTK elsewhere; DGPS countrywide |
| hobbyist_eligibility | yes — no surveying-licence requirement; open self-service registration; community forum posts confirm individual/developer signups |
| legal_residency_required | ? — no published residency restriction; no confirmed non-resident registration |
| last_confirmed_alive | 2026-05-17 — `http://www.trignet.co.za/` HTTP 200; TCP `trignet.co.za:2101` timed out from sandbox (intermittent; 2026-05-16 probe succeeded with 77 STR, Trimble Caster 5.2). FIG 2026 paper (NGI-authored, May 2026) independently states "over 70 operational CORS stations" as of Oct 2025. |
| datum_epoch | **ITRF2005 @ epoch 2010.02** — cited operator-owned: NGI page states "co-ordinates of TrigNet stations ... are based on ITRF 2005 (epoch 2010.02)" at https://ngi.dalrrd.gov.za/index.php/technical-information/geodesy-and-gps/world-geodetic-system-1984-wgs84-and-the-international-terrestrial-reference-frame-itrf. Note: passive control framework = Hartebeesthoek94 (ITRF91 @ 1994.0); active GNSS framework = ITRF2005 @ 2010.02. |

### TrigNet Details

- **Mandate:** Section 3A, Land Survey Act 8 of 1997 (per FIG 2026 paper, NGI-authored).
- **TrigNet 2030 strategy:** NGI developing modernisation roadmap — "resilient, user-centric, interoperable CORS infrastructure integrated with regional and global geodetic frameworks" (FIG 2026 paper). No published tariff change; free-policy reiterated.
- **Operator:** Chief Directorate: National Geo-spatial Information (CD:NGI), Dept. of Agriculture, Land Reform and Rural Development (DALRRD)
- **Auth:** Basic (username + password, Base64) post-registration
- **Caster software:** Trimble Ntrip Caster 5.2 (front-end, observed 2026-05-12 + -16); back-end "Trimble Pivot Platform" tag still on STR records
- **Protocol:** NTRIP v1/v2; needs real NTRIP client (RTKLIB, Lefebure, u-blox) — plain HTTP libraries fail
- **Service tiers:**

| Tier | Accuracy | Coverage |
|---|---|---|
| DGPS | ~0.35 m | countrywide |
| Single-base RTK | ~0.05 m | within 30–40 km of each station |
| Network RTK (VRS) | ~0.03 m | Gauteng, Western Cape, KZN clusters only |

---

## Caster 2: HxGN SmartNet South Africa — UNCONFIRMED

| Field | Value |
|---|---|
| landing_url | https://hxgnsmartnet.com/coverage-map (403 Forbidden in probes) |
| access_url | — no ZA-specific signup page identified |
| host:port | not publicly disclosed |
| tariff | not published; US tier benchmark "upwards of $5,000/year"; ZAR pricing absent |
| num_stations | ? |
| vrs | ? |
| hobbyist_eligibility | ? — no free tier identified |
| legal_residency_required | ? |
| last_confirmed_alive | unconfirmed; Leica has ZA commercial presence but no ZA-specific MP list found 2026-05-16 |
| datum_epoch | omitted — no citable declaration |

Not a hobbyist option until pricing + endpoint disclosed.

---

## Volunteer / Global Supplements (informational; ingested-globals)

- **rtk2go (rtk2go.com:2101):** 1 ZAF — `LouwNPP` (Paulpietersburg, KZN/MP border, -27.34/30.90), RTCM 3.3 MSM (project sourcetable scan 2026-05-13).
- **Centipede (crtk.net:2101):** 1 ZAF — `PIER` (-32.43/25.74, Eastern Cape near Pearston), u-blox ZED-F9P, RTCM3 GPS+GLO+GAL+BDS.
- **IGS-IP (BKG):** 7 ZAF stations within 1500 km of Pretoria (HARB, HRAG, HRAO, HRAG (multi-MP), RBAY, SUT1, SUTM, CTWN) — single-base raw 1 Hz. Also carries HARB00ZAF0, SUTM00ZAF0, WIND00NAM0 (IGS observation streams reaching southern Africa); AUSCORS sourcetable re-exposes these as an IGS-partner pass-through artefact, but canonical attribution is IGS-IP.
- Verification: `py scripts/stations_by_radius.py -25.7 28.2 1500` 2026-05-16 = 53 stations on trignet alone + supplements.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| TrigNet RINEX (daily/hourly all stations) | http://www.trignet.co.za/ | free (R 0.00; same NGI public mandate) |

## Negative Findings

- Trimble VRS Now: no ZA coverage confirmed.
- Topcon Topnet Live: no ZA coverage confirmed.
- No commercial private NTRIP network with published ZAR tariff + endpoint beyond TrigNet.

## Sources
- TrigNet operator landing: https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network
- TrigNet datum citation (operator-owned): https://ngi.dalrrd.gov.za/index.php/technical-information/geodesy-and-gps/world-geodetic-system-1984-wgs84-and-the-international-terrestrial-reference-frame-itrf — "TrigNet ... based on ITRF 2005 (epoch 2010.02)"
- NGI datums + coordinate systems page: https://ngi.dalrrd.gov.za/index.php/technical-information/geodesy-and-gps/datum-s-and-coordinate-systems
- TrigNet portal: http://www.trignet.co.za/
- Direct TCP sourcetable probe `trignet.co.za:2101` 2026-05-16 — SOURCETABLE 200 OK, Trimble Caster 5.2, 77 STR entries, Content-Length 11783
- TCP probe 2026-05-17 — timed out from sandbox (DNS 196.15.132.2 ok; HTTP 80 portal returns 200); not a service outage
- FIG 2026 paper (Parker, NGI) "Status and Future of TrigNet" — https://fig.net/resources/proceedings/fig_proceedings/fig2026/papers/ts01h/TS01H_parker_14083_abs.pdf (presented FIG Congress 2026, Cape Town, 24-29 May 2026; states "over 70 operational CORS" Oct 2025, 3 NRTK/VRS clusters, TrigNet 2030 strategy, ITRF alignment)
- `py scripts/stations_by_radius.py -25.7 28.2 1500` 2026-05-16 — 53 trignet stations + rtk2go LouwNPP + centipede PIER + igs_ip ZA cluster
- ardusimple ZA: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-south-africa/ (also: docs/ardusimple/ZA_SouthAfrica.md)
- b4x.com NTRIP forum thread (Nov 2024 live TrigNet connections): https://www.b4x.com/android/forum/threads/ntrip-mount-points.163904/
- HxGN SmartNet (403): https://hxgnsmartnet.com/coverage-map
- ntrip-list.com Africa: https://ntrip-list.com/africa/
