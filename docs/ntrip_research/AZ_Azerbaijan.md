# Azerbaijan [AZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-probe; 2026-05-15 deep research unchanged)

## Status: RESTRICTED — one national NTRIP caster (AzPOS); contract-gated, no anonymous endpoint; 1 free rtk2go volunteer base in greater Baku.

## AzPOS — Azerbaijan Positioning Observation System

| Field | Value |
|---|---|
| **landing_url** | https://www.emlak.gov.az/en/page/view/96 (operator-owned; "About AzPOS") |
| **access_url** | https://www.emlak.gov.az/en/page/view/96 — same operator page describes the service, eligibility ("legal entities and individuals"), and routes applicants to AzPOS staff for the bilateral agreement. Direct contact: azpos@emlak.gov.az, tel. (012) 562-82-70, mobile (050) 759-11-44 / (050) 229-25-23 (Baku, Yasamal district) |
| **host:port** | Provisional: `azpos.az:2101`. DNS still resolves to 185.161.226.29 (re-checked 2026-05-17, this sandbox); TCP 2101/80/443 all timed out from this sandbox. ArduSimple's country page confirms users receive NTRIP credentials only after applying via the operator portal — the actual delivered host/port is contract-dependent. No public sourcetable is published. |
| **tariff** | Not publicly listed. Service is governed by a bilateral agreement signed at the State Service on Property Issues office in Baku; AZN pricing has never been posted on emlak.gov.az or in operator press releases. No tier table to record. VAT status unknown — not declared on any public operator material. Date observed: 2026-05-15. |
| **num_stations** | ~45 physical CORS: 37 from the 2014 commissioning + 8 added in Karabakh in 2024 (Fuzuli, Jebrail, Zangilan, Kəlbəcər ×2, Ağdam, Şuşa, Laçın). |
| **vrs** | yes — backend documented in recent operator project material as Leica GNSS Spider (VRS-capable). |
| **hobbyist_eligibility** | no (effectively) — eligibility text accepts "legal entities and individuals", but the contract is bilateral, Azerbaijani-language, requires in-person/email engagement with the Baku office, and excludes anonymous or self-service signup. No hobbyist tariff exists. |
| **legal_residency_required** | ? — not stated explicitly. The contract-based access model and Azerbaijani-language process in practice favour residents or local agents; non-residents have no documented path. |
| **last_confirmed_alive** | 2026-05-15 — operator page https://www.emlak.gov.az/en/page/view/96 reachable via WebFetch (HTTP 200). Caster itself not probeable from this sandbox (TCP filtered); no public sourcetable to verify. Most recent public evidence of operational continuity: 2024 Karabakh expansion. |
| **datum_epoch** | Omitted — 2014 operator documentation states "WGS-84, UTM zones 38/39" but provides no epoch realization or official declaration document. Per tightened spec, no citable URL → omit. |

### Signals & Backend
- GPS + GLONASS (2014 baseline); Galileo + BeiDou indicated in post-2020 operator project documentation consistent with a Leica Spider upgrade.
- Control centre supports up to 100 parallel RTK users and 25 parallel web-service users (2014 spec, unchanged in public material).
- Station spacing 30–40 km; per-station usable RTK radius ~20 km; communication range up to 70 km (2014 spec).
- Services: real-time RTK + DGNSS + RINEX post-processing on request.

### Most Recent Project Announcements
- **2014** — AzPOS commissioned with 37 stations across mainland Azerbaijan (Karabakh excluded). UNOOSA workshop paper documented architecture and RTK service launch.
- **2024** — 8 new stations installed in the post-2020 reintegrated Karabakh region (Fuzuli, Jebrail, Zangilan, two in Kəlbəcər, Ağdam, Şuşa, Laçın) per ResearchGate "Post-war Restoration of the AzPOS Network in Karabakh" (2024). 24-hour test measurements at Fuzuli used Leica GS18.
- No public re-launch, public tariff, or public sourcetable announcement for 2025–2026. Service has been in continuous commercial operation since 2014.

## Free / Volunteer Alternatives in Azerbaijan

| Source | Mountpoint | Lat / Lon | Notes |
|---|---|---|---|
| rtk2go | `WHTCTY` | 40.38, 49.89 | Single volunteer base in greater Baku; visible in `data/stations.json` 2026-05-15 via `rtk2go.com:2101`. Free, no signup. Single-base RTK only — usable within ~20 km of Baku. |

