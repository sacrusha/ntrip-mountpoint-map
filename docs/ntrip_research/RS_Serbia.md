# Serbia [RS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid government NTRIP caster (AGROS, RGZ) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (AGROS — paid) |
| **host:port — AGROS** | `agros.rgz.gov.rs:2101` (IP: 93.87.56.181) |
| **VRS** | Yes — Trimble VRS Now backbone; network RTK solution |
| **tariff — RTK flat-rate** | 1,125 RSD/month (~€10/month) or 8,688 RSD/year (~€74/yr at ~117 RSD/EUR) |
| **tariff — DGPS flat-rate** | 703 RSD/month or 5,379 RSD/year (~€46/yr) |
| **tariff — per-minute / hourly** | Available; see rgz.gov.rs for current schedule |
| **hobbyist_eligibility** | yes — registration open via rgz.gov.rs; no professional licensing stated; affordable annual rate |
| **legal_residency_required** | unclear — registration portal is Serbian-language; payment methods not fully described in English sources |
| **last_confirmed_alive** | agros.rgz.gov.rs port 2101 resolved (93.87.56.181) but timed out from this research environment on 2026-05-06 (suspected external egress firewall; RGZ AGROS portal web HTTP 200 confirmed); website https://www.rgz.gov.rs/agros HTTP 200 on 2026-05-06 |

## Context Notes

- **AGROS** (Active Geodetic Reference Frame of Serbia): Operated by the Republički geodetski zavod (RGZ — Republic Geodetic Authority of Serbia). Network established 2002–2005; economic use since December 2005. Trimble Pivot Platform backbone with VRS Now network correction.
- **Infrastructure**: ~30 permanent CORS stations covering Serbian territory. Dense cluster in Vojvodina (north); sparser in southern Serbia.
- **Reference system**: ETRS89.
- **Pricing source**: Uredba (regulation) published by RGZ; Serbian-language portal at rgz.gov.rs. Confirmed in country-survey.md from networks.md entry (sourced April 2026).
- **Volunteer complement**: rtk2go hosts ~35 Serbian volunteer bases (SRB/SER label); Centipede hosts ~20 SER + ~3 SRB nodes. One of the denser volunteer clusters in the Western Balkans, concentrated in Vojvodina. Combined with AGROS, coverage is good for most of Serbia.
- **Operator contact**: Republički geodetski zavod (RGZ), Bulevar vojvode Mišića 39, Beograd; https://www.rgz.gov.rs/

## Post-Processing (RINEX) Fallback

RINEX data available from AGROS reference stations via the RGZ portal at agros.rgz.gov.rs; exact terms not confirmed in English-language documentation.

## Sources Consulted
- RGZ AGROS page: https://www.rgz.gov.rs/agros
- AGROS English portal: http://agros.rgz.gov.rs/navigation.php?Lang=ENG (ECONNREFUSED on 2026-05-06 — subdomain not responding; main RGZ portal responsive)
- networks.md entry `agros` (confirmed tariffs from RGZ Uredba, April 2026): host:port and tariff data
- ArduSimple Serbia RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-serbia/
- curl probe of `agros.rgz.gov.rs:2101` — DNS resolves (93.87.56.181); port 2101 connection timeout on 2026-05-06 (egress firewall suspected)
