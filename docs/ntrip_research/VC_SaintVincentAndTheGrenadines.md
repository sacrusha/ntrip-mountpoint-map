# Saint Vincent and the Grenadines [VC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (re-verified 2026-05-13: still no national NTRIP caster; nearest EarthScope NOTA station is `CN47_RTCM3P3` in Saint Lucia at 58 km north of Kingstown — closer than previously documented; CN46 in Carriacou (Grenada) is at 88 km, CN04 in Saint Lucia at 89 km; CARDTP digital-mapping fieldwork commenced Dec 2024 – Jan 2025 with This is PLACE, but TOR still describes a static geodetic deliverable rather than a CORS/NTRIP network)

## Status: No national caster — no EarthScope/COCONet station in VC territory; nearest free single-base streams are EarthScope NOTA stations in Saint Lucia and Grenada (Carriacou) within 60–90 km

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS stream in VC territory** | No — no COCONet or EarthScope NOTA station is located in Saint Vincent or the Grenadines islands |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster found (re-confirmed 2026-05-13) |

---

## National Surveying Authority

The **Lands and Surveys Department**, under the Ministry of Transport, Works, Urban Development and Local Government (`transport.gov.vc`), is the responsible geodetic authority for Saint Vincent and the Grenadines. No NTRIP caster, CORS host:port, or real-time GPS correction service operated by this department was found as of 2026-05-06.

---

## Most Recent Project Announcement

**Caribbean Digital Transformation Project — Geodetic Network Modernisation and Digital Mapping (2022–2026)**

The Government of Saint Vincent and the Grenadines, under the World Bank-financed Caribbean Digital Transformation Project (P171528, USD 28 million across Dominica, Grenada, Saint Lucia, and Saint Vincent and the Grenadines), issued a Terms of Reference for "Consultancy Services for the Modernization of the Geodetic Reference Frame."

Key scope per the TOR:
- Upgrade and densification of the SVG geodetic control network
- Geodetic survey of control monuments in ITRF (International Terrestrial Reference Frame), reference to nearest IGS stations
- Analysis of the existing network (triangulation and levelling monuments) using static dual-frequency GNSS — minimum 30 minutes of observations per point + reoccupation at different visible-constellation
- No CORS or real-time NTRIP component is described in the TOR — the deliverable is an adjusted geodetic reference frame, not a live correction service

The TOR document is undated on the procurement portal but was active during the project execution window (2022–2026). No procurement award, completion notice, or CORS/NTRIP follow-on announcement was found as of 2026-05-13.

**Related CARDTP activity (December 2024 – January 2025)**: The Caribbean Digital Transformation Project partnered with the non-profit "This is PLACE" to carry out digital mapping of Saint Vincent and the Grenadines using a special fixed-wing drone that can take off vertically (December 2024 through January 2025). This is an aerial-imagery and base-map deliverable, not an RTK CORS deployment. Equipment worth USD 137,924.46 was handed over to the Lands and Surveys Department in February 2024 under the same CARDTP umbrella.

Source: https://procurement.gov.vc/eprocure/images/pdf/CurrentBids/SVG_CARDTP_C_CQS_3_TOR_GEODETIC_NETWORK_SURVEY.pdf  
Source (digital mapping 2024-2025): https://www.searchlight.vc/news/2024/12/13/digital-mapping-of-svg-expected-to-provide-high-quality-data/  
Source (CARDTP equipment handover Feb 2024): https://dtp.gov.vc/index.php/news/38-digital-transformation-project-donates-equipment-to-lands-surveys

**Note**: The 2022 World Bank OECS Data for Decision Making Project (Grenada, Saint Lucia, Saint Vincent) funded GIS and data management capacity; it contained no GNSS CORS component.

Source: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/

---

## Context Notes

