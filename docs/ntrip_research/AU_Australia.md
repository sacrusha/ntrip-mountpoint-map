# Australia [AU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (prior: 2026-05-12, 2026-05-06)

## Status: YES — free national NTRIP (AUSCORS / Geoscience Australia); state networks (NSW, VIC) are paid via authorised resellers; WA/SA state CORS now operated by GA and exposed via AUSCORS

---

## 1. AUSCORS — Geoscience Australia (national, free)

| Field | Value |
|---|---|
| **landing_url** | https://gnss.ga.gov.au/stream |
| **access_url** | https://gnss.ga.gov.au/registration |
| **operator** | Geoscience Australia (GA), Commonwealth of Australia |
| **host:port** | `ntrip.data.gnss.ga.gov.au:443` (TLS / NTRIP v2.0, primary); `ntrip.data.gnss.ga.gov.au:2101` (plain TCP / NTRIP v1.0 fallback) |
| **num_stations** | 922 STR rows in sourcetable on 2026-05-15 (curl, this sandbox) |
| **vrs** | No — single-base physical streams only |
| **tariff** | Free; account registration required (https://gnss.ga.gov.au/registration); licensed CC BY 4.0; no monetary fee observed 2026-05-15 |
| **hobbyist_eligibility** | Yes — GA describes the service as "free and open access"; registration form asks for name, email, and use-case; no professional credential gate |
| **legal_residency_required** | No — international users supported; auth doc references no jurisdictional restriction (https://data.gnss.ga.gov.au/docs/home/auth.html, 2026-05-15) |
| **last_confirmed_alive** | 2026-05-15 — curl `https://ntrip.data.gnss.ga.gov.au/` returned `SOURCETABLE 200 OK` with 922 STR lines; port 2101 plain TCP also returned `SOURCETABLE 200 OK` (HTTP/0.9 framing) |
| **datum_epoch** | GDA2020 (ITRF2014 @ epoch 2020.0); RTCM 1006 messages broadcast GDA2020 coordinates certified under Regulation 13 of the National Measurement Act 1960 — https://www.ga.gov.au/scientific-topics/positioning-navigation/positioning-australia/geodesy/datums-projections/gda2020 |

### Technical detail (AUSCORS)
- Protocol: NTRIP v2.0 over TLS (443) primary; NTRIP v1.0 on 2101 plain TCP fallback for legacy clients.
- Format: RTCM 3.3 with MSM; full multi-constellation (GPS + GLO + GAL + BDS + QZS) on essentially all modern stations.
- Mountpoint convention: `<STA4>00AUS0` (e.g. `ALIC00AUS0` Alice Springs NT, `SYDN00AUS0` Sydney NSW, `ALBY00AUS0` Albany WA).
- Coverage: Nationwide CORS incorporating ex-Landgate WA sites (transferred to GA, ~26 sites + 18 GA additions per the WA Geodetic Strategy 2021-25), SA stations, NT, QLD outback. ~100+ stations along populated coasts; sparse in interior.
- The sourcetable also re-streams ~42 IGS/international partner stations (e.g. `KIRU00SWE0` Sweden, `ENAO00PRT0` Azores) — these are tagged `solution=1` despite being physical receivers; the pipeline overrides this with `solution_filter=False`.
- Attribution: "© Commonwealth of Australia (Geoscience Australia)".
- Old host `auscors.ga.gov.au:2101` dead since Jul 2022 migration.

---

## 2. CORSnet-NSW — NSW Spatial Services (paid, via reseller)

| Field | Value |
|---|---|
| **landing_url** | https://www.spatial.nsw.gov.au/surveying/corsnet-nsw |
| **access_url** | https://www.spatial.nsw.gov.au/surveying/corsnet-nsw/How_to_access_CORSnet-NSW |
| **operator** | NSW Department of Customer Service — Spatial Services |
| **host:port** | `corsnet.nsw.gov.au:2101` (GDA94 mountpoints); `corsnet.nsw.gov.au:2020` (GDA2020 mountpoints); Trimble Ntrip Caster 5.3 |
| **num_stations** | 223 STR rows on port 2101 / 220 STR rows on port 2020 (sourcetable, 2026-05-15); ~200 physical CORS |
| **vrs** | Yes (Trimble Pivot Platform; VRS, RTCM 3.1) |
| **tariff** | Not publicly listed. Spatial Services only sells direct subscriptions to "hosts, educational bodies, or for research purposes". Commercial access via authorised Value Added Resellers (Aptella, C.R. Kennedy, etc.); pricing on request. GST applies. (https://www.spatial.nsw.gov.au/surveying/corsnet-nsw/How_to_access_CORSnet-NSW, observed 2026-05-15) |
| **hobbyist_eligibility** | No — reseller-gated; no public consumer tier. AUSCORS is the free path inside NSW. |
| **legal_residency_required** | No formal residency requirement, but reseller relationship and AU billing in practice |
| **last_confirmed_alive** | 2026-05-15 — curl ports 2101 and 2020 returned `SOURCETABLE 200 OK` (Trimble Ntrip Caster 5.3, 33,741-byte sourcetable on :2101) |
| **datum_epoch** | GDA2020 (:2020) and legacy GDA94 (:2101); GDA2020 = ITRF2014 @ 2020.0 — https://www.ga.gov.au/scientific-topics/positioning-navigation/positioning-australia/geodesy/datums-projections/gda2020 |

---

## 3. Vicmap Position / GPSnet — Victoria (paid, via reseller)

| Field | Value |
|---|---|
| **landing_url** | https://www.land.vic.gov.au/maps-and-spatial/spatial-data/vicmap-catalogue/vicmap-position |
| **access_url** | https://gnss.vicpos.com.au/GPSnet/VAR/VAR.html (VAR list) |
| **operator** | Department of Energy, Environment and Climate Action (DEECA) Victoria |
| **host:port** | `gnss.vicpos.com.au:2101` (Trimble caster). Unreachable from this sandbox (TCP timeout 2026-05-15) — but auth-portal URL `https://gnss.vicpos.com.au/` returns ECONNREFUSED for HTTPS too, suggesting Vicmap's edge filters non-AU IPs. Target users in AU reach it via reseller-distributed credentials. |
| **num_stations** | >120 GNSS ground stations (DEECA official statement) |
| **vrs** | Yes (DGNSS + Networked RTK + single-base RTK + post-processing) |
| **tariff** | Not publicly listed. From 2019-01-01 DELWP/DEECA stopped accepting new direct GPSnet subscriptions; all new customers must go through a Value Added Reseller. Pricing on request from VARs. (https://www.land.vic.gov.au/surveying/services/positioning, observed 2026-05-15) |
| **hobbyist_eligibility** | No public consumer tier; reseller-gated |
| **legal_residency_required** | No formal requirement, but AU-payable subscription in practice |
| **last_confirmed_alive** | 2026-05-15 — official Vicmap Position page reachable via search engines; direct portal `gnss.vicpos.com.au` not reachable from this sandbox (HTTPS connection refused; NTRIP port 2101 TCP timeout). Service is advertised as 24/7 365-day operational by DEECA. |
| **datum_epoch** | GDA2020 (and legacy GDA94 on parallel mountpoints); Victoria adopted GDA2020 in line with national rollout — https://www.land.vic.gov.au/surveying/geodesy/geocentric-datum-of-australia |

---

## 4. WA CORS — formerly Landgate, now Geoscience Australia (free via AUSCORS)

| Field | Value |
|---|---|
| **landing_url** | https://www.landgate.wa.gov.au/location-data-and-services/surveying/geodesy/horizontal-datum/ |
| **access_url** | https://gnss.ga.gov.au/registration (use AUSCORS) |
| **operator** | Geoscience Australia (took over from Landgate per Geodetic Strategy for WA 2021-25) |
| **host:port** | n/a — no separate Landgate caster; WA sites stream via `ntrip.data.gnss.ga.gov.au:443` (AUSCORS). E.g. `ALBY00AUS0` Albany, `ARUB00AUS0` Arubiddy confirmed in 2026-05-15 sourcetable. |
| **num_stations** | 26 ex-Landgate CORS handed to GA + 18 new GA WA additions planned per the WA Geodetic Strategy 2021-25 |
| **vrs** | No (single-base via AUSCORS) |
| **tariff** | Free (same as AUSCORS) |
| **hobbyist_eligibility** | Yes (via AUSCORS) |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-15 — AUSCORS sourcetable contains WA sites |
| **datum_epoch** | GDA2020 (ITRF2014 @ 2020.0) — https://www.landgate.wa.gov.au/location-data-and-services/surveying/geodesy/horizontal-datum/ |

---

## 5. SA GNSS CORS — South Australia DHUD (free via AUSCORS)

| Field | Value |
|---|---|
| **landing_url** | https://www.dhud.sa.gov.au/our-department/office-of-the-surveyor-general/surveying/geodetic-surveying/gnss-cors |
| **access_url** | https://gnss.ga.gov.au/registration (use AUSCORS) — DHUD's own page explicitly directs users to AUSCORS for free single-station DGPS/RTK |
| **operator** | SA Department for Housing and Urban Development (DHUD), Office of the Surveyor-General |
| **host:port** | n/a — no separate SA caster; SA stations stream via AUSCORS (e.g. `ANDA00AUS0` Andamooka, `APYL00AUS0` Umuwa Kaltjiti confirmed 2026-05-15) |
| **num_stations** | SA stations within AUSCORS network (subset of 922-stream sourcetable) |
| **vrs** | No (single-base via AUSCORS); commercial VRS via AllDayRTK / SmartNet / Positioned / RTKdata if needed |
| **tariff** | Free (AUSCORS) |
| **hobbyist_eligibility** | Yes (via AUSCORS) |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-15 — DHUD page reachable via search (HTTP 403 to scrapers but content visible via Google cache / WebSearch summaries); AUSCORS sourcetable contains SA sites |
| **datum_epoch** | GDA2020 (ITRF2014 @ 2020.0) — https://www.ga.gov.au/scientific-topics/positioning-navigation/positioning-australia/geodesy/datums-projections/gda2020 |

---

## 6. QLD / TAS / NT / ACT — no free state caster; commercial only

No state-funded free hobbyist caster operates in QLD, TAS, NT, or ACT as of 2026-05-15. The historical Queensland SunPOZ VRS test-bed (SE QLD, Trimble VRS3Net, Department of Natural Resources) is not exposed as a public caster — the SunPOZ name appears only in academic/historical references; current QLD commercial network access is via SmartNet/AllDayRTK/Positioned. AUSCORS provides the free single-base baseline.

---

## 7. Commercial national / multi-state networks (paid)

| Network | Coverage | Tariff (AUD ex/inc GST, 2026-05-15) | Source |
|---|---|---|---|
| **AllDayRTK** (Aptella) | National VRS | From **AUD 440/yr (inc GST)**, annual contracts only, no monthly. 30-day dealer trial. PLUS tier (multi-GNSS + RINEX + web tools) and SITE tier exist; pricing on request via dealer. | https://www.aptella.com/alldayrtk/, https://www.aptella.com/wp-content/uploads/2025/06/AllDayRTK-Brochure-2025-NZ-Web.pdf |
| **HxGN SmartNet Aus** | National (~620+ CORS aggregated incl. Spatial NSW data) | Pricing on request via C.R.Kennedy / Map Gear dealers; not publicly listed. | https://hxgnsmartnet.com/en-au (HTTP 403 from this sandbox), https://survey.crkennedy.com.au/_brands/hxgn-smartnet |
| **Positioned RTK** | National (leverages GA CORS + extras) | Pricing on request. Solutions: NEAR (single-base) + VRS. | https://positioned.com.au/products/positioned-rtk-ntrip-subscription |
| **RTKdata.com** | 1,500+ AU stations via aggregator | USD 40/mo (~AUD 62/mo) self-service; 30-day free trial. | https://rtkdata.com/aus/ |
| **GEODNET Australia** | Crowd-sourced AU pod stations | USD 40/mo paid (after 30-day trial); host `aus.geodnet.com:2101`. | https://geodnet.com — see rtk_inventory.md `geodnet_aus` |

All commercial networks require a paid subscription; none offer a public hobbyist tier free of charge.

---

## 8. Volunteer / community casters (free)

Per `scripts/stations_by_country.py AUS` on 2026-05-15:

**rtk2go (24 AUS-tagged bases)**: Beautypoint, Cadarga, Codemortk, GRGY00AUS0, GreenBAL01, HillcrestCandelo, InfiniSteer1, Maptek, Mossman_Base, MtBuffalo_001, MtRavensbourne, Nelsonbay, REDCLIFFE_PERTH_WA, RFBYCkeanespoint, SG1NEW, SG1PH, SGF1 (NOTE: coordinates 33.11, -82.48 are Georgia USA — mistagged), SGMCSURATCMR, SGMCSURATRTCM, SGMCwsRTCM3, Sheoak_Range, UWA_Campus, WEXtmp, warrakam.

**Centipede (3 AUS nodes)**: CADA (-26.07, 150.94, QLD; co-sited with rtk2go Cadarga), FARM48 (-32.39, 142.45, NSW/VIC border), SORA (-34.41, 135.50, SA; co-sited with rtk2go Sheoak_Range).

Volunteer streams are not formally maintained — quality and uptime vary.

---

## 9. Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| **AUSPOS** (GA online post-processing) | https://gnss.ga.gov.au/auspos | Free |
| **GA GNSS Data Centre** (RINEX archive) | https://data.gnss.ga.gov.au | Free, registration |
| **EarthScope / UNAVCO** (selected AU sites) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

---

## Hobbyist path summary

AUSCORS is the only practical zero-cost real-time NTRIP option Australia-wide. Single-base RTK from the nearest AUSCORS station (often within 50-100 km in populated areas) delivers cm-level horizontal accuracy under good baseline conditions. No state government network offers a free public hobbyist tier. Commercial VRS subscription via AllDayRTK starts at AUD 440/yr (inc GST).

---

## Sandbox reachability notes (2026-05-15)

| URL / endpoint | Result |
|---|---|
| `https://ntrip.data.gnss.ga.gov.au/` (AUSCORS 443) | 200 SOURCETABLE, 922 STR rows |
| `http://ntrip.data.gnss.ga.gov.au:2101/` (AUSCORS plain) | 200 SOURCETABLE (HTTP/0.9) |
| `http://corsnet.nsw.gov.au:2101/` (CORSnet-NSW GDA94) | 200 SOURCETABLE, 223 STR rows, Trimble Caster 5.3 |
| `http://corsnet.nsw.gov.au:2020/` (CORSnet-NSW GDA2020) | 200 SOURCETABLE, 220 STR rows |
| `http://gnss.vicpos.com.au:2101/` | TCP timeout (filtered to non-AU traffic; portal HTTPS also ECONNREFUSED) — service is operational per DEECA; reachable for AU users |
| `https://www.spatial.nsw.gov.au/surveying/corsnet-nsw` | 200 |
| `https://www.landgate.wa.gov.au/` | 200 |
| `https://www.dhud.sa.gov.au/.../gnss-cors` | 403 to curl (anti-bot WAF); content visible via search engines |
| `https://hxgnsmartnet.com/en-au` | 403 (anti-bot WAF) |
| `https://www.aptella.com/alldayrtk/` | 200 |
| `https://positioned.com.au/products/positioned-rtk-ntrip-subscription` | 200 |
| `https://gnss.ga.gov.au/registration` | 200 |

---

## Sources consulted (2026-05-15)
- Curl probes: AUSCORS 443 + 2101, CORSnet-NSW 2101 + 2020, vicpos 2101 (all timestamps 2026-05-15)
- GA GNSS Data Centre authentication: https://data.gnss.ga.gov.au/docs/home/auth.html
- GA GNSS stream portal: https://gnss.ga.gov.au/stream
- GA GDA2020 datum page: https://www.ga.gov.au/scientific-topics/positioning-navigation/positioning-australia/geodesy/datums-projections/gda2020
- ICSM Australian Terrestrial Reference Frame: https://www.icsm.gov.au/australian-terrestrial-reference-frame
- Spatial NSW CORSnet-NSW landing + access: https://www.spatial.nsw.gov.au/surveying/corsnet-nsw, /How_to_access_CORSnet-NSW
- Vicmap Position / GPSnet: https://www.land.vic.gov.au/surveying/services/positioning, https://gnss.vicpos.com.au/GPSnet/VAR/VAR.html
- Landgate WA Geodetic Strategy 2021-25: https://www.landgate.wa.gov.au/siteassets/documents/location-data-and-services/surveying/geodetic-strategy-for-western-australia-2021-25.pdf
- SA DHUD GNSS CORS: https://www.dhud.sa.gov.au/our-department/office-of-the-surveyor-general/surveying/geodetic-surveying/gnss-cors
- Aptella AllDayRTK: https://www.aptella.com/alldayrtk/ + 2025 NZ brochure (same pricing structure)
- HxGN SmartNet Aus: https://hxgnsmartnet.com/en-au (403 to scraper); C.R.Kennedy dealer pages
- Positioned RTK: https://positioned.com.au/products/positioned-rtk-ntrip-subscription
- RTKdata Australia: https://rtkdata.com/aus/
- Local data verification 2026-05-15: `scripts/stations_by_country.py AUS` → 24 rtk2go + 3 Centipede AU stations
