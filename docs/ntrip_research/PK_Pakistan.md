# Pakistan [PK] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: NO national public NTRIP RTK caster — SUPARCO's Pak-Rehber NRTK exists but is restricted to authorised users in Karachi only; a single rtk2go community base in Karachi is the only public free option

No publicly accessible government NTRIP RTK service is available to a Pakistani hobbyist nationwide. The two paths that exist:

1. **Pak-Rehber (SUPARCO Business Solutions)** — operational NRTK in Karachi metro, authorised-users-only, no published tariff or self-service registration. Disqualified for hobbyist use (restricted).
2. **rtk2go `Stingray_tech`** — single volunteer base in Karachi (operator: Stingray Technologies, a Karachi defence-tech firm), the only free real-time option, useful within ~30 km of central Karachi.

Survey of Pakistan (SoP) — the national mapping organisation — has procured 31 new GNSS monuments (bid open 17 Dec 2024; construction window ~6–8 months per tender snippet; actual completion timeline unconfirmed as of 2026-05-23 — sop.gov.pk + surveyofpakistan.gov.pk ECONNREFUSED) for the National Geodetic Datum infrastructure under the Surveying and Mapping Act 2014; the tender is for static benchmark monuments, not a real-time CORS/NTRIP service, and no public NTRIP caster has been announced under this work. Outside Karachi the practical hobbyist path is a self-hosted base station or satellite-based PPP.

**Legal note (Surveying and Mapping Act 2014, as amended):** the Act establishes the Surveyor-General as the licensing authority for "geospatial data collection, surveying, and mapping activities," and Section 20 criminalises printing, displaying, disseminating, using, or circulating "incorrect and unofficial versions of the map of Pakistan" with up to 5 years' imprisonment and/or PKR 5 million fine (per The News reporting on amendments; full text at na.gov.pk). The Act's text does not explicitly name private NTRIP/CORS/RTK base operation, but hobbyists self-hosting a base in Pakistan should be aware: the licensing regime is the legal context, even if real-time correction streams are not specifically called out. No enforcement against private NTRIP operators publicly reported.

---

## Pak-Rehber Precise Positioning Service — SUPARCO Business Solutions

| Field | Value |
|---|---|
| operator | SUPARCO Business Solutions (Pvt.) Ltd. — commercial arm of SUPARCO (Pakistan Space and Upper Atmosphere Research Commission, Federal Ministry of Defence) |
| landing_url | https://suparco.gov.pk/precise-positioning-service/ |
| access_url | https://suparco.biz/satcom-navigational-solutions/ |
| access_type | restricted |
| coverage | Karachi metropolitan area + ~20 km outskirts only (per Pak-Rehber brochure 2025); SUPARCO COPUOS 2024/2025 statements describe the GBAS service as "Proof of Concept" with the option to extend to "any region of interest across Pakistan on requirement basis subject to availability of GSM/3G/4G data communication services" — not deployed elsewhere as of 2026-05-23. |
| num_stations | unknown — operator does not publish a station list. Coverage description ("Karachi metro + 20 km") implies a small NRTK network (single-digit physical bases likely). |
| hobbyist_eligibility | no — operator explicitly limits use: "Only authorized users can use the Pak-Rehber precise positioning service" (Pak-Rehber brochure 2025-03). Authorisation process and tariff not publicly documented; SUPARCO COPUOS 2025 statement repeats "authorized users" wording. |

### Restricted-caster prose

SUPARCO's satellite-navigation programme has three branded components, which the operator's own portals (`suparco.gov.pk` vs `suparco.biz`) describe somewhat inconsistently:

- **Pak-Rehber** — the GNSS RTK / NRTK precision-positioning service ("Pak-Rehber Precise Positioning Service provides positioning data through GNSS Real-Time Kinematic (RTK) network; centimeter-level accuracy is available with unmatched reliability" — `suparco.gov.pk/precise-positioning-service/`).
- **Pak-GBAS** — operator-labelled "Ground Based Augmentation System" but in fact branded over the same NRTK platform that powers Pak-Rehber: "Pak-GBAS utilizing Network Real-Time Kinematic (NRTK) technology to enable real-time cm-level positioning through provision of correction signals to authorized users in Karachi" (`suparco.biz/satcom-navigational-solutions/`; COPUOS STSC 2024 + 2025 statements). This conflicts with the ICAO/EUROCONTROL definition of GBAS (VHF-broadcast LAAS-style precision-approach service for aviation). SUPARCO's use of "GBAS" is a brand label for its ground-augmentation programme of which the NRTK service is the operational arm; the two names refer to the same underlying Karachi NRTK network. PCAA (Civil Aviation Authority) is a collaborating partner per Wikipedia / SUPARCO sources, so a future ICAO-conformant Pak-GBAS for aviation may emerge.
- **Pak-SBAS** — L-band satellite-broadcast SBAS, launched/demonstrated at the Cholistan Rally 2026-02-15. Spec 2.5 m → 15 cm positioning accuracy via GPS+BDS correction signals "inside & outside Pakistan" (COPUOS STSC 2025). SBAS class, out of scope for this project.

