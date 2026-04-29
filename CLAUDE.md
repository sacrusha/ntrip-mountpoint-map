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
  When updating or adding entries, use the
  [`update-country-survey`](.claude/skills/update-country-survey/SKILL.md)
  skill — it bundles the tier scheme, per-country task brief, and
  agent-orchestration pattern used in the bulk audit (commit `4942fa6`).
- [`docs/global-survey.md`](docs/global-survey.md) — same for multi-country
  and global networks.
- [`docs/gnss-ai-guide.md`](docs/gnss-ai-guide.md) — technical GNSS primer
  for AI sessions; consult when needed for background. Casually referred to
  as "the AI guide".
- [`data/help_topics.json`](data/help_topics.json) — searchable user-facing
  help repository (22 interlinked topics + 4 popovers) surfaced via the
  Help button on the map. Two topics are canonical references:
  `is-this-for-me` catalogues representative hobbyist use cases (amateur
  archaeology / palaeontology, rare-plant demography, nest logging, DIY
  robot mowers, drone GCPs, RC bathymetry, OSM cm-mapping, cave entrance
  tie-ins) — the record of who the project is for; `antenna-placement`
  documents the rover-side multipath checklist that drives fix quality
  once corrections arrive.
- [`guide.html`](guide.html) — long-form standalone primer linked from
  the map banner. Audience-anchored to hobbyists; UK spelling. Numeric
  figures (TTFF, baselines, prices) must stay aligned with
  `data/help_topics.json` — both files derive from the AI guide.

## Repository layout

