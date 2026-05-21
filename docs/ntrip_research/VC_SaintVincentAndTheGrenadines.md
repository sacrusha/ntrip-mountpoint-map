# Saint Vincent and the Grenadines [VC] — NTRIP RTK

## Status
NO national caster. NO COCONet/NOTA station on SVG soil. Nearest free realtime = EarthScope NOTA stations in St. Lucia (58 km) and Carriacou-Grenada (88 km).

| Field | Value |
|---|---|
| National NTRIP RTK caster | No |
| In-territory GNSS stream | No |
| hobbyist_eligibility | N/A |
| legal_residency_required | N/A |
| last_confirmed_alive | N/A |
| datum_epoch | N/A (no caster) |

## National authority

Lands and Surveys Dept, Ministry of Transport/Works/Urban Dev/Local Gov (`transport.gov.vc`). No NTRIP, no CORS host, no realtime correction service.

## Most recent project

**Caribbean Digital Transformation Project (CARDTP, World Bank P171528, USD 94M total; SVG component USD 30M) — Geodetic Network Modernisation TOR (2022–2026)**:
- Densify SVG geodetic control net; reference monuments to ITRF via nearest IGS.
- Static dual-freq GNSS, ≥30 min/point + reoccupation.
- **No CORS / NTRIP component.** Deliverable = adjusted reference frame, not a live caster.
- TOR undated; active during 2022–2026 window. No award/completion notice; no follow-on CORS announcement found 2026-05-17.

CARDTP digital-mapping fieldwork (Dec 2024 – Jan 2025) with non-profit "This is PLACE" using fixed-wing VTOL drone = aerial imagery / base-map deliverable. Not RTK CORS. Feb 2024 equipment handover USD 137,924.46 to Lands & Surveys (CARDTP umbrella).

Sources:
- TOR: https://procurement.gov.vc/eprocure/images/pdf/CurrentBids/SVG_CARDTP_C_CQS_3_TOR_GEODETIC_NETWORK_SURVEY.pdf
- Searchlight (digital mapping): https://www.searchlight.vc/news/2024/12/13/digital-mapping-of-svg-expected-to-provide-high-quality-data/
- Equipment handover: https://dtp.gov.vc/index.php/news/38-digital-transformation-project-donates-equipment-to-lands-surveys

2022 World Bank OECS Data for Decision Making Project (GD/LC/VC) = GIS + data-mgmt capacity, no CORS. https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/

## Nearest free NTRIP

`stations_by_radius.py 13.25 -61.20 300` (2026-05-21): 9 stations — earthscope 5 [LCA:2, DMA:1, GRD:1, TTO:1], auscors 1 [MTQ], centipede 1 [MTQ], igs_ip 1 [MTQ], mirai 1 [MTQ]. Detail (per 2026-05-17 probe):
- earthscope: `CN47_RTCM3P3` 13.71N, 60.94W — 58 km (LCA); `CN46_RTCM3P3` 12.49N, 61.43W — 88 km (GRD); `CN04_RTCM3P3` 14.02N, 60.97W — 89 km (LCA); `CN48_RTCM3P3` — 245 km (DMA); `CN57_RTCM3P3` — 270 km (TTO).
- auscors / igs_ip / mirai: `LMMF00MTQ0` 14.59N, -61.00W — 151 km (Martinique).
- centipede: `DEPZ` 14.76N, -61.17W — 168 km (Martinique).

Practical RTK: CN47 @ 58 km = comfortable edge for dual-freq multi-constellation single-base; CN46 @ 88 km = degraded, workable for decimetre ag/GIS. cm-fix unlikely beyond ~60 km. NOTA = free non-commercial under NULA (annual renewal at earthscope.org/user/licenses); commercial $1,000/seat/yr (5-seat min for direct billing; 5-seat 2-week trial). Datum for NOTA streams: ITRF2014 @ 2026-03-30 per operator page (WebFetch 200 2026-05-21).

## No alternatives

- rtk2go / Centipede: 0 VC-coded stations 2026-05-13.
- Regional commercial NTRIP (PointOne, GEODNET, RTKdata): no VC coverage.
- Hobbyists wanting cm-fix on SVG: deploy local base.

## Post-processing (RINEX)

No SVG-specific archive at EarthScope/IGS/UNAVCO. World Bank TOR deliverable (if completed) = static control points, not RINEX stream.

## Sources
- SVG CARDTP TOR (above)
- World Bank P171528: https://documents1.worldbank.org/curated/en/099021825090536460/pdf/P171528-57158ae9-a7ed-4f3a-93a5-82cf34215f70.pdf
- WB OECS D4DM: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/
- Searchlight (digital mapping): https://www.searchlight.vc/news/2024/12/13/digital-mapping-of-svg-expected-to-provide-high-quality-data/
- Searchlight (L&S improvements): https://www.searchlight.vc/news/2024/02/09/major-improvements-coming-lands-surveys-department/
- Equipment handover: https://dtp.gov.vc/index.php/news/38-digital-transformation-project-donates-equipment-to-lands-surveys
- SVG DTP: https://dtp.gov.vc/
- EarthScope NOTA realtime: https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA: https://www.earthscope.org/nota/
- Radius probe 2026-05-21: `stations_by_radius.py 13.25 -61.20 300` — 9 stations across 5 sources
- `stations_by_country.py VC` / `VCT` 2026-05-21 — "No stations"
- rtk2go / Centipede: no VC entries
- NTRIP-list.com / ArduSimple: no VC entry
