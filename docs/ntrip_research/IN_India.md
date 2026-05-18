# India [IN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-12 entry; HTTP IP 103.205.244.106 still serves SoI portal; HTTPS portal + Region 2 (103.206.29.4:2105) sandbox-unreachable — geo-route consistent w/ prior; subscription-charges page WebFetch ECONNREFUSED 2026-05-17)

## Status: YES — national SoI CORS caster operational; paid for private users; Indian ID required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **landing_url — SoI CORS** | `https://cors.surveyofindia.gov.in/` — operator-owned portal (Survey of India CORS). Describes service, regions, station coverage. |
| **access_url — SoI CORS** | `https://cors.surveyofindia.gov.in/subscription-charges` — pricing + registration terms. More useful than the bare portal for someone deciding to subscribe. |
| **host:port — Region 1** | `103.205.244.106:2101` (UP, Uttarakhand, Haryana, Punjab, Himachal Pradesh, NCR, MP, Rajasthan) |
| **host:port — Region 2** | `103.206.29.4:2105` (Maharashtra, Karnataka, south) |
| **portal** | https://cors.surveyofindia.gov.in (HTTPS portal not reachable from sandbox 2026-05-12 + 2026-05-17 — geo-routing pattern; HTTP at 103.205.244.106 returns HTTP 200 + portal HTML 200 OK 2026-05-17 + portal markup 2026 footer, confirming alive) |
| **tariff — Gov / Academic** | Free (no subscription fee; KYC registration required) |
| **tariff — private (RTK, excl. GST)** | ₹5,000/mo · ₹15,000/3 mo · ₹30,000/6 mo · ₹60,000/yr; add 18% GST → ₹5,900 · ₹17,700 · ₹35,400 · ₹70,800 incl. GST (last confirmed via subscription-charges page 2026-05-04; re-fetch attempts 2026-05-12 + 2026-05-17 returned ECONNREFUSED from sandbox — geo-routing) |
| **tariff — private (DGNSS, excl. GST)** | ₹2,000/mo (DGNSS1) incl. GST ₹2,360; DGNSS3/DGNSS12 prices not confirmed publicly |
| **tariff VAT note** | 18% GST added at checkout; all prices above are gross (incl. GST) where confirmed |
| **promotional free access (private sector)** | Confirmed: SoI has run promotional free 3-month CORS access campaigns for private-sector users (Geospatial World coverage 2025; SoI's own X/Facebook accounts have continued to repost a "Free Subscription of CORS Services by Survey of India" announcement as recently as October 2025 — see SoI X status 1983899442022367368, 2025-10-30). Promotional terms re-issued periodically; post-promo status reverts to the paid tariff above |
| **hobbyist_eligibility** | Unclear / conditionally yes — private individuals can register and pay; no surveying licence required |
| **legal_residency_required** | Yes (effectively) — Aadhaar Card or PAN Card required for registration; foreign nationals cannot hold either in the ordinary course |
| **last_confirmed_alive** | 2026-05-17 — `http://103.205.244.106` returned HTTP 200 (ASP.NET portal, fresh session cookie 2026-05-17); HTTPS portal cors.surveyofindia.gov.in + Region 2 NTRIP `103.206.29.4:2105` both sandbox-unreachable (geo-route, not outage); rtk2go shows 1 IN station (IndiaTN02, Tamil Nadu, 10.97,78.08); AUSCORS rebroadcasts 2 IN IGS stations (GDKG, IISC); igs_ip carries 3 (GDKG, IISC, IITK Kanpur) |
| **datum_epoch** | omitted — no citable operator declaration. SoI CORS subscription page not re-fetchable; connection-settings page sandbox-unreachable 2026-05-17. National survey datum is WGS84-based per IS public statements but no real-time-service datum statement obtained from operator portal |

## Context Notes

- **SoI CORS** is the Survey of India Continuously Operating Reference Stations network; 1,105+ stations across most of India (operational since ~2022). National portal: cors.surveyofindia.gov.in. NTRIP mount point carries RTCM3 / NRTK (VRS) corrections at ±3–4 cm claimed accuracy.
- **Region 1** covers the north and central states; **Region 2** covers Maharashtra, Karnataka, and further south. An older IP (117.251.x.x) cited in early tutorials for the Maharashtra/Karnataka region appears superseded by Region 2.
- **Andhra Pradesh (70 stations):** Signed MoU with SoI on 13 October 2025 to integrate all 70 AP CORS stations into the national SoI CORS network (confirmed by Times of India 2025-10-17, SoI X status 1979437501711368536 dated 2025-10-17, and Financial Content / WRAL coverage 2025-10-17). No standalone AP NTRIP endpoint remains; AP stations are migrating to SoI infrastructure. No new SoI regional endpoint for AP publicly announced as of 2026-05-12. Contact: itdept.sslr@gmail.com.
- **Tamil Nadu (70 stations):** Department of Survey and Settlement operates 70 CORS stations on rooftops of state government buildings. Network is a closed internal tool for departmental cadastral resurvey only; no public NTRIP access. Has not signed an MoU with SoI as of 2026-05-04. Portal: tnlandsurvey.tn.gov.in (live 2026-05-04).
- **Kerala:** MoU with SoI signed 18 Jan 2021 for a VRS/NTRIP/NavIC-capable network. CORS equipment installed and used by DSLR staff; no public NTRIP endpoint or tariff published as of 2026-05-04. Portal: dslr.kerala.gov.in (live 2026-05-04). Most recent announcement: 2021-05-24 — https://dslr.kerala.gov.in/en/2021/05/24/cors-network/.
- **ISRO / NavIC:** NavIC is a GNSS constellation, not a CORS/NTRIP RTK correction network. No ISRO-operated NTRIP caster exists.
- **Private operators noted (out of scope):** GEODNET (India stations via HYFIX reseller hyfix.in), RTKdata (rtkdata.com, from $40/mo, 30-day trial), Trimble VRS Now and HxGN SmartNet (no confirmed India production coverage as of Apr 2026), TopNET Live (India coverage unconfirmed).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SoI CORS RINEX download** | https://cors.surveyofindia.gov.in | ₹150/GB + 18% GST (Online GNSS Data Processing); raw RINEX available post-registration |
| **EarthScope / GAGE** (sparse scientific stations) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (email rtgps@earthscope.org for credentials); legacy UNAVCO real-time platform retired 2025-07-29 |
| **IGS Real-Time Service** | ntrip.igs-ip.net:2101 | Free (sparse India coverage; insufficient for dense field RTK) |

## Sources Consulted
- SoI CORS portal and subscription-charges page: https://cors.surveyofindia.gov.in/subscription-charges
- SoI CORS connection-settings: https://cors.surveyofindia.gov.in/connection-settings
- SoI CORS HTTP landing: http://103.205.244.106
- AP–SoI MoU announcement: SoI LinkedIn/Facebook/Instagram + Times of India 2025-10-17
- Tamil Nadu land survey portal: https://tnlandsurvey.tn.gov.in
- Kerala DSLR CORS announcement: https://dslr.kerala.gov.in/en/2021/05/24/cors-network/
- RTKdata India coverage note: https://www.rtkdata.com (observed 2026-05-04)
- Contact for pricing gaps: cors-grb.soi@gov.in
- SoI X — Andhra Pradesh CORS integration MoU (2025-10-17): https://x.com/india_soi/status/1979437501711368536
- SoI X — Free Subscription of CORS Services repost (2025-10-30): https://x.com/india_soi/status/1983899442022367368
- Financial Content / WRAL — AP CORS integration coverage (2025-10-17): https://markets.financialcontent.com/wral/article/tokenring-2025-10-17-andhra-pradesh-forges-geospatial-future-cors-integration-promises-precision-revolution
- Geospatial World — SoI announces three-month free CORS service for private sector: https://geospatialworld.net/prime/soi-announces-three-month-free-cors-service-for-private-sector/
- rtk2go IN station count: 1 (IndiaTN02 in Tamil Nadu) — 2026-05-17 pipeline snapshot via `scripts/stations_by_country.py IND`. AUSCORS rebroadcasts 2 IN (GDKG, IISC); igs_ip carries 3 (GDKG, IISC, IITK)
- ArduSimple India cache (docs/ardusimple/IN_India.md 2026-05-16): notes only SoI CORS as national paid service; aligns w/ this entry
