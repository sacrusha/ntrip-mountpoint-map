# Uruguay [UY] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status

YES — free national caster REGNA-ROU (IGM) with single-base + VRS + iMAX
nationwide. No commercial alternative verified. RAMSAC (AR) cross-border
stations are visible within practical single-base range of the Río de la
Plata coast and the Río Uruguay corridor (covered in `AR_Argentina.md`).

## REGNA-ROU — Instituto Geográfico Militar (IGM)

| Field | Value |
|---|---|
| operator | Instituto Geográfico Militar (IGM), Uruguay |
| landing_url | https://igm.gub.uy/2016/05/20/servicios-regna-rou/ (operator post: "libre y sin costo para los usuarios") |
| access_url | https://igm.gub.uy/geoportal/instructivos-2/ (geoportal "instructivos" — guides for use/configure). Bare signup: https://rtk.igm.gub.uy/sbc/ |
| access_type | free-signup |
| sourcetable | `rtk.igm.gub.uy:2101` (IP 201.217.132.178; `GNSS Spider 7.11.1.109/1.0`). `curl --http0.9` 2026-05-23 → 96 STR rows / 8,991 bytes (unchanged from cache). |
| coverage | Uruguay nationwide. VRS hull covers populated coast + interior with the Dec 2025 expansion densifying interior departments (Tacuarembó, Rivera, Artigas, Durazno, Flores). |
| num_stations | 35 unique physical CORS — deduped from 96 STR entries (per-format `-V2` legacy + `_MSM4` / `_GNSS_MSM3` variants of the same site). Reflects Dec 2025 +8 expansion. |
| vrs | yes — VRS + iMAX (`RTCM3-VRS`, `RTCM3-iMAX`, 13 zone-keyed VRS mountpoints `VRS-A/B/C/D/E/G/J/K/M/N/O/P/Z`, plus `VRS-MSM4` multi-constellation) |
| tariff | not applicable — "El Servicio no tiene costo" / "servicio de Corrección Diferencial en Tiempo Real (DGNSS/RTK) y Post Proceso (DGNSS/PP) libre y sin costo" (operator post 2016, re-verified 2026-05-23) |
| hobbyist_eligibility | yes — open registration; no licence requirement stated |
| residency_required | ? — Spanish-only portal; no explicit residency clause; foreign users not excluded but signup form not English-localised |
| datum_epoch | omitted — no citable operator-portal declaration (checked: igm.gub.uy/2016/05/20/servicios-regna-rou/ 2026-05-23; igm.gub.uy/geoportal/instructivos-2/ 2026-05-23; rtk.igm.gub.uy/sbc/ 2026-05-23). SIRGAS bulletins describe REGNA-ROU as SIRGAS-tied (SIRGAS-ROU98 @ 1995.4 in older docs), but those are SIRGAS publications, not IGM operator pages. |
| stations_source | sourcetable above + https://igm.gub.uy/geoportal/instructivos-2/ |

### Mountpoint conventions

Legacy single-base RTCM3 GPS+GLONASS streams (`UYMO`, `UYTD`, `UYAR`, …);
GPS+GLO+GAL+BDS multi-constellation MSM4 streams on newer stations
(`UYBU_MSM4`, `UYFS_MSM4`, `UYLA_MSM4`, `UYLM_MSM4`, `UYMA_MSM4`, `UYPT_MSM4`,
`UYRB_MSM4`, `UYSC_MSM4`, `UYSJ_MSM4`, …); 13 zone-keyed VRS mountpoints
(letters A,B,C,D,E,G,J,K,M,N,O,P,Z — note: not the full alphabet, F/H/I/L/Q/R/S/T/U/V/W/X/Y are absent), plus generic `RTCM3-VRS`, `RTCM3-iMAX`, and `VRS-MSM4`.

The cached sourcetable also exposes `IGM1` at (-34.57, -58.44) — that is the
IGN-AR HQ station in Buenos Aires (also in `ramsac.sourcetable`), rebroadcast
through REGNA-ROU's caster; and `UYBA` at (-62.18, -58.90), the Uruguayan
Artigas Antarctic Station on King George Island. Neither counts toward the
35-CORS UY-soil tally.

### Dec 2025 expansion

