# Sint Maarten [SX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-probed; prior: 2026-05-17 / 2026-05-07)

## Status: YES — Kadaster St. Maarten sells paid CORS access (XCG-priced); host:port not public; nearest free fallback is EarthScope CN59 on Anguilla (~20 km); Kadaster NL AGRS.BES does NOT cover SX

| Field | Value |
|---|---|
| **landing_url** | https://kadaster.sx/ |
| **access_url** | https://kadaster.sx/services/ (price list; subscription via `registry@kadaster.sx` — no self-service portal) |
| **Operator** | Stichting Kadaster- en Hypotheekwezen Sint Maarten (foundation established 1999, official property registrar of Sint Maarten) |
| **Service name** | "Use of CORS station" (line item in the public services catalogue; no marketing brand) |
| **host:port** | Not disclosed on public web. `kadaster.sx:2101` times out (CDN-fronted, no NTRIP listener; curl probe 2026-05-22, 8 s timeout). Obvious subdomains `ntrip.kadaster.sx` and `cors.kadaster.sx` do not resolve (DNS NXDOMAIN, 2026-05-22). Typical Caribbean-cadaster pattern: caster host, port, and credentials issued post-subscription; no public sourcetable. |
| **num_stations** | Unknown — operator has not published a station count or sourcetable |
| **vrs** | ? — not declared (Dutch-side area 34 km² — a single base ~10 km from any rover already gives short-baseline RTK; service mode not disclosed) |
| **tariff** | Per receiver: **XCG 360.00 / month** (≈ USD 202.30) or **XCG 3,600.00 / year** (≈ USD 2,022.50) — observed inline on `kadaster.sx/services/` 2026-05-21. Annual = 10× monthly (implicit 2-month, ~16.7% discount). USD figures stated on the page imply ~1.78 XCG/USD versus the official 1.79 XCG/USD peg (Central Bank of Curaçao & Sint Maarten) — penny-rounding by the operator. |
| **VAT/TOT** | Sint Maarten levies BBO/TOT at 5% on services (rate confirmed via Sint Maarten gov / HBN Tax 2025-2026). Page does not state whether the XCG price is gross or net; verify on invoice. |
| **hobbyist_eligibility** | ? — catalogue contextualises CORS access alongside professional cadastral services (boundary staking, admeasurement certificates). No explicit individual tier, no explicit exclusion. Uniform per-receiver pricing. |
| **legal_residency_required** | ? — no published rule; subscription invoiced in XCG, and customer flow has traditionally targeted licensed SX surveyors |
| **last_confirmed_alive** | 2026-05-21 — `kadaster.sx/services/` HTTP 200 (Server: cloudflare); CORS price lines re-read (XCG 360.00/mo + XCG 3,600.00/yr, USD 202.30 / 2,022.50). |
| **datum_epoch** | omitted — no operator declaration. Kadaster SX service catalogue lists the CORS line item without frame/epoch; not citable per primer rule. |

## Kadaster NL AGRS.BES — Does NOT Cover SX

AGRS.BES (`ntrip.kadaster.nl:2101`) serves Bonaire / Sint Eustatius / Saba — the BES *special municipalities* — only. Sint Maarten is a constituent country, not a Dutch municipality; its land registry is run by an autonomous foundation. Confirmed: no SX-coded mountpoint on the `ntrip.kadaster.nl` sourcetable (curl probe 2026-05-21). See `BQ_Bonaire.md` for AGRS.BES detail.

A 2026-02 Letter of Intent between Kadaster St. Maarten and Kadaster Netherlands toward a Caribbean Cadaster Association is institutional cooperation only, not an NTRIP merger.

## Nearest Free Options

EarthScope's Network of the Americas (NOTA, ex-COCONet) station **CN59** on Anguilla (~18.21°N, –63.05°W; country tag AIA) sits ~16 km north of the Dutch border on St. Martin / Sint Maarten — the only free RTK source within practical single-base RTK range of SX.

Additional free streams within ~75 km of the centre of SX (`py scripts/stations_by_radius.py 18.07 -63.05 100` 2026-05-22) but **beyond typical single-base RTK baseline** (>30 km):

- **CN58_RTCM3P3** — EarthScope Anguilla, 18.59°N, –63.43°W, ~70 km from SX. Second Anguilla NOTA station; not preferred over CN59 (15.6 km vs 70 km).
- **SABY00BES0 / SABY0** — AGRS.BES Saba, 17.65°N, –63.22°W, ~50 km from SX. Free, anonymous, multi-constellation RTCM 3.3 on `ntrip.kadaster.nl:2101` (see `BQ_Bonaire.md`).
- **SEUS00BES0 / SEUS0** — AGRS.BES Sint Eustatius, 17.50°N, –62.98°W, ~64 km from SX. Free, anonymous, multi-constellation RTCM 3.3.

These three additional free options are listed for completeness; CN59 is the only one inside the clean <30 km single-base RTK envelope for SX.

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3 streams) — `:443` TLS is generic NTRIP convention, not separately documented on EarthScope's portal |
| **Mountpoint** | `CN59_RTCM3P3` (single-base RTCM 3.3) |
| **Stream type** | Single-base RTCM 3.3 — not VRS |
| **tariff — noncommercial** | Free under EarthScope NULA (account required) |
| **tariff — commercial** | USD 1,000 / seat / year (EarthScope commercial license, page observed 2026-05-21) |
| **hobbyist_eligibility** | Yes — NULA covers scientific / educational / humanitarian / hobbyist use |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-21 — CN59_RTCM3P3 returned by `py scripts/stations_by_radius.py 18.07 -63.05 50` at 15.6 km, AIA tag (project EarthScope snapshot) |
| **datum_epoch** | ITRF2014 (NOTA frame; epoch declared as 2026-03-30 with "best estimates" caveat for some stations) — https://www.earthscope.org/data/gnss-realtime/ |

