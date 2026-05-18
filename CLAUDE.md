Scope: NTRIP map. Webpage visual map + written guide, public RTK correction networks for hobbyists + small shops needing guaranteed sub-metre GPS. Out: enterprise / B2B. Out: DGNSS (multi-metre real-world; sub-metre claims = marketing, controlled-env only). PPP/SSR/HAS: alternative mentioned in guide, not project focus.

## Claude Behavioral Rules
 
/caveman skill -> prompt generation, thinking, internal docs. Default level: full. visitor-facing excluded: README.md, guide.html index.html (UI strings) data/help_topics.json data/country_markers.json, everything else included, do not defer to existing style
Must read caveman skill at start of first turn.

*Never* ignore instructions. 
*Never* invent instructions, 
*Never* change order of instructions when multiple instructions arrive in one set.

When writing subagent tasks, always preserve user intent. Never invent subagent constraints, like how to do the task, what tools to use, how to format the output. When forwarding a task to an agent be as literal as you can be without sabotaging the task.
 
Before non-trivial tasks, resolve ambiguity: ask user for clarification before wasting tokens and time doing meaningless or even harmful work. Do not rush to action without thorough understanding of what you're asked to do

Refactoring & cleanup always in scope. Propose bigger changes that allow more clean up.
Fix by reduced total complexity much better than by added, even if fix itself is much more complex.
Performance is doing things correct, not doing them wrong faster.

Don't do empathy. Being questioned or corrected must lead to analysis, frame challenges when appropriate, never blind submission.

AskUserQuestion tool banned.

## Repository layout

index.html                    # map - Leaflet SPA, all UI.
guide.html                    # visitor primer, linked from map. Keep aligned w/ help_topics.json.
scripts/fetch_stations.py        # updates .sourcetable + source_health.json + stations.json.
scripts/fetch_stations.proc.md   # edit rules for fetch_stations.py SOURCES. Read BEFORE editing .py.
scripts/inject_seo_help.py       # splices hidden SEO mirror of help_topics.json into index.html. Run after editing help_topics.json; commit index.html diff same commit.
scripts/deploy_pages.ps1         # local Cloudflare Pages deploy. Runs on worktree ntrip-mountpoint-map.scheduler/; dev on worktree ntrip-mountpoint-map/.
scripts/refresh_and_deploy.ps1   # Task Scheduler -> fetch_stations.py -> rebase data-refresh onto main -> commit data/ -> deploy_pages.ps1. Logs: .tmp/refresh_and_deploy/. Flags: -SkipGit, -SkipDeploy.
scripts/register_scheduled_task.ps1 # (re-)register Task Scheduler job.
scripts/                         # investigation toolset, each takes -h for purpose + examples.
  stations_by_country.py, stations_by_radius.py # station lookup
  stations_inspect.py # data/stations.json schema + per-source detail
  sources_list.py # filter SOURCES list in fetch_stations.py
  source_health.py # data/source_health.json summary + per-id lookup
  network_lookup.py # find network across networks.md, surveys, research, markers, stations.json, SOURCES
data/
  country_markers.json           # static; network/country-level markers, visitor-facing
  country_markers.proc.md        # edit rules for country_markers.json. Read BEFORE editing .json.
  help_topics.json               # searchable user-facing help. Surfaced via Help button on map; aligned w/ guide.html.
  <source>.sourcetable           # cached raw NTRIP response per fetched caster.
  stations.json                  # fetched mountpoint data, consumed by index
docs/
  gnss-ai-guide.md               # deep GNSS primer. Read before changing guide or help.
  requirements.md                # product spec, possibly outdated
  global-survey.md               # Greppable RTK landscape, global networks.
  networks.md                    # Greppable, researched NTRIP networks
  networks.proc.md               # edit rules for networks.md.
  pipeline.md                    # pipeline: ntrip_research -> networks -> (markers + fetch).
  ntrip_research/*               # primary research (CC_Name.md), feeds pipeline, 
  ardusimple/*                   # dealer cache (CC_*.md), side input research_task phase-1
  research_task.txt              # produces ntrip_research/ entries
  research_task.primer.txt	# short NTRIP ai-primer for research tasks.
  target-users.md	             # defines target users
.tmp/ # all temp files


## Gotchas

- Generating large text blocks (>2kB) time out. File: skeleton first then fill, Prompt: multiple sequential prompts.
- Design for Light & Dark mode.

