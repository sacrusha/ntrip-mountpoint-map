# Slovenia [SI] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-13)
**status:** YES — paid national NTRIP (SIGNAL); free for public bodies, students, and civil society (with documentation); individuals can subscribe at €829.44/yr excl. VAT. Strong volunteer mesh: 4 rtk2go + 4 Centipede SI bases.

## SIGNAL — Omrežje SIGNAL

| field | value |
|---|---|
| landing_url | https://gu-signal.si/ |
| access_url | https://gu-signal.si/postopek-registracije/ |
| operator | GURS (Geodetska uprava Republike Slovenije) via Geodetski inštitut Slovenije, Jamova c. 2, 1000 Ljubljana |
| host:port | `178.172.26.131:8080` — live `SOURCETABLE 200 OK` from `NTRIP Trimble Ntrip Caster 5.2`, 113 STR rows, 16,355 bytes, 2026-05-21 |
| vrs | yes — `VRSSLO(2_3)`, `VRSSLO(3_1)`, `VRSCMRp`, `VRSCMRx`, `MULTI(2_3)/(3_1)`, `MULTI_CMRx`, `MacSLO(3_1)` |
| network type | VRS, MAC/MAX (MacSLO), individual station streams, cross-border (KOPR_fvg / AT / HU / HR relays) |
| constellations | GPS+GLO on RTCM 2.3/3.1; GPS+GLO+GAL+BDS on CMRx / MSM streams |
| num_stations | 16 Slovenian CORS (Bovec, Brežice, Celje, Črnomelj, Idrija, Ilirska Bistrica, Koper, Lendava, Ljubljana, Maribor, Nova Gorica, Ptuj, Radovljica, Slovenj Gradec, Trebnje, …) plus cross-border relays in the sourcetable. |
| tariff — flat-rate annual | **€829,44 / year excl. VAT** (billing year 2025-04-01 → 2026-03-31 per registration page WebFetch 2026-05-21; the new 2026-04-01 → 2027-03-31 billing year is now in force but no updated headline figure was published on the pricing page at fetch time — confirm current rate with `gps@gis.si` before subscribing). 25% early-bird discount → €622,08 if contracted before 2025-07-31 + paid in one instalment (window closed for 2025-26 year). |
| tariff — per-minute (RTCM) | €0,12 / connected minute excl. VAT; quarterly billing (monthly if invoice > €25) |
| tariff — RINEX commercial | €0,26 / s server-processing time (≈ €4,21 / h of RINEX data) |
| tariff — TOP commercial (static / rapid-static) | €0,26 / s server-processing time |
| tariff — public bodies / RTCM Non-Commercial | **Free** (documentation to `gps@gis.si` within 1 week of registration) |
| tariff — students / civil society | **Free** with institutional verification |
| VAT | Slovenian standard 22%; prices above excl. VAT |
| hobbyist_eligibility | yes — natural persons (fizična oseba) may register; no professional licence required |
| legal_residency_required | ? — no explicit restriction for non-Slovenian EU users; registration requires postal mail of signed contract (4 copies) to Geodetski inštitut Slovenije |
| last_confirmed_alive | 2026-05-21 — `178.172.26.131:8080` SOURCETABLE 200 OK, Trimble Ntrip Caster 5.2, 113 STR rows |
| datum_epoch | omitted — SIGNAL operator portal (gu-signal.si registration and services pages, WebFetch 2026-05-21) contains no frame/epoch declaration. D96/TM is Slovenia's official CRS (ETRS89 national realization, mean EUREF campaign epoch 1995.55 rounded to "1996"), but the primer's citation rule requires an operator portal/spec/decree URL — none found on SIGNAL pages. No state gazette URL found that pins the broadcast epoch for SIGNAL streams. Gap noted explicitly; confirm with `gps@gis.si` or GURS technical documentation if epoch matters for your application. |

## Context

- Sourcetable (113 STR records, 2026-05-21 probe) includes network products (`VRSSLO 2.3 / 3.1`, `VRSCMRp`, `VRSCMRx`, `MULTI 2_3`, `MULTI 3_1`, `MULTI_CMRx`, `MacSLO(3_1)`) plus individual SI station streams (e.g. `GSR1(2_3)` Ljubljana, `MRBR(2_3)` Maribor, `BOVC(2_3)` Bovec, `KOPR(2_3)` Koper) and cross-border streams (`KOPR_fvg`, etc.).
- RTCM formats: 2.3 (GPS), 3.1 (GPS+GLO), 3.2 MSM5/MSM7 (multi-constellation), CMR+, CMRx.
- Registration: complete online form → receive contract by email → sign 4 copies → post to Geodetski inštitut Slovenije → receive credentials by email (~2 business days).
- Non-commercial eligibility (public administration, students, civil societies serving public interest) requires supporting documentation to `gps@gis.si` within one week of application.
- The SIGNAL portal (gu-signal.si) is in Slovenian; English support via 01 200 29 29 or `gps@gis.si`.
- Tariff page re-fetched 2026-05-21: wording unchanged from 2025-04 schedule. The new 2026-04 → 2027-03 billing year is in force from the operator side but the public pricing page had not propagated a new headline figure at fetch time.

## Volunteer supplement (2026-05-21)

- **rtk2go** (`SVN` country): 4 bases — `FRELIH` (Krize, 46.34 N 14.30 E), `Kmetija-Budic` (Brežice, 45.87 N 15.65 E), `Lukez` (Črnomelj, 45.58 N 15.19 E), `MarkovciRTK` (Markovci, 46.39 N 15.93 E). All RTCM 3.2-3.3 with multi-constellation MSM.
- **Centipede** (`SVN`): 4 operator-tagged SVN entries — `MAKO` (46.387 N 15.543 E), `OUCE` (46.680 N 16.139 E), `PRIME` (46.375 N 15.778 E), and `SIPOS` (45.563 N 20.704 E — operator-tagged SVN but coordinates place it in Vojvodina, Serbia; see `RS_Serbia.md`). **3 usable Centipede bases within Slovenia; SIPOS is geographically mis-tagged.**
- Useful complementary coverage in eastern + south-eastern Slovenia, but SIGNAL remains the primary RTK source with national-VRS coverage.

## Post-processing fallback

| Service | URL | Cost |
|---|---|---|
| SIGNAL RINEX / post-processing | https://gu-signal.si/ | €0,26/s server time (≈ €4,21/h of data); free for public bodies |
| SIGNAL open data (OPSI) | https://podatki.gov.si/dataset/podatki-omrezja-signal | free (historic GNSS observations) |

## Sources

- GURS SIGNAL portal: https://gu-signal.si/
- SIGNAL NTRIP access page: https://gu-signal.si/dostop-do-ntrip-streznika/ (IP 178.172.26.131, port 8080)
- SIGNAL RTK mountpoints: https://gu-signal.si/rtk-dostopne-tocke-in-stevilke/
- SIGNAL registration + pricing: https://gu-signal.si/postopek-registracije/ (WebFetch 2026-05-21 — €829,44 / 622,08 / 0,12 €/min / 0,26 €/s confirmed)
- Live caster: `curl --http0.9 http://178.172.26.131:8080/` → SOURCETABLE 200 OK, Trimble Ntrip Caster 5.2, 113 STR (2026-05-21)
- Local: `data/centipede.sourcetable` 2026-05-21 (4 SVN); `data/rtk2go.sourcetable` 2026-05-21 (4 SVN); `py scripts/stations_by_country.py SVN` → 4 + 4 = 8
