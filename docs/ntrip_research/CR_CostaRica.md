# Costa Rica [CR] — NTRIP RTK Research

**researched:** 2026-05-17 (prior: 2026-05-12)
**status:** YES — free national caster (IGN-CR / SNIT), 14 single-base mountpoints live; no VRS; volunteer bases supplement Pacific NW + Central Valley.

## Service A — IGN-CR / SNIT caster (national, free)

| field | value |
|---|---|
| landing_url | https://www.snitcr.go.cr/ |
| access_url | https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NTE5NTU5MQ%3D%3D |
| host:port | `igncaster.snitcr.go.cr:2101` (Server: NTRIP BKG Caster/2.0.44) |
| operator | IGN-CR (Instituto Geográfico Nacional, Registro Nacional, Ministerio de Justicia y Paz); SNIT portal |
| vrs | no — per-station only |
| num_stations | 14 physical CORS (1 STR = 1 station; all carry `Prueba` tag in misc field, residual since 2023 launch) |
| mountpoints | `QUEP3 LBRA3 NYCO3 SAGE3 NEIL3 CIQE3 PUNT3 RIDC3 LIMN3 BRBR3 CHLS3 LCRZ3 CAPO3 PJMZ3` — RTCM 3.3, 1004+1008 legacy (no MSM), GPS+GLO+GAL+BDS, hw `Trimble TRM159900.00 SCIS` |
| tariff | 0 CRC / $0 — SNIT account only; observed 2026-05-12 |
| hobbyist_eligibility | yes — open SNIT registration, no license |
| legal_residency_required | unclear — cédula or passport accepted on form, foreign-passport approval undocumented |
| last_confirmed_alive | 2026-05-12 — direct sourcetable fetch returned 14 STR + CAS + NET. Not re-tested 2026-05-17 (research date) — last verified 2026-05-12 portal + caster probe |
| datum_epoch | CR-SIRGAS, ITRF08 (IGb08), epoch 2014.59 / projection CRTM05. Cited: https://www.snitcr.go.cr/pdfs/normativa_tecnica/NTIG_CR01_06_2023%20V2%20MARCO%20DE%20REFERENCIA%20GEOD%C3%89SICO%20DE%20COSTA%20RICA.pdf (NTIG_CR01_06.2023 V2; Decree 40962-MJP supersedes CR05) |

### Registration
1. SNIT account → snitcr.go.cr
2. Herramientas → Herramientas GNSS → Caster, accept terms
3. Credentials activate at 00:00 + 12:00 CST (UTC−6). Wait ≤12 h.
4. Connect rover to `igncaster.snitcr.go.cr:2101`, pick nearest mountpoint. Baseline target <20 km; max <50 km (no VRS).

### Notes
- BKG caster, open-source. MSM not broadcast — rovers must accept legacy 1004 GPS L1+L2. Multi-constellation MSM (1077/1087/1097/1127) absent despite station tracking GPS+GLO+GAL+BDS.
- Network ref site = Curridabat / San José; sourcetable CAS = `Caster-Nacional-Costa-Rica`, country `CRI`, ref 9.92°N/-84.05°W.

## Service B — PX GNSS (private, commercial)
landing_url: http://pxgnss.com/ntrip/redpx.php  
~13 stations, no public pricing or host:port. Contact form. Aimed at surveying / agri. tariff: not published — quote on request via contact form. hobbyist_eligibility ?, residency ?.

## Volunteer fallback
- rtk2go: 3 CRI bases — `DGEOB1` Huacas 10.36N/-85.78W, `DoleVNC` Alajuela 10.36N/-84.25W, `OVSI` 10.00N/-84.11W (project archive 2026-05).
- EarthScope NOTA: 2 CRI streams — `QSEC_RTCM3P3` 9.84N/-85.36W, `VRAI_RTCM3P3` 9.92N/-83.19W (NULA registration).
Useful as backup while SNIT account validation pending.

## Post-processing
- SNIT RINEX: https://www.snitcr.go.cr/ (free, SNIT account)
- SIRGAS-CON: https://sirgas.ipgh.org/
- EarthScope archive: https://www.earthscope.org/data/ (NULA)

## Sources
- SNIT portal: https://www.snitcr.go.cr/ (HTTPS 200, 2026-05-12)
- IGN-CR caster announcement: https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NTE5NTU5MQ%3D%3D
- RIDC/NEIL/CAPO addition (Feb): https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NjA1MjY3OA%3D%3D
- Caster tutorial PDF: https://www.snitcr.go.cr/pdfs/tutoriales_presentaciones/HERRAMIENTA%20CASTER.pdf
- Datum NTIG_CR01_06.2023 V2: https://www.snitcr.go.cr/pdfs/normativa_tecnica/NTIG_CR01_06_2023%20V2%20MARCO%20DE%20REFERENCIA%20GEOD%C3%89SICO%20DE%20COSTA%20RICA.pdf
- Direct sourcetable fetch: `http://igncaster.snitcr.go.cr:2101/` → HTTP/1.1 200 SOURCETABLE, BKG 2.0.44, 14 STR (2026-05-12)
- PX GNSS: http://pxgnss.com/ntrip/redpx.php
- ArduSimple CR: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-costa-rica/

## Gaps
- Foreign-passport SNIT approval undocumented. Contact: snit.info@rnp.go.cr.
- MSM upgrade absent. MSM-only rovers must enable legacy 1004 fallback.
- `Prueba` test tag persists since 2023 launch — operational status confirmed, label residual.
