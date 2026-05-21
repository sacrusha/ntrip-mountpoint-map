# Bulgaria [BG] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-15)
**status:** YES — one commercial NRTK caster (GeoNet / GEO-RTK, ~30 CORS, VRS). No free state-run service. 5 rtk2go + 2 Centipede BGR volunteer single-base streams provide partial free coverage; SOFI EUREF / IGS station available for RINEX post-processing.

## Primary caster — GeoNet / GEO-RTK

| field | value |
|---|---|
| landing_url | https://geonet.bg/ |
| access_url | https://geonet.bg/abonamenti.html (subscription overview; links to Solitech tariff PDF as the sole pricing source) |
| operator | "Зенит-Гео" ЕООД (Zenit-Geo Ltd) owns/operates the network; "Солитех" АД (Solitech AD) is licensed operator of record since 2011-04-04 and the contracting/distribution partner; Solitech is Trimble's reseller for Bulgaria. |
| host:port | `gnss.geonet.bg:2101` (also `95.43.249.1:2101`). Live `SOURCETABLE 200 OK` from `NTRIP Trimble Ntrip Caster 5.2`, 7 STR rows, 766 bytes, 2026-05-21. (Mountpoints are VRS-only + 2 EUREF rebroadcasts; access requires contracted credentials.) |
| num_stations | 30 physical CORS, nationwide, ~74 km mean baseline (Solitech English service page 2026-05-21) |
| vrs | yes — Solitech service pages explicitly advertise VRS for GEO-RTK and VRS DGNSS for the GIS/map tier. Constellations GPS+GLO+GAL+BDS+QZS; formats RTCM MSM, RTCM 3.1, RTCM 2.3, CMRx, CMR+. |
| tariff | All figures from Solitech tariff PDF dated 01.04.2026, ex-VAT (BG VAT 20%). **Unlimited RTK** (single account): RTK1 €105/mo · RTK3 €250/3mo · RTK6 €395/6mo · RTK12 €600/yr. Multi-account discount on unlimited: 5% (2 accts) / 7% (3 accts) / negotiated for 4+. **Included-minutes plan "ГеоНет 150"**: €15/mo flat + 150 RTK min included + €0.10/min overage, up to 2 accounts, **24-month minimum contract**. **PPData** (RINEX post-processing minutes) €0.10/min. GPRS data traffic not included; client provides SIM (~1 MB/h). Currency: EUR — switched from BGN with Bulgaria's 2025-01-01 euro adoption (prior 03.2024 PDF priced RTK12 at 1095 лв.). PDF: https://solitech.bg/wp-content/uploads/2026/04/planove-geonet-04.2026.pdf |
| hobbyist_eligibility | ? — geonet.bg/help.html (re-verified 2026-05-21) states access requires credentials issued „след сключване на договор" (after contract signing). Service targets geodesy, construction, agriculture, GIS; no individual/consumer pricing tier published; no explicit exclusion of private individuals. The cheapest entry is "ГеоНет 150" at €15/mo, but this plan requires a **24-month minimum contract** (€360 minimum commitment), which is a significant barrier for hobbyist or occasional use. Unlimited plans start at €105/mo. |
| legal_residency_required | ? — no geographic restriction stated publicly. Contract execution with Solitech АД (Sofia) is required; in practice this implies Bulgarian banking/legal capacity. |
| last_confirmed_alive | 2026-05-21 — `gnss.geonet.bg:2101` SOURCETABLE 200 OK from Trimble Ntrip Caster 5.2; 7 STR (4 VRS + 2 EUREF rebroadcast + 1 CMRx) |

`datum_epoch` omitted — Bulgaria's national CRS is BGS2005 (national realization of ETRS89, adopted 2010-07-29), but neither geonet.bg nor the Solitech service pages publish an explicit datum/epoch declaration for the GEO-RTK product, so no operator citation exists.

GeoNet holds АГКК Certificate of Conformity №013/2020, renewed 2024-07-01 (valid through 2026), per Instruction РД-02-20-25/2011 — see sources below. Relevant context for trust/institutional status; not a per-caster spec field.

### GeoNet sourcetable (2026-05-21)

| Mount | Format | Constellations | Network |
|---|---|---|---|
| `RTCM_31_VRS` | RTCM 3.1 | GPS+GLO | GeoNet |
| `RTCM_23_VRS` | RTCM 2.3 | GPS | GeoNet |
| `CMRplus_VRS` | CMR+ | GPS+GLO | GeoNet |
| `4xGNSS_VRS` | RTCM 3.4 | GPS+GLO+GAL+BDS+QZS | GeoNet |
| `4xGNSS_CMRx` | CMRx | GPS+GLO+GAL+BDS+QZS | GeoNet |
| `ZLATICA` | RTCM 3.4 | GPS+GLO+GAL+BDS+QZS | EUREF (rebroadcast, 42.71 N 24.14 E) |
| `STZG` | RTCM 3.4 | GPS+GLO+GAL+BDS+QZS | EUREF (rebroadcast, 42.43 N 24.63 E) |

