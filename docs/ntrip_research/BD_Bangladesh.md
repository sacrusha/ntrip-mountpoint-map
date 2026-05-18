# Bangladesh [BD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-15; data.sob.gov.bd login portal re-verified live with signup form; SoB main `sob.gov.bd` direct WebFetch still fails certificate validation from sandbox; no change to declared VRS endpoint, station count, or pricing publication status)

## Status: YES — Survey of Bangladesh national VRS NTRIP service (paid, subscription via SoB Data Service portal); plus 2 Centipede volunteer bases (Dhaka, Chittagong)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — SoB VRS (paid, national) + 2 Centipede volunteer nodes (BENGLA2 near Dhaka, BENGLA4 near Chittagong) |
| **Operator** | Survey of Bangladesh (SoB / বাংলাদেশ জরিপ অধিদপ্তর), Ministry of Defence |
| **Network name** | SoB GNSS CORS Network (6 stations) feeding a VRS service ("SOB VRS WEB") |
| **landing_url** | https://data.sob.gov.bd/ — SoB Data Service portal (sandbox-reachable; login + signup form 200 OK 2026-05-15; canonical operational landing for RTK service request). Informational page on main site: `https://sob.gov.bd/site/page/2e0fd063-09e4-4512-a470-a5fbd3668c71/Geodetic-` (trailing hyphen is the literal CMS slug — verified via Google index 2026-05-17, not a truncation; sandbox cannot WebFetch directly because of cert-chain validation on sob.gov.bd). |
| **access_url** | https://data.sob.gov.bd/ (signup → request RTK service); ArduSimple lists `http://202.40.181.3:8021` as legacy registration / coverage portal |
| **host:port — SoB VRS** | `202.53.170.98:8011` (declared on SoB Geodetic Service page). Legacy candidate `202.40.181.3:8021` is the older portal IP per ArduSimple; should be treated as potentially stale. Direct curl from this sandbox not possible (sandbox lacks egress to Bangladeshi IPs). **Alive status unconfirmed** — primer [reachability]: extraordinary evidence that target user can reach is not demonstrated from this sandbox (no operator-side status page, no third-party probe with date stamp, only the SoB page declaring the endpoint). Caster alive status pending an in-country or alternative-network probe. |
| **vrs** | Yes — SoB documentation describes a "Virtual Reference Station Software" running on the data-centre server, computed against the 6 CORS plus surrounding IGS reference stations |
| **tariff — SoB** | Subscription required; pricing **not published** anywhere on `sob.gov.bd` or `data.sob.gov.bd` (verified 2026-05-15). Payment historically accepted via Rocket / bKash / SureCash (Bangladeshi mobile-banking platforms) per SoB data-service model. Date observed: 2026-05-15. |
| **num_stations** | 6 confirmed (operator-verified: Dhaka, Chittagong, Rajshahi, Khulna, Maulavibazar, Rangpur — operational since 19 December 2011). Expansion to ~73 announced but unverified (no operator status page, completion date, or ground-truth confirmation found 2026-05-17). |
| **hobbyist_eligibility** | yes — no professional-licence gate stated on SoB Data Service portal. Practical-access barrier (Bengali-first UI + Bangladeshi mobile number for signup + mobile-banking payment) is UX, not a legal eligibility restriction; see context note below. ArduSimple notes UX is "not very user-friendly". |
| **legal_residency_required** | no — not explicitly required. Practical barrier (Bangladeshi phone number / mobile-banking account for payment) is a payment-rail issue, not a legal residency gate; see context note below. |
| **last_confirmed_alive** | 2026-05-15 — `data.sob.gov.bd` login portal reachable and responsive (signup flow visible). SoB main domain reachable via mirror `sob.portal.gov.bd`. Direct TCP probe of `202.53.170.98:8011` from this sandbox not possible (sandbox egress restricted). ArduSimple Bangladesh page refreshed 2026-05-15. |
| **datum_epoch** | Omitted — no citable official declaration found. Howlader (UN-GGIM-AP) PDF on Bangladesh geodetic reference frame exists but the file delivered was image-only (no extractable text). EPSG references Bangladesh as using Gulshan 303 (historic) and WGS 84 / TM 90 NE (current projection) but neither is a citable SoB datum+epoch declaration. |

---

## Context Notes

- **Practical-access barriers (not legal/eligibility barriers):** SoB Data Service portal signup is Bengali-first, requires a Bangladeshi mobile number for OTP, and payment historically routes through Rocket / bKash / SureCash mobile-banking platforms which themselves require a Bangladeshi phone + bank account. A foreign hobbyist without a BD phone and BD mobile-banking account effectively cannot complete signup or pay — but this is a UX + payment-rail constraint, not a stated professional-licence requirement or legal residency rule. Practical implication: same as a hard restriction for foreign hobbyists; conceptually distinct.
- **Centipede mountpoints BENGLA2 / BENGLA4 are not blocked by any of the above** — they sit on `crtk.net:2101` with shared credentials and need no SoB account.

