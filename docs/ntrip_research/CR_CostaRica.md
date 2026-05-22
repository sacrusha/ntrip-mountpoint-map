# Costa Rica [CR] — NTRIP RTK Research

**Date researched:** 2026-05-22 (IGN-CR caster re-probed: 12 STR + BKG 2.0.44 sourcetable returned; CR-SIRGAS decree confirmed in NTIG_CR01_06.2023 V2; PX GNSS still equipment-tied. LCRZ3 and PJMZ3 absent from today's sourcetable — earlier captures listed 14, intermittent or decommissioned)

## Status: YES — free national caster (IGN-CR / SNIT) with 12 single-base CORS streams in live sourcetable as of 2026-05-22. No VRS. Volunteer + EarthScope NOTA + IGS-IP rebroadcast supplement Pacific NW and Central Valley.

## Service A — IGN-CR / SNIT caster (national, free)

| Field | Value |
|---|---|
| landing_url | https://www.snitcr.go.cr/ |
| access_url | https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NTE5NTU5MQ%3D%3D (caster announcement; SNIT account at https://gnss.rnp.go.cr/SBC/Account/Index?returnUrl=%2FSBC) |
| host:port | `igncaster.snitcr.go.cr:2101` (Server: NTRIP BKG Caster/2.0.44) |
| operator | IGN-CR (Instituto Geográfico Nacional, Registro Nacional, Ministerio de Justicia y Paz); SNIT portal |
| num_stations | 12 STR present in live sourcetable 2026-05-22 (earlier 2026-05-12 captures listed 14 including LCRZ3 and PJMZ3 — both absent today, status uncertain: intermittent dropout or decommissioned. 1 STR = 1 station; all carry `Prueba` tag in misc field, residual since 2023 launch) |
| mountpoints | `QUEP3 LBRA3 NYCO3 SAGE3 NEIL3 CIQE3 PUNT3 RIDC3 LIMN3 BRBR3 CHLS3 CAPO3` — all RTCM 3.3, legacy msg 1004+1008 (no MSM), GPS+GLO+GAL+BDS, receiver Trimble TRM159900.00 SCIS. `LCRZ3` (La Cruz, Guanacaste NW) and `PJMZ3` (Pejibaye / Pérez Zeledón area) seen in prior probes, absent from 2026-05-22 sourcetable |
| vrs | No — per-station only |
| tariff | 0 CRC / USD 0 — SNIT account only |
| hobbyist_eligibility | Yes — open SNIT registration, no surveyor licence required |
| legal_residency_required | Unclear — cédula or passport accepted on form; foreign-passport approval undocumented in operator-side materials. Contact `snit.info@rnp.go.cr` for non-CR applicant clarification |
| last_confirmed_alive | 2026-05-22 — direct sourcetable fetch from `igncaster.snitcr.go.cr:2101` returned `SOURCETABLE 200 OK` (NTRIP BKG Caster 2.0.44/2.0), 12 STR + 1 CAS + 1 NET. SNIT portal HTTP 200. Caster `Caster-Nacional-Costa-Rica`, ref 9.92°N/-84.05°W |
| datum_epoch | **CR-SIRGAS, ITRF08 (IGb08), epoch 2014.59 / projection CRTM05** — Decree 40962-MJP (24 Jan 2018, Gaceta 66 of 17 Apr 2018) supersedes prior CR05. Cited in NTIG_CR01_06.2023 V2: "Su primera definición está alineada a la solución IGb08 del ITRF08 en la época 2014.59". URL: https://www.snitcr.go.cr/pdfs/normativa_tecnica/NTIG_CR01_06_2023%20V2%20MARCO%20DE%20REFERENCIA%20GEOD%C3%89SICO%20DE%20COSTA%20RICA.pdf |

### Registration

1. Create SNIT account at https://www.snitcr.go.cr/ (Crear cuenta)
2. Herramientas → Herramientas GNSS → Caster, accept terms
3. Credentials activate at 00:00 or 12:00 CST (UTC−6); wait ≤12 h
4. Connect rover to `igncaster.snitcr.go.cr:2101`, pick nearest mountpoint. Baseline target <20 km; max usable <50 km (no VRS, single-base degrades via ppm)

### Notes

- BKG caster, open-source. MSM is **not** broadcast — rovers must accept legacy 1004 GPS L1+L2. Multi-constellation MSM (1077/1087/1097/1127) absent despite station tracking GPS+GLO+GAL+BDS.
- `Prueba` test tag persists since 2023 launch on all 14 mountpoints — operational status confirmed, label residual; not a maturity indicator.

## Service B — PX GNSS (private, equipment-tied)

| Field | Value |
|---|---|
| landing_url | http://pxgnss.com/ntrip/redpx.php (operator page describing the NTRIP network) |
| access_url | Skip — access bundled with PX GNSS equipment purchase; no standalone subscription page found |
| operator | PX (San José; equipment dealer + network operator) |
| num_stations | 13 PX-operated bases as of 2026-05-22 (operator page `redpx.php`: "actualmente con 13 bases y está en constante crecimiento"). PX's homepage additionally markets access to "free bases + IGN bases" — effectively a bundling of PX's own + the IGN-CR free caster (~50 bases total advertised) |
| vrs | No — coverage circles around per-station radii (green 20 km / yellow 35 km / red 50 km) on operator page |
| tariff | Not publicly published; bundled with equipment purchase. Public-page accuracy claims: <4 cm at 20 km / <8 cm at 35 km / <15 cm at 50 km |
| hobbyist_eligibility | Unclear — operator copy targets surveyors; equipment-gated access blocks rover-only hobbyist sign-up |
| legal_residency_required | Unclear |
| last_confirmed_alive | 2026-05-22 — `pxgnss.com/ntrip/redpx.php` reachable; coverage map shows 13 bases |
| datum_epoch | omitted — no operator-side declaration |

## Service C — volunteer + foreign-operated free streams

`py scripts/stations_by_country.py CRI` 2026-05-22 returns 20 stations across 4 sources: 12 IGN-CR (above) + 3 IGS-IP + 2 EarthScope NOTA + 3 rtk2go.

| Source | Stations | Notes |
|---|---|---|
| rtk2go | `DGEOB1` (Huacas 10.36 N -85.78 W), `DoleVNC` (Alajuela 10.36 N -84.25 W), `OVSI` (10.00 N -84.11 W) | Free; community bases, no QoS |
| EarthScope NOTA | `QSEC_RTCM3P3` (9.84 N -85.36 W, Nicoya peninsula), `VRAI_RTCM3P3` (9.92 N -83.19 W, Caribbean side) | `ntrip.earthscope.org:2101`; free non-commercial via NULA; commercial USD 1,000/seat/yr. Datum ITRF2014 / NOTA epoch 2026-03-30 |
| BKG IGS-IP rebroadcast | `CIQE00CRI0`, `NEIL00CRI0`, `SAGE00CRI0` (each at the corresponding IGN-CR station location) | `www.igs-ip.net:2101`; free BKG account. Source: IGN-CR feed surfaced via IGS-IP. Useful as a no-CR-account fallback for the same physical CORS |

## Post-processing

- SNIT RINEX: https://www.snitcr.go.cr/ (free, SNIT account) — same station network as the caster
- SIRGAS-CON RINEX: https://sirgas.ipgh.org/
- EarthScope archive: https://www.earthscope.org/data/ (NULA)

## Sources

- SNIT portal: https://www.snitcr.go.cr/ (HTTPS 200 2026-05-22)
- IGN-CR caster announcement (Feb 2023): https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NTE5NTU5MQ%3D%3D
- RIDC/NEIL/CAPO addition announcement: https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NjA1MjY3OA%3D%3D
- Caster tutorial PDF: https://www.snitcr.go.cr/pdfs/tutoriales_presentaciones/HERRAMIENTA%20CASTER.pdf
- Datum NTIG_CR01_06.2023 V2 (CR-SIRGAS / ITRF08 IGb08 / epoch 2014.59): https://www.snitcr.go.cr/pdfs/normativa_tecnica/NTIG_CR01_06_2023%20V2%20MARCO%20DE%20REFERENCIA%20GEOD%C3%89SICO%20DE%20COSTA%20RICA.pdf
- Decree 40962-MJP (supersedes CR05): cited inside NTIG_CR01_06.2023 V2; Gaceta No. 66 of 17 Apr 2018
- Direct sourcetable fetch: `http://igncaster.snitcr.go.cr:2101/` → SOURCETABLE 200 OK, BKG 2.0.44, 12 STR (2026-05-22; prior 2026-05-12 capture had 14 STR including LCRZ3 + PJMZ3, both absent today)
- PX GNSS network page (13 PX bases): http://pxgnss.com/ntrip/redpx.php
- PX GNSS homepage (equipment-tied access): https://pxgnss.com/es/
- BKG IGS-IP sourcetable (CIQE00CRI0 / NEIL00CRI0 / SAGE00CRI0): `www.igs-ip.net:2101`
- ArduSimple CR: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-costa-rica/
- Local pipeline `py scripts/stations_by_country.py CRI` 2026-05-22: 12 ign_cr_cors + 3 igs_ip + 2 earthscope + 3 rtk2go = 20 MPs

## Gaps

- Foreign-passport SNIT approval undocumented. Contact `snit.info@rnp.go.cr` for clarification.
- MSM upgrade absent on IGN-CR caster. MSM-only rovers must enable legacy 1004 fallback.
- `Prueba` test tag still on every IGN-CR STR since 2023 — operational status confirmed by sourcetable presence, label residual.
- PX GNSS tariff not public; access tied to equipment purchase, not directly evaluable as a hobbyist path.
- LCRZ3 + PJMZ3 status: absent from 2026-05-22 sourcetable, present 2026-05-12. Could be intermittent maintenance or decommissioning; SNIT has not announced status change. Re-probe on next research pass.
