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
  country_markers.json        # Static; country-level markers (104 entries, 3 tiers).
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

## Current state (2026-04-22, branch claude/add-russia-china-coverage-WMPJr)

**65 sources, ~5,472 stations** in `data/stations.json`. Sources:
rtk2go, Centipede, FReDNet, GeoRTK, 14× SAPOS Länder, ERGNSS, APOS (AT),
AUSCORS, PositioNZ, SatRef HK, InaCORS, TrigNet, RBMC-IP, RAMSAC, REGNA-ROU (UY),
FLEPOS, WALCORS, SPSLux, ASG-EUPOS, CROPOS, ESTPOS, LatPos, IGAC, EarthScope NOTA,
MIRAI, CORS-KOREA, IceCORS, KSA-CORS,
**Italian regional**: SPIN3, GPS-UMBRIA, GNSS Abruzzo+Lazio, SIT Puglia, GNSS Campania,
**US state DOT (physical+VRS)**: WISCORS, FPRN, ARDOT RTN, MaCORS, VECTOR VT,
AzCORS, GCGC RTN, AlCORS, ORGN, MSRN, NYSNet, InCORS, IARTN,
**US state DOT (VRS-only)**: KyCORS, MnCORS, ODOT RTN, MoDOT RTN, WVRTN, MaineDOT.

**Source config in one place:** `color` and `label` live in `SOURCES` in
`fetch_stations.py` and are emitted to `stations.json`. `SOURCE_COLORS` /
`SOURCE_LABELS` in the frontend are populated from JSON at load time — not
hardcoded. `SOURCE_AUTH` (credentials and popup hints) stays in `index.html`.

**VRS / network-solution filtering:** `parse_sourcetable` now drops mountpoints
where the NTRIP `nmea` field (field 11) is `"1"`. NMEA=1 means the caster
requires the rover to send its position, which is the defining trait of VRS,
iMAX, MAC, FKP, and NEAREST streams — they have no fixed antenna and report a
fake reference coordinate. Physical single-base stations always have NMEA=0.
This drops 104 virtual mountpoints across sources that the old `filter_vrs`
heuristic (same-coordinate pile) couldn't catch: FReDNet (−11), IGAC (−17),
InaCORS (−4), REGNA-ROU (−19), SAPOS HE (−4) / RP (−11) / SL (−6), SPSLux
(−17), IceCORS (−12), Centipede (−2 NEAR/NEAR4), CORS-KOREA (−5 format
variants).

Two casters incorrectly tag their physical stations with NMEA=1 and get
`"nmea_filter": False` in `SOURCES`: **rtk2go** (caster-wide misconfiguration
— all 764 physical stations tagged nmea=1) and **GeoRTK** (2 physical u-blox
F9P stations). Any future source with the same issue gets the same exception.

**VRS-only networks** (CROPOS, ASG-EUPOS, FLEPOS, WALCORS, ESTPOS, LatPos,
KSA-CORS, 10 SAPOS states, + 6 US state DOT: KyCORS, MnCORS, ODOT RTN,
MoDOT RTN, WVRTN, MaineDOT) expose only virtual mountpoints — correctly
dropped to 0 stations by the nmea filter or `filter_vrs()`. Rendered as
coloured VRS circles when live data is present; stale or never-fetched sources
fall through to grey circles. The old hardcoded `VRS_NETWORKS` array has been
replaced by `buildCountryMarkers()`, which reads all three tiers directly from
`data/country_markers.json`. APOS (AT) and all Italian regional networks are
physical-coord-vrs — show as regular pins with `pins:true` VRS badges. Full
NRTK polygons are deferred.

**`data/country_markers.json`:** static file (not pipeline-generated) with
104 entries across three tiers — `vrs` (23 VRS-only circles + 39 pinned-network
fallbacks with `"pins":true`), `deferred` (14 grey circles: ReNEP, LitPOS,
UGRF, ETCORS, DOL Thailand, Italian deferred regionals, ACORN, ZAKPOS, GPSBru),
`info` (28 circled-? markers: paid and restricted networks). All three tiers
are live in `index.html` via `buildCountryMarkers()`. Toggle panel shows
"VRS networks (N)", "Pending (N)", "Restricted (N)" sections.
Design spec in `docs/requirements.md` § Country-level markers.

**`yearly_cost` field in `docs/networks.md`:** all paid and paid-affordable
entries carry a `**yearly_cost**:` field for reference (not yet in JSON).

**Longitude normalisation:** `parse_sourcetable` now normalises 0-360°
longitudes to ±180 (ERGNSS: 114/128 affected; AUSCORS: 2/808). `lon` is
included in `station_fingerprint` so the next pipeline run rewrites JSON.

**5 sources timing out in CI:** FLEPOS, WALCORS, ESTPOS, LatPos, KSA-CORS.
Handled gracefully by fallback-to-cached-sourcetable. See `**investigate**:`
in `docs/networks.md`.

