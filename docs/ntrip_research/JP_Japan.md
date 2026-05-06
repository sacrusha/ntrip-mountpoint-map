# Japan [JP] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — multiple private commercial NTRIP RTK casters; GSI GEONET raw data open but no public RTK caster; QZSS CLAS free satellite alternative

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No free government caster; yes — commercial NTRIP casters (multiple private operators using GEONET data) |
| **National CORS** | GEONET — 1,300+ stations operated by GSI (Geospatial Information Authority); raw 1-sec data open since 2002 for private sector use |
| **Government NTRIP RTK caster** | None — GSI does not operate a public NTRIP RTK caster; real-time data licensed to private service providers |
| **host:port — Nippon GPS Data Service** | `ntrip.gpsdata.co.jp:2101` (primary commercial provider using GEONET data) |
| **tariff — Nippon GPS Data Service** | Registration fee + tiered usage plans: FREE/DAY/MINUTE/YEAR courses; changing course costs ¥5,500 incl. tax. Exact per-course rates not publicly listed on pricing page as of 2026-05-06; contact gpsdata.co.jp |
| **host:port — SoftBank ichimill** | NTRIP endpoint issued after account registration (softbank.jp/biz/services/analytics/ichimill/) |
| **tariff — ichimill** | ¥39,600/year (1 device, tax inclusive); campaign discounts available; ~¥3,300/month effective |
| **VRS** | Yes — ichimill and Nippon GPS Data Service both offer Network RTK / VRS |
| **hobbyist_eligibility** | ichimill: yes — individual accounts accepted; GNSS receiver or drone can use NTRIP access. Nippon GPS: yes — individual accounts documented |
| **legal_residency_required** | ichimill: yes effectively — Japanese address/corporate registration required; foreign individuals cannot easily sign up. Nippon GPS: unclear |
| **last_confirmed_alive** | 2026-05-06 (gpsdata.co.jp pricing page HTTP 200; ichimill.aeroentry.jp and softbank.jp/biz/services/analytics/ichimill/ HTTP 200 confirmed) |

## QZSS CLAS — Free Satellite-Broadcast Alternative

Japan operates QZSS (Quasi-Zenith Satellite System, "Michibiki"), which broadcasts free centimeter-level corrections via the L6 band:
- **CLAS** (Centimeter Level Augmentation Service): 1–2 cm accuracy throughout Japan; free; no internet or SIM required; requires a CLAS-capable receiver (e.g., u-blox NEO-D9C, Septentrio, dedicated CLAS receivers).
- **MADOCA** (Multi-GNSS Advanced Demonstration tool for Orbit and Clock Analysis): decimeter-level globally; free.
- **Note**: CLAS is a satellite-broadcast PPP-RTK service, not NTRIP. It is an excellent alternative to NTRIP for users with compatible hardware.

## Context Notes

- **GEONET**: GSI's ~1,300-station GNSS CORS network at ~20 km spacing, covering the Japanese archipelago. 30-second RINEX data is open and free via the GEONET portal (terras.gsi.go.jp). 1-second real-time data was opened to the private sector in 2002, enabling commercial network RTK services.
- **Nippon GPS Data Service Corporation (gpsdata.co.jp)**: The primary long-running commercial network RTK provider, operational since 2002. Directly uses GEONET stations plus supplementary stations. Offers VRS corrections via NTRIP. Pricing tiered (FREE / DAY / MINUTE / YEAR courses); registration fee applies. The "FREE" course likely has limited mountpoints or low usage caps — not confirmed.
- **SoftBank ichimill**: A major commercial RTK network with 3,300+ proprietary base stations (SoftBank cellular infrastructure + supplementary sites) plus QZSS augmentation. ¥39,600/year per device (tax incl.) as of 2025 pricing (sekido-rc.com confirmed). Includes access to NTRIP and optionally CLAS-based corrections. Primarily marketed to corporate users and drone operators but individual purchase is documented.
- **Other commercial casters**: Additional private network RTK operators include GeoOrtk.jp (operated by Geosense), regional surveying company casters, and equipment-vendor networks. Full inventory not researched.
- **GO!GNSS / MIRAI real-time data**: The GSI-affiliated go.gnss.go.jp portal provides experimental real-time data distribution (MIRAI project) for research; this is not a production NTRIP RTK service for general users.
- **Hobbyist note**: Japan's RTK landscape is dominated by commercial providers with no free public NTRIP caster. QZSS CLAS is the practical free alternative for users with a CLAS-capable receiver. RTK2go hosts a small number of volunteer Japanese base stations.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GSI GEONET 30-sec RINEX** | https://terras.gsi.go.jp/ | Free (registration required) |
| **GSI GEONET 1-sec RINEX (MIRAI)** | https://go.gnss.go.jp/mirai/realtime/ | Limited / research access |

## Sources Consulted
- GSI GEONET overview: https://www.gsi.go.jp/ENGLISH/geonet_english.html
- GSI GEONET data provision: https://terras.gsi.go.jp/
- Nippon GPS Data Service: https://www.gpsdata.co.jp/
- Nippon GPS Data Service pricing: https://www.gpsdata.co.jp/pricing_plan/
- Nippon GPS Data Service real-time service: https://www.gpsdata.co.jp/service_menu/realtime/
- ichimill SoftBank: https://www.softbank.jp/biz/services/analytics/ichimill/
- ichimill pricing (Sekido): https://sekido-rc.com/?pid=160912940
- ichimill IT-EX product page: https://www.it-ex.com/products/maker/softbank/ichimill.html
- GO!GNSS MIRAI real-time: https://go.gnss.go.jp/mirai/realtime/
- Lefixea LRTK GEONET + RTK guide (Japanese): https://www.lrtk.lefixea.com/en/blog-rtk-57/057
- ArduSimple Japan: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-japan/
- NTRIP-list Asia: https://ntrip-list.com/asia/
