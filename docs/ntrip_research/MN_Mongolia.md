# Mongolia [MN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-12 — NTRIP endpoint identified)

## Status: YES — MonPOS national NTRIP caster identified (rtk.gazar.gov.mn); access via published rover account

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — MonPOS (Mongolian Positioning System / MGL_network), operated by ALMGG / gazar.gov.mn |
| **host:port** | `rtk.gazar.gov.mn` (also reachable at IP `66.181.168.80`) — port not published in our sources; likely standard NTRIP 2101 or Leica Spider 8080/9001. Curl test from sandbox not possible. |
| **Mountpoint** | `MGL_network` — network RTK (VRS-style); accuracy 2 cm + 1 ppm within ~35 km of the nearest station; RTCM 3.x required |
| **Published credentials** | Username `rover` / password `262461` (widely reported in surveying community posts as the public access account; treat as shared demo credentials — verify with ALMGG before relying on them long-term) |
| **Portal** | https://monpos.gazar.gov.mn/ — MonPOS web portal; CORS status at http://cors.gazar.gov.mn/all/ ; online GNSS processing system at https://en.gazar.gov.mn/system/10 |
| **tariff** | Not publicly published; "rover/262461" account suggests open or demo access for cadastral/survey use. Formal licensed-survey accounts almost certainly require contract with ALMGG. |
| **hobbyist_eligibility** | Likely yes via the shared rover account for casual use; unverified for systematic/commercial use |
| **legal_residency_required** | Unknown; no explicit residency requirement found |
| **last_confirmed_alive** | MonPOS portal pages live as of 2026-05-12; published rover credentials referenced in recent (2024–2026) community sources. WebFetch of monpos.gazar.gov.mn and cors.gazar.gov.mn returned TLS certificate errors from sandbox — site is up but uses an outdated/self-signed cert. |

## Most Recent Project Announcement

- **2024–2026 (community reporting):** MonPOS NTRIP endpoint and rover credentials `rover / 262461` for mountpoint `MGL_network` (rtk.gazar.gov.mn or 66.181.168.80) circulated in Mongolian surveying community references. ALMGG's online-systems page (en.gazar.gov.mn/system/10) describes MONPOS as the GNSS online processing system.
- **2011 (ongoing):** ALMGG (now operating as gazar.gov.mn) built an initial 6-station CORS network in Ulaanbaatar, Darkhan, and Erdenet with support from the US Millennium Challenge Corporation / ILS. The network has expanded to 38–40+ stations nationwide.
- **2019:** mycoordinates.org article describes the ALMGG CORS network as delivering "centimeter level real time corrections for applications such as cadastral, surveying, construction and mining."
- **ALMGG online systems portal:** https://en.gazar.gov.mn/p/613-110

## Context Notes

- Mongolia has a well-developed CORS infrastructure of 38–40+ stations equipped with Trimble NetR8/NetR9 receivers and choke-ring antennas, all operated by the government geodesy agency (ALMGG / gazar.gov.mn).
- **NTRIP service** is live as MonPOS at `rtk.gazar.gov.mn` (IP `66.181.168.80`) with mountpoint `MGL_network` and shared rover credentials (`rover` / `262461`) widely circulated in the Mongolian surveying community. Service description specifies 2 cm + 1 ppm accuracy within ~35 km, RTCM 3.x required.
- **CORS monitoring page**: http://cors.gazar.gov.mn/all/ lists CORS station locations and heights (TLS cert issue in sandbox).
- A secondary academic GNSS network (7 stations around Ulaanbaatar) is run by the Seismological Department of the Institute of Astronomy and Geophysics (IAG), Mongolian Academy of Sciences — for geodynamics research only.
- **IGS station ULAB** (Ulaanbaatar): founded 1997 jointly by GFZ Potsdam (Germany) and IAG/MAS; serves as the master station for GNSS-based geodetic activities in Mongolia. RINEX archive available via EarthScope/IGS.
- Private mining-sector companies reportedly operate additional CORS, but access would be proprietary.
- Regional commercial networks (GEODNET, ONOCOY, PointOne): no confirmed Mongolia coverage.
- **No rtk2go / Centipede / EarthScope coverage** within 500 km of Ulaanbaatar (py scripts/stations_by_radius.py 47.92 106.92 500 returns no stations, 2026-05-12).
- **Contact**: +976-51260203 · +976-11-322683 · info@gazar.gov.mn · Government Building XII, Barilgachidiin square, Chingeltei district, 4th khoroo, Ulaanbaatar.
- Practical workaround if rover account fails: contact ALMGG directly for a licensed account, or use satellite-based PPP (Trimble RTX, NRCAN PPP, Galileo HAS coverage limited at high latitude).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **ALMGG / gazar.gov.mn** — daily RINEX files at 30 s sample rate from CORS network | https://en.gazar.gov.mn/p/613-110 | Likely free for geodetic/survey use; registration required (unconfirmed) |
| **IGS / ULAB station** (Ulaanbaatar) — founded 1997 by GFZ Germany + IAG/MAS; long-running global geodetic station | https://www.earthscope.org/data/gnss-data/ | Free |

## Sources Consulted
- mycoordinates.org — "GNSS-CORS geodetic network development in Mongolia" (2019): https://mycoordinates.org/gnss-cors-geodetic-network-development-in-mongolia/
- MundoGEO — "ILS Delivers CORS Infrastructure in Mongolia" (2011): https://mundogeo.com/en/2011/01/03/ils-delivers-cors-infrastructure-in-mongolia/
- GIM International — "CORS Infrastructure Supporting GIS Mapping": https://www.gim-international.com/content/news/cors-infrastructure-supporting-gis-mapping
- ALMGG official portal: https://en.gazar.gov.mn/
- ALMGG MONPOS GNSS online processing system: https://en.gazar.gov.mn/system/10
- MonPOS web portal (TLS cert expired in sandbox): https://monpos.gazar.gov.mn/
- CORS station status: http://cors.gazar.gov.mn/all/
- ALMGG online systems: https://en.gazar.gov.mn/p/613-110
- ovorkhangai.gazar.gov.mn (Mongolian-language CORS page): https://ovorkhangai.gazar.gov.mn/?n=1490&p=770
- Surveying community search (2026-05-12) — confirms NTRIP endpoint `rtk.gazar.gov.mn` / `66.181.168.80`, mountpoint `MGL_network`, rover credentials `rover` / `262461`, RTCM 3.x, 2 cm + 1 ppm within ~35 km
- ArduSimple country RTK list (Mongolia not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2go monitor (no Mongolia stations observed)
- py scripts/stations_by_radius.py 47.92 106.92 500 (2026-05-12) — zero rtk2go/Centipede/EarthScope stations within 500 km of Ulaanbaatar
