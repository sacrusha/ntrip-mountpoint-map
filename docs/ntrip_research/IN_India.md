# India [IN] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: YES — national SoI CORS caster (NRTK) operational; paid for private users; Indian-resident photo-ID required

The only pareto NTRIP RTK caster for a hobbyist physically located in India is the Survey of India CORS network (national, paid, Indian-ID-gated). No free or cheaper-than-SoI public option exists with usable density inside India: rtk2go carries 1 IN base, AUSCORS rebroadcasts 2 IN IGS stations, igs_ip carries 3 IN stations — all single-base with multi-hundred-km gaps. Government-but-state CORS networks (Tamil Nadu, Kerala) are closed; Andhra Pradesh's 70 stations were absorbed into SoI via the 13 Oct 2025 MoU.

---

## SoI CORS — Survey of India Continuously Operating Reference Stations

| Field | Value |
|---|---|
| operator | Survey of India (Department of Science & Technology, Govt. of India) |
| landing_url | https://cors.surveyofindia.gov.in/ |
| access_url | https://cors.surveyofindia.gov.in/subscription-charges.html |
| access_type | paid (private/PSU); free for Central Govt, State Govt, and Government academic institutions |
| coverage | National. Region 1 — Punjab, Himachal Pradesh, Uttarakhand, Haryana, Rajasthan, Uttar Pradesh, Bihar, Madhya Pradesh, Chhattisgarh, Telangana, Assam, Arunachal Pradesh, Tripura, Manipur, Mizoram, Meghalaya, Nagaland, plus UTs NCR/Delhi and Chandigarh (16 states + 2 UTs, per `cors.surveyofindia.gov.in/subscription.php` snippet 2026-05-23). Region 2 — Maharashtra, Karnataka, Gujarat, Goa, Kerala, Odisha, Jharkhand, West Bengal, Sikkim, J&K, Ladakh, Andamans, Lakshadweep, Dadra-NH, Daman-Diu. Region 3 — Andhra Pradesh, Tamil Nadu, Puducherry (AP integrated into SoI per 13 Oct 2025 MoU; AP's 70 stations migrating to SoI infrastructure — no separate public AP NTRIP endpoint announced as of 2026-05-23; TN's separate departmental network remains closed and outside SoI). Region 1 is further zoned by SoI into Zone 1 (full RTPS+RDS), Zone 2 (RTPS limited to 30–40 cm DGNSS only; includes Bihar and parts of NE), and Zone 3 (no RTPS/RDS yet). |
| num_stations | 1,105+ physical CORS (operator figure, repeated in SoI X post 2025-10-30 and GoI ISTI portal). Additional 70 ex-AP stations being integrated per 13 Oct 2025 MoU. |
| sourcetable | `103.205.244.106:2101` (Region 1) SOURCETABLE 200 OK 2026-05-23 — Trimble Pivot Caster 5.3, 4 mountpoints: `RTCM_VRS` (RTCM 3.4, GPS+GLO+GAL+BDS+QZS, VRS), `RTCM_FKP` (RTCM SAPOS, GPS+GLO, FKP), `RTCM_MAC` (RTCM3Net, GPS+GLO, MAC), `RTCM_DGNSS` (RTCM 2.3, sub-metre code only). All four flagged nmea=1,solution=1 (NRTK; rover must push GGA). NavIC not advertised in `RTCM_VRS` constellation list despite operator portal text claiming NavIC integration (CORS receivers track IRNSS at the station — broadcast inclusion in NRTK stream unverified). `103.206.29.4:2105` (Region 2) reprobed 2026-05-23 with 20 s timeout, no response from sandbox — consistent with prior probes 2026-05-12/17/23; no independent third-party sourcetable cache located. Per-station physical mounts are not exposed via either NTRIP sourcetable (operator publishes them behind portal login only). |
| vrs | yes (VRS/MAC/FKP all advertised in sourcetable) |
| tariff | Private/PSU only. Private RTK unlimited: ₹5,000 + 18% GST = ₹5,900/mo (₹15,000 + GST / 3 mo; ₹30,000 + GST / 6 mo; annual extrapolates to ~₹60,000 + GST = ₹70,800/yr — annual tier not separately re-confirmed 2026-05-23). RTK + 10 h RINEX bundle: ₹5,032 + GST = ₹5,938/mo. DGNSS (sub-metre code) post-processing: ₹2,164 + GST/mo. Online GNSS Processing (RINEX post-processing service — NOT real-time RTK; epoch-capped data download for static survey post-processing): ₹180 + GST/mo (10 h cap), ₹540 + GST/3 mo, ₹1,800 + GST/6 mo, ₹3,600 + GST/yr. 18% GST rate is standard Indian IT-services rate, not separately operator-cited. Promotional 3-month free window for private individuals ran 1 Nov 2025 – 31 Jan 2026 (LinkedIn SoI post 2025-10-30, Geospatial World coverage); window expired. SoI's "Free Subscription of CORS Services" banner reposted on X 2025-10-30 (status 1983899442022367368) appears to re-promote that same Nov 2025 – Jan 2026 window rather than announce a new one — no later free-period extension confirmed as of 2026-05-23 (checked: SoI X/LinkedIn 2026-05-23; subscription portal WebSearch snippets 2026-05-23). Default treatment: paid for hobbyists today. All figures observed via WebSearch snippets of `cors.surveyofindia.gov.in/subscription-charges.html` 2026-05-23; direct WebFetch from sandbox returned ECONNREFUSED (also tried `cors.surveyofindia.gov.in/policies/subscription_sop.pdf` 2026-05-23 — ECONNREFUSED). |
| hobbyist_eligibility | yes (no surveyor licence required), conditional on Indian-resident photo ID. SoI registration portal lists Voter ID, Driving Licence, Aadhaar Card, or PAN Card as acceptable photo-ID proof. |
| residency_required | yes (effective). All four accepted IDs are Indian-resident documents in the ordinary course. Foreign-national paths exist but require Indian-residency entanglement: (a) resident-foreigner Aadhaar — ≥182-day Indian residency rule per `uidai.gov.in` FAQ "Resident Foreign Nationals" (1461-english-uk); (b) foreign-citizen PAN via Form 95 — see `services.india.gov.in/service/detail/apply-for-pan-card-online-foreign-citizens`. Neither is realistic for a non-resident hobbyist. |
| stations_source | https://cors.surveyofindia.gov.in/ portal map (login-gated for full per-station listing); HTTP fallback http://103.205.244.106/ also serves the portal. Sourcetable on `103.205.244.106:2101` exposes only NRTK mountpoints, not physical bases — physical station list lives behind login. No public unauthenticated station-coverage map located (checked: cors.surveyofindia.gov.in 2026-05-23; surveyofindia.gov.in/pages/continuously-operating-reference-stations-cors- 2026-05-23; Geospatial World / ISTI Portal entries 2026-05-23 — narrative only, no public map image). |
| datum_epoch | omitted — no real-time-service datum statement found in citable operator portal page reachable from sandbox (checked: cors.surveyofindia.gov.in subscription/connection-settings/introduction pages 2026-05-23 ECONNREFUSED; cors.surveyofindia.gov.in/policies/guidelines-for-network-rtk-survey-7.pdf 2026-05-23 WebFetch timeout 60 s; cors.surveyofindia.gov.in/policies/subscription_sop.pdf 2026-05-23 ECONNREFUSED). SoI's national Ground Control Point library is realised in ITRF2008 epoch 2005 (Current Science 127(2) 2024-07-25 and SoI 2024 White Paper on Geodetic Infrastructure), and the surveyor-general's office proposes migration to ITRF2020 + dynamic-epoch coordinates, but neither document is the operator's portal and neither explicitly binds the broadcast NRTK stream's frame. Third-party tutorial (Surveygyaan / mycoordinates.org) describes SoI CORS coordinate output as "WGS-84 or geographical projection" without operator-grade epoch citation. Caster sourcetable mountpoints (RTCM_VRS / RTCM_FKP / RTCM_MAC) do not carry a misc-field datum tag. Working assumption for hobbyists is ITRF2008 ep 2005 (matches GCP framework); a survey-grade user should obtain the operator-portal NRTK Guidelines PDF directly. |

