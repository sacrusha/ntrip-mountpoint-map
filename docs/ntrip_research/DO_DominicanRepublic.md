# Dominican Republic [DO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — multiple active public NTRIP casters

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (FUNDCORSRD curl-confirmed live; IGN REGNA-RD government; CODIA CORS-MET licensed-only; TopNETlive commercial) |
| **host:port — FUNDCORSRD** | `190.166.228.161:2103` (sourcetable retrieved directly 2026-05-06; ~50 mountpoints, RTCM 3.0 + RTCM 3.2/3.3 paired streams; SNIP [wPRO] R3.19.00) |
| **host:port — IGN REGNA-RD** | `ntrip.ign.gob.do` (registration portal reachable; NTRIP port 2101 timed out, likely Cloudflare WAF) |
| **host:port — CODIA CORS-MET** | not published (CODIA-licensed members only) |
| **host:port — TopNETlive** | `rtk.topnetlive.com:2101` (Topcon commercial; DR coverage listed on corsstations.com) |
| **tariff** | FUNDCORSRD: not published — credentials via fundcorsrd.com / fundcorsrd@gmail.com. IGN REGNA-RD: appears free. CODIA: gated. TopNETlive: paid commercial. |
| **hobbyist_eligibility** | FUNDCORSRD: unclear — non-profit founded by surveyors but states it serves "society in general" (838+ users as of 2025); IGN: unclear; CODIA: no (licensed CODIA members only); TopNETlive: yes (open commercial) |
| **legal_residency_required** | unclear |
| **last_confirmed_alive** | FUNDCORSRD: 2026-05-06 (sourcetable retrieved live). IGN REGNA-RD portal: 2026-05-06 reachable (port behind WAF). |

## Most Recent Project Announcement

**IGN REGNA-RD expansion** — November 2025. The Instituto Geográfico Nacional expanded the REGNA-RD CORS network beyond the original 2 stations (Moca, Puerto Plata). Registration portal at ntrip.ign.gob.do remained reachable; the actual NTRIP port appears to sit behind a Cloudflare WAF that blocks raw TCP connections to 2101 from outside Cloudflare-allowed paths.

## Context Notes

- **FUNDCORSRD** (Fundación CORS-RD): Non-profit caster founded by surveyors in 2016. Sourcetable was retrieved live on 2026-05-06 from `190.166.228.161:2103` and lists ~50 mountpoints covering the full national territory (32 physical stations transmitting both RTCM 3.0 and RTCM 3.2/3.3 streams). Caster software: SNIP [wPRO] R3.19.00. The caster is closed: credentials are issued via direct request through fundcorsrd.com or fundcorsrd@gmail.com. Self-described as serving "society in general," with 838+ users reported as of 2025. Pricing not surfaced publicly.
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
