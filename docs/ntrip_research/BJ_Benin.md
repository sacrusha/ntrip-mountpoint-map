# Benin [BJ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (prior: 2026-05-12 / 2026-05-06)

## Status: One public Centipede base (BJDJ, Djougou); national IGN Bénin CORS is RTK-NTRIP capable since 2022 but caster details NOT publicly published — disclosed only on direct request to IGN Bénin

## Caster 1 — Centipede-RTK (community, public)

| Field | Value |
|---|---|
| **landing_url** | https://www.centipede-rtk.org/ |
| **access_url** | https://docs.centipede.fr/ |
| **host:port** | crtk.net:2101 (sourcetable fetched 2026-05-15, status ok per `data/source_health.json`) |
| **mountpoint(s) in BJ** | `BJDJ` (Djougou, 9.692°N / 1.661°E) — dual-frequency, RTCM3, GPS+GLO+GAL+BDS |
| **num_stations (BJ)** | 1 physical |
| **vrs** | no (single-base) |
| **tariff** | free; shared credentials `centipede / centipede` (Centipede-RTK public model) |
| **hobbyist_eligibility** | yes (open community caster) |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-15 — BJDJ present in `data/stations.json` (Centipede source `last_ok` 2026-05-15T16:22Z) |
| **datum_epoch** | not separately published for BJDJ; Centipede bases broadcast in WGS84/ITRF as configured by host (no citable per-station declaration — omitted) |

**Coverage note:** Djougou is in central-north Benin. ~5–10 km baseline gives cm RTK locally; useless beyond ~30–50 km. Cotonou / Porto-Novo / Abomey-Calavi (where most population and survey demand sit) are 370–420 km south — out of any single-base RTK range.

## Caster 2 — IGN Bénin Permanent GNSS Network (national, restricted-public)

