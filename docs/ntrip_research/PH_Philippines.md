# Philippines [PH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh; prior pass 2026-05-12)

## Status: YES — national government NTRIP caster operating (PAGeNet); paid subscription; live sourcetable verified

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | PAGeNet (Philippine Active Geodetic Network) |
| **Operator** | NAMRIA — National Mapping and Resource Information Authority |
| **landing_url** | https://pagenet.namria.gov.ph/AGN/AboutPagenet.aspx (PAGeNet About page) |
| **access_url** | https://pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx (Services & Fees page — registration form + tariff) |
| **host:port** | `pagenet.namria.gov.ph:2101` — confirmed live (HTTP/0.9 SOURCETABLE OK, 60 STR rows) on 2026-05-12 |
| **vrs** | yes — `NRTK_VRS` mountpoint exposed in the public sourcetable (RTCM 3, GPS, position from Manila area 14.54°N, 121.04°E). Also `NRTK_MAC` (network-RTK Master-Auxiliary, GPS+GLO) and `PGD2020_NB_MSM5` (network broadcast in PGD2020 datum, GPS+GLO+GAL+BDS+QZSS MSM5). Single-base mountpoints `PCEB_RTCM3_MSM5`, `PMOG`, `PSUR`, `PCDN`, `PMRV`, `PKEN`, `PMAG`, `PBUT`, `PURD`, `PTAC`, `PKLY` etc. on Leica GNSS Spider. |
| **num_stations** | unknown — operator publishes 60 mountpoints (3 NRTK products + ~57 single-base `Pxxx_RTCM3*` streams) in the live sourcetable, but a physical CORS count is not declared on the PAGeNet About / Services pages. Per primer [stations-vs-mps], physical-station count requires an operator figure; treat ~57 as an upper bound (some single-base mountpoint names may be alternate-format streams from the same site). |
| **tariff — One-time registration** | PHP 1,000 per client (~$17.7 USD @ 56.5 PHP/USD) |
| **tariff — Per-hour RTK** | PHP 100.00 / hr / rover (~$1.77/hr) |
| **tariff — 1-day unlimited RTK** | PHP 1,000 (+ PHP 500 per extra rover) (~$17.7) |
| **tariff — 5-day unlimited RTK** | PHP 3,500 (~$61.9) |
| **tariff — 15-day unlimited RTK** | PHP 7,500 (~$132.7) |
| **tariff — 1-month unlimited RTK** | PHP 12,000 (~$212.4) |
| **tariff — RINEX 1–30 sec** | PHP 50/MB (per the live Services & Fees page; earlier "1–20 sec" wording was an error) |
| **tariff — RINEX 30–60 sec** | Free |
| **tariff — Coordinate computation** | Free |
| **VAT** | No VAT applicable — government regulatory charges, not sales transactions |
| **hobbyist_eligibility** | Yes — registration open to individuals; online form; no surveying company licence required per FAQ |
| **legal_residency_required** | Unclear — no explicit nationality/residency restriction stated; however, payment for non-Metro Manila clients requires Philippine bank deposit (LandBank), which may be a practical barrier for foreigners. Contact pagenet@namria.gov.ph to clarify. |
| **last_confirmed_alive** | `pagenet.namria.gov.ph:2101` SOURCETABLE 200 OK + ENDSOURCETABLE re-confirmed 2026-05-17 (curl --http0.9, 60 STR rows; NRTK_MAC, NRTK_VRS, PGD2020_NB_MSM5 all still listed). Fee schedule unchanged. |
| **datum_epoch** | unchanged — operator citation incomplete. PAGeNet's "About" page states: "It provides a continuous link to the International Terrestrial Reference Frame (ITRF)" (https://pagenet.namria.gov.ph/AGN/AboutPagenet.aspx) — no specific ITRF realisation or epoch is given. The `PGD2020_NB_MSM5` mountpoint name suggests the new Philippine Geodetic Datum 2020 is on-air, but per primer [datum-epoch] **a mountpoint name is not an operator declaration**; mark datum_epoch as not citable until NAMRIA publishes a PGD2020 specification page. |

## Context Notes

- **PAGeNet** (`pagenet.namria.gov.ph`): Operated by NAMRIA, a government agency under the Department of Environment and Natural Resources. The NTRIP caster hostname **and port 2101 are confirmed by live sourcetable probe** (2026-05-12) — earlier wording calling the port "inferred" is outdated.
- **Datum (mountpoint-name evidence)**: The `PGD2020_NB_MSM5` mountpoint suggests a Philippine Geodetic Datum 2020 (PGD2020) network broadcast in MSM5 (GPS+GLO+GAL+BDS+QZSS); older mountpoints use a legacy `RTCM 3` stream. Treat the PGD2020 inference as suggestive, not declarative — the operator About page only mentions a generic ITRF link.
- **Payment**: Non-Metro Manila clients can pay via deposit slip to a LandBank account, making the service nationally accessible. Contact: pagenet@namria.gov.ph / (632) 8884-2849.
- **Tariff source**: Full schedule published at `pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx`, observed 2026-05-12; identical to 2026-05-06 capture.
- **Service uptime**: Described as 24/7 operational on the portal; most recent news post dated April 2023 but fees page and caster are current.
- **Volunteer rtk2go presence** (`scripts/stations_by_country.py PHL` 2026-05-17): 2 community bases — `CATNAV01` (14.68°N, 121.08°E, Metro Manila), `YASSER123` (6.09°N, 124.43°E, Mindanao). Other ingested sources contribute: AUSCORS + MIRAI rebroadcast PTGG (14.54°N, 121.04°E), IGS-IP carries PIMO + PTGG.

## Post-Processing (RINEX) Fallback

| Service | Cost |
|---|---|
| RINEX 30–60 sec (unlimited download, included with RTK subscription) | Free |
| RINEX 1–30 sec (per live Services & Fees page; earlier "1–20 sec" wording was an error) | PHP 50/MB |

## Sources Consulted
- PAGeNet Services & Fees page: https://pagenet.namria.gov.ph/AGN/ServicesAndFees.aspx (re-confirmed 2026-05-12; fees unchanged from 2026-04-30 / 2026-05-06)
- PAGeNet FAQs: http://pagenet.namria.gov.ph/AGN/FAQs.aspx
- PAGeNet About: http://pagenet.namria.gov.ph/AGN/AboutPagenet.aspx
- NAMRIA FOI inventory listing (PAGeNet domain confirmation)
- UNOOSA archived presentation (host domain confirmation)
- Contact: pagenet@namria.gov.ph / (632) 8884-2849
- curl probe of `pagenet.namria.gov.ph:2101` — SOURCETABLE 200 OK re-confirmed 2026-05-17 (60 STR rows; NRTK_VRS, NRTK_MAC, PGD2020_NB_MSM5 + 57 single-base `Pxxx_RTCM3*`)
- WebFetch `pagenet.namria.gov.ph/AGN/AboutPagenet.aspx` 2026-05-17 — only ITRF reference, no operator PGD2020 datum/epoch statement found
