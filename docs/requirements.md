# Product spec — ntrip-mountpoint-map

## Product statement

A map of **free NTRIP sources delivering better than ~50 cm positioning
accuracy**, globally. If a user only needs ~20–40 cm, the banner points
them at **Galileo HAS** (free, global, no signup, receiver-level); this
site is for users who need better than HAS.

## Target users

- **Discovery mode:** hobbyists or small shops (<20 people) who need
  better-than-phone GPS and don't yet know what NTRIP / RTK / NRTK is.
  They need to learn what exists, what's free, what's nearby, and whether
  any of it meets their needs.
- **Migration mode:** users with an inherited configuration whose old
  mountpoint no longer works. They know **where** geographically they
  need coverage, but not necessarily the mountpoint name.

**Not** the target: enterprise / B2B with budget for commercial VRS
(HxGN SmartNet, Trimble VRS Now, Leica SmartNet, etc.).

## Out of scope

- Commercial / paid caster networks.
- Sub-metre DGNSS-only mountpoints (dominated by free Galileo HAS).
- Raw-observation networks without real-time RTK (EPN / EUREF-IP;
  those are for post-processing).
- Per-user authentication, account creation, saved configurations.
- Mobile-app or native clients; this is a single static page served
  from GitHub Pages.
- Text search for mountpoint names. Users know where they need coverage.

## Data pipeline

GitHub Actions workflow (`.github/workflows/update-stations.yml`) — runs four
times a day (01/07/13/19 UTC) plus on `workflow_dispatch`:

1. Fetch sourcetables from each configured caster (see `SOURCES` in
   `scripts/fetch_stations.py`).
2. Parse STR lines. Drop `carrier == 0` (DGNSS-only). When the carrier
   field is empty and format begins with `RTCM 3.x`, infer `carrier = 2`
   (rtk2go publishes most entries with blank carrier — required to
   retain them). Drop mountpoints where `nmea == 1` — the defining trait
   of VRS/iMAX/MAC/FKP/NEAREST streams, which have no fixed antenna and
   report a fake reference coordinate. Sources where the caster
   misconfigures physical stations as `nmea=1` get `"nmea_filter": false`
   in `SOURCES` (currently rtk2go and GeoRTK).
3. Tag each station with `carrier` (1 = L1, 2 = L1+L2, 3 = tri-band),
   `carrierInferred` flag, `format`, `legacyFormat` (RTCM 2.x), and
   `country`.
4. If the parsed station fingerprint is unchanged since the last commit,
   exit without writing.
5. Otherwise write raw sourcetables, `data/stations.json`, commit to
   `main`. The push step uses a 3-attempt rebase-retry loop to handle
   concurrent PR merges.
6. If a caster is unreachable, reuse its previous raw sourcetable on
   disk so a transient outage doesn't wipe known-good data.

### JSON shape

```json
{
  "updated": "2026-04-19T20:15:22+00:00",
  "scope": "free NTRIP sources delivering better than ~50 cm",
  "sources": {
    "<sourceId>": {
      "url": "http://.../",
      "status": "ok" | "stale: ..." | "error: ...",
      "fetched_at": "...",
      "stations": [
        { "name": "...",
          "lat": 0.0, "lon": 0.0,
          "latStr": "...", "lonStr": "...",
          "carrier": 1 | 2 | 3,
          "carrierInferred": false,
          "format": "RTCM 3.2",
          "legacyFormat": false,
          "country": "XXX", "fee": "N" }
      ]
    }
  },
  "networks": [
    {
      "id": "...", "name": "...", "country": "...",
      "type": "single-base" | "nrtk",
      "access": "free" | "registration" | "category" | "restricted",
      "registrationUrl": "...",
      "coveragePolygon": null | [[lat, lon], ...],
      "stationIds": ["..."]
    }
  ]
}
```

`networks` is currently empty; schema anticipates future NRTK ingestion.

## Visual design

### Zoom bands

- **z ≥ 10** — detailed view. Per-station dots with labels, accuracy
  rectangles, full popups.
- **z 6–9** — dots (no labels, no accuracy boxes) + coverage raster
  (translucent). Popups on click.
- **z ≤ 5** — coverage raster only. No dots.

Thresholds are constants at the top of `index.html` (`ZOOM_DETAIL`,
`ZOOM_DOTS`).

### Why accuracy rectangles at close zoom

