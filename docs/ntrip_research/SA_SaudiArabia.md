# Saudi Arabia [SA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — KSA-CORS (free government network, 209 stations, VRS); endpoint reachability from non-SA IPs UNCONFIRMED

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (free, self-registration) — reachability from outside Saudi Arabia / GCC unconfirmed |
| **Network name** | KSA-CORS (Kingdom of Saudi Arabia Continuously Operating Reference Station Network) |
| **Operator** | GEOSA — General Authority for Survey and Geospatial Information (formerly GASGI / GCS) |
| **host:port — current** | `ksacors.geoportal.sa:2101` (active portal domain as of 2026-05-06) |
| **host:port — legacy** | `ksacors.gcs.gov.sa:2101` (old domain; login page still resolves but domain authority migrated to GEOSA/geoportal.sa) |
| **host:port — obsolete** | `KSACORS.gcs.gov.sa` / `ksacors.geosa.gov.sa` — NXDOMAIN / redirected as of 2026-04 |
| **tariff** | **Free** — subscription is free and automatically renewed. Source: FAQ at gasgi.gov.sa / geosa.gov.sa (confirmed 2026-05-06). No VAT, no fee schedule. |
| **VRS** | Yes — KSA-GRF17 datum, VRS (Virtual Reference Station) method; GPS+GLO+GAL+BDS |
| **hobbyist_eligibility** | **Yes** — registration open to any user; no licensed-surveyor requirement documented. Self-service online registration at `ksacors.geoportal.sa` or by downloading and emailing the registration form to info@geosa.gov.sa. |
| **legal_residency_required** | **Unclear** — no explicit residency restriction in published documentation; registration form requests personal/organisational details but no nationality gate has been confirmed or denied from external sources. |
| **last_confirmed_alive** | `ksacors.geoportal.sa` portal page confirmed HTTP 200 on 2026-05-06; NTRIP sourcetable on port 2101 timed out from a non-SA external IP on 2026-05-06 (consistent with CI failure noted in networks.md). Endpoint may be IP-restricted to Saudi/GCC addresses or may have connectivity issues. |

---

## Service Details

### KSA-CORS — Network Overview

**Operator:** GEOSA (General Authority for Survey and Geospatial Information) — previously operated under GCS (General Commission for Survey) and GASGI.
**Portal:** https://ksacors.geoportal.sa/ (primary, 2026)
**Legacy portal:** https://ksacors.gcs.gov.sa/ (login page still accessible; underlying NTRIP caster domain status unclear)
**Registration:** Online at `ksacors.geoportal.sa/RegisterAccount.aspx` — OR — download form from site, sign, scan, email to info@geosa.gov.sa
**National platform service listing:** https://my.gov.sa/en/services/294222

### Station Count and Coverage

| Attribute | Value |
|-----------|-------|
| Physical CORS stations | 209 declared (KSA-wide, high-density national grid) |
| Coverage area | All of Saudi Arabia (~2.15 million km²) |
| Datum | KSA-GRF17 (Saudi national spatial reference system, SANSRS) |
| Signals | GPS + GLONASS + Galileo + BeiDou (quad-constellation) |
| Corrections | VRS (Virtual Reference Station) — single-coordinate rover input; RTCM streamed back |
| Mountpoints visible externally | 0 (VRS-only; single-coord model returns no physical station list) |

### Access Method (per v2.1 Getting Started Guide)

1. Register at `ksacors.geoportal.sa` (online form or email)
2. Receive username + password from GEOSA/KSA-CORS team
3. Configure GNSS rover: NtripCaster = `ksacors.geoportal.sa`, Port = `2101`
4. Send NMEA GGA sentence (rover position) to receive VRS corrections

Receivers must support VRS / NTRIP to connect. Standard NTRIP v1/v2 clients (RTKLIB, Lefebure, u-blox AssistNow, SurvCE, Field Genius) are compatible.

### Endpoint Reachability Issue

`ksacors.geoportal.sa:2101` has been timing out in the project's CI pipeline since at least 2026-04. The portal website (HTTPS) is reachable from external IPs. The NTRIP port (TCP 2101) does not respond to external probes. This is consistent with two possible explanations:

1. **IP geo-restriction:** The caster firewall only accepts connections from Saudi or GCC IP ranges.
2. **Domain / port migration:** GEOSA migrated from `gcs.gov.sa` → `geosa.gov.sa` → `geoportal.sa`; the NTRIP daemon may not yet be fully propagated to the new domain's port 2101 configuration.

The v2.1 guide (fetched from `ksacors.geoportal.sa`) still references port 2101 as the active NtripCaster port. Verification from a Saudi/GCC IP is required to confirm current operability.

