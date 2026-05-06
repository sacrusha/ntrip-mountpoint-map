# Denmark [DK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO free public NTRIP — three registered commercial providers; state contributes stations but provides no public free caster

---

## Regulatory Context

Klimadatastyrelsen (Danish Climate Data Agency, formerly Geodatastyrelsen) is the national geodetic authority. It **registers and controls** commercial GNSS positioning service providers for use in cadastral and official surveying, but operates **no free public NTRIP caster** itself. The authority contributes 13 reference stations to the GPSnet/RTKconnect infrastructure. Free RINEX archiving is available via Dataforsyningen.

---

## Service A: GPSnet.dk (Geoteam A/S) — primary cadastral network

| Field | Value |
|---|---|
| **Operator** | Geoteam A/S, Ballerup (registered: 2008-09-01) |
| **host:port** | Not published without subscription; SIM-card-based delivery model; contact geoteam.dk for credentials |
| **VRS** | Yes — based on Trimble VRS technology; "RTK corrections with 2 cm accuracy across all of Denmark" |
| **tariff** | Short-term login: 1 week / 1 month / 3 months available via geoteam.dk/produkt/Referencenet/729/korttidslogin — **specific DKK amounts not publicly displayed** (prices shown after login/quote). Annual subscriptions for surveying, agriculture, construction, drones — contact Geoteam. Date observed: 2026-05-06. Source: https://www.geoteam.dk/produkter/gpsnetdk |
| **hobbyist_eligibility** | **Yes** — multiple subscription tiers including "drone" and "research and development"; no professional licence check stated |
| **legal_residency_required** | **Unclear** — no explicit restriction; Danish company; SIM card delivery implies Danish telecom |
| **last_confirmed_alive** | geoteam.dk portal accessible 2026-05-06; approved by Klimadatastyrelsen for cadastral use |

- **Stations:** Contributing stations from Klimadatastyrelsen (13) + Geoteam proprietary stations; Klimadatastyrelsen announced expansion to 15 state stations (April 2025 Hanstholm addition)
- **Format:** RTCM, CMRx; VRS network solution

---

## Service B: HxGN SmartNet Denmark (Hexagon / Leica Geosystems)

| Field | Value |
|---|---|
| **Operator** | Leica Geosystems A/S, Herlev (registered: 2008-09-01; now Hexagon) |
| **host:port** | Not published without subscription; contact hxgnsmartnet.com/da |
| **VRS** | Yes — Hexagon HxGN SmartNet NRTK |
| **tariff** | Not published; enterprise subscription; contact Hexagon Denmark distributor. Date observed: 2026-05-06. Source: https://hxgnsmartnet.com/da/services/smartnet-nrtk |
| **hobbyist_eligibility** | **Unclear** — primarily professional/enterprise |
| **legal_residency_required** | **Unclear** |
| **last_confirmed_alive** | hxgnsmartnet.com/da accessible 2026-05-06 |

---

## Service C: RTKconnect.dk (RTKconnect ApS) — newest, 110+ stations

| Field | Value |
|---|---|
| **Operator** | RTKconnect ApS, Holstebro (registered: 2024) |
| **host:port** | Not published without subscription; contact rtkconnect.dk |
| **VRS** | Yes — FKP (Flächen-Korrektur-Parameter) pseudo-reference network solution; also supports traditional VRS |
| **tariff** | **6,599 DKK + VAT / year** (1-year subscription); **19,797 DKK + VAT / 3 years** (includes support contract valued at 7,164 DKK); volume pricing 2,999 DKK/user/year for 11+ simultaneous users. VAT rate: 25% (Denmark standard). Date observed: 2026-05-06. Source: https://rtkconnect.dk/products/rtk-netvaerk |
| **hobbyist_eligibility** | **Yes** — single-login per subscription, unlimited devices; no licence requirement stated |
| **legal_residency_required** | **Unclear** |
| **last_confirmed_alive** | rtkconnect.dk accessible and showing 100% uptime (last 365 days) as of 2026-05-06 |

- **Stations:** ~111 base stations including 13 from Klimadatastyrelsen; avg baseline 10 km
- **Precision:** Class A typical — <1 cm horizontal, <2 cm vertical
- **Format:** RTCM3, L1/L2/L5, MSM7; GPS, GLONASS, Galileo, BeiDou

---

## Free / Volunteer Alternatives

| Option | Notes |
|---|---|
| **Centipede** (crtk.net) | ~8–10 Denmark-coded nodes; sparse; better in Jutland |
| **RTK2go** (rtk2go.com) | ~17 Denmark-coded volunteer bases; no QoS guarantee |
| **Dataforsyningen GNSS** | **Free CORS RINEX archive** for post-processing only (not real-time); registration at dataforsyningen.dk |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **Dataforsyningen GNSS** — national CORS RINEX archive | https://dataforsyningen.dk/data/4717 | Free (account required) |

## Sources Consulted
- Klimadatastyrelsen GNSS positioning services: https://www.klimadatastyrelsen.dk/kortlaegning/geodaesi/gnss-positioneringstjenester
- Klimadatastyrelsen GNSS expansion announcement (Apr 2025): https://www.klimadatastyrelsen.dk/om-klimadatastyrelsen/nyheder/nyhedsarkiv/2025/apr/klimadatastyrelsen-udvider-nettet-af-gnss-maalestationer
- Geoteam / GPSnet.dk: https://www.geoteam.dk/produkter/gpsnetdk
- GPSnet short-term login: https://www.geoteam.dk/produkt/Referencenet/729/korttidslogin
- RTKconnect pricing: https://rtkconnect.dk/products/rtk-netvaerk
- HxGN SmartNet Denmark: https://hxgnsmartnet.com/da/services/smartnet-nrtk
- Dataforsyningen GNSS Denmark: https://dataforsyningen.dk/data/4717
- ArduSimple Denmark page: https://www.ardusimple.dk/rtk-correction-services-and-ntrip-casters-in-denmark/
- NTRIP-list.com Europe: https://ntrip-list.com/europe/
