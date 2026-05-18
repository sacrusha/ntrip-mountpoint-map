# Kenya [KE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06; verified 2026-05-12; datum + caster re-confirmed 2026-05-17 | USD/KES: 1 USD ≈ 129–130 KES (CBK / xe.com, May 2026)

## Status: ONE ACTIVE private NTRIP caster (Muya CORS) — PAYG tariff now confirmed

---

## Service 1: Muya CORS — ACTIVE (Measurement Systems Ltd)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | **Yes** |
| **host:port** | Not publicly disclosed — credentials (IP, port, username, password) issued per account on registration |
| **tariff** | **KES 400 / 2 hours (Pay As You Go), valid 30 days** (≈ USD 3.10 PAYG). Subscriber chooses hourly / daily / monthly duration at checkout; longer-term rates not publicly itemised. Payment by M-Pesa mobile money. Source: https://measurementsystems.org/service/cors-corrections-services/ (Pay-As-You-Go price quoted by Measurement Systems; reconfirmed via web search snippet 2026-05-12). Contact: support@muya-cors.com / +254 798 519 942 / +254 111 433 499. VAT inclusion not stated. |
| **hobbyist_eligibility** | Unclear (likely yes) — T&C permit "surveying and related activities" and "automated GNSS control of farming and agricultural machinery and construction engineering machinery"; recreational/hobbyist use is not explicitly mentioned but not excluded. "Safety-of-Life use" is explicitly prohibited. |
| **legal_residency_required** | **No** — no geographic restriction in T&C; governing law is Kenyan courts (dispute clause only). M-Pesa payment is, however, easiest from a Kenyan mobile wallet. |
| **last_confirmed_alive** | **2026-05-17** — muya-cors.com reachable; pricing snippet (KES 400 / 2 h PAYG) re-observed via Measurement Systems product page. Field-use case study Feb 2025 (Orbital Africa, Kitisuru Nairobi). |
| **vrs** | ? — operator pages do not describe network-RTK / VRS / MAC / FKP; "25+ reference stations" + RINEX/NTRIP wording is consistent with single-base raw streams but no explicit statement either way. Sourcetable not publicly probed (host:port issued per account). |
| **datum_epoch** | omitted -- no citable network-frame declaration. muya-cors.com (2026-05-17) only states that **base coordinates are computed** in ITRF2014 (current observation epoch) via OPUS-NGS + Trimble RTX online processing; verbatim: *"Muya CORS base stations coordinates are computed regularly using ... OPUS-National Geodetic Survey of USA, Trimble RTX online processing services based on ITRF2014 and current observation epoch."* User-selectable output datums offered are WGS84 and Kenya Arc 1960 (UTM / Cassini-Soldner projections). No on-page text declares ITRF2014 as the network's broadcast/output frame, so per primer [datum-epoch] citation rule this is downgraded from a declaration to `omitted`. |

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
- https://muya-cors.com/ and T&C (muya-cors.com/terms_and_conditions — observed 2026-05-12; reconfirmed 2026-05-17 incl. datum declaration "WGS84 / Kenya Arc 1960 / ITRF2014 (current epoch)" via OPUS-NGS + Trimble RTX)
- https://measurementsystems.org/service/cors-corrections-services/ — KES 400 / 2 h PAYG quote (observed via WebSearch snippet 2026-05-12)
- https://kenya.measurementsystems.org/knowledge_base/ntrip-cors-explained
- ArduSimple Kenya page (ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kenya/)
- https://orbital.co.ke (Feb 2025 Muya CORS field use)
- FIG 2022 — Kenya Geodetic Reference Frame proceedings
- RCMRD corsdata.rcmrd.org, cors.rcmrd.org
- IGS network (network.igs.org) — MALI, RCMN
- RTK2GO, ntrip-list.com/africa/, corsstations.com — no KE rtk2go mountpoints in current stations.json
- Kenya Power X/Twitter post Apr 2025
- xe.com / CBK USD/KES rate
