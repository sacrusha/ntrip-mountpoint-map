# Spain [ES] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (revision; original 2026-05-06)

## Status: YES — free national NTRIP (ERGNSS/SPTR) + multiple free regional casters; VRS; one of the densest free RTK ecosystems in Europe. ERGNSS/SPTR and CATNET sourcetables live-confirmed via direct NTRIP probe 2026-05-17.

**Note on Canary Islands:** The Canary Islands (ES-Canarias) are covered in a separate file (`ES-Canarias.md`) which details SPTR and GRAFCAN REPCAN. The national ERGNSS/SPTR service described below also covers the Canary Islands via its CERCANA3M mountpoint; refer to ES-Canarias.md for archipelago-specific caveats.

---

## Service A: ERGNSS / SPTR — IGN España (national, primary — FREE)

| Field | Value |
|---|---|
| **Operator** | IGN España — Instituto Geográfico Nacional |
| **host:port — network solutions (VRS/MAC/FKP)** | `ergnss-tr.ign.es:2101` (also IP 192.148.213.42) |
| **host:port — single-station** | `ergnss-tr.ign.es:2102` |
| **host:port — data-only caster** | `ergnss-ip.ign.es:2101` (also IP 193.144.251.13) |
| **VRS** | Yes — VRS3M, MAC3M, FKP3M, CERCANA3M (MSM); legacy: VRS3, MAC3, FKP3, CERCANA3 |
| **Best mountpoints** | `CERCANA3M` (auto-routes to nearest station, RTCM 3.2 MSM4, automatic failover); `VRS3M` (VRS, full network, MSM) |
| **tariff** | **Free — €0.00 / $0.00** (no VAT). Date observed: 2026-05-17. Source: https://www.ign.es/web/gds-gnss-tiempo-real |
| **hobbyist_eligibility** | **Yes** — open self-registration; no professional licence required; ~12,000 registered users as of Jan 2024 (~60% agricultural sector) |
| **legal_residency_required** | **No** — no residency restriction published |
| **last_confirmed_alive** | **2026-05-17** — sourcetable retrieved live from `ergnss-tr.ign.es:2101` (1 733 bytes; 8 STR rows: CERCANA3, CERCANA3M, FKP3, FKP3M, MAC3, MAC3M, VRS3, VRS3M; Server: NTRIP GNSMART_Caster 2.0/1.0; IP 192.148.213.42) |
| **datum_epoch** | Canary stations: REGCAN95 (operator-declared, 2024-02-01 coordinate update notice). Mainland: ETRS89 implied but **not** explicitly stated by IGN on the SPTR/ERGNSS page — `omitted -- no citable declaration for mainland`. Source: https://www.ign.es/web/gds-gnss-tiempo-real |

### ERGNSS/SPTR Network Details
- **Stations:** 272 GNSS reference stations (IGN permanent stations + stations from 13 regional autonomous community networks + Puertos del Estado tide gauge stations). Latest expansion (Jun 2025 transportes.gob.es presentation) adds PNAV, ARAJ, HOND
- **Processing:** Divided into 17 processing subnets for optimal RTK computation
- **Constellations:** GPS + GLONASS + Galileo + BeiDou (multi-constellation, RTCM 3.2 MSM4/MSM7)
- **Registration:** http://ergnss.ign.es/gnuserportal/
- **Max simultaneous connections:** 10 per account
- **Regional networks integrated:** ARAGEA (Aragón), ERVA (Valencia), ITACYL (Castilla y León), RAP (Andalucía), REGAM (Murcia), REP (Extremadura), RGAC (Cantabria), RGAN (Navarra), RGAPA (Asturias), RGE (Basque Country), RGM (Madrid), RIOJA (La Rioja), XGAIB (Balearic Islands), Puertos del Estado

---

## Service B: RAP Andalucía — Junta de Andalucía (regional, FREE)

| Field | Value |
|---|---|
| **Operator** | Junta de Andalucía — Instituto de Estadística y Cartografía de Andalucía |
| **host** | `rap.juntadeandalucia.es` (also IP 217.12.23.44) |
| **port** | Not publicly documented; standard NTRIP 2101 or contact IECA for parameters |
| **VRS** | Yes — RAP operates 22 multi-constellation GNSS stations + 6 shared with ERGNSS + 13 additional ERGNSS stations in/bordering Andalucía |
| **tariff** | **Free — €0.00** (gratuito). Date observed: 2026-05-06. Source: https://www.juntadeandalucia.es/institutodeestadisticaycartografia/rap |
| **hobbyist_eligibility** | **Yes** — open registration |
| **last_confirmed_alive** | RAP portal accessible 2026-05-06 |
| **datum_epoch** | omitted -- no citable operator declaration |

---

## Service C: CATNET — Institut Cartogràfic i Geològic de Catalunya (ICGC) (regional, FREE)

