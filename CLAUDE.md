A map & guide on free public RTK correction networks for hobbyists and small
shops who need better than ~5–10 m GPS accuracy. Enterprise / B2B is out of scope.
DGNSS out of scope due to low real world accuracy.
PPP/SSR/HAS mentioned as alternative in guide, not what this projedct is about.

## Repository layout

```
index.html                    # Single-page Leaflet app — all UI.
guide.html                    # long-form standalone visitor primer linked from the map. content must stay aligned /w /help_topics.json
scripts/fetch_stations.py     # updates .sourcetable files, source_health.json, stations.json.
scripts/inject_seo_help.py    # splices a hidden SEO mirror of help_topics.json into index.html. Run after editing help_topics.json; commit the index.html diff in the same commit.
.github/workflows/
  update-stations.yml         # Runs fetch_stations.py 4 times a day, commits to main.
data/
  stations.json               # fetched data, consumed by index
  country_markers.json        # Static; country-level markers, content visitor facing
  help_topics.json            # searchable visitor-facing help repository surfaced via the Help button on the map, content must stay aligned /w guide.html
  <source>.sourcetable        # Raw archives per fetched caster.
docs/ 
  gnss-ai-guide.md # deep technical GNSS primer for ai, consume before making changes to guide or help
  requirements.md # product spec, target users, out-of-scope, data-model, visual design, tech choices, deferred items. Consult when necessary to understand target users, design, etc.
  country-survey.md #Greppable RTK landscape by country, answers *how* public RTK coverage in country works. Always ensure edits match format and scope of existing entries. 
  global-survey.md #Greppable RTK landscape, global networks.
  networks.md # Greppable list of known networks, Endpoints, credentials, cost, etc. Always ensure edits match format and scope of existing entries.
  
.claude/process/                # rules for the RTK survey pipeline. Read the relevant per-file meta BEFORE editing the affected file.
  pipeline.md                   # cross-file flow: country-survey → networks → markers + fetch. Referenced by all per-file metas.
  country-survey.md             # rules for editing docs/country-survey.md
  networks.md                   # rules for editing docs/networks.md
  country-markers.md            # rules for editing data/country_markers.json
  fetch-stations.md             # rules for editing scripts/fetch_stations.py SOURCES
.claude/skills/update-country-survey/SKILL.md # Workflow runbook for batch country audits. Defers to .claude/process/ for per-file rules.
.claude/token-reduction-patterns.md #rules for producing token-optimized content for ai consumption, applies to gnss-ai-guide.md, can be used for other ai facing content
  
```

## Gotchas

- Generating large text blocks (2kB) in this env will timeout and fail. Workaround with iteratarive output;, skeleton-first then edit; bash py etc for repetitive work.
- All color and design edits must always consider Light and Dark mode.
- Sandbox has very limited internet access. WebSearch tool works, pretty much nothing else does, test environment before relying on it.
- Pipeline filter flags (nmea_filter / solution_filter in SOURCES): both default True. Set nmea_filter=False only if the caster mislabels physical stations as NMEA=1; solution_filter=False only if it mislabels them as solution=1. Never set solution_filter=False for rtk2go — it is the only guard against the NEAR-xxx VRS streams. See parse_sourcetable docstring for full rules.
