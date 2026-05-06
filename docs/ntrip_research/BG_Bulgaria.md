# Bulgaria [BG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — private commercial NTRIP caster operating (GeoNet / GEO-RTK); pricing not publicly listed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private/commercial) |
| **Network name** | GeoNet — ГНСС мрежа ГеоНет (GEO-RTK) |
| **Operator** | "Зенит-Гео" ЕООД (Zenit-Geo Ltd), commercial private operator; technical/distribution partner: "Солитех" АД (Solitech AD), official Trimble reseller for Bulgaria |
| **Certification** | Certificate of conformity No. 013/2020 (renewed to 2026 per 2024-07-01 news); certified against Instruction РД-02-20-25/2011 by АГКК (Agency for Geodesy, Cartography and Cadastre) |
| **host:port** | `gnss.geonet.bg:2101` (also documented with direct IP `95.43.249.1:2101`) |
| **VRS** | Not confirmed from public sources |
| **tariff** | Null — pricing exists in PDF at `https://solitech.bg/wp-content/uploads/2026/04/planove-geonet-04.2026.pdf` (April 2026 edition) but could not be accessed during research. No individual tariff figures published as plain HTML on geonet.bg. Contact: info@geonet.bg / 0700 1 GNSS (0700 1 4677) |
| **hobbyist_eligibility** | Unclear — access requires a contract ("след сключване на договор"). Service description targets geodesy, construction, agriculture, and GIS. No explicit exclusion of private individuals stated, but no individual/consumer pricing tier is advertised. Requires contacting Solitech АД. |
| **legal_residency_required** | Unclear — no geographic restriction stated on the public website; however, the contract-based access model implies Bulgarian business/legal presence may be expected in practice |
| **last_confirmed_alive** | 2026-04-30 (geonet.bg loaded normally; subscriptions page live and linking to April 2026 PDF; most recent news item dated 2024-07-01 — certificate renewal) |

## Context Notes

- **GeoNet Bulgaria** (`gnss.geonet.bg:2101`): Private NTRIP network operated by Zenit-Geo Ltd and distributed by Solitech AD (Trimble Bulgaria). Confirmed active by АГКК certification renewal in July 2024.
- **Connection details**: Documented on the public help page (`geonet.bg/help.html`): "IP адрес: 95.43.249.1 или gnss.geonet.bg | Port: 2101".
- **Subscription structure**: The subscriptions page (`geonet.bg/abonamenti.html`) describes two plan types: (1) unlimited access to RTK and DGPS corrections (heavy users), and (2) plans with included monthly RTK and PPData consumption (occasional users). All pricing is in the Solitech PDF only.
- **Pricing gap**: The Solitech PDF (`planove-geonet-04.2026.pdf`, dated April 2026) is the sole source of tariff figures; the domain solitech.bg was not accessible from the research environment. To obtain current pricing: contact info@geonet.bg or call 0700 1 4677.
- **No free/government tier**: Bulgaria has no known free public RTK caster. GeoNet is the primary real-time network.

## Sources Consulted
- GeoNet Bulgaria main site: https://geonet.bg/ (observed 2026-04-30)
- GeoNet subscriptions page: https://geonet.bg/abonamenti.html (observed 2026-04-30)
- GeoNet help page: https://geonet.bg/help.html (host:port confirmation)
- Tariff PDF (inaccessible from research env): https://solitech.bg/wp-content/uploads/2026/04/planove-geonet-04.2026.pdf
- Contact: info@geonet.bg / 0700 1 4677
