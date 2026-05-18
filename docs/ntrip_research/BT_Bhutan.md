# Bhutan [BT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior 2026-05-15, 2026-05-12, initial 2026-05-06)

## Status: YES — active government NTRIP caster (DrukNet / MIRACaster); annual subscription required; live SOURCETABLE confirmed 2026-05-15

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government-operated; annual subscription required) |
| **Operator** | National Land Commission Secretariat (NLCS), Royal Government of Bhutan |
| **Network name** | DrukNet GNSS National Network |
| **Caster software** | MIRACaster (Server header: `NTRIP MIRACaster MIRASpaco-00001/2.0`); platform branded MiraNet v2.0.0, operated by MIRASpaco (Portugal) |
| **landing_url** | https://web.nlcs.gov.bt/cors-facility/ |
| **access_url** | https://miranet.druknet.net/pre-registration/form |
| **host:port** | `ntrip.druknet.net:2101` (hostname does not resolve in public DNS; direct IP `103.252.84.100:2101` returned SOURCETABLE 200 OK on 2026-05-17 re-probe) |
| **num_stations** | 14 active mountpoints in live sourcetable (re-confirmed 2026-05-17): THIM, BUMT, KANG, PHUN, DTNG, LHUN, DGPL, HAAC, SPGT, WNGD, SIPS, ZHEM, GASA, JOMO. All RTCM3.3; multi-GNSS (BDS+GAL+GLO+GPS+IRS+QZS+SBAS) |
| **RTCM messages** | Sourcetable STR rows advertise RTCM 3.3 with MSM7 across all constellations (per probe 2026-05-17; sourcetable Server header `NTRIP MIRACaster MIRASpaco-00001/2.0`). Format-details field per STR row contains the MSM7 set `1077` (GPS), `1087` (GLONASS), `1097` (Galileo), `1107` (SBAS), `1117` (QZSS), `1127` (BeiDou) alongside station metadata (1005/1006/1007/1008/1033) and ephemeris messages; exact per-row message-list strings vary per mountpoint and are recorded in the cached sourcetable. Carrier flag = 2 (L1+L2). nmea=0, solution=0 across all 14 mountpoints (single-base, no rover GGA required). |
| **vrs** | No — single-base only; 14 physical mountpoints, no VRS/MAC/iMAX entries in sourcetable |
| **tariff — Government agencies** | Nu. 10,000 / year · "unlimited users" (Dzongkhags + 4 Gelyong Thromdes) |
| **tariff — Private sector** | Basic Nu. 10,000 / yr · 1 user; Standard Nu. 17,500 / yr · 2 users; Premium Nu. 22,500 / yr · 3 users |
| **tariff — Educational / research** | Free — official supporting document proving teaching/research purpose required |
| **Simultaneous-connection rule** | CORS Facility page: *"Simultaneous connections to the network are not allowed, that is, each subscription can only make one connection to the network at the same time"* and *"the users will be given **a** credential (Username and Password)"* (singular). Operator text is ambiguous between (a) the 1/2/3-user tiers granting N separate credentials, each one-session-at-a-time, and (b) one shared credential with N being an authorised-headcount cap. Resolving requires contacting NLCS directly. |
| **hobbyist_eligibility** | **No** (see note) |
| **legal_residency_required** | Not stated; pre-registration form at miranet.druknet.net accepts global submissions, but credentials are released only after administrative approval |
| **datum_epoch** | **omitted — no operator-declared horizontal datum for RTK output.** NLCS Cadastral Guideline v1 Dec 2023 declares vertical (DrukGeoid 2015) only; no horizontal frame is declared by NLCS for the DrukNet RTK output. Per primer [datum-epoch] vertical-only declarations do not populate this field. |
| **last_confirmed_alive** | 2026-05-17 — direct TCP probe `curl --http0.9 http://103.252.84.100:2101/` returned `SOURCETABLE 200 OK` from `NTRIP MIRACaster MIRASpaco-00001/2.0`, server date `Sun, 17 May 2026 14:06:12 GMT`, 14 STR records, 1,766 bytes. CORS Facility page WebFetch 2026-05-17 returned identical tariff schedule; CORS Notification page latest entry still 3 September 2025. |

## Most Recent Project Announcement

- **3 September 2025**: NLCS published a CORS Notification on web.nlcs.gov.bt/cors-notification/ (image-only; text not machine-readable from the page).
- **May 2025**: NCRP Journal 2025 published (web.nlcs.gov.bt) — confirms NLCS institutionally active.
- **2025–2026 (inferred from live sourcetable)**: Two new mountpoints **GASA** (27.908°N, 89.728°E — Gasa Dzongkhag, north-west) and **JOMO** (26.894°N, 92.099°E — easternmost station, near Trashigang) appear in the current sourcetable but were not in prior 2024 NSDI metadata (which listed 13 stations). DEOT and GELE no longer appear, consistent with 2024 decommissioning flag.
- **August 2024**: NSDI CORS metadata last revised (13 stations at that time).
- **2014**: Network founded with 6 initial CORS stations.

