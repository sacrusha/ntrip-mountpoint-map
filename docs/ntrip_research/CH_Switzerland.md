# Switzerland [CH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revising 2026-05-06 entry)

## Status: YES — paid national NTRIP/VRS (swipos / swisstopo); no free public tier; Centipede has ~30 CHZ + rtk2go ~20 CHE volunteer nodes giving partial free Plateau / Jura coverage

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid only) |
| **Operator** | swisstopo (Federal Office of Topography / Bundesamt für Landestopografie) |
| **Service name** | swipos (Swiss Positioning Service) |
| **host:port** | `www.swipos.ch:2101` (plain TCP; verified live 2026-05-12 — `SOURCETABLE 200 OK`, `Server: NTRIP Trimble Ntrip Caster 5.2`) · `www.swipos.ch:2102` (TLS / NTRIP-2 over SSL — recommended; credential-gated) |
| **VRS** | Yes — VRS computed from 31 AGNES permanent stations + neighbouring country stations |
| **tariff — pay-per-use** | CHF 0.50 / minute (for RINEX data or RTK VRS corrections; all fees net, VAT not included). Same since April 2023 simplification. |
| **tariff — annual flatrate** | CHF 1,500 / year (first licence) · CHF 600 / year (2nd and 3rd licence, same reseller) · CHF 200 / year (each additional licence). Page still current 2026-05-12. |
| **tariff — swipos-INFRA** | CHF 310 / month / station (raw CORS stream access for infrastructure operators) |
| **tariff — swipos-NAV** | Free (sub-metre navigation corrections; not RTK — DGNSS-class, out of project scope) |
| **VAT** | All fees net (ohne MwSt. / sans TVA / senza IVA) — Swiss VAT (currently 8.1%) applies on top |
| **hobbyist_eligibility** | Yes — paid subscription available to individuals; no professional licence required |
| **legal_residency_required** | No — swisstopo accepts international users |
| **last_confirmed_alive** | 2026-05-12 — `curl http://www.swipos.ch:2101/` returned `SOURCETABLE 200 OK` and full 4-mountpoint sourcetable; sourcetable line `CAS;www.swipos.ch;2101;swipos-GISGEO;swisstopo;1;CHE;46.9;7.5;...` |

## Mountpoints (VRS — swipos-GIS/GEO, verified from live sourcetable 2026-05-12)

| Mountpoint | Format | Height frame | Constellations | Bitrate | Note |
|---|---|---|---|---|---|
| `MSM_GISGEO_LV95LHN95` | RTCM 3.4 (MSM4) | LHN95 (modern orthometric) | GPS+GLO+GAL+BDS | 4000 | Recommended for current receivers |
| `MSM_GISGEO_LV95LN02` | RTCM 3.4 (MSM4) | LN02 (1902 levelling) | GPS+GLO+GAL+BDS | 4000 | |
| `VRS_GISGEO_LV95LN02` | RTCM 3.1 (legacy) | LN02 | GPS+GLO | 2500 | Backward-compatibility stream |
| `VRS_GISGEO_LV95LHN95` | RTCM 3.1 (legacy) | LHN95 | GPS+GLO | 2500 | Backward-compatibility stream |

**Format upgrade observed**: prior research recorded these as RTCM 3.2 MSM7. The sourcetable on 2026-05-12 reports `RTCM 3.4` with message profile `1005(5),1007/1033(5),MSM4(1)` — i.e. swisstopo has rolled the MSM streams to RTCM 3.4 / MSM4 (lower-bandwidth MSM variant suitable for the 4-system L1+L2 product). swisstopo's docs now recommend MSM4 + secure NTRIP (SSL/TLS over port 2102). Individual AGNES station raw access and swipos-NAV remain available; full sourcetable also lists a `swipos` NET record pointing to https://www.swisstopo.ch/swipos and the `CAS` self-record.

## Registration

- Online order form at shop.swipos.ch; login credentials typically issued on the following working day.
- Pay-per-use requires activation before each session; flatrate licences are valid for 12 months.
- Rover must support NTRIP protocol and RTCM 3.2 MSM (older RTCM 3.1 receivers use the VRS_* mountpoints).
- Communication costs (SIM data) are the user's responsibility.

## Context Notes

