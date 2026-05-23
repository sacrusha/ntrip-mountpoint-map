# Bangladesh [BD] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: YES — Survey of Bangladesh (SoB) national VRS NTRIP service (paid, gated by Bangladeshi mobile + mobile-banking); 2 Centipede volunteer bases (Dhaka, Chittagong) are the only free real-time option

Two pareto paths for a Bangladesh-resident hobbyist:

1. **SoB VRS / SOB Online Data Service** — national VRS over 6 (now 6 SoB-operated; possibly being expanded under JICA) physical CORS. Paid, no published tariff, signup gated through `data.sob.gov.bd` with a Bangladeshi mobile number + bKash/Rocket/SureCash payment rail.
2. **Centipede `BENGLA1` (Dhaka) + `BENGLA4` (Chittagong)** — two volunteer bases in the same Centipede pool. Free, no registration; covers Dhaka and Chittagong metros within ~30 km each.

Outside the two Centipede bases and the SoB-paid path there is no other free or cheaper-than-SoB public option. A separate Columbia-University-led 16-station tectonic-research GNSS network (Mike Steckler / Dhaka University) operates in southern/eastern Bangladesh for plate-motion / land-subsidence science but is research-only — not a public NTRIP RTK service. Disqualified, covered below.

---

## SoB VRS — Survey of Bangladesh CORS Network

| Field | Value |
|---|---|
| operator | Survey of Bangladesh (SoB / বাংলাদেশ জরিপ অধিদপ্তর), Ministry of Defence |
| landing_url | https://sob.gov.bd/site/page/2e0fd063-09e4-4512-a470-a5fbd3668c71/Geodetic- |
| access_url | https://data.sob.gov.bd/signup-user.php |
| access_type | paid |
| coverage | National Bangladesh from 6 primary CORS (Dhaka, Chittagong, Rajshahi, Khulna, Maulavibazar, Rangpur, operational since 19 December 2011). Inter-station baselines run ~150–250 km — substantially outside the 30–70 km envelope needed for reliable VRS-class accuracy throughout the hull; degradation away from station sites is significant. **JICA-funded densification under way:** the "Permanent GNSS CORS Network Project" (main contractor Toyota Tsusho Corporation; subcontractor Tec International; local contractor Project Promoters Pvt. Ltd.) is densifying to **73 nationwide locations** plus modernised tidal stations, JICA preparatory survey published January 2018, "actively implementing" status 2024 per projectpromoters.com. May 2025 SoB+JICA seminar (BSS News 2025-05-27) confirms continued investment; current operational-station-count delta or new NTRIP mountpoint inventory was not located on the operator portal (checked: sob.gov.bd Geodetic Services 2026-05-23; data.sob.gov.bd 2026-05-23; sob.portal.gov.bd 2026-05-23). |
| num_stations | 6 SoB primary CORS confirmed operational (operator-confirmed via SoB Geodetic Services page; corroborated by The Guardian BD 2014, ardusimple.com 2026-05-23). Up to 73 total stations under JICA densification (Toyota Tsusho contractor, scope from JICA 2018 preparatory survey; current operational count of the densified network not publicly reported). |
| sourcetable | `202.53.170.98:8011` (declared on SoB Geodetic Services page) — sandbox probe 2026-05-23 timed out at 12 s (egress geo-restriction to BD likely; not necessarily an outage). Legacy operator portal `202.40.181.3:8021` returned HTTP 200 with ASP.NET map portal markup 2026-05-23, confirming SoB infrastructure alive though no NTRIP sourcetable served on that port. No third-party caster cache (e.g. SNIP `monitor.use-snip.com`) lists this host. Mountpoint name, format details, and constellation set are not publicly published; operator portal exposes them only after login. |
| vrs | yes — SoB Geodetic Services page documents a "Virtual Reference Station Software" running on the SoB data-centre server, synthesising corrections from the 6 SoB CORS plus surrounding IGS reference stations (The Guardian BD 2014; SoB portal). |
| tariff | not published — `cors.surveyofindia` style fee table absent on sob.gov.bd, data.sob.gov.bd, and sob.portal.gov.bd as of 2026-05-23 (checked: WebSearch indexed snippets 2026-05-23; data.sob.gov.bd WebFetch returned login-only landing 2026-05-23; sob.gov.bd direct WebFetch cert-chain validation fails from sandbox 2026-05-23). The Guardian BD 2014 wording: "Connection to some govt. organizations are already provided free of cost for trial basis" + "geo-information users on payment." Payment rail is bKash/Rocket/SureCash mobile-banking per SoB online data-service model — requires a Bangladeshi mobile + account. |
| hobbyist_eligibility | yes-in-principle, gated-by-payment-rail-in-practice. No surveying-licence or eligibility gate stated on `data.sob.gov.bd`. The practical access barrier is payment infrastructure (Bangladeshi phone OTP at signup + bKash/Rocket/SureCash for payment) — UX/payment-rail constraint, not a legal eligibility rule. ArduSimple Bangladesh page notes UX is "not very user-friendly." |
| residency_required | no (legally) — no statute or operator declaration of residency requirement. Practically yes (de-facto), via mobile-banking gate. |
| stations_source | Coverage map on legacy portal `http://202.40.181.3:8021/Map/SensorMap.aspx` (ASP.NET map UI per ArduSimple 2026-05-23 confirmation); no public station-name list found on operator portal as of 2026-05-23. Primary-CORS names also documented in The Guardian BD 2014 article (Dhaka, Chittagong, Rajshahi, Khulna, Maulavibazar, Rangpur). |
| datum_epoch | ITRF2008 (datum family + realisation; epoch not declared by operator). Grokipedia "Survey of Bangladesh" entry (synthesising published sources) states: "SoB established a network of GNSS Continuous Operating Reference Stations (CORS) starting in 2011 with six permanent stations tied to ITRF2008, later densified to support real-time positioning and national spatial data infrastructure (NSDI) development." The Guardian BD 2014 states the network "conforms to the latest International Terrestrial Reference Frame (ITRF) standards." The specific epoch year is not declared on any operator page reachable from sandbox 2026-05-23 (checked: sob.gov.bd Geodetic Services page WebFetch cert error 2026-05-23; data.sob.gov.bd login-only; un-ggim-ap.org Howlader PDF retrieved in prior research is image-stream-only with no extractable text; researchgate displacement-monitoring paper 331850561 HTTP 403). ArduSimple's Bangladesh page lists the coordinate system as "Global WGS84" (2026-05-23) — vendor characterisation, not operator declaration. Working assumption for hobbyists: ITRF2008 at the 2011 station-establishment epoch (or close to it); survey-grade users should request the operator's per-station coordinate sheet. |