**Non-standard ports in pipeline:** spslux:5005, inacors:2001, latpos:5001,
alcors:10011, mncors:9000, orgn:9879, msrn:10700, incors:10000. All handled
by standard urllib/socket — no special-casing needed.

**Bare IPs in pipeline:** vector (`20.185.11.35`), orgn (`167.131.0.205`),
odot_rtn (`156.63.133.115`). Valid URLs, handled normally.

**EarthScope overlap:** US state DOT networks (especially ORGN, MSRN, NYSNet,
AzCORS, MnCORS) may share physical stations with EarthScope NOTA, producing
duplicate pins at identical coordinates. VRS-only state networks avoid this.
Deduplication is a future task.

**Documentation rule — no direct email addresses in docs:** `docs/networks.md`
and `docs/country-survey.md` must not contain bare `user@domain` email addresses.
Link to the relevant website instead; the website can describe a sign-up process
that involves sending an email. Applied retroactively to all entries in this session.

**Russia (RU) and China (CN) country-survey entries** are now fully documented
(were 2–3 line stubs). RU: covers СДКМ/SDCM (SBAS only), ФАГС/ВГС (no public
NTRIP), and four commercial networks (EFT-CORS, RTKNet, HIVE, ГЕОСПАЙДЕР) with
₽ pricing and host:port detail plus post-2022 sanctions context. CN: covers
测量法 legal barrier to all government/provincial CORS, BGAS/provincial CORS
(licensed orgs only), and three commercial services (Qianxun ¥3,600/yr,
China Mobile CORS ¥3,600/yr, Tencent RTK ~¥998/yr — status unconfirmed).
Nine new `docs/networks.md` entries added: `tencent_rtk` (paid-affordable),
`eft_cors`, `rtknet`, `hive_cors`, `geospider` (RU paid), `qianxun`, `cmcc_cors`
(CN paid), `sdcm`, `bgas_china` (rejected). No pipeline additions — no free
hobbyist NTRIP exists in either country.

**Open / deferred (by priority):**
1. NRTK / VRS coverage polygons: rendering scaffolded (`networks: []` in JSON)
   but no polygon data ingested. VRS stopgap markers are the placeholder.
2. Network endpoint verification — see `docs/networks.md` `**investigate**:`
   (5 CI-failing) and `**missing**:` (11 deferred: renep, litpos, thailand_dol,
   zakpos; Italian: tpos, stpos, gnss_veneto, gnss_liguria, sicilianet,
   molise_gnss; US: acorn).
3. EarthScope overlap deduplication — US state DOT physical stations may
   duplicate EarthScope NOTA pins.
4. `SOURCE_AUTH.openNote` strings are derivable from `access`+`registration`
   already in JSON; could be dropped from `index.html`. Deferred — requires
   popup refactor.
5. Uganda UGRF CORS (ugrf.mlhud.go.ug, 78 stations, free as of 2024) — public
   NTRIP endpoint not discoverable without completing registration. Revisit if
   host:port is confirmed publicly.

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

- **rtk2go carrier field:** blank for most entries even on RTCM 3.x MSM
  streams. Parser infers `carrier = 2` when format starts with `RTCM 3`;
  without this, only ~2 of 800+ rtk2go mountpoints survive. Preserve this.
- **rtk2go nmea field:** all entries (including physical single-base stations)
  have `nmea=1`. This is a caster misconfiguration. `"nmea_filter": False` in
  SOURCES prevents the nmea filter from dropping the entire network. If you
  remove that flag, rtk2go drops to 0 stations.
- **Workflow push race:** cron runs can race human PR merges. The push step
  has a 3-attempt rebase-retry loop; don't simplify it.
- **Leaflet `L.DomUtil.create` signature:** third arg is a DOM parent, not a
  className. Passing a string throws inside `addTo` and silently freezes the
  page. Use `L.DomUtil.create('div')` with no extra args.
- **`preferCanvas: true`** — required so `L.circleMarker` renders to canvas;
  without it, per-station SVG blows the DOM budget at ~2k+ stations.
- **Country marker state keys:** VRS uses `state[sid]` (bare) so that
  `pins:true` networks share the same key as their physical-station checkbox —
  adding a `vrs_` prefix would silently decouple them. Grey uses
  `state['grey:'+id]`, info uses `state['info:'+id]`. The `:` separator cannot
  appear in any id (`[a-zA-Z0-9_]`), so no collision is possible.

## Testing

- `node --check` on the extracted inline `<script>` block catches JS syntax.
- `python3 scripts/fetch_stations.py` runs the pipeline locally; sandboxed
  environments without network fall through to the cached-sourcetable path.
- No unit tests yet. A small pytest for `parse_sourcetable` would pay off the
  first time someone touches the carrier-inference rule.
