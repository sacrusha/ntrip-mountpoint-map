# Palestine [PS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-23 (prior: 2026-05-17). WebSearch for PA / PLA / An-Najah / Birzeit / donor-funded CORS announcements returned no infrastructure news. Radius probe of Ramallah 31.9/35.2 within 50 km still returns only the Israeli rtk2go base `misgav_dov` (44.6 km, ISR — not Palestinian-operated).
last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-17
last_caster_search_date: 2026-05-23

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **datum_epoch** | omitted -- no citable operator declaration (no operating service to cite) |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Most Recent Project Announcement

**Palestinian Land Authority "Land Sector Strategy 2021–2023"**: Geodetic standardization listed as a goal — no CORS/NTRIP rollout publicly announced.
Contact: Palestinian Land Authority (PLA) — https://www.devex.com/organizations/palestinian-land-authority-pla-153017

No JICA, USAID, World Bank, or EU (PEGASE-framework) funded public CORS/NTRIP project announcement for Palestine found in any indexed source.

## Context Notes

- **Private RTK services**: An academic paper (~2020) states "GNSS surveying in Palestine is implemented by private sector companies providing real-time GNSS correction services" — but these are unnamed and no public NTRIP endpoint is indexed.
- **Bnei Eli Etkes SpiderNET** (etkes.com): Israeli private network with ~60 stations, some physically located in West Bank cities (Ramallah, Jenin, Jericho, Burin, Sinjil, Dura). Israeli company (+972-9-7415043), no public NTRIP host:port, no published pricing, access policy for Palestinian residents unknown.
- **Survey of Israel (Mapi)**: Paid national NTRIP service; covers Israel proper; West Bank coverage status unconfirmed; portal returned HTTP 403 at research date.
- **IGS stations near Palestine**: TELA, RAMO, DRAG, JSLM (Jerusalem) — post-processing RINEX archives only, not real-time RTK streams.
- **GNSS spoofing**: Since Oct 2023, Israel operates persistent GPS/GNSS spoofing across the region (IDF airbase, northern Israel), disrupting civilian GNSS across Lebanon, Syria, Jordan, Egypt, Cyprus, and the West Bank. Any RTK caster in the West Bank would face this as a fundamental operational hazard.
- An-Najah National University / Palestinian Land Authority partnership on National Geodetic Network (2017 workshop) — discussed VRS concepts but no operational caster announced.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS/CDDIS** (NASA) — Israeli IGS stations TELA (Tel Aviv), RAMO (Ramon), DRAG (Dead Sea), JSLM (Jerusalem); nearest reference data for West Bank post-processing | https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html | Free (NASA Earthdata account required) |

Note: GNSS spoofing active in the region since Oct 2023 — may affect post-processed data quality as well as real-time.

## Verification Snapshot (2026-05-23)

- `py scripts/stations_by_country.py PSE` → "No stations for 'PSE'". Zero ingested-globals coverage.
- `py scripts/stations_by_radius.py 31.9 35.2 50` (Ramallah 50 km) → 1 rtk2go station `misgav_dov` at 31.81, 34.74 (44.6 km, ISR — Israel volunteer base, not Palestinian-operated).
- WebSearch for PA / PLA / An-Najah / Birzeit / donor-funded (JICA, USAID, World Bank, EU PEGASE) CORS or NTRIP announcements returned only conflict / settler-violence / land-registration coverage; no geodetic infrastructure news.
- Israeli land-registration push into Area C (Feb 2026 cabinet decisions) continues to tighten rather than expand surveying access for Palestinians in Area C terrain.
- Bnei Eli Etkes "SpiderNET" (Israeli, private; Leica distributor): no public sourcetable, hobbyist tariff, or published access policy for Palestinian residents. Who Profits database lists bases in Ramallah, Jenin, Jericho, Burin, Sinjil, Dura.
- GNSS spoofing across Israel/Lebanon/Jordan/Sinai/Cyprus, persistent since October 2023, remains an operational hazard for rover work in the West Bank or Gaza.

## Sources Consulted
- RTK2GO sourcetable, SNIP monitor
- NTRIP-list.com, corsstations.com
- IGS Network (network.igs.org) — 0 results for PS
- GitHub mvarga1989 CORS list
- ArduSimple Israel page
- Academia.edu Palestine GNSS paper
- etkes.com (Bnei Eli Etkes SpiderNET)
- Who Profits database
- Survey of Israel (Mapi) portal
- RTKdata, HxGN SmartNet
- WebSearch 2026-05-12 — no PA / PLA / An-Najah CORS or NTRIP announcement found
