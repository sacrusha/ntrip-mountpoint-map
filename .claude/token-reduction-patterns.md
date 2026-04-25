# Token reduction patterns for AI-only markdown

Audience: LLM only. No humans read these files. Goal: cut tokens without losing facts.

Target: 40-60% reduction with zero fact loss. Anything past ~50% on technical files
starts dropping derivations and intermediate calculations — preserve formulas + results,
drop derivations only when both formula and result remain.

## Caveman prose

- Drop articles: the, a, an.
- Drop copulas/auxiliaries: is, are, was, will be, has been.
- Drop pronouns/subjects when implied: "It returns X" -> "returns X".
- Drop hedging/politeness: please, note that, it is worth mentioning, as you can see, in order to.
- Drop filler adverbs: actually, basically, essentially, simply, just, really, very, quite.
- Imperative + telegraphic: "After the script finishes, the workflow commits" -> "script done -> workflow commits".
- Numbers as digits: "twenty stations" -> "20 stations".
- Common words over rare: utilize -> use, approximately -> ~, therefore -> ->.

## Symbols replace words (in prose)

- `->` for flow, causation, "then", "becomes", "if-then".
- `=` for "means", "equals", "is".
- `!=` / `≠` for "not", "differs from".
- `&` and, `|` or, `+` with/plus, `~` approximately, `@` at/location, `#` count.
- `>=` / `<=` for thresholds.
- Chains: "fetch -> parse -> filter -> write" beats "first fetch, then parse, then filter, then write".

## Structural compression

- Dense bullets over prose paragraphs (skip transition words).
- Tables/TSV for repeated key:value across many records.
- Flat sections with prefix tags `[ingest]`, `[render]` instead of deep heading trees.
- One blank line max between blocks. Never `\n\n\n`.
- No `---` horizontal rules. No ASCII art. No trailing whitespace.

## Markdown pruning

- Drop `**bold**` and `*italic*` unless meaning depends on emphasis.
- Drop link-text duplication: `[foo](foo)` -> bare URL.
- Backticks only on real identifiers, not common words.
- Headings as tags, not titles: `## Pipeline` not `## How the ingestion pipeline processes data`.
- **Keep section-number prefixes** (`### 5.4 Foo`). Cross-references like `§5.4` depend on them.
- No inline HTML (`<br>`, `<details>`).

## Lexical compression

- Declare abbreviations once at top, reuse mechanically. Example: `MP=mountpoint, ST=sourcetable`.
- Domain acronyms uppercased, never re-expanded after first use: VRS, NRTK, NTRIP.
- Drop unit restatement when section establishes them.
- Consistent casing for the same term (NTRIP vs Ntrip vs ntrip = wasted tokens).

## Redundancy removal

- State each fact once. Cross-reference by id, don't restate.
- No recap/summary sections that repeat the body.
- One example per pattern, not three.
- Cut "obvious" qualifiers: "The Python script written in Python" -> "fetch_stations.py".
- Cut motivational/context paragraphs unless they encode a decision.

## Tokenizer micro-tricks (PROSE ONLY)

- ASCII over Unicode in prose: `--` not `—`, `"` not `"`, `...` not `…`, regular space not nbsp.
- Avoid CamelCase/snake_case when a natural word works (`getUserName` >1 token, `username` = 1).
- Drop thousand-separators: `5,472` -> `5472`. Drop decorative `~` when number is exact.
- ISO dates: `2026-04-22` not `April 22, 2026`.

**These rules apply in prose only.** See "Constraints" for what stays verbatim.

## Format escape hatch

When content is purely structured records, leave markdown:
- JSONL, TSV, or `id|field1|field2` per line beats markdown tables.
- Markdown table separators (`|---|---|`) are pure overhead.

## Constraints — do NOT touch

### Verbatim in ANY context (prose, code, tables)

- Identifiers, file paths, URLs, error strings.
- Spec field names: `<StationName>`, `<MonumentCode>`, RINEX/ANTEX/RTCM/NMEA fields. Do NOT abbreviate (`<StaName>` is wrong).
- Sample protocol strings: NMEA sentences (`$GPGGA,123519,...,0.9,545.4,M,...`), RTCM message lists, JSON examples, log lines, shell command snippets. Byte-identical — do not "fix spacing" or drop commas while reflowing.
- Numbers carrying precision (coordinates, frequencies, port numbers, version strings).
- Section-number anchors (§5.4, §3.2). Cross-references depend on them.
- Provenance markers (`✓` = confirmed, `~` = inferred). Per-claim, not stylistic.

### Inside fenced code blocks (` ``` `)

**Byte-identical to original. No exceptions.** Recurring bugs:

