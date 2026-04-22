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
- Country-level markers for regions with no physical pins: coloured VRS circles
  (virtual networks with live data), grey circles (free networks pending
  ingestion — Portugal, Lithuania, Thailand, Venezuela…), circled ? (paid or
  restricted networks). All driven by `data/country_markers.json`.
- Popups surface the three strings you need for your NTRIP client —
  server host, port, mountpoint name — each with a one-click copy button,
  plus a direct link to the registration page where one is needed.
- Accuracy rectangle at close zoom encodes the precision of the reported
  coordinates, so pins in physically implausible locations don't destroy
  trust in the data.
- Plain-language banner and expandable "how it works" panel aimed at
  hobbyists: explains why GPS drifts, distinguishes standalone PPP/HAS
  devices (fee-free units from ~$2,900; subscription hardware from ~$850 +
  fees) from free network RTK, and gives honest hardware price
  ranges. Links to a full hobbyist guide (`guide.html`).
- `guide.html` — standalone primer covering: compatibility check for
  existing survey gear (Trimble, Leica, Topcon), complete assembled unit
  recommendations (Emlid), DIY path (ArduSimple), step-by-step NTRIP
  connection with NTRIP client pointers, DIY base station setup, and
  plain-English glossary. Prices in €/$; no US-only products.
- Filters DGNSS-only mountpoints (sub-metre, out of scope), VRS/network-
  solution streams (no fixed coordinates), and flags legacy RTCM 2.x streams
  in popups.
- IP-based geolocation (ipwho.is) for initial map centre — no permission
  prompt.
- Source-agnostic frontend and pipeline: adding a caster is one line in
  `scripts/fetch_stations.py`.

## Data sources currently fetched

**~5,472 stations** across 65 sources as of 2026-04. Sourcetable fetches are
public (RTCM 10402.1 — reading the sourcetable is its intended use); stream
access requires registration where noted. VRS-only sources appear in the
toggle panel with 0 pins (virtual mountpoints have no fixed coordinates).

### Open access (no account needed)

| Source | Endpoint | Notes |
|--------|----------|-------|
| rtk2go.com | `rtk2go.com:2101` | ~860 volunteer bases globally; any email as username |
| CentipedeRTK | `crtk.net:2101` | ~1,200 bases; dense in France; login `centipede`/`centipede` |
| GeoRTK (Geosense) | `geortk.jp:2101` | ~40 stations, Japan; no auth |

### Free with registration

