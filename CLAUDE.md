# Start here — handover for the next session

A map of **free NTRIP corrections capable of better than ~50 cm GPS
accuracy**. Target users are hobbyists and small shops (<20 people) in two
modes: discovery ("what exists? what's nearby? is any of it useful for me?")
and migration ("my old mountpoint stopped working, show me alternatives near
where I work"). Enterprise / B2B is explicitly out of scope — if a user only
needs ~30 cm, the banner points them at Galileo HAS instead of listing
sub-metre DGNSS sources.

## Pointers

- [`docs/requirements.md`](docs/requirements.md) — product spec, target users,
  out-of-scope, data-model, visual design, tech choices, deferred items.
- [`docs/networks.md`](docs/networks.md) — **authoritative technical record for
  every investigated network**, whether included or not. Endpoints, credentials,
  pricing, pipeline status, drop rationale. Read this before touching code.
  If it's not here, don't add it to the pipeline. Entries with `**investigate**:`
  need endpoint/connectivity verification; entries with `**missing**:` need
  research before they can be ingested.
- [`docs/country-survey.md`](docs/country-survey.md) — how RTK works country
  by country: which networks exist, access model (free/paid/registration),
  open questions. Not a network reference — detail lives in networks.md.
- [`docs/global-networks.md`](docs/global-networks.md) — same scope as
  country-survey.md but for multi-country and global networks (RTK2go,
  Centipede, EarthScope, Galileo HAS, etc.). Not a network reference.

## Repository layout

```
index.html                    # Single-page Leaflet app — all UI.
scripts/fetch_stations.py     # Hourly sourcetable fetch + parse + diff.
.github/workflows/
  update-stations.yml         # Cron + workflow_dispatch, runs the Python.
data/
  stations.json               # Canonical JSON, consumed by index.html.
  <source>.sourcetable        # Raw archives per caster.
```

## How updates flow

1. Cron (or manual `workflow_dispatch`) fires on `main`.
2. Workflow runs `scripts/fetch_stations.py`, which fetches each caster
   listed in `SOURCES`, parses, filters DGNSS, writes `data/stations.json`
   and per-source raw sourcetables.
3. If the parsed station fingerprint is unchanged vs. the previous commit,
   the script exits without writing — no commit, no Pages rebuild.
4. Otherwise the workflow commits as `github-actions[bot]` with a
   rebase-retry loop to handle concurrent pushes (human PR merges) and
   pushes back to `main`.
5. GitHub Pages rebuilds the site from `main`. `index.html` fetches
   `./data/stations.json` on page load.

## Branch convention

Develop on feature branches, PR into `main`. The workflow only runs against
`main`, so anything touching data ingestion needs to land on `main` to be
exercised.

## Current state (end of session 2026-04-20)

**Implemented:**
- Hourly GitHub Actions workflow with rebase-retry, DGNSS filter, carrier/
  format tagging, carrier-inference fallback for rtk2go's empty-field lines.
- **37 sources** in the pipeline; **~5,600 stations** in `data/stations.json`.
  Sources include rtk2go, Centipede, FReDNet, GeoRTK, 13× SAPOS Länder,
  ERGNSS, AUSCORS, PositioNZ, SatRef HK, InaCORS, TrigNet, RBMC-IP, RAMSAC,
  FLEPOS, WALCORS, SPSLux, ASG-EUPOS, CROPOS, ESTPOS, LatPos, IGAC,
  EarthScope NOTA, MIRAI, CORS-KOREA, KSA-CORS.
- **NTRIP 1.0 raw-TCP fallback** in `fetch()`: catches `BadStatusLine` (which
  Python's urllib does NOT wrap in URLError) and retries via raw socket.
  Required for SAPOS casters and SatRef HK.
- Three-band zoom UX: coverage raster only at z ≤ 5, canvas circleMarker
  dots 6 ≤ z ≤ 9, viewport-culled detail layer (labels + accuracy
  rectangles + popups) at z ≥ 10.
- Coverage raster: two-pass alpha-accumulate + 256-entry colour LUT
  (green < 10 km → pale red 50–100 km).
- KDBush v3 spatial index; linear fallback if CDN fails.
- IP-based geolocation via ipwho.is for initial map centre.
- Popups: accuracy summary, legacy-RTCM-2 warning, per-source connection
  block with copy buttons.
- Dismissible banner with localStorage persistence and HAS fallback mention.
- `SOURCE_COLORS`, `SOURCE_LABELS`, `SOURCE_AUTH` config in `index.html`
  for all 37 sources. Adding a new source only requires a `SOURCES` entry
  in `fetch_stations.py` + optional frontend config — no other changes.

**VRS-only networks (0 physical stations on map):**
CROPOS, ASG-EUPOS, FLEPOS, WALCORS, InaCORS, ERGNSS, ESTPOS, LATPOS,
KSA-CORS, and most SAPOS states expose only VRS virtual mountpoints
(lat=0, lon=0 or a single shared coord), correctly dropped by `filter_vrs()`.
UI shows 0 stations identically for VRS-by-design and fetch failures —
process gap: no "VRS — no pins expected" status separate from "error — pins missing".
Coverage for these networks requires NRTK polygons (deferred).

**5 sources timing out in CI:** FLEPOS, WALCORS, ESTPOS, LATPOS, KSA-CORS.
Fallback-to-cached-sourcetable logic handles this gracefully.
See `**investigate**:` fields in `docs/networks.md` for what to verify.

**Open / deferred (by priority):**
1. NRTK / VRS coverage polygons: rendering scaffolded (`networks: []` in JSON,
   polygon + centroid marker ready) but no data ingested. VRS-only networks need
   manual polygon config.
2. RTK/DGNSS/PPP/HAS/SSR primer — banner copy jargon audit + "learn more"
   rewrite for hobbyist audience.
3. Network endpoint verification and deferred ingestion — see `docs/networks.md`
   entries with `**investigate**:` (5 CI-failing) and `**missing**:` (4 deferred).

## Design notes worth preserving

- **Why accuracy rectangles at detail zoom:** sourcetables report
  coordinates at variable decimal precision (2–5 decimals). Without the
  rectangle, a pin rendered at the reported point can land in a lake or
  off a cliff — users lose trust in the whole dataset. The rectangle
  shows "station is somewhere in this box" and is derived from the
  coordinate string precision, not a configurable quantity.
- **Why not marker clustering:** the zoom-band swap + viewport cull +
  coverage raster already carry the rendering load up to ~15k stations.
  Clustering adds a dependency and changes the per-station click UX.
  Reconsider only if the station count exceeds that range.
- **Why KDBush over RBush:** stations are static per render, range
  queries dominate, KDBush is ~1 KB smaller. Rebuilt on toggle-filter
  change (still cheap at 1000s of points). Null-safe fallback if the
  CDN script fails.
- **Workflow idempotency:** the station fingerprint includes carrier +
  format so the script only skips writing when the parsed station set
  is byte-identical. `carrierInferred` is currently NOT in the
  fingerprint; flip this if you change the inference rule and want the
  next run to rewrite.

## Gotchas

- **`fetch_stations.py` vs. rtk2go carrier field:** rtk2go leaves the
  NTRIP STR carrier field blank for most entries even when the stream
  is RTCM 3.x MSM. The parser infers `carrier = 2` when the format
  starts with `RTCM 3`; without this, only ~2 of 800+ rtk2go
  mountpoints survive the filter. Preserve this behaviour.
- **Workflow push race:** scheduled cron runs can race human PR merges
  between checkout and push. The push step has a 3-attempt
  rebase-retry loop; don't simplify it.
- **Leaflet `L.DomUtil.create` signature:** third arg is a DOM parent,
  not a className. Passing a string there throws inside `addTo` and
  aborts the async loader silently (previous bug — the whole page
  froze on "Locating viewer…"). Use `L.DomUtil.create('div')` with
  no extra args; Leaflet adds the `leaflet-control` class itself.
- **`preferCanvas: true` on the map** — required so `L.circleMarker`
  renders to a canvas pane, otherwise per-station SVG overlays blow
  the DOM budget at ~2k+ stations.

## Testing

- `node --check` on the extracted inline `<script>` block (see `scripts/`
  history of session for the one-liner) catches JS syntax.
- `python3 scripts/fetch_stations.py` runs the pipeline locally; useful
  for parser smoke tests. Sandboxed environments without network will
  fall through to the cached-sourcetable path.
- No unit tests yet. A small pytest for `parse_sourcetable` would pay
  for itself the first time someone touches the carrier-inference rule.
