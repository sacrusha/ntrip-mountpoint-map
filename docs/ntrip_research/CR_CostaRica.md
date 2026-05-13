# Costa Rica [CR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: YES — free national NTRIP caster (IGN-CR / SNIT), 14 physical CORS confirmed live on direct sourcetable fetch 2026-05-12; per-station mountpoints only (no VRS computed stream); registration via SNIT account; plus one small private network (PX GNSS)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | IGN-CR — Instituto Geográfico Nacional, within Registro Nacional / SNIT (Sistema Nacional de Información Territorial) |
| **host:port** | `igncaster.snitcr.go.cr:2101` (Server: NTRIP BKG Caster/2.0.44; confirmed via direct sourcetable fetch 2026-05-12; HTTP/1.1 200 SOURCETABLE; 14 STR mountpoints; CAS record advertises the same caster as `Caster-Nacional-Costa-Rica`, country `CRI`, ref point 9.92°N / -84.05°W (Curridabat/San José)) |
| **VRS** | No — sourcetable shows 14 per-station mountpoints in format `<SITE>3` (e.g., `QUEP3`, `LBRA3`); no VRS/MAX/iMAX/network-solution mountpoints visible. Reference Stations field on every STR record is `2` (i.e., single-site) |
| **Mountpoints (14)** | `QUEP3` Quepos (9.42°N, -84.17°W) · `LBRA3` Liberia (10.63°N, -85.44°W) · `NYCO3` Nicoya (10.14°N, -85.46°W) · `SAGE3` San-Isidro-PZ (9.37°N, -83.70°W) · `NEIL3` Ciudad-Neilly (8.64°N, -82.94°W) · `CIQE3` Ciudad-Quesada (10.32°N, -84.43°W) · `PUNT3` Puntarenas (9.98°N, -84.83°W) · `RIDC3` Curridabat (9.92°N, -84.05°W) · `LIMN3` Limón (9.99°N, -83.03°W) · `BRBR3` Bribri (9.62°N, -82.82°W) · `CHLS3` Los-Chiles (11.03°N, -84.71°W) · `LCRZ3` La-Cruz (11.08°N, -85.63°W) · `CAPO3` Cariari (10.37°N, -83.73°W) · `PJMZ3` Puerto-Jiménez (9.54°N, -83.31°W) — all RTCM 3.3, GPS+GLO+GAL+BDS (4-constellation), 1004(1) + 1008(10) cycle, identified hardware "Trimble TRM159900.00 SCIS", "Prueba" (test) tag on all streams |
| **Constellations** | GPS, GLONASS, Galileo, BeiDou (all 14 stations) — confirmed on sourcetable |
| **RTCM format** | RTCM 3.3, message types 1004 (legacy GPS L1+L2 obs) + 1008 (antenna descriptor) only; no MSM messages observed — single-frequency / dual-frequency RTK works but newer RTCM 3.3 MSM rovers will fall back to legacy mode |
| **tariff** | **Free — CRC 0 / $0.00.** SNIT account registration required. Date observed: 2026-05-12. Source: https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NTE5NTU5MQ%3D%3D |
| **VAT status** | N/A — service is free of charge |
| **hobbyist_eligibility** | **Yes** — no professional licence requirement stated; open registration via SNIT portal |
| **legal_residency_required** | **Unclear** — registration asks for cédula (Costa Rican national ID) or passport; foreign access not explicitly blocked, but no documented confirmation of foreign-only-passport acceptance |
| **last_confirmed_alive** | 2026-05-12 — direct sourcetable fetch `http://igncaster.snitcr.go.cr:2101/` returned 14 STR records + CAS + NET (Server: NTRIP BKG Caster/2.0.44). Portal `snitcr.go.cr` HTTPS 200 |

## Registration Process

1. Create a free SNIT account at `https://www.snitcr.go.cr/` (Servicio Nacional de Información Territorial)
2. Navigate to **Herramientas → Herramientas GNSS → Caster** (lateral navigation bar)
3. Accept the terms and conditions of use ("Acepto los términos y condiciones")
4. **Validation window**: account credentials are activated against the caster at **12:00 midnight and 12:00 noon** Costa Rica time (UTC−6). Initial access may require waiting up to 12 hours after registration.
5. Connect GNSS receiver to `igncaster.snitcr.go.cr:2101` and select an individual station mountpoint from the sourcetable nearest to the work site (baseline <~50 km for RTK fix; <~20 km for production accuracy)

## Network Details

