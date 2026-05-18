# Cape Verde [CV] — NTRIP RTK Research

**researched:** 2026-05-17 (prior: 2026-05-12)
**status:** NO active public NTRIP RTK caster. One IGS post-processing CORS (CPVG, Sal). No real-time RTK service for hobbyists.

| field | value |
|---|---|
| landing_url | https://ingt.gov.cv/ (national geodetic authority; no NTRIP section) |
| access_url | n/a |
| Active NTRIP RTK caster | no |
| host:port | n/a |
| tariff | n/a |
| hobbyist_eligibility | n/a |
| legal_residency_required | n/a |
| last_confirmed_alive | n/a |
| datum_epoch | omitted — no caster, no operator declaration |

## Most recent project announcement

None. No formal national NTRIP/RTK project found in development-bank (World Bank, AfDB), UN, or trade-press sources as of 2026-05-17. Closest prior signal = Ministério das Finanças RFQ "Supply, Actualization and Densification of the Permanent GNSS Stations Network in Cabo Verde" (mf.gov.cv document, 2022) — procurement only, no operational service announced since.

OVCV (Observatório Vulcanológico de Cabo Verde, INMG / Uni-CV / ITER Tenerife) runs a GPS deformation network on Fogo for geophysical research; scientific, not public NTRIP.

## Context

- **INGT** — Instituto Nacional de Gestão do Território (`ingt.gov.cv`) responsible for cartography, cadastre, geodesia, IDE-CV. Page lists "Cartografia e geodesia" as a service area but publishes no NTRIP / sourcetable / tariff as of 2026-05-17 (WebFetch 200, content silent on real-time GNSS).
- **CPVG (Espargos, Sal)** — IGS CORS, four-char `CPVG`, DOMES 39601M001, hosted by INMG on REGINA (CNES/IGN France). Daily/hourly RINEX via CDDIS + IGN-IGS. **No real-time RTCM NTRIP.** Single station ~750 km offshore from rest of archipelago = unusable for cross-island RTK regardless. `data/igs_ip.sourcetable` mirror = CPVG present as IGS archive flag, not real-time.
- **Geography** — 10 islands over ~580 km ocean. Meaningful national RTK needs ≥1 CORS/island. Not documented.
- **AFREF** — no CV real-time NTRIP contribution identified.
- **SIRGAS / EarthScope** — Americas-focused; no CV stations.
- **rtk2go / Centipede** — zero CPV-coded streams (project 2026-05 archives).
- **Commercial PPP** — GEODNET / ONOCOY / PointOne no CV coverage.

## Practical workaround
Hobbyist needs cm RTK on a CV island → self-operated local base + rover (single-baseline ≤30 km), or SBAS / Galileo HAS (m-level free), or Trimble RTX / Skylark / PointPerfect (paid satellite delivery).

## Post-processing
| Service | URL | Cost |
|---|---|---|
| IGS CDDIS — CPVG | https://cddis.nasa.gov/archive/gnss/data/ | free (NASA Earthdata) |
| IGN-IGS / REGINA | https://igs.ign.fr/ | free |
| SONEL — CPVG height series | https://www.sonel.org/spip.php?page=gps&idStation=3597 | free |

## Sources
- INGT: https://ingt.gov.cv/ (2026-05-17; no NTRIP)
- IDE-CV: https://idecv.gov.cv/
- INMG geofísica: https://www.inmg.gov.cv/index.php/servicos/geofisica
- SONEL CPVG: https://www.sonel.org/spip.php?page=gps&idStation=3597
- IGS station log: https://files.igs.org/pub/station/oldlog/cpvg_20230309.log
- IGS network: https://network.igs.org/
- Min Finanças RFQ (2022 procurement): https://www.mf.gov.cv/documents/20126/0/RFQ+-+SUPPLY,+ACTUALIZATION+AND+DENSIFICATION+OF+THE+PERMANENT+GNSS+STATIONS+NETWORK+IN+CABO+VERDE..pdf/941433bb-85b7-037e-2f35-3fc927078bcb
- `data/rtk2go.sourcetable` + `data/centipede.sourcetable` (project, 2026-05): 0 CPV STR

## Gaps
- 2022 RFQ outcome unknown — whether contract awarded + densification executed not findable in open sources.
- INGT internal use of CPVG / future plan undisclosed.
