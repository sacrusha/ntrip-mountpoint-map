# Turks and Caicos Islands [TC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified from 2026-05-13 — no operational change; Survey & Mapping Department and EarthScope coverage unchanged)

## Status: No caster — no EarthScope / COCONet station in TCI territory; nearest scientific stations are ~200+ km away, well beyond single-base RTK range

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS stream in TC territory** | No — no COCONet or EarthScope NOTA station is located in Turks and Caicos Islands waters |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster found |

---

## National Surveying Authority

The **Survey and Mapping Department** (Lands Division, Attorney General's Chambers, `gov.tc/landsurvey`) is the national geodetic and cadastral authority for the Turks and Caicos Islands (UK Overseas Territory). Its stated responsibilities include establishment and maintenance of the geodetic network and the national cadastre.

No NTRIP caster, CORS host:port, real-time RTK correction service, or public announcement of a planned GNSS correction service was found as of 2026-05-13. The department's public-facing website (`gov.tc/landsurvey`) provides map calculation tools, FAQ pages about surveys, and contact information, but contains no GNSS data download or CORS section. The TCI Government Land Survey Ordinance (Chapter 9.03) regulates cadastral practice but contains no provision establishing a CORS service.

---

## COCONet / EarthScope Coverage Gap

No COCONet station was installed in Turks and Caicos Islands territory. The COCONet network (~85 stations) covers neighbouring islands including:
- **Hispaniola** (Haiti / Dominican Republic): CN06 (Porto Plata area), CN17 (Port-au-Prince area)
- **Cuba**: CN08, CN51 area
- **Puerto Rico / USVI** area (USGS / CORS stations)

The nearest EarthScope NOTA stations to TCI are the Dominican Republic COCONet stations (~200–300 km SE) and the Bahamas area stations to the northwest — all well beyond single-base RTK working range (~20–30 km for cm accuracy).

---

## Most Recent Project Announcement

No CORS, GNSS network, or NTRIP-related announcement was found from the Turks and Caicos Islands government as of 2026-05-13. The Survey and Mapping Department's web presence shows routine cadastral and land surveying services; no capital project for geodetic infrastructure modernisation was found in the TCI Government Gazette (2025 issues checked), budget statements, or development partner documents. The only recent geospatial initiative is the Darwin-Plus-funded Marine Spatial Planning project (terraInstitute.org consultancy, marine-focused, no terrestrial CORS).

---

## Context Notes

- **No volunteer bases**: Zero TC-coded stations on rtk2go or Centipede as of 2026-05-13 (re-cross-checked via `py scripts/stations_by_radius.py 21.7 -71.7 200` — no hits within 200 km of central TCI).
- **No commercial NTRIP coverage**: No regional or global commercial NTRIP network lists TCI coverage.
- **UK Overseas Territory context**: As a UK OT, TCI does not participate in OS Net (Ordnance Survey's UK CORS network), which is restricted to Great Britain. No FCO/FCDO geospatial programme for the territories providing NTRIP was found.
- **Hobbyist options**: None identified. Users would need to deploy a local base station or rely on global PPP/SSR correction services (Trimble RTX, Galileo HAS, etc.) for precision work.

---

## Post-Processing (RINEX) Fallback

No CORS RINEX archive for the Turks and Caicos Islands was found at EarthScope, IGS, or UNAVCO as of 2026-05-13. Nearest RINEX-capable scientific stations are the COCONet sites on Hispaniola and the Bahamas — usable for PPP / PPK at 200–400 km baselines but not for RTK.

---

## Sources Consulted
- TCI Survey and Mapping Department: https://gov.tc/landsurvey/
- TCI Government Gazettes 2025: https://gov.tc/cgis/2025-tci-gazettes
- TCI WebGIS portal: https://webgis.gov.tc/
- EarthScope GNSS real-time data: https://www.earthscope.org/data/gnss-realtime/
- EarthScope NOTA: https://www.earthscope.org/nota/
- RTK2go / Centipede sourcetables — no TC stations found
- NTRIP-list.com — no TC entry found
