# Moldova [MD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-17 — no tariff schedule change; caster + creds unchanged)

## Status: YES — MOLDPOS national RTK network active; registration required; open to any GPS receiver owner

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — MOLDPOS (Moldova Positioning System), operated by S.E. INGEOCAD under the Agency for Geodesy, Cartography and Cadastre (AGCC / agcc.gov.md) |
| **landing_url — MOLDPOS** | `https://moldpos.md/` — operator-owned MOLDPOS service site (RO/RU); describes the network, mountpoints (VRS/MAX/MSM, FreeZone), test credentials. Alternative: `https://agcc.gov.md/content/moldpos` (AGCC agency-level MOLDPOS page). |
| **access_url — MOLDPOS** | http://moldpos.ingeocad.md/SBC/Account/Register — Leica Spider Business Center registration (bare sign-up form). MDL tariff schedule not published in open web (`moldpos.md/tarife` and `/preturi` returned HTTP 404 on 2026-05-12); pricing is contact-only via `moldpos@ingeocad.md`. |
| **host:port — MOLDPOS** | `185.108.183.29 : 8080` (updated from former IP 188.237.130.50:8080). SBC portal: `moldpos.ingeocad.md`. Source: moldpos.md official pages, observed 2026-05-06. |
| **tariff — MOLDPOS** | Paid service (became paid per AGCC Order No. 04 of 06.01.2012). Current MDL tariff schedule not published in open sources — contact INGEOCAD at moldpos@ingeocad.md or +373 22 881200 for current rates. Free test credentials for trial zones: login `moldpos` / password `moldpos`. |
| **datum_epoch** | omitted — no citable operator declaration. INGEOCAD/AGCC prose mentions ETRS89 alignment (EuroGeographics context) but no operator-side stream/RINEX/portal cite states the caster output frame. |
| **hobbyist_eligibility** | Open — INGEOCAD explicitly states "MOLDPOS is an open network; any GPS receiver owner can join" (MOLDPOS – ОТКРЫТАЯ СЕТЬ: ЛЮБОЙ ОБЛАДАТЕЛЬ GPS ПРИЕМНИКА МОЖЕТ ПРИСОЕДИНИТЬСЯ К НАМ). Registration via SBC portal appears sufficient; no licensed-surveyor restriction found. |
| **legal_residency_required** | Not stated; no explicit residency requirement found. |
| **last_confirmed_alive** | WebFetch of `185.108.183.29:8080` returned socket closed unexpectedly (connection established then closed — consistent with an NTRIP caster responding to HTTP probe with non-HTTP data) on 2026-05-06. moldpos.ingeocad.md SBC portal (login page) HTTP 200 confirmed 2026-05-06. |

## Most Recent Project Announcement

**MOLDPOS modernisation (2025)**: A 2025 INGEOCAD procurement notice references "modernizarea Sistemului Național de Poziționare MOLDPOS" — acquisition of 5 additional Leica Spider licenses to allow adding new CORS stations to the network. As of 2026-05-06 the exact expanded station count is not publicly announced, but the network started with 10 permanent GNSS stations at founding (2011) and has grown since.

**Galileo integration**: Moldova's positioning system added Galileo to GPS and GLONASS (reported in GPS World). The MSM mountpoint confirms multi-constellation support. Moldova is an EU candidate country (2022); AGCC is a EuroGeographics member and aligns MOLDPOS to ETRS89.

## Context Notes

- **Caster connection details**:
  - IP: `185.108.183.29` · Port: `8080` (non-standard; Leica Spider NTRIP caster default)
  - Former IP `188.237.130.50:8080` is superseded — use the current IP above
  - SBC web portal: http://moldpos.ingeocad.md/SBC/
  - Registration (new account): http://moldpos.ingeocad.md/SBC/Account/Register (Leica Spider Business Center v7.10.0.114)
  - Station status map: http://moldpos.ingeocad.md/SBC/User/SiteMap/SiteMapPublic
