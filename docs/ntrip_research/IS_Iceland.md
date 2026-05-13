# Iceland [IS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-07 entry — caster re-probed and confirmed live)

## Status: YES — free national NTRIP RTK caster operating (IceCORS); registration required (no fee); operated by national mapping authority transferred to Náttúrufræðistofnun (Natural Science Institute of Iceland)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — free of charge, registration required |
| **Network name** | IceCORS — Jarðstöðvakerfi Íslands (Icelandic GNSS Reference Station Network) |
| **Operator** | Náttúrufræðistofnun Íslands (Natural Science Institute of Iceland; merged Veðurstofa/LMÍ functions); successor for the GNSS reference network historically operated by **Landmælingar Íslands (LMÍ)**. The user-facing portal moved from `lmi.is` to `natt.is` between 2024 and 2026 — `https://www.lmi.is/is/maelingar/thjonustur/icecors` redirects to `https://www.natt.is/is/landmaelingar/jardstodvakerfi` |
| **Mandate basis** | Národvarúðarstöð (national geodetic infrastructure) under Iceland's Náttúrufræðistofnun; reference frame ISN2016 (ITRF2014, epoch 2016.0) |
| **host:port** | `178.19.53.126:2101` (Geo++ GNSMART caster, banner `NTRIP GNSMART_Caster 2.0/1.0`) — re-confirmed live 2026-05-12: `SOURCETABLE 200 OK`, 12 STR rows, `Content-Length: 1255`, same mountpoint roster (AUSV/GEVK/SENG/VOGC + RTCM30 selectors + VRS3 network mounts in RTCM 3.0 and RTCM 3.2 MSM variants) |
| **Registration / portal** | `https://ggn01.lmi.is/` (account portal — historically operated under LMÍ subdomain; still active May 2026); contact `icecors@natt.is` (per existing networks.md note + ardusimple.com confirmation) |
| **VRS** | Yes — VRS3 (RTCM 3.0) and VRS3_MSM (RTCM 3.2 MSM) network mountpoints, plus FKP-style nearest-station selectors `RTCM30` and `RTCM30_MSM` (both at `0,0` in sourcetable). Single-base streams for individual stations: `AUSV_RTK`, `GEVK_RTK`, `SENG_RTK`, `VOGC_RTK` (all near Reykjavík/Reykjanes peninsula) plus `_MSM` variants |
| **Number of stations** | 33 physical GNSS reference stations at 70–100 km spacing nationwide (per existing networks.md description); only 4 individually-addressable physical mounts exposed in the public sourcetable (AUSV, GEVK, SENG, VOGC — all near Reykjavik) — remaining 29 stations are reached only via the RTCM30 nearest-station selector or VRS3 network mountpoint |
| **Constellations** | GPS + GLONASS (RTCM 3.0 mountpoints) and GPS + GLONASS + Galileo (RTCM 3.2 MSM mountpoints) per sourcetable; BeiDou not advertised |
| **tariff** | Free of charge — `natt.is` IceCORS service description states the data is free for users (per ardusimple.com and pre-existing networks.md confirmation citing natt.is). No published commercial tariff |
| **hobbyist_eligibility** | Yes — registration form/email contact accepts any user. No professional-licence requirement documented |
| **legal_residency_required** | Unclear — no public restriction on foreign users; in practice, registration appears to require contacting `icecors@natt.is` with company name (or individual name), contact name, and email; no Icelandic kennitala (national ID) or local address is publicly required, but the email-based vetting allows the operator discretion. ArduSimple's Iceland guide (2026-04-30 observation) lists IceCORS as a "free national service" requiring registration on the website without limiting eligibility to Icelandic residents |
| **last_confirmed_alive** | 2026-05-12 — `178.19.53.126:2101` returned `SOURCETABLE 200 OK` (`GNSMART_Caster 2.0/1.0`, 12 STR rows including `VRS3`, `VRS3_MSM`, `RTCM30`, `RTCM30_MSM`, plus 8 single-base mounts for AUSV/GEVK/SENG/VOGC). `https://ggn01.lmi.is/` portal HTTP 200. Caster, portal (ggn01.lmi.is), and contact path (icecors@natt.is) all operational. IceCORS service page: `https://www.natt.is/is/landmaelingar/jardstodvakerfi`. |

