# China [CN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revising 2026-05-07 entry)

## Status: NO free public NTRIP for individuals. Three commercial nationwide RTK services dominate (Qianxun · CMCC OneNet · Tencent CORS), each ~CNY 400/month or CNY 3,600–3,800/yr for an individual annual account. Provincial CORS networks are licensed-only under 测绘资质 (surveying qualification) and not hobbyist-accessible. Foreign individuals face hard barriers (Chinese phone number + 实名认证 national-ID verification) at every service. Volunteer NTRIP is negligible in mainland China (3 rtk2go bases, 0 Centipede).

| Field | Value |
|---|---|
| **Active free public NTRIP RTK caster** | No |
| **Active commercial NTRIP RTK casters** | Yes — Qianxun, CMCC, Tencent (and equipment-vendor networks: Huace 一张网, etc.) — all three NTRIP endpoints curl-verified `SOURCETABLE 200 OK` on 2026-05-12 |
| **Active national licensed CORS** | Yes — NGCC / Ministry of Natural Resources, 2,700+ stations, no public endpoint |
| **Foreign hobbyist eligibility** | No practical path for any of the above |
| **Hong Kong note** | HK has its own free SatRef NTRIP — covered in `HK_HongKong.md`. Macao has free MoSRef — `MO_Macao.md`. This file is mainland-only. |
| **last_confirmed_alive (commercial NTRIP endpoints)** | 2026-05-12 — Qianxun ports 8001/8002/8003 (all `SOURCETABLE 200 OK`), Tencent `cors.tencent.com:8001` (`SOURCETABLE 200 OK`), CMCC product portals reachable |

---

## Legal Framework

The 中华人民共和国测绘法 (Surveying and Mapping Law of the PRC, 2002, revised 2017), Articles 27–29, requires institutional 测绘资质 (surveying qualifications) to operate or access fixed reference station networks. All government and provincial CORS networks are closed to unlicensed individuals as a matter of statute. Foreign organisations operating fixed reference stations in mainland China require additional approvals from the Ministry of Natural Resources and have historically been denied.

The 自然资源部 ("Notice on Strengthening Survey & Mapping Information Security Management for Intelligent Connected Vehicles") tightened this framework further for automotive applications in 2024.

---

## 1. Qianxun (千寻位置 / 千寻知寸 FindCM) — Dominant commercial operator

| Field | Value |
|---|---|
| **Operator** | Qianxun Sensing Network Co., Ltd. (千寻位置网络有限公司) — Alibaba + Norinco / SASAC joint venture |
| **Service brands** | FindCM (千寻知寸, cm-level RTK), FindMSM / FindAR (sub-metre SSR), FindFAST / FastFind (PPP-RTK / SSR PPP) |
| **host:port (NTRIP)** | `rtk.ntrip.qxwz.com` ports `8001` (ITRF2008) · `8002` (WGS84) · `8003` (CGCS2000). All three returned `SOURCETABLE 200 OK` from `Server: POP_GW_Ntrip_1.0` on 2026-05-12. |
| **IP (cached)** | 39.107.207.235 (resolved 2026-05-12; DNS varies by region) |
| **Mountpoints (sourcetable observed 2026-05-12)** | `AUTO` (RTCM3X, full GNSS auto-pick), `RTCM30_GG` (RTCM3X, legacy GPS+GLO with 1004/1012), `RTCM23_GPS` (RTCM2X, legacy GPS-only), `RTCM32_GGB` (RTCM3X, MSM7 GPS+GLO+BDS) |
| **VRS** | Yes — nationwide VRS computed from 2,700+ reference stations |
| **Constellations** | GPS · GLONASS · BeiDou · Galileo · (QZSS for higher tiers) |
| **Coverage** | 33 mainland provinces / direct-administered municipalities (excl. HK / Macao / Taiwan) |
| **Tariff — individual** | CNY 400/month or CNY 3,600/year (single-account "single-day-single-network" survey use) — Leicado reseller listing confirmed 2026-05-12; CNY 3,600–3,800/yr commonly quoted on the survey-equipment market. 5-hour free trials available via the Qianxun trial portal. |
| **Tariff — SSR/PPP-RTK enterprise** | CNY 8,000–12,000/year (FastFind SSR Asia-Pacific) |
| **hobbyist_eligibility — Chinese national** | Yes in practice — register at qxwz.com or mall.qxwz.com using Chinese mobile number; pay via Alipay/WeChat Pay |
| **hobbyist_eligibility — foreign** | No practical path — registration requires Chinese mobile number and 实名认证 (real-name ID verification with Chinese ID card / mainland-issued document) |
| **legal_residency_required** | Yes in practice (real-name verification gate) |
| **last_confirmed_alive** | 2026-05-12 — three NTRIP ports curl-verified (sourcetable returned, ENDSOURCETABLE present); product pages active |
| **Sources** | https://www.qxwz.com/products/findcm · https://mall.qxwz.com/market/services/FindCM · https://findcm.my.qxwz.com/ |

