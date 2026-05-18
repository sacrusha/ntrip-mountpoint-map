# Russia [RU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-12)
**Exchange rate used:** ~85 RUB / 1 USD (approximate spot, 2026-05-02; not re-checked)

## Status: YES — multiple commercial NTRIP casters operating nationally

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — multiple operators |
| **Operators confirmed** | EFT CORS · GeoSpider · RTKNet · HIVE |
| **hobbyist_eligibility** | Yes for all four — individual registration without company licence |
| **legal_residency_required** | Unclear for all — no explicit residency ban stated; payment infrastructure and coverage are Russia-focused |
| **VAT rate** | 5% (confirmed by EFT CORS and GeoSpider; RTKNet not stated on pricing page) |

## Operator 1 — EFT CORS (ООО ЕФТ Груп)

| Field | Value |
|---|---|
| **landing_url** | `https://www.eft-cors.ru/` — operator-owned EFT CORS service landing (RU). Describes the network, stations, services. |
| **access_url** | `https://www.eft-cors.ru/prices` — full tariff schedule (RTK, RTK+, RTK for EFT hardware, RINEX) with VAT-inclusive prices. More useful than landing for sign-up decision. `bp.eft-cors.ru/register` is the bare billing-portal registration form, not a service description page. |
| **host:port** | `ntrip.eftgroup.ru:2101` — sandbox curl REFUSED 2026-05-17 (egress block; service marketed as 24/7 per operator portal) |
| **portal** | https://www.eft-cors.ru; billing: bp.eft-cors.ru |
| **coverage** | 800+ base stations across 85 Russian regions (operator-stated, eft-cors.ru landing 2026-05-17); 15,000+ active users claimed. Stations include EFT-brand hardware + 24h backup power + redundant comms. |
| **datum_epoch** | omitted -- no citable operator declaration |
| **tariff — RTK standard (non-EFT hardware, incl. 5% VAT)** | 3-day trial: free · 1 day: ₽420 · 2 days: ₽735 · 1 mo: ₽5,250 · 3 mo: ₽14,175 · 6 mo: ₽26,775 · 12 mo: ₽50,400 (source: eft-cors.ru/prices, observed 2026-05-02) |
| **tariff — RTK+ enhanced (non-EFT hardware, incl. 5% VAT)** | 3-day trial: free · 1 mo: ₽6,300 · 3 mo: ₽17,010 · 6 mo: ₽32,130 · 12 mo: ₽60,480 |
| **tariff — RTK for EFT hardware (incl. 5% VAT)** | 1 mo: ₽3,150 · 3 mo: ₽8,505 · 6 mo: ₽16,065 · 12 mo: ₽30,240 |
| **tariff — RINEX extended (incl. 5% VAT)** | Basic 30 s intervals: free · 1 day: ₽250 · 1 wk: ₽500 · 1 mo: ₽1,000 · 3 mo: ₽2,700 · 6 mo: ₽4,800 · 12 mo: ₽8,400 |
| **hobbyist_eligibility** | Yes — email-only registration; no company required |
| **legal_residency_required** | Unclear — no explicit restriction; payment primarily Russian cards/WebMoney/Qiwi |
| **last_confirmed_alive** | 2026-05-02 — site fully loaded, © 2026 footer, registration/login active |

Note: Original domain `eftcors.ru` has an SSL certificate error; active service operates via `ntrip.eftgroup.ru`.

## Operator 2 — GeoSpider / ГЕОСПАЙДЕР (ООО "НПП "ГЕОМАТИК")

