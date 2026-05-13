# Jamaica [JM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry)

## Status: No confirmed public NTRIP caster — EarthScope scientific streams available; NLA VRS network status unknown

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | Unknown — NLA VRS/RTK network built historically but no public endpoint confirmed as of 2026-05-06 |
| **Scientific GNSS streams in JM territory** | Yes — EarthScope NOTA (former COCONet) CN10 (Morant Cay), CN11 (Pedro Cay / San Pedro Cay), CN12 (Kingston / UWI Mona campus); all on `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | EarthScope streams: **Yes** (noncommercial tier, individual account). NLA network: **Unclear** — no public documentation |
| **legal_residency_required** | EarthScope: **No**. NLA: **Unclear** |
| **last_confirmed_alive** | 2026-05-12 — EarthScope GNSS real-time portal HTTP 200 (NULA v. 2025-05-30); pipeline (`scripts/stations_by_country.py JAM`) shows EarthScope CN11_RTCM3P3 and CN12_RTCM3P3 currently active; CN10 not in current sourcetable snapshot. NLA portal nla.gov.jm: no NTRIP endpoint found |

---

## EarthScope NOTA — COCONet Stations in Jamaica Territory

| Station | Location | Notes | In live sourcetable 2026-05-12 |
|---|---|---|---|
| **CN10** | Morant Cay (~130 km SE of Kingston) | Remote cay; challenging corrosive marine environment; battery/comms upgrades performed | **No** — not present in current pipeline snapshot (likely temporarily down) |
| **CN11** | Pedro Cay / San Pedro Cay (~130 km S of Kingston) | Remote cay; fiberglass enclosure, 1200 Ah battery bank after upgrades | Yes (`CN11_RTCM3P3`, 17.02, −77.78) |
| **CN12** | Kingston — UWI Mona campus, Physics Dept roof | Most useful for positioning on Jamaica main island; operated in partnership with UWI Earthquake Unit | Yes (`CN12_RTCM3P3`, 18.00, −76.75) |

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

**Spatial Innovision Ltd.** (the Caribbean's Trimble business partner, est. 1998) was awarded a major contract by the **Ministry of Agriculture, Jamaica** (the Minister's award announcement is dated **12 March 2008** per Spatial Innovision's own news page) to install and commission a **National Virtual Reference System (VRS)** built on Trimble Navigation Limited hardware. The infrastructure was built on existing Cable & Wireless Frame Relay + MPLS lines plus GSM/GPRS networks from Cable & Wireless and Digicel, enabling cellphone-class end-user equipment to access nationwide RTK corrections.

As of 2026-05-12:
- No NTRIP host:port, caster address, or public access URL for the NLA VRS network was found in any source.
- The NLA website (nla.gov.jm) and the Jamaica Business Gateway (jamaicabusinessgateway.com) describe land administration services but contain no GNSS/NTRIP correction service listing.
- The Surveys and Mapping Division page (nla.gov.jm/content/surveys-and-mapping) makes no reference to a live RTK correction service.
- A separate 13-station scientific CORS network operated by the NLA in collaboration with UW-Madison (Prof. Chuck DeMets) for plate motion research exists; its data are post-processed, not streamed via NTRIP.

It is possible the NLA VRS network continues to operate internally for licensed surveyors under a credential-restricted endpoint not publicly advertised. No confirmation or denial was found.

---

## Most Recent Project Announcement

No recent (2022–2026) announcement of a new Jamaican national CORS or NTRIP expansion was found. The eLandJamaica portal (elandjamaica.nla.gov.jm) focuses on titling and mapping, not correction streaming. The most concrete Jamaican RTK infrastructure milestone remains the **2008 Spatial Innovision / Ministry of Agriculture Trimble VRS contract**.

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
- Spatial Innovision news — Ministry of Agriculture Jamaica National GPS Infrastructure contract (announcement dated 2008-03-12): https://www.spatialvision.com/ministry-of-agriculture-jamaica-signs-major-contract-with-spatial-innovision-to-deliver-the-national-gps-infrastructure/
- Jamaica country report (UN GGIM 2011): https://ggim.un.org/country-reports/documents/Jamaica-2011-country-report.pdf
- Pipeline EarthScope JAM stations: 2 (CN11, CN12) — 2026-05-12 via `scripts/stations_by_country.py JAM`
- UW-Madison / Jamaica GPS network: http://www.geology.wisc.edu/~chuck/Jamaica/
- RTK2go / Centipede sourcetables — no JM stations found
- NTRIP-list.com North America — no JM entry found
