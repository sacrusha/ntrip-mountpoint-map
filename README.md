# ntrip-mountpoint-map

Interactive map of free public NTRIP RTK correction mountpoints. Aimed at
hobbyists and small shops looking for cm-accurate GPS corrections — if you
need only ~30 cm, use Galileo HAS instead; this site is for users who need
better.

**Live demo:** https://sacrusha.github.io/ntrip-mountpoint-map/

## Features

- Pre-aggregated station data refreshed hourly by a GitHub Actions workflow;
  page loads from a static `data/stations.json`, no third-party proxy.
- Three zoom bands: canvas distance-to-nearest-station raster (far), plain
  dots (mid), labelled dots + accuracy rectangles + popups (close).
- 4-band coverage palette reflecting RTK baseline math: green < 10 km,
  yellow-green 10–30 km, amber 30–50 km, pale red 50–100 km.
- Popups surface the three strings you need for your NTRIP client —
  server host, port, mountpoint name — each with a one-click copy button.
- Accuracy rectangle at close zoom encodes the precision of the reported
  coordinates, so pins in physically implausible locations don't destroy
  trust in the data.
- Dismissible scope banner with a pointer to Galileo HAS for users who
  don't need cm-level accuracy.
- Filters the DGNSS-only mountpoints the pipeline encounters (out of scope
  — dominated by free HAS) and flags legacy RTCM 2.x streams in popups.
- IP-based geolocation (ipwho.is) for initial map centre — no permission
  prompt.
- Source-agnostic frontend and pipeline: adding a caster is one line in
  `scripts/fetch_stations.py`.

## Data sources currently fetched

| Source | URL | Access |
|--------|-----|--------|
| rtk2go.com | `http://rtk2go.com:2101/` | free, no registration for rovers |
| CentipedeRTK | `http://caster.centipede.fr:2101/` | free, no registration |
| FReDNet (OGS, IT-NE) | `http://gnsscaster.regione.fvg.it:8080/` | free, no registration |
| RTKdata.online | `http://rtkdata.online:2101/` | community caster, best-effort |

See [`docs/networks.md`](docs/networks.md) for research on additional free
networks (FLEPOS, WALCORS, ASG-EUPOS, SAPOS, CROPOS, IBGE RBMC-IP, AUSCORS,
PositioNZ, …) — most require registration, so adding them needs credentials
stored as GitHub Actions secrets.

The NTRIP sourcetable is a public protocol endpoint (RTCM 10402.1) — reading
it is its intended use.

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
- GitHub Actions — hourly sourcetable fetch + commit to `main`
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
