# Russia [RU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-02
**Exchange rate used:** ~85 RUB / 1 USD (approximate spot rate, 2026-05-02)

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
| **host:port** | `ntrip.eftgroup.ru:2101` |
| **portal** | https://www.eft-cors.ru; billing: bp.eft-cors.ru |
| **coverage** | Russia-wide |
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
| **host:port** | `geo-spider.net:2101` |
| **portal** | https://geospider.ru |
| **coverage** | Saint Petersburg, Moscow, Leningrad, Novgorod, Pskov, Tver, Vologda oblasts + expanding; 200+ stations |
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
| **host:port** | `94.250.250.43:2101` (also `cors.rtknet.ru:2101`; additional regional ports 6030–6041 for RTCM32-MSM streams) |
| **portal** | https://rtknet.ru |
| **coverage** | Russia-wide |
| **tariff** | "Сутки" until end of next day: ₽400 · 1 mo: ₽4,000 · 3 mo: ₽10,000 · 6 mo: ₽18,000 · 12 mo: ₽30,000 (source: rtknet.ru/выбор-тарифного-плана/, observed 2026-05-02); VAT inclusion not stated on pricing page — gap, confirm with msk@geodetika.ru |
| **free trial** | 3-day trial for new users (contact msk@geodetika.ru or 8 800 600-38-77) |
| **hobbyist_eligibility** | Yes — self-service registration; user agreement is a standard public offer (договор-оферта) |
| **legal_residency_required** | Unclear — Russia-wide coverage; Yandex Pay and bank transfer payment; no explicit residency restriction stated |
| **last_confirmed_alive** | 2026-05-02 — site active, news posted 2026-04-15, new base stations being added |

## Operator 4 — HIVE (Индустриальные геодезические системы / Geosystems.aero)

| Field | Value |
|---|---|
| **host:port** | `hive.geosystems.aero:2101` |
| **portal** | https://hive.geosystems.aero |
| **coverage** | 742 stations across 79 Russian regions (station-owner contributed; no VRS computation layer — single-baseline RTK per station) |
| **tariff** | Per-station, per-day model; first 100 KB (~5 minutes) free per connection day; per-day and per-hour RINEX prices are station-specific and visible only after login on the map. Account management plans: "Спутник" (individual, no fixed monthly fee) · "Шаттл" (small company) · "Энтерпрайз 750/1500" (₽750–₽1,500/mo per employee for monitoring features). Actual RTK data cost is not publicly listed. (source: hive.geosystems.aero/pricing, observed 2026-05-02) |
| **hobbyist_eligibility** | Yes — "Спутник" plan for individuals; email + password registration; no licence required |
| **legal_residency_required** | No / Unclear — accepts VISA/MC; no explicit residency requirement; de facto Russia-focused |
| **last_confirmed_alive** | 2026-05-02 — landing page, 742-station map, and forum (forum.geosystems.aero) all live |

## Summary Table

| Operator | host:port | Cheapest daily RTK (incl. VAT) | Monthly RTK (incl. VAT) | Annual RTK (incl. VAT) | Hobbyist OK? | Last alive |
|---|---|---|---|---|---|---|
| EFT CORS | `ntrip.eftgroup.ru:2101` | ₽420 (~$4.94) | ₽5,250 (~$61.76) | ₽50,400 (~$593) | Yes | 2026-05-02 |
| GeoSpider | `geo-spider.net:2101` | ₽315 (~$3.71, until midnight) | ₽5,250 (~$61.76) | ₽44,100 (~$519, 30% off) | Yes | 2026-05-02 |
| RTKNet | `94.250.250.43:2101` | ₽400 (~$4.71, until next midnight) | ₽4,000 (~$47.06) | ₽30,000 (~$353) | Yes | 2026-05-02 |
| HIVE | `hive.geosystems.aero:2101` | Per-station (not public) | Per-station (not public) | Per-station (not public) | Yes | 2026-05-02 |

## Known Data Gaps
- **RTKNet VAT:** Pricing page does not state whether prices include or exclude 5% VAT. Confirm: msk@geodetika.ru / 8 800 600-38-77.
- **HIVE per-station prices:** Only visible after login on the map. Contact: support@geosystems.aero.
- **GeoSpider sourcetable:** `geo-spider.net:2101` confirmed via third-party guides and AI Overview but not directly curl-verified. Confirm via geospider.ru/instructions PDF or s@geospider.ru.

## Sources Consulted
- EFT CORS prices: https://www.eft-cors.ru/prices (observed 2026-05-02)
- GeoSpider tariff: https://geospider.ru/tarif (observed 2026-05-02)
- RTKNet tariff: https://rtknet.ru/выбор-тарифного-плана/ (observed 2026-05-02)
- RTKNet official parameters guide: rtknet.ru/pdf/spravka-rtknet.pdf
- HIVE pricing: https://hive.geosystems.aero/pricing (observed 2026-05-02)
- HIVE NTRIP setup forum: forum.geosystems.aero/t/nastrojki-ntrip/1233
