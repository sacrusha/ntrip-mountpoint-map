# Start here — handover for the next session

A map of **free public RTK correction networks** for hobbyists and small
shops (<20 people) who need better than ~5–10 m GPS accuracy without a paid
subscription. Two use modes: discovery ("what exists nearby?") and migration
("my old mountpoint stopped working, show me alternatives"). Enterprise / B2B
is out of scope. DGNSS filtered out. PPP/SSR/HAS mentioned as a pointer but
not covered — fee-free complete units from ~$2,900, subscription-dependent
hardware from ~$850 + fees.

## Pointers

- [`docs/requirements.md`](docs/requirements.md) — product spec, target users,
  out-of-scope, data-model, visual design, tech choices, deferred items.
- [`docs/networks.md`](docs/networks.md) — **authoritative record for every
  investigated network**, included or not. Endpoints, credentials, pipeline
  status, drop rationale. Read before touching ingestion code. Entries with
  `**investigate**:` need verification; `**missing**:` need research first.
- [`docs/country-survey.md`](docs/country-survey.md) — RTK landscape by
  country (access model, open questions). Detail lives in networks.md.
- [`docs/global-survey.md`](docs/global-survey.md) — same for multi-country
  and global networks.

## Repository layout

```
index.html                    # Single-page Leaflet app — all UI.
guide.html                    # Plain-English hobbyist primer (static page).
scripts/fetch_stations.py     # Sourcetable fetch + parse + diff.
.github/workflows/
  update-stations.yml         # Cron + workflow_dispatch, runs the Python.
data/
  stations.json               # Canonical JSON, consumed by index.html.
  <source>.sourcetable        # Raw archives per caster.
```

## How updates flow

1. Cron (or manual `workflow_dispatch`) fires on `main`.
2. `fetch_stations.py` fetches each caster in `SOURCES`, parses, filters
   DGNSS, writes `data/stations.json` and per-source sourcetables.
3. If the parsed station fingerprint is unchanged, the script exits — no
   commit, no Pages rebuild.
4. Otherwise the workflow commits as `github-actions[bot]` with a
   rebase-retry loop and pushes to `main`.
5. GitHub Pages rebuilds. `index.html` fetches `./data/stations.json` on load.

Adding a new source: one entry in `SOURCES` in `fetch_stations.py` with
`color` and `label` fields — no frontend changes needed. Optionally add an
entry to `SOURCE_AUTH` in `index.html` for connection hints in popups.

## Branch convention

Develop on feature branches, PR into `main`. The workflow only runs against
`main`, so ingestion changes need to land there to be exercised.

## Current state (2026-04-20, PRs #18 + #20 + claude/add-bike-networks-OsR6J)

**40 sources, ~5,600+ stations** in `data/stations.json`. Sources: rtk2go,
Centipede, FReDNet, GeoRTK, 14× SAPOS Länder, ERGNSS, APOS (AT, Free*),
AUSCORS, PositioNZ, SatRef HK, InaCORS, TrigNet, RBMC-IP, RAMSAC, FLEPOS,
WALCORS, SPSLux, ASG-EUPOS, CROPOS, ESTPOS, LatPos, IGAC, EarthScope NOTA,
MIRAI, CORS-KOREA, IceCORS, KSA-CORS.

**Source config in one place:** `color` and `label` live in `SOURCES` in
`fetch_stations.py` and are emitted to `stations.json`. `SOURCE_COLORS` /
`SOURCE_LABELS` in the frontend are populated from JSON at load time — not
hardcoded. `SOURCE_AUTH` (credentials and popup hints) stays in `index.html`.

**VRS-only networks** (CROPOS, ASG-EUPOS, FLEPOS, WALCORS, ESTPOS, LatPos,
KSA-CORS, 10 SAPOS states) expose only virtual mountpoints — correctly
dropped to 0 stations by `filter_vrs()`. Shown as purple stopgap circles in
the Sources toggle panel with a ring swatch and `(VRS)` count badge. Toggling
hides/shows the circle and respects tier filters. `VRS_NETWORKS` in
`index.html` holds the centroids; SAPOS states with physical-coord data (HE,
RP, SL, SN) are excluded. APOS (AT) is physical-coord-vrs with 37 distinct
station coords — shows as regular pins with a pins:true VRS badge. Full NRTK
polygons are deferred.

