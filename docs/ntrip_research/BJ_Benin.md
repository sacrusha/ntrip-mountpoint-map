# Benin [BJ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21

## Status

One public Centipede base in country (`BJDJ`, Djougou). National IGN Bénin CORS network (7 stations) is RTK-NTRIP capable since 2022, free of charge on request, but the caster host:port is **not** publicly published — disclosed only after registration via IGN Bénin / the CatIS citizen portal.

## Caster 1 — Centipede-RTK (community, public)

| Field | Value |
|---|---|
| **landing_url** | https://www.centipede-rtk.org/ |
| **access_url** | https://docs.centipede.fr/ (anonymous; shared credentials `centipede / centipede`) |
| **host:port** | `caster.centipede.fr:2101` (alias `crtk.net:2101`) — mountpoint `BJDJ`, country tag `BEN`, 9.692 N 1.661 E (Djougou) |
| **num_stations** | 1 physical |
| **vrs** | no — single-base; RTCM3 (1004/1005/1008/1012/1020/1033/1042/1046/1077/1087/1097/1127); GPS+GLO+GAL+BDS; receiver u-blox ZED-F9P on RTKBase 2.7.0 |
| **tariff** | free |
| **hobbyist_eligibility** | yes (open community caster) |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-21 — STR row `STR;BJDJ;BEN;RTCM3;…;CentipedeRTK` returned by live probe of `caster.centipede.fr:2101` |
| **datum_epoch** | omitted — Centipede does not publish a per-volunteer-base epoch declaration |

Coverage: Djougou is in central-north Benin. ~5–10 km baseline gives cm RTK locally; useless beyond ~30–50 km. Cotonou / Porto-Novo / Abomey-Calavi (where most population and survey demand sit) are 370–420 km south — out of single-base RTK range.

## Caster 2 — IGN Bénin Permanent GNSS Network (national, restricted-public)

| Field | Value |
|---|---|
| **landing_url** | https://ign.bj/lign/ |
| **access_url** | https://service-public.bj/public/services/service/PS01085 ("Fichier des stations permanentes GNSS"); CatIS information system entry at https://catistest.xroad.bj/systems/IS00004 lists `http://gps.ign.bj/` as the data-download URL |
| **host:port** | not publicly published — disclosed by IGN Bénin to registered users only. CatIS entry IS00004 names `http://gps.ign.bj/` as the data-download URL, but the hostname **does not resolve** (NXDOMAIN, probed 2026-05-22) — either the caster sits behind a different (unpublished) hostname or `gps.ign.bj` is a placeholder. |
| **num_stations** | 7 physical: Cotonou, Abomey, Savalou, Parakou, Natitingou, Nikki, Kandi |
| **vrs** | ? — not stated in any public document |
| **tariff** | free of charge on request from IGN Bénin (per Houessou et al. 2025, AJSET) |
| **hobbyist_eligibility** | ? — network purpose is cadastral / land-rights; no published policy excludes hobbyists, none confirms eligibility |
| **legal_residency_required** | ? — registration path via `service-public.bj` (Beninese citizen portal); non-residents may face onboarding friction, not formally barred |
| **last_confirmed_alive** | 2026-05-21 — `ign.bj/lign/` HTTP 200 (institutional site, no NTRIP page exposed); CatIS entry IS00004 reachable; no caster endpoint to anonymously confirm |
| **datum_epoch** | paper-sourced only — Houessou et al. 2025 AJSET §2.2 describes the IGN Bénin RTK NTRIP service as expressing coordinates in **WGS 84 / ITRF2005, UTM Zone 31N**. This is not an IGN Bénin first-party declaration; `ign.bj`, `service-public.bj` PS01085, and CatIS IS00004 do not name a datum/epoch publicly. Per primer rule, only operator declarations are strictly citable — treat this as a peer-reviewed pointer, not an operator portal citation. Source: https://www.sciencepublishinggroup.com/article/10.11648/j.ajset.20251003.15 |

## Context

