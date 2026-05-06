# Sri Lanka [LK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — active private commercial NTRIP caster (CORSnet); subscription required, pricing not public

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private commercial; subscription required) |
| **Operator** | CORSnet (Pvt) Ltd (spun off from SULECO Pvt Ltd, which launched the network in 2014) |
| **Network name** | CORSnet |
| **host:port** | `corsnet.lk:2101` (standard NTRIP port; host confirmed via website; mountpoints provided post-subscription via dashboard) |
| **tariff — CORSnet** | Not publicly listed in LKR or any currency; multiple subscription packages exist — contact info@corsnet.lk or CORSnet dashboard for current rates. Testimonials cite "affordable pricing." |
| **hobbyist_eligibility** | Yes — open to all individuals; user categories include surveying, construction, GIS, drone operations, precision agriculture; no professional credential requirement stated |
| **legal_residency_required** | No — non-residents can subscribe; no residency requirement stated |
| **last_confirmed_alive** | corsnet.lk homepage returned content (21 stations, 315+ customers, 172,000+ RTK-hours) on WebFetch 2026-05-06. curl probe of corsnet.lk:2101 NOT executed — see Sources. |

## Most Recent Project Announcement

- **2024 (ongoing)**: CORSnet describes itself as "the largest and most trusted RTK network in Sri Lanka," with 21 CORS stations islandwide and 315+ active customers. 172,000+ RTK service-hours on record.
- **20 May 2014**: CORSnet launched by SULECO (Pvt) Ltd — first islandwide CORS RTK network in Sri Lanka, initially covering Western and Sabaragamuwa provinces.
- **2014–present**: Network expanded to whole-island coverage; operations transferred to CORSnet (Pvt) Ltd as separate entity.

Note: SULECO's own service page (sulecoltd.com/cors-rtk/) states 17 reference stations; CORSnet's homepage states 21. Discrepancy may reflect pages being updated at different times. 21 is the more current figure per the primary CORSnet homepage (2026-05-06).

## Context Notes

- **CORSnet** is Sri Lanka's only known islandwide commercial NTRIP RTK network. Operated by CORSnet (Pvt) Ltd; technical and sales support provided by parent/affiliate SULECO (Pvt) Ltd.
- **Station count**: 21 CORS stations "strategically positioned across Sri Lanka" per corsnet.lk homepage (2026-05-06). SULECO's page quotes 17 — use 21 as current.
- **Services**: Differential GNSS (DGNSS, sub-metre), single-base RTK, Network RTK (NRTK / VRS), RINEX post-processing — all via NTRIP and TCP/IP. Correction formats supported: RTCM 2.x / 3.x, CMR, CMR+, sCMRx, RTD, NMEA.
- **Accuracy**: 2.5 mm + 0.5 ppm (static mode); 15 mm + 1 ppm (RTK mode) per published specs.
- **Pricing**: Not publicly disclosed. Multiple subscription packages exist; rates provided on inquiry. No LKR amounts found in any public source as of 2026-05-06. "Affordable pricing" mentioned in customer testimonials.
- **Access procedure**: Contact CORSnet (info@corsnet.lk or phone) → receive subscription package details → pay → account activated → NTRIP credentials and mountpoint list delivered via CORSnet Dashboard.
- **Mountpoints**: Not publicly listed; provided to subscribers via dashboard after account activation.
- **Survey Department of Sri Lanka** (survey.gov.lk): Does not operate a separate public NTRIP service.
- **Global fallbacks**: GEODNET and ONOCOY coverage for Sri Lanka not confirmed at research date. No Sri Lanka stations visible in RTK2go or Centipede sourcetables.
- **Contact — CORSnet/SULECO**:
  - CORSnet: info@corsnet.lk · corsnet.sup@gmail.com · +94 77 213 1310 · +94 77 038 2265
  - SULECO general: +94 11 282 8100 · sulecoltd@sltnet.lk · sales@suleco.lk
  - SULECO technical support: technical@sulecoltd.com · +94 77 359 5396
  - Address: No. 44, Baddagana South Road, Sri Jayawardenepura Kotte 10100, Sri Lanka
  - Office hours: 24/7 support advertised.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **CORSnet RINEX download** — available to active subscribers | https://corsnet.lk/ | Included in subscription (pricing on inquiry) |
| **EarthScope / GAGE archive** — scientific GNSS stations in region | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- CORSnet homepage (21 stations, 315+ customers): https://corsnet.lk/
- CORSnet about page: https://corsnet.lk/about-us/
- CORSnet launch announcement (May 2014): https://corsnet.lk/news/ambitious-launch-of-the-cors-network-in-sri-lanka/
- SULECO CORSnet page (17 stations cited): https://sulecoltd.com/cors-rtk/
- SULECO contact page (full contact directory): https://sulecoltd.com/contact/
- SULECO company overview: https://sulecoltd.com/about/
- ArduSimple Sri Lanka listing: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- Survey Department of Sri Lanka: https://survey.gov.lk/sdweb/home.php
- curl probe of `corsnet.lk:2101` — NOT EXECUTED: sandbox TCP/shell tools blocked during research 2026-05-06. corsnet.lk WebFetch returned page content confirming active service 2026-05-06. Direct SOURCETABLE response NOT independently confirmed.
