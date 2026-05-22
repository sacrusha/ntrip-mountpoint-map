# Nigeria [NG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21

## Status

NIGNET (Nigerian Permanent GNSS Reference Network, operated by OSGOF) runs a live MIRACaster NTRIP service at `ntrip.nignet.net:21011` via the MIRAnet portal `miranet.nignet.net` (operator MIRASpaco under contract to OSGOF). Account approval is manual; no published tariff or hobbyist tier. One free volunteer base in Oyo on rtk2go. No other volunteer / community NTRIP coverage in country.

## Caster 1 — NIGNET / MIRACaster (national, restricted-public)

| Field | Value |
|---|---|
| **landing_url** | https://miranet.nignet.net/ (MIRAnet — "GNSS Data Management Platform"; the OSGOF homepage menu links to this as "osgof-cors station", confirming MIRAnet is the official NIGNET access route) |
| **access_url** | https://miranet.nignet.net/pre-registration/form (operator pre-registration form: Full Name, Email, Organization, Telephone, Preferred Username; manual approval, no self-service signup) |
| **host:port** | `ntrip.nignet.net:21011` — caster live 2026-05-21, anonymous GET returns `HTTP/1.1 500 Internal Server Error` with `Server: NTRIP MIRACaster TeroMovigo-190108/2.0` and `Ntrip-Version: Ntrip/2.0` headers (auth-required, expected behaviour) |
| **num_stations** | **3 live, observed 2026-05-21** — the MIRAnet portal homepage embeds a Google Maps script with three station pins (`KNKN00NGA` ~11.98 N 8.54 E Kano area, `ABFC00NGA` ~9.03 N 7.49 E Abuja area, `WRDE00NGA` ~5.51 N 5.74 E Warri area). OSGOF cites 15 stations at NIGNET launch (2008, AFREF contribution) and announced a 165-station expansion in 2021; the productionised MIRAnet portal currently surfaces 3 — a substantial gap below both the historical 15 and the 165-target. Academic literature flags inconsistent uptime at the original ~15 stations. |
| **mountpoints** | 3 live pins on `miranet.nignet.net` map embed (2026-05-21): `KNKN00NGA`, `ABFC00NGA`, `WRDE00NGA` — IGS-style 9-character names. None of these match the legacy NIGNET 4-character station-IDs (ABUZ Zaria, BKFP Birnin Kebbi, CGGT Toro, CLBR Calabar, FUTY Yola, GEMB Gembu, HUKP Kano, MDGR Maiduguri, OSGF Abuja, RUST Port Harcourt, ULAG Lagos, UNEC Enugu) tested in 2017-era academic work, so naming was renumbered when MIRASpaco productionised the network. Live sourcetable is gated by auth so mountpoint-name == station-name mapping cannot be verified anonymously. |
| **vrs** | ? — MIRAnet platform supports raw single-base streams; whether a network/VRS product is offered is not documented publicly |
| **tariff** | not publicly published; OSGOF communications mention "after payment of subscription fees" without specific NGN amounts or tier structure |
| **hobbyist_eligibility** | ? — registration form collects Organization, suggesting institutional intent; no published hobbyist tier |
| **legal_residency_required** | ? — registration form does not require a Nigerian ID or address, but approval is at OSGOF/MIRASpaco discretion |
| **last_confirmed_alive** | 2026-05-21 — `https://miranet.nignet.net/` HTTP 200; `ntrip.nignet.net:21011` accepts TCP, responds with `HTTP/1.1 500 Internal Server Error` + `Server: NTRIP MIRACaster TeroMovigo-190108/2.0` to anonymous GET |
| **datum_epoch** | omitted — no citable operator declaration on osgof.gov.ng or miranet.nignet.net. Per primer, do NOT infer from AFREF / ITRF / NIGNET academic literature |

### Background

