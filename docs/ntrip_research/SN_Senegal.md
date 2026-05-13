# Senegal [SN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13

## Status: ACTIVE public NTRIP caster — SENCORS

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | **Yes** |
| **host:port** | `caster.geodesie.sn:2101` (Leica GNSS Spider 7.11.1.109/1.0) |
| **tariff** | Not publicly disclosed. Subscription plan described as "3 mois (90 jours) — Forfaitaire — Illimitée" (90-day flat-rate, unlimited). Price in XOF/USD not visible without account login. Contact ANAT: contact@anat.sn / +221 33 832 15 06. Date observed: 2026-05-13. Source: https://geodesie.sn/SBC/Account/Index |
| **hobbyist_eligibility** | Unclear — registration form requires username/password/name/email/company (free-text, no licence number). No stated restriction, but institutional context targets cadastral professionals. |
| **legal_residency_required** | Unclear — no residency requirement stated on public pages |
| **last_confirmed_alive** | 2026-05-13 — TCP probe of `caster.geodesie.sn:2101` returned `SOURCETABLE 200 OK` (Server: GNSS Spider 7.11.1.109/1.0); 24 STR mountpoints visible. Portal `https://geodesie.sn/` showed "Le réseau est opérationnel" on 2026-05-04 at 12:02. |

## Network Details

- **Operator:** ANAT (Agence Nationale de l'Aménagement du Territoire) / DTGC
- **Software:** Leica Spider Business Center (SBC) — caster reports Server: GNSS Spider 7.11.1.109/1.0
- **Portal:** https://geodesie.sn/ | Account: https://geodesie.sn/SBC/Account/Index | Carto: https://geodesie.sn/xyz/ | RINEX: https://geodesie.sn/xyz/cdc
- **Network products (from live sourcetable 2026-05-13):** `SENCORS-VRS` (network VRS, GPS+GLO+GAL), `SENCORS-NEAR` (nearest-station, IGNFI tag), `SENCORS_i-MAX` (Leica i-MAX network solution). All RTCM 3, position 15.62°N -16.24°E (Dakar / central caster reference).
- **Individual station mountpoints visible in sourcetable (2026-05-13):** SENCORS_BAMB (Bambey 14.69/-16.44), SENCORS_TOUB (Touba 14.92/-15.93), SENCORS_LING (Linguère 15.40/-15.06), SENCORS_LOUG (Louga 15.62/-16.24), SENCORS_SOKO (13.87/-16.37), SENCORS_STLO (16.03/-16.49), SENCORS_BIGN (Bignona 12.81/-16.23), SENCORS_KEDO (Kédougou 12.56/-12.18), SENCORS_KIDI (14.47/-12.22), SENCORS_KOLD (Kolda 12.89/-14.94), SENCORS_MATA (Matam 15.67/-13.26), SENCORS_NDIO (Ndioum 16.51/-14.65), SENCORS_RICH (Richard-Toll 16.46/-15.67), SENCORS_SEDH (Sédhiou 12.71/-15.56), SENCORS_TAMB (Tambacounda 13.73/-13.66), SENCORS_ZIGU (Ziguinchor 12.58/-16.27), SENCORS_NDAN (Ndangalma 15.28/-16.53), SENCORS_FATI (Fatick 14.34/-16.42), SENCORS_TIVA (Tivaouane 14.95/-16.81), SENCORS_DKR1 (Dakar 14.95/-16.81), SENCORS_MBOU (Mbour 14.72/-17.44). **21 physical stations visible** plus the three network products = ~24 mountpoint records.
- **Service type:** Real-time NRTK (Network RTK / VRS + i-MAX + nearest-station + single-base)

## Timeline

| Date | Event |
|---|---|
| 2022–2024 | PROCASEF project installs 16 CORS stations across Senegal |
| Oct 2024 | Stations 12 & 13 installed (Touba hospital, Tambacounda aerodrome) |
| Early 2025 | SENCORS portal (geodesie.sn) goes online with Leica SBC |
| 2025 | 5 JICA stations integrated |
| Jan 7, 2026 | Critical disk failure — SENCORS goes offline |
| Mar 16, 2026 | **SENCORS restored** — `caster.geodesie.sn:2101` confirmed operational |
| May 4, 2026 | Network status: operational (last portal update on geodesie.sn) |
| May 13, 2026 | Live TCP probe of `caster.geodesie.sn:2101` returned `SOURCETABLE 200 OK`; 24 mountpoints (3 network products + 21 single-station + cross-border tags) |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **SENCORS / geodesie.sn** — RINEX data download available via same Leica SBC portal as NTRIP | https://geodesie.sn/SBC/ | Same subscription as NTRIP (cost not publicly disclosed); contact contact@anat.sn |

## Sources
- https://geodesie.sn/?p=256 (SENCORS return announcement, 2026-03-16)
- https://geodesie.sn/ (status portal — last update 2026-05-04 "Le réseau est opérationnel")
- https://procasef.com/avec-16-nouvelles-stations-cors-le-procasef-modernise-le-reseau-geodesique-du-senegal/
- https://ignfi.fr/en/implementation-of-the-geodetic-reference-network-in-senegal-procasef/
- https://anat.sn/actualites/modernisation-geodesique-au-senegal-5-stations-gps-cors-redefinissent-la-precision-des-donnees-geospatiales/9577/
- https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-senegal/
- TCP probe of `caster.geodesie.sn:2101` 2026-05-13 → SOURCETABLE 200 OK, 24 STR records, Server: GNSS Spider 7.11.1.109/1.0
- Local data check 2026-05-13: `py scripts/stations_by_country.py SEN` → Centipede 2 SN nodes (GORA, NKHR — both in/near Dakar region), supplementing SENCORS.
