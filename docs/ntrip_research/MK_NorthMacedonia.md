# North Macedonia [MK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-17 — quasi-geoid datum cite added)

## Status: YES — MAKPOS national NRTK active; quasi-geoid heights real-time since Feb 2026; paid subscription

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — MAKPOS (Macedonian Positioning System), operated by AREC (Agency for Real Estate Cadastre, katastar.gov.mk). |
| **landing_url** | https://makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx — MAKPOS SpiderWeb landing. Backup: https://www.katastar.gov.mk/en/data/services/ |
| **access_url** | https://makpos.katastar.gov.mk/sbc/Account/Register — Spider Business Center registration (tariff schedule not published in open web; contact AREC). |
| **host:port** | `makpos.katastar.gov.mk:9001` (Leica GNSS Spider RT Proxi Server + NTRIP Caster). |
| **Sample mountpoint** | `iMAX-GNSS` — iMAX-style NRTK, GPS + GLONASS + Galileo. |
| **num_stations** | 14 physical CORS at 50–70 km spacing across ~25,700 km². |
| **vrs** | Yes — iMAX (Trimble-style master-aux variant, server-interpolated; nmea=1 in ST). |
| **tariff** | Paid subscription via SBC. MKD schedule not published; one source claimed free-of-charge for users with compatible GNSS on 3G/GPRS — unverified, likely conditional or stale. Contact AREC. |
| **hobbyist_eligibility** | Likely yes — SBC sign-up open; no surveyor-licence wall observed. |
| **legal_residency_required** | Not stated. |
| **last_confirmed_alive** | 2026-02-23 AREC quasi-geoid press release confirms MAKPOS operational with real-time grid + height; SBC portal HTTP 200 historically. Alberding worldwide-datastreams probe on port 9001 returned "Caster not available" 2026-05-12 — interpret as restricted external probe, not service shutdown. 2026-05-17 WebFetch of `makpos.katastar.gov.mk` and SpiderWeb landing → ECONNREFUSED from sandbox; service announcements through Feb 2026 confirm activity. |
| **datum_epoch** | **ETRS89** — operator-declared by AREC in the MK_HREF2022 deployment press release https://www.katastar.gov.mk/en/2026/02/23/the-first-official-quasi-geoid-model-has-been-put-into-use-for-the-territory-of-the-republic-of-north-macedonia/ (ellipsoidal heights in ETRS89; converted to NVT1 normal-orthometric heights via the MK_HREF2022 quasi-geoid, internal ±4.0 cm, external ±10 cm). Epoch: 1989.0 (ETRS89 realization anchor; not an applied user epoch — ETRS89 is plate-fixed, rovers do not propagate coordinates to a current epoch). |

## Recent activity
- **2026-02-23** — AREC deployed MK_HREF2022 hybrid quasi-geoid (Govt Decision 2025-11-25). Built with Kartverket (Norway), verified by Lantmäteriet (Sweden). 2,470 gravimetric points (all NVT3 benchmarks + 5 × 5 km grid). MAKPOS now serves grid + quasi-geoid correction in real time. Desktop transformation app for registered users.
- **2020-04-08** — Galileo multi-constellation upgrade.

## Services
- **DGPS** — 0.3–0.5 m, RTCM 2.x, GPRS + NTRIP.
- **RTK** — 0.02–0.04 m, RTCM 2.x/3.x, GPRS + NTRIP, with real-time quasi-geoid height since 2026-02.
- **Precise positioning** — <0.01 m, RINEX, internet distribution.

## Context
- 14-CORS spatial density good for flat/rolling terrain (mean spacing 50–70 km inside ~25,700 km²); mountainous regions may degrade VRS performance.
- AREC Sector for Geodetic Works administers MAKPOS: https://www.katastar.gov.mk/en/about-us/contact/sectors-in-arec/sector-for-geodetic-works/
- Nearest free RTK alternatives outside MK are rtk2go bases in Bulgaria (~155 km from Skopje) — beyond single-base range.

## Post-processing (RINEX) fallback
| Service | URL | Cost |
|---|---|---|
| MAKPOS — RINEX via SBC | https://makpos.katastar.gov.mk/sbc/ | paid; contact AREC |
| EUREF EPN — regional CORS | https://epncb.oma.be/ | free (account) |

## Sources consulted
- AREC MAKPOS SpiderWeb portal: https://makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx
- AREC SBC registration: https://makpos.katastar.gov.mk/sbc/Account/Register
- AREC Galileo upgrade (2020-04-08): https://www.katastar.gov.mk/en/2020/04/08/makpos-system-upgraded-for-galileo-functionalities/
- AREC MK_HREF2022 deployment + datum cite (2026-02-23): https://www.katastar.gov.mk/en/2026/02/23/the-first-official-quasi-geoid-model-has-been-put-into-use-for-the-territory-of-the-republic-of-north-macedonia/
- AREC data and services overview: https://www.katastar.gov.mk/en/data/services/
- Alberding worldwide NTRIP map (probe of :9001 returned "Caster not available" 2026-05-12): https://www.alberding.eu/cgi-bin/map.cgi?caster=makpos.katastar.gov.mk&port=9001&lang=en
- ArduSimple North Macedonia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-macedonia/
- EuroGeographics — AREC profile: https://eurogeographics.org/member/agency-for-real-estate-cadastre/
- GitHub sctg-development RtkGps issue #14 (mentions `iMAX-GNSS` mountpoint)
- docs/rtk_inventory.md `makpos` block
