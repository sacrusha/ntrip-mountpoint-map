# Philippines [PH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh; prior pass 2026-05-06)

## Status: YES — national government NTRIP caster operating (PAGeNet); paid subscription; live sourcetable verified

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | PAGeNet (Philippine Active Geodetic Network) |
| **Operator** | NAMRIA — National Mapping and Resource Information Authority |
| **host:port** | `pagenet.namria.gov.ph:2101` — confirmed live (HTTP/0.9 SOURCETABLE OK, 60 STR rows) on 2026-05-12 |
| **VRS** | Yes — `NRTK_VRS` mountpoint exposed in the public sourcetable (RTCM 3, GPS, position from Manila area 14.54°N, 121.04°E). Also `NRTK_MAC` (network-RTK Master-Auxiliary, GPS+GLO) and `PGD2020_NB_MSM5` (network broadcast in PGD2020 datum, GPS+GLO+GAL+BDS+QZSS MSM5). Single-base mountpoints `PCEB_RTCM3_MSM5`, `PMOG`, `PSUR`, `PCDN`, `PMRV`, `PKEN`, `PMAG`, `PBUT`, `PURD`, `PTAC`, `PKLY` etc. on Leica GNSS Spider. |
| **num_stations (sourcetable rows)** | 60 distinct mountpoints / streams in live sourcetable on 2026-05-12 (mix of single-base CORS + 3 network products). Physical CORS count ≥ ~50. |
| **tariff — One-time registration** | PHP 1,000 per client (~$17.7 USD @ 56.5 PHP/USD) |
| **tariff — Per-hour RTK** | PHP 100.00 / hr / rover (~$1.77/hr) |
| **tariff — 1-day unlimited RTK** | PHP 1,000 (+ PHP 500 per extra rover) (~$17.7) |
| **tariff — 5-day unlimited RTK** | PHP 3,500 (~$61.9) |
| **tariff — 15-day unlimited RTK** | PHP 7,500 (~$132.7) |
| **tariff — 1-month unlimited RTK** | PHP 12,000 (~$212.4) |
| **tariff — RINEX 1–20 sec** | PHP 50/MB |
| **tariff — RINEX 30–60 sec** | Free (included with subscription) |
| **tariff — Coordinate computation** | Free |
| **VAT** | No VAT applicable — government regulatory charges, not sales transactions |
| **hobbyist_eligibility** | Yes — registration open to individuals; online form; no surveying company licence required per FAQ |
| **legal_residency_required** | Unclear — no explicit nationality/residency restriction stated; however, payment for non-Metro Manila clients requires Philippine bank deposit (LandBank), which may be a practical barrier for foreigners. Contact pagenet@namria.gov.ph to clarify. |
| **last_confirmed_alive** | `pagenet.namria.gov.ph:2101` SOURCETABLE 200 OK + ENDSOURCETABLE confirmed 2026-05-12 (curl HTTP/0.9, 60 STR rows). PAGeNet Services & Fees page intact (fee schedule unchanged from 2026-05-06 capture). |

## Context Notes

- **PAGeNet** (`pagenet.namria.gov.ph`): Operated by NAMRIA, a government agency under the Department of Environment and Natural Resources. The NTRIP caster hostname **and port 2101 are confirmed by live sourcetable probe** (2026-05-12) — earlier wording calling the port "inferred" is outdated.
- **Datum**: New `PGD2020_NB_MSM5` mountpoint indicates a Philippine Geodetic Datum 2020 (PGD2020) network broadcast in MSM5 (multi-constellation: GPS+GLO+GAL+BDS+QZSS). Older mountpoints use a `RTCM 3` legacy stream.
- **Payment**: Non-Metro Manila clients can pay via deposit slip to a LandBank account, making the service nationally accessible. Contact: pagenet@namria.gov.ph / (632) 8884-2849.
- **Tariff source**: Full schedule published at `pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx`, observed 2026-05-12; identical to 2026-05-06 capture.
- **Service uptime**: Described as 24/7 operational on the portal; most recent news post dated April 2023 but fees page and caster are current.
- **Volunteer rtk2go presence** (`scripts/stations_by_country.py PHL` 2026-05-12): 2 community bases — `CATNAV01` (14.68°N, 121.08°E, Metro Manila), `YASSER123` (6.09°N, 124.43°E, Mindanao).

## Post-Processing (RINEX) Fallback

| Service | Cost |
|---|---|
| RINEX 30–60 sec (unlimited download, included with RTK subscription) | Free |
| RINEX 1–20 sec | PHP 50/MB |

## Sources Consulted
- PAGeNet Services & Fees page: https://pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx (re-confirmed 2026-05-12; fees unchanged from 2026-04-30 / 2026-05-06)
- PAGeNet FAQs: http://pagenet.namria.gov.ph/AGN/FAQs.aspx
- PAGeNet About: http://pagenet.namria.gov.ph/AGN/AboutPagenet.aspx
- NAMRIA FOI inventory listing (PAGeNet domain confirmation)
- UNOOSA archived presentation (host domain confirmation)
- Contact: pagenet@namria.gov.ph / (632) 8884-2849
- curl probe of `pagenet.namria.gov.ph:2101` — SOURCETABLE 200 OK confirmed 2026-05-12 (60 STR rows; mountpoints include `NRTK_VRS`, `NRTK_MAC`, `PGD2020_NB_MSM5`, plus single-base `Pxxx_RTCM3*`)
