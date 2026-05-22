# Turks and Caicos Islands [TC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: NO public NTRIP RTK caster — no station in TC territory; nearest scientific site (EarthScope CN14, Bahamas) is ~213 km from Grand Turk, the rest >250 km — all well beyond single-base RTK range

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | No |
| landing_url | n/a |
| access_url | n/a |
| host:port | n/a |
| tariff | n/a |
| num_stations | 0 in TC territory |
| vrs | n/a |
| hobbyist_eligibility | n/a |
| legal_residency_required | n/a |
| last_confirmed_alive | n/a |
| datum_epoch | omitted — no caster to declare |

## National surveying authority

The **Survey and Mapping Department** (Lands Division, Attorney General's Chambers, `gov.tc/landsurvey/`) is the national geodetic and cadastral authority. Stated remit: "The department is responsible for the standardization and production of all Surveying and Mapping activities and the maintenance of the national cadaster and the country's geodetic network" (WebFetch 2026-05-22). No CORS / NTRIP / real-time RTK reference on the public site. No GNSS data section, no host:port, no announcement of a planned correction service. The Land Survey Ordinance (Chapter 9.03) regulates cadastral practice without mandating CORS infrastructure.

## COCONet / EarthScope coverage gap

No COCONet/NOTA station was installed in TC territory. Per `py scripts/stations_by_radius.py 21.75 -71.80 400` (Grand Turk-centric, 2026-05-22) → 9 EarthScope hits on Dominican Republic (6), Bahamas (2), Haiti (1). Closest is **CN14_RTCM3P3** (Bahamas) at ~213 km; the other 8 sit >250 km. All well beyond reliable single-base RTK range (~20–30 km cm-accuracy on dual-frequency hardware).

## Volunteer / commercial overlay (2026-05-22)

Zero TC-tagged mountpoints on rtk2go, Centipede, GEODNET, ONOCOY (`stations_by_country.py TCA` → empty across all sources). Within a 450 km radius of Grand Turk: 12 EarthScope + 1 IGS + 1 rtk2go station, all on Dominican Republic — closest non-TC rtk2go site (`geofis_ovni`) at ~415 km; none usable for RTK. No commercial network advertises TC coverage. As a UK Overseas Territory, TC does not participate in OS Net (UK-mainland-only). No FCO/FCDO geospatial programme providing NTRIP located.

## Recent project announcements

None located for a TC CORS / NTRIP service. The Survey and Mapping Department's web presence shows routine cadastral activity; no capital project for geodetic infrastructure in TCI Government Gazettes (2025 issues checked), budget statements, or development-partner documents. The recent Darwin-Plus-funded Marine Spatial Planning project (terraInstitute.org) is marine-focused with no terrestrial CORS.

## Sources
- TCI Survey and Mapping Department: https://gov.tc/landsurvey/ (WebFetch 2026-05-22 — "responsible for ... the maintenance of the national cadaster and the country's geodetic network"; no GNSS/CORS/NTRIP)
- TCI Lands Division: https://gov.tc/lands/
- TCI Data Portal — Survey and Mapping Department: https://dataportal.gov.tc/is/organization/surveymp
- EarthScope NOTA: https://www.earthscope.org/nota/
- Local pipeline 2026-05-22: `stations_by_country.py TCA` → no stations; `stations_by_radius.py 21.75 -71.80 400` → 9 EarthScope hits across DOM (6) / BHS (2) / HTI (1), closest CN14 at ~213 km; `stations_by_radius.py 21.75 -71.80 450` adds 1 IGS DOM + 1 rtk2go DOM, all beyond RTK range
