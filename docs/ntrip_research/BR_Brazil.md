# Brazil [BR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior 2026-05-15)

## Status: YES — free national government caster (RBMC-IP) + multiple commercial casters; no separately-accessible state-level free caster verified

## Primary caster — RBMC-IP (IBGE)

| Field | Value |
|---|---|
| **landing_url** | https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16332-rbmc-ip-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-em-tempo-real.html |
| **access_url** | https://www.gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip |
| **host:port** | `gps-ntrip.ibge.gov.br:2101` (advertised alt IP `170.84.40.52:2101`) — re-probed 2026-05-17, HTTP 200, 30,466 bytes, 146 total `STR;` rows of which 142 country=BRA (down from 147 BRA on 2026-05-15; likely transient outage of ~5 stations, sourcetable composition else unchanged) |
| **tariff** | Free; gov.br federal account required; cap of 5 simultaneous mountpoints per user; 1,000 concurrent connections caster-wide (per IBGE service page, observed 2026-05-17) |
| **num_stations** | 153 physical RBMC stations declared operational (IBGE Dec 2025 announcement); 142 BRA-coded streams in live sourcetable 2026-05-17 (was 147 on 2026-05-15). Gap of ~11 = stations offline, RINEX-only, or announced-but-not-yet-streaming (see Caruaru below). |
| **vrs** | No — single-base; mountpoints map 1:1 to physical sites (e.g. `BRAZ1`, `POLI1`, `CUIB1`) |
| **hobbyist_eligibility** | Yes — open to any user, no professional licence required |
| **legal_residency_required** | No — gov.br registration is open to non-residents (CPF *or* passport accepted at signup; foreign-passport path documented on gov.br) |
| **last_confirmed_alive** | 2026-05-17 — `curl http://gps-ntrip.ibge.gov.br:2101/` HTTP 200, 30,466 bytes, 142 BRA `STR;` rows |
| **datum_epoch** | SIRGAS2000, epoch 2000.4 — Brazilian official geodetic reference frame since 2005 per IBGE [Resolução do Presidente nº 1/2015](https://geoftp.ibge.gov.br/metodos_e_outros_documentos_de_referencia/normas/rpr_01_2015_sirgas2000.pdf) (mandates SIRGAS2000 as national frame; epoch 2000.4 is the SIRGAS realisation reference epoch, not directly re-declared per-RBMC-IP stream by IBGE). Sourcetable also exposes `SIRGAS00001`/`SIRGAS00002` IGS-combination SSR streams (BKG passthroughs, station = Frankfurt — not RTK, out of scope) |

### Mountpoint conventions

- Per-station single-base streams: 5-character RBMC code + `1` (or `0` for legacy), e.g. `BRAZ1` (Brasília), `POLI1` (USP São Paulo), `POAL1` (Porto Alegre), `CUIB1` (Cuiabá), `RNNA1` (Natal). Format RTCM 3.0, messages 1004/1006/1008/1012/1013/1019/1020/1033, GPS+GLONASS legacy obs (no MSM, no BDS/GAL multi-const in standard streams). A handful of streams advertise Galileo/BDS where receiver supports it but message-number evidence in the live sourcetable still leans 1004/1012 legacy.
- **MSM / multi-constellation status for 2023-25 new stations** (MGGV, ALMC, ROCO0, STHA0, ROSA0, SPLI0): live sourcetable 2026-05-17 shows these stations using the same RTCM 3.0 legacy message set as older RBMC stations (1004/1006/1008/1012/1013/1019/1020/1033, GPS+GLONASS). No MSM7 (107x/108x/109x/110x/111x) and no per-station BDS/GAL multi-const observation streams confirmed for the new mountpoints. If IBGE has plans to upgrade RBMC-IP to MSM/multi-const, no public announcement has surfaced.
- SSR/ephemeris passthroughs from BKG Frankfurt: `SSRA02IGS0_SIRGAS2000`, `SSRA03IGS0_SIRGAS2000`, `SSRA03IGS0`, `BCEP00BKG0` — **NOT RTK, out of project scope**. These are SSR/PPP-RTK and broadcast-ephemeris streams (per primer: SSR ≠ OSR, not single-base or NRTK corrections); they are useful only to PPP-RTK / ephemeris-only clients, not to the hobbyist RTK rover use case the project targets. Pipeline should not treat these as RTK mountpoints.

### Coverage

All 26 states + Federal District. Densest in SP/MG/RJ/PR/RS (south-east + south). Sparse but present in Amazon basin (POVE-Porto Velho RO, PAAR-Altamira PA, AMHA, AMPT, AMTE in AM) and north-east interior. Useful single-base RTK baseline radius ~30 km per IBGE (commonly extended to 50–70 km in practice with degraded accuracy).

### Recent expansion

- 2024-12-09: 5 new stations inaugurated — Governador Valadares (MG, MGGV), Maceió (AL, ALMC), Januária (MG), Pinhais (PR), Nova Friburgo (RJ). MGGV and ALMC replace legacy GVA1/ALMA codes. (IBGE Agência de Notícias)
- 2023-12-20: 6 new stations operationalized — Blumenau/SC, Cascavel/PR, Guajará-Mirim/RO, Guaíra/PR, Irecê/BA, Resende/RJ. Total reached 147 then. (A Mira)
- 2025-12 (per IBGE communications): 3 new stations inaugurated at Caruaru (PE), Colorado do Oeste (RO), Santa Helena (PR). Total cited: **153 stations**. Live sourcetable 2026-05-17: `ROCO0` (Colorado do Oeste) and `STHA0` (Santa Helena) confirmed streaming; **no Caruaru / PE mountpoint present** — announced but not yet live. (IBGE news / X account; confirmed via MundoGEO Connect 2025 mirror)
- Sourcetable also includes `ROSA0` (Rosana, SP) and `SPLI0` (Lins, SP) — these were on IBGE's pre-2025 expansion roadmap and are now operational; exact inauguration date not pinned down in this pass.
- Strategic expansion plan announced 2024 targets ongoing growth focused on major population centres; no public 2026 inauguration list yet at time of research.

## Commercial / volunteer alternatives

| Provider | Endpoint | Type | Tariff (BRL unless noted, observed 2026-05-15) | hobbyist | Notes |
|---|---|---|---|---|---|
| **geoRTK** | host:port not published pre-registration, confirmed via signup-flow inspection (configured per account after signup at geortk.com.br) | network RTK + PPK | R$10/day · R$79/week · R$219/month · R$2,099/year (=R$175/mo equiv); 30-day free trial; monthly cancel anytime, annual cancel within first 30 days; no VAT statement on pricing page | Yes | Launched 1 Sep 2025; 500-station target by end-2026; coverage map at geortk.com.br/ferramentas/mapa-de-cobertura. 1 concurrent user per plan tier |
| **Geo+ (GeoPlus / Guandalini / SPGeo reseller)** | endpoint per-account; landing geoplusbrasil.com or spgeo.com.br/rede-ntrip-ppp-rtk | hybrid NRTK + PPP-RTK | Quote via WhatsApp/contact form; no public price list; plans NRTK / PPP-RTK / ULTIMATE; daily / weekly / monthly / annual on demand | ? (treated as B2B agro/survey) | Claims 130+ bases (SP near-total) expanding S/SE/NE; "100% Brazilian hybrid infrastructure" per Mundogeo 2025-12-09 piece |
| **RoverConnect (CPE Tecnologia)** | endpoint per-account | single-base NTRIP | Weekly/monthly prepaid via cpetecnologia.com.br; pricing requires product page open | Yes | Surveying / ag focus; uses CPE-owned bases |
| **RTKdata** | rtkdata.com/br | network RTK | USD 40/month; 30-day free trial | Yes | International multi-country operator; BR-specific station count not declared |
| **TopNET Live (Topcon)** | topconpositioning.com regional | network RTK | Subscription; BR pricing not published | Likely yes (commercial subscription) | South-America regional product; BR node count not declared |
| **rtk2go** (volunteer/Centipede-style) | rtk2go.com:2101 | volunteer single-base | Free, best-effort | Yes | ~17 BR-coded bases (see local data); concentrated SP metro + south (RS/SC/PR); a handful in Amazon (NTRIPTEC -3.23/-52.23) and north-east (m2f_eng BA) |

## State-level CORS

Despite expectations of state programs, **no independent free public NTRIP caster at the state level was verified** as of 2026-05-15:

- **São Paulo — UNESP/FCT "Rede GNSS-SP"**: An NTRIP caster is documented at FCT/UNESP Presidente Prudente listing 11 stations (SPAR, CHPI, SPCA, NEIA, ILHA, OURI, PPTE, ROSA, SJRP, POLI, UBAT). Access by email request to `gege@fct.unesp.br` describing institution and intended use. Operator self-describes as **research-grade**: "we can not offer reliability, availability and integrity." Treated as not hobbyist-suitable. Some of these stations are also re-exposed inside RBMC-IP (PPTE1, POLI1, ROSA1, UBA10).
- **IGC-SP** (Instituto Geográfico e Cartográfico, SP state geodetic office): contributes stations to RBMC-IP; no independent state caster endpoint found.
- **MG / RJ / BA**: same pattern — state-operated reference sites feed RBMC-IP rather than running independent casters.
- **IPGH RJ / "Topcon NTRIP"** (mentioned in older surveys): no current independent caster confirmed; IPGH is the SIRGAS umbrella organisation (regional), not a Brazilian state operator.

## Post-Processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| RBMC RINEX archive (IBGE) — per-station daily/hourly | https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/rede-geodesica/16258-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-rbmc.html | Free (gov.br account required) |
| IBGE PPP online (PPP-GPS) | https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16334-ppgps.html | Free |
| EarthScope NOTA — select BR stations | https://www.earthscope.org/data/gnss-realtime/ | Free non-commercial (NULA) |

## Probes & sandbox notes

- `curl http://gps-ntrip.ibge.gov.br:2101/` — 2026-05-17 HTTP 200, 30,466 bytes, 146 total STR / 142 BRA (was 30,915 bytes / 147 BRA on 2026-05-15; ~5-station net dropout, likely transient).
- `geortk.com.br/planos` WebFetch 2026-05-17 confirms unchanged BRL pricing: R$10/day · R$79/week · R$219/month · R$2,099/year, 30-day free trial.
- `agenciadenoticias.ibge.gov.br` HTTP 403 to WebFetch (anti-bot); MundoGEO / MundoGEO Connect / A Mira mirrors usable.
- **GEODNET / Onocoy Brazil probe (2026-05-17)**: GEODNET runs a paid South-America node `sa.geodnet.com:2101` (~USD 40/month, removed from project SOURCES 2026-04-20 as paid-only — per `scripts/fetch_stations.py` SOURCES comments and `docs/rtk_inventory.md#geodnet_sa`). HYFIX.AI / GEODNET public map (geodnet.com) shows triangle nodes inside Brazil but the operator's NTRIP service is gated behind subscription; no free hobbyist tier — out of project scope. Onocoy public coverage map (onocoy.com) and Centipede crowd-source map were both checked: Onocoy lists no BR-located miner node in the Brazil region as of 2026-05-17 (positive negative). Hobbyist-eligible free routes for BR remain RBMC-IP (gov), EarthScope NOTA selected stations, and rtk2go volunteer bases (~17 BR-coded as of 2026-05-15).

## Sources

- IBGE RBMC-IP service page: https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16332-rbmc-ip-rede-brasileira-de-monitoramento-continuo-dos-sistemas-gnss-em-tempo-real.html
- IBGE RBMC-IP English page: https://www.ibge.gov.br/en/geosciences/geodetic-positioning/services-for-geodetic-positioning/19291-brazilian-network-for-continuous-monitoring-of-the-gnss-systems-in-real-time.html
- gov.br RBMC-IP access (signup): https://www.gov.br/pt-br/servicos/obter-acesso-a-rbmc-ip
- IBGE Dec 2024 (5 new stations): https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/42130-ibge-inaugura-cinco-novas-estacoes-da-rede-brasileira-de-monitoramento-continuo-e-publica-as-series-temporais-de-redes-geodesicas
- IBGE Dec 2025 (3 new stations, 153 total): https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/45406-ibge-inaugura-tres-novas-estacoes-da-rede-brasileira-de-monitoramento-continuo-e-publica-series-temporais-de-redes-geodesicas
- IBGE Dec 2023 (6 new stations, A Mira mirror): https://www.amiranet.com.br/noticia/ibge-operacionaliza-seis-novas-estacoes-da-rede-brasileira-de-monitoramento-continuo-e-publica-as-series-temporais-de-redes-geodesicas-380
- MundoGEO Dec 2024 coverage: https://mundogeo.com/2024/12/16/ibge-inaugura-5-novas-estacoes-da-rbmc-e-publica-series-temporais-de-redes-geodesicas/
- SIRGAS-RT NTRIP project background: https://sirgas.ipgh.org/docs/Boletines/Bol14/38_Hoyer_et_al_NTRIP_SIRGAS_RT.pdf
- UNESP Rede GNSS-SP: https://www.fct.unesp.br/Home/Pesquisa/GEGE/GNSS_SP_Network.html
- geoRTK plans: https://www.geortk.com.br/planos · launch news: https://www.geortk.com.br/noticias/geortk-lanca-rede-rtk-no-brasil-com-cobertura-quase-nacional-e-precos-competitivos · coverage map: https://www.geortk.com.br/ferramentas/mapa-de-cobertura
- GeoPlus (Geo+) network: https://geoplusbrasil.com/ · SPGeo reseller page: https://www.spgeo.com.br/rede-ntrip-ppp-rtk · MundoGEO 2025-12-09 hybrid-infrastructure piece: https://mundogeo.com/2025/12/09/guandalini-redefine-a-precisao-no-campo-com-o-servico-geo-a-unica-infraestrutura-hibrida-100-brasileira/
- CPE RoverConnect: https://www.cpetecnologia.com.br/servico-de-correcao-rtk-ntrip-rover-connect-plano-semanal/p
- RTKdata Brasil: https://rtkdata.com/br/
- ArduSimple BR overview: https://pt.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-brazil/
- Emlid community BR NTRIP thread: https://community.emlid.com/t/estacoes-de-referencia-base-correcoes-ntrip-para-rtk-recursos-no-brasil/15553
- Pipeline / local data: rtk2go BR-coded bases (17, per `scripts/stations_by_country.py BRA`); sourcetable probe live 2026-05-15