Most widely deployed commercial CORS in China; default for surveyors, drone industry, autonomous-vehicle developers; the assumed "China RTK service" in third-party rover documentation.

---

## 2. China Mobile CORS / 中国移动 OnePoint (CMCC高精度定位)

| Field | Value |
|---|---|
| **Operator** | China Mobile Communications Corporation (中国移动) — branded "OnePoint 高精度定位" / "中移智能" |
| **Stations** | 4,400+ reference stations (CMCC investment of ~CNY 336M; densest Chinese commercial network by station count) |
| **Coverage** | Mainland China except HK / Macao / Taiwan and a few unpopulated regions |
| **Service tiers** | Sub-metre · cm-level · mm-level (post-processed) |
| **Protocol** | NTRIP (CMCC interaction mode in receiver UI) |
| **host:port** | Not openly published; provisioned per account on activation |
| **Tariff — individual** | ~CNY 3,600/year (survey-trade reseller listings 2024–2026) — same bracket as Qianxun, marketed as the cost-effective alternative; "OneNet" pricing emphasised as bundling-friendly for IoT devices on China Mobile data plans |
| **hobbyist_eligibility — Chinese national** | Yes — open to individuals; account purchase via CMCC business portal or survey reseller |
| **hobbyist_eligibility — foreign** | No practical path — requires Chinese mobile number, real-name verification |
| **legal_residency_required** | Yes in practice |
| **last_confirmed_alive** | 2026-05-07 (CMCC Beijing high-precision portal reachable; reseller listings current) |
| **Sources** | http://group.bj.chinamobile.com/index/solutionnew/standardproduct/location/ · https://www.leicado.com/leicadearticle-detail/bElvRQ6W (reseller, pricing) |

CMCC's stronger angle is bundling: account paired with a CMCC SIM/data plan for IoT (drones, agricultural autosteer, shared-bike fleets, autonomous logistics, port automation).

---

## 3. Tencent CORS (腾讯网络RTK / Tencent Location Services)

