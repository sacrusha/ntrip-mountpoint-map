# Brazil [BR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free national government caster (RBMC-IP) + multiple commercial casters

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **host:port — RBMC-IP** | `gps-ntrip.ibge.gov.br:2101` (alt IP: `170.84.40.52:2101`) |
| **tariff — RBMC-IP** | Free; gov.br account required; 5 simultaneous mountpoints per user; 1,000 concurrent connections max |
| **type — RBMC-IP** | Single-base |
| **hobbyist_eligibility** | Yes — open to any user; no professional licence required |
| **legal_residency_required** | No — gov.br registration is open to non-Brazilians; no explicit residency requirement |
| **last_confirmed_alive** | IBGE RBMC-IP confirmed operational; 5 new stations inaugurated Dec 2024; pipeline CI sourcetable probe 2026-05-06 |

## Network Coverage

RBMC-IP is operated by IBGE (Instituto Brasileiro de Geografia e Estatística). As of 2026-05-06 the network has approximately 150 stations; the IBGE caster receives data from 149 RBMC stations. Stations cover all 26 states and the Federal District, with densest coverage in the south and south-east (São Paulo, Minas Gerais, Rio de Janeiro, Paraná, Rio Grande do Sul). Coverage is sparse in the Amazon basin and north-eastern interior (Amazonas, Pará, Roraima, Amapá, Maranhão interior). Reference frame: SIRGAS2000 (ITRF-compatible).

Recent expansion: IBGE inaugurated 5 new RBMC stations on 9 December 2024 at Governador Valadares (MG), Maceió (AL), Januária (MG), Pinhais (PR), and Nova Friburgo (RJ), all transmitting RTCM 3.2 MSM via NTRIP. Additional stations in Lins/SP (SPLI) and Rosana/SP (ROSA) were planned for 2025.

## Commercial Alternatives

| Provider | host:port | Type | Tariff (observed 2026-05-06) | Notes |
|---|---|---|---|---|
| **geoRTK** | not published publicly (via geortk.com.br) | network RTK + PPK | BRL 10/day · BRL 79/week; monthly/annual plans; 30-day free trial | Launched Sep 2025; claims largest RTK/PPK network in Brazil; 500-station goal by 2026; coverage map at geortk.com.br/ferramentas/mapa-de-cobertura |
| **GeoPlus** | not published publicly (via geoplusbrasil.com) | network RTK (PPP-RTK + NTRIP) | not listed publicly; contact required | Multi-constellation, multi-signal; national coverage claim |
| **RoverConnect (CPE Tecnologia)** | not published (cpetecnologia.com.br) | single-base NTRIP | weekly plan listed; pricing via website | Short-term prepaid; surveying/agriculture focus |
| **RTKdata** | not published (rtkdata.com/br/) | network RTK | USD 40/month; 30-day free trial | International service with Brazilian coverage; pricing in USD |
| **TopNET Live (Topcon)** | via topconpositioning.com | network RTK | subscription; pricing not published for BR | Regional South America coverage; BR-specific nodes unconfirmed |

## State-Level CORS

No state-level free public NTRIP casters were confirmed beyond RBMC-IP as of 2026-05-06:
- **São Paulo**: The state geodetic office (IGC-SP, Instituto Geográfico e Cartográfico) operates CORS stations contributing to RBMC-IP; no independent SP-state NTRIP caster endpoint found.
- **Bahia**: No separate Bahia DGC NTRIP caster confirmed; Bahia stations appear in the RBMC-IP network.
- **Minas Gerais / Rio de Janeiro**: Same pattern — state stations contribute to IBGE/RBMC-IP rather than operating independent casters.

## Context Notes

- **RBMC-IP access**: Registration via gov.br (Cadastro.gov.br). The 5-simultaneous-mountpoint cap is not a practical barrier for individual hobbyists; the 1,000-concurrent-user global cap may occasionally cause connection refusals during peak demand.
- **Volunteer**: ~19 BR-coded bases on rtk2go, concentrated in São Paulo metro and southern states (RS, SC, PR). Small number of Centipede nodes.
- **Coverage gap**: Amazon basin and north-east interior (Amazonas interior, parts of Pará, Roraima, Piauí) have no RBMC-IP station within useful single-base baseline distances. Commercial networks (geoRTK, GeoPlus) claim national coverage but rely partly on RBMC-IP stations re-streamed or augmented; independent verification of Amazon coverage is not possible remotely.
- **geoRTK launch**: Service launched 1 September 2025; pricing observed at geortk.com.br/planos on 2026-05-06. IVA (ICMS/ISS) applicability to digital services varies by state; pricing on website shown as base rate.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **RBMC RINEX archive** (IBGE) — full per-station archive | https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/rede-geodesica/16258-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-rbmc.html | Free (gov.br account required) |
| **IBGE PPGPS online PPP** | https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16334-ppgps.html | Free |
| **EarthScope NOTA** — selected Brazilian stations | https://www.earthscope.org/data/gnss-realtime/ | Free non-commercial (NULA) |

## Sources Consulted
- IBGE RBMC-IP service page: https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16332-rbmc-ip-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-em-tempo-real.html
- gov.br RBMC-IP access page: https://www.gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip
- IBGE Dec 2024 inauguration announcement: https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/42130-ibge-inaugura-cinco-novas-estacoes-da-rede-brasileira-de-monitoramento-continuo-e-publica-as-series-temporais-de-redes-geodesicas
- MundoGEO Dec 2024 expansion coverage: https://mundogeo.com/2024/12/16/ibge-inaugura-5-novas-estacoes-da-rbmc-e-publica-series-temporais-de-redes-geodesicas/
- ArduSimple RTK correction services Brazil: https://pt.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-brazil/
- geoRTK launch announcement: https://www.geortk.com.br/noticias/geortk-lanca-rede-rtk-no-brasil-com-cobertura-quase-nacional-e-precos-competitivos
- geoRTK pricing page: https://www.geortk.com.br/planos
- geoRTK coverage map: https://www.geortk.com.br/ferramentas/mapa-de-cobertura
- GeoPlus network: https://geoplusbrasil.com/
- RTKdata Brazil: https://rtkdata.com/br/
- CPE Tecnologia RoverConnect: https://www.cpetecnologia.com.br/servico-de-correcao-rtk-ntrip-rover-connect-plano-semanal/p
- Emlid community Brazil NTRIP resources thread: https://community.emlid.com/t/estacoes-de-referencia-base-correcoes-ntrip-para-rtk-recursos-no-brasil/15553
- Pipeline CI sourcetable probe — ~149 BR stations confirmed 2026-05-06
