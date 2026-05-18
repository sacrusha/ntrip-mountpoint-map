# Puerto Rico [PR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-12)

## Status: PARTIAL — real-time GNSS data via EarthScope NOTA (geodetic, non-commercial); 1 commercial VRS net (VRS Systems PR / HLCM); no free public RTK-VRS caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (geodetic, not RTK-VRS) — EarthScope NOTA streams 1 Hz GPS/GNSS data from Puerto Rico PBO stations via NTRIP. One commercial VRS network (VRS Systems PR, HLCM Group) exists with no public pricing. |
| **EarthScope NOTA — host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3) · `:2105` (BINEX) · `:2108` (point positioning) |
| **EarthScope NOTA — tariff** | Free for non-commercial use under NULA (Non-commercial Use Licence Agreement); commercial licensing: contact EarthScope |
| **EarthScope NOTA — eligibility** | Yes for non-commercial use; 1 Hz geodetic data, not a VRS RTK product — rover must handle baseline math |
| **VRS Systems PR — operator** | HLCM Group, Inc. (Trimble distributor for Puerto Rico and the Caribbean) |
| **VRS Systems PR — host:port** | Not publicly published; subscription required (contact 787-398-8852 or sales@hlcmgroup.com) |
| **VRS Systems PR — tariff** | Not publicly disclosed (commercial subscription only) |
| **VRS Systems PR — eligibility** | Commercial subscription — hobbyist tier not confirmed |
| **PRSN CORS** | NTRIP page on prsn.uprm.edu / redsismica.uprm.edu was previously referenced (country-survey.md); the project page link returns HTTP 404 / ECONNREFUSED on 2026-05-12; cannot confirm an active public NTRIP endpoint |
| **datum_epoch** | EarthScope NOTA → IGS20 (global, ITRF2020 realization). NGS PRMI station page declares NAD83(2011) for NCN-archived coords. RTK-VRS service (HLCM) does not publish a service-side datum. Citation: EarthScope at https://www.earthscope.org/data/gnss-realtime/. For HLCM commercial VRS: `omitted -- no citable operator declaration`. |
| **last_confirmed_alive** | EarthScope NOTA operational; PR-specific PBO stations (PRMI, PRGY, P780) streaming 2026-05-17 (P780 in earthscope ST at 18.08, -66.58 — local index). |

## Service Details

### EarthScope NOTA (free, non-commercial)

