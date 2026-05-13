# Bahamas [BS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: National 23-station Trimble Pivot CORS exists (deployed ~2020 for Dept. of Lands & Surveys); no public NTRIP endpoint disclosed — EarthScope scientific streams available on two outer islands

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | Physical infrastructure exists (23 Trimble CORS + 3 tide gauges, Bahamas Department of Lands & Surveys, Spatial Dimension/Trimble project ~2020) — but no public host:port, sourcetable, or self-service registration portal has been published. Likely Trimble Pivot Platform; if operational it is gated for licensed Bahamian surveyors via Lands & Surveys. |
| **Scientific GNSS streams in BS territory** | Yes — EarthScope NOTA (former COCONet) CN13 (San Salvador Island) and CN14 (Mathew Town, Great Inagua); all on `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | EarthScope: **Yes** (noncommercial tier — no surveying licence required, individual account accepted). Bahamian national CORS: **unclear** — no published policy, likely restricted to licensed Bahamian surveyors. |
| **legal_residency_required** | EarthScope: **No** — no nationality or residency restriction in NULA. Bahamian national CORS: unclear. |
| **last_confirmed_alive** | 2026-05-12 (EarthScope portal reachable; NULA dated v. 2025-05-30); Spatial Dimension project page still served as of 2026-05-12. No live Bahamian NTRIP endpoint has ever been probed; none surfaces in any public sourcetable directory. |

---

## EarthScope NOTA — COCONet Stations in Bahamas Territory

| Station | Location | Notes |
|---|---|---|
| **CN13** | San Salvador Island, central Bahamas | ~460 km SE of Nassau |
| **CN14** | Mathew Town, Great Inagua, southernmost Bahamas | ~525 km SE of Nassau; ~80 km NE of Haiti/Cuba channel |

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT VRS/Network-RTK) |
| **Tariff — noncommercial** | **Free (USD $0.00)** — account + annual NULA acceptance required. Date observed: 2026-05-06. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **Tariff — commercial** | **USD $1,000 per seat per year** (EarthScope 501(c)(3); no VAT). Date observed: 2026-05-06. Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |

**Practical caveat**: CN13 and CN14 are both located on outer islands far from Nassau (New Providence) and Grand Bahama, where most commercial and survey activity occurs. Nassau is ~460 km from the nearest COCONet station; single-base RTK is not viable at that distance. Users in Nassau and the northern Bahamas have no practical COCONet coverage for RTK.

**Note on legacy platform**: Old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

---

## National Surveying Authority

The **Department of Lands and Surveys** (Bahamas Government) is the responsible body for geodetic and cadastral work. NOAA's National Geodetic Survey database lists an AUTEC (Atlantic Underwater Test and Evaluation Center) CORS station in Andros, Bahamas, operated by the US Navy, but this is a US Federal installation and not a Bahamian national service.

### Bahamas National CORS (Spatial Dimension / Trimble, ~2020)

A 23-station Bahamian national CORS network plus 3 tide-gauge monitoring stations was deployed for the Department of Lands and Surveys by Spatial Dimension in partnership with Trimble Inc. as part of a broader land-management modernisation programme (Trimble Pivot Platform + Landfolio cadastral software). Bahamian surveying kits for field crews were procured under the same contract. Reference: Spatial Dimension project profile (https://www.spatialdimension.com/projects/bahamas-department-of-lands-and-surveys, observed 2026-05-12; Trimble press release referenced June 2020).

- **Host:port**: Not published. No public NTRIP sourcetable. No website on bahamas.gov.bs surfaces the caster URL. The deployment uses Trimble Pivot software (RTK/VRS-capable) but the caster endpoint is not advertised publicly.
- **Coverage**: 23 stations across the archipelago — sufficient density (~700 km W-E, ~1,200 km N-S spread) for network RTK across populated islands if operated as VRS, but unconfirmed.
- **Hobbyist access**: Not confirmed available. The deployment is explicitly tied to cadastral/surveying modernisation under the Department of Lands and Surveys; access is most likely gated to licensed Bahamian surveyors via institutional procedure (no online self-service portal found).
- **Workaround for hobbyists**: EarthScope COCONet streams CN13/CN14 remain the only confirmed publicly accessible streams in Bahamian territory, but practical only for users on/near San Salvador and Great Inagua (>460 km from Nassau).

---

## Most Recent Project Announcement

**Bahamas Department of Lands & Surveys 23-CORS deployment (Spatial Dimension / Trimble, ~2020)** — reference: https://www.spatialdimension.com/projects/bahamas-department-of-lands-and-surveys. No further public announcement of a public NTRIP service tier through 2024–2026. No CARICOM or regional geodetic CORS project specific to the Bahamas was identified beyond this single deployment.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive** — COCONet CN13 and CN14 RINEX | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

## Sources Consulted
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/
- EarthScope commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- COCONet site info (station list including CN13, CN14): https://coconet.unavco.org/site-info/site-info.html
- COCONet network overview: https://coconet.unavco.org/
- NOAA NGS CORS database (AUTEC Andros reference): https://geodesy.noaa.gov/CORS/
- Spatial Dimension — Bahamas Department of Lands and Surveys CORS project profile (23 Trimble CORS + 3 tide gauges): https://www.spatialdimension.com/projects/bahamas-department-of-lands-and-surveys (observed 2026-05-12)
- Bahamas.gov.bs Department of Lands and Surveys page: https://www.bahamas.gov.bs/agencies/department-of-lands-and-surveys (HTTP 403 from automated fetch 2026-05-12; no public CORS link via Google)
- NTRIP-list.com North America — no BS entry found
- RTK2go / Centipede sourcetables — no BS stations found