The 2025-03 Pak-Rehber brochure on `suparco.biz` (HTTP 403 from sandbox 2026-05-23; quote sourced from prior 2026-04-30 fetch retained in this research lineage) describes the Karachi-metro footprint and the authorised-users-only gate explicitly: "Only authorized users can use the Pak-Rehber precise positioning service." The "+20 km outskirts" extent is brochure-derived; the broader "Karachi only" footprint is independently confirmed by multiple SUPARCO portal pages and COPUOS statements. No public host:port, sourcetable URL, mountpoint name, datum, tariff, or self-service registration form has been located after targeted search 2026-05-23 — access is via SUPARCO institutional channels (the Karachi office number 021 34690765-79 on `suparco.gov.pk/contact-us/` 2026-05-23 is SUPARCO's general line, not a Pak-Rehber subscription desk). One IEEE conference paper (Sirajuddin et al., doc 11004397, 2024) reports using Pak-Rehber for an academic localisation experiment via authorised SUPARCO access — the paper does not document the subscription mechanism.

**Underlying hardware lineage:** UniStrong Science and Technology Co. (Beijing) commissioned a 5-base BeiDou-enabled CORS network with a central processing centre in Karachi on 21 May 2014 in cooperation with SUPARCO (China Daily 2014-05-23; Chinese Satellite Navigation Office MoU referenced in later coverage). Reported then as "2 cm real-time, 5 mm post-processed." Whether the present-day Pak-Rehber service is the operational continuation of this UniStrong-built network is not stated in operator portals; the timing, location, accuracy, and Karachi-only footprint align. Treated as plausible same-asset continuity, not operator-confirmed.

---

## rtk2go — `Stingray_tech` (Karachi)

| Field | Value |
|---|---|
| operator | Stingray Technologies (Pvt.) Ltd. (stingray.com.pk) — Karachi-based defence-tech firm |
| landing_url | http://rtk2go.com/ |
| access_url | http://rtk2go.com/how-to-connect/ |
| access_type | free |
| coverage | single base at 24.89 N, 67.09 E (Karachi). Single-base RTK effective ~10–30 km; degrades with baseline. Useful only for users inside Karachi metro. |
| num_stations | 1 |
| sourcetable | `rtk2go.com:2101` SOURCETABLE 200 OK 2026-05-23 (SNIP simpleNTRIP_Caster_[wPRO]R3.19.22 of Mar 12 2026). Mountpoint row: `STR;Stingray_tech;Karachi;RTCM 3.2;1005(1), 1033(10), 1074(1), 1084(1), 1094(1), 1124(1);;;SNIP;PAK;24.89;67.09;1;0;SNIP;none;B;N;6540;` — carrier blank (rtk2go convention; physical-mount override in fetch_stations.py), RTCM 3.2 MSM4-class observations GPS+GLO+GAL+BDS (no NavIC, no QZSS), nmea=1 (rtk2go misconfig — single-base, no GGA required), solution=0, ~6.5 kB/s. Only PK row in the rtk2go sourcetable. |
| vrs | no — single-base RTCM 3.2 stream, no NRTK |
| tariff | omit |
| hobbyist_eligibility | yes — open community caster. rtk2go terms apply: register with name/email, reservation message required, no payment. |
| residency_required | no |
| stations_source | rtk2go sourcetable: `curl --http0.9 http://rtk2go.com:2101/` (filter for PAK rows). Also visible at http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101 and in the local pipeline via `scripts/stations_by_country.py PAK` (1 station, lat 24.89, lon 67.09 — 2026-05-23). |
| datum_epoch | omitted — no operator declaration. rtk2go bases are operator-self-installed; rtk2go provides no central QC and does not enforce a datum/epoch. Per the project primer "no operator declaration -> omit"; working assumption for an autonomous-survey-in TMODE3 base is WGS84 with metre-level absolute drift (relative-positioning still 1–3 cm). |

---

## Cross-border reachability (for users near a frontier)

Pakistan borders India (east), China (NE), Iran (west), and Afghanistan (NW). The only neighbouring country with a usable cm-accurate NTRIP network within plausible single-base range of a Pakistani frontier is India (SoI CORS Region 1). A hobbyist within ~10–30 km of the Wagah/Attari border crossing could in principle receive a Region-1 SoI VRS fix near the line, but SoI CORS requires an Indian-resident photo ID (Voter ID / Driving Licence / Aadhaar / PAN) for registration — practically inaccessible to a Pakistani national. China's BeiDou augmentation services (Qianxun) are not advertised for cross-border use into Pakistan. Iran and Afghanistan have no publicly accessible RTK networks. **Conclusion: no realistic cross-border RTK path for a Pakistan-resident hobbyist.** See `docs/ntrip_research/IN_India.md`.

## Disqualified / context (covered in own files)

- **Centipede-RTK** — no PK-tagged mountpoints (local pipeline 2026-05-23). Centipede is a recipe-only frame in the "Rest of World" zone; no Pakistani volunteer bases. See `docs/ntrip_research/Centipede.md`.
- **EarthScope / NOTA** — no PK stations (local pipeline 2026-05-23). Legacy UNAVCO real-time platform retired 2025-07-29. See `docs/ntrip_research/Earthscope.md`.
- **IGS-IP** — no PK stations in `data/igs_ip.sourcetable` 2026-05-23. The "KARR" mountpoint in IGS-IP is `KARR00AUS0` — Harding River Dam, Western Australia (-20.98 S, 117.10 E), not Karachi. (Previous research erroneously claimed KARR = Karachi.) Closest active IGS real-time station to Pakistan: `KIT3` (Kitab, Uzbekistan). No PK-located IGS RTS station found. Historic Pakistan-based RINEX-contributing stations (PINSTECH / NUST / SUPARCO research receivers) not located in UNAVCO/IGS public archive listings (checked 2026-05-23; absence of in-list PK entries is the negative-evidence, full archive walk not attempted). See `docs/ntrip_research/IGS-IP.md`.
- **EUREF-IP** — no PK stations (regional scope is Europe). See `docs/ntrip_research/EUREF-IP.md`.
- **AUSCORS** — no PK stations rebroadcast (local pipeline 2026-05-23 lists 2 IN + 1 LKA from the Asia feed).
- **MIRAI** — no PK stations (local pipeline 2026-05-23 lists LKA-2 only).
- **GEODNET / HYFIX / ONOCOY / PointOne / RTKdata / TopNET Live** — no Pakistan-specific coverage publicly disclosed (checked station maps + dealer directories 2026-05-23: hyfix.ai/pages/network, geodnet.com map, rtkdata.com network, pointonenav.com, topconpositioning.com TopNET Live coverage tool, onocoy.com map — Pakistan absent from all station footprints; some advertise "global" coverage but provide no in-country physical bases). Local vendor dealers Nedo Corporation (Topcon distributor PK) and similar resellers run demo gear but do not advertise public NTRIP services.
- **Qianxun / BDStar BeiDou CORS Pakistan (UniStrong, 2014)** — 5-base BeiDou CORS in Karachi commissioned 2014-05-21 (China Daily 2014-05-23). Operationally absorbed under SUPARCO; not advertised as a separate public service. Coverage is the same Karachi-metro footprint that Pak-Rehber describes today. See "Underlying hardware lineage" note in the Pak-Rehber block above.
- **Survey of Pakistan (SoP) static GNSS monuments** — Surveying and Mapping Act 2014; tender for 31 new GNSS monuments (bid open 17 Dec 2024; construction ~6–8 months) is for static geodetic-datum benchmarks under the NSDI programme (sop.gov.pk / nsdi.gov.pk), not a real-time CORS/NTRIP service. The "240 levelling benchmarks" figure cited in earlier research could not be re-confirmed from accessible sources 2026-05-23 — tender PDF was reachable in earlier research but ECONNREFUSED from sandbox today. NSDI Pakistan (nsdi.gov.pk) has not published any roadmap for a national real-time CORS service. No public NTRIP caster has been announced by SoP as of 2026-05-23.
- **Pak-SBAS (SUPARCO)** — Pakistan's L-band satellite-based augmentation; demonstrated at Cholistan Rally 2026-02-15. 2.5 m → 15 cm positioning spec per COPUOS 2025 statement — sub-metre/few-decimetre satellite augmentation broadcast direct via satellite, NOT NTRIP RTK. Out of scope for this project (SBAS class). Receiver units expected to be delivered to government agencies and selected private-sector partners before end of 2026 per corsstations.com reporting.
- **Northern Pakistan (Gilgit-Baltistan / Azad Kashmir / Khyber-Pakhtunkhwa frontier zones):** no known public RTK or volunteer rtk2go bases; mapping activity additionally restricted under defence-sensitive-area provisions of the Surveying and Mapping Act 2014. Tier-2 cities (Lahore, Islamabad, Rawalpindi, Faisalabad, Multan, Peshawar, Quetta) likewise have no known public NTRIP bases — checked rtk2go sourcetable 2026-05-23 (only PK row is `Stingray_tech` Karachi); no Pakistani survey/GIS community bases publicly registered located 2026-05-23.

## Sources Consulted (2026-05-23)

- SUPARCO Pak-Rehber precise positioning service portal: `https://suparco.gov.pk/precise-positioning-service/` (curl SSL-bypass returned mostly inline CSS; key text via WebSearch indexed snippet 2026-05-23 — "Pak-Rehber Precise Positioning Service provides positioning data through GNSS Real-Time Kinematic (RTK) network. Centimeter-level accuracy is available with unmatched reliability"). WebFetch ECONNREFUSED / cert error / 418 from sandbox.
- SUPARCO Business Solutions: `https://suparco.biz/satcom-navigational-solutions/` (operator-confirmed Pak-GBAS NRTK + Pak-Rehber + Pak-SBAS triad; "authorized users in Karachi" wording).
- SUPARCO Satellite Navigation programme overview: `https://suparco.gov.pk/major-programmes/sat-nav-program/`.
- Pak-Rehber brochure (PDF): `https://suparco.biz/wp-content/uploads/2025/03/pak-rehber.pdf` — HTTP 403 from sandbox 2026-05-23 (was reachable 2026-04-30 per prior research; "Only authorized users" quote sourced from that earlier fetch).
- Pak-Rehber academic use: Sirajuddin et al., "Design and Implementation of a Localization App to Achieve Sub-Meter Level Accuracy using Suparco's Pak-Rehber Precise Positioning Service" — IEEE doc 11004397 (2024).
- Pakistan COPUOS STSC 2024 statement: `https://www.unoosa.org/documents/pdf/copuos/stsc/2024/Statements/8_Pakistan_STSC_1.pdf` (cited via search snippets; "GBAS on Proof of Concept basis ... authorized users").
- Pakistan COPUOS STSC 2025 statement: `https://www.unoosa.org/documents/pdf/copuos/stsc/2025/Statements/3_Pakistan_for_upload.pdf` (Pak-SBAS spec 2.5 m → 15 cm; GBAS PoC restated).
- Cholistan Rally Pak-SBAS launch 2026-02-15: `https://www.app.com.pk/national/suparco-launches-advanced-pak-sbas-navigation-system-at-cholistan-rally-2026/`; `https://www.pakistantoday.com.pk/2026/02/15/suparco-tests-pak-sbas-navigation-system-at-cholistan-rally-shows-high-precision-tracking`.
- Stingray Technologies (Pakistan): `https://stingray.com.pk/` — Karachi defence-tech firm; operator of `Stingray_tech` rtk2go mount.
- rtk2go sourcetable live probe: `curl --http0.9 http://rtk2go.com:2101/` 2026-05-23 → confirms `Stingray_tech` row PAK 24.89,67.09 RTCM 3.2 GPS+GLO+GAL+BDS.
- Survey of Pakistan: `https://surveyofpakistan.gov.pk/` and `https://sop.gov.pk/` (both ECONNREFUSED from sandbox 2026-05-23). GNSS monument tender: `https://www.surveyofpakistan.gov.pk/SiteImage/Misc/files/Final%20Draft%20tender%20construction.pdf` (ECONNREFUSED 2026-05-23; details via tendersontime.com snippet — 31 GNSS monuments + 240 BMs, delivery 30 Dec 2025).
- NSDI Pakistan: `https://nsdi.gov.pk/` (NSDI mandate, Mapping Act 2014 reference).
- Local pipeline counts via `scripts/stations_by_country.py PAK` 2026-05-23: rtk2go = 1 (Stingray_tech 24.89, 67.09); auscors / igs_ip / euref_ip / centipede / earthscope / mirai = 0.
- ArduSimple Pakistan dealer cache: not present (`docs/ardusimple/PK*` does not exist; ardusimple.com has no `/rtk-correction-services-and-ntrip-casters-in-pakistan/` page — HTTP 404 2026-05-23).
- mvarga1989 community CORS list: Pakistan not listed (`https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks`).
- Surveying and Mapping Act 2014 (full text): `https://www.na.gov.pk/uploads/documents/1397721138_588.pdf`; consolidated `https://www.nasirlawsite.com/laws/sama.htm`. Amendment penalty reporting (5-year jail / PKR 5M fine under Section 20 for unofficial Pakistan maps): `https://www.thenews.com.pk/print/723903-amendments-to-surveying-mapping-act-5-years-jail-for-using-unofficial-pak-maps` (WebFetch 2026-05-23 confirmed).
- UniStrong / BeiDou Pakistan 2014 reference: `https://usa.chinadaily.com.cn/china/2014-05/23/content_17536411.htm`; `https://tribune.com.pk/story/712376/pakistan-becomes-first-country-to-deploy-chinas-beidou-gps-network`; `https://geospatialworld.net/news/pakistan-adopts-chinas-beidou-navigation-system/`.