### Operator Contact

| Contact type | Value |
|---|---|
| Registration email | info@geosa.gov.sa |
| Legacy registration email | info@gcs.gov.sa |
| GEOSA website | https://www.geosa.gov.sa/en/products/geodesy/pages/ksa-cors.aspx |
| GASGI FAQ (archived) | https://gasgi.gov.sa/En/Products/Geodesy/FAQ/Pages/FAQAboutKSA-CORS.aspx |

---

## Commercial Alternatives

No independent commercial NTRIP provider with confirmed Saudi Arabia coverage has been identified. The ArduSimple Saudi Arabia RTK page notes KSA-CORS as the primary (and only documented) option; Galileo HAS is mentioned as a free global fallback for ~40 cm accuracy without connectivity.

Global commercial networks (GEODNET, ONOCOY, PointOne, HxGN SmartNet) do not list Saudi Arabia in their coverage maps.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **KSA-CORS RINEX data download** — static RINEX from 209 stations; available via GEOSA portal after registration | https://ksacors.geoportal.sa/ | Free (same registration) |
| **EarthScope / IGS** — select Saudi IGS stations (e.g., ARSH, JFNG) contribute to IGS; download via EarthScope | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

---

## Context Notes

- **GEOSA brand evolution:** The network was originally GCS → GASGI → now GEOSA (General Authority for Survey and Geospatial Information, established by Royal Decree). The geoportal.sa domain is the current authoritative domain as of 2026.
- **SANSRS v2.0 (Dec 2022):** Saudi Arabia published the Saudi Arabia National Spatial Reference System v2.0 implementation guidelines, standardising KSA-GRF17 as the national datum. KSA-CORS is the primary realisation mechanism.
- **Hobbyist practical path:** Register by email (info@geosa.gov.sa); wait for credentials; test `ksacors.geoportal.sa:2101` from inside the country. Galileo HAS (free, global, ~40 cm, no connectivity needed) is the recommended fallback for users unable to access KSA-CORS from outside KSA.
- **No rtk2go/Centipede presence:** Zero SA mountpoints on rtk2go or Centipede.

---

## Negative Findings

- `ksacors.geoportal.sa:2101` — connection timeout from external IP (2026-05-06)
- `KSACORS.gcs.gov.sa` — NXDOMAIN as of 2026-04
- rtk2go monitor: zero SA mountpoints
- Centipede: zero SA nodes
- GEODNET, ONOCOY, PointOne, HxGN SmartNet: no Saudi Arabia coverage confirmed

---

## Sources Consulted
- GEOSA KSA-CORS product page: https://www.geosa.gov.sa/en/products/geodesy/pages/ksa-cors.aspx
- KSA-CORS portal (ksacors.geoportal.sa): https://ksacors.geoportal.sa/
- KSA-CORS Getting Started v2.1 (PDF): https://ksacors.geoportal.sa/WelcomePage/Getting%20Started%20with%20KSA-CORS%20Network_v.2.1.pdf
- KSA-CORS Getting Started v1.0 (geoportal.sa): https://www.geoportal.sa/pdf/Getting_Started_with_KSA-CORS_Network_v1.0.pdf
- How to Register v1.0 (PDF): https://www.geoportal.sa/pdf/How_to_Register_to_KSA-CORS_Network_v.1.0.pdf
- FAQ about KSA-CORS (GASGI/GEOSA): https://gasgi.gov.sa/En/Products/Geodesy/FAQ/Pages/FAQAboutKSA-CORS.aspx
- KSA-CORS national platform service listing: https://my.gov.sa/en/services/294222
- Saudipedia KSA-CORS article: https://saudipedia.com/en/article/4075/government-and-politics/communication-and-information-technology/saudi-arabia-continuously-operating-reference-station-ksa-cors-network
- SANSRS v2.0 implementation guidelines (PDF, Dec 2022): https://www.geoportal.sa/pdf/SANSRS_Implementation_Guidelines_V_2_0.pdf
- KSA-CORS and unification of CORS networks in KSA (EGU/IAG-Comm4 2022 abstract): https://meetingorganizer.copernicus.org/iag-comm4-2022/iag-comm4-2022-33.html
- Evaluation of KSACORS for hydrographic surveys (Taylor & Francis, 2020): https://www.tandfonline.com/doi/full/10.1080/19475705.2020.1799081
- ArduSimple Saudi Arabia RTK/NTRIP page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-saudi-arabia/
- ntrip-list.com (Middle East / Asia): https://ntrip-list.com/
- curl probe of `ksacors.geoportal.sa:2101` — connection timeout from external IP, 2026-05-06
