# Iraq [IQ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry — findings unchanged)

## Status: NO confirmed public NTRIP caster (CORS network exists; no public stream found)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — CORS with VRS capability exists; public NTRIP stream not confirmed |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no public service confirmed |
| **legal_residency_required** | null — no public service confirmed |
| **last_confirmed_alive** | null — no public NTRIP stream confirmed at any date |

## Most Recent Project Announcement

- **2005–2012 (IGRS establishment):** The Iraqi Geodetic Reference System (IGRS) was built with US government support (NOAA/NGS and US Army Corps of Engineers). Initially 7 CORS stations were installed by the Iraq Ministry of Water Resources / State Commission on Survey. Iraqi engineers were trained to install additional CORS and maintain the network as part of the IGS.
- **2024 (academic):** A paper published in the Journal of Engineering (University of Baghdad), Vol. 30 No. 8 (2024), assessed GNSS data collected at five main CORS sites (ZAXO, ISER, ISBA, ISKU, ISNA) for 2015–2022. The study confirmed stations are operational and linked to IGS. No NTRIP public access mentioned.
- **iraqsurveying.com:** A private commercial company (established 2019) sells GNSS receivers and CORS equipment in Iraq — not an NTRIP service provider.

## Context Notes

- The IGRS CORS network is managed by the State Commission on Survey under the Ministry of Water Resources. Some stations were documented as having VRS (Virtual Reference Station) capability for RTK data collection, but no public NTRIP endpoint has been published.
- NOAA's national CORS database (per ELT RTK Base reference, 2025) records the Baghdad CORS station (ISBA) as **non-operational** since its 2008 establishment, while Erbil (ISER) and Najaf (ISNA) are listed as operational. The Journal of Engineering 2024 evaluation cross-checks data from ZAXO, ISER, ISBA, ISKU, ISNA over 2015–2022.
- Security and infrastructure conditions (post-2003 reconstruction context) historically limited public geodetic services; conditions have improved but no public RTK service announcement has emerged.
- The Iraq Survey Board and State Commission on Survey have primary authority over geodetic infrastructure; their websites do not publish external NTRIP endpoints.
- No commercial CORS/RTK network for Iraq was found in any surveying industry or hobbyist source.
- Global commercial networks (GEODNET, ONOCOY, PointOne): no Iraq coverage confirmed.
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS, NRCAN PPP).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS data archive** — IGRS stations (ISER, ISBA, ISKU, ISNA, ZAXO) may have archival RINEX; check IGS/EarthScope | https://www.unavco.org/data/gps-gnss/ | Free non-commercial (if publicly archived) |
| **EarthScope/GAGE** — regional IGS-affiliated stations | https://www.unavco.org/data/gps-gnss/ | Free non-commercial |

## Sources Consulted
- GPS World — "Iraq on the Map: Installing Reference Stations for Accurate Engineering": https://www.gpsworld.com/defensenavigationon-edge-iraq-map-11145/
- Journal of Engineering (University of Baghdad) — "Assessment of the GNSS Data Collected at the Main CORS of the Iraqi Geodetic Network" (2024): https://joe.uobaghdad.edu.iq/index.php/main/article/view/2747
- ResearchGate — IGRS CORS distribution map: https://www.researchgate.net/publication/382824689_Assessment_of_the_GNSS_Data_Collected_at_the_Main_Continuously_Operating_Reference_Stations_CORS_of_the_Iraqi_Geodetic_Network
- Iraq Surveying (commercial company): https://iraqsurveying.com/
- ArduSimple country RTK list (Iraq not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- mvarga1989 GitHub GNSS CORS networks list (Iraq not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2go monitor (no Iraq stations observed; confirmed 2026-05-12 via `scripts/stations_by_country.py IRQ` — no IRQ tag in any source)
- ELT RTK Base / NOAA CORS reference notes (ISBA non-operational since 2008): https://gnss.store/blogs/elt-rtk-base/2-types-of-cors-stations
- NOAA CORS network: https://geodesy.noaa.gov/CORS/