Sourcetables report station coordinates with variable decimal precision
(some entries round to 2 decimals ≈ 1 km, some to 5 ≈ 1 m). If we dropped
a pin at the reported point without context, a station whose caster
listed `47.25, 8.50` could land in the middle of a lake, up a cliff, or
in a supermarket car park. First-time users seeing a physically
implausible pin location **lose trust in the whole dataset**.

The dashed rectangle drawn around each pin at close zoom encodes the
width of the reported-precision box: the station is somewhere inside it,
not necessarily at the centre. Derived from the coordinate string
(`latStr`, `lonStr`) — not a configurable quantity.

Only shown at z ≥ 10 where it's readable without dominating. At wider
zooms the coverage raster dominates and per-station precision is
irrelevant.

### Coverage raster (canvas distance field)

`CoverageLayer` is a `L.GridLayer` that renders per-tile canvas raster
as a distance-to-nearest-station field:

- **Pass 1**: each station within range paints a white radial gradient
  with linear alpha (1 at centre, 0 at `R_FLOAT` = 100 km). Composited
  with `globalCompositeOperation = 'lighten'`, so each pixel's alpha
  ends up = max across contributing stations = `1 − distance_to_nearest /
  R_FLOAT`.
- **Pass 2**: `getImageData` / JS loop / `putImageData` maps that alpha
  through a 256-entry `COVERAGE_LUT` to discrete distance bands:

| Band         | strength    | Colour              | Meaning                    |
|--------------|-------------|---------------------|----------------------------|
| < 10 km      | > 0.9       | green               | cm-RTK excellent           |
| 10–30 km     | 0.7 – 0.9   | yellow-green        | cm-RTK good                |
| 30–50 km     | 0.5 – 0.7   | amber               | marginal / float           |
| 50–100 km    | 0.01 – 0.5  | pale red            | float decimetre, multi-band only |
| > 100 km     | < 0.01      | transparent         | out of usable range        |

KDBush-backed per-tile spatial query restricts the alpha pass to
stations whose 100 km circle can reach the tile bbox (lon-pad scales
with `cos(lat)`).

### NRTK rendering (scaffolded, no data yet)

When `networks[].type == "nrtk"` is present in the JSON:

- Translucent coverage polygon fill.
- Clickable centroid marker; popup shows name, access terms, registration
  URL, member-station list.
- At close zoom, member base stations still render as normal dots.

Polygon source: **concave hull** of member stations, computed in the
Python workflow. Per-network override to a manually defined polygon via
a config file when the hull is inadequate.

### Country-level markers

For countries where no physical station pins appear, a country-centroid marker
communicates what is known. Four tiers:

| Marker | When shown | Hobbyist message |
|---|---|---|
| Coloured VRS circle | In-pipeline VRS-only network, working | Sign up — corrections exist, no fixed antennas |
| Grey VRS circle | Free network confirmed; endpoint not yet in pipeline | Something free exists here; we haven't connected it yet |
| Circled **?** | Paid, restricted, or existence unverified | Dead end or legwork required — popup explains |
| Nothing | Not investigated, or genuinely nothing confirmed | — |

Tier assignment is stored in the `tier` field of `data/country_markers.json`
(derived from `status` in `docs/networks.md`):

- `vrs` + live pipeline data → coloured circle (same colour as source in toggle panel)
- `vrs` + stale or never-fetched → grey circle (falls through automatically)
- `deferred` (free; endpoint withheld or not found) → grey circle
- `info` (`paid-affordable`, `paid`, `restricted`) → **?** marker
- No entry, or no public NTRIP ever confirmed → no marker

The grey circle reuses the existing stale/grey visual language and is the most
colorblind-safe encoding (achromatic vs. coloured, no hue dependency).

A lock icon was considered for paid/restricted but rejected: in a map covered
with rtk2go and Centipede volunteer pins, a lock at country-centroid scale reads
as "the nearby stations are locked" rather than "this country has no free
network." The **?** is unambiguous and self-documents as "click for info."

The grey VRS circle is the same shape as the coloured in-pipeline circles; the
grey variant extends the same idiom to the not-yet-ingested case so that the
deferred free tier (Portugal, Lithuania, Thailand, Uganda…) is visually
recognisable as "same kind of thing, not done yet."

