# Croatia [HR] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-12)
**status:** YES — CROPOS national NRTK; VPPS (Network RTK / VRS) free since 2022; only registration (40 EUR one-off) and GPPS post-processing remain billed.

## CROPOS — Croatian Positioning System

| field | value |
|---|---|
| landing_url | https://www.cropos.hr/ |
| access_url | https://www.cropos.hr/o-sustavu/naknade-za-koristenje-podataka-cropos-sustava |
| operator | Državna geodetska uprava (DGU) — State Geodetic Administration |
| host:port | `gnss.cropos.hr:2101` (alt `195.29.198.194:2101`) — live `SOURCETABLE 200 OK` from `NTRIP Trimble Ntrip Caster 5.2`, 15 STR rows, 2026-05-21 |
| num_stations | 41 Croatian CORS (after April 2025 Čazma + Daruvar additions; DGU also fuses 18 cross-border stations into the network solution) |
| vrs | yes — sourcetable is exclusively network/VRS mountpoints; no per-station single-base mounts published |
| tariff — VPPS (Network RTK / VRS) | **Free** since 7 April 2022 (Narodne novine 39/2022) |
| tariff — DPS (Differential / sub-metre) | **Free** since 7 April 2022 — out of scope (DGNSS, carrier 0) but noted |
| tariff — registration (one-time) | 40,00 EUR — observed 2026-05-21 on cropos.hr fees page, per Pravilnik NN 56/2023 + NN 106/25 |
| tariff — GPPS (post-processing) | 0,06 EUR / minute — observed 2026-05-21 on cropos.hr fees page (same regulation) |
| tariff — archived data | 0,06 EUR/min retrieval + 30,00 EUR/hour preparation |
| VAT | Croatia 25%; CROPOS fees page lists figures in EUR per the cited regulation, VAT treatment per HR tax rules |
| hobbyist_eligibility | yes — natural persons may register; no surveying-licence requirement; one-off 40 EUR covers free RTK |
| legal_residency_required | ? — registration is by email to `cropos@dgu.hr` (or post / fax to DGU Zagreb); no explicit residency clause |
| last_confirmed_alive | 2026-05-21 — `195.29.198.194:2101` SOURCETABLE 200 OK, 15 STR rows, `NTRIP Trimble Ntrip Caster 5.2`, 2276 bytes |
| datum_epoch | omitted — no citable operator declaration of epoch on cropos.hr. HTRS96 (≡ ETRS89) is the national frame and `CROPOS_VRS_HTRS96` / `CROPOS_VRS_GGG_HTRS96` mountpoints exist; HDKS (Hrvatski Državni Koordinatni Sustav) streams also published for legacy work. |

### Sourcetable (2026-05-21)

15 VRS-only streams. Trimble Pivot Platform zeroes the published coordinates (`HRV;0;0`).

| Mount | Format | Constellations |
|---|---|---|
| `CROPOS_VRS_RTCM31` | RTCM 3.1 | GPS+GLO |
| `CROPOS_VRS_DGNSS` | RTCM 2.3 | GPS+GLO (sub-metre) |
| `CROPOS_VRS_HTRS96` | RTCM 3.1 | GPS+GLO (native HTRS96/ETRF) |
| `CROPOS_VRS_HDKS` | RTCM 3.1 | GPS+GLO (legacy Croatian grid) |
| `CROPOS_VRS_HDKS_NE` / `_NW` | RTCM 3.1 | GPS+GLO (HDKS zoned) |
| `CROPOS_VRS_CMRx` | RTCM 3.1 | GPS+GLO (CMRx framing) |
| `CROPOS_VRS_GGG_CMRx` | CMRx | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_DGNSS` | RTCM 2.4 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_HDKS` / `_NE` / `_NW` | RTCM 3.2 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_HTRS96` | RTCM 3.2 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_GGG_RTCM32` | RTCM 3.2 | GPS+GLO+GAL+BDS+QZS |
| `CROPOS_VRS_RTCM23` | RTCM 2.3 | GPS+GLO |

