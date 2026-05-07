# ntrip-mountpoint-map

Interactive map of free public **NTRIP mountpoints** and **RTK correction
networks** worldwide. Find a free **RTCM correction stream** near you for
centimetre-accurate GPS — built for hobbyists and small shops who need
better than 5–10 m GPS without a paid subscription. About 5,400 stations
across 66 networks (rtk2go, Centipede, EarthScope NOTA, SAPOS, AUSCORS,
IBGE RBMC-IP, ERGNSS, …), refreshed four times daily by a GitHub Actions
workflow.

**Live demo:** https://sacrusha.github.io/ntrip-mountpoint-map/

**Companion guide:** [`guide.html`](https://sacrusha.github.io/ntrip-mountpoint-map/guide.html) — practical primer on
NTRIP, RTK hardware, antenna placement, and DIY base stations.

## Features

- Pre-aggregated station data refreshed four times daily by a GitHub Actions
  workflow; page loads from a static `data/stations.json`, no third-party proxy.
- Three zoom bands: canvas distance-to-nearest-station raster (far), plain
  dots (mid), labelled dots + accuracy rectangles + station details card (close).
- 4-band coverage palette reflecting RTK baseline math: green < 10 km,
  yellow-green 10–30 km, amber 30–50 km, pale red 50–100 km.
- Source and access-tier toggles: filter by network and by access level
  (Free / Free with registration / Free with conditions).
- Staleness display: sources offline 3–7 days shown as grey dots and excluded
  from the coverage raster; sources offline ≥7 days hidden entirely.
- Country-level markers for regions with no physical pins: coloured VRS rings
  (virtual networks with live data, dark-green centroid antenna for clicks),
  bright-green antenna markers for per-station (RS) networks, grey rings or
  grey antennas for stale or not-yet-ingested networks, circled $ / ✕ / ?
  for affordable / restricted / info networks. All driven by
  `data/country_markers.json`. Country markers fade out at z≥6 where individual
  station dots take over.
- The station details card slides up from the bottom of the viewport on any
  marker click, surfacing the three strings you need for your NTRIP client —
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
- `guide.html` — standalone primer covering: scope (NTRIP defined,
  ongoing data cost), compatibility check for existing survey gear
  (Trimble, Leica, Topcon), complete assembled unit recommendations
  (Emlid), DIY path (ArduSimple), step-by-step NTRIP connection with
  NTRIP client pointers, antenna placement (the largest accuracy lever
  after baseline), DIY base station setup, real-world hobbyist examples,
  and a glossary. Prices in €/$; no US-only products.
- `data/help_topics.json` — searchable in-map help (22 interlinked
  topics, 4 popovers) surfaced via the Help button. Covers concepts
  (NTRIP, VRS, datum offsets, ionospheric storms), connect-step
  troubleshooting, antenna placement, false-fix and jamming awareness,
  and a use-case catalogue (`is-this-for-me`).
- Filters DGNSS-only mountpoints (sub-metre, out of scope), VRS/network-
  solution streams (no fixed coordinates), and flags legacy RTCM 2.x streams
  in the station details card.
- IP-based geolocation (ipwho.is) for initial map centre — no permission
  prompt.
- Source-agnostic frontend and pipeline: adding a caster is one line in
  `scripts/fetch_stations.py`.

## Data sources currently fetched

**~5,472 stations** across 66 sources as of 2026-04. Sourcetable fetches are
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
| **Mesa County RTVRN** | US — Colorado (western) | VRS (~33 underlying) | rtvrn.mesacounty.us |

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
records country-level knowledge for the 66 in-pipeline networks plus known
networks not yet ingested. **221 markers** as of 2026-04-29. Three tiers appear
on the map for regions with no physical pins: coloured VRS circles (virtual
networks with live data), grey circles (~83 free networks pending ingestion —
Portugal, Lithuania, Thailand, Venezuela, plus the country-survey-audit
additions across Africa / Caribbean / Central Asia), and circled ? (~75 paid
or restricted networks — swipos, CPOS, HEPOS, ROMPOS, AGROS, TUSAGA-Aktif,
CZEPOS, MIRANET, the Russia and China commercial clusters, Dubai DVRS, Peru
REGPMOC, Quebec MERN, Israel APN, etc.).

A complementary `docs/country-survey.md` documents the RTK access landscape
for **188 country/territory entries** (top-120 GDP ∪ top-120 population +
administered territories), with Tier A entries carrying a contextual paragraph
where sanctions, civil war, or legal barriers materially affect access. See
[`docs/networks.md`](docs/networks.md) for per-network endpoints, credentials,
and the deferred candidates list.

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

## FAQ

### How do I find a free NTRIP mountpoint near me?

Open the [map](https://sacrusha.github.io/ntrip-mountpoint-map/) — it
auto-centres on your approximate location via IP geolocation. Pins within
~10 km of you give cm-accurate RTK on a dual-frequency receiver; up to
~30 km is still good; up to ~50 km is workable. Click any pin to copy the
server, port, and mountpoint into your NTRIP client.

### What is an NTRIP caster list?

An NTRIP caster is an internet endpoint that streams RTK correction data
from one or more reference stations. Its **sourcetable** lists every
mountpoint it exposes — name, format, supported constellations, fee
status. This map aggregates the public sourcetables from 66 casters and
plots each physical reference station; the station card gives you the three
strings your NTRIP client needs (server, port, mountpoint).

### Do these mountpoints actually work without paying?

Yes. Every source on the map is free, in one of three access tiers:
**open** (no account — rtk2go, Centipede, GeoRTK), **free with
registration** (most national networks: SAPOS, AUSCORS, ERGNSS, RBMC-IP,
…), and **free with conditions** (EarthScope's non-commercial NULA,
APOS Austria's agriculture-only tier, …). Commercial / paid networks
are deliberately excluded — see [`docs/networks.md`](docs/networks.md)
for what was investigated and rejected.

### What hardware do I need to use these corrections?

A dual-frequency (L1+L2 minimum) GNSS receiver with NTRIP-client
support. Single-frequency receivers and smartphone GPS chips cannot do
RTK regardless of configuration. The cheapest path is an ArduSimple
simpleRTK2B kit (~€275 + a phone running an NTRIP client). The
[guide](https://sacrusha.github.io/ntrip-mountpoint-map/guide.html) has
hardware recommendations across the price range.

### Why are there no pins in [my country]?

Three possibilities, distinguished by the country-level circle on the
map. A **coloured circle** means a VRS-only network covers the country —
sign up; corrections exist but virtual mountpoints have no fixed
coordinates to plot. A **grey circle** means a free network is known but
not yet ingested. A **circled ?** means the only options are paid or
restricted; click for details. A blank country has no confirmed free
option as of the most recent survey.

### How is "centimetre-accurate GPS" different from regular GPS?

Standalone GPS drifts 5–10 m due to atmospheric and satellite-clock
errors. A nearby reference station measures those errors in real time
and streams the correction over the internet via NTRIP. Your receiver
applies it and the error largely cancels out, getting you to 1–3 cm
within ~10 km of the station and typically better than 5 cm out to ~30
km on a multi-band receiver.

### Where does the data come from?

A GitHub Actions workflow fetches sourcetables from every configured
caster four times a day (01/07/13/19 UTC), parses STR lines, drops
DGNSS-only and VRS streams, and commits the result to
[`data/stations.json`](data/stations.json) on `main`. See
[`docs/networks.md`](docs/networks.md) for every endpoint, credentials,
and audit trail of what was investigated.

## Data attributions

Station coordinates, mountpoint names, formats, and constellations are
republished from each operator's NTRIP sourcetable. Where the operator's
licence requires attribution, the required wording is reproduced in the
in-app help drawer and in
[`guide.html`](https://sacrusha.github.io/ntrip-mountpoint-map/guide.html#attributions).
Briefly:

- **AUSCORS** — © Commonwealth of Australia (Geoscience Australia), data
  licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **PositioNZ** — Sourced from Land Information New Zealand and licensed
  for re-use under
  [Creative Commons Attribution 4.0 New Zealand](https://creativecommons.org/licenses/by/4.0/).
- **Centipede-RTK** — © Centipede-RTK contributors. Database under
  [ODbL v1.0](https://opendatacommons.org/licenses/odbl/1-0/);
  documentation/software content under
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- **ERGNSS** — Fuente: Instituto Geográfico Nacional de España. Attribution
  required per Orden FOM/2807/2015.
- **EarthScope NOTA** — GNSS data © EarthScope Consortium, made available
  under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) per the
  Non-Commercial Use Licence Agreement (NULA), which incorporates CC BY 4.0
  by reference for the underlying data.

Other operators ingested by this project publish their sourcetables
without an attribution clause; each network is still credited by name in
the map's station card and in [`docs/networks.md`](docs/networks.md).

## License

MIT — see [LICENSE](LICENSE). The MIT licence covers this project's source
code only; station data carries the licences attributed above.
