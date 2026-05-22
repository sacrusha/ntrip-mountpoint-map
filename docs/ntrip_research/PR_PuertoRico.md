# Puerto Rico [PR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior: 2026-05-17)

## Status

PARTIAL coverage. Two layers:

1. **EarthScope NOTA** (federal, free for noncommercial under NULA, USD 1,000/seat/yr commercial) — broadcasts 1 Hz raw RTCM 3.3 GNSS data from PBO stations in Puerto Rico via NTRIP at `ntrip.earthscope.org:2101`. NOT a VRS / Network-RTK product; rovers must handle the single-base baseline.
2. **VRS Systems PR (HLCM Group, Inc.)** — the only commercial Network-RTK service in Puerto Rico; Trimble Pivot Platform; 8 GPS/GNSS reference receivers around the island. NTRIP host:port not publicly published; no published tariff; subscription via HLCM Group.

A third operator, **PRSN / UPRM Mayagüez**, runs ~18 scientific GNSS stations across PR + adjacent islands + USVI for seismic/geodetic research. Its `prsn.uprm.edu` NTRIP-info page was historically referenced in third-party survey notes; both `prsn.uprm.edu` and `redsismica.uprm.edu/our_work/instrumentation.php` confirm GNSS stations exist but neither documents a public NTRIP service. PRSN's instrumentation page (2026-05-21) states real-time data is transmitted over VHF/UHF radios, spread-spectrum, microwave, satellite, and Internet to Mayagüez — no public NTRIP endpoint advertised.

