# El Salvador [SV] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (revised from 2026-05-06 — pricing reconfirmed, EarthScope SSIA scientific stream verified inside SV territory)

## Status: YES — active private NTRIP caster (Survey3G); no government caster; one free scientific EarthScope NOTA stream (SSIA, near San Salvador) is also available with a noncommercial-use account

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private commercial, subscription-based) |
| **Operator** | Survey GC SA. de C.V. (trading as **Survey3G**), San Miguel, El Salvador |
| **Network name** | NTRIP SURVEY — El Salvador |
| **host:port — Survey3G** | not published; IP, port, username, password disclosed by email after subscription payment |
| **tariff — Survey3G (2026, USD)** | USD 15 / 7 days · USD 30 / 15 days · USD 45 / 30 days (monthly) · USD 135 / 3 months · USD 450 / 12 months (source: survey3g.com/servicios-de-ntrip/, reconfirmed 2026-05-13 — page header explicitly labels schedule "2026"); El Salvador uses USD as official currency; no VAT (IVA) line-itemed on the published schedule |
| **hobbyist_eligibility** | Yes — subscription open to individuals; no surveyor licence or professional registration required |
| **legal_residency_required** | No explicit requirement stated; appears to target El Salvador-based users but no residency gate on sign-up |
| **last_confirmed_alive** | 2026-05-13 — `survey3g.com/servicios-de-ntrip/` HTTP 200 with 2026 price schedule; curl-probe of an undisclosed Survey3G IP:port not possible from sandbox (no public host:port) |

## EarthScope NOTA — SSIA (scientific real-time stream inside El Salvador)

A single EarthScope NOTA / COCONet station is located inside Salvadoran territory at the Servicio Nacional de Estudios Territoriales (SNET) site in San Salvador. It is reachable as a free single-base RTCM 3 stream under EarthScope's noncommercial NULA licence, distinct from Survey3G:

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (TCP) / `:443` (TLS) |
| **Mountpoint** | `SSIA_RTCM3P3` (single-base RTCM 3 from station SSIA, 13.70°N, –89.12°W; country tag SLV in `data/stations.json`) |
| **Stream type** | Single-base RTCM 3 — not VRS. Suitable for short-baseline RTK from San Salvador and the central highlands |
| **tariff — noncommercial** | Free (NOAA / NSF NULA — Non-commercial Use License Agreement; EarthScope account required) |
| **tariff — commercial** | USD 1,000 / seat / year (EarthScope commercial licence, 2024) |
| **hobbyist_eligibility** | Yes — open to noncommercial users worldwide; NULA acceptance required |
| **legal_residency_required** | No |

A second NOTA station, CN21 (Honduras side, ~194 km east of San Salvador) is too far for single-base RTK but useful for PPK / post-processing in eastern El Salvador. (Verified 2026-05-13 via `py scripts/stations_by_radius.py 13.7 -89.2 200`.)

## Most Recent Project Announcement

No formal government announcement. Survey3G describes itself as "pioneer in El Salvador" for NTRIP, operating continuously since launch. The price schedule on `survey3g.com/servicios-de-ntrip/` is dated 2026 (page reconfirmed 2026-05-13). The legacy `survey3g.com/ntrip/` slug remains 404; current pricing is at `servicios-de-ntrip/`.

## Context Notes

- **Survey3G** (survey3g.com): A private geomatics company — legal name **Survey GC SA. de C.V.** — based in Residencial Obrajuelo, AV Quetzalcoatl, Casa 12 Polg #3, Quelepa, San Miguel, El Salvador. Distributes South, CHCNav, Topcon, and DWSitePro equipment and operates the only known national NTRIP correction network. The company brands itself as "el primer proveedor de NTRIP en El Salvador." Email `survey3g@hotmail.com`, phone +503 7031-5173. WhatsApp / Facebook / YouTube linked from the homepage.
- **CORS stations (6):** SAN MIGUEL, PERKÍN, LA UNIÓN, SAN SALVADOR (UES — Universidad de El Salvador, for research/education only — labeled temporary), SANTA ANA, COJUTEPEQUE. Each station covers approximately 50 km radius; combined coverage claims ~90 % of the national territory. Constellations: GPS + GLONASS + BeiDou + Galileo L1/L2/L5 at all stations.
- **Activation lead time:** New subscribers require 48 hours advance notice for configuration and testing; existing subscribers need 32 hours. Credentials are unique per subscription period (start/end dates). No automatic renewal.
- **Internet requirement:** Standard data connection required (promotional or capped packages may cause issues per operator policy).
- **Service interruptions:** Lost days from outages beyond operator control are added proportionally to the subscription at no cost.
- **Host:port:** Not disclosed publicly. Provided via email after subscription confirmation. Users configure IP, port, username, and password in their NTRIP client.
- **Connectivity test:** Available on request before purchase ("Si quieres realizar una prueba de conectividad, escríbenos").
- **No national government NTRIP caster found.** Centro Nacional de Registros (CNR) manages geodetic infrastructure but no publicly documented NTRIP stream was found.
- **SIRGAS-RT:** El Salvador appears in historical SIRGAS RT cooperation documents for Central America but no active SIRGAS-RT caster node for El Salvador was found in public registries.
- **Volunteer (rtk2go / Centipede / commercial):** zero confirmed SV bases on rtk2go or Centipede (2026-05-13). No GEODNET, ONOCOY, HxGN SmartNet, Topcon TopNET Live, or Trimble VRS Now coverage confirmed for El Salvador.
- **Global commercial fallbacks:** Galileo HAS (~25–40 cm, no internet); own base-station setup; EarthScope SSIA for a free NULA-bound single-base alternative.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope NOTA SSIA + CN21** (San Salvador + Honduras border) RINEX | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (NULA + account); USD 1,000/seat/yr commercial |
| **SIRGAS station data** (stations shared with SIRGAS) | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |
| **NOAA NGS CORS** (any shared El Salvador stations in NCN) | https://geodesy.noaa.gov/CORS/ | Free |

## Sources Consulted
- Survey3G services page: https://survey3g.com/servicios-de-ntrip/ — HTTP 200, 2026 tariff table reconfirmed 2026-05-13
- Survey3G homepage: https://survey3g.com/ — company address, contact info, equipment brands reconfirmed 2026-05-13
- Survey3G NTRIP policy: https://survey3g.com/politicas-de-servicios-ntrip/ — activation rules, coverage, service interruption policy (confirmed 2026-05-06)
- Survey3G NTRIP page: https://survey3g.com/ntrip/ — HTTP 404 (pricing now at `servicios-de-ntrip/`)
- EarthScope NOTA real-time portal: https://www.earthscope.org/data/gnss-realtime/
- EarthScope licensing / NULA + USD 1,000 commercial seat: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- `data/stations.json` cross-check (`py scripts/stations_by_radius.py 13.7 -89.2 200`) — SSIA EarthScope station confirmed inside El Salvador, country tag SLV
- SIRGAS-RT bulletins (sirgas.ipgh.org)
- rtcm-ntrip.org (no El Salvador entries found)
- ArduSimple El Salvador page (no dedicated page found)
- rtk2go / Centipede — zero SV-coded bases (2026-05-13)
