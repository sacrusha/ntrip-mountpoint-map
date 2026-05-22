# fetch_stations.py — process

Per-file rules for `scripts/fetch_stations.py` source code. Pipeline
context: `../docs/pipeline.md`.

## Role

NTRIP-protocol fetcher and sourcetable parser. Reads operational config
from `../data/rtk_map.json` endpoints; writes `data/stations.json` +
`data/source_health.json` + cached `data/<endpoint_id>.sourcetable`
files. Run by GitHub Actions cron 4×/day.

## Source types

Each `endpoints[]` entry in `../data/rtk_map.json` carries a `type`
field; default is `"ntrip"` for back-compat. The `HANDLERS` dict in
`fetch_stations.py` dispatches on this field. Add a new type by writing
an `_fetch_<type>_source(src) -> (sid, result, was_fresh)` handler and
registering it in `HANDLERS`.

| type | When to use | Cache file |
|---|---|---|
| `ntrip` | Live NTRIP caster sourcetable (`GET / HTTP/1.0`). Default. | `data/<id>.sourcetable` |
| `file` | One-shot input that never updates upstream: forum-transcribed station lists, manually-curated PDFs, blog-extracted coords. Editor commits the JSON; pipeline re-reads it every run. | `data/external_<id>.json` |
| `scraped` | Operator portal that DOES update but is not an NTRIP sourcetable: HTML refmaps, IGS sitelog directories, KMLs. Refreshed on a per-source interval (default 7 d). | `data/<id>.scraped.json` |

**Shared schema across all JSON caches** (file, scraped, and internal
`_m3g_*` helpers): top-level fields are `last_updated` (ISO instant or
bare date), `source_url`, optional `pin_origin`, plus the cache-specific
payload (`stations[]` for file/scraped, `features{}` / `update_ts{}` /
`attrs{}` / `projects{}` for `_m3g_*`). Naming is uniform — there is no
`last_reviewed` / `last_scraped` / `fetched_at` variant; if you find one
in a new cache, rename it. `stations.json` source records keep their
own `fetched_at` + `last_ok` pair (last attempt vs last success) because
they need to distinguish those — caches only exist on success and so
have one timestamp.

### `scraped` source type

Use when the upstream operator publishes station data on a portal that
keeps changing (new stations added, antennas re-surveyed, IDs renamed)
but the format is not an NTRIP sourcetable. The handler imports a
per-source scraper module from `../scripts/scrapers/<name>.py`,
serialises the result to a JSON cache, and serves the cache for up to
`interval_days` before re-running the scraper.

**Endpoint shape** in `../data/rtk_map.json`:
```json
{
  "type": "scraped",
  "id": "sapos_BB_ext",
  "scraper": "sapos_bb",
  "interval_days": 7,
  "pin_origin": "register"
}
```

| field | required | notes |
|---|---|---|
| `type` | yes | Must be `"scraped"`. |
| `id` | yes | Cache-file basename: `data/<id>.scraped.json`. Set explicitly so the cache is stable across endpoint reorderings. |
| `scraper` | yes | Module name under `scripts/scrapers/`. `"sapos_bb"` -> `scripts/scrapers/sapos_bb.py`. |
| `interval_days` | optional, default `7` | Minimum gap between scrapes. Cache served unchanged when fresh; re-scraped only when the cache's `last_updated` timestamp is older than this. |
| `pin_origin` | optional | Written into every station record (`register` for operator-published station registers, `forum` for community lists, etc.). Defaults to `"external"`. |

**Cache format** (`data/<id>.scraped.json`):
```json
{
  "last_updated": "2026-05-21T12:34:56+00:00",
  "source_url":   "https://example.org/stations/",
  "pin_origin":   "register",
  "stations": [
    {"name": "AAAA", "lat": 12.34, "lon": 56.78, "country": "DEU"}
  ]
}
```

**Cadence rationale**: NTRIP sourcetables refresh 4×/day because the
fetch is one HTTP round-trip per caster. A scraped portal typically
needs N+1 round-trips (index + per-station detail page); hammering it
4×/day is rude to the operator and surfaces no new data — operator
registers churn on the order of weeks, not hours. Default 7 days; bump
shorter only when the operator demonstrably updates more often.

**Failure mode**: if the scrape raises any exception (network blip,
HTML restructure, parser bug), the handler falls back to the existing
cache and tags the source `stale` — the cron-driven NTRIP retry loop
will hit it again on the next run. If no cache exists either, status
is `error` and 0 stations ship. Behaviour parallels how
`_fetch_ntrip_source` reuses the `.sourcetable` cache on caster outage.

**Scraper module shape** (`scripts/scrapers/<name>.py`):
- Exposes a `scrape() -> dict` or `scrape(src: dict) -> dict` callable.
  The dispatcher inspects the signature: a no-arg `scrape()` is for
  single-source scrapers; the `scrape(src)` form lets one generic
  scraper serve many networks by reading the endpoint dict.
