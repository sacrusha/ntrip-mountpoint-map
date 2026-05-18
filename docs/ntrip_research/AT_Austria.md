# Austria [AT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-probe; 2026-05-15 deep research unchanged)

## Status: YES — two nationwide NTRIP RTK casters

1. **APOS** (BEV) — government national service. Free for agriculture/forestry via eAMA; paid for all others.
2. **EPOSA** — private consortium (ÖBB / Wiener Netze / Burgenland Energie). Quote-only commercial pricing.

Plus 14 rtk2go volunteer bases + 1 Centipede node supplementing coverage (mostly eastern Austria).

---

## Caster 1: APOS (BEV)

| Field | Value |
|---|---|
| **landing_url** | https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html |
| **access_url** | https://portal.bev.gv.at/portal/page?_pageid=713,3175360&_dad=portal&_schema=PORTAL |
| **Operator** | BEV — Bundesamt für Eich- und Vermessungswesen |
| **host:port** | `aposrtk.bev.gv.at:2101` (HTTP/0.9 NTRIP, Trimble Ntrip Caster 4.3) |
| **vrs** | yes — nationwide VRS, no baseline-distance degradation |
| **num_stations** | ~40 physical CORS (BEV official page); brochure cites "75" incl. cross-border partners; pipeline counts 0 directly (sourcetable advertises only VRS/MAC mountpoints, not raw bases) |
| **hobbyist_eligibility** | yes — paid standard tier open to any individual; eAMA free tier needs Austrian agricultural registration |
| **legal_residency_required** | no for paid tier; eAMA free tier requires Austrian agricultural enterprise (LFBIS-Nr.) |
| **datum_epoch** | ETRS89 / ETRF2000, epoch 2002.56 — source: https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html |
| **last_confirmed_alive** | 2026-05-17 — `aposrtk.bev.gv.at:2101` re-probed via curl --http0.9: SOURCETABLE 200 OK, Trimble Caster 4.3, 7 STR rows present (`APOS_DGPS`, `APOS_NET3`, `APOS_VRS`, `APOS_VRS3`, `APOS_VRS32_MSM`, `APOS_VRS32_MSM_3D`, `APOS_VRS32_GRID2021`) |

### Tariff (observed 2026-05-15, source: https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html)
- **APOS-RTK** (cm): €50 one-time setup + €0.0015/s OR €20/day OR €200/month. Net; VAT not stated; standard Austrian 20% VAT presumed for commercial users.
- **APOS-DGPS** (dm): €0.00015/s OR €2/day OR €20/month.
- **APOS RAW** (raw RINEX, all stations): paid subscription, professional/institutional only. Five-figure annual fee bracket; €50,000/yr figure from prior research is no longer cited on the public BEV pricing page — treat as unverified.
- **eAMA free tier**: free for agriculture/forestry since 1 Feb 2021. LKO documents the subsidy-equivalent as €150/year per enrolled operation (counted under de-minimis aid; declaration requirement ends 2027-01-01). Prior "€400/yr" figure not corroborated in 2026 sources.

### Mountpoints (live sourcetable, 2026-05-15)
| Mountpoint | Format | Constellations | Notes |
|---|---|---|---|
| `APOS_DGPS` | RTCM 2.3 | GPS | Sub-metre DGNSS |
| `APOS_VRS` | RTCM 2.3 | GPS+GLO | Legacy VRS for older receivers |
| `APOS_VRS3` | RTCM 3.1 | GPS+GLO | Standard VRS |
| `APOS_NET3` | RTCM 3.1 | GPS+GLO | MAC network (master-aux) |
| `APOS_VRS32_MSM` | RTCM 3.2 MSM5 | GPS+GLO+GAL | Multi-constellation VRS |
| `APOS_VRS32_MSM_3D` | RTCM 3.2 MSM5 | GPS+GLO+GAL | 3D network interpolation |
| `APOS_VRS32_GRID2021` | RTCM 3.2 MSM5 | GPS+GLO+GAL | VRS + MGI Grid 2021 transform |

Note: prior research mentioned a speculative `APOS_Extended_plus` (BeiDou). Not present in live sourcetable; removed. `APOS_VRS32_GRID2021` is the current modern mount.

### eAMA registration
1. Log in to eAMA (services.ama.at) with Betriebsnummer (LFBIS-Nr.) + PIN/handysignatur.
2. Portal auto-redirects to BEV registration form; credentials issued within ~48 business hours.
3. Multiple device "rovers" supported per account.
Eligible: agricultural/forestry operations, contract operators, machinery rings, public research/advisory bodies in the sector.

