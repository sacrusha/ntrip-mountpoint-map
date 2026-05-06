# Switzerland [CH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid national NTRIP/VRS (swipos / swisstopo); no free public tier; sparse rtk2go volunteer coverage

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid only) |
| **Operator** | swisstopo (Federal Office of Topography / Bundesamt für Landestopografie) |
| **Service name** | swipos (Swiss Positioning Service) |
| **host:port** | `www.swipos.ch:2101` (plain TCP, confirmed live 2026-05-06) · `www.swipos.ch:2102` (TLS-encrypted; timeout from external; likely credential-gated) |
| **VRS** | Yes — VRS computed from 31 AGNES permanent stations + neighbouring country stations |
| **tariff — pay-per-use** | CHF 0.50 / minute (for RINEX data or RTK VRS corrections; all fees net, VAT not included) |
| **tariff — annual flatrate** | CHF 1,500 / year (first licence) · CHF 600 / year (2nd and 3rd licence, same reseller) · CHF 200 / year (each additional licence) |
| **tariff — swipos-INFRA** | CHF 310 / month / station (raw CORS stream access for infrastructure operators) |
| **tariff — swipos-NAV** | Free (sub-metre navigation corrections; not RTK) |
| **VAT** | All fees net (ohne MwSt. / sans TVA / senza IVA) — Swiss VAT (currently 8.1%) applies on top |
| **hobbyist_eligibility** | Yes — paid subscription available to individuals; no professional licence required |
| **legal_residency_required** | No — swisstopo accepts international users |
| **last_confirmed_alive** | `www.swipos.ch:2101` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl confirmed) |

## Mountpoints (VRS — swipos-GIS/GEO)

| Mountpoint | Format | Height frame | Constellations |
|---|---|---|---|
| `MSM_GISGEO_LV95LN02` | RTCM 3.2 MSM (recommended) | LN02 (1902 levelling) | GPS+GLO+GAL+BDS3 |
| `MSM_GISGEO_LV95LHN95` | RTCM 3.2 MSM (recommended) | LHN95 (modern orthometric) | GPS+GLO+GAL+BDS3 |
| `VRS_GISGEO_LV95LN02` | RTCM 3.1 (legacy) | LN02 | GPS+GLO |
| `VRS_GISGEO_LV95LHN95` | RTCM 3.1 (legacy) | LHN95 | GPS+GLO |

Additional mountpoints for CORS (individual AGNES station raw access) and swipos-NAV are available in the sourcetable. Encrypted NTRIP v2 access recommended; TLS-capable receivers should connect via port 2102.

## Registration

- Online order form at shop.swipos.ch; login credentials typically issued on the following working day.
- Pay-per-use requires activation before each session; flatrate licences are valid for 12 months.
- Rover must support NTRIP protocol and RTCM 3.2 MSM (older RTCM 3.1 receivers use the VRS_* mountpoints).
- Communication costs (SIM data) are the user's responsibility.

## Context Notes

- Switzerland has no free government NTRIP tier. swipos is the only official VRS RTK product.
- The AGNES (Automatic GNSS Network for Switzerland) backbone of 31 stations underpins swipos. Selected AGNES stations participate in EUREF EPN; RINEX download available via swisstopo.
- **rtk2go volunteer coverage:** Several CHE-coded volunteer base stations present; coverage sparse but includes major urban centres (Zürich, Bern, Basel area). No Centipede presence for Switzerland.
- **Liechtenstein (LI):** No independent caster. Fully relies on swipos or Austrian APOS; swipos coverage extends into Liechtenstein territory given station proximity.
- Data volume: ~3 MB/hour for RTCM 3 + NTRIP (per swisstopo documentation).
- Contact: swipos@swisstopo.ch / +41 58 469 01 21

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **swipos RINEX** (AGNES stations) | Via swipos portal; CHF 0.50/min or included in flatrate | Paid |
| **EUREF EPN** (selected Swiss AGNES stations: BERN, ZIMM, DAVO, GENO, PAYE, POTS, SASS) | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- swisstopo swipos pricing page: https://www.swisstopo.admin.ch/en/swipos-services-prices-and-ordering (observed 2026-05-06)
- swisstopo swipos-GIS/GEO product: https://www.swisstopo.admin.ch/en/swipos-gisgeo-for-rtk-and-postprocessing-applications (observed 2026-05-06)
- swisstopo technical details for swipos: https://www.swisstopo.admin.ch/en/technical-details-for-swipos (observed 2026-05-06)
- swisstopo swipos FAQ: https://www.swisstopo.admin.ch/en/swipos-frequently-asked-questions (observed 2026-05-06)
- gpsd-users mailing list (historical hostname reference www.swipos.ch:2102): https://lists.nongnu.org/archive/html/gpsd-users/2014-12/msg00033.html (observed 2026-05-06)
- GitHub NTRIP client for swipos: https://github.com/Michael-Perna/NTRIP_Client (observed 2026-05-06)
- curl probe of `www.swipos.ch:2101` — SOURCETABLE 200 OK confirmed 2026-05-06
- rtk2go.com mountpoint list (CHE stations, observed 2026-05-06)