### NRTK notes

- Trimble Pivot back-end, 4 NRTK mountpoints (VRS / MAC / FKP / DGNSS code).
- All NRTK mounts require rover GGA upload to receive RTCM (sourcetable flags nmea=1, solution=1; this is correct, not a misconfig).
- Operator-claimed real-time RTK accuracy: ±3 cm canonical (CORS portal `cors-services.php`, mirrored in `introduction.html`, ISTI Portal entry, PIB press release PRID=1967096). NRTK "3–4 cm" range appears in some operator restatements as the best-practice-real-world figure. DGNSS code-only stream is 30–40 cm (operator).
- ~70 km mean station spacing inside operational hull — adequate for VRS-style cm-accurate fix throughout the covered states.

### Regional integration status

- **Andhra Pradesh (70 stations):** integrated into SoI national network per MoU signed 13 Oct 2025 (Times of India 2025-10-17, SoI X 1979437501711368536, Financial Content / WRAL 2025-10-17). Becomes part of SoI's Region 3. Operational handover status as of 2026-05-23 still ambiguous: no separate AP NTRIP endpoint (Vijayawada/Visakhapatnam) located in operator portal or third-party sources; presumed served via SoI Region 3 once subscription gating is activated. A hobbyist in AP should presently subscribe to SoI rather than seek an AP-state caster.
- **Tamil Nadu:** Tamil Nadu Department of Survey and Settlement operates a state-internal CORS network on government-building rooftops for cadastral resurvey. District-level confirmations exist (Kancheepuram 3 stations, Cuddalore pillars) but no statewide total is publicly published — earlier file claim of "70 stations" was unsubstantiated and the 70-figure in Indian CORS discourse refers specifically to AP. No public NTRIP, no tariff, no MoU with SoI as of 2026-05-23. Portal: https://tnlandsurvey.tn.gov.in. Disqualified — closed.
- **Kerala:** MoU signed with SoI on 18 Jan 2021 for a VRS/NTRIP/NavIC network; hardware deployed and used by DSLR field staff. No public NTRIP endpoint or tariff published. Latest public note: https://dslr.kerala.gov.in/en/2021/05/24/cors-network/ . Disqualified — closed.

