# Nepal [NP] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: NO national public NTRIP RTK caster — EarthScope streams one Nepal CORS (KUGE, near Kathmandu) over its global caster, only realistically reachable real-time path

No Nepali agency operates a publicly documented NTRIP endpoint as of 2026-05-23. Two paths exist for a hobbyist physically located in Nepal:

1. **EarthScope NOTA / `KUGE_RTCM3P3`** — single Trimble NetR9 base near Kathmandu (27.62 N, 85.54 E) streamed via `ntrip.earthscope.org:2101` (legacy `rtgpsout.unavco.org:2101` retired 2025-07-29). Free for non-commercial use after NULA registration. The only realistically reachable real-time stream inside Nepal as of 2026-05-23. Useful within ~10–30 km of Kathmandu/Bhaktapur; single-base, NOT VRS.
2. **Self-hosted base** — for any work outside ~30 km of Kathmandu, the practical hobbyist path is to deploy a local base and a rover, or use satellite-based PPP (Trimble RTX commercial; Galileo HAS free, ~20–40 cm).

Nepal's Survey Department / Geodetic Survey Division operates 2 government CORS at Nagarkot and an additional reference station at the Minbhawan head-office complex, with ambition for 50+ stations covering the country — no public NTRIP endpoint has been advertised under this work as of 2026-05-23.

---

## EarthScope NOTA — `KUGE_RTCM3P3` (Kathmandu)

