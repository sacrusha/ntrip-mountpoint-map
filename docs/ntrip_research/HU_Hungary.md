# Hungary [HU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — two active NTRIP RTK casters: GNSSnet.hu (national paid service) and Centipede-RTK (free, dense volunteer network with strong Hungarian presence)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — multiple |
| **Network 1 name** | GNSSnet.hu |
| **Operator — GNSSnet.hu** | Lechner Nonprofit Kft. (Lechner Tudásközpont) / Kozmikus Geodéziai Obszervatórium (KGO, Penc) |
| **host:port — GNSSnet.hu** | `ntrip1.gnssnet.hu:2101` (primary, Budapest) · `ntrip2.gnssnet.hu:2101` (backup, Penc) — two independently operating, identically configured servers |
| **VRS — GNSSnet.hu** | Yes — Network RTK (hálózati RTK) and DGNSS corrections; RTCM 3.x MSM |
| **tariff — annual unlimited RTK** | HUF 150,000 net (source: gnssnet.hu, via lechnerkozpont.hu "Árcsökkenés" article; observed 2026-05-06) |
| **tariff — 30 consecutive days** | HUF 15,000 net (source: same) |
| **tariff — 90 days flexible** | Below annual rate proportionally; non-consecutive days selectable |
| **tariff — 150 days flexible** | Below annual rate proportionally; non-consecutive days selectable |
| **VAT** | Hungarian standard ÁFA is 27%; prices above are net (nettó) |
| **hobbyist_eligibility — GNSSnet.hu** | Yes — individual registration accepted; no professional licence requirement |
| **legal_residency_required — GNSSnet.hu** | Unclear — no explicit residency restriction found; Hungarian billing address/bank may be preferred |
| **last_confirmed_alive — GNSSnet.hu** | 2026-05-06 (gnssnet.hu loaded HTTP 200; NTRIP1 and NTRIP2 sourcetable buttons visible; PDF price list link active) |
| **Network 2 name** | Centipede-RTK |
| **Operator — Centipede-RTK** | Open community project (INRAE origin, France); Hungarian nodes operated by individual volunteers |
| **host:port — Centipede-RTK** | `caster.centipede.fr:2101` (global caster) |
| **VRS — Centipede-RTK** | No — individual base station streams only; nearest-base selection |
| **tariff — Centipede-RTK** | Free — open access, no registration required |
| **hobbyist_eligibility — Centipede-RTK** | Yes — open to all |
| **legal_residency_required — Centipede-RTK** | No |
| **last_confirmed_alive — Centipede-RTK** | 2026-05-06 (centipede-rtk.org operational; Hungary coverage confirmed via map) |

## Context Notes

- **GNSSnet.hu overview**: The national GNSS correction service operated by Lechner Nonprofit Kft. (formerly FÖMI). Network consists of 35 domestic and 19 border reference stations (total ~54). Provides both real-time RTK/Network RTK and post-processing RINEX. Launched early 2000s; long-running government-operated commercial service.
- **GNSSnet.hu price reduction**: A lechnerkozpont.hu article titled "Árcsökkenés a GNSSnet.hu átalánydíjas szolgáltatásaiban" (Price reduction in GNSSnet.hu flat-rate services) documents the current pricing (HUF 150,000 net/year). The PDF price list at `gnssnet.hu/pdf/gnss_valosideju_szolg_arak.pdf` was downloadable on 2026-05-06 but is in Hungarian. ÁFA (VAT) in Hungary is 27% — the highest in the EU — so gross annual price is approximately HUF 190,500.
- **GNSSnet.hu DGNSS**: Also offers DGNSS sub-meter corrections at lower subscription cost; out of scope for this research.
- **FarmRTK.hu**: A separate agricultural RTK service (farmrtk.hu), linked from gnssnet.hu, targeting precision agriculture with optimized mountpoints. Pricing not researched separately.
- **Centipede-RTK in Hungary**: Hungary has achieved among the densest Centipede-RTK coverage in continental Europe, with over 130 volunteer base stations installed primarily by farmers, achieved within roughly two years. Coverage is effectively nationwide. Hungarian-language tutorial videos on using Centipede RTK are published on YouTube (playlist on DIY community RTK). The global Centipede caster (`caster.centipede.fr:2101`) carries all Hungarian mountpoints — no separate national caster.
- **Hobbyist choice**: For hobbyists, Centipede-RTK is the recommended starting point — entirely free, no registration, and effectively nationwide coverage. GNSSnet.hu is the professional-grade option with VRS and guaranteed uptime SLA.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GNSSnet.hu RINEX post-processing** | https://www.gnssnet.hu/ (login required) | Included with subscription or separate; contact for tariff |
| **GNSSnet.hu online RINEX transform (eHT2)** | https://eht2.gnssnet.hu/ | Bundled with account |

## Sources Consulted
- GNSSnet.hu main site + realtime service page: https://www.gnssnet.hu/index.php?r=site/realtime (curl 200 + page content confirmed 2026-05-06)
- GNSSnet.hu NTRIP1 sourcetable link: http://ntrip1.gnssnet.hu:2101/sourcetable.htm
- GNSSnet.hu NTRIP2 sourcetable link: http://ntrip2.gnssnet.hu:2101/sourcetable.htm
- Lechner Kft. price reduction article: https://lechnerkozpont.hu/cikk/arcsokkenes-a-gnssnet-hu-atalanydijas-szolgaltatasaiban
- GNSSnet.hu price PDF: https://www.gnssnet.hu/pdf/gnss_valosideju_szolg_arak.pdf
- GNSSnet.hu service description PDF: https://www.gnssnet.hu/pdf/gnssnet.hu_szolgaltatas_leiras.pdf
- Lechner GNSS service page: https://lechnerkozpont.hu/oldal/gnss
- Centipede-RTK home: https://www.centipede-rtk.org/
- Centipede-RTK Hungary coverage map: https://map.centipede-rtk.org/
- INRAE Centipede Hungary article: https://www.inrae.fr/en/news/democratising-precision-guided-agriculture-ever-expanding-centipede-rtk-network
- YouTube DIY community RTK Hungary playlist: https://www.youtube.com/playlist?list=PLcjIHVKrhRGavnBJ66A0once8LmNFwiCr
- ArduSimple Hungary: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-hungary/
