# Belarus [BY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15
**Exchange rate used:** ~2.84 BYN / 1 USD (approximate spot rate, May 2026)

## Status: YES — single state-monopoly NTRIP caster (ССТП РБ / Belgeodesiya); residency-restricted, paid contract only; no free hobbyist tier; no commercial alternative

| Field | Value |
|---|---|
| **landing_url** | https://geo.by/services/sstp |
| **access_url** | https://geo.by/services/sstp/predostavlenie-informatsii-sstp (lists `Публичный договор`, accession-application form, RTK manual, RINEX manual, and tariff PDF) |
| **Active public NTRIP RTK caster** | Yes — single state operator |
| **Operator** | РУП «Белгеодезия» (RUE Belgeodesiya — state unitary enterprise) under Государственный комитет по имуществу Республики Беларусь (State Committee for Property of the Republic of Belarus) |
| **Service name** | ССТП РБ — Спутниковая система точного позиционирования Республики Беларусь (Satellite System of Precise Positioning of the Republic of Belarus); brand "Сеть ПДП" (Network of Permanently-Operating Reference Stations) |
| **Mandate basis** | Public-offer contract (Публичный договор присоединения) under Belarusian Civil Code; tariff schedule explicitly titled "для резидентов Республики Беларусь" |
| **host:port** | `sstp.geo.by:8080` (IP fallback `93.125.21.51:8080` — same caster, identical sourcetable); confirmed 2026-05-15 |
| **num_stations** | 47 advertised STR records on port 8080 (24 distinct physical CORS mountpoints + VRS/NEAR/Agro/DGPS variants); operator declares ~98 physical CORS nationwide (full network not exposed in the public sourcetable) |
| **Mountpoints (port 8080, fetched 2026-05-15)** | VRS network solution: `BelarusVRS`, `BelarusVRS(MSM5)`, `BelarusVRS(MSM4)`, `BelarusVRSMSM5`; nearest-station: `NEAR`, `NEAR(MSM5)`, `NEARMSM5`, `NEARMSM4`; DGPS: `BelarusDGPS`, `NearDGPS`; precision-agriculture network: `AgroVRS`, `AgroNEAR`, `AgroGPS`, `AgroN`, `AgroMSM4`, `AgroCMR`; per-station agriculture: `AgroPINSK`, `AgroLUNINEC`, `AgroSKDL`, `AgroBBER`, `AgroSLUC`, `AgroIVAC`, `AgroSLON`; physical CORS: `SOKO`, `MRIT`, `DKSH`, `ZHLO`, `KLNK`, `UZDA`, `KLEC`, `PLES`, `RADO`, `SMOR`, `minsk`, `GROD`, `LUNI`, `BBER`, `STOL`, `VITR`, `GORO`, `ZHIT`, `BY01`, `BERE`, `NOVP`, `VILE`, `LIOZ`, `MRGO` |
| **vrs** | Yes — `BelarusVRS*`, `AgroVRS` mountpoints flagged solution=1, NMEA=1 (network solution requiring GGA from rover); `NEAR*` mountpoints serve nearest-physical-station correction (solution=0, NMEA=0/1) |
| **Constellations** | GPS+GLO on legacy mountpoints (`BelarusVRS`, `NEAR`, `BelarusDGPS`, `AgroGPS`, `AgroN`); GPS+GLO+GAL+BDS on MSM4/MSM5 mountpoints and most Agro-* mountpoints |
| **RTCM format** | RTCM 3 across all current mountpoints; legacy CMR available on `AgroCMR`; software stack Leica GNSS Spider 7.8.3.9486 |
| **datum_epoch** | Real-time RTK delivered in ITRS, realisation ITRF2005; post-processing RINEX additionally available in ITRS, СК-95, СК-63, or local systems. Declared on operator page https://geo.by/services/sstp/predostavlenie-informatsii-sstp ("ITRS (в реализации ITRF2005) – для режима реального времени"). No epoch publicly stated. |
| **tariff — RTK metered ("Общий")** | 0.24 BYN/min RTK (~$0.085/min, ~$5.07/hr) |
| **tariff — RTK fixed ("Точная навигация") per device/month** | 150.78 BYN/month (~$53.09/month); ~1,809 BYN/yr (~$637/yr) via monthly renewal; no annual flat rate published |
| **tariff — DGPS metered ("Общий")** | 0.06 BYN/min (~$0.021/min) for 0.25–1 m accuracy |
| **tariff — DGPS fixed ("Навигация DGPS") per device/month** | 37.70 BYN/month (~$13.27/month) |
| **tariff — RINEX (post-processing) per file** | 3.63 BYN per 1-hour file from one CORS (~$1.28/file) |
| **tariff — Precision agriculture per-connection ("Точное земледелие")** | Tiered: 1 conn 150.00 / 2–5 conn 135.00 / 6–10 conn 112.50 / 11–25 conn 87.00 / 26–50 conn 81.00 / 51–100 conn 75.00 / 101+ conn 69.00 BYN per connection per month |
| **tariff — Agriculture flat-rate (territorial restriction)** | 700.00 BYN/month or 6,000.00 BYN/year (~$2,113/yr) per device, unlimited connections, limited to Customer's registered land-use parcel(s) |
| **tariff — Educational ("Учебный") plan** | Belarusian state-funded educational institutions only; per-minute rate cell empty in published PDF (gap) |
| **VAT status** | All tariffs explicitly stated "без НДС" (excluding 20% VAT); telecom transmission costs also excluded |
| **Tariff source** | https://geo.by/images/tariffs.pdf — 2-page Russian PDF effective 2023-05-01; HTTP 200, Content-Length 142,832; identical file served 2026-05-15 as in May 2026 (no 2024–2026 revision) |
| **hobbyist_eligibility** | No (effective). The "Общий" plan text covers "неограниченному кругу пользователей", so an individual may sign the public-offer contract on paper, but: (1) no self-service portal; (2) tariff title restricts to residents; (3) sanctions context (below) restricts non-resident access. Cheapest path (RTK fixed) is ~$637/yr — above the project's $200/yr hobbyist cutoff. |
| **legal_residency_required** | Yes — tariff title explicitly limits service to residents of the Republic of Belarus (физических и юридических лиц со статусом резидента); contract execution requires Belarusian banking and tax data |
| **last_confirmed_alive** | 2026-05-15 — direct sourcetable fetch `http://sstp.geo.by:8080/` returned `SOURCETABLE 200 OK`, `Server: GNSS Spider 7.8.3.9486/1.0`, 47 STR records, Content-Length 4,796. IP fallback `http://93.125.21.51:8080/` returned identical sourcetable. `geo.by/services/sstp` and `geo.by/images/tariffs.pdf` both HTTP 200 via nginx/1.22.0 (HTTP→HTTPS 301). Port 8081 connected but returned no body — closed/idle, not a separate caster as of 2026-05-15. |

