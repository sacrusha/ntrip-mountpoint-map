# Suriname [SR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-probed; prior: 2026-05-17 / 2026-05-13)

## Status: YES — MI-GLIS national CORS network with NTRIP subscription; paid since 2024-07-01; quote-based pricing, no published tariff; eligibility appears professional/institutional

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | MI-GLIS — Management Instituut voor Grondregistratie en Land Informatie Systeem (`miglis.sr`); Suriname land-registry / cadastral authority, under the Ministerie van Grond- en Bosbeheer (Ministry of Land and Forest Management) |
| **Service name** | MI-GLIS CORS Services |
| **host:port** | Not published on the public web. Issued by email after a subscription contract is signed. Raw-data portal at `corsruwedata.miglis.sr` (login-gated; TCP-connect refused from this sandbox 2026-05-13) |
| **mountpoint(s)** | Not published; presumably one mountpoint per CORS station (8 stations) and/or a VRS mountpoint — unconfirmed |
| **stream type** | RTK / single-base RTCM 3.x from each physical CORS |
| **vrs** | ? — not stated publicly. With 8 CORS spread across the coastal strip and interior mines, a network-RTK / VRS product is geometrically possible (some inter-station baselines exceed 70 km in the interior, e.g. Brokopondo–Merian, which limits VRS quality), but no operator declaration of a VRS / NRTK mountpoint was found on `miglis.sr` or in the application material |
| **num_stations** | 8 physical CORS (see table below) |
| **constellations** | Trimble Zephyr Geodetic antennas; mix of Trimble receivers (mainly NetR9/NetR5 class hardware on station photos) — multi-GNSS hardware, exact constellation list not published |
| **datum** | ITRF00 (operator notation; standard reading is ITRF2000 — the 2000 realization is commonly written "ITRF00") |
| **datum_epoch** | cited https://miglis.sr/cors-data-stations/ — ITRF00; epoch not declared by operator (operator portal lists "Datum: ITRF00" inline next to the 8-station table; no epoch shown) |
| **tariff — published** | No public tariff. Subscription requested by emailing `corsserver@miglis.sr` with: completed CORS-services application form (`AANVRAAGFORMULIER CORS DIENSTEN MI-GLIS`) and an N-formulier (instrument-registration form). After approval the customer signs a contract with a chosen package and receives NTRIP credentials |
| **tariff — known fragments** | Re-opening a closed account: **USD 25.00** (carried from prior research file; not re-located on `miglis.sr/cors-data-stations/`, `miglis.sr/diensten/`, `miglis.sr/tarieven/` (2021-04 PDF), or the application-form PDF on 2026-05-22 — likely sourced from an emailed quote, not public web). Invoicing reported in Surinamese Dollar (SRD) at the weekly Central Bank of Suriname exchange rate, valid 14 business days from invoice issue. Specific monthly / annual / per-station rates not on the public web on 2026-05-22 |
| **VAT** | Suriname BTW (VAT) currently 10 % on most services (rate confirmed in Belastingdienst SR schedule) — not separately broken out in the price fragments seen |
| **hobbyist_eligibility** | ? — application form is `TBV OVERIGE INSTANTIES` (For Other Institutions). The form, the contract requirement, and the N-formulier (instrument registration) all point to a professional/institutional flow. No public hobbyist tier; nothing explicitly bars an individual from applying, but the workflow is not designed for one-off use |
| **legal_residency_required** | ? — Suriname-based contract law applies (SRD invoicing, Surinamese banking). No explicit residency rule on the public site, but in practice an SRD-billed contract requires a local point of payment |
| **registration** | Email `corsserver@miglis.sr`. Application form (PDF): `https://miglis.sr/wp-content/uploads/2023/08/AANVRAAGFORMULIER-CORS-DIENSTEN-MI-GLIS-TBV-OVERIGE-INSTANTIES.pdf` |
| **last_confirmed_alive** | 2026-05-21 — `miglis.sr/cors-data-stations/` HTTP 200; 8-station table + "Datum: ITRF00" + NTRIP application instructions (`corsserver@miglis.sr`) all unchanged from 2026-05-13. `corsruwedata.miglis.sr` remains login-gated |

## MI-GLIS CORS Stations (8)

| Code | Location | Host site | Easting | Northing | Height (m) |
|---|---|---:|---:|---:|---:|
| PMB1 | Paramaribo | Maritime Authority | 705405.696 | 644546.816 | -29.234 |
| SRZN | Zanderij | Johan Adolf Pengel Int'l Airport | 699085.163 | 603327.531 | -17.067 |
| SRBR | Brokopondo | Telesur substation | 723871.246 | 559597.099 | 27.548 |
| SRTK | Tijgerkreek | Telesur substation | 656676.670 | 646146.332 | -24.622 |
| SRMM | Nassau / Merian | Newmont (Merian mine) | 771708.743 | 565483.678 | 62.074 |
| SRHR | Nickerie / Henarpolder | Telesur substation | 512338.242 | 647221.429 | -19.567 |
| SRTS | Coronie / Totness | Telesur (Soemboredjo) | 574399.950 | 648841.012 | -22.763 |
| SRMG | Marowijne / Moengo | Telesur Moengo | 787443.548 | 622125.708 | -13.162 |

Coordinates are in UTM Zone 21N on the local Suriname datum projection (per the MI-GLIS station page). All stations on ITRF00. Coverage spans the populated Atlantic coastal strip from Nickerie in the west to Moengo in the east plus the interior mining areas at Brokopondo and Merian; the largely unpopulated southern interior (Sipaliwini) is not covered.

## Most Recent Project Announcement

