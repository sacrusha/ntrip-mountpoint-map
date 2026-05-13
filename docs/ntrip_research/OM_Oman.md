# Oman [OM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh; prior pass 2026-05-06)

## Status: YES — OmanCORSnet active (~47 physical stations, expanding to 60+; Leica GNSS Spider VRS caster live on port 2101); hobbyist eligibility unconfirmed, tariff not published

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — OmanCORSnet (caster live on `omancorsnet.gov.om:2101`) |
| **Network name** | OmanCORSnet |
| **Operator** | NSGIA — National Survey and Geospatial Information Authority (successor to NSA, National Survey Authority, under Ministry of Defence) |
| **host:port — portal (Spider Business Center)** | `https://omancorsnet.gov.om/SBC/Account/Index` |
| **host:port — NTRIP caster** | `omancorsnet.gov.om:2101` — SOURCETABLE 200 OK on 2026-05-12 (curl). Server header: `GNSS Spider 7.11.1.109/1.0`. Sourcetable lists 8 mountpoints: `Nearest`, `MAX`, `VRS`, `UTM-40-Auto-Geoid`, `UTM-39-Auto-Geoid`, `MAX-Geoid-39`, `MAX-Geoid-40`, `ONGD23`. RTCM 3, GPS+GLO. Physical CORS are not exposed as individual streams. Authentication required to actually stream data — sourcetable is open. |
| **VRS** | Yes — confirmed; sourcetable advertises `VRS`, `MAX` (Master-Auxiliary), and `Nearest` network-RTK mountpoints. Leica GNSS Spider platform. |
| **Datum** | `ONGD23` mountpoint suggests an updated Oman National Geodetic Datum (ONGD23) is in use alongside ONGD17 / UTM 39N / UTM 40N projections. |
| **num_stations** | ~47 physical CORS (per NSGIA), with stated plan to expand beyond 60 |
| **tariff** | Not publicly listed; subscription management via Spider Business Center |
| **hobbyist_eligibility** | Unclear — no hobbyist or individual tier documented; ArduSimple Oman page indicates registration required but does not specify licensed-professional-only restriction |
| **legal_residency_required** | Unclear — no explicit restriction found; non-resident eligibility unconfirmed |
| **last_confirmed_alive** | Caster `omancorsnet.gov.om:2101` SOURCETABLE 200 OK confirmed 2026-05-12 (curl HTTP/0.9; ENDSOURCETABLE returned) |

---

## Service Details

### OmanCORSnet — Network Overview

**Established:** 2016 (47 CORS sites installed by National Survey Authority).
**Operator brand evolution:** NSA (National Survey Authority) → NSGIA (National Survey and Geospatial Information Authority); geoportal at `nsaomangeoportal.gov.om`.
**Stations:** 47 continuously operating GNSS reference stations distributed across Oman (~309,500 km²).
**Datum:** ONGD17 — Oman National Geodetic Datum 2017 (ITRF2014, epoch 2017.0). ONGD17 replaced the earlier GD-Oman reference.
**Signals:** Multi-constellation GNSS (exact constellation support not confirmed from public docs).
**Software platform:** Leica GNSS Spider (Spider Business Center) — the standard Leica CORS management / subscription platform. This is the same platform used by other commercial/government networks (e.g., HxGN SmartNet affiliates).
**Geoid:** OMANGEOID (national geoid model) — part of the Oman National Spatial Reference System alongside OmanCORSnet and ONGD17.

### Portal and Access

The Spider Business Center (SBC) at `https://omancorsnet.gov.om/SBC/Account/Index` is the login / subscription management frontend. The NTRIP caster runs on the same host on port 2101 and serves an open sourcetable (confirmed 2026-05-12). Streaming any mountpoint requires NTRIP credentials issued through the SBC after registration / approval.

ArduSimple's Oman page states that to access real-time services, registration on the website or email contact is required to receive NTRIP credentials — consistent with a gated access model.

**No evidence of an open hobbyist tier** was found. The network is aimed at professional surveying and geodetic applications, but no explicit "licensed surveyor only" language was retrieved from public pages. Fees, if any, are managed through the SBC subscription system.

### Mountpoint Breakdown (sourcetable, 2026-05-12)

