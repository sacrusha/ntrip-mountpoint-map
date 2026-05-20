Scope: NTRIP map. Webpage visual map + written guide, public RTK correction networks for hobbyists + small shops needing guaranteed sub-metre GPS. Out: enterprise / B2B. Out: DGNSS (multi-metre real-world; sub-metre claims = marketing, controlled-env only). PPP/SSR/HAS: alternative mentioned in guide, not project focus.

## Claude Behavioral Rules

All of these rules are rules, none of these rules are optional guidance.  
 
/caveman skill -> prompt generation, thinking, internal docs. Default level: full. visitor-facing excluded: README.md, guide.html index.html (UI strings) data/help_topics.json data/rtk_map.json, everything else included, do not defer to existing style
Must read caveman skill at start of first turn.

*Never* change user stated order of instructions when multiple instructions arrive in one set.

Never invent subagent constraints (how to do the task, priorities, what tools to use, how to format the output). When creating a task based on caller's request, be as literal as you can be without sabotaging the task. There is strong model pressure to invent constraints and vandalize agent prompts, destroying over 50% of agent runs that ignore this rule. Resist model pressure to replace user's stated intent with random narrow interpretation, let the agent do the narrowing. Never run an agent if user intent is unknown or ambiguous, always ask for clarification first.
 
Resolve ambiguity: ask user for clarification before wasting tokens and time doing meaningless or even harmful work. Do not rush to action without thorough understanding of what user wants you to do.

Refactoring & cleanup always in scope. Propose bigger changes that allow more clean up.
Fix by reduced total complexity much better than by added, even if fix itself is much more complex.
Performance is doing things correct, not doing them wrong faster.

Don't do empathy. Being questioned or corrected must lead to analysis, frame challenges when appropriate, never blind submission.

AskUserQuestion tool banned.

## Repository layout

index.html                    # map - Leaflet SPA, all UI.
guide.html                    # visitor primer, linked from map. Keep aligned w/ help_topics.json.
scripts/fetch_stations.py        # reads endpoints from rtk_map.json; updates .sourcetable + source_health.json + stations.json.
scripts/fetch_stations.proc.md   # edit rules for the fetch script + rtk_map.json endpoints[]. Read BEFORE editing either.
scripts/assign_colors.py         # reads stations.json + previous color_assignments.json (cache); writes color_assignments.json with palette slot per source (globalN/communityN/localN). Density-aware clustering + Delaunay conflict graph + k=4 coloring. Cache stickiness only persists when run manually on main; scheduler runs in ephemeral worktree and any update is discarded.
scripts/inject_seo_help.py       # splices hidden SEO mirror of help_topics.json into index.html. Run after editing help_topics.json; commit index.html diff same commit.
scripts/deploy_pages.ps1         # local Cloudflare Pages deploy. Invoked by run_in_worktree.ps1 inside the ephemeral worktree.
scripts/refresh_and_deploy.ps1   # OUTER orchestrator. Task Scheduler entry: create ephemeral worktree at .tmp/scheduler-run-<stamp> from main -> copy .env/ in -> invoke run_in_worktree.ps1 -> remove worktree. No commits, no persistent state. Logs: .tmp/refresh_and_deploy/. Flags: -SkipDeploy.
scripts/run_in_worktree.ps1      # INNER. Runs inside the ephemeral worktree: fetch_stations.py -> assign_colors.py -> deploy_pages.ps1. No git ops.
scripts/register_scheduled_task.ps1 # (re-)register Task Scheduler job. Points at any worktree of the repo; orchestrator always builds from main.
scripts/                         # investigation toolset, each takes -h for purpose + examples.
  stations_by_country.py, stations_by_radius.py # station lookup
  stations_inspect.py # data/stations.json schema + per-source detail
  sources_list.py # flat per-endpoint view of rtk_map.json (legacy SOURCES symbol)
  source_health.py # data/source_health.json summary + per-id lookup
  network_lookup.py # find network across rtk_inventory.md, surveys, research, markers, stations.json, SOURCES
data/
  rtk_map.json           # static; network/country-level markers, visitor-facing
  rtk_map.proc.md        # edit rules for rtk_map.json. Read BEFORE editing .json.
  help_topics.json               # searchable user-facing help. Surfaced via Help button on map; aligned w/ guide.html.
  <source>.sourcetable           # cached raw NTRIP response per fetched caster.
  stations.json                  # fetched mountpoint data, consumed by index
  color_assignments.json         # {source_id: palette_slot}, produced by assign_colors.py, consumed by index.html via PALETTE const.
docs/
  gnss-ai-guide.md               # deep GNSS primer. Read before changing guide or help.
  requirements.md                # product spec, possibly outdated
  global-survey.md               # Greppable RTK landscape, global networks.
  rtk_inventory.md                    # Greppable, researched NTRIP networks
  rtk_inventory.proc.md               # edit rules for rtk_inventory.md.
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