### Global / cross-border casters with sparse Indian presence

These are documented in their own files and are not pareto inside India:

- **rtk2go** — 1 volunteer base in IN: `IndiaTN02` at 10.97 N, 78.08 E (central Tamil Nadu, near Tiruchirappalli/Trichy) per local pipeline snapshot 2026-05-23. Single-base, ~10–30 km effective baseline; the only free option for a TN hobbyist near Trichy. See `docs/ntrip_research/Rtk2go.md`.
- **IGS-IP** — 3 IN stations: GDKG (Gadanki, 13.46 N 79.18 E), IISC (Bangalore, 13.02 N 77.57 E), IITK (Kanpur, 26.52 N 80.23 E). Sparse; not field-RTK-usable in general but viable single-base near each site. See `docs/ntrip_research/EUREF-IP.md` and `docs/ntrip_research/IGS-IP.md`.
- **AUSCORS** — rebroadcasts 2 IN IGS stations (GDKG, IISC) as part of its Asia-Pacific feed (confirmed via local pipeline 2026-05-23). Disqualified for primary use in India (same stations as IGS-IP, no added coverage).
- **MIRAI (Japan QZS GNSS Data Sharing)** — no IN stations carried in current sourcetable (local pipeline 2026-05-23 lists MIRAI as LKA-2 only). Disqualified — no Indian coverage.
- **EarthScope / NOTA RTGPS** — no Indian stations in current sourcetable; legacy UNAVCO real-time platform retired 2025-07-29. The 3 IN igs_ip stations remain live independent of NOTA (separate BKG/IGS distribution path). See `docs/ntrip_research/Earthscope.md`.
- **GEODNET via HYFIX India** — paid commercial service, ₹34,000/yr (~$358) yearly single-device per `hyfix.in/products/geodnet-rtk-subscription-yearly` 2026-05-23, free 30-day trial. Coverage density inside India not publicly disclosed by HYFIX/GEODNET (hyfix.in/pages/network and hyfix.ai/pages/network checked 2026-05-23 — global narrative only, no India station count or map). Out of scope (commercial / blockchain-mined network with unverifiable India coverage).
- **RTKdata** — $40/mo commercial reseller bundling third-party networks; coverage map only mentions "20,000+ stations in 140+ countries" without India-specific breakdown. Out of scope (no own India infrastructure).
- **ISRO / NavIC (IRNSS)** — NavIC is a GNSS constellation, not a CORS/NTRIP RTK correction network. SoI CORS receivers track NavIC at the antenna, but the broadcast NRTK RTCM stream observed 2026-05-23 advertises GPS+GLO+GAL+BDS+QZS only (NavIC corrections not exposed in `RTCM_VRS` constellation list). No ISRO-operated NTRIP caster exists.
- **GAGAN (GPS-Aided GEO Augmented Navigation)** — Indian SBAS (satellite-based augmentation), not NTRIP RTK. Sub-metre accuracy via L1 GEO broadcast — out of scope for this project (DGNSS class).

