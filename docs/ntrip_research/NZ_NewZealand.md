# New Zealand [NZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free government NTRIP caster (PositioNZ-RT, LINZ) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (PositioNZ-RT — free) |
| **host:port — PositioNZ-RT** | `positionz-rt.linz.govt.nz:2101` (IP: 161.65.59.99) |
| **VRS** | No — single-base only; streams raw RTCM from nearest physical CORS; recommended use within 15 km of the connected station |
| **tariff** | Free — registration required |
| **hobbyist_eligibility** | yes — no professional licensing or commercial restrictions stated; open registration |
| **legal_residency_required** | no — no residency restriction found in public documentation |
| **last_confirmed_alive** | `positionz-rt.linz.govt.nz:2101` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl verified) |

## Context Notes

- **PositioNZ-RT**: Operated by Toitū Te Whenua Land Information New Zealand (LINZ); data streaming managed by GeoNet. Free real-time NTRIP service providing 1 Hz GNSS data from the PositioNZ CORS network in NZGD2000 reference frame.
- **Infrastructure**: 37 continuously operating reference stations (CORS) throughout New Zealand (including Chatham Islands) and Antarctica (Scott Base). Signals from GPS, GLONASS, Galileo, BeiDou, QZSS.
- **Mountpoint naming convention**: `XXXX00NZL0` (e.g., WARK00NZL0 = Warkworth). Full mountpoint list available via GeoNet. RTCM 3.1 format.
- **Single-base limitation**: PositioNZ-RT streams raw observations, not VRS corrections. Users should connect to their nearest station and stay within 15 km. For longer baselines, accuracy degrades. No network solution / VRS product currently offered by LINZ.
- **AUSCORS**: The Australian CORS network (Geoscience Australia) extends to some NZ-adjacent stations and is accessible free of charge; useful as supplemental coverage.
- **Registration**: Account registration required at geodesy.linz.govt.nz; free.
- **Recent improvement**: BKG NtripCaster software deployment reduced PositioNZ-RT average stream latencies significantly (reported 50–90% reduction).
- **Operator contact**: Toitū Te Whenua LINZ geodetic team; positionz@linz.govt.nz

## Commercial / Paid Alternatives

- **Trimble CenterPoint VRS (Vantage NZ)**: VRS network RTK for NZ; paid; primarily targets agriculture and professional survey. Contact Vantage NZ (vantage-nz.com) for pricing.
- **HaloRTK**: NZ-based commercial NTRIP network; website (halortk.co.nz) had an expired SSL certificate on 2026-05-06 — service status uncertain.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **PositioNZ-PP** — online PPP post-processing service | https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-post-processing-service | Free |
| **PositioNZ GNSS Data** — raw RINEX download from all 37 CORS | https://data.govt.nz/catalogue-guide/showcase/positionz-gnss-data | Free |
| **GeoNet GNSS archive** — supplemental stations | https://www.geonet.org.nz/ | Free |

## Sources Consulted
- LINZ PositioNZ-RT page: https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-real-time-service
- LINZ PositioNZ-RT connection page: https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-real-time-service/connect-positionz-real-time-service
- LINZ PositioNZ overview: https://www.linz.govt.nz/products-services/geodetic/positionz
- GeoNet PositioNZ-RT latency announcement: https://www.geonet.org.nz/news/3koCTl5HQsiUIGIk0eUg0O
- ArduSimple NZ RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-new-zealand/
- Vantage NZ CenterPoint VRS: https://www.vantage-nz.com/portfolio/centerpoint-vrs/
- HaloRTK NZ: https://halortk.co.nz/ (SSL certificate expired 2026-05-06)
- curl probe of `positionz-rt.linz.govt.nz:2101` — SOURCETABLE 200 OK confirmed 2026-05-06
