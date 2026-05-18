# Central African Republic [CF] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified — no operational change) | Currency: XAF (Central African CFA franc, CEMAC zone) — fixed peg €1 = 655.957 XAF

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **landing_url** | null — no operator portal exists |
| **access_url** | null — no service exists |
| **host:port** | null |
| **tariff** | null — no service exists |
| **num_stations** | 0 |
| **vrs** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster has ever been confirmed alive |
| **datum_epoch** | OMIT — no national active geodetic datum published |

## Most Recent Project Announcement

None found. No published project timeline for any CAR CORS/NTRIP service exists as of 2026-05-17. The Ministry of Town Planning (`minurbanisme-rca.org`) lists only land-reform, housing, and Bangui-district rehabilitation programmes — no satellite-positioning, geodesy, or CORS line items.

**AFREF (regional context):** Each AFREF participating country is expected to operate at least one continuously transmitting station. CAR remains absent from AFREF's operational contributing countries; GIM International "Fully Fledged CORS Map for Africa" article reconfirms CAR among the gaps. No CAR station in IGS Network as of 2026-05-17.

## Context Notes

- **No GNSS CORS infrastructure**: CAR has no IGS-affiliated permanent GNSS station, no CORS, no NTRIP caster of any kind.
- **BANGA/Bangui (legacy)**: Appears in older UNAVCO/GAGE DAI listings as a one-off campaign-mode GPS occupation for ITRF/plate-motion solutions — NOT a continuously operating CORS. No NTRIP mountpoint and no real-time stream has ever been associated with the monument.
- **No CF entry** in: IGS network, ITRF2020, SONEL, AFREF operational list, GIM International Africa CORS map, GitHub mvarga1989/The-list-of-GNSS-CORS-RTK-networks.
- **Operator landscape**: ICASEES (`icasees.org`) is statistics-only; geodesy/cartography fall nominally under the Ministry of Town Planning, Land Reform, Cities and Housing (`minurbanisme-rca.org`), which publishes no GNSS programme.
- **Enabling-condition deficits**: Active CPC insurgency, Africa Corps (formerly Wagner) presence since 2018, electricity access 17.6% of population nationally (rural 2.3%, urban 37.4%; World Bank EG.ELC.ACCS.ZS, 2023 — https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS?locations=CF), and limited backbone internet jointly impede any fixed-infrastructure investment.
- **DePIN networks**: GEODNET, ONOCOY, Centipede-RTK, RTKdata — none report any CF coverage as of 2026-05-17.
- **Local pipeline data (verified 2026-05-17)**: `py scripts/stations_by_country.py CAF` returns `No stations for 'CAF'`. `py scripts/stations_by_radius.py 4.39 18.55 800` returns `No stations within 800 km of (4.39, 18.55)`. Nearest pipeline-known stations (1500 km radius) are EarthScope RUBO/KMBR/NYBA in Rwanda at ~1370 km — far outside any usable RTK baseline.

## Nearest Cross-Border Alternative (within ~50 km)

**None.** CAR's borders are with Chad (TD), Sudan (SD), South Sudan (SS), DR Congo (CD), Republic of the Congo (CG), and Cameroon (CM). None of these neighbours operate a public NTRIP caster reachable from CAR territory; the closest known public free streams are >1000 km away. There is no viable cross-border RTK option for any point inside CAR.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — legacy BANGA/Bangui campaign-mode monument may have limited historical RINEX; current archive holdings unverified | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); CAR data availability uncertain |

## Sources Consulted (2026-05-17)
- IGS network.igs.org — 0 CF results (WebFetch)
- IGSNetwork.json, IGS station log archive
- UNAVCO/GAGE Data Archive Interface
- ITRF2020 network list
- SONEL GNSS database
- AFREF (UN-SPIDER, RCMRD apps portal)
- GitHub mvarga1989 CORS list
- GIM International CORS Africa map
- RTKdata, RTK2GO, Centipede-RTK, GEODNET, ONOCOY
- BKG NTRIP, EarthScope/GAGE real-time
- `minurbanisme-rca.org` (Ministry of Town Planning, Land Reform, Cities and Housing) — no GNSS programme listed
- `icasees.org` — statistics only, no geodesy mandate
- Local pipeline: `data/stations.json` via `stations_by_country.py CAF` and `stations_by_radius.py 4.39 18.55 800`
