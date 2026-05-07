# Japan [JP] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07

## Status: YES — multiple free public NTRIP RTK casters: MIRAI (Cabinet Office SPAC, free, registration required, 16 JP stations + ~300 worldwide partners, single-base raw observations), GeoRTK (Geosense, free, ~500+ JP volunteer/private mountpoints), GEONET (post-processing only, no public NTRIP). Commercial alternatives: SoftBank ichimill, Nippon GPS Data Service. QZSS CLAS available via L6 satellite for hardware-supporting receivers.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — multiple free + multiple commercial |
| **Network 1 — name** | MIRAI / Go!GNSS |
| **Operator — MIRAI** | Cabinet Office (内閣府), National Space Policy Secretariat / SPAC (Satellite Positioning Research and Application Center); launched 2022-04-01 |
| **host:port — MIRAI** | `ntrip.go.gnss.go.jp:2101` (plain TCP) · `ntrip.go.gnss.go.jp:443` (TLS) — confirmed live 2026-05-07: `SOURCETABLE` returned 324 STR rows with 16 Japan-located physical stations and ~300 worldwide partner stations (Australia 176, NZ 55, USA 11, Canada 11, Antarctica 5, Argentina 4, French Polynesia 3, etc.) |
| **VRS — MIRAI** | No — single-base raw observations only (rover computes RTK baseline). RTCM 3.2 with MSM 1077/1087/1097/1117/1127 + ephemeris 1019/1020/1042/1044/1045/1046; many constellations (GPS+GLO+GAL+BDS+QZS) on most stations |
| **tariff — MIRAI** | Free of charge ("real-time/archived data from monitoring stations connected to MIRAI are available free of charge" — qzss.go.jp 2022-04-01 launch notice) |
| **hobbyist_eligibility — MIRAI** | Yes — disclaimer text reads *"The MIRAI data are shared openly for the benefit of all scientific, educational, and commercial users for peaceful purposes only."* No nationality / hobbyist / commercial distinction. Account is `Go!GNSS account → NtripCaster authorization` (separate two-step) |
| **legal_residency_required — MIRAI** | No — Go!GNSS Terms of Use make no nationality or residency restriction; the disclaimer simply requires "peaceful purposes" and attribution. Account email-verified within 24 h, NtripCaster authorization application within 24 h |
| **MIRAI account validity** | Accounts expire after 365 days inactivity (per existing networks.md note); attribution required: *"Source: GO!GNSS GO!JAPAN website (URL)"* etc. |
| **last_confirmed_alive — MIRAI** | 2026-05-07 — `ntrip.go.gnss.go.jp:2101` returned `SOURCETABLE` with 324 streams; site `go.gnss.go.jp` reachable; sign-up and authorization pages active |
| **Network 2 — name** | GeoRTK |
| **Operator — GeoRTK** | 株式会社ジオセンス (Geosense Co., Ltd.), Kobe |
| **host:port — GeoRTK** | `geortk.jp:2101` — confirmed live 2026-05-07: `SOURCETABLE 200 OK`, ~69 STR rows visible directly; `https://geortk.jp/mountpoint` page shows ~500+ registered mountpoints across Japan + 1 in Thailand (last-updated stamp `2026年5月7日21:59`) |
| **VRS — GeoRTK** | No — individual base-station streams; nearest selection by user |
| **tariff — GeoRTK** | Free — *"利用料は当面無料ですが、有料になる場合は１年以上前にご連絡します"* ("usage is free for the time being; if a fee is introduced we will notify users at least 1 year in advance"). No payment infrastructure on the site |
| **hobbyist_eligibility — GeoRTK** | Yes — open access; registration is required only for **operators of reference stations** (uploading), not for **rover users** (downloading). Mountpoint list at `geortk.jp/mountpoint` is publicly accessible without auth |
| **legal_residency_required — GeoRTK** | No formal residency requirement for download; the operator restricts new *reference station* registrations to physical stations within Japan |
| **last_confirmed_alive — GeoRTK** | 2026-05-07 — `geortk.jp:2101` `SOURCETABLE 200 OK`; mountpoint list timestamped 2026-05-07 21:59 JST |
| **Network 3 — GEONET (post-processing)** | GSI (Geospatial Information Authority of Japan) — ~1,300 stations at ~20 km spacing. **No public NTRIP caster**; raw 1-second / 30-second RINEX is open via `terras.gsi.go.jp` (registration required). Real-time GEONET data is *internally* relayed to MIRAI and to licensed private operators. |

