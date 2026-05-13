# Grenada [GD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry) | XCD/USD: fixed peg 1 USD = 2.70 XCD

## Status: No national caster — EarthScope scientific stream available on dependency island

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS stream in Grenada territory** | Yes — EarthScope COCONet CN46, Carriacou (`ntrip.earthscope.org:2101`) |
| **hobbyist_eligibility** | **Yes** (noncommercial tier — no surveying licence required, individual account accepted) |
| **legal_residency_required** | **No** — no nationality or residency restriction in NULA |
| **last_confirmed_alive** | 2026-05-12 — `ntrip.earthscope.org:2101` SOURCETABLE 200 OK (curl probe); CN46_RTCM3P3 mountpoint present, station country code GRD, lat/lon 12.49/-61.43, SEAT_REQUIRED |

---

## EarthScope COCONet CN46 — Carriacou, Grenada

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (also port 2105 BINEX, 2108 PPP) |
| **Station** | CN46 — Mount Pleasant, Carriacou (Grenada dependency, ~35 km north of main island) |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT a VRS/Network-RTK service) |
| **Tariff — noncommercial** | **Free (USD $0.00 / XCD $0.00)** — account + annual NULA acceptance required. Date observed: 2026-05-12. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **Tariff — commercial** | **USD $1,000 / XCD $2,700 per seat per year** (no VAT — EarthScope is US 501(c)(3) nonprofit). Min 5 seats for direct billing. Date observed: 2026-05-12. Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |

**Practical caveat**: CN46 is on Carriacou, ~35–75 km from Grenada's main island — at the outer edge or beyond single-base RTK reliable range (~20–30 km for cm accuracy). Users on the main island would likely need a local base station.

**Note on legacy platform**: Old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

---

## Most Recent National Project Announcement

None found for a dedicated Grenada CORS/NTRIP service.

- **2019–2022**: World Bank / Fugro full-island LiDAR/aerial survey → national GIS/digital twin. No CORS component.
  URL: https://www.esri.com/about/newsroom/blog/grenada-digital-twin-climate-change
- **2022**: World Bank OECS Data for Decision Making Project (Grenada, Saint Lucia, Saint Vincent). No GNSS CORS component.
  URL: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/

No OECS or CARICOM geodetic CORS/NTRIP project for Grenada identified.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — COCONet CN46 (Carriacou) RINEX archive; same platform as real-time stream | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

## Sources Consulted
- https://www.earthscope.org/data/gnss-realtime/
- https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- COCONet site-info (coconet.unavco.org)
- EarthScope NOTA (network.igs.org)
- RTK2GO, IGS network, SIRGAS station list
- NTRIP-list.com, corsstations.com
- ArduSimple country directory
- World Bank OECS project
- curl probe of `ntrip.earthscope.org:2101` 2026-05-12 — SOURCETABLE 200 OK; CN46_RTCM3P3 entry verified (country=GRD, 12.49/-61.43, SEAT_REQUIRED)
- WebSearch 2026-05-12 ("Grenada CORS GNSS RTK NTRIP service Caribbean 2025 2026") — no new national CORS announcement
