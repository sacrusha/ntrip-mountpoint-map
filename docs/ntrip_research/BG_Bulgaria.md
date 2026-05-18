# Bulgaria [BG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-15; geonet.bg/help.html re-verified — host `gnss.geonet.bg` / IP `95.43.249.1` / port `2101` / contract-based credentials unchanged; FLEPOS-style hobbyist exclusion does NOT apply here, see notes; tariff PDF URL still serves the 04.2026 edition)

## Status: YES — one commercial network-RTK caster (GeoNet / GEO-RTK, ~30 CORS, VRS). No free state-run service. 6 rtk2go + 2 Centipede BGR volunteer single-base streams provide partial free coverage; SOFI EUREF/IGS station available for RINEX post-processing.

## Primary caster: GeoNet / GEO-RTK

| Field | Value |
|---|---|
| **Network name** | GeoNet — ГНСС мрежа ГеоНет (commercial product: GEO-RTK) |
| **Operator** | „Зенит-Гео" ЕООД (Zenit-Geo Ltd) — owner/operator. „Солитех" АД (Solitech AD) is the licensed operator of record (since 2011-04-04) and the contracting/distribution partner; Solitech is Trimble's reseller for Bulgaria. |
| **landing_url** | https://geonet.bg/ |
| **access_url** | https://geonet.bg/abonamenti.html (subscription overview; links to Solitech tariff PDF as the sole pricing source) |
| **host:port** | `gnss.geonet.bg:2101` (also resolvable as `95.43.249.1:2101`; both documented on geonet.bg/help.html 2026-05-15) |
| **num_stations** | 30 physical CORS, nationwide coverage, ~74 km mean baseline (Solitech English service page 2026-05-15) |
| **vrs** | yes — Solitech service pages explicitly name VRS for GEO-RTK and VRS DGNSS for the GIS/map tier; supported constellations GPS+GLONASS+Galileo+BeiDou; RTCM MSM, RTCM 3.1, RTCM 2.3, CMRx, CMR+ |
| **Certification** | АГКК Certificate of Conformity №013/2020, renewed 2024-07-01 (valid through 2026), per Instruction РД-02-20-25/2011 |
| **tariff** | All figures from Solitech tariff PDF dated 01.04.2026, ex-VAT (BG VAT 20%). Unlimited RTK (single account): RTK1 €105/mo · RTK3 €250/3mo · RTK6 €395/6mo · RTK12 €600/yr. Multi-account discount on unlimited: 5% (2 accts) / 7% (3 accts) / negotiated for 4+. Included-minutes plan „ГеоНет 150": €15/mo flat + 150 RTK min included + €0.10/min overage, up to 2 accounts, **24-month minimum contract**. PPData (RINEX post-processing minutes) €0.10/min. GPRS data traffic not included; client provides SIM (~1 MB/h). Currency: EUR — switched from BGN with Bulgaria's 2025-01-01 euro adoption (prior 03.2024 PDF priced RTK12 at 1095 лв.). PDF: https://solitech.bg/wp-content/uploads/2026/04/planove-geonet-04.2026.pdf |
| **hobbyist_eligibility** | unknown — geonet.bg/help.html states access requires credentials issued „след сключване на договор" (after contract signing). Service positioning targets geodesy, construction, agriculture, GIS. No individual/consumer pricing tier published; no explicit exclusion of private individuals either. Cheapest sustained-use entry is „ГеоНет 150" at €15/mo, but it carries a 24-month minimum and a contract. Test profiles with temporary credentials are mentioned. |
| **legal_residency_required** | unknown — no geographic restriction stated publicly. Contract execution with Solitech АД (Sofia) is required; in practice this implies Bulgarian banking/legal capacity. |
| **last_confirmed_alive** | 2026-05-15 — geonet.bg, geonet.bg/help.html, geonet.bg/abonamenti.html, solitech.bg/en/services/gnss-network-geonet all loaded; 04.2026 tariff PDF retrievable and extractable; sourcetable host probe not attempted (caster is credentialed) |

`datum_epoch` omitted — Bulgaria's national CRS is BGS2005 (national realization of ETRS89, adopted 2010-07-29), but neither geonet.bg nor the Solitech service pages publish an explicit datum/epoch declaration for the GEO-RTK product, so no operator citation exists.

## Free / volunteer fallback

