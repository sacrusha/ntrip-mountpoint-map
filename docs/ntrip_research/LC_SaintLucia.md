# Saint Lucia [LC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: No national caster — EarthScope NOTA streams two co-located scientific stations

| Field | Value |
|---|---|
| National NTRIP RTK caster | No |
| Public scientific caster in LC | EarthScope NOTA (former COCONet) — `ntrip.earthscope.org:2101` |
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://www.earthscope.org/data/gnss-realtime/ (sign-up flow + license terms on same page) |
| host:port | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) |
| num_stations | 2 — CN04 (14.02, -60.97) on NEMO building rooftop, Castries; CN47 (13.71, -60.94) at Vieux Fort Lighthouse (southernmost tip of island, ~34 km south of CN04) |
| vrs | No — raw 1 Hz multi-constellation RTCM 3.3 MSM7 single-base streams |
| tariff — noncommercial | Free (USD $0.00); EarthScope account + annual NULA acceptance required. Observed 2026-05-22. Source: https://www.earthscope.org/data/gnss-realtime/ |
| tariff — commercial | USD $1,000 per seat per year ("Commercial licenses are priced at $1,000 per seat and are valid for one year"). EarthScope is a US 501(c)(3) nonprofit; no VAT. Observed 2026-05-22. |
| hobbyist_eligibility | Yes — NULA allows individuals for scientific, educational, humanitarian use; no surveying licence required |
| legal_residency_required | No — NULA imposes no nationality/residency restriction |
| last_confirmed_alive | 2026-05-22 — local `data/earthscope.sourcetable` refreshed 2026-05-21 (source_health ok) lists CN04 + CN47; EarthScope realtime landing page HTTP 200 with `ntrip.earthscope.org:2101` + ITRF2014 |
| datum_epoch | ITRF2014; NOTA stations epoch 2026-03-30 — operator-declared at https://www.earthscope.org/data/gnss-realtime/ ("All raw data streams use the ITRF2014 reference frame"; "For NOTA stations, the epoch date is 2026-03-30"). Cited 2026-05-22. |

## EarthScope NOTA stations in Saint Lucia

Two separate sites installed 2014 in collaboration with UWI and the Ministry of Physical Development (per UNAVCO install report):
- **CN04** on the rooftop of the National Emergency Management Organisation (NEMO) building, Castries (north of the island).
- **CN47** at the Vieux Fort Lighthouse, southernmost tip of Saint Lucia; data telemeters to a tower at the Cable and Wireless building in Vieux Fort.

The two stations are ~34 km apart and provide complementary north/south coverage. With CN04 near Castries and CN47 near Vieux Fort, most of the populated island is within ~15–20 km of one of the two bases — workable single-base RTK range. Soufrière (west coast, between the two stations) is ~25 km from either.

Legacy platform note: `rtgpsout.unavco.org` retired 2025-07-29; all streams now on `ntrip.earthscope.org`.

## National surveying authority

**Survey & Mapping Section**, Ministry of Physical Development, Housing and Urban Renewal (`govt.lc/ministries/physical-development/survey-mapping-section`), is the responsible body. Collaborated with UNAVCO on the 2014 CN04/CN47 install. No NTRIP caster of its own; no public announcement of a planned national RTK/CORS network 2014–2026. The 2022 World Bank OECS Data for Decision Making Project funded GIS capacity but contains no GNSS CORS component.

## Volunteer / commercial overlay (2026-05-22)

Zero LC stations on rtk2go, Centipede, GEODNET, ONOCOY per local pipeline + WebSearch. EarthScope is the only public NTRIP source.

## Sources
- EarthScope GNSS realtime: https://www.earthscope.org/data/gnss-realtime/ (WebFetch 2026-05-22 — `ntrip.earthscope.org:2101`, ITRF2014, epoch 2026-03-30, $1,000/seat/yr commercial, free noncommercial)
- EarthScope commercial announcement (2024-03-07; service live 2024-05-01): https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- EarthScope NULA PDF: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf (served; text not extractable from sandbox this run)
- UNAVCO news — CN04/CN47 Saint Lucia install: https://www.unavco.org/news/unavco-installs-coconet-cgps-sites-cn04-and-cn47-in-saint-lucia/
- Government of Saint Lucia — Survey & Mapping Section: https://www.govt.lc/ministries/physical-development/survey-mapping-section
- World Bank OECS Data for Decision Making Project: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/
- Local pipeline 2026-05-22: `data/earthscope.sourcetable` lines 125 (CN04) + 144 (CN47) tag `LCA`; `stations_by_country.py LCA` returns the two stations; rtk2go/centipede return zero LC stations
