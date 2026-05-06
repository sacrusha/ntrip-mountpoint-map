# Senegal [SN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: ACTIVE public NTRIP caster — SENCORS

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | **Yes** |
| **host:port** | `caster.geodesie.sn:2101` |
| **tariff** | Not publicly disclosed. Subscription plan described as "3 mois (90 jours) — Forfaitaire — Illimitée" (90-day flat-rate, unlimited). Price in XOF/USD not visible without account login. null — contact ANAT: contact@anat.sn / +221 33 832 15 06. Date observed: 2026-05-06. Source: https://geodesie.sn/SBC/Account/Index |
| **hobbyist_eligibility** | Unclear — registration form requires username/password/name/email/company (free-text, no licence number). No stated restriction, but institutional context targets cadastral professionals. |
| **legal_residency_required** | Unclear — no residency requirement stated on public pages |
| **last_confirmed_alive** | 2026-05-04 (portal showed "Le réseau est opérationnel"; Leica SBC login page reachable 2026-05-06) |

## Network Details

- **Operator:** ANAT (Agence Nationale de l'Aménagement du Territoire) / DTGC
- **Software:** Leica Spider Business Center (SBC)
- **Portal:** https://geodesie.sn/ | Account: https://geodesie.sn/SBC/Account/Index
- **Stations:** ~19+ CORS stations nationwide
  - 16 PROCASEF stations (World Bank / IGN-FI + Leica Geosystems consortium, 2022–2024)
  - 5 JICA stations integrated 2025: DKR1, FATI, MBOU, NDAN, TIVA (5 more planned 2025/2026)
- **Service type:** Real-time NRTK (Network RTK / VRS)

## Timeline

| Date | Event |
|---|---|
| 2022–2024 | PROCASEF project installs 16 CORS stations across Senegal |
| Oct 2024 | Stations 12 & 13 installed (Touba hospital, Tambacounda aerodrome) |
| Early 2025 | SENCORS portal (geodesie.sn) goes online with Leica SBC |
| 2025 | 5 JICA stations integrated |
| Jan 7, 2026 | Critical disk failure — SENCORS goes offline |
| Mar 16, 2026 | **SENCORS restored** — `caster.geodesie.sn:2101` confirmed operational |
| May 4, 2026 | Network status: operational (last portal update) |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **SENCORS / geodesie.sn** — RINEX data download available via same Leica SBC portal as NTRIP | https://geodesie.sn/SBC/ | Same subscription as NTRIP (cost not publicly disclosed); contact contact@anat.sn |

## Sources
- https://geodesie.sn/?p=256 (SENCORS return announcement, 2026-03-16)
- https://geodesie.sn/ (status portal)
- https://procasef.com/avec-16-nouvelles-stations-cors-le-procasef-modernise-le-reseau-geodesique-du-senegal/
- https://ignfi.fr/en/implementation-of-the-geodetic-reference-network-in-senegal-procasef/
- https://anat.sn/actualites/modernisation-geodesique-au-senegal-5-stations-gps-cors-redefinissent-la-precision-des-donnees-geospatiales/9577/
- https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-senegal/