## Free / volunteer fallback (2026-05-21)

- **rtk2go** (`BGR`, 5 single-base streams in `data/rtk2go.sourcetable` 2026-05-21; the prior-listed `BG-BRESTOVO-ST` has dropped off the live sourcetable):
  - `DR_TODOROV` 41.94 N 25.55 E (Haskovo, south)
  - `MESTY` 42.67 N 23.00 E (Meshtitsa, Sofia region)
  - `Pernik` 42.60 N 23.02 E (Pernik, Sofia region)
  - `Me4etoagro` 42.59 N 26.48 E (Zheliu Voivoda, central east)
  - `RUSE_BG` 43.86 N 25.96 E (Ruse, Danube north)
- **Centipede** (`BGR`, 2 single-base streams in `data/centipede.sourcetable` 2026-05-21):
  - `AGROEKIP` 43.405 N 27.380 E (Varna area, Unicore UM982)
  - `BGDD` 43.408 N 24.446 E (central north, Septentrio Mosaic-X5)

Together these volunteer bases give partial single-base RTK coverage of central, northern, and eastern Bulgaria; access is open (rtk2go: any-email signup; Centipede: free account). Sofia/Pernik area is well covered (MESTY + Pernik ~26 km from Sofia centre). Southwest (Blagoevgrad, Plovdiv) and the Black-Sea south coast are uncovered by volunteer bases.

## RINEX / reference data

- **SOFI00BGR0** — EUREF/IGS permanent station, Sofia (42.56 N 23.39 E), tri-constellation RTCM 3.3 stream on euref-ip.net and products.igs-ip.net. Useful for post-processing and for verifying receiver health; not a commodity RTK base.

## Out-of-scope / not free public RTK

- **BULiPOS** (`bulipos.eu`) — iPOS Ltd. / Institute of Water Problems (BAS) / Bulgarian Aerospace Agency research-oriented GNSS infrastructure. No public NTRIP RTK service, no self-service registration.
- **АГКК / Cadastre Agency** (`cadastre.bg`) — certifies GeoNet but operates no competing free state RTK caster.
- **GEODNET** — commercial decentralized network, paid; not a dedicated BG national service. Removed from this BG entry as a separate global network tracked in its own scope.

## Sources

- GeoNet home: https://geonet.bg/
- GeoNet connection details: https://geonet.bg/help.html — host `gnss.geonet.bg`, IP `95.43.249.1`, port `2101`, contract-based credentials (WebFetch 2026-05-21)
- GeoNet subscriptions: https://geonet.bg/abonamenti.html — two plan types; pricing only via Solitech PDF (WebFetch 2026-05-21)
- GeoNet About: https://www.geonet.bg/About_us.html — 30 stations, Zenit-Geo as owner/operator
- Solitech tariff PDF, 01.04.2026 edition: https://solitech.bg/wp-content/uploads/2026/04/planove-geonet-04.2026.pdf
- Prior tariff PDF (03.2024, BGN — for YoY): https://solitech.bg/wp-content/uploads/2024/04/geonet-03.2024.pdf
- Solitech GNSS network (EN): https://www.solitech.bg/en/services/gnss-network-geonet — 30 stations, 74 km mean baseline, Trimble Alloy + Zephyr 3 (WebFetch 2026-05-21)
- Solitech GEO-RTK service page: https://solitech.bg/uslugi/osnovni-uslugi/gnss-mrezha-geonet/geo-rtk/ — VRS, 2 cm accuracy, GPS+GLO+GAL+BDS, RTCM MSM
- АГКК certification (2024-07-01, valid through 2026): https://geonet.bg/news.html · https://www.cadastre.bg/en/content/certificate-compliance-assessment-%E2%84%96-003-2014-gnss-infrastructure-network-%E2%80%9Cgeonet%E2%80%9D
- BULiPOS landing: http://bulipos.eu/en/bulipos1.html
- АГКК (Cadastre Agency): https://www.cadastre.bg/en/frontpage
- BGS2005 datum reference (informational, not operator-cited): https://epsg.io/7797
- ArduSimple BG (no national RTK noted): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bulgaria/
- Live caster: `curl --http0.9 http://gnss.geonet.bg:2101/` SOURCETABLE 200 OK Trimble Ntrip Caster 5.2, 7 STR (2026-05-21)
- Local: `data/centipede.sourcetable` 2026-05-21 (AGROEKIP, BGDD); `data/rtk2go.sourcetable` 2026-05-21 (6 BGR rows); `py scripts/stations_by_country.py BGR` → 5 rtk2go + 2 centipede + 1 EUREF + 1 IGS
