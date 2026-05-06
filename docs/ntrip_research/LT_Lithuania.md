# Lithuania [LT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — national NTRIP RTK caster operating (LitPOS); registration required; tariff not publicly listed (subscription-based; contact required)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | LitPOS (Lithuanian Positioning System) |
| **Operator** | GIS-Centras (National Centre for Remote Sensing and Geoinformatics), under Construction Sector Development Agency (formerly Nacionalinė žemės tarnyba prie Žemės ūkio ministerijos) |
| **host:port** | Not published on public web pages; issued to registered users. NTRIP caster accessed via geoportal.lt account. Connection settings in RTCM 2.1, 2.3, 3.1, 3.2, CMR, CMR+, CMRx formats |
| **VRS** | Yes — Network RTK / VRS corrections; ±2 cm RTK; DGPS (±0.3–0.5 m); GPPS (post-processing, up to 1 mm) |
| **tariff** | Not publicly listed on the English LitPOS pages; registration is via Google Form (geoportal.lt/web/litpos-en/registration). Pricing provided after registration approval. Anecdotal sources suggest service may be free or very low cost for Lithuanian state-sector users; private/commercial pricing unclear |
| **hobbyist_eligibility** | Unclear — registration form (Google Forms) is open to any applicant, but approval is by the operator. No explicit professional licence requirement found |
| **legal_residency_required** | Unclear — form is in English and Lithuanian; no explicit restriction, but contact info suggests Lithuanian entity preferred |
| **last_confirmed_alive** | 2026-05-06 (geoportal.lt/web/litpos-en loaded HTTP 200; registration, status, and application pages all accessible; GIS-Centras listed as manager of Spatial Information Portal) |

## Service Details

### Network
LitPOS consists of 35 permanent GNSS reference stations covering the entire territory of Lithuania, operational since July 2007. Average inter-station distance approximately 50 km.

### EUPOS integration
LitPOS is Lithuania's contribution to the EUPOS (European Position Determination System) consortium of 17 Central and Eastern European countries. LitPOS users can also access 3 ASG-EUPOS (Polish) stations and 6 LATPOS (Latvian) stations under EUPOS cooperation agreements, effectively extending coverage into neighbouring areas.

### Formats and accuracy
Real-time services: RTK (±2 cm), DGPS (±0.3–0.5 m), GPPS (post-processing up to 1 mm). Correction formats: RTCM 2.1, 2.3, 3.1, 3.2, CMR, CMR+, CMRx, DGPS RTCM 2.1–2.4.

### Registration
Registration is via a Google Forms application linked from the geoportal.lt/web/litpos-en/registration page. Users must create a geoportal.lt account. LitPOS credentials (username + password for NTRIP) are then issued by the operator (contact: LitPOS@geoportal.lt). There is no self-service credential issuance.

## Context Notes

- **Operator restructuring**: LitPOS was historically administered by Nacionalinė žemės tarnyba (National Land Service). As of 2025, the Spatial Information Portal of Lithuania (geoportal.lt) is managed by the Construction Sector Development Agency; GIS-Centras is listed as the technical operator in the footer. These transitions may have affected pricing and access policies.
- **Pricing opacity**: The English-language LitPOS pages list no tariffs. The Lithuanian-language portal (geoportal.lt, /litpos-paslauga path) also does not display prices publicly. One academic paper describes LitPOS as used "by governmental institutions as well as private sector," suggesting at minimum two user tiers exist.
- **Hobbyist note**: The lack of public pricing and the requirement for a Google Form application make LitPOS harder to access ad-hoc than some neighbouring national services (Latvia's LATPOS, Estonia's ESTPOS are similarly opaque). Contact LitPOS@geoportal.lt for current tariff information.
- **EUPOS reference**: The M3G GNSS metadata entry for LitPOS: https://gnss-metadata.eu/MOID/projnet.5f366a387e27d32c1b218ac2

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **LitPOS RINEX (GPPS post-processing)** | https://www.geoportal.lt/geoportal/web/litpos-en/application | Via subscription account |
| **EPN archive** | https://epncb.oma.be/ | Free |

## Sources Consulted
- LitPOS English about page: https://www.geoportal.lt/geoportal/web/litpos-en (HTTP 200, 2026-05-06)
- LitPOS registration page: https://www.geoportal.lt/geoportal/web/litpos-en/registration
- LitPOS application page: https://www.geoportal.lt/geoportal/web/litpos-en/application
- LitPOS status page: https://www.geoportal.lt/geoportal/web/litpos-en/status
- LitPOS contacts: https://www.geoportal.lt/geoportal/web/litpos-en/contacts
- M3G LitPOS GNSS metadata: https://gnss-metadata.eu/MOID/projnet.5f366a387e27d32c1b218ac2
- LitPOS performance analysis (Vilnius Tech, 2017): https://etalpykla.vilniustech.lt/bitstream/handle/123456789/155251/10th_ICEE_2017-161.pdf
- LitPOS Bernese processing paper: https://etalpykla.vilniustech.lt/handle/123456789/118908
- ArduSimple Lithuania: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-lithuania/
- NTRIP-list Europe: https://ntrip-list.com/europe/
