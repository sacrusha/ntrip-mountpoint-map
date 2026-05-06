# UAE [AE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — DVRS (Dubai Municipality) active; professional application only; no hobbyist path confirmed; portal status uncertain

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (DVRS — restricted professional access) |
| **Network name** | DVRS — Dubai Virtual Reference System |
| **Operator** | Dubai Municipality, Survey Department |
| **host:port** | `geodubai.dm.gov.ae:2101` (historical; portal returning errors/timeouts as of 2026-04-30 — see below) |
| **VRS** | Yes — VRS method; RTCM corrections streamed back on NMEA GGA submission |
| **tariff** | Not publicly listed; professional application required via Dubai Municipality DM portal |
| **hobbyist_eligibility** | No confirmed hobbyist path; access is application-based, restricted to surveying, construction, GIS, and government contractors |
| **legal_residency_required** | Unclear; no explicit residency requirement stated but professional licensing implied |
| **last_confirmed_alive** | `geodubai.dm.gov.ae` portal page returned HTTP 200 (pages default.aspx) and a Registration page (Registration.aspx) found live on 2026-05-06; NTRIP port 2101 status unconfirmed from external IP |

---

## Service Details

### DVRS — Network Overview

**Established:** March 2002 (first NRTK network in the Middle East).
**Original infrastructure:** 5 continuously operating base stations (Leica hardware), GNSMART network processing (Geo++), RTCM output.
**Current scale (as of known public documentation):** 18+ 4-constellation reference stations covering Dubai Emirate, with VRS (Virtual Reference Station) corrections.
**Datum:** Dubai Local Coordinate System / UAE national geodetic datum.
**Signals:** GPS + GLONASS + Galileo + BeiDou (quad-constellation per networks.md entry).

### Portal Status (2026-04-30 / 2026-05-06)

The primary DVRS sub-page at `dm.gov.ae/survey-department/dubai-virtual-reference-station/` has been returning errors or 404, and was flagged in the project's investigation notes as of 2026-04-30 as "returning errors — service may have been restructured or migrated to DM e-services." The GeoDubai portal (`geodubai.dm.gov.ae`) pages (`/en/Pages/default.aspx`, `/sites/buildingsmart/en/Pages/Registration.aspx`) were confirmed reachable on 2026-05-06 via indexed links. The NTRIP port 2101 on the historical hostname was not confirmed from an external IP.

**Likely explanation:** Dubai Municipality may have migrated the DM survey portal to their unified e-services infrastructure. The GeoDubai portal remains the access front-end; the underlying caster hostname/port may have changed. Credentials were always issued via the DM portal application, not a public self-registration page.

### Access Method

Surveyors and licensed professionals submit a request via the DM portal (or historically directly to the Survey Department) and receive DVRS NTRIP credentials. The NTRIP connection returns VRS-corrected RTCM data on submission of a NMEA GGA sentence from the rover. RINEX data download for select GNSS stations is also available via the portal.

Known users: RTA, DEWA, military departments, private construction companies, infrastructure developers. No hobbyist or individual tier is documented.

---

## Other Emirates — Known Gaps

No separate Abu Dhabi, Sharjah, or UAE-federal NTRIP caster endpoint has been publicly documented:

- **Abu Dhabi / ADSIC / HAAD / DMA:** Abu Dhabi has CORS infrastructure (the station ADCC appears in academic NetworkRTK literature), but no public NTRIP caster URL or registration page has been identified for Abu Dhabi Emirate.
- **Sharjah:** No independent Sharjah CORS NTRIP endpoint found.
- **Federal / UAE national caster:** No UAE-federal NTRIP network found; each emirate manages its own geodetic infrastructure.
- **rtk2go / Centipede:** Zero AE stations on rtk2go or Centipede as of 2026-05-06.
- **GEODNET:** The GEODNET coverage map (rtk.geodnet.com) is referenced as a global commercial option; no confirmed UAE GEODNET station count was found in public search results.

---

## Commercial Alternatives

No independent commercial NTRIP provider with confirmed UAE coverage (other than DVRS via Dubai Municipality) has been identified from public sources. Global commercial networks (GEODNET, PointOne, HxGN SmartNet) do not list confirmed UAE coverage from public documentation.

Global free fallback: **Galileo HAS** (~40 cm accuracy, no connectivity required, globally available including UAE).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **DVRS / GeoDubai** — RINEX data download for select GNSS stations | https://geodubai.dm.gov.ae/ | Requires DM portal account; professional access |
| **IGS / EarthScope** — regional IGS-affiliated station(s) in or near UAE | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

---

## Negative Findings

- `dm.gov.ae/survey-department/dubai-virtual-reference-station/` — returning errors / 404 as of 2026-04-30
- `geodubai.dm.gov.ae:2101` — NTRIP sourcetable not confirmed from external IP
- rtk2go: zero AE mountpoints
- Centipede: zero AE nodes
- No Abu Dhabi, Sharjah, or federal UAE NTRIP caster found
- ArduSimple UAE page mentions "National RTK Network" and DVRS but lists no alternative hobbyist-accessible NTRIP casters with endpoints

---

## Sources Consulted
- Dubai Municipality DVRS page: https://www.dm.gov.ae/survey-department/dubai-virtual-reference-station/
- GeoDubai portal: https://geodubai.dm.gov.ae/en/Pages/default.aspx
- GeoDubai Registration page: https://geodubai.dm.gov.ae/sites/buildingsmart/en/Pages/Registration.aspx
- Geospatial World interview — "Dubai's Reference Station, Middle East's First": https://geospatialworld.net/prime/interviews/dubai-reference-station-middle-east-first/
- ResearchGate — "Testing the Dubai Virtual Reference System (DVRS) National GPS-RTK Network": https://www.researchgate.net/publication/299730995_Testing_the_Dubai_Virtual_Reference_System_DVRS_National_GPS-RTK_Network
- Geospatial World — "Establishment & Testing of DVRS": https://geospatialworld.net/article/establishment-testing-of-dubai-virtual-reference-system-dvrs-national-gps-rtk-network/
- ArduSimple UAE NTRIP page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-uae-united-arab-emirates/
- GEODNET coverage map: https://rtk.geodnet.com/coverage/
- networks.md entry `dvrs` (project internal, date_added 2026-04-30)
- country-survey.md entry `AE — UAE` (project internal, date_added 2026-04-30)
- Investigation notes next.txt entry 82 (project internal)