- Returns `{"source_url": str, "stations": [{"name", "lat", "lon",
  "country"?}, ...]}`.
- Raises any exception on failure — the handler catches and falls back.
- Should be self-contained (stdlib + urllib only; no project-internal
  imports beyond stdlib + the `_<name>` helper modules). Treat it like
  a thin adapter.
- One module per upstream **source-of-truth** — not one module per
  network. A scraper backed by a per-network operator portal is
  one-to-one; a scraper backed by a multi-network aggregator (M3G,
  NGS bulk) is one-to-many, with the per-network spec read from the
  endpoint dict. Separate failure surfaces still matter for the
  cache-fallback contract: each endpoint id gets its own
  `.scraped.json` cache regardless of which scraper produced it.

**Shared helpers** (`scripts/scrapers/_<name>.py`, underscore-prefixed):
- A module-naming convention for internal helpers that several
  per-source scrapers share. Four patterns are in tree:
  - `_arcgis.py` — parameterised ArcGIS REST query/paging helper.
    Per-source scrapers (`iartn`, `vector`, `wvrtn`) pass their layer
    URL + name-field; the helper is not itself a data source.
  - `_ngs_bulk.py` — one upstream file (`nad83_2011_geo.comp.txt`)
    consumed by two per-state filters (`ardot_rtn`, `ct_acorn`). The
    file fetches once per pipeline run (double-checked locking around
    an in-process cache so concurrent stale-cache scrapers don't each
    download); each state-filter scraper writes its own `.scraped.json`
    cache.
  - `_sitelog.py` — IGS-format sitelog regex + DMS-string-to-decimal
    conversion. Consumed by `sapos_bb`, `sapos_nw`, `flepos` (all three
    parse IGS sitelogs from different operator portals but the
    line-format inside is identical).
  - `_m3g.py` — M3G (gnss-metadata.eu) integration. Four endpoints
    wrapped: master GeoJSON (id→coords), metadata-list (id→update_ts
    cursor), per-project membership page (moid→9-char ID universe),
    per-station IGS sitelog (retirement flag, agency). Membership
    universe needs the retirement filter because M3G project pages
    are sticky on removals — verified against ESTPOS (10 retired
    predecessors lingered alongside successors) and WALCORS (1
    retired station). The per-station sitelog cache is incremental:
    `fetch_station_attrs(ids)` only re-fetches sitelogs whose
    `update(system-time)` changed since the last run. Disk caches
    at `data/_m3g_features.json`, `_m3g_metadata.json`,
    `_m3g_projects.json`, `_m3g_station_attrs.json` (all gitignored,
    7-day TTL except station-attrs which is incremental).
    Consumed by the generic `m3g` scraper.
- Helpers MUST NOT register themselves in `data/rtk_map.json`; only
  scrapers do. Importing a helper from a scraper module uses
  package-relative `from . import _name` syntax.

