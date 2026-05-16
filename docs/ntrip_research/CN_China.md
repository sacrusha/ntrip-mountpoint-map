# China [CN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: NO free public NTRIP for individuals in mainland China.

Three commercial nationwide RTK services dominate (Qianxun · CMCC OneNet · Tencent CORS), all gated by Chinese mobile number + 实名认证 real-name verification. Provincial CORS networks are licensed-only under 测绘资质 (surveying qualification) and unavailable to individuals. Volunteer NTRIP is effectively absent (2 rtk2go bases nationwide, 0 Centipede, 0 EarthScope real-time). HK and Macao are covered in separate files (`HK_HongKong.md`, `MO_Macao.md`).

| Field | Value |
|---|---|
| Active free public NTRIP | No |
| Active commercial NTRIP | Yes — Qianxun, CMCC, Tencent — three operator endpoints curl-verified `SOURCETABLE 200 OK` on 2026-05-15 |
| National licensed CORS | Yes — Ministry of Natural Resources / NGCC, 2,700+ stations, no public endpoint |
| Foreign hobbyist eligibility | None — real-name verification + Chinese mobile gate at every commercial service; 测绘资质 gate at every government service |
| datum_epoch | CGCS2000 = ITRF97 @ epoch 2000.0, ellipsoid GRS80 (a=6378137 m, 1/f=298.257222101); adopted 2008-07-01 by NASG. Cited https://epsg.io/4490 and https://link.springer.com/article/10.1186/s43020-020-00032-w |

---

## Legal Framework

The 中华人民共和国测绘法 (Surveying and Mapping Law of the PRC, 2002, revised 2017), Articles 27–29, requires institutional 测绘资质 (surveying qualifications) to operate or access fixed reference station networks. Government and provincial CORS are closed to unlicensed individuals as a matter of statute. Foreign organisations operating fixed reference stations in mainland China require additional Ministry of Natural Resources approvals and have historically been denied. Acquisition or republication of CORS network data is restricted, not just stream-auth-gated.

The 2024 Notice on Strengthening Survey & Mapping Information Security Management for Intelligent Connected Vehicles (自然资源部) tightened this framework for automotive applications.

---

## 1. Qianxun (千寻位置 / FindCM)

| Field | Value |
|---|---|
| landing_url | https://www.qxwz.com/products/findcm |
| access_url | https://mall.qxwz.com/market/services/FindCM |
| operator | Qianxun Sensing Network Co., Ltd. (千寻位置网络有限公司) — Alibaba + Norinco / SASAC JV |
| host:port | `rtk.ntrip.qxwz.com:8001` (ITRF2008) · `:8002` (WGS84) · `:8003` (CGCS2000) — all three returned `SOURCETABLE 200 OK` from `Server: POP_GW_Ntrip_1.0_1773149729/1.0` on 2026-05-15, full 4-mountpoint dump with `ENDSOURCETABLE`. Resolves to 39.107.207.235 (varies by region/DNS) |
| mountpoints (probed 2026-05-15) | `AUTO` (RTCM3X, GNSS auto-pick), `RTCM30_GG` (RTCM3X legacy GPS+GLO 1004/1012), `RTCM23_GPS` (RTCM2X legacy GPS-only 1/31/41), `RTCM32_GGB` (RTCM3X MSM7 GPS+GLO+BDS 1074/1084/1124) |
| num_stations | 2,700+ reference stations |
| vrs | yes — nationwide VRS computed from 2,700+ stations; 33 mainland provinces / direct-administered municipalities |
| constellations | GPS · GLONASS · BeiDou · Galileo · (+QZSS for higher tiers) |
| tariff — individual | CNY 400/month or CNY 3,600/year (FindCM single-account, individual or unit pricing identical; observed 2026-05-15 at Leicado reseller); 5-hour free trials via Qianxun trial portal |
| tariff — enterprise SSR/PPP-RTK | CNY 8,000–12,000/year (FastFind Asia-Pacific tier) |
| hobbyist_eligibility | yes for Chinese nationals (qxwz.com or mall.qxwz.com signup; Alipay/WeChat Pay); no for foreigners — 实名认证 real-name verification with mainland ID required, no documented passport path |
| legal_residency_required | yes in practice (real-name gate) |
| last_confirmed_alive | 2026-05-15 — three NTRIP ports curl-verified; product pages active |
| Sources | Leicado reseller (CNY 400/mo, CNY 3,600/yr re-confirmed 2026-05-15): https://www.leicado.com/product-detail/BQa9vQxB ; help center: https://help.qxwz.com/758413038 ; reseller pricing reference: https://www.gdxych.com/cors/qxyzh.html |

