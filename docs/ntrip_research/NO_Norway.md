# Norway [NO] — NTRIP RTK Caster Research

## Status: YES — paid government NTRIP caster (CPOS, Kartverket) operating; no free hobbyist tier

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (CPOS — paid) |
| **landing_url** | https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos (operator service guide) |
| **access_url** | https://www.kartverket.no/en/on-land/posisjon/ordering-positioning-services (subscription ordering page) |
| **host:port — CPOS** | `159.162.103.14:2101` |
| **num_stations** | over 280 geodetic stations spread across the entire country — operator citation: Kartverket satellite-and-positioning-data page (2026-05-21), https://proxy.kartverket.no/en/api-and-data/satellite-and-positiong-data. Mainland Norway; Svalbard/Jan Mayen excluded. Sourcetable lists only ~10 network products, not individual stations (primer [stations-vs-mps]). |
| **vrs** | yes — VRS is the primary delivery method; system calculates a virtual reference station near the user's position from 280+ permanent geodetic stations nationwide |
| **tariff — CPOS Standard (Surveying)** | NOK 11,000 /yr excl. VAT (1–3 subscriptions); NOK 8,000 /yr excl. VAT (4th+ subscription) · price list last updated 2024-04-12 (operator declaration: "All prices are per year excluding VAT"), current 2026-05-21 |
| **tariff — Norge Digitalt partner (Standard)** | NOK 10,500 /yr (1–2 subs); NOK 7,000 /yr (3–5); NOK 5,500 /yr (6th+) — discounted partner pricing (`Norge Digitalt` cooperating public bodies) |
| **tariff — CPOS Fast (Fixed Installation)** | NOK 8,000 /yr excl. VAT |
| **tariff — CPOS Landbruk (Agriculture)** | NOK 5,000 /yr excl. VAT |
| **tariff — CPOS Utland (Abroad)** | NOK 5,000 /yr excl. VAT — for existing CPOS customers needing Swedish positioning services; grants SWEPOS access for an existing CPOS subscriber |
| **tariff — CPOS Virksomhet (Enterprise)** | Contact Kartverket — enterprise pricing tier listed on the ordering page; no public price declared |
| **tariff — CPOS Undervisning (Teaching)** | Free — listed as a subscription type on the ordering form (price page does not enumerate it); confirm scope with kundesenter@kartverket.no |
| **tariff — CPOS Forskning (Research)** | Free — ordering-form subscription type; max-term + Research Council prerequisite not on the public ordering page |
| **tariff — CPOS Innovasjon (Innovation)** | Free — ordering-form subscription type; aimed at pre-commercial startups |
| **tariff — CPOS test** | Free 1-month trial; auto-converts to paid subscription unless cancelled before expiry (per ordering page) |
| **tariff — DPOS (legacy DGNSS, RTCM 2.3)** | NOK 2,500 /yr excl. VAT — listed separately on the price page (out of project scope: DGNSS, msg 1/3) |
| **tariff — ETPOS (post-processing)** | NOK 8,000 /yr excl. VAT — listed as its own line on the 2024-04-12 price page; the "included with CPOS" assertion in older drafts is NOT supported by the current price page wording |
| **hobbyist_eligibility** | unclear — no explicit hobbyist tier; subscriptions appear business/organisation-oriented; no explicit block on individuals; 1-month free trial available |
| **legal_residency_required** | unclear — not explicitly stated; billing address required; no residency restriction found in public terms |
| **last_confirmed_alive** | `159.162.103.14:2101` SOURCETABLE 200 OK confirmed 2026-05-21 (curl --http0.9, Trimble Ntrip Caster 4.1; 10 STR rows: CPOSGLONASS, CPOSHREF, CPOSCMR, CPOSFAST, SVALBARD, HREFNN1954, HREFNN2000, CPOSRTCM32, DPOS, CPOSGPS) |
| **datum_epoch** | EUREF89 (horizontal) + NN1954/NN2000 (height) — operator declaration (guide-to-cpos, 2026-05-21): "Correction data is given in RTCM format in official reference frame EUREF89/NN1954/NN2000"; "The service covers mainland Norway." No published epoch on the public page. Citation: https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos |

## Context Notes

