# Costa Rica [CR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free national NTRIP caster (IGN-CR / SNIT); registration required; plus one small private network

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | IGN-CR — Instituto Geográfico Nacional, within SNIT (Sistema Nacional de Información Territorial) |
| **host:port** | `igncaster.snitcr.go.cr:2101` |
| **VRS** | Unclear — mountpoints are per physical station; no confirmed VRS computed stream found |
| **tariff** | **Free — CRC 0 / $0.00.** SNIT account registration required. Date observed: 2026-05-06. Source: https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NTE5NTU5MQ%3D%3D |
| **hobbyist_eligibility** | **Yes** — no professional licence requirement stated; open registration via SNIT portal |
| **legal_residency_required** | **Unclear** — registration asks for cédula or passport; foreign access not explicitly blocked |
| **last_confirmed_alive** | SNIT portal (snitcr.go.cr) HTTP 200 confirmed 2026-05-06; IGN caster announced active via SNIT news post 2023 |

## Registration Process

1. Create a free SNIT account at `https://www.snitcr.go.cr/`
2. Navigate to Herramientas → Herramientas GNSS → Caster tool
3. Accept terms and conditions
4. Note: account credentials undergo a validation cycle at **12:00 midnight and 12:00 noon** Costa Rica time — initial access may require waiting up to 12 hours after registration
5. Connect GNSS receiver to `igncaster.snitcr.go.cr:2101`; select individual station mountpoint from the sourcetable

## Network Details

- **Operator:** IGN-CR (Instituto Geográfico Nacional de Costa Rica) under the Registro Nacional
- **Reference frame:** CR05 / CRTM05 (Costa Rica geodetic reference frame, ITRF-aligned)
- **CORS network:** National GNSS network — specific station count not publicly documented; the SNIT sourcetable shows individual station-coded mountpoints
- **Constellations:** Unknown (not publicly documented); likely GPS/GLONASS at minimum
- **Station PDF** (2023): https://www.snitcr.go.cr/pdfs/datos_informativos/Red%20de%20estaciones%20GNSS.pdf — describes RINEX download, post-processing, and NTRIP services

## Private / Commercial Option

**PX GNSS** (`pxgnss.com`) operates a private 13-station network across Costa Rica offering centimetre-accuracy RTK. Coverage zones: ~20 km radius per base (optimal), up to 50 km (degraded). No public pricing or NTRIP host/port published; contact via website form. This is a paid commercial service aimed at professional surveyors and agricultural users.

## Context Notes

- The SNIT caster is administered by the IGN-CR under the Registro Nacional del Ministerio de Justicia. The free service is described as part of the national territorial information infrastructure.
- YouTube tutorial (official IGN-CR): "Conexión a CORS GNSS Costa Rica por Ntrip Red Oficial IGN" — demonstrates live connection to igncaster.snitcr.go.cr.
- No VRS computed stream confirmed; if VRS is required, PX GNSS is the only identified option (unclear if they offer VRS).
- Costa Rica is absent from RTK2go and Centipede sourcetables.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SNIT RINEX download** — archive via SNIT Herramientas GNSS | https://www.snitcr.go.cr/ | Free (SNIT account required) |
| **SIRGAS regional archive** — limited Costa Rica stations | https://sirgas.ipgh.org/ | Free |

## Sources Consulted
- SNIT portal: https://www.snitcr.go.cr/
- SNIT IGN caster announcement: https://www.snitcr.go.cr/Noticias/detallenoticia2?id=bm90aWNpYTo6MTY3NTE5NTU5MQ%3D%3D
- SNIT GNSS PDF (accessed 2026-05-06): https://www.snitcr.go.cr/pdfs/datos_informativos/Red%20de%20estaciones%20GNSS.pdf
- PX GNSS network: http://pxgnss.com/ntrip/redpx.php
- Registro Nacional NTRIP guide: https://www.rnpdigital.com/Usos%20y%20aplicaciones%20de%20la%20red%20NTRIP%20del%20Registro%20Nacional.pdf
- YouTube IGN-CR tutorial: https://www.youtube.com/watch?v=Ha9wAJy-BJI
- ArduSimple Costa Rica page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-costa-rica/