Most widely deployed commercial CORS in China; default for surveyors, drone industry, autonomous-vehicle developers. Brands: FindCM (cm-level RTK), FindMSM/FindAR (sub-metre SSR), FindFAST/FastFind (PPP-RTK / SSR).

---

## 2. China Mobile CORS / 中国移动 OneNet (CMCC高精度定位)

| Field | Value |
|---|---|
| landing_url | http://group.bj.chinamobile.com/index/solutionnew/standardproduct/location/ |
| access_url | OMIT — no consumer self-service portal; sold through CMCC business / survey resellers |
| operator | China Mobile Communications Corporation (中国移动) — branded "OnePoint 高精度定位" / "中移智能" |
| host:port | Not publicly published; provisioned per account on activation. No public sourcetable to probe. |
| num_stations | 4,400+ reference stations (CMCC investment ~CNY 336M; densest commercial network by self-reported station count) |
| vrs | yes — NTRIP CMCC interaction mode in receiver UIs |
| tariff — individual | ~CNY 3,600/year (survey-reseller listings 2024–2026, same bracket as Qianxun); positioned as cost-effective for IoT bundling with CMCC SIM/data plans |
| hobbyist_eligibility | yes for Chinese nationals via CMCC business portal or reseller; no for foreigners — Chinese mobile + real-name verification |
| legal_residency_required | yes in practice |
| last_confirmed_alive | 2026-05-15 — landing portal reachable; no probable NTRIP endpoint to probe directly |
| Sources | https://www.leicado.com/leicadearticle-detail/bElvRQ6W (reseller, pricing); landing portal above |

CMCC's distinguishing angle is bundling: account paired with a CMCC SIM/data plan for IoT (drones, agricultural autosteer, shared-bike fleets, autonomous logistics, port automation).

---

## 3. Tencent CORS (腾讯网络RTK / Tencent Location Services)

| Field | Value |
|---|---|
| landing_url | https://lbs.qq.com/rtk/ |
| access_url | OMIT — self-service signup deprecated; current page routes to enterprise inquiry / SDK integration. Hobbyist resale via survey channels (e.g. qxcors.net). |
| operator | Tencent Location Services (腾讯位置服务, lbs.qq.com) |
| host:port | `cors.tencent.com:8001` returned `SOURCETABLE 200 OK` from `Server: TECNETCORS/1.0` on 2026-05-15 (full 7-mountpoint dump with `ENDSOURCETABLE`); resolves 183.47.109.226 / 121.14.23.32. Higher ports (`:8002`–`:8005`) historically advertised but not re-probed individually. |
| mountpoints (probed 2026-05-15) | `RTCM32_GRC`, `RTCM32_GNSS`, `RTCM32_GNSS2`, `RTCM32_GRECJ`, `RTCM32_S1`, `RTCM32_C`, `RTCM32_GRECJ2` — 7 mountpoints, all RTCM3X. Naming reflects constellation combinations (G=GPS, R=GLO, E=GAL, C=BDS, J=QZS). |
| num_stations | 2,800+ virtual network reference stations; 33 mainland provinces; 2 cm horizontal / 5 cm vertical claimed; 99.99% availability |
| vrs | yes |
| tariff — historical (Oct 2022 launch) | CNY 7.88 / 1 d · CNY 18.88 / 3 d · CNY 38.88 / 7 d · CNY 128.88 / 30 d · CNY 998.88 / 365 d. Still widely reproduced by survey resellers. |
| tariff — current (2026) | Self-service hobbyist purchase has been deprecated from public lbs.qq.com/rtk; no primary post-2024 Tencent-direct price confirmed. Reseller channels (qxcors.net etc.) continue to sell short-duration shares at the 2022 floor. |
| hobbyist_eligibility | mixed for Chinese nationals (grey-market reseller route still works); no for foreigners — Tencent ID / WeChat / business-licence gate |
| legal_residency_required | yes in practice |
| last_confirmed_alive | 2026-05-15 — `cors.tencent.com:8001` curl-verified; lbs.qq.com/rtk product page reachable |
| Sources | https://lbs.qq.com/rtk/ · https://www.sohu.com/a/579386199_120296774 (host:port + mountpoint reference) · http://www.qxcors.net/product/26.html (reseller resale) |