## Mountpoint Catalogue (sourcetable 2026-05-07)

| Mount | Format | Type | lat,lon | Station |
|---|---|---|---|---|
| `AUSV_RTK` | RTCM 3.0 | single-base RTK | 63.84, -22.42 | AUSV (Auðnur, Reykjanes) |
| `AUSV_RTK_MSM` | RTCM 3.2 MSM | single-base RTK | 63.84, -22.42 | AUSV |
| `GEVK_RTK` | RTCM 3.0 | single-base RTK | 63.84, -22.47 | GEVK |
| `GEVK_RTK_MSM` | RTCM 3.2 MSM | single-base RTK | 63.84, -22.47 | GEVK |
| `SENG_RTK` | RTCM 3.0 | single-base RTK | 63.88, -22.43 | SENG |
| `SENG_RTK_MSM` | RTCM 3.2 MSM | single-base RTK | 63.88, -22.43 | SENG |
| `VOGC_RTK` | RTCM 3.0 | single-base RTK | 63.98, -22.33 | VOGC |
| `VOGC_RTK_MSM` | RTCM 3.2 MSM | single-base RTK | 63.98, -22.33 | VOGC |
| `RTCM30` | RTCM 3.0 | nearest-station selector | 0, 0 | (network — selects closest of 33) |
| `RTCM30_MSM` | RTCM 3.2 MSM | nearest-station selector | 0, 0 | (network — selects closest of 33) |
| `VRS3` | RTCM 3.0 | network VRS | 0, 0 | (computed VRS) |
| `VRS3_MSM` | RTCM 3.2 MSM | network VRS | 0, 0 | (computed VRS) |

