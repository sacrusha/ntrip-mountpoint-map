# Tunisia [TN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: ACTIVE — national NTRIP caster (OTC); paid subscription; published tariff in TND

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid subscription) |
| **Network name** | OTC GNSS Network |
| **Operator** | Office de la Topographie et du Cadastre (OTC), Ministry of Equipment and Housing — otc.nat.tn |
| **host:port — OTC** | Not publicly listed; credentials issued by OTC commercial department upon subscription |
| **tariff — OTC** | 60 TND / 1 day · 480 TND / 15 days · 840 TND / 30 days · 2 400 TND / 3 months · 3 600 TND / 6 months · 4 800 TND / 9 months · 6 000 TND / 12 months (source: otc.nat.tn/geodesy/gnss/subscription, observed 2026-05-06) |
| **hobbyist_eligibility** | Marketed to professionals ("professionnels"); individual hobbyist eligibility not confirmed; document download required per tier |
| **legal_residency_required** | No explicit overseas restriction found; service is Tunisia-focused |
| **last_confirmed_alive** | otc.nat.tn/geodesy/gnss HTTP 200 confirmed 2026-05-06; otc.nat.tn/geodesy/gnss/subscription HTTP 200 with pricing confirmed 2026-05-06; curl probe of `otc.nat.tn:2101` — ECONNREFUSED 2026-05-06 09:14 UTC |

## Most Recent Project Announcement

OTC began building its permanent GNSS network in 2005 (first 3 stations: Tunis, Monastir, Sfax). By 2011 the full 23-station network covering Tunisia (excluding the Saharan south) was operational. The national geodetic datum NTT (Nouvelle Triangulation Tunisienne) was adopted in 2009, linked to ITRF2000 / WGS84. OTC has offered commercial GNSS subscriptions since 2011. No new expansion beyond 23 stations was found in 2023–2026 sources.

- OTC GNSS page: https://www.otc.nat.tn/geodesy/gnss
- OTC subscription page: https://www.otc.nat.tn/geodesy/gnss/subscription
- OTC geodetic networks page: https://www.otc.nat.tn/geodesy/networks
- OTC NTT reference page: https://www.otc.nat.tn/geodesy/ntt

## Context Notes

- **Network size:** 23 permanent GNSS stations distributed across Tunisia, excluding the Saharan south. Stations connect to the central Tunis server via GSM modem and UHF radio. Each station includes a meteorological sensor (temperature, pressure, humidity) and a tilt-meter.
- **Geodetic datum:** NTT (Nouvelle Triangulation Tunisienne), adopted 2009, tied to ITRF2000 / WGS84. The classical Carthage datum remains in legal use for historical cadastral documents.
- **Services:** Network RTK (NTRIP); RINEX download in delayed mode; automatic coordinate computation. No single-base RTK mode described — corrections are network-derived.
- **Tariff detail (confirmed from OTC subscription page 2026-05-06):**
  - 60 TND / 1 day
  - 480 TND / 15 days
  - 840 TND / 30 days
  - 2 400 TND / 3 months
  - 3 600 TND / 6 months
  - 4 800 TND / 9 months
  - 6 000 TND / 12 months
  - Each tier requires downloading a "document requis" (required document) via the subscription page. VAT status not stated on the public page.
- **Access procedure:** Create an account at otc.nat.tn → subscribe to a tier → download the required document for that tier → commercial department issues NTRIP credentials. Subscription page: https://www.otc.nat.tn/geodesy/gnss/subscription.
- **Contact — Commercial Department (Direction Commerciale):**
  - Telephone: +216 71 771 100 ext. 301 / +216 71 891 477 ext. 301
  - Fax: +216 71 770 448
  - Email: d.commerciale@otc.nat.tn
- **Caster host probe:** WebFetch attempt on `otc.nat.tn:2101` returned ECONNREFUSED — the caster endpoint is not exposed on that hostname/port publicly. Actual host delivered with credentials post-subscription.
- **Coverage gap:** The Saharan south (roughly south of Gafsa/Tozeur latitude) has no permanent stations; corrections may be unreliable or unavailable in those areas.
- **Global commercial fallbacks:** Centipede-RTK has no Tunisia base stations. GEODNET and ONOCOY coverage not confirmed for Tunisia.
- **Practical workaround:** Subscribe to OTC (lowest cost entry: 60 TND/day); deploy a local base for single-base RTK; or use Galileo HAS / PPP for sub-metre accuracy without subscription.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **OTC GNSS delayed-mode RINEX** — from 23 stations, via OTC account | https://www.otc.nat.tn/geodesy/gnss | Subscription fee (same tiers as RTK; contact OTC) |
| **IGS / EarthScope archive** — TUNIS (TNML) station for post-processing | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |

## Sources Consulted
- OTC GNSS page: https://www.otc.nat.tn/geodesy/gnss
- OTC subscription page (tariff confirmed): https://www.otc.nat.tn/geodesy/gnss/subscription
- OTC geodetic networks page: https://www.otc.nat.tn/geodesy/networks
- OTC NTT page: https://www.otc.nat.tn/geodesy/ntt
- OTC missions page: https://otc.nat.tn/mission
- ArduSimple Tunisia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-tunisia/
- NTRIP-list.com — no Tunisia entries found 2026-05-06
- RTK2go monitor (monitor.use-snip.com) — no Tunisia mountpoints visible 2026-05-06
- curl probe of `otc.nat.tn:2101` — ECONNREFUSED 2026-05-06 09:14 UTC
- WebFetch of otc.nat.tn/geodesy/gnss/subscription — HTTP 200, full tariff table extracted 2026-05-06
- WebFetch of otc.nat.tn/geodesy/gnss — HTTP 200, 23-station network and contact info confirmed 2026-05-06
