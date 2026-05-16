# Bahamas [BS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: National 23-station Trimble Pivot CORS exists (deployed ~2020 for Dept. of Lands & Surveys); no public NTRIP endpoint disclosed — EarthScope scientific streams available on two outer islands

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | Physical infrastructure exists (23 Trimble CORS + 3 tide gauges, Bahamas Department of Lands & Surveys, Spatial Dimension/Trimble deployment ~2020) — but no public host:port, sourcetable, or self-service registration portal has been published. Platform is Trimble Pivot (RTK/VRS-capable); if operational it is gated for licensed Bahamian surveyors via Lands & Surveys. |
| **Scientific GNSS streams in BS territory** | Yes — EarthScope NOTA (former COCONet) CN13 (San Salvador Island) and CN14 (Mathew Town, Great Inagua); both on `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | EarthScope: **Yes** (noncommercial tier — no surveying licence required, individual account accepted). Bahamian national CORS: **unclear** — no published policy, likely restricted to licensed Bahamian surveyors. |
| **legal_residency_required** | EarthScope: **No** — no nationality or residency restriction in NULA. Bahamian national CORS: unclear. |
| **last_confirmed_alive** | 2026-05-15 — EarthScope sourcetable fetched (CN13_RTCM3P3, CN14_RTCM3P3 both present, country BHS, SEPT POLARX5, GPS+GLO+BDS+GAL+SBAS+QZS, RTCM 3.3 MSM7); Spatial Dimension project page HTTP 200; Trimble Land Administration project page HTTP 404 (page removed since prior pass); bahamas.gov.bs Lands & Surveys page HTTP 403 to automated fetch. No live Bahamian government NTRIP endpoint has ever been probed; none surfaces in any public sourcetable directory. |

---

## EarthScope NOTA — COCONet Stations in Bahamas Territory

| Station | Location | Notes |
|---|---|---|
| **CN13** | San Salvador Island, central Bahamas (24.07, -74.53) | ~460 km SE of Nassau |
| **CN14** | Mathew Town, Great Inagua, southernmost Bahamas (20.98, -73.68) | ~525 km SE of Nassau |

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP). Sourcetable fetch 2026-05-15: HTTP 200, 239,923 bytes; CN13/CN14 confirmed present. |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT VRS/Network-RTK) |
| **Tariff — noncommercial** | **Free (USD $0.00)** — account + annual NULA acceptance required. Source: https://www.earthscope.org/data/gnss-realtime/ (HTTP 200, 2026-05-15) |
| **Tariff — commercial** | **USD $1,000 per seat per year** (EarthScope 501(c)(3); no VAT). Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ (HTTP 200, 2026-05-15) |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf (HTTP 200, 2026-05-15) |
| **datum_epoch** | OMIT — EarthScope distributes raw RTCM 3.3 single-base streams referenced to per-station ITRF coordinates published in the station log; no single national datum_epoch applies. |

**Practical caveat**: CN13 and CN14 are both located on outer islands far from Nassau (New Providence) and Grand Bahama, where most commercial and survey activity occurs. Nassau is ~460 km from the nearest COCONet station; single-base RTK is not viable at that distance. Users in Nassau and the northern Bahamas have no practical COCONet coverage for RTK.

**Note on legacy platform**: Old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

---

## National Surveying Authority

The **Department of Lands and Surveys** (Bahamas Government) is the responsible body for geodetic and cadastral work. NOAA NGS's CORS database lists an AUTEC (Atlantic Underwater Test and Evaluation Center) reference station in Andros, Bahamas, operated by the US Navy, but this is a US federal installation and not a Bahamian national service.

### Bahamas National CORS (Spatial Dimension / Trimble, ~2020)

A 23-station Bahamian national CORS network plus 3 tide-gauge monitoring stations was deployed for the Department of Lands and Surveys by Spatial Dimension in partnership with Trimble Inc. as part of a broader land-management modernisation programme (Trimble Pivot Platform + Landfolio cadastral software, contract awarded January 2020; project profile dated June 2020). Bahamian surveying kits for field crews were procured under the same contract. Reference: https://www.spatialdimension.com/projects/bahamas-department-of-lands-and-surveys (HTTP 200, 2026-05-15).

- **Host:port**: Not published. No public NTRIP sourcetable. bahamas.gov.bs returns HTTP 403 to automated fetch; no manual-browser inspection has surfaced a public caster URL via the Department's pages.
- **Coverage**: 23 stations across the archipelago — sufficient density (~700 km W-E, ~1,200 km N-S spread) for network RTK across populated islands if operated as VRS, but unconfirmed.
- **Hobbyist access**: Not confirmed available. The deployment is explicitly tied to cadastral/surveying modernisation under the Department of Lands and Surveys; access is most likely gated to licensed Bahamian surveyors via institutional procedure (no online self-service portal found).
- **Workaround for hobbyists**: EarthScope COCONet streams CN13/CN14 remain the only confirmed publicly accessible streams in Bahamian territory, but practical only for users on/near San Salvador and Great Inagua (>460 km from Nassau).

---

## Cross-Border Alternatives (~50 km)

None. The Bahamas archipelago is surrounded by open water. Nearest free public RTK streams in any direction are: Florida (US — NOAA NGS does not provide RTK corrections; some Florida county/state networks exist but are gated to in-state users), Cuba (no public NTRIP caster identified), and the BES Islands ~1,500 km SE (out of scope for cross-border use). No usable cross-border free RTK within practical baseline of any Bahamian island.

---

## Most Recent Project Announcement

**Bahamas Department of Lands & Surveys 23-CORS deployment (Spatial Dimension / Trimble, contract January 2020; project profile June 2020)** — https://www.spatialdimension.com/projects/bahamas-department-of-lands-and-surveys. No further public announcement of a public NTRIP service tier through 2024–2026. Trimble Land Administration project page (https://landadmin.trimble.com/projects/bahamas-land-management-system/) is now HTTP 404 (2026-05-15) — page apparently removed since the prior pass; the Spatial Dimension page remains the primary surviving public reference.

No CARICOM or regional geodetic CORS project specific to the Bahamas was identified beyond this single deployment.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive** — COCONet CN13 and CN14 RINEX | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

---

## Sources Consulted (probed 2026-05-15)
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/ — HTTP 200
- EarthScope commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ — HTTP 200
- EarthScope NULA PDF: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf — HTTP 200
- EarthScope NTRIP sourcetable: `http://ntrip.earthscope.org:2101/` — HTTP 200, CN13_RTCM3P3 + CN14_RTCM3P3 entries present, country=BHS
- COCONet site info: https://coconet.unavco.org/site-info/site-info.html — HTTP 200
- NOAA NGS CORS database: https://geodesy.noaa.gov/CORS/ — HTTP 200 (AUTEC Andros listed; US Navy installation, not Bahamian service)
- Spatial Dimension — Bahamas DLS CORS project profile: https://www.spatialdimension.com/projects/bahamas-department-of-lands-and-surveys — HTTP 200
- Trimble Land Administration — Bahamas Land Management System: https://landadmin.trimble.com/projects/bahamas-land-management-system/ — HTTP 404 (page removed)
- Bahamas.gov.bs Department of Lands and Surveys: https://www.bahamas.gov.bs/agencies/department-of-lands-and-surveys — HTTP 403 to automated fetch
- rtk2go SNIP sourcetable: `http://rtk2go.com:2101/SNIP::SOURCETABLE` — HTTP 200, no BHS/Bahamas/Nassau/Inagua/Andros/Freeport mountpoints
- Centipede-RTK public map: https://map.centipede-rtk.org/ — no Bahamian bases visible (verified via search; no BHS entries surfaced)
- NTRIP-list.com North America — no BS entry
