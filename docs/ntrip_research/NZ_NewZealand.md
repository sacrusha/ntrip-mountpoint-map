# New Zealand [NZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh; prior pass 2026-05-12)

## Status: YES — free government NTRIP caster (PositioNZ-RT, LINZ) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (PositioNZ-RT — free) |
| **landing_url** | https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-real-time-service (operator service page) |
| **access_url** | https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-real-time-service/connect-positionz-real-time-service (connection + registration instructions) |
| **host:port — PositioNZ-RT** | `positionz-rt.linz.govt.nz:2101` (IP: 161.65.59.99) |
| **num_stations** | ~52 physical CORS — 37 LINZ-operated PositioNZ sites + ~15 GeoNet GNSS stations re-streamed by the same caster (operator declarations on LINZ + GeoNet pages). Live sourcetable: 62 STR rows on 2026-05-17 (some sites publish multiple format streams). |
| **mountpoints** | 62 active streams in sourcetable on 2026-05-12 (mix of LINZ + GeoNet sites; e.g. AUCK00NZL0, BLUF00NZL0, CHTI00NZL0, AVLN00NZL0). RTCM 3.2/3.3 MSM (GPS+GLO+GAL+BDS+QZS). |
| **vrs** | no — single-base only; streams raw RTCM from nearest physical CORS; recommended use within 15 km of the connected station. LINZ does not operate a VRS / network-RTK product. |
| **tariff** | Free — registration required |
| **hobbyist_eligibility** | yes — no professional licensing or commercial restrictions stated; open registration |
| **legal_residency_required** | no — no residency restriction found in public documentation |
| **last_confirmed_alive** | `positionz-rt.linz.govt.nz:2101` SOURCETABLE 200 OK confirmed 2026-05-17 (curl --http0.9, BKG NtripCaster 2.0.36/2.0 server header; 62 STR rows) |
| **datum_epoch** | NZGD2000 — operator declaration: "This free service allows users of real-time GNSS equipment to obtain positions in terms of New Zealand Geodetic Datum 2000 (NZGD2000)" (LINZ PositioNZ-RT page, https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-real-time-service). NZGD2000 is plate-fixed (Australian plate); semi-dynamic per primer [datum-epoch]; deformation model maintained by LINZ. No epoch printed on the real-time service page. |

## Context Notes

- **PositioNZ-RT**: Operated by Toitū Te Whenua Land Information New Zealand (LINZ); data streaming managed by GeoNet. Free real-time NTRIP service providing 1 Hz GNSS data from the PositioNZ CORS network in NZGD2000 reference frame.
- **Infrastructure**: 37 LINZ-operated continuously operating reference stations (CORS) throughout New Zealand (including Chatham Islands) and Antarctica (Scott Base). The PositioNZ-RT caster also re-streams ~15 GeoNet-operated GNSS stations, bringing the active mountpoint total to ~62 as confirmed in the live sourcetable (2026-05-12). Signals: GPS, GLONASS, Galileo, BeiDou, QZSS.
- **Mountpoint naming convention**: `XXXX00NZL0` (e.g., WARK00NZL0 = Warkworth, AUCK00NZL0 = Whangaparaoa No 3). Operator tag in sourcetable is `LINZ` or `GeoNet` per station. Format: RTCM 3.2/3.3 with MSM (1004, 1012, 1006, 1008, 1013, 1033, 1074, 1084, 1094, 1114, 1124).
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
- curl probe of `positionz-rt.linz.govt.nz:2101` — SOURCETABLE 200 OK confirmed 2026-05-17 (62 STR rows; mix of LINZ and GeoNet operators)
- Volunteer rtk2go presence (`stations_by_country.py NZL`, 2026-05-17): 11 rtk2go bases — Ash_NZ, Ealing_NZ, Fireycreek, HitchcockFarm, JYFL, MathewsLaneBase, SurreyHills_NZ, TakiViewFarm, jacksbay, knapdaleRTK, opihi (Fireycreek new since 2026-05-12)
- AUSCORS NZL-tagged rebroadcast: 54 stations; IGS-IP: 8 stations — useful supplemental coverage