- **No COCONet / EarthScope station in VC territory**: COCONet covers the Caribbean with ~85 stations; none is on Saint Vincent, the Grenadines, or the Vincentian dependency islands.
- **Nearest EarthScope NOTA stations to Kingstown (13.25°N, 61.20°W)** per project pipeline (`py scripts/stations_by_radius.py 13.25 -61.20 300`, 2026-05-13):
  - `CN47_RTCM3P3` — 13.71°N, 60.94°W — 58 km (Saint Lucia, country tag `LCA`)
  - `CN46_RTCM3P3` — 12.49°N, 61.43°W — 88 km (Carriacou, Grenada, country tag `GRD`)
  - `CN04_RTCM3P3` — 14.02°N, 60.97°W — 89 km (Saint Lucia, country tag `LCA`)
  - `CN48_RTCM3P3` — 15.44°N, 61.42°W — 245 km (Dominica, country tag `DMA`)
  - `CN57_RTCM3P3` — 10.84°N, 60.94°W — 270 km (Trinidad and Tobago, country tag `TTO`)
- **Practical RTK baseline**: CN47 (Saint Lucia, 58 km) and CN46 (Carriacou, 88 km) are within the upper limit of single-base RTK practicality for dual-frequency multi-constellation receivers (~30–80 km is typical for cm-level fix; 58 km is at the comfortable edge, 88 km is degraded but workable for ag/GIS-grade decimetre accuracy). These are free non-commercial under EarthScope's NOTA licence — the closest free correction sources for SVG users.
- **No volunteer bases**: Zero VC-coded stations on rtk2go, Centipede, or any other aggregated source as of 2026-05-13.
- **No commercial NTRIP coverage**: No regional Caribbean commercial NTRIP network (Point One, GEODNET, RTKdata, etc.) lists VC coverage.
- **Hobbyist options**: Best free option is EarthScope NOTA's CN47 station in Saint Lucia (58 km from Kingstown) — single-base, requires the NOTA non-commercial licence (free self-service at earthscope.org/user/licenses; annual renewal). For higher accuracy on the southern Grenadines, CN46 on Carriacou is a closer fit. Hobbyists in central Saint Vincent (Kingstown and inland) can expect float-level or degraded-fix performance from CN47; cm-level fix is unlikely beyond 60 km. For survey-grade work, hobbyists should deploy a local base station.

---

## Post-Processing (RINEX) Fallback

No CORS RINEX archive specifically for Saint Vincent and the Grenadines was found at EarthScope, IGS, or UNAVCO. The geodetic survey deliverable from the World Bank project (if completed) may have established new control-point coordinates in ITRF, but these are not distributed as a RINEX stream.

---

## Sources Consulted
- SVG CARDTP Geodetic Network Survey TOR: https://procurement.gov.vc/eprocure/images/pdf/CurrentBids/SVG_CARDTP_C_CQS_3_TOR_GEODETIC_NETWORK_SURVEY.pdf
- World Bank Caribbean Digital Transformation Project (P171528): https://documents1.worldbank.org/curated/en/099021825090536460/pdf/P171528-57158ae9-a7ed-4f3a-93a5-82cf34215f70.pdf
- World Bank OECS Data for Decision Making Project: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/
- Searchlight SVG — digital mapping Dec 2024 – Jan 2025: https://www.searchlight.vc/news/2024/12/13/digital-mapping-of-svg-expected-to-provide-high-quality-data/
- Searchlight SVG — Lands & Surveys Department improvements: https://www.searchlight.vc/news/2024/02/09/major-improvements-coming-lands-surveys-department/
- CARDTP equipment handover (Feb 2024): https://dtp.gov.vc/index.php/news/38-digital-transformation-project-donates-equipment-to-lands-surveys
- SVG Digital Transformation Project: https://dtp.gov.vc/
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/
- EarthScope Network of the Americas (NOTA): https://www.earthscope.org/nota/
- Project pipeline radius probe (2026-05-13): `py scripts/stations_by_radius.py 13.25 -61.20 300` — returns 5 EarthScope stations (CN47, CN46, CN04, CN48, CN57) and 1 Centipede station (DEPZ in Martinique, 168 km)
- RTK2go / Centipede sourcetables — no VC-tagged stations found 2026-05-13
- NTRIP-list.com — no VC entry found
- ArduSimple country directory — no VC page found