The NSF GAGE Facility (EarthScope Consortium) broadcasts 1 Hz GNSS data from ~1,100 NOTA stations including Puerto Rico stations via NTRIP at `ntrip.earthscope.org`. Confirmed PR stations include PRMI, PRGY (both NCN/NOTA, PRGY coordinates updated Feb 2020 after the Jan 2020 earthquake) and P780 (visible in the project's earthscope sourcetable at 18.08, -66.58).

Real-time access requires an EarthScope account and acceptance of the NULA (Non-commercial Use Licence Agreement). Commercial use requires a separate license. The data is geodetic 1 Hz raw — not a VRS service; rovers must handle baseline computation to a single nearby NOTA station.

### VRS Systems PR / HLCM Group (commercial, paid)

VRS Systems PR is described as the only company in Puerto Rico that owns and operates a network RTK service. Operated by HLCM Group, Inc. (Trimble distributor). The network runs on Trimble Pivot Platform software. The July 2022 upgrade added Galileo and BeiDou observations alongside the existing GPS+GLONASS support. Service is described as 24/7.

No public NTRIP host:port, no published pricing, no published hobbyist tier. Station count: eight GPS/GNSS receivers around the island per HLCM marketing copy (hlcmgroup.com/vrs.php, July 2022 upgrade page; page returned 404 on 2026-05-12 but the figure is preserved in WebSearch cached snippets). Subscription contact: HLCM Group, 787-398-8852, sales@hlcmgroup.com.

### COCONet / Network of the Americas

COCONet (Continuously Operating Caribbean GPS Observational Network) is a 100+ station Caribbean network funded by NSF. Real-time 1 Hz streams in BINEX / RTCM 2.3 / RTCM 3.1 are available via NTRIP on request (email previously rtgps@unavco.org; UNAVCO is now folded into EarthScope/NOTA). Puerto Rico COCONet/PBO stations stream through `ntrip.earthscope.org` after the UNAVCO → EarthScope consolidation.

### PRSN CORS (status: unconfirmed)

The Puerto Rico Seismic Network (UPRM Mayagüez) operates 18 permanent GPS stations across PR, the US/British Virgin Islands and adjacent islands (Trimble Alloy, NetRS, NetR9 + Topcon). Their internal page `prsn.uprm.edu/English/research/geodesy/NTRIP_info.php` has been referenced in `country-survey.md` as describing an NTRIP service, but on 2026-05-12 the page returns HTTP 404 / ECONNREFUSED and no host:port has been independently confirmed from open sources. Treat the PRSN NTRIP service as unconfirmed pending direct UPRM contact.

## Context Notes

- **Puerto Rico is a US territory** — geodetic infrastructure falls under NOAA/NGS federal programs. NOAA NCN itself does not operate a public NTRIP caster; it releases RINEX within ~1 hr for post-processing.
- **No free public RTK/VRS caster** equivalent to US state RTN networks (InCORS, NC RTN, etc.). NGS encourages state DOTs / commercial partners to fill this gap; none free confirmed as of 2026-05-12. The only commercial RTN identified is VRS Systems PR (HLCM Group).
- **Local project data** — `py scripts/stations_by_country.py PRI` (2026-05-17) returns 1 rtk2go (PR-YAUCO1 at 18.02, -66.84) + 1 earthscope (P780 at 18.08, -66.58). Unchanged from prior. Volunteer presence minimal.
- **Commercial roaming networks** (Trimble VRS Now, Hexagon SmartNet): not extended to Puerto Rico per public coverage maps.
- **Practical option for hobbyists**: set up own base station; use EarthScope NOTA single-base on a nearby NOTA station; Galileo HAS (~40 cm, no internet); GEODNET coverage unconfirmed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **NOAA NCN RINEX archive** — Puerto Rico stations; data within ~1 hr | https://geodesy.noaa.gov/CORS/ | Free |
| **UNAVCO/EarthScope GNSS archive** — NOTA Puerto Rico stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (NULA) |

## Sources Consulted
- NOAA NCN main page: https://geodesy.noaa.gov/CORS/
- NOAA NCN data and products: https://geodesy.noaa.gov/CORS/data.shtml
- NOAA NCN station page — PRMI: https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=PRMI
- NGS Puerto Rico earthquake coordinate update (2020): https://geodesy.noaa.gov/web/news/coordinates-puerto-rico-earthquake.shtml
- EarthScope NOTA network: https://www.earthscope.org/nota/
- EarthScope real-time GNSS data (NTRIP): https://www.earthscope.org/data/gnss-realtime/
- COCONet project: https://coconet.unavco.org/
- VRS Systems PR (HLCM Group, 2022 upgrade page): https://www.hlcmgroup.com/vrs.php (page returned 404 on 2026-05-12; cached in WebSearch results)
- HLCM blog (Trusted technology, May 2025): https://blog.hlcmgroup.com/2025/05/26/trusted-technology-to-transform-infrastructure-in-puerto-rico-and-the-caribbean/
- HLCM Group: https://www.hlcmgroup.com/
- PRSN Mayagüez (research/geodesy/NTRIP): http://www.prsn.uprm.edu/English/research/geodesy/NTRIP_info.php (ECONNREFUSED 2026-05-12)
- PRSN instrumentation page: https://redsismica.uprm.edu/english/our_work/instrumentation.php
- ArduSimple USA page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- RTK2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Local `py scripts/stations_by_country.py PRI` (2026-05-17) — 1 rtk2go (PR-YAUCO1), 1 earthscope (P780)