`_GGG_` prefix = full-GNSS quad-constellation network solution; non-`GGG_` are GPS+GLO only.

## Context

- Launched 9 Dec 2008. Densification campaigns added 5 stations (Split, Zagreb, Jastrebarsko, Glina, Pazin) in Feb 2023 and 2 stations (Čazma, Daruvar) in early April 2025; DGU plans a further 2 by end of 2025. Total Croatian CORS now 41 plus 18 cross-border feeds.
- Free-RTK basis: Law on Amendments to the Law on State Survey and Real Estate Cadastre (NN 39/2022, eff. 2022-04-07) abolished VPPS and DPS charges. Only registration + GPPS remain billable. Cropos.hr landing page still quotes legacy kuna figures (300 kn registration / 0,5 kn per minute) in narrative text; **the fees page under the same site supersedes them with current EUR amounts per Pravilnik NN 56/2023 + NN 106/25.**
- Reference frame: HTRS96 (Croatian Terrestrial Reference System 1996, the Croatian realization of ETRS89). HDKS streams cover legacy Croatian state grid uses.
- Registration: email scan/sign to `cropos@dgu.hr` or post/fax to DGU Zagreb (Gruška 20, +385 1 6165 430); 40 EUR registration fee; credentials issued after approval.
- Portal `gnss.cropos.hr` provides station status + post-processing access.

## Volunteer / cross-border free supplement

- **rtk2go (`HRV` in stations.json + live `rtk2go.sourcetable` 2026-05-21)**: 2 community bases — `Tiho1234` (Miholec, 46.05 N 16.44 E, RTCM 3.2) and `VargaRTKhr` (Sivica, 46.44 N 16.50 E, RTCM 3.2). Both in northern Croatia near the SLO/HU border. Marginal supplement only; the rest of HR is fully served by free CROPOS VPPS.
- **Centipede**: zero HRV nodes in the live caster sourcetable 2026-05-21.

## Post-processing fallback

| Service | URL | Cost |
|---|---|---|
| CROPOS RINEX / GPPS | https://gnss.cropos.hr/ | 0,06 EUR/min |
| EUREF EPN (DUBR, OSIJ, PORE, RIJE, ZADA, etc.) | https://www.epncb.oma.be/ | free |

## Sources

- CROPOS home + landing text (33+ stations, services, free-since-2022): https://www.cropos.hr/ (WebFetch 2026-05-21)
- CROPOS fees page (current EUR pricing, regulation NN 56/2023 + NN 106/25): https://www.cropos.hr/o-sustavu/naknade-za-koristenje-podataka-cropos-sustava (WebFetch 2026-05-21 — 40 EUR registration + 0,06 EUR/min GPPS confirmed)
- CROPOS VPPS service page (technical only, free): https://www.cropos.hr/servisi/vpps (WebFetch 2026-05-21)
- DGU April 2025 expansion announcement (41 stations total, Čazma + Daruvar): https://dgu.gov.hr/vijesti/dvije-nove-referentne-stanice-u-mrezi-cropos-sustava/6556 (WebFetch 2026-05-21)
- Live caster sourcetable: `curl --http0.9 http://195.29.198.194:2101/` — `SOURCETABLE 200 OK Server: NTRIP Trimble Ntrip Caster 5.2`, 15 STR, 2276 bytes (2026-05-21)
- ArduSimple Croatia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-croatia/
- HKOIG law amendment note: https://www.hkoig.hr/novo-dodano/vijesti-iz-struke/uvjeti-koristenja-cropos-sustava-vezano-za-donesene-izmjene-zakona-o-drzavnoj-izmjeri-i-katastru-nekretnina
- Local data: `data/rtk2go.sourcetable` 2026-05-21 — `Tiho1234`, `VargaRTKhr` both listed with HRV country and RTCM 3.2 GPS+GLO+GAL+BDS frames
