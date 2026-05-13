# Portugal [PT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (prior version: 2026-05-06)

## Status: YES — free government NTRIP caster (ReNEP, DGT) operating; new Funchal station added 2026-05-01

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (ReNEP — free) |
| **Operator** | Direção-Geral do Território (DGT), Ministry of Territorial Cohesion |
| **host:port — ReNEP** | `193.137.94.71` (FQDN behind the public portal `renep.dgterritorio.gov.pt`); port 2101 (physical/single-base RTCM3), port 2102 (MSM5), port 2106 (nearest-station VRS), port 2108 (network corrections). Source: project's networks.md entry `renep` (DGT-confirmed), and Leica/ArduSimple guides citing 2101/2106/2108. |
| **Number of stations** | 47 (national territory: mainland + Azores + Madeira); Funchal added 2026-05-01 |
| **VRS** | Yes — port 2106 (nearest-station VRS) and port 2108 (network corrections) per the DGT real-time products PDF and networks.md |
| **Datum / Reference frame** | ETRS89 (mainland) · ITRF93 (Azores, Madeira) |
| **Accuracy** | < 10 cm minimum (DGT); RTK technique delivers 2–5 cm horizontal |
| **tariff** | Free — "standard products and services are at no cost" (DGT); registration required |
| **hobbyist_eligibility** | yes — registration open to all GNSS equipment users; no professional licensing stated |
| **legal_residency_required** | no explicit residency requirement stated |
| **last_confirmed_alive** | ReNEP portal HTTP 200 on 2026-05-12; most recent operator news item dated 2026-05-01 ("Funchal — nova estação"); RTK service page states "operacional" |

## Service Details

### ReNEP — Rede Nacional de Estações Permanentes GNSS

Portugal's national GNSS CORS network providing free real-time RTK and post-processing data in ETRS89 (mainland) and ITRF93 (Azores/Madeira). Operated by Direção-Geral do Território (DGT), Ministry of Territorial Cohesion.

### Real-time Products / Ports

Per the DGT "ReNEP produtos tempo real" PDF and the project's networks.md entry:

| Port | Product |
|---|---|
| 2101 | Physical / single-base, RTCM 3 |
| 2102 | MSM5 (multi-signal message) |
| 2106 | Nearest-station VRS |
| 2108 | Network corrections |

Host: `193.137.94.71` — also reachable behind the DGT portal `renep.dgterritorio.gov.pt`.

### Coverage and 2026-05-12 Update

47 stations across mainland Portugal, Azores and Madeira. The 2026-05-01 news item "Funchal — nova estação" announces the addition of a new station at Funchal (Madeira), increasing the Madeira sub-network coverage. Recent operational changes also reported at Leiria, Fajão and Melriça.

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
| **ReNEP RINEX FTP** — hourly/daily RINEX files from all 47 CORS | ftp://ftp.dgterritorio.pt/ReNEP/ | Free (no login required) |
| **EUREF Permanent Network** — selected Portuguese stations | https://epncb.oma.be/ | Free |

## Sources Consulted
- ReNEP portal: https://renep.dgterritorio.gov.pt/ (HTTP 200, 2026-05-12; news item Funchal nova estação dated 2026-05-01)
- ReNEP stations list: https://renep.dgterritorio.gov.pt/estacoes
- ReNEP stations table: https://renep.dgterritorio.gov.pt/estacoes-lista
- ReNEP real-time products PDF: https://renep.dgterritorio.gov.pt/sites/default/files/ReNEP-produtos-tempo-real.pdf
- DGT "How to use ReNEP" (EN): https://www.dgterritorio.gov.pt/node/803?language=en
- DGT geodesic infrastructure: https://www.dgterritorio.gov.pt/geodesia/infraestrutura-geodesica
- ReNEP RTK operational status: https://renep.dgterritorio.gov.pt/node/1142
- ReNEP RTK access limitations notice (2019): http://renep.dgterritorio.gov.pt/node/1132
- ANACOM ReNEP description PDF: https://www.anacom.pt/streaming/rede_nacional_estacoes_permanentesGNSS.pdf?contentId=992948&field=ATTACHED_FILE
- ArduSimple Portugal RTK page: https://pt.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-portugal/
- gov.pt ReNEP service page: https://www2.gov.pt/servicos/consultar-a-informacao-da-rede-nacional-de-estacoes-permanentes-gnss-renep-
- Project networks.md entry `renep` (host 193.137.94.71, port mapping)
- Project country-survey.md entry `PT — Portugal` (date_added 2026-04-29)
- Local: `py scripts/stations_by_country.py PRT` (2026-05-12) — 1 rtk2go base (H_Moita_NTRIP at 38.44, -8.46)