**Generic scrapers** (multi-network, `scripts/scrapers/<name>.py`):
- Currently one in tree:
  - `m3g.py` — every network registered on M3G uses this scraper.
    Endpoint config requires `country` (ISO3) plus either `moid`
    (M3G project page; preferred — auto-discovers added/retired
    stations) or `ids` (manual 4-char list, fallback when no M3G
    project exists). Retirement is auto-detected by reading each
    station's IGS sitelog (Section 3 last non-template receiver
    block's `Date Removed`). Retired IDs are filtered and logged.

    **Optional sourcetable affiliation** (`affiliation_from: "<ntrip_id>"`,
    optional `mountpoint_pattern` regex): intersects the M3G universe
    against physical mountpoints currently in the sibling NTRIP
    endpoint's cached sourcetable. Catches operator-side retirements
    M3G hasn't reflected yet — sourcetable drops a station the moment
    it stops broadcasting RTCM; M3G project pages can lag months. Soft
    fall-back: missing sourcetable or no mountpoint matches → full
    M3G universe. Default pattern `^([A-Z0-9]{4})` captures IGS-style
    4-char prefixes from format-suffixed mountpoints
    (`CAKO_RTCM3` → `CAKO`); operators using non-standard mountpoint
    naming (SAPOS's 4-digit numerics) need a custom pattern or shouldn't
    use this flag.
- Adding a new M3G-backed network is a `rtk_map.json` data edit, not a
  scrapers/ code edit: add an endpoint of `type:"scraped"`,
  `scraper:"m3g"`, with `country` + `moid`. Add `affiliation_from`
  pointing at the sibling NTRIP endpoint's id when the operator
  publishes physical mountpoints (use the four-char `^([A-Z0-9]{4})`
  default unless you verified the operator uses a different naming).

## When to edit this file

Adding, removing, or retuning a network is **not** a `.py` edit any
more — it is a data edit in `../data/rtk_map.json`. See
`../data/rtk_map.proc.md` for the pipeline-operation rules (status→
endpoints sweep, filter flag overrides, multi-endpoint setup,
port-picking, after-edit checks).

Edit `fetch_stations.py` when the script's own behaviour needs
adjusting:

- NTRIP protocol / sourcetable shape evolves (new fields, new STR
  layout, new transport quirks).
- Parser needs a new carrier class, format mapping, or coordinate
  normalisation.
- Fetch transport needs a new fallback (raw NTRIP/1.0 TCP was added
  when modern HTTP clients started failing on the caster's
  `BadStatusLine`).
- stations.json schema gains an operational field (e.g. per-endpoint
  status detail), or the merge rules across endpoints change.

## Coord overrides (operator-published bad coords)

Some casters publish wrong or placeholder antenna coords (Trimble Pivot
Platform installs are repeat offenders; NPS had 22 sites off by 30–4700
km, ERGNSS ICOL0 rounds 1-decimal sloppily so the truth falls outside
the uncertainty rectangle). Per-station overrides live in
`../data/coord_overrides.json`.

Entry shape:
```json
{ "mountpoint": "NAME", "bad": {"lat": X, "lon": Y},
  "fix": {"lat": X', "lon": Y'[, "latPrec": N, "lonPrec": N]},
  "note": "why + provenance" }
```

`parse_sourcetable` loads the file once at import (`COORD_OVERRIDES`) and
replaces coords (and optionally precision) whenever **all three** —
mountpoint name, parsed lat, parsed lon — match an entry exactly. Float
equality holds because the parser stores the same IEEE-754 value as the
JSON loader for any short decimal the operator publishes; the `bad`
field must match the post-`0..360 -> ±180` normalised lon.

Triple-match guard means a stale override silently stops firing the
moment the operator fixes their sourcetable — no quiet rewrite of good
data. Per-source log gains a `, N corrected` suffix when any entries hit.

## stations.json source-record schema

Operational fields only — fetched / runtime state. Editorial fields
(`label`, `region`, `access`, `registration`, `note`, `country`, ...)
live in `../data/rtk_map.json` and are read by `index.html` via
`markersById[sid]` at render time. Do not re-introduce them here; the
dual write was cleaned out to eliminate drift. Current source-record
keys: `url`, `credentials`, `near`, `user`, `pass`, `userNote`,
`status`, `fetched_at`, `last_ok`, `stations`.

## Post-process / DGPS filter

`parse_sourcetable` drops two non-RTK stream classes that some Trimble
Pivot casters publish alongside real-time RTK streams:

- **`format == "RAW"`** — raw observation broadcast for RINEX-style
  post-processing. No standard rover consumes RAW in real time.
  Trimble Pivot casters publish `*_RAW` mountpoints next to every
  `*_RTCM3.x` variant (CROPOS does this for all 35 physical stations).
- **`format == "RTCM 2.x"` AND `format-details` contains `PBS`** —
  Trimble Pivot's DGPS-targeted variant. Real RTCM 2.x RTK uses
  messages 18/19/22/23/24/59; the PBS (Position Broadcast Service)
  auxiliary message is RTCM 3 territory and signals the operator
  intends this stream for DGPS rovers, not RTK. CROPOS `*_DPS_23`
  matches. PBS *alongside* `RTCM 3.x` is the normal Trimble Pivot
  RTK config (nps_cors, kycors, sapos_*) — those are kept.

Counted as `dropped_postproc` in per-source log: `, N post-process`.

## Per-station `vrsRequired`

Stations parsed from an endpoint with `"vrs_required": true` in
`../data/rtk_map.json` carry `"vrsRequired": true` in their per-station
record. `index.html` renders them with a smaller pin and a popup that
suppresses the usual Server/Port/Mountpoint copy block (the mountpoint
name is not a valid connect string — the operator only allows VRS),
replacing it with the network's VRS endpoint URL and a "feeds into
VRS" line. Omitted when false to keep diffs small.

The flag rides on the per-endpoint config so a future case where one
network mixes connectable stations on one endpoint with VRS-required
stations on another endpoint Just Works without further plumbing.
Per-station overrides are not implemented yet but the per-station
shape leaves room.

`station_fingerprint` includes `vrsRequired` so toggling the flag on
an existing endpoint triggers a stations.json rewrite (without it the
"unchanged data" short-circuit would keep the old un-flagged record).

## After-edit checks

```sh
# Module-load smoke test:
python -c "from scripts.fetch_stations import NETWORKS, SOURCES; print(len(NETWORKS), len(SOURCES))"

# Local dry-fetch when network is available (fails open in sandbox):
python scripts/fetch_stations.py
# Expected stdout per endpoint: "[sid] fetched N stations (dropped X DGNSS, Y invalid[, Z net-sol])"
```
