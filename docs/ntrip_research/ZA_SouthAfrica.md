# South Africa [ZA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (re-verification of 2026-05-06 baseline; new sourcetable probe) | USD/ZAR rate: 1 USD = 16.589 ZAR

## Status: ACTIVE — TrigNet (free government network); sourcetable retrieved live 2026-05-12

---

## Service 1: TrigNet (CONFIRMED ACTIVE)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | **Yes** |
| **landing_url** | `https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network` — operator-owned (CD:NGI under DALRRD) TrigNet description page. States the R 0.00 free-of-charge policy. Alternative: `http://www.trignet.co.za/` (the operator-owned portal/Spider home). |
| **access_url** | Skip — landing_url describes the registration path; no operator-owned non-form access doc identified beyond the portal welcome. `http://www.trignet.co.za/RegisterAccount.aspx` is the bare registration form, not a service description page. |
| **host:port** | `trignet.co.za:2101` — direct TCP/sourcetable probe 2026-05-12 returned SOURCETABLE 200 OK, server `NTRIP Trimble Ntrip Caster 5.2`, Content-Length 11487 |
| **Caster software** | Trimble Ntrip Caster 5.2 (observed 2026-05-12 — upgraded from older Trimble Pivot platform; mountpoint entries still tagged "Trimble Pivot Platform" as the back-end CORS engine) |
| **num_stations** | ~83 STR entries in 2026-05-12 sourcetable, covering single-base RTCM 3.4 mounts (e.g. `Pret-SB` at -25.73, 28.28) and three Network RTK clusters (`RTKNetWCape`, plus Gauteng/KZN equivalents) |
| **vrs** | Yes — Network RTK (VRS-equivalent) in Gauteng, Western Cape, KZN clusters; single-base RTK elsewhere; DGPS countrywide |
| **tariff** | **R 0.00 (free)** — all NGI products and services are free of charge per official NGI policy. No VAT on zero-price government service. USD equivalent: $0.00. Date observed: perennial policy, confirmed 2024–2026. Source: https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network |
| **hobbyist_eligibility** | **Yes** — no surveying licence required; registration is open self-service at trignet.co.za/RegisterAccount.aspx; forum posts confirm individual/developer registrations |
| **legal_residency_required** | Unclear — no stated residency restriction, but no confirmed non-resident registrations found |
| **registration** | http://www.trignet.co.za/RegisterAccount.aspx |
| **last_confirmed_alive** | 2026-05-12 — direct TCP probe of `trignet.co.za:2101` returned SOURCETABLE 200 OK with ~83 mountpoints, Content-Length 11487, Date header `Tue, 12 May 2026 22:00:44 UTC`; HEAD probe of `http://www.trignet.co.za/` HTTP 200 on 2026-05-13 |

### TrigNet Details

**Operator:** Chief Directorate: National Geo-spatial Information (CD:NGI), Dept. of Agriculture, Land Reform and Rural Development (DALRRD)
**Portal:** http://www.trignet.co.za | Register: http://www.trignet.co.za/RegisterAccount.aspx
**Authentication:** Username + password (Basic Auth, Base64) — obtained after registration
**Example mountpoint:** `Ctwn-SB` (Cape Town single-base)
**Protocol:** NTRIP v1/v2 — requires proper NTRIP client (RTKLIB, Lefebure, u-blox); standard HTTP libraries fail

### Service Tiers

| Tier | Accuracy | Coverage |
|------|----------|----------|
| DGPS | ~0.35 m | Countrywide |
| Single-base RTK | ~0.05 m | Within 30–40 km of each station |
| Network RTK (VRS) | ~0.03 m | Gauteng, Western Cape, KwaZulu-Natal clusters |

---

## Service 2: HxGN SmartNet South Africa (UNCONFIRMED)

| Field | Value |
|---|---|
| **Status** | Unconfirmed — Leica Geosystems has ZA commercial presence; SmartNet coverage map returned 403 Forbidden; no ZA-specific mountpoints publicly listed |
| **host:port** | Not publicly disclosed |
| **tariff** | Not published (US plans cited as "upwards of $5,000/year"; ZAR pricing not found) |
| **hobbyist_eligibility** | Unclear |
| **legal_residency_required** | Unclear |

---

## Service 3: RTK2GO Community Caster (informational)

- **host:port:** `rtk2go.com:2101` | Free
- 2026-05-13 sourcetable scan: one ZAF entry — `LouwNPP` (Paulpietersburg, KZN/MP border, -27.34, 30.90), RTCM 3.3 MSM, NMEA filter requires a real mount. Quality/uptime not guaranteed.

## Service 4: Centipede-RTK (informational)

- **host:port:** `caster.centipede.fr:2101` | Free
- 2026-05-13 sourcetable scan: one ZAF entry — `PIER` (-32.431, 25.743, Eastern Cape, near Pearston), u-blox ZED-F9P, RTCM3 GPS+GLO+GAL+BDS. Single hobbyist node; not a national network.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **TrigNet RINEX download** — same free service; daily/hourly RINEX files from all TrigNet stations | http://www.trignet.co.za/ | **Free** (same NGI policy — R 0.00) |

## Negative Findings

- **Trimble VRS Now**: No South Africa coverage confirmed.
- **Topcon Topnet Live**: No ZA coverage confirmed.
- No private commercial RTK NTRIP network with published tariff and confirmed endpoint found beyond TrigNet.

## Sources
- https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network
- https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-south-africa/
- https://www.b4x.com/android/forum/threads/ntrip-mount-points.163904/ (Nov 2024 live connection)
- https://hxgnsmartnet.com/coverage-map
- https://ntrip-list.com/africa/
- x-rates.com (ZAR/USD 2026-05-06)
- Direct TCP sourcetable probe `trignet.co.za:2101` 2026-05-12 — SOURCETABLE 200 OK, Trimble Ntrip Caster 5.2, ~83 STR entries (Content-Length 11487)
- Project sourcetables `data/rtk2go.sourcetable` and `data/centipede.sourcetable` 2026-05-13 — LouwNPP (rtk2go) and PIER (Centipede) tagged ZAF