Tencent's 2022 entry briefly disrupted Qianxun/CMCC pricing (CNY 998.88/yr ≈ 27% of their CNY 3,600/yr tier). The retreat to enterprise positioning mirrors Tencent Cloud's broader B2B pivot; remaining hobbyist purchase is via grey-market resellers.

---

## 4. Equipment-vendor commercial networks

Chinese GNSS receiver manufacturers operate their own CORS networks, primarily as bundled differentiators with hardware sales. No hobbyist self-service tier published; foreign-individual access not viable.

- **Huace 华测一张网 (CHC Navigation "One Network")** — 4,235 reference stations claimed (densest by self-report), AI-assisted ionosphere modelling; bundled with CHC X-series rovers. https://www.huace.cn/informationDetail/183 · https://www.huace.cn/pdDetail/57
- **South GNSS / SOUTH "南方"** — bundled with South receivers; widely used in surveying education and county survey teams. No public NTRIP price.
- **ComNav / Unicore** — receiver chipset / OEM; networks tied to enterprise integrators, not retail.

---

## 5. Government CORS — National & Provincial (licensed only)

### 全国卫星导航定位基准站网 (National CORS) — Ministry of Natural Resources / NGCC

| Field | Value |
|---|---|
| operator | NGCC (National Geomatics Center of China) under Ministry of Natural Resources / 自然资源部 (formerly NASG) |
| num_stations | 2,700+ |
| Feeds | 北斗地基增强系统 (BeiDou Ground-Based Augmentation System / BGAS) |
| Public NTRIP | None — licensed CORS access only |
| Access | Restricted to organisations holding 测绘资质 (Class A/B/C surveying qualifications) under contract with provincial bureaus |
| hobbyist_eligibility | no |
| legal_residency_required | N/A — licence-gated, not residency-gated |

### 省级CORS网 (Provincial CORS — all 34 provinces / municipalities / autonomous regions)

- First operational provincial network: **SZCORS Shenzhen** (2003)
- Every province / direct-administered municipality / autonomous region now operates its own
- Some are free for licensed organisations (e.g. SZCORS public-service tier); others charge — example: **Sichuan provincial CORS at CNY 8,000/yr**
- All require organisational credentials + valid 测绘资质
- Not accessible to individuals or foreigners

Pipeline note: tracked in `docs/networks.md` under `bgas_china` (national) and `chinese_provincial_cors` (provincial bundle); both rejected from the public map pipeline as licensed-only.

---

## 6. BeiDou GBAS / SBAS-style augmentation (informational)

China's BeiDou Ground-Based Augmentation System (open services since May 2021):
- **Wide-area augmentation** — metre to sub-metre, satellite-broadcast (free, no NTRIP) — out of project scope (DGNSS-class)
- **Regional real-time augmentation** — dm-level, licensed only
- **Real-time PPP/RTK** — cm-level, commercial subscription via Qianxun / CMCC / Tencent

PPP-B2b (BeiDou-3 satellite-delivered PPP) is free over-the-air for compatible receivers but is satellite SSR, not internet NTRIP — out of scope alongside QZSS CLAS / Galileo HAS.

---

## 7. CMONOC — research network, NOT a hobbyist NTRIP path

