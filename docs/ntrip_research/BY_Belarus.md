# Belarus [BY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07 (initial 2026-05-06)
**Exchange rate used:** ~2.84 BYN / 1 USD (approximate spot rate, 2026-05-07)

## Status: YES — single state-monopoly NTRIP caster (ССТП РБ / Belgeodesiya); residency-restricted, paid contract only; no free hobbyist tier; no commercial alternative

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — single state operator |
| **Operator** | РУП «Белгеодезия» (RUE Belgeodesiya — state unitary enterprise), under Государственный комитет по имуществу Республики Беларусь (Госкомимущество — State Committee for Property of the Republic of Belarus) |
| **Service name** | ССТП РБ — Спутниковая система точного позиционирования Республики Беларусь (Satellite System of Precise Positioning of the Republic of Belarus); brand "Сеть ПДП" (Network of Permanently-Operating Reference Stations) |
| **Mandate basis** | Public-offer contract (Публичный договор присоединения) under Belarusian Civil Code; tariffs effective 2023-05-01, schedule explicitly titled "для резидентов Республики Беларусь" |
| **host:port** | `sstp.geo.by:8080` (IP fallback `93.125.21.51:8080`); confirmed via direct sourcetable fetch 2026-05-07 (`SOURCETABLE 200 OK`, `Server: GNSS Spider 7.8.3.9486`, 47 STR records, Content-Length 4796) |
| **Mountpoints (port 8080, fetched 2026-05-07)** | VRS network solution: `BelarusVRS`, `BelarusVRS(MSM5)`, `BelarusVRS(MSM4)`, `BelarusVRSMSM5`; nearest-station: `NEAR`, `NEAR(MSM5)`, `NEARMSM5`, `NEARMSM4`; DGPS: `BelarusDGPS`, `NearDGPS`; precision-agriculture network: `AgroVRS`, `AgroNEAR`, `AgroGPS`, `AgroN`, `AgroMSM4`, `AgroCMR`; per-station agriculture: `AgroPINSK`, `AgroLUNINEC`, `AgroSKDL`, `AgroBBER`, `AgroSLUC`, `AgroIVAC`, `AgroSLON`; physical CORS: `SOKO`, `MRIT`, `DKSH`, `ZHLO`, `KLNK`, `UZDA`, `KLEC`, `PLES`, `RADO`, `SMOR`, `minsk`, `GROD`, `LUNI`, `BBER`, `STOL`, `VITR`, `GORO`, `ZHIT`, `BY01`, `BERE`, `NOVP`, `VILE`, `LIOZ`, `MRGO` (47 mountpoints; 24 advertised physical stations on port 8080; full national network ≈98 CORS) |
| **VRS** | Yes — `BelarusVRS*` mountpoints flagged solution=1, NMEA=1 (network solution requiring GGA from rover); `NEAR*` mountpoints serve nearest-physical-station correction (solution=0, NMEA=0/1) |
| **Constellations** | GPS+GLO on legacy mountpoints (`BelarusVRS`, `NEAR`, `BelarusDGPS`, `AgroGPS`, `AgroN`); GPS+GLO+GAL+BDS on MSM4/MSM5 mountpoints and most Agro-* mountpoints (modernised in last 1–2 years) |
| **RTCM format** | RTCM 3 across all current mountpoints; legacy CMR available on `AgroCMR`; software stack Leica GNSS Spider 7.8.3.9486 |
| **tariff — RTK metered ("Общий" plan)** | 0.24 BYN/min RTK (~$0.085/min, ~$5.07/hr); plan is for "unlimited circle of users except those covered by other plans" |
| **tariff — RTK fixed ("Точная навигация") per device per month** | 150.78 BYN/month (~$53.09/month); ~$637/yr if renewed monthly; no annual flat rate published |
| **tariff — DGPS metered ("Общий" plan)** | 0.06 BYN/min DGPS (~$0.021/min) for 0.25–1 m accuracy |
| **tariff — DGPS fixed ("Навигация DGPS") per device per month** | 37.70 BYN/month (~$13.27/month) |
| **tariff — RINEX (post-processing) per file** | 3.63 BYN per 1-hour file from one CORS (~$1.28/file); no bulk discount published |
| **tariff — Precision agriculture per-connection ("Точное земледелие" volume tiers)** | 1 connection 150.00 BYN/month, 2–5 connections 135.00 BYN/conn-month, 6–10 connections 112.50 BYN/conn-month, 11–25 connections 87.00 BYN, 26–50 connections 81.00 BYN, 51–100 connections 75.00 BYN, 101+ connections 69.00 BYN (per individual connection per calendar month, billed by actual count of unique device connections per month) |
| **tariff — Agriculture flat-rate (with land-use territorial restriction)** | 700.00 BYN/calendar month or 6,000.00 BYN/calendar year (~$2,113/yr) per device, unlimited connections, geographically limited to Customer's registered land-use parcel(s) |
| **tariff — Educational ("Учебный") plan** | Available only to Belarusian state-funded educational institutions for postgrad/master's research; per-minute rate cell empty in published PDF (gap) |
| **VAT status** | All tariffs explicitly stated "без НДС" (excluding 20% VAT); transmission costs over telecoms links also explicitly excluded and billed separately |
| **hobbyist_eligibility** | Unclear in practice — "Общий" plan text states corrections are provided "неограниченному кругу пользователей, кроме тех, кто подпадает под действие иных тарифных планов" (unlimited circle of users except those covered by other plans), implying any individual may sign the public-offer contract. However: (1) no self-service web portal exists, all access requires signed paper contract with Belgeodesiya; (2) the entire tariff PDF is titled "для резидентов Республики Беларусь"; (3) sanctions context (see Notes) restricts non-resident access in practice. |
| **legal_residency_required** | Yes — tariff title explicitly limits service to residents of the Republic of Belarus (физических и юридических лиц со статусом резидента); contract execution requires Belarusian banking and tax data |
| **last_confirmed_alive** | 2026-05-07 — sourcetable fetch returned 200 OK with 47 STR records; geo.by main site, services/sstp page, tariff PDF, public-contract PDF, RTK manual PDF all served normally |

