# Bahrain [BH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: YES — SLRB PRN (Permanent Reference Network) is FREE for registered users; covers entire kingdom; access by email application

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (registration required; free) |
| **Network name** | PRN — Permanent Reference Network |
| **Operator** | Survey & Land Registration Bureau (SLRB), Kingdom of Bahrain |
| **host:port** | Not publicly advertised on SLRB website; issued in registration email after application |
| **VRS** | Likely yes (network-RTK service per SLRB description "real-time correction… through GPS network"); not explicitly stated in public material |
| **tariff** | **Free of charge** — explicit note on SLRB PRN subscription page: "this service may incur charges in the future" but at observation date the service is free |
| **hobbyist_eligibility** | Yes in principle — application form accepts both "Individual" and "Agent" applicant types; no licensed-surveyor requirement stated. Practical eligibility may favour Bahraini residents/professionals |
| **legal_residency_required** | Not stated as a hard requirement in the public terms; mailing address on the application form supports both local and foreign applicants in principle |
| **last_confirmed_alive** | 2026-05-12 — `slrb.gov.bh/en/permanent-reference-networkprn` returned the live PRN subscription page; processing time stated as 1–2 working days |

---

## Service Details

### Application Process

1. Download the **GPS Network Application Form** from the SLRB PRN subscription page (`slrb.gov.bh/en/permanent-reference-networkprn`).
2. Send the completed form together with a covering letter to **PRN@slrb.gov.bh**.
3. SLRB issues credentials within **1–2 working days**.
4. Use of permission is limited to **one device per credential**; sharing access is prohibited.

### Coverage

The PRN provides the geodetic basis for all surveying operations in Bahrain. Per SLRB documentation the **whole of Bahrain** is supported with this service. Service is available **24 / 7**. Bahrain's territory is small (~765 km²) and a single well-sited reference station can cover the entire kingdom within typical RTK baseline limits (~30 km); SLRB does not publicly disclose the number or location of physical reference stations.

### Technical Specifications

Specific technical specifications (NTRIP host:port, mountpoint names, RTCM versions, VRS type, supported constellations) are **not published on the public SLRB website** and are issued only in the credentials email. SLRB describes the service as "Real-Time Correction Service for Surveying through GPS Network."

### Contact

- **Email**: PRN@slrb.gov.bh (preferred) or info@slrb.gov.bh
- **Phone**: +973 17507000
- **Address**: Building 517, Road 1010, Manama 410, Kingdom of Bahrain
- **Application page**: https://www.slrb.gov.bh/en/permanent-reference-networkprn

---

## Volunteer / Community Coverage

- **rtk2go**: zero BH-coded mountpoints (verified via `data/stations.json` 2026-05-12).
- **Centipede-RTK**: zero BH nodes.
- **No stations within 100 km of Manama** (26.0, 50.55) on rtk2go, Centipede, or EarthScope. Bahrain's only realistic free-RTK path is therefore the SLRB PRN itself.

---

## Commercial / Cross-Border Alternatives

No independent commercial NTRIP provider with confirmed Bahrain coverage has been identified. Global networks (GEODNET, PointOne, HxGN SmartNet, ONOCOY, Swift Skylark) do not list Bahrain in coverage maps from public documentation.

**KSA-CORS spill (cross-border)**: KSA-CORS stations near Dammam / Al-Ahsa (Eastern Province, Saudi Arabia) are approximately 25–50 km from Bahrain Island. KSA-CORS VRS *may* provide marginal RTK coverage in Bahrain — especially in the northern Manama / Muharraq area — but this is unconfirmed, and KSA-CORS has reachability issues from non-SA IPs (see SA_SaudiArabia.md). Now that SLRB PRN is free, the KSA-CORS fallback is no longer needed.

**Global free PPP fallback**: **Galileo HAS** (~40 cm accuracy, no connectivity required, globally available including Bahrain).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SLRB PRN RINEX** — likely available to subscribers; not publicly documented as a separate product | https://www.slrb.gov.bh/en/permanent-reference-networkprn | Free / contact required |
| **IGS / EarthScope** — no IGS station in Bahrain in current public station list | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

---

## Key Update vs. Prior Research

The prior version of this file recorded the PRN as access-restricted to licensed surveyors with no public registration path. **That was incorrect.** SLRB publishes a clear self-service registration path (downloadable application form, email to PRN@slrb.gov.bh, 1–2 day processing) and explicitly states the service is **free of charge** at the present time. This re-classifies Bahrain from "no free NTRIP" to "free national NTRIP with registration."

---

## Sources Consulted
- SLRB PRN subscription page: https://www.slrb.gov.bh/en/permanent-reference-networkprn (WebFetch 2026-05-12: free of charge, application by email, 1–2 day processing, 24/7 availability, individual or agent applicants)
- SLRB E-Services page: https://www.slrb.gov.bh/en/e-services
- SLRB main site: https://www.slrb.gov.bh/en/
- SLRB PRN information page (Arabic-language general info): https://www.slrb.gov.bh/InformationCenter/GeneralInfoDetail/?PageId=942&ChnlId=63&ChnlId2=62 (404 at observation; English page is canonical)
- ArduSimple Bahrain NTRIP page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kingdom-of-bahrain/ (observed 2026-05-12: mentions PRN as free national service with coverage map; no host:port published)
- mvarga1989 GitHub CORS list (Bahrain not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- `data/stations.json` verified 2026-05-12: zero BH-coded entries on rtk2go, Centipede, or EarthScope; zero stations within 100 km of Manama on any tracked free source
- SA_SaudiArabia.md (cross-border KSA-CORS context)
