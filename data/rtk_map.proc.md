# rtk_map.json — process

Per-file rules for `data/rtk_map.json`. Pipeline context:
`../docs/pipeline.md`. Target users: `../docs/target-users.md` — every
`note` is read by a hobbyist on the map, not a developer.

**Refactoring is in scope; consider the entire entry on every edit.** See
`../docs/pipeline.md` §"Edit discipline".

## Role

editorial user-facing extract of `rtk_inventory.md` - "what the user on a network marker&popup needs to know." 

## markers Field reference

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Matches `rtk_inventory.md` block id when one exists. Stable — used as React-style key downstream. |
| `name` | yes | What appears in the popup header. UI label, not the legal entity. |
| `region` | yes for single-country | What appears after "Covers". Country name + clarifier ("Spain", "China (nationwide)", "Belgium (Flanders)"). Hidden for `tier:weird`. Omitted on aggregator stubs. |
| `country` | yes | ISO 3166-1 alpha-2 for single-country networks; pseudo-code (`global`, `americas`, `europe`) for aggregator stubs spanning multiple countries. |
| `lat`,`lon` | yes for single-country | Marker map placement. Omitted on aggregator stubs (rtk2go, Centipede, EarthScope, EUREF-IP, IGS-IP) — they render no country-zoom marker; the entry exists only to carry editorial data for the future per-pin mountpoint card. |
| `tier` | yes | `free`, `paid`, `restricted`, `weird` |
| `access` | for free | `open`, `registration`, `conditions` |
| `vrs` | when true | boolean, "true" if network delivers VRS/NRTK streams
| `yearly_cost` | recommended on paid* | '$X/yr' / 'X €/yr' / '£X/yr', etc. local currency. if no yearly option, fall back to /mo, /h, /min, one time payment. Only one price, additional relevant pricing options in note field. No known pricing = no yearly_cost field
| `yearly_cost_normalized` | required if yearly_cost present | Integer, used as color hint for affordability  |
| `stations_declared` | when known | Integer
| `registration` | when useful | URL describing the network (operator, what it is, how to register/gain access); prefer the most official source. Skip rather than link a bare login or form page. |
| `note` | conditional | If helpful to target user |
| `endpoints` | when fetchable | Array of operational fetch endpoints. Most networks have one; some have multiple (e.g. `ergnss` mainland + Canary VRS sub-service). Each endpoint: `{url, credentials?: {user, pass, userNote}, near?: bool, nmea_filter?: false, solution_filter?: false}`. Defaults: filters true, near false. Empty/missing for paid/restricted/weird networks (no pipeline fetch). |

**No `color` field.** Marker colours are derived automatically:
  - Free-tier markers with endpoints → palette slot from `data/color_assignments.json` (produced by `scripts/assign_colors.py`), looked up in `PALETTE` in `index.html`.
  - Paid/restricted/weird tiers → tier rules at runtime (`PAID_TIER_ICONS` in `index.html`).
  - Free markers with endpoints but no current palette assignment (fetcher returning 0 stations) → fallback grey, signalling "no data".

## How markers render

markers are displayed at lat/lon, symbol depends on tier & vrs. Color for paid depends on yearly_cost_normalized
popup builder in `index.html` auto-fills from the marker's
structured fields:

  **header**: `name`
  **access banner** : "Paid subscription required" etc. — auto from `tier`/`access`
  **yearly_cost**: yearly_cost
  **region** : "Covers <b>{region}</b>." — hidden for `tier:weird`
  **stations_declared**: "(stations_declared) reference stations"
  **note**: note
  **registration**: auto-rendered as a clickable URL
  
Free networks also display their individual mountpoints on the map
  
## Notes

- Target users are defined in /docs/target-users.md - You must not edit a note without having read this file. Instructions to edit a note are instructions to read this file first. Editing a note without having read target-users.md are a major error.
- **Do not restate what other fields cover.** Do not restate what the map already communicates. Don't mention coverage by other networks, the other networks are on the map.
- **No internal-facing language** The note is for target-users *only*.
- **No filler.** "Useful where no free regional caster exists" is fluff. "Professional focus; no explicit hobbyist ban" is fluff. If a sentence doesn't tell the user something they can act on, cut it.
- **Matter-of-fact, ≤2 short sentences, ~250 chars.** Length is a budget; if you need more, cut earlier.
- **No claims about other networks** unless it adds significant practical value to a user choosing what to use, beyond what is obvious from the map. Avoid both explicit claims ("Centipede station in the north is an alternative") and implicit ones ("The only network in Calabria").
- **No US/Western framing.** Users of a network are physically there. They are locals.
- **Preserve correct names** Don't write "national ID" when you can write "Kazakh ИИН/БИН ID"
- **Harassment guard.** No bare email, phone, named individuals, bank/IBAN, postal address.
- No cryptic acronyms unexpanded on first use (FKP, iMAX, SBC portal, SPID) — spell
  out or omit.