## Context Notes

- **Network history**: ССТП РБ is the single national CORS network. Belgeodesiya (РУП «Белгеодезия», successor to Белаэрокосмогеодезия) has operated reference stations under the State Committee for Property since the network's inception. Belgeodesiya cites ~98 continuously-operating reference stations with declared horizontal accuracy 1–5 cm RTK and 0.25–1 m DGPS. The public sourcetable exposes 24 physical CORS — the rest are presumably visible only via VRS/NEAR network products.
- **Belarus and EUREF**: Belgeodesiya began uploading GNSS data to EUREF Permanent Network (EPN) analysis centres on 2020-03-01. This is a one-way contribution to academic processing; it does **not** grant access to real-time NTRIP streams from outside Belarus.
- **Sanctions context**: EU Regulation 765/2006 (Belarus sanctions, extended through 2024–2026 packages) and parallel US/UK controls suspend exports of dual-use surveying equipment to Belarus. Topcon, Trimble, and Leica publicly suspended GNSS distribution to Belarus in 2022. Belarusian distributor channels (geotop.by, geoportal.by) sell only non-Western brands (CHCNav, South, Hi-Target, Geomax). Even a Belarus-resident hobbyist faces a constrained rover market on top of the contract-only access model.
- **Access workflow**: (1) download `Публичный договор присоединения` PDF from geo.by; (2) sign and submit the join-agreement (заявление о присоединении) with Belarusian tax/account details; (3) Belgeodesiya issues unique NTRIP credentials for one device per contract; (4) caster `sstp.geo.by:8080` connects with the issued login. No web self-service signup. No published account-portal URL.
- **Tariff PDF reading**: A `0.91 BYN` figure appears in the layout-extraction near Plan 1 "Общий" but is unlabeled in the column structure — unresolved gap, requires direct contact with Belgeodesiya to confirm purpose.
- **Volunteer alternatives — none**: `py scripts/stations_by_country.py BLR` and `py scripts/stations_by_radius.py 53.90 27.57 200` both return zero stations. rtk2go has no confirmed BY-coded bases; Centipede has no BY nodes; NOTA/EarthScope does not cover Belarus. Sanctions, ICANN .by ccTLD restrictions, and the closed contract-only access model mean there is no public-internet hobbyist path to centimetre-level corrections in Belarus.

