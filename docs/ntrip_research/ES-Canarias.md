# Canary Islands [ES-Canarias / EU-region] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 | EUR/USD: 1 EUR = 1.1686 USD (2026-05-05)
**Note:** Canary Islands are outside the EU VAT area — IGIC (7%) applies instead of Spain's standard 21% VAT.

## Status: TWO ACTIVE public NTRIP casters

---

## Service A: IGN España SPTR (FREE — recommended first)

| Field | Value |
|---|---|
| **host:port (network solutions)** | `ergnss-tr.ign.es:2101` |
| **host:port (single-station)** | `ergnss-tr.ign.es:2102` |
| **Best mountpoint for Canaries** | `CERCANA3M` (auto-routes to nearest station, RTCM 3.2 MSM4, automatic failover) |
| **tariff** | **Free — €0.00 / $0.00** (no VAT). Date observed: 2026-05-06. Source: https://www.ign.es/web/gds-gnss-tiempo-real |
| **hobbyist_eligibility** | **Yes** — no professional licence required; open self-registration. ~12,000 registered users as of Jan 2024, ~60% agricultural sector. |
| **legal_residency_required** | **No** — no residency restriction published |
| **last_confirmed_alive** | Portal accessible May 2026; REGCAN95 coordinate update for all Canaries stations: 2024-02-01; 272-station count confirmed in 2024–2025 documentation |

**Operator:** Instituto Geográfico Nacional (IGN España)
**Registration:** http://ergnss.ign.es/gnuserportal/
**Max simultaneous connections:** 10 per account

### IGN Canary Islands Stations (representative)
EH01 (El Hierro), FUER (Fuerteventura), GOME (La Gomera), IZAN (Tenerife/Izaña), LPAL (La Palma), LP01 (La Palma/Volcán), LZ01/LZ02 (Lanzarote), MASP (Gran Canaria), TN01/TN02/TN03 (Tenerife), ULP2 (Las Palmas GC) — 15–16 stations.

---

## Service B: GRAFCAN REPCAN (paid, Canarian regional network)

| Field | Value |
|---|---|
| **host:port** | `195.53.241.146:2101` (also `gnss.grafcan.es`) |
| **Best mountpoint for Canaries** | `CERCANA3M` (also: `GRAF3M`, `GRAF3`, individual station codes) |
| **tariff** | Annual fee per device/receiver — **amount NOT publicly disclosed**; purchase via https://tiendavirtual.grafcan.es (Tienda Virtual → sección Varios). Free for public administration with active SITCAN contract. Contact: datos@grafcan.com |
| **IGIC (local VAT)** | 7% IGIC applies (Canary Islands not in EU VAT area) — whether price is quoted net or gross not confirmed |
| **USD equivalent** | Not determinable — base EUR price not published |
| **Date observed** | 2026-05-06. Source: https://www.grafcan.es/servicios/red-estaciones-gnss/ |
| **hobbyist_eligibility** | Unclear — no explicit surveying licence requirement, but billing process implies institutional context (invoice required in registration form) |
| **legal_residency_required** | Unclear — no stated restriction |
| **last_confirmed_alive** | Hardware update Jan 2024; website active Dec 2024; data archive active 2025–2026; REGCAN95 update 2024-02-01 |

**Operator:** Cartografía de Canarias S.A. (GRAFCAN)
**Stations:** 20 stations (AGUI, ALDE, ALJR, ANTI, ARGU, FRON, GRAF, HRIA, LIVA, MAZO, MORJ, OLIV, SNMG, STEI, STTE, TERR, TIAS, TRLJ, VHMO, YAIZ)
**Format:** RTCM 3.2 MSM5 (most stations); CMR+/RTCM 2.3 on SNMG and TIAS only
**Registration:** https://pre-web.grafcan.es/servicios/red-estaciones-gnss/alta-gnss/

---

## Network RTK Caveat

Both GRAFCAN and IGN explicitly note that network RTK solutions (VRS/MAC/FKP) are **less reliable in archipelago geometries**. `CERCANA3M` (nearest single station with automatic failover) is the officially recommended mountpoint for the Canary Islands on both systems.

---

## Services Investigated and Excluded

| Network | Finding |
|---------|---------|
| HxGN SmartNet Spain | No confirmed Canary Islands coverage; Spanish distributor offices only on mainland/Mallorca |
| Centipede-RTK | No Canary Islands stations confirmed |
| RTK2GO | No Canary Islands mountpoints found |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **GRAFCAN RINEX archive** — daily/hourly RINEX for all 20 REPCAN stations; open FTP/HTTP access | https://gnss.grafcan.es/ | **Free** (open directory, no account required) |
| **IGN ERGNSS RINEX download** — RINEX for all IGN Canaries stations via national geodata portal | https://www.ign.es/web/gds-gnss-datos-observacion | **Free** (account registration required) |

## Sources
- https://www.ign.es/web/gds-gnss-tiempo-real
- https://www.grafcan.es/servicios/red-estaciones-gnss/
- https://tiendavirtual.grafcan.es
- https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-spain/
- https://ntrip-list.com/europe/
- https://www.idecanarias.es/listado_servicios/red-geodesica-activa-gnss
- exchange-rates.org (EUR/USD 2026-05-05)