## QZSS CLAS — Free Satellite-Broadcast Alternative (out of scope but relevant)

Japan operates QZSS (Quasi-Zenith Satellite System, "Michibiki"), broadcasting free centimeter-level corrections via the L6 band:
- **CLAS** (Centimeter Level Augmentation Service): 1–6 cm accuracy throughout Japan; free; no internet/SIM required; needs CLAS-capable receiver (u-blox NEO-D9C, Septentrio mosaic-X5, dedicated CLAS receivers).
- **MADOCA-PPP**: decimeter-level globally; free; powered partly by MIRAI ground segment.
- Note: CLAS is satellite PPP-RTK, not NTRIP. It is a strong alternative for users with compatible hardware and is **listed for completeness** — primary research scope is NTRIP.

## Commercial / Paid Network RTK (informational)

| Provider | Endpoint | Tariff | Notes |
|---|---|---|---|
| **SoftBank ichimill** | issued post-registration | ¥39,600/yr per device, tax incl. (~$257/yr) — over the $200/yr cutoff | ~3,300+ proprietary base stations + QZSS augmentation; primarily corporate/drone customers; foreign individuals face friction (Japanese corporate registration usually required) |
| **Nippon GPS Data Service** | `ntrip.gpsdata.co.jp:2101` | tiered FREE/DAY/MINUTE/YEAR plans + ¥5,500 plan-change fee; per-tier rates not on public page | Long-running commercial provider using GEONET data since 2002 |
| **Other commercial** | various | various | Equipment-vendor and surveying-company casters; e.g. Topcon TOPNET-V relays. Not catalogued here |

## Mountpoint Sample — MIRAI (Japan-located, 2026-05-07 sourcetable)

| Mountpoint | Location | Receiver |
|---|---|---|
| `AIRA00JPN` | Aira (Kagoshima) | TRIMBLE |
| `CCJ200JPN` | Ogasawara | TRIMBLE |
| `CHNN00JPN` | Nanjo (Okinawa) | TRIMBLE |
| `GMSD00JPN` | Tanegashima | Trimble |
| `HACH00JPN` | Hachijō Island | TOPCON |
| `ISHI00JPN` | Ishioka (Ibaraki) | TRIMBLE |
| `JCH300JPN` | Ogasawara (separate stream) | Trimble |
| `MIZU00JPN` | Mizusawa (Iwate) | euronet |
| `MSSA00JPN` | Saku (Nagano) | Trimble |
| `QKBP00JPN` | Kobe | JAVAD TRE_3 |
| `QMYP00JPN` | Miyakojima (Okinawa) | JAVAD TRE_3 |
| `QSPP00JPN` | Sapporo | JAVAD TRE_3 |
| `STK200JPN` | Shintotsukawa (Hokkaidō) | TRIMBLE |
| `TKSC00JPN` | Tsukuba | Trimble |
| `TSK200JPN` | Tsukuba (alternate stream) | TRIMBLE |
| `QAKP00USA` | (US Alaska, listed under USA mount stem but coords -149.98) | JAVAD TRE_3 |

(Plus ~300 worldwide partner stations: Australia 176, NZ 55, USA 11, Canada 11, etc.)

## Context Notes