- **NIGNET** established by OSGOF in 2008 with 15 stations as Nigeria's contribution to AFREF.
- **2021 expansion announcement**: 165-station target at ≤50 km spacing nationwide; rollout status opaque. The MIRAnet portal map currently surfaces 3 stations (Kano/Abuja/Warri), so the practical live network in 2026 sits well below both the 15-station 2008 launch state and the 165-station target. Inter-station baselines of 500-1,000 km across 923,768 km² greatly exceed single-base RTK range.
- **NTRIP implementation history**: A 2017 University of Beira Interior thesis documented building a BKG-based NTRIP caster + PHP/MySQL management system + PayPal billing for NIGNET. The current production deployment (`miranet.nignet.net` + MIRACaster on port 21011) is the productionised continuation, run by MIRASpaco — a private operator that also installs/rehabilitates GNSS CORS networks in Nigeria, Mozambique and Angola.
- **OSGOF site link**: the OSGOF homepage menu explicitly links to https://miranet.nignet.net/ as "osgof-cors station", confirming MIRAnet is the official NIGNET access route.
- **MIRACaster** software identifies as `NTRIP MIRACaster TeroMovigo-190108/2.0` — TeroMovigo (https://teromovigo.com/) is MIRASpaco's umbrella brand for geomatics services.

## Caster 2 — rtk2go `fssoyo` (community, public)

| Field | Value |
|---|---|
| **landing_url** | http://rtk2go.com/ |
| **access_url** | http://rtk2go.com/ (any-email shared credential model; mountpoint name is the username, password `none`) |
| **host:port** | `rtk2go.com:2101` — mountpoint `fssoyo`, country tag `NGA`, 7.84 N 3.95 E (Oyo); RTCM 3.2 MSM (1006/1008/1013/1033/1074/1084/1094/1124/1230) |
| **num_stations** | 1 |
| **vrs** | no — single base operated by **Federal School of Surveying, Oyo** (FSSOYO) per rtk2go station tag |
| **tariff** | free |
| **hobbyist_eligibility** | yes |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-21 — `STR;fssoyo;Oyo;RTCM 3.2;…;NGA;7.84;3.95;…;SNIP;none;B;N;4100;` returned by live rtk2go sourcetable probe |
| **datum_epoch** | omitted — rtk2go is no-enforcement; per primer, frame is operator-set and not declared in sourcetable |

Coverage: useful only in the immediate Oyo / Ibadan area (~30 km single-base range). Lagos (~140 km SW), Abuja, Port Harcourt out of range.

## Other Coverage — Negative Findings

- **Centipede**: 0 NGA stations (verified 2026-05-21 via live `caster.centipede.fr:2101` sourcetable).
- **EarthScope (NOTA)**: 0 NGA NTRIP streams; IGS station ABUZ exists as RINEX archive only.
- **GEODNET / ONOCOY / PointOne / Skylark**: no NG coverage confirmed 2026-05-21.
- **Ardusimple Nigeria page**: lists no national network; states "as far as we know Nigeria is not among them" (re: countries with a national RTK network ardusimple recommends), pointing users at the global free tier (rtk2go, IGS, EarthScope) — this predates / does not cover the MIRAnet NIGNET productionisation.
- **Galileo HAS**: free PPP-RTK alternative usable across Nigeria for decimetre-class accuracy (~5 min convergence).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| NIGNET RINEX archive — via OSGOF / MIRAnet portal | https://miranet.nignet.net/ | unknown — account required |
| IGS / EarthScope — ABUZ (Zaria), the Nigerian IGS station | https://www.earthscope.org/data/gnss-data/ | free non-commercial (NULA + seat) |

## Probes (2026-05-21)

| Endpoint | Result |
|---|---|
| `https://miranet.nignet.net/` | HTTP 200, 20.4 KB — MIRAnet portal live; modal references `ntrip.nignet.net:21011`; embedded Google Maps script declares `LocationData = [[11.98, 8.54], [9.03, 7.49], [5.51, 5.74]]` with `StationNames = ['KNKN00NGA', 'ABFC00NGA', 'WRDE00NGA']` — 3 live station pins, no more |
| `http://ntrip.nignet.net:21011/` (anonymous NTRIPv2 GET) | `HTTP/1.1 500 Internal Server Error`, `Server: NTRIP MIRACaster TeroMovigo-190108/2.0`, `Ntrip-Version: Ntrip/2.0` (auth required) |
| `curl --http0.9 http://ntrip.nignet.net:21011/` (NTRIPv1-style probe) | empty response — anonymous NTRIPv1 probe returned no sourcetable bytes; consistent with auth gating but different from the explicit 500 returned to NTRIPv2 |
| `http://rtk2go.com:2101/` | `STR;fssoyo;Oyo;RTCM 3.2;…;NGA;7.84;3.95;…;SNIP` confirmed |

## Sources

- OSGOF official site: https://osgof.gov.ng/ (menu links to miranet.nignet.net as "osgof-cors station")
- MIRAnet portal: https://miranet.nignet.net/ (live 2026-05-21; references `ntrip.nignet.net:21011`)
- MIRAnet pre-registration form: https://miranet.nignet.net/pre-registration/form
- MIRASpaco company page: https://miraspaco.com/ and https://miraspaco.com/gnss/
- TeroMovigo (MIRASpaco umbrella brand): https://teromovigo.com/portfolio/
- UBI thesis on NIGNET NTRIP implementation (2017): https://ubibliorum.ubi.pt/handle/10400.6/5840
- Space Watch Africa — 165-CORS expansion announcement: https://spacewatchafrica.com/nigeria-to-establish-new-165-cors-station-beginning-from-2021/
- FMIC — UNECA donation of CORS equipment to OSGOF: https://fmic.gov.ng/uneca-donates-equipment-of-cors-to-osgof/
- DOAJ — NIGNET stability evaluation: https://doaj.org/article/5d416470808f4841bc1d945385f7b1b9
- Academia.edu — Ojigi paper on NIGNET RTK services: https://www.academia.edu/8484226
- ArduSimple Nigeria: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-nigeria/
- Federal School of Surveying, Oyo (rtk2go base operator): https://www.facebook.com/fssoyo/
- Local: `py scripts/stations_by_country.py NGA` → 1 (rtk2go / fssoyo)
