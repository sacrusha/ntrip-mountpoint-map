# Azerbaijan [AZ] - NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: RESTRICTED - one national NTRIP caster (AzPOS); bilateral Azerbaijani-language contract gates access. One free rtk2go volunteer base in greater Baku.

## AzPOS - Azerbaijan Positioning Observation System

| Field | Value |
|---|---|
| operator | State Service on Property Issues under the Ministry of Economy (Emlak Meseleleri Dovlet Xidmeti); operator entity for the CORS network is the Cadastre and Land Surveying Service |
| landing_url | https://www.emlak.gov.az/en/page/view/96 |
| access_url | https://www.emlak.gov.az/en/page/view/96 |
| access_type | paid |
| coverage | 37 mainland CORS + 8 added in reintegrated Karabakh per 2024 paper (operator portal still lists 37 only as of 2026-05-23); 30-40 km station spacing; per-station RTK radius ~20 km, communication range up to 70 km (2014 operator spec, unchanged in public material) |
| num_stations | 37 per operator portal (emlak.gov.az/en/page/view/96 refetched 2026-05-23: "37 reference stations in the country, 3 of which are in the mountains"); 8 Karabakh stations (Fuzuli, Jebrail, Zangilan, Kelbajar1, Kelbajar2, Agdam, Shusha, Lachin) added per 2024 AMA-journal paper "Post-war Restoration of the AzPOS Network in Karabakh" - operator total not yet updated to reflect expansion |
| tariff | not published - emlak.gov.az AzPOS page describes service + eligibility only; pricing governed by bilateral service agreement signed at the State Service on Property Issues office in Baku; no public AZN figures (checked: emlak.gov.az/en/page/view/96 2026-05-23; ardusimple.com Azerbaijan page 2026-05-16; readkong AzPOS paper mirror 2026-05-23; web search "azpos.az SBC tariff 2025/2026" 2026-05-23) |
| hobbyist_eligibility | no - operator text accepts "legal entities and individuals" but the contract is bilateral, Azerbaijani-language, requires in-person / email engagement with the Baku Yasamal office, and excludes anonymous or self-service signup; no hobbyist tariff exists |
| sourcetable | not reachable - provisional host `azpos.az:2101` resolves (185.161.226.29 refetched 2026-05-23) but TCP 2101/80/443 filtered from this sandbox; no third-party confirmation of geo-block published (checked: monitor.use-snip.com 2026-05-23; ntrip-list.com 2026-05-23; mvarga1989 GNSS CORS list 2026-05-23) |
| vrs | ? - operator material describes Leica-Spider-style architecture (which supports NRTK / VRS / MAX / iMAX) but no operator declaration of NRTK products surfaced; no NRTK-style mountpoint names confirmed (checked: emlak.gov.az/en/page/view/96 2026-05-23; ardusimple Azerbaijan page 2026-05-23; UNOOSA 2014 paper) |
| residency_required | yes - bilateral Azerbaijani-language contract signed at the Baku Yasamal office; no remote / non-resident signup channel exists |
| stations_source | https://www.emlak.gov.az/en/page/view/96 (operator descriptive text; no live map; no public sourcetable URL) |

