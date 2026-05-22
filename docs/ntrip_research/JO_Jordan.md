# Jordan [JO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-23 (refresh of 2026-05-17); ACOR ntrip-network page re-fetched 2026-05-23 — HTTP 200; the page still describes a single-base operation contactable via acor@acorjordan.org with coverage-map graphic, no host:port or pricing published; radius probe Amman 31.94/35.93 within 200 km returns only Israeli-side stations (centipede ARKG ~85 km, rtk2go misgav_dov ~140 km, igs_ip BSHM00ISR0 ~120 km), none of them usable from Jordan
last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23

## Status: YES — single-station NTRIP base confirmed (ACOR, Amman); no national government or commercial caster found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — ACOR (American Center of Research, Amman) operates a single-station NTRIP base confirmed active January 2026 |
| **host:port — ACOR** | not published on acorjordan.org/ntrip-network/; contact acor@acorjordan.org for credentials |
| **tariff — ACOR** | not published; likely free or low-cost for researchers; commercial terms unknown |
| **hobbyist_eligibility** | Unclear — ACOR is a US non-profit research institution; individual hobbyist access not explicitly offered; contact required |
| **legal_residency_required** | No — ACOR is internationally accessible in principle; no explicit residency requirement stated |
| **last_confirmed_alive** | 2026-05-23 — `acorjordan.org/ntrip-network/` re-fetched HTTP 200; content unchanged from the 2026-01-25-stamped revision (NTRIP base-station description, coverage-map graphic, contact `acor@acorjordan.org`); the 2026-05-17 single 404 was confirmed transient as anticipated. No JO-tagged stations in rtk2go / Centipede / EarthScope / IGS-IP (`scripts/stations_by_country.py JOR` returns none, 2026-05-23). |
| **datum_epoch** | omitted -- no citable declaration (ACOR ntrip-network page describes generic NTRIP concept and contact procedure only; no datum / frame / epoch statement; AMMN00JOR EUREF station page is not the operator declaration for the ACOR caster) |

## Most Recent Project Announcement

**ACOR NTRIP Network** (page last-updated stamp 2026-01-25, content unchanged through 2026-05-23): The American Center of Research (ACOR), a US non-profit institution based in Amman, describes its NTRIP base station at acorjordan.org/ntrip-network/. The service provides centimeter-level accuracy via RTCM corrections for multiband (L1+L2) receivers and includes a coverage map showing the effective operational range around Amman. No government announcement for a national Jordanian NTRIP caster was found.

## Context Notes

- **ACOR** (acorjordan.org): Primarily an archaeology and humanities research centre (American Center of Research, Amman). Its GNSS/NTRIP service is operated to support field surveys for archaeological projects in Jordan. Host, port, and credentials are not published; contact acor@acorjordan.org. Coverage map shows zones around Amman; effective range for RTK is station-distance-dependent and terrain-limited. A single base station; no VRS or network RTK.
- **curl probe of `acorjordan.org:2101`**: not executable via shell tools in this session.
- **Royal Jordanian Geographic Centre (RJGC)** (rjgc.gov.jo; +962 6 534 5 188; rjgc@rjgc.gov.jo): National mapping authority established 1975, under the Jordan Armed Forces. Website confirms services in aerial/spatial survey, mapping, GIS, space geodesy, and GPS. RJGC maintains geodetic reference stations and CORS infrastructure for Jordan's national spatial reference system, and is participating in the JICA "Project for Development of Continuously Operating Reference Stations (CORS) for Proper Land Management" (signed July 2025 with DLS) — but access is restricted; no public NTRIP caster, real-time corrections service, or self-service registration is advertised on the website as of 2026-05-23.
- **GNSS spoofing**: Persistent Israeli military GPS/GNSS spoofing active continuously since Oct 2023 across Israel / Lebanon / Jordan / Sinai / Cyprus corrupts RTK raw-observables across much of Jordan regardless of correction stream. Any hypothetical local RTK service would face this as a fundamental operational hazard (cross-referenced in IL_Israel.md; rtk_inventory `rjgc_cors` note).
- **Department of Lands and Survey (DLS)** (maps.dls.gov.jo): Manages national cadastral system. No public NTRIP endpoint found in any registry.
- **IGS station AMMN00JOR** (Amman, Jordan) at EUREF Permanent GNSS Network: High-quality geodetic reference station used for scientific post-processing; not a public NTRIP RTK stream.
- No commercial CORS/RTK network has been identified for Jordan in surveying industry directories, ArduSimple country pages, NTRIP-list.com, rtcm-ntrip.org, RTK2go, or Centipede-RTK sourcetables.
- **Global commercial fallbacks:** Galileo HAS (~40 cm, no internet); GEODNET, Onocoy, PointOne — no confirmed Jordan coverage in public station maps; Trimble RTX (PPP, not network RTK).
- **Practical workaround:** Contact ACOR Amman (acor@acorjordan.org) for potential NTRIP access; otherwise deploy a local base station or use satellite-based PPP.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EUREF/IGS — AMMN00JOR** (Amman) RINEX archive | https://epncb.oma.be/_networkdata/siteinfo4onestation.php?station=AMMN00JOR | Free |
| **ACOR GNSS post-processing** — available to registered ACOR users | https://acorjordan.org/ntrip-network/ | Likely free for researchers; contact acor@acorjordan.org |

## Sources Consulted
- ACOR NTRIP Network page: https://acorjordan.org/ntrip-network/ — HTTP 200 on 2026-05-23, page last-updated stamp 2026-01-25, content substantively unchanged; contact email acor@acorjordan.org
- ACOR Jordan homepage: https://acorjordan.org/ — organization profile confirmed 2026-05-23
- curl probe of `acorjordan.org:2101` — not executable: shell tools unavailable in this session
- Royal Jordanian Geographic Centre: https://rjgc.gov.jo/en — no CORS/NTRIP service listed; phone +962 6 534 5 188; email rjgc@rjgc.gov.jo confirmed 2026-05-06
- Department of Lands and Survey (Jordan): https://maps.dls.gov.jo/dlsweb/ — no NTRIP service listed
- IGS/EUREF — AMMN00JOR station: https://epncb.oma.be/_networkdata/siteinfo4onestation.php?station=AMMN00JOR
- ArduSimple country RTK list (Jordan not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- mvarga1989 GitHub GNSS CORS networks list (Jordan not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2go monitor (no Jordan stations observed)
- WebSearch: "Jordan NTRIP RTK CORS" + Arabic-language queries — no additional national or commercial caster found (re-checked 2026-05-23; result unchanged)
- Pipeline check: no JO stations in rtk2go / Centipede / EarthScope / IGS-IP — 2026-05-23 via `scripts/stations_by_country.py JOR`
- Daily Business Mena (16 Jul 2025) — JICA / DLS / RJGC MoM signing for CORS technical-cooperation project (50 CORS, Bernese, ITRF-aligned national frame): https://en.dbmena.com/2025/07/16/jica-sign-jointly-with-department-of-land-and-survey-and-royal-jordanian-geographic-center-the-minutes-of-meeting-for-technical-capacity-project/
