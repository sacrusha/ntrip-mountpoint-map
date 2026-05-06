# Slovakia [SK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — national government NTRIP caster operating (SKPOS); paid subscription

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | SKPOS (Slovak Real-Time Positioning Service) |
| **Operator** | Geodetický a kartografický ústav Bratislava (GKÚ Bratislava) / ÚGKK SR |
| **Mandate basis** | Act 215/1995 + ÚGKK SR Regulation 300/2009 |
| **host:port** | `skpos.gku.sk:2101` (old IP active until 2026-06-30 per April 2026 notice; IP not disclosed in public docs) |
| **VRS** | Yes (phase corrections / VRS RTK; 2–4 cm accuracy) |
| **tariff — RTK 1 month (1 device)** | €25 (~$28 USD) |
| **tariff — RTK 1 year (1 device)** | €70 (~$79 USD); includes 50 h RINEX |
| **tariff — RTK 1 year (2 devices/SIMs)** | €140 (~$158 USD) |
| **tariff — DGNSS 1 year (1 device)** | €25 (~$28 USD); includes 50 h RINEX; code corrections, 0.3–1 m accuracy |
| **tariff — Post-processing RINEX (per hour)** | €3.00 base + €0.07/hr |
| **tariff — Post-processing RINEX (bulk)** | €70 / 1,000 hr/year |
| **VAT status** | Not explicitly labelled on public-facing pages; GKÚ Bratislava is a public state institution (príspevková organizácia); charges set by ÚGKK SR price order; historically treated as fees net of VAT for B2B invoicing — not stated explicitly |
| **hobbyist_eligibility** | Yes — registration form explicitly offers account type "Fyzická osoba bez živnostenského listu" (Natural person without trade/business licence) as the first option in the user-type dropdown; no professional registration required |
| **legal_residency_required** | No — registration country list includes virtually every UN member state; no restriction to Slovak residents; state organisations/municipalities get free access under Act 145/1995, but paid individual access is internationally open |
| **last_confirmed_alive** | 2026-04-30 (skpos.gku.sk loaded normally; registration portal functional; most recent news entry dated 2026-04-23: "List of supported antennas for SKPOS Online Postprocessing") |

## Context Notes

- **SKPOS** (`skpos.gku.sk:2101`): Long-running national geodetic service operated by the Slovak national mapping authority. Offers both real-time RTK/VRS corrections and post-processing RINEX download from the same subscription.
- **2022 price revision**: Site news dated 2022-12-22 states "due to increased operating costs, there were price adjustments on 22/12/2022." The tariff above reflects post-revision prices. The pre-2022 GKÚ Cenník PDF (č.j. 2–124/2014, valid from 1 May 2014) is obsolete.
- **IP migration**: An April 2026 news notice on the site states the old IP address will remain active until 2026-06-30 during a transition; the hostname `skpos.gku.sk` is the authoritative address going forward.
- **Free access**: State organisations and municipalities receive free access under a separate legal provision; individual/commercial paid access is open internationally.

## Post-Processing (RINEX) Fallback

Included within SKPOS subscription (50 h RINEX included with RTK or DGNSS annual plans). Additional RINEX beyond the included hours: €3.00 base + €0.07/hr, or bulk 1,000 hr/year for €70.

## Sources Consulted
- SKPOS English service-description page: https://skpos.gku.sk/en/o-skpos.php (product table, "Price" column; observed 2026-04-30)
- SKPOS registration portal: https://skpos.gku.sk/register/ (order form, service selection dropdown; observed 2026-04-30)
- Site news: skpos.gku.sk (2026-04-23 and 2022-12-22 notices)