```
index.html                    # Single-page Leaflet app — all UI.
guide.html                    # Plain-English hobbyist primer (static page).
scripts/fetch_stations.py     # Sourcetable fetch + parse + diff.
.github/workflows/
  update-stations.yml         # Cron + workflow_dispatch, runs the Python.
data/
  stations.json               # Canonical JSON, consumed by index.html.
  country_markers.json        # Static; country-level markers (221 entries, 3 tiers).
  help_topics.json            # Static; in-map help (22 topics + 4 popovers).
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

## Current state (2026-04-29, branch claude/review-documentation-yELxu)

**66 sources, ~5,472+ stations** in `data/stations.json`. Sources:
rtk2go, Centipede, FReDNet, GeoRTK, 14× SAPOS Länder, ERGNSS, APOS (AT),
AUSCORS, PositioNZ, SatRef HK, InaCORS, TrigNet, RBMC-IP, RAMSAC, REGNA-ROU (UY),
FLEPOS, WALCORS, SPSLux, ASG-EUPOS, CROPOS, ESTPOS, LatPos, IGAC, EarthScope NOTA,
MIRAI, CORS-KOREA, IceCORS, KSA-CORS,
**Italian regional**: SPIN3, GPS-UMBRIA, GNSS Abruzzo+Lazio, SIT Puglia, GNSS Campania,
**US state DOT (physical+VRS)**: WISCORS, FPRN, ARDOT RTN, MaCORS, VECTOR VT,
AzCORS, GCGC RTN, AlCORS, ORGN, MSRN, NYSNet, InCORS, IARTN,
**US state DOT (VRS-only)**: KyCORS, MnCORS, ODOT RTN, MoDOT RTN, WVRTN, MaineDOT,
**US county-level (VRS-only)**: Mesa County RTVRN (CO).

**2026-04-29 additions (this branch)**: bulk audit of `docs/country-survey.md` against
top-120 GDP ∪ top-120 population + 42 administered territories (~232 entities). Survey
went from ~110 to **188 country/territory entries**; `docs/networks.md` from 182 to **238
network blocks**; `data/country_markers.json` from 122 to **221 markers** (+68 deferred,
+31 info). Documented `**date_added**:` field convention (per-country heading required;
per-network optional) and a Tier A/B/C entry scheme. Process codified as the
[`update-country-survey`](.claude/skills/update-country-survey/SKILL.md) skill — future
country-survey edits should use it. Commit `4942fa6` is the audit; `7b175c3` is the
skill+review pass.

**2026-04-27 additions (prior branch)**: surveyed user-supplied US-state list against
`docs/networks.md`. 13 of 17 already covered (`incors`, `kycors`, `macors`, `msrn`,
`mncors`, `gcgc_rtn`, `modot_rtn`, `nysnet`, `orgn`, `vector`, `wsrn`, `wvrtn`,
`wiscors`). Four were missing — added as documentation entries:
- `mesa_rtvrn` (US-CO): VRS-only, free with registration, 33 underlying CORS,
  `rtvrn.mesacounty.us:2101` — added to pipeline SOURCES + country_markers vrs tier;
  cache will populate on next CI run.
- `crtn` (US-CA): SOPAC California Real Time Network, paid-affordable, $100 one-time
  fee (universities/schools exempt), `132.239.152.4:2102-2105` zone-based ports,
  ~250 stations clearinghouse for SCIGN/BARD/SCIGN-Pasadena/CVSRN/OCRTN/NOTA.
  Documented; not added to pipeline (paid). info marker added to country_markers.
- `bard` (US-CA): UC Berkeley + USGS Bay Area Regional Deformation network, ~40
  stations. No independent caster — streams disseminated via `crtn` (paid) and many
  stations also archived in `earthscope` (free, in-pipeline). Documented as deferred
  with dual-access note.
- `panga` (US-WA, OR, ID): CWU Pacific Northwest Geodetic Array, ~220 PANGA + ~700
  NOTA stations. No independent public caster. Reachable via `earthscope` (free) or,
  for WA only, `wsrn` (paid). Documented as deferred.

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
**221 entries** across three tiers as of 2026-04-29 — `vrs` (63 VRS-only circles +
pinned-network fallbacks with `"pins":true`), `deferred` (~83 grey circles: free
networks not yet in the pipeline including Portugal ReNEP, Lithuania LitPOS, Thailand
DOL, the country-survey-audit additions across Africa / Caribbean / Central Asia, and
the Italian deferred regionals), `info` (~75 circled-? markers: paid and restricted
networks including swipos, CPOS, HEPOS, ROMPOS, AGROS, MONTEPOS, BiHPOS, TUSAGA-Aktif,
CZEPOS, SKPOS, MIRANET, e-GNSS, the EFT-CORS / RTKNET / HIVE / GEOSPIDER Russia cluster,
Qianxun / China Mobile / Tencent CN cluster, Dubai DVRS, Peru REGPMOC, Quebec MERN,
Israel APN, etc.). All three tiers
are live in `index.html` via `buildCountryMarkers()`. Toggle panel shows
"VRS networks (N)", "Pending (N)", "Restricted (N)" sections.
Design spec in `docs/requirements.md` § Country-level markers.
**Manual maintenance obligation:** whenever a network is added to or removed
from `docs/networks.md`, update `data/country_markers.json` accordingly. The
file is never generated by the workflow.

**Tier semantics are strict** (see `docs/requirements.md` § Country-level
markers and the `update-country-survey` skill for the full rules):
- `deferred` = a **free** national-scale service is confirmed; only the
  endpoint is the gap. The note must truthfully open with "N stations, free."
  Do not use this tier as a generic "I documented something" marker.
- `info` = a **substantial national-scale** paid or restricted operator. A
  small private surveying company with stations in a few cities does NOT
  earn a country-level marker; describe it inline in the country prose only.
- No marker = investigated, found nothing operational, or found only
  closed-government / post-processing-only / regional-too-small services.
  Absence of a marker is itself a signal — don't pad with markers for the
  sake of comprehensiveness.

The `note` field on every marker is **user-facing** (renders in map popups
for hobbyists). Plain English; expand or avoid acronyms; no internal
classifications; no audit-document phrasing.

**SEO help-topic mirror in `index.html`:** the help drawer's contents only
enter the DOM after a click, so crawlers (and Googlebot's slow JS-render
queue) never index that copy. `scripts/inject_seo_help.py` splices a
visually-hidden `<section class="sr-only">` with every topic's `q` and `lead`
between sentinel comments `<!-- SEO_HELP_START -->` / `<!-- SEO_HELP_END -->`
in `index.html`. **Run it whenever you edit `data/help_topics.json`** and
commit the resulting `index.html` change in the same commit. The script is
idempotent — re-running with no data change produces no diff. Not wired
into the cron workflow (the cron only commits `data/`); it's a manual regen
step like updating `country_markers.json`.

**`yearly_cost` field in `docs/networks.md`:** required on every paid and
paid-affordable entry. Format: local currency literal in the value, with the
USD/EUR equivalent in the country-survey prose (`(~$X/yr)` parenthetical).
Greppable for currency audits. Not yet mirrored in `data/stations.json`.

**`date_added` field in `docs/country-survey.md`:** required on every country
heading. Format: `**date_added**: 2026-04-29` on the line immediately under
`### CC — Country Name`. Bulk-only backfill passes use yesterday's date so they
are greppable separately from substantive research-driven edits — see the
[`update-country-survey`](.claude/skills/update-country-survey/SKILL.md) skill
for the convention. Optional secondary `**date_added**:` per `## id` block in
`docs/networks.md` when a network is revised independently of its country entry.

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
hobbyist NTRIP exists in either country. Seven new `data/country_markers.json`
entries added (one per network, each at its own region): `eft_cors` (Moscow),
`rtknet` (Ural/Yekaterinburg), `hive_cors` (Novosibirsk), `geospider`
(NW Russia/St. Petersburg), `qianxun` (Beijing), `cmcc_cors` (Shanghai),
`tencent_rtk` (Shenzhen).

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
6. **`country_markers.json` "deferred" tier is a misnomer — refactor pending.**
   The current name suggests "we're deferring this" but the actual semantic is
   "free service confirmed; only the host:port is the gap." The 2026-04-29
   audit revealed how easily the name misleads: ~75 markers got added under
   "deferred" for entries that were not free at all (post-processing-only,
   government-internal, defence-controlled). The audit's marker additions
   were reverted (markers back to 122; see `docs/requirements.md` § Country-
   level markers and the strict tier-rule in
   `.claude/skills/update-country-survey/SKILL.md` for the intended semantic),
   but the underlying tag should be renamed to something self-documenting
   (`endpoint-pending`, `free-pending`, or similar) and any reclassification
   of the 99 audit-introduced `networks.md` blocks should happen in the same
   pass. The audit's `networks.md` `status` field was already normalised to
   the controlled vocabulary (`in-pipeline | deferred | paid | paid-affordable
   | restricted | rejected | candidate`); re-tiering should follow that.

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

