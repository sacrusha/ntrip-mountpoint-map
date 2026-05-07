# Agent intended Write
- batch: usw
- target: D:\Projects\ntrip-mountpoint-map\docs\ntrip_research\US-W_West.md
- transcript line: 188

## CONTENT (full file)

```markdown
# USA — West Region [US-W] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07

**Scope:** US Census West region — California (CA), Nevada (NV), Oregon (OR), Washington (WA), Idaho (ID), Montana (MT), Wyoming (WY), Utah (UT), Colorado (CO), Arizona (AZ), New Mexico (NM), Hawaii (HI). Alaska is covered separately in `US-AK_Alaska.md`. National operators (EarthScope NOTA, NPS CORS) are covered in `US-NPS_NationalParkService.md` and country-survey.md; only their West-specific footprint is summarised here.

## Status: PARTIAL — public NTRIP RTK exists in 6 of 12 Western states (free in 4: CA, OR, AZ, CO; paid in 2: WA, UT/NV-via-Utah; MT paid). Five Western states have no free or paid state-level NTRIP RTK service in 2026 (ID, WY, NM, HI; NV state-level only via Utah's TURN).

## Federal / supra-state — relevant Western footprint

| Service | Status (West) | Notes |
|---|---|---|
| **EarthScope NOTA** | Free, in-pipeline | `ntrip.earthscope.org:2101` — densest US coverage is the Western Cordillera (PBO heritage); ~700+ Western stations under non-commercial NULA. Hobbyist-eligible. See country-survey § US. |
| **NPS CORS** | Free, manual provisioning | `rtk.nps.gov:2101` — many Western parks (Yellowstone, Glacier, Yosemite, Grand Canyon, Olympic, etc.); credentials only via gnss_posnav@nps.gov. See `US-NPS_NationalParkService.md`. |
| **NOAA NDGPS / USCG DGPS** | Decommissioned | Last sites turned off 2020 (USCG inland) and 2022 (Great Lakes / St. Lawrence). DGNSS, out of project scope anyway. |

---

## State-level operators — by state

### CA — California

#### CRTN (California Real Time Network) — SOPAC / UCSD

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Scripps Orbit and Permanent Array Center (SOPAC), UC San Diego — clearinghouse for SOPAC/SCIGN, BARD (UC Berkeley/USGS), USGS Pasadena SCIGN, Caltrans CVSRN, Orange County OCRTN, EarthScope NOTA-CA |
| **host:port** | `132.239.152.4:2102` (NorCal zones 1–2) · `:2103` (NorCal zones 3–4) · `:2104` (SoCal zone 5) · `:2105` (SoCal zone 6) — confirmed on SOPAC pages 2026-02-21 |
| **Type** | Single-base (RTCM 3.0, 1 Hz, latency <1 s); ~250 stations |
| **Tariff** | USD 100 one-time processing fee (universities and schools exempt). Below the project's $200/yr affordability cutoff — surfaced as paid-affordable. No annual subscription. (Source: sopac-csrc.ucsd.edu/index.php/crtn, observed 2026-05-07) |
| **VRS?** | No — single-base streams from physical stations |
| **hobbyist_eligibility** | Unclear-leaning-yes — registration via Survey Monkey form; no statement excluding individuals; no licence field. Credentials issued in ~7 days. |
| **legal_residency_required** | No statement; UC San Diego policy does not impose a residency restriction on the form. |
| **last_confirmed_alive** | 2026-05-07 — SOPAC CRTN page reachable; February 2026 station-list update published (added DWR stations 1500, ARBC, CWD1, ORLD; coordinates in NAD83(2011)) |

#### Caltrans CVSRN

Restricted: access limited to vetted state/county agency partners under data-sharing agreements. CVSRN data are mirrored into CRTN, so the Caltrans antennae are reachable through CRTN with the $100 fee. Not a hobbyist option directly. (See networks.md `calrtns`.)

#### BARD (Bay Area Regional Deformation network)

Research array — ~40 stations around the SF Bay / Northern California, operated by UC Berkeley BSL + USGS Menlo Park. No independent public caster: streams are exposed via SOPAC CRTN and EarthScope NOTA. Same physical antennae, two access paths. (See networks.md `bard`.)

#### Local agency networks (CA)

- **San Diego County Real Time Network (SDCRTN)** — operated by County of San Diego, ~13 stations. Free for County employees and approved partners; non-county users go through CRTN. Procedure document at sandiegocounty.gov/content/dam/sdc/dpw/COUNTY_SURVEYOR/SDCRTN_procedures2.pdf describes registration via the County Surveyor.
- **Orange County OCRTN** — Orange County Public Works; mirrored into CRTN. No standalone hobbyist caster.

### NV — Nevada

#### Nevada GPS Network (formerly Washoe County) — operated by State of Utah / UGRC

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Utah Geospatial Resource Center (UGRC) — Washoe County transferred operations to UGRC; portal at `nevadagps.utah.gov` |
| **host:port** | `168.179.231.11:2102` (NAD83/94 HARN) · `165.239.144.7:2101` (NAD83(2011)) — sourced from Washoe County / UGRC docs |
| **Type** | VRS (Trimble Pivot) |
| **Tariff** | USD 600/yr per login — same TURN GPS Bill Pay account used; one subscription currently grants access to both TURN (UT) and Nevada GPS (Reno area). Above the $200/yr hobbyist cutoff. (Source: gis.utah.gov/products/turn, observed 2026-05-07) |
| **VRS?** | Yes |
| **hobbyist_eligibility** | Yes — individual sign-up via turngps-billpay.ugrc.utah.gov; no licence required |
| **legal_residency_required** | No — Utah ID account creation is the only requirement; not state-residency-bound |
| **last_confirmed_alive** | 2026-05-07 — `nevadagps.utah.gov` portal reachable |

#### Las Vegas Valley Water District (LVVWD) GPS Base Station Network

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Las Vegas Valley Water District (in cooperation with NDOT, City of Las Vegas, Clark County Water Reclamation District, Lincoln County NV) |
| **host:port** | host not publicly listed; **port 9899**. Mountpoint names match site names (e.g. `nvbm`). |
| **Type** | Single-base — multiple sites across Las Vegas Valley + partner agency sites; storage is 5-second epoch RINEX in 1-hour files |
| **Tariff** | Not publicly listed — credentials issued by the District Surveyor on contact (702-258-7163) |
| **hobbyist_eligibility** | Unclear — application form at lvvwd.com/apps/base-station-network-access/ collects entity/use info; no published policy on hobbyist eligibility |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | 2026-05-07 — application form and survey resources page reachable |

#### Other NV options

- EarthScope NOTA covers Nevada with several stations (Basin and Range, PBO heritage) — free, in-pipeline.
- Northern NV is partially within TURN GPS coverage (TURN is documented to serve "southern Nevada" as well — see UT below).

### OR — Oregon

#### ORGN (Oregon Real-time GNSS Network) — ODOT

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Oregon DOT (ODOT) |
| **host:port** | `167.131.0.205:9879` (single-base solutions) · `167.131.0.205:9881` (network solutions) — confirmed in ODOT Trimble Access connection PDFs at oregon.gov/odot/ORGN/Documents/ |
| **Software** | Leica GNSS Spider |
| **Type** | Physical-coord + network (VRS / nearest-base); ~100 stations |
| **Tariff** | Free — "All rover users will be issued a rover account at no direct charge" (ODOT Products and Services page, observed 2026-05-07). ODOT reserves the right to introduce nominal O&M fees in future; partners would remain exempt. |
| **VRS?** | Yes — both single-base and network streams |
| **hobbyist_eligibility** | Yes-leaning — no licence requirement; rover request form treats individuals identically; ODOT contact ORGN@odot.oregon.gov |
| **legal_residency_required** | No statement; not stated as restricted |
| **last_confirmed_alive** | 2026-05-07 — oregon.gov ORGN pages reachable |

### WA — Washington

#### WSRN (Washington State Reference Network) — WSDOT

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | WSDOT (with PANGA / Central Washington University contributing antennae, comms, and archiving for Puget Sound stations) |
| **host:port** | Caster at wsrn3.org (sourcetable / map portal); host:port not openly published — issued only after subscription. (CI from this sandbox returns ECONNREFUSED on the v3 portal — likely ACL or geofencing.) |
| **Software** | Trimble Pivot |
| **Type** | Physical-coord + VRS |
| **Tariff** | USD 1,900/yr (1 account) · USD 5,700/yr (5 accounts) · USD 10,000/yr (10 accounts) — pricing structure last documented in a 2015 Caltrans Preliminary Investigation memo (dot.ca.gov real-time-gps-networks-pi-a11y.pdf) and reaffirmed in 2016 RPLS forum discussion. Above the $200/yr hobbyist cutoff. WSDOT/WSRN partners (state agencies, contributing organisations) access free of charge. |
| **VRS?** | Yes — multiple correction formats per station (RTCM 3.1, RTCM 3.2 MSM, CMR+) |
| **hobbyist_eligibility** | Unclear-leaning-no — service is positioned for surveyors and engineering firms; no published hobbyist tier |
| **legal_residency_required** | Unclear — no published residency clause; subscription is open to non-Washington entities in practice |
| **last_confirmed_alive** | 2026-05-07 — wsrn.org and wsrn3.org pages indexed and described in third-party sources; direct sandbox fetch of `wsrn.org` and `wsrn3.org` returned ECONNREFUSED, but the service is documented as continuously operational by WSDOT and listed in 2024–2026 third-party comparisons |

### ID — Idaho

**No state-operated public NTRIP RTK service.** A 2010 ISU GIS Center / Frontier Precision / Monsen / UGRC project established a southeastern Idaho VRS network (Pocatello/ISU + Jerome, Twin Falls, Blackfoot, Idaho Falls, with planned Rupert, Aberdeen, Soda Springs). Today this network feeds into TURN GPS Utah's coverage footprint ("portions of Idaho, Wyoming, and southern Nevada" per UGRC) — access is therefore through the same TURN GPS subscription described under UT.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (state-operated)** | No |
| **Coverage paths** | TURN GPS UT (paid USD 600/yr) over southeastern Idaho; EarthScope NOTA (free, in-pipeline) for ~30+ Idaho stations |
| **last_confirmed_alive (TURN-via-Idaho)** | 2026-05-07 — UGRC documentation explicitly lists Idaho coverage |

#### Most recent project announcement

The 2024 Idaho Geospatial Office Geodetic Control TWG (gis.idaho.gov/geodetic-control-twg) lists "real-time correction network" as an ongoing focus area in cooperation with NGS for an Idaho spatial reference system update; no caster has been announced as of 2026-05-07.

### MT — Montana

#### MTSRN (Montana State Reference Network) — Montana State Library

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Montana State Library (with MDT, tribal nations, counties, educational institutions, private partners). Subscription service launched March 2022. |
| **host:port** | Caster on `mtsrn.org`; host:port issued post-subscription, not openly published |
| **Type** | VRS (Trimble Pivot) |
| **Tariff** | USD 1,500/yr per login, effective 2024-07-01. One-time discount of USD 1,200 was offered to subscribers prior to 2024-06-01 (valid through 2025-07-01). Rates re-published in January of each odd-numbered year, taking effect July 1 of that year — no 2026-07-01 update yet announced as of 2026-05-07. (Source: msl.mt.gov/mtsrn/) Above the $200/yr hobbyist cutoff. |
| **VRS?** | Yes |
| **hobbyist_eligibility** | Unclear-leaning-no — publicised as a subscription service for surveying, engineering, agriculture, construction; no hobbyist tier published. Contributing organisations (donating equipment/services) may receive multiple free logins; educational users have separate agreements. |
| **legal_residency_required** | No — no published residency clause. Coverage and outreach are Montana-specific. |
| **last_confirmed_alive** | 2026-05-07 — msl.mt.gov/mtsrn/ portal reachable; MTSRN coordinator at mtsrn@mt.gov / 406-444-0240 |

### WY — Wyoming

**No state-operated public NTRIP RTK service.** Professional Land Surveyors of Wyoming (plsw.org/cors/) maintains a list of CORS sites; these are NGS CORS for post-processing only. EarthScope NOTA covers Wyoming with PBO-heritage stations (free, in-pipeline). UGRC TURN GPS covers "portions of Wyoming" — practically the southwest corner adjacent to Utah (via paid USD 600/yr subscription).

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (state-operated)** | No |
| **Coverage paths** | EarthScope NOTA (free, in-pipeline) — best general Wyoming option; TURN GPS UT (paid) for southwest WY |
| **Most recent project announcement** | None — no public WyoCORS/WYDOT real-time network has been announced as of 2026-05-07 |

### UT — Utah

#### TURN GPS — UGRC (Utah Geospatial Resource Center)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Utah Geospatial Resource Center (UGRC), a division of the Utah Division of Technology Services. Branded as "Utah Reference Network GPS / TURN." |
| **host:port** | `165.239.144.5:2101` — confirmed at gis.utah.gov/documentation/turn/connecting/ (observed 2026-05-07) |
| **Recommended mountpoint** | `GNSS-VRS-NAD83-RTCM32` (full GNSS network solution: GPS+GLONASS+Galileo+BeiDou; RTCM 3.2 MSM). Additional mountpoints in CMRx, CMRp, RTCM 3.1; nearest-base "MS-" prefixed mountpoints for network-edge users. |
| **Datum** | NAD83(2011), epoch 2010.0000 |
| **Type** | VRS + nearest-base; ~100+ stations across UT and portions of ID, WY, southern NV |
| **Tariff** | USD 600/yr per user login, valid one full year from sign-up date. Currently a single subscription grants both TURN (UT) and Nevada GPS Network (Reno area) access; UGRC has indicated this may split per-region in the future. Above the $200/yr hobbyist cutoff. (Source: gis.utah.gov/products/turn, observed 2026-05-07) |
| **VRS?** | Yes |
| **hobbyist_eligibility** | Yes — Utah ID account creation at turngps-billpay.ugrc.utah.gov; no licence required; payment by card |
| **legal_residency_required** | No — Utah ID is required (a Utah-state digital identity account, not state residency); non-residents can register a Utah ID for online services |
| **last_confirmed_alive** | 2026-05-07 — gis.utah.gov pages and turngps.utah.gov portal reachable |

### CO — Colorado

#### Mesa County RTVRN — Mesa County Public Works

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Mesa County Public Works (Western Colorado) |
| **host:port** | `rtvrn.mesacounty.us:2101` — confirmed via Mesa County PDFs (2025-05) |
| **Type** | VRS only (no single-base mountpoints exposed); ~33 underlying stations (17 NGS CORS + 16 county/partner). Mountpoints: `VRS_CMR`, `VRS_CMRx`, `VRS_RTCMv3`, `VRS_CMR_RTX`, `VRS_CMRx_RTX`, `VRS_RTCMv3_RTX`. Trimble PIVOT backend. |
| **Tariff** | Free to the public — sign up at rtvrn.mesacounty.us/RegisterAccount.aspx |
| **VRS?** | Yes — VRS only |
| **hobbyist_eligibility** | Yes — public sign-up form; no licence required |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-07 — mesacounty.us/departments-and-services/public-works/gps-survey/real-time-virtual-reference-network-rtvrn page reachable; 2025-05 documentation revisions published |

#### State-level Colorado

No CDOT-operated statewide NTRIP RTK service. Coverage outside western Colorado (Mesa County RTVRN footprint) relies on EarthScope NOTA (free, in-pipeline) — Colorado is reasonably well-covered by NOTA, especially the Front Range and southern Colorado.

### AZ — Arizona

#### AzCORS — Arizona Department of Water Resources (ADWR)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Arizona Department of Water Resources (ADWR) |
| **host:port** | `azcors.azwater.gov:2101` — current mountpoint listing in `AZCORS_InformationAndMountpoints.pdf` (azwater.gov/sites/default/files/2024-02/) |
| **Software** | Leica GNSS Spider |
| **Type** | Physical-coord + VRS; ~51 stations (continuing expansion — March 2025 announcement of new ADWR-built CORS site adding to both AZCORS and the NOAA NCN) |
| **Tariff** | Free — open-data policy for both real-time and RINEX; register an AzCORS account at azcors.azwater.gov/sbc/Account/Index?returnUrl=/sbc/ (Source: azwater.gov/hydrology/azcors, observed 2026-05-07) |
| **VRS?** | Yes |
| **hobbyist_eligibility** | Yes — self-service registration; no licence requirement |
| **legal_residency_required** | No statement — open-data network |
| **last_confirmed_alive** | 2026-05-07 — azwater.gov pages reachable; 2025-03-19 ADWR press release confirms ongoing expansion |

#### AZGPS (commercial)

AZGPS, Inc. (azgps.net, founded November 2004) operates a commercial Trimble VRS network in Arizona and Southern California. Subscription pricing not publicly listed; prospective subscribers must contact AZGPS directly. Out of scope for this project's hobbyist focus given undisclosed commercial pricing.

### NM — New Mexico

**No confirmed state-operated public NTRIP RTK service in 2026.** The Albuquerque Real-Time GNSS Network (ARTGN), launched 2007 by the City of Albuquerque, operated as a paid subscription service (~USD 200/month historical figure from 2010 American Surveyor article); current operational status as of 2026-05-07 is undocumented online. The City of Albuquerque GIS contact (Loren Risenhoover, City Surveyor, 505-768-3614) is the authoritative source.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (state-operated)** | No |
| **ARTGN status** | Operational status undocumented post-2013; no recent press releases or municipal updates found |
| **NMDOT** | Operates CORS stations primarily for internal department survey work; restricts real-time RTK access to authorised personnel — not public/hobbyist accessible |
| **Coverage paths** | EarthScope NOTA (free, in-pipeline) — provides Western NM coverage including PBO heritage sites (TUCUMCARI, PIETOWN, WHITE SANDS region) |
| **Most recent project announcement** | None for a public NM caster as of 2026-05-07. Commercial RTKdata (USD 40/mo) covers all 33 NM counties — above $200/yr cutoff. |

### HI — Hawaii

**No state-operated public NTRIP RTK service.** A December 2024 GPS World survey of US public RTK stations explicitly lists Hawaii as having no public service. Pacific GPS Facility (UH SOEST / HIGP) operates real-time GPS processing for research (constraining KOK1, KOKB, MKEA to ITRF2000) but does not run a public NTRIP caster. Kīlauea GPS network is an HVO/USGS+UH+Stanford research collaboration, not public.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Coverage paths** | EarthScope NOTA (free, in-pipeline) — handful of Hawaii stations (e.g. KOKB, MAUI, HILO area) |
| **Commercial** | Topcon Topnet Live (Oct 2024 announcement: 180 new geodetic reference stations across Western US + Hawaii); commercial subscription, pricing not publicly listed. NPS CORS includes 8 Pacific stations (Hawaii Volcanoes, Haleakalā) but `HALE` and `HAVO` were flagged offline as of 2026-05-02 (per US-NPS file). |
| **Most recent project announcement** | Topnet Live expansion (2024-10-28); no public Hawaii state caster announcement located |

---

## Summary Table — by access cost

| State | Service | host:port | Tariff (annual unless noted) | Hobbyist OK? | Last alive |
|---|---|---|---|---|---|
| CA | CRTN (SOPAC) | `132.239.152.4:2102/3/4/5` | USD 100 one-time | Yes (unclear hobbyist policy) | 2026-05-07 |
| OR | ORGN (ODOT) | `167.131.0.205:9879` / `:9881` | Free | Yes | 2026-05-07 |
| AZ | AzCORS (ADWR) | `azcors.azwater.gov:2101` | Free | Yes | 2026-05-07 |
| CO | Mesa County RTVRN | `rtvrn.mesacounty.us:2101` | Free (Western CO only) | Yes | 2026-05-07 |
| NV | LVVWD GPS Network | host n/p, port 9899 | Not listed | Unclear | 2026-05-07 |
| UT | TURN GPS (UGRC) | `165.239.144.5:2101` | USD 600/yr | Yes | 2026-05-07 |
| NV | Nevada GPS (UGRC) | `168.179.231.11:2102` / `165.239.144.7:2101` | USD 600/yr (TURN account) | Yes | 2026-05-07 |
| MT | MTSRN | host n/p (mtsrn.org) | USD 1,500/yr | Unclear (no hobbyist tier) | 2026-05-07 |
| WA | WSRN (WSDOT) | host n/p (wsrn3.org) | USD 1,900/yr (1 acct) | Unclear-leaning-no | 2026-05-07 |
| ID | none state-level | n/a | n/a | n/a | n/a |
| WY | none state-level | n/a | n/a | n/a | n/a |
| NM | ARTGN status unverified | n/a | historically ~$200/mo | unverified | unverified |
| HI | none | n/a | n/a | n/a | n/a |

## Volunteer/community casters in US-W (rtk2go)

Per `data/stations.json` summary in country-survey § US (date 2026-05-02): rtk2go has ~142 US bases total, with the **Pacific Northwest** (especially WA + OR) one of the densest US clusters. WA, OR, CA also host individual rtk2go bases. Centipede has ~3 US nodes nationally; coverage in US-W is negligible. (Volunteer counts are derived from data/stations.json via the procedures in `country-survey.proc.md`; this file does not edit them.)

## Gaps and notes

- **ID, WY, NM, HI** have no confirmed free/affordable public NTRIP RTK in 2026. Hobbyists rely on EarthScope NOTA (free, non-commercial NULA) wherever a NOTA station is within usable single-base distance (~30–50 km).
- **NV** state-operated coverage is bifurcated: northern Nevada (Reno area) is now under Utah UGRC management as a paid service; southern Nevada has the LVVWD network with undisclosed pricing and a non-self-service registration path.
- **WSRN (WA)** is significantly more expensive than peer state networks (USD 1,900/yr vs USD 600 for TURN/Nevada GPS, USD 1,500 for MTSRN). PANGA/CWU contributes Puget Sound antennae to WSRN but is not itself a public hobbyist NTRIP source — those antennae are also reachable via free EarthScope NOTA.
- **CRTN's USD 100 one-time fee** is the most affordable Western US gateway to a large station network; falls under the project's $200/yr cutoff. Hobbyist eligibility is not formally stated but the registration form does not exclude individuals.
- **Mesa County RTVRN's footprint** is geographically narrow (Western Colorado only) but the underlying NGS CORS overlap with EarthScope NOTA means duplicate physical pins are expected if both are pipelined.
- **ARTGN (NM)** historical paid service status is the largest unresolved item — needs a direct contact with the Albuquerque City Surveyor to confirm whether the caster is still running.

## Sources Consulted

### Federal / supra-state
- EarthScope NOTA: `ntrip.earthscope.org:2101` (in country-survey.md and networks.md `earthscope`)
- NPS CORS: https://ntrip.nps.gov/ (see `US-NPS_NationalParkService.md`)
- NDGPS decommissioning: federalregister.gov/documents/2018/03/21/2018-05684/ + USCG NavCen + DOT/PNT pages

### CA
- SOPAC CRTN: https://sopac-csrc.ucsd.edu/index.php/crtn/ (observed 2026-05-07; February 2026 station-list update)
- SOPAC CRTN station list and connecting docs: sopac-csrc.ucsd.edu/wp-content/uploads/2019/11/Connecting_to_CRTN_*.pdf
- SDCRTN procedures: sandiegocounty.gov/content/dam/sdc/dpw/COUNTY_SURVEYOR/SDCRTN_procedures2.pdf
- Caltrans D6 RTN page: dot.ca.gov/caltrans-near-me/district-6/district-6-programs/d6-land-surveys/d6-rtn-gps
- 2015 Caltrans Preliminary Investigation memo (multi-state RTN comparison): dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/preliminary-investigations/real-time-gps-networks-pi-a11y.pdf

### NV
- Washoe County GPS Base Stations: washoecounty.gov/csd/engineering_capitalprojects/development_services/gps_base_stations/index.php (UGRC migration noted)
- nevadagps.utah.gov portal
- LVVWD survey/right-of-way page: lvvwd.com/engineering-resources/survey-right-of-way/index.html
- LVVWD account request: lvvwd.com/apps/base-station-network-access/

### OR
- ORGN ODOT: oregon.gov/odot/orgn/pages/index.aspx, products-services.aspx, rover-requests.aspx
- ORGN connection PDFs (host:port): oregon.gov/odot/ORGN/Documents/Network-Connection-TSC2-Trimble-Access.pdf, Single-Base-Solutions-TSC2-Trimble-Access.pdf

### WA
- WSRN: wsrn.org, wsrn3.org (sandbox CI returns ECONNREFUSED but service is documented as operational)
- WSRN FAQ: wsrn3.org/WSRN_FAQ.pdf
- 2015 Caltrans PI memo (pricing tiers)
- 2016 RPLS forum confirmation that WSRN pricing is annual

### ID
- ISU GIS Center RTN history: giscenter.isu.edu/research/Techpg/GC/rtn.htm; pdf/PDF_GC/RTNforIdaho.pdf
- Frontier Precision SE Idaho RTN announcement: frontierprecision.com/news/real-time-gnss-network-southeast-idaho/
- Idaho Geospatial Office Geodetic Control TWG: gis.idaho.gov/geodetic-control-twg

### MT
- MTSRN: msl.mt.gov/mtsrn/, mtsrn.org (Welcome, FAQ, How it Works), msl.mt.gov/about/publications/about-the-library/MTSRN_IBC-E_202412.pdf
- MTSRN launch / pricing announcements: content.govdelivery.com/accounts/MTLIBRARY/bulletins/391a2ef and 393bfda

### WY
- PLSW CORS: plsw.org/cors/
- Wyoming Geodetic Coordination: geodetic.geospatialhub.org/pages/resources

### UT
- UGRC TURN GPS: gis.utah.gov/products/turn/, gis.utah.gov/documentation/turn/connecting/, gis.utah.gov/products/sgid/cadastre/turn-gps/
- TURN GPS portal: turngps.utah.gov, secure.utah.gov/turngps/, turngps-billpay.ugrc.utah.gov/

### CO
- Mesa County RTVRN: mesacounty.us/departments-and-services/public-works/gps-survey/real-time-virtual-reference-network-rtvrn
- RTVRN portal: rtvrn.mesacounty.us, rtvrn.mesacounty.us/RegisterAccount.aspx
- Mesa County 2025-05 documentation: mesacounty.us/sites/default/files/2025-05/RTVRN%20Mountpoint%20Names.pdf, RTVRN%20Login%20Instructions%20and%20NTRIP%20Mountpoints.pdf

### AZ
- ADWR AzCORS: azwater.gov/hydrology/azcors
- AZCORS Information and Mountpoints PDF (Feb 2024): azwater.gov/sites/default/files/2024-02/AZCORS_InformationAndMountpoints.pdf
- ADWR 2025-03-19 expansion press release: azwater.gov/news/articles/2025-03-19
- AZGPS (commercial): azgps.net

### NM
- ARTGN background (American Surveyor 2010): amerisurv.com/2010/12/05/real-time-gnss-network-in-new-mexico/
- City of Albuquerque AGRS page: cabq.gov/municipaldevelopment/architects-engineers-contractors/construction-services/albuquerque-geodetic-reference-system
- ARTGN connection guide (2013, archived): yumpu.com/en/document/view/17923468/
- City contact: Loren Risenhoover, 505-768-3614

### HI
- Pacific GPS Facility (UH SOEST): soest.hawaii.edu/pgf/, soest.hawaii.edu/pgf/SEQ/processing.shtml
- Topcon Topnet Live expansion (Oct 2024): topconpositioning.com/us/en/articles/topcon-announces-significant-expansion-of-topnet-live-coverage-across-western-usa-and-hawaii
- GPS World 2024 public RTK base stations list: gpsworld.com/finally-a-list-of-public-rtk-base-stations-in-the-u-s/

```