Data backing: `data/country_markers.json` — static file, currently 120 entries.
Fields: `id`, `name`, `region`, `country` (ISO 3166-1 α-2), `lat`, `lon`,
`tier`, `source_id` (vrs tier only — links to `stations.json` for colour and
registration URL), `pins` (boolean; true = physical station pins already on
map), `access`, `registration`, `yearly_cost`, `stations_declared`, `note`.
Frontend suppresses a `vrs`-tier circle when `pins` is false and the source
currently has stations in the live feed (network regained physical pins).
`pins:true` entries always show a VRS circle regardless of station count.
**Maintained by hand; not generated by the pipeline.** When adding or removing
a network in `docs/networks.md`, update this file in the same commit: paid or
restricted networks get an `info` marker; free networks whose endpoint is not
yet in the pipeline get a `deferred` marker; new in-pipeline VRS-only sources
get a `vrs` marker. Each network gets its own marker, positioned at the
geographic area it covers (regional networks → region centroid, nationwide
networks → country or company headquarters).

### Onboarding banner

- Top-of-viewport horizontal strip, full width, ~56 px tall.
- Scope sentence + HAS nudge + expandable "learn more" (inline panel).
- Dismiss × on the right. Dismissal persisted in `localStorage` under a
  versioned key so a future content change re-surfaces it.

### Popups

Plain language, minimised:

```
<name>
~1 cm accuracy within 10 km, good to 30 km, usable to 50 km.
[Legacy RTCM 2.x warning if legacyFormat]
Server:     <host>          [copy]
Port:       <port>          [copy]
Mountpoint: <name>          [copy]
[repeat per source the station is in]
```

### Toggles

Collapsible panel, top-right:

- **Source** checkboxes generated from whatever is present in
  `data.sources` — one per configured caster.
- **Access** checkboxes: Free / Registration / Category / Restricted
  (currently placeholder — only `free` has backing data).
- **VRS networks (N)** — master toggle + per-network rows for VRS circles.
- **Pending (N)** — master toggle + per-network rows for grey circles
  (free networks not yet in the live feed).
- **Restricted (N)** — master toggle + per-network rows for circled-?
  markers (paid or restricted networks).
- On change, re-filter stations, re-render dots + coverage raster +
  detail layer + country markers.

### User-facing help content

Two files carry user-facing copy:

- **`guide.html`** — standalone long-form primer linked from the banner.
  Audience: technical hobbyists with no GNSS background (citizen
  science, amateur archaeology / paleontology, botanical and wildlife
  monitoring, automation tinkering). UK spelling. Sections cover scope,
  why standalone GPS drifts, hardware compatibility and buying guide,
  using the map, dead-mountpoint replacement, step-by-step connecting,
  antenna placement, DIY base station, real-world examples, glossary.
- **`data/help_topics.json`** — searchable in-map help surfaced via the
  Help button. ~22 interlinked topics across eight categories
  (Getting started, Before you start, Connect, Concepts, Migration,
  Troubleshooting, Advanced, Meta) plus four popovers shown on map
  elements. Each topic exposes `lead` / `body` / `deep` / `related` so
  readers progress from a one-sentence answer to detailed explanation.
  Canonical entries: `is-this-for-me` (use-case catalogue, audience
  anchoring, SEO) and `antenna-placement` (multipath checklist).

Numeric figures (TTFF, baseline ranges, accuracy targets, prices) must
match between the two files. The technical reference for those numbers
is `docs/gnss-ai-guide.md`. Use "GPS" colloquially in narrative prose
but "GNSS" where the wording is structurally about multi-constellation
hardware or signals — L1 and L2 are not "GPS frequencies" because
Galileo E1 and E5b sit on those same bands.

## Tech choices

- **Leaflet 1.9** + **OpenStreetMap** tiles.
- **KDBush v3** (UMD, ~3 KB from unpkg) for spatial queries.
- **Pure JS** in a single `index.html`. No build step.
- **Python stdlib** only for the workflow script.
- **IP geolocation** via ipwho.is (no permission prompt, ~city accuracy).
- **No marker clustering** library — zoom-band swap + viewport cull +
  canvas raster carry the rendering load.

## Deferred

- Validation of FReDNet and RTKdata.online after first real workflow
  run post-merge.
- Registration-gated casters (ASG-EUPOS, FLEPOS, WALCORS, SAPOS, CROPOS,
  IBGE RBMC-IP, AUSCORS, PositioNZ) — need credentials as Actions
  secrets.
- Real NRTK polygon data (concave-hull computation in the workflow).
- Colourblind-friendly palette tuning.
- `precLabel` hardcoded at `cos(47°)`; fix to use station latitude.
- Pseudo / dynamic mountpoints like Centipede's `NEAR` — auto-route to
  nearest base from rover's NMEA-GGA. Not fixed geographic points; need
  a separate visual (virtual entry in the toggle panel, not a map marker)
  and a flag in the source schema.
