# US Virgin Islands [VI] — NTRIP RTK

## Status
NO territory caster. EarthScope NOTA streams `STVI_RTCM3P3` (St. Thomas) + NPS_CORS streams `VIIS_RTCM3` (St. John, Virgin Islands NP) + IGS-IP streams `CRO100VIR0` (St. Croix). NOAA NCN holds 4 USVI CORS (RINEX only). No VRS.

## Caster 1: EarthScope NOTA — STVI (St. Thomas)

| Field | Value |
|---|---|
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://data.earthscope.org/ (NULA acceptance) |
| host:port | `ntrip.earthscope.org:2101` (RTCM 3.3); `:2105` BINEX; `:2108` PPP onboard (GGK/GSOF) |
| Mountpoint | `STVI_RTCM3P3` — 18.34N, -64.97W. Trimble NETR9. RTCM 3.3 MSM7 (GPS+GLO+BDS+GAL+SBAS+QZS), 1 Hz, single-base. |
| num_stations | 1 (STVI). |
| vrs | no |
| tariff | Free non-commercial (NULA acceptance, annual renewal). Commercial USD 1,000/seat/yr (min 5 seats direct billing). 5-seat × 2-week trial available. |
| hobbyist_eligibility | yes (NULA personal use). |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-21 — NOTA realtime page WebFetch 200 (verbatim "All raw data streams use the ITRF2014 reference frame. For NOTA stations, the epoch date is 2026-03-30"). Last TCP probe 2026-05-12 had `STVI_RTCM3P3` line present (TRIMBLE NETR9, USA, 18.34/-64.97). |
| datum_epoch | ITRF2014 @ 2026-03-30 — cited via operator page https://www.earthscope.org/data/gnss-realtime/ ("For NOTA stations, the epoch date is 2026-03-30"). |

## Caster 2: NPS_CORS — VIIS (St. John, Virgin Islands NP)

| Field | Value |
|---|---|
| landing_url | https://www.nps.gov/aboutus/gpsapp.htm (NPS GPS app/CORS service overview) |
| access_url | (project sourcetable cache; NPS CORS ingested-global within project) |
| host:port | NPS CORS caster (ingested via project pipeline; do not direct-probe per primer) |
| Mountpoint | `VIIS_RTCM3` — 18.34N, -64.79W (St. John, Virgin Islands National Park), ~19 km E of STVI. |
| num_stations | 1 (VIIS). |
| vrs | no |
| tariff | Free (NPS public service) |
| hobbyist_eligibility | yes |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-21 — `stations_by_radius.py 18.34 -64.97 200` lists `VIIS_RTCM3` on nps_cors at 19 km. |
| datum_epoch | omitted — no operator declaration on accessible NPS pages |

## Caster 3: IGS-IP — CRO100VIR0 (St. Croix, single-base)

| Field | Value |
|---|---|
| landing_url | https://network.igs.org/CRO100VIR |
| access_url | https://register.rtcm-ntrip.org/cgi-bin/registration.cgi (BKG IGS-IP) |
| host:port | www.igs-ip.net:2101 (ingested-global) |
| Mountpoint | `CRO100VIR0` — Christiansted, St. Croix, 17.76N, -64.58W. RTCM3 1 Hz raw, single-base. |
| num_stations | 1 (CRO1). |
| vrs | no |
| tariff | Free; BKG IGS-IP registration |
| hobbyist_eligibility | yes |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-21 — `stations_by_country.py VIR` → 1 station (CRO100VIR0 on igs_ip). |
| datum_epoch | omitted — IGS network page does not formally declare frame/epoch for CRO1 coordinates |

## Other USVI GNSS infra (not real-time NTRIP)

- NOAA NCN CORS in VQ state code: STVI (UNAVPS), VITH (NGSSTA), CRO1 St. Croix VLBA (JPL), VIKH Kingshill (NGSSTA). RINEX only; no NOAA public caster confirmed.
- PRSN/UPRM: ~18 GNSS stations across PR+USVI+BVI (operator page https://redsismica.uprm.edu/english/our_work/instrumentation.php). No NTRIP service, public hostname, or access policy published on operator page; status of any internal stream unknown.

## Coverage in project sources

`stations_by_radius.py 18.34 -64.97 200` (2026-05-21): 9 stations total — earthscope 6 [USA:3, AIA:1, PRI:1, VGB:1], nps_cors 2 [USA:2], igs_ip 1 [VIR:1]. Detail:
- earthscope: STVI_RTCM3P3 [USA] @ 0 km, CUPR_RTCM3P3 [USA, PR] @ 33 km, CN03_RTCM3P3 [VGB] @ 62 km, CN58_RTCM3P3 [AIA] @ 165 km, P780_RTCM3P3 [PRI] @ 173 km, AOPR_RTCM3P3 [USA] @ 188 km.
- nps_cors: VIIS_RTCM3 [USA] @ 19 km (St. John, Virgin Islands NP), SAJU_RTCM3 [USA, PR] @ 122 km.
- igs_ip: CRO100VIR0 [VIR] @ 76 km (St. Croix).

Baseline accuracy guidance: ZED-F9P + survey antenna ~7mm + 1ppm. CRO1 from St. Thomas at 76 km = theoretical ~83 mm; practice typically worse; sub-decimetre at best, no cm-fix at that range. Useful for sub-metre / decimetre work only. Zero VI volunteer (rtk2go/centipede) bases.

## Post-processing (RINEX)

- NOAA NCN: STVI, VITH, CRO1, VIKH — free. https://geodesy.noaa.gov/CORS/
- EarthScope/GAGE: STVI via PRGPS DOI 10.7283/T5VD6WTH — free non-commercial.

## Sources
- EarthScope NOTA realtime: https://www.earthscope.org/data/gnss-realtime/ (ITRF2014 @ 2026-03-30; ports 2101/2105/2108; commercial $1,000/seat/yr, 5-seat min for direct billing, 5-seat 2-week trial)
- Commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- NOTA overview: https://www.earthscope.org/nota/
- STVI DOI: 10.7283/T5VD6WTH
- NOAA NCN station list (VQ): https://geodesy.noaa.gov/CORS/sort_sites.shtml
- PRSN/UPRM instrumentation: https://redsismica.uprm.edu/english/our_work/instrumentation.php
- IGS CRO1 page: https://network.igs.org/CRO100VIR
- NPS GNSS overview: https://www.nps.gov/aboutus/gpsapp.htm
