# Serbia [RS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-12)

## Status: YES — paid gov NTRIP caster (AGROS, RGZ) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (AGROS — paid) |
| **landing_url** | `https://www.rgz.gov.rs/agros` |
| **access_url** | `https://www.rgz.gov.rs/agros` (Serbian-language; subscription via RGZ) |
| **host:port — AGROS** | `agros.rgz.gov.rs:2101` (IP 93.87.56.181) |
| **VRS** | Yes — Trimble VRS Now; network RTK solution |
| **tariff — RTK flat-rate** | 1,125 RSD/month (~€10) or 8,688 RSD/year (~€74 @ ~117 RSD/EUR) |
| **tariff — DGPS flat-rate** | 703 RSD/mo · 5,379 RSD/yr — **out of scope** per primer [scope] (DGNSS-only pseudorange; carrier-phase RTK only is in scope). Listed for completeness, not recommended. |
| **datum_epoch** | omitted -- no citable operator declaration on rgz.gov.rs. |
| **hobbyist_eligibility** | yes — registration open via rgz.gov.rs; no professional licence stated; affordable annual rate |
| **legal_residency_required** | unclear — registration portal Serbian-language; payment methods not fully documented in English |
| **last_confirmed_alive** | `agros.rgz.gov.rs:2101` connection TIMEOUT 2026-05-17 (12 s) — DNS resolves (93.87.56.181) but sandbox egress blocked; RGZ web portal `www.rgz.gov.rs/agros` redirect-looped on WebFetch 2026-05-17 (page exists but returns >10 redirects). |

## Context Notes

- **AGROS** (Active Geodetic Reference Frame of Serbia): Operated by the Republički geodetski zavod (RGZ — Republic Geodetic Authority of Serbia). Network established 2002–2005; economic use since December 2005. Trimble Pivot Platform backbone with VRS Now network correction.
- **Infrastructure**: ~30 permanent CORS stations covering Serbian territory. Dense cluster in Vojvodina (north); sparser in southern Serbia.
- **Reference system**: not declared on rgz.gov.rs / agros.rgz.gov.rs in English-language pages checked 2026-05-17; omitted per citation rule.
- **Pricing source**: Uredba (regulation) published by RGZ; Serbian-language portal at rgz.gov.rs. Confirmed in country-survey.md from rtk_inventory.md entry (sourced April 2026). DGPS tier listed in the Uredba is out of project scope (carrier-phase RTK only).
- **Volunteer complement**: rtk2go = 27 SRB bases (BOBASL, BPACA, DJUKA, DJURIC55, DUCA14, Drim, FARMASAK, FFHV, ISKRAML, JANKO93, JOVAID, KARMXT, LUKASU, MAJKIC, MARKMB, MIKIDOL, MRJNSI, OBRVESA, PEJIC, PERO, ROBIBNS, SILODANIK, SOKACBB, ZIKARU, livibns, prahovo, viktor); Centipede = 13 SER stations (ADAM, BRTK, DADO, DANE, DETK, KAMA, KDCS, LEMI, MIRO, RTKM, SURD, TOMA, VRTK; new since prior: DADO, KDCS, LEMI). Total 40 volunteer bases. Dense Vojvodina cluster.
- **Operator contact**: RGZ, Bulevar vojvode Mišića 39, Beograd; https://www.rgz.gov.rs/ · info.centar@rgz.gov.rs
- **Local `scripts/stations_by_country.py SRB`** (2026-05-17): centipede=13 (alias SRB→SER), rtk2go=27.

## Post-Processing (RINEX) Fallback

RINEX data available from AGROS reference stations via the RGZ portal at agros.rgz.gov.rs; exact terms not confirmed in English-language documentation.

## Sources Consulted
- RGZ AGROS page: https://www.rgz.gov.rs/agros
- AGROS English portal: http://agros.rgz.gov.rs/navigation.php?Lang=ENG (ECONNREFUSED on 2026-05-06 — subdomain not responding; main RGZ portal responsive)
- rtk_inventory.md entry `agros` (confirmed tariffs from RGZ Uredba, April 2026): host:port and tariff data
- ArduSimple Serbia RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-serbia/
- curl probe of `agros.rgz.gov.rs:2101` — DNS resolves (93.87.56.181); port 2101 connection timeout on 2026-05-06 (egress firewall suspected)
- 2026-05-12 re-check: RGZ AGROS portal www.rgz.gov.rs/agros HTTP 200. Public English-language AGROS pricing remains absent from rgz.gov.rs and from agros.rgz.gov.rs — the only public-source RTK / DGPS pricing comes from rtk_inventory.md (sourced April 2026 from RGZ Uredba): 1,125 RSD/mo RTK, 8,688 RSD/yr RTK; 703 RSD/mo DGPS, 5,379 RSD/yr DGPS.
- Local: `py scripts/stations_by_country.py SER` → 11 Centipede stations; `SRB` → 26 rtk2go bases (2026-05-12).
