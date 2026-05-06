# India [IN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-04

## Status: YES — national SoI CORS caster operational; paid for private users; Indian ID required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **host:port — Region 1** | `103.205.244.106:2101` (UP, Uttarakhand, Haryana, Punjab, Himachal Pradesh, NCR, MP, Rajasthan) |
| **host:port — Region 2** | `103.206.29.4:2105` (Maharashtra, Karnataka, south) |
| **portal** | https://cors.surveyofindia.gov.in |
| **tariff — Gov / Academic** | Free (no subscription fee; KYC registration required) |
| **tariff — private (RTK, excl. GST)** | ₹5,000/mo · ₹15,000/3 mo · ₹30,000/6 mo · ₹60,000/yr; add 18% GST → ₹5,900 · ₹17,700 · ₹35,400 · ₹70,800 incl. GST (observed 2026-05-04; source: cors.surveyofindia.gov.in/subscription-charges) |
| **tariff — private (DGNSS, excl. GST)** | ₹2,000/mo (DGNSS1) incl. GST ₹2,360; DGNSS3/DGNSS12 prices not confirmed publicly |
| **tariff VAT note** | 18% GST added at checkout; all prices above are gross (incl. GST) where confirmed |
| **hobbyist_eligibility** | Unclear / conditionally yes — private individuals can register and pay; no surveying licence required; promotional free access for private individuals ran Nov 2025 – Jan 2026; post-promo status reverts to paid tier |
| **legal_residency_required** | Yes (effectively) — Aadhaar Card or PAN Card required for registration; foreign nationals cannot hold either in the ordinary course |
| **last_confirmed_alive** | 2026-05-04 — `http://103.205.244.106` returned full portal content including © 2026 footer; HTTPS portal also reachable |

## Context Notes

- **SoI CORS** is the Survey of India Continuously Operating Reference Stations network; 1,105+ stations across most of India (operational since ~2022). National portal: cors.surveyofindia.gov.in. NTRIP mount point carries RTCM3 / NRTK (VRS) corrections at ±3–4 cm claimed accuracy.
- **Region 1** covers the north and central states; **Region 2** covers Maharashtra, Karnataka, and further south. An older IP (117.251.x.x) cited in early tutorials for the Maharashtra/Karnataka region appears superseded by Region 2.
- **Andhra Pradesh (70 stations):** Signed MoU with SoI on 13 October 2025 to integrate all 70 AP CORS stations into the national SoI CORS network (confirmed by Times of India 2025-10-17 and SoI social media). No standalone AP NTRIP endpoint remains; AP stations are migrating to SoI infrastructure. No new SoI regional endpoint for AP publicly announced as of 2026-05-04. Contact: itdept.sslr@gmail.com.
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