- **MIRAI is the de-facto "free national NTRIP RTK caster" for Japan** for users who can compute RTK at the rover (most modern rovers do). Its 16 Japanese stations are sparse compared with the ~1,300-station GEONET, but each station provides full multi-constellation MSM observations and is enough for single-base RTK at typical baselines (<50 km).
- **GeoRTK is the practical hobbyist option for nationwide single-base coverage** — ~500+ mountpoints distributed across Japan including dense Hokkaidō (Obihiro, Sapporo, Naganuma, Embetsu, Asahikawa) and Honshū regional bases (Yokohama, Niigata, Okayama, Miyazaki, Kyushu/Fukuoka, Shimane). Coverage is operator-volunteered (farmers, researchers, hobbyists), so quality varies by station; sourcetable shows many at lat/lon `0,0` (uncalibrated) and most with `nmea=0,solution=0`. Pipeline currently fetches GeoRTK with `nmea_filter=False, solution_filter=False` per existing networks.md note.
- **GEONET real-time has no public NTRIP**: GSI exposes 30-second RINEX (free, registration) and 1-second RINEX (limited research access via MIRAI archive); real-time NTRIP is licensed only to the private sector. This is the primary historical reason commercial casters dominate.
- **QZSS CLAS satellite-broadcast** fills the "free real-time RTK" niche for hardware that supports L6, complementing MIRAI/GeoRTK NTRIP.
- **Pipeline coverage** (stations.json 2026-05-06 fetch): JP = 43 GeoRTK + 22 rtk2go + 16 MIRAI + 6 AUSCORS = 87 unique JP entries. The MIRAI pipeline count (16) matches the JPN-tagged station count visible in the live sourcetable today.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GSI GEONET 30-sec RINEX (terras)** | https://terras.gsi.go.jp/ | Free (registration required) |
| **MIRAI archive (RINEX)** | https://go.gnss.go.jp/mirai/realtime/ (and archive section) | Free (Go!GNSS account) |
| **IGS / EarthScope partner stations** | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted

- MIRAI service page: https://go.gnss.go.jp/mirai/realtime/ (host/port confirmed 2026-05-07)
- Go!GNSS authorization (NtripCaster account): https://go.gnss.go.jp/authorization/
- Go!GNSS Terms of Use: https://go.gnss.go.jp/terms/ (attribution clause)
- MIRAI Disclaimer: https://go.gnss.go.jp/terms/disclaimer.html (peaceful-purposes clause: *"shared openly for the benefit of all scientific, educational, and commercial users for peaceful purposes only"*)
- MIRAI launch announcement: https://qzss.go.jp/en/overview/notices/mirai_220401.html (launched 2022-04-01, free of charge)
- Live MIRAI sourcetable: `curl http://ntrip.go.gnss.go.jp:2101/` → 324 STR rows, 16 JPN, ~300 worldwide partner (2026-05-07)
- GeoRTK home: https://geortk.jp (Japanese, EULA at /eula)
- GeoRTK mountpoint list: https://geortk.jp/mountpoint (~500+ mountpoints, 2026-05-07)
- Geosense corporate: https://www.geosense.co.jp/ (Kobe-based; news_ntripcaster_open announces caster launch)
- Live GeoRTK sourcetable: `curl http://geortk.jp:2101/` → `SOURCETABLE 200 OK`, 69 STR rows visible directly (2026-05-07)
- GSI GEONET overview: https://www.gsi.go.jp/ENGLISH/geonet_english.html
- GSI terras.gsi.go.jp data portal: https://terras.gsi.go.jp/
- Nippon GPS Data Service: https://www.gpsdata.co.jp/ ; pricing: https://www.gpsdata.co.jp/pricing_plan/
- SoftBank ichimill: https://www.softbank.jp/biz/services/analytics/ichimill/ (¥39,600/yr per device, tax incl., 2025 schedule via sekido-rc.com)
- ArduSimple Japan: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-japan/
- NTRIP-list Asia: https://ntrip-list.com/asia/
- Existing networks.md `mirai` entry (~325 stations, NULA-style auth, 365-day inactivity expiry)
- Existing networks.md `geortk` entry (`nmea_filter=False, solution_filter=False`, ~41 stations historic — now expanded to ~500+ per current site stamp)
- Stations.json 2026-05-06 fetch: JP = 43 geortk + 22 rtk2go + 16 mirai + 6 auscors entries
