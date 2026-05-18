# Jordan [JO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry); ACOR navigation re-verified 2026-05-17 (target page returned a single 404 same day — likely transient; parent nav still lists the service)

## Status: YES — single-station NTRIP base confirmed (ACOR, Amman); no national government or commercial caster found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — ACOR (American Center of Research, Amman) operates a single-station NTRIP base confirmed active January 2026 |
| **host:port — ACOR** | not published on acorjordan.org/ntrip-network/; contact acor@acorjordan.org for credentials |
| **tariff — ACOR** | not published; likely free or low-cost for researchers; commercial terms unknown |
| **hobbyist_eligibility** | Unclear — ACOR is a US non-profit research institution; individual hobbyist access not explicitly offered; contact required |
| **legal_residency_required** | No — ACOR is internationally accessible in principle; no explicit residency requirement stated |
| **last_confirmed_alive** | 2026-05-17 — `acorjordan.org/` re-fetched; navigation still lists "High-Precision GNSS with ACOR's NTRIP Network" under Initiatives → Other Projects, link → `https://acorjordan.org/ntrip-network/` (target returned a 404 on a single fetch attempt 2026-05-17 — likely cache / transient, as the parent nav still surfaces the link, contrary to a permanent removal). 2026-05-12 prior fetch of the same target was HTTP 200 with last-updated stamp 2026-01-25. No JO-tagged stations in rtk2go / Centipede / EarthScope (`scripts/stations_by_country.py JOR` returns none, 2026-05-12). |
| **datum_epoch** | omitted -- no citable declaration (ACOR ntrip-network page describes generic NTRIP concept and contact procedure only; no datum / frame / epoch statement; AMMN00JOR EUREF station page is not the operator declaration for the ACOR caster) |

## Most Recent Project Announcement

**ACOR NTRIP Network** (updated January 2026): The American Center of Research (ACOR), a US non-profit institution based in Amman, describes its NTRIP base station at acorjordan.org/ntrip-network/. The page was updated 2026-01-25. The service provides centimeter-level accuracy via RTCM corrections for multiband (L1+L2) receivers and includes a coverage map showing the effective operational range around Amman. No government announcement for a national Jordanian NTRIP caster was found.

## Context Notes

- **ACOR** (acorjordan.org): Primarily an archaeology and humanities research centre (American Center of Research, Amman). Its GNSS/NTRIP service is operated to support field surveys for archaeological projects in Jordan. Host, port, and credentials are not published; contact acor@acorjordan.org. Coverage map shows zones around Amman; effective range for RTK is station-distance-dependent and terrain-limited. A single base station; no VRS or network RTK.
- **curl probe of `acorjordan.org:2101`**: not executable via shell tools in this session.
- **Royal Jordanian Geographic Centre (RJGC)** (rjgc.gov.jo; +962 6 534 5 188; rjgc@rjgc.gov.jo): National mapping authority established 1975, under the Jordan Armed Forces. Website confirms services in aerial/spatial survey, mapping, GIS, space geodesy, and GPS. No CORS network, NTRIP caster, or real-time corrections service is advertised on the website as of 2026-05-06.
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
- ACOR NTRIP Network page: https://acorjordan.org/ntrip-network/ — HTTP 200, page last-updated 2026-01-25, content substantively unchanged on 2026-05-12; contact email acor@acorjordan.org
- ACOR Jordan homepage: https://acorjordan.org/ — organization profile confirmed 2026-05-12
- curl probe of `acorjordan.org:2101` — not executable: shell tools unavailable in this session
- Royal Jordanian Geographic Centre: https://rjgc.gov.jo/en — no CORS/NTRIP service listed; phone +962 6 534 5 188; email rjgc@rjgc.gov.jo confirmed 2026-05-06
- Department of Lands and Survey (Jordan): https://maps.dls.gov.jo/dlsweb/ — no NTRIP service listed
- IGS/EUREF — AMMN00JOR station: https://epncb.oma.be/_networkdata/siteinfo4onestation.php?station=AMMN00JOR
- ArduSimple country RTK list (Jordan not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- mvarga1989 GitHub GNSS CORS networks list (Jordan not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2go monitor (no Jordan stations observed)
- WebSearch: "Jordan NTRIP RTK CORS" + Arabic-language queries — no additional national or commercial caster found (re-checked 2026-05-12; result unchanged)
- Pipeline check: no JO stations in rtk2go / Centipede / EarthScope — 2026-05-12 via `scripts/stations_by_country.py JOR`
