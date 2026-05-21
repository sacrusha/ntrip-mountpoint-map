# Uzbekistan [UZ] — NTRIP RTK

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
| num_stations | 30–50 planned (2016/2017 Ergashev et al. architecture paper); ~3 confirmed active Samarkand → Tashkent in 2024 E3S paper. No post-2024 disclosure found. |
| hobbyist_eligibility | No — restricted to licensed surveyors / state agencies |
| legal_residency_required | unclear (moot; no open registration) |
| last_confirmed_alive | 2026-05-21 — operator portal `uzgeodezkadastr.uz` reachability degraded across recent probes (HTTP 200 on 2026-05-13; DNS NXDOMAIN 2026-05-17; ECONNREFUSED 2026-05-21); sandbox/transit issue not ruled out. Government portal `gov.uz/en/kadastr/sections/geodeziya-va-kartografiya-yo-nalishi` reachable but content is navigation only — no UZPOS, CORS, or NTRIP detail. No public UZPOS NTRIP endpoint discoverable. |
| datum_epoch | omitted — no citable operator declaration. |

## Project / literature

- **2016–2017 Ergashev et al. (ScienceDirect)** — UZPOS plan: 50 reference stations, Type-A (300-400 km, geodetic) + Type-B (50-80 km, RTK). Architecture only; no endpoint, no public-access policy. https://www.sciencedirect.com/science/article/pii/S1674984717300526
- **2024 E3S Conferences** — "Analysis of quality of measurements of permanent base stations" — 3 UZPOS stations in Samarkand continuously stream to Tashkent control centre for archival / post-processing / scientific use. Closed, archival service, not open NTRIP. https://www.e3s-conferences.org/articles/e3sconf/pdf/2024/28/e3sconf_icape2024_02020.pdf

## Notes

- No open-data mandate analogue (cf. Indonesia Law 4/2011). Post-Soviet Central-Asian pattern: CORS = internal professional asset.
- Volunteer / commercial coverage: 0 rtk2go, 0 Centipede, 0 NOTA (out of footprint), 0 commercial (GEODNET / PointOne / RTKdata / HxGN SmartNet / Trimble VRS Now).
- Cross-border: nearest KZ/KG state CORS also closed-access; KG nearest stations 300+ km from Tashkent. Hobbyists must deploy private base.

## IGS station coverage

`stations_by_radius.py 41.3 69.3 800` (2026-05-21): 1 physical IGS station, 2 source-records:
- auscors: `KITG00UZB0` 39.13N, 66.89E @ 316 km from Tashkent (Kitab Observatory, southern UZ). AUSCORS CC BY 4.0 — free w/ AUSCORS registration.
- igs_ip: `KITG00UZB0` same station, BKG IGS-IP creds — raw 1 Hz RTCM single-base.

KITG is ~316 km SSW of Tashkent (too far for cm-fix RTK; ppm error ~32 cm at 30 mm+1 ppm). Useful as static / post-processing ref or sub-m sparse-coverage RTK in Samarkand / Bukhara / Qashqadaryo regions.

A second IGS station, TASH (Tashkent, 41.33N 69.30E, SEPT ASTERX4), is registered as `TASH00UZB` but the IGS network page records an "offline" advisory dated 2025-06-05; RINEX continues to be archived intermittently (last archived ~April 2026 per IGS page). Realtime stream not advertised through any ingested caster; treat as RINEX-only.

## Post-processing (RINEX)

| Service | URL | Cost |
|---|---|---|
| TASH (IGS / EarthScope archive; intermittent uptime per IGS advisory) | https://www.earthscope.org/data/gnss-data/ | Free non-comm |
| TASH (EPN supplementary) | https://www.epncb.oma.be/ | Free |
| KITG (IGS / EarthScope archive) | https://www.earthscope.org/data/gnss-data/ | Free non-comm |

## Sources
- Operator portal: https://uzgeodezkadastr.uz/ (200 on 2026-05-13; reachability degraded since)
- Gov portal Geodesy directorate (navigation only, no operational detail): https://gov.uz/en/kadastr/sections/geodeziya-va-kartografiya-yo-nalishi
- National GIS open data: https://open.ngis.uz/
- ScienceDirect Ergashev (2016/2017): https://www.sciencedirect.com/science/article/pii/S1674984717300526
- E3S 2024 measurements analysis: https://www.e3s-conferences.org/articles/e3sconf/pdf/2024/28/e3sconf_icape2024_02020.pdf
- European Science journal (CORS architecture): https://europeanscience.org/index.php/1/article/view/632
- EPSG datum 1392: https://epsg.io/1392-datum
- IGS TASH00UZB station page (offline advisory + RINEX continuity): https://network.igs.org/TASH00UZB
- NTRIP-list.com Asia: https://ntrip-list.com/asia/
- `stations_by_radius.py 41.3 69.3 800` 2026-05-21: KITG00UZB0 @ 316 km (auscors + igs_ip).
- `stations_by_country.py UZ` / `UZB` 2026-05-21 — 2 records, 1 station.