The 陆态网络 Crustal Movement Observation Network of China (CMONOC, 246 continuous GPS stations, currently in Phase II) is a geophysical research network for earthquake monitoring, plate tectonics, and ionospheric studies operated under the China Earthquake Administration / NGCC. It does NOT provide a public real-time NTRIP service. A small subset of CMONOC stations contribute to IGS MGEX (BJFS, SHAO, WUHN, URUM, etc.) for RINEX post-processing only. See https://files.igs.org/pub/resource/pubs/06_darmstadt/IGS%20WS%202006%20Papers%20PDF/5_Gan_Paper2IGS_Preceedings.pdf

---

## Foreign-User Reality

There is **no public, free, or self-service NTRIP path** for non-resident hobbyists in mainland China. Barriers stack:

1. **Commercial (Qianxun, CMCC, Tencent)** — all require Chinese mobile number + 实名认证 real-name verification with mainland ID. No documented passport-based registration path.
2. **Government (national + provincial CORS)** — closed to individuals by statute under 测绘资质 institutional licensing, irrespective of nationality.
3. **Vendor networks (CHC, South)** — bundled with hardware sales through Chinese distributors; foreign hobbyist channel undeveloped.
4. **Private base deployment** — operating a fixed reference station inside China without 测绘资质 violates the Surveying and Mapping Law; short-baseline private base+rover for a single user is a legal grey area, tolerated for non-published use.
5. **GEODNET (web3 / DePIN)** — geodnet.com publishes a public coverage map (https://rtk.geodnet.com/coverage/). Mainland-China deployment exists but density and continuity must be verified per site before deployment; international hobbyist access via GEOD tokens is permitted by GEODNET but the legality of running an unregistered mainland-China base under 测绘法 is unresolved.

In practice, foreign workers and students in mainland China who need RTK rely on: (a) GEODNET tokens where local miner coverage is adequate, (b) a friend / employer's Qianxun account, or (c) short-baseline own-base deployment (single private base for single user).

---

## Volunteer Coverage (rtk2go + Centipede + EarthScope)

Live counts from `data/stations.json`, fetched 2026-05-15 via `py scripts/stations_by_country.py CHN`:

| Source | CHN total | Notes |
|---|---|---|
| rtk2go | 2 | `CHENKATE` (22.67°N, 113.91°E — Pearl River Delta / Shenzhen) and `JinshitanNB` (39.09°N, 122.03°E — Liaoning / Dalian Jinshitan). `Daniel_Bynav` (Hunan, in prior 2026-05-07 research) has dropped from the source list. |
| Centipede | 0 | No CHN nodes |
| EarthScope | 0 | CHN not in EarthScope country list (a handful of Chinese IGS stations exist as RINEX-only data via IGS MGEX / NOTA — not a real-time NTRIP path) |

Volunteer real-time coverage in mainland China is effectively absent (2 rtk2go bases for a population of 1.4 billion).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| IGS MGEX (Chinese stations: BJFS, SHAO, WUHN, URUM, etc.) | https://www.igs.org/mgex/ ; https://network.igs.org/ | Free non-commercial |
| EarthScope IGS data archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| iGMAS (国际GNSS监测评估系统) | http://www.igmas.org/ | Free academic |
| CMONOC stations (subset to MGEX) | via IGS MGEX above | Free non-commercial |
| Qianxun RINEX archive | qxwz.com account | Paid subscription |

---

## Datum & Epoch

National datum is **CGCS2000** (China Geodetic Coordinate System 2000):
- Referred to ITRF97 at reference epoch 2000.0
- Ellipsoid: GRS80 (semi-major axis a = 6378137 m, inverse flattening 1/f = 298.257222101)
- Officially adopted 2008-07-01 by NASG (now Ministry of Natural Resources / 自然资源部)
- Origin: Earth centre of mass; orientation: BIH 1984.0
- Sources: https://epsg.io/4490 (EPSG:4490) · https://link.springer.com/article/10.1186/s43020-020-00032-w (Cheng et al., Satellite Navigation 2020 — quotes "CGCS2000 is referred to ITRF97 at the reference epoch 2000.0")

Qianxun explicitly publishes one NTRIP port per reference frame: `:8001` = ITRF2008 · `:8002` = WGS84 · `:8003` = CGCS2000. Receiver workflows in mainland China typically request `:8003` to keep coordinates in the national CGCS2000 frame.

---

## Gaps & Observations

1. **No free public NTRIP for individuals exists in mainland China.** This is structural — the Surveying and Mapping Law is the binding constraint, not an oversight.
2. **The commercial market is a three-way oligopoly** (Qianxun, CMCC, Tencent) at near-identical CNY ~3,000–3,600/yr individual pricing. Tencent's 2022 CNY 998.88/yr disruption was real but has been retracted from self-service.
3. **Provincial pricing is heterogeneous** — Sichuan CNY 8,000/yr is one published example; SZCORS has a free public tier; most are quote-only and licence-gated regardless of price.
4. **Foreign-user gap is hard.** Foreign individuals operating in China should plan for either (a) institutional sponsorship via an employer with 测绘资质, (b) own-base deployment under careful interpretation of the law, or (c) GEODNET / private CORS-share where feasible.
5. **The volunteer network gap is unlikely to close** — rtk2go dropped from 3 to 2 CHN bases since 2026-05-07; Centipede has no Chinese presence; the regulatory environment discourages community deployment.
6. **GEODNET / DePIN networks are the most plausible new free-ish path,** with the caveat that operating an unregistered mainland-China base under 测绘法 is unresolved.

---

## Sources Consulted

- Qianxun FindCM product page: https://www.qxwz.com/products/findcm
- Qianxun mall (FindCM, pricing): https://mall.qxwz.com/market/services/FindCM
- Qianxun real-name authentication help: https://help.qxwz.com/758413038
- Leicado Qianxun reseller pricing (CNY 400/mo, CNY 3,600/yr, re-confirmed 2026-05-15): https://www.leicado.com/product-detail/BQa9vQxB
- Gdxych.com Qianxun reseller listing: https://www.gdxych.com/cors/qxyzh.html
- China Mobile CORS / OneNet portal: http://group.bj.chinamobile.com/index/solutionnew/standardproduct/location/
- Leicado CMCC reseller listing: https://www.leicado.com/leicadearticle-detail/bElvRQ6W
- Tencent Location Services RTK: https://lbs.qq.com/rtk/
- Tencent NTRIP host/port + mountpoint reference: https://www.sohu.com/a/579386199_120296774 ; https://www.sohu.com/a/580039508_120296774
- Tencent reseller listing: http://www.qxcors.net/product/26.html
- Huace 华测一张网: https://www.huace.cn/informationDetail/183 ; https://www.huace.cn/pdDetail/57
- Springer/Cheng et al. on China geodetic frame: https://link.springer.com/article/10.1186/s43020-020-00032-w
- EPSG:4490 CGCS2000 entry: https://epsg.io/4490
- ArduSimple China caster review (confirms no national free network): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-china/
- Han Kun Law commentary on intelligent-vehicle survey/mapping security notice: https://hankunlaw.com/portal/article/index/cid/8/id/14389
- CMONOC IGS phase-II paper: https://files.igs.org/pub/resource/pubs/06_darmstadt/IGS%20WS%202006%20Papers%20PDF/5_Gan_Paper2IGS_Preceedings.pdf
- GEODNET coverage map: https://rtk.geodnet.com/coverage/
- curl probes 2026-05-15: `rtk.ntrip.qxwz.com:8001 / :8002 / :8003` (all `SOURCETABLE 200 OK`, `Server: POP_GW_Ntrip_1.0_1773149729/1.0`, 4 mountpoints, `ENDSOURCETABLE`); `cors.tencent.com:8001` (`SOURCETABLE 200 OK`, `Server: TECNETCORS/1.0`, 7 mountpoints, `ENDSOURCETABLE`)
- Local pipeline data: `data/stations.json` (rtk2go CHN = 2 — `CHENKATE` 22.67/113.91, `JinshitanNB` 39.09/122.03; centipede CHN = 0; EarthScope CHN = 0; fetched 2026-05-15)