| Bug | Wrong | Right |
|---|---|---|
| × → x | `Nsats x Nsigs`, `40.3x10¹⁶`, `nx0.5625` | `Nsats × Nsigs`, `40.3×10¹⁶`, `n×0.5625` |
| − (U+2212) → - | `DD_phase = (φ_a - φ_b)` | `DD_phase = (φ_a − φ_b)` |
| – (en-dash) → - | `(1071-1077, 1081-1087)` | `(1071–1077, 1081–1087)` |
| … → ... | `n = -7...+6` | `n = −7…+6` |

The "ASCII over Unicode" rule from "Tokenizer micro-tricks" is for PROSE. Code blocks are exempt.

### Math operators in prose

Treat `×`, `÷`, `±` as identifiers, not stylistic Unicode.

- `HDOP × σ_UERE` is a formula — `×` stays.
- `2× better`, `~1.5–2× horizontal`, `5°×5° grid`, `3× GSD`: `×` is meaningful.
- `latency × velocity (10 m/s × 500 ms)`: math notation.
- `±10 mm`: precision notation.

If swapping `×` to `x` would create the ambiguity of "is x a variable or multiplication?", leave `×`.

### Markdown tables

- Each data row has exactly N pipes (N = column count + 1).
- To "compact" a row, keep all N-1 cells; use `—` (or `-`) for empty cells.
- To drop content, drop the entire row.
- **Never concatenate two rows** by removing trailing/leading pipes — produces a single corrupted row that renders unreadable. Real bug: `| MSM3 | compact | compact | — | — | |` + `| MSM4 | full | full | — | half-cycle | … |` collapsed into `| MSM3 | compact | compact | MSM4 | full | full | - | half-cycle | … |`.

## Verification pass (run after bulk reduction)

```sh
# Original on disk:
git show HEAD:path/to/file.md > /tmp/orig.md
cp path/to/file.md /tmp/curr.md

# 1. Table row pipe counts — adjacent rows in the same table must match.
awk '/^\|/{n=gsub(/\|/,"|"); print NR"\t"n"\t"$0}' /tmp/curr.md \
  | awk -v p=0 -v pn="" '$2!=p && p>0 {print "MISMATCH "NR-1" -> "NR; print pn; print $0} {p=$2; pn=$0}'

# 2. Math identifier preservation — × ÷ ± − count should drop only from sentence merges.
for s in '×' '÷' '±' '−'; do
  printf '%s: orig=%d curr=%d\n' "$s" \
    "$(grep -c "$s" /tmp/orig.md)" "$(grep -c "$s" /tmp/curr.md)"
done

# 3. Code block byte-diff — must be identical.
awk '/^```/{f=!f; next} f' /tmp/orig.md > /tmp/orig.code
awk '/^```/{f=!f; next} f' /tmp/curr.md > /tmp/curr.code
diff /tmp/orig.code /tmp/curr.code   # any diff in formulas/identifiers = bug

# 4. x-as-multiply leaks (× silently swapped to x).
grep -nE '[0-9]+\s*x\s*[0-9]|[A-Za-z]+\s*x\s*[A-Za-z]+\s*(=|bits|m/s)' /tmp/curr.md

# 5. Spec field-name abbreviations.
grep -nE '<Sta[A-Z]|<Mon[A-Z]|<dur>|<int>|<sys>' /tmp/curr.md   # should be empty

# 6. Sample-string corruption (NMEA, JSON, etc).
grep -nE '\$GPGGA' /tmp/curr.md   # spot-check field counts
```

After reducing a 50k-token file, expect 3-6 findings on first pass — most fall into the
recurring-bug table above. Re-run the verification after each fix round.

## Process notes

- Reduce in passes, not all at once: extract pure-prose section -> compress -> verify -> next.
- Run reducer on a single section first as calibration before batching the rest.
- Skeleton-first writes for large files (Write call timeout: ~300 s thinking before stream starts).
- Reviewer agents in parallel are useful but watch for 5-hour token limits — sequential is safer for long files.
- Don't strip provenance markers (`✓` `~`) for token gains: they encode confidence per claim and the legend can't recover which claim was confirmed.
- Don't strip section-number prefixes for token gains: `§5.4` cross-references depend on them.

## Example

Before (~38 tokens):
> Note that the parser will drop any mountpoint where the NMEA field is set to 1, because this indicates that the caster requires the rover to send its position.

After (~16 tokens):
> parser drops MP if nmea=1 (caster needs rover pos -> VRS)

~55% reduction, no information loss for an LLM.

## Lint candidates

Search-and-cut: ` the `, ` is `, ` are `, `\n\n\n`, `**`, "in order to", "note that", "it is worth", "as mentioned", "please note".

Search-and-flag (likely bugs introduced by overzealous reduction):
- ` x ` between digits — likely `× → x` corruption.
- `<Sta[A-Z]`, `<Mon[A-Z]`, `<dur>`, `<int>`, `<sys>` — abbreviated spec field names.
- Adjacent table rows with mismatched pipe counts.
- Code-block diff against original showing any change.
