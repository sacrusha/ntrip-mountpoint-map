# Handoff: Contextual Help System

This package replaces the current **two-guide** help architecture in `ntrip-mountpoint-map` (the first-visit `#how-dialog` modal + the long-form `#guide-dialog` that fetches `guide.html`) with a single **just-in-time help system** that answers the question the user is actually asking, where they're asking it.

> **Note for implementer:** this design was prototyped against a slightly earlier snapshot of the repo. Before you start, scan `index.html` for the symbols listed in §"What this replaces" to confirm they still exist with those names. If they've been renamed/refactored, apply the same logical changes to their replacements.

---

## About the design files

Everything in `reference/` is an **HTML design reference**, not production code to paste in. Two files:

- `reference/help-system.html` — live interactive prototype of the proposed system. Click through the demo list on the right side to see each interaction.
- `reference/evaluation.html` — the design evaluation that led to this work; useful background but not required reading.

The implementation target is the **existing `index.html`** — this codebase is a deliberately single-file, no-build, vanilla-JS + Leaflet project (see `CLAUDE.md` at repo root). Do **not** introduce a framework, bundler, or new runtime dependencies. Reuse the existing CSS-variable theme tokens, the existing `<dialog>` pattern being retired, and the existing popup structure in `buildPopup()` / `serverBlock()`.

## Fidelity

**High-fidelity for behaviour and content. Medium-fidelity for visual styling.**

- **Behaviour, IA, and copy** — ship as shown in the prototype. The 13 topics, chip copy, popover copy, search behaviour, keyboard shortcuts, and grouping are all final.
- **Visual styling** — the prototype uses IBM Plex (Sans/Serif/Mono) and a slightly refined dark palette; the real site uses system-sans and a different dark palette via CSS variables. **Adopt the existing site's type stack and `:root` CSS variables** (see `--panel-bg`, `--fg`, `--muted`, `--link`, `--accent`, `--warn`, `--code-bg`, `--srv-border`, `--btn-bg`, etc. — all defined at the top of `index.html`). Don't load Plex, don't change the existing palette. The prototype's layout, spacing, component sizes, and interaction states should transfer 1:1; only the type and colour values differ.

## What this replaces

Four pieces of the current UI are retired. All are in `index.html`:

| Remove | Current location |
|---|---|
| First-visit "Getting centimetre-accurate GPS" modal | `<dialog id="how-dialog">` markup; `setupBanner()` function which auto-opens it gated on `localStorage['ntrip-howit-seen']`; the `.how-cta` link inside that points into the guide |
| Full long-form guide modal | `<dialog id="guide-dialog">` markup; the module-scope `openGuideDialog()` function; the inline anon IIFE at end of file that wires its close button |
| Banner "Guide" button | `<button id="banner-guide-btn">Guide</button>` inside `#banner`; its `onclick=openGuideDialog` wiring inside `setupBanner()` |
| Popup footer "Receiver setup guide →" link | The trailing `<p class="guide-link">…openGuideDialog();…</p>` inside `buildPopup()`'s returned HTML |

`setupBanner()` itself is **not** entirely removed — it also manages `document.body.classList.add('banner-visible')` and wires the `#banner-near-btn`, both of which stay. Rename the function if useful, or just strip the `#how-dialog` / `#guide-btn` wiring from inside it.

The `guide.html` file itself is **kept** as a plain static page at `/guide.html` — it's publicly linkable and the long-form primer remains useful for anyone who arrives there directly. The map UI no longer fetches it into a modal.

---

## What this adds

Three surfaces, built into `index.html`:

### 1. Banner Help button

Replace `#banner-guide-btn` ("Guide") with a `?` Help button that opens the new drawer. Same slot in `#banner`, same styling family (`border:1px solid #3d5a73; color:#9ec8ff;` — reuse the existing `#banner-guide-btn` CSS, just change the ID and label).

```html
<button id="banner-help-btn" aria-label="Help"><span class="q">?</span> Help</button>
```

Keyboard shortcut: `/` (when no input is focused) opens the drawer.

### 2. Inline help chips in the station popup

Small `?` affordances rendered in `buildPopup()` / `serverBlock()` next to two specific terms. They must not break the existing `.popup-plain` layout.

