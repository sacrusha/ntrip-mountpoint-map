# Iraq [IQ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-23 (refresh of 2026-05-17 entry — findings unchanged; 1 IQ rtk2go station `Hawber` at 35.55/45.48 (Sulaymaniyah region) appears in `scripts/stations_by_country.py IRQ` — a volunteer base of unknown provenance and reliability, not a public service; radius probe Baghdad 33.3/44.4 within 300 km re-confirms `Hawber` as the only IQ-tagged result; no IGRS operator announcement located)
last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-17
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: NO confirmed public NTRIP caster (CORS network exists; no public stream found)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — CORS with VRS capability exists; public NTRIP stream not confirmed |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no public service confirmed |
| **legal_residency_required** | null — no public service confirmed |
| **last_confirmed_alive** | null — no public NTRIP stream confirmed at any date |
| **datum_epoch** | omitted — no citable operator declaration. IGRS HARN positions are referenced to ITRF2000 on the GRS80 ellipsoid per the US National Geodetic Survey description and IOGP Guidance Note 22 "Geodetic referencing in Iraq" (May 2015); the State Commission on Survey publishes no operator portal with a real-time-service datum statement (checked: ngs.noaa.gov/external/IGRS 2026-05-23; iogp.org/bookstore Guidance Note 22 2026-05-23; amerisurv.com 2005-10 article 2026-05-23) |

## Most Recent Project Announcement

- **2005–2012 (IGRS establishment):** The Iraqi Geodetic Reference System (IGRS) was built with US government support (NOAA/NGS and US Army Corps of Engineers). Initially 7 CORS stations were installed by the Iraq Ministry of Water Resources / State Commission on Survey. Iraqi engineers were trained to install additional CORS and maintain the network as part of the IGS.
- **2024 (academic):** A paper published in the Journal of Engineering (University of Baghdad), Vol. 30 No. 8 (2024), assessed GNSS data collected at five main CORS sites (ZAXO, ISER, ISBA, ISKU, ISNA) for 2015–2022. The study confirmed stations are operational and linked to IGS. No NTRIP public access mentioned.
- **iraqsurveying.com:** A private commercial company (established 2019) sells GNSS receivers and CORS equipment in Iraq — not an NTRIP service provider.

## Context Notes

- The IGRS CORS network is managed by the State Commission on Survey under the Ministry of Water Resources. Some stations were documented as having VRS (Virtual Reference Station) capability for RTK data collection, but no public NTRIP endpoint has been published.
- NOAA's NCN per-station page for Baghdad ISBA (https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=ISBA) lists ISBA as **non-operational** (operator IRAGDS); Erbil (ISER) and Najaf (ISNA) appear as operational on their NCN station pages. The Journal of Engineering 2024 evaluation analysed ZAXO, ISER, ISBA, ISKU, ISNA data over 2015–2022 from the IGS/NGS archive (post-processing of historical observations), which is consistent with ISBA having ceased real-time operation at some point during or after that window — the "non-operational" NCN status post-dates the archived data, not contradicts it.
- Security and infrastructure conditions (post-2003 reconstruction context) historically limited public geodetic services; conditions have improved but no public RTK service announcement has emerged.
- The Iraq Survey Board and State Commission on Survey have primary authority over geodetic infrastructure; their websites do not publish external NTRIP endpoints.
- No commercial CORS/RTK network for Iraq was found in any surveying industry or hobbyist source. A single rtk2go volunteer mount `Hawber` (35.55, 45.48 — northeast of Sulaymaniyah, KRI) is the only IQ-tagged station in the project pipeline as of 2026-05-23; provenance and uptime not independently verified, accessible via rtk2go.com:2101 under standard any-email rtk2go convention. Coverage useful only inside ~30 km of the base.
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
- RTK2go monitor: 1 IRQ-tagged station `Hawber` (35.55, 45.48) surfaced in pipeline 2026-05-23 via `scripts/stations_by_country.py IRQ`. No IRQ tag in centipede/earthscope/euref_ip/igs_ip/auscors/mirai sources.
- NOAA NCN per-station page — ISBA Baghdad (non-operational, operator IRAGDS): https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=ISBA
- NOAA NCN per-station page — ISER Erbil: https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=ISER
- NOAA NCN per-station page — ISNA Najaf: https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=ISNA
- NGS — IGRS reference frame description: https://www.ngs.noaa.gov/external/IGRS/
- IOGP Guidance Note 22 — "Geodetic referencing in Iraq" (May 2015): https://www.iogp.org/bookstore/wp-content/uploads/sites/2/woocommerce_uploads/2017/01/373-22.pdf
- The American Surveyor (Oct 2005) — "Development of the Iraqi Geospatial Reference System": https://amerisurv.com/2005/10/31/development-of-the-iraqi-geospatial-reference-system/
