# Uruguay [UY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (re-verified 2026-05-13: SOURCETABLE 200 OK with 96 STR entries; 35 unique physical stations after deduplicating per-format variants; 15 VRS streams (VRS-A through VRS-Z plus `RTCM3-VRS` / `RTCM3-iMAX`); multi-constellation MSM4 mountpoints (`UY**_MSM4`) confirm GPS+GLO+GAL+BDS support on the 2025 SinoGNSS M300 Pro stations)

## Status: YES — free national government caster (REGNA-ROU) with VRS; no commercial alternatives found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **host:port** | `rtk.igm.gub.uy:2101` (IP 201.217.132.178; `GNSS Spider 7.11.1.109/1.0` caster) |
| **tariff** | Free — "El Servicio no tiene costo" (IGM official statement) |
| **type** | Single-base + VRS (Virtual Reference Station) + iMAX (`RTCM3-iMAX` mountpoint) |
| **registration** | Required — web form at `rtk.igm.gub.uy/SBC/Account/Register` |
| **hobbyist_eligibility** | Yes — open registration; no professional licence requirement stated |
| **legal_residency_required** | Unclear — registration portal is in Spanish; no explicit residency requirement found; foreign users not explicitly excluded |
| **last_confirmed_alive** | 2026-05-13 — `rtk.igm.gub.uy:2101` SOURCETABLE 200 OK (curl probe; 96 STR entries returned: ~62 physical-station mountpoints + 15 VRS + iMAX + multi-constellation MSM4 variants). IGM REGNA-ROU service page HTTP 200. |

## Network Coverage

REGNA-ROU (Red Geodésica Nacional Activa de la República Oriental del Uruguay) is operated by the Instituto Geográfico Militar (IGM) of Uruguay. As of 2026-05-13 the live sourcetable advertises 35 unique physical stations (after deduplicating `-V2` legacy and `_MSM4`/`_GNSS_MSM3` format-variant entries) covering Uruguay's 176,215 km² territory. VRS and iMAX are available (15 VRS mountpoints regional-zone keyed A–Z, plus `RTCM3-VRS` and `RTCM3-iMAX`); 1–2 cm horizontal precision claimed with dual-frequency equipment. Reference frame: SIRGAS-ROU (ITRF-compatible). 1,000+ registered users as of 2025.

**December 2025 expansion**: IGM incorporated 8 new multiconstellation CORS stations equipped with SinoGNSS (COMNAV) M300 Pro receivers and SinoGNSS AT600 antennas, delivered via KPN METIOR. The MSM4 mountpoints visible in the live sourcetable (`UYBU_MSM4`, `UYFS_MSM4`, `UYLA_MSM4`, `UYLM_MSM4`, `UYMA_MSM4`, `UYPT_MSM4`, `UYRB_MSM4`, `UYSC_MSM4`, `UYSJ_MSM4`, etc., all RTCM 3 declaring `GPS+GLO+GAL+BDS`) align with the December 2025 multi-constellation roll-out and improve coverage density across interior departments (Tacuarembó, Rivera, Artigas, Durazno, Flores areas). Older stations still stream RTCM 3 GPS+GLO only (`UYMO`, `UYTD`, `UYAR`, etc.).

## Commercial Alternatives

No commercial NTRIP RTK caster specific to Uruguay was identified as of 2026-05-13. The free REGNA-ROU service covers the entire country and appears to meet hobbyist needs without a paid alternative.

- **rtk2go**: 1 station within 400 km of Montevideo per project pipeline (`MPBSAS001` in Argentina, 238 km NW — Buenos Aires region); no UY-tagged volunteer streams in `data/stations.json` as of 2026-05-13.
- **Centipede**: No UY stations.
- **GEODNET**: No confirmed UY GEODNET nodes.
- **International commercial services** (RTKdata, geoRTK, TopNET Live): May claim Uruguay coverage via Argentina- or Brazil-hosted stations but Uruguay-specific nodes unconfirmed; REGNA-ROU is the practical free option.

## Context Notes

- **Free VRS availability**: REGNA-ROU is notable in South America for offering VRS (network RTK) at no cost — most national free casters in the region are single-base only. VRS eliminates the need to manually select the nearest mountpoint and provides corrections synthesised for the rover's actual location.
- **Friction**: Spanish-language portal is the main access barrier for non-Spanish speakers; registration is self-service online. No documented case of foreign-resident registration being rejected.
- **RAMSAC cross-border reach**: Several RAMSAC (Argentina) stations near the Uruguayan border (e.g., Colón, Concordia, Monte Caseros) appear in the rtk2go sourcetable. These are not dedicated UY casters but may provide single-base corrections for border-region users at baselines under 50 km.
- **Service mandate**: REGNA-ROU is operated under the IGM's statutory geodetic mandate; there is no published sunset date or access restriction. Service continuity risk is low given institutional backing.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGM CORS RINEX** — REGNA-ROU station data | https://igm.gub.uy/geoportal/instructivos-2/ | Free (same account as NTRIP) |
| **EarthScope NOTA** — selected UY stations | https://www.earthscope.org/data/gnss-realtime/ | Free non-commercial (NULA) |

## Sources Consulted
- IGM REGNA-ROU service page: https://igm.gub.uy/2016/05/20/servicios-regna-rou/
- IGM real-time service instructivos / geoportal: https://igm.gub.uy/geoportal/instructivos-2/
- IGM Dec 2025 CORS expansion announcement: https://igm.gub.uy/2025/12/16/el-igm-incorpora-ocho-nuevas-estaciones-cors-para-fortalecer-la-regna-rou/
- REGNA-ROU SIRGAS bulletin (2022): https://sirgas.ipgh.org/docs/Boletines/Bol22/02-ServicioUruguayo-REGNA-ROU_RTK.pdf
- REGNA-ROU SIRGAS bulletin (2013): https://www.sirgas.org/fileadmin/docs/Boletines/Bol18/35f_Yelicich_et_al_2013_Posicionamiento_GNSS_y_NTRIP-RTK.pdf
- GPS Uruguay NTRIP/RTK explainer: https://www.gpsuruguay.com/pages/como-funciona-el-sistema-rtk
- Live sourcetable (2026-05-13): `curl http://rtk.igm.gub.uy:2101/` → SOURCETABLE 200 OK, 96 STR entries (35 unique physical stations + 15 VRS + multi-constellation MSM4)
- Pipeline CI sourcetable probe — UY stations confirmed 2026-05-13