The 4 single-base mountpoints are clustered on the Reykjanes peninsula near the GEVK volcanic zone. Connecting to the wider network requires either the `RTCM30`/`RTCM30_MSM` nearest-station selector (rover sends NMEA GGA, caster picks the closest of the 33 stations) or the `VRS3`/`VRS3_MSM` virtual-reference-station mountpoint (computed correction at the rover's position).

## Pipeline Note

Stations.json 2026-05-06 fetch reports `IS = 2 auscors` (i.e. only 2 IceCORS-area stations are picked up by the AUSCORS sourcetable, not by the IceCORS caster directly). The IceCORS caster itself is currently not pipeline-fetched; per existing networks.md note, all IceCORS sourcetable streams carry `nmea=1`, including the 4 single-base mounts which have unique coordinates and `solution=0`, so the default `nmea_filter=True` drops them. Setting `nmea_filter=False` would yield the 4 visible Reykjanes physical pins; the remaining 29 stations would still require sourcetable enrichment to display.

## Service Details

- **Network purpose**: Dual-use — maintains the Icelandic national coordinate reference frame (ISN2016) and provides real-time RTK to users. Iceland sits astride the Mid-Atlantic Ridge spreading at ~2 cm/year and the network captures crustal deformation as well as serving rover positioning.
- **Reference frame**: ISN2016, ITRF2014 epoch 2016.0. Velocities are nontrivial; for cm-level rover work the network corrections are accurate, but for mm-level static work users should consult Náttúrufræðistofnun for current deformation models.
- **Spacing**: 70–100 km between stations, adequate for RTK across the populated coastal ring; interior Highlands and Vatnajökull have sparse coverage and limited cellular connectivity.
- **Software platform**: Geo++ GNSMART (caster banner). Same platform used by Latvia (LatPos), Iceland (IceCORS), and Hungary (GNSSnet.hu) — facilitating GNSMART-style VRS/FKP mountpoints.
- **Institutional handover**: LMÍ (Landmælingar Íslands, founded 1956) was historically the operator. Effective ~2024–2025, geodetic functions were folded into Náttúrufræðistofnun Íslands (Natural Science Institute of Iceland). The user-facing IceCORS page now lives at `natt.is`; `lmi.is` issues a 301 to natt.is. The contact email migrated from `icecors@lmi.is` to `icecors@natt.is`; the registration portal `ggn01.lmi.is` retains the LMÍ-era subdomain.
- **Caster misconfiguration**: GNSMART tags all mountpoints `NMEA=1` including the 4 single-base entries (which have unique coordinates and `solution=0`). The pipeline default `nmea_filter=True` therefore drops all IceCORS pins; `nmea_filter=False` would be needed once display of partial data is acceptable.

## Context Notes

- **Tectonic caveat**: For cm-level RTK surveying, ISN2016 is fully adequate without manual epoch-correction. mm-level geodetic users should fetch up-to-date station velocities from Náttúrufræðistofnun.
- **Coverage gaps**: Iceland's interior (Highlands, Vatnajökull glacier area) has limited or no cellular internet coverage, making NTRIP reception impractical despite nearby IceCORS stations in some areas. Coastal and Reykjavík-area coverage is solid.
- **Agriculture/farming**: IceCORS is promoted for precision agriculture in Iceland. Bændablaðið (the Icelandic farming newspaper) published a feature on IceCORS-enabled fertiliser guidance.
- **No VRS-network polygons in pipeline**: VRS3 and RTCM30 mountpoints carry coordinates `0,0` and are not directly mappable; only the 4 Reykjanes single-base mounts have real coordinates exposed in the sourcetable.
- **REYK IGS station**: A continuously-operating monitoring station in Reykjavík is part of the global IGS network (separate from IceCORS), maintained in cooperation with LMÍ/Náttúrufræðistofnun.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **LMÍ Geo-service / RINEX download** | https://www.lmi.is/is/maelingar/gogn-til-nidurhals/geo-service (likely re-homed to natt.is during the 2024–2026 institutional consolidation) | Free |
| **EUREF EPN — REYK** | https://www.epncb.oma.be/_networkdata/siteinfo4onestation.php?station=REYK00ISL | Free |
| **IGS station REYK** | https://igs.org/network | Free |

## Sources Consulted

- IceCORS Náttúrufræðistofnun page (post-handover): https://www.natt.is/is/maelingar/thjonustur/icecors — was 200 on 2026-05-07, **returns HTTP 404 on 2026-05-12** (page removed/restructured during ongoing institutional consolidation; caster + portal remain alive)
- IceCORS user portal: https://ggn01.lmi.is/ (still resolves; user-facing geodetic portal in Icelandic)
- LMÍ legacy IceCORS page (now redirects): https://www.lmi.is/is/maelingar/thjonustur/icecors
- Live caster sourcetable: `curl http://178.19.53.126:2101/` → `SOURCETABLE 200 OK Server: NTRIP GNSMART_Caster 2.0/1.0` (12 STR rows, 2026-05-07)
- ArduSimple Iceland: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-iceland/ (lists IceCORS as free national service via `https://ggn01.lmi.is/`, observed 2026-04-30)
- LMÍ corporate page: https://www.lmi.is/um-landmaelingar/
- Náttúrufræðistofnun: https://www.natt.is/en
- NKG Iceland national report (ISN2016): https://www.nordicgeodeticcommission.com/wp-content/uploads/2021/03/NKG_WGRF2020_3-4_NatRep-Iceland.pdf
- Bændablaðið IceCORS agriculture feature: https://www.bbl.is/skodun/a-faglegum-notum/betri-nyting-aburdar-med-hjalp-icecors-leidrettingarkerfis-landmaelinga-islands
- LMÍ AMAP project profile: https://projects.amap.no/project/landmaelingar-islands-the-national-land-survey-of-iceland-lmi-lmi/
- EuroGeographics member page: https://eurogeographics.org/member/national-land-survey-of-iceland/
- Existing networks.md `icecors` entry: docs/networks.md (33 stations, 70–100 km spacing, GNSMART, registration via icecors@natt.is — pipeline NMEA filter caveat documented)
- Stations.json 2026-05-06 fetch: 2 IS stations from AUSCORS source (REYK, HOFN); IceCORS caster not in pipeline due to `nmea=1` filter
