# Alaska, USA [US-AK] — NTRIP RTK Caster Research (ACORN)
**Date researched:** 2026-05-02

## Status: YES — ACORN is operational and explicitly free; hobbyist access likely but not formally confirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | Alaska's Continuously Operating Reference Network (ACORN) |
| **operator** | Alaska Dept. of Natural Resources (DNR) / Division of Mining, Land & Water; partners: AK DOT&PF, National Park Service, EarthScope/UNAVCO, City of Fairbanks, UAA, Enstar, USFWS |
| **host:port** | `www.acorn-gnss.net:2101` |
| **software** | Trimble Pivot Web |
| **tariff** | null — explicitly free public service; no rate card published; 2025 DGGS presentation states "data products will be shared freely" |
| **hobbyist_eligibility** | Unclear (likely yes) — self-service registration at acorn-gnss.net; no professional licence or company field required; login requires "Organization" field (purpose ambiguous); formal confirmation via ACORN@ALASKA.GOV |
| **legal_residency_required** | Unclear — registration form includes "Country" field suggesting international use is structurally possible; no stated residency requirement |
| **last_confirmed_alive** | 2026-05-02 — portal at https://www.acorn-gnss.net responded normally; login and registration pages functional |

## Mountpoints

| Mountpoint | Type |
|---|---|
| `MS_RTCM3` | Single-base RTK (connects to nearest station) |
| `VRS_SouthCentral_RTCM3` | Network RTK / VRS |
| `VRS_Interior_RTCM3` | Network RTK / VRS |
| `VRS_SouthEast_RTCM3` | Network RTK / VRS |

Stream format: RTCM3. Recommended rover: dual-frequency, RTCM 3X capable.

## Context Notes

- ACORN is a multi-agency state government network, not a commercial service. The 2023 DGGS presentation (Peter Flint, DNR) confirms partners provide "free or paid access to existing data stream" — "paid" refers to inter-agency cost-sharing arrangements, not end-user fees.
- The FAQ page at https://www.acorn-gnss.net/FAQ.aspx returns only "FAQs Coming Soon!" as of 2026-05-02. Terms-of-use page requires login.
- NPS is a contributing partner to ACORN and maintains its own separate national NPS CORS network (rtk.nps.gov:2101).
- No phone number or public pricing contact is published; contact ACORN@ALASKA.GOV for registration questions.

## Sources Consulted
- ACORN portal: https://www.acorn-gnss.net (observed 2026-05-02)
- 2025 DGGS workshop presentation (mountpoints, host, port, registration): https://dggs.alaska.gov/webpubs/dggs/ago/documents/2025AKGeoSummit/Workshop_Gervelis_State_of_Alaska_ACORN.pdf
- 2023 DGGS presentation (free public service statement): https://dggs.alaska.gov/webpubs/dggs/ago/documents/2023AKGeoSummit/2023AKGeoSummit_Session5_Flint.pdf
- Contact: ACORN@ALASKA.GOV
