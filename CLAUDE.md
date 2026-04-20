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
  pricing, pipeline status, confidence tiers, drop rationale. Read this before
  touching code. If it's not here, don't add it to the pipeline.
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

**5 sources currently failing in CI:**
Endpoint fixes applied this session; all 5 remain timing out in GitHub Actions.
Diagnosis: GitHub Actions egress firewall blocks outbound ports 2101/5001/8083
to government NTRIP casters. Fallback-to-cached-sourcetable logic handles this
gracefully — stations remain in the JSON from the last successful fetch.
- `flepos` — URL fixed (`ntrip.flepos.be` → `flepos.vlaanderen.be:2101`); still times out.
- `walcors` — correct endpoint (`gnss.wallonie.be:2101`); intermittent outages documented.
- `estpos` — correct endpoint (`gnss-rtk.maaamet.ee:8083`); also requires credentials.
- `latpos` — port fixed (2101 → 5001 per Alberding caster directory); still times out.
- `ksa_cors` — domain fixed (`KSACORS.gcs.gov.sa` → `ksacors.geoportal.sa:2101`).

**VRS-only networks (0 physical stations on map):**
- CROPOS, ASG-EUPOS, FLEPOS, WALCORS, InaCORS, ERGNSS, ESTPOS, LATPOS,
  KSA-CORS, and most SAPOS states — sourcetables expose only VRS virtual
  mountpoints (lat=0, lon=0 or single shared coord), correctly dropped.
  Coverage representation via NRTK polygons is deferred (see below).
- UI shows 0 stations identically for VRS-by-design and fetch failures —
  no distinction visible to users. Process gap: need a "VRS — no pins
  expected" status separate from "error — pins missing".

**Open / deferred (by priority):**
1. Failing CI sources — 5 sources (FLEPOS, WALCORS, ESTPOS, LATPOS,
   KSA-CORS) consistently time out. Likely cause: stale endpoint URL
   (as seen with IceCORS raw IP and Centipede domain migration) or
   location-based firewall on the operator's side. Each needs manual
   endpoint verification before assuming it's dead.
2. NRTK / VRS coverage polygons: NRTK rendering is scaffolded
   (`networks: []` in JSON, polygon + centroid marker ready) but no data
   ingested. VRS-only networks don't expose physical station coordinates —
   manual polygon config needed for those.
3. Access-tier toggles (Registration / Category / Restricted) shown in
   UI but filter nothing — no backing data yet. Either hide or populate
   per-station in pipeline.
4. SAPOS BY: fee (€20/yr non-agricultural) shown in popup; keeps the
   source in pipeline. Decide long-term whether to separate it out or
   leave as-is.
5. Deferred networks (ReNEP PT, LitPOS LT, Thailand DOL, APOS AT) —
   marked deferred pending endpoint discovery or registration. Revisit
   with fresh research; may have been prematurely deferred.
6. ESTPOS: free until Aug 2026 — no automated reminder. Review before
   then; either re-confirm extension or remove from pipeline.
7. RTK/DGNSS/PPP/HAS primer — banner copy jargon audit + "learn more"
   rewrite for hobbyist audience.
8. NRTK polygon data for VRS networks — big feature, see above.

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
