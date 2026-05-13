# Bhutan [BT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: YES — active government NTRIP caster (DrukNet / MIRACaster); annual subscription required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government-operated; annual subscription required) |
| **Operator** | National Land Commission Secretariat (NLCS), Royal Government of Bhutan |
| **Network name** | DrukNet GNSS National Network |
| **Caster software** | MIRACaster (operated by MIRASpaco — Measuring Earth from Space, Portugal) |
| **host:port — NLCS DrukNet** | `ntrip.druknet.net:2101` (IP: 103.252.84.100) |
| **tariff — Government agencies** | Nu. 10,000 / year · unlimited simultaneous users (Dzongkhags + 4 Gelyong Thromdes) |
| **tariff — Corporations / private firms** | Nu. 10,000 / year · 1 user · Basic; Nu. 17,500 / year · 2 users · Standard; Nu. 22,500 / year · 3 users · Premium |
| **tariff — Educational / research** | Free — official supporting document proving teaching/research purpose required |
| **hobbyist_eligibility** | Individual hobbyist tier not explicitly defined; educational/research free tier may be accessible to serious hobbyists who can submit a supporting letter demonstrating research intent |
| **legal_residency_required** | Not stated; pre-registration form open globally at miranet.druknet.net |
| **last_confirmed_alive** | 2026-05-12 — `miranet.nlcs.gov.bt` HTTP 200 (Apache/2.4.52 Ubuntu); `web.nlcs.gov.bt/cors-facility/` HTTP 200 (nginx/1.18.0) with tariff schedule unchanged from 2026-05-06 snapshot; NSDI metadata still revised August 2024. Direct NTRIP SOURCETABLE probe of `ntrip.druknet.net:2101` not executed (NTRIP/2.0 not testable in this sandbox); HTTP-layer reachability of the portal confirmed. |

## Most Recent Project Announcement

- **August 2024**: NLCS CORS / DrukNet NSDI metadata record last revised (nsdi.systems.gov.bt), confirming 13 CORS stations operational.
- **2023**: Two new stations (SIPS and ZHEM) added, bringing total to 13 active stations. Leica hardware; server hosted by MIRASpaco (Portugal).
- **May 2025**: NLCS published NCRP Journal 2025 (web.nlcs.gov.bt), confirming NLCS institutionally active and CORS network context referenced.
- **2014**: Network founded with 6 initial CORS stations (THIM, BUMT, KANG, PHUN, GELE, DEOT). Note: DEOT and GELE are flagged for decommissioning; effective current total may vary.

## Context Notes

- **DrukNet** is the official name of Bhutan's national GNSS CORS network; **MIRACaster** is the caster software/portal. The NTRIP server is maintained by MIRASpaco (Portugal) on behalf of NLCS. The MIRANet web application at miranet.nlcs.gov.bt / www.miranet.druknet.net provides RINEX data download and account management.
- **13 CORS stations** as of 2024 (NSDI metadata confirmed); covers ~38,000 km² of mountainous terrain. Stations installed in waves: 6 in 2011–2012 (THIM, BUMT, KANG, PHUN, GELE, DEOT); DTNG added 2020; WNGD, DGPL added 2020; HAAC, LHUN, SPGT added 2022; SIPS, ZHEM added 2023. DEOT and GELE flagged for decommissioning (net operational count may be 11–13).
- **Geographic coverage**: West 88.626°E to East 92.232°E; South 26.417°N to North 28.496°N.
- **Each subscription allows one simultaneous connection** per user slot (Basic = 1 slot, Standard = 2, Premium = 3).
- **Pre-registration**: Form at https://miranet.druknet.net/pre-registration/form — fields: Full Name, Email, Organization (optional), Telephone, Preferred Username. Account activated after administrative approval; credentials sent automatically.
- **RINEX post-processing**: Daily and hourly RINEX data available for download on the MIRANet portal; included in subscription. Educational accounts also get RINEX access.
- **Official vertical datum**: DrukGeoid 2015 used with CORS network for cadastral surveys.
- **Cadastral guidelines** (NLCS, Dec 2023): baseline up to 40 km acceptable using CORS as base station. Precision claimed: centimeter-level horizontal RTK.
- **Contact**: Jamphel Gyeltshen, Topographic Division, Sr. Surveyor — Phone: 02-331447. NLCS main office: web.nlcs.gov.bt.
- **VAT/tax**: Bhutan corporate tax is 25%; subscription tariffs as listed on CORS Facility page do not specify whether taxes are inclusive or exclusive.
- Bhutan's network is notably advanced for its size and economic context, reflecting sustained NLCS institutional investment in geodetic infrastructure since 2011.
- No Bhutan stations appear in the RTK2go or Centipede sourcetables (confirmed monitor.use-snip.com check at research date).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **DrukNet MIRANet RINEX archive** — daily and hourly data, 13 stations | https://miranet.nlcs.gov.bt | Included in paid subscription (Nu. 10,000–22,500/yr); free with educational account |
| **IGS / EarthScope archive** — any IGS stations in Bhutan, if any | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- NLCS CORS Facility page (tariff tiers confirmed): https://web.nlcs.gov.bt/cors-facility/
- DrukNet / MIRANet portal: https://miranet.nlcs.gov.bt/
- MIRANet pre-registration form: https://miranet.druknet.net/pre-registration/form
- Bhutan NSDI CORS metadata (13 stations, revised Aug 2024): https://nsdi.systems.gov.bt/portal/sharing/rest/content/items/453406824ec04042b261c114cea594f9/info/metadata/metadata.xml?format=default&output=html
- NLCS GNSS-RTK Cadastral Guideline v1 Dec 2023: https://web.nlcs.gov.bt/wp-content/uploads/2023/12/Guideline-for-using-GNSS-RTK-in-Cadastral_Surveyingv1.pdf
- NLCS NCRP Journal 2025: https://web.nlcs.gov.bt/wp-content/uploads/2025/05/NCRP_JOURNAL_2025.pdf
- NLCS CORS Notification page: https://web.nlcs.gov.bt/cors-notification/
- MIRASpaco GNSS page: https://miraspaco.com/gnss/
- RTK2go monitor (no BT stations): http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- curl probe of `ntrip.druknet.net:2101` — NOT EXECUTED: sandbox TCP/shell tools blocked during research 2026-05-06. miranet.nlcs.gov.bt WebFetch returned HTTP 200 (portal active). Direct NTRIP SOURCETABLE response NOT confirmed.