- **Write tool — use skeleton-first for large files:** Generating a large
  text block in a single Write call requires a long thinking phase that can
  exceed the ~300 s idle timeout and produce nothing. Instead: Write a skeleton
  (section headers + one-line placeholders) first, then fill each section with
  a separate Write or Edit call. Each call keeps its thinking phase short and
  the stream alive.

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

- **Theme variables — never inline a hex for muted/foreground text:** the
  `:root` block in `index.html` defines `--fg`, `--muted`, `--accent`, etc.
  with light- and dark-mode values. Inline `style="color:#555/#666/#888"` in
  popup HTML or toggle-panel rows bypasses this and renders unreadable on the
  dark `--panel-bg` (`#1e3048`). Use `color:var(--muted)` for de-emphasised
  text, `color:var(--fg)` for body, `color:var(--link)` for links. Same goes
  for any new `bindTooltip` / `L.control` — Leaflet ships defaults with
  hard-coded white; the `@media(prefers-color-scheme:dark)` block re-skins
  `.leaflet-tooltip`, `.leaflet-bar a`, and `.leaflet-control-attribution`.
  When adding a new Leaflet UI element, check whether it picks up those
  overrides or needs another rule.

- **User-facing copy lives in two files** — `guide.html` (long-form primer)
  and `data/help_topics.json` (in-map help). Numeric figures must stay
  aligned across both: TTFF 30-90 s, L1+L2 useful baseline ~30 km,
  cost-on-top ~5 MB/h mobile data, etc. The AI guide is the source of
  truth for the underlying numbers. Style rules: UK spelling
  (centimetre / metre / behaviour); use "GPS" colloquially in narrative
  prose but switch to "GNSS" wherever the wording is structurally about
  multi-constellation hardware or signals — L1 and L2 are not "GPS
  frequencies" because Galileo E1 and E5b sit on the same bands.

## Testing

- `node --check` on the extracted inline `<script>` block catches JS syntax.
- `python3 scripts/fetch_stations.py` runs the pipeline locally; sandboxed
  environments without network fall through to the cached-sourcetable path.
- No unit tests yet. A small pytest for `parse_sourcetable` would pay off the
  first time someone touches the carrier-inference rule.