## Context Notes

- **Two-country island**: Saint Martin / Sint Maarten is split between French Saint Martin (MF, north, ~53 km²) and Dutch Sint Maarten (SX, south, ~34 km²). French side has no free RTK caster either; IGN-FI RGAF09 is the framework datum but no public real-time CORS operates in the Antilles.
- **Kadaster St. Maarten, 2025 GIS-ready**: A 2025-07-25 press release reported the Foundation deployed an in-house ArcGIS Enterprise + ArcGIS Pro + Drone2Map platform on-prem, partnered with GIS4C B.V. The CORS-station product visible on the public services page postdates this milestone.
- **e-VROMI** (Government of Sint Maarten, Dec 2024 / Aug 2025): USD 12 million Trust-Fund project deploying ArcGIS for national address management. GIS workflows only — no public NTRIP caster.
- **2026-02 LOI**: Kadaster St. Maarten + Kadaster NL signed a Letter of Intent toward a Caribbean Cadaster Association (CCA). Institutional cooperation; no NTRIP infrastructure component.
- **Volunteer / community casters**: zero rtk2go bases for SX, zero Centipede nodes (cross-checked 2026-05-22; `py scripts/stations_by_radius.py 18.07 -63.05 100` returns 8 stations within 100 km — 2 EarthScope on Anguilla, 4 AGRS.BES on Saba/Sint Eustatius, 2 IGS-IP relays of the same AGRS.BES antennas; none in SX or French Saint Martin).
- **No IGS / BKG station on-island**; nearest IGS sites are ABMF (Guadeloupe, ~250 km S) and CRO1 (St. Croix USVI, ~280 km W) — beyond RTK range, usable only for PPP/PPK.
- **Practical recommendation**:
  1. **Free path**: EarthScope CN59 (Anguilla, ~20 km), NULA non-commercial.
  2. **Paid SX-domestic**: Kadaster St. Maarten CORS at XCG 3,600/yr (~USD 2,000) — targets on-island professionals.
  3. **Self-deployed base**: u-blox F9P / Septentrio Mosaic on a clear-sky Dutch-side rooftop + rtk2go push covers short-baseline RTK for under USD 500 hardware (less than one Kadaster SX year).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope NOTA — CN59 (Anguilla)** | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (NULA + account) |
| **IGS — ABMF Guadeloupe / CRO1 USVI** | https://cddis.nasa.gov/ | Free (Earthdata account) |
| **Kadaster St. Maarten — historic RINEX archive** | https://kadaster.sx/services/ | Pricing unclear; line items refer to monthly / annual CORS access; archive product not separately listed |

## Sources Consulted

- Kadaster St. Maarten — services + price list (HTTP 200 2026-05-21; "Use of CORS station per month: XCG 360.00 / USD 202.30", "per year: XCG 3,600.00 / USD 2,022.50"): https://kadaster.sx/services/
- Kadaster St. Maarten — home / about: https://kadaster.sx/ + https://kadaster.sx/about/
- 721news — "Kadaster St. Maarten Now Officially GIS Ready" (2025-07-25): https://www.721news.com/2025/07/kadaster-st-maarten-now-officially-gis-ready/
- Soualiga Newsday — same announcement: https://www.soualiganewsday.com/index.php?option=com_k2&view=item&id=62154
- Spatial Dimension — Sint Maarten Kadaster Landfolio project (no GNSS RTK): https://www.spatialdimension.com/projects/sint-maarten-kadaster
- Sint Maarten Government — e-VROMI launch: https://www.sintmaartengov.org/news/pages/Government-Launches-e-VROMI-Project-with-ArcGIS-Software-to-Revolutionize-National-Address-Management-and-Digital-Transform.aspx
- St. Maarten Open Data / VROMI portal: https://gis-vromi-sxm.opendata.arcgis.com/
- Caribbean Cadaster Association LOI (Feb 2026): https://www.721news.com/2026/02/kadaster-st-maarten-and-kadaster-netherlands-bes-advance-regional-cooperation-with-letter-of-intent-for-caribbean-cadaster-association/
- EarthScope NOTA realtime portal (host, ports, NULA, ITRF2014): https://www.earthscope.org/data/gnss-realtime/
- EarthScope platform transition (legacy retired 2025-07-29; mountpoint rename): https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- EarthScope commercial licensing USD 1,000 / seat / yr: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- Central Bank of Curaçao & Sint Maarten — XCG = Caribbean guilder, fixed peg 1.79 XCG = 1 USD: https://www.centralbank.cw/functions/banknotes-coins/caribbean-guilder
- HBN Law & Tax — Sint Maarten 5% BBO/TOT on services: https://hbnlawtax.com/tax-instant-news/end-of-the-year-tax-alerts-sint-maarten-3/
- AGRS.BES sourcetable cross-check (no SX mountpoints; curl probe 2026-05-21): http://ntrip.kadaster.nl:2101/
- kadaster.sx:2101 NTRIP probe (2026-05-22) — TCP connect timed out (CDN-fronted, no NTRIP listener). `ntrip.kadaster.sx` and `cors.kadaster.sx` — DNS NXDOMAIN.
- Companion: `BQ_Bonaire.md` (AGRS.BES detail)
