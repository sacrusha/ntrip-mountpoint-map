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
  those are for post-processing) — excluded from the ingestion pipeline.
  Substantial free national RINEX networks (e.g. INEGI RGNA) are
  documented in `ntrip_research/` and `rtk_inventory.md`, and surface on
  the map as `weird` markers carrying a "free RINEX, no NTRIP" note so
  target users know free post-processing data exists in their country.
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
  rectangles, station details card on click.
- **z 6–9** — dots (no labels, no accuracy boxes) + coverage raster
  (translucent). Country-level glyph markers stay visible for the first
  two of these levels and hide further in, so the country-to-stations
  hand-off is gradual rather than abrupt.
- **z ≤ 5** — coverage raster + country-level glyph markers + coverage
  rings. No dots.

Thresholds are constants at the top of `index.html` (`ZOOM_DETAIL`,
`ZOOM_LABELS`, `ZOOM_DOTS`, `ZOOM_TAGS_HIDE`).

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
- Clickable centroid marker; the station card shows name, access terms,
  registration URL, member-station list.
- At close zoom, member base stations still render as normal dots.

Polygon source: **concave hull** of member stations, computed in the
Python workflow. Per-network override to a manually defined polygon via
a config file when the hull is inadequate.

### Country-level markers

For countries where no physical station pins appear, a country-centroid marker
communicates what is known. Four visual treatments:

| Marker | When shown | Hobbyist message |
|---|---|---|
| Coloured VRS ring + dark-green antenna at centroid | Free VRS network whose caster was reachable on the most recent fetch (live). Station count irrelevant — VRS-only casters that publish only virtual mountpoints qualify. Ring is visual-only; clicks land on the antenna. | Sign up — corrections exist, no fixed antennas |
| Bright-green antenna only (no ring) | Free per-station (RS) network whose caster was reachable on the most recent fetch. Caster publishes a list of physical bases; user picks the closest. | Sign up — pick a base near you |
| Grey ring + grey antenna at centroid | Free network whose endpoint is unknown / registration-gated, or a known free network where the most recent fetch failed (≥3 days since last successful contact) | Something free exists here; we couldn't reach the caster recently |
| Circled **$** / **✕** / **?** | Substantial national-scale network: paid, restricted, or info-only (jamming, non-NTRIP, announced-not-live, etc.). | Dead end or legwork required — card explains |
| Nothing | None of the above (investigation found nothing operational, post-processing-only, defence-internal, regional surveying company too small to flag, etc.). Post-processing-only government networks still get survey + `rtk_inventory.md` entries even though they produce no marker. | — |

The data model is **two orthogonal axes** plus runtime data presence.

`tier` (in `data/rtk_map.json`) describes the network's nature for a hobbyist:

- `free` — no fee to use. With `vrs:true` and live ingested data, renders
  as a coloured ring + dark-green centroid antenna. Without `vrs`, with
  live ingested data, renders as a bright-green centroid antenna (no
  ring) — the per-station/RS-network case. With no live data (stale,
  unknown endpoint, registration-gated), renders as grey ring + grey
  antenna. The `note` field for a free marker without ingested data
  should be able to truthfully begin with "N stations, free."
- `paid` — substantial national-scale paid commercial operator (swipos,
  CPOS, US-state DOTs, HEPOS, ROMPOS, AGROS, CRTN). Renders as **$** glyph;
  colour is a hint derived from `yearly_cost_normalized` (green = affordable,
  red = expensive).
- `restricted` — substantial national-scale operator with no hobbyist path
  at any price (TxDOT CORS, KazGeoDesy, DVRS). Renders as **✕** glyph.
- `weird` — anything interesting to a target user that doesn't fit the
  other tiers. The freeform note carries the explanation and is the
  value proposition of this tier. Examples: non-standard NTRIP
  (qc_mern), active jamming/spoofing (apn), infrastructure too sparse
  to work (igrs), free RINEX-only with no real-time NTRIP (rgna_mx,
  ign_gt_cors), network announced/under construction but not yet
  operational (sen_cors, fiji_dlss_cors), government CORS distributed
  only via licensed commercial resellers (os_net), micro-state with no
  local service (li_cors, sm_cors). Renders as **?** glyph. The card
  hides the access/coverage labels for this tier (info-only context).

`vrs` (boolean flag) is **orthogonal** to tier. `vrs: true` means the network
delivers VRS / network-RTK streams. Free SAPOS, paid swipos, and restricted
DVRS all carry the flag. Single-base networks and unknown-stream-type entries
omit it. Absence means nothing about access.

Whether station data is ingested is a third axis, runtime-derived from
`data/stations.json`. The renderer uses (tier × vrs × data-presence) to pick
visuals:

Routing keys off `staleness` only (whether the caster was reachable on
the most recent fetch — within ~3 days for `live`, 3–7 for `stale`,
≥7 or never for `dead`). Station count does not gate the colour; a
live VRS-only caster with zero ingested physical stations is still
green.

- `tier:free + vrs:true + live` → coloured ring + dark-green antenna
- `tier:free + vrs:true + stale or dead` → grey ring + grey antenna
- `tier:free + no vrs flag + live` → bright-green antenna (no ring)
- `tier:free + no vrs flag + stale or dead` → grey ring + grey antenna
- `tier:paid` → **$** glyph (colour from `yearly_cost_normalized`: green = affordable, red = expensive); `tier:restricted` → **✕** glyph; `tier:weird` → **?** glyph

Country-level glyph markers (paid tiers + free-network antennas) fade
out as the user zooms in (see "Zoom bands" above). Coverage rings stay
visible at all zoom levels.

