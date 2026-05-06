# Aruba [AW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO public NTRIP caster; one geodetic-research GNSS station (COCONet CN19) with RINEX only

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Free RINEX / post-processing** | Yes — via EarthScope/NOTA (COCONet CN19 station) |
| **Volunteer rtk2go coverage** | No confirmed ABW-coded stations |
| **hobbyist_eligibility** | n/a (no caster) |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | n/a |
| **Most recent project announcement** | None found as of 2026-05-06 |

## Context Notes

- **No RTK correction service operates on Aruba island.** Aruba (ISO 3166-1 AW) is an autonomous constituent country of the Kingdom of the Netherlands but is not covered by the Kadaster/NSGI AGRS.BES network. AGRS.BES covers only the three BES special municipalities (Bonaire, Sint Eustatius, Saba). Aruba, Curaçao, and Sint Maarten have separate constitutional status and are not included. See `CW_Dutch_Caribbean.md` and `BQ_Bonaire.md`.
- **COCONet CN19 (near California Lighthouse, NW Aruba):** Installed by UNAVCO engineers 2–9 June 2013 in cooperation with the Meteorological Department of Aruba. The station is part of EarthScope's Network of the Americas (NOTA). RINEX data is freely downloadable via EarthScope's data portal. Real-time NTRIP streaming from this station has not been confirmed; NOTA selectively streams a subset of Caribbean stations to IGS real-time data centres, and Aruba was not listed in a confirmed NOTA public NTRIP stream as of 2026-05-06.
- **Aruba Government survey capacity:** The Department for Infrastructure Management and Planning (DIP, gobierno.aw) handles survey and land registration. No CORS or RTK network infrastructure was found on their public web presence.
- **Practical fallback for RTK in Aruba:** Set up a local base station (rover + base) or use a global commercial correction service (PointPerfect, GEODNET, etc.). The nearest free caster streams (AGRS.BES Bonaire, `ntrip.kadaster.nl:2101`) are ~130 km east — beyond usable RTK baseline range — but accessible for scientific post-processing reference.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / NOTA** — COCONet CN19 RINEX archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **UNAVCO GNSS data portal** — historical CN19 dataset | https://www.unavco.org/data/doi/10.7283/T5HD7SZB | Free |

## Sources Consulted
- UNAVCO COCONet CN19 Aruba installation report: https://www.unavco.org/news/unavco-installs-coconet-cgps-site-in-aruba/ (observed 2026-05-06)
- EarthScope NOTA network: https://www.earthscope.org/nota/ (observed 2026-05-06)
- Kadaster BES sourcetable (no AW entries confirmed): http://ntrip.kadaster.nl:2101/sourcetable.htm (curl verified 2026-05-06)
- NL_Netherlands.md research note (AGRS.BES scope limited to Bonaire/Saba/Sint Eustatius)
- Government of Aruba DIP: https://www.gobierno.aw/en/department-for-infrastructure-management-and-planning-dip-0 (observed 2026-05-06)
- CW_Dutch_Caribbean.md (existing research file)