---

## CORS / VRS Network

- **Six permanent GNSS reference stations**, operational since 19 December 2011: Dhaka, Chittagong, Rajshahi, Khulna, Maulavibazar, Rangpur.
- VRS software on the SoB data-centre server synthesises corrections from the 6 CORS plus surrounding IGS stations.
- Service objectives (per SoB): RTK and post-processing GNSS, tectonic-plate-movement monitoring, earthquake-vulnerability prediction, geodetic-control-network upgrades.
- "GNSS CORS Network expansion" programme on `sob.gov.bd` targets ~73 additional locations; completion not verified for 2026.

---

## Volunteer (Centipede) Coverage

Per `data/stations.json` and Centipede roster, two BGD-coded nodes:

- **BENGLA2** — 23.7220°N, 90.4010°E (Dhaka area). Stream via `crtk.net:2101` (canonical Centipede host since 2025-03-18; legacy `caster.centipede.fr:2101` still resolves but migration not guaranteed indefinitely). Free, no rover registration.
- **BENGLA4** — 22.2700°N, 91.8120°E (Chittagong area). Same caster. Free, no rover registration.

Standard Centipede credentials `centipede` / `centipede`. RTCM3, NTRIP v1/v2.

No rtk2go BD-coded bases (`data/stations.json` confirms 0). No EarthScope/NOTA coverage (Bangladesh outside Americas-region scope). No IGS-RT mountpoint within Bangladesh.

---

## Hobbyist Path

1. **For Dhaka metro (~30 km of BENGLA2)**: use Centipede `crtk.net:2101` mountpoint `BENGLA2`. Free.
2. **For Chittagong (~30 km of BENGLA4)**: same caster, mountpoint `BENGLA4`. Free.
3. **National coverage / outside Centipede single-base range**: register at `data.sob.gov.bd`, request RTK service. Expect Bengali UI, mobile-banking payment, unpublished pricing.
4. **Otherwise**: local single-base RTK, or Galileo HAS (~40 cm, free, no internet).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| SoB Geodetic Service (informational; trailing hyphen is literal CMS slug) | https://sob.gov.bd/site/page/2e0fd063-09e4-4512-a470-a5fbd3668c71/Geodetic- | Online order + mobile-banking payment |
| SoB Data Service portal | https://data.sob.gov.bd/ | Login required |
| IGS archive (station DHAK / DHAKA, Dhaka) | https://igs.org/network/ | Free non-commercial |

---

## Sources Consulted (2026-05-15)
- SoB Geodetic Service page: https://sob.gov.bd/site/page/2e0fd063-09e4-4512-a470-a5fbd3668c71/Geodetic- — declares `202.53.170.98:8011` VRS endpoint and the six-CORS network. Sandbox probe: TLS cert verification fails on direct WebFetch, but Bengali mirror `sob.portal.gov.bd` reachable via Google index; content confirmed via WebSearch snippet 2026-05-15.
- SoB main site: https://sob.gov.bd — direct WebFetch failed (cert chain). Mirror `sob.portal.gov.bd` reachable.
- SoB Data Service portal: https://data.sob.gov.bd/ — WebFetch 2026-05-15 returned a working login + signup form; no pricing on the page; no mention of NTRIP/RTK/VRS on the landing page itself (gated behind login).
- ArduSimple Bangladesh page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bangladesh/ — WebFetch 2026-05-15 OK; lists `http://202.40.181.3:8021` as registration portal + `Map/SensorMap.aspx` coverage map; no pricing.
- UN-SPIDER SoB profile: https://www.un-spider.org/survey-bangladesh-sob — background only.
- Wikipedia "Survey of Bangladesh": https://en.wikipedia.org/wiki/Survey_of_Bangladesh — background only.
- UN-GGIM-AP "Geodetic Infrastructure and Reference Frame of Bangladesh" (Howlader): https://un-ggim-ap.org/sites/default/files/media/meetings/Plenary08/WG1_S2B_3%20Rouf%20Howlader_Geodetic%20Infrastructure%20%20and%20Reference%20Frame%20of%20Bangladesh.pdf — PDF fetched 2026-05-15 but body was an embedded JPEG stream; no extractable datum/epoch declaration.
- Centipede-RTK docs: https://docs.centipede.fr/docs/centipede/3_connect_caster.html — confirms caster host:port + open hobbyist access.
- `data/stations.json` (local, 2026-05-15) — confirms BENGLA2 (23.7220, 90.4010) and BENGLA4 (22.2700, 91.8120) under country `BGD`; zero rtk2go BD entries.
- `scripts/stations_by_radius.py 23.81 90.41 100` (local, 2026-05-15) — confirms BENGLA2 at 9.8 km from Dhaka centre.