- Anchor in events: "installed 2022", "announced Apr 2024", "free since
  Law 1955/2019". Avoid "as of 2026-05-12", bare "currently", or
  "recently"
- UK spelling. "GPS" colloquially; "GNSS" only when hardware/signal
  detail forces it.


## When to add a marker 

The marker represents a pareto point - coverage, affordability / official-ness. It exists because, without it, a target user would miss something they need to know to fit their need. If the marker only confirms absence ("nothing exists"), omit it unless there's a relevant political explanation why nothing exists for now, that implies when that might change.

### Tier picker

| Tier | Add when | Note convention |
|---|---|---|
| `free` | Free network with a defined country/region home. The marker is the country-zoom entry point — it surfaces editorial info (registration, stations_declared, note) and hides at `z>=8` where pins take over. Add regardless of whether pins render: VRS-only, pipeline-dead, and pin-producing networks all get a marker. Skip only for aggregators / global casters with no single placement (rtk2go, Centipede, EarthScope NOTA, EUREF-IP, IGS-IP, AGRS.NL across NL+BES, MIRAI). | Open with `"N stations, free."` when no data is ingested yet. Otherwise often skip note entirely; structured fields suffice. |
| `paid` | Substantial paid commercial operator. Affordability is conveyed via `yearly_cost_normalized`. | Why a hobbyist would still care, free trial |
| `restricted` | Substantial network with no hobbyist path at any price (licence gate, sector-only, bundled-hardware). National ID requirement is noteworthy, but doesn't make a network restricted - users should be assumed to often be locals | The specific blocker in plain words, and the next-best free alternative if one exists. |
| `weird` | User-relevant fact that the structured fields cannot carry. The note IS the marker. Past examples (illustrative, not exhaustive): RINEX-only / no real-time NTRIP, announced-but-not-live network, sparse infra (huge baselines), GNSS jamming or spoofing, reseller-only distribution, non-standard NTRIP, named operator with no published endpoint, civil-war disruption, micro-state with no local service. | The note is load-bearing — it has to stand alone. |

## Endpoints — fetch pipeline membership

Free-tier markers with a published host:port carry an `endpoints[]`
array; the fetcher (`../scripts/fetch_stations.py`) iterates these and
writes per-network station data into `stations.json`. Editing
`endpoints[]` is the normal way to add, remove, or retune a fetched
network — **not** a `fetch_stations.py` change.

### Endpoint shape

```json
{
  "url": "http://rtk.gazar.gov.mn:2101/",
  "id": "ergnss_sptr",
  "credentials": {"user": "rover", "pass": "262461", "userNote": "your registered username"},
  "near": true,
  "nmea_filter": false,
  "solution_filter": false
}
```

| field | required | notes |
|---|---|---|
| `url` | yes | Full NTRIP URL with trailing slash; `http://` even if the host serves https — the fetcher falls back to raw NTRIP/1.0 TCP if HTTP GET returns `BadStatusLine`. |
| `id` | only when needed | Cache-file basename (`../data/<id>.sourcetable`). Defaults to the network id for `endpoints[0]`, `<network_id>_<idx>` otherwise. Set explicitly to preserve an existing cache file across migrations (e.g. `ergnss_sptr`). |
| `credentials` | optional | Shared/public creds shown in popup. `{user?, pass?, userNote?}`. `userNote` describes a variable username (e.g. "your email address") — render-only, not part of auth. |
| `near` | optional, default `false` | True surfaces the `NEAR` auto-select hint in popup. |
| `nmea_filter` | optional, default `true` | Set `false` only when the caster mislabels real physical stations with `nmea=1`. See filter-flag rules below. |
| `solution_filter` | optional, default `true` | Set `false` only when the caster mislabels physical stations with `solution=1`. Rarer than `nmea_filter` overrides. |

### Trigger — `rtk_inventory.md` status drives endpoint membership

The decision lives upstream in `../docs/rtk_inventory.md`. When a
block's `status:` changes, sweep `endpoints[]`:

| rtk_inventory.md status | endpoints action | Rationale |
|---|---|---|
| `free` with host:port | **add endpoint** to the marker | Free endpoint, must ingest. |
| `candidate` | **add endpoint** | Endpoint known, ready to verify in production. The next cron run is the test. |
| `paid` | **remove `endpoints[]`** if present | Paid → renders as country marker, not pin. |
| `restricted` | **remove `endpoints[]`** if present | Same. |
| `weird` | usually **remove `endpoints[]`** | Weird means structured fields can't carry the story — pins lie. Keep only when stream metadata genuinely helps users. |