IGM added 8 multi-constellation CORS (COMNAV SinoGNSS M300 Pro receivers +
SinoGNSS AT600 antennas, delivered via KPN METIOR). Densifies the interior.
Total user base ~1,000 national + international users per IGM communications.
Source: https://igm.gub.uy/2025/12/16/el-igm-incorpora-ocho-nuevas-estaciones-cors-para-fortalecer-la-regna-rou/

## Coverage / alternatives

- Free VRS at no cost is rare in South America; REGNA-ROU is currently the only such service in the region.
- Friction: Spanish-only portal.
- Commercial international claims (RTKdata, TopNET Live) may include UY via AR/BR-hosted nodes; not UY-specific.
- Centipede / GEODNET / Onocoy: no UY nodes confirmed (0 UY-tagged volunteer streams in stations.json, 2026-05-23).

### RAMSAC (AR) cross-border + IGS — `stations_by_radius.py -34.9 -56.2 500` (2026-05-23)

106 stations within 500 km of Montevideo: regna_rou 69, ramsac 32 [ARG], igs_ip 1 [ARG], auscors 1 [ARG], rbmc_ip 1 [BRA], rtk2go 2 [ARG/BRA]. Note: 22 RAMSAC stations sit within 400 km of Montevideo. Nearest:

- `UYCO-v3.0` (-34.46, -57.84) ~ 158 km — Colonia del Sacramento, **physically on UY soil**, tagged ARG by RAMSAC sourcetable because operator = IGN-AR (IGN-AR accepts cross-border contributed nodes — see Tronix SRL / Asunción precedent in `AR_Argentina.md`; precise host-institution for UYCO not pinned in IGN public docs as of 2026-05-23)
- `LPGS-v3.0` (-34.90, -57.93) ~ 158 km — La Plata, AR
- `AGGO-v3.0` (-34.87, -58.14) ~ 177 km — AGGO Geodetic Obs, AR
- `IGM1-v3.3` (-34.57, -58.44) ~ 208 km — IGN-AR HQ, Buenos Aires
- `UYSO-v3.0` (-33.26, -58.01) ~ 247 km — Soriano, UY soil (RAMSAC-distributed)
- `UYPA-v3.0` (-32.29, -58.07) ~ 338 km — Paysandú, UY soil (RAMSAC-distributed)

Plus IGS-IP `AGGO00ARG0` and AUSCORS `LPGS00ARG0` within 160–180 km. The
RAMSAC `UYCO/UYSO/UYPA` streams are IGN-AR-hosted streams of UY-soil
contributing stations — usable cross-border but operator = AR, not REGNA-ROU.
See `AR_Argentina.md`.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| IGM CORS RINEX | https://igm.gub.uy/geoportal/instructivos-2/ | Free (same account) |
| NOTA selected UY | https://www.earthscope.org/data/gnss-realtime/ | Free non-commercial |
| RAMSAC RINEX (cross-border) | https://www.ign.gob.ar/NuestrasActividades/Geodesia/Ramsac | Free (IGN-AR registration) |

## Sources

- IGM REGNA-ROU service page: https://igm.gub.uy/2016/05/20/servicios-regna-rou/ (200 2026-05-23, "libre y sin costo" re-quoted)
- IGM geoportal instructivos: https://igm.gub.uy/geoportal/instructivos-2/
- IGM Dec 2025 +8 stations: https://igm.gub.uy/2025/12/16/el-igm-incorpora-ocho-nuevas-estaciones-cors-para-fortalecer-la-regna-rou/
- SIRGAS bulletin (2022, Pampillon REGNA-ROU): https://sirgas.ipgh.org/docs/Boletines/Bol22/02-ServicioUruguayo-REGNA-ROU_RTK.pdf
- SIRGAS bulletin (2013, Yelicich et al.): https://www.sirgas.org/fileadmin/docs/Boletines/Bol18/35f_Yelicich_et_al_2013_Posicionamiento_GNSS_y_NTRIP-RTK.pdf
- GPS Uruguay primer: https://www.gpsuruguay.com/pages/como-funciona-el-sistema-rtk
- Live sourcetable probe `curl --http0.9 http://rtk.igm.gub.uy:2101/` 2026-05-23 → 96 STR / 8,991 bytes
- Radius probe `stations_by_radius.py -34.9 -56.2 500` 2026-05-23 — RAMSAC AR + UY-soil stations cross-border, regna_rou national hull
