# ntrip-mountpoint-map

Interactive map of NTRIP RTK correction mountpoints, aggregated live from [rtk2go.com](http://rtk2go.com:2101/) and [Centipede](http://caster.centipede.fr:2101/).

**Live demo:** https://sacrusha.github.io/ntrip-mountpoint-map/

## Features

- Reads pre-aggregated station data from `data/stations.json`, refreshed hourly by a GitHub Actions workflow
- Derives positional accuracy from coordinate string precision (trailing zeros preserved)
- Draws a dashed uncertainty box around each station scaled to its coordinate precision
- Merges stations that appear in both networks at the same location under one marker
- Renders nearest stations first (using browser geolocation, falls back to map centre)
- Colour coding: red = rtk2go only, orange = Centipede only, split circle = both networks
- Click any marker for network membership, coordinates, and location uncertainty in metres

## Data pipeline

Sourcetables are fetched server-side by `.github/workflows/update-stations.yml`
(hourly, plus `workflow_dispatch`), parsed by `scripts/fetch_stations.py`, and
committed to `main` as:

- `data/rtk2go.sourcetable` — raw sourcetable (archival)
- `data/centipede.sourcetable` — raw sourcetable (archival)
- `data/stations.json` — parsed, structured view consumed by `index.html`

Commits only happen when the parsed station set actually changed, so the
timestamp in `stations.json` only moves on real data changes. If a caster is
temporarily unreachable, its last-known good sourcetable is reused.

| Source | URL |
|--------|-----|
| rtk2go.com | `http://rtk2go.com:2101/` |
| Centipede | `http://caster.centipede.fr:2101/` |

The NTRIP sourcetable is a public protocol endpoint (RTCM 10402.1) — reading it is its intended use.

## Stack

- [Leaflet](https://leafletjs.com/) — BSD-2-Clause
- [OpenStreetMap](https://www.openstreetmap.org/) tiles — data © OpenStreetMap contributors, [ODbL](https://opendatacommons.org/licenses/odbl/)
- GitHub Actions — hourly sourcetable fetch + commit to `main`

## Usage

Open `index.html` from any HTTP/HTTPS server. Opening from `file://` will not work — OSM tiles and Centipede CORS both require a real HTTP origin.

Simplest local option:
```bash
python -m http.server 8000
# then open http://localhost:8000
```

Or enable GitHub Pages (Settings → Pages → main branch → / root) for a hosted version.

## License

MIT — see [LICENSE](LICENSE)