| Field | Value |
|---|---|
| **landing_url** | https://ign.bj/lign/ |
| **access_url** | https://service-public.bj/public/services/service/PS01085 ("Fichier des stations permanentes GNSS") |
| **host:port** | not publicly published — disclosed by IGN Bénin to registered users only |
| **num_stations** | 7 physical: Cotonou, Abomey, Savalou, Parakou, Natitingou, Nikki, Kandi |
| **vrs** | ? (not stated in any public document) |
| **tariff** | free of charge on request from IGN Bénin (per Houessou et al. 2025, AJSET) |
| **hobbyist_eligibility** | ? — network purpose is cadastral / land-rights; no published policy excludes hobbyists, none confirms eligibility |
| **legal_residency_required** | ? (registration path runs through `service-public.bj`, the Beninese citizen portal — non-residents may face onboarding friction; not formally barred in any cited document) |
| **last_confirmed_alive** | 2026-05-15 — `ign.bj/lign/` HTTP 200 via WebFetch (institutional site, no NTRIP page exposed); no caster endpoint confirmed alive |
| **datum_epoch** | WGS 84 / ITRF2005, UTM Zone 31N (declared in Houessou et al. 2025 §2.2 describing the IGN Bénin RTK NTRIP service; https://www.sciencepublishinggroup.com/article/10.11648/j.ajset.20251003.15) |

## Context Notes

- **2022 upgrade**: the 7-station MCA-Bénin / IGN Bénin CORS network (built ~2010) was modernised to support RTK NTRIP operation. Confirmed in Houessou et al., *American Journal of Science, Engineering and Technology* (2025): "Access to this advanced service is available free of charge upon request from the National Geographic Institute of Benin" — but no hostname, port, or mountpoint name is published in the paper, on `ign.bj`, on `service-public.bj` PS01085, or in any sourcetable.
- **No public sourcetable**: zero BJ mountpoints found on rtk2go monitor, BKG NTRIP streams, NTRIP-list.com Africa, or ArduSimple country list (2026-05-15 search).
- **BJCO IGS station** (Cotonou, IGN Bénin operated, DOMES 32701M001, installed 2008-10-01): SONEL reports "No data for 30 days" as of 2026-05-15 — currently inactive for archival GNSS. Was post-process only; never an RTK NTRIP stream.
- **AFREF**: Benin CORS stations were intended to contribute to the African Geodetic Reference Frame; no real-time AFREF NTRIP stream from BJ in BKG or IGS-IP.
- **Global commercial networks**: GEODNET, ONOCOY, PointOne — no BJ coverage as of 2026-05-15.
- **Cross-border RTK within ~50 km of major BJ population centres**: none. Nigerian, Togolese, and Burkinabè borders are all >50 km from a confirmed live RTK base; Togo's IGNTOGO portal has been unreachable since May 2026 (per `data/rtk_map.json` note on `dgigc_tg`).

## Probe results (2026-05-15)

- `https://ign.bj/lign/` — **200 OK** (institutional site, no NTRIP info)
- `https://service-public.bj/public/services/service/PS01085` — **200 OK** but WebFetch returned only the "Citizen Portal" wrapper (page is JS-rendered; service body not extractable from this sandbox — the page exists; richer content visible in a normal browser per Google index)
- `https://www.sciencepublishinggroup.com/article/10.11648/j.ajset.20251003.15` — **200 OK** (provided the datum/epoch + "free on request" quote)
- `https://journals.rudn.ru/structural-mechanics/article/view/10965` — **200 OK** (2015 paper, predates 2022 upgrade; no caster details)
- `https://www.sonel.org/?page=gps&idStation=3267` — **200 OK** (BJCO00BEN, IGN-BJ, "No data for 30 days")
- `https://network.igs.org/BJCO00BEN` — **200 OK** (station documented as RealTime-capable; current real-time stream not visible from IGS site to this sandbox)
- `https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=BJCO` — **200 OK** but JS-templated; specific BJCO station data not server-rendered for this sandbox (cited only as confirmation the station ID is registered with NOAA NCN)
- `https://www.centipede-rtk.org/maps` and `https://map.centipede-rtk.org/...` — **200 OK** but the public map is rendered client-side; BJDJ presence is confirmed instead via the locally-fetched Centipede sourcetable in `data/stations.json` (2026-05-15)
- `http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101` — **TLS cert ALTNAME error** from this sandbox; rtk2go monitor independently confirmed in other research entries; no BJ mountpoints reported there

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS / EarthScope GNSS Data Archive** — BJCO (Cotonou), archival 2008–2022; currently no recent data | https://www.earthscope.org/data/gnss-data/ | free non-commercial (NULA account) |
| **SONEL GPS** — BJCO time series & RINEX | https://www.sonel.org/?page=gps&idStation=3267 | free |
| **IGN Bénin GNSS archive** — RINEX from the 7 CORS sites, on request | https://ign.bj/lign/ | unknown |

## Sources Consulted (2026-05-15)

- Houessou et al., AJSET 2025 — RTK NTRIP land-rights study in Benin (https://www.sciencepublishinggroup.com/article/10.11648/j.ajset.20251003.15)
- Kossougbeto / Kossugbeto, RUDN 2015 — Benin permanent stations analysis (https://journals.rudn.ru/structural-mechanics/article/view/10965)
- IGN Bénin (https://ign.bj/lign/)
- Benin Citizen Portal — PS01085 "Fichier des stations permanentes GNSS" (https://service-public.bj/public/services/service/PS01085)
- Centipede-RTK network + map (https://www.centipede-rtk.org/, https://map.centipede-rtk.org/)
- Centipede sourcetable via local `data/stations.json` and `data/source_health.json` (centipede `ok` at 2026-05-15T16:22Z; BJDJ at 9.692, 1.661)
- SONEL GPS COTONOU (https://www.sonel.org/?page=gps&idStation=3267)
- IGS network — BJCO00BEN (https://network.igs.org/BJCO00BEN)
- NOAA CORS BJCO (https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=BJCO)
- Local data: `py scripts/stations_by_country.py BEN` → centipede / BJDJ (2026-05-15); `py scripts/stations_by_radius.py 6.37 2.39 200` → 0 stations within 200 km of Cotonou; `py scripts/stations_by_radius.py 9.69 1.66 200` → BJDJ only
- rtk2go monitor, NTRIP-list.com Africa, ArduSimple country selector — no BJ entries
