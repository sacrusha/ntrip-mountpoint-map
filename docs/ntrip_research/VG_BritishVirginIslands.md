# British Virgin Islands [VG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: No national caster — EarthScope COCONet CN03 confirmed live in pipeline

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS stream in VG territory** | Yes — EarthScope NOTA (former COCONet) CN03_RTCM3P3, Tortola area; `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | **Yes** (noncommercial tier — no surveying licence required, individual account accepted) |
| **legal_residency_required** | **No** — no nationality or residency restriction in NULA |
| **last_confirmed_alive** | CN03_RTCM3P3 present in project's live EarthScope sourcetable (stations.json, 2026-05-06); EarthScope portal confirmed reachable; NULA dated v. 2025-05-30 |

---

## EarthScope NOTA — COCONet CN03, British Virgin Islands

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) |
| **Mountpoint** | `CN03_RTCM3P3` |
| **Location** | 18.49°N, −64.40°W — Tortola area, British Virgin Islands |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (GPS + GLONASS + BDS + Galileo + SBAS + QZSS), dual-frequency; single-base reference, NOT a VRS/Network-RTK service |
| **Tariff — noncommercial** | **Free (USD $0.00)** — account + annual NULA acceptance required. Date observed: 2026-05-06. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **Tariff — commercial** | **USD $1,000 per seat per year** (EarthScope is US 501(c)(3) nonprofit; no VAT). Min 5 seats for direct billing. Date observed: 2026-05-06. Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |

**Coverage note**: CN03 is on Tortola (the main island of the BVI group). Single-base RTK is reliable within ~20–30 km of the antenna. Anegada (60 km N) and more distant Grenadine-adjacent islands would be at the outer limit or beyond reliable RTK range.

**Legacy platform note**: The old UNAVCO caster (`rtgpsout.unavco.org`) was retired 2025-07-29. All COCONet/NOTA streams now served exclusively from `ntrip.earthscope.org`.

---

## National Surveying Authority

The **Land and Survey Department** (`bvi.gov.vg/departments/land-and-survey-department`) maintains the National Geodetic Framework for the British Virgin Islands. No NTRIP caster, CORS endpoint, real-time RTK correction service, or public announcement of a planned government GNSS correction service was found as of 2026-05-06.

As a UK Overseas Territory, the BVI does not participate in OS Net (Ordnance Survey's GB-only CORS network). No FCDO geospatial aid programme for BVI providing NTRIP was found.

---

## Most Recent Project Announcement

No dedicated BVI national CORS/NTRIP project announcement was found. The only identified real-time GNSS resource is the legacy COCONet (now EarthScope NOTA) CN03 station installed by UNAVCO/NSF for Caribbean geophysics monitoring.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive** — COCONet CN03 RINEX archive; same platform as real-time stream | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

---

## Sources Consulted
- EarthScope GNSS real-time data: https://www.earthscope.org/data/gnss-realtime/
- EarthScope commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- EarthScope NOTA: https://www.earthscope.org/nota/
- EarthScope platform transition announcement: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- BVI Land and Survey Department: https://www.bvi.gov.vg/departments/land-and-survey-department
- Project stations.json sourcetable — CN03_RTCM3P3 (VGB) confirmed present 2026-05-06
- RTK2go / Centipede sourcetables — no VG stations found
- NTRIP-list.com — no VG entry found
