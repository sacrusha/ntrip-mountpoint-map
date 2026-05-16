---
name: translate
description: >
  Migrate prose to a target style via round-trip workflow. Tmp file first,
  replace on success, original preserved as original.orig
---

Translate & replace prose to target style/language with semantic round-trip check. 

## Steps

1. **translate**: target-style draft -> `.tmp/<basename>.tmp` (original unchanged).
2. **reverse-review**: read tmp; verify original is a faithful translation of tmp (flip direction). List deltas -- info original adds tmp doesn't imply, or info tmp adds original lacks.
3. **resolve**: change tmp, or edit original if Resolution allows. Edit both until reverse-review clean.
4. **final**: forward review original -> tmp & fix. 
5. **replace**: If all passed, rename original to original.orig, remame tmp to original.

## Resolution

Default: ask caller per delta.
Alternate: caller may pass policy in advance, e.g. "prefer terser", "drop X-related details", "keep tech terms verbatim", "abort on delta > N words". Apply policy first; ask caller only for cases policy doesn't cover.

## Auto-Clarity

Abort + escalate when:
- target style underspecified (e.g. caveman level not given)
- Resolution fails on safety-relevant content (ex: warnings, citation rules, deny-lists, license terms)
- deltas exceed reasonable resolution budget w/o caller policy

## Boundaries

- Do not edit original except after Resolution.
- Preserve verbatim: names, technical terms, code blocks, error strings, URLs, identifiers, file paths, citations, dates, formulas, numeric values.
