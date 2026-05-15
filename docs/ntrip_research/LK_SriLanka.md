# Sri Lanka [LK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: TWO active NTRIP RTK casters in Sri Lanka — **SLCORSnet** (government, Survey Department, public pricing in LKR, registration open online, Western Province phase-1 coverage) and **CORSnet** (private commercial, islandwide, 21 stations, pricing on request)

| Field | SLCORSnet (government) | CORSnet (private) |
|---|---|---|
| **Operator** | Survey Department of Sri Lanka (Surveyor General's Office, Colombo) | CORSnet (Pvt) Ltd, spun off from SULECO (Pvt) Ltd |
| **Network name** | SLCORSnet — Sri Lanka Continuously Operating Reference Station Network | CORSnet |
| **host:port** | `222.165.190.67:2101` — confirmed live 2026-05-12 (`SOURCETABLE 200 OK`, Server: `GNSMART_Caster/1.0`, 7 STR rows; CAS row also published) | `corsnet.lk:2101` (IPv4 104.198.14.52); TCP probe **timed out 2026-05-12** from this sandbox. WebFetch of `corsnet.lk` HTML returned 200; caster endpoint unconfirmed on this date. Marketing site live |
| **VRS** | Yes — `VRS`, `VRS_BDS`, `VRS_MSM4`, `FKP`, `MAC`, `MSM`, plus `SBASE_MSM4` single-base mountpoint | Yes — DGNSS, single-base RTK, Network RTK / VRS, RINEX post-processing |
| **GNSS systems** | RTCM 3.0 / 3.1 / 3.2; mountpoints labelled `gnss`; `VRS_BDS` and `VRS_MSM4`/`SBASE_MSM4` include BDS via MSM4 messages; `MSM` advertises MSM5 for GPS+GLONASS+Galileo+BDS | GPS+GLONASS+Galileo+BeiDou per CORSnet product page |
| **Number of stations** | Phase-1: Western Province + surrounding areas (exact count not published on `slcorsnet.survey.gov.lk`; "About" page shows placeholder counters). Full-island coverage and offshore hydrographic coverage planned for completion phases | 21 CORS stations islandwide (per corsnet.lk homepage 2026-05-12) — 17 stations cited on older SULECO page |
| **tariff** | **Public LKR pricing (incl. all taxes), source: slcorsnet.survey.gov.lk/how-to-use/pricing/, fetched 2026-05-12:** 1 day = **2,000 LKR**; 7 days = **10,000 LKR**; 30 days = **30,000 LKR**; 365 days = **360,000 LKR**. 30-day and 1-year subscribers also receive free GNWEB (RINEX delivery) and SSRPOST (post-processing) access for the same period. **Payment**: cash deposit to People's Bank Narahenpita branch, account `119-1-001-0-9027253` (Surveyor General); deposit slip emailed/faxed (011 2055971) to SLCORSnet admin; account activation within ~28 h | Not publicly disclosed; "multiple packages" cited; rates on inquiry (`info@corsnet.lk` / phone). Customer testimonials describe "affordable pricing"; no LKR figure published 2026-05-12 |
| **hobbyist_eligibility** | Open — anyone needing cm-level real-time positioning is named explicitly ("Anyone who needs real-time cm level GNSS positioning"). Registration is online; no professional licence requirement on the public pages | Open — registration form at `corsnet.lk/user/register/` requires only name, company, email, password, phone, address; no professional credential check |
| **legal_residency_required** | No explicit requirement; payment method (in-country LKR bank deposit at People's Bank Narahenpita) is the practical residency-bias factor — a foreign hobbyist would need a Sri Lankan bank account or a local proxy to pay | No explicit residency clause stated |
| **registration** | `http://www.slcorsnet.survey.gov.lk/` → Login / Register link; account creation free; service activation requires payment | `https://corsnet.lk/user/register/` |
| **last_confirmed_alive** | 2026-05-12 — caster sourcetable 200 OK; pricing page reachable | 2026-05-12 — `corsnet.lk` HTTPS site live (homepage, register, FAQ pages all reachable); TCP probe of port 2101 timed out from this sandbox |

---

## SLCORSnet (government)

### Sourcetable (live, 2026-05-12)

```
Server: GNSMART_Caster/1.0
CAS;127.0.0.1;2101;;;0;LKA;6.50;79.60;0.0.0.0;0;
NET;Sri Lanka Network;;B;Y;;;;None
STR;FKP;FKP v3.0;RTCM3.0;...;LKA;6.50;79.50;1;1;GNSMART
STR;MAC;MAC v3.1;RTCM3.1;...;LKA;6.50;79.50;1;1;GNSMART
STR;MSM;MSM;RTCM3.2;1005,1007,1033,1075,1125,1230;LKA;6.50;79.50;1;1;GNSMART
STR;SBASE_MSM4;Single Base;RTCM3.2;1006,1008,1032,1033,1074,1084,1094,1124,1230;LKA;6.50;79.50;1;0;GNSMART
STR;VRS;Virtual RS v3.0;RTCM3.0;...;LKA;6.50;79.50;1;1;GNSMART
STR;VRS_BDS;Virtual RS v3.2 with BDS;RTCM3.2;...;LKA;6.50;79.50;1;1;GNSMART
STR;VRS_MSM4;Multi Signal Msg;RTCM3.2;1006,1008,1032,1033,1074,1084,1094,1124,1230;LKA;6.50;79.50;1;1;GNSMART
```

All seven STR rows carry `solution=1` (network solution; `SBASE_MSM4` is `solution=0` as the single-base stream). All rows labelled `LKA` country code, coordinates 6.50, 79.50 — Western Province centroid (Phase-1 footprint).

### Coverage

- **Phase 1 (current)**: Western Province and surrounding areas; supports RTK in Colombo, Gampaha, Kalutara districts and adjacent areas
- **Planned**: full-island plus offshore hydrographic coverage (date not announced)
- The `About` page shows placeholder counters (`Stations 0+`, `Years in Service 0+`, `Stations Yet to Come 0+`); pages were last updated for the 2022–2025 site copyright span

### Services

1. **Real-time GNSS Correction Service** — VRS, FKP, MAC, plus PRS (Pseudo Reference Station) and single-base via SBASE_MSM4
2. **GNWEB** — online RINEX raw-data delivery (physical or Virtual RINEX) — included with 30-day and 1-year tiers
3. **SSRPOST** — online autonomous GNSS post-processing service — included with 30-day and 1-year tiers
4. Real-time monitoring of user GNSS peripherals via the SLCORSnet portal

### Connection details (for NTRIP clients)

| Setting | Value |
|---|---|
| Caster address | `222.165.190.67` |
| Port | `2101` |
| Username | chosen by user at registration |
| Password | chosen by user at registration |
| Mountpoints | `VRS`, `VRS_BDS`, `VRS_MSM4`, `FKP`, `MAC`, `MSM`, `SBASE_MSM4` |

### Contacts (SLCORSnet)

- Phone: +94 11 236 9011
- Email: `slcorsnet@survey.gov.lk`
- Address: Department of Survey, 150 Kirula Road, Colombo 00500, Sri Lanka
- Payment fax: 011 2055971

---

## CORSnet (private)

- **landing_url**: `https://corsnet.lk/` — operator-owned commercial CORSnet homepage. Describes the islandwide 21-station network, accuracy claims, service modes, and registration entry-point. About page `https://corsnet.lk/about-us/` is a useful sibling.
- **access_url**: Skip — pricing is sales-contact only ("rates on inquiry"); no operator-owned access/tariff page exists beyond the landing. `corsnet.lk/user/register/` is the bare registration form, not a service description page.
- **History**: Launched 20 May 2014 by SULECO (Pvt) Ltd as Sri Lanka's first islandwide commercial CORS RTK network, initially covering Western and Sabaragamuwa provinces. Operations now under CORSnet (Pvt) Ltd; SULECO provides technical/sales support
- **Station count 2026-05-12**: 21 stations (corsnet.lk homepage). Older SULECO product page still lists 17. 315+ active customers, 172,000+ RTK service-hours per homepage banner
- **Services**: DGNSS (sub-metre), single-base RTK, Network RTK / VRS, RINEX post-processing — via NTRIP and TCP/IP. Correction formats: RTCM 2.x / 3.x, CMR, CMR+, sCMRx, RTD, NMEA
- **Accuracy claims**: 2.5 mm + 0.5 ppm (static), 15 mm + 1 ppm (RTK)
- **Access**: Register at `corsnet.lk/user/register/` (email verification required) → enquire/pay → admin activates account → NTRIP credentials and mountpoint list delivered via the CORSnet dashboard. Mountpoints are not published publicly
- **Contact**: `info@corsnet.lk`, `corsnet.sup@gmail.com`, +94 77 213 1310, +94 77 038 2265; address No. 44, Beddagana South, Pita Kotte; phone numbers on FAQ page: 0772131310 / 0770323439

---

## Other notes

- **Survey Department of Sri Lanka** (`survey.gov.lk`) operates SLCORSnet through the Geodetic Survey arm of the Surveyor General's Office. The `/sdweb/pages_service_geodetic_survey.php?...&l=s` page references SLCORSnet by name and links onward to `slcorsnet.survey.gov.lk`
- **Global volunteer / scientific networks for LK**:
  - `py scripts/stations_by_country.py` — none of rtk2go / Centipede / EarthScope report LK pins as of 2026-05-12
  - `py scripts/stations_by_radius.py 7.0 81.0 500` — zero matches within 500 km (Sri Lanka is geographically isolated from any volunteer base)
  - GEODNET, ONOCOY coverage for LK not confirmed 2026-05-12
- **Practical hobbyist guidance for Sri Lanka**: SLCORSnet is the only public-pricing path for a foreigner or hobbyist; expect to pay 2,000 LKR (~6 USD at May 2026 rates) for a 24-hour subscription, which is cheap by international standards. Payment via Sri Lankan bank deposit is the main friction — a local contact or in-country travel is needed to complete the payment. CORSnet is private and quote-based.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SLCORSnet GNWEB / SSRPOST** — included with 30-day or 1-year subscription | http://www.slcorsnet.survey.gov.lk/ | 30,000 LKR / 30 days; 360,000 LKR / year |
| **CORSnet RINEX** — available to active subscribers | https://corsnet.lk/ | Included in subscription |
| **EarthScope / IGS archive** — no LK station in archive; nearest IGS is in southern India | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted

- SLCORSnet homepage: http://www.slcorsnet.survey.gov.lk/
- SLCORSnet pricing page: http://www.slcorsnet.survey.gov.lk/how-to-use/pricing/
- SLCORSnet how-to-use: http://www.slcorsnet.survey.gov.lk/how-to-use/
- SLCORSnet about: http://www.slcorsnet.survey.gov.lk/about/
- Survey Department of Sri Lanka — Geodetic Survey / CORS Network: https://survey.gov.lk/sdweb/pages_service_geodetic_survey.php?id=d80d8ae23ba3e3a32bea5739e9a83e4246930dae&l=s
- Survey Department of Sri Lanka home: https://survey.gov.lk/
- CORSnet homepage: https://corsnet.lk/
- CORSnet about page: https://corsnet.lk/about-us/
- CORSnet register page: https://corsnet.lk/user/register/
- CORSnet launch announcement (May 2014): https://corsnet.lk/news/ambitious-launch-of-the-cors-network-in-sri-lanka/
- SULECO CORSnet page: https://sulecoltd.com/cors-rtk/
- SULECO contact page: https://sulecoltd.com/contact/
- ArduSimple Sri Lanka: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- Live caster probe (2026-05-12): `curl --http0.9 http://222.165.190.67:2101/sourcetable.txt` → SOURCETABLE 200 OK; 7 STR rows; Server `GNSMART_Caster/1.0`; Content-Length 1273
- Live caster probe (2026-05-12): `curl http://corsnet.lk:2101/` → connection timed out after 15 s; TCP path from this sandbox not open. Webserver corsnet.lk:443 returned 200 (HTML, 21 stations / 315+ customers banner)
- Local pipeline check (2026-05-12): `py scripts/stations_by_country.py` shows no LK/LKA entries in rtk2go, Centipede, or EarthScope; `py scripts/stations_by_radius.py 7.0 81.0 500` returns no stations within 500 km