### Paid-tier signup
Email `kundenservice@bev.gv.at` or +43 1 21110-822160. **Fixed IPv4 must be registered per device** — dynamic IPs not accepted.

---

## Caster 2: EPOSA

| Field | Value |
|---|---|
| **landing_url** | https://www.eposa.at/en/ |
| **access_url** | https://www.eposa.at/en/kundensupport (signup via form at info@eposa.at) |
| **Operator** | EPOSA — joint venture of Wiener Netze GmbH, ÖBB Infrastruktur AG, Burgenland Energie AG |
| **host:port** | `ntrip.eposa.at:2101` (NTRIP GNSMART_Caster 2.0/1.0) |
| **vrs** | yes — VRS mountpoints + virtual RINEX |
| **num_stations** | 39 physical (counted from live `*-RAW-4G` streams in sourcetable 2026-05-15); operator declares "more than 40" own + 9 external partner stations (~49 total) |
| **hobbyist_eligibility** | ? — no explicit hobbyist exclusion in T&Cs found; service marketed to commercial/surveying users. Signup is application-based (info@eposa.at) so case-by-case. Pricing model favours short-term/seconds tariff for small jobs. |
| **legal_residency_required** | ? — Austrian invoicing implied; not explicitly stated |
| **datum_epoch** | ETRS89 / ETRF (transformation to MGI Austria 2021 grid available via `-TR`/`-ETRF` mountpoints) — official declaration page not found in public materials; **omitted from authoritative claim per spec.** |
| **last_confirmed_alive** | 2026-05-17 — `ntrip.eposa.at:2101/sourcetable.txt` re-probed: 51 STR rows incl. 39 `*-RAW-4G` physical stations; GNSMART_Caster/2.0; HTML index also serves at `/` |

### Tariff (observed 2026-05-15, source: https://www.eposa.at/abrechnung)
Three billing models; **no public price list** — EUR amounts not disclosed on operator pages, only billing-model descriptions:
- **Sekundenpauschale** (per-second) — short jobs / occasional use; billed quarterly on total connection seconds.
- **Tagespauschale** (per-day flat) — 24/7 access on connection days; billed quarterly.
- **Jahrespauschale** (annual flat) — unlimited use; billed quarterly or annually.

VAT not stated. No minimum contract length stated. No explicit hobbyist tier. Resellers (e.g. UTB) offer hourly EPOSA access bundles. Direct contact required for pricing.

### Mountpoints (live sourcetable extract, 2026-05-15)
**VRS streams (NMEA/Y, requires Basic auth):**
| Mountpoint | Format | Constellations | Notes |
|---|---|---|---|
| `RTK-3` | RTCM 3.0 | GPS+GLO | VRS, no transform |
| `RTK-3-ETRF` | RTCM 3.0 | GPS+GLO | VRS + ETRF central transform |
| `RTK-3-TR` | RTCM 3.0 | GPS+GLO | VRS + MGI grid central |
| `RTK-3-TR-M28/M31/M34` | RTCM 3.0 | GPS+GLO | VRS + transform params in stream |
| `RTK-32-4G` | RTCM 3.2 MSM4 | GPS+GLO+GAL+BDS | VRS, no transform |
| `RTK-32-4G-ETRF` | RTCM 3.2 MSM4 | GPS+GLO+GAL+BDS | VRS + ETRF central transform |
| `RTK-32-4G-TR` | RTCM 3.2 MSM4 | GPS+GLO+GAL+BDS | VRS + MGI grid central |
| `RTK-32-4G-TR-M28/M31/M34` | RTCM 3.2 MSM4 | GPS+GLO+GAL+BDS | VRS + transform params in stream |

**39 physical stations** (`*-RAW-4G`, NMEA=0, requires Basic auth, RTCM 3.2 MSM4 GNSS): ALST, AMST, ANDA, ANDF, ATPU, BADE, DALA, GRAZ, GUMM, GUSS, JENB, KIBG, KLAG, LAND, LEIB, LEOB, LEOP, LIEZ, LINZ, MATR, MATT, MIST, MURZ, OBER, OCHS, PAMA, ROET, SAAL, SALZ, SEEF, SHEI, SHLA, SILL, SONN, TRAI, WEYE, WOBG, WOFU, ZIDF.

### Coverage
Nationwide Austria + ~80 km into DE, IT, LI, SI, SK, HU, CH (per operator).

