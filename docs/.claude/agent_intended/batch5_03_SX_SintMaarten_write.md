# Agent intended Write
- batch: batch5
- target: D:\Projects\ntrip-mountpoint-map\docs\ntrip_research\SX_SintMaarten.md
- transcript line: 233

## CONTENT (full file)

```markdown
# Sint Maarten [SX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07 (revised from 2026-05-06)

## Status: YES (revised) — Kadaster St. Maarten now offers a paid CORS reference-station subscription (XCG-priced); host:port not on public web; nearest free fallback is EarthScope CN59 on Anguilla (~20 km); Kadaster NL AGRS does NOT cover SX

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — Kadaster St. Maarten CORS subscription product. **Previous status ("no caster") revised 2026-05-07** based on price-list discovery on `kadaster.sx/services` listing "Use of CORS station per month / per year" |
| **Operator** | Stichting Kadaster- en Hypotheekwezen Sint Maarten (private foundation established 1999, official property registrar of Sint Maarten) — `kadaster.sx` |
| **Service name** | "Use of CORS station" (no marketing name — sold as a line item in the Kadaster St. Maarten service catalogue) |
| **host:port** | Not disclosed on public web (typical Caribbean-cadaster pattern: caster host, port, and credentials issued on subscription; no public sourcetable) |
| **VRS** | Unclear — Kadaster St. Maarten has not published a station count or sourcetable. The Dutch side of the island is 34 km², so even a single physical reference station ~10 km from any rover gives sub-cm VRS-equivalent baseline; whether the product is single-base RTCM3 or a VRS solution is unconfirmed |
| **tariff — monthly** | XCG 360.00 / month per receiver — approx USD 202.30 at 2026-05 cross rate (XCG = Caribbean guilder, replaced Netherlands Antillean guilder ANG in 2025, pegged 1.79 XCG ≈ 1 USD) |
| **tariff — annual** | XCG 3,600.00 / year per receiver — approx USD 2,022.50 (equivalent to 10× monthly fee — implicit 2-month / ~16.7 % annual discount) |
| **VAT/TOT status** | Sint Maarten levies TOT (Turnover Tax / Belasting op Bedrijfsomzetten / BBO) at 5 % on services. The price list does not flag whether TOT is included; verify on invoice |
| **hobbyist_eligibility** | Unclear — service catalogue describes professional cadastral / surveying clients (boundary staking out, certificates of admeasurement). No explicit individual / non-professional tier; no explicit exclusion either. Pricing is uniform per receiver |
| **legal_residency_required** | Unclear — Kadaster St. Maarten customer flow has traditionally invoiced licensed surveyors operating in SX. No published residency rule for the CORS product |
| **last_confirmed_alive** | 2026-05-07 (`kadaster.sx/services` HTTP 200 with CORS-station price line in the live price table; "Kadaster St. Maarten Now Officially GIS Ready" press confirmed 2025-07-25 GIS deployment) |

## Kadaster NL AGRS — Does NOT Cover SX

The Dutch Caribbean AGRS (Actief GNSS Referentiesysteem) caster `ntrip.kadaster.nl:2101` covers the BES special-municipality islands — Bonaire (BQ), Sint Eustatius (SE), and Saba (SA) — but **not** Sint Maarten (SX). Sint Maarten is a constituent country of the Kingdom of the Netherlands, not a Dutch municipality, and its land registry is run by an autonomous foundation (Kadaster St. Maarten), not by Kadaster Netherlands. Confirmed: no SX-coded mountpoint on `ntrip.kadaster.nl` sourcetable. See `CW_Dutch_Caribbean.md` for the BES detail.

A 2026-02 Letter of Intent between Kadaster St. Maarten and Kadaster Netherlands (BES) toward a Caribbean Cadaster Association is institutional cooperation, not an operational NTRIP merger.

## Nearest Free Option — EarthScope NOTA, Anguilla

EarthScope's Network of the Americas (NOTA) inherited the COCONet Caribbean GNSS network. Station **CN59** on Anguilla (~18.21°N, –63.05°W; country code AIA) sits ~20 km north of the Dutch–French border on St. Martin / Sint Maarten and is reachable from SX territory.

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (TCP) / `:443` (TLS) |
| **Mountpoint** | `CN59_RTCM3P3` (and similar single-base streams; sourcetable lookup at the EarthScope NOTA portal) |
| **Stream type** | Single-base RTCM 3 — not VRS. Suitable for short-baseline RTK at ~20 km |
| **Constellations** | Multi-GNSS (GPS / GLONASS / Galileo / BeiDou) on dual-frequency choke-ring class hardware |
| **tariff — noncommercial** | Free (NOAA / NSF NULA — Non-commercial Use License Agreement; account required) |
| **tariff — commercial** | USD 1,000 / seat / year (EarthScope commercial license, 2024) |
| **hobbyist_eligibility** | Yes — sign-up for an EarthScope user account, accept NULA, request real-time access |
| **legal_residency_required** | No (international free service) |

## Context Notes

- **Two-country island**: Saint Martin / Sint Maarten is split between French Saint Martin (MF, north) and Dutch Sint Maarten (SX, south). Total area ~87 km², SX side ~34 km². Neither side has a free public NTRIP service. French side has no free RTK caster either; the IGN-FI RGAF09 framework is referenced as a datum but has no real-time CORS in the Antilles operating publicly.
- **Kadaster St. Maarten, 2025 GIS-ready**: A 2025-07-25 press release confirmed the Foundation deployed an in-house ArcGIS Enterprise + ArcGIS Pro + Drone2Map platform with on-prem infrastructure, partnered with GIS4C B.V. The CORS-station product appears alongside drone-mapping and "field GNSS into parcel fabric" workflows in their 2025–2026 service expansion. The Foundation also signaled it would introduce drone-based mapping and aerial data collection "in the coming months" (as of mid-2025).
- **e-VROMI** (Government of Sint Maarten, Dec 2024 / Aug 2025): A USD-12-million Trust-Fund-backed project deploying ArcGIS for national address management. Project handles GIS workflows but does not operate a public NTRIP caster.
- **Volunteer**: zero rtk2go bases for SX, zero Centipede nodes (cross-checked 2026-05-07 via station coordinates filtered to 18.0–18.2°N / –63.2–−63.0°W bounding box).
- **No IGS station** on the island; nearest IGS sites are ABMF (Guadeloupe, ~250 km south) and CRO1 (St. Croix USVI, ~280 km west) — too far for RTK, suitable for PPP/PPK.
- **Practical recommendation**:
  1. **Free path**: EarthScope CN59 (Anguilla, ~20 km) for noncommercial RTK. Pre-condition: NULA-license-compatible use case.
  2. **Paid SX-domestic path**: Kadaster St. Maarten CORS subscription at XCG 3,600 / yr (~USD 2,000) — high price for hobbyists; product targets professional surveyors operating on-island.
  3. **Self-deployed base**: a u-blox F9P or Trimble single-board on a clear-sky rooftop on the Dutch side, with rtk2go relay for short-baseline RTK to oneself, costs <USD 500 hardware and is competitive with one year of Kadaster SX subscription.

## Most Recent Project Announcement

- **2025-07-25**: "Kadaster St. Maarten Now Officially GIS Ready" — deployment of in-house GIS infrastructure (ArcGIS Enterprise / Pro / Drone2Map) and announcement of upcoming drone-based mapping. The CORS-station product visible on the public services page postdates this milestone.
  Sources: https://www.721news.com/2025/07/kadaster-st-maarten-now-officially-gis-ready/ ; https://www.soualiganewsday.com/index.php?option=com_k2&view=item&id=62154

- **2026-02**: Kadaster St. Maarten and Kadaster Netherlands signed a Letter of Intent toward a Caribbean Cadaster Association (CCA). Cadastral-cooperation focus; no NTRIP infrastructure component.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope NOTA — CN59 (Anguilla)** | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (NULA + account) |
| **IGS — ABMF Guadeloupe / CRO1 USVI** | https://cddis.nasa.gov/ | Free (Earthdata account) |
| **Kadaster St. Maarten — historic RINEX archive** | https://kadaster.sx/services/ | Pricing unclear; line items refer to monthly / annual CORS access; archive product not separately listed |

## Sources Consulted

- Kadaster St. Maarten — Services & price list: https://kadaster.sx/services/ — confirmed price lines "Use of CORS station per month: XCG 360.00 / USD 202.30" and "Use of CORS station per year: XCG 3,600.00 / USD 2,022.50" (observed 2026-05-07)
- Kadaster St. Maarten — home: https://kadaster.sx/ (foundation, 1999 establishment; no GNSS detail on home page)
- Kadaster St. Maarten — about: https://kadaster.sx/about/ (foundation profile)
- "Kadaster St. Maarten Now Officially GIS Ready" — 721news.com (2025-07-25): https://www.721news.com/2025/07/kadaster-st-maarten-now-officially-gis-ready/
- "Kadaster St. Maarten Now Officially GIS Ready" — Soualiga Newsday: https://www.soualiganewsday.com/index.php?option=com_k2&view=item&id=62154
- Spatial Dimension — Sint Maarten Kadaster Landfolio project: https://www.spatialdimension.com/projects/sint-maarten-kadaster (no GNSS RTK detail)
- Government of Sint Maarten — e-VROMI project announcement: https://www.sintmaartengov.org/news/pages/Government-Launches-e-VROMI-Project-with-ArcGIS-Software-to-Revolutionize-National-Address-Management-and-Digital-Transform.aspx
- St. Maarten Open Data (GIS / VROMI portal): https://gis-vromi-sxm.opendata.arcgis.com/
- Caribbean Cadaster Association LOI (Feb 2026): https://www.721news.com/2026/02/kadaster-st-maarten-and-kadaster-netherlands-bes-advance-regional-cooperation-with-letter-of-intent-for-caribbean-cadaster-association/
- EarthScope NOTA real-time GNSS portal: https://www.earthscope.org/data/gnss-realtime/ ; transition to new platform: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- EarthScope licensing / NULA + USD 1,000 commercial seat: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- CW_Dutch_Caribbean.md (companion file confirming AGRS BES coverage and SX exclusion)

```
