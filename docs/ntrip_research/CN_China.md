# China [CN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO free public NTRIP; dominant commercial operator is Qianxun (千寻位置); 34 provincial/municipal CORS networks require licensed access; foreign access effectively blocked by registration requirements

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (free/open); Yes (commercial subscription) |
| **Note** | Hong Kong (HK) has its own separate free service — SatRef — see `HK_HongKong.md` |

---

### Qianxun Sensing Network (千寻位置 / 千寻知寸 FindCM) — Dominant Commercial Operator

| Field | Value |
|---|---|
| **Operator** | Qianxun Sensing Network Co., Ltd. (千寻位置网络有限公司) — Alibaba + SASAC joint venture |
| **Service name** | FindCM (千寻知寸) — centimetre-level RTK; FindMSM — sub-metre SSR |
| **host:port** | `rtk.ntrip.qxwz.com:8001` (ITRF2008) · `:8002` (WGS84) · `:8003` (CGCS2000) |
| **Mountpoints** | `AUTO` (4-constellation 13-frequency: GPS+GLO+BDS+GAL) · `RTCM32_GGB` (legacy 3-constellation 8-frequency) |
| **VRS** | Yes — nationwide VRS computed from 2,000+ reference stations |
| **Stations** | 2,000+ across mainland China |
| **Constellations** | GPS, GLONASS, BeiDou, Galileo, (QZSS for 5-star tier) |
| **tariff — subscription** | Trial: 5-hour free trial available via Qianxun trial centre; paid plans: approx. CNY 400/month (individual survey account, from third-party reseller listings 2024) or CNY 3,600/year; enterprise pricing varies |
| **tariff — SSR/PPP tier** | CNY 8,000–12,000/year (FastFind SSR service, Asia-Pacific coverage) |
| **hobbyist_eligibility** | Technically yes for Chinese nationals — but real-name registration (Chinese phone number + national ID) required; foreign individuals face practical barriers |
| **legal_residency_required** | Yes in practice — Chinese mobile phone number required for account registration; Chinese national identity verification (实名认证) mandatory |
| **last_confirmed_alive** | Qianxun commercial service active as of 2026-05-06 (website HTTP 200; qxwz.com) |

---

### National CORS Network (全国CORS / NGCC)

| Field | Value |
|---|---|
| **Operator** | NGCC (National Geomatics Center of China / 国家地理信息资源目录服务系统) + provincial survey bureaus |
| **Coverage** | 34 provincial/municipal CORS networks; ~2,800+ stations nationwide |
| **Access** | Licensed access only — restricted to licensed surveying enterprises under contract with provincial survey bureaus; not accessible to individuals or foreign entities |
| **host:port** | Not published publicly |

---

### BDS Ground-Based Augmentation System (GBAS / 地基增强系统)

China's BeiDou GAS (Ground Augmentation System) began open services in May 2021, providing:
- Wide-area augmentation: metre to sub-metre accuracy (free, broadcast)
- Regional real-time augmentation: dm-level accuracy (licensed)
- Real-time PPP/RTK: cm-level (commercial subscription via Qianxun or CMCC)

China Mobile (CMCC) also operates an RTK correction service for commercial clients.

---

## Registration Reality for Foreign Users

No public, free, or self-service NTRIP access path exists for foreign hobbyists in mainland China. Barriers:
1. Qianxun FindCM requires Chinese phone number and real-name ID verification
2. Provincial CORS networks require licensed surveying enterprise contracts
3. The national CORS network is not publicly accessible
4. Western CORS commercial services (PointPerfect, GEODNET) offer partial mainland China coverage as alternatives

GEODNET (web3-based community CORS) has expanding China coverage with some international hobbyist access — worth checking if operating in China.

## Volunteer Coverage (rtk2go)

A small number of CHN-coded rtk2go volunteer bases exist, concentrated around major cities. No Centipede CHN presence.

## Hong Kong Note

Hong Kong (HK) operates a separate and independent free NTRIP service — SatRef (Survey and Mapping Office, CEDD). It is covered in a dedicated file `HK_HongKong.md` and is not part of this CN entry.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **CMONOC / iGMAS** — selected China CORS RINEX (scientific) | https://www.igs.org/mgex/ (IGS MGEX stations in China) | Free non-commercial |
| **EarthScope** — IGS stations CHU1/WUHN/SHAO/BJFS/URUM | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **Qianxun RINEX** | Via qxwz.com account | Paid subscription |

## Sources Consulted
- Qianxun official site: https://www.qxwz.com/product-service-findcm.html (observed 2026-05-06)
- Qianxun control console: https://findcm.my.qxwz.com/ (observed 2026-05-06)
- CSDN Qianxun NTRIP config guide (host/port details): https://blog.csdn.net/hailiannanhai/article/details/78172313 (observed 2026-05-06)
- xueceliang.cn Qianxun FAQ: https://www.xueceliang.cn/ce/qxwzqxzcfcjwt.html (observed 2026-05-06)
- njhq.com third-party reseller pricing (CNY 400/month / 3,600/year): http://www.njhq.com.cn/post/1498.html (observed 2026-05-06)
- CORS Stations profile on China CORS: https://corsstations.com/networks/china-cors-network-qianxun-spatial-intelligence-gnss-rtk-service/ (observed 2026-05-06)
- ChinAI Substack on Qianxun+BeiDou: https://chinai.substack.com/p/chinai-192-qianxun-beidou-spatiotemporal (observed 2026-05-06)
- Springer Nature — BDS high-precision services: https://link.springer.com/article/10.1186/s43020-024-00143-8 (observed 2026-05-06)
- ArduSimple China caster list (confirms no national free network): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-china/ (observed 2026-05-06)