AzPOS is governed under the Ministry of Economy's State Service on Property Issues; the AzPOS contact channel is azpos@emlak.gov.az / (012) 562-82-70 / (050) 759-11-44 / (050) 229-25-23 (Baku, Yasamal district, Sh. Mehdiyev str. 269). The 2014 commissioning paper describes Leica-Spider-style architecture, GPS+GLONASS baseline; Control Centre supports up to 100 parallel RTK users and 25 parallel web-service users. BeiDou support is not stated on the operator portal (emlak.gov.az lists GPS + GLONASS + Galileo); whether AzPOS now streams BeiDou is unverified. The 2024 Karabakh expansion was documented in the AMA-journal paper "Post-war Restoration of the AzPOS Network in Karabakh" (8 stations: Fuzuli, Jebrail, Zangilan, Kelbajar1, Kelbajar2, Agdam, Shusha, Lachin; 30 km coverage radius each) with 24-hour test measurements at Fuzuli using Leica GS18. Per the paper the 8 Karabakh stations bring AzPOS to 45 total, but emlak.gov.az still lists 37 only (refetched 2026-05-23) - operator portal lag, not contradiction. The 2024 operator material continues to describe WGS-84 with UTM zones 38/39 as the published frame; the ardusimple.com Azerbaijan page lists "Coordinate System: Global WGS84" for AzPOS consistent with this. No epoch realization or operator-portal declaration URL is provided; per the operator-declaration rule, datum_epoch is omitted. Provisional host `azpos.az:2101` (DNS still resolves to 185.161.226.29, refetched 2026-05-23) has TCP 2101 / 80 / 443 filtered from this sandbox - no public sourcetable is published, and credentials/host are issued contract-side; no third-party reachability confirmation surfaced.

## Free / volunteer fallback

| Source | Mountpoint | Lat / Lon | Notes |
|---|---|---|---|
| rtk2go | `WHTCTY` | 40.38 N, 49.89 E | Single volunteer base in greater Baku (verified 2026-05-23 in `data/rtk2go.sourcetable`, RTCM 3.2 GPS+GLO+GAL+BDS, single-base; rtk2go convention any-email / no password). Free, no signup. Usable within ~20 km of Baku. Anchor accuracy on rtk2go is typically TMODE3 survey-in (1-3 m absolute, frozen at install; relative accuracy still cm) - rover positions are repeatable but not tied to a declared frame. |

No Centipede, EarthScope, GEODNET, ONOCOY, PointOne, or Swift Skylark stations have been observed inside Azerbaijan as of 2026-05-23. The next-nearest free RTK source on any side (Turkey TUSAGA-Aktif, Iran SHAMIM, Russia FAGS) is >200 km from any Azerbaijani settlement and either residency-gated or geo-blocked.

## Hobbyist path

1. **Greater Baku (<=20 km)** - try rtk2go `WHTCTY` (free, no signup, single-base RTK).
2. **Elsewhere in Azerbaijan** - no free RTK path. AzPOS access requires a bilateral Azerbaijani-language contract with the Baku office; effectively restricted to local entities.
3. **Self-host** - deploy a base/rover pair, or stream a base to rtk2go.com / Centipede for community use.
4. **PPP / SSR fallback** - Galileo HAS (~20 cm horizontal, free, satellite-delivered) for sub-metre work where RTK is unavailable.

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| AzPOS RINEX archive (via service agreement) | https://www.emlak.gov.az/en/page/view/96 | Governed by AzPOS agreement; not publicly priced |
| IGS BAKU station archive | https://network.igs.org/ | Free non-commercial |

## Sources

- AzPOS operator page (English; refetched 2026-05-23 - 37+3 mountain stations, "legal entities and individuals" eligibility, Baku Yasamal contact): https://www.emlak.gov.az/en/page/view/96
- ArduSimple Azerbaijan: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-azerbaijan/
- UNOOSA 2014 GNSS workshop AzPOS paper: https://www.unoosa.org/documents/pdf/psa/activities/2014/trieste-gnss/33.pdf
- ReadKong mirror of AzPOS cadastre paper (WGS-84 / UTM38-39): https://www.readkong.com/page/azerbaijan-positioning-observation-system-azpos-for-real-3736136
- ResearchGate "Post-war Restoration of the AzPOS Network in Karabakh" (2024): https://www.researchgate.net/publication/389768010_Post-war_Restoration_of_the_AzPOS_Network_in_Karabakh
- Geospatial World AzPOS commercial-launch notice: https://www.geospatialworld.net/news/azerbaijan-positioning-observation-system-put-into-commercial-use/
- Local 2026-05-23: `data/rtk2go.sourcetable` row 863 `WHTCTY;Baku;...;AZE;40.38;49.89` confirmed; `scripts/stations_by_country.py AZE` -> 1 rtk2go station only
