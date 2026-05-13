# Svalbard [SJ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13

## Status: LIMITED — 1 Centipede node at Ny-Ålesund (NYAWIPEV, AWIPEV research station); CPOS (Kartverket) covers mainland Norway only, does not extend to Svalbard; Kartverket geodetic observatory raw data purchasable but not a public RTK caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No public caster; one Centipede volunteer node only |
| **Volunteer (Centipede)** | 1 node — `NYAWIPEV` at 78.923°N, 11.923°E (Ny-Ålesund, Spitsbergen) — `caster.centipede.fr:2101`; operated by / associated with the AWIPEV Franco-German Arctic research station. Confirmed in local `data/stations.json` (Centipede tag SJM) 2026-05-13 |
| **Volunteer (rtk2go)** | 0 SJ bases confirmed (no SJ/SJM tag in rtk2go data) |
| **CPOS (Kartverket, Norway)** | Explicitly covers **mainland Norway only** — Kartverket "Guide to CPOS" states "The service covers mainland Norway", so Svalbard and Jan Mayen are excluded; `159.162.103.14:2101` |
| **Kartverket geodetic observatory** | Ny-Ålesund observatory operates permanent GNSS stations; raw RTCM 3.2 MSM5 data available to purchase by agreement; contact post@kartverket.no; **not a public NTRIP RTK caster** |
| **hobbyist_eligibility** | Centipede NYAWIPEV: yes — free, open; Kartverket raw data: commercial agreement only |
| **legal_residency_required** | Centipede: no; Kartverket data purchase: no explicit residency requirement, but requires commercial/research agreement |
| **last_confirmed_alive** | Centipede NYAWIPEV node present in local Centipede archive 2026-05-13 (`py scripts/stations_by_radius.py 78.22 15.65 200` returns NYAWIPEV at 113.3 km from Longyearbyen); Kartverket Ny-Ålesund observatory continuously operational |
| **tariff** | Centipede: free; Kartverket raw station data: price on application |

## CPOS Does Not Cover Svalbard

Kartverket's CPOS service is explicitly described as covering "mainland Norway" (fastlandet). In Norwegian geodetic context this means Norway without Svalbard and Jan Mayen. CPOS users in Longyearbyen or elsewhere on Svalbard cannot receive VRS corrections from the CPOS caster at `159.162.103.14:2101` because no Svalbard reference stations feed into the CPOS network solution.

ETPOS (Kartverket post-processing, included with CPOS subscription) similarly uses mainland stations; NOK 8,000 + VAT/yr if purchased standalone.

## Kartverket Geodetic Observatory at Ny-Ålesund

The Norwegian Mapping Authority operates a geodetic earth observatory at Ny-Ålesund, Svalbard — the northernmost of its kind globally. The Brandal facility (opened 2018) includes a 20 m VLBI radio telescope plus permanent GNSS receivers. Kartverket provides the GNSS station data in RTCM 3.2 MSM5 format to third parties who purchase it under data agreements, for use in their own positioning services. This is not a public NTRIP caster; it is a paid raw-data feed for operators building services.

The Satref control center (`satref.geodesi.no`) monitors Kartverket's positioning infrastructure including Svalbard stations.

## NYAWIPEV Centipede Node

The single Centipede node `NYAWIPEV` at approximately 78.9°N in Ny-Ålesund is the only free public RTK correction option for Svalbard. Its practical RTK coverage radius is ~20–40 km — sufficient for operations in the Kongsfjorden area (Ny-Ålesund, Kings Bay). Longyearbyen (~120 km SE) is outside reliable RTK range from this single node.

The AWIPEV Arctic Research Station is jointly operated by the Alfred Wegener Institute (AWI, Germany) and the Institut polaire français Paul-Émile Victor (IPEV, France). The Centipede node at this station provides real-time GNSS corrections in the Ny-Ålesund research village.

## Most Recent Project Announcement

No announced Kartverket plan to extend CPOS or DPOS to Svalbard as of 2026-05-13. Kartverket's "Guide to CPOS" still states the service covers "mainland Norway" without further extension. Kartverket's 2023–2024 Svalbard white paper analysis (High North News) addresses sovereignty and infrastructure but does not reference a public RTK correction service expansion.

No additional Centipede or rtk2go nodes for Svalbard have been announced.

## Context Notes

- **Practical RTK for Longyearbyen**: No free public RTK option. Hobbyists and researchers in Longyearbyen must deploy their own local base station or rely on PPP (Galileo HAS, ~40 cm) or commercial global correction services.
- **EUREF/IGS stations**: The Ny-Ålesund area hosts several IGS/EPN reference stations (e.g., `NYA1`, `NYAL`). These stream raw GNSS data via the EarthScope NTRIP caster (`ntrip.earthscope.org:2101`) and the BKG/ROB euref-ip broadcasters — free with registration. These are raw observation streams, not network RTK VRS corrections; they are usable as a single-base NTRIP stream for RTK within ~30–40 km.
- **EarthScope NTRIP**: `ntrip.earthscope.org:2101` carries real-time streams from IGS global network stations including Svalbard. Free with EarthScope account (no residency restriction). Single-base coverage only.
- **GEODNET**: No confirmed GEODNET node in Svalbard. Unlikely given the infrastructure constraints of the archipelago.
- **Hobbyist RTK summary**: For Ny-Ålesund area — Centipede NYAWIPEV (free) or EarthScope/euref-ip IGS stream (free, single-base). For Longyearbyen and the rest of Svalbard — no free public RTK; deploy own base or use PPP.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / GAGE** (IGS stations NYA1, NYAL at Ny-Ålesund) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **Kartverket ETPOS** (mainland-only, NOT Svalbard) | https://www.kartverket.no/en/on-land/posisjon/guide-to-etpos | NOK 8,000 + VAT/yr (or free with CPOS subscription) |

## Sources Consulted
- Kartverket Guide to CPOS: https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos
- Kartverket User Guide Positioning Services: https://www.kartverket.no/en/on-land/posisjon/user-guide-positioning-services
- Kartverket Geodetic Earth Observatory: https://www.kartverket.no/en/about-kartverket/geodetic-earth-observatory
- Kartverket Observatory information: https://www.kartverket.no/en/about-kartverket/geodetic-earth-observatory/information-about-the-observatory
- Kartverket satellite and positioning data: https://proxy.kartverket.no/en/api-and-data/satellite-and-positiong-data
- Satref control center: https://satref.geodesi.no/
- AWIPEV Arctic Research Station: https://www.awipev.eu/ · https://institut-polaire.fr/en/arctic/awipev-station/
- Centipede-RTK network: https://www.centipede-rtk.org/ · https://map.centipede-rtk.org/
- EarthScope GNSS realtime: https://www.earthscope.org/data/gnss-realtime/
- High North News Svalbard White Paper analysis: https://www.highnorthnews.com/en/sovereignty-governance-and-infrastructure-analysis-svalbards-white-paper-2023-2024
