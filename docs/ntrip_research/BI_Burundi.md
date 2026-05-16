# Burundi [BI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (prior: 2026-05-12, initial 2026-05-06)
**Note:** "BI — IG" refers to IGEBU (Institut Géographique du Burundi), the national geographic institute.

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **landing_url** | n/a (no caster) |
| **access_url** | n/a (no caster) |
| **host:port** | null |
| **tariff** | null |
| **num_stations** | 0 (no BI station in any public registry) |
| **vrs** | n/a |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |
| **datum_epoch** | not citable — Burundi has no published modern GNSS datum/epoch (legacy datum Arc 1960 / Clarke 1880 in continued use per 2016 academic source; no official modernisation declaration found) |

## Most Recent Project Announcement / Activity

None operational. Adjacent activities involving GNSS but no public CORS/NTRIP output:
- **PRRPB land-certification programme** (Burundi Landscape Restoration and Resilience Project, World Bank-financed): IGNFI/GEOFIT-LADEC consortium in Bujumbura (Isare) and Muyinga (Buhinyuza) provinces — >105,000 hill surveys, >103,000 land certificates. Uses GNSS for cadastral survey but no public CORS/NTRIP endpoint announced. URL: https://ignfi.fr/en/references/burundi-landscape-restoration-and-resilience-project-prrpb/
- **RCMRD AFREF capacity-building workshop** (12–15 August 2024) included Burundi but produced no operational caster. URL: https://ric2024.rcmrd.org/afref
- **Bureau de Centralisation Géomatique (BCG)** under the Second Vice-President's office — coordinates GIS/geomatics across ministries; no CORS deployment plan in the public news feed (verified 2026-05-15). URL: https://sp-bcg.gov.bi/

## National Mapping Agency

**IGEBU** (Institut Géographique du Burundi) — https://www.igebu.bi/ (HTTP 200 nginx/1.27.1, observed 2026-05-15)
Established 1980 (Decree 100/146). Three departments: Cartography & Topography, Hydrometeorology & Hydrogeology, Administrative & Financial.
- JICA partnership since 2009: updating cartography of Bujumbura and Gitega using GPS, remote sensing, GIS. No CORS/NTRIP deployment ever announced.
- IGEBU's `/notres-stations/` page lists **17 stations — all classified "Land (fixed)" weather/hydromet stations**, none are GNSS/CORS. URL: https://www.igebu.bi/notres-stations/
- Cartographie service page (`/Services/cartographie/`) mentions GPS, télédétection, SIG, drones — no GNSS reference network. URL: https://www.igebu.bi/Services/cartographie/

## Context Notes

- **No BI GNSS station in any public registry**: IGS Network (0 results for BI), AFREF Operational Data Centre (afrefdata.org refused TCP connection from sandbox 2026-05-15), SONEL, EarthScope/GAGE, mvarga1989 community CORS list (BI not listed). Local `data/stations.json`: 0 BDI mountpoints.
- **Geodetic status**: Active datum still Arc 1960 (Clarke 1880 ellipsoid) — not yet modernised to a GNSS-based national reference frame; ground control marks largely no longer visible in field (per SCIRP 2016 geodetic datum transformation paper for Burundi). No 2024–2026 official declaration of a modernised datum found.
- **RCMRD**: Burundi is one of 20 RCMRD member states. The Leica SBC portal (corsdata.rcmrd.org) requires login; no Burundi-specific content accessible.
- **AFREF/EAFREF**: Burundi is in the EAFREF (East African) regional sub-set but is NOT among AFREF countries listed with operational CORS stations.
- **Global commercial/community networks**: GEODNET, ONOCOY, Centipede-RTK, RTKdata, RTK2GO — zero BI coverage.

## Nearest Cross-Border Alternative

**Not within 50 km.** The 3 free EarthScope NOTA stations in western Rwanda — `KMBR_RTCM3P3` (-1.83, 29.29), `NYBA_RTCM3P3` (-1.76, 29.35), `RUBO_RTCM3P3` (-1.73, 29.26) — are 172–184 km north of Bujumbura (per `scripts/stations_by_radius.py`), too far for short-baseline RTK. They stream via `ntrip.earthscope.org:2101` under the EarthScope NULA (non-commercial). Useful only for crews working in the northernmost border zone toward Lake Kivu.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **RCMRD CORS data portal** — Burundi is an RCMRD member; if any BI station were ever connected, RINEX could be accessed via the login-gated Leica SBC portal. No BI station confirmed at the portal. | https://corsdata.rcmrd.org/sbc | Unknown — login required; contact rcmrd@rcmrd.org |

## Sandbox Probe Log (2026-05-15)

- `https://www.igebu.bi/` → HTTP 200 (nginx/1.27.1)
- `https://sp-bcg.gov.bi/` → HTTP 200 (Apache)
- `http://www.afrefdata.org/welcome.php` → ECONNREFUSED (server side; not a sandbox routing issue — AFREF data portal is intermittently offline; cannot independently verify BI absence from AFREF ODC this run, relying on prior cross-checks)
- `py scripts/stations_by_country.py BDI` → 0 stations
- `py scripts/stations_by_radius.py -3.38 29.36 200` → 3 EarthScope RW stations (>170 km)

## Contact for Status Enquiries
- IGEBU Cartography & Topography Dept (via https://www.igebu.bi/)
- BCG (Bureau de Centralisation Géomatique) — https://sp-bcg.gov.bi/
- RCMRD (AFREF/CORS programme): rcmrd@rcmrd.org

## Sources Consulted (2026-05-15)
- IGEBU website https://www.igebu.bi/ (incl. `/notres-stations/`, `/Services/cartographie/`)
- BCG https://sp-bcg.gov.bi/
- IGS Network https://network.igs.org/ (0 BI)
- AFREF http://www.afrefdata.org/ (unreachable this run; prior cross-checks show 0 BI)
- RCMRD https://corsdata.rcmrd.org/sbc, https://ric2024.rcmrd.org/afref
- IGNFI PRRPB https://ignfi.fr/en/references/burundi-landscape-restoration-and-resilience-project-prrpb/
- mvarga1989 GNSS CORS list (BI absent) https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2GO http://rtk2go.com/, Centipede-RTK https://www.centipede-rtk.org/, RTKdata https://rtkdata.online/network — 0 BI
- SCIRP 2016 geodetic datum transformation paper for Burundi
- Local: `data/stations.json` (0 BDI), `scripts/stations_by_radius.py` (RW EarthScope cluster >170 km)
