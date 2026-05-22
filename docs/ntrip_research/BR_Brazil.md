# Brazil [BR] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status

YES — free national government caster (RBMC-IP, IBGE) covers all 26 states +
DF; one viable commercial alternative (geoRTK, hobbyist-priced subscription
built on GEODNET infrastructure) verified. No independently accessible free
state-level NTRIP caster confirmed. rtk2go has ~17 BR-coded volunteer bases
concentrated in SP / South — covered in `rtk2go.md`.

## RBMC-IP — IBGE (free national caster)

| Field | Value |
|---|---|
| operator | Instituto Brasileiro de Geografia e Estatística (IBGE) |
| landing_url | https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16332-rbmc-ip-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-em-tempo-real.html |
| access_url | https://www.gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip |
| access_type | free-signup (requires gov.br federal account, Bronze/Silver/Gold tier) |
| sourcetable | `gps-ntrip.ibge.gov.br:2101` (alt IP `170.84.40.52:2101`). `curl --http0.9` 2026-05-23 → 149 STR rows / 31,267 bytes, of which 145 country=BRA and 4 are BKG passthroughs (SSRA02/SSRA03 IGS-combination SSR + BCEP ephemeris, country=DEU — not RTK, out of scope) |
| coverage | All 26 states + Federal District. Densest in SP/MG/RJ/PR/RS. Sparse but present in Amazon (POVE Porto Velho, PAAR Altamira, AMHA/AMPT/AMTE) and north-east interior. Effective single-base radius ~30 km per IBGE (often stretched to 50–70 km with degraded accuracy). |
| num_stations | 153 declared by IBGE December 2025 announcement; 145 BRA streams in live sourcetable probe 2026-05-23 (vs 148 BRA-tagged rows in cached `data/rbmc_ip.sourcetable` — live probe slightly lower, consistent with stations temporarily offline). Gap from 153 ≈ stations not yet streaming (e.g. Caruaru / PE announced 2025-12 but absent from sourcetable) plus outages. |
| vrs | no — single-base; mountpoints map 1:1 to physical sites, with many stations dual-streamed as `<code>1` (legacy RTCM 3.0 GPS+GLO+SBAS) and `<code>0` (RTCM 3.2/3.3 MSM7 GPS+GLO+GAL+BDS+SBAS) — e.g. `BRAZ1`/`BRAZ0` Brasília, `POLI1`/`POLI0` USP SP, `POAL1` Porto Alegre, `CUIB1` Cuiabá |
| tariff | not applicable — "Este serviço é gratuito para o cidadão" (gov.br); cap 5 mountpoints per user, 1,000 concurrent connections caster-wide |
| hobbyist_eligibility | yes — open to any user, no professional licence required |
| residency_required | no — gov.br registration accepts foreign passport as alternative to CPF; documented on gov.br federal signup. No documented rejection of non-resident accounts. |
| datum_epoch | SIRGAS2000, epoch 2000.4 — Brazilian official geodetic frame since 2005, per IBGE Resolução do Presidente nº 1/2015 (https://geoftp.ibge.gov.br/metodos_e_outros_documentos_de_referencia/normas/rpr_01_2015_sirgas2000.pdf). Frame not re-asserted per-stream by IBGE, but mandated nationally. |
| stations_source | sourcetable above + https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/rede-geodesica/16258-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-rbmc.html |

### Mountpoint conventions

Per-station streams: 5-character RBMC code + `1` (legacy RTCM 3.0 GPS+GLO+SBAS,
message set 1004/1006/1008/1012/1013/1019/1020/1033 — `BRAZ1`, `POLI1`,
`POAL1`, `CUIB1`, `RNNA1`, …) or + `0` (RTCM 3.2/3.3 MSM7 GPS+GLO+GAL+BDS+SBAS,
message set 1006/1008/1019/1020/1033/1042/1045/1077/1087/1097/1107/1127 —
`BRAZ0`, `POLI0`, `MGGV0`, `ALMC0`, `STHA0`, `ROSA0`, `SPLI0`, …). Sourcetable
2026-05-23 shows both `…1` and `…0` mountpoints coexist for many sites — the
`1` is legacy RTCM 3.0, the `0` is multi-constellation MSM7. Exception:
`ROCO0` (Colorado do Oeste, 2025-12 station) streams legacy RTCM 3.0
GPS+GLO only despite the `0` suffix.

SSR / ephemeris passthroughs `SSRA02IGS0_SIRGAS2000`, `SSRA03IGS0_SIRGAS2000`,
`SSRA03IGS0`, `BCEP00BKG0` are BKG Frankfurt PPP-RTK / broadcast-ephemeris
streams — out of project scope (SSR ≠ OSR; not single-base or NRTK).

### Recent expansion (build-up to current 153)

- 2023-12-20 — +6 stations operational: Blumenau/SC, Cascavel/PR,
  Guajará-Mirim/RO, Guaíra/PR, Irecê/BA, Resende/RJ. Network reached
  145 total (anchored back from IBGE Dec 2024 post citing 150 stations after
  the +5 2024-12 inauguration → 150 − 5 = 145 pre-2024).
- 2024-12-09 — +5 stations inaugurated, 150 total (IBGE post): Governador
  Valadares/MG (`MGGV0`), Maceió/AL (`ALMC0`), Januária/MG, Pinhais/PR,
  Nova Friburgo/RJ. `MGGV0` and `ALMC0` are new sites that re-use the
  observation series of deactivated legacy codes `GVA1` / `ALMA`; IBGE
  counts the +5 as net new inaugurations against the 145-station baseline.
- 2025-12 — +3 stations: Caruaru/PE, Colorado do Oeste/RO (`ROCO0`), Santa
  Helena/PR (`STHA0`); IBGE post cites 153 total. Live sourcetable
  2026-05-23 confirms `ROCO0` and `STHA0` streaming, **Caruaru/PE not yet
  present** in mountpoint list. `ROSA0` (Rosana/SP) and `SPLI0` (Lins/SP)
  also operational from earlier pre-2025 roadmap — exact inauguration date
  not pinned down here.

### Commercial / volunteer alternatives

| Provider | Endpoint | Type | Tariff (BRL, 2026-05-23) | Hobbyist | Notes |
|---|---|---|---|---|---|
| **geoRTK** | host:port assigned post-signup (geortk.com.br) | NRTK + PPK | R$10/day · R$79/week · R$219/month · R$2,099/year (≈R$175/month annual); 30-day free trial; monthly cancel anytime, annual cancel within first 30 days. VAT inclusion not stated on plans page. | yes (self-service) | Launched 2025-09; states 300+ stations in coverage map page (2026-05-23), target 500 by end-2026; built on **GEODNET distributed network** (operator description, not own CORS). 1 simultaneous user per plan tier. Most viable hobbyist commercial option in BR. |
| **Geo+ (Guandalini / SPGeo)** | per-account; geoplusbrasil.com / spgeo.com.br | hybrid NRTK + PPP-RTK | Quote via WhatsApp/contact form; no public list | ? (B2B agro/survey) | Claims 130+ own bases, SP near-total; "100% Brazilian hybrid infrastructure". Disqualified for hobbyist landing: no transparent pricing. |
| **CPE RoverConnect** | per-account | single-base NTRIP | Weekly/monthly prepaid via cpetecnologia.com.br; pricing not published | yes (in principle) | Survey/ag focus; uses CPE-owned bases. |
| **RTKdata** | rtkdata.com/br | NRTK | USD 40/mo · 30-day free trial | yes | International operator; BR station count not declared. |
| **TopNET Live (Topcon)** | regional | NRTK | Subscription; BR pricing not published | likely yes | South-America regional product; BR node count not declared. |
| **GEODNET (direct)** | `sa.geodnet.com:2101` | network | ~USD 40/mo, paid-only | yes | Project SOURCES removed 2026-04 as paid-only. |
| **rtk2go BR bases** | rtk2go.com:2101 | volunteer single-base | free, best-effort | yes | ~17 BR-coded mountpoints, concentrated SP + South (RS/SC/PR), a handful Amazon + NE. See `rtk2go.md`. |

### State-level CORS — no independent free caster verified

- **UNESP/FCT "Rede GNSS-SP"** (Presidente Prudente, SP): 11-station NTRIP caster, access by email to `gege@fct.unesp.br` describing institution + intended use. Operator self-describes as research-grade ("we can not offer reliability, availability and integrity"). Not hobbyist-suitable. Several of these stations are re-exposed in RBMC-IP (PPTE1, POLI1, ROSA1, UBA10) anyway.
- **IGC-SP / MG / RJ / BA state geodetic offices**: contribute stations to RBMC-IP, no independent state caster endpoint found.
- "IPGH RJ" mentioned in older surveys: IPGH is the SIRGAS umbrella organisation (regional), not a BR state operator.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| RBMC RINEX archive (per-station daily/hourly) | https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/rede-geodesica/16258-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-rbmc.html | Free (gov.br account) |
| IBGE PPP online (PPP-GPS) | https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16334-ppgps.html | Free |
| EarthScope NOTA select BR stations | https://www.earthscope.org/data/gnss-realtime/ | Free non-commercial |

## Sources

- IBGE RBMC-IP service page: https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16332-rbmc-ip-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-em-tempo-real.html
- gov.br RBMC-IP signup: https://www.gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip (verified 2026-05-23: "Este serviço é gratuito para o cidadão"; max 5 stations/user; 1,000 concurrent connections caster-wide; gov.br Bronze/Silver/Gold required)
- IBGE Dec 2024 (+5 stations): https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/42130-ibge-inaugura-cinco-novas-estacoes-da-rede-brasileira-de-monitoramento-continuo-e-publica-as-series-temporais-de-redes-geodesicas
- IBGE Dec 2025 (+3 stations, 153 total): https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/45406-ibge-inaugura-tres-novas-estacoes-da-rede-brasileira-de-monitoramento-continuo-e-publica-series-temporais-de-redes-geodesicas
- IBGE Dec 2023 (+6 stations, A Mira mirror): https://www.amiranet.com.br/noticia/ibge-operacionaliza-seis-novas-estacoes-da-rede-brasileira-de-monitoramento-continuo-e-publica-as-series-temporais-de-redes-geodesicas-380
- IBGE Resolução do Presidente nº 1/2015 (SIRGAS2000@2000.4): https://geoftp.ibge.gov.br/metodos_e_outros_documentos_de_referencia/normas/rpr_01_2015_sirgas2000.pdf
- geoRTK plans: https://www.geortk.com.br/planos · sobre (network basis): https://www.geortk.com.br/sobre · coverage map: https://www.geortk.com.br/ferramentas/mapa-de-cobertura (300+ stations claimed 2026-05-23, target 500 end-2026)
- GeoPlus (Geo+): https://geoplusbrasil.com/ · SPGeo: https://www.spgeo.com.br/rede-ntrip-ppp-rtk
- CPE RoverConnect: https://www.cpetecnologia.com.br/servico-de-correcao-rtk-ntrip-rover-connect-plano-semanal/p
- RTKdata Brasil: https://rtkdata.com/br/
- UNESP Rede GNSS-SP: https://www.fct.unesp.br/Home/Pesquisa/GEGE/GNSS_SP_Network.html
- ArduSimple BR overview: https://pt.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-brazil/
- Live probe `curl --http0.9 http://gps-ntrip.ibge.gov.br:2101/` 2026-05-23 → 149 STR / 31,267 bytes, 145 BRA + 4 BKG SSR/ephemeris
- Pipeline `scripts/stations_by_country.py BRA` 2026-05-23: 196 stations across rbmc_ip 147, igs_ip 23, rtk2go 16, auscors 8, mirai 2
