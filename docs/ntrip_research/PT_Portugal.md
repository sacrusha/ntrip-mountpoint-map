# Portugal [PT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free government NTRIP caster (ReNEP, DGT) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (ReNEP — free) |
| **host:port — ReNEP** | Not published on the public portal; connection details provided after account activation. Leica equipment documented to use ports 2101, 2106, 2108. FQDN pattern: likely `renep.dgterritorio.gov.pt` or a sub-domain (not confirmed externally). |
| **VRS** | Unclear — portal describes single-station RTK streams; no VRS/iMAX product confirmed in public documentation |
| **tariff** | Free — "standard products and services are at no cost" (DGT); registration required |
| **hobbyist_eligibility** | yes — registration open to all GNSS equipment users; no professional licensing stated |
| **legal_residency_required** | no explicit residency requirement stated |
| **last_confirmed_alive** | ReNEP portal (renep.dgterritorio.gov.pt) HTTP 200 on 2026-05-06; RTK service page states "operacional" (operational) — date of that notice not confirmed |

## Context Notes

- **ReNEP** (Rede Nacional de Estações Permanentes GNSS): Operated by Direção-Geral do Território (DGT), Ministry of Territorial Cohesion. Portugal's national GNSS CORS network providing free real-time RTK and post-processing data in ETRS89 (mainland) and ITRF93 (Azores/Madeira).
- **Coverage**: Mainland Portugal + Azores + Madeira autonomous regions.
- **Accuracy**: Better than 10 cm stated as minimum; RTK technique delivers 2–5 cm horizontal.
- **Current RTK status**: A 2019 service notice stated disruptions affecting only RTK (not RINEX). A separate page states RTK "operacional" using GPS constellation only. Galileo/GLONASS addition to the RTK stream not confirmed.
- **Access procedure**: Register at renep.dgterritorio.gov.pt; after approval receive NTRIP credentials. Contact: renep@dgterritorio.pt / +351 21 381 96 00.
- **RINEX FTP**: ftp://ftp.dgterritorio.pt/ReNEP/ — raw data from all stations, no authentication required.
- **Military network**: CIGeoE (Centro de Informação Geoespacial do Exército, Army) also operates GNSS infrastructure but it is not open to the public.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ReNEP RINEX FTP** — hourly/daily RINEX files from all CORS | ftp://ftp.dgterritorio.pt/ReNEP/ | Free (no login required) |
| **EUREF Permanent Network** — selected Portuguese stations | https://epncb.oma.be/ | Free |

## Sources Consulted
- ReNEP portal: https://renep.dgterritorio.gov.pt/
- ReNEP stations list: https://renep.dgterritorio.gov.pt/estacoes
- ReNEP real-time products PDF (binary; not parsed): https://renep.dgterritorio.gov.pt/sites/default/files/ReNEP-produtos-tempo-real.pdf
- DGT "How to use ReNEP" page: https://www.dgterritorio.gov.pt/node/803?language=en
- ReNEP RTK operational status: https://renep.dgterritorio.gov.pt/node/1142
- ReNEP RTK access limitations notice (2019): http://renep.dgterritorio.gov.pt/node/1132
- ANACOM ReNEP description PDF: https://www.anacom.pt/streaming/rede_nacional_estacoes_permanentesGNSS.pdf?contentId=992948&field=ATTACHED_FILE
- ArduSimple Portugal RTK page: https://pt.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-portugal/
- gov.pt ReNEP service page: https://www2.gov.pt/servicos/consultar-a-informacao-da-rede-nacional-de-estacoes-permanentes-gnss-renep-