| Field | Value |
|---|---|
| **Operator** | Tencent Location Services (腾讯位置服务, lbs.qq.com) |
| **Service launch** | August 2022 as public-beta; transitioned to commercial pricing late 2022 |
| **Stations** | 2,800+ virtual network reference stations |
| **Coverage** | 33 mainland provinces / direct-administered municipalities |
| **Accuracy** | 2 cm horizontal / 5 cm vertical claimed; 99.99% service availability |
| **host:port (NTRIP)** | `cors.tencent.com:8001` returned `SOURCETABLE 200 OK` from `Server: TECNETCORS/1.0` on 2026-05-12; resolves to 183.47.109.226 / 121.14.23.32. Higher ports (`:8002`–`:8005`) historically advertised for different reference frames / epochs but not re-probed individually. |
| **Mountpoints (verified 2026-05-12)** | `RTCM32_GRC`, `RTCM32_GNSS`, `RTCM32_GNSS2`, `RTCM32_GRECJ`, `RTCM32_S1`, `RTCM32_C`, `RTCM32_GRECJ2` — 7 mountpoints, all RTCM3X. Naming reflects constellation combinations (G=GPS, R=GLO, E=GAL, C=BDS, J=QZS). |
| **Protocol** | NTRIP 2.0 |
| **Tariff — historical (Oct 2022)** | CNY 7.88 / 1 day · CNY 18.88 / 3 days · CNY 38.88 / 7 days · CNY 128.88 / 30 days · CNY 998.88 / 365 days |
| **Tariff — current (2026)** | Self-service hobbyist purchase has been deprecated from the public lbs.qq.com/rtk product page (routes to enterprise inquiry / SDK integration). The 2022 retail pricing is still widely reproduced by survey resellers (e.g. qxcors.net) but no primary post-2024 Tencent price page has been re-confirmed. |
| **hobbyist_eligibility — Chinese national** | Mixed — survey-reseller channels still sell short-duration accounts; Tencent direct now positions as enterprise SDK customers |
| **hobbyist_eligibility — foreign** | No practical path — Tencent ID / WeChat / business-licence gate |
| **legal_residency_required** | Yes in practice |
| **last_confirmed_alive** | 2026-05-12 — `cors.tencent.com:8001` curl-verified (full 7-mountpoint sourcetable returned, ENDSOURCETABLE present); lbs.qq.com/rtk product page reachable |
| **Sources** | https://lbs.qq.com/rtk/ · https://www.sohu.com/a/579386199_120296774 (host:port + mountpoint reference) · http://www.qxcors.net/product/26.html (reseller resale) |

Tencent's 2022 entry briefly disrupted Qianxun/CMCC pricing (CNY 998/yr ≈ 27% of their CNY 3,600/yr tier). The retreat to enterprise positioning mirrors Tencent Cloud's broader B2B pivot; remaining hobbyist purchase is via grey-market resellers selling short-duration shares.

---

## 4. Equipment-vendor commercial networks (CHC, South, ComNav, Unicore)

Chinese GNSS receiver manufacturers operate their own CORS networks, primarily as bundled differentiators with hardware sales:

- **Huace 华测一张网 (CHC Navigation "One Network")** — claims 4,235 reference stations (densest by self-report), AI-assisted ionosphere modelling. Pricing not on public page; sold paired with CHC X-series rovers and bundled subscriptions. Source: https://www.huace.cn/informationDetail/183 ; https://www.huace.cn/pdDetail/57
- **South GNSS / SOUTH "南方"** — bundled with South receivers; widely used in surveying education and county-level survey teams. No public NTRIP price; reseller channels.
- **ComNav / Unicore** — receiver chipset / OEM; networks tied to enterprise integrators, not retail.

None of the vendor networks publish a hobbyist self-service tier; foreign-individual access not viable.

---

## 5. Government CORS — National & Provincial (licensed only)

### 全国卫星导航定位基准站网 (National CORS) — Ministry of Natural Resources / NGCC

| Field | Value |
|---|---|
| **Operator** | NGCC (National Geomatics Center of China) under Ministry of Natural Resources / 自然资源部 (formerly NASG) |
| **Stations** | 2,700+ |
| **Feeds** | 北斗地基增强系统 (BeiDou Ground-Based Augmentation System / BGAS) |
| **Public NTRIP** | None — licensed CORS access only |
| **Access** | Restricted to organisations holding 测绘资质 (Class A/B/C surveying qualifications) under contract with provincial bureaus |
| **hobbyist_eligibility** | No |
| **legal_residency_required** | N/A — licence-gated, not residency-gated |

### 省级CORS网 (Provincial CORS — all 34 provinces / municipalities / autonomous regions)

