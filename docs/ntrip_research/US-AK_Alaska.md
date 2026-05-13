# Alaska, USA [US-AK] — NTRIP RTK Caster Research (ACORN)
**Date researched:** 2026-05-02 (re-verified 2026-05-13; SOURCETABLE probed live, mountpoint list expanded to 8, sourcetable confirms multi-constellation GPS+GLO+GAL+BDS, new NorthWest VRS and NortonSound experimental VRS added since 2026-05-02)

## Status: YES — ACORN is operational and explicitly free; hobbyist access likely but not formally confirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | Alaska's Continuously Operating Reference Network (ACORN) |
| **operator** | Alaska Dept. of Natural Resources (DNR) / Division of Mining, Land & Water; partners: AK DOT&PF, National Park Service, EarthScope/UNAVCO, City of Fairbanks, UAA, Enstar, USFWS |
| **host:port** | `www.acorn-gnss.net:2101` (IP 18.216.199.86) |
| **software** | Trimble Pivot Platform / VRS3Net (`NTRIP Trimble Ntrip Caster 5.2`) |
| **tariff** | null — explicitly free public service; no rate card published; 2025 DGGS presentation states "data products will be shared freely" |
| **hobbyist_eligibility** | Unclear (likely yes) — self-service registration at acorn-gnss.net; no professional licence or company field required; login requires "Organization" field (purpose ambiguous); formal confirmation via ACORN@ALASKA.GOV |
| **legal_residency_required** | Unclear — registration form includes "Country" field suggesting international use is structurally possible; no stated residency requirement |
| **last_confirmed_alive** | 2026-05-13 — `www.acorn-gnss.net:2101` SOURCETABLE 200 OK (8 STR entries; curl probe); portal at https://www.acorn-gnss.net HTTP 200 |

## Mountpoints (live 2026-05-13)

| Mountpoint | Type | Format | Constellations |
|---|---|---|---|
| `MS_RTCM3` | Single-base (nearest station) | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_SouthCentral_RTCM3` | Network RTK / VRS | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_SouthCentral_CMRx` | Network RTK / VRS (Trimble) | CMRx | GPS+GLO+GAL+BDS |
| `VRS_Interior_RTCM3` | Network RTK / VRS | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_SouthEast_RTCM3` | Network RTK / VRS | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_SouthEast_CMRx` | Network RTK / VRS (Trimble) | CMRx | GPS+GLO+GAL+BDS |
| `VRS_NorthWest_RTCM3` | Network RTK / VRS (added since 2026-05-02) | RTCM 3.4 | GPS+GLO+GAL+BDS |
| `VRS_NortonSound_RTCM3_EXPERIMENTAL` | Experimental VRS for the Seward Peninsula / Norton Sound region | RTCM 3.4 | GPS+GLO+GAL+BDS |

Stream format: RTCM 3.4 (and CMRx for the two Trimble-targeted mountpoints). Recommended rover: dual-frequency, RTCM 3X capable. All eight mountpoints declare a four-constellation message set, an upgrade from the GPS+GLO-only configuration referenced in older ACORN documentation.

## Context Notes

- ACORN is a multi-agency state government network, not a commercial service. The 2023 DGGS presentation (Peter Flint, DNR) confirms partners provide "free or paid access to existing data stream" — "paid" refers to inter-agency cost-sharing arrangements, not end-user fees.
- The FAQ page at https://www.acorn-gnss.net/FAQ.aspx returns only "FAQs Coming Soon!" as of 2026-05-02. Terms-of-use page requires login.
- NPS is a contributing partner to ACORN and maintains its own separate national NPS CORS network (rtk.nps.gov:2101).
- No phone number or public pricing contact is published; contact ACORN@ALASKA.GOV for registration questions.
- The 2026-05-13 live sourcetable shows a `NET;` line absent — the caster currently advertises only a `CAS;` clause; this is normal for a Trimble Pivot single-tenant deployment.

## EarthScope NOTA — Alaska coverage (free non-commercial alternative)

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3) |
| **Alaska station count** | 140 permanent stations across the Aleutians, mainland, and Arctic (EarthScope NOTA "Learn about NOTA" page); ~66 fall within 1,500 km of Fairbanks per project pipeline data. 87 of the AK NOTA stations are inside the subduction zone footprint (Akutan, Augustine, Unimak volcanic clusters). |
| **tariff** | Free non-commercial (annual self-service licence renewal); USD 1,000/seat/yr commercial |
| **last_confirmed_alive** | 2026-05-13 — `ntrip.earthscope.org:2101` SOURCETABLE 200 OK (1,080 STR entries globally) |
| **notes** | EarthScope NOTA is the densest single-base alternative in Alaska. ACORN's 8 VRS / single-base mountpoints are the only network-RTK option; NOTA fills the gaps between ACORN's three regional VRS solutions (SouthCentral, Interior, SouthEast, NorthWest) with raw physical-station streams. |

## Sources Consulted
- ACORN portal: https://www.acorn-gnss.net (HTTP 200 and NTRIP SOURCETABLE 200 OK observed 2026-05-13)
- ACORN live sourcetable (8 STR, 2026-05-13): `curl http://www.acorn-gnss.net:2101/`
- 2025 DGGS workshop presentation (mountpoints, host, port, registration): https://dggs.alaska.gov/webpubs/dggs/ago/documents/2025AKGeoSummit/Workshop_Gervelis_State_of_Alaska_ACORN.pdf
- 2023 DGGS presentation (free public service statement): https://dggs.alaska.gov/webpubs/dggs/ago/documents/2023AKGeoSummit/2023AKGeoSummit_Session5_Flint.pdf
- EarthScope NOTA Alaska station count and operational scope: https://www.earthscope.org/nota/learn/
- Contact: ACORN@ALASKA.GOV