**`yearly_cost` field in `docs/networks.md`:** all paid and paid-affordable
entries now carry a `**yearly_cost**:` field for reference (not yet in JSON).

**Longitude normalisation:** `parse_sourcetable` now normalises 0-360°
longitudes to ±180 (ERGNSS: 114/128 affected; AUSCORS: 2/808). `lon` is
included in `station_fingerprint` so the next pipeline run rewrites JSON.

**5 sources timing out in CI:** FLEPOS, WALCORS, ESTPOS, LatPos, KSA-CORS.
Handled gracefully by fallback-to-cached-sourcetable. See `**investigate**:`
in `docs/networks.md`.

**Open / deferred (by priority):**
1. NRTK / VRS coverage polygons: rendering scaffolded (`networks: []` in JSON)
   but no polygon data ingested. VRS stopgap markers are the placeholder.
2. Network endpoint verification — see `docs/networks.md` `**investigate**:`
   (5 CI-failing) and `**missing**:` (9 deferred: renep, litpos, thailand_dol,
   mncors, orgn, msrn, nysnet, wiscors candidate, zakpos).
3. US state DOT networks (WISCORS, MnCORS, ORGN, MSRN, NYSNet) — deferred;
   need endpoint verification and EarthScope overlap check.
4. `SOURCE_AUTH.openNote` strings are derivable from `access`+`registration`
   already in JSON; could be dropped from `index.html`. Deferred — requires
   popup refactor.

## Design notes

- **Accuracy rectangles at detail zoom:** sourcetables report coordinates at
  variable precision (2–5 decimals). The rectangle shows "station is somewhere
  in this box" — derived from coordinate string precision, not configurable.
  Without it, a pin can land in a lake and destroy trust in the dataset.
- **No marker clustering:** the zoom-band swap + viewport cull + coverage
  raster carry the load to ~15k stations. Reconsider only beyond that.
- **KDBush over RBush:** stations are static per render, range queries
  dominate, KDBush is ~1 KB smaller. Rebuilt on toggle-filter change.
- **Workflow idempotency:** fingerprint includes carrier, format, and `lon`
  (normalised float). `carrierInferred` is NOT in the fingerprint — flip this
  if you change the inference rule.

## Gotchas

- **Corrupt cached sourcetable kills the fetch thread:** in `fetch_source`,
  `parse_sourcetable()` on the cached file is called outside the
  `try/except` block. A corrupted `.sourcetable` would raise an unhandled
  exception and kill that thread. Pre-existing; low probability (files are
  written atomically). Fix when adding per-source retry logic.
- **rtk2go carrier field:** blank for most entries even on RTCM 3.x MSM
  streams. Parser infers `carrier = 2` when format starts with `RTCM 3`;
  without this, only ~2 of 800+ rtk2go mountpoints survive. Preserve this.
- **Workflow push race:** cron runs can race human PR merges. The push step
  has a 3-attempt rebase-retry loop; don't simplify it.
- **Leaflet `L.DomUtil.create` signature:** third arg is a DOM parent, not a
  className. Passing a string throws inside `addTo` and silently freezes the
  page. Use `L.DomUtil.create('div')` with no extra args.
- **`preferCanvas: true`** — required so `L.circleMarker` renders to canvas;
  without it, per-station SVG blows the DOM budget at ~2k+ stations.

## Testing

- `node --check` on the extracted inline `<script>` block catches JS syntax.
- `python3 scripts/fetch_stations.py` runs the pipeline locally; sandboxed
  environments without network fall through to the cached-sourcetable path.
- No unit tests yet. A small pytest for `parse_sourcetable` would pay off the
  first time someone touches the carrier-inference rule.
