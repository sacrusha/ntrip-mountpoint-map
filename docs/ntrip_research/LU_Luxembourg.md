# Luxembourg [LU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free government NTRIP caster (SPSLux) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (SPSLux — free) |
| **host:port — SPSLux** | `stream.spslux.lu:5005` (IP: 185.106.24.68) |
| **VRS** | Yes — iMAX and VRS network correction types offered; both provide equivalent cm-level accuracy |
| **tariff** | Free — all SPSLux real-time and post-processing services are provided at no cost in line with Luxembourg's open-data policy |
| **hobbyist_eligibility** | yes — no professional licensing requirement stated; open registration |
| **legal_residency_required** | unclear — not explicitly required; open-data policy implies broad access; no restriction stated in public documentation |
| **last_confirmed_alive** | `stream.spslux.lu:5005` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl verified) |

## Context Notes

- **SPSLux** (Satellite Positioning System Luxembourg): National GNSS positioning network operated by the Administration du Cadastre et de la Topographie (ACT), Geodetic Department. Provides Network RTK (iMAX and VRS correction types) and DGNSS corrections in real time.
- **Infrastructure**: 13 continuously operating reference stations (some on international territory managed by partner networks). Provides horizontal accuracy of ~2–3 cm and vertical ~3–5 cm under good conditions.
- **Correction types / mountpoints**: iMAX (network corrections optimised for Leica equipment) and VRS (standard; compatible with all major receiver brands); DGNSS stream also available. Full mountpoint list downloadable from the ACT portal. Signals from GPS, GLONASS, Galileo, BeiDou processed.
- **Access**: Registration required via the ACT cadastre portal shop on first login (subscribe to "SPSLUX (N)RTK" package — zero cost). Mobile data (GSM/4G) required for real-time access.
- **Reference system**: ETRS89 / ITRF; delivers positions in Luxembourg national reference frame compatible with EUPOS standards.
- **Operator contact**: spslux@act.etat.lu

## Post-Processing (RINEX) Fallback

RINEX data available via the same ACT portal at no cost after registration. FTP access to archived observation files.

## Sources Consulted
- SPSLux service overview: https://act.public.lu/fr/gps-reseaux/spslux1.html
- SPSLux NTRIP/Caster page: https://act.public.lu/fr/gps-reseaux/spslux1/ntripcasterclient.html
- SPSLux access page: https://act.public.lu/fr/gps-reseaux/spslux1/1spsluxaccess.html
- SPSLux mountpoints page: https://act.public.lu/fr/gps-reseaux/spslux1/spsluxmountpoints.html
- ArduSimple Luxembourg RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-luxembourg/
- curl probe of `stream.spslux.lu:5005` — SOURCETABLE 200 OK confirmed 2026-05-06
