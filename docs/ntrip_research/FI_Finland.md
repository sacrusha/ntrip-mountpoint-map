# Finland [FI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (revision; original 2026-05-06)

## Status: MIXED — two free NLS casters (DGNSS free/open, live-confirmed; RTK research-only restricted); dense volunteer rtk2go coverage (~129 FIN bases); paid commercial options

**NLS 2026 price update note:** The 2026-01-01 NLS price changes apply to property-owner/cadastral charges; the announcement explicitly notes that "the prices of the Land Information Service as well as interface services and data services will remain unchanged" — FINPOS DGNSS therefore remains free in 2026 (re-checked 2026-05-17).

---

## Service A: FINPOS DGNSS — National Land Survey of Finland (FREE, open)

| Field | Value |
|---|---|
| **Operator** | NLS — Maanmittauslaitos (National Land Survey of Finland) |
| **host:port — unencrypted** | `opencaster.nls.fi:2102` |
| **host:port — TLS encrypted** | `opencaster.nls.fi:2105` |
| **VRS** | No — nearest physical station auto-selected |
| **Mountpoints** | `DGNSS` (nearest station, RTCM 2.2); `DGNSS-12SAT` (up to 12 satellites, older receivers); `DGNSS-MSM1` (nearest station, RTCM 3.2) |
| **Accuracy** | **~0.5 m** — this is a DGNSS service only (submeter, not RTK-grade centimetre) |
| **tariff** | **Free — €0.00.** Open data. Credentials via free registration. Date observed: 2026-05-17. Source: https://www.maanmittauslaitos.fi/en/finpos/dgnss |
| **hobbyist_eligibility** | **Yes** — open registration, no licence check |
| **legal_residency_required** | **No** |
| **last_confirmed_alive** | **2026-05-17** — sourcetable retrieved live from `opencaster.nls.fi:2102` (919 bytes; 4 STR rows: DGNSS, DGNSS-12SAT, DGNSS-MSM1, DGNSS-PIES; Server: NTRIP GNSMART_Caster 2.0/1.0) |
| **datum_epoch** | EUREF-FIN (operator: "The corrections are accompanied by the EUREF-FIN coordinates for the reference stations"); epoch not stated by operator. Source: https://www.maanmittauslaitos.fi/en/finpos/dgnss |

**Important:** This is a DGNSS (submeter) service, **not RTK** (centimetre). It is free and open but does not meet RTK-grade accuracy requirements.

---

## Service B: FINPOS RTK — National Land Survey of Finland (RESTRICTED — research/testing only)

| Field | Value |
|---|---|
| **Operator** | NLS — Maanmittauslaitos |
| **host:port** | `opencaster.nls.fi:2101` (unencrypted); `opencaster.nls.fi:2105` (TLS) |
| **VRS** | Yes — VRS-FKP (virtual reference station using network error modelling); also SINGLE (nearest station), LIIKKUVA-VRS, LIIKKUVA-SINGLE |
| **Mountpoints** | `VRS-FKP`, `SINGLE`, `VRS-FKP-OLD` (RTCM3.1 legacy), `LIIKKUVA-VRS`, `LIIKKUVA-SINGLE` |
| **tariff** | Not applicable — access is **not for sale**; granted on application for 3-month periods (renewable with feedback) |
| **hobbyist_eligibility** | **No** — restricted to "research and testing purposes, for example, for the development of new positioning methods, devices and services." Justification for use required at registration. |
| **legal_residency_required** | Unclear — Finnish research institution preferred |
| **last_confirmed_alive** | maanmittauslaitos.fi/en/finpos/rtk accessible 2026-05-17 (registration gated) |
| **datum_epoch** | EUREF-FIN (same NLS frame as FINPOS DGNSS). Source: https://www.maanmittauslaitos.fi/en/finpos/dgnss |

- **FinnRef network:** ~50 reference stations; modernised 2012–2014 (20 stations), further densified 2017–2018 to ~50
- **Note (Dec 2024):** NLS stopped sending real-time GNSS data to the EUREF EPN on 1 December 2024 (Finnish Government announcement); this affects European geodetic data exchange but does not change the domestic FINPOS service availability.

