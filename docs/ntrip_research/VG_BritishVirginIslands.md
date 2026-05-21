# British Virgin Islands [VG] — NTRIP RTK

## Status
NO national caster. EarthScope NOTA `CN03_RTCM3P3` on Tortola = only realtime stream. No VRS. UK Overseas Territory; BVI not in OS Net (OS Net covers Great Britain only — https://www.ordnancesurvey.co.uk/geodesy-positioning/os-net).

## EarthScope NOTA — CN03 (Tortola)

| Field | Value |
|---|---|
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://data.earthscope.org/ (NULA acceptance) |
| host:port | `ntrip.earthscope.org:2101` (RTCM 3.3); `:2105` BINEX; `:2108` PPP onboard (GGK/GSOF) |
| Mountpoint | `CN03_RTCM3P3` — 18.49N, -64.40W. Septentrio POLARX5. RTCM 3.3 MSM7 (GPS+GLO+BDS+GAL+SBAS+QZS), 1 Hz, single-base. |
| num_stations | 1 (CN03). |
| vrs | no |
| tariff | Free non-commercial (NULA, annual renewal). Commercial USD 1,000/seat/yr (min 5 seats direct billing). EarthScope = US 501(c)(3); no VAT. |
| hobbyist_eligibility | yes (NULA personal use). |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-21 — NOTA realtime page WebFetch 200 (ITRF2014 @ 2026-03-30 verbatim). Last TCP probe 2026-05-12 had `CN03_RTCM3P3` line present (SEPT POLARX5, VGB, 18.49/-64.40). `stations_by_country.py VGB` → 1 station (CN03 on earthscope). |
| datum_epoch | ITRF2014 @ 2026-03-30 — cited via operator page https://www.earthscope.org/data/gnss-realtime/. |

## Coverage notes

CN03 on Tortola. Single-base RTK reliable ~20-30 km. Anegada (60 km N) = outer limit / beyond. Legacy UNAVCO caster `rtgpsout.unavco.org` retired 2025-07-29 — all NOTA traffic on `ntrip.earthscope.org`.

`stations_by_radius.py 18.49 -64.40 200` (2026-05-21): 15 stations total — agrs_nl 5 [BES:5], earthscope 5 [AIA:2, USA:2, VGB:1], igs_ip 3 [BES:2, VIR:1], nps_cors 2 [USA:2]. Detail:
- earthscope: CN03 @ 0 km, STVI_RTCM3P3 [USA] @ 62 km, CUPR_RTCM3P3 [USA, PR] @ 95 km, CN58/CN59 [AIA] @ 103-146 km.
- igs_ip: CRO100VIR0 [VIR, St. Croix] @ 83 km — RTCM3 1 Hz, BKG-creds alternative to NOTA.
- agrs_nl (Netherlands AGRS): 5 BES (Caribbean Netherlands) stations on Saba/St. Eustatius/Bonaire. Tortola → Saba straight-line is 172 km (Saba is the closest BES island); other agrs_nl stations farther still. All require AGRS-NL auth and are beyond useful single-base RTK range from Tortola.

## National authority

BVI Land and Survey Dept (`bvi.gov.vg/departments/land-and-survey-department`) maintains National Geodetic Framework. No NTRIP, no CORS endpoint, no announced realtime correction service. No FCDO geospatial aid programme for BVI found.

## No project announcement

Only realtime GNSS asset is legacy COCONet (now NOTA) CN03. No dedicated BVI national NTRIP plan.

## Post-processing (RINEX)

EarthScope GNSS Data Archive (CN03 RINEX) — free non-commercial; USD 1,000/seat/yr commercial. https://www.earthscope.org/data/gnss-data/

## Sources
- https://www.earthscope.org/data/gnss-realtime/ (ITRF2014 @ 2026-03-30; ports 2101/2105/2108; $1,000/seat/yr commercial, 5-seat min, 5-seat 2-week trial)
- https://www.earthscope.org/nota/
- Commercial licence: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- Platform transition: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- BVI L&S Dept: https://www.bvi.gov.vg/departments/land-and-survey-department
- OS Net (GB-only coverage scope): https://www.ordnancesurvey.co.uk/geodesy-positioning/os-net
- Tortola → Saba distance (172 km): https://www.distancefromto.net/between/Tortola/Saba
- rtk2go / Centipede: no VG entries.
- NTRIP-list.com: no VG entry.
