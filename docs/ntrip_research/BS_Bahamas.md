# Bahamas [BS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior: 2026-05-17)

## Status

A national 23-station Trimble CORS network plus 3 tide-gauges was deployed by Spatial Dimension and Trimble for the Department of Lands & Surveys (contract January 2020; project profile June 2020). No public NTRIP host:port, sourcetable, or self-service registration portal has been published; access policy is not stated on either operator-side page (Spatial Dimension or `bahamas.gov.bs`). EarthScope NOTA scientific streams remain the only publicly accessible NTRIP product in Bahamian territory, and they sit on outer islands (CN13 San Salvador, CN14 Great Inagua) far from any populated area.

| Field | Value |
|---|---|
| National NTRIP RTK caster | Physical infrastructure exists (23 Trimble CORS + 3 tide gauges, Bahamas Department of Lands & Surveys, Spatial Dimension / Trimble deployment ~2020) — no public host:port, sourcetable, or self-service registration portal. Platform is Trimble Pivot (RTK/VRS-capable); if operational it is gated for licensed Bahamian surveyors via Lands & Surveys. |
| Scientific GNSS streams in BS territory | Yes — EarthScope NOTA `CN13` (San Salvador) and `CN14` (Mathew Town, Great Inagua); both on `ntrip.earthscope.org:2101` |
| landing_url | N/A for national caster (no public landing page). EarthScope NOTA: https://www.earthscope.org/data/gnss-realtime/ |
| access_url | N/A for national caster (no public access portal). EarthScope NOTA: https://data.earthscope.org/ |
| host:port | N/A for national caster (not published). EarthScope NOTA: `ntrip.earthscope.org:2101` |
| num_stations | National caster: 23 Trimble CORS + 3 tide-gauges (physical; not publicly streamed). EarthScope NOTA in BHS territory: 2 (CN13, CN14) |
| vrs | National caster: unknown (Trimble Pivot is VRS-capable, no operator confirmation). EarthScope NOTA: No — single-base raw RTCM 3.3 MSM7 |
| hobbyist_eligibility | EarthScope: yes (noncommercial NULA — individual account accepted). Bahamian national CORS: unclear — no published policy, likely restricted to licensed Bahamian surveyors. |
| legal_residency_required | EarthScope: no. Bahamian national CORS: unclear. |
| last_confirmed_alive | 2026-05-21 — EarthScope NTRIP `ntrip.earthscope.org:2101` `SOURCETABLE 200 OK` (curl); pipeline `py scripts/stations_by_country.py BHS` confirms 2 stations (CN13, CN14). Spatial Dimension project page HTTP 200. Trimble Land Administration page (`landadmin.trimble.com/projects/bahamas-land-management-system/`) still HTTP 404. `bahamas.gov.bs` Department of Lands & Surveys page HTTP 403 to automated fetch. No live Bahamian government NTRIP endpoint has ever been probed; none surfaces in any public sourcetable directory. |

## EarthScope NOTA — COCONet stations in Bahamas territory

| Station | Location | Notes |
|---|---|---|
| CN13 | San Salvador Island, central Bahamas (24.07, -74.53) | ~460 km SE of Nassau |
| CN14 | Mathew Town, Great Inagua, southernmost Bahamas (20.98, -73.68) | ~525 km SE of Nassau |

| Field | Value |
|---|---|
| host:port | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) — `SOURCETABLE 200 OK` 2026-05-21 |
| Stream type | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT VRS / Network-RTK) |
| Tariff — noncommercial | Free (USD $0.00) — account + annual NULA acceptance required. Source: https://www.earthscope.org/data/gnss-realtime/ |
| Tariff — commercial | USD $1,000 per seat per year (EarthScope 501(c)(3); no VAT). Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| NULA version | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |
| datum_epoch | ITRF2014, epoch 2026-03-30 (declared on operator portal: "All raw data streams use the ITRF2014 reference frame. For NOTA stations, the epoch date is 2026-03-30") — applies to CN13/CN14 as NOTA/COCONet stations. FAQ does not state whether the date is fixed for the lifetime of the stream or refreshed as NOTA positions are reprocessed. |

**Practical caveat**: CN13 and CN14 are both located on outer islands far from Nassau (New Providence) and Grand Bahama, where most commercial and survey activity occurs. Nassau is ~460 km from the nearest COCONet station; single-base RTK is not viable at that distance. Users in Nassau and the northern Bahamas have no practical COCONet coverage for RTK.

**Note on legacy platform**: Old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

## National Surveying Authority

The **Department of Lands and Surveys** (Bahamas Government) is the responsible body for geodetic and cadastral work. NOAA NGS's CORS database lists an AUTEC (Atlantic Underwater Test and Evaluation Center) reference station in Andros, Bahamas, operated by the US Navy. This is a US federal installation, not a Bahamian national service; NOAA NCN itself is post-processing RINEX only and does not run a public NTRIP caster (per NCN FAQ), so AUTEC is not a real-time RTK option regardless of operator. No rtk2go / EarthScope / IGS NTRIP mountpoint for AUTEC has been observed in any public sourcetable.

