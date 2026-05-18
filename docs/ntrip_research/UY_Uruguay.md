# Uruguay [UY] — NTRIP RTK
**Date:** 2026-05-17 re-verify: IGM landing HTTP 200; "libre y sin costo" re-quoted; registration `rtk.igm.gub.uy/sbc/`. No new operator-page datum declaration — datum_epoch stays omitted. New radius probe surfaces RAMSAC (Argentina) cross-border + Uruguay-coast stations within practical range of Montevideo — previously not listed.

## Status
YES — free national caster REGNA-ROU (IGM) with single-base + VRS + iMAX. No commercial alt.

## REGNA-ROU — sole caster

| Field | Value |
|---|---|
| landing_url | https://igm.gub.uy/2016/05/20/servicios-regna-rou/ (operator post: "libre y sin costo para los usuarios") |
| access_url | https://igm.gub.uy/geoportal/instructivos-2/ (geoportal "instructivos" — guides for use/configure). Bare registration: https://rtk.igm.gub.uy/sbc/ |
| operator | Instituto Geográfico Militar (IGM), Uruguay |
| host:port | `rtk.igm.gub.uy:2101` (IP 201.217.132.178; `GNSS Spider 7.11.1.109/1.0`) |
| Type | Single-base + VRS + iMAX (`RTCM3-VRS`, `RTCM3-iMAX`, `VRS-A` … `VRS-Z`) |
| num_stations | 35 unique physical CORS (deduped from 96 STR entries: per-format `-V2` legacy + `_MSM4` / `_GNSS_MSM3` variants). Reflects Dec 2025 +8 expansion. |
| Mountpoints | RTCM3, GPS+GLO (legacy stations `UYMO`, `UYTD`, `UYAR`, …) + GPS+GLO+GAL+BDS multi-constellation MSM4 (`UYBU_MSM4`, `UYFS_MSM4`, `UYLA_MSM4`, `UYLM_MSM4`, `UYMA_MSM4`, `UYPT_MSM4`, `UYRB_MSM4`, `UYSC_MSM4`, `UYSJ_MSM4`, …); 15 VRS zone-keyed mountpoints A-Z. |
| vrs | yes (VRS + iMAX) |
| tariff | Free — "El Servicio no tiene costo" / "libre y sin costo para los usuarios" (IGM 2016 post). |
| hobbyist_eligibility | yes — open registration; no licence req stated. |
| legal_residency_required | unclear — Spanish-only portal; no explicit residency req; foreign users not excluded. |
| last_confirmed_alive | 2026-05-13 — `rtk.igm.gub.uy:2101` SOURCETABLE 200 OK, 96 STR entries. 2026-05-17 — IGM landing HTTP 200 (operator cost statement re-quoted), geoportal HTTP 200. |
| datum_epoch | omitted — no citable operator-portal declaration. (SIRGAS bulletins state SIRGAS-ROU98 @ 1995.4 but those are not IGM operator pages; primer rule disallows.) |

## Dec 2025 expansion

IGM added 8 multi-constellation CORS, COMNAV SinoGNSS M300 Pro receivers + SinoGNSS AT600 antennas, delivered via KPN METIOR. Densifies interior (Tacuarembó, Rivera, Artigas, Durazno, Flores). Older stations still RTCM3 GPS+GLO. Source: https://igm.gub.uy/2025/12/16/el-igm-incorpora-ocho-nuevas-estaciones-cors-para-fortalecer-la-regna-rou/

## Coverage / alternatives

- Free VRS = rare in S. America at no cost.
- Friction: Spanish-only portal.
- Commercial intl (RTKdata, geoRTK, TopNET Live): may claim UY via AR/BR-hosted stations; not UY-specific.
- Centipede / GEODNET: no UY nodes confirmed. 0 UY-tagged volunteer streams in stations.json 2026-05-17.

### RAMSAC (AR) cross-border + IGS — `stations_by_radius.py -34.9 -56.2 400` (2026-05-17)

22 RAMSAC stations within 400 km of Montevideo. RAMSAC = AR national CORS via IGN-AR; CC-licensed, free w/ registration. Nearest:
- `UYCO-v3.0` -34.46, -57.84 @ 158 km (Colonia, UY territory — coords tagged ARG by sourcetable but station IS in Uruguay; RAMSAC distributes for UY cross-border)
- `LPGS-v3.0` -34.90, -57.93 @ 158 km (La Plata, AR)
- `AGGO-v3.0` -34.87, -58.14 @ 177 km (AGGO Geodetic Obs, AR)
- `IGM1-v3.3` -34.57, -58.44 @ 208 km (IGN-AR HQ, Buenos Aires)
- `UYSO-v3.0` -33.26, -58.01 @ 247 km (Soriano, UY territory)
- `UYPA-v3.0` -32.29, -58.07 @ 338 km (Paysandú, UY territory)

Plus IGS-IP `AGGO00ARG0` and AUSCORS `LPGS00ARG0` within 160-180 km. RAMSAC `UYCO/UYSO/UYPA` are IGN-AR-hosted streams of UY-soil stations — usable cross-border but operator = AR, not REGNA-ROU.

## Post-processing (RINEX)

| Service | URL | Cost |
|---|---|---|
| IGM CORS RINEX | https://igm.gub.uy/geoportal/instructivos-2/ | Free (same account) |
| NOTA selected UY | https://www.earthscope.org/data/gnss-realtime/ | Free non-comm |

## Sources
- IGM REGNA-ROU service page: https://igm.gub.uy/2016/05/20/servicios-regna-rou/ (200 2026-05-17, "libre y sin costo")
- IGM geoportal instructivos: https://igm.gub.uy/geoportal/instructivos-2/ (200 2026-05-17)
- IGM Dec 2025 expansion: https://igm.gub.uy/2025/12/16/el-igm-incorpora-ocho-nuevas-estaciones-cors-para-fortalecer-la-regna-rou/
- SIRGAS bulletin (2022, Pampillon REGNA-ROU): https://sirgas.ipgh.org/docs/Boletines/Bol22/02-ServicioUruguayo-REGNA-ROU_RTK.pdf
- SIRGAS bulletin (2013, Yelicich et al.): https://www.sirgas.org/fileadmin/docs/Boletines/Bol18/35f_Yelicich_et_al_2013_Posicionamiento_GNSS_y_NTRIP-RTK.pdf
- GPS Uruguay primer: https://www.gpsuruguay.com/pages/como-funciona-el-sistema-rtk
- Live sourcetable probe 2026-05-13: `curl http://rtk.igm.gub.uy:2101/` → 200 OK, 96 STR entries.
- Radius probe 2026-05-17: `stations_by_radius.py -34.9 -56.2 400` (RAMSAC AR cross-border + IGS LPGS/AGGO visible).
