# Saint Vincent and the Grenadines [VC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: No national caster — no EarthScope/COCONet station in VC territory

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS stream in VC territory** | No — no COCONet or EarthScope NOTA station is located in Saint Vincent or the Grenadines islands |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster found |

---

## National Surveying Authority

The **Lands and Surveys Department**, under the Ministry of Transport, Works, Urban Development and Local Government (`transport.gov.vc`), is the responsible geodetic authority for Saint Vincent and the Grenadines. No NTRIP caster, CORS host:port, or real-time GPS correction service operated by this department was found as of 2026-05-06.

---

## Most Recent Project Announcement

**Caribbean Digital Transformation Project — Geodetic Network Modernisation (2022–2025)**

The Government of Saint Vincent and the Grenadines, under the World Bank-financed Caribbean Digital Transformation Project (P171528, USD 28 million across Dominica, Grenada, Saint Lucia, and Saint Vincent and the Grenadines), issued a Terms of Reference for "Consultancy Services for the Modernization of the Geodetic Reference Frame."

Key scope per the TOR:
- Upgrade and densification of the SVG geodetic control network
- Geodetic survey of control monuments in ITRF (International Terrestrial Reference Frame)
- Analysis of the existing network (triangulation and levelling monuments) using static dual-frequency GNSS
- No CORS or real-time NTRIP component is described in the TOR — the deliverable is an adjusted geodetic reference frame, not a live correction service

The TOR document is undated on the procurement portal but was active during the project execution window (2022–2025). No procurement award, completion notice, or CORS/NTRIP follow-on announcement was found as of 2026-05-06.

Source: https://procurement.gov.vc/eprocure/images/pdf/CurrentBids/SVG_CARDTP_C_CQS_3_TOR_GEODETIC_NETWORK_SURVEY.pdf

**Note**: The 2022 World Bank OECS Data for Decision Making Project (Grenada, Saint Lucia, Saint Vincent) funded GIS and data management capacity; it contained no GNSS CORS component.

Source: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/

---

## Context Notes

- **No COCONet / EarthScope station in VC territory**: COCONet covers the Caribbean with ~85 stations; none is on Saint Vincent, the Grenadines, or the Vincentian dependency islands. The nearest EarthScope stations are CN46 (Carriacou, Grenada, ~100 km SE) and stations on Barbados (~180 km E), both well outside practical single-base RTK range.
- **No volunteer bases**: Zero VC-coded stations on rtk2go or Centipede as of 2026-05-06.
- **No commercial NTRIP coverage**: No regional Caribbean commercial NTRIP network (Point One, GEODNET, RTKdata, etc.) lists VC coverage.
- **Hobbyist options**: Nearest free correction source is the EarthScope CN46 station on Carriacou (~100 km), useful only for PPP-like accuracy at that baseline; hobbyists in SVG would need to deploy a local base station.

---

## Post-Processing (RINEX) Fallback

No CORS RINEX archive specifically for Saint Vincent and the Grenadines was found at EarthScope, IGS, or UNAVCO. The geodetic survey deliverable from the World Bank project (if completed) may have established new control-point coordinates in ITRF, but these are not distributed as a RINEX stream.

---

## Sources Consulted
- SVG CARDTP Geodetic Network Survey TOR: https://procurement.gov.vc/eprocure/images/pdf/CurrentBids/SVG_CARDTP_C_CQS_3_TOR_GEODETIC_NETWORK_SURVEY.pdf
- World Bank Caribbean Digital Transformation Project (P171528): https://documents1.worldbank.org/curated/en/099021825090536460/pdf/P171528-57158ae9-a7ed-4f3a-93a5-82cf34215f70.pdf
- World Bank OECS Data for Decision Making Project: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/520151651261033077/
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/
- EarthScope Network of the Americas (NOTA): https://www.earthscope.org/nota/
- RTK2go / Centipede sourcetables — no VC stations found
- NTRIP-list.com — no VC entry found
- ArduSimple country directory — no VC page found