**2024-07-01** — MI-GLIS officially began charging for CORS services (transition from a free pilot phase that ran since the network's modernisation in the late 2010s). Subscription must be applied for in advance via `corsserver@miglis.sr`.

(IDB project SU-L1067 — Spatial Planning Suriname — signed Dec 2024 is land-planning and environmental management; no documented GNSS/CORS component.)

## Context Notes

- **MI-GLIS** (Management Instituut voor Grondregistratie en Land Informatie Systeem, `miglis.sr`): public/private institute reporting to the Ministerie van Grond- en Bosbeheer, runs the land registration and the national CORS network. Contact: `info@miglis.sr` / `corsserver@miglis.sr` / `finance@miglis.sr`; phone +597-403783.
- **NTRIP discovery**: the MI-GLIS service page explicitly mentions "NTRIP account" delivery after approval, confirming this is a real-time NTRIP caster — not RINEX-only as the previous research file stated.
- **Application workflow**: completed CORS-services application form (PDF on `miglis.sr/wp-content/uploads/2023/08/AANVRAAGFORMULIER-CORS-DIENSTEN-MI-GLIS-TBV-OVERIGE-INSTANTIES.pdf`) + N-formulier (instrument registration); reply by MI-GLIS with contract and NTRIP credentials.
- **rtk2go / Centipede / EarthScope**: 0 SR-coded stations on rtk2go or Centipede; 0 EarthScope NOTA station within 600 km of Paramaribo. The nearest public-aggregator stations are in French Guiana — KOUG00GUF0 (AUSCORS rebroadcast, 295 km) and CYNE00GUF0 (BKG IGS-IP, 333 km) — both far beyond RTK baseline. (`py scripts/stations_by_radius.py 5.85 -55.2 600` 2026-05-21.)
- **Cross-border alternatives within ~50 km**: none. Brazilian RBMC-IP nearest stations ~700–900 km from Paramaribo. French Guiana hosts KOUG (Kourou) and CYNE (Cayenne) physical CORS rebroadcast by AUSCORS / IGS-IP, but distances to Paramaribo are 295 / 333 km — far beyond RTK baseline.
- **SIRGAS-CON**: Suriname has at least one static GNSS monument processed by IBGE's SIRGAS-CON analysis centre — **post-processing RINEX only**, not a public NTRIP RTK stream. The MI-GLIS CORS network is operationally separate from the SIRGAS-CON archived monument(s).
- **GISsat NV** (Esri/Trimble distributor in Suriname): resells Trimble Catalyst (PPP/SSR) and is not the MI-GLIS caster operator.
- **No commercial network** (GEODNET, ONOCOY, HxGN SmartNet, Topcon NetG5/TopNET, Trimble VRS Now, Centipede-RTK, RTKdata) has confirmed SR coverage.
- **Practical recommendation for hobbyists**:
  1. Apply via `corsserver@miglis.sr` — pricing is quote-only, and the workflow is geared to institutions, so be prepared to be re-quoted or refused for individual non-survey use.
  2. **Self-deployed base**: u-blox F9P / Septentrio Mosaic on a clear-sky rooftop in Paramaribo is the cheapest cm-accuracy path for a Surinamese hobbyist (no national volunteer caster exists, so an rtk2go push from your own base is the route).
  3. **PPP-only**: Galileo HAS (free, ~25–40 cm horizontal) and Trimble RTX (paid, sub-decimetre) work everywhere in Suriname without an NTRIP subscription.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **MI-GLIS CORS raw-data portal** | https://corsruwedata.miglis.sr/ (login-gated) | Same subscription as NTRIP (see tariff fragments above) |
| **EarthScope GNSS Data Archive** / SIRGAS-CON for the Suriname static monument(s) processed by IBGE | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); USD 1,000/seat/yr commercial |

## Sources Consulted

- MI-GLIS CORS stations page (8-station table, NTRIP workflow, "Datum: ITRF00"): https://miglis.sr/cors-data-stations/ — HTTP 200 confirmed 2026-05-21
- MI-GLIS CORS application form (PDF): https://miglis.sr/wp-content/uploads/2023/08/AANVRAAGFORMULIER-CORS-DIENSTEN-MI-GLIS-TBV-OVERIGE-INSTANTIES.pdf
- MI-GLIS tariffs page (links 2021-04 tariff PDF; PDF downloaded and parsed with pdftotext 2026-05-22 — contents enumerate items 1–63 incl. GPS rover/operator rental but contain no NTRIP / CORS subscription line. PDF predates 2024-07-01 paid-NTRIP switch and has not been re-issued.): https://miglis.sr/tarieven/
- MI-GLIS services overview: https://miglis.sr/diensten/
- MI-GLIS homepage: https://miglis.sr/
- MI-GLIS CORS map (ArcGIS Online): https://www.arcgis.com/apps/mapviewer/index.html?webmap=bcb159ff6cd545959df359d20d59fb84
- MI-GLIS Twitter / X (`@MIGLISSURINAME`): https://x.com/miglissuriname
- Ministerie van Grond- en Bosbeheer / MI-GLIS section: https://gov.sr/ministeries/ministerie-van-grond-en-bosbeheer/mi-glis/
- Cross-aggregator coverage check 2026-05-21 (`py scripts/stations_by_country.py SUR` returns no stations; `py scripts/stations_by_radius.py 5.85 -55.2 600` returns 2 GUF-tagged stations 295 / 333 km away)
- IDB projects SU-T1146 / SU-L1067 — no GNSS/CORS component
- SIRGAS station list, IGS Real-Time Service, NTRIP-list.com South America — no additional Suriname caster
- HxGN SmartNet, GEODNET, ONOCOY, Centipede-RTK, RTKdata, Trimble VRS Now, ArduSimple country directory — no Suriname coverage (2026-05 searches)
