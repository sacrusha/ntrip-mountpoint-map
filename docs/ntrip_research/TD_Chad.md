# Chad [TD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified from 2026-05-13 — no operational change) | Currency: XAF (Central African CFA franc, CEMAC zone) — 1 USD ≈ 560.59 XAF (fixed peg: €1 = 655.957 XAF)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null — no service exists |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A |

No CORS network, no NTRIP caster, no RTK service of any kind — government, commercial, or community.

## Most Recent Infrastructure Project

**RGT20 — Réseau Géodésique du Tchad 2020** (passive pillar network, not CORS)

- **Operator:** IGN FI (now GEOFIT Group) and local firm BECC, under contract to MATDHU (Ministry of Land Management); funded at 5.5 billion XAF (~€8.4 M)
- **Scope:** 75 geodetic monuments + 50 orientation pillars around N'Djamena; also DTM, DEM, orthoimages, urban GIS databases
- **First pillar inaugurated:** 2020-03-16
- **Project completed:** 2021-02-03
- **Source:** https://www.ignfi.fr/en/actu/tchad-inauguration-le-16-mars-de-la-premiere-borne-geodesique/

This is a traditional passive survey control network — physical pillars only, no CORS, no real-time GNSS, no NTRIP.

## Commercial Providers

No commercial RTK provider (GEODNET, onocoy, SmartNet, Trimble VRS Now) has confirmed Chad coverage.

## Post-Processing (RINEX) Fallback

No national GNSS archive. Nearest scientific GNSS stations are in Cameroon and Nigeria (IGS / AFREF). EarthScope / CDDIS may have sparse regional data. **No rtk2go or Centipede stations within 800 km of N'Djamena** (re-cross-checked 2026-05-13 via `py scripts/stations_by_radius.py 12.13 15.05 800` — zero hits). Nearest volunteer base is `fssoyo` in Nigeria, ~333 km from the south-western corner of Chad — beyond single-base RTK range.

## Sources Consulted
- IGNFI / GEOFIT RGT20 project pages (confirmed reachable 2026-05-13):
  - https://www.ignfi.fr/en/actu/tchad-inauguration-le-16-mars-de-la-premiere-borne-geodesique/
  - https://www.ignfi.fr/en/portfolio-item/infrastructure-de-donnees-spatiales-sur-ndjamena-et-ses-environs-tchad/
- RTK2GO, ntrip-list.com/africa/, corsstations.com — no TD entries
- GEODNET, ONOCOY, Trimble VRS Now, HxGN SmartNet, Topcon TopNET Live — no TD coverage confirmed
- AFREF capacity-building records — no CORS station confirmed for Chad
- `data/stations.json` cross-check (`py scripts/stations_by_radius.py 12.13 15.05 800`) — zero stations
