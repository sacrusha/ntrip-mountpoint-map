# Denmark [DK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: NO free public NTRIP — three Klimadatastyrelsen-registered commercial providers (GPSnet.dk, HxGN SmartNet, RTKconnect.dk); state contributes 13–15 reference stations but operates no free public caster. Free RINEX archive via Dataforsyningen. Sparse volunteer alternatives: ~17 rtk2go DK bases + 8 Centipede DK nodes per project archives

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
| **last_confirmed_alive** | geoteam.dk portal HTTPS 200 confirmed 2026-05-12; remains on Klimadatastyrelsen approved-provider list |

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
| **last_confirmed_alive** | hxgnsmartnet.com/da accessible 2026-05-12 |

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
| **last_confirmed_alive** | rtkconnect.dk accessible 2026-05-12; service product page still shows the same 6,599 DKK / 19,797 DKK / 2,999 DKK tiering and 100% uptime claim; Klimadatastyrelsen approval timestamped 17 November 2023 |

- **Stations:** ~111 base stations including 13 from Klimadatastyrelsen; avg baseline 10 km
- **Precision:** Class A typical — <1 cm horizontal, <2 cm vertical
- **Format:** RTCM3, L1/L2/L5, MSM7; GPS, GLONASS, Galileo, BeiDou

---

## Free / Volunteer Alternatives

| Option | Notes |
|---|---|
| **Centipede** (crtk.net) | 8 Denmark-coded nodes per `scripts/stations_by_country.py DNK` (2026-05 snapshot): `AGBI`, `AGLU`, `AGRB`, `AGSA`, `AGSB`, `AGTH`, `HZAG`, `OVTA`. Heavily clustered in Jutland (55–57°N, 8–10°E); near-zero coverage in Sjælland east. The `AG*` prefix on most suggests a coordinated agricultural-farmer deployment. |
| **RTK2go** (rtk2go.com) | 17 Denmark-coded volunteer bases per `scripts/stations_by_country.py DNK` (2026-05 snapshot): `EC8700DNK`, `HEGRTK`, `Hvej12`, `KRAGELUND`, `Lovgaard`, `NGBRTKBASE`, `O-TorebyLL`, `Overtanget`, `PNRTK`, `SDS_RTK`, `SdrKildal`, `Sindal`, `Slagelse-PHK`, `TOLSHOEJ`, `Tystofte`, `Ugilt`, `roesdal`. Mostly Jutland; one node `Slagelse-PHK` (55.41°N/11.34°E) provides western Sjælland coverage. No QoS guarantee. |
| **Dataforsyningen GNSS** | **Free CORS RINEX archive** for post-processing only (not real-time); registration at dataforsyningen.dk |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **Dataforsyningen GNSS** — national CORS RINEX archive | https://dataforsyningen.dk/data/4717 | Free (account required) |

## Sources Consulted
- Klimadatastyrelsen GNSS positioning services: https://www.klimadatastyrelsen.dk/kortlaegning/geodaesi/gnss-positioneringstjenester (re-verified 2026-05-12 — 3 registered providers: Geoteam (Sep 2008), Leica Geosystems / HxGN (Sep 2008), RTKconnect ApS (2024); state monitors, does not operate)
- Klimadatastyrelsen GNSS expansion announcement (Apr 2025): https://www.klimadatastyrelsen.dk/om-klimadatastyrelsen/nyheder/nyhedsarkiv/2025/apr/klimadatastyrelsen-udvider-nettet-af-gnss-maalestationer
- Geoteam / GPSnet.dk: https://www.geoteam.dk/produkter/gpsnetdk (re-verified 2026-05-12 — no public pricing; subscription quote required; subscription categories cover surveying, agriculture, contractors, R&D, short-term, drones)
- GPSnet short-term login: https://www.geoteam.dk/produkt/Referencenet/729/korttidslogin
- RTKconnect pricing: https://rtkconnect.dk/products/rtk-netvaerk (re-verified 2026-05-12 — 6,599 DKK + VAT / 1-year; 19,797 DKK + VAT / 3-year incl. support contract valued at 7,164 DKK; volume 2,999 DKK/user/year for 11+ users; Klimadatastyrelsen approval 17 November 2023)
- HxGN SmartNet Denmark: https://hxgnsmartnet.com/da/services/smartnet-nrtk
- Dataforsyningen GNSS Denmark: https://dataforsyningen.dk/data/4717
- ArduSimple Denmark page: https://www.ardusimple.dk/rtk-correction-services-and-ntrip-casters-in-denmark/
- NTRIP-list.com Europe: https://ntrip-list.com/europe/
- Project pipeline `scripts/stations_by_country.py DNK` (2026-05 snapshot): 17 rtk2go bases + 8 Centipede nodes — see Free/Volunteer table above
