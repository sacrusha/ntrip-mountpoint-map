# Fiji [FJ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; original 2026-05-06)

## Status: NO confirmed public NTRIP caster (infrastructure present, no access policy). Re-verified 2026-05-17: no DLSS NTRIP endpoint, registration portal, or access policy has been published since the 2022 SPC milestone; FIG 2025 proceedings discuss "data handling and compilation" but do not reference a public real-time NTRIP service.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (10 CORS stations exist; no public NTRIP) |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster confirmed alive |
| **datum_epoch** | omitted -- no citable operator declaration (no public DLSS portal) |

## Most Recent Project Announcement

**Fiji Geodetic Datum project (SPC partnership)** — 8 stations added 2019–2022 to the existing Suva and Lautoka long-standing CORS, bringing the network to 10 stations. SPC's 2022 milestone article noted access regulations were still being developed. No public NTRIP endpoint has been announced since.

## Context Notes

- **DLSS (Department of Lands & Survey Services) CORS network**: 10 stations including long-standing Suva and Lautoka plus 8 added 2019–2022 under the Fiji Geodetic Datum project with SPC (Pacific Community).
- **No access policy/regulation** in place: the SPC 2022 milestone article states explicitly "there is no regulation at the moment for accessing data from the COR stations"; once the geodetic datum is finalised, policy/legislation will be reviewed. No update to access policy has been publicly announced as of 2026-05-17.
- **No public NTRIP endpoint** has been published.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede-RTK): no Fiji coverage confirmed.
- Practical workaround for hobbyists: deploy a local base station for single-base RTK, or use satellite-based PPP services.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / IGS** — Suva station SUVA00FJI (4-char: SUVA); in-operation 10+ years | https://www.earthscope.org/data/gnss-data/ | Free noncommercial; USD 1,000/seat/yr commercial |
| **SONEL** — SUVA station RINEX archive 1999–2020 | https://www.sonel.org/spip.php?page=gps&idStation=849 | Free |
| **Geoscience Australia GNSS Data Centre** — APREF-contributing Pacific stations; anonymous download via SFTP/S3/HTTPS | https://data.gnss.ga.gov.au/ | Free |
| **DLSS CORS (8 stations: Labasa, Nabouwalu, Taveuni, Kadavu, Koro Island, Lakeba, Ono-i-Lau, Rotuma)** — No data access regulation or public portal as of 2022 SPC milestone; contact Department of Lands & Survey | https://www.lands.gov.fj/ | Unknown (direct contact) |

## Sources Consulted
- SPC (Pacific Community) — Fiji Geodetic Datum milestone (Sep 2022): https://www.spc.int/updates/blog/2022/09/milestone-for-fiji
- FIG 2018 — Establishment of GNSS CORS Fiji (Samisoni): https://www.fig.net/resources/proceedings/2018/09_rfip/1.2%20Establishment%20of%20GNSS%20CORS%20PS.pdf
- FIG 2025 — Fiji Geodetic Datum Surveys (Tabua & Lal): https://fig.net/resources/proceedings/fig_proceedings/fig2025/ppt/ts01h/TS01H_tabua_lal_13343_ppt.pdf
- Pacific Data Hub — Fiji geodetic datum surveys dataset: https://pacificdata.org/data/dataset/oai-www-spc-int-4e09dc78-c2d5-45bd-8d58-a0b33a899665
- EarthScope / IGS data archive: https://www.earthscope.org/data/gnss-data/
- SONEL — Suva (SUVA00FJI) station data: https://www.sonel.org/spip.php?page=gps&idStation=849
- Geoscience Australia GNSS Data Centre (APREF): https://data.gnss.ga.gov.au/
- NTRIP-list.com Pacific: https://ntrip-list.com/
