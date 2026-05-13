# Bulgaria [BG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refreshed 2026-05-13: Solitech 04.2026 tariff PDF extracted)

## Status: YES — private commercial NTRIP caster operating (GeoNet / GEO-RTK); 04.2026 Solitech tariff PDF extracted and pricing now confirmed (€600/yr unlimited RTK ex-VAT); plus 6 rtk2go and 2 Centipede volunteer bases providing partial free coverage

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private/commercial) |
| **Network name** | GeoNet — ГНСС мрежа ГеоНет (GEO-RTK) |
| **Operator** | "Зенит-Гео" ЕООД (Zenit-Geo Ltd), commercial private operator; technical/distribution partner: "Солитех" АД (Solitech AD), official Trimble reseller for Bulgaria |
| **Certification** | Certificate of conformity No. 013/2020 (renewed to 2026 per 2024-07-01 news); certified against Instruction РД-02-20-25/2011 by АГКК (Agency for Geodesy, Cartography and Cadastre) |
| **host:port** | `gnss.geonet.bg:2101` (also documented with direct IP `95.43.249.1:2101`) |
| **VRS** | Not confirmed from public sources |
| **tariff** | Solitech tariff PDF extracted 2026-05-13 (`https://solitech.bg/wp-content/uploads/2026/04/planove-geonet-04.2026.pdf`, dated 01.04.2026, ex-VAT). Unlimited RTK: RTK1 €105/mo · RTK3 €250/3mo · RTK6 €395/6mo · RTK12 €600/yr. Included-minutes: ГеоНет 150 = €15/mo monthly fee + 150 RTK min included + €0.10/min overage, valid for up to 2 accounts, 24-month minimum contract. PPData €0.10/min. Multi-account discount on unlimited plans: 5% (2 accts) / 7% (3 accts) / negotiated for 4+. Currency switched BGN → EUR with Bulgaria's 2025-01-01 euro adoption (the 03.2024 edition of the same PDF was in лв./BGN with RTK12 1095 лв.). No individual tariff figures published as plain HTML on geonet.bg. Contact: info@geonet.bg / 0700 1 GNSS (0700 1 4677) |
| **hobbyist_eligibility** | Unclear — access requires a contract ("след сключване на договор"). Service description targets geodesy, construction, agriculture, and GIS. No explicit exclusion of private individuals stated, but no individual/consumer pricing tier is advertised. Requires contacting Solitech АД. |
| **legal_residency_required** | Unclear — no geographic restriction stated on the public website; however, the contract-based access model implies Bulgarian business/legal presence may be expected in practice |
| **last_confirmed_alive** | 2026-04-30 (geonet.bg loaded normally; subscriptions page live and linking to April 2026 PDF; most recent news item dated 2024-07-01 — certificate renewal) |

## Context Notes

- **GeoNet Bulgaria** (`gnss.geonet.bg:2101`): Private NTRIP network operated by Zenit-Geo Ltd and distributed by Solitech AD (Trimble Bulgaria). Confirmed active by АГКК certification renewal in July 2024.
- **Connection details**: Documented on the public help page (`geonet.bg/help.html`): "IP адрес: 95.43.249.1 или gnss.geonet.bg | Port: 2101".
- **Subscription structure**: The subscriptions page (`geonet.bg/abonamenti.html`) describes two plan types: (1) unlimited access to RTK and DGPS corrections (heavy users), and (2) plans with included monthly RTK and PPData consumption (occasional users). All pricing is in the Solitech PDF only.
- **Pricing (extracted 2026-05-13 from PDF text)**: The Solitech PDF `planove-geonet-04.2026.pdf` dated 01.04.2026 is the sole source of tariff figures and is now retrievable via the public URL. Four unlimited-RTK plans (€105 / €250 / €395 / €600 for 1 / 3 / 6 / 12 months ex-VAT) plus an included-minutes plan "ГеоНет 150" (€15/mo flat, 150 RTK min included, two accounts, 24-month minimum). PPData (post-processing minute pricing) €0.10/min. Multi-account unlimited discount 5/7%. Prior 03.2024 edition (also still on Solitech CDN) priced in BGN: RTK12 1095 лв., ГеоНет 30 / 60 included-minutes tiers; the Apr-2026 revision drops those two small tiers, switches to euro, and re-prices RTK12 at €600 (~1173 BGN, ≈7% YoY uplift after currency conversion).
- **No free/government tier**: Bulgaria has no known free public RTK caster from a state agency. AGKK (Agency for Geodesy, Cartography and Cadastre) certifies GeoNet but does not run a competing free service. **BULiPOS** (`bulipos.eu`) — operated by iPOS Ltd. in partnership with the Institute of Water Problems (BAS) and the Bulgarian Aerospace Agency — is a research-oriented GNSS network ("Bulgarian referent system for indicating location and for orienting in space"); no public NTRIP RTK service or self-service registration found. GeoNet remains the primary commercial real-time network.
- **Volunteer free bases**: 6 rtk2go BGR-coded bases visible in `data/stations.json` 2026-05-12 — `BG-BRESTOVO-ST` (43.14°N, 24.93°E, central north), `DR_TODOROV` (41.94°N, 25.55°E, south), `MESTY` and `Pernik` (Sofia region, 42.59–42.67°N, 23.00–23.02°E), `Me4etoagro` (42.59°N, 26.48°E, central east), `RUSE_BG` (43.86°N, 25.96°E, Danube north). Plus 2 Centipede BGR nodes — `AGROEKIP` (43.40°N, 27.38°E, Varna area) and `BGDD` (43.41°N, 24.45°E, central north). Together these give partial single-base RTK coverage of central, northern and eastern Bulgaria; access via `rtk2go.com:2101` / `caster.centipede.fr:2101`, no signup.

## Sources Consulted
- GeoNet Bulgaria main site: https://geonet.bg/ (observed 2026-04-30)
- GeoNet subscriptions page: https://geonet.bg/abonamenti.html (WebFetch 2026-05-12 — confirmed two plan-type architecture; pricing only in Solitech PDF)
- GeoNet help page: https://geonet.bg/help.html (WebFetch 2026-05-12 — confirmed host `gnss.geonet.bg` / IP `95.43.249.1`, port `2101`, contract-based access)
- Tariff PDF (04.2026, full text extracted 2026-05-13 via WebFetch + local pypdf): https://solitech.bg/wp-content/uploads/2026/04/planove-geonet-04.2026.pdf
- Prior tariff PDF (03.2024, BGN pricing, kept on Solitech CDN — useful for YoY comparison): https://solitech.bg/wp-content/uploads/2024/04/geonet-03.2024.pdf
- Solitech GEO-RTK service page (confirms VRS / MAX / FKP network-RTK product line): https://solitech.bg/uslugi/osnovni-uslugi/gnss-mrezha-geonet/geo-rtk/ (observed 2026-05-13)
- BULiPOS Bulgarian referent system page: http://bulipos.eu/en/bulipos1.html (research-oriented network; no NTRIP RTK service detail published)
- Bulgarian Geodesy, Cartography and Cadastre Agency: https://www.cadastre.bg/en/frontpage (administers GeoNet certification; does not operate a competing free state RTK caster)
- ArduSimple Bulgaria page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bulgaria/
- `data/stations.json` 2026-05-12 — 6 rtk2go BGR bases and 2 Centipede BGR nodes confirmed (mountpoint list above)
- Contact: info@geonet.bg / 0700 1 4677
