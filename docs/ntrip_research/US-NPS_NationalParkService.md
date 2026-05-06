# USA National Park Service CORS [US-NPS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-02

## Status: YES — NPS CORS operational and free; manual account provisioning; hobbyist eligibility unclear

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **operator** | U.S. Department of the Interior, National Park Service (NPS) |
| **host:port** | `rtk.nps.gov:2101` (current; portal still accessible at ntrip.nps.gov) |
| **software** | Trimble Pivot (Trimble NetR9 receivers) |
| **tariff** | null — no fee schedule published; federal government service provided at no cost to authorized users |
| **account provisioning** | Manual — contact gnss_posnav@nps.gov; no self-service registration |
| **hobbyist_eligibility** | Unclear — login form requires only email + password; accounts provisioned by NPS staff; no published eligibility policy for external/hobbyist users; contacting gnss_posnav@nps.gov required to confirm |
| **legal_residency_required** | Unclear — no residency or citizenship requirement stated publicly; access is at NPS staff discretion |
| **last_confirmed_alive** | 2026-05-02 — https://ntrip.nps.gov/ returned full station coordinate table and active site notice; © 2026 Trimble footer |

## Stream Characteristics

| Parameter | Value |
|---|---|
| Solution type | Single Base RTK |
| Update rate | 1 second |
| Message format | RTCM MSM4 |
| Datum | NAD 1983 (2011) 2010.0; transitioning to MYCS3 (update applied 2026-02-13) |
| Coverage | CONUS, Alaska, Pacific (Hawaii, American Samoa), Marianas |

## Station Count (live portal, 2026-05-02)

~100 active CONUS stations + 17 Alaska + 8 Pacific + 3 Marianas. Several stations flagged offline: DESO, GAA2, GAA3, HALE, HAVO, PAAL, SAJU.

## Hostname Note

The portal page at https://ntrip.nps.gov states: "Real-Time Correction Configuration — NTRIP Address: **rtk.nps.gov** Port: **2101**." The portal-level domain `ntrip.nps.gov` remains accessible but the active NTRIP caster endpoint for rover connections is `rtk.nps.gov:2101`. Earlier documentation (Nov 2022 DGGS PDF) listed `ntrip.nps.gov:2101`; the live portal now explicitly directs to `rtk.nps.gov:2101`.

## Context Notes

- NPS CORS is a federal government survey infrastructure network, not a public community service. Primary purpose is supporting NPS internal GIS and field survey operations; however, NPS partners with ACORN (Alaska), EarthScope/UNAVCO, and external contractors, indicating non-NPS access has been granted historically.
- No pricing, subscription tiers, or external-access policy is published on any NPS GNSS public page.
- The datum transition to MYCS3 (Multi-Year Coordinate Solution 3) was applied in the ntrip.nps.gov system on 2026-02-13 using August 2025 data.

## Sources Consulted
- Live NPS GNSS portal: https://ntrip.nps.gov/ (observed 2026-05-02)
- Nov 2022 DGGS/NPS slide deck (host, port, solution type, MSM4, datum): https://dggs.alaska.gov/webpubs/dggs/ago/documents/2022AGC_GISDay/Day_1-4_Joel_Cusick_Hi_Precision_BaseStations.pdf
- Contact: gnss_posnav@nps.gov
