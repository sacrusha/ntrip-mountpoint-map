# fetch_stations.py — process

Per-file rules for `scripts/fetch_stations.py`. Pipeline context:
`../docs/pipeline.md`.

**Refactoring is in scope; consider the entire entry on every edit.** See
`../docs/pipeline.md` §"Edit discipline".

## Role

Ingests configured NTRIP casters into `data/stations.json`. Run by
GitHub Actions cron 4×/day; consumed by `index.html`. The `SOURCES` list
near the top of the script is the operational subject — each dict is
one caster to fetch.

## Editing SOURCES is routine — do it, don't escalate

Adding, removing, and tuning SOURCES entries is a **normal pipeline
operation**, not a sensitive change. When the trigger below fires, make
the edit. **Do not refuse, defer, ask the user first, or invent
preconditions that aren't in this file.**

Safe by design (see module docstring):

- Tolerates fetch failures — retries, falls back to the previous
  on-disk sourcetable, and on second failure leaves the source as
  `staleness:'dead'` (grey ring in UI).
- Cannot corrupt `stations.json` — a byte-identical guard skips the
  write when the parsed set is unchanged.
- Adds are reversible by deletion. Iterating on filter flags is cheap.

The safest file in the pipeline to edit. Treat it that way.

## Trigger — `networks.md` status drives SOURCES membership

The decision lives upstream in `docs/networks.md`. When a block's
`status:` changes, sweep `SOURCES`:

| networks.md status | SOURCES action | Rationale |
|---|---|---|
| `free` with host:port | **add** | Free endpoint, must ingest. |
| `candidate` | **add** | Endpoint known, ready to verify in production. The next cron run is the test. |
| `paid` | **remove** if present | Paid → renders as country marker, not pin. |
| `restricted` | **remove** if present | Same. |
| `weird` | usually **remove** | Weird means structured fields can't carry the story — pins lie. Keep only when stream metadata genuinely helps users. |


## Don't gate on reachability you can't test

The sandbox has no outbound network access to NTRIP casters. **Do not
refuse to add an entry because the host hasn't been verified from this
environment** — that is not a precondition this file imposes. Trust the
upstream `networks.md` fields (`host`, `port`, `status`, `type`).

The next cron run is the live verifier. If the host is wrong, the run
logs surface it and the entry can be tuned in a follow-up commit.
Pre-validation from this environment is impossible and not required.

When upstream research already curled the endpoint, the `ntrip_research/`
file usually records the verification. That's enough evidence.

## SOURCES entry shape

```python
{
  "id":         "almgg_mn",                    # stable; matches networks.md block id; used as
                                               # `data/<id>.sourcetable` filename and stations.json key
  "url":        "http://rtk.gazar.gov.mn:2101/", # full NTRIP URL; trailing slash; http:// even if host
                                               # serves https — script falls back to raw NTRIP/1.0 TCP
                                               # if the HTTP GET returns BadStatusLine
  "color":      "#9e6b00",                     # marker colour — pick a country-distinctive hex; avoid
                                               # collisions with neighbouring networks at the same zoom
  "label":      "MonPOS",                      # short UI string in popups + filter panel
  "type":       "physical-vrs",                # see "type field" below
  "country":    ["MN"],                        # list; ISO 3166-1 alpha-2. ["global"] for aggregators
                                               # (rtk2go, Centipede). ["americas"] etc. for regional
                                               # multi-country casters (EarthScope)
  "region":     "Friuli-Venezia Giulia",       # optional; sub-national qualifier
  "group":      "italy-regional",              # optional; clusters related sources in the UI filter
  "credentials":{"user":"rover","pass":"262461"}, # optional; shared/public creds shown in popup
  "access":     "open",                        # "open" | "registration" | "conditions" — see below
  "registration": "https://monpos.gazar.gov.mn", # signup URL; None for fully open casters
  "near":       True,                          # optional; surfaces NEAR hint in popup
  "user":       "centipede",                   # optional; only on free servces iff it's public knowledge. literal username for copy-to-rover popup
  "pass":       "centipede",                   # optional; only on free servces iff it's public knowledge. literal password
  "userNote":   "your registered username",    # optional; popup hint when user is variable
  "openNote":   "Free registration required",  # optional; popup access blurb
  "nmea_filter":    False,                     # optional; default True — see filter flags
  "solution_filter": False,                    # optional; default True — see filter flags
}
```

### `access` values
- `open` — connect immediately, no account.
- `registration` — free for everyone; signup required.
- `conditions` — free but may not apply to you (national ID, non-commercial only, fee for some uses, expiring trial).