## Context Notes

- **Network history**: ССТП РБ is the single national CORS network. Belgeodesiya (РУП «Белгеодезия», successor to "Белаэрокосмогеодезия") has operated reference stations under the State Committee for Property since the network's inception. Belgeodesiya cites ~98 continuously-operating reference stations covering the country with declared horizontal accuracy 1–5 cm RTK and 0.25–1 m DGPS. Since March 2020, station data is also fed to two analytical centres of the EPN (EUREF Permanent Network) for academic processing — but the RTK correction service is entirely separate from EUREF.
- **Belarus and EUREF**: Belgeodesiya began uploading GNSS data to EUREF Permanent Network (EPN) processing centres on 2020-03-01, making selected Belarusian reference station RINEX data available to the scientific community via the EPN archive. This is a one-way contribution to academic processing — it does not grant access to real-time NTRIP streams.
- **Sanctions context**: EU Regulation 765/2006 (Belarus sanctions, extended through 2024–2025 packages) and parallel US/UK controls suspend exports of dual-use goods and advanced surveying equipment to Belarus. Topcon, Trimble, and Leica Geosystems publicly suspended GNSS product distribution to Belarus in 2022. Replacement rover hardware is materially harder to source than in unsanctioned neighbours; the Belarusian distributor channel (geotop.by, geoportal.by) is restricted to non-Western brands (CHCNav, South, Hi-Target, Geomax). This compounds the access barrier — even a Belarus-resident hobbyist who could sign the public contract faces a constrained hardware market.
- **Access workflow**: (1) download `Публичный договор присоединения` PDF from `geo.by/about/public_contract_pred_yclyg_SSTP.pdf`; (2) sign and submit the join-agreement (заявление о присоединении) with Belarusian tax/account details; (3) Belgeodesiya issues unique NTRIP credentials for one device per contract; (4) caster `sstp.geo.by:8080` connects with the issued login. No web self-service signup. No published account-portal URL.
- **Tariff PDF reading**: The official `geo.by/images/tariffs.pdf` (effective 2023-05-01) is structured as two pages of stacked tables. After PDF text extraction with proper UTF-8 layout, the reading is: Plan 1 "Общий" — RTK 0.24 BYN/min, DGPS 0.06 BYN/min, RINEX 3.63 BYN/file/hr; Plan 3 "DGPS" — 0.06 BYN/min; Plan 4 "Точная навигация" — 150.78 BYN/month; Plan 5 "Навигация DGPS" — 37.70 BYN/month; Plan 6 "Точное земледелие" — tiered per-connection schedule from 150.00 down to 69.00 BYN; bottom panel — agriculture flat 700/month or 6,000/year with territorial restriction. A `0.91 BYN` figure appears in the layout-extraction near Plan 1 but is unlabeled in the column structure — gap, contact required to confirm purpose.
- **Volunteer alternatives — none**: rtk2go has zero confirmed BY-coded bases (verified against `data/rtk2go.sourcetable` 2026 archives); Centipede has zero BY nodes. Sanctions, ICANN .by ccTLD restrictions, and the closed contract-only access model mean Belarus has no public-internet hobbyist path to centimetre-level corrections.
- **Coordinate frames**: Real-time corrections delivered in ITRS (realisation ITRF2005); post-processing RINEX offered in ITRS, СК-95, СК-63, or local systems. ITRF2005 is older than current ITRF2020/2014 used by neighbouring networks — relevant for cross-border hobbyists processing static data, immaterial for hobbyist RTK rover use.
- **Equipment context (per geoportal.by)**: Active distributors note that GNSS receivers are configured by entering server IP, port, login, password into the rover's NTRIP client; Belgeodesiya supplies these credentials per signed contract. Compatible hardware listed includes CHCNav i50/i90, South Galaxy G1/G6, Hi-Target V60, Geomax Zenith — i.e., non-Western brands legal to import under sanctions.