### NRTK / VRS notes

- VRS service objectives per SoB: RTK + post-processing, tectonic-plate monitoring, earthquake-vulnerability prediction, geodetic-control-network upgrades.
- Bernese back-end: SoB Geodetic Services page documents that the VRS solution is "computed with respect to IGS Stations surrounding Bangladesh using Bernese software, and coordinates are input to the VRS NET" — Bernese-driven NRTK.
- 6-CORS-over-147,570-km² gives mean inter-station spacing ~200 km — well outside the 30–70 km envelope needed for VRS to deliver cm-accurate fix throughout the hull. Expect strong degradation away from each physical CORS site; fix-quality will resemble single-base RTK with ppm-scaled error at typical baselines. Underserved hobbyist regions on the current (pre-densification) 6-station network: Sylhet haor / tea region (~80–120 km from Maulavibazar but high terrain variability), Cox's Bazar coastal belt (~150 km from Chittagong), Sundarbans (~100–150 km from Khulna), Barisal division. JICA densification to 73 stations is the planned remedy.
- May 2025 SoB seminar with JICA chief representative Ichiguchi Tomohide present (BSS News 2025-05-27) reaffirms ongoing JICA-funded geospatial cooperation. Operational status of the 73-station densified network not publicly broken out by station count or NTRIP-endpoint update on operator portal 2026-05-23.

---

## Centipede — `BENGLA1` (Dhaka) + `BENGLA4` (Chittagong)

