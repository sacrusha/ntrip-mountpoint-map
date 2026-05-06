# Sudan [SD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no operational public NTRIP RTK caster; conflict severely disrupts civil infrastructure

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | None found |
| **VRS** | N/A |
| **tariff** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A |

## Most Recent Project / Context

**Sudan CORS / AFREF participation**: The Sudan Survey Authority (SSA), established 1899, is the sole government agency mandated for surveying, mapping and charting. As part of AFREF (African Geodetic Reference Frame) programme, GPS simulation studies and network design were conducted to identify ~55 stable, geologically secure locations for a Sudanese ITRF geodetic control network. However, no operational public CORS network or NTRIP caster has been found.

**Armed conflict (April 2023–present)**: Conflict between the Sudanese Armed Forces (SAF) and the Rapid Support Forces (RSF) erupted in April 2023. Khartoum — the location of SSA headquarters and likely any GNSS infrastructure — suffered severe urban warfare and infrastructure destruction. Civil geodetic services are assessed as non-functional for the duration of hostilities. As of 2026-05-06 no ceasefire or restoration of civil administration in Khartoum has been confirmed.

**GNSS interference**: UKMTO advisories (mid-2024 through 2025) noted GNSS interference in the Port Sudan area and near Bab al-Mandab, complicating GNSS use even in the relatively stable Red Sea coast region.

## Context Notes

- No NTRIP RTK caster exists or has recently existed for Sudan.
- No volunteer rtk2go or Centipede stations from Sudan are known.
- AFREF's Africa-wide analysis identified Sudan as one of the most underserved regions for GNSS reference station coverage.
- The situation mirrors Libya (LY): structural absence of functioning central geodetic administration compounded by active conflict makes near-term public RTK service implausible.
- **Practical advice**: Deploy a local base station. Port Sudan (currently the de-facto administrative seat) may offer better physical security but no geodetic infrastructure.
- **SSA Facebook presence**: Sudan Survey Authority SSA maintains a Facebook page (facebook.com/people/Sudan-Survey-Authority-SSA/100069140112993/) but it is not a functional GNSS service channel.

## Post-Processing (RINEX) Fallback

No RINEX data from Sudanese stations is publicly available. The closest IGS-class stations are in Ethiopia, Egypt, and Kenya. EarthScope/UNAVCO archives no Sudanese CORS as of 2026-05-06.

## Sources Consulted
- UN GGIM Sudan 2015 country report (SSA establishment and AFREF 55-station plan): https://ggim.un.org/country-reports/documents/Sudan-2015-country-report.pdf
- SSA Facebook: https://www.facebook.com/people/Sudan-Survey-Authority-SSA/100069140112993/
- AFREF progress documentation (GNSS station gap in Sudan / Central Africa region): https://ggim.un.org/UNGGCE/2nd_mtg_IAC_4th_plenary_SCOG/AFREF.pdf
- GIM International AFREF article: https://www.gim-international.com/content/article/development-between-2000-and-2015?output=pdf
- GPSPATRON maritime GNSS interference report (Sudan/Red Sea, 2025): https://gpspatron.com/maritime-gnss-interference-worldwide-a-cumulative-analysis-2025/
- Libya entry in country-survey.md (parallel situation reference)
- No NTRIP endpoint found on ntrip-list.com, rtcm-ntrip.org, or rtk2go for Sudan
