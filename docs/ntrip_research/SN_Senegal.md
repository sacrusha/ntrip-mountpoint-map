# Senegal [SN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-probed sourcetable; unchanged from 2026-05-17 — 25 STR records, 22 physical stations)

## Status: ACTIVE public NTRIP caster — SENCORS

| Field | Value |
|---|---|
| **landing_url** | https://geodesie.sn/ (status portal — ANAT/DTGC operator) |
| **access_url** | https://geodesie.sn/SBC/Account/Index (Leica Spider Business Center registration + subscription order) |
| **Active public NTRIP RTK caster** | **Yes** |
| **host:port** | `caster.geodesie.sn:2101` (Leica GNSS Spider 7.11.1.109/1.0) |
| **num_stations** | 22 physical CORS (per live sourcetable 2026-05-21) |
| **vrs** | yes — `SENCORS-VRS` (network VRS, GPS+GLO+GAL), `SENCORS_i-MAX` (Leica i-MAX), `SENCORS-NEAR` (nearest-station alias, IGNFI-flagged). All three network products advertised nmea=1 in sourcetable. |
| **tariff** | Not publicly disclosed. Subscription plan described as "3 mois (90 jours) — Forfaitaire — Illimitée" (90-day flat-rate, unlimited). Price in XOF/USD not visible without account login. Contact ANAT: contact@anat.sn / +221 33 832 15 06. Date observed: 2026-05-21. Source: https://geodesie.sn/SBC/Account/Index |
| **hobbyist_eligibility** | ? — registration form requires username/password/name/email/company (free-text, no licence number). No stated restriction, but institutional context targets cadastral professionals. |
| **legal_residency_required** | ? — no residency requirement stated on public pages |
| **last_confirmed_alive** | 2026-05-21 — `curl --http0.9 -A NTRIP/1.0` of `caster.geodesie.sn:2101` returned `SOURCETABLE 200 OK` (Server: GNSS Spider 7.11.1.109/1.0; Content-Length 2886); 25 STR records (3 network products + 22 physical). `https://geodesie.sn/` portal status "Le réseau est opérationnel" (2026-05-04 12:02) still latest. |
| **datum_epoch** | omitted — no citable operator declaration. `geosenegal.gouv.sn` references "Système sénégalais de référence spatiale (SSRS)" managed by ANAT/DTGC with first IGS-connected GNSS in 2014, but does not publish ellipsoid / frame / epoch. |

## Network Details

