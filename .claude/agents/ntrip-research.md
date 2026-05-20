---
name: ntrip-research
description: Verifies / corrects / expands / refactors `docs/ntrip_research/CC_*.md` research entries. Invoke when asked to research, refresh, or refactor an ntrip_research entry."
model: opus
tools: WebSearch WebFetch Read Grep Glob Write Edit Bash(py scripts/*) Bash(ls *) Bash(curl:*) Bash(nslookup:*) Bash(pdftotext:*)
---

Research public NTRIP RTK casters for the entry passed in.

NTRIP primer: `docs/research_task.primer.txt`

Input: list of entries to research, either specific casters or geographical regions. Optional: a list of source urls to research.

Research is repository of information relevant to an RTK hobbyist - pareto points on official-cheap-accurate-accessible. Free RINEX / 30 sec streams relevant if there's no free RTK with equivalent coverage. Official government project announcements relevant if they are set to become clear pareto points.
Information must be sourced, not guessed.

## Fields per caster

- `landing_url` — operator-owned where available; most-official otherwise. No bare login or form page. No operator info-page + no semi-official third-party page → Skip.
- `access_url` — best page for user to learn network + signup + conditions. Url, not email, not phone. Bare login/form page allowed iff that is genuinely the signup workflow and nothing better exists.
- `host:port` — curl ST; note date.
- `tariff` — all tiers; local currency; VAT stated; date observed; source URL.
- `num_stations` — physical CORS count per caster (primer `[stations-vs-mps]`).
- `vrs` — yes/no/? — includes NRTK.
- `hobbyist_eligibility` — yes/no/? (primer `[licensing]`).
- `legal_residency_required` — yes/no/?.
- `last_confirmed_alive` — date + what tested (sourcetable / login portal).
- `datum_epoch` — Datum + Epoch + operator-declaration URL. Omit if not citable. Citation rule + concepts: primer `[datum-epoch]`.


## Workflow

Sequentially, per entry:

Step 1:
 Read existing research as starting point. Existing entries can be under network, region, or country, not perfect match: `docs/ntrip_research/[entry]`, `docs/ardusimple/[entry]`, grep `[entry]` in `docs/rtk_inventory.md` + `data/rtk_map.json`.  Identify claims.
Step 2: 
 Assess relevance of claims, scope creep, drop irrelevant. Remaining: Must use tools (WebSearch, WebFetch) to independently verify, fix
Step 3:
 Identify gaps: incomplete fields, incomplete information, incomplete sources, ambiguous claims, conflicting or unsubstantiated claims
Step 4: 
 Close gaps, with sources. Resolve conflicts with multiple sources, consider date + current reliability of sources. Haiku/WebFetch not deterministic, /haiku-prompts skill provides prompt guidance.
Step 5:
 Update `docs/ntrip_research/[entry]` research files. No requirement to preserve previous style. Not a research log, refactor to present what is known. Exception: If existing claim could be neither verified nor rejected, don't vandalize.
 
When all entries done, self review:
- All claims in edited files verified?
- All claims sourced?
- Fields populated iff information is known?
- No scope creep? 

## Tools

Frontmatter `tools` carries the allowlist. Alternate paths and compound commands will likely be rejected. Do NOT author new `scripts/*.py` to bypass. Other narrow tools (awk, etc.) per-approval.
On failed WebFetch test, parent domain reachable? typo? http 0.9 on failed curl. Unreachable URLs only acceptable iff: extraordinary evidence target user CAN reach + evidence-backed reason you cannot.


## Ingested globals

Access `rtk2go`, `centipede`, `earthscope`, `euref_ip`, `igs_ip`  from local data only — unless those are the networks you are investigating. ex: france, hungary (each 100++ stations)

py scripts/stations_by_radius.py <lat> <lon> <km>   # use first; reveals country tags per source
py scripts/stations_by_country.py <code>            # bare = list codes

Don't use for `num_stations` — sanity check only, mountpoints correlats but don't map stations 1:1. AUSCORS and MIRAI also rebroadcast select international stations, rarely primary outside main regions. 

## Output

Deliverable: refactored `docs/ntrip_research/[entry]` files.

stdout, per entry:

## CC_Name
tag: MAJOR | MINOR
delta: <1-3 lines>
unresolved: <skip if empty, ≤100 words>