| Field | Value |
|---|---|
| **Operator** | Institut Cartogràfic i Geològic de Catalunya (ICGC; formerly ICC) |
| **host:port** | `catnet-ip.icgc.cat:2101` (previous host: `catnet-ip.icc.es:8080`; updated March 2019) |
| **VRS** | Yes — RTKAT virtual station service (RTCM 2.3 / 3.0 + centimetre precision) |
| **tariff** | **Free** — account registration required via ICGC. Date observed: 2026-05-17. Source: https://catnet-ip.icgc.cat/ |
| **hobbyist_eligibility** | **Yes** |
| **last_confirmed_alive** | **2026-05-17** — sourcetable retrieved live from `catnet-ip.icgc.cat:2101` (3 288 bytes; primary mountpoint `VRS3M` multi-GNSS GPS+GLO+GAL+BDS RTCM 3 MSM, plus ~25 single-station `<CODE>2_DGNSS` legacy RTCM 2 mountpoints; Server: GNSS Spider 7.11.1.109) |
| **datum_epoch** | omitted -- no citable operator declaration on the public portal |
- Service operational since January 2006; uses NTRIP protocol

---

## Additional Regional Networks (Free)

| Region | Network | Operator | Notes |
|---|---|---|---|
| Balearic Islands | XGAIB (Xarxa de Geodèsia Activa de les Illes Balears) | SITIBSA (Govern de les Illes Balears) | Integrated into ERGNSS; also accessible separately; free |
| Asturias | RGAPA (Red GNSS Activa del Principado de Asturias) | Principado de Asturias | **No authentication required** (open access); integrated into ERGNSS |
| Basque Country | RGE (Red GNSS de Euskadi) | Gobierno Vasco | Free, registration required; integrated into ERGNSS |
| Madrid | RGM (Red GNSS de Madrid) | Comunidad de Madrid | Integrated into ERGNSS |
| La Rioja | RIOJA network | Gobierno de La Rioja | Free; see iderioja.larioja.org |
| Navarra | RGAN | Gobierno de Navarra | Integrated into ERGNSS |
| Valencia | ERVA | ICV — Institut Cartogràfic Valencià | Free; own caster at icv.gva.es; also integrated into ERGNSS |
| Canary Islands | SPTR + GRAFCAN REPCAN | IGN / GRAFCAN | See `ES-Canarias.md` |

**Key point:** All the above regional networks are also accessible through the unified ERGNSS/SPTR national caster (`ergnss-tr.ign.es:2101`) via a single IGN registration — no need for separate accounts per region except for ICGC/CATNET (which has its own registration).

---

## Commercial Option: HxGN SmartNet Spain

HxGN SmartNet (Hexagon/Leica) operates in Spain but has no published public pricing portal for Spain specifically. Enterprise subscription; contact Hexagon España distributor. Given the richness of the free public network (ERGNSS + regional casters), HxGN SmartNet is not a typical hobbyist option in Spain.

---

## Practical Notes for Hobbyists

- **ERGNSS registration is free and open** — the main friction is completing the online form at ergnss.ign.es/gnuserportal. The GNSS Visor at ntrip.rep-gnss.es lists all active casters from Spanish public bodies.
- The recommended mountpoint for most users is `CERCANA3M` — it auto-selects the nearest physical station or VRS depending on network density, and provides RTCM 3.2 MSM4 corrections usable by all modern receivers.
- Canary Islands users: see `ES-Canarias.md` for CERCANA3M caveats in archipelago geometries and GRAFCAN REPCAN details.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ERGNSS RINEX archive** — per-station RINEX download | https://www.ign.es/web/gds-gnss-datos-observacion | Free (account required) |
| **CATNET RINEX** | https://catnet-ip.icgc.cat/ | Free |
| **RAP Andalucía RINEX** | https://www.juntadeandalucia.es/institutodeestadisticaycartografia/rap | Free |

## Sources Consulted
- Live NTRIP probe of `ergnss-tr.ign.es:2101` — 2026-05-17 (sourcetable retrieved, 8 STR; curl --http0.9)
- Live NTRIP probe of `catnet-ip.icgc.cat:2101` — 2026-05-17 (sourcetable retrieved, ~26 STR; curl --http0.9)
- IGN España ERGNSS/SPTR: https://www.ign.es/web/gds-gnss-tiempo-real
- ERGNSS registration: http://ergnss.ign.es/gnuserportal/
- GNSS Visor (REPGNSS casteres): http://ntrip.rep-gnss.es/casteres.php
- "El Servicio de Posicionamiento GNSS en Tiempo Real del IGN" — transportes.gob.es Jun 2025: https://www.transportes.gob.es/recursos_mfom/comodin/recursos/06_el-servicio-de-posicionamiento-gnss-en-tiempo-real-del-ign.pdf
- RAP Andalucía: https://www.juntadeandalucia.es/institutodeestadisticaycartografia/rap/nodos
- CATNET / ICGC: https://catnet-ip.icgc.cat/
- ERVA Valencia: https://icv.gva.es/es/web/icv-erva
- IDErioja GNSS La Rioja: https://www.iderioja.larioja.org/index.php?id=21&lang=en
- REDES GNSS PUBLICAS EN ESPAÑA (EPOS-ES 2023 presentation): https://epos-es.org/wp-content/uploads/2023/11/Presentaciones-ReunionGNSS_20231127.pdf
- ArduSimple Spain: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-spain/
- ES-Canarias.md (existing research file for Canary Islands)