- **Operator:** IGN-CR (Instituto Geográfico Nacional de Costa Rica) under the Registro Nacional, Ministerio de Justicia y Paz
- **Caster software:** BKG NtripCaster 2.0.44 (open-source, free reference implementation from Germany's BKG)
- **Reference frame:** CR05 / CRTM05 (Costa Rica geodetic reference frame, ITRF-aligned)
- **CORS network:** 14 physical stations as of 2026-05-12 (verified via sourcetable). Per the SNIT GNSS PDF, the Registro Nacional maintains the national CORS network with RINEX archive and online post-processing also available
- **Constellations:** GPS, GLONASS, Galileo, BeiDou (all four on every active stream; confirmed by sourcetable observed 2026-05-12)
- **No VRS computed stream:** The caster broadcasts per-physical-station only. For sites further than ~20 km from the nearest station, RTK fix quality will degrade; users wanting network RTK across Costa Rica need PX GNSS or self-operated VRS

## Private / Commercial Option

**PX GNSS** (`pxgnss.com`) operates a private 13-station network across Costa Rica offering centimetre-accuracy RTK. Coverage zones: ~20 km radius per base (optimal), up to 50 km (degraded). No public pricing or NTRIP host/port published; contact via website form. This is a paid commercial service aimed at professional surveyors and agricultural users.

## Context Notes

- The SNIT caster is administered by the IGN-CR under the Registro Nacional del Ministerio de Justicia. The free service is described as part of the national territorial information infrastructure.
- YouTube tutorial (official IGN-CR): "Conexión a CORS GNSS Costa Rica por Ntrip Red Oficial IGN" — demonstrates live connection to igncaster.snitcr.go.cr.
- No VRS computed stream confirmed; if VRS is required, PX GNSS is the only identified option (unclear if they offer VRS).
- **Volunteer alternative**: rtk2go has 3 CRI-coded bases (`DGEOB1` 10.36°N/-85.78°W Liberia/Guanacaste, `DoleVNC` 10.36°N/-84.25°W, `OVSI` 10.00°N/-84.11°W) per `data/rtk2go.sourcetable` 2026-05; EarthScope has 2 CRI stations (`QSEC_RTCM3P3` 9.84°N/-85.36°W, `VRAI_RTCM3P3` 9.92°N/-83.19°W). Both are useful as cross-check or backup if the SNIT account validation is delayed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SNIT RINEX download** — archive via SNIT Herramientas GNSS | https://www.snitcr.go.cr/ | Free (SNIT account required) |
| **SIRGAS regional archive** — Costa Rica stations contributed to SIRGAS-CON | https://sirgas.ipgh.org/ | Free |
| **EarthScope/UNAVCO** — limited CR stations cross-listed | https://www.earthscope.org/data/ | Free (NULA account) |

## Sources Consulted
- SNIT portal: https://www.snitcr.go.cr/ (HTTPS 200; 2026-05-12)
- SNIT IGN caster announcement: https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NTE5NTU5MQ%3D%3D
- SNIT GNSS reconnection notice: https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NjA1MjY3OA%3D%3D
- SNIT GNSS PDF (accessed 2026-05-12): https://www.snitcr.go.cr/pdfs/datos_informativos/Red%20de%20estaciones%20GNSS.pdf
- SNIT Herramienta Caster tutorial PDF: https://www.snitcr.go.cr/pdfs/tutoriales_presentaciones/HERRAMIENTA%20CASTER.pdf
- **Direct sourcetable fetch (2026-05-12, research env)**: `http://igncaster.snitcr.go.cr:2101/` returned HTTP/1.1 200 SOURCETABLE, NTRIP BKG Caster/2.0.44, 14 STR + 1 CAS + 1 NET
- PX GNSS network: http://pxgnss.com/ntrip/redpx.php
- Registro Nacional NTRIP guide: https://www.rnpdigital.com/Usos%20y%20aplicaciones%20de%20la%20red%20NTRIP%20del%20Registro%20Nacional.pdf
- YouTube IGN-CR tutorial: https://www.youtube.com/watch?v=Ha9wAJy-BJI
- ArduSimple Costa Rica page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-costa-rica/

## Known Data Gaps
- **Foreign-resident registration outcome**: SNIT registration form accepts foreign passports for ID, but no public confirmation that IGN-CR routinely approves foreign-passport-only NTRIP subscriptions. Direct contact with `snit.info@rnp.go.cr` recommended.
- **MSM upgrade**: Sourcetable advertises only legacy RTCM 3 messages (1004 + 1008); modern multi-constellation MSM (1077/1087/1097/1127) is not broadcast even though receivers track GPS+GLO+GAL+BDS. Users with MSM-only rovers should configure RTCM 3 legacy compatibility.
- **"Prueba" (test) tag**: All 14 STR records carry a `Prueba` (test) note in the misc field. Service has been described as operational since 2023; whether the test tag is a residual label or indicates ongoing validation is unconfirmed.
