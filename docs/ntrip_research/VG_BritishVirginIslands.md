# British Virgin Islands [VG] — NTRIP RTK
**Date:** 2026-05-17 (delta vs 2026-05-13: NOTA realtime page declares `ITRF2014 @ 2026-03-30` — datum_epoch now citable; project-source probe surfaces IGS-IP `CRO100VIR0` (USVI, St. Croix) @ 83 km — secondary BKG-creds option for southern BVI work).

## Status
NO national caster. EarthScope NOTA `CN03_RTCM3P3` on Tortola = only realtime stream. No VRS. UK Overseas Territory; BVI not in OS Net.

## EarthScope NOTA — CN03 (Tortola)

| Field | Value |
|---|---|
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://data.earthscope.org/ (NULA acceptance) |
| host:port | `ntrip.earthscope.org:2101` (RTCM 3.3); :2105 BINEX; :2108 PPP |
| Mountpoint | `CN03_RTCM3P3` — 18.49N, -64.40W. Septentrio POLARX5. RTCM 3.3 MSM7 (GPS+GLO+BDS+GAL+SBAS+QZS), 1 Hz, single-base. |
| num_stations | 1 (CN03). |
| vrs | no |
| tariff | Free non-commercial (NULA, annual renewal). Commercial USD 1,000/seat/yr (min 5 seats direct billing). EarthScope = US 501(c)(3); no VAT. |
| hobbyist_eligibility | yes (NULA personal use). |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-12 — TCP probe `ntrip.earthscope.org:2101` returned `CN03_RTCM3P3` (SEPT POLARX5, VGB, 18.49/-64.40). NOTA realtime page HTTP 200 2026-05-17. |
| datum_epoch | ITRF2014 @ 2026-03-30 — cited via operator page https://www.earthscope.org/data/gnss-realtime/. |

## Coverage notes

CN03 on Tortola. Single-base RTK reliable ~20-30 km. Anegada (60 km N) = outer limit / beyond. Legacy UNAVCO caster `rtgpsout.unavco.org` retired 2025-07-29 — all NOTA traffic on `ntrip.earthscope.org`.

`stations_by_radius.py 18.49 -64.40 200` (2026-05-17):
- earthscope: CN03 @ 0 km, STVI_RTCM3P3 [USA] @ 62 km, CUPR_RTCM3P3 [USA, PR] @ 95 km, CN58/CN59 [AIA] @ 103-146 km.
- igs_ip: CRO100VIR0 [VIR, St. Croix] @ 83 km — RTCM3 1 Hz, BKG-creds alternative to NOTA.

## National authority

BVI Land and Survey Dept (`bvi.gov.vg/departments/land-and-survey-department`) maintains National Geodetic Framework. No NTRIP, no CORS endpoint, no announced realtime correction service. No FCDO geospatial aid programme for BVI found.

## No project announcement

Only realtime GNSS asset is legacy COCONet (now NOTA) CN03. No dedicated BVI national NTRIP plan.

## Post-processing (RINEX)

EarthScope GNSS Data Archive (CN03 RINEX) — free non-commercial; USD 1,000/seat/yr commercial. https://www.earthscope.org/data/gnss-data/

## Sources
- https://www.earthscope.org/data/gnss-realtime/ (2026-05-17: 200; ITRF2014 @ 2026-03-30)
- https://www.earthscope.org/nota/
- Commercial licence: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- Platform transition: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- BVI L&S Dept: https://www.bvi.gov.vg/departments/land-and-survey-department
- TCP probe 2026-05-12: CN03_RTCM3P3 present.
- `stations_by_radius.py 18.49 -64.40 200` 2026-05-17 (CN03, STVI, CUPR, CN58, CN59, CRO1 visible).
- rtk2go / Centipede: no VG entries.
- NTRIP-list.com: no VG entry.
