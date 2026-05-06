# Mongolia [MN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: POSSIBLE active public NTRIP caster (unconfirmed public access)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — CORS infrastructure exists; public NTRIP stream not confirmed |
| **host:port** | Unknown |
| **tariff** | Unknown |
| **hobbyist_eligibility** | Unknown |
| **legal_residency_required** | Unknown |
| **last_confirmed_alive** | Unknown — CORS network operational as of 2019 (most recent confirmed date found) |

## Most Recent Project Announcement

- **2011 (ongoing):** The Agency for Land Administration and Management, Geodesy and Cartography (ALMGG, now operating as gazar.gov.mn) built an initial 6-station CORS network in Ulaanbaatar, Darkhan, and Erdenet with support from the US Millennium Challenge Corporation / ILS. The network has expanded to 38–40+ stations nationwide.
- **2019:** mycoordinates.org article describes the ALMGG CORS network as delivering "centimeter level real time corrections for applications such as cadastral, surveying, construction and mining." No NTRIP endpoint URL published externally.
- **ALMGG online systems portal:** https://en.gazar.gov.mn/p/613-110 (lists online services but NTRIP access details not publicly documented as of research date).

## Context Notes

- Mongolia has a well-developed CORS infrastructure of 38–40+ stations equipped with Trimble NetR8/NetR9 receivers and choke-ring antennas, all operated by the government geodesy agency (ALMGG / gazar.gov.mn).
- The network officially "supplies centimeter level real time corrections" per published sources, suggesting an RTK/NTRIP distribution layer exists internally; however, no externally accessible NTRIP caster host:port has been documented in English or Mongolian-language web sources as of 2026-05-06.
- A secondary academic GNSS network (7 stations around Ulaanbaatar) is run by the Seismological Department of the Institute of Astronomy and Geophysics (IAG), Mongolian Academy of Sciences — for geodynamics research only, not an RTK corrections service.
- **IGS station ULAB** (Ulaanbaatar): founded 1997 jointly by GFZ Potsdam (Germany) and IAG/MAS; serves as the master station for GNSS-based geodetic activities in Mongolia. RINEX archive available via EarthScope/IGS.
- Private mining-sector companies reportedly operate additional CORS, but access would be proprietary.
- Regional commercial networks (GEODNET, ONOCOY, PointOne): no confirmed Mongolia coverage confirmed.
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, NRCAN PPP, Galileo HAS).

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
- ALMGG online systems: https://en.gazar.gov.mn/p/613-110
- ovorkhangai.gazar.gov.mn (Mongolian-language CORS page): https://ovorkhangai.gazar.gov.mn/?n=1490&p=770
- ArduSimple country RTK list (Mongolia not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2go monitor (no Mongolia stations observed)