**rtk2go (rtk2go.com:2101)** — 6 BGR single-base streams, all probed Up 2026-05-15 (>95% uptime in the SNIP status panel):
- `BG-BRESTOVO-ST` 43.14°N 24.93°E — Brestovo, central north (RTCM 3.3)
- `DR_TODOROV` 41.94°N 25.55°E — Haskovo, south (RTCM 3.2)
- `MESTY` 42.67°N 23.00°E — Meshtitsa, Sofia region (RTCM 3.2)
- `Pernik` 42.60°N 23.02°E — Pernik, Sofia region (RTCM 3.3)
- `Me4etoagro` 42.59°N 26.48°E — Zheliu Voivoda, central east (RTCM 3.2)
- `RUSE_BG` 43.86°N 25.96°E — Ruse, Danube north (RTCM 3.2)

**Centipede (`crtk.net:2101`, formerly `caster.centipede.fr`)** — 2 BGR single-base streams in the live sourcetable 2026-05-15:
- `AGROEKIP` 43.405°N 27.380°E — Varna area (Unicore UM982, GLO+GAL+SBS+BDS+GPS)
- `BGDD` 43.408°N 24.446°E — central north (Septentrio Mosaic-X5, GLO+GAL+BDS+GPS)

Together these volunteer bases give partial single-base RTK coverage of central, northern, and eastern Bulgaria; access is open (rtk2go: any email signup; Centipede: free account). Sofia/Pernik area is well covered (MESTY + Pernik ~26 km from Sofia centre). Southwest (Blagoevgrad, Plovdiv) and the Black-Sea south coast are uncovered by volunteer bases.

## RINEX / reference data

- **SOFI00BGR0** — EUREF/IGS permanent station, Sofia (42.56°N 23.39°E), tri-constellation RTCM 3.3 stream on euref-ip.net and products.igs-ip.net. Useful for post-processing and for verifying receiver health; not a commodity RTK base.

## Out-of-scope / not free public RTK

- **BULiPOS** (`bulipos.eu`) — iPOS Ltd. / Institute of Water Problems (BAS) / Bulgarian Aerospace Agency research-oriented GNSS infrastructure. No public NTRIP RTK service, no self-service registration.
- **АГКК / Cadastre Agency** (`cadastre.bg`) — certifies GeoNet but operates no competing free state RTK caster.
- **GEODNET** — commercial decentralized network, paid; previously removed from project scope (rtkdata.com aggregator).

## Sources

- GeoNet home: https://geonet.bg/ (WebFetch 2026-05-15)
- GeoNet connection details: https://geonet.bg/help.html — host `gnss.geonet.bg`, IP `95.43.249.1`, port `2101`, contract-based credentials (WebFetch 2026-05-15)
- GeoNet subscriptions: https://geonet.bg/abonamenti.html — two plan types; pricing only via Solitech PDF (WebFetch 2026-05-15)
- GeoNet About: https://www.geonet.bg/About_us.html — confirms 30 stations, Zenit-Geo as owner/operator (WebFetch 2026-05-15)
- Solitech tariff PDF, 01.04.2026 edition: https://solitech.bg/wp-content/uploads/2026/04/planove-geonet-04.2026.pdf (fetched + text-extracted locally 2026-05-15)
- Prior tariff PDF (03.2024, BGN pricing — useful for YoY): https://solitech.bg/wp-content/uploads/2024/04/geonet-03.2024.pdf
- Solitech GNSS network (EN): https://www.solitech.bg/en/services/gnss-network-geonet — 30 stations, 74 km mean baseline, Trimble Alloy + Zephyr 3 (WebFetch 2026-05-15)
- Solitech GEO-RTK service page: https://solitech.bg/uslugi/osnovni-uslugi/gnss-mrezha-geonet/geo-rtk/ — VRS, 2 cm accuracy, GPS+GLO+GAL+BDS, RTCM MSM (WebFetch 2026-05-15)
- АГКК certification announcement (2024-07-01, valid through 2026): https://geonet.bg/news.html ; archive entry: https://www.cadastre.bg/en/content/certificate-compliance-assessment-%E2%84%96-003-2014-gnss-infrastructure-network-%E2%80%9Cgeonet%E2%80%9D
- BULiPOS landing: http://bulipos.eu/en/bulipos1.html
- АГКК (Cadastre Agency): https://www.cadastre.bg/en/frontpage
- BGS2005 datum reference (informational, not operator-cited): https://epsg.io/7797
- ArduSimple country page (third-party, dated): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bulgaria/
- Local data: `data/stations.json` updated 2026-05-15T16:22Z — 6 rtk2go BGR + 1 Centipede BGR (AGROEKIP) + 1 EUREF + 1 IGS (both SOFI00BGR0)
- Live probe `http://rtk2go.com:2101/SNIP::STATUS` 2026-05-15 — all 6 BGR bases Up
- Live probe `http://crtk.net:2101/` sourcetable 2026-05-15 — AGROEKIP + BGDD listed
- Operator contact: info@geonet.bg / support@geonet.bg / 0700 1 4677