### Registration
Submit application form (download on eposa.at) → email to `info@eposa.at` → activated same/next business day.

---

## Volunteer / Community Bases (rtk2go + Centipede)

Confirmed via `scripts/stations_by_country.py AUT` on 2026-05-15:

**rtk2go (14 bases):** AUT00OBDA0, AUT_A-GLAS, AUT_RAMETZHOFEN_ETRS, AUT_STY_AVL, AUT_VIE_27, BullaWnk, Checker_G, HalleinANDATA, Horn, Kasing, Loosdorf, Wal_GPS, Wieselburg, ibk-thabest.

**Centipede (1 base):** BOKU (Vienna, 48.32°N 16.07°E, BOKU university campus).

Coverage clusters: Vienna / Lower Austria / Styria. Western Alps (Vorarlberg, most of Tirol outside Innsbruck) sparse. Single-base, no VRS — baseline-distance accuracy degradation applies.

Prior research listed 15 rtk2go bases; one has dropped off (current count 14). No new bases added.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **APOS-PP** (post-processing, no registration) | https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html | Free (per BEV public page) |
| **APOS RAW** | BEV portal, paid subscription | Professional-tier fee, not publicly listed |
| **EUREF EPN** (GRAZ, WIEN, LINZ, SBGZ, etc.) | https://www.epncb.oma.be/ | Free |

---

## Cross-Border Notes
- **Liechtenstein (LI):** no own caster. APOS reaches eastern LI (free via eAMA for AT-registered agri/forestry users). Swiss swipos (paid) covers all of LI directly. EPOSA also covers LI per operator (~80 km cross-border).
- **APOS integrates partner stations** from SAPOS Bavaria (DE), FReDNet Friuli (IT), swipos AGNES (CH) for VRS edge coverage — explains "75 stations" brochure figure vs. ~40 domestic CORS.

---

## Sources Consulted (live as of 2026-05-15 unless noted)
- BEV APOS English product page (tariff + datum): https://www.bev.gv.at/en/Services/Products/Austrian-POsitioning-Service.html (WebFetch 2026-05-15 OK)
- BEV APOS portal (pricing details page): https://portal.bev.gv.at/portal/page?_pageid=713,3175360&_dad=portal&_schema=PORTAL
- BEV APOS brochure (PDF, "75 stations" figure): https://www.bev.gv.at/dam/jcr:557736c5-bac5-42c6-8445-25b1ffee3c27/AustrianPOsitioningService-Broschuere.pdf
- LKO eAMA APOS FAQ: https://www.lko.at/kostenfreier-rtk-korrekturdatendienst-hier-geht-s-zu-allen-infos-und-zur-registrierung+2400+3309904 (WebFetch 2026-05-15 OK; €150/yr de-minimis figure + 2027 sunset of declaration)
- EPOSA homepage: https://www.eposa.at/en/ (WebFetch OK)
- EPOSA Echtzeit-Positionierung: https://www.eposa.at/en/echtzeit-positionierung (WebFetch OK)
- EPOSA Abrechnungsmodelle (billing models, no prices): https://www.eposa.at/abrechnung (WebFetch OK)
- EPOSA FAQ (mountpoint names, signup): https://www.eposa.at/en/faq (WebFetch OK)
- EPOSA Infrastruktur: https://www.eposa.at/en/infrastruktur (WebFetch OK — "more than 40 + 9 external")
- ArduSimple Austria caster overview: https://www.ardusimple.de/rtk-correction-services-and-ntrip-casters-in-austria/ (WebFetch OK)
- Live curl probes 2026-05-17 (re-confirm; 2026-05-15 deep-probe unchanged):
  - `aposrtk.bev.gv.at:2101/` → HTTP/0.9 200, Trimble Ntrip Caster 4.3, 7 STR rows (`APOS_DGPS`, `APOS_NET3`, `APOS_VRS`, `APOS_VRS3`, `APOS_VRS32_MSM`, `APOS_VRS32_MSM_3D`, `APOS_VRS32_GRID2021`)
  - `ntrip.eposa.at:2101/sourcetable.txt` → 51 STR rows incl. 39 `*-RAW-4G` physical stations (set unchanged from 2026-05-15)
- Local pipeline data (`scripts/stations_by_country.py AUT`, 2026-05-17): 14 rtk2go + 1 Centipede (BOKU) + 4 EUREF-IP (GRAZ, PFA3, SBG2, TRF2) + 2 IGS-IP (GRAZ, GRZ2).