- **Operator:** ANAT (Agence Nationale de l'Aménagement du Territoire) / DTGC (Direction des Travaux Géographiques et Cartographiques)
- **Software:** Leica Spider Business Center (SBC) — caster reports Server: GNSS Spider 7.11.1.109/1.0
- **Portal:** https://geodesie.sn/ | Account: https://geodesie.sn/SBC/Account/Index | Carto: https://geodesie.sn/xyz/ | RINEX: https://geodesie.sn/xyz/cdc
- **Network products:** `SENCORS-VRS` (VRS, GPS+GLO+GAL), `SENCORS-NEAR` (nearest-station, IGNFI tag), `SENCORS_i-MAX` (Leica i-MAX). All RTCM 3, advertised position 15.62°N -16.24°E (Louga area, central caster reference).
- **Physical mountpoints (live sourcetable 2026-05-21):** SENCORS_BAMB (Bambey 14.69/-16.44), SENCORS_TOUB (Touba 14.92/-15.93), SENCORS_LING (Linguère 15.40/-15.06), SENCORS_LOUG (Louga 15.62/-16.24), SENCORS_SOKO (13.87/-16.37), SENCORS_STLO (16.03/-16.49 — country tag `DSE` anomaly), SENCORS_BIGN (Bignona 12.81/-16.23), SENCORS_KEDO (Kédougou 12.56/-12.18), SENCORS_KIDI (14.47/-12.22 — country tag blank), SENCORS_KOLD (Kolda 12.89/-14.94), SENCORS_MATA (Matam 15.67/-13.26), SENCORS_NDIO (Ndioum 16.51/-14.65), SENCORS_RICH (Richard-Toll 16.46/-15.67), SENCORS_SEDH (Sédhiou 12.71/-15.56), SENCORS_TAMB (Tambacounda 13.73/-13.66), SENCORS_ZIGU (Ziguinchor 12.58/-16.27), SENCORS_NDAN (Ndangalma 15.28/-16.53), SENCORS_FATI (Fatick 14.34/-16.42), SENCORS_TIVA (Tivaouane 14.95/-16.81), SENCORS_DKR1 (Dakar 14.95/-16.81 — coords duplicate of TIVA, likely placeholder), SENCORS_MBOU (Mbour 14.72/-17.44), SENCORS_KAFF (Kaffrine 14.10/-15.55). **22 physical stations + 3 network products = 25 STR records.**
- **Service type:** Real-time NRTK (Network RTK / VRS + i-MAX + nearest-station + single-base)

## Timeline

| Date | Event |
|---|---|
| 2022–2024 | PROCASEF (World Bank, $80M, 2021–2026) installs 16 CORS stations under IGN FI / Leica Geosystems consortium |
| Sep 2023 | ANAT confirms acquisition of 5 JICA-funded CORS stations; install in Dakar region announced (anat.sn/9577) |
| Oct 2024 | Stations 12 & 13 installed (Touba hospital, Tambacounda aerodrome) |
| Dec 2024 | JICA experts meet ANAT to launch installation phase — physical install planned Sep 2025; first tests Sep 2026 (anat.sn/10619). Integration of the 5 JICA stations into the live SENCORS sourcetable is not confirmed in any identified source as of 2026-05-21 (current 22-station count is accounted for by PROCASEF rollout). |
| Early 2025 | SENCORS portal (geodesie.sn) goes online with Leica SBC |
| Jan 7, 2026 | Critical disk failure — SENCORS goes offline |
| Mar 16, 2026 | **SENCORS restored** — `caster.geodesie.sn:2101` confirmed operational |
| May 4, 2026 | Portal status: operational ("Le réseau est opérationnel") |
| May 17–21, 2026 | Sourcetable stable at 25 STR records (22 physical + 3 network products) |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **SENCORS / geodesie.sn** — RINEX data download available via same Leica SBC portal as NTRIP | https://geodesie.sn/SBC/ | Same subscription as NTRIP (cost not publicly disclosed); contact contact@anat.sn |

## Sources
- https://geodesie.sn/?p=256 (SENCORS return announcement, 2026-03-16)
- https://geodesie.sn/ (status portal — last update 2026-05-04 "Le réseau est opérationnel"; re-fetched 2026-05-21)
- https://geodesie.sn/SBC/Account/Index (Leica SBC subscription page; "Forfaitaire — Illimitée — 3 mois (90 jours)"; re-fetched 2026-05-21)
- https://procasef.com/avec-16-nouvelles-stations-cors-le-procasef-modernise-le-reseau-geodesique-du-senegal/
- https://ignfi.fr/en/implementation-of-the-geodetic-reference-network-in-senegal-procasef/
- https://anat.sn/actualites/modernisation-geodesique-au-senegal-5-stations-gps-cors-redefinissent-la-precision-des-donnees-geospatiales/9577/ (Sep 2023 — JICA station acquisition)
- https://anat.sn/actualites/modernisation-du-reseau-geodesique-le-senegal-va-se-doter-de-5-nouvelles-stations-cors-grace-a-la-jica/10619/ (Dec 2024 — JICA install planned Sep 2025, tests Sep 2026)
- https://www.geosenegal.gouv.sn/systeme-senegalais-de-reference-spatiale.html (SSRS — ANAT/DTGC; no published datum/epoch parameters)
- https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-senegal/
- TCP probe of `caster.geodesie.sn:2101` 2026-05-21 → SOURCETABLE 200 OK, 25 STR records, Server: GNSS Spider 7.11.1.109/1.0
- Local data: `py scripts/stations_by_country.py SEN` → Centipede 2 SN nodes (NKHR Ndoffane area 14.479/-16.404, GORA Gorée/Dakar 14.785/-17.311) + IGS-IP DAKR (14.72/-17.44 Dakar). These supplement SENCORS — independent caster footprints.
