# rtk_inventory.md — process

Per-file rules for `docs/rtk_inventory.md`. Pipeline context:
`pipeline.md` (same dir).

**Refactoring is in scope; consider the entire entry on every edit.** See
`pipeline.md` §"Edit discipline".

No bare email addresses. **Harassment guard.**

## Role

Internal refined operator catalogue. Per-network blocks (status,
host:port, yearly_cost, …). Developer-facing.

## File facts

- ~3000 lines. Grep + targeted Read.
- One block per network with `## id`, fields, free-form notes.
- Optional `**date_added**:` per block when revised independently.

## Curation threshold

A block exists iff the operator is relevant to target users (target-user.md).
A free 5 station RINEX only network is relevant if there is nothing else, but irrelevant if there is also a 50 station free VRS network. To be relevant a network must represent a pareto point on cost/capability/official-ness. Small surveying companies → country prose only.

## Status discipline

The `status:` field drives the marker sweep — be strict.

`free`: Free NTRIP/RTK service.
`paid`: Civilian-accessible for a fee. Requires `**yearly_cost**:`.
`restricted`: Exists but unobtainable for the target user at any price.
`RINEX`: Free RINEX post processing
`other`: Use for user-relevant entries that don't fit. Freeform note is load-bearing part of the block. If a user (target-users.md) landing on the country would be helped by knowing this exists or a network doesn't work the way the other fields suggest, it's `other`. Past examples: announced-not-live, sparse infra, reseller-only, non-standard NTRIP, GNSS-spoofed airspace, civil war.

deferred, rejected, etc are hallucinated statuses that do not exist.

## Format:

Each field is one line. Caveats, alternative URLs, probe notes, multi-tier prices, future-tense → prose.

---

## auscors — AUSCORS (AU)

status:	free | paid | restricted | RINEX | other 
country:	AU — Australia
operator:	Name of the operator/agency
landing_url:	Network landing page (required, every network). Operator-owned where available; most-official source otherwise.
access_url:	URL describing how to register/gain access. Skip if not more useful than landing_url:. Not a bare signup form.
host:port:	`host:port` - freeform if partially known, otherwise skip. prefer url over ip.
vrs:	yes | no | unknown - Use only for RTK networks. "yes" covers any NRTK product, not just mountpoints literally named "VRS".
access:    free / registration / paid [brief terms] / government-internal
stations:  N (approximate), skip if unknown, freeform if complicated
yearly_cost:	Only on paid | restricted networks. Single short line, primary annual tier: `€120/yr (~$130/yr)`. If no annual plan, most practical sustained-use plan (`€12/mo (~$13/mo)`).
yearly_cost_normalized:	Only on paid networks. ~ annual cost in USD. One time fees get amortized over 3 years.
If only pay per use, assume 3000 minutes, or random 50 days of use over year.
last_researched_date: 2026-04-30
`investigate`:	conflicts that research must authoritatively resolve, but hasn't yet. "no network exists" is not a conflict.

<prose>

---