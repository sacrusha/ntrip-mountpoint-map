# North Macedonia [MK] — NTRIP RTK Research

**researched:** 2026-05-21 (refresh of 2026-05-17)
**status:** YES — MAKPOS national NRTK (AREC). Quasi-geoid heights real-time since February 2026. Paid subscription; tariff not published in open web.

## MAKPOS — Macedonian Positioning System

| field | value |
|---|---|
| landing_url | https://makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx (SpiderWeb landing). Backup: https://www.katastar.gov.mk/en/data/services/ |
| access_url | https://makpos.katastar.gov.mk/sbc/Account/Register (Leica Spider Business Center self-registration) |
| operator | AREC — Agency for Real Estate Cadastre of the Republic of North Macedonia (katastar.gov.mk) |
| host:port | `makpos.katastar.gov.mk:9001` (185.177.14.205) — Leica GNSS Spider RT Proxi + NTRIP Caster. TCP probe from sandbox 2026-05-21 timed out (port 9001 firewalled to non-MK traffic), consistent with prior probes; service announcements through Feb 2026 confirm operational. |
| sample mountpoint | `iMAX-GNSS` — iMAX-style NRTK, GPS + GLONASS + Galileo |
| num_stations | 14 physical CORS across ~25,700 km² (mean inter-station distance ~43 km from area/count arithmetic; "50-70 km spacing" cited in prior research without a traceable primary source URL — contact AREC for official network map) |
| vrs | yes — iMAX (Trimble-style master-aux variant, server-interpolated; nmea=1 in ST) |
| tariff | Paid subscription via SBC; MKD price schedule not published in the open web (no search hits on katastar.gov.mk; Macedonian-language search also returned no tariff results; ArduSimple MK page lists no pricing). One older source claimed free-of-charge for users with compatible GNSS on 3G/GPRS — unverified, likely conditional or stale. Contact AREC (info@katastar.gov.mk). |
| hobbyist_eligibility | ? — SBC sign-up form is open with no surveyor-licence wall observed, but payment accessibility has not been verified (tariff not public; currency MKD; payment method unknown for non-residents). Downgraded from "likely yes" due to unverified payment path. |
| legal_residency_required | ? — not stated |
| last_confirmed_alive | service assumed operational — `makpos.katastar.gov.mk:9001` TCP timeout from sandbox after 15 s (port 9001 geo-/firewall restricted; no sourcetable reachable). SpiderWeb landing ECONNREFUSED from sandbox. AREC press release 2026-02-23 confirms deployment of MK_HREF2022 quasi-geoid model, indicating the service was operational at that date. No sandbox-reachable sourcetable or login portal confirmation available. |
| datum_epoch | **ETRS89** — AREC operator-declared in the MK_HREF2022 deployment press release (https://www.katastar.gov.mk/en/2026/02/23/the-first-official-quasi-geoid-model-has-been-put-into-use-for-the-territory-of-the-republic-of-north-macedonia/) — "ellipsoidal heights in ETRS89", converted to NVT1 normal-orthometric via the MK_HREF2022 quasi-geoid (internal ±4.0 cm, external ±10 cm). Epoch not stated; ETRS89 is plate-fixed, rovers do not propagate to current epoch. |

## Services

- **DGPS** — 0.3-0.5 m, RTCM 2.x, GPRS + NTRIP (out of scope for project)
- **RTK** — 0.02-0.04 m, RTCM 2.x/3.x, GPRS + NTRIP, with real-time quasi-geoid height since 2026-02
- **Precise positioning** — <0.01 m, RINEX, internet distribution

## Recent activity

- **2026-02-23** AREC deployed the MK_HREF2022 hybrid quasi-geoid (Govt Decision 2025-11-25). Built with Kartverket (Norway), verified by Lantmäteriet (Sweden). 2,470 gravimetric points (all NVT3 benchmarks plus 5 × 5 km grid). MAKPOS now serves grid + quasi-geoid correction in real time. A desktop transformation app is available for registered users.
- **2020-04-08** Galileo multi-constellation upgrade.

## Context

- 14-CORS spatial density good for flat/rolling terrain; mountainous regions may degrade VRS performance.
- AREC Sector for Geodetic Works administers MAKPOS: https://www.katastar.gov.mk/en/about-us/contact/sectors-in-arec/sector-for-geodetic-works/
- Nearest free RTK alternatives outside MK are rtk2go bases in Bulgaria (`MESTY`, `Pernik` ~155 km from Skopje) — beyond practical single-base range.
- Local data: `py scripts/stations_by_country.py MKD` returns 1 EUREF + 1 IGS (academic streams `SKO100MKD0`). Zero rtk2go / Centipede MK volunteer bases.

## Post-processing

| Service | URL | Cost |
|---|---|---|
| MAKPOS RINEX via SBC | https://makpos.katastar.gov.mk/sbc/ | paid; contact AREC |
| EUREF EPN (`SKO100MKD0`) | https://epncb.oma.be/ | free (account) |

## Sources

- AREC MAKPOS SpiderWeb portal: https://makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx
- AREC SBC registration: https://makpos.katastar.gov.mk/sbc/Account/Register
- AREC Galileo upgrade (2020-04-08): https://www.katastar.gov.mk/en/2020/04/08/makpos-system-upgraded-for-galileo-functionalities/
- AREC MK_HREF2022 deployment + ETRS89 cite (2026-02-23): https://www.katastar.gov.mk/en/2026/02/23/the-first-official-quasi-geoid-model-has-been-put-into-use-for-the-territory-of-the-republic-of-north-macedonia/
- AREC data and services: https://www.katastar.gov.mk/en/data/services/
- ArduSimple North Macedonia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-macedonia/
- EuroGeographics member page: https://eurogeographics.org/member/agency-for-real-estate-cadastre/
- Live caster probe: `curl --http0.9 http://185.177.14.205:9001/` TCP timeout 15 s 2026-05-21 (geo-restricted)
- Local: `data/euref_ip.sourcetable` + `data/igs_ip.sourcetable` 2026-05-21 (SKO100MKD0)