No Centipede-RTK, EarthScope, GEODNET, ONOCOY, PointOne, or Swift Skylark stations have been observed inside Azerbaijan as of the 2026-05-15 snapshot. Nearest cross-border alternatives (>200 km from any Azerbaijani settlement) are not viable.

## Hobbyist Path
1. **In or near Baku (≤20 km)** — try rtk2go `WHTCTY` first (free, no signup, single-base RTK).
2. **Elsewhere in Azerbaijan** — no free RTK path. AzPOS access requires a bilateral Azerbaijani-language contract with the Baku office; effectively restricted to local entities.
3. **Self-host** — deploy a personal base/rover pair, or stream a base to rtk2go.com / Centipede / ONOCOY for community use.
4. **PPP / SSR fallback** — Galileo HAS (~20 cm horizontal, free, satellite-delivered, no internet needed) for sub-metre work where RTK is unavailable.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| AzPOS RINEX archive (via service agreement) | https://www.emlak.gov.az/en/page/view/96 | Governed by AzPOS agreement; not publicly priced |
| IGS BAKU station archive | https://network.igs.org/ | Free non-commercial |

## URL Probes (2026-05-15, this sandbox)

| URL | Result |
|---|---|
| https://www.emlak.gov.az/en/page/view/96 | 200 (WebFetch — content extracted) |
| https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-azerbaijan/ | 200 (WebFetch — content extracted) |
| https://www.unoosa.org/documents/pdf/psa/activities/2014/trieste-gnss/33.pdf | 200 (WebFetch — PDF binary, limited text extraction) |
| https://docplayer.net/48966253-Azerbaijan-positioning-observation-system-azpos-for-real-estate-cadastre-data-base.html | ECONNREFUSED (sandbox; target-user-reachable per WebSearch hit) |
| https://www.readkong.com/page/azerbaijan-positioning-observation-system-azpos-for-real-3736136 | 200 (WebFetch — extracted "WGS-84 in UTM 38/39") |
| https://www.researchgate.net/publication/389768010_Post-war_Restoration_of_the_AzPOS_Network_in_Karabakh | 403 Forbidden (sandbox; abstract visible via WebSearch) |
| https://www.geospatialworld.net/news/azerbaijan-positioning-observation-system-put-into-commercial-use/ | Not refetched 2026-05-15; cited from prior research |
| https://qrgs.emlak.gov.az/ | 404 (operator Karabakh GIS portal — separate cadastre product, not AzPOS) |
| `azpos.az:2101` TCP | Sandbox timeout (DNS OK → 185.161.226.29; ports filtered from this sandbox) |
| `rtk2go.com:2101` | Not probed live; mountpoint `WHTCTY` confirmed via `data/stations.json` 2026-05-15 snapshot |

## Sources Consulted
- AzPOS operator page (English): https://www.emlak.gov.az/en/page/view/96
- ArduSimple Azerbaijan country page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-azerbaijan/
- UNOOSA 2014 GNSS workshop AzPOS paper: https://www.unoosa.org/documents/pdf/psa/activities/2014/trieste-gnss/33.pdf
- ReadKong mirror of AzPOS cadastre paper (WGS-84 / UTM38–39 reference): https://www.readkong.com/page/azerbaijan-positioning-observation-system-azpos-for-real-3736136
- ResearchGate "Post-war Restoration of the AzPOS Network in Karabakh" (2024): https://www.researchgate.net/publication/389768010_Post-war_Restoration_of_the_AzPOS_Network_in_Karabakh
- Geospatial World AzPOS commercial-launch notice: https://www.geospatialworld.net/news/azerbaijan-positioning-observation-system-put-into-commercial-use/
- FIG 2020 "Digital Land Cadastre Information System in Azerbaijan": https://www.fig.net/resources/proceedings/fig_proceedings/fig2020/papers/ts04h/TS04H_jafarov_khanalibayli_10649.pdf
- Local: `data/stations.json` 2026-05-15 — rtk2go `WHTCTY` [AZE] (40.38, 49.89); no Centipede/EarthScope/GEODNET/ONOCOY stations in AZE.
- RTK2go monitor (target-user-reachable; sandbox TLS-altname error): http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