| Field | Value |
|---|---|
| **host:port** | `geo-spider.net:2101` — sandbox DNS `Could not resolve host` 2026-05-17 (likely IP-only or filtered) |
| **portal** | https://geospider.ru |
| **coverage** | Saint Petersburg, Moscow, Leningrad, Novgorod, Pskov, Tver, Vologda oblasts + Karelia, Smolensk; 200+ stations |
| **datum_epoch** | omitted -- no citable operator declaration |
| **tariff — RTK МСК (incl. 5% VAT)** | 1 day (until midnight): ₽315 · 1 calendar day: ₽525 · 7 days: ₽2,100 · 14 days: ₽3,150 · 1 mo: ₽5,250 · 3 mo: ₽14,175 (10% off) · 6 mo: ₽25,200 (20% off) · 1 yr: ₽44,100 (30% off) · 2 yr: ₽75,600 (40% off) · 3 yr: ₽103,950 (45% off) · 4 yr: ₽126,000 (50% off) (source: geospider.ru/tarif, observed 2026-05-02) |
| **tariff — RINEX standard (incl. 5% VAT)** | 1 day: ₽525 · 7 days: ₽1,050 · 14 days: ₽1,575 · 1 mo: ₽2,100 · 3 mo: ₽5,670 (10% off) · 6 mo: ₽10,080 (20% off) · 1 yr: ₽17,640 (30% off) · 2 yr: ₽30,240 (40% off) |
| **tariff — RINEX high-frequency (per day, incl. 5% VAT)** | 1 Hz: ₽210 · 2 Hz: ₽525 · 5 Hz: ₽1,050 · 10 Hz: ₽2,100 · 20 Hz: ₽3,150 · 50 Hz: ₽5,250 |
| **hobbyist_eligibility** | Yes — individual sign-up without company registration; form collects name, email, phone, rover brand |
| **legal_residency_required** | Unclear — coverage and payment are Russia-specific; no explicit restriction |
| **last_confirmed_alive** | 2026-05-02 — site fully loaded, tariff page current, active promotions visible |

Note: A 6-month RINEX figure of ₽1,080 appears on one part of the tariff page; ₽10,080 is mathematically correct (20% off ₽12,600) and should be treated as authoritative.

## Operator 3 — RTKNet (ООО "ГЕОДЕТИКА" / Geodetika)

| Field | Value |
|---|---|
| **landing_url** | `https://rtknet.ru/` — operator-owned RTKNet landing (RU). Describes the network, regional coverage, stations. Not a bare login. |
| **access_url** | `https://rtknet.ru/выбор-тарифного-плана/` — tariff page with all subscription tiers (day/month/3/6/12 mo). More useful than landing for sign-up. |
| **host:port** | `cors.rtknet.ru:2101` (also IP 94.250.250.43; regional ports 6030–6041 for RTCM32-MSM streams) — `curl -A 'NTRIP/1.0' --max-time 8 http://cors.rtknet.ru:2101/` 2026-05-17 returned SOURCETABLE 200 OK, server header `EagleGnss-basic/200826`, ~19 STR records (mountpoint names include regional RTCM32-MSM streams; ENDSOURCETABLE terminator present). |
| **portal** | https://rtknet.ru |
| **coverage** | Russia-wide; news 2026-05-13 added EFRE (Yefremov, Tula); 2026 additions: Tolyatti, Shakhovskaya (Moscow region, Apr 2026), Voznesenskoye (Arkhangelsk, Mar 2026), Pskov (Jan 2026), Rylsk (Kursk) |
| **tariff** | "Сутки" until end of next day: ₽400 · 1 mo: ₽4,000 · 3 mo: ₽10,000 · 6 mo: ₽18,000 · 12 mo: ₽30,000 (source: rtknet.ru/выбор-тарифного-плана/, observed 2026-05-17); VAT NOT stated on pricing page (gap; confirm via msk@geodetika.ru) |
| **free trial** | 3-day trial for new users; also free network access bundled when buying RTK receiver from Geodetika; referral program = 2nd free year |
| **datum_epoch** | omitted -- no citable operator declaration |
| **hobbyist_eligibility** | Yes — self-service registration; user agreement = public offer (договор-оферта) |
| **legal_residency_required** | Unclear — Russia-wide coverage; Yandex Pay + bank transfer; no explicit residency restriction |
| **last_confirmed_alive** | 2026-05-17 — `cors.rtknet.ru:2101` SOURCETABLE responds (EagleGnss-basic/200826); news 2026-05-13 EFRE station added |

## Operator 4 — HIVE (Индустриальные геодезические системы / Geosystems.aero)

| Field | Value |
|---|---|
| **host:port** | `hive.geosystems.aero:2101` — sandbox curl REFUSED 2026-05-17 (egress block; portal HTTP 200 alive) |
| **portal** | https://hive.geosystems.aero |
| **coverage** | **386 stations across 61 Russian regions** (station-owner contributed; no VRS computation layer — single-baseline RTK per station). Per landing page 2026-05-17 (unchanged from 2026-05-12): 386 / 61 / 78,198 RTK-hours / 20,015 RINEX orders. See Known Data Gaps for the historical 742-figure context. |
| **tariff** | Per-station, per-day model; first 100 KB (~5 min) free per connection day; per-day/hour RINEX prices station-specific, visible only after login on map. Account plans: "Спутник" (individual, no monthly fee) · "Шаттл" (small co) · "Энтерпрайз 750/1500" (₽750–1,500/mo per employee). Actual RTK data cost not publicly listed. (source: hive.geosystems.aero/pricing, observed 2026-05-02) |
| **datum_epoch** | omitted -- no citable operator declaration |
| **hobbyist_eligibility** | Yes — "Спутник" plan; email + password registration; no licence required |
| **legal_residency_required** | No / Unclear — accepts VISA/MC; no explicit residency requirement; de facto Russia-focused |
| **last_confirmed_alive** | 2026-05-17 — landing page live, same 386 / 61 figure |