## Post-Processing (RINEX) Fallback

- **Belgeodesiya RINEX**: 3.63 BYN per 1-hour file from one CORS via signed contract; procedure documented in `geo.by/about/Manual_RINEX.pdf`. Same residency restriction.
- **EUREF EPN archive**: Selected Belarusian stations contributed since 2020-03-01; free download via https://www.epncb.oma.be/ — academic use; daily 30-second RINEX, no real-time stream. This is the only path for non-residents to obtain raw Belarusian GNSS data.

## Nearest cross-border alternative within ~50 km

None. The closest external public RTK options are several hundred km from Belarusian population centres:
- **Poland (ASG-EUPOS)** — paid, EU-resident workflow; nearest CORS ~30–50 km west of Brest at the Belarus border, but RTK service requires a Polish-resident GUGiK account.
- **Lithuania (LitPOS)** — state-run, Lithuanian-resident workflow; nearest CORS near Vilnius is ~35 km from the Belarusian border but RTK service requires NGSS/National Land Service registration.
- **Latvia (LatPos)**, **Russia (regional commercial networks)** — comparable residency/contract barriers; Russia under separate sanctions.

For a Belarus-resident hobbyist, no cross-border free NTRIP exists within useful baseline distance.

## Most Recent Public Announcement (date + URL)

- Tariff PDF effective 2023-05-01 (`https://geo.by/images/tariffs.pdf`) — last published price update; still served unchanged on 2026-05-15 (same Content-Length 142,832 as prior fetches).
- 2020-03-01 onward: continued integration of Belgeodesiya CORS data into EPN analysis centres (BELTA 2020 announcement: https://eng.belta.by/economics/view/belarus-about-to-start-sharing-gnss-data-with-european-network-128634-2020/). No public announcement of new self-service portal, new station deployments, or tariff revision in 2024–2026 review window.

## Sources Consulted

- ССТП РБ services landing page: https://geo.by/services/sstp (observed 2026-05-15)
- ССТП РБ "Предоставление информации сети ПДП" detail page: https://geo.by/services/sstp/predostavlenie-informatsii-sstp (observed 2026-05-15)
- Belgeodesiya tariff PDF: https://geo.by/images/tariffs.pdf (effective 2023-05-01; observed 2026-05-15)
- Belgeodesiya public-offer contract template: https://geo.by/about/public_contract_pred_yclyg_SSTP.pdf
- Belgeodesiya RTK manual: https://geo.by/about/Manual_RTK.pdf
- Belgeodesiya RINEX manual: https://geo.by/about/Manual_RINEX.pdf
- Direct sourcetable fetch: `http://sstp.geo.by:8080/` and `http://93.125.21.51:8080/` (Server: GNSS Spider 7.8.3.9486/1.0; 47 STR; observed 2026-05-15; HTTP 0.9 fallback required)
- State Property Committee profile (English): https://gki.gov.by/en/activity_branches-geomaps-en/
- Belarusian distributor commentary (CORS pricing context): https://geotop.by/news/2082/bezlimitnye-rtk-popravki/
- Geoportal Belarus (rover connection guide): https://geoportal.by/katalog/gps_gnss_priemniki_dlja_geodezii/podklyuchenie-k-seti-bazovyh-stanciy-74/
- State Committee on Property GNSS user guide (PDF): https://nca.by/upload/medialibrary/b65/5vk1ph5lep7lx7ap9fn2lbq9glnn4utf/prilozhenie_2_rukovodstvo_po_ispol_zovaniu_gnss.pdf
- BELTA news (EPN data sharing, 2020): https://eng.belta.by/economics/view/belarus-about-to-start-sharing-gnss-data-with-european-network-128634-2020/
- GPS World coverage of EPN sharing: https://www.gpsworld.com/belarus-to-start-sharing-gnss-data-with-european-network/
- Contact: Belgeodesiya, info@belgeodesy.by, +375 17 334 79 49, 220029, Minsk, Masherova Ave 17

## Known Data Gaps

- **0.91 BYN line item**: Unlabeled in PDF extraction near Plan 1 — confirm purpose with Belgeodesiya support.
- **"Учебный" (Educational) RTK rate**: Per-minute price cell empty in published PDF; not a hobbyist path regardless.
- **Annual RTK flat rate**: None published. Effective annual cost via "Точная навигация" monthly auto-renewal is ~1,809 BYN/yr (~$637/yr per device).
- **Self-service registration**: None. Paper contract only.
- **Datum epoch**: ITRF2005 realisation declared but no explicit reference epoch published.
