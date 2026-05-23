# Bhutan [BT] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: YES — active government NTRIP caster (DrukNet, NLCS), annual subscription required, hobbyist tier limited (cheapest paid Nu. 10,000/yr ~USD 120)

Bhutan has exactly one operational NTRIP RTK caster: **DrukNet** (NLCS), with 14 active single-base mountpoints spanning the country and a clear public tariff schedule. No free public alternative — there are no rtk2go, Centipede, IGS-IP, EUREF-IP, or AUSCORS stations in Bhutan; local pipeline 2026-05-23 returns zero `BTN` rows in every ingested source.

A casual hobbyist faces an effective floor of Nu. 10,000/yr (~USD 120) for a Basic private subscription; the free educational/research tier requires an institutional supporting document so does not generalise to hobbyists. There is no cross-border free path: India (south/east/west) requires Indian-resident photo ID for SoI CORS, and China-Tibet (north) has no public cross-border NTRIP service.

---

## DrukNet — Bhutan GNSS National Network (NLCS)

| Field | Value |
|---|---|
| operator | National Land Commission Secretariat (NLCS), Royal Government of Bhutan. Caster software MIRACaster, hosted on MIRASpaco (Portugal) infrastructure — `Server: NTRIP MIRACaster MIRASpaco-00001/2.0` on the live sourcetable 2026-05-23. |
| landing_url | https://web.nlcs.gov.bt/cors-facility/ |
| access_url | https://miranet.druknet.net/pre-registration/form |
| access_type | paid |
| coverage | Nationwide Bhutan from 14 physical single-base CORS. Live sourcetable 2026-05-23 station coords span 88.88°E (SIPS) → 92.10°E (JOMO) longitude and 26.82°N (DTNG) → 27.91°N (GASA) latitude — covers all 20 dzongkhags with a maximum within-country baseline ~370 km. Network station spacing varies; in western Bhutan (Thimphu/Paro/Haa/Wangdue) baselines between stations are short enough for cm-grade single-base RTK across the populated zone; in central and eastern dzongkhags (Bumthang, Lhuentse, Trashigang, Mongar) baselines stretch ~40–80 km. Cadastral guideline acceptance is up to 40 km from a CORS base. |
| num_stations | 14 single-base CORS active in live sourcetable 2026-05-23: **THIM** (Thimphu, 27.4801 N, 89.6303 E), **BUMT** (Bumthang, 27.5447 N, 90.7229 E), **KANG** (Kanglung/Trashigang, 27.2869 N, 91.5238 E), **PHUN** (Phuentsholing, 26.8501 N, 89.3949 E), **DTNG** (Dewathang, 26.82 N, 91.46 E), **LHUN** (Lhuentse, 27.5916 N, 91.1941 E), **DGPL** (Dagapela, 26.9336 N, 89.9564 E), **HAAC** (Haa, 27.3880 N, 89.2845 E), **SPGT** (Sarpang/Gelephu, 26.8596 N, 90.2697 E), **WNGD** (Wangdue Phodrang, 27.5167 N, 89.9778 E), **SIPS** (Samtse/Sipsu, 27.0075 N, 88.8836 E), **ZHEM** (Zhemgang, 26.9420 N, 90.8910 E), **GASA** (Gasa, 27.9077 N, 89.7283 E), **JOMO** (easternmost station near Trashigang, 26.8944 N, 92.0995 E). Two stations added since 2024 (GASA, JOMO); two retired (DEOT, GELE — present in 2024 NSDI metadata, not in live 2026-05-23 sourcetable). Network founded 2014 with 6 initial Trimble bases. |
| sourcetable | `103.252.84.100:2101` SOURCETABLE 200 OK 2026-05-23, 1594 bytes (`Server: NTRIP MIRACaster MIRASpaco-00001/2.0`). 14 STR rows, all RTCM 3.3, all `BTN` country tag, carrier=2 (L1+L2), all nmea=0 and solution=0 (single-base physical mountpoints, no rover GGA required). Constellation list per row: `BDS+GAL+GLO+GPS+IRS+QZS+SBAS` (NavIC/IRNSS included). Network field varies across rows: 8 rows tagged `druknet`, 6 rows tagged `Bhutan` (operator-internal labelling, not service-affecting). Hostname `ntrip.druknet.net` returns NXDOMAIN against public DNS resolvers 2026-05-23 — connect by direct IP `103.252.84.100:2101`. Format-details field is sparse on this caster (some rows show "RTCM3.3", "RTCM", or "sbf" placeholder rather than full MSM message lists); rover-side handling per RTCM 3.3 spec recommended. |
| vrs | no — single-base only; 14 physical mountpoints, no VRS/MAC/FKP/iMAX entries in sourcetable. |
| tariff | Per `web.nlcs.gov.bt/cors-facility/` 2026-05-23 (Bhutanese Ngultrum; 1 BTN ≈ 1 INR ≈ 0.012 USD May 2026). **Government agencies (Dzongkhags + 4 Gelyong Thromdes)**: Nu. 10,000/yr lump-sum for unlimited users. **Private/corporate**: Basic Nu. 10,000/yr 1 user; Standard Nu. 17,500/yr 2 users; Premium Nu. 22,500/yr 3 users. **Educational/research**: free, requires official supporting document. **Simultaneous-connection rule** (operator quote verbatim): "Simultaneous connections to the network are not allowed, that is, each subscription can only make one connection to the network at the same time." This unambiguously means **one concurrent connection per subscription regardless of user count** — a Standard 2-user or Premium 3-user tier grants N named credentials sharing a single concurrent slot, not N parallel sessions. Hobbyist-relevant: useful only for organisations rotating between named users, not for multiple simultaneous rovers. Credentials non-transferable; disabled at end of subscription. |
| hobbyist_eligibility | no (effective). No hobbyist-specific tier in tariff schedule; cheapest entry is the Basic private slot at Nu. 10,000/yr (~USD 120). Free educational/research tier requires an institutional supporting document, which a casual hobbyist cannot self-furnish. A surveyor working at a Bhutanese institution can use the educational tier; a tourist or unaffiliated foreigner cannot, and a Bhutanese hobbyist must pay the Basic tier or qualify via an institution. |
| residency_required | no (legally). Pre-registration form at `miranet.druknet.net/pre-registration/form` accepts global submissions (fields: Full Name, Email, Organization optional, Telephone, Preferred Username). De-facto barrier is the NLCS administrative approval step + tariff payment in Bhutanese Ngultrum; foreign hobbyists may need a local intermediary for payment. |
| stations_source | Live sourcetable at `103.252.84.100:2101` (filter for BTN rows); 14 STR rows enumerated above. NSDI portal metadata snapshot revised 2024-05-07 (13 stations at that time): `https://nsdi.systems.gov.bt/portal/sharing/rest/content/items/453406824ec04042b261c114cea594f9/info/metadata/metadata.xml`. Coverage map referenced from NLCS CORS Facility page. |
| datum_epoch | DRUKREF 03 / Bhutan National Geodetic Datum (EPSG datum 1058; geographic 2D CRS EPSG:5262; projected CRS EPSG:5266 DRUKREF 03 / Bhutan National Grid; per-dzongkhag projected CRSs EPSG:5292–5311 for dzongkhag-specific TM zones). GRS 1980 ellipsoid; National-Grid TM uses central meridian 90° E, scale 1.0, false easting 250,000 m, false northing 0. Source authority: Department of Survey and Land Records (DSLR), NLCS Bhutan, with information provided via Lantmäteriet Sweden (Swedish-government technical cooperation on Bhutan's national geodetic infrastructure); EPSG database revision 2010-09-06. **DRUKREF 03 and WGS 84 are both realisations of ITRS** (EPSG:5266 note), with `TOWGS84[0,0,0,0,0,0,0]` and stated 1.0 m accuracy — effectively coincident at the metre level. ITRF realisation year and epoch are not stated on EPSG / operator pages reachable from sandbox 2026-05-23 (DRUKREF "03" naming suggests an establishment around 2003 but not confirmed; EPSG datum 1058 page HTTP 403 from sandbox). Vertical datum: DrukGeoid 2015 per NLCS Cadastral Guideline v1 Dec 2023. |

### Single-base notes

- **MSM-vs-legacy compatibility**: All 14 mountpoints advertise RTCM 3.3 but the live sourcetable shows sparse format-details fields (some rows just `RTCM3.3`/`RTCM`/`sbf`). Rover-side handling per RTCM 3.3 multi-constellation spec is required; u-blox ZED-F9P / Emlid Reach RS2+/RS3 / Trimble survey receivers handle the full message set. Older RTCM 3.0/3.1-only receivers will likely not process all messages.
- **NavIC (IRNSS) broadcast**: All 14 mountpoints advertise `IRS` (IRNSS/NavIC) in the constellation list — unusual breadth for a small national network and suggests Septentrio/Trimble multi-constellation receivers across all 14 stations. Combined with QZSS, this is the broadest constellation coverage of any single-base network in the broader South Asia region documented in this research set.
- **Cadastral acceptance**: NLCS Cadastral Guideline v1 December 2023 accepts RTK baselines up to 40 km from a CORS base for cadastral work.
- **Mountpoint geographic coverage matrix** (14 stations vs 20 dzongkhags):
  - Thimphu metro + Paro Valley: THIM, HAAC (10–30 km baselines, cm-grade fix).
  - South-west border zone (busiest BT-IN crossing at Phuentsholing/Jaigaon), Samtse, Sarpang/Gelephu: PHUN, SIPS, SPGT — PHUN is the densest single-base hub for the south-west.
  - Central north-west (Punakha/Wangdue/Gasa): WNGD, GASA.
  - Central south (Dagana, Tsirang, Zhemgang): DGPL, ZHEM.
  - Central north (Bumthang, Lhuentse): BUMT, LHUN.
  - East (Mongar, Trashigang, Trashiyangtse, Samdrup Jongkhar/Dewathang): KANG, DTNG, JOMO.
  - **Dzongkhags reachable only at the network's accuracy edge** under the 14-station 2026-05-23 layout: Trongsa (mid-country, between BUMT to the east and WNGD to the west, ~50–70 km baselines), Pemagatshel and Trashiyangtse (east-central, ~50–80 km from KANG/JOMO), Tsirang centre (~40–50 km from DGPL and ZHEM). These districts sit outside the cadastral-guideline 40 km hull for nearest stations and would require densification to reach guideline-quality service.
- **MIRASpaco / MiraNet** (Portuguese MIRACaster vendor; `miraspaco.com/gnss/` 2026-05-23: "Installation and rehabilitation of GNSS CORS networks ... Dedicated and flexible solutions to transmit and manage GNSS data for post-processing and RTK"). Vendor's other customer list not publicly enumerated — niche operator with limited web presence. Provides the caster software + the MiraNet web app at `miranet.nlcs.gov.bt` / `www.miranet.druknet.net`. RINEX (daily + hourly) download is included in paid subscription and educational accounts.
- **Recent updates (2025)**: Latest CORS Notification on `web.nlcs.gov.bt/cors-notification/` dated 3 September 2025 (image-only screenshot; text not machine-extractable from sandbox — content presumed to relate to GASA/JOMO additions or DEOT/GELE retirements given network-evolution timing, but not directly verified). NCRP Journal 2025 published May 2025 (PDF binary stream, content not extractable). Two new mountpoints (GASA, JOMO) appear in current sourcetable; not present in 2024 NSDI metadata.
- **DNS / direct-IP-only operability caveat**: `ntrip.druknet.net` returns NXDOMAIN against public resolvers 2026-05-23 — the caster is reachable only by direct IP `103.252.84.100:2101`. Rovers must be configured by IP, not hostname; signals minimal DNS/TLS migration headroom for the operator. Long-term subscribers should expect to update by IP if NLCS migrates infrastructure.
- **NLCS contact**: Jamphel Gyeltshen, Sr. Surveyor, Topographic Division — Phone +975 02-331447 (per CORS Facility page 2026-05-23).

---

## Cross-border reachability

Bhutan borders India (south/east/west — Sikkim, West Bengal, Assam, Arunachal Pradesh) and China-Tibet (north).

- **India SoI CORS** — Region 1 covers Assam and Arunachal Pradesh; Region 2 covers West Bengal and Sikkim. A hobbyist near the Bhutan-India border could in principle pick up SoI VRS within ~10–30 km of the line. Concrete proximity examples: Haa / Samtse (BT west) → Sikkim Region-2 stations (Gangtok area, ~30–60 km from western BT edge); Phuentsholing/Jaigaon (BT south-west) → West Bengal Region-2; Samdrup Jongkhar/Mela Bazar (BT south-east) → Assam Region-1. SoI requires an Indian-resident photo ID (Voter ID / DL / Aadhaar / PAN), blocking Bhutanese nationals regardless of geographic proximity. See `docs/ntrip_research/IN_India.md`.
- **China-Tibet** — Qianxun Spatial Intelligence (BeiDou-augmentation operator covering China including TAR) does not publish cross-border service into Bhutan (checked: Qianxun coverage map 2026-05-23 references China-only deployment; no Bhutanese reseller located; the BT-TAR northern border (Gasa, Lunana) is a closed military frontier, ruling out practical cross-frontier mobile-data roaming or service access even if Qianxun's TAR-adjacent coverage were nominally usable).
- **For foreign hobbyists visiting Bhutan**: tourism is governed by the Sustainable Development Fee (SDF, USD 100–200/day depending on season and origin); against that daily cost, the DrukNet Basic subscription (Nu. 10,000/yr ≈ USD 120) is negligible. Foreign researchers with a Bhutanese institutional sponsorship letter may qualify for the educational tier; tourists without institutional affiliation must pay the Basic tier.
- **Conclusion: no realistic cross-border free RTK path for a Bhutan-resident hobbyist; foreign visitors should budget the Basic tier as part of the broader visit cost.**

---

## Disqualified / context (covered in own files)

- **rtk2go** — 0 BT-tagged mountpoints (local pipeline 2026-05-23 confirms; live rtk2go sourcetable has no BTN rows). See `docs/ntrip_research/Rtk2go.md`.
- **Centipede-RTK** — 0 BT-tagged mountpoints (local pipeline 2026-05-23). See `docs/ntrip_research/Centipede.md`.
- **IGS-IP** — 0 BT stations in `data/igs_ip.sourcetable` 2026-05-23. No IGS RTS station inside Bhutan; closest IGS RT stations are KIT3 (Kitab, Uzbekistan, far west) and SGOC (Colombo, far south). See `docs/ntrip_research/IGS-IP.md`.
- **EUREF-IP** — no BT stations (regional scope is Europe). See `docs/ntrip_research/EUREF-IP.md`.
- **EarthScope / NOTA RTGPS** — no BT stations (Americas-region scope; legacy UNAVCO real-time platform retired 2025-07-29). See `docs/ntrip_research/Earthscope.md`.
- **AUSCORS** — no BT stations rebroadcast (local pipeline 2026-05-23 lists 2 IN + 1 LKA from the Asia feed; no BTN row).
- **MIRAI** — no BT stations (local pipeline 2026-05-23 lists LKA-2 only).
- **GEODNET / HYFIX / ONOCOY / PointOne / RTKdata / TopNET Live** — no Bhutan-specific coverage publicly disclosed in any of these networks' station maps 2026-05-23 (checked station maps + dealer directories).
- **ArduSimple Bhutan page** — does not exist (`ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bhutan/` — not in country list 2026-05-23).

## Sources Consulted (2026-05-23)

- DrukNet live sourcetable probe: `curl --http0.9 http://103.252.84.100:2101/` 2026-05-23 → SOURCETABLE 200 OK, 14 STR rows, `Server: NTRIP MIRACaster MIRASpaco-00001/2.0`.
- NLCS CORS Facility page: `https://web.nlcs.gov.bt/cors-facility/` (WebFetch 2026-05-23 — tariff schedule, simultaneous-connection rule, contact details).
- NLCS CORS Notification page: `https://web.nlcs.gov.bt/cors-notification/` — latest entry 3 September 2025 (image-only screenshot).
- DrukNet MiraNet portal: `https://miranet.nlcs.gov.bt/`.
- MiraNet pre-registration form: `https://miranet.druknet.net/pre-registration/form`.
- Bhutan NSDI CORS metadata (13 stations, revised Aug 2024): `https://nsdi.systems.gov.bt/portal/sharing/rest/content/items/453406824ec04042b261c114cea594f9/info/metadata/metadata.xml`.
- NLCS GNSS-RTK Cadastral Guideline v1 December 2023: `https://web.nlcs.gov.bt/wp-content/uploads/2023/12/Guideline-for-using-GNSS-RTK-in-Cadastral_Surveyingv1.pdf` (PDF binary stream from sandbox 2026-05-23; vertical datum DrukGeoid 2015 confirmed in earlier extraction).
- NLCS Manual for DRUK CORSNet Data Sharing v1 August 2021: `https://www.nlcs.gov.bt/wp-content/uploads/2022/07/Manual_for_DRUK_CORSNet_Data_Sharing_v1.pdf` (PDF binary stream from sandbox 2026-05-23).
- NLCS NCRP Journal 2025: `https://web.nlcs.gov.bt/wp-content/uploads/2025/05/NCRP_JOURNAL_2025.pdf`.
- NLCS Land Services Guideline 2026: `https://web.nlcs.gov.bt/wp-content/uploads/2026/02/Guideline-for-Land-Services.pdf`.
- DRUKREF 03 / Bhutan National Grid EPSG:5266: `https://epsg.io/5266` (GRS 1980, TM 90 E, ITRS realisation aligned with WGS 84).
- Bhutan National Geodetic Datum EPSG datum 1058: `https://epsg.org/datum_1058/Bhutan-National-Geodetic-Datum.html` (HTTP 403 from sandbox 2026-05-23; metadata via WebSearch snippets — source authority DSLR/NLCS via Lantmäteriet Sweden).
- georepository DRUKREF 03 entry: `https://georepository.com/crs_5262/DRUKREF-03.html` (cert error from sandbox 2026-05-23).
- MIRASpaco GNSS page: `https://miraspaco.com/gnss/` (caster vendor).
- NLCS Twitter @nlcsbhutan: `https://twitter.com/nlcsbhutan` (operator social channel).
- Local pipeline counts via `scripts/stations_by_country.py BTN` 2026-05-23: 0 stations across all ingested sources (DrukNet caster is not in the project pipeline as of this research).