- First operational provincial network: **SZCORS Shenzhen** (2003)
- Every province / direct-administered municipality / autonomous region now operates its own
- Some are free for licensed organisations (e.g. SZCORS public-service tier); others charge — example: **Sichuan provincial CORS at CNY 8,000/yr**
- All require organisational credentials + valid 测绘资质
- Not accessible to individuals or foreigners

Pipeline note: tracked in `docs/networks.md` under `bgas_china` (national) and `chinese_provincial_cors` (provincial bundle); both rejected from the public map pipeline as licensed-only.

---

## 6. BeiDou GBAS / SBAS-style augmentation (informational)

China's BeiDou Ground-Based Augmentation System began open services in May 2021 and provides:
- **Wide-area augmentation** — metre to sub-metre, satellite-broadcast (free, no NTRIP) — out of scope for this project (DGNSS-class)
- **Regional real-time augmentation** — dm-level, licensed only
- **Real-time PPP/RTK** — cm-level, commercial subscription via Qianxun / CMCC / Tencent

PPP-B2b (BeiDou-3 satellite-delivered PPP) is free over-the-air for compatible receivers but is satellite SSR, not internet NTRIP — out of project scope alongside QZSS CLAS / Galileo HAS.

---

## Foreign-User Reality

There is **no public, free, or self-service NTRIP path** for non-resident hobbyists in mainland China. Barriers stack:
1. Qianxun, CMCC, Tencent — all require Chinese mobile number + 实名认证 (real-name ID verification with mainland ID card)
2. Provincial / national CORS — require 测绘资质 institutional licensing (closed to individuals regardless of nationality)
3. Vendor networks (CHC, South, etc.) — bundled with hardware sales through Chinese distributors, foreign hobbyist channel undeveloped
4. **GEODNET** (web3 / DePIN community CORS, geodnet.com) has expanding mainland China coverage with international hobbyist access; worth checking on its coverage map for region-specific availability before assuming
5. Setting up a private base station inside China without 测绘资质 violates the Surveying and Mapping Law

In practice, foreign workers and students in mainland China who need RTK use: (a) GEODNET tokens if coverage exists, (b) a friend / employer's Qianxun account, or (c) deploy their own short-baseline base+rover (a single private base for a single user is a legal grey area but tolerated for short-baseline non-published use).

---

## Volunteer Coverage (rtk2go + Centipede + EarthScope)

Live counts from `data/stations.json` (fetched 2026-05-12T18:17Z):

| Source | CHN total | Notes |
|---|---|---|
| **rtk2go** | 3 | `CHENKATE` (22.67°N, 113.91°E — Pearl River Delta / Shenzhen), `Daniel_Bynav` (28.23°N, 112.88°E — Hunan / Changsha), `JinshitanNB` (39.09°N, 122.03°E — Liaoning / Dalian Jinshitan) |
| **Centipede** | 0 | No CHN nodes |
| **EarthScope** | (a few IGS stations: BJFS Beijing, SHAO Shanghai, WUHN Wuhan, URUM Urumqi, CHU1 — research-grade, RINEX-only via NOTA / IGS, not real-time NTRIP) | Not a hobbyist real-time path |

Volunteer real-time coverage in mainland China is effectively absent (3 rtk2go bases for a population of 1.4 billion).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| IGS MGEX (China stations: BJFS, SHAO, WUHN, URUM, etc.) | https://www.igs.org/mgex/ ; https://network.igs.org/ | Free non-commercial |
| EarthScope IGS data archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| iGMAS (国际GNSS监测评估系统) | http://www.igmas.org/ | Free academic |
| CMONOC (Crustal Movement Observation Network of China) | Selected stations via MGEX | Free non-commercial |
| Qianxun RINEX archive | qxwz.com account | Paid subscription |

---

## Gaps & Observations