## Summary Table

| Operator | host:port | Cheapest daily RTK (incl. VAT) | Monthly RTK (incl. VAT) | Annual RTK (incl. VAT) | Hobbyist OK? | Last alive |
|---|---|---|---|---|---|---|
| EFT CORS | `ntrip.eftgroup.ru:2101` | ₽420 (~$4.94) | ₽5,250 (~$61.76) | ₽50,400 (~$593) | Yes | 2026-05-17 (portal) |
| GeoSpider | `geo-spider.net:2101` | ₽315 (~$3.71, until midnight) | ₽5,250 (~$61.76) | ₽44,100 (~$519, 30% off) | Yes | 2026-05-17 (portal) |
| RTKNet | `cors.rtknet.ru:2101` | ₽400 (~$4.71, until next midnight) | ₽4,000 (~$47.06) | ₽30,000 (~$353) | Yes | 2026-05-17 (ST OK) |
| HIVE | `hive.geosystems.aero:2101` | Per-station (not public) | Per-station (not public) | Per-station (not public) | Yes | 2026-05-17 (portal) |

## Known Data Gaps
- **RTKNet VAT:** Pricing page does not state include/exclude 5% VAT. Confirm: msk@geodetika.ru / 8 800 600-38-77.
- **HIVE per-station prices:** Only visible after login on map. Contact: support@geosystems.aero.
- **HIVE station count drop (742 → 386):** Unexplained between 2026-05-02 and 2026-05-17. Possible causes: counter reset, station-owner departures, counting-method change. Verify with support@geosystems.aero.
- **GeoSpider sourcetable:** `geo-spider.net` DNS not resolvable from sandbox 2026-05-17. Confirm via geospider.ru/instructions PDF or s@geospider.ru.
- **GeoSpider station count:** "200+" landing-page text; no exact published figure.
- **EFT-CORS station count:** Operator landing page states "800+ base stations" 2026-05-17 (vs. no count in prior file). Verify with info@eft-cors.ru.
- **Datum/epoch for all 4 RU casters:** No operator-side declaration on portals checked 2026-05-17 — `omitted` per citation rule. Russia historically uses GSK-2011 / SK-42 / SK-95 / PZ-90.11 but no operator URL cites these for RTK output frame.

## Sources Consulted
- EFT CORS prices: https://www.eft-cors.ru/prices (observed 2026-05-02)
- GeoSpider tariff: https://geospider.ru/tarif (observed 2026-05-02)
- RTKNet tariff: https://rtknet.ru/выбор-тарифного-плана/ (observed 2026-05-02)
- RTKNet official parameters guide: rtknet.ru/pdf/spravka-rtknet.pdf
- HIVE pricing: https://hive.geosystems.aero/pricing (observed 2026-05-02)
- HIVE NTRIP setup forum: forum.geosystems.aero/t/nastrojki-ntrip/1233
- HIVE landing (EN): https://hive.geosystems.aero/landing?locale=en (2026-05-17: 386 stations / 61 regions / 78,198 RTK hours / 20,015 RINEX orders — UNCHANGED from 2026-05-12)
- EFT CORS landing https://www.eft-cors.ru/ (2026-05-17): claims "800+ base stations", "15,000+ users", "85 regions" coverage
- RTKNet 2026-05-17 — latest news 13 May 2026 (EFRE Yefremov Tula station)
- RTKNet curl probe `cors.rtknet.ru:2101` 2026-05-17: SOURCETABLE 200 OK (EagleGnss-basic/200826, ~19 STR records)
- EFT-CORS curl `ntrip.eftgroup.ru:2101` 2026-05-17: connection REFUSED (sandbox egress block; portal alive)
- HIVE curl `hive.geosystems.aero:2101` 2026-05-17: connection REFUSED (sandbox egress block)
- GeoSpider DNS `geo-spider.net` 2026-05-17: not resolved from sandbox
- Local `scripts/stations_by_country.py RUS` (2026-05-17): 1 mirai-mirrored station KZN2 (Kazan)
