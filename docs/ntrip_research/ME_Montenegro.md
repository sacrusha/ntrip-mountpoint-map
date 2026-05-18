# Montenegro [ME] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-17 — no EUR tariff in open web; 2024-04-11 PDF still latest)

## Status: YES — government NTRIP caster operating (MONTEPOS); endpoint not public; paid subscription

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government-operated) |
| **Network name** | MontePos — Mreža Stalnih GNSS Stanica Crne Gore |
| **Operator** | Uprava za nekretnine (Real Estate Administration), Vlada Crne Gore (Government of Montenegro) |
| **Admin contact** | Goran Popović, dipl.inž.geod., Načelnik odsjeka za geodetske radove i državnu granicu — Tel: +382 67 641 119 — Email: uznmontepos@gmail.com |
| **access_url** | https://www.gov.me/clanak/montepos — MontePos operator signup/info page (application form + giro-account payment instructions; endpoint disclosed after sign-up) |
| **num_stations** | 9 |
| **host:port** | Null — not published on any public-facing page. NTRIP endpoint is disclosed after submitting signed application form and payment. |
| **vrs** | ? |
| **tariff** | Null — tariff figures exist in PDF at `https://wapi.gov.me/download/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0?version=1.0` (published 2024-04-11, "MontePos- tehnički detalji", 382 KB) but domain wapi.gov.me was not accessible from research environment. Subscription periods confirmed: 24h, 48h, 1 month, 3 months, 6 months, 1 year, 2 years. Currency: EUR (Montenegro uses EUR). |
| **Payment process** | Payment to giro account 832-1081-58, purpose field "Montepos - RTK"; submit signed application form to uznmontepos@gmail.com or at Uprava za nekretnine counter offices |
| **Application form** | https://wapi.gov.me/download/3647961e-34ab-41e7-9bf6-282a116f72ff?version=1.0 (394 KB, published 2024-04-11) |
| **Service modules** | MontePos–RTK (Real-Time Kinematic) and MontePos–PPK (Post-Processed Kinematic). Established 2005; published 2–3 cm RTK accuracy. |
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
- MONTEPOS public page: https://www.gov.me/clanak/montepos (observed 2026-04-30; re-verified URL pattern 2026-05-12)
- Real Estate Administration: https://www.uzn.me/ (TLS/connection error from sandbox 2026-05-12 — cited in third-party sources as the canonical MontePos pricing host)
- gov.me site news (latest entry up to 2026-03; page publication 2024-04-11)
- Tariff PDF "MontePos- tehnički detalji" (WebFetch timeout 2026-05-12; remains the authoritative tariff document): https://wapi.gov.me/download/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0?version=1.0  · mirror: https://www.gov.me/dokumenta/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0
- Application form PDF: https://wapi.gov.me/download/3647961e-34ab-41e7-9bf6-282a116f72ff?version=1.0
- Community summary (2026-05-12 search): MontePos established 2005; offers RTK + PPK modules; 2–3 cm accuracy
- Contact: uznmontepos@gmail.com / +382 67 641 119
- py scripts/stations_by_radius.py 42.5 19.3 250 (2026-05-12) — zero rtk2go/Centipede/EarthScope volunteer stations within 250 km of Podgorica (no cross-border free alternative)
- 2026-05-17 WebFetch of gov.me/clanak/montepos — page still dated 2024-04-11; no EUR figures inline; subscription periods still 24h / 48h / 1m / 3m / 6m / 1y / 2y; tariff numbers remain in the wapi.gov.me PDF (not parsed from sandbox)
