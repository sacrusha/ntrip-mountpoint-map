# Philippines [PH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — national government NTRIP caster operating (PAGeNet); paid subscription

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | PAGeNet (Philippine Active Geodetic Network) |
| **Operator** | NAMRIA — National Mapping and Resource Information Authority |
| **host:port** | `pagenet.namria.gov.ph:2101` (port 2101 inferred standard NTRIP; exact port disclosed post-subscription per RTK Connection Guide) |
| **VRS** | Not confirmed from public sources; network RTK implied |
| **tariff — One-time registration** | PHP 1,000 per client (~$17.7 USD @ 56.5 PHP/USD) |
| **tariff — Per-hour RTK** | PHP 100.00 / hr / rover (~$1.77/hr) |
| **tariff — 1-day unlimited RTK** | PHP 1,000 (+ PHP 500 per extra rover) (~$17.7) |
| **tariff — 5-day unlimited RTK** | PHP 3,500 (~$61.9) |
| **tariff — 15-day unlimited RTK** | PHP 7,500 (~$132.7) |
| **tariff — 1-month unlimited RTK** | PHP 12,000 (~$212.4) |
| **tariff — RINEX 1–20 sec** | PHP 50/MB |
| **tariff — RINEX 30–60 sec** | Free (included with subscription) |
| **tariff — Coordinate computation** | Free |
| **VAT** | No VAT applicable — government regulatory charges, not sales transactions |
| **hobbyist_eligibility** | Yes — registration open to individuals; online form; no surveying company licence required per FAQ |
| **legal_residency_required** | Unclear — no explicit nationality/residency restriction stated; however, payment for non-Metro Manila clients requires Philippine bank deposit (LandBank), which may be a practical barrier for foreigners. Contact pagenet@namria.gov.ph to clarify. |
| **last_confirmed_alive** | 2026-04-30 (portal homepage and Services & Fees page fully loaded; service described as 24/7 operational; last news post April 2023) |

## Context Notes

- **PAGeNet** (`pagenet.namria.gov.ph`): Operated by NAMRIA, a government agency under the Department of Environment and Natural Resources. The NTRIP caster hostname is confirmed from NAMRIA FOI inventory listing and an archived UNOOSA presentation; the exact connection details (mountpoints, confirmed port) are provided after subscription.
- **Payment**: Non-Metro Manila clients can pay via deposit slip to a LandBank account, making the service nationally accessible. Contact: pagenet@namria.gov.ph / (632) 8884-2849.
- **Tariff source**: Full schedule published at `pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx`, observed 2026-04-30.
- **Service uptime**: Described as 24/7 operational on the portal; most recent news post dated April 2023 but fees page is current.

## Post-Processing (RINEX) Fallback

| Service | Cost |
|---|---|
| RINEX 30–60 sec (unlimited download, included with RTK subscription) | Free |
| RINEX 1–20 sec | PHP 50/MB |

## Sources Consulted
- PAGeNet Services & Fees page: https://pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx (observed 2026-04-30)
- NAMRIA FOI inventory listing (PAGeNet domain confirmation)
- UNOOSA archived presentation (host domain confirmation)
- Contact: pagenet@namria.gov.ph / (632) 8884-2849