## Post-Processing (RINEX) Fallback

- **Belgeodesiya RINEX**: 3.63 BYN per 1-hour file from one CORS, available via signed contract; procedure documented in `geo.by/about/Manual_RINEX.pdf`. Same residency restriction.
- **EUREF EPN archive**: Selected Belarusian stations contributed since 2020-03-01; free download via https://www.epncb.oma.be/ — academic-use; daily 30-second RINEX, no real-time stream.

## Most Recent Public Announcement (date + URL)

- 2024-12 onward: continued integration of Belgeodesiya CORS data into EPN analysis centres (geo.by/en/ news). No public announcement of new self-service portal, new station deployments, or tariff revision in 2024–2026 review window.
- Tariff PDF dated 2023-05-01 (`geo.by/images/tariffs.pdf`) — last published price update; tariff list still served from the same URL on 2026-05-07.

## Sources Consulted
- ССТП РБ services landing page (Russian): https://geo.by/services/sstp (observed 2026-05-07)
- ССТП РБ "Предоставление информации сети ПДП" detail page: https://geo.by/services/sstp/predostavlenie-informatsii-sstp (observed 2026-05-07)
- Belgeodesiya tariff PDF: https://geo.by/images/tariffs.pdf (effective 2023-05-01; observed 2026-05-07; 2-page Russian PDF, full text extracted)
- Belgeodesiya public-offer contract template: https://geo.by/about/public_contract_pred_yclyg_SSTP.pdf
- Belgeodesiya RTK manual: https://geo.by/about/Manual_RTK.pdf
- Belgeodesiya RINEX manual: https://geo.by/about/Manual_RINEX.pdf
- Direct sourcetable fetch: `http://sstp.geo.by:8080/` (Server: GNSS Spider 7.8.3.9486; 47 STR; observed 2026-05-07; HTTP 0.9 fallback required)
- State Property Committee profile (English): https://gki.gov.by/en/activity_branches-geomaps-en/
- Belarusian distributor commentary (CORS pricing context): https://geotop.by/news/2082/bezlimitnye-rtk-popravki/
- Geoportal Belarus (rover connection guide): https://geoportal.by/katalog/gps_gnss_priemniki_dlja_geodezii/podklyuchenie-k-seti-bazovyh-stanciy-74/
- State Committee on Property GNSS user guide (PDF): https://nca.by/upload/medialibrary/b65/5vk1ph5lep7lx7ap9fn2lbq9glnn4utf/prilozhenie_2_rukovodstvo_po_ispol_zovaniu_gnss.pdf
- BELTA news (EPN data sharing announcement, 2020): https://eng.belta.by/economics/view/belarus-about-to-start-sharing-gnss-data-with-european-network-128634-2020/
- GPS World coverage of EPN sharing: https://www.gpsworld.com/belarus-to-start-sharing-gnss-data-with-european-network/
- Contact: Belgeodesiya, info@belgeodesy.by, +375 17 334 79 49

## Known Data Gaps
- **0.91 BYN line item**: Unlabeled in mis-aligned tariff PDF extraction — confirm purpose with Belgeodesiya support.
- **"Учебный" (Educational) RTK rate**: Per-minute price cell appears empty in published PDF; Belgeodesiya did not publish the educational rate explicitly. Plan is available only to Belarusian state education institutions for postgrad work — not a hobbyist path.
- **Annual RTK flat rate**: None published. Effective annual cost via "Точная навигация" monthly auto-renewal is ~1,809.36 BYN/yr (~$637/yr per device) — well above the project's $200/yr hobbyist cutoff.
- **Self-service registration**: None. Verify via direct contact with Belgeodesiya whether any web self-service exists outside the public-contract paper workflow.
- **Port 8081**: Older country-survey notes referenced port 8081 as a separate "Precision Agriculture" caster. As of 2026-05-07, port 8081 was not reachable from the research environment, and all Agro-* mountpoints are now consolidated on port 8080. The 8081 reference may be obsolete.
