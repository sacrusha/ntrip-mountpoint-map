# Azerbaijan [AZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: ACTIVE — national NTRIP caster (AzPOS); credentials issued post-registration; endpoint not publicly advertised

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (registration required) |
| **Network name** | AzPOS (Azerbaijan Positioning Observation System) |
| **Operator** | State Service on Property Issues under the Ministry of Economy — emlak.gov.az |
| **host:port — AzPOS** | Not publicly documented; host and port issued with credentials after service agreement is signed |
| **tariff — AzPOS** | Not publicly listed; governed by bilateral service agreement; contact AzPOS staff at azpos@emlak.gov.az |
| **hobbyist_eligibility** | Both legal entities and individuals may apply; no explicit hobbyist restriction found; formal agreement required |
| **legal_residency_required** | No explicit residency restriction stated; agreement governed by Azerbaijani law |
| **last_confirmed_alive** | emlak.gov.az/en/page/view/96 HTTP 200 confirmed 2026-05-06; curl probe of `azpos.az:2101` — ECONNREFUSED 2026-05-06 09:14 UTC (endpoint not publicly exposed on that host/port) |

## Most Recent Project Announcement

AzPOS was commissioned by the State Committee on Property Issues (subsequently absorbed into the Ministry of Economy). A 2014 UNOOSA workshop paper documented the network's architecture, control-centre software, and RTK service capability. No formal re-launch or expansion announcement was found for 2023–2026; the service has been in continuous commercial operation since at least 2014.

- AzPOS about page: https://www.emlak.gov.az/en/page/view/96
- UNOOSA 2014 presentation: https://www.unoosa.org/documents/pdf/psa/activities/2014/trieste-gnss/33.pdf
- Geospatial World commercial-launch notice: https://www.geospatialworld.net/news/azerbaijan-positioning-observation-system-put-into-commercial-use/

## Context Notes

- **Network size:** 37 continuously operating GNSS reference stations distributed across Azerbaijan (excluding mountainous zones with 3 mountain stations included). Stations spaced 30–40 km apart; usable RTK radius ~20 km per station; communication range up to 70 km.
- **Concurrent user capacity:** Control centre supports up to 100 parallel RTK users simultaneously (per UNOOSA 2014 documentation).
- **Signals tracked:** GPS (American) and GLONASS (Russian); 24/7 continuous operation.
- **Services offered:** RTK (real-time kinematics) and DGNSS; post-processing via RINEX archive on request.
- **Software platform:** Not publicly disclosed in recent sources; 2014 documentation referenced a proprietary control-centre system.
- **Operator identity:** The operator entity referenced in some documents is the "Kadastr və Yer Quruluşu Layihə Tədqiqat Mərkəz" (Design Research Centre for Cadastre & Land Management), which operates AzPOS under the State Service on Property Issues / Ministry of Economy umbrella.
- **Access procedure:** Applicants submit a request at emlak.gov.az; staff provide a service agreement for review; credentials (NTRIP host, port, mountpoints, username, password) are issued after agreement is signed. No anonymous or open-access endpoint exists.
- **Caster host probe:** WebFetch attempt on `azpos.az:2101` returned ECONNREFUSED — confirming the caster endpoint is not exposed on that hostname/port publicly. The actual hostname is issued privately post-registration.
- **Global commercial fallbacks:** No Azerbaijan-specific coverage confirmed on GEODNET, ONOCOY, Centipede-RTK, PointOne, or RTK2go as of 2026-05-06.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **AzPOS RINEX archive** — available via emlak.gov.az upon registration | https://www.emlak.gov.az/en/page/view/96 | Governed by service agreement; pricing not public |
| **IGS / EarthScope archive** — BAKU IGS station for post-processing | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |

## Sources Consulted
- AzPOS about page: https://www.emlak.gov.az/en/page/view/96
- UNOOSA 2014 GNSS workshop paper: https://www.unoosa.org/documents/pdf/psa/activities/2014/trieste-gnss/33.pdf
- DocPlayer mirror of AzPOS system paper: https://docplayer.net/48966253-Azerbaijan-positioning-observation-system-azpos-for-real-estate-cadastre-data-base.html
- Geospatial World AzPOS commercial-launch notice: https://www.geospatialworld.net/news/azerbaijan-positioning-observation-system-put-into-commercial-use/
- ArduSimple Azerbaijan page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-azerbaijan/
- RTK2go monitor (monitor.use-snip.com) — no Azerbaijan mountpoints visible 2026-05-06
- NTRIP-list.com — no Azerbaijan entries found 2026-05-06
- curl probe of `azpos.az:2101` — ECONNREFUSED 2026-05-06 09:14 UTC
- WebFetch of emlak.gov.az/en/page/view/96 — HTTP 200, content extracted 2026-05-06
