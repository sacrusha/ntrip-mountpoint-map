# Agent intended Write
- batch: batch5
- target: D:\Projects\ntrip-mountpoint-map\docs\ntrip_research\SG_Singapore.md
- transcript line: 202

## CONTENT (full file)

```markdown
# Singapore [SG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07

## Status: YES — single national NTRIP RTK caster operating (SiReNT, Singapore Land Authority); paid subscription, SingPass/CorpPass-gated

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | SiReNT — Singapore Satellite Positioning Reference Network |
| **Operator** | Survey Services, Singapore Land Authority (SLA), a statutory board under the Ministry of Law |
| **Mandate basis** | National geospatial reference framework, established 2006; Trimble Alloy receivers refresh 2022 |
| **Stations** | 5 reference stations (SNTU @ Nanyang Technological University, SKEP @ Keppel Club, SLOY @ Loyang, SSEK @ Senoko, SNYP @ Nanyang Polytechnic). Earlier reporting referencing "10 stations" appears to mix in densification/structural-monitoring sites; the canonical service network on Wikipedia and SLA documentation is 5 |
| **host:port** | `203.127.20.71:2101` (commonly cited; SLA's Services page does not republish the IP openly — it is delivered to subscribers along with the Subscription ID and token) |
| **VRS** | Yes — SiReNT offers both Single-Base RTK (SBR) and Network RTK (VRS) via NTRIP; also Single-Base DGNSS and Network DGNSS for sub-metre code corrections |
| **Formats** | RTCM 2.3 / 3.1 / 3.2 and CMR (per SLA Services page); chosen at the rover according to firmware support |
| **tariff — RTK or DGNSS, 1st–9th account** | S$107.00 / account / month — GST-inclusive (S$~$80 USD at 2026-05 rate ≈ US$80/mo, ~US$960/yr) |
| **tariff — RTK or DGNSS, 10th–50th account** | S$64.20 / account / month, GST-inclusive |
| **tariff — RTK or DGNSS, 51st+ account** | S$32.10 / account / month, GST-inclusive (volume tier, presumably for fleet/enterprise) |
| **VAT/GST status** | "Cost inclusive of GST" stated explicitly on app.sla.gov.sg/sirent/Page/Services. Singapore GST 9% (since 1 Jan 2024). |
| **Trial** | 3-day trial available, one per calendar month per subscriber, accessible after CorpPass or SingPass login |
| **hobbyist_eligibility** | No (in practice). Sign-up requires SingPass (Singapore citizen / PR / FIN-holder) for individual subscribers, or CorpPass for businesses ("If you are registering for an account on behalf of your company, you must use the company's CorpPass account."). Account creation is gated to Singapore digital identity. There is no anonymous, OAuth-Google, or e-mail-only path |
| **legal_residency_required** | Yes (de facto). NRIC requires citizenship or PR; FIN requires a long-term pass tied to study/work/residence; CorpPass requires a Singapore-registered legal entity (UEN). Foreign hobbyists outside Singapore have no native registration path |
| **last_confirmed_alive** | 2026-05-07 (app.sla.gov.sg/sirent/Page/Services and app.sla.gov.sg/sirent/Page/FAQ both reachable; Tier-pricing table loaded; FAQ last updated 2020-06-08 but service operational; Trimble customer-story page describes 2022 Alloy hardware refresh) |

## Mountpoints (overview, names not republished by SLA)

SLA publishes service modes — Single-Base RTK (SBR), Network RTK (VRS), Single-Base DGNSS, Network DGNSS — but does not expose the sourcetable on a public URL. The 5-station physical layout (SNTU, SKEP, SLOY, SSEK, SNYP) is the canonical reference; per-mountpoint names are delivered alongside the Subscription ID after registration.

## Context Notes

- **Mandate**: SLA established SiReNT in 2006; the original 5-corner geometry (4 perimeter + 1 centre at NYP) covers the 728 km² island with 10–15 km baselines, well within VRS-RTK ideal range. In 2010 SiReNT added telematics and structural-monitoring solutions to the catalogue. In 2022 Trimble Alloy receivers were rolled out across the network, advertising 3 cm absolute Smart-Nation-grade accuracy.
- **Identity-system gate**: SingPass and CorpPass are not generic e-government logins — they are tied to Singapore residency / legal entity. A non-resident foreign hobbyist who does not hold a FIN cannot create a SingPass account, and cannot obtain a CorpPass without registering a Singapore business (typically requiring a local registered address and at least one Singapore-resident director or nominee). There is no alternative international login. This makes SiReNT effectively closed to foreign hobbyists.
- **GST 9 %**: All tier prices on the SLA Services page are stated as GST-inclusive. Net of GST: S$98.17 / S$58.90 / S$29.45 per month respectively (as of 2024-01-01 GST rate change to 9 %).
- **Volunteer alternatives**: Zero rtk2go bases in SG; zero Centipede nodes. The city-state has no free RTK fallback. Visiting hobbyists using Singapore mobile networks could in principle subscribe to short-range commercial services like u-blox PointPerfect (SSR via PPP-RTK, not classical NTRIP RTK), but no free single-frequency or RTK option exists.
- **Trial caveat**: The 3-day SiReNT trial requires the same SingPass/CorpPass login as a paying subscription; it does not bypass the Singapore-identity gate.
- **No volume-discount path for individuals**: Tier-2 (S$64.20) and Tier-3 (S$32.10) only apply to the 10th–50th and 51st+ accounts under a single CorpPass — i.e., a fleet operator. A single hobbyist can never reach Tier 2.

## Practical workaround for non-resident hobbyists

There is no practical free or affordable hobbyist path for non-Singapore-residents. Options:
- A Singapore-resident colleague registers a SingPass account and shares NTRIP credentials (terms-of-service violation; not recommended).
- Deploy a personal base station within the city's permitted bands (a Wi-Fi base on a residence rooftop is unregulated for receive-only; an NTRIP server can be hosted on rtk2go but no SG community has appeared in the public sourcetable).
- Use satellite-based PPP/PPP-RTK (Trimble RTX, u-blox PointPerfect, NavIC at L5 once supported) — out of scope for this guide but the only realistic non-NTRIP path.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **SiReNT Post Processing On-Demand** — RINEX file generation from the 5 reference stations | https://app.sla.gov.sg/sirent | Subscription required (same SingPass/CorpPass gate) |
| **SiReNT Post Processing Archive** — historical RINEX archive | https://app.sla.gov.sg/sirent | Subscription required |
| **IGS — NTUS (Nanyang Technological University)** — long-running IGS reference station, daily 30 s RINEX | https://network.igs.org/NTUS00SGP | Free (CDDIS / IGS data centre account) |

## Sources Consulted
- SiReNT main portal: https://app.sla.gov.sg/sirent (observed 2026-05-07)
- SiReNT Services / pricing page: https://app.sla.gov.sg/sirent/Page/Services — tariff tiers, GST-inclusive note, formats list, trial mention (observed 2026-05-07)
- SiReNT FAQ: https://app.sla.gov.sg/sirent/Page/FAQ (last updated 2020-06-08)
- SiReNT Our Services description: https://app.sla.gov.sg/sirent/About/OurServices — RTK / DGNSS / Post Processing / Telematics service catalogue
- SiReNT Wikipedia entry: https://en.wikipedia.org/wiki/SiReNT — 2006 launch, 5-station geometry, 2010 telematics extension
- Trimble customer story (2022 Alloy refresh): https://geospatial.trimble.com/en/resources/customer-story/smart-move-singapore-land-authority-leverages-precise-positioning-and-geospatial-innovations-to-transform-this-vibrant-city
- ArduSimple Singapore RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-singapore/ (page rev. 2026-05-07; describes SiReNT as paid national service)
- IRAS / Singpass Foreign user Account documentation: https://www.iras.gov.sg/digital-services/others/singpass-foreign-user-account-(sfa)-for-foreign-individuals — confirms SingPass requires SG identity
- Wise / Statrys / Singbac CorpPass guides — confirms CorpPass requires registered Singapore entity

```
