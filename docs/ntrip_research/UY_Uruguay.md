# Uruguay [UY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free national government caster (REGNA-ROU) with VRS; no commercial alternatives found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **host:port** | `rtk.igm.gub.uy:2101` |
| **tariff** | Free — "El Servicio no tiene costo" (IGM official statement) |
| **type** | Single-base + VRS (Virtual Reference Station) |
| **registration** | Required — web form at `rtk.igm.gub.uy/SBC/Account/Register` |
| **hobbyist_eligibility** | Yes — open registration; no professional licence requirement stated |
| **legal_residency_required** | Unclear — registration portal is in Spanish; no explicit residency requirement found; foreign users not explicitly excluded |
| **last_confirmed_alive** | IGM REGNA-ROU service page confirmed HTTP 200 on 2026-05-06; pipeline CI sourcetable probe active |

## Network Coverage

REGNA-ROU (Red Geodésica Nacional Activa de la República Oriental del Uruguay) is operated by the Instituto Geográfico Militar (IGM) of Uruguay. As of 2026-05-06 the network has approximately 26 stations covering Uruguay's 176,215 km² territory. VRS is available; 1–2 cm horizontal precision claimed with dual-frequency equipment. Reference frame: SIRGAS-ROU (ITRF-compatible). 1,000+ registered users as of 2025.

**December 2025 expansion**: IGM incorporated 8 new multiconstellation CORS stations equipped with SinoGNSS (COMNAV) M300 Pro receivers and SinoGNSS AT600 antennas, delivered via KPN METIOR. This brings the operational total to ~26 stations and improves coverage density across interior departments (Tacuarembó, Rivera, Artigas, Durazno, Flores areas).

## Commercial Alternatives

No commercial NTRIP RTK caster specific to Uruguay was identified as of 2026-05-06. The free REGNA-ROU service covers the entire country and appears to meet hobbyist needs without a paid alternative.

- **rtk2go**: ~2 volunteer bases near the Argentine border (likely RAMSAC cross-border stations); no dedicated UY-coded volunteer streams confirmed.
- **Centipede**: Negligible UY presence.
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
- Pipeline CI sourcetable probe — ~26 UY stations confirmed 2026-05-06
