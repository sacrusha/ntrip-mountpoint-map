# Montenegro [ME] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — government NTRIP caster operating (MONTEPOS); endpoint not public; paid subscription

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government-operated) |
| **Network name** | MontePos — Mreža Stalnih GNSS Stanica Crne Gore |
| **Operator** | Uprava za nekretnine (Real Estate Administration), Vlada Crne Gore (Government of Montenegro) |
| **Admin contact** | Goran Popović, dipl.inž.geod., Načelnik odsjeka za geodetske radove i državnu granicu — Tel: +382 67 641 119 — Email: uznmontepos@gmail.com |
| **Network size** | 9 CORS stations across Montenegro |
| **host:port** | Null — not published on any public-facing page. NTRIP endpoint is disclosed after submitting signed application form and payment. |
| **VRS** | Not confirmed from public sources |
| **tariff** | Null — tariff figures exist in PDF at `https://wapi.gov.me/download/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0?version=1.0` (published 2024-04-11, "MontePos- tehnički detalji", 382 KB) but domain wapi.gov.me was not accessible from research environment. Subscription periods confirmed: 24h, 48h, 1 month, 3 months, 6 months, 1 year, 2 years. Currency: EUR (Montenegro uses EUR). |
| **Payment process** | Payment to giro account 832-1081-58, purpose field "Montepos - RTK"; submit signed application form to uznmontepos@gmail.com or at Uprava za nekretnine counter offices |
| **Application form** | https://wapi.gov.me/download/3647961e-34ab-41e7-9bf6-282a116f72ff?version=1.0 (394 KB, published 2024-04-11) |
| **hobbyist_eligibility** | Yes (likely) — no professional licence requirement mentioned anywhere on the public page; application/form system appears open to natural persons |
| **legal_residency_required** | Unclear — no residency restriction stated explicitly; giro account payment system and in-person counter option suggest it is designed for residents; no explicit exclusion of non-residents |
| **last_confirmed_alive** | 2026-04-30 (gov.me/clanak/montepos loaded normally; page publication date 2024-04-11; site news up to 2026-03; NTRIP caster endpoint unknown for independent verification) |

## Context Notes

- **MONTEPOS** endpoint is not published. Users must submit a signed application form (PDF) and make payment to a giro account, after which the NTRIP hostname/IP and credentials are disclosed. This is a common pattern for Balkan government CORS networks.
- **Technical details**: The PDF document "MontePos- tehnički detalji" (382 KB, 2024-04-11) is described as containing both the full technical details and the price list ("zahtjev sa cjenovnikom"). This is the authoritative tariff source but was inaccessible from the research environment.
- **To obtain tariff and endpoint**: Contact Goran Popović at uznmontepos@gmail.com or +382 67 641 119, or attempt to download the PDF directly from wapi.gov.me.
- **No free tier**: No free or open-access NTRIP stream documented for Montenegro.

## Most Recent Official Document

"MontePos- tehnički detalji" PDF published 2024-04-11 — contains technical parameters, tariff schedule, and application form:
- Technical details + price list: https://wapi.gov.me/download/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0?version=1.0
- Application form ("Zahtjev za MontePos"): https://wapi.gov.me/download/3647961e-34ab-41e7-9bf6-282a116f72ff?version=1.0

## Sources Consulted
- MONTEPOS public page: https://www.gov.me/clanak/montepos (observed 2026-04-30)
- gov.me site news (latest entry up to 2026-03; page publication 2024-04-11)
- Tariff PDF (inaccessible from research env): https://wapi.gov.me/download/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0?version=1.0
- Contact: uznmontepos@gmail.com / +382 67 641 119
