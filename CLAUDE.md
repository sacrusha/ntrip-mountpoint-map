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
- [`docs/networks.md`](docs/networks.md) — refined list of free public
  NTRIP casters. Confidence tiers + explicit paid/restricted drops + candidates
  for future ingestion.

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

Develop on `claude/move-data-loading-workflow-8y7Vl`, PR into `main`. The
workflow only runs against `main`, so anything touching data ingestion
needs to land on `main` to be exercised.

## Current state (end of last session)

**Implemented:**
- Hourly GitHub Actions workflow with rebase-retry, DGNSS filter, carrier/
  format tagging, carrier-inference fallback for rtk2go's empty-field lines.
- Four sources in the pipeline: rtk2go, Centipede, FReDNet, GeoRTK (Japan).
- Three-band zoom UX: coverage raster only at z ≤ 5, canvas circleMarker
  dots 6 ≤ z ≤ 9, viewport-culled detail layer (labels + accuracy
  rectangles + popups) at z ≥ 10.
- Coverage raster is a proper distance-to-nearest field: two-pass
  alpha-accumulate + 256-entry colour LUT (green < 10 km → pale red 50–100
  km). No overlap-colour artefacts.
- KDBush v3 spatial index over visible stations; used by the coverage tile
  loop and the detail-layer viewport cull. Linear fallback if the CDN
  script fails.
- IP-based geolocation via ipwho.is for initial map centre, no permission
  prompt.
- Popups: accuracy summary in plain language, legacy-RTCM-2 warning, one
  server / port / mountpoint block per source the station is in — each
  line with its own copy button.
- Dismissible top banner with localStorage-persisted dismissal and a
  "learn more" expander. HAS fallback is named explicitly.
- Source-agnostic frontend: sources map + colour/label config at the top
  of `index.html`. Adding a new source is "add to `SOURCES` in
  `fetch_stations.py`" plus optional entries in `SOURCE_COLORS` /
  `SOURCE_LABELS` for presentation — no other code change required.

**Open / deferred (by priority):**
1. Verify FReDNet actually serves data — added in the last session; first
   post-merge workflow run will confirm the sourcetable fetch succeeds.
2. Access-tier toggles (Registration / Category / Restricted) currently
   have no backing data — they're shown but filter nothing. Either hide
   them until data exists or populate the tier per-station in the pipeline.
3. Next caster candidates with confirmed endpoints (see
   `docs/networks.md`): FReDNet is already in. Registration-required ones
   (ASG-EUPOS, FLEPOS, WALCORS, SAPOS, CROPOS, IBGE RBMC-IP, AUSCORS,
   PositioNZ) need credentials stored as GitHub Actions secrets before
   they can be fetched.
4. NRTK rendering is scaffolded (`networks: []` in the JSON, polygon +
   clickable centroid marker ready) but no NRTK data is ingested yet.
   First target when adding an NRTK source (e.g. ASG-EUPOS with its
   national service area) should produce the first non-empty `networks[]`
   entry — compute the coverage hull in the workflow.
5. `precLabel` (in `index.html`) still uses a hardcoded `cos(47°)` for the
   longitude-to-metres conversion. Only used inside the accuracy-rectangle
   tooltip (which is already off by default). Fix: use the station's own
   latitude. Flagged earlier by review, low severity.
6. Mountpoint text search + URL deep-link (`?m=NAME`) — not in this
   iteration's scope; users know geographically where they need coverage,
   so map panning is the main interaction.
7. Jargon audit of the banner / onboarding copy: the banner leads with
   "NTRIP" and "50 cm", which a first-time user without vocabulary may
   bounce from. Plain-language rewrite is a cheap win.

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