- Switzerland has no free government NTRIP tier. swipos is the only official VRS RTK product.
- The AGNES (Automatic GNSS Network for Switzerland) backbone of 31 stations underpins swipos. Selected AGNES stations participate in EUREF EPN; RINEX download available via swisstopo.
- **rtk2go volunteer coverage:** 20 CHE-coded volunteer base stations as of 2026-05-12 fetch (BERBU, BeLaAG01, Diemerswil, FP07, Gtown, ICOMOST, LAX1090, LT05, Mirmenhof, Ormalingen_Ribi, PSHS, Riddes_station, SFRTK, Solothurn, TOMI, VSG01, chgevymg8a, eid_genoss, suedostschweiz, wegenstetten_1). Coverage spans Plateau (Zürich/Bern/Basel/Solothurn), Jura, Valais, and a thinner Alpine presence.
- **Centipede volunteer coverage:** 30 CHZ-coded nodes as of 2026-05-12 (Centipede uses non-ISO code `CHZ` for Switzerland — *not* Czech Republic; the actual ISO code for Switzerland is `CHE` and Czech is `CZE`, both of which are also used by other sources). Major clusters along the Plateau (Bern, Lausanne, Yverdon, Basel/Solothurn corridor, Zürich, Eastern Switzerland). The 2026-05-06 entry's "no Centipede presence" claim was a research error: archived snapshots of `caster.centipede.fr:2101` show CHZ stations have existed since at least 2023. Genuine growth of the Swiss Centipede footprint is also real and documented from Wayback snapshots — **the world has changed AND prior research undercounted**:
  - 2023-01-01 (Wayback `caster.centipede.fr:2101` snapshot): **7 CHZ stations**
  - 2024-01-01 (Wayback): **10 CHZ stations**
  - 2025-01-01 (Wayback): **18 CHZ stations**
  - 2026-05-13 (live `crtk.net:2101` probe): **30 CHZ stations**
  
  So the trend is genuine ~4× growth over three years, not a sudden recent appearance. The current density makes Centipede a meaningful free alternative to swipos for Plateau hobbyists. Receiver mix is consistent with steady community deployment (mostly RTKBase-based U-blox ZED-F9P, a few Unicore UM980 and Septentrio MOSAIC-X5).
- **Liechtenstein (LI):** No independent caster. Fully relies on swipos or Austrian APOS; swipos coverage extends into Liechtenstein territory given station proximity.
- Data volume: ~3 MB/hour for RTCM 3 + NTRIP (per swisstopo documentation).
- Contact: swipos@swisstopo.ch / +41 58 469 01 21

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **swipos RINEX** (AGNES stations) | Via swipos portal; CHF 0.50/min or included in flatrate | Paid |
| **EUREF EPN** (selected Swiss AGNES stations: BERN, ZIMM, DAVO, GENO, PAYE, POTS, SASS) | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- swisstopo swipos pricing page: https://www.swisstopo.admin.ch/en/swipos-services-prices-and-ordering (observed 2026-05-12)
- swisstopo swipos-GIS/GEO product: https://www.swisstopo.admin.ch/en/swipos-gisgeo-for-rtk-and-postprocessing-applications (observed 2026-05-12 — confirms MSM4 / RTCM 3.4 / NTRIP-2 SSL recommendation)
- swisstopo technical details for swipos: https://www.swisstopo.admin.ch/en/technical-details-for-swipos (observed 2026-05-12)
- swisstopo swipos FAQ: https://www.swisstopo.admin.ch/en/swipos-frequently-asked-questions (observed 2026-05-12)
- swisstopo "Administrative simplifications of swipos as of 1 April 2023" (pricing model unchanged through 2026-05-12): https://www.swisstopo.admin.ch/en/administrative-simplifications-of-the-swiss-positioning-service-swipos-as-of-1-april-2023
- gpsd-users mailing list (historical hostname reference www.swipos.ch:2102): https://lists.nongnu.org/archive/html/gpsd-users/2014-12/msg00033.html
- GitHub NTRIP client for swipos: https://github.com/Michael-Perna/NTRIP_Client
- curl probe of `www.swipos.ch:2101` — full SOURCETABLE 200 OK + 4-mountpoint dump captured 2026-05-12
- Local pipeline data: `data/stations.json` (rtk2go CHE = 20, centipede CHZ = 30; fetched 2026-05-12T18:17Z)
- Wayback Machine snapshots of `http://caster.centipede.fr:2101/` filtered for `;CHZ;`: 2023-01-01 = 7 stations, 2024-01-01 = 10, 2025-01-01 = 18; current `crtk.net:2101` 2026-05-13 = 30. Confirms genuine multi-year growth of Swiss Centipede footprint — the 2026-05-06 "no Centipede presence" claim was a prior-research undercount, not a real-world disappearance.
- See also `docs/ntrip_research/_centipede_country_codes.md` for the full Centipede non-ISO country-code legend (CHZ, ENG, DAN, ROM, SER all non-standard).