### Bahamas National CORS (Spatial Dimension / Trimble, ~2020)

A 23-station Bahamian national CORS network plus 3 tide-gauge monitoring stations was deployed for the Department of Lands and Surveys by Spatial Dimension in partnership with Trimble Inc. as part of a broader land-management modernisation programme (Trimble Pivot Platform + Landfolio cadastral software, contract awarded January 2020; project profile dated June 2020). Bahamian surveying kits for field crews were procured under the same contract.

- **Host:port**: Not published. No public NTRIP sourcetable. `bahamas.gov.bs` returns HTTP 403 to automated fetch; no manual-browser inspection has surfaced a public caster URL via the Department's pages.
- **Coverage**: 23 stations across an archipelago spanning ~700 km W-E and ~1,200 km N-S. Even distribution would put mean station spacing well above the ~70 km VRS effectiveness threshold from the primer, so a single national VRS across all of the Bahamas is geometrically implausible; densification on individual island groups (e.g. New Providence, Grand Bahama, Abacos) would be required for effective NRTK. The Spatial Dimension project page does not break the 23-station list down by island, so the actual per-island density is unknown.
- **Hobbyist access**: Not confirmed available. The deployment is explicitly tied to cadastral / surveying modernisation under the Department of Lands and Surveys; access is most likely gated to licensed Bahamian surveyors via institutional procedure (no online self-service portal found).
- **Workaround for hobbyists**: EarthScope COCONet streams CN13 / CN14 remain the only confirmed publicly accessible streams in Bahamian territory, but practical only for users on / near San Salvador and Great Inagua (>460 km from Nassau).

## Cross-Border Alternatives (~50 km)

None practical. The Bahamas archipelago is surrounded by open water. Nearest free public RTK streams are: Florida (US — NOAA NGS does not provide RTK corrections; some Florida county / state networks exist but are gated to in-state users), Cuba (no public NTRIP caster identified — institutionally gated GEOCUBA service), and the Turks & Caicos Islands (~150 km SE of Great Inagua; no public NTRIP service identified for TCA either — searches return no rtk2go / EarthScope / IGS Caicos mountpoints). GEODNET coverage map shows no Bahamas-side stations as of 2026-05-21. No usable cross-border free RTK within practical baseline of any Bahamian island.

## Most Recent Project Announcement

- **Bahamas Department of Lands & Surveys 23-CORS deployment** (Spatial Dimension / Trimble; contract January 2020; project profile June 2020) — https://www.spatialdimension.com/projects/bahamas-department-of-lands-and-surveys (page fetched and read 2026-05-21: confirms "a 23-station CORS was implemented" plus 3 tide-gauge monitoring stations, in partnership with Trimble; intended use is "management of Crown Lands, Leases and other transaction types" and the contract also delivered surveying/GPS kits for survey crews; the page does NOT publish deployment dates, an NTRIP host, or any mention of VRS/public access). No further public announcement of a public NTRIP service tier through 2024-2026.
- Trimble Land Administration project page (https://landadmin.trimble.com/projects/bahamas-land-management-system/) was HTTP 404 on 2026-05-15 and remains HTTP 404 on 2026-05-21; the Spatial Dimension page remains the primary surviving public reference.
- No CARICOM or regional geodetic CORS project specific to the Bahamas was identified beyond this single deployment.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| EarthScope GNSS Data Archive — COCONet CN13 and CN14 RINEX | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); USD 1,000/seat/yr commercial |

## Sources

- EarthScope GNSS real-time data: https://www.earthscope.org/data/gnss-realtime/ — HTTP 200, 2026-05-21
- EarthScope commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ — HTTP 200
- EarthScope NULA PDF: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf
- EarthScope NTRIP sourcetable: `ntrip.earthscope.org:2101` — curl 2026-05-21, SOURCETABLE 200 OK
- COCONet site info: https://coconet.unavco.org/site-info/site-info.html
- NOAA NGS CORS database: https://geodesy.noaa.gov/CORS/ (AUTEC Andros listed; US Navy installation, not Bahamian service)
- Spatial Dimension — Bahamas DLS CORS project profile: https://www.spatialdimension.com/projects/bahamas-department-of-lands-and-surveys — HTTP 200
- Trimble Land Administration — Bahamas Land Management System: https://landadmin.trimble.com/projects/bahamas-land-management-system/ — HTTP 404 (page removed)
- Bahamas.gov.bs Department of Lands and Surveys: https://www.bahamas.gov.bs/agencies/department-of-lands-and-surveys — HTTP 403 to automated fetch
- rtk2go SNIP sourcetable: `http://rtk2go.com:2101/SNIP::SOURCETABLE` — no BHS / Bahamas / Nassau / Inagua / Andros / Freeport mountpoints in project archive
- Centipede-RTK public map: https://map.centipede-rtk.org/ — no Bahamian bases visible
- NTRIP-list.com North America — no BS entry
