# Sri Lanka [LK] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: TWO active NTRIP RTK casters in Sri Lanka

1. **SLCORSnet** — government, Survey Department of Sri Lanka, public LKR pricing, registration open online, Phase-1 coverage (Western Province). Confirmed live `222.165.190.67:2101` 2026-05-23.
2. **CORSnet** — private commercial, islandwide ~21 stations, no public pricing (sales-quote). Web portal alive but caster `corsnet.lk:2101` TCP times out from sandbox 2026-05-23 (probable geo-restriction).

Both casters require payment + registration. There is **no free public NTRIP RTK option for Sri Lanka** — no rtk2go, Centipede, or volunteer base on the island as of 2026-05-23 (local pipeline 0 LK in those sources). AUSCORS rebroadcasts 1 LK IGS station (SGOC, Colombo) and MIRAI carries 2 (QKNP, SGOC) — useful single-base context for Colombo-area hobbyists who can register with those casters, but neither offers VRS in LK.

---

## SLCORSnet — Sri Lanka Continuously Operating Reference Station Network (government)

| Field | Value |
|---|---|
| operator | Survey Department of Sri Lanka (Surveyor General's Office, Colombo) — Ministry of Lands |
| landing_url | http://www.slcorsnet.survey.gov.lk/ |
| access_url | http://www.slcorsnet.survey.gov.lk/how-to-use/pricing/ |
| access_type | paid |
| coverage | Phase 1 (current as of 2026-05-23): Western Province + surrounding areas — Colombo, Gampaha, Kalutara districts, supports VRS RTK throughout that hull. Full-island + offshore-hydrographic coverage planned; no completion date announced. About-page station counters render as `0+` placeholders. The 7-mountpoint sourcetable carries all rows at the same fixed coordinate (6.50 N, 79.50 E — Western Province centroid), suggesting a small physical-station cluster supporting the VRS computation. |
| num_stations | small (single-digit) physical CORS supporting Phase-1 Western-Province VRS — exact count not published on operator portal (checked: slcorsnet.survey.gov.lk About 2026-05-23 — placeholder `0+` counters; survey.gov.lk Geodetic Survey page 2026-05-23 — no count). The 21-station figure in some third-party summaries is CORSnet (private), not SLCORSnet (government). |
| sourcetable | `222.165.190.67:2101` SOURCETABLE 200 OK 2026-05-23 (Server `GNSMART_Caster/1.0`, Content-Length 1273). 7 STR rows: `FKP` (RTCM 3.0 FKP), `MAC` (RTCM 3.1 MAC), `MSM` (RTCM 3.2 MSM5 GPS+GLO+GAL+BDS), `SBASE_MSM4` (RTCM 3.2 MSM4 single-base, solution=0), `VRS` (RTCM 3.0), `VRS_BDS` (RTCM 3.2 VRS with BDS), `VRS_MSM4` (RTCM 3.2 VRS with MSM4). All STR rows nmea=1, all NRTK rows solution=1, single-base row solution=0; all rows at 6.50 N, 79.50 E (Western Province centroid placeholder, not physical station coordinates). Format-details fields include datum-related RTCM messages 1030, 1031, 1032 (network-RTK residuals + reference-station coordinates) — confirms standard GNSMART back-end NRTK. |
| vrs | yes — explicit `VRS`, `VRS_BDS`, `VRS_MSM4` mountpoints, plus FKP and MAC. Single-base `SBASE_MSM4` also available. |
| tariff | All-tax-inclusive LKR pricing, per `http://www.slcorsnet.survey.gov.lk/how-to-use/pricing/` curl-fetched 2026-05-23: **1 day (24 h) = 2,000 LKR; 7 days = 10,000 LKR; 30 days = 30,000 LKR; 365 days = 360,000 LKR.** 30-day and 1-year tiers also receive free GNWEB (online RINEX delivery) + SSRPOST (online post-processing) access for the same period. Payment: cash deposit to Department of Survey's official bank account (per pricing page 2026-05-23: "all users are requested to directly deposit cash into the Department of Survey's Bank account and email or fax the Bank cash deposit slip to the SLCORSnet admin"). Account: Surveyor General, account 119-1-001-0-9027253, People's Bank Narahenpita branch; fax deposit slip to 011 2055971; account activation within 28 h. |
| hobbyist_eligibility | yes — operator-named addressable users: "Anyone who needs real-time cm level GNSS positioning"; no surveying-licence gate on slcorsnet.survey.gov.lk; no professional-credential check at registration. |
| residency_required | no (legally) — no statutory or operator declaration. De-facto barrier is the LKR-cash-deposit payment rail: a foreign hobbyist needs a Sri Lankan bank account or an in-country proxy to complete payment at People's Bank Narahenpita. ArduSimple note ("website may not be very user-friendly") underscores the UX barrier. |
| stations_source | Live sourcetable at `222.165.190.67:2101` (only the VRS+single-base mountpoint inventory; no per-physical-station coords). Operator About page `http://www.slcorsnet.survey.gov.lk/about/` 2026-05-23 — placeholder `0+` counters. Survey Department Geodetic Survey page `https://survey.gov.lk/sdweb/pages_service_geodetic_survey.php?id=d80d8ae23ba3e3a32bea5739e9a83e4246930dae&l=s` cross-links to slcorsnet. |
| datum_epoch | WGS84 → SLD99 (Sri Lanka Datum 1999) transformation broadcast in the RTCM stream — SLCORSnet About page 2026-05-23 explicitly states "Also provides live-streaming of DATUM transformation parameters coupled with standard RTCM." Survey Department Geodetic Survey page 2026-05-23: "The transformation parameters were computed from the global datum called WGS84 to local datum called Everest 1830." SLD99 (EPSG:5235) is on Everest 1830 (1937 adjustment) ellipsoid, transverse Mercator with origin 7.00047 N / 80.77171 E. ITRF realisation/epoch of the WGS84 side not declared by operator; academic literature (Survey Review 2010 / current science articles) notes SLD99 "has not been connected properly to the ITRF, … around 1.9 m vertical deviation in Sri Lankan GPS datum with respect to the latest realization of ITRF." Working assumption for a cm-accurate user: rover receives WGS84-aligned RTCM with on-the-fly SLD99 transformation messages applied; horizontal accuracy benefits from the transform, vertical has known 1.9 m bias relative to current ITRF. |

### NRTK / VRS notes

- SLCORSnet was established at the end of 2016 (Geodetic Survey page; SLCORSnet About).
- GNSMART back-end (Geo++ GmbH Garbsen, Germany; same enterprise platform used by SAPOS Germany and many other national NRTK networks). Possible German technical-cooperation origin not confirmed in any source 2026-05-23; treated as off-the-shelf vendor choice rather than aid-funded.
- RTCM messages 1030/1031/1032 in network-RTK streams indicate proper NRTK residuals + station coordinate broadcasting.
- The seven mountpoints serve different rover-capability classes: legacy RTCM 3.0 (VRS), RTCM 3.1 (MAC), RTCM 3.2 multi-constellation (VRS_BDS, VRS_MSM4, MSM, SBASE_MSM4), plus FKP for rovers capable of using broadcast plane-correction parameters.
- "PRS" (Pseudo Reference Station) is documented on the About page as an additional service for older rovers not designed for NRTK — not present in sourcetable, likely a software mode within VRS.
- **GNWEB** = online RINEX raw-data delivery (physical-station or Virtual RINEX, for post-processing). **SSRPOST** = Geo++ online autonomous post-processing service for GNSS raw data — both included free with 30-day and 1-year tiers, otherwise priced separately.
- **Phase-1 hull and southern reach:** operator describes Phase 1 as "Western province and surrounding areas" (Colombo, Gampaha, Kalutara). No operator statement confirms VRS-quality coverage extends to Galle/Matara (Southern Province, ~120–160 km from Colombo) or the central hills (Kandy / Nuwara Eliya). For users beyond the Phase-1 hull a Phase-2 island-wide rollout is planned (no date announced 2026-05-23). The MIRAI-rebroadcast IGS station QKNP near Kandy (see Scientific-network presence below) is the practical single-base fallback for the central region.
- **No free or academic trial tier** found in any operator-portal page 2026-05-23 (checked: slcorsnet.survey.gov.lk how-to-use, pricing, about, primary-services, secondary-services). Unlike India SoI's free academic/government access, SLCORSnet's published model is paid-only for all users.
- **Operational longevity caveat for hobbyists:** SLCORSnet HTTPS cert expired 2026-05-23 (HTTP and curl-k still functional); a hobbyist purchasing a 1-year (360,000 LKR) tier should weigh maintenance posture before committing.
- **24-h activation vs 1-day tier viability:** the cash-deposit-and-fax payment process plus 28-h activation SLA means the 2,000 LKR / 1-day pass is effectively unusable for same-day or next-day rover work — only sensible for users who can pre-stage payment a day or two before fieldwork.

---

## CORSnet — CORSnet (Pvt) Ltd (private)

| Field | Value |
|---|---|
| operator | CORSnet (Pvt) Ltd, spun off from SULECO (Pvt) Ltd. Address: No. 44, Beddagana South, Pita Kotte. |
| landing_url | https://corsnet.lk/ |
| access_url | https://corsnet.lk/user/register/ |
| access_type | paid |
| coverage | Islandwide Sri Lanka. CORSnet (Pvt) Ltd homepage 2026-05-23: "first, islandwide" RTK network; SULECO legacy page (sulecoltd.com/cors-rtk/) names Western + Sabaragamuwa as initial 2014-launch focus that has since extended to the whole country. Stated service hours: 172,000+ RTK service-hours; 315+ active customers (corsnet.lk banner 2026-05-23). |
| num_stations | 21 (corsnet.lk homepage 2026-05-23; some third-party summaries cite 23 or legacy 17 — homepage is authoritative). |
| sourcetable | `corsnet.lk:2101` curl probe 2026-05-23 — TCP connection timed out after 15 s (egress geo-restriction to LK presumed, not a confirmed outage). HTTPS web portal corsnet.lk:443 returns 200 from sandbox 2026-05-23 (homepage + register + FAQ + about pages all reachable). No public sourcetable cache. Mountpoint inventory undisclosed pre-login. |
| vrs | yes — operator documents DGNSS, single-base RTK, Network RTK / VRS, RINEX post-processing. Correction formats: RTCM 2.x / 3.x, CMR, CMR+, sCMRx, RTD, NMEA. |
| tariff | not on public website; pricing on enquiry via `info@corsnet.lk` / phone (+94 77 213 1310, +94 77 038 2265) (checked: corsnet.lk homepage 2026-05-23; corsnet.lk/about-us/ 2026-05-23; corsnet.lk/industries/ 2026-05-23; corsnet.lk/faq/ 2026-05-23; sulecoltd.com/cors-rtk/ 2026-05-23 — "multiple packages" mentioned, no LKR figure published). |
| hobbyist_eligibility | yes — registration form (`corsnet.lk/user/register/`) requires only name, company, email, password, phone, address; no professional-credential check. |
| residency_required | no — registration form open; payment rail not publicly disclosed but corsnet.lk has online "Get New Connection" flow suggesting digital payment options exist (unlike SLCORSnet's cash-deposit-only model). |
| stations_source | Operator-portal post-login (mountpoint inventory delivered via CORSnet dashboard after subscription). No public coverage map URL beyond marketing prose on the homepage. |
| datum_epoch | SLD99 grid (Sri Lanka Datum 1999) — corsnet.lk homepage 2026-05-23 states "SLD99 grid coordinates" as the output reference. Same Everest 1830 ellipsoid as SLCORSnet's transformation target. WGS84 → SLD99 transformation applied by the rover or the caster; ITRF realisation/epoch of the WGS84 side not declared by operator. Same ~1.9 m vertical-deviation caveat vs latest ITRF applies. |

### Private-caster prose

CORSnet was launched 20 May 2014 by SULECO (Pvt) Ltd as Sri Lanka's first islandwide commercial CORS RTK network (initial focus Western + Sabaragamuwa provinces). Operations now under the spinoff CORSnet (Pvt) Ltd; SULECO provides technical/sales support. Accuracy claims (sulecoltd.com / corsnet.lk): 2.5 mm + 0.5 ppm (static post-processing), 15 mm + 1 ppm (RTK). Service modes documented: DGNSS (sub-metre code), single-base RTK, Network RTK / VRS, RINEX post-processing. Customer testimonials describe "affordable pricing" but no LKR figure is published publicly; bracket positioning relative to SLCORSnet's published 30,000 LKR/month tier is unknown — interested users must contact sales.

---

## Cross-border reachability + scientific-network presence

Sri Lanka is geographically isolated (~30 km strait to India, otherwise ocean). The only neighbouring NTRIP option is India SoI CORS Region 3 — Tamil Nadu side. But SoI requires an Indian-resident photo ID, blocking LK nationals. **No realistic cross-border free RTK path.** See `docs/ntrip_research/IN_India.md`.

Scientific-network presence in Sri Lanka:

- **IGS station SGOC** (Survey Department, Narahenpita, Colombo — 6.892 N, 79.874 E per IGS Network station log `network.igs.org/SGOC00LKA`). Real-time GNSS + RINEX active. AUSCORS rebroadcasts it (local pipeline 2026-05-23: 1 LK row); MIRAI also carries it (local pipeline 2026-05-23: 2 LK rows = SGOC + QKNP).
- **QKNP** (Kandy area, 7.27 N, 80.73 E per local pipeline 2026-05-23). Not present in current IGS Network public station-log query (`network.igs.org/QKNP00LKA` → HTTP 404 2026-05-23); appears to be a Sri Lankan secondary GNSS station rebroadcast through MIRAI without an IGS station log. Operator/host institution not publicly identified (Survey Department secondary station, academic deployment at Peradeniya University, or Japanese-funded research station are plausible but unconfirmed — checked: network.igs.org, mirai station map, Peradeniya University Faculty of Geomatics 2026-05-23 with no QKNP attribution surfaced).
- Real-time RTCM access via AUSCORS/MIRAI is registration-gated but free for academic/research use, and gives a single-base option in Colombo (via SGOC) and Kandy (via QKNP) without involving SLCORSnet/CORSnet — see `docs/ntrip_research/AUSCORS.md` and primer for MIRAI details. **Practical implication: for a hobbyist in central-hills Sri Lanka (Kandy / Nuwara Eliya / tea estates) beyond SLCORSnet's Phase-1 Western-Province hull, MIRAI-rebroadcast QKNP is the de-facto single-base RTK option short of CORSnet's quote-priced commercial service.**
- MIRAI is Japanese-operated (Cabinet Office of Japan, QZSS Strategy Office); the EarthScope/UNAVCO 2025-07-29 real-time-platform retirement does not affect MIRAI's data flow.

---

## Disqualified / context (covered in own files)

- **rtk2go** — 0 LK-tagged mountpoints (local pipeline 2026-05-23; live rtk2go sourcetable has no LKA rows). See `docs/ntrip_research/Rtk2go.md`.
- **Centipede-RTK** — 0 LK-tagged mountpoints (local pipeline 2026-05-23; live Centipede sourcetable has no LKA rows). See `docs/ntrip_research/Centipede.md`.
- **IGS-IP** — `SGOC` (Survey Department, Colombo) is an IGS station but is rebroadcast via AUSCORS/MIRAI in our pipeline, not via the primary `igs-ip.net` caster (local pipeline 2026-05-23: 0 LK rows in `igs_ip.sourcetable`). See `docs/ntrip_research/IGS-IP.md`.
- **EUREF-IP** — no LK stations (regional scope is Europe). See `docs/ntrip_research/EUREF-IP.md`.
- **EarthScope / NOTA RTGPS** — no LK stations (Americas-region scope; legacy UNAVCO real-time platform retired 2025-07-29). See `docs/ntrip_research/Earthscope.md`.
- **GEODNET / HYFIX / ONOCOY / PointOne / RTKdata / TopNET Live** — no Sri Lanka-specific coverage publicly disclosed in any of these networks' station maps 2026-05-23 (checked station maps and dealer directories).
- **Global GIS (globalgis.lk)** — Sri Lankan surveying-equipment dealer (Nugegoda; founded 2014 by Sabaragamuwa University Faculty of Geomatics graduates; D. Nishshanka De Silva, licensed surveyor). Operates a `cors-network` page that publishes LKR-priced packages (Starter 2,000 LKR/day; Basic 12,600 LKR/week; Premium 45,000 LKR/month; Starter+ 112,500 LKR/3-mo; Basic+ 180,000 LKR/6-mo; Premium+ 300,000 LKR/year — `globalgis.lk/cors-network/` 2026-05-23) **but is a reseller of "SLSD CORS Network" (Sri Lanka Survey Department) — i.e. SLCORSnet — not an independent CORS operator** (company-page quick-links direct users to `slcorsnet.survey.gov.lk`; vendor portfolio is eSurvey/Kolida/GeoMax/Pentax/SXBlue/MicroSurvey/Ohmex/Keson — no caster-software vendor listed). The Global GIS pricing is reseller-markup over SLCORSnet's published 2,000/10,000/30,000/360,000 LKR tiers and is interesting only as a third-party access path (potentially smoother payment than the cash-deposit-and-fax flow on slcorsnet.survey.gov.lk). Treated as covered by the SLCORSnet entry above; no separate caster.
- **`scripts/stations_by_radius.py 7.0 81.0 500`** 2026-05-23 — only the AUSCORS/MIRAI SGOC + MIRAI QKNP entries; no volunteer base within 500 km. Sri Lanka is geographically isolated from any free volunteer network.

## Sources Consulted (2026-05-23)

- SLCORSnet sourcetable live probe: `curl --http0.9 http://222.165.190.67:2101/` 2026-05-23 → SOURCETABLE 200 OK, GNSMART_Caster/1.0, 7 STR rows.
- SLCORSnet homepage: `http://www.slcorsnet.survey.gov.lk/` (HTTPS cert expired 2026-05-23; HTTP and curl -k both work).
- SLCORSnet pricing page (curl-fetched 2026-05-23 — confirms 2,000 / 10,000 / 30,000 / 360,000 LKR tiers; People's Bank Narahenpita Surveyor General account 119-1-001-0-9027253; 28 h activation; fax 011 2055971): `http://www.slcorsnet.survey.gov.lk/how-to-use/pricing/`.
- SLCORSnet How-to-use: `http://www.slcorsnet.survey.gov.lk/how-to-use/`.
- SLCORSnet About: `http://www.slcorsnet.survey.gov.lk/about/` (confirms DATUM transformation parameters live-streamed with RTCM; Phase-1 Western Province coverage; established end of 2016).
- Survey Department of Sri Lanka — Geodetic Survey / CORS Network: `https://survey.gov.lk/sdweb/pages_service_geodetic_survey.php?id=d80d8ae23ba3e3a32bea5739e9a83e4246930dae&l=s` (WGS84 → Everest 1830 transformation parameters statement).
- Survey Department home: `https://survey.gov.lk/`.
- Sri Lanka NSDI: `https://nsdi.gov.lk/survey-department-sri-lanka`.
- CORSnet homepage: `https://corsnet.lk/` (21 stations, 172k+ RTK hours, 315+ customers, SLD99 grid).
- CORSnet About: `https://corsnet.lk/about-us/`.
- CORSnet Industries: `https://corsnet.lk/industries/`.
- CORSnet Register: `https://corsnet.lk/user/register/`.
- CORSnet FAQ: `https://corsnet.lk/faq/`.
- CORSnet TCP probe 2026-05-23: `curl http://corsnet.lk:2101/` — connection timed out 15 s (sandbox geo-restriction presumed).
- SULECO legacy CORS page: `https://sulecoltd.com/cors-rtk/` (2014 launch history, accuracy 2.5 mm + 0.5 ppm static / 15 mm + 1 ppm RTK).
- ArduSimple Sri Lanka dealer cache: `docs/ardusimple/LK_SriLanka.md` 2026-05-16 — names SLCORSnet as the national paid service.
- ArduSimple Sri Lanka page: `https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-sri-lanka/`.
- SLD99 / Sri Lanka Grid 1999 EPSG:5235: `https://epsg.io/5235` (Everest 1830 1937 ellipsoid, transverse Mercator origin 7.00047 N / 80.77171 E).
- Survey Review (Curtin espace) "On the Geodetic Datums in Sri Lanka": `https://espace.curtin.edu.au/bitstream/handle/20.500.11937/3840/137779_137779.pdf?sequence=2` (SLD99-ITRF connection issues; ~1.9 m vertical deviation).
- Journal of Geospatial Surveying (Sri Lanka): `https://jgs.sljol.info/articles/10.4038/jgs.v2i1.34` (GPS-levelling datum variation case study).
- KDU repository "Review on National Geodetic Control Network — SLD_99": `https://ir.kdu.ac.lk/bitstream/handle/345/3252/pdfresizer.com-pdf-split%20(10).pdf?sequence=1&isAllowed=y`.
- Local pipeline counts via `scripts/stations_by_country.py LKA` 2026-05-23: auscors = 1 (SGOC 6.89,79.87), mirai = 2 (SGOC, QKNP 7.27,80.73); centipede / igs_ip / euref_ip / earthscope / rtk2go = 0.
- Global GIS LK (SLCORSnet reseller; LKR pricing schedule): `https://globalgis.lk/cors-network/` 2026-05-23; company page `https://globalgis.lk/company/` 2026-05-23 (founders, vendor portfolio).
- Geo++ GNSMART back-end vendor: `https://www.geopp.de/gnsmart-network-rtk/` (Geo++ GmbH Garbsen, Germany — same enterprise NRTK platform as SAPOS DE).
- IGS Network SGOC station log: `https://network.igs.org/SGOC00LKA` 2026-05-23 (Narahenpita, Colombo; 6.892075 N, 79.874178 E; GPS+GLO+GAL+BDS+QZSS+SBAS).
- IGS Network QKNP station log: `https://network.igs.org/QKNP00LKA` — HTTP 404 2026-05-23; no public IGS station log under this code, despite the QKNP mountpoint being rebroadcast in MIRAI's sourcetable.
