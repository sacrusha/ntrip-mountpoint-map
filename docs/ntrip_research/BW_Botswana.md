# Botswana [BW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (previous 2026-05-12)

## Status: National CORS network exists (DSM, ~55 stations); no public NTRIP endpoint disclosed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | None — physical CORS network operates internally; no caster host:port published |
| **Network name** | Botswana National CORS Network (DSM) |
| **Operator** | Department of Surveys and Mapping (DSM), Ministry of Lands and Water Affairs (`gov.bw`), Gaborone |
| **landing_url** | https://www.gov.bw/land-management/maps-and-geospatial-data |
| **access_url** | none — no public registration or sourcetable portal identified |
| **host:port** | not published |
| **tariff** | not publicly listed; access via institutional channel (licensed surveyors / cadastral workflow) |
| **num_stations** | ~55 physical CORS (project commenced 2011, ~10 stations/yr; 2017 thesis observed 28 of installed stations functioning) |
| **vrs** | unknown — no sourcetable available |
| **hobbyist_eligibility** | not advertised; DSM materials frame CORS use around cadastral surveying |
| **legal_residency_required** | unknown — no published terms |
| **last_confirmed_alive** | 2026-05-15 — `gov.bw/land-management/maps-and-geospatial-data` reachable; page describes maps/orthophotos/DEMs only, no NTRIP/RTK service exposed; no BW mountpoints on rtk2go, Centipede, or ntrip-list.com Africa |
| **datum_epoch** | OMIT — no public caster to attach datum to; institutional frame is BNGRS02 (legacy BTRS / Cape Datum / Modified Clarke 1880) |

## Operator

**Department of Surveys and Mapping (DSM)**
Ministry of Lands and Water Affairs
Private Bag 0037, Gaborone, Botswana
Landing: https://www.gov.bw/land-management/maps-and-geospatial-data

## Network Details

- **Station count:** ~55 physical CORS (a 2024 academic update cites 56). Build-out from 2011 at ~10 stations/year.
- **Coverage:** ~582,000 km²; nominal inter-station spacing ~30–40 km.
- **Geodetic framework:** BNGRS02 (Botswana National Geodetic Reference System 2002); legacy BTRS / Cape Datum / Modified Clarke 1880 still in use for older records.
- **Operational status:** 2017 academic thesis observed only ~28 stations functioning; subsequent interviews attribute downtime primarily to internet infrastructure constraints rather than hardware. No public uptime report has been published since.
- **RTK baseline limit:** DSM cadastral guidance permits RTK from CORS up to 40 km baseline.
- **Caster software / host:port:** not published; no sourcetable surfaced through DSM or any third-party directory.

## Negative Findings (verified 2026-05-15)

- rtk2go sourcetable (`http://rtk2go.com:2101/`): zero BW mountpoints. The only string matching "BW" is `PFORZEM` (Pforzheim, Baden-Württemberg, Germany).
- ntrip-list.com Africa: lists only AFREF and easynav.xyz/GEODNET; no Botswana entry.
- Centipede public network: no BW base stations.
- IGS Network (network.igs.org, 534 stations as of 2026-05-15): no Botswana site located via current search.
- ArduSimple South-Africa / Africa directory: no Botswana caster.
- GIM International CORS-for-Africa survey: Botswana remains catalogued as "unmapped".

## Nearest cross-border alternatives

No public NTRIP base within ~50 km of any Botswana border has been identified. The closest public rtk2go bases observed via `scripts/stations_by_radius.py -24.65 25.91 800` are:

| Mountpoint | Country | Lat / Lon | Distance from Gaborone | Notes |
|---|---|---|---|---|
| `LouwNPP` | ZAF | -27.3400, 30.9000 | ~582 km | Volunteer base, far outside RTK range |
| `mabuda_farm` | SWZ | -26.4700, 31.9400 | ~638 km | Volunteer base, far outside RTK range |

South Africa's **TrigNet** (gov't, free for South-African users) does not extend across the border into Botswana; baselines to any operational TrigNet site exceed RTK-usable distance for Gaborone and points further west/north.

## Most Recent Project Reference

- **2017 academic thesis (Högskolan i Gävle / DiVA portal)** — station-by-station status map, ~28 of installed stations operational. Still the most detailed public snapshot.
- **2024 LinkedIn post** — DSM joined SURPAC regional surveying-software user community; describes cadastral-workflow modernisation, not a public NTRIP rollout.
- No 2025–2026 announcement of public NTRIP service surfaced through WebSearch (queries against `gov.bw`, "DSM Botswana", "Botswana CORS NTRIP 2025/2026", Onocoy/GeodNet/SwiftNav coverage).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| DSM Botswana RINEX archive | https://www.gov.bw/ (contact DSM directly) | unknown — availability not publicly documented |
| EarthScope / IGS data centre (regional sites) | https://www.earthscope.org/data/gnss-data/ | free for non-commercial use (account required) |
| HartRAO (SA) IGS regional archive | https://geodesy.hartrao.ac.za/ | free for non-commercial use |

## Sources Consulted (2026-05-15)

- gov.bw Maps and Geospatial Data: https://www.gov.bw/land-management/maps-and-geospatial-data
- DiVA portal — Botswana CORS academic thesis (2017): https://www.diva-portal.org/smash/get/diva2:1137711/FULLTEXT02
- GIM International — Developing a Fully Fledged CORS Map for Africa: https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- OICRF DSM cadastral information system reference: https://www.oicrf.org/-/botswana-department-of-survey-and-mapping-dsm-cadastral-information-system
- LinkedIn (May 2024) — DSM Botswana joins SURPAC user community: https://www.linkedin.com/pulse/department-surveys-mapping-dsm-botswana-joins-other-surveyor-gowera
- rtk2go sourcetable probe `http://rtk2go.com:2101/` 2026-05-15 — zero BW mountpoints
- monitor.use-snip.com rtk2go monitor page (647 kB HTML pulled 2026-05-15) — no Botswana, Gaborone, Francistown, Maun, or Kasane matches
- ntrip-list.com Africa: https://ntrip-list.com/africa/ — no Botswana entry
- IGS Network station list: https://network.igs.org/ — no Botswana site surfaced
- ArduSimple Africa directory: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-south-africa/ — no Botswana entry