- **Mountpoints**:
  - Production zone: `VRS` (Virtual Reference Station), `MAX` (Master–Auxiliary Corrections), `MSM` (Multi-Signal Messages — GPS+GLONASS+Galileo)
  - Free test zones (FreeZone — open without subscription): `FZUTM` (Technical University of Moldova), `FZUASM` (State Agrarian University), `FZMA` (Ministry of Defence), `FZINGEOCAD`, `FZCDEIC` (Centre of Excellence in Construction). Test zone credentials: login `moldpos` / password `moldpos`.
- **Tariff**: Became paid per Order No. 04 of 06.01.2012. The MDL schedule is not published online; a 2025 government procurement reference (achizitii.md) confirms "Serviciul de acces la Sistemul Național Global MOLDPOS" is an active paid service. Contact INGEOCAD for pricing.
- **Accuracy**: RTK via VRS/MAX/MSM — cm-level precision using RTCM and TCP/IP delivery via NTRIP protocol.
- **Contact**: moldpos@ingeocad.md · info@ingeocad.md · +373 22 881200 · Chișinău, str. Pușkin 47, of. 225 · Tel. 022 881 214 (MOLDPOS desk)
- **AGCC**: info@agcc.gov.md · +373 22 881255
- **Practical workaround**: Register at moldpos.ingeocad.md/SBC/Account/Register; test free zones (FZxxx mountpoints, credentials moldpos/moldpos) before paying. Contact moldpos@ingeocad.md for tariff schedule and subscription contract.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **MOLDPOS SBC** — RINEX data for registered users; historical observations | http://moldpos.ingeocad.md/SBC/ | Paid; contact INGEOCAD |
| **EarthScope GNSS Data Archive** — IGS/EUREF-affiliated Moldova stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |
| **EUREF Permanent GNSS Network (EPN)** — regional CORS near Moldova | https://epncb.oma.be/ | Free (account required) |

## Sources Consulted
- moldpos.md (official MOLDPOS site) — caster IP 185.108.183.29:8080, mountpoints (VRS, MAX, MSM, FreeZone), test credentials moldpos/moldpos, Galileo note; observed 2026-05-06
- moldpos.ingeocad.md/SBC — Leica Spider Business Center v7.10.0.114; HTTP 200 confirmed 2026-05-06
- ingeocad.md — "MOLDPOS open network, any GPS receiver owner can join" (Russian text); 2025 modernisation procurement note; 5 new Spider licenses; contact info@ingeocad.md · +373 22 881200; observed 2026-05-06
- agcc.gov.md/content/moldpos — AGCC MOLDPOS page; EU candidate country / EuroGeographics context; observed 2026-05-06
- groups.google.com/g/UGGCM — "SERVICII PUBLICE MOLDPOS" thread; Order No. 04 of 06.01.2012 (paid service); old IP 188.237.130.50:8080; Chișinău address str. Pușkin 47; observed 2026-05-06
- GPS World — "Moldova's positioning system now uses Galileo" (GPS+GLONASS+Galileo confirmation)
- Scribd — "MOLDPOS – GNSS-Positioning Service of Moldova – CHIRIAC" (2012 paper; network founding, 10-station initial deployment)
- ardusimple.com/rtk-correction-services-and-ntrip-casters-in-moldova/ — confirms paid national service; SBC registration URLs
- EuroGeographics — AGCC member profile (ETRS89 alignment, EU candidate context)
- WebFetch probe of `185.108.183.29:8080` — socket closed unexpectedly (NTRIP/non-HTTP response received) 2026-05-06
- WebFetch probe of `moldpos.md:8080` — ECONNREFUSED 2026-05-06 (hostname-based access on port 8080 not responding; use IP directly)
- RTK2go monitor — no Moldova NTRIP streams confirmed
- py scripts/stations_by_radius.py 47.0 28.5 200 (2026-05-12) — only nearest free RTK stations are POPINCIUC (rtk2go, Romania, 125 km) and VASLUI (Centipede, Romania, 108 km) — both outside reliable single-base range (~35 km) from Chișinău
- moldpos.md/tarife and moldpos.md/preturi return HTTP 404 (re-verified 2026-05-17) — tariff schedule still not published in open web; pricing remains contact-only via moldpos@ingeocad.md
- 2026-05-17 WebFetch of moldpos.md returned only the general overview (GNSS basics, no host/port/tariff); SBC portal at moldpos.ingeocad.md still the operational entry point