| Mountpoint | Format | Constellations | Solution | Notes |
|---|---|---|---|---|
| `Nearest` | RTCM 3 | GPS+GLO | Single-base (nearest CORS to rover) | nmea=1, solution=0 |
| `MAX` | RTCM 3 | GPS+GLO | Network RTK (Master-Auxiliary / iMAX) | nmea=1, solution=1 |
| `VRS` | RTCM 3 | GPS+GLO | Virtual Reference Station | nmea=1, solution=1 |
| `UTM-40-Auto-Geoid` | RTCM 3 | GPS+GLO | UTM zone 40N projection, geoid model applied | nmea=1, solution=1 |
| `UTM-39-Auto-Geoid` | RTCM 3 | GPS+GLO | UTM zone 39N projection, geoid model applied | nmea=1, solution=1 |
| `MAX-Geoid-39` | RTCM 3 | GPS+GLO | Network RTK + geoid (UTM 39N) | nmea=1, solution=1 |
| `MAX-Geoid-40` | RTCM 3 | GPS+GLO | Network RTK + geoid (UTM 40N) | nmea=1, solution=1 |
| `ONGD23` | RTCM 3 | GPS+GLO | Native ONGD23 datum stream | nmea=1, solution=1 |

Multi-constellation (Galileo/BeiDou) mountpoints are not exposed publicly — current sourcetable shows GPS+GLONASS only.

### IGS Station

An IGS station at Muscat (MUSK) broadcasts raw GNSS observations via EarthScope/IGS-IP streams. This is a raw observation stream, not an RTK corrections stream, and is not a substitute for an NTRIP RTK caster. It is useful for post-processing.

---

## Commercial Alternatives

No independent commercial NTRIP provider with confirmed Oman coverage has been identified. Global networks (GEODNET, PointOne, HxGN SmartNet) do not list confirmed Oman coverage from public documentation.

Global free fallback: **Galileo HAS** (~40 cm accuracy, no connectivity required, globally available including Oman).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **OmanCORSnet / NSGIA** — RINEX data download (via same Spider Business Center portal, if access granted) | https://omancorsnet.gov.om/ | Registration required; fee unknown |
| **IGS / EarthScope** — Muscat IGS station (MUSK) raw GNSS observations | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **NSGIA Geoportal** | https://www.nsaomangeoportal.gov.om/en/oman-corsnet | Information page; link to OmanCORSnet |

---

## Negative Findings

- NTRIP caster host:port is `omancorsnet.gov.om:2101` (now confirmed by direct probe — earlier assumption that it was undisclosed was wrong); however **credentials and per-station mountpoints are not public**
- Tariff / fee schedule not publicly documented
- Hobbyist eligibility: unclear (not explicitly denied but no individual tier found)
- rtk2go: zero OM mountpoints (no OMN-tagged stations in current local index)
- Centipede: zero OM nodes
- GEODNET, PointOne, HxGN SmartNet: no Oman coverage confirmed in public documentation
- NAGSN acronym used in project's country-survey.md does not appear in current NSGIA documentation; current official name is OmanCORSnet

---

## Sources Consulted
- Investigation notes next.txt entry 85 (project internal)
- country-survey.md entry `OM — Oman` (project internal, date_added 2026-04-28)
- NSGIA OmanCORSnet page: https://www.nsaomangeoportal.gov.om/en/oman-corsnet
- NSGIA About page: https://www.nsaomangeoportal.gov.om/en/about-nsa
- NSGIA ONGD17 page: https://www.nsaomangeoportal.gov.om/en/ongd17
- OmanCORSnet Spider Business Center login: https://www.omancorsnet.gov.om/SBC/Account/Index?returnUrl=/SBC
- Oman Geospatial Forum PDF — "Latest Geospatial Infrastructure in Oman": http://omangeospatialforum.org/presentation/latest-geospatial-infrastructure-in-Oman-national-development-benefits.pdf
- GIM International — "Oman Launches New Geodetic Datum": https://www.gim-international.com/content/article/oman-launches-new-geodetic-datum
- Geospatial World — "Oman Moves Ahead with New Geodetic Datum": https://geospatialworld.net/article/oman-moves-ahead-with-new-geodetic-datum/
- FIG 2024 — "A New Reference Frame for Oman": https://www.fig.net/resources/proceedings/fig_proceedings/fig2024/papers/ts08f/TS08F_al_balushi_abolghasem_et_al_12396.pdf
- ArduSimple Oman NTRIP page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-oman/
- EarthScope IGS data (Muscat station): https://www.earthscope.org/data/gnss-data/
- curl probe of `omancorsnet.gov.om:2101` — SOURCETABLE 200 OK confirmed 2026-05-12 (8 mountpoints listed; GNSS Spider 7.11 server)
