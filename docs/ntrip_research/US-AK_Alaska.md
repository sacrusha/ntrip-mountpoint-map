# Alaska, USA [US-AK] — NTRIP RTK Caster Research (ACORN)

## Status: YES — ACORN operational and free; hobbyist eligibility likely but not formally confirmed

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | Yes |
| Network name | Alaska's Continuously Operating Reference Network (ACORN) |
| Operator | Alaska DNR / Division of Mining, Land & Water. Partners: AK DOT&PF, NPS, EarthScope/UNAVCO, City of Fairbanks, UAA, Enstar, USFWS |
| landing_url | https://www.acorn-gnss.net — operator Trimble Pivot Web; bare URL = login wall but canonical network face |
| access_url | https://www.acorn-gnss.net — self-service registration via same portal; non-self-service questions: ACORN@ALASKA.GOV |
| host:port | `www.acorn-gnss.net:2101` (IP 18.216.199.86) |
| software | Trimble Pivot / VRS3Net (NTRIP Trimble Caster 5.2) |
| num_stations | Physical CORS count not declared on operator pages. 8 mountpoints live: 1 nearest-station alias (`MS_RTCM3`) + 5 regional VRS + 1 NorthWest VRS + 1 experimental NortonSound VRS. Trimble Pivot single-tenant convention hides per-station ST entries |
| tariff | Free — explicit per 2025 DGGS workshop ("data products will be shared freely"). No rate card |
| vrs | Yes — 5 regional VRS + experimental NortonSound VRS; `MS_RTCM3` = nearest-station alias |
| hobbyist_eligibility | Unclear — self-service registration; no professional licence field; portal requires "Organization" field (purpose ambiguous); 2023 Flint DGGS deck says partners receive "free or paid access" (paid = inter-agency cost-sharing, not end-user fee) but no confirmed hobbyist case located. Confirm: ACORN@ALASKA.GOV |
| legal_residency_required | Unclear — Country field on form suggests international use possible; no stated residency rule |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK`, 8 STR; portal HTTP 200 |
| datum_epoch | NAD83(2011) Epoch 2010.0 — Alaska DNR (Gervelis) 2025 DGGS AKGeoSummit ACORN workshop PDF: "Reference Position: NAD83(2011) Epoch 2010.0 / Height above Ellipsoid (m)". Citation: https://dggs.alaska.gov/webpubs/dggs/ago/documents/2025AKGeoSummit/Workshop_Gervelis_State_of_Alaska_ACORN.pdf. **Citation quality**: ACORN operator slide deck delivered by Alaska DNR (the network operator) at state geodesy workshop — operator authorship affirmed, but slide-deck format vs. dedicated spec page. No operator-portal datum statement located (FAQ "Coming Soon!"). Confirm with `ACORN@ALASKA.GOV` for survey-grade work |

## Mountpoints (live 2026-05-18)

| Mountpoint | Type | Format | Constellations |
|---|---|---|---|
| `MS_RTCM3` | Single-base nearest | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_SouthCentral_RTCM3` | VRS | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_SouthCentral_CMRx` | VRS Trimble | CMRx | GPS+GLO+GAL+BDS |
| `VRS_Interior_RTCM3` | VRS | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_SouthEast_RTCM3` | VRS | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_SouthEast_CMRx` | VRS Trimble | CMRx | GPS+GLO+GAL+BDS |
| `VRS_NorthWest_RTCM3` | VRS | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_NortonSound_RTCM3_EXPERIMENTAL` | VRS Seward Pen / Norton Sound (EXPERIMENTAL — stability unknown; operator does not publish stability/availability tier for this mount, suitability for hobbyists vs geodetic/research partners not stated) | RTCM 3.4 | GPS+GLO+GAL+BDS |

All eight mountpoints serve GPS+GLO+GAL+BDS — upgrade from older GPS+GLO-only config in historical ACORN docs.

## Notes

- Multi-agency state government network, not commercial. 2023 DGGS slide deck (Flint): partners provide "free or paid access to existing data stream" — "paid" = inter-agency cost-sharing, not end-user fee.
- FAQ at https://www.acorn-gnss.net/FAQ.aspx = placeholder ("FAQs Coming Soon!"). Terms-of-use requires login.
- 2025-08 ACORN added NorthWest VRS + experimental NortonSound VRS (vs older 5-region catalog).
- GPS World Dec 2024 public RTK list pre-dates current ACORN form ("two PBO RTK bases ... otherwise no public service") — outdated.
- NPS partner; broader NPS CORS = `US-NPS_NationalParkService.md` (source id `nps`), not duplicated here.
- Trimble Pivot single-tenant deployment: no `NET;` clause; sourcetable = mountpoint list only.

## EarthScope NOTA — Alaska fallback

See `US-NOTA_NetworkOfTheAmericas.md` for operator-scope detail. AK sub-coverage: ~140 NOTA stations across Aleutians, mainland, Arctic; densest seismically active arc. Fills single-base gaps between ACORN's regional VRS hulls. Datum mismatch (NOTA ITRF2014 ep 2026-03-30 vs ACORN NAD83(2011) ep 2010.0) — rover-side transform required for state-frame survey. Per-radius queries via `py scripts/stations_by_radius.py <lat> <lon> <km>`.

## Sources

- ACORN portal: https://www.acorn-gnss.net
- Live sourcetable: `curl --http0.9 -A 'NTRIP/1.0' http://www.acorn-gnss.net:2101/`
- 2025 DGGS workshop (datum, mountpoints, host, registration): https://dggs.alaska.gov/webpubs/dggs/ago/documents/2025AKGeoSummit/Workshop_Gervelis_State_of_Alaska_ACORN.pdf
- 2023 DGGS (Flint) free-service statement: https://dggs.alaska.gov/webpubs/dggs/ago/documents/2023AKGeoSummit/2023AKGeoSummit_Session5_Flint.pdf
- ACORN StoryMap: https://storymaps.arcgis.com/stories/72e4d646b51a4c56bddcc0ecc9f16ecd
- ACORN ArcGIS dataset: https://gis.data.alaska.gov/datasets/alaskas-continuously-operating-reference-network-acorn-1/about
- Contact: ACORN@ALASKA.GOV
