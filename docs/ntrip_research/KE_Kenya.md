# Kenya [KE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 | USD/KES: 1 USD = 129.87 KES (CBK / xe.com, 2026-05-05)

## Status: ONE ACTIVE private NTRIP caster (Muya CORS)

---

## Service 1: Muya CORS — ACTIVE (Measurement Systems Ltd)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | **Yes** |
| **host:port** | Not publicly disclosed — credentials (IP, port, username, password) issued per account on registration |
| **tariff** | Not publicly disclosed. Flexible tiers (hourly / daily / monthly) — no KES or USD figures in any public source. Contact: support@muya-cors.com / +254 798 519 942 / +254 111 433 499. Date observed: 2026-05-06. Source: https://muya-cors.com/ |
| **hobbyist_eligibility** | Unclear (likely yes) — T&C require no professional licence; "company" field in registration appears non-mandatory; agricultural machinery use explicitly permitted in T&C |
| **legal_residency_required** | **No** — no geographic restriction in T&C; governing law is Kenyan courts (dispute clause only) |
| **last_confirmed_alive** | **2026-05-06** — portal and login reachable today; confirmed in active field use Feb 2025 (Orbital Africa case study, Kitisuru Nairobi) |

**Operator:** Measurement Systems Limited, Nairobi
**Website:** https://muya-cors.com/
**Network:** 25+ reference stations covering Kenya
**Constellations:** GPS, GLONASS, BeiDou, Galileo
**Service type:** Real-time RTK via NTRIP; also RINEX post-processing
**Accuracy:** Sub-centimetre claimed

---

## Service 2: Survey of Kenya (SoK) — No public NTRIP

| Field | Value |
|---|---|
| **Status** | ~20 Tier-3 CORS installed for KENREF (Kenya Geodetic Reference Frame) — used internally for geodetic densification; no public NTRIP caster published |
| **host:port** | null — no public endpoint |
| **tariff** | null |

Third-party CORS require gazettement by Director of Surveys before cadastral use — regulatory barriers remain. (Source: FIG 2022 proceedings)

---

## Service 3: RCMRD — Login-gated, not confirmed as public RTK

| Field | Value |
|---|---|
| **Status** | CORS node at RCMRD HQ Nairobi (Leica 1200GG, Spider Business Centre v7.8.1); data portal corsdata.rcmrd.org requires authenticated login; IGS stream RCMN at igs-ip.net is a single-station raw observation stream (not network RTK/VRS) |
| **host:port** | corsdata.rcmrd.org (login-gated; not a public NTRIP RTK service) |
| **tariff** | Not public; oriented toward research/institutional post-processing |

---

## Service 4: Kenya Power / IESR CORS — Announced April 2025, not yet live

| Field | Value |
|---|---|
| **Status** | Kenya Power (@KenyaPower on X, ~Apr 27 2025): 15-station CORS network announced, targeting "professionals engaged in precise land and engineering surveys" under IESR; still undergoing gazettement submission as of announcement. No live NTRIP stream confirmed. |
| **host:port** | null — not yet published |
| **URL** | https://x.com/KenyaPower/status/1916418017329623087 |

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **Muya CORS RINEX** — post-processing data available via same subscription as NTRIP | https://muya-cors.com/ | Same tiers as NTRIP (cost not publicly disclosed); contact support@muya-cors.com |
| **EarthScope GNSS Data Archive** — IGS stations MALI (Malindi) and RCMN (RCMRD Nairobi) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |
| **RCMRD CORS data portal** — institutional/research RINEX access; login-gated | https://corsdata.rcmrd.org/sbc | Unknown — contact rcmrd@rcmrd.org |

## IGS Stations in Kenya (scientific, not RTK)

- **MALI / MAL200KEN** (Malindi): IGS station; raw GNSS observations via igs-ip.net — single-station scientific stream, not network RTK
- **RCMN** (RCMRD Nairobi): Same — raw observations for geodesy

---

## Sources Consulted
- https://muya-cors.com/ and T&C
- ArduSimple Kenya page (ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kenya/)
- https://orbital.co.ke (Feb 2025 Muya CORS field use)
- FIG 2022 — Kenya Geodetic Reference Frame proceedings
- RCMRD corsdata.rcmrd.org, cors.rcmrd.org
- IGS network (network.igs.org)
- RTK2GO, ntrip-list.com/africa/, corsstations.com
- Kenya Power X/Twitter post Apr 2025
- xe.com / CBK USD/KES rate
