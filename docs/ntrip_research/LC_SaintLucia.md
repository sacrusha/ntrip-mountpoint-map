# Saint Lucia [LC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified EarthScope live page; ITRF2014 datum cite added; no national-caster change)

## Status: No national caster — EarthScope scientific streams available (two stations, co-located)

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS streams in LC territory** | Yes — EarthScope NOTA (former COCONet) CN04 and CN47, both on roof of NEMO building, Castries area; `ntrip.earthscope.org:2101` |
| **landing_url — EarthScope NOTA** | https://www.earthscope.org/data/gnss-realtime/ (operator-owned EarthScope realtime data page) |
| **access_url — EarthScope NOTA** | https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf (NULA registration document — distinct from landing page) |
| **num_stations — EarthScope NOTA (LC territory)** | 2 — CN04 (14.02 N / -60.97 E) + CN47 (13.71 N / -60.94 E), both co-located on NEMO building roof, Castries |
| **vrs — EarthScope NOTA** | no — raw 1 Hz single-base RTCM 3.3 MSM7 streams, not VRS/Network-RTK |
| **hobbyist_eligibility** | **Yes** (noncommercial tier — no surveying licence required, individual account accepted) |
| **legal_residency_required** | **No** — no nationality or residency restriction in NULA |
| **last_confirmed_alive** | 2026-05-17 — `py scripts/stations_by_country.py LCA` returns CN04 (14.02 N / -60.97 E) + CN47 (13.71 N / -60.94 E) tagged `earthscope`; EarthScope GNSS realtime landing page WebFetch HTTP 200 (2026-05-17) confirms `ntrip.earthscope.org:2101` + ITRF2014 frame. EarthScope NULA v. 2025-05-30 |
| **datum_epoch** | ITRF2014; NOTA station coordinate epoch 2026-03-30 -- operator-declared on EarthScope realtime page (cited 2026-05-17). Citation: https://www.earthscope.org/data/gnss-realtime/ ("All raw data streams use the ITRF2014 reference frame"; "epoch date is 2026-03-30" for NOTA stations) |

---

## EarthScope NOTA — COCONet Stations in Saint Lucia

| Station | Location | Installation | Notes |
|---|---|---|---|
| **CN04** | Roof of NEMO building, Saint Lucia | ~2014 (UNAVCO/NSF) | Installed in partnership with UWI and St. Lucia Ministry of Physical Development, Housing and Urban Renewal |
| **CN47** | Roof of NEMO building, Saint Lucia | February 2014 | Second monument at same NEMO building; provides redundancy |

Both CN04 and CN47 appear to be at or near the same site (NEMO headquarters, Castries region). Having two co-located monuments improves data reliability but does not extend geographic coverage. For RTK on southern Saint Lucia (Vieux Fort, Soufrière), the single-base baseline from Castries is ~30–40 km, which is at the edge of reliable cm-accuracy range.

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT VRS/Network-RTK) |
| **Tariff — noncommercial** | **Free (USD $0.00)** — account + annual NULA acceptance required. Date observed: 2026-05-17. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **Tariff — commercial** | Annual subscription "based on the number of simultaneous connections"; specific seat figure (previously reported $1,000/seat/year) no longer disclosed on the 2024-03-07 announcement page (WebFetch 2026-05-17). Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |

**Note on legacy platform**: Old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

---

## National Surveying Authority

The **Survey & Mapping Section**, Ministry of Physical Development, Housing and Urban Renewal (`govt.lc/ministries/physical-development/survey-mapping-section`), is the responsible government body for geodetic and cadastral work in Saint Lucia. The ministry collaborated with UNAVCO on the CN04/CN47 installation in 2014. No NTRIP caster, CORS endpoint, or real-time GPS correction service operated by the Survey & Mapping Section was found as of 2026-05-12. No public announcement of a planned national RTK/CORS network was found in any cadastral, World Bank, or trade-press source.

The 2022 World Bank **OECS Data for Decision Making Project** (Grenada, Saint Lucia, Saint Vincent) funded GIS and data management capacity, but contained no GNSS CORS component.

---

## Most Recent Project Announcement

None found for a dedicated Saint Lucia national CORS/NTRIP service.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive** — COCONet CN04 and CN47 RINEX | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

## Sources Consulted
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/
- EarthScope commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- UNAVCO news — COCONet CN04 and CN47 Saint Lucia installation: https://www.unavco.org/news/unavco-installs-coconet-cgps-sites-cn04-and-cn47-in-saint-lucia/
- COCONet site info: https://coconet.unavco.org/site-info/site-info.html
- Government of Saint Lucia — Survey & Mapping Section: https://www.govt.lc/ministries/physical-development/survey-mapping-section
- World Bank OECS Data for Decision Making Project: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/
- NTRIP-list.com North America — no LC entry found
- RTK2go / Centipede sourcetables — no LC stations found
- Local pipeline verification (2026-05-17): `py scripts/stations_by_country.py LCA` returns the two EarthScope `LCA` entries (CN04 14.02,-60.97 and CN47 13.71,-60.94); rtk2go/centipede return zero LC stations
- EarthScope realtime landing page (2026-05-17): WebFetch HTTP 200, declares `ntrip.earthscope.org:2101` + ITRF2014 + NOTA epoch 2026-03-30
