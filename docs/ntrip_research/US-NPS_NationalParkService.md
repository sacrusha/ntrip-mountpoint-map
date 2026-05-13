# USA National Park Service CORS [US-NPS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-02 (re-verified 2026-05-13; SOURCETABLE 200 OK with 141 STR entries; all 7 stations previously flagged offline are back in the live sourcetable)

## Status: YES — NPS CORS operational and free; manual account provisioning; hobbyist eligibility unclear

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **operator** | U.S. Department of the Interior, National Park Service (NPS) |
| **host:port** | `rtk.nps.gov:2101` (current; portal still accessible at ntrip.nps.gov) |
| **software** | Trimble Pivot Platform (`NTRIP Trimble Ntrip Caster 5.2`); Trimble NetR9 receivers in the field |
| **tariff** | null — no fee schedule published; federal government service provided at no cost to authorized users |
| **account provisioning** | Manual — contact gnss_posnav@nps.gov; no self-service registration |
| **hobbyist_eligibility** | Unclear — login form requires only email + password; accounts provisioned by NPS staff; no published eligibility policy for external/hobbyist users; contacting gnss_posnav@nps.gov required to confirm |
| **legal_residency_required** | Unclear — no residency or citizenship requirement stated publicly; access is at NPS staff discretion |
| **last_confirmed_alive** | 2026-05-13 — `rtk.nps.gov:2101` SOURCETABLE 200 OK with 141 STR mountpoints (curl probe). Portal at https://ntrip.nps.gov/ HTTP 200 (© 2026 Trimble footer). |

## Stream Characteristics

| Parameter | Value |
|---|---|
| Solution type | Single Base RTK |
| Update rate | 1 second |
| Message format | RTCM 3.2 (most stations) / RTCM 3.4 (newest stations, e.g. DESO_RTCM3); declared message set `1004(1),1005/1007(5),PBS(10)` |
| Constellations | GPS + GLONASS + Galileo + BeiDou (live sourcetable) — upgrade from the earlier MSM4 GPS-only configuration documented in 2022 |
| Datum | NAD 1983 (2011) 2010.0; MYCS3 (NGS Multi-Year CORS Solution 3, released by NGS 2025-06-10 in ITRF2020 epoch 2020.00) applied to ntrip.nps.gov system on 2026-02-13 using August 2025 data |
| Coverage | CONUS, Alaska, Pacific (Hawaii, American Samoa), Marianas |

## Station Count (live sourcetable, 2026-05-13)

141 active mountpoints total (was ~128 active on 2026-05-02). The 7 stations previously flagged offline (DESO, GAA2, GAA3, HALE, HAVO, PAAL, SAJU) are all back in the live sourcetable as of 2026-05-13. Spot-confirmed Pacific stations include HAVO_RTCM3 (Hawaii Volcanoes), HALE_RTCM3 (Haleakalā, Maui), KAHO_RTCM3, KEF1_RTCM3, PUHE_RTCM3 (all Hawaii). Spot-confirmed Alaska stations include DENA_RTCM3 (Denali), GAA2_RTCM3, GAA3_RTCM3 (Gates of the Arctic), GLAC_RTCM3 (Glacier Bay), KEF1_RTCM3, KNAI_RTCM3, LACL_RTCM3.

## Hostname Note

The portal page at https://ntrip.nps.gov states: "Real-Time Correction Configuration — NTRIP Address: **rtk.nps.gov** Port: **2101**." The portal-level domain `ntrip.nps.gov` remains accessible but the active NTRIP caster endpoint for rover connections is `rtk.nps.gov:2101`. Earlier documentation (Nov 2022 DGGS PDF) listed `ntrip.nps.gov:2101`; the live portal now explicitly directs to `rtk.nps.gov:2101`.

## Context Notes

- NPS CORS is a federal government survey infrastructure network, not a public community service. Primary purpose is supporting NPS internal GIS and field survey operations; however, NPS partners with ACORN (Alaska), EarthScope/UNAVCO, and external contractors, indicating non-NPS access has been granted historically.
- No pricing, subscription tiers, or external-access policy is published on any NPS GNSS public page.
- The datum transition to MYCS3 (Multi-Year CORS Solution 3, released by NGS 2025-06-10 in ITRF2020 epoch 2020.00) was applied in the ntrip.nps.gov system on 2026-02-13 using August 2025 data.
- 2026-05-13 sourcetable shows no `NET;` line — the caster currently advertises only `CAS;`; this is normal for the Trimble Pivot deployment. The `NPSNet` identifier is in the per-stream NET column (`STR;…;NPSNet;…`).

## Sources Consulted
- Live NPS GNSS portal: https://ntrip.nps.gov/ (HTTP 200 observed 2026-05-13)
- Live sourcetable (2026-05-13): `curl http://rtk.nps.gov:2101/` → SOURCETABLE 200 OK, 141 STR entries
- NGS MYCS3 release page: https://geodesy.noaa.gov/CORS/news/mycs3/mycs3.shtml (MYCS3 released 2025-06-10 in ITRF2020 epoch 2020.00)
- Nov 2022 DGGS/NPS slide deck (host, port, solution type, MSM4, datum): https://dggs.alaska.gov/webpubs/dggs/ago/documents/2022AGC_GISDay/Day_1-4_Joel_Cusick_Hi_Precision_BaseStations.pdf
- Contact: gnss_posnav@nps.gov