1. **No free public NTRIP for individuals exists in mainland China.** This is structural — the Surveying and Mapping Law is the binding constraint, not an oversight.
2. **The commercial market is a three-way oligopoly** (Qianxun, CMCC, Tencent) at near-identical pricing (~CNY 3,600/yr ± 30%). Tencent's 2022 CNY 998.88/yr disruption was real but appears to have been retracted; current floor is back to ~CNY 3,000–3,600/yr.
3. **Provincial pricing is heterogeneous** — Sichuan CNY 8,000/yr is one published example; SZCORS has a free public tier; most are quote-only and licence-gated regardless of price.
4. **Foreign-user gap is hard.** Even a Chinese national resident's account cannot legally be transferred. Foreign individuals operating in China should plan for either (a) institutional sponsorship via an employer with 测绘资质, (b) own-base deployment under careful interpretation of the law, or (c) GEODNET / private CORS-share where feasible.
5. **The volunteer network gap is unlikely to close** — both rtk2go and Centipede have minimal Chinese presence and the regulatory environment discourages community deployment of fixed reference stations by individuals.
6. **GEODNET / DePIN networks are the most plausible new free-ish path.** Worth a follow-up dedicated probe in 6–12 months.

---

## Sources Consulted

- Qianxun FindCM product page: https://www.qxwz.com/products/findcm (observed 2026-05-12)
- Qianxun mall (FindCM): https://mall.qxwz.com/market/services/FindCM (observed 2026-05-12)
- Qianxun control console: https://findcm.my.qxwz.com/ (observed 2026-05-12)
- Qianxun NTRIP host/port reference: https://blog.csdn.net/hailiannanhai/article/details/78172313
- Qianxun NTRIP IP/host CSDN Q&A: https://ask.csdn.net/questions/8506233
- xueceliang.cn Qianxun FAQ: https://www.xueceliang.cn/ce/qxwzqxzcfcjwt.html
- CORS Stations profile of Qianxun: https://corsstations.com/networks/china-cors-network-qianxun-spatial-intelligence-gnss-rtk-service/
- ChinAI Substack on Qianxun + BeiDou: https://chinai.substack.com/p/chinai-192-qianxun-beidou-spatiotemporal
- njhq.com Qianxun reseller pricing: http://www.njhq.com.cn/post/1498.html ; http://www.njhq.com.cn/post/552.html
- Leicado Qianxun reseller pricing (CNY 400/mo, 3,600/yr re-confirmed 2026-05-12): https://www.leicado.com/product-detail/BQa9vQxB
- China Mobile CORS / OneNet (CMCC): http://group.bj.chinamobile.com/index/solutionnew/standardproduct/location/ (observed 2026-05-12)
- CMCC reseller pricing reference: https://www.leicado.com/leicadearticle-detail/bElvRQ6W
- Tencent Location Services RTK: https://lbs.qq.com/rtk/ (observed 2026-05-12)
- Tencent NTRIP host/port + mountpoints reference: https://www.sohu.com/a/579386199_120296774 ; https://www.sohu.com/a/580039508_120296774
- Tencent reseller listing: http://www.qxcors.net/product/26.html
- Huace 华测一张网 description: https://www.huace.cn/informationDetail/183 ; https://www.huace.cn/pdDetail/57
- Springer Nature — BDS high-precision services: https://link.springer.com/article/10.1186/s43020-024-00143-8
- ArduSimple China caster review (confirms no national free network): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-china/
- Han Kun Law commentary on intelligent-vehicle survey/mapping security notice: https://hankunlaw.com/portal/article/index/cid/8/id/14389
- curl probes 2026-05-12: `rtk.ntrip.qxwz.com:8001 / :8002 / :8003` and `cors.tencent.com:8001` all returned `SOURCETABLE 200 OK` with full mountpoint dumps
- Local pipeline data: `data/stations.json` (rtk2go CHN = 3, centipede CHN = 0; fetched 2026-05-12T18:17Z)
