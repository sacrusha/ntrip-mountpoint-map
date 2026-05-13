# Azerbaijan [AZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: ACTIVE — national NTRIP caster (AzPOS); credentials issued post-registration; endpoint provisionally `azpos.az:2101` but authentication-gated, no public sourcetable; 1 rtk2go volunteer base in Baku

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (registration required; no anonymous endpoint) |
| **Network name** | AzPOS — Azerbaijan Positioning Observation System |
| **Operator** | State Service on Property Issues under the Ministry of Economy (Əmlak Məsələləri Dövlət Xidməti) — operator entity "Kadastr və Yer Quruluşu Layihə Tədqiqat Mərkəz" (Design Research Centre for Cadastre & Land Management); contact via emlak.gov.az |
| **host:port — AzPOS** | Provisionally `azpos.az:2101` (referenced in third-party material); authentication-gated, no sourcetable response to unauthenticated queries. The actual delivered hostname/port is issued to each subscriber after a service agreement is signed |
| **tariff — AzPOS** | Not publicly listed; governed by bilateral service agreement. Contact: azpos@emlak.gov.az |
| **Network size** | ~45 physical CORS (up from the original 37 stations of the 2014 commissioning; 8 stations added in the Karabakh region in 2024: Fuzuli, Jebrail, Zangilan, Kəlbəcər ×2, Ağdam, Şuşa, Laçın) |
| **Backend / VRS** | Leica GNSS Spider (per recent project documentation) — VRS-capable; supports GPS + GLONASS + Galileo + BeiDou |
| **hobbyist_eligibility** | "Legal entities and individuals" both accepted per operator description; no licensed-surveyor requirement, but a formal bilateral agreement is required. Process is conducted in Azerbaijani |
| **legal_residency_required** | Not explicitly stated, but the contract-based access model with a Baku-based office in practice favours Azerbaijani residents or local agents |
| **last_confirmed_alive** | 2026-05-12 — `emlak.gov.az/en/page/view/96` reachable; no public sourcetable confirmation possible (no anonymous endpoint) |

## Most Recent Project Announcements

- **2014** — AzPOS commissioned with 37 stations across Azerbaijan (excluding mountainous Karabakh region under Armenian control at that time). UNOOSA workshop paper documented architecture, control-centre software, and RTK service capability.
- **2024** — Network expanded to ~45 stations after the post-2020 reintegration of the Karabakh region: 8 new stations at Fuzuli, Jebrail, Zangilan, two sites in Kəlbəcər district, Ağdam, Şuşa, Laçın.
- No formal re-launch or public-tariff announcement has been issued for 2025–2026; service has been in continuous commercial operation since 2014.

## Context Notes

- **Station spacing**: 30–40 km between CORS; usable RTK radius ~20 km per station; communication range up to 70 km per the 2014 documentation.
- **Concurrent user capacity**: Control centre supports up to 100 parallel RTK users (2014 spec).
- **Signals**: GPS + GLONASS (2014 baseline); recent project documentation cites Galileo + BeiDou support consistent with a Leica Spider upgrade.
- **Services offered**: Real-time RTK, DGNSS, and post-processing via RINEX archive on request.
- **Access procedure**: Applicants submit a request via `emlak.gov.az`; staff provide a service agreement for review; credentials (NTRIP host, port, mountpoints, username, password) are issued after the agreement is signed. **No anonymous or self-service public endpoint exists.**
- **Caster host probe**: `azpos.az:2101` is not publicly resolvable to a sourcetable from outside Azerbaijan; consistent with an authentication-gated caster where the public DNS hostname is a façade.
- **Volunteer rtk2go**: 1 base — `WHTCTY` at 40.38°N, 49.89°E (greater Baku, country code `AZE`), visible in `data/stations.json` 2026-05-12 snapshot via `rtk2go.com:2101`. Single base only; useful within ~20 km of Baku.
- **Centipede / EarthScope**: zero AZ-coded stations.
- **Global commercial fallbacks**: No Azerbaijan-specific coverage confirmed on GEODNET, ONOCOY, Centipede-RTK, PointOne, Swift Skylark.

## Hobbyist Path

1. **In or near Baku** — try rtk2go `WHTCTY` first (free, no signup, single-base RTK within ~20 km).
2. **Elsewhere in Azerbaijan** — no free RTK path. AzPOS access requires a bilateral contract in Azerbaijani; effectively restricted for non-residents.
3. **Self-host or PPP fallback** — deploy a local base/rover pair, or use Galileo HAS (~40 cm, free, no internet required) for sub-metre work.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **AzPOS RINEX archive** — available via emlak.gov.az upon registration | https://www.emlak.gov.az/en/page/view/96 | Governed by service agreement; pricing not public |
| **IGS / EarthScope archive** — BAKU IGS station for post-processing | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- AzPOS about page: https://www.emlak.gov.az/en/page/view/96
- UNOOSA 2014 GNSS workshop paper (architecture, control centre): https://www.unoosa.org/documents/pdf/psa/activities/2014/trieste-gnss/33.pdf
- DocPlayer mirror of AzPOS system paper: https://docplayer.net/48966253-Azerbaijan-positioning-observation-system-azpos-for-real-estate-cadastre-data-base.html
- Geospatial World AzPOS commercial-launch notice: https://www.geospatialworld.net/news/azerbaijan-positioning-observation-system-put-into-commercial-use/
- ArduSimple Azerbaijan page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-azerbaijan/
- country-survey.md AZ entry (2026-04-30; documents 45-station expansion and Leica Spider backend)
- `data/stations.json` 2026-05-12 — rtk2go `WHTCTY` [AZE] (40.38, 49.89) confirmed; no Centipede / EarthScope AZE stations
- RTK2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