### `type` values
- `single-base` — physical antennas, each with a distinct coordinate.
- `physical-vrs` (and legacy `physical-coord-vrs`) — sourcetable carries physical mounts plus VRS/NRTK overlays.
- `vrs-only` — sourcetable exposes only virtual / single-coord mountpoints. Yields 0 physical pins after `filter_vrs` collapses identical-coord rows; renders as a country-level VRS ring driven by `country_markers.json`.
- `unknown` — cannot determine from the sourcetable.

## Filter flags — `nmea_filter`, `solution_filter`

Defaults: both `True`. Only override with a one-line `#` comment giving
the parse-rationale.

The defaults drop two classes of mountpoint:
- **`nmea=1`** — caster expects rover to upload a GGA position, defining
  trait of VRS/network-solution streams (iMAX, MAC, FKP, NEAR).
- **`solution=1`** — STR-line tagged as a computed network solution
  rather than a physical receiver.

Override when a caster mislabels real physical stations:

- `nmea_filter=False` — physical mounts are wrongly tagged `nmea=1`.
  Tell: many distinct real coordinates appear in the dropped set
  (e.g. SNIP, Leica Spider defaults).
- `solution_filter=False` — physical mounts are wrongly tagged
  `solution=1`. Rarer.
- **Never `solution_filter=False` on `rtk2go`** — it is the only guard
  against the NEAR-xxx VRS streams (rtk2go also disables `nmea_filter`).

When debugging filter behaviour:

```sh
# Inspect what got dropped vs kept on the last run:
grep "$ID" data/<sid>.sourcetable | awk -F';' '{print $1,$2,$10,$11,$12,$13}'
#                                       ^line ^name ^lat ^lon ^nmea ^solution
```

Concrete cases in tree (good calibration):

| Source | Override | Why |
|---|---|---|
| `rtk2go` | `nmea_filter=False` | tags all physical stations nmea=1; NEAR-xxx caught by solution_filter |
| `geortk` | both `False` | physical stations tagged both nmea=1 and solution=1 |
| `renep` | `nmea_filter=False` | 39 of 47 physical stations tagged nmea=1; VRS mounts on separate ports |
| `auscors` | `solution_filter=False` | 42 IGS partner stations tagged solution=1; all physical with fixed coords |
| `igac` | `nmea_filter=False` | Leica Spider default; physical mounts on port 2102 tagged nmea=1 |
| `almgg_mn` | `solution_filter=False` | SNIP caster tags 6 physical stations solution=1 |
| `nps_cors` | `nmea_filter=False` | Trimble Pivot tags all 141 physical stations nmea=1 |

## Picking ports when networks.md offers several

Many operators expose multiple ports. Pick the one yielding **physical
single-base mounts** in raw form:

- IGAC: `:2101` is VRS-only (NEAR/iMAX/VIRS), `:2102` has 143 station mounts → pin `:2102`.
- ERGNSS: `ergnss-ip.ign.es:2101` for data-only mainland; SPTR sub-service at `ergnss-tr.ign.es:2101` for Canaries.
- ROMPOS (if it ever flipped to free): `:2101` VRS, `:2105` single-base → pin `:2105`.

When sourcetable has duplicate names across formats (`AAAA_RTCM3`,
`AAAA_RTCM2`, `AAAA_MSM`), `parse_sourcetable` keeps each row and the
downstream merge dedupes by coordinate. Don't pre-filter formats here.

## Carrier 0 (DGNSS) is dropped silently

`parse_sourcetable` discards `carrier=0` mounts — DGNSS-only is
sub-50-cm and out of scope. Don't try to keep them by tweaking filters.

## After-edit checks

Run before committing:

```sh
# Syntax check — broken dict means the cron run errors out hard.
python -c "from scripts.fetch_stations import SOURCES; print(len(SOURCES))"

# Local dry-fetch when network is available (fails open in sandbox):
python scripts/fetch_stations.py
# Expected stdout per source: "[sid] fetched N stations (dropped X DGNSS, Y invalid[, Z net-sol])"
# Zero stations on a "physical-vrs" or "single-base" entry → filter flags need attention.
```

Watch for:
- 0 stations on an entry that should have many → wrong port, or
  filter dropped them all.
- "all sources failed and no cached data was refreshed" → script
  exited 0 and made no changes; safe to re-try later.
- `data/<sid>.sourcetable` shows up in git status → expected on first
  successful fetch for a new source; commit it.

## Conventions for the SOURCES list itself

- Order: roughly grouped by region/operator family (SAPOS together,
  Italian regionals together, US state-DOTs together). Insert near
  similar neighbours, not at end-of-file.
- One-line `#` comment per entry when it captures a non-obvious port,
  filter rationale, or migration date — these comments are the
  institutional memory.
- When removing an entry, leave a one-line tombstone comment with the
  reason and date (e.g. `# APOS (AT) removed 2025-XX-XX — paid for
  hobbyists; surfaced as country_markers.json paid marker.`). Make
  re-discovery trivial.