---

## Service C: Trimnet VRS (Geotrim Oy) — commercial, paid

| Field | Value |
|---|---|
| **Operator** | Geotrim Oy (Trimble distributor Finland) |
| **host** | trimnet.fi (login portal); NTRIP host provided after subscription |
| **VRS** | Yes — VRS technology; ~130 reference stations across Finland |
| **tariff** | Not published publicly; "request a quote" model; contact geotrim.fi for per-device pricing. Date observed: 2026-05-06. Source: https://geotrim.fi/palvelut/trimnet-vrs/ |
| **hobbyist_eligibility** | **Unclear** — primarily professional/enterprise |
| **last_confirmed_alive** | geotrim.fi accessible 2026-05-06; trimnet.fi login portal active |
| **datum_epoch** | omitted -- no citable operator declaration |

- Products: Trimnet Pro, Trimnet Pro+, Trimnet Pro+ ADV; 1–2 cm RTK accuracy; nationwide Finland coverage

---

## Service D: HxGN SmartNet Finland (Hexagon / Leica)

| Field | Value |
|---|---|
| **Operator** | Geosystems Finland Oy (Hexagon distributor) |
| **host:port** | Not published without subscription |
| **VRS** | Yes — HxGN SmartNet NRTK |
| **tariff** | Not published; enterprise subscription; contact hxgnsmartnet.com |
| **hobbyist_eligibility** | **Unclear** |
| **last_confirmed_alive** | hxgnsmartnet.com accessible 2026-05-06 |
| **datum_epoch** | omitted -- no citable operator declaration |

---

## Volunteer Coverage (Best Free RTK Option for Hobbyists)

Finland has exceptionally dense volunteer RTK coverage — the best in the EU:

| Network | Finland-coded stations | Notes |
|---|---|---|
| **RTK2go** | ~129 FIN-coded bases (data/stations.json, last verified 2026-05-12) | Concentrated in southern Finland and around Helsinki; no QoS guarantee |
| **Centipede** | 18 FIN-coded nodes (data/stations.json, last verified 2026-05-12) | Sparse but growing |

This volunteer density makes Finland one of the best-covered countries for free hobbyist RTK in Europe despite the absence of a free government RTK caster.

## Practical Notes for Hobbyists

- For free centimetre RTK: use RTK2go volunteer bases (dense in south Finland). Connect to `rtk2go.com:2101`, select a FIN-coded mountpoint near your location.
- For submeter positioning (free, open): use FINPOS DGNSS at `opencaster.nls.fi:2102`.
- For centimetre RTK nationally: subscribe to Trimnet (Geotrim) or HxGN SmartNet.
- FINPOS RTK is not accessible to hobbyists without institutional justification.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **FINPOS RINEX** — free open data via NLS | https://www.maanmittauslaitos.fi/en/finpos/raakadata | Free (account required) |
| **EUREF/EPN** — Finnish EPN stations | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- NLS FINPOS overview: https://www.maanmittauslaitos.fi/en/finpos
- NLS DGNSS service: https://www.maanmittauslaitos.fi/en/finpos/dgnss
- NLS RTK service: https://www.maanmittauslaitos.fi/en/finpos/rtk
- NLS stops EPN data (Dec 2024): https://mmm.fi/en/-/national-land-survey-of-finland-stops-sending-real-time-gnss-data-to-epn-on-1-december-2024-
- FinnRef stations: https://www.maanmittauslaitos.fi/en/research/research/other-research-and-measuring-stations/finnref-gnss-stations
- Geotrim / Trimnet VRS: https://geotrim.fi/palvelut/trimnet-vrs/
- HxGN SmartNet: https://hxgnsmartnet.com/services/smartnet-nrtk
- ResearchGate — FinnRef vs Trimnet coverage (2018 paper): https://www.researchgate.net/figure/Nationwide-NRTK-networks-in-Finland-FinnRef-left-is-operated-by-the-FGI-NLS-TrimNet_fig1_330659680
- ArduSimple Finland page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-finland/
- NTRIP-list.com Europe (FinnRef free entry): https://ntrip-list.com/europe/
