# ntrip-mountpoint-map

Interactive map of public/free **NTRIP mountpoints** and **RTK correction
networks** worldwide. Built for hobbyists and small shops who want
decimetre or centimetre GPS, without a paid subscription. 

**Live demo:** https://ntrip-mountpoint-map.pages.dev/

**Companion guide:** [`guide.html`](https://ntrip-mountpoint-map.pages.dev/ntrip-mountpoint-map/guide.html) — practical primer on
NTRIP, RTK hardware, antenna placement, and DIY base stations.


## Stack

- [Leaflet](https://leafletjs.com/) — BSD-2-Clause
- [KDBush](https://github.com/mourner/kdbush) — ISC, spatial index
- [OpenStreetMap](https://www.openstreetmap.org/) tiles — data ©
  OpenStreetMap contributors, [ODbL](https://opendatacommons.org/licenses/odbl/)
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

## Where does the data come from?

A scheduled job fetches sourcetables from every configured
caster multiple times a day, parses STR lines, drops
DGNSS-only and VRS streams, and commits the result to
[`data/stations.json`](data/stations.json) on `main`. See
[`docs/rtk_inventory.md`](docs/rtk_inventory.md) for every endpoint, credentials,
and audit trail of what was investigated.

## Why not use Github Pages?

We did, then we got shadow banned ("flagged") by a Github robot and the manual review process took over 2 weeks to respond. Access is now restored until it isn't, so we're staying with the Github-independent host for now.

## Data attributions

Station coordinates, mountpoint names, formats, and constellations are
republished from each operator's NTRIP sourcetable. Where the operator's
licence requires attribution, the required wording is reproduced in the
in-app help drawer and in
[`guide.html`](https://ntrip-mountpoint-map.pages.dev/guide.html#attributions).

## License

MIT — see [LICENSE](LICENSE). The MIT licence covers this project's source
code only; station data carries the licences attributed above.