## Sources Consulted (2026-05-23 verification cycle)

- SoI CORS sourcetable probe: `curl --http0.9 http://103.205.244.106:2101/` → SOURCETABLE 200 OK 2026-05-23 (Trimble Pivot 5.3, 4 mountpoints).
- Subscription-charges page (WebSearch snippet of `cors.surveyofindia.gov.in/subscription-charges.html`, 2026-05-23): RTK ₹5,000 + GST/mo unlimited, RTK+10h-RINEX bundle ₹5,032 + GST/mo, 3-mo / 6-mo / annual tiers prorated; DGNSS ₹2,164 + GST/mo; Online GNSS Processing ₹180–3,600 + GST.
- SoI CORS portal `https://cors.surveyofindia.gov.in/cors-services.php` and `introduction.html` (WebSearch-indexed, direct WebFetch ECONNREFUSED from sandbox 2026-05-23): mountpoint formats, ±3 cm accuracy, NRTK 24×7.
- SoI CORS registration page `https://cors.surveyofindia.gov.in/registration.php` (WebSearch-indexed): accepted photo IDs = Voter ID / Driving Licence / Aadhaar / PAN.
- LinkedIn post: SoI offers 3-month free CORS, 1 Nov 2025 – 31 Jan 2026: `https://www.linkedin.com/posts/surveyofindia_surveyofindia-cors-geospatial-activity-7389614969484414977-EyVK` (WebFetched 2026-05-23).
- Geospatial World: "SOI Announces Three Month Free CORS Service for Private Sector": `https://geospatialworld.net/prime/soi-announces-three-month-free-cors-service-for-private-sector/` (2025).
- Andhra Pradesh integration MoU 13 Oct 2025: SoI X status 1979437501711368536; Financial Content / WRAL `https://markets.financialcontent.com/wral/article/tokenring-2025-10-17-andhra-pradesh-forges-geospatial-future-cors-integration-promises-precision-revolution`.
- SoI "Free Subscription of CORS Services" repost 2025-10-30: `https://x.com/india_soi/status/1983899442022367368` (WebFetch 402; WebSearch snippet).
- Datum context (not real-time-service citation): Current Science 127(2) 2024-07-25 (`https://www.currentscience.ac.in/Volumes/127/02/0147.pdf`); SoI 2024 White Paper on Geodetic Infrastructure (`https://surveyofindia.gov.in/UserFiles/files/White_paper_on_Geodetic_Infrastructure_15052024(1).pdf`).
- Tamil Nadu DSS portal: `https://tnlandsurvey.tn.gov.in`. Kerala DSLR CORS: `https://dslr.kerala.gov.in/en/2021/05/24/cors-network/`.
- ArduSimple India dealer cache: `docs/ardusimple/IN_India.md` 2026-05-16 — names only SoI CORS as the national paid service.
- Local pipeline counts via `scripts/stations_by_country.py IND` 2026-05-23: auscors 2, igs_ip 3, rtk2go 1.
- HYFIX India GEODNET reseller: `https://www.hyfix.in/products/geodnet-rtk-subscription-yearly` 2026-05-23 (₹34,000/yr).
- RTKdata commercial: `https://www.rtkdata.com/` 2026-05-23.