- **CPOS** (Continuously Operating Positioning Service): Operated by Kartverket (Norwegian Mapping Authority). ~280 permanent geodetic stations covering mainland Norway. ~5,000 active users. 24/7 operation with weekday monitoring. Coverage is mainland Norway only — Svalbard and Jan Mayen are explicitly excluded (see SJ_Svalbard entry for details).
- **Subscription types**: CPOS Standard is the main commercial offering. CPOS Fast is for fixed/mobile installations (excavators, drones). CPOS Landbruk targets precision agriculture at a lower price point. Drone operators sourced this at ~NOK 7,980 /yr via resellers (e.g., Scandinavian Drone).
- **ETPOS billed separately on the current price page**: NOK 8,000 /yr ex-VAT. Earlier drafts asserting "ETPOS included with any CPOS subscription" do not match the 2024-04-12 price page, which lists ETPOS as its own line item alongside CPOS Standard/Fast/Landbruk/Utland. Treat as separate purchase unless Kartverket confirms otherwise in writing.
- **Nordic interoperability**: CPOS Utland (NOK 5,000/yr excl. VAT) is for existing CPOS customers needing Swedish positioning services — grants SWEPOS access for an existing CPOS subscriber on the same username.
- **No free public tier**: Hobbyists must pay at minimum CPOS Landbruk (NOK 5,000/yr) or use the 1-month free trial. No ongoing free access for private individuals.
- **Volunteer coverage** (`scripts/stations_by_country.py NOR` 2026-05-19): rtk2go = 28 NOR-tagged bases; **Centipede = 23 NOR-tagged bases** (sourcetable 2026-05-19; Centipede has built out densely in Norway since 2025); EUREF-IP = 5 stations (NABG/OSLS/STAS/TRDS/VARS); IGS-IP = 3 (LYR1, NABG, OSL1); AUSCORS rebroadcasts NYA2 (Svalbard); MIRAI rebroadcasts NYA2 + QTRP. Volunteer coverage is now adequate over most populated Norway south of ~64°N; sparser further north but a handful of high-latitude rtk2go nodes exist (e.g. Fauske, SANDNESS, ROMA1).
- **Sourcetable products vs physical CORS**: the CPOS caster exposes 10 network-broadcast mountpoints (CPOSGLONASS, CPOSHREF, CPOSCMR, CPOSFAST, SVALBARD, HREFNN1954, HREFNN2000, CPOSRTCM32, DPOS, CPOSGPS) — each is a NRTK product, not a single physical station. The ~280 physical reference stations are not enumerated in the public sourcetable (primer [stations-vs-mps] — num_stations from operator, not ST row count).
- **`SVALBARD` mountpoint on CPOS**: present in the sourcetable (live-confirmed 2026-05-21); RTCM 3.1, carrier 2 (RTK-capable), lat/lon=0, nmea=1, solution=0 — same VRS/network-product pattern as all other CPOS mountpoints. Kartverket's Guide to CPOS and the public documentation make no mention of Svalbard coverage; the guide explicitly states "mainland Norway" only. The mountpoint likely routes through the Ny-Ålesund geodetic observatory data that Kartverket sells via paid data agreements (see SJ_Svalbard entry) — accessible only to subscribers with a separate commercial data arrangement, not a general CPOS subscription. This does not change the "CPOS mainland-only" conclusion for SJ.
- **Operator contact**: kundesenter@kartverket.no / +47 32 11 80 00

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ETPOS** — post-processing; billed separately per the 2024-04-12 price page | https://www.kartverket.no/en/on-land/posisjon/guide-to-etpos | NOK 8,000 /yr ex-VAT (separate line item on Kartverket price page; not bundled with CPOS) |
| **EUREF Permanent Network** — selected Norwegian CORS (ETRF89) | https://epncb.oma.be/ | Free |

## Sources Consulted
- Kartverket CPOS guide: https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos (confirms VRS-based service)
- Kartverket price list for positioning services: https://www.kartverket.no/en/on-land/posisjon/price-list-for-positioning-services (last updated 2024-04-12; operator declares "All prices are per year excluding VAT"; lists Standard, Fast, Landbruk, Utland, Virksomhet tiers plus Norge Digitalt partner pricing — all NOK, ex-VAT; re-verified 2026-05-21)
- Kartverket satellite and positioning data (station count source): https://proxy.kartverket.no/en/api-and-data/satellite-and-positiong-data (2026-05-21 — "over 280 geodetic stations spread across the entire country")
- Kartverket ordering page: https://www.kartverket.no/en/on-land/posisjon/ordering-positioning-services
- Kartverket user guide: https://www.kartverket.no/en/on-land/posisjon/user-guide-positioning-services
- Kartverket terms of agreement: https://www.kartverket.no/en/on-land/posisjon/terms-of-agreement-regarding-positioning-services
- Scandinavian Drone CPOS subscription listing (~NOK 7,980): https://www.scandinaviandrone.no/produkt/kartverket-cpos-abonnement-for-droner/
- ArduSimple Norway RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-norway/
- curl probe of `159.162.103.14:2101` — SOURCETABLE 200 OK confirmed 2026-05-17 (curl --http0.9; 10 STR rows; Trimble Ntrip Caster 4.1)
- Local pipeline `scripts/stations_by_country.py NOR` (2026-05-19): rtk2go 28, centipede 23, euref_ip 5, igs_ip 3, auscors 1 (NYA2 Ny-Ålesund), mirai 2 (NYA2 + QTRP)