| Field | Value |
|---|---|
| operator | EarthScope Consortium (Geodetic Facility for the Advancement of Geoscience — GAGE; ex-UNAVCO) under NSF funding; base hardware deployed in cooperation with Tribhuvan University and Nepal Department of Mines and Geology (DMG) per UNAVCO/EarthScope Nepal-station provenance. |
| landing_url | https://www.earthscope.org/data/gnss-data/real-time/ |
| access_url | https://www.earthscope.org/data/ |
| access_type | free-signup (non-commercial NULA = unlimited seats free; commercial = USD 1,000/seat/yr; 2-week 5-seat trial available once per account — `earthscope.org/data/gnss-realtime/` 2026-05-23. See global EarthScope entry) |
| coverage | Single base at 27.62 N, 85.54 E. Coords land ~30 km east-southeast of central Kathmandu (~27.71 N, 85.32 E), in the Dhulikhel / Banepa area of Kavre district — Kathmandu University main campus is in Dhulikhel, making "KUGE" plausibly an abbreviation referencing Kathmandu University (siting matches; EarthScope station-log PDF not directly extractable from sandbox 2026-05-23 to confirm verbatim expansion). Single-base RTK effective ~10–30 km; covers eastern Kathmandu Valley (Bhaktapur, Banepa, Panauti, Dhulikhel) and reaches central Kathmandu / Patan / Lalitpur at the edge of useful baseline. Pokhara (~200 km west), Janakpur, Biratnagar all far outside single-base range. |
| num_stations | 1 (only the KUGE base is real-time-streamed; ~15 other UNAVCO/DMG Nepal CORS — JMLA, NPGJ, JMSM, BESI, CHLM, NAST, SYBC, SNDL, RMJT, BRNZ + newer DLPA, DNSG, HETA, CHWN, KLCK — archive-only or sporadic per the Nepal GNSS Array literature, not in the real-time NTRIP feed). |
| sourcetable | `ntrip.earthscope.org:2101` SOURCETABLE 200 OK 2026-05-23 — single NPL row: `STR;KUGE_RTCM3P3;KUGE_RTCM3P3;RTCM 3.3;1005(60),1007(60),1013(1),1029(60),1033(60),1077(1),1087(1),1097(1),1107(1),1117(1);2;GPS+GLO+BDS+GAL+SBAS+QZS;EARTHSCOPE;NPL;27.62;85.54;0;0;TRIMBLE NETR9;None;N;Y;0;SEAT_REQUIRED;` — RTCM 3.3 MSM7 GPS+GLO+BDS+GAL+SBAS+QZS, nmea=0, solution=0 (single-base), Trimble NetR9 back-end, `SEAT_REQUIRED` misc-field flags the NULA seat gate. |
| vrs | no — single-base RTCM 3.3 stream from one Trimble NetR9 receiver. |
| hobbyist_eligibility | yes — non-commercial NULA-signup users; no surveying-licence gate. |
| residency_required | no — open globally with NULA. |
| stations_source | EarthScope NOTA station map https://www.earthscope.org/data/gnss-data/ and live sourcetable at `ntrip.earthscope.org:2101` (filter for NPL rows). Local pipeline cache via `scripts/stations_by_country.py NPL` 2026-05-23 confirms the single KUGE entry. |
| datum_epoch | ITRF (operator's global frame; specific realisation and epoch shift over time as EarthScope refreshes station coordinates; see `docs/ntrip_research/Earthscope.md` for EarthScope-global datum policy). Not declared in sourcetable misc field; EarthScope publishes per-station coordinates in current ITRF realisation with periodic refresh. For Nepal specifically, the local Nepal-Everest 1984 national datum has been distorted by the April 2015 Gorkha earthquake (Mw 7.8) — coordinates near Kathmandu shifted up to ~2 m co-seismically. Nepal's Survey Department is planning a semi-dynamic national datum based on ITRF2014 with reference epoch post-quake-sequence and a National Deformation Model (Coordinates magazine / NepJOL geodetic-modernisation literature 2020-2024). KUGE's broadcast coords on the EarthScope caster reflect EarthScope's ITRF realisation at refresh; hobbyists requiring Nepali-cadastral-compatible coordinates need post-processing transformation. |

### Single-base notes

- KUGE is a Trimble NetR9 receiver; rover-side hardware should support RTCM 3.3 MSM7 multi-constellation. u-blox ZED-F9P (popular hobbyist receiver) handles RTCM 3.3 MSM4/MSM7. Emlid Reach RS2+/RS3 and Trimble survey receivers handle the full message set. Older RTCM 3.0/3.1-only receivers will not process MSM4/MSM7 families.
- EarthScope seat model (per `earthscope.org/data/gnss-realtime/` 2026-05-23):
  - **Trial license**: 5 seats × 2 weeks, once per account, lowest-friction onboarding path for a Nepali hobbyist who wants to test KUGE before applying for NULA.
  - **Non-commercial (NULA)**: unlimited seats, free; requires NULA application acceptance.
  - **Commercial**: USD 1,000 per seat per year.
  - A seat = one concurrent connection to a data stream; users can switch streams freely without exceeding the seat count.
- `SEAT_REQUIRED` misc-field on the sourcetable confirms the seat-gate; mountpoint name `KUGE_RTCM3P3` follows the standard `PNUM_RTCM3P3` naming for raw RTCM 3.3 streams on port 2101.
- Register at `https://www.earthscope.org/user/licenses` (NULA / commercial / trial all managed there).
- Cadastral-coord transformation workflow for Nepal: KUGE's broadcast coords are in EarthScope's current ITRF realisation; for cadastral-survey-compatible output a hobbyist needs either (a) DoS-published Helmert / 14-parameter transformation to Nepal-Everest 1984, (b) post-processing in a GIS that supports ITRF→Nepal-Everest, or (c) wait for the planned ITRF2014-based semi-dynamic national datum + NDM rollout. No public DoS online transformation tool located 2026-05-23 (analogous to NZ PositioNZ-PP or AU AUSPOS not yet operational in Nepal).
- Satellite-PPP fallback for outside-KUGE areas: Galileo HAS free ~20–40 cm convergence; Trimble RTX commercial. Both subject to multipath/sky-obstruction degradation in Himalayan terrain (canopy in mid-hills, deep valleys in mountain regions) — convergence times degrade significantly compared to clear-sky Terai/Kathmandu Valley operation.
- Mobile-data coverage caveat: NTRIP requires IP path; Nepal's 4G coverage is solid in Kathmandu Valley and major Terai/Hill highway corridors but patchy in mid-hills + mountain districts. For Pokhara-area or Karnali-Sudurpashchim hobbyists the binding constraint may be mobile-data availability rather than baseline distance.

---

## Cross-border reachability + national-network status

Nepal borders India (south/east/west) and China-Tibet (north). The Indian SoI CORS Region 1 covers Bihar (south of Nepal's Madhesh Province), Uttar Pradesh (south of Lumbini/Sudurpashchim), and Uttarakhand (west of Sudurpashchim) — in principle a hobbyist within ~30 km of the Indo-Nepal border could pick up Region-1 VRS near the line. But SoI CORS requires an Indian-resident photo ID (Voter ID / DL / Aadhaar / PAN) for registration — practically inaccessible to a Nepali national. Tibet/China has no publicly accessible NTRIP RTK service for cross-border use. **Conclusion: no realistic cross-border free RTK path for an NP-resident hobbyist.** See `docs/ntrip_research/IN_India.md`.

### Nepal national CORS plans (informational; not currently providing public NTRIP)

- **Survey Department / Department of Survey (DoS / नापी विभाग, `dos.gov.np`)** under the Ministry of Land Management, Cooperatives and Poverty Alleviation. Headquarters at Minbhawan, Kathmandu. Director General Prakash Joshi (Wikipedia, 2025). Geodetic Survey Branch maintains 2 operational CORS at Nagarkot plus a base at the Minbhawan complex (visible in the operator's home-page carousel 2026-05-23 as "CORS station in the Survey Department Premise"). Operator's stated ambition: 50+ CORS stations nationwide.
- **National datum modernisation** (Coordinates magazine "Towards a modernized geodetic datum for Nepal"; NepJOL Journal on Geoinformatics 2080 BS / 2023 AD; ResearchGate "Developing New National Geodetic Reference Frame of Nepal"): existing Nepal-Everest 1984 datum is distorted by India-Eurasia plate convergence + 2015 Gorkha earthquake (Mw 7.8) co-seismic displacement (~2 m near Kathmandu) + Mw 7.3 May 2015 aftershock. Proposed replacement: semi-dynamic datum on ITRF2014 with reference epoch post-quake-sequence, National Deformation Model (NDM) for crustal velocities + co-seismic offsets. 20 stations from the Nepal GPS Array could function as CORS, though 4 sites have data-link issues. Survey Department recommendation to develop Network-RTK + online-processing services analogous to PositioNZ-PP / AUSPOS — not yet operational.
- **JICA Nepal cooperation:** JICA has an active country office in Nepal but no published JICA-funded CORS densification project for Nepal located 2026-05-23 (a JICA "Annex 1. Proposed Specifications of CORS equipment" PDF — `openjicareport.jica.go.jp/pdf/12340881_02.pdf` — exists but the parent project's scope and country could not be conclusively pinned to Nepal from accessible sources; Bangladesh's similar JICA CORS densification is well-documented but unrelated). JICA-JAXA partnership (10-year MoU 2024) discusses CORS utilisation in developing countries generally.
- **Department of Mines and Geology (DMG, `dmgnepal.gov.np`)** — co-operator of the Nepal CORS network with UNAVCO/EarthScope; primary mission is seismology and geological monitoring, not survey-grade RTK corrections.
- **National Geoportal Nepal (`nationalgeoportal.gov.np`)** under the Geographic Information Infrastructure Division — geospatial data portal, not an NTRIP service.
- **Nepal NGIIP (National Geographic Information Infrastructure Programme)** is the policy umbrella; no NTRIP service rollout published.

---

## Disqualified / context (covered in own files)

- **rtk2go** — 0 NP-tagged mountpoints (local pipeline 2026-05-23; live rtk2go sourcetable has no NPL rows). See `docs/ntrip_research/Rtk2go.md`.
- **Centipede-RTK** — 0 NP-tagged mountpoints (local pipeline 2026-05-23). See `docs/ntrip_research/Centipede.md`.
- **IGS-IP** — 0 NP stations in `data/igs_ip.sourcetable` 2026-05-23. (The Nepal GPS Array scientific stations are archive-only / not in the real-time IGS-IP feed; KUGE is broadcast via EarthScope, not via igs-ip.net.) See `docs/ntrip_research/IGS-IP.md`.
- **EUREF-IP** — no NP stations (regional scope is Europe). See `docs/ntrip_research/EUREF-IP.md`.
- **AUSCORS** — no NP stations rebroadcast (local pipeline 2026-05-23 lists 2 IN + 1 LKA from the Asia feed; no NPL row).
- **MIRAI** — no NP stations (local pipeline 2026-05-23 lists LKA-2 only).
- **GEODNET / HYFIX / ONOCOY / PointOne / RTKdata / TopNET Live** — no Nepal-specific coverage publicly disclosed in any of these networks' station maps 2026-05-23 (checked station maps + dealer directories).
- **ArduSimple Nepal page** — does not exist (`ardusimple.com/rtk-correction-services-and-ntrip-casters-in-nepal/` → HTTP 404 2026-05-23). Nepal absent from the ArduSimple country list.
- **China / Tibet cross-border** — Qianxun Spatial Intelligence (the BeiDou-augmentation operator covering China including Tibet Autonomous Region) does not publish cross-border service into Nepal (checked: Qianxun coverage map references China-only deployment 2026-05-23; no Nepalese reseller located). Practically also constrained by border-zone restrictions on cross-frontier mobile-data roaming. Disqualified — no cross-border RTK path from the north.
- **Nepali commercial RTK / private CORS deployments** — no commercial NTRIP caster located in Nepal as of 2026-05-23 (no SoB-analogue paid service, no CORSnet-LK-analogue islandwide private network, no announced Trimble/Topcon/Leica reseller-hosted CORS in Kathmandu or Pokhara). Drone-mapping firms and survey companies in Kathmandu likely run private bases for their own jobs but none expose a public NTRIP endpoint that surfaced in search 2026-05-23. The operational void for hobbyists outside Kathmandu Valley (Pokhara, Chitwan, Janakpur, Biratnagar, Butwal, Nepalgunj, Dhangadhi, Birgunj) is the headline finding.
- **EarthScope post-UNAVCO continuity:** EarthScope's `ntrip.earthscope.org` platform is the migration target from the retired `rtgpsout.unavco.org` (retired 2025-07-29). KUGE streaming has continuity on the new platform — confirmed alive 2026-05-23 sourcetable probe.

## Sources Consulted (2026-05-23)

- EarthScope NOTA sourcetable live probe: `curl --http0.9 http://ntrip.earthscope.org:2101/` 2026-05-23 → confirms single NPL row `KUGE_RTCM3P3` at 27.62 N, 85.54 E, RTCM 3.3 MSM7, Trimble NetR9, SEAT_REQUIRED.
- EarthScope GNSS real-time: `https://www.earthscope.org/data/gnss-data/real-time/`.
- EarthScope data portal: `https://www.earthscope.org/data/`.
- Department of Survey Nepal homepage: `https://dos.gov.np/` (English/Nepali) — carousel mentions "CORS station in the Survey Department Premise" 2026-05-23.
- Wikipedia "Survey Department (Nepal)": `https://en.wikipedia.org/wiki/Survey_Department_(Nepal)` — DG Prakash Joshi; FY 2081/82 budget NRS 2.924 B; Minbhawan HQ.
- Department of Mines and Geology Nepal: `https://dmgnepal.gov.np/en` and `https://www.dmgnepal.gov.np/en/divisions/geological-mapping-section-6959`.
- National Geoportal Nepal: `https://nationalgeoportal.gov.np/`.
- Shanker KC blog "GNSS activities on Nepal" 2019-09-01: `https://shankerkcblog.wordpress.com/2019/09/01/gnss-activities-on-nepal/` — confirms 11 existing CORS (JMLA, NPGJ, JMSM, BESI, CHLM, NAST, SYBC, SNDL, RMJT, BRNZ) + 5 new (DLPA, DNSG, HETA, CHWN, KLCK) + 2 DoS at Nagarkot + plan for 50+.
- mycoordinates.org "Towards a modernized geodetic datum for Nepal": `https://mycoordinates.org/towards-a-modernized-geodetic-datum-for-nepal/` — ITRF2014 semi-dynamic plan, ~2 m Gorkha co-seismic distortion near Kathmandu.
- MDPI Remote Sensing "Advancements of Geodetic Activities in Nepal" 2022 (Tan et al.): `https://www.mdpi.com/2072-4292/14/7/1586` (WebFetch HTTP 403 2026-05-23; cited via search snippet).
- ResearchGate "Developing New National Geodetic Reference Frame of Nepal": `https://www.researchgate.net/publication/392211781_Developing_New_National_Geodetic_Reference_Frame_of_Nepal`.
- NepJOL Journal on Geoinformatics 2080 BS / 2023 AD: `https://giwmscdnone.gov.np/media/pdf_upload/sd%20journal%202080_z1u70s7.pdf` (3 MB PDF; binary stream not extractable via WebFetch 2026-05-23).
- NepJOL "GNSS Practice in Survey Department": `https://www.nepjol.info/index.php/NJG/article/view/23009`.
- FIG paper "The Fundamental Role of GNSS in Modern Surveying" (Nepal): `https://www.fig.net/resources/proceedings/fig_proceedings/nepal/papers/ts03b/TS03B_upadhyaya_gyawali_et_al_12890.pdf`.
- mycoordinates.org "UN/Nepal Workshop on GNSS" 2016: `https://mycoordinates.org/united-nationsnepal-workshop-on-the-applications-of-gnss/`.
- Geospatial World "Surveying Mount Everest using GNSS and CORS" 2020: `https://geospatialworld.net/article/surveying-mount-everest-using-gnss-and-cors/` (re-measurement of Everest height with national resources).
- JICA Nepal office: `https://www.jica.go.jp/nepal/english/index.html`.
- JICA "CORS utilization in developing countries" 2020-11-05: `https://www.jica.go.jp/english/news/field/2020/20201105_01.html`.
- ArduSimple Nepal page: HTTP 404 2026-05-23 (`https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-nepal/`).
- Local pipeline counts via `scripts/stations_by_country.py NPL` 2026-05-23: earthscope = 1 (KUGE_RTCM3P3); auscors / centipede / igs_ip / euref_ip / mirai / rtk2go = 0.
