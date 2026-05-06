# South Africa [ZA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 | USD/ZAR rate: 1 USD = 16.589 ZAR

## Status: ACTIVE — TrigNet (free government network)

---

## Service 1: TrigNet (CONFIRMED ACTIVE)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | **Yes** |
| **host:port** | `trignet.co.za:2101` |
| **tariff** | **R 0.00 (free)** — all NGI products and services are free of charge per official NGI policy. No VAT on zero-price government service. USD equivalent: $0.00. Date observed: perennial policy, confirmed 2024–2025. Source: https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network |
| **hobbyist_eligibility** | **Yes** — no surveying licence required; registration is open self-service at trignet.co.za/RegisterAccount.aspx; forum posts confirm individual/developer registrations |
| **legal_residency_required** | Unclear — no stated residency restriction, but no confirmed non-resident registrations found |
| **last_confirmed_alive** | Nov 2024 (live NTRIP connection attempt confirmed in B4X forum); web index Feb 2026; @TrigNet_RSA X/Twitter reported "fully operational" 2024–2025 |

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
- Individual SA base stations may appear intermittently — not a national network; quality/uptime not guaranteed.

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
