# Uzbekistan [UZ] — NTRIP RTK
**Date:** 2026-05-17 (delta vs 2026-05-13: uzgeodezkadastr.uz DNS now NXDOMAIN — site reachability worse than 05-13's HTTP 200; correction to prior file: AUSCORS + IGS-IP both publish IGS station `KITG00UZB0` (Kitab, 39.13N, 66.89E) — single IGS-tier UZ MP, free under AUSCORS / BKG-creds terms. Prior "zero stations within 800 km" claim was wrong).

## Status
NO public domestic NTRIP. State UZPOS CORS network exists, restricted to licensed surveyors + state agencies. One IGS station (KITG, Kitab Observatory) reachable via AUSCORS + IGS-IP — useful for southern UZ work but ~316 km from Tashkent.

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | No (state UZPOS network exists, not open) |
| Network name | UZPOS (Uzbekistan Positioning) |
| Operator | State Committee for Land Resources, Geodesy, Cartography and State Cadastre (UzGeodezKadastr) |
| landing_url | https://uzgeodezkadastr.uz/ |
| access_url | (none — no public NTRIP registration path published) |
| host:port | not publicly documented |
| tariff | not published |
| num_stations | 30–50 planned; ~3 confirmed active Samarkand → Tashkent (2024 paper) |
| hobbyist_eligibility | No — restricted to licensed surveyors / state agencies |
| legal_residency_required | unclear (moot; no open registration) |
| last_confirmed_alive | 2026-05-17 — operator portal `uzgeodezkadastr.uz` DNS NXDOMAIN today; was HTTP 200 on 2026-05-13. No public UZPOS endpoint discoverable. |
| datum_epoch | omitted — no citable operator declaration. |

## Project / literature

- **2016–2017 Ergashev et al. (ScienceDirect)** — UZPOS plan: 50 reference stations, Type-A (300-400 km, geodetic) + Type-B (50-80 km, RTK). Architecture only; no endpoint, no public-access policy. https://www.sciencedirect.com/science/article/pii/S1674984717300526
- **2024 E3S Conferences** — "Analysis of quality of measurements of permanent base stations" — 3 UZPOS stations in Samarkand continuously stream to Tashkent control centre for archival / post-processing / scientific use. Closed, archival service, not open NTRIP. https://www.e3s-conferences.org/articles/e3sconf/pdf/2024/28/e3sconf_icape2024_02020.pdf

## Notes

- No open-data mandate analogue (cf. Indonesia Law 4/2011). Post-Soviet Central-Asian pattern: CORS = internal professional asset.
- Volunteer / commercial coverage: 0 rtk2go, 0 Centipede, 0 NOTA (out of footprint), 0 commercial (GEODNET / PointOne / RTKdata / HxGN SmartNet / Trimble VRS Now).
- Cross-border: nearest KZ/KG state CORS also closed-access; KG nearest stations 300+ km from Tashkent. Hobbyists must deploy private base.

## IGS station coverage

`stations_by_radius.py 41.3 69.3 800` (2026-05-17): 1 physical IGS station, 2 source-records:
- auscors: `KITG00UZB0` 39.13N, 66.89E @ 316 km from Tashkent (Kitab Observatory, southern UZ). AUSCORS CC BY 4.0 — free w/ AUSCORS registration.
- igs_ip: `KITG00UZB0` same station, BKG IGS-IP creds — raw 1 Hz RTCM single-base.

KITG is ~316 km SSW of Tashkent (too far for cm-fix RTK; ppm error ~32 cm at 30 mm+1 ppm). Useful as static / post-processing ref or sub-m sparse-coverage RTK in Samarkand / Bukhara / Qashqadaryo regions.

## Post-processing (RINEX)

| Service | URL | Cost |
|---|---|---|
| TASH (IGS / EarthScope archive) | https://www.earthscope.org/data/gnss-data/ | Free non-comm |
| TASH (EPN supplementary) | https://www.epncb.oma.be/ | Free |

## Sources
- https://uzgeodezkadastr.uz/ (200 on 2026-05-13; DNS NXDOMAIN 2026-05-17)
- ScienceDirect Ergashev: https://www.sciencedirect.com/science/article/pii/S1674984717300526
- E3S 2024 measurements analysis: https://www.e3s-conferences.org/articles/e3sconf/pdf/2024/28/e3sconf_icape2024_02020.pdf
- NTRIP-list.com Asia: https://ntrip-list.com/asia/
- `stations_by_radius.py 41.3 69.3 800` 2026-05-17: KITG00UZB0 @ 316 km (auscors + igs_ip).
