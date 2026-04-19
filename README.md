# ntrip-mountpoint-map

Interactive map of NTRIP RTK correction mountpoints, aggregated live from [rtk2go.com](http://rtk2go.com:2101/) and [Centipede](http://caster.centipede.fr:2101/).

**Live demo:** https://sacrusha.github.io/ntrip-mountpoint-map/

## Features

- Fetches live data from two public NTRIP casters on every page load
- Derives positional accuracy from coordinate string precision (trailing zeros preserved)
- Draws a dashed uncertainty box around each station scaled to its coordinate precision
- Merges stations that appear in both networks at the same location under one marker
- Renders nearest stations first (using browser geolocation, falls back to map centre)
- Colour coding: red = rtk2go only, orange = Centipede only, split circle = both networks
- Click any marker for network membership, coordinates, and location uncertainty in metres

## Data sources

| Source | URL | Access |
|--------|-----|--------|
| rtk2go.com | `http://rtk2go.com:2101/` | via CORS proxy (codetabs.com) |
| Centipede | `http://caster.centipede.fr:2101/` | direct (CORS enabled) |

The NTRIP sourcetable is a public protocol endpoint (RTCM 10402.1) — reading it is its intended use.

## Stack

- [Leaflet](https://leafletjs.com/) — BSD-2-Clause
- [OpenStreetMap](https://www.openstreetmap.org/) tiles — data © OpenStreetMap contributors, [ODbL](https://opendatacommons.org/licenses/odbl/)
- [codetabs.com CORS proxy](https://codetabs.com/cors-proxy/cors-proxy.html) — for rtk2go cross-origin fetch

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
