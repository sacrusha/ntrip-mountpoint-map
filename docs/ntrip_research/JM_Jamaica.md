# Jamaica [JM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: No confirmed public NTRIP caster — EarthScope scientific streams available; NLA VRS network status unknown

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | Unknown — NLA VRS/RTK network built historically but no public endpoint confirmed as of 2026-05-06 |
| **Scientific GNSS streams in JM territory** | Yes — EarthScope NOTA (former COCONet) CN10 (Morant Cay), CN11 (Pedro Cay / San Pedro Cay), CN12 (Kingston / UWI Mona campus); all on `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | EarthScope streams: **Yes** (noncommercial tier, individual account). NLA network: **Unclear** — no public documentation |
| **legal_residency_required** | EarthScope: **No**. NLA: **Unclear** |
| **last_confirmed_alive** | 2026-05-06 (EarthScope portal reachable; NULA dated v. 2025-05-30). NLA portal nla.gov.jm: HTTP 200 but no NTRIP endpoint found |

---

## EarthScope NOTA — COCONet Stations in Jamaica Territory

| Station | Location | Notes |
|---|---|---|
| **CN10** | Morant Cay (~130 km SE of Kingston) | Remote cay; challenging corrosive marine environment; battery/comms upgrades performed |
| **CN11** | Pedro Cay / San Pedro Cay (~130 km S of Kingston) | Remote cay; fiberglass enclosure, 1200 Ah battery bank after upgrades |
| **CN12** | Kingston — UWI Mona campus, Physics Dept roof | Most useful for positioning on Jamaica main island; operated in partnership with UWI Earthquake Unit |

CN10 and CN11 are isolated islets 80+ miles offshore and are outside practical single-base RTK range from any populated area on the main island. **CN12 in Kingston is the only station relevant to hobbyist RTK use on Jamaica.**

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT VRS/Network-RTK) |
| **Tariff — noncommercial** | **Free (USD $0.00)** — account + annual NULA acceptance required. Date observed: 2026-05-06. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **Tariff — commercial** | **USD $1,000 per seat per year** (EarthScope 501(c)(3); no VAT). Date observed: 2026-05-06. Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |

**Note on legacy platform**: Old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

---

## National Land Agency (NLA) VRS Network

**Spatial Innovision Ltd.** (a UK GIS firm) provided professional services to Jamaica's Ministry of Land & Environment and the National Land Agency to establish a national real-time GPS infrastructure of Virtual Reference Stations for RTK corrections — described at the time as "a first for the Caribbean and the developing world" and integrating GPRS, GPS, and frame relay. The project is documented on Spatial Innovision's projects page but carries no date; internal evidence suggests delivery in the mid-2000s.

As of 2026-05-06:
- No NTRIP host:port, caster address, or public access URL for the NLA VRS network was found in any source.
- The NLA website (nla.gov.jm) and the Jamaica Business Gateway (jamaicabusinessgateway.com) describe land administration services but contain no GNSS/NTRIP correction service listing.
- The Surveys and Mapping Division page (nla.gov.jm/content/surveys-and-mapping) makes no reference to a live RTK correction service.
- A separate 13-station scientific CORS network operated by the NLA in collaboration with UW-Madison (Prof. Chuck DeMets) for plate motion research exists; its data are post-processed, not streamed via NTRIP.

It is possible the NLA VRS network continues to operate internally for licensed surveyors under a credential-restricted endpoint not publicly advertised. No confirmation or denial was found.

---

## Most Recent Project Announcement

No recent (2022–2026) announcement of a new Jamaican national CORS or NTRIP expansion was found. The eLandJamaica portal (elandjamaica.nla.gov.jm) focuses on titling and mapping, not correction streaming.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive** — COCONet CN10, CN11, CN12 RINEX | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |
| **NLA 13-station scientific CORS** — processed via UW-Madison GIPSY; data page | http://www.geology.wisc.edu/~chuck/Jamaica/ | Free (research/scientific use) |

## Sources Consulted
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/
- EarthScope commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- UNAVCO COCONet Jamaica upgrade article: https://www.unavco.org/news/unavco-upgrades-coconet-cgps-sites-in-jamaica/
- COCONet site info: https://coconet.unavco.org/site-info/site-info.html
- CN12 station overview: https://www.unavco.org/instrumentation/networks/status/coconet/overview/CN12
- UWI Earthquake Unit: https://www.mona.uwi.edu/earthquake/
- NLA website: https://www.nla.gov.jm/content/surveys-and-mapping
- Spatial Innovision Jamaica project: https://www.spatialvision.com/projects/
- UW-Madison / Jamaica GPS network: http://www.geology.wisc.edu/~chuck/Jamaica/
- RTK2go / Centipede sourcetables — no JM stations found
- NTRIP-list.com North America — no JM entry found
