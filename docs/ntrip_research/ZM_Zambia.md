# Zambia [ZM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verification of 2026-05-16 baseline)

## Status: NO public NTRIP RTK caster. IGS station ZAMB (Lusaka) streams via BKG IGS-IP — single-base 1 Hz raw, not a Zambia-operated service.

## Caster 1: IGS-IP ZAMB (BKG, global ingested)

| Field | Value |
|---|---|
| landing_url | https://network.igs.org/ZAMB00ZMB |
| access_url | https://register.rtcm-ntrip.org/cgi-bin/registration.cgi (BKG IGS-IP account) |
| host:port | www.igs-ip.net:2101 (ingested-global, do not direct-probe per primer) |
| tariff | free; BKG IGS-IP registration |
| num_stations | 1 (`ZAMB00ZMB0`, Lusaka, -15.43, 28.31) |
| vrs | no — single-base raw 1 Hz |
| hobbyist_eligibility | yes (free BKG account) |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-17 — `py scripts/stations_by_country.py ZMB` shows ZAMB00ZMB0 on igs_ip (-15.43 / 28.31, Lusaka); 1 station total |
| datum_epoch | omitted — no citable declaration on IGS network page for ZAMB frame/epoch |

Note: ZAMB is an IGS observation stream broadcast via BKG IGS-IP. Single physical station; RTK utility = single-base only, baseline-limited. Not a Zambia-administered network. Not counted as a national caster.

## Caster 2: National Zambia NTRIP

None. No NTRIP service launch or CORS expansion announcement found for Zambia 2026-05-17. Zambia Survey Department (ZSD, Ministry of Lands and Natural Resources) participates in AFREF/SAFREF geodetic framework. Repeat WebSearch ("Zambia Survey Department CORS NTRIP RTK 2026") 2026-05-17 → only generic global NTRIP results, no ZM-specific announcement.

## Volunteer / Global Coverage

- rtk2go: zero ZM mountpoints (ingested).
- Centipede: zero ZM.
- EarthScope NOTA: zero ZM.
- EUREF-IP: zero ZM (outside Europe scope).
- `py scripts/stations_by_country.py ZM` 2026-05-16: `No stations for 'ZM'` — code not tagged because helper uses 3-letter country codes; cross-check via `py scripts/stations_by_radius.py -15.41 28.28 200` → ZAMB00ZMB0 on igs_ip at ~0 km from Lusaka.

## Context

- National authority: Zambia Survey Department (ZSD), Ministry of Lands and Natural Resources. University of Zambia Surveying Dept (UNZA) collaborated with ZSD + HartRAO on geodetic infrastructure.
- ZAMB IGS station: hosted at ZSD Lusaka under HartRAO Space Geodesy Programme (SARAO, ZA). Streams via BKG IGS-IP; daily RINEX to HartRAO data centre + RCMRD AFREF archive.
- SAFREF scope: ZM with BW, LS, MW, NA, ZA, SZ, ZW. SAFREF = reference-frame realisation, no NTRIP service.
- AFREF: ZM among ~22 countries with ≥1 operational CORS contributing to AFREF ODC (RINEX archive, not RTK streaming).
- Commercial NTRIP networks (GEODNET, ONOCOY, PointOne, HxGN SmartNet): zero ZM coverage.
- Regional: ZW has ZINGSA CORS (gated, contact-only); TZ has partially functional TanRef (endpoint unconfirmed). No cross-border RTK reach into ZM.
- Practical hobbyist path: local base for single-base RTK; ZAMB via IGS-IP for one Lusaka-centric option; EarthScope/IGS RINEX for post-processing.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| ZAMB RINEX — HartRAO data centre | https://geodesy.hartrao.ac.za/site/en/data-and-products/gnss.html | free (account/request) |
| RCMRD AFREF archive | https://www.rcmrd.org/ | unknown; contact RCMRD |
| IGS data archive (incl. ZAMB) | https://www.earthscope.org/data/gnss-data/ | free non-commercial (NULA) |

## Sources
- IGS ZAMB station page: https://network.igs.org/ZAMB00ZMB
- HartRAO IGS stations: http://www.hartrao.ac.za/geodesy/THEIGSST.htm
- HartRAO GNSS data centre: https://geodesy.hartrao.ac.za/site/en/data-and-products/gnss.html
- AFREF map (GIM Intl): https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- AFREF Newsletter No. 6 (RCMRD): https://rcmrd.org/images/AFREF-Newslettes/6-AFREF-Newsletter-No.-6A.pdf
- UN-SPIDER AFREF: https://un-spider.org/space-application/space-application-matrix/african-geodetic-reference-frame-afref
- ntrip-list.com Africa: https://ntrip-list.com/africa/ (ZM absent)
- ardusimple ZA regional context: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-south-africa/
- `py scripts/stations_by_radius.py -15.41 28.28 200` 2026-05-16 — ZAMB00ZMB0 on igs_ip
- `py scripts/stations_by_country.py ZMB` 2026-05-17 — 1 station (ZAMB00ZMB0 on igs_ip)
- WebSearch "Zambia Survey Department CORS NTRIP RTK GNSS 2025 2026" 2026-05-16 — null
- WebSearch "Zambia Survey Department CORS NTRIP RTK 2026" 2026-05-17 — null