No entry → no marker. This covers the case where a country was
investigated and found to have nothing of value to a target user —
closed defence networks, abandoned programmes, niche scientific
archives with no PPK signal, tiny private surveying companies. Absence
of a marker is itself a signal: "we looked, found nothing useful."
Don't add a marker just to mark the investigation; the ntrip_research/
prose is the canonical record. Free RINEX-only networks and other
"interesting but not directly usable" cases get a `weird` marker, not
silence.

Grey reuses the existing stale visual language (achromatic vs. coloured)
and is the most colorblind-safe encoding (no hue dependency).

A lock icon was considered for paid/restricted but rejected: in a map covered
with rtk2go and Centipede volunteer pins, a lock at country-centroid scale reads
as "the nearby stations are locked" rather than "this country has no free
network." The **$** / **✕** / **?** glyphs are unambiguous and self-document.

Grey ring/antenna shares the shape of the coloured free-network ring/antenna;
the grey variant extends the same idiom to the not-yet-ingested case so that
free networks without published endpoints (Portugal, Lithuania, Thailand,
Uganda…) read as "same kind of thing, not done yet."

Data backing: `data/rtk_map.json` — static file, currently **122 entries**.
Fields: `id`, `name`, `region`, `country` (ISO 3166-1 α-2), `lat`, `lon`,
`tier` (one of `free`, `paid`, `restricted`, `weird`),
`vrs` (optional boolean; `true` if the network delivers VRS / network-RTK
streams), `source_id` (links to `stations.json` for colour and registration
URL when the source is in the pipeline), `pins` (boolean; true = physical
station pins already on map), `access`, `registration`, `yearly_cost`,
`stations_declared`, `note`.

The **`note` field is user-facing** — it renders in the marker's station card
on the map and is read by hobbyists. Plain language; expand or avoid acronyms
("permanent GPS reference network" not "CORS"); never mention internal
classifications like the `$200/yr cutoff`; never include audit-document
phrasing like "no English pricing page" or "±2 cm horizontal accuracy at 95 %
confidence." A good note tells the user what they need to know to act.
Frontend suppresses the country-level ring + centroid antenna for a
`tier:free + vrs:true` entry when `pins` is false and the source currently
has stations in the live feed (network is fully covered by physical pins).
`pins:true` entries always show a VRS ring + antenna regardless of
station count.
**Maintained by hand; not generated by the pipeline.** When adding or removing
a network in `docs/rtk_inventory.md`, update this file in the same commit: pick
the tier per the rules above (`free` / `paid` / `restricted` / `weird`),
add `"vrs": true` if the network delivers VRS
streams, and otherwise omit the flag. Each network gets its own marker,
positioned at the geographic area it covers (regional networks → region
centroid, nationwide networks → country or company headquarters).

### Onboarding banner

- Top-of-viewport horizontal strip, full width, ~56 px tall.
- Scope sentence + HAS nudge + expandable "learn more" (inline panel).
- Dismiss × on the right. Dismissal persisted in `localStorage` under a
  versioned key so a future content change re-surfaces it.

### Station card

Two presentation modes for the same payload, dispatched per click via
`matchMedia('(pointer: coarse)')`:

- **Desktop / pointer:fine** — marker-anchored Leaflet popup (the
  long-standing behaviour). Vertical desktops keep this path because
  pointer is the discriminator, not viewport size.
- **Touch / pointer:coarse** — `#card-sheet` overlay anchored to the
  bottom of the viewport. Centred fixed-width (~420 px) above 768 px
  wide; full-width strip across the bottom on phones. No auto-pan.

Click-through is unified: any marker (station, network centroid,
paid-tier glyph) plus the map-click radius search routes through
`showCard(html, latlng)`. Plain language, minimised body for a station
hit:

```
<name>
~1 cm accuracy within 10 km, good to 30 km, usable to 50 km.
[Legacy RTCM 2.x warning if legacyFormat]
Server:     <host>          [copy]
Port:       <port>          [copy]
Mountpoint: <name>          [copy]
[repeat per source the station is in]
```

Network and paid-tier hits show name + access tier + region + note +
registration link (info-tier hides the access/region lines). Single
card surface at a time: opening the help drawer, ESC, map-click on
empty space, or clicking a different marker all dismiss / replace.

### Toggles

Collapsible panel, top-right. Default expanded; user can collapse via the
corner ✕ or a right-swipe (≥60 px, horizontal-dominant). When collapsed,
a fixed top-right ☰ handle (44 × 44 px on coarse pointers) restores it.
State persists across sessions in `localStorage`.

- **Source** checkboxes generated from whatever is present in
  `data.sources` — one per configured caster.
- **Access** checkboxes: Free / Registration / Category / Restricted
  (currently placeholder — only `free` has backing data).
- **Tags** section (header):
  - **VRS networks (N)** — master toggle + per-network rows for the
    coloured VRS ring + dark-green centroid antenna.
  - **RS networks (N)** — master toggle for bright-green per-station
    antennas (free networks where you pick a base manually).
  - **Stale (N)** — master toggle for grey ring + grey antenna
    (free networks with no fresh data).
  - Visual separator, then per-tier toggles for **Affordable** / **Paid**
    / **Restricted** / **Info** glyph markers.
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
- `precLabel` hardcoded at `cos(47°)`; fix to use station latitude.
- Pseudo / dynamic mountpoints like Centipede's `NEAR` — auto-route to
  nearest base from rover's NMEA-GGA. Not fixed geographic points; need
  a separate visual (virtual entry in the toggle panel, not a map marker)
  and a flag in the source schema.
