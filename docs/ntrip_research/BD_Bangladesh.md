# Bangladesh [BD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: YES — Survey of Bangladesh national VRS NTRIP service (free RINEX + paid RTK with mobile-banking payment); plus 1 Centipede node in Chittagong

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government VRS) + 1 Centipede volunteer node (BENGLA4) |
| **Operator** | Survey of Bangladesh (SoB / বাংলাদেশ জরিপ অধিদপ্তর), Ministry of Defence |
| **Network name** | SoB GNSS CORS Network (6 stations) feeding a VRS service ("SOB VRS WEB") |
| **host:port — SoB VRS** | `202.53.170.98:8011` (current per SoB; older `202.40.181.3:8021` recorded by ArduSimple is likely the legacy portal IP — both should be treated as candidate endpoints pending direct probe) |
| **VRS** | Yes — described by SoB as a "Virtual Reference Station Software" running on the data-centre server, computed against the 6 CORS stations plus surrounding IGS reference stations |
| **tariff — SoB** | Subscription required; pricing not posted on the public site. Payment is accepted via **Rocket / bKash / SureCash** (Bangladesh mobile-banking platforms), confirming an active commercial subscription tier intended also for domestic individuals |
| **hobbyist_eligibility** | Open in principle — registration is via the SoB Data Service portal (`data.sob.gov.bd`) with no professional-licence prerequisite stated. ArduSimple notes the portal is "not very user-friendly"; expect a Bengali-only or limited-English UX |
| **legal_residency_required** | Not explicitly required; however mobile-banking payment options (Rocket / bKash / SureCash) effectively favour applicants with a Bangladeshi phone number / bank account |
| **last_confirmed_alive** | 2026-05-12 — `sob.gov.bd` reachable; Bengali Geodetic Service page mentions SOB VRS WEB at `202.53.170.98:8011`; direct curl of the caster port not executed from this environment. ArduSimple page last refreshed Aug 2025 |

---

## CORS / VRS Network

- **Six permanent GNSS reference stations**, operational since 19 December 2011:
  Dhaka, Chittagong, Rajshahi, Khulna, Maulavibazar, Rangpur.
- SoB documentation mentions a current programme to expand the network to ~73 additional locations ("GNSS CORS Network expansion" page on `sob.gov.bd`); ground-truth completion status as of 2026 not confirmed.
- Inside the SoB data centre, VRS software synthesises corrections from the 6 CORS plus surrounding IGS stations.
- Service objectives (per SoB): RTK and post-processing GNSS, tectonic-plate-movement monitoring, earthquake-vulnerability prediction, and Bangladesh geodetic-control-network upgrades.

---

## Volunteer (Centipede) Coverage

- **BENGLA4** — Centipede node near Chittagong (22.27°N, 91.81°E), country code `BGD`. Single base; usable for hobbyist RTK within ~20–30 km of Chittagong. Stream via `caster.centipede.fr:2101`. Free, no registration of the rover required.
- No rtk2go BD-coded bases confirmed.
- No EarthScope / NOTA coverage (Bangladesh outside Americas-region NOTA scope).

---

## Hobbyist Path

1. **For Chittagong / SE Bangladesh**: connect a rover to Centipede `caster.centipede.fr:2101` mountpoint **BENGLA4** — free, no signup. Useful within ~30 km of the base.
2. **For Dhaka / national coverage**: register at `data.sob.gov.bd`, request RTK service, expect to pay via Rocket / bKash / SureCash. Pricing is not published; you will need a Bangladeshi mobile-banking account to actually transact.
3. **Outside both**: set up a local base station (single-base RTK) or use **Galileo HAS** (~40 cm, free, no internet required).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **Survey of Bangladesh — Geodetic Service** | https://sob.gov.bd/site/page/2e0fd063-09e4-4512-a470-a5fbd3668c71/Geodetic- | Online order + mobile-banking payment |
| **SOB Data Service portal** | https://data.sob.gov.bd/ | Login required |
| **SOB VRS WEB (RTK service entry point)** | http://202.53.170.98:8011 (current) · http://202.40.181.3:8021 (legacy) | Subscription |
| **IGS archive** — IGS station DHAK (Dhaka) for post-processing reference | https://igs.org/network/ | Free non-commercial |

---

## Sources Consulted
- SoB Geodetic Service page (English): https://sob.gov.bd/site/page/2e0fd063-09e4-4512-a470-a5fbd3668c71/Geodetic- (observed 2026-05-12 — confirmed `202.53.170.98:8011` VRS endpoint and the six-CORS network)
- SoB main site (Bengali / English): https://sob.gov.bd (observed 2026-05-12)
- SoB CORS expansion page: https://sob.gov.bd/site/page/5d6a4fc0-34b2-42f4-86c5-1fefc9b97e58/-
- SoB Data Service portal: https://data.sob.gov.bd/
- Bangladesh national portal page on SoB: http://gis.gov.bd/en/organization_profile.php?organization=39
- ArduSimple Bangladesh NTRIP page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bangladesh/ (lists `202.40.181.3:8021` as the registration portal — likely legacy; UX noted "may not be very user-friendly")
- Wikipedia "Survey of Bangladesh" article: https://en.wikipedia.org/wiki/Survey_of_Bangladesh
- UN-SPIDER SoB profile: https://www.un-spider.org/survey-bangladesh-sob
- `data/stations.json` 2026-05-12 — Centipede `BENGLA4` Chittagong [BGD] confirmed; zero rtk2go BD entries
