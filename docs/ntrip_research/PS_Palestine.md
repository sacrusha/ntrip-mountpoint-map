# Palestine [PS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (prior version: 2026-05-06)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
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

## 2026-05-12 Re-Check Notes

- No new public NTRIP caster announcement found for the Palestinian Authority,
  Palestinian Land Authority (PLA), An-Najah National University, or any
  donor-funded project (JICA, USAID, World Bank, EU). WebSearch returned only
  conflict / settler-violence / land-registration coverage; no geodetic
  infrastructure news.
- Israeli land-registration push into Area C (Feb 2026 cabinet decisions)
  intensifies the political and operational constraints on any Palestinian
  CORS rollout in open-area C terrain — surveying access for Palestinians is
  reportedly tightening rather than expanding.
- Bnei Eli Etkes "SpiderNET" (Israeli, private; Leica distributor) — no
  evidence of a public sourcetable, hobbyist tariff, or formal access policy
  for Palestinian residents. Listed on Who Profits as operating bases in the
  West Bank (Ramallah, Jenin, Jericho, Burin, Sinjil, Dura).
- GNSS spoofing across Israel/Lebanon/Jordan/Sinai/Cyprus, persistent since
  October 2023, remains an operational hazard for any rover work in the West
  Bank or Gaza.

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
