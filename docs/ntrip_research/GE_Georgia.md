# Georgia [GE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry)

## Status: ACTIVE — national NTRIP caster (GEO-CORS / NAPR); Spider Business Center registration required; endpoint not publicly advertised

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (registration required) |
| **Network name** | GEO-CORS |
| **Operator** | National Agency of Public Registry (NAPR), Ministry of Justice of Georgia — napr.gov.ge |
| **host:port — GEO-CORS** | Not publicly documented; delivered with SBC credentials post-registration; SBC portal at http://geocors.napr.gov.ge/SBC |
| **tariff — GEO-CORS** | Not publicly listed; governed by NAPR subscription terms; contact ghahubia@napr.gov.ge or +995 577 62 03 33 |
| **hobbyist_eligibility** | Registration is open to applicants; no explicit hobbyist restriction found; terms not publicly disclosed |
| **legal_residency_required** | No explicit overseas-user restriction found; NAPR is a Georgian state agency |
| **last_confirmed_alive** | `geocors.napr.gov.ge/SBC` Spider Business Center login page HTTP 200 confirmed 2026-05-12; curl probe of `geocors.napr.gov.ge:2101` — connection timed out 2026-05-12 21:00 UTC (consistent with closed/credential-gated caster) |
| **Volunteer fallback** | rtk2go: 1 GEO-coded base "geotimege" (~41.69, 44.86 — Tbilisi area) in `data/stations.json` 2026-05-12 |

## Most Recent Project Announcement

GEO-CORS was established when geodetic and cartographic functions transferred to NAPR in 2011. The network was documented at 16 stations in a 2012 UNOOSA presentation and has since expanded. A station at MKRN was added in 2019. The most recent confirmed station count found in research is 26 continuously operating stations. ArduSimple's Georgia page (checked 2026-05-06) explicitly states that Georgia "is not among" countries with a listed national RTK network — reflecting that GEO-CORS is not visible to external aggregators due to its closed-registration model.

- NAPR official site: https://www.napr.gov.ge/en/
- GEO-CORS SBC portal: http://geocors.napr.gov.ge/SBC
- UNOOSA 2012 NAPR presentation: https://www.unoosa.org/documents/pdf/psa/activities/2012/un-latvia/ppt/4-21.pdf
- EuroGeographics NAPR profile: https://eurogeographics.org/member/national-agency-of-public-registry/

## Context Notes

- **Network size:** 26 continuously operating GNSS reference stations covering Georgia's territory (excluding the occupied regions of Abkhazia and South Ossetia). The 2012 UNOOSA documentation cited 16 stations; the network has been expanded since.
- **Software platform:** Leica GNSS Spider / Spider Business Center (SBC). The SBC portal provides real-time positioning services, RINEX download from SpiderWeb, automatic computation, and user/subscription management.
- **Access procedure:** Users register through the Spider Business Center portal at http://geocors.napr.gov.ge/SBC. Post-approval, credentials include NTRIP host, port, and mountpoints. No anonymous or open-access endpoint.
- **Caster host probe:** WebFetch attempt on `geocors.napr.gov.ge:2101` returned ECONNREFUSED — confirming the caster is not exposed on that hostname/port without credentials or a different endpoint address.
- **Contact:** Giuli Hahubia (GEO-CORS contact); email ghahubia@napr.gov.ge; phone +995 577 62 03 33. These contact details were surfaced in search results referencing the NAPR geodesy division.
- **Scientific use:** GEO-CORS data is used for geophysical research, including contemporary crustal deformation studies in the Caucasus (referenced in EGU 2021 abstract literature).
- **Correction types offered:** Real-time RTK; RINEX delayed download via SBC; automated coordinate computation.
- **Volunteer fallback:** One Tbilisi-area volunteer base ("geotimege") confirmed on RTK2go via the local `data/stations.json` snapshot 2026-05-12 — single base, ~41.69/44.86 lat/lon, hobbyist-grade. No Centipede or EarthScope coverage.
- **Global commercial fallbacks:** No Georgia-country coverage confirmed on GEODNET, ONOCOY, or other commercial networks as of 2026-05-12.
- **Practical workaround:** Register directly at geocors.napr.gov.ge/SBC; or deploy a local base for single-base RTK; or use Galileo HAS / PPP for sub-decimetre accuracy without subscription.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GEO-CORS RINEX archive** — downloadable via Spider Business Center after registration | http://geocors.napr.gov.ge/SBC | Governed by NAPR subscription terms; pricing not public |
| **EarthScope / IGS archive** — Caucasus region IGS stations | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |

## Sources Consulted
- GEO-CORS Spider Business Center portal: http://geocors.napr.gov.ge/SBC
- GEO-CORS SBC service page: http://geocors.napr.gov.ge/SBC/spider-business-center
- Geo-CORS Facebook page: https://www.facebook.com/geocorsgeorgia/
- NAPR official site: https://www.napr.gov.ge/en/
- NAPR EuroGeographics profile: https://eurogeographics.org/member/national-agency-of-public-registry/
- UNOOSA 2012 NAPR presentation: https://www.unoosa.org/documents/pdf/psa/activities/2012/un-latvia/ppt/4-21.pdf
- DocPlayer NAPR paper mirror: https://docplayer.net/52055361-Ministry-of-justice-of-georgia-national-agency-of-public-registry-napr.html
- ArduSimple Georgia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-georgia/
- RTK2go monitor (monitor.use-snip.com) — 1 GEO-coded volunteer base ("geotimege", ~41.69/44.86) present in local sourcetable snapshot 2026-05-12; no other GE mountpoints
- NTRIP-list.com — no Georgia (country) entries found 2026-05-12
- ADS abstract on Caucasus crustal deformation: https://ui.adsabs.harvard.edu/abs/2021EGUGA..23.2675K/abstract
- curl probe of `geocors.napr.gov.ge:2101` — ECONNREFUSED 2026-05-06 09:14 UTC; re-probed 2026-05-12 — connection timed out (consistent with closed/credential-gated caster)
- curl probe of `http://geocors.napr.gov.ge/SBC` 2026-05-12 — HTTP 200 (login portal reachable)
- WebSearch for NAPR/GEO-CORS contact — ghahubia@napr.gov.ge and +995 577 62 03 33 confirmed 2026-05-06