- **Carrier chip** — next to the `.acc` line rendered by `accuracySummary()`. The chip fires popover key `carrier`.
- **Mountpoint chip** — next to the "Mountpoint" label rendered by `cpRow('Mountpoint', mountpoint)` in `serverBlock()`. The chip fires popover key `mountpoint`.

Both popovers contain a 2-sentence explanation + a "Learn more →" link that deep-links into the Help drawer (see §3).

### 3. Help drawer

A right-side slide-in panel (width 420px on desktop, full-width on mobile at the existing `max-width:600px` breakpoint) containing:

- A search field at the top.
- 13 topics, grouped by category, each with a one-line question + a collapsible answer.
- Cross-link chips at the bottom of each answer ("→ related question").
- A `<details>` "Deep dive" disclosure inside answers that need the long-form detail.

### 4. First-run toast

Bottom-right corner toast, shown instead of the auto-opening `#how-dialog` on first visit:

> **New here?**
> One-minute orientation: what this map shows, how to use a station.
> [Take the tour →] [I know RTK]

"Take the tour" opens the drawer scrolled to the `whats-this-map` topic. "I know RTK" dismisses. First-visit-only, gated by the **same `localStorage['ntrip-howit-seen']` key already in use** — don't introduce a new key; users who've already dismissed the old modal should not see the new toast.

---

## Files to add

```
data/help_topics.json          — the 13-topic content model (this handoff includes it, ready to ship)
```

That's it. Everything else edits `index.html`.

---

## Implementation guide

### Add the topics data

Copy `help_topics.json` from this handoff into `data/` at the repo root. `index.html` will `fetch('./data/help_topics.json', {cache:'no-cache'})` on load — use the same `fetchWithTimeout` helper already defined, and add it to the existing `Promise.allSettled([...])` block that loads `stations.json`, `source_health.json`, and `country_markers.json`. A failed fetch should degrade gracefully (drawer still opens, shows "help content unavailable" message) — don't block map render on it.

Schema:

```js
{
  "categories": ["Getting started", "Before you start", "Connect", ...],
  "popovers": {
    "carrier":    { "title": "...", "body": "...", "deepKey": "carrier-l1l2" },
    "mountpoint": { "title": "...", "body": "...", "deepKey": "mountpoint" }
  },
  "topics": {
    "whats-this-map": {
      "cat": "Getting started",
      "icon": "▦",
      "q": "What am I looking at?",
      "sub": "In 30 seconds",
      "lead": "First paragraph — answers the question directly.",
      "body": "<p>Additional HTML. Assume this is trusted content (we author it).</p>",
      "deep": "Optional long-form string shown under <details>.",
      "related": ["is-my-gear-compatible", "how-to-connect-emlid"]
    }
  }
}
```

13 topics ship in this handoff. Add more by editing the JSON only.

### Remove the old guides

In `index.html`:

