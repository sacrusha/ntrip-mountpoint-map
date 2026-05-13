# Dominican Republic [DO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revision; original 2026-05-06)

## Status: YES — multiple active public NTRIP casters

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (FUNDCORSRD curl-confirmed live 2026-05-12; IGN REGNA-RD government; CODIA CORS-MET licensed-only; TopNETlive commercial) |
| **host:port — FUNDCORSRD** | `190.166.228.161:2103` — sourcetable retrieved live 2026-05-12 (11 308 bytes; 74 STR rows = 37 physical stations × paired RTCM 3.0 + RTCM 3.2/3.3 streams; multi-GNSS GPS+GLO+GAL+BDS; SNIP [wPRO] R3.19.00 of:Dec 19 2025) |
| **host:port — IGN REGNA-RD** | `ntrip.ign.gob.do` (registration portal reachable; NTRIP port 2101 sandbox-timeout — Cloudflare WAF/IP filter) |
| **host:port — CODIA CORS-MET** | not published (CODIA-licensed members only) |
| **host:port — TopNETlive** | `rtk.topnetlive.com:2101` (Topcon commercial; DR coverage listed on corsstations.com) |
| **num_stations** | FUNDCORSRD: 37 (live sourcetable 2026-05-12); IGN REGNA-RD: 2 original + Nov-2025 expansion (size not enumerated publicly) |
| **vrs** | FUNDCORSRD: no (single-station mountpoints only — each station offers an RTCM 3.0 stream and an RTCM 3.2/3.3 MSM stream); IGN REGNA-RD: ? |
| **tariff** | FUNDCORSRD: not published — credentials via fundcorsrd.com / fundcorsrd@gmail.com. IGN REGNA-RD: appears free. CODIA: gated. TopNETlive: paid commercial. |
| **hobbyist_eligibility** | FUNDCORSRD: unclear — non-profit founded by surveyors but states it serves "society in general" (838+ users as of 2025); IGN: unclear; CODIA: no (licensed CODIA members only); TopNETlive: yes (open commercial) |
| **legal_residency_required** | unclear |
| **registration** | FUNDCORSRD: contact form at fundcorsrd.com / email fundcorsrd@gmail.com. IGN REGNA-RD: https://ntrip.ign.gob.do/ |
| **last_confirmed_alive** | FUNDCORSRD: **2026-05-12** (sourcetable retrieved live, 11 308 bytes). IGN REGNA-RD portal: 2026-05-06 reachable (NTRIP port behind WAF/IP filter). |

## Most Recent Project Announcement

**IGN REGNA-RD expansion** — November 2025. The Instituto Geográfico Nacional expanded the REGNA-RD CORS network beyond the original 2 stations (Moca, Puerto Plata). Registration portal at ntrip.ign.gob.do remained reachable; the actual NTRIP port appears to sit behind a Cloudflare WAF that blocks raw TCP connections to 2101 from outside Cloudflare-allowed paths.

## Context Notes

- **FUNDCORSRD** (Fundación CORS-RD): Non-profit caster founded by surveyors in 2016. Sourcetable was retrieved live on **2026-05-12** from `190.166.228.161:2103` and lists **74 STR rows = 37 physical stations** transmitting paired RTCM 3.0 (legacy GPS+GLO) and RTCM 3.2/3.3 MSM (multi-GNSS GPS+GLO+GAL+BDS, frequently MSM7 1077/1087/1097/1127) streams. Coverage extends nationwide (e.g. BARA La Romana, FCAC Azua, FCBN Bani, FCBO Bonao, FCSC Santiago and many others). Caster software: SNIP [wPRO] R3.19.00 (build of 2025-12-19). The caster is closed: credentials are issued via direct request through fundcorsrd.com or fundcorsrd@gmail.com. Self-described as serving "society in general," with 838+ users reported as of 2025. Pricing not surfaced publicly. Strategic agreement with IGN confirmed in 2025 press coverage to contribute to the Dominican Republic's Satellite Geodetic System.
- **IGN REGNA-RD** (Instituto Geográfico Nacional): Government service. Hostname `ntrip.ign.gob.do` and registration portal confirmed reachable on 2026-05-06; raw NTRIP port (2101) timed out, consistent with Cloudflare proxying. The service appears to be free for registered users. Originally 2 stations (Moca, Puerto Plata); November 2025 expansion announced (size/locations not yet enumerated in public sources).
- **CODIA CORS-MET**: Restricted to licensed members of CODIA (Colegio Dominicano de Ingenieros, Arquitectos y Agrimensores) — not accessible to non-licensed individuals or hobbyists.
- **TopNETlive (Topcon)**: Paid commercial global subscription network; `rtk.topnetlive.com:2101`; DR coverage listed on corsstations.com. Open enrolment via Topcon dealers; pricing not on public Topcon page.
- **No free unrestricted public caster** confirmed; FUNDCORSRD and IGN REGNA-RD both gate access via registration.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGN REGNA-RD** — RINEX from REGNA-RD CORS stations | https://ign.gob.do/ | Likely free with account |
| **FUNDCORSRD** — RINEX archive accompanies live caster | https://fundcorsrd.com/ | Account required |
| **EarthScope / SIRGAS-CON** — DR stations in SIRGAS tier | https://www.earthscope.org/data/gnss-data/ | Free noncommercial; USD 1,000/seat/yr commercial |

## Sources Consulted
- FUNDCORSRD sourcetable (`190.166.228.161:2103`) — live curl probe 2026-05-06
- fundcorsrd.com homepage
- IGN Dominican Republic (ign.gob.do)
- ntrip.ign.gob.do registration portal
- CODIA-CORS-MET program references via CODIA
- TopNETlive coverage listing on corsstations.com
- NTRIP-list.com Caribbean/North America
- GEODNET, ONOCOY coverage maps
- SIRGAS-CON station list