## Context Notes

- **DrukNet** is the official name of Bhutan's national GNSS CORS network; **MIRACaster** is the NTRIP caster software, hosted by **MIRASpaco** (Portugal) on behalf of NLCS. The MIRANet web application at miranet.nlcs.gov.bt / www.miranet.druknet.net provides RINEX download and account management.
- **14 active mountpoints** (2026-05-15 SOURCETABLE), up from 13 in 2024 NSDI metadata. Net change: +GASA, +JOMO; –DEOT, –GELE (decommissioning previously flagged). Coverage spans ~88.88°E (SIPS) to ~92.10°E (JOMO), ~26.82°N (DTNG) to ~27.91°N (GASA) — broadly all of Bhutan; max baseline within country ~370 km.
- **Mountpoint format**: all 14 streams are RTCM 3.3, multi-constellation (GPS+GLO+GAL+BDS+QZS+IRS+SBAS). Carrier flag = 2 (L1+L2). No NMEA position required (mountpoints are physical base stations, not VRS).
- **Pre-registration**: Form at https://miranet.druknet.net/pre-registration/form — fields: Full Name, Email, Organization (optional), Telephone, Preferred Username. Credentials issued after administrative approval.
- **Tariff/user-slot interpretation (UNRESOLVED)**: The CORS Facility page says "each subscription can only make one connection at the same time" and that the user receives "a credential" (singular). This is ambiguous between (a) 1/2/3 separate credentials per tier, each one-session-at-a-time, and (b) one shared credential with N being an authorised-headcount cap. The two readings have very different operational implications for multi-user organisations; resolving requires direct contact with NLCS.
- **RINEX post-processing**: Daily and hourly RINEX data available via the MiraNet portal; included in subscription. Educational accounts also receive RINEX access.
- **Datum**: Official vertical datum DrukGeoid 2015. Horizontal datum not declared in published NLCS material (Cadastral Guideline v1 Dec 2023 sets out RTK procedure but does not declare the horizontal frame the DrukNet caster streams in). Cadastral guideline accepts baselines up to 40 km from a CORS base.
- **Hobbyist eligibility rationale**: No explicit hobbyist tier in tariff schedule. Cheapest paid private slot is Nu. 10,000/yr (~USD 120). The free educational/research tier requires an institutional supporting document; a casual hobbyist cannot self-qualify. Net effect: casual hobbyist access is closed — `hobbyist_eligibility = no`.
- **Contact**: Jamphel Gyeltshen, Sr. Surveyor, Topographic Division — Phone: 02-331447. NLCS HQ: web.nlcs.gov.bt.
- **No Bhutan stations in third-party casters**: confirmed not present in RTK2go or Centipede sourcetables; only the official DrukNet caster serves Bhutan CORS data.
- **Cross-border alternatives within ~50 km**: None known. Nearest plausible alternatives are well beyond 50 km — India (no public CORS NTRIP within 50 km of the BT border that hobbyists can access), Nepal, Bangladesh, China (Tibet) — none currently offer open hobbyist-eligible NTRIP feeds in that range.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **DrukNet MiraNet RINEX archive** — daily and hourly data, 14 stations | https://miranet.nlcs.gov.bt | Included in paid subscription (Nu. 10,000–22,500/yr); free with educational account |
| **IGS / EarthScope archive** — any IGS stations in Bhutan, if any | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- Direct NTRIP SOURCETABLE probe (2026-05-15, 20:00:53 UTC): `curl --http0.9 --max-time 10 http://103.252.84.100:2101/` → `SOURCETABLE 200 OK`, 14 STR records (THIM, BUMT, KANG, PHUN, DTNG, LHUN, DGPL, HAAC, SPGT, WNGD, SIPS, ZHEM, GASA, JOMO). DNS `ntrip.druknet.net` returned NXDOMAIN against multiple public resolvers; direct IP works.
- NLCS CORS Facility page: https://web.nlcs.gov.bt/cors-facility/
- DrukNet / MiraNet portal: https://miranet.nlcs.gov.bt/ (MiraNet v2.0.0, live UTC clock 2026-05-15)
- MiraNet pre-registration form: https://miranet.druknet.net/pre-registration/form
- NLCS CORS Notification page (latest 3 September 2025): https://web.nlcs.gov.bt/cors-notification/
- Bhutan NSDI CORS metadata (13 stations, revised Aug 2024): https://nsdi.systems.gov.bt/portal/sharing/rest/content/items/453406824ec04042b261c114cea594f9/info/metadata/metadata.xml?format=default&output=html
- NLCS GNSS-RTK Cadastral Guideline v1 Dec 2023: https://web.nlcs.gov.bt/wp-content/uploads/2023/12/Guideline-for-using-GNSS-RTK-in-Cadastral_Surveyingv1.pdf
- NLCS NCRP Journal 2025: https://web.nlcs.gov.bt/wp-content/uploads/2025/05/NCRP_JOURNAL_2025.pdf
- MIRASpaco GNSS page: https://miraspaco.com/gnss/
- RTK2go monitor (no BT stations): http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
