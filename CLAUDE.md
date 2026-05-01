A map & guide on free public RTK correction networks for hobbyists and small
shops who need better than ~5–10 m GPS accuracy. Enterprise / B2B is out of scope.
DGNSS out of scope due to low real world accuracy.
PPP/SSR/HAS mentioned as alternative in guide, not what this projedct is about.

## Repository layout

```
index.html                    # Single-page Leaflet app — all UI.
guide.html                    # long-form standalone visitor primer linked from the map. content must stay aligned /w /help_topics.json
scripts/fetch_stations.py     # updates .sourcetable files, source_health.json, stations.json.
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
  
.claude/skills/update-country-survey/SKILL.md # Rules on how to update country-survey.md, networks.md, never edit those files without having read this file 
.claude/token-reduction-patterns.md #rules for producing token-optimized content for ai consumption, applies to gnss-ai-guide.md, can be used for other ai facing content
  
```

## Gotchas

Generating large text blocks (2kB) requires long thinking phases that will exceed the ~300 s idle timeout and fail. Workaround with iteratarive output, skeleton-first then edit, and bash py etc for repetitive work.
All color and design edits must always consider Light and Dark mode.
Sandbox has very limited internet access. SearchTool works, pretty much nothing else does, test environment before relying on it.
