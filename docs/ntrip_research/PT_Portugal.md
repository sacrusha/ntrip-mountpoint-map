# Portugal [PT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-12)

## Status: YES — free gov NTRIP caster (ReNEP, DGT) operating; Funchal station live since 2026-05-01

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (ReNEP — free) |
| **Operator** | Direção-Geral do Território (DGT), Ministry of Territorial Cohesion |
| **landing_url** | `https://renep.dgterritorio.gov.pt/` |
| **access_url** | `https://renep.dgterritorio.gov.pt/node/add/registo` (registration form) |
| **host:port — ReNEP** | `193.137.94.71:2101` (FQDN `renep.dgterritorio.gov.pt`). Ports per DGT "Produtos tempo real" PDF (Fev.2025): 2101 single-base RTCM3 GPS+GLO; 2102 single-base RTCM3 MSM5 (GPS+GLO+GAL, some + BDS); 2106 Nearest-Station (NSRT23, NSRT, NSR5); 2108 Network Corrections (ACRT, ACR5). |
| **num_stations** | 46 advertised on :2101 ST 2026-05-17 (incl. FUN1 Funchal new). PDT lists ~50 mountpoints across 2101+2102 incl. MELR Melriça, SCA1 S. Manços, ODEM new. ReNEP portal prose still cites "47 CORS" in places — current observed = 46 on live ST 2026-05-17. |
| **VRS** | Yes — port 2106 (Nearest-Station VRS) + port 2108 (Automatic Cells Network Correction). |
| **datum_epoch** | ETRS89 mainland · ITRF93 Azores + Madeira (DGT-declared on ReNEP portal: "Sistemas de Referência ETRS89 (continente) e ITRF93 (regiões autónomas)" — confirmed 2026-05-17 via renep.dgterritorio.gov.pt). No public epoch declaration in operator docs. |
| **Accuracy** | < 10 cm minimum (DGT); RTK 2–5 cm horizontal |
| **tariff** | Free; registration required |
| **hobbyist_eligibility** | yes — open to all GNSS users; no professional licence required |
| **legal_residency_required** | no explicit residency requirement |
| **last_confirmed_alive** | `193.137.94.71:2101` SOURCETABLE 200 OK 2026-05-17 (Leica GNSS Spider 7.8.0.9445); 46 STR records advertised; FUN1 Funchal present (32.65, -16.89). |

## Service Details

### ReNEP — Rede Nacional de Estações Permanentes GNSS

Portugal's national GNSS CORS network providing free real-time RTK and post-processing data in ETRS89 (mainland) and ITRF93 (Azores/Madeira). Operated by Direção-Geral do Território (DGT), Ministry of Territorial Cohesion.

### Real-time Products / Ports (DGT PDF "Produtos tempo real", Fev.2025)

| Port | Product | Constellations |
|---|---|---|
| 2101 | Single-base (manual) RTCM3 | GPS+GLO |
| 2102 | Single-base RTCM3 MSM5 | GPS+GLO+GAL (some stations +BDS) |
| 2106 | Nearest-station: NSRT23 (RTCM2.3), NSRT (RTCM3), NSR5 (MSM5 4-constel) | varies |
| 2108 | Network Corrections: ACRT (RTCM3), ACR5 (MSM5) | varies, ACR5 = 4-constel |

Host: `193.137.94.71` (FQDN `renep.dgterritorio.gov.pt`). 4-constellation (GPS+GLO+GAL+BDS) confirmed via PDF MSM5 tables — significant upgrade vs. prior project notes that suggested GPS-only.

### Coverage + Recent Operational Changes

46 stations on live ST 2026-05-17 (mainland Portugal + Azores: FRNS Furnas, PDEL Ponta Delgada, TERC Terceira, FLRS Flores; + Madeira: FUNC + FUN1 Funchal). News timeline 2026:
- 2026-05-01 FUN1 Funchal new station live
- 2026-03-10 Melriça inactive (again)
- 2026-02-24 Melriça resumed
- 2026-02-06 Leiria + Fajão operational
- 2026-02-02 Fajão + Melriça offline