1. Delete the `<dialog id="how-dialog">…</dialog>` and `<dialog id="guide-dialog">…</dialog>` elements from the body.
2. Delete the module-scope `openGuideDialog()` function (bottom of file) and its close-button-wiring IIFE immediately below it.
3. Inside `setupBanner()`, delete the `guideBtn.onclick`, `#how-dialog-close` wiring, the `dlg.addEventListener('click',…)` backdrop-close handler, and the `localStorage['ntrip-howit-seen']` auto-open block. Keep the `document.body.classList.add('banner-visible')` line.
4. In `buildPopup()`, delete the trailing `<p class="guide-link">…</p>` from the returned HTML. Replace with the popup footer in §"Popup changes" below.
5. Delete CSS rules scoped to `#how-dialog`, `#guide-dialog`, `.how-cta`, `.guide-link` (but keep variables like `--cta-bg` / `--cta-border` if they're reused elsewhere — grep first).
6. In the banner HTML, rename `#banner-guide-btn` to `#banner-help-btn` and change its label from "Guide" to `<span class="q">?</span> Help`. Keep the existing CSS rule, just duplicate the selector for the new ID or rename.

### Add the new UI

Markup (inside `<body>`, after `#shell` is fine):

```html
<!-- first-run toast, hidden by default; JS shows it only if !localStorage['ntrip-howit-seen'] -->
<div class="toast" id="toast" hidden>…</div>

<!-- help drawer -->
<div class="scrim" id="scrim"></div>
<aside class="drawer" id="help-drawer" aria-label="Help">
  <div class="dh"><h3>Help</h3><button class="x" id="help-close">✕</button></div>
  <div class="dsearch">
    <input type="text" id="help-search" placeholder="Ask a question — e.g. 'Emlid', 'base station', 'VRS'" />
  </div>
  <div class="dbody" id="help-body"></div>
</aside>

<!-- popover host — one singleton div, reused -->
<div id="popover-layer"></div>
```

**Z-index note:** the drawer sits above the map but below Leaflet's popup system. The existing site uses z-index 10000 on `#banner`; use 10001 for `#scrim` and 10002 for `#help-drawer`. Popovers anchored to popup chips use 10003.

The full CSS + JS for these components is in `reference/help-system.html`. Port them with the following token substitutions:

| Prototype value | Ship value |
|---|---|
| `font-family:'IBM Plex Sans',…` | Remove — inherit the existing `system-ui,-apple-system,'Segoe UI',Roboto,…` stack on `<body>` |
| `font-family:'IBM Plex Serif',…` | Replace with the existing serif use (`Georgia,ui-serif,serif`) — that's what `#banner-brand` uses |
| `font-family:'IBM Plex Mono',…` | Replace with `ui-monospace,Menlo,monospace` (the stack `.popup-plain code` already uses) |
| `background:#1e3048` hardcoded | `var(--panel-bg)` |
| `#e8eef4` foreground | `var(--fg)` |
| `#94a7b8` muted | `var(--muted)` |
| `#9ec8ff` link | `var(--link)` |
| `#4caf77` accent | `var(--accent)` |
| `#d4a030` warn | `var(--warn)` |
| `#0d1922` code bg | `var(--code-bg)` |
| `#2d4256` border | `var(--code-border)` / `var(--panel-border)` / `var(--srv-border)` (pick by context) |

Both light and dark themes must work. The existing `:root{…}` + `@media(prefers-color-scheme:dark)` pattern covers this — just use the variables consistently and the drawer will theme correctly in both.

### Popover positioning

Popovers are positioned relative to the chip that opened them:

- `arrow:"top-left"` (default) — popover below chip, arrow at top-left.
- `arrow:"left"` — popover right of chip, arrow at left.

Clamp `left` so the popover never overflows the viewport. **Watch out for Leaflet's popup DOM**: chips live inside `.leaflet-popup-content`, which has its own stacking context and auto-scrolls when content is tall. Append the popover to `document.body` (not to the popup), positioned in viewport coords with `position: fixed`, so it escapes the popup's overflow clip. Close any open popover on map pan/zoom (listen for `map.on('movestart', hidePopover)`).

Reference impl: `showPopover()` in `reference/help-system.html`. The only change: in the live site, use `position: fixed` + viewport coords instead of the prototype's `position: absolute` inside a fixed stage.

### Popup footer change

Today `buildPopup()` ends with:

```html
<p class="guide-link"><a href="./guide.html" onclick="event.preventDefault();openGuideDialog();">Receiver setup guide →</a></p>
```

Replace with:

```html
<div class="popup-actions">
  <button class="b-primary" onclick="__ntripCopyAll(this, '<escaped payload>')">Copy all</button>
  <button class="b-secondary" onclick="__ntripOpenHelp('how-to-connect-emlid')">How to connect ↗</button>
</div>
```

- **"Copy all"** — new helper `window.__ntripCopyAll(btn, text)` alongside the existing `__ntripCopy`. Joins server/port/mountpoint/user/pass (one line per field, `key: value`) into the clipboard. Same "✓" confirmation animation as `__ntripCopy`. Multi-source popups: emit one block per source with a blank line between.
- **"How to connect ↗"** — new helper `window.__ntripOpenHelp(topicId)` opens the drawer scrolled to the given topic.

Style `.b-primary` / `.b-secondary` off the existing `.popup-plain button.cp` pattern — same border / padding / font-size, just full-width-within-popup.

### Keyboard

- `/` opens the drawer (unless focus is in an input or textarea).
- `Esc` closes any open popover first; if none open, closes the drawer.
- `↑ / ↓` inside the drawer moves topic focus (optional, stretch goal).

### Mobile

At `max-width:600px` (the existing breakpoint), the drawer fills the viewport width. The banner Help button stays text+icon on mobile; the "Near me" button can collapse to icon-only via `.btn-label{display:none;}` under the same media query if space is tight.

---

## Acceptance criteria

Ship when:

- [ ] `<dialog id="how-dialog">` and `<dialog id="guide-dialog">` and their CSS blocks are removed from `index.html`.
- [ ] `openGuideDialog()` and its wiring IIFE are removed.
- [ ] `#banner-guide-btn` is renamed to `#banner-help-btn` and its click handler opens the new drawer, not the old guide modal.
- [ ] First visit shows the toast (not the old `#how-dialog`). "Take the tour" opens the drawer on `whats-this-map`. Dismissing sets `localStorage['ntrip-howit-seen']='1'`. Second visit shows neither.
- [ ] `/` keyboard shortcut opens the drawer.
- [ ] Drawer fetches `./data/help_topics.json` and renders all 13 topics grouped by category, in the order specified in `categories`.
- [ ] Drawer search filters topics as the user types (matches across `q`, `sub`, `lead`, `body`, `deep`).
- [ ] Clicking a topic expands it inline; "Deep dive" `<details>` inside expands further.
- [ ] Related-topic chips in each answer jump to the related topic (collapse current, expand target, scroll into view).
- [ ] Station popup renders `?` chips next to the accuracy line and next to the Mountpoint field. Clicking either opens a popover with "Learn more →" that opens the drawer at the right deep-link target.
- [ ] Popovers anchored to popup chips escape the popup's overflow clip and close on map pan/zoom.
- [ ] Popup footer has "Copy all" (copies full connection payload) and "How to connect ↗" (opens drawer at `how-to-connect-emlid`) in place of the `guide-link` row.
- [ ] Both light and dark themes render correctly.
- [ ] No new runtime dependencies added (no React, no build step, no font loads beyond what's already in the site).
- [ ] `guide.html` is still reachable as a plain page at `/guide.html` — don't delete it.
- [ ] `Esc` closes popover + drawer. Scrim click closes drawer.

---

## Open questions for the implementer

1. **Keep `guide.html` as a static page?** Recommended: yes. It's useful for deep-linking from forums / social, is SEO-indexable, and costs nothing to leave in place. The in-map UI no longer links into it from any surface, which is the important change.
2. **URL-hash state for deep links.** Nice-to-have: `#help=how-to-connect-emlid` opens the drawer scrolled to that topic on page load. Useful for forum posts. Not in the acceptance criteria above; call it if you want it.
3. **Help chip density in popups.** I've specified two chips (carrier, mountpoint). The popup already contains other jargon ("Legacy RTCM 2.x", "openNote" strings). Start with two, measure whether users are still confused, add more chips later. Resist the urge to chip every technical term in the first pass — noise kills the signal.

---

## Design tokens (quick reference — all already in `index.html`)

| Concept | Use variable |
|---|---|
| Panel background | `--panel-bg` |
| Panel border | `--panel-border` |
| Foreground text | `--fg` |
| Muted text | `--muted` |
| Link accent | `--link` |
| Primary accent (green) | `--accent` |
| Warn / attention | `--warn` |
| Code background | `--code-bg` |
| Code border | `--code-border` |
| Button background | `--btn-bg` |
| Button border | `--btn-border` |
| Button hover | `--btn-hover` |
| Section separator | `--srv-border` |

Spacing: use the existing site's padding conventions (`8px 12px` for panel interiors, `4px` between rows — see `#toggles.leaflet-control`).

Radii: 3–5 px, matching the site's existing `border-radius` values.

---

## Files in this handoff

```
design_handoff_help_system/
├── README.md                       — this file
├── help_topics.json                — 13-topic content model, drop in data/
└── reference/
    ├── help-system.html            — interactive prototype (demo list on right)
    └── evaluation.html             — design evaluation leading to this work
```
