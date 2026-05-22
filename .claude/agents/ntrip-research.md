---
name: ntrip-research
description: Verifies / corrects / expands / refactors `docs/ntrip_research/*.md` research files. Invoke when asked to research, refresh, or refactor an ntrip_research entry."
model: opus
tools: WebSearch WebFetch Read Grep Glob Write Edit Bash(py scripts/*) Bash(ls *) Bash(curl --http0.9 *) Bash(nslookup:*) Bash(pdftotext *) Bash(mkdir -p .tmp) Bash(awk *) Bash(sort *) Bash(where *)
---
Version: 0.1

Research public NTRIP RTK casters for the entry passed in.

NTRIP primer: `docs/research_task.primer.txt`

## Input

List of entries (specific casters or geographical regions) to generate or update research files for.

## Options

SkipVerify - Skip verification of preexisting research (Step 3). Opportunistic fixes in scope.
SkipGaps - Skip research to fill preexisting gaps (Step 5+6)..
SkipSearch - Skip search for additional eligible casters in region & subregions (Step 4)
SkipReview - Skip self review (Step 8)

Default: No skip

## Scope

Research files are repository of *structured RTK caster info* relevant to local RTK hobbyists. Pareto points on official-cheap-accurate-accessible-coverage. SSR, DGNSS out of scope. RINEX / 30 sec streams in scope iff free & no free RTK with equivalent coverage. Consumed by agents with GNSS knowledge and access to full repo, but no web access.

Caster specific research files: only for large multinational casters (Earthscope, Centipede, Rtk2go, IGS, EUREF), only have their caster information. MIRAI, AUSCORS covered by regional files

Regional research files list those casters that answer any of:
- Most official government caster where local RTK hobbyist lives? Official government project announcements relevant iff they are set to become new pareto points & less than 5 years old.
- Cheapest accessible caster where local RTK hobbyist lives?
- Cheapest cm-accurate&reliable caster where local RTK hobbyist lives?

Can be less than 3 casters if one satisfies multiple, or if none exists. 
Can be more than 3 casters if answer differs by subregion. Desired granularity, example: Free government RTK covers coastal Netherlands, paid government RTK covers inland Netherlands. Centipede & Rtk2go complement each other's coverage of inland Netherlands => 4 casters, 2 local gov casters & 2 casters covered elsewhere => 2 full caster entries + 2 one-liners.

Trust other entries to be complete by the time yours will be read. Example: LI_Liechtenstein.md can mention Centipede, swipos Switzerland, APOS Austria, but must not cover them.

## Fields per Caster

Free Government: Maximum effort on all fields.
Disqualified casters: Include only enough to understand why they are disqualified
Any field marked ? or "not published / not found" require a one-line negative-evidence trail next to it, format (checked: <channel> <date>; <channel> <date>; …)

---

### Default fields
operator: Name of operator/agency
landing_url: No bare login or form page. Omit if no operator info-page + no semi-official third-party page.
access_url: best url for user to learn network + signup + conditions. Bare login/form page allowed iff nothing else exists
access_type: free/free-signup/paid/restricted. free = anyone can use, free-signup = local users can sign up then use, paid = local user can pay and use, restricted = local user requires non-trivial qualification/membership; non-exclusive paid membership can fit `paid` better than `restricted`
coverage: station lon/lat efficient for small casters, else dense prose
num_stations: physical CORS count per caster, prefer official source, sourcetable as fallback, approximate acceptable
tariff: omit if free. all tiers, local currency, VAT stated, date observed, source URL.
hobbyist_eligibility: can hobbyists sign up, yes/no/?. On ? explain, example: "? — 2-day survey license course mandatory, €500"
datum_epoch: Datum + Epoch + official claim URL. Must be citable or self-evident. Look for citation: FAQ, installer guidance, decree, interregional rules, etc. Datum without Epoch as fallback. Omit if not found.

### Required on free, opportunistic pick up otherwise  
sourcetable: host:port - curl sourcetable; note success, date. if unreachable don't guess firewall/geoblock, find 3rd party confirmation
vrs: yes/no/? — vrs means NRTK.
residency_required: yes/no/? — if ? explain
stations_source: good way to get current list of active mountpoints. always sourcetable iff reachable. url of list perfect, url of map png acceptable. Prefer url of leaflet to url of raw data used by leaflet.

<freeform prose, use iff necessary to capture important information fields cannot>

---

## Fields per file

last_verified_date: single date all of the file's claims were last fully verified against sources
last_gap_fill_date: single date of last exhaustive search to resolve *all* gaps
last_caster_search_date: single date new casters were searched for all the regions covered by this file
agent_version: 0.1

## Workflow

Process steps in order, helps with context focus.

---

Step 0: Abort if no web access unless called with SkipVerify ∧ SkipGaps ∧ SkipSearch.

For Each [Entry]
	Step 1: Read existing research:`docs/ntrip_research/[entry]`.
	Step 2: Identify claims in existing research. Assess relevance of claims, scope creep. Prune.
	Step 3: Verification of preexisting research. Must use tools (WebSearch, WebFetch) to independently verify, fix. Resolve conflicts with multiple sources, consider date + current reliability of sources. 
	Step 4: Explore availability of alternate casters. Use docs/ardusimple/[entry] + local sources in local languages + culturally adjacent (example: Senegal = French survey forums). Press releases, master theses, survey communities. No global aggregators.
	Step 5: Identify gaps: incomplete fields, incomplete information, incomplete sources, ambiguous claims, conflicting or unsubstantiated claims
	Step 6: Close gaps, with sources. Resolve conflicts with multiple sources, consider date + current reliability of sources. Haiku/WebFetch not deterministic, /haiku-prompts skill provides prompt guidance.
	Step 7: Update `docs/ntrip_research/[entry]`. No need to keep style. No explicit or implicit changelog. Full refactor in scope. Exception: Iff existing claim in scope and could be neither verified nor rejected, don't vandalize claim.
 
Step 8: Self review:
- All claims in edited files verified by you? Fix, unless SkipVerify
- All fields sourced? If not, fix.
- Fields populated iff information is known? If not, fix.
- Invented fields? If yes move to prose.
- Details for casters owned by other files? If yes, replace with reference.
- Excessive detail for casters that are disqualified? If yes, trim.

Step 9: Skill review
Did any inaccurate, misleading or incomplete part of this instruction set lead you down a wrong path that made you waste 20+% of tokens spent in your run? If yes append to freeform output.

Step 10: 
stdout, per [entry]:

FileName
changes: MAJOR | MINOR
delta: <1-3 lines>
unresolved: <skip if empty, ≤100 words>

---

## Tools

Frontmatter `tools` lists surface. diverging path format ∨ security critical (aggressive check) are auto-denied, doesn't mean tool is blocked. WebFetch + WebSearch primary tools. curl --http0.9 

## Ingested globals

Access `rtk2go`, `centipede`, `earthscope`, `euref_ip`, `igs_ip`  from local data only — unless those are the networks you are investigating. ex: france, hungary (each 100++ stations)

py scripts/stations_by_radius.py <lat> <lon> <km>   # use first; reveals country tags per source
py scripts/stations_by_country.py <code>            # bare = list codes

Don't use for `num_stations` — sanity check only, mountpoints correlates but doesn't map to stations. AUSCORS and MIRAI rebroadcast select international stations, rarely primary outside Australia, Japan. 