| Field | Value |
|---|---|
| operator | Centipede-RTK community (caster); individual base operators in BD (not publicly named per station) |
| landing_url | https://www.centipede-rtk.org/ |
| access_url | https://docs.centipede.fr/docs/centipede/3_connect_caster.html |
| access_type | free |
| coverage | Two single-base mountpoints: `BENGLA1` at 23.722 N, 90.401 E (Dhaka, useful ~10–30 km radius); `BENGLA4` at 22.270 N, 91.812 E (Chittagong, ~10–30 km radius). No coverage outside those two metros. |
| num_stations | 2 |
| sourcetable | `crtk.net:2101` SOURCETABLE 200 OK 2026-05-23. Both BD rows: `STR;BENGLA1;BGD;RTCM3;1004,1005,1006,1008,1012,1019,1020,1033,1042,1045,1046,1077,1087,1097,1107,1127,1230;3;GLO+GAL+SBS+BDS+GPS;NONE;BGD;23.722;90.401;0;0;NTRIP RTKBase Septentrio_Mosaic-X5 2.7.0 4.15.1;none;N;N;15200;CentipedeRTK` and `STR;BENGLA4;...;BGD;22.270;91.812;...;CentipedeRTK`. Both Septentrio Mosaic-X5 + RTKBase, RTCM3 MSM7 GPS+GLO+GAL+BDS+SBAS (no NavIC, no QZSS), carrier=3, ~15 kB/s. Single-base mountpoints (nmea=0, solution=0); no VRS. Legacy host `caster.centipede.fr:2101` still resolves but `crtk.net:2101` is the canonical Centipede host since 2025-03-18 — see `docs/ntrip_research/Centipede.md`. |
| vrs | no — single-base RTCM3 streams from two physical Septentrio receivers |
| hobbyist_eligibility | yes |
| residency_required | no |
| stations_source | `curl --http0.9 http://crtk.net:2101/` filtered for `BGD` rows; also visible via the Centipede live map at https://map.centipede-rtk.org/ and in the local pipeline via `scripts/stations_by_country.py BGD` (2026-05-23 local cache shows 1 — pipeline cache stale relative to upstream which serves both). |

### Hobbyist path summary

- **Inside ~30 km of Dhaka centre** → `crtk.net:2101 / BENGLA1` (free, no payment, no Bangladeshi-phone requirement).
- **Inside ~30 km of Chittagong centre** → `crtk.net:2101 / BENGLA4` (same).
- **Anywhere else in Bangladesh** → SoB VRS subscription via `data.sob.gov.bd` — paid (tariff not published), Bangladeshi mobile + mobile-banking required; for foreign hobbyists effectively a hard barrier despite being legally open. Otherwise: self-hosted base, satellite PPP (Galileo HAS), or post-processing.

---

## Cross-border reachability (for users near a frontier)

Bangladesh borders India (3 sides — North, West, East) and Myanmar (SE).

- **India SoI CORS** — Region 1 covers Tripura, Mizoram, Meghalaya, Manipur, Assam, Bihar; Region 2 covers West Bengal. A hobbyist near the Jessore/Benapole border crossing is ~70–90 km from Kolkata (West Bengal, SoI Region 2) — within VRS hull range in principle. Same for users in northern Bangladesh near the Meghalaya/Assam border (Region 1 northeast). But SoI CORS registration requires an Indian-resident photo ID (Voter ID / DL / Aadhaar / PAN), making this practically inaccessible to a Bangladesh national regardless of geographic proximity. See `docs/ntrip_research/IN_India.md`.
- **Myanmar** — no publicly known NTRIP RTK service (checked: WebSearch 2026-05-23 — no Myanmar national CORS portal, no ardusimple Myanmar page found, no rtk2go/IGS-IP Myanmar stations in local pipeline 2026-05-23).
- **Conclusion: no realistic cross-border free RTK path for a BD-resident hobbyist.**

---

## Disqualified / context (covered in own files where applicable)