| Source | Region | Stations | Registration |
|--------|--------|----------|--------------|
| FReDNet (OGS) | NE Italy + border AT/SI | ~28 | frednet.crs.ogs.it |
| SAPOS (14 Länder) | Germany | ~80 VRS/physical | per-state at sapos.de |
| ERGNSS (IGN) | Spain | ~128 | ergnss.ign.es/gnuserportal/ |
| AUSCORS (GA) | Australia | ~811 | gnss.ga.gov.au/registration |
| PositioNZ-RT (LINZ) | New Zealand | ~62 | linz.govt.nz |
| SatRef (Lands Dept) | Hong Kong | ~22 | geodetic.gov.hk |
| InaCORS (BIG) | Indonesia | VRS only | nrtk.big.go.id |
| TrigNet (NGI) | South Africa | ~72 | trignet.co.za |
| RBMC-IP (IBGE) | Brazil | ~140 | gov.br RBMC-IP signup |
| RAMSAC (IGN) | Argentina | ~204 | ign.gob.ar portal |
| FLEPOS | Belgium (Flanders) | 45 VRS | flepos.vlaanderen.be |
| WALCORS | Belgium (Wallonia) | 23 VRS | gnss.wallonie.be |
| SPSLux (ACT) | Luxembourg | VRS only | spslux.lu/SBC/ |
| ASG-EUPOS | Poland | VRS | system.asgeupos.pl |
| CROPOS | Croatia | VRS | cropos.hr |
| LatPos (LGIA) | Latvia | VRS | latpos.lgia.gov.lv/SBC |
| IGAC MAGNA-ECO | Colombia | VRS only | redgeodesica-sbc.igac.gov.co/sbc |
| MIRAI (Go!GNSS) | Japan | ~325 | go.gnss.go.jp |
| IceCORS (LMÍ) | Iceland | VRS only | natt.is |
| **SPIN3 GNSS** | Italy — Piemonte + Lombardia + VdA | ~39 | spingnss.it |
| **GPS-UMBRIA** | Italy — Umbria | 12 | gpsumbria.regione.umbria.it |
| **GNSS Abruzzo+Lazio** | Italy — Abruzzo + Lazio | ~29 | gnss-rtk.regione.abruzzo.it |
| **SIT Puglia** | Italy — Puglia | 12 | sit.puglia.it |
| **WISCORS** | US — Wisconsin | ~180 | wiscors.dot.wi.gov |
| **FPRN** | US — Florida | ~120 | myfloridagps.com |
| **ARDOT RTN** | US — Arkansas | ~50 | gps.ardot.gov |
| **MaCORS** | US — Massachusetts | 22 | macorsrtk.massdot.state.ma.us |
| **VECTOR VT** | US — Vermont | ~15 | vcgi.vermont.gov |
| **AzCORS** | US — Arizona | 51 | azcors.azwater.gov |
| **GCGC RTN** | US — Mississippi / Gulf Coast | ~35 | rtn.usm.edu |
| **AlCORS** | US — Alabama | ~50 | dot.state.al.us |
| **KyCORS** | US — Kentucky | VRS | kycors.ky.gov |
| **MnCORS** | US — Minnesota | VRS | mndot.gov |
| **ORGN** | US — Oregon | ~100 | oregon.gov/odot |
| **MSRN** | US — Michigan | ~120 | michigan.gov/mdot |
| **NYSNet** | US — New York | ~150 | dot.ny.gov |
| **InCORS** | US — Indiana | ~70 | incors.in.gov |
| **IARTN** | US — Iowa | 83 | iowadot.gov |
| **ODOT RTN** | US — Ohio | VRS | transportation.ohio.gov |
| **WVRTN** | US — West Virginia | VRS | transportation.wv.gov |
| **MaineDOT** | US — Maine | VRS | maine.gov/mdot |

### Free with conditions

| Source | Region | Stations | Condition |
|--------|--------|----------|-----------|
| EarthScope NOTA | Americas | ~1,096 | Non-commercial use only (annual NULA) |
| CORS-KOREA | South Korea | ~498 | Korean national ID may be required |
| KSA-CORS (GEOSA) | Saudi Arabia | 209 VRS | Registration may require local credentials |
| ESTPOS | Estonia | 40 VRS | Free until Aug 2026 only |
| APOS (BEV) | Austria | 37 | Free for agriculture/forestry (eAMA); paid for others |
| **GNSS Campania** | Italy — Campania | ~18 | SPID digital identity required for new users |
| **MoDOT RTN** | US — Missouri | VRS | Notarized access agreement required |

VRS-only networks expose virtual mountpoints only — no physical station
coordinates — so they appear as stopgap circles in the toggle panel with 0
pins on the map. Coverage polygons are deferred.

A companion file `data/country_markers.json` (static, not pipeline-generated)
records country-level knowledge for all 65 in-pipeline networks plus known
networks not yet ingested. Three marker tiers appear on the map for regions
with no physical pins: coloured VRS circles (virtual networks with live data),
grey circles (free networks pending ingestion — Portugal, Lithuania, Thailand,
Venezuela…), and circled ? (paid or restricted networks — swipos, CPOS, HEPOS,
ROMPOS, Dubai DVRS, Peru REGPMOC, Quebec MERN, Israel APN, etc.).

See [`docs/networks.md`](docs/networks.md) for endpoints, credentials, and
remaining candidates (11 deferred including 6 Italian regional networks).

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
