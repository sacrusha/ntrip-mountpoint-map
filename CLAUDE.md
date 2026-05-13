A map & guide on free public RTK correction networks for hobbyists and small
shops who need better than ~5–10 m GPS accuracy. Enterprise / B2B is out of scope.
DGNSS out of scope due to low real world accuracy.
PPP/SSR/HAS mentioned as alternative in guide, not what this project is about.

## Repository layout

```
index.html                    # Single-page Leaflet app — all UI.
guide.html                    # long-form standalone visitor primer linked from the map. content must stay aligned /w /help_topics.json
scripts/fetch_stations.py        # updates .sourcetable files, source_health.json, stations.json.
scripts/fetch_stations.proc.md   # editing rules for fetch_stations.py SOURCES. Read BEFORE editing the .py.
scripts/inject_seo_help.py       # splices a hidden SEO mirror of help_topics.json into index.html. Run after editing help_topics.json; commit the index.html diff in the same commit.
.github/workflows/
  update-stations.yml            # Runs fetch_stations.py 4 times a day, commits to main.
data/
  stations.json                  # fetched data, consumed by index
  country_markers.json           # Static; country-level markers, content visitor facing
  country_markers.proc.md        # editing rules for country_markers.json. Read BEFORE editing the .json.
  help_topics.json               # searchable visitor-facing help repository surfaced via the Help button on the map, content must stay aligned /w guide.html
  <source>.sourcetable           # Raw archives per fetched caster.
docs/
  gnss-ai-guide.md               # deep technical GNSS primer for ai, consume before making changes to guide or help
  requirements.md                # product spec, target users, out-of-scope, data-model, visual design, tech choices, deferred items. Consult when necessary to understand target users, design, etc.
  global-survey.md               # Greppable RTK landscape, global networks.
  networks.md                    # Greppable list of known networks, Endpoints, credentials, cost, etc. Always ensure edits match format and scope of existing entries.
  networks.proc.md               # editing rules for networks.md. Read BEFORE editing.
  pipeline.md                    # cross-file flow: ntrip_research → country-survey → networks → markers + fetch. Referenced by all per-file .proc.md sidecars.
  ntrip_research/                # per-country primary research files (CC_Name.md), citation-grade. Upstream input to country-survey.md — see pipeline.md "Research stage".
  research_task.txt              # prompt template used to produce ntrip_research/ entries; research is run in an external web-enabled environment, not this sandbox.
  target-users.md	             # read to understand who the target users are			

.claude/token-reduction-patterns.md # rules for producing token-optimized content for ai consumption, applies to gnss-ai-guide.md, can be used for other ai facing content
  
```

## Gotchas

- Generating large text blocks (2kB) in this env will timeout and fail. Workaround with iterative output; skeleton-first then edit; bash py etc for repetitive work.
- All color and design edits must always consider Light and Dark mode.
- Sandbox has very limited internet access. WebSearch tool works, pretty much nothing else does, test environment before relying on it.
- Pipeline filter flags (nmea_filter / solution_filter in SOURCES): both default True. Set nmea_filter=False only if the caster mislabels physical stations as NMEA=1; solution_filter=False only if it mislabels them as solution=1. Never set solution_filter=False for rtk2go — it is the only guard against the NEAR-xxx VRS streams. See parse_sourcetable docstring for full rules.