- **rtk2go** — 0 BD-tagged mountpoints (local pipeline 2026-05-23 confirms; live rtk2go sourcetable 2026-05-23 has no `BGD` rows). See `docs/ntrip_research/Rtk2go.md`.
- **IGS-IP** — no BD-located IGS RT station in `data/igs_ip.sourcetable` 2026-05-23. IGS station `DHAK` (Dhaka, on `network.igs.org`) historically contributed RINEX but is not a current real-time RTS mountpoint. Post-processing RINEX archives via `igs.bkg.bund.de` remain free. See `docs/ntrip_research/IGS-IP.md`.
- **EUREF-IP** — no BD stations (regional scope is Europe). See `docs/ntrip_research/EUREF-IP.md`.
- **EarthScope / NOTA RTGPS** — no BD stations (Americas-region scope; legacy UNAVCO real-time platform retired 2025-07-29). See `docs/ntrip_research/Earthscope.md`.
- **AUSCORS** — no BD stations rebroadcast (local pipeline 2026-05-23 lists 2 IN + 1 LKA from the Asia feed).
- **MIRAI** — no BD stations (local pipeline 2026-05-23 lists LKA-2 only).
- **GEODNET / HYFIX / ONOCOY / PointOne / RTKdata / TopNET Live** — no Bangladesh-specific coverage publicly disclosed (station maps checked 2026-05-23; Bangladesh absent from all). Local survey-instrument vendors (Benchmark Instruments, TechnoPlanet, Bdsthapati, ensun-listed top-9 land-surveying firms) sell RTK gear but do not advertise public NTRIP services.
- **Columbia University / Dhaka University tectonic GNSS network (Mike Steckler)** — 16 research stations in Bangladesh tracking tectonic plate motion and delta subsidence (sinking <1 mm/y revealed). Active fieldwork November 2025: 3 of 16 transmitting to the US, 13 needing repair, 3 new being added (GPS World 2025-11; news.climate.columbia.edu 2025-11-06). NOT a public NTRIP RTK service: data flows to US-based science archives for post-processing, supported via NSF funding routed through the EarthScope Consortium. (EarthScope/UNAVCO retired its public real-time NTRIP platform 2025-07-29, but Steckler's research data flow is to science archives, not the retired real-time platform, so the retirement is non-impacting for this network.) Out of scope. Mike Steckler profile: `https://people.climate.columbia.edu/users/profile/michael-s-steckler`. Stations concentrated in Sylhet tea region and southern coastal belt — geographically overlap the underserved zones of the SoB-6-CORS network, but research-only and not retrievable as RTK corrections.
- **Bangladesh JICA seminar 2025-05-27** — Survey of Bangladesh + JICA + Defence Ministry seminar on "Geospatial Technology Transformation: GNSS (CORS) as the Key to Sustainable Infrastructure Development in Bangladesh." Confirms ongoing JICA-supported CORS investment under the densification project; no public NTRIP-service deliverable or tariff disclosed at the seminar per BSS News 2025-05-27.

## Legal context (Surveying / Mapping)

Bangladesh's primary surveying statute is the **Survey Act 1875** (bdlaws.minlaw.gov.bd act-details-32) — a colonial-era act covering land surveying and demarcation. SoB additionally operates under the "Rules for Classification, Custody and Issue of Aerial Photographs" (Ministry of Defence), with classified-vs-public categorisation for aerial photographs. **Neither instrument explicitly regulates private NTRIP/CORS/RTK base operation**; private surveying companies operate under SoB registration (`sob.gov.bd/pages/static-pages/6922dcff933eb65569e13189` lists registered companies) but no equivalent of Pakistan's 5-year-jail Section 20 amendment applies to NTRIP base hosting. Hobbyist self-hosting a base in BD is not specifically prohibited; sensitive-area mapping is the de-facto restriction (defence/military zones, border belts).

## Out-of-scope augmentation (one-line disambiguation for BD readers)

A Bangladesh hobbyist Googling "Bangladesh GNSS corrections" may surface satellite augmentation that is NOT NTRIP RTK:

- **Galileo HAS** — free global SSR satellite augmentation, ~20–40 cm without internet. SSR class, out of scope.
- **GAGAN (India SBAS)** — covers Bangladesh airspace incidentally; sub-metre L-band satellite augmentation. SBAS class, out of scope.

Neither replaces the SoB VRS or Centipede paths for cm-accurate RTK.

## Sources Consulted (2026-05-23)

- SoB Geodetic Services page: `https://sob.gov.bd/site/page/2e0fd063-09e4-4512-a470-a5fbd3668c71/Geodetic-` (declares `202.53.170.98:8011` VRS endpoint; cert-chain validation fails from sandbox WebFetch 2026-05-23).
- SoB main site mirror: `https://sob.portal.gov.bd/` (reachable via Google index 2026-05-23 — confirms 6-CORS list).
- SoB Data Service portal: `https://data.sob.gov.bd/` — WebFetch 2026-05-23 returned login + signup form, no pricing, no NTRIP info on landing.
- SoB Data Service signup: `https://data.sob.gov.bd/signup-user.php`.
- SoB news on upgraded data portal: `https://sob.gov.bd/pages/news/6922db52933eb65569e09634`.
- Legacy SoB portal IP: `http://202.40.181.3:8021/` curl probe 2026-05-23 returned HTTP 200 ASP.NET map portal markup (alive, no NTRIP sourcetable on this port).
- SoB VRS endpoint `202.53.170.98:8011` curl probe 2026-05-23 — 12 s timeout (sandbox egress geo-restriction to BD presumed; not a confirmed outage).
- ArduSimple Bangladesh page: `https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bangladesh/` — confirms SoB as paid national + WGS84 coordinate-system characterisation 2026-05-23.
- The Guardian BD (2014): `https://theguardianbd.net/4634/` — 6 SoB CORS primary + 50–60 secondary planned; ITRF-aligned datum; "RTK correction available through internet"; paid for non-govt.
- BSS News seminar 2025-05-27: `https://www.bssnews.net/news/277274` — SoB + JICA seminar on GNSS CORS.
- Centipede live sourcetable: `curl --http0.9 http://crtk.net:2101/` 2026-05-23 — confirms `BENGLA1` (Dhaka 23.722, 90.401) and `BENGLA4` (Chittagong 22.270, 91.812), both Septentrio Mosaic-X5 + RTKBase RTCM3 MSM7 GPS+GLO+GAL+BDS+SBAS.
- Centipede docs: `https://docs.centipede.fr/docs/centipede/3_connect_caster.html`.
- Centipede live map: `https://map.centipede-rtk.org/`.
- Mike Steckler / Columbia Climate School Bangladesh GNSS coverage: `https://www.gpsworld.com/researcher-recounts-adventure-updating-gnss-stations-in-bangladesh/` (2025-11); `https://news.climate.columbia.edu/2025/11/06/repairing-global-navigation-satellite-systems-in-the-land-of-tea/`.
- UN-GGIM-AP Howlader Bangladesh geodetic-infrastructure PDF (image-stream, no extractable text): `https://un-ggim-ap.org/sites/default/files/media/meetings/Plenary08/WG1_S2B_3%20Rouf%20Howlader_Geodetic%20Infrastructure%20%20and%20Reference%20Frame%20of%20Bangladesh.pdf`.
- Local pipeline counts via `scripts/stations_by_country.py BGD` 2026-05-23: centipede = 1 cached (live sourcetable carries 2 — pipeline-cache-stale; refresh-cadence artefact, not a fetch bug); auscors / igs_ip / euref_ip / earthscope / mirai / rtk2go = 0.
- ArduSimple Bangladesh dealer cache: `docs/ardusimple/BD_Bangladesh.md` 2026-05-16 — only names SoB as national paid.
- IDMS Project & JICA SoB page: `https://sob.gov.bd/site/page/7ce70d3e-1e84-49c5-9ad4-6b596a0270ae/IDMS-Project-&-JICA` and Bangla mirror `http://sob.portal.gov.bd/pages/static-pages/6922dcef933eb65569e12d01` — names the JICA-funded IDMS project as the umbrella for the GNSS CORS densification. WebFetch cert error from sandbox 2026-05-23; content sourced via WebSearch snippets.
- JICA preparatory survey for Bangladesh GNSS CORS densification + tidal stations (January 2018): `https://openjicareport.jica.go.jp/618/618/618_101_12338752.html` (publisher info reachable; full PDF report 12338752_01.pdf binary).
- Permanent GNSS CORS Network Project (project-promoter overview): `https://projectpromoters.com/permanent-gnss-cors-network-project-in-bangladesh/` 2026-05-23 — confirms 73-location densification, Toyota Tsusho main contractor, "actively implementing" as of 2024.
- Survey Act 1875 (BD): `http://bdlaws.minlaw.gov.bd/act-details-32.html`.
- Grokipedia "Survey of Bangladesh" (synthesising published sources including ITRF2008 datum claim): `https://grokipedia.com/page/survey_of_bangladesh` — HTTP 403 from sandbox 2026-05-23, content sourced via WebSearch snippet.
- Geosystem Corp BD geodetic-survey overview: `https://geosystembd.com/geodetic-control-survey/`.
- gis.gov.bd SoB organisation profile: `http://gis.gov.bd/en/organization_profile.php?organization=39`.
