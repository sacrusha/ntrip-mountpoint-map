# ntrip-mountpoint-map

Interactive map of free public NTRIP RTK correction mountpoints. Aimed at
hobbyists and small shops looking for cm-accurate GPS corrections within
~100 km of a reference station.

**Live demo:** https://sacrusha.github.io/ntrip-mountpoint-map/

## Features

- Pre-aggregated station data refreshed four times daily by a GitHub Actions
  workflow; page loads from a static `data/stations.json`, no third-party proxy.
- Three zoom bands: canvas distance-to-nearest-station raster (far), plain
  dots (mid), labelled dots + accuracy rectangles + popups (close).
- 4-band coverage palette reflecting RTK baseline math: green < 10 km,
  yellow-green 10–30 km, amber 30–50 km, pale red 50–100 km.
- Source and access-tier toggles: filter by network and by access level
  (Free / Free with registration / Free with conditions).
- Staleness display: sources offline 3–7 days shown as grey dots and excluded
  from the coverage raster; sources offline ≥7 days hidden entirely.
- Popups surface the three strings you need for your NTRIP client —
  server host, port, mountpoint name — each with a one-click copy button,
  plus a direct link to the registration page where one is needed.
- Accuracy rectangle at close zoom encodes the precision of the reported
  coordinates, so pins in physically implausible locations don't destroy
  trust in the data.
- Dismissible scope banner with a pointer to Galileo HAS for users who
  don't need cm-level accuracy.
- Filters DGNSS-only mountpoints (sub-metre, out of scope) and flags legacy
  RTCM 2.x streams in popups.
- IP-based geolocation (ipwho.is) for initial map centre — no permission
  prompt.
- Source-agnostic frontend and pipeline: adding a caster is one line in
  `scripts/fetch_stations.py`.

## Data sources currently fetched

**~5,600 stations** across ~40 casters as of 2026-04. Sourcetable fetches are
public (RTCM 10402.1 — reading the sourcetable is its intended use); stream
access requires registration where noted.

### Open access (no account needed)

| Source | Endpoint | Notes |
|--------|----------|-------|
| rtk2go.com | `rtk2go.com:2101` | ~860 volunteer bases globally; any email as username |
| CentipedeRTK | `crtk.net:2101` | ~1,200 bases; dense in France; login `centipede`/`centipede` |
| GeoRTK (Geosense) | `geortk.jp:2101` | ~40 stations, Japan; no auth |

### Free with registration

| Source | Region | Stations | Registration |
|--------|--------|----------|--------------|
| FReDNet (OGS) | NE Italy | ~39 | frednet.crs.ogs.it |
| SAPOS (14 Länder) | Germany | ~80 | per-state forms at sapos.de (Bayern: free for agriculture, €20/yr otherwise) |
| ERGNSS (IGN) | Spain | ~128 | ergnss.ign.es/gnuserportal/ |
| AUSCORS (GA) | Australia | ~811 | gnss.ga.gov.au/registration |
| PositioNZ-RT (LINZ) | New Zealand | ~62 | LINZ account + positionz@linz.govt.nz |
| SatRef (Lands Dept) | Hong Kong | ~22 | geodetic.gov.hk |
| InaCORS (BIG) | Indonesia | ~4 | nrtk.big.go.id |
| TrigNet (NGI) | South Africa | ~72 | trignet.co.za |
| RBMC-IP (IBGE) | Brazil | ~140 | gov.br RBMC-IP signup |
| RAMSAC (IGN) | Argentina | ~204 | ign.gob.ar portal |
| FLEPOS | Belgium (Flanders) | 45 VRS | flepos.vlaanderen.be |
| WALCORS | Belgium (Wallonia) | 23 VRS | gnss.wallonie.be |
| SPSLux (ACT) | Luxembourg | ~17 VRS | spslux.lu/SBC/ |
| ASG-EUPOS | Poland | VRS | system.asgeupos.pl |
| CROPOS | Croatia | VRS | cropos.hr |
| ESTPOS | Estonia | 40 VRS | geoportaal.maaamet.ee |
| LatPos (LGIA) | Latvia | VRS | latpos.lgia.gov.lv/SBC |
| IGAC MAGNA-ECO | Colombia | ~17 | redgeodesica-sbc.igac.gov.co/sbc |
| MIRAI (Go!GNSS) | Japan | ~325 | go.gnss.go.jp |
| IceCORS (LMÍ) | Iceland | ~20 | natt.is |

### Free with conditions

| Source | Region | Stations | Condition |
|--------|--------|----------|-----------|
| EarthScope NOTA | Americas | ~1,096 | Non-commercial use only (annual NULA) |
| CORS-KOREA | South Korea | ~498 | Korean national ID may be required |
| KSA-CORS (GEOSA) | Saudi Arabia | 209 VRS | ksacors.geoportal.sa |
| ESTPOS | Estonia | 40 VRS | Free until Aug 2026 only |

VRS-only networks (CROPOS, ASG-EUPOS, FLEPOS, WALCORS, etc.) expose virtual
mountpoints only — no physical station coordinates — so they show 0 pins on
the map. Coverage polygons for these are deferred. See
[`docs/networks.md`](docs/networks.md) for endpoints, credentials, and
candidates for future ingestion.

## Contributing / Next-session handover

If you're Claude (or a human) picking this up: start with
[`CLAUDE.md`](CLAUDE.md). It captures the product scope, the repo layout,
the update flow, current implementation state, deferred items, and gotchas
from prior sessions. The product spec lives in
[`docs/requirements.md`](docs/requirements.md).

## Stack

- [Leaflet](https://leafletjs.com/) — BSD-2-Clause
- [KDBush](https://github.com/mourner/kdbush) — ISC, spatial index
- [OpenStreetMap](https://www.openstreetmap.org/) tiles — data ©
  OpenStreetMap contributors, [ODbL](https://opendatacommons.org/licenses/odbl/)
- GitHub Actions — four times daily sourcetable fetch + commit to `main`
- [ipwho.is](https://ipwho.is/) — IP-based geolocation for initial map centre

## Usage

Open `index.html` from any HTTP/HTTPS server. Opening from `file://` won't
work — OSM tiles and the stations.json fetch both need a real HTTP origin.

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Or enable GitHub Pages (Settings → Pages → main branch → `/ (root)`) for a
hosted version.

## License

MIT — see [LICENSE](LICENSE).