| Field | Value |
|---|---|
| EarthScope NOTA — host:port | `ntrip.earthscope.org:2101` (RTCM 3.3) · `:2105` (BINEX) · `:2108` (point positioning) — `SOURCETABLE 200 OK` 2026-05-21 |
| EarthScope NOTA — tariff | Free for non-commercial use under NULA; commercial USD 1,000/seat/yr |
| EarthScope NOTA — eligibility | Yes for non-commercial use; raw 1 Hz geodetic data, not a VRS product |
| EarthScope NOTA — PR stations confirmed | Real-time NTRIP (2026-05-21 sourcetable snapshot): only `P780_RTCM3P3` (18.08, -66.58). PRMI and PRGY are historical NOTA PR stations and present in the EarthScope RINEX archive (post-processing), but neither appears in the live NTRIP sourcetable snapshot — they are RINEX-archive coverage only. PRGY coordinates were updated Feb 2020 by NGS after the Jan 2020 earthquake. |
| VRS Systems PR — operator | HLCM Group, Inc. (Trimble distributor for Puerto Rico and the Caribbean) |
| VRS Systems PR — host:port | Not publicly published; subscription only. |
| VRS Systems PR — access_url | n/a — no public registration or pricing page; subscription contact via HLCM Group corporate channels (see Service Details below) |
| VRS Systems PR — num_stations | 8 GPS/GNSS receivers around the island per the 2022 `hlcmgroup.com/vrs.php` upgrade copy. That page returned HTTP 404 on 2026-05-21; the 8-receiver figure is reproduced from the prior research note and historic cached snippets but is not re-confirmable from any current live operator page (corsstations.com, checked 2026-05-21, does not list any PR networks). Treat as historical figure pending fresh confirmation. |
| VRS Systems PR — software | Trimble Pivot Platform; July 2022 upgrade added Galileo + BeiDou |
| VRS Systems PR — tariff | Not publicly disclosed (commercial subscription only) |
| VRS Systems PR — eligibility | Commercial subscription — hobbyist tier not advertised |
| PRSN CORS NTRIP | Status: unconfirmed — `prsn.uprm.edu` reachable historically but the `/English/research/geodesy/NTRIP_info.php` page returned ECONNREFUSED 2026-05-21; no operator-portal disclosure of a public NTRIP endpoint |
| datum_epoch | EarthScope NOTA: ITRF2014, epoch 2026-03-30 (operator declaration https://www.earthscope.org/data/gnss-realtime/; FAQ does not state whether the epoch advances over time). NGS NCN station pages declare NAD83(2011) for NCN-archived coordinates of PRMI etc. VRS Systems PR (HLCM): omitted — no citable operator service-side declaration. As a Trimble Pivot service in a US territory it most likely operates in NAD83(2011), the default for US-based Pivot deployments, but no operator page confirms this. |
| last_confirmed_alive | 2026-05-21 — EarthScope NTRIP `SOURCETABLE 200 OK`; `P780_RTCM3P3` in pipeline snapshot |

## Service Details

### EarthScope NOTA (free for noncommercial)

EarthScope Consortium broadcasts 1 Hz GNSS data from ~1,100 NOTA stations via NTRIP at `ntrip.earthscope.org`. Confirmed PR stations include PRMI, PRGY, P780. Real-time access requires an EarthScope account and acceptance of the NULA (Non-commercial Use Licence Agreement). Commercial use requires a separate licence at USD 1,000/seat/yr. Data are geodetic 1 Hz raw — not VRS; rovers must handle the single-base baseline computation.

### VRS Systems PR / HLCM Group (commercial, paid)

"VRS Systems PR is the only company in Puerto Rico that owns and operates its system … VRS Systems PR in Puerto Rico now fully support GPS, GLONASS, and now, Galileo and BeiDou satellite systems." Service is described as 24/7. Subscription contact via HLCM Group corporate channels (phone +1-787-398-8852, sales@hlcmgroup.com per the HLCM Group homepage); no public registration URL exists.

### PRSN CORS (status: unconfirmed for public NTRIP)

PRSN (Red Sísmica de Puerto Rico, UPRM Mayagüez) operates 18 permanent GPS stations across PR + the US/British Virgin Islands + adjacent islands (Trimble Alloy, NetRS, NetR9 + Topcon). The PRSN instrumentation page (`redsismica.uprm.edu/english/our_work/instrumentation.php`, HTTP 200 2026-05-21) describes real-time data transmission to Mayagüez via VHF/UHF radios, spread-spectrum, microwave, satellite, and Internet, but does not advertise a public NTRIP endpoint. Treat the PRSN NTRIP service as unconfirmed pending direct UPRM contact.

## Context Notes

- **Puerto Rico is a US territory** — geodetic infrastructure falls under NOAA / NGS federal programmes. NOAA NCN itself does not operate a public NTRIP caster; it releases RINEX within ~1 hr for post-processing.
- **No free unrestricted public RTK/VRS caster** equivalent to US state RTN networks (InCORS, NC RTN, etc.). NGS encourages state DOTs / commercial partners to fill this gap; none free confirmed as of 2026-05-21. The only commercial RTN identified is VRS Systems PR (HLCM Group).
- **Local project data** — `py scripts/stations_by_country.py PRI` (2026-05-21): 1 rtk2go (`PR-YAUCO1`, 18.02, -66.84) + 1 earthscope (`P780`, 18.08, -66.58). Volunteer presence minimal. `PR-YAUCO1` is a community rtk2go base on the south coast at Yauco; rtk2go terms allow hobbyist use with any-email registration (shared community credentials, no SLA). Within roughly 30 km it would deliver typical single-base RTK accuracy for a hobbyist within Yauco/Guánica/Ponce; outside that radius single-base error grows by ~1 ppm. Mountpoint format/constellation not separately probed.
- **Commercial roaming networks** (Trimble VRS Now, Hexagon SmartNet): not extended to Puerto Rico per public coverage maps.
- **Practical option for hobbyists**: set up own base station; use EarthScope NOTA single-base on a nearby NOTA station; Galileo HAS (~40 cm, no internet); GEODNET coverage unconfirmed in PR.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| NOAA NCN RINEX archive — Puerto Rico stations; data within ~1 hr | https://geodesy.noaa.gov/CORS/ | Free |
| UNAVCO / EarthScope GNSS archive — NOTA Puerto Rico stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (NULA); USD 1,000/seat/yr commercial |

## Sources

- NOAA NCN main page: https://geodesy.noaa.gov/CORS/
- NOAA NCN data and products: https://geodesy.noaa.gov/CORS/data.shtml
- NOAA NCN station page — PRMI: https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=PRMI
- NGS Puerto Rico earthquake coordinate update (2020): https://geodesy.noaa.gov/web/news/coordinates-puerto-rico-earthquake.shtml
- EarthScope NOTA: https://www.earthscope.org/nota/
- EarthScope real-time GNSS data: https://www.earthscope.org/data/gnss-realtime/ (HTTP 200 2026-05-21; ITRF2014 + epoch 2026-03-30 declared in FAQ)
- EarthScope NTRIP sourcetable: `ntrip.earthscope.org:2101` (curl 2026-05-21, SOURCETABLE 200 OK)
- COCONet project: https://coconet.unavco.org/
- VRS Systems PR (HLCM Group, 2022 upgrade page; HTTP 404 to WebFetch 2026-05-21 but figure preserved in cached snippets and reaffirmed by HLCM Trimble distributor pages): https://www.hlcmgroup.com/vrs.php
- HLCM blog (May 2025): https://blog.hlcmgroup.com/2025/05/26/trusted-technology-to-transform-infrastructure-in-puerto-rico-and-the-caribbean/
- HLCM Group: https://www.hlcmgroup.com/
- HLCM Trimble GNSS Systems: https://www.hlcmgroup.com/geospatial.php
- PRSN Mayagüez (research/geodesy/NTRIP): http://www.prsn.uprm.edu/English/research/geodesy/NTRIP_info.php (ECONNREFUSED 2026-05-21)
- PRSN instrumentation page (HTTP 200 2026-05-21): https://redsismica.uprm.edu/english/our_work/instrumentation.php
- ArduSimple USA page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- `py scripts/stations_by_country.py PRI` (2026-05-21) — 1 rtk2go (`PR-YAUCO1`), 1 earthscope (`P780`)
