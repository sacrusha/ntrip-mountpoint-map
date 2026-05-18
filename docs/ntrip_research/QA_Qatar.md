# Qatar [QA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-12)

## Status: YES — QCORS active (9 stations); subscription required; restricted to gov/licensed surveyors; no hobbyist path confirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — QCORS (restricted access) |
| **Network name** | QCORS — Qatar Continuously Operating Reference Stations |
| **Operator** | CGIS — Centre for GIS, Ministry of Municipality (State of Qatar) |
| **host:port** | Not publicly disclosed; issued post-subscription |
| **VRS** | Likely yes — 9-station network with TCP/IP data center, web portal; ±2 cm horizontal accuracy claimed |
| **tariff** | Not publicly listed; subscription via CGIS application |
| **hobbyist_eligibility** | Unclear — described as serving "government and private survey and mapping communities"; no confirmed individual/hobbyist tier |
| **legal_residency_required** | Unclear — no explicit restriction found; non-resident eligibility unconfirmed |
| **datum_epoch** | omitted -- no citable operator declaration for NTRIP output frame on CGIS portal. |
| **last_confirmed_alive** | CGIS portal `gisqatar.org.qa` referenced (HTTP 200, 2026-05-06); 2026-05-17 WebFetch returned empty body. No NTRIP-specific endpoint reachable from public sources. |

---

## Service Details

### QCORS — Network Overview

**Established:** Network installed 2009, operations commenced 2010.
**Operator:** CGIS (Centre for GIS) under Qatar's Ministry of Municipality (formerly Ministry of Municipality and Environment).
**Stations:** 9 reference stations connected via TCP/IP protocol; data transmitted to a central data center.
**Accuracy:** ±2 cm horizontal, ±10 cm vertical across Qatar's territory.
**Datum / Reference:** Not declared on CGIS portal (omitted per citation rule).
**Signals:** Multi-constellation GNSS (exact constellation mix not confirmed from public docs; system pre-dates mass BeiDou deployment).

### Access Policy

QCORS is described in academic and government sources as serving "government and private survey and mapping communities" requiring subscription. The service provides "economical advantages against conventional GNSS surveying where two GPS units are necessary." No public self-registration page or hobbyist tier has been identified. Access requires application to CGIS.

**CGIS contact (from public sources):**
- Telephone: +974 4426 6284
- Fax: +974 4426 2532
- Email: cgisinfo@gisqatar.org.qa
- Portal: https://www.gisqatar.org.qa/

### Territory Context

Qatar is small (~11,586 km², peninsula jutting into the Persian Gulf). A 9-station network is sufficient for national RTK coverage. Despite this modest scale, no public NTRIP endpoint has been disclosed.

### CGIS GeoPortal

A CGIS GeoPortal (`geoportal.gisqatar.org.qa/qmape/`) is live and provides GIS web mapping services. The RTK/NTRIP corrections service is separate and gated behind CGIS subscription approval.

---

## Commercial Alternatives

No independent commercial NTRIP provider with confirmed Qatar coverage has been identified. Global networks (GEODNET, PointOne, HxGN SmartNet, ONOCOY) do not list Qatar in confirmed coverage maps from public documentation.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **CGIS / QCORS** — RINEX data download (via CGIS subscription, if granted) | https://www.gisqatar.org.qa/ | Subscription required; fee unknown |
| **IGS / EarthScope** — check for any IGS station in Qatar | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

---

## Negative Findings

- QCORS NTRIP caster host:port not publicly disclosed (re-checked 2026-05-12)
- Tariff / fee schedule not publicly documented
- Hobbyist eligibility: unclear (not explicitly denied but no individual tier documented)
- rtk2go: zero QA mountpoints (re-confirmed `py scripts/stations_by_country.py QAT` → "No stations for 'QAT'", 2026-05-17)
- Radius probe `py scripts/stations_by_radius.py 25.3 51.5 200` 2026-05-17 → zero stations of any source within 200 km of Doha
- Centipede: zero QA nodes
- EarthScope NOTA: not applicable (NOTA is Americas-only)
- GEODNET, PointOne, HxGN SmartNet: no Qatar coverage confirmed in public docs
- No "World Cup legacy" commercial NTRIP network; FIFA 2022 World Cup construction drove no open-access CORS beyond QCORS
- WebSearch 2026-05-17 — no public host:port, tariff, or hobbyist-tier announcement located; CGIS most-recent news = aerial mapping 2021-2025 + Qatar Vision 2030 digital-twin plan (no QCORS public-access change)

---

## Sources Consulted
- Investigation notes next.txt entry 86 (project internal)
- country-survey.md entry `QA — Qatar` (project internal, date_added 2026-04-28)
- CGIS portal: https://www.gisqatar.org.qa/en/page3/test.html (Services)
- CGIS About page: https://gisqatar.org.qa/en/page1/test.html
- CGIS GeoPortal: https://geoportal.gisqatar.org.qa/qmape/
- CGIS on Geospatial World: https://resource.geospatialworld.net/user/centre-for-gis-qatar-cgis
- Qatar e-government portal — "Request Geographic Information System Software Licenses": https://portal.www.gov.qa/wps/portal/Home/Government-Services/
- Qatar Survey Manual (PDFCOFFEE): https://pdfcoffee.com/qatar-survey-manual-pdf-free.html
- UN-GGIM Exchange Forum 2013 — "Qatar's GIS Cooperation with Local Community": https://ggim.un.org/ggim_20171012/docs/meetings/Exchange_Forum_2013/Opening%20Remarks/ExchangeForum_CGIS-Qatar_El-WahabHamouda.pdf
- mvarga1989 GitHub — community CORS/RTK networks list (Qatar not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- ArduSimple country listing (Qatar not listed with dedicated page): https://www.ardusimple.com/rtk-correction-services-in-your-country/