### Access Procedure

1. Register at https://renep.dgterritorio.gov.pt/node/add/registo
2. DGT reviews the application
3. NTRIP credentials are issued by email after approval
4. Configure rover with host `193.137.94.71` or `renep.dgterritorio.gov.pt`, port + mountpoint per Real-time Products PDF

### RTK Constellation Coverage Gap

A 2019 service notice (renep.dgterritorio.gov.pt/node/1132) stated disruptions affecting only RTK (not RINEX). A separate page states RTK "operacional" — current status appears stable, though it is not clear from public documentation whether Galileo/GLONASS/BeiDou are included alongside GPS in the RTK stream. GPS-only RTK still meets the < 10 cm accuracy target.

### Contact

- Email: renep@dgterritorio.pt
- Phone: +351 21 381 96 00
- Fax: +351 21 381 96 99
- Address: Rua Artilharia 1, 107, 1099-052 Lisboa, Portugal

### RINEX (post-processing) — Free, No Auth

`ftp://ftp.dgterritorio.pt/ReNEP/` — hourly/daily RINEX files from all CORS, no registration.

### Military Network (out of scope)

CIGeoE (Centro de Informação Geoespacial do Exército, Army) also operates GNSS infrastructure but it is not open to the public.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ReNEP RINEX FTP** — hourly/daily RINEX files from all CORS (46 on live ST 2026-05-17; portal prose says 47) | ftp://ftp.dgterritorio.pt/ReNEP/ | Free (no login required) |
| **EUREF Permanent Network** — selected Portuguese stations | https://epncb.oma.be/ | Free |

## Sources Consulted
- ReNEP portal: https://renep.dgterritorio.gov.pt/ (HTTP 200, 2026-05-12; news item Funchal nova estação dated 2026-05-01)
- ReNEP stations list: https://renep.dgterritorio.gov.pt/estacoes
- ReNEP stations table: https://renep.dgterritorio.gov.pt/estacoes-lista
- ReNEP real-time products PDF: https://renep.dgterritorio.gov.pt/sites/default/files/ReNEP-produtos-tempo-real.pdf (Fev.2025 ed., GPS+GLO+GAL+BDS MSM5 confirmed)
- DGT "How to use ReNEP" (EN): https://www.dgterritorio.gov.pt/node/803?language=en
- DGT geodesia PDF (ITRF93 Azores+Madeira declaration): https://www.dgterritorio.gov.pt/sites/default/files/ficheiros-geodesia/1-InfraestuturaGeodesica-DGeod.pdf
- DGT geodesia URL `https://www.dgterritorio.gov.pt/geodesia/infraestrutura-geodesica` → HTTP 404 on 2026-05-17 (page moved/removed)
- ReNEP RTK operational status: https://renep.dgterritorio.gov.pt/node/1142
- ReNEP RTK access limitations notice (2019): http://renep.dgterritorio.gov.pt/node/1132
- ANACOM ReNEP description PDF: https://www.anacom.pt/streaming/rede_nacional_estacoes_permanentesGNSS.pdf?contentId=992948&field=ATTACHED_FILE
- ArduSimple Portugal RTK page: https://pt.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-portugal/
- gov.pt ReNEP service page: https://www2.gov.pt/servicos/consultar-a-informacao-da-rede-nacional-de-estacoes-permanentes-gnss-renep-
- Project rtk_inventory.md entry `renep` (host 193.137.94.71, port mapping)
- Local `scripts/stations_by_country.py PRT` (2026-05-17): renep=46, EUREF-IP=8, IGS-IP=5, AUSCORS=1 (PDEL mirror), MIRAI=1 (ENAO mirror), rtk2go=2 (H_Moita_NTRIP, R4F_RTK_ENV2).