- **2022 upgrade**: the 7-station MCA-Bénin / IGN Bénin CORS network (built ~2010 with Millennium Challenge Account Benin funding) was modernised to support RTK NTRIP operation. Houessou et al. 2025 confirm: "Access to this advanced service is available free of charge upon request from the National Geographic Institute of Benin" — but no hostname, port or mountpoint name is published in the paper, on `ign.bj`, on `service-public.bj` PS01085, on the CatIS system page, or in any sourcetable.
- **CatIS**: Benin Cadastral Information System. CatIS entry IS00004 names the IGN as owner of the "Stations CORS GNSS Permanentes" subsystem and points users at `http://gps.ign.bj/`. The hostname does not expose a public NTRIP sourcetable (requires registration).
- **AFREF**: Benin CORS stations were intended to contribute to the African Geodetic Reference Frame; no real-time AFREF NTRIP stream from BJ in BKG or IGS-IP.

## Volunteer / Free Coverage

- Centipede: 1 (BJDJ Djougou). `py scripts/stations_by_country.py BEN` → 1.
- rtk2go: 0 BJ mountpoints (probed 2026-05-21).
- GEODNET / ONOCOY / PointOne: no BJ coverage 2026-05-21.
- Cross-border RTK within ~50 km of major BJ population centres: none. Nigerian, Togolese and Burkinabè borders are all >50 km from a confirmed live RTK base.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| IGS / EarthScope — BJCO (Cotonou), IGN-BJ operated; **currently inactive** per SONEL station page (status flagged "No data for 30 days", colour orange — observed at https://www.sonel.org/?page=gps&idStation=3267 on 2026-05-22) | https://www.earthscope.org/data/gnss-data/ | free non-commercial (NULA account) |
| SONEL GPS — BJCO time series & RINEX (status "No data for 30 days" 2026-05-22) | https://www.sonel.org/?page=gps&idStation=3267 | free |
| IGN Bénin GNSS archive — RINEX from the 7 CORS sites, on request | https://ign.bj/lign/ | unknown |

## Probes (2026-05-21)

- `https://ign.bj/lign/` — HTTP 200, institutional page, no NTRIP info
- `https://catistest.xroad.bj/systems/IS00004` — entry exists, names IGN as owner, points at `http://gps.ign.bj/` for data download
- `gps.ign.bj` DNS lookup — NXDOMAIN (2026-05-22); the CatIS-cited hostname does not resolve, so the entry effectively names no reachable endpoint
- `ign.bj` DNS lookup — resolves to 102.215.93.78; institutional site responds but exposes no NTRIP page
- `https://www.sonel.org/?page=gps&idStation=3267` — BJCO status indicator "No data for 30 days (orange)" observed 2026-05-22
- `http://caster.centipede.fr:2101/` — `STR;BJDJ;BEN;…` confirmed
- `http://rtk2go.com:2101/` — no BEN mountpoints
- `https://www.sciencepublishinggroup.com/article/10.11648/j.ajset.20251003.15` — Houessou et al. AJSET 2025 paper accessible; confirms WGS84/ITRF2005, UTM Zone 31N, free-on-request access

## Sources

- Houessou et al., AJSET 2025 — RTK NTRIP land-rights study in Benin: https://www.sciencepublishinggroup.com/article/10.11648/j.ajset.20251003.15
- Kossougbeto / Kossugbeto, RUDN 2015 — Benin permanent stations analysis (pre-2022 upgrade, no caster details): https://journals.rudn.ru/structural-mechanics/article/view/10965
- IGN Bénin: https://ign.bj/lign/
- Benin Citizen Portal — PS01085 "Fichier des stations permanentes GNSS": https://service-public.bj/public/services/service/PS01085
- CatIS — "Stations CORS GNSS Permanentes" (IS00004, IGN Bénin owner): https://catistest.xroad.bj/systems/IS00004
- Centipede-RTK network + map: https://www.centipede-rtk.org/, https://map.centipede-rtk.org/
- Centipede sourcetable via `caster.centipede.fr:2101` live probe (2026-05-21)
- SONEL GPS COTONOU: https://www.sonel.org/?page=gps&idStation=3267
- IGS network — BJCO00BEN: https://network.igs.org/BJCO00BEN
- NOAA CORS BJCO: https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=BJCO
- Local: `py scripts/stations_by_country.py BEN` → 1 (centipede / BJDJ); `py scripts/stations_by_radius.py 6.37 2.39 200` → 0 within 200 km of Cotonou; `py scripts/stations_by_radius.py 9.69 1.66 200` → BJDJ only
