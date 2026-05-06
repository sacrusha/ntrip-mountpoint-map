# Oman [OM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — OmanCORSnet active (47 stations, Spider Business Center portal); access gated behind registration; hobbyist eligibility and tariff unknown

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — OmanCORSnet (confirmed live portal) |
| **Network name** | OmanCORSnet |
| **Operator** | NSGIA — National Survey and Geospatial Information Authority (successor to NSA, National Survey Authority, under Ministry of Defence) |
| **host:port — portal** | `omancorsnet.gov.om` (Spider Business Center login: `omancorsnet.gov.om/SBC/Account/Index`) |
| **host:port — NTRIP caster** | Not publicly disclosed; issued post-registration |
| **VRS** | Likely yes — 47-station network uses Leica GNSS Spider software (Spider Business Center), which supports VRS |
| **tariff** | Not publicly listed; subscription management via Spider Business Center |
| **hobbyist_eligibility** | Unclear — no hobbyist or individual tier documented; ArduSimple Oman page indicates registration required but does not specify licensed-professional-only restriction |
| **legal_residency_required** | Unclear — no explicit restriction found; non-resident eligibility unconfirmed |
| **last_confirmed_alive** | `omancorsnet.gov.om/SBC/Account/Index` — Spider Business Center login page confirmed reachable (search-indexed) as of 2026-05-06 |

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

The Spider Business Center (SBC) at `omancorsnet.gov.om/SBC/Account/Index` is the login / subscription management frontend. This is consistent with a paid or restricted service requiring prior registration. NTRIP caster host:port details are not published and are presumably delivered to registered users post-approval.

ArduSimple's Oman page states that to access real-time services, registration on the website or email contact is required to receive NTRIP credentials — consistent with a gated access model.

**No evidence of an open hobbyist tier** was found. The network is aimed at professional surveying and geodetic applications, but no explicit "licensed surveyor only" language was retrieved from public pages. Fees, if any, are managed through the SBC subscription system.

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

- NTRIP caster host:port not publicly disclosed
- Tariff / fee schedule not publicly documented
- Hobbyist eligibility: unclear (not explicitly denied but no individual tier found)
- rtk2go: zero OM mountpoints
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