The marker entry itself stays through these transitions; only
`endpoints[]` and `tier` change.

### Don't gate on reachability you can't test

Sandboxed editors cannot reach NTRIP casters. **Do not refuse to add an
endpoint because the host hasn't been verified from your environment** —
that's not a precondition this file imposes. Trust the upstream
`rtk_inventory.md` fields. The next cron run is the live verifier; if
the host is wrong, run logs surface it and the entry can be tuned in a
follow-up commit.

### Filter flag overrides — `nmea_filter`, `solution_filter`

Defaults: both `true`. Only override when the caster mislabels real
physical stations.

The defaults drop two classes of mountpoint:
- **`nmea=1`** — caster expects rover to upload a GGA position,
  defining trait of VRS/network-solution streams (iMAX, MAC, FKP, NEAR).
- **`solution=1`** — STR-line tagged as a computed network solution
  rather than a physical receiver.

Override when a caster mislabels physical stations:

- `nmea_filter: false` — physical mounts are wrongly tagged `nmea=1`.
  Tell: many distinct real coordinates appear in the dropped set
  (e.g. SNIP, Leica Spider defaults).
- `solution_filter: false` — physical mounts are wrongly tagged
  `solution=1`. Rarer.
- **Never `solution_filter: false` on `rtk2go`** — it is the only
  guard against the NEAR-xxx VRS streams (rtk2go also disables
  `nmea_filter`).

When debugging filter behaviour, inspect what got dropped vs kept on
the last run:

```sh
grep "$ID" ../data/<sid>.sourcetable | awk -F';' '{print $1,$2,$10,$11,$12,$13}'
#                                       ^line ^name ^lat ^lon ^nmea ^solution
```

Concrete cases in tree (good calibration):

| Network | Override | Why |
|---|---|---|
| `rtk2go` | `nmea_filter: false` | tags all physical stations nmea=1; NEAR-xxx caught by solution_filter |
| `geortk` | both `false` | physical stations tagged both nmea=1 and solution=1 |
| `renep` | `nmea_filter: false` | 39 of 47 physical stations tagged nmea=1; VRS mounts on separate ports |
| `auscors` | `solution_filter: false` | 42 IGS partner stations tagged solution=1; all physical with fixed coords |
| `igac` | `nmea_filter: false` | Leica Spider default; physical mounts on port 2102 tagged nmea=1 |
| `almgg_mn` | `solution_filter: false` | SNIP caster tags 6 physical stations solution=1 |
| `nps_cors` | `nmea_filter: false` | Trimble Pivot tags all 141 physical stations nmea=1 |

### Picking ports when rtk_inventory.md offers several

Many operators expose multiple ports. Pick the one yielding **physical
single-base mounts** in raw form:

- IGAC: `:2101` is VRS-only (NEAR/iMAX/VIRS), `:2102` has 143 station mounts → pick `:2102`.
- ERGNSS: `ergnss-ip.ign.es:2101` for data-only mainland (`endpoints[0]`); SPTR sub-service at `ergnss-tr.ign.es:2101` as `endpoints[1]` with explicit `id: "ergnss_sptr"` for cache continuity.
- ROMPOS (if it ever flipped to free): `:2101` VRS, `:2105` single-base → pick `:2105`.

When a sourcetable has duplicate mountpoints across formats
(`AAAA_RTCM3`, `AAAA_RTCM2`, `AAAA_MSM`), the fetcher's parser keeps
each row and the downstream merge dedupes by coordinate. Don't
pre-filter formats at the endpoint level.

### Multi-endpoint networks

A network with two casters (mainland + a sub-service for outlying
regions, for example) is one marker with two entries in `endpoints[]`.
The fetcher fetches each endpoint, merges stations by `(name, lat,
lon)`, and writes one stations.json record under the network's id.
Combined status is `ok` if any endpoint succeeded fresh, `stale` if
any cached, else `error`.

Sub-service endpoints don't get their own marker. ergnss SPTR is a
sub-service of ergnss, not a separate network. Two endpoints in one
marker is the model.

### After-edit checks

```sh
# JSON-validity smoke test:
python -c "import json; json.load(open('data/rtk_map.json', encoding='utf-8'))"

# Endpoint-shape smoke test (loads via fetch_stations module):
python -c "from scripts.fetch_stations import NETWORKS, SOURCES; print(len(NETWORKS), len(SOURCES))"

# Local dry-fetch when network is available (fails open in sandbox):
python scripts/fetch_stations.py
# Expected stdout per endpoint: "[sid] fetched N stations ..."
# Zero stations on a free single-base entry → filter flags need attention.
```
